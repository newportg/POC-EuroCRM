# EuroCRM POC — Component List

**Target:** Model-Driven Power App + SQL Database (Dataverse)
**Scope:** CRM Lite MVP (Phase 0) + Capital Markets (Phase 1)
**Source:** [[solution-overview]], [[data-model-overview]], [[architecture-key-components]]

---

## 1. SQL Database (Dataverse)

### Core Domain Tables — Account & Contact

| Table | Type | Description |
| ----- | ---- | ----------- |
| `account` | OOB extended | Organisation, brand, legal entity, fund, SPV |
| `contact` | OOB extended | Individual person linked to Account |

**Key Account fields:** `accountid`, `name`, `accounttype`, `address1_*`, `telephone1`, `emailaddress1`, `owningbusinessunit`, `parentaccountid`, `kf_accountclassification`, `kf_entitytype`

**Key Contact fields:** `contactid`, `firstname`, `lastname`, `jobtitle`, `emailaddress1`, `telephone1`, `parentcustomerid` (lookup to Account), `kf_processingconsent`

---

### Core Domain Tables — Property

| Table | Type | Description |
| ----- | ---- | ----------- |
| `kf_site` | Custom | Physical building or land parcel (canonical address) |
| `kf_property` | Custom | Commercial asset register |

**kf_Site key fields:** Country-neutral address elements (UPU S42a-6), `kf_addressfull`, `kf_uprn`, `kf_cadastralref`, `kf_loqateid`

**kf_Property key fields:** Identity, address, geocoded, sector, type, status, tenure, areas, floors, parking, asking price, ESG

---

### Capital Markets Tables (Phase 1)

| Table | Category | Description |
| ----- | -------- | ----------- |
| `kf_deal` | Core | Core deal record with 8-stage BPF |
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

---

### Supporting & Infrastructure Tables

| Table | Category | Description |
| ----- | -------- | ----------- |
| `kf_siccode` | Reference | SIC code reference table |
| `kf_energyrating` | Reference | Energy performance ratings |
| `kf_gdprrequest` | Compliance | GDPR data subject requests |
| `kf_auditexport` | Compliance | Audit trail export |
| `kf_stagegaterule` | Config | BPF stage gate validation rules |
| `kf_integrationlog` | Infra | Integration transaction logging |

---

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
| Account | Main + Quick Create | Brand/Group vs Legal Entity classification |
| Contact | Main + Quick Create | Linked to Account via parentcustomerid |
| kf_Site | Main | Country-neutral address with Loqate integration |
| kf_Property | Main | Commercial asset register |
| kf_Deal | Main | 8-stage BPF drives form stages |
| kf_DealProperty | Quick Create | Sub-grid on Deal form |
| kf_Pitch | Main | Pitch tracking |
| kf_NDA | Main | NDA with counterparty + signatory |
| kf_Bid | Main | Multi-round bid with investor profile link |
| kf_InvestorProfile | Main | Strategy per Brand/Group |

### Business Process Flow (BPF)

**Capital Markets 8-Stage Deal Lifecycle:**

| Stage | Name | Gate |
| ----- | ---- | ---- |
| S1 | Origination | — |
| S2 | Pitch & Mandate | Conflict check |
| S3 | Instruction | Multi-jurisdiction KYC |
| S4 | Marketing | — |
| S5 | Bidding | — |
| S6 | Exclusivity | — |
| S7 | Due Diligence | Country-specific regulatory gates |
| S8 | Completion | Notarial deed / billing |

### Views & Dashboards

| View / Dashboard | Purpose |
| ---------------- | ------- |
| Active Deals Pipeline | Deal pipeline by stage, country, service line |
| Client 360 | Account with contacts, deals, properties |
| WIP Report | Revenue at risk by deal stage |
| Investor Registry | Investor profiles by strategy/geography |
| KYC Status | Compliance status across legal entities |

### Security Model

