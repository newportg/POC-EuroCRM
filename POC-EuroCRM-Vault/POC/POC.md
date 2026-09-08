# EuroCRM POC — Component List

**Approach:** Model-Driven Power App on Dataverse with **SQL as the source of truth** (Option B)
**Database:** Single Azure SQL database — all domain data stored in SQL, exposed to the app via Dataverse virtual tables (Virtual Connector Provider)
**Decision (07/09/2026):** Option A (Dataverse-native tables) **rejected** — enterprise requires data stored in a SQL database
**Scope:** CRM Lite MVP (Phase 0) + Capital Markets (Phase 1)
**Source:** [[solution-overview]], [[data-model-overview]], [[architecture-key-components]]

---

## 1. SQL Schema (System of Record)

All tables below live in one Azure SQL database (`EuroCRMPOC`). Dataverse maps each as a virtual table over a single SQL connection.

**Schema rules (enforced from day one):**

- GUID primary key + one string primary-name field on every exposed table (required for CRUD via virtual tables)
- `int` / `nvarchar` only — **never expose** `bigint` (maps to decimal), `datetime2`, `time`, `geometry`, `geography`, `rowversion` (cannot map)
- `nvarchar` for external references (SIREN, KRS, UPRN, registration numbers)
- System-versioned temporal tables for audit (7-year retention)
- Read-optimised views for form display

### Client Tables

| Table | Type | Description |
| ----- | ---- | ----------- |
| `kf_account` | SQL custom | Organisation, brand, legal entity, fund, SPV. Models the OOB Account field set (`kf_accountid` GUID, `kf_name`, `kf_accounttype`, address elements, `kf_accountclassification`, `kf_entitytype`, `kf_registrationnumber`, `kf_industry`) |
| `kf_contact` | SQL custom | Individual linked to Account (`kf_contactid`, `kf_firstname`, `kf_lastname`, `kf_jobtitle`, `kf_emailaddress1`, `kf_telephone1`, `kf_accountid` FK, `kf_processingconsent`) |

**Design note:** the OOB Dataverse Account/Contact tables are not used — SQL carries the same field set. This drops OOB activities/notes/timeline features; acceptable for POC, revisit only if the enterprise requires them.

### Property Tables

| Table | Type | Description |
| ----- | ---- | ----------- |
| `kf_site` | SQL custom | Physical building or land parcel (canonical address) |
| `kf_property` | SQL custom | Commercial asset register |

**kf_Site key fields:** Country-neutral address elements (UPU S42a-6), `kf_addressfull`, `kf_uprn`, `kf_cadastralref`, `kf_loqateid`

**kf_Property key fields:** Identity, address, geocoded, sector, type, status, tenure, areas, floors, parking, asking price, ESG

### Capital Markets Tables (Phase 1)

| Table | Category | Description |
| ----- | -------- | ----------- |
| `kf_deal` | Core | Core deal record with 8-stage lifecycle (SQL state machine, not BPF) |
| `kf_dealproperty` | Junction | Links deal and property (allocation, ERV, occupancy) |
| `kf_pitch` | Origination | Competitive pitch tracking |
| `kf_nda` | Origination | NDA management |
| `kf_bid` | Bidding | Multi-round bid management |
| `kf_ddmilestone` | Due Diligence | DD milestone tracking |
| `kf_redflag` | Due Diligence | Risk and red flag tracking |
| `kf_kycrecord` | Compliance | KYC/AML compliance at legal entity level |
| `kf_investorprofile` | Investors | Investment preferences and strategy |
| `kf_dataroomaccess` | Compliance | Data room access management |
| `kf_feeschedule` | Commercials | Fee structure per deal |
| `kf_transactionreport` | Reporting | Auto-generated transaction reports |

### Supporting & Infrastructure Tables

