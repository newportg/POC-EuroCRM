# Architecture — Key Components

Status: Draft
Parent: [[solution-overview]]
Source: European CRM Architecture Review 2.pdf, EU CRM Data Model.xlsx

## Platform Decision

**Current Hypothesis:** Power Apps model-driven apps on Dataverse are a better fit where the value sits in a custom Knight Frank data model rather than a packaged sales process.

See [[power-apps-rationale]] for detailed analysis.

## Key Components

### 1. Dataverse Platform (L1)

Microsoft-managed foundation providing:
- Custom tables with relationships
- Business Process Flows (BPFs)
- Security roles + Business Units
- Dataverse audit trail
- API access (OData + custom)
- Mobile access

### 2. KF_Core (L2)

Global core layer defining the base schema:
- **40+ table shells** — Account, Contact, Property, Site, Deal, DealProperty, NDA, Bid, etc.
- **Option sets** — All custom option sets defined at this layer
- **BU hierarchy** — Business Unit structure for security and data ownership
- **Base security** — RBAC roles and permissions
- **Integration base** — Outlook sync, SharePoint, Power BI connectors

### 3. Region Layer (L3)

KF_Europe configuration:
- EUR default currency
- GDPR baseline compliance
- Regional Power BI dashboard
- Cross-border data sharing rules

### 4. Country Layers (L4)

Country-specific extensions:
- **KF_France** — `kf_fr_*` columns, CNIL compliance, notarial requirements
- **KF_Germany** — `kf_de_*` columns, BDSG compliance
- **KF_Poland** — `kf_pl_*` columns
- **KF_Spain** — `kf_es_*` columns, right-of-refusal rules

### 5. Service Line Core (L5)

Service-line specific BPFs and workflows:

| Service Line | Component | BPF Stages |
| ------------ | --------- | ---------- |
| Capital Markets | KF_CapitalMarkets_Core | 8-stage (Origination → Completion) |
| OSS | KF_OSS_Core | Future |
| Valuations | KF_Valuations_Core | Future |
| Residential | KF_Residential_Core | Future |
| Finance Integration | KF_Finance_Integration | WIP bridge to D365 Finance |

### 6. Service Line + Country (L6)

Country variants inheriting from L5:
- KF_CM_France — French regulatory gates (city pre-emption, notarial deed)
- KF_CM_Spain — Spanish regulatory gates (right-of-refusal)
- KF_OSS_France — Future

### 7. Cross-Border Overlays (L7)

Multi-market entities:
- **KF_EIT** — European Investment Team for cross-border portfolios
- **KF_Private_Office** — UHNW individuals spanning CM, Residential, Valuations

## Core Data Entities

### Client Domain

| Entity | Purpose |
| ------ | ------- |
| Account | Organisation, brand, legal entity, fund, SPV |
| Contact | Individual person linked to Account |
| kf_InvestorProfile | Investment strategy per Brand/Group |

### Property Domain

| Entity | Purpose |
| ------ | ------- |
| kf_Site | Physical building or land parcel |
| kf_Property | Commercial asset register |
| kf_ResProperty | Residential asset register |
| kf_DealProperty | Junction: deal ↔ property |

### Deal Domain (Capital Markets)

| Entity | Purpose |
| ------ | ------- |
| kf_Deal | Core deal record with 8-stage BPF |
| kf_Pitch | Competitive pitch tracking |
| kf_NDA | NDA management |
| kf_Bid | Multi-round bid management |
| kf_DDMilestone | Due diligence tracking |
| kf_RedFlag | Risk tracking |

### Compliance Domain

| Entity | Purpose |
| ------ | ------- |
| kf_KYCRecord | KYC/AML at legal entity level |
| kf_GDPRRequest | GDPR data subject requests |
| kf_DataRoomAccess | Data room access management |

### Finance Domain

| Entity | Purpose |
| ------ | ------- |
| kf_FeeSchedule | Fee structure per deal |
| kf_WIP | Work in progress tracking |
| kf_TransactionReport | Auto-generated transaction reports |

## Integration Components

| Component | Target | Purpose |
| --------- | ------ | ------- |
| Power Automate | Outlook | Email sync, activity tracking |
| Power Automate | SharePoint | Auto-provision deal folders |
| Power Automate | CI-Journeys | Marketing handoff |
| Finance Bridge | D365 Finance | 9 integration flows (Project, Budget, Invoice, WIP) |
| Loqate | Dataverse | Auto-address validation for kf_Site |
| Copilot | Dataverse | AI-powered client matching |
| Power BI | Dataverse | Dashboards and reporting |
| ECS Publisher | ECS (Enterprise Connectivity Services) | Publish change notifications for Major entity create/update |

### ECS Publications

Every create/update of a **Major entity** (Client, Property, Deal domains — confirm definitive list with TDA) publishes a change notification to the Knight Frank ECS platform, the internal notification and message bus that keeps other systems informed of changes. Publication is performed from a Dataverse plugin / Power Automate flow; delivery is asynchronous and logged in `kf_IntegrationLog`. See [[architecture-application]] for the detailed pattern.

## Technical Rules

- KF_Core defines ALL option sets and custom tables as base
- No regional fork can create duplicate tables
- Each layer is a separate managed solution
- No unmanaged customisations in TEST, UAT, or PROD
- Layer 6 adds columns with country prefixes, never renames standard stages
- Adding a country = new L4 + L6 | Adding a service line = new L5

## Related Documents

- [[solution-package-model]] — Layer model details
- [[client-data-model]] — Client entity schema
- [[property-data-model]] — Property entity schema
- [[capital-markets-data-model]] — Capital Markets entity schema
- [[wip-data-model]] — WIP and Finance integration
- [[data-model-core-tables]] — Layer 2 table definitions
- [[architecture-diagram]] — Visual component diagram