| Component | Purpose |
| --------- | ------- |
| Business Units | Country-level (France, Germany, Spain, Poland) |
| Security Roles | RBAC: Broker, Manager, Compliance, Admin |
| Field-Level Security | Sensitive fields (consent, KYC, financial) |

---

## 3. Solution Package Structure (POC)

For a POC, the layered model simplifies to:

| Solution | Layer | Contents |
| -------- | ----- | -------- |
| `KF_Core_POC` | L2 | All custom tables, option sets, base security |
| `KF_CapitalMarkets_POC` | L5 | CM BPF, CM-specific entities, stage gates |

**Note:** L3/L4/L6/L7 layers are collapsed for POC — country and region logic baked into KF_Core_POC.

---

## 4. Summary: What to Build

### SQL / Dataverse

- **18 custom tables** (kf_* prefixed)
- **2 extended OOB tables** (Account, Contact)
- **~15 option sets** (deal status, property type, sector, etc.)
- **1 Business Process Flow** (8-stage Capital Markets)
- **Relationships:** 1:N, N:N junctions (DealProperty)

### Power App

- **10+ entity forms** (main, quick create)
- **5+ views** (pipeline, client 360, WIP, investors, KYC)
- **1 dashboard** (Power BI or embedded)
- **Security roles** (4 roles: Broker, Manager, Compliance, Admin)

### Integrations (Deferred)

- Outlook email sync (Power Automate)
- SharePoint deal folder provisioning (Power Automate)
- Loqate address validation (Power Automate)
- Finance bridge to D365 (future)

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

---

## 5. Build Task List

### Phase A — Environment & Solutions

- [ ] Create a Dataverse environment (dev/trial, EU region)
- [ ] Create solution publisher (e.g. `KF POC`)
- [ ] Create solutions: `KF_Core_POC` (L2) and `KF_CapitalMarkets_POC` (L5)
- [ ] Enable audit for the environment

### Phase B — Data Model (KF_Core_POC)

- [ ] Define option sets (~15): deal status, stage, property type, tenure, sector, account classification, entity type, KYC status, consent basis, etc.
- [ ] Extend `account` — add `kf_accountclassification`, `kf_entitytype`, `kf_registrationnumber`, `kf_industry`
- [ ] Extend `contact` — add `kf_processingconsent`, `kf_consentsource`
- [ ] Create `kf_site` — country-neutral address fields (UPU S42a-6), `kf_addressfull`, `kf_uprn`, `kf_cadastralref`, `kf_loqateid`
- [ ] Create `kf_property` — identity, address, sector, type, status, tenure, areas, floors, parking, asking price, ESG
- [ ] Create `kf_energyrating`, `kf_siccode` reference tables
- [ ] Create `kf_gdprrequest`, `kf_auditexport`, `kf_stagegaterule`, `kf_integrationlog` supporting tables
- [ ] Create `kf_wip` — WIP tracking fields from [[wip-data-model]]

### Phase C — Capital Markets Tables (KF_CapitalMarkets_POC)

- [ ] Create `kf_deal` — deal fields, status, stage, `kf_accountid`, `kf_contactid`, `kf_legalentityaccountid`
- [ ] Create `kf_dealproperty` junction — `kf_allocationpercent`, `kf_passingrent`, `kf_erv`, `kf_occupancy`, `kf_wault`, `kf_capitalvalue_psm`
- [ ] Create `kf_pitch`, `kf_nda`, `kf_bid`, `kf_ddmilestone`, `kf_redflag`
- [ ] Create `kf_kycrecord`, `kf_dataroomaccess`, `kf_investorprofile`
- [ ] Create `kf_feeschedule`, `kf_transactionreport`

### Phase D — Relationships & Keys

- [ ] Account 1:N Contact
- [ ] Account 1:N kf_Deal (client org); legal entity Account 1:N kf_Deal
- [ ] kf_Deal 1:N kf_DealProperty; kf_Property 1:N kf_DealProperty
- [ ] Account/Contact 1:N kf_NDA, kf_Bid, kf_KYCRecord
- [ ] kf_InvestorProfile 1:N kf_Bid
- [ ] kf_Deal 1:N kf_WIP
- [ ] Set up alternate keys / business rules as needed