| Table | Category | Description |
| ----- | -------- | ----------- |
| `kf_siccode` | Reference | SIC code reference table |
| `kf_energyrating` | Reference | Energy performance ratings |
| `kf_gdprrequest` | Compliance | GDPR data subject requests |
| `kf_auditexport` | Compliance | Audit trail export (fed by temporal tables) |
| `kf_stagegaterule` | Config | Stage transition rules for the deal lifecycle |
| `kf_stagehistory` | Infra | Stage transition history (written by SQL trigger) |
| `kf_integrationlog` | Infra | Integration transaction logging |

### WIP / Finance Tables

| Table | Description |
| ----- | ----------- |
| `kf_wip` | Work in progress tracking (deal to fee earned) |

**kf_WIP key fields:** `kf_wipid`, `kf_parenttype`, `kf_instructionid`, `kf_netfeetogroup`, `kf_officeretained`, `kf_probability`, `kf_grossfee`, `kf_reportingmonth`, `kf_wipstatus`, `kf_invoicenumber`

---

## 2. Model-Driven Power App

### Entity Forms

| Entity | Form Type | Notes |
| ------ | --------- | ----- |
| kf_Account | Main + Quick Create | Brand/Group vs Legal Entity classification |
| kf_Contact | Main + Quick Create | Linked to Account via N:1 lookup |
| kf_Site | Main | Country-neutral address |
| kf_Property | Main | Commercial asset register |
| kf_Deal | Main | Stage header + stage-gate fields (no BPF) |
| kf_DealProperty | Quick Create | N:1 lookups to Deal and Property |
| kf_Pitch | Main | Pitch tracking |
| kf_NDA | Main | NDA with counterparty + signatory |
| kf_Bid | Main | Multi-round bid with investor profile link |
| kf_InvestorProfile | Main | Strategy per Brand/Group |

### Deal Stage Lifecycle (replaces BPF)

Enforced by a SQL transition trigger; history recorded in `kf_stagehistory`; rules in `kf_stagegaterule`.

| Stage | Name | Gate | % Complete |
| ----- | ---- | ---- | ---------- |
| S1 | Origination | — | 5% |
| S2 | Pitch & Mandate | Conflict check | 15% |
| S3 | Instruction | Multi-jurisdiction KYC | 25% |
| S4 | Marketing | — | 35% |
| S5 | Bidding | — | 50% |
| S6 | Exclusivity | — | 65% |
| S7 | Due Diligence | Country-specific regulatory gates | 85% |
| S8 | Completion | Notarial deed / billing | 100% |

### Views & Dashboards

| View / Dashboard | Purpose |
| ---------------- | ------- |
| Active Deals Pipeline | Deal pipeline by stage, country, service line |
| Client 360 | Contacts, deals, properties filtered by account (N:1 lookups — no parent subgrids) |
| WIP Report | Revenue at risk by deal stage |
| Investor Registry | Investor profiles by strategy/geography |
| KYC Status | Compliance status across legal entities |

### Security Model

| Component | Purpose |
| --------- | ------- |
| SQL Row-Level Security | Row filtering (country, BU) — the shared connector credential means RLS is authoritative |
| Dataverse Roles | App-level only (Broker, Manager, Admin) — do not filter rows |
| Business Unit | Single BU for POC |

---

## 3. Solution Package Structure (POC)

| Solution | Layer | Contents |
| -------- | ----- | -------- |
| `KF_Core_POC` | L2 | Virtual table definitions, N:1 relationships, base app security |
| `KF_CapitalMarkets_POC` | L5 | CM entities, stage-lifecycle views, deal forms |

**Notes:**

- L3/L4/L6/L7 collapsed — country/region logic baked into SQL views + RLS
- The SQL schema itself is **not** a Dataverse solution — managed by T-SQL scripts / dacpac, deployed to Azure SQL
- One Dataverse connection reference shared by all virtual tables

---

## 4. Summary: What to Build

### SQL (Azure SQL, system of record)

- **1 database** (`EuroCRMPOC`), **24 tables** — GUID PKs, `int`/`nvarchar` only
- **Deal stage state machine**: `kf_deal.stage` + transition trigger + `kf_stagehistory` + `kf_stagegaterule`
- **Temporal tables** for audit, unique indexes + fuzzy-match dedup proc
- **Read-optimised views** for form display

