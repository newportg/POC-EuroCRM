# EuroCRM POC — Phase 0 Execution Guide

Sequence of commands and manual steps to provision the Phase 0 environment (Azure SQL + Dataverse) and run the virtual-table relationship spike.

**Targets:** `main.bicep` (Azure SQL) · `deploy.ps1` (orchestrator + Dataverse) · `sql/spike-schema.sql` (spike data)
**Result:** Azure SQL `EuroCRMPOC`, Dataverse environment "EuroCRM POC", 5 virtual tables, a walked relationship chain, and a go/no-go decision recorded in `POC.md`.

---

## 0. Prerequisites (one-time)

| Tool | Install | Notes |
| ---- | ------- | ----- |
| PowerShell | Built into Windows | 5.1+ |
| Azure CLI | `winget install Microsoft.AzureCLI` | Or MSI from microsoft.com |
| Bicep | Bundled with Azure CLI | `az bicep install` if missing |
| Power Platform admin module | `Install-Module Microsoft.PowerApps.Administration.PowerShell -Scope CurrentUser` | Used by deploy.ps1 for the Dataverse environment |
| SQL tooling | SSMS or Azure Data Studio, or sqlcmd | For the spike schema |

**Open a NEW PowerShell window after installing** — PATH changes from installers are not visible in already-open sessions (this bit us during Bicep testing).

Verify the tools:

```powershell
az version
az bicep version
Get-Module -ListAvailable Microsoft.PowerApps.Administration.PowerShell
```

---

## 1. Automated provisioning

### 1a. One-shot orchestrator (recommended)

```powershell
cd "C:\Source\Obsidian\Projects\POC-EuroCRM\POC-EuroCRM-Vault\POC\infra"
.\deploy.ps1 -SqlAdminPassword '<STRONG_PASSWORD>'
```

**Sign-in account:** the script logs in as `gary.newport@devknightfrank.onmicrosoft.com` (override with `-LoginUsername`). The account has MFA, so expect **two interactive sign-ins**, both completed in the browser:

1. **Azure CLI** — `az login` prompt (falls back to device-code flow if the username prompt is rejected for MFA)
2. **Power Platform** — `Connect-PowerAppsAccount` sign-in dialog

The script verifies the signed-in Azure user matches the expected account and aborts with instructions if it doesn't.

The script walks through:

1. `az login` (interactive) and optionally `az account set`
2. `az group create` → `rg-eurocrm-poc` in `westeurope`
3. Bicep deploy → SQL server `eurpoc-sql`, database `EuroCRMPOC` (serverless, auto-pause 60 min), Azure-services firewall rule
4. Power Platform → Dataverse environment "EuroCRM POC" (Developer SKU, europe, EUR)
5. Prints outputs (SQL FQDN, connection template) and the remaining manual steps

Optional overrides:

```powershell
.\deploy.ps1 -SqlAdminPassword '<pwd>' `
  -SubscriptionId '<guid>' `
  -ResourceGroup 'rg-eurocrm-poc' `
  -Location 'westeurope' `
  -DataverseSku 'Developer' `
  -DataverseLocation 'europe'
```

### 1b. Manual alternative (same result, step by step)

```powershell
# Sign in and pick the subscription
az login
az account show

# Deploy the SQL side
az deployment group create `
  --resource-group rg-eurocrm-poc `
  --template-file main.bicep `
  --parameters main.parameters.json
```

Edit `main.parameters.json` first — `sqlAdminPassword` is a placeholder.

### 1c. Optional — allow your workstation through the SQL firewall

The connector (Azure) is covered by the `AllowAllWindowsAzureIps` rule. For direct SSMS/sqlcmd access from your machine:

```powershell
az sql server firewall-rule create `
  --resource-group rg-eurocrm-poc `
  --server eurpoc-sql `
  --name dev-laptop `
  --start-ip-address '<YOUR_IP>' `
  --end-ip-address '<YOUR_IP>'
```

Your public IP: `Invoke-RestMethod https://api.ipify.org`

---

## 2. Manual processes (maker portal)

### 2.1 Install the Virtual Connector Provider

1. Go to the AppSource listing: <https://appsource.microsoft.com/product/dynamics-365/mscrm.connector_provider>
2. **Get it now** → select the environment **EuroCRM POC**
3. Wait for the install to complete (async — check Solutions until the solution appears)
4. Verify: make.powerapps.com → **Solutions** → "Virtual Connector Provider" present

### 2.2 Create the SQL connection