### Phase E — Security Model

- [ ] Create Business Units: France, Germany, Spain, Poland
- [ ] Create security roles: Admin, Broker, Manager, Compliance
- [ ] Assign table-level privileges per role
- [ ] Enable field-level security on consent / KYC / financial fields

### Phase F — Business Process Flow

- [ ] Create 8-stage Capital Markets BPF on kf_Deal (S1 Origination → S8 Completion)
- [ ] Map stages to % complete for WIP calculation (5/15/25/35/50/65/85/100%)
- [ ] Configure stage gate validation via kf_stagegaterule

### Phase G — Model-Driven App

- [ ] Create model-driven app `EuroCRM POC`
- [ ] Build forms: Account, Contact, kf_Site, kf_Property, kf_Deal (BPF header), kf_DealProperty (quick create), kf_Pitch, kf_NDA, kf_Bid, kf_InvestorProfile
- [ ] Add kf_DealProperty sub-grid on kf_Deal form (**Option A only** — Option B: N:1 lookup on kf_DealProperty + filtered view instead; virtual tables cannot be the 1 side of a 1:N)
- [ ] Build views: Active Deals Pipeline, Client 360, WIP Report, Investor Registry, KYC Status
- [ ] Build dashboard (embedded Power BI or system dashboard)
- [ ] Set app sitemap: Clients, Properties, Deals, Compliance, Reports

### Phase H — Sample Data & Validation

- [ ] Seed sample data: 2-3 Brand/Group accounts, legal entities, contacts
- [ ] Seed sample data: sites, properties (FR/DE/ES/PL), one multi-asset deal
- [ ] Walk a sample deal through all 8 BPF stages and verify gates fire
- [ ] Create investor profile + bid records linked to a deal
- [ ] Verify security roles restrict cross-BU access
- [ ] Verify WIP values roll up per stage %
- [ ] Ready demo script for POC walkthrough

---

## 6. Minimum Technology Stack

Two variants. **Option A** is the simplest ("Dataverse is the database"). **Option B** satisfies the enterprise requirement that data is stored in a real SQL database, using Dataverse virtual tables — SQL becomes the system of record, Dataverse stores only the app/metadata.

### Shared Requirements (both options)

| Layer | Minimum | Notes |
| ----- | ------- | ----- |
| Tenant | One Microsoft 365 tenant | Free M365 Developer tenant works for POC |
| Licensing | Power Apps Developer Plan (free) | Upgrade to per-user licenses only when moving to prod |
| Environment | 1x Dataverse environment | Provisioned via Power Platform admin center |
| Build tool | make.powerapps.com | All tables, forms, views created here |
| Admin rights | One account: System Administrator + Environment Maker | Same account is enough for POC |
| Solutions | 2 unmanaged: `KF_Core_POC`, `KF_CapitalMarkets_POC` | Unmanaged is fine in dev — managed-only rule applies to TEST/UAT/PROD |

### Option A — Dataverse as Database

| Layer | Minimum | Notes |
| ----- | ------- | ----- |
| Database | Dataverse | Native tables; simplest option, full feature set (BPF, auditing, calculated fields) |

### Option B — SQL as Source of Truth (Virtual Tables)

| Layer | Minimum | Notes |
| ----- | ------- | ----- |
| Database | Azure SQL (preferred) or SQL Server + on-prem data gateway | Hosts all ~18 `kf_*` tables as the system of record |
| Schema rule | GUID (or integer) primary key + one string primary-name field per table | Required for full CRUD through virtual tables; views are read-only |
| Dataverse link | Virtual tables via Virtual Connector Provider (SQL Server connector) | GA; created from the Entity Catalog in make.powerapps.com; SQL connection may use SQL auth or Entra ID |
| Security | Row-level security enforced in SQL (RLS / views) | The connector uses one shared credential set — app security roles do not filter rows |