### Dataverse

- **24 virtual tables** via Virtual Connector Provider (one SQL connection)
- **N:1 relationships** on child tables (no parent subgrids — virtual tables cannot be the 1 side of a 1:N)
- **No Dataverse BPF** — lifecycle lives in SQL

### Power App

- **10+ entity forms** (main, quick create)
- **5+ views** (pipeline, client 360, WIP, investors, KYC)
- **Security**: SQL RLS + 3 app roles
- **No dashboards** in first iteration

### Integrations (Deferred)

- Outlook email sync (Power Automate)
- SharePoint deal folder provisioning (Power Automate)
- Loqate address validation (Power Automate)
- Finance bridge to D365 (future)

---

## 5. Build Task List

### Phase 0 — Spike & Decision (half day)

- [ ] Provision scratch Dataverse environment + Azure SQL DB
- [ ] Build Account → Contact → Deal → DealProperty chain as virtual tables; confirm N:1 lookups and filtered views work
- [ ] Verify enum/choice column mapping and label display
- [ ] Verify business rules work on virtual-table forms
- [ ] Record the go/no-go decision in this note

### Phase A — Environment & Solutions

- [ ] Create Dataverse environment (dev/trial, EU region)
- [ ] Provision Azure SQL DB (`EuroCRMPOC`) + connector credentials (Entra ID preferred)
- [ ] Create solution publisher (e.g. `KF POC`)
- [ ] Create solutions: `KF_Core_POC` (L2) and `KF_CapitalMarkets_POC` (L5)

### Phase B — SQL Schema: Core (T-SQL)

- [ ] Create `kf_account`, `kf_contact` — GUID PKs, `int`/`nvarchar` only, no `bigint`/`datetime2`
- [ ] Create `kf_site`, `kf_property`
- [ ] Create `kf_siccode`, `kf_energyrating` reference tables
- [ ] Create `kf_gdprrequest`, `kf_auditexport`, `kf_stagegaterule`, `kf_stagehistory`, `kf_integrationlog`
- [ ] Create `kf_wip` — fields from [[wip-data-model]]
- [ ] Enable system-versioned temporal tables (audit, 7-year retention)
- [ ] Create read-optimised views for form display

### Phase C — SQL Schema: Capital Markets

- [ ] Create `kf_deal` — deal fields, `kf_stage` (int), `kf_accountid`, `kf_contactid`, `kf_legalentityaccountid`
- [ ] Create `kf_dealproperty` junction — `kf_allocationpercent`, `kf_passingrent`, `kf_erv`, `kf_occupancy`, `kf_wault`, `kf_capitalvalue_psm`
- [ ] Create `kf_pitch`, `kf_nda`, `kf_bid`, `kf_ddmilestone`, `kf_redflag`
- [ ] Create `kf_kycrecord`, `kf_dataroomaccess`, `kf_investorprofile`
- [ ] Create `kf_feeschedule`, `kf_transactionreport`
- [ ] Add unique indexes + fuzzy-match dedup stored proc

### Phase D — Dataverse Virtual Tables & Relationships

- [ ] Install/update Virtual Connector Provider; create SQL connection + connection reference
- [ ] Create virtual tables from the Entity Catalog (one connection, all tables)
- [ ] Map primary keys (GUID) and primary-name fields on each virtual table
- [ ] Define N:1 lookups on children: Contact→Account, DealProperty→Deal and →Property, Bid→InvestorProfile, NDA/KYC→Account
- [ ] Set External Name = FK column on each lookup; unique per attribute; identical text formatting on PK and FK

### Phase E — Security

- [ ] Implement SQL Row-Level Security (country/BU filtering)
- [ ] Provision the minimal connector credential (read/write to the exposed tables only)
- [ ] Create Dataverse roles: Admin, Broker, Manager (app-level only)

### Phase F — Deal Stage Lifecycle in SQL