1. make.powerapps.com → **Data → Connections** → **+ New connection** → **SQL Server**
2. Enter: server = the FQDN output from deploy (`eurpoc-sql.database.windows.net`), database = `EuroCRMPOC`
3. Authentication: SQL auth (sqladmin) **or** Entra ID (preferred — set `sqlEntraAdminObjectId` in the Bicep parameters first)
4. Save; the Entity Catalog step below can auto-generate the connection reference

### 2.3 Deploy the spike schema

```powershell
sqlcmd -S <FQDN> -U sqladmin -P '<pwd>' -d EuroCRMPOC `
  -i "POC\infra\sql\spike-schema.sql"
```

Or open the file in SSMS/Azure Data Studio and execute against `EuroCRMPOC`.

Verify the seeded chain with the query at the bottom of the file — expect one account, one contact, one deal, one lot, one property.

### 2.4 Create the virtual tables (Entity Catalog)

1. make.powerapps.com → **Data → Tables**
2. Open the **Entity Catalog for <connection>** row created by the connector
3. For each of `kf_account`, `kf_contact`, `kf_property`, `kf_deal`, `kf_dealproperty`:
   - **Edit** → set "Configure as virtual table" = **Yes**
   - Set the **primary key** to the GUID column (e.g. `kf_dealid`)
   - Set the **primary name** to the string column (e.g. `kf_name`)
4. Creation is asynchronous — if tables don't appear, check **Settings → System Jobs** (look for `ConnectorGenerateVEPlugin` system jobs)

### 2.5 Define the N:1 relationships

Virtual tables cannot be the "1" side of a 1:N — model lookups on the child:

| Child (N) | Parent (1) | External Name (= FK column) |
| --------- | ---------- | --------------------------- |
| `kf_contact` | `kf_account` | `kf_accountid` |
| `kf_deal` | `kf_account` (client org) | `kf_accountid` |
| `kf_deal` | `kf_account` (legal entity) | `kf_legalentityaccountid` |
| `kf_dealproperty` | `kf_deal` | `kf_dealid` |
| `kf_dealproperty` | `kf_property` | `kf_propertyid` |

Rules: External Name must match the SQL FK column exactly, must be unique per table, and PK/FK formatting must be identical.

### 2.6 Build the minimal spike app

1. make.powerapps.com → **Apps → + New app → Model-driven**
2. Name: "EuroCRM POC Spike"
3. Add a page for `kf_deal` (default form + one view: Deals by stage)
4. Add one **filtered view** — e.g. kf_contact where `kf_account` = a chosen account (this is the "Client 360" pattern replacing parent subgrids)

### 2.7 Validate and record the decision

1. Open the app, open the seeded deal, and confirm related data resolves through the lookups
2. Create a new contact from the form (tests CRUD through the connector)
3. Note behaviour of: choice/label display on enum columns, any business rules, subgrid vs filtered view
4. **Record the go/no-go decision and findings in `POC/POC.md`** (Phase 0 checkboxes)

---

## 3. Troubleshooting

| Symptom | Fix |
| ------- | --- |
| `az` / `bicep` not recognized | Open a new terminal — PATH refresh after install |
| "Resource not found for the segment `msdyn_get_required_fields`" | Update the Virtual Connector Provider solution: Solutions → History → check `ConnectorProvider`, re-import from AppSource |
| "Connection 'x' not found in current environment" | Version 1,029+ of Connector Provider; re-import from AppSource |
| Virtual table shows only 1 record / empty | Source table has no primary key — add GUID PK and recreate |
| Lookups don't resolve in views/subgrids | External Name ≠ FK column, or PK/FK formatting mismatch — check `ExternalName` per column |
| Only 1,000 rows returned from a relationship | Known cap — filter the query/views |
| Create/update fails on a SQL view | Views are read-only — use tables, not views, for the spike |
| Dataverse environment shows in admin center but not maker portal | Wait a few minutes for sync, then refresh |
| Data not retrievable after recreating a connection | Share the recreated connection with the Virtual Connector Provider app (Connection → Share) |

---

## 4. Expected outputs

| Resource | Name | Where used |
| -------- | ---- | ---------- |
| Resource group | `rg-eurocrm-poc` | All Azure resources |
| SQL server | `eurpoc-sql` | Connector connection, SSMS |
| SQL database | `EuroCRMPOC` | System of record — all `kf_*` tables |
| Dataverse environment | EuroCRM POC | Virtual tables, builds the app |
| Solutions (Dataverse) | `KF_Core_POC`, `KF_CapitalMarkets_POC` | Created in Phase A after go/no-go |

Related: `POC.md` (component list, task list, stack), `POC/infra/main.bicep` + `deploy.ps1` + `sql/spike-schema.sql`.