**Trade-offs in Option B:**

- **No Business Process Flow on virtual tables** — the 8-stage Capital Markets lifecycle becomes a `kf_stage` option-set field + views, not a BPF
- No Dataverse auditing, calculated/rollup fields, or duplicate detection — audit and computed values live in SQL
- `bigint` columns map to decimal in Dataverse — design SQL types accordingly
- Lookups between virtual and native tables work but with constraints — test the Account → Deal → Property chain early
- Every read is a live connector call to SQL — fine for POC, no caching

### Not Needed for the POC

- Production Power Apps/Dataverse licenses
- Managed environments, DLP policies, ALM pipelines
- Power Automate or Power BI licenses — integrations and dashboards deferred
- All integrations: Loqate, Outlook, SharePoint, ECS, Finance bridge
- Data gateway — only if Option B uses on-prem SQL Server instead of Azure SQL

### Minimal Build Footprint

**Keep (essential):**

- Phase A — environment + 2 solutions
- Phases B-D — tables, trimmed to: `account`, `contact`, `kf_site`, `kf_property`, `kf_deal`, `kf_dealproperty` (+ `kf_investorprofile`, `kf_bid` for the bidding demo)
- Phase F — the 8-stage BPF (**Option A only**; Option B replaces it with a stage field + stage views)
- Phase G — app with 4-6 forms + one pipeline view
- Phase H — seeded demo data

**Drop for first iteration:**

- Phase E — single Business Unit + one role instead of 4 BU / 4 roles
- WIP table, supporting tables, compliance tables
- Dashboards

---

## 7. Option B — Deficiency Fixes

### 1. No BPF on virtual tables

| Strategy | How | Effort |
| -------- | --- | ------ |
| **Stage machine in SQL** (recommended) | `kf_deal.stage` (int) + SQL trigger/constraint enforcing legal transitions + `kf_stagehistory` table. The DB owns the lifecycle; the app just edits a stage field. Audit comes free via the history table. | Medium |
| **Power Automate validation** | Cloud flow on update validates the transition. Works against virtual tables via the connector. | Low |
| **Form-level mimics** | Conditional tabs + business rules driven by the stage field give a BPF-like experience; legal transitions still enforced in SQL. | Low |
| **Hybrid (last resort)** | Keep only `kf_deal` native in Dataverse for the BPF; mirror to SQL for reporting. Breaks "SQL owns all data" — only if BPF is non-negotiable. | Medium |

The 8-stage CM lifecycle maps to a stage enum + stage-gate rule table (`kf_stagegaterule` already in the model) — nothing functionally lost.

### 2. No audit / calculated fields / duplicate detection

| Gap | SQL-side fix |
| --- | ------------ |
| **Audit** (7-year retention) | SQL system-versioned temporal tables + `kf_audit` table; optionally expose a read-only view for an audit screen |
| **Calculated/rollup** (WIP %, deal totals) | Compute in SQL views and expose as virtual-table columns; maintained columns or indexed views for heavy rollups |
| **Option set display** | Enum columns surface as plain numbers unless mapped to choices — verify mapping in spike; label via a `kf_label` reference view if needed |
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
| **Model N:1 lookups on the child** | Contact carries the Account lookup; kf_DealProperty carries Deal + Property lookups. Parent-side subgrids are unsupported for virtual parents — build filtered views ("Client 360": contacts where account = X) instead |
| **ExternalName discipline** | Lookup External Name must exactly match the FK column; unique per attribute; identical text formatting (CAST) on PK and FK |
| **Standard-table lookups** | Resolve via PK (GUID) or an **Alternate Key** on the standard table |

**Spike before Phase D (half day):** build the Account → Contact → Deal → DealProperty chain in a scratch environment and confirm lookups and subgrid behaviour.

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
5. **Spike first** (half day): relationship chain, choice-column mapping, business-rule support on virtual tables