- [ ] Encode 8 stages + % complete (5/15/25/35/50/65/85/100) in `kf_stagegaterule`
- [ ] Transition trigger enforcing legal moves; write `kf_stagehistory` on every change
- [ ] Build stage header + conditional tabs on the kf_Deal form

### Phase G — Model-Driven App

- [ ] Create model-driven app `EuroCRM POC`
- [ ] Build forms: kf_Account, kf_Contact, kf_Site, kf_Property, kf_Deal (stage header), kf_DealProperty (quick create), kf_Pitch, kf_NDA, kf_Bid, kf_InvestorProfile
- [ ] Build views: Active Deals Pipeline, Client 360 (filtered by account), WIP Report, Investor Registry, KYC Status
- [ ] Set app sitemap: Clients, Properties, Deals, Compliance, Reports

### Phase H — Sample Data & Validation

- [ ] Seed sample data: 2-3 Brand/Group accounts, legal entities, contacts
- [ ] Seed sample data: sites, properties (FR/DE/ES/PL), one multi-asset deal
- [ ] Advance the sample deal through all 8 stages via the stage field; verify SQL gates fire and `kf_stagehistory` records
- [ ] Create investor profile + bid records linked to a deal (N:1 lookups)
- [ ] Verify RLS restricts cross-country row access
- [ ] Verify WIP values roll up per stage %
- [ ] Ready demo script for POC walkthrough

---

## 6. Minimum Technology Stack

### Required

| Layer | Minimum | Notes |
| ----- | ------- | ----- |
| Tenant | One Microsoft 365 tenant | Free M365 Developer tenant works for POC |
| Licensing | Power Apps Developer Plan (free) | Upgrade to per-user licenses only when moving to prod |
| Environment | 1x Dataverse environment | Provisioned via Power Platform admin center |
| Database | 1x Azure SQL database | All business data; system of record |
| Schema tooling | SSMS / Azure Data Studio (or a dacpac in a pipeline) | Deploys the 24 tables, views, triggers, RLS |
| Dataverse link | Virtual Connector Provider + SQL connection reference | GA; created from the Entity Catalog in make.powerapps.com |
| Build tool | make.powerapps.com | Forms, views, app built here |
| Admin rights | One account: System Administrator + Environment Maker | Same account is enough for POC |
| Solutions | 2 unmanaged: `KF_Core_POC`, `KF_CapitalMarkets_POC` | Unmanaged is fine in dev — managed-only rule applies to TEST/UAT/PROD |

### Not Needed for the POC

- Production Power Apps/Dataverse licenses
- Managed environments, DLP policies, ALM pipelines
- Power Automate or Power BI licenses — integrations and dashboards deferred
- On-prem data gateway — Azure SQL only
- All integrations: Loqate, Outlook, SharePoint, ECS, Finance bridge

### Minimal Build Footprint

**Keep (essential):**

- Phase 0 — spike (half day)
- Phase A — environment + solutions + Azure SQL
- Phases B-C — tables, trimmed to: `kf_account`, `kf_contact`, `kf_site`, `kf_property`, `kf_deal`, `kf_dealproperty` (+ `kf_investorprofile`, `kf_bid` for the bidding demo)
- Phase D — virtual tables + N:1 relationships
- Phase F — SQL stage machine (demo centrepiece)
- Phase G — app with 4-6 forms + one pipeline view
- Phase H — seeded demo data

**Drop for first iteration:**

- Phase E — single SQL role + one Dataverse admin role; RLS on country filter only if time permits
- WIP table, supporting tables, compliance tables
- Dashboards

---

## 7. Option B — Deficiency Fixes

### 1. No BPF on virtual tables

| Strategy | How | Effort |
| -------- | --- | ------ |
| **Stage machine in SQL** (chosen) | `kf_deal.stage` (int) + SQL trigger/constraint enforcing legal transitions + `kf_stagehistory` table. The DB owns the lifecycle; the app just edits a stage field. Audit comes free via the history table. | Medium |
| **Power Automate validation** | Cloud flow on update validates the transition. Works against virtual tables via the connector. | Low |
| **Form-level mimics** | Conditional tabs + business rules driven by the stage field give a BPF-like experience; legal transitions still enforced in SQL. | Low |
| **Hybrid (last resort)** | Keep only `kf_deal` native in Dataverse for the BPF; mirror to SQL for reporting. Breaks "SQL owns all data" — rejected unless BPF becomes a hard enterprise requirement. | Medium |

The 8-stage CM lifecycle maps to a stage enum + stage-gate rule table (`kf_stagegaterule` already in the model) — nothing functionally lost.

### 2. No audit / calculated fields / duplicate detection

| Gap | SQL-side fix |
| --- | ------------ |
| **Audit** (7-year retention) | SQL system-versioned temporal tables + `kf_auditexport` view |
| **Calculated/rollup** (WIP %, deal totals) | Compute in SQL views and expose as virtual-table columns; maintained columns or indexed views for heavy rollups |
| **Option set display** | Enum columns surface as plain numbers unless mapped to choices — verify mapping in Phase 0 spike; label via a `kf_label` reference view if needed |
| **Duplicate detection** | SQL unique indexes (hard prevention) + fuzzy-match stored proc (SIREN/KRS/name) called from a button/flow |

**Platform constraints to inherit:** 1:N relationship queries cap at 1,000 rows (filter early); negative filters (Does Not Equal) break paging — avoid them in views.

### 3. `bigint` → decimal mapping

Rule: **never expose `bigint` to Dataverse.**

- GUID primary keys on every exposed table (required anyway)
- `int` for enumerations and small magnitudes
- `nvarchar` for long external references (SIREN, KRS, UPRN) to avoid decimal display
- Keep `bigint` only in backing columns the app never maps, or `CAST` to `nvarchar` in the view

### 4. Relationship constraints

| Strategy | How |
| -------- | --- |
| **One connection, one database** | All domain tables in a single Azure SQL DB through one connection — virtual-to-virtual relationships are supported within the same provider |
| **Model N:1 lookups on the child** | kf_Contact carries the kf_Account lookup; kf_DealProperty carries Deal + Property lookups. Parent-side subgrids are unsupported for virtual parents — build filtered views ("Client 360": contacts where account = X) instead |
| **ExternalName discipline** | Lookup External Name must exactly match the FK column; unique per attribute; identical text formatting (CAST) on PK and FK |
| **Standard-table lookups** | Resolve via PK (GUID) or an **Alternate Key** on the standard table |

**Spike before Phase D:** covered by Phase 0 — build the Account → Contact → Deal → DealProperty chain in a scratch environment and confirm lookups and subgrid behaviour.

### 5. Live connector reads

| Strategy | How |
| -------- | --- |
| **Azure SQL, not on-prem** | Avoids the gateway hop |
| **Read-optimised views** | Point virtual tables at views that pre-join/denormalise what forms display |
| **Index what the app filters on** | Cover indexes on filtered columns; no functions in filter predicates |
| **Read replica for reporting** | Reporting queries don't touch the app-facing connection |
| **Map only used columns** | Skip ntext/blob/geometry/geography/datetime2/time/rowversion — these SQL types can't map (or only partially) |

At POC scale performance is a non-issue; park read-replica work until load exists.

### Recommended POC Combination

1. **Schema conventions:** GUID PKs, `int`/`nvarchar` only, text-consistent lookups, one Azure SQL DB, one connection
2. **Stage lifecycle in SQL** (trigger + `kf_stagehistory` + `kf_stagegaterule`) — no BPF, no hybrid
3. **Temporal tables for audit**, views for computed values, unique indexes for dedup
4. **N:1 lookups + filtered views** instead of parent subgrids
5. **Spike first** (Phase 0): relationship chain, choice-column mapping, business-rule support on virtual tables

---

## Related

- [[solution-overview]]
- [[data-model-overview]]
- [[data-model-core-tables]]
- [[architecture-key-components]]
- [[capital-markets-data-model]]
- [[property-data-model]]
- [[client-data-model]]
- [[wip-data-model]]
- [[solution-package-model]]
- [[crm-lite-mvp-scope]]