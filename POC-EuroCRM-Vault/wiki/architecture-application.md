# Architecture — Application

Status: Draft
Parent: [[solution-overview]]
Source: European CRM Architecture Review 2.pdf, EU CRM Data Model.xlsx

## Application Architecture Overview

EuroCRM is built on **Power Apps model-driven apps on Dataverse** — a custom CRM platform rather than a packaged sales process (D365 Sales). The application is structured as a set of managed solutions deployed across 8 layers (L0-L7).

See [[power-apps-rationale]] for the platform selection rationale.

## Platform Selection Rationale

### Why Not D365 Sales?

| D365 Sales Assumption | KF Reality |
| ---------------------- | ---------- |
| Lead → Opportunity → Quote → Order → Invoice | Competitive pitching → NDA → Multi-round bidding → DD → Completion |
| Product Catalogue | Advisory services, not products |
| LinkedIn Sales Navigator | Custom investor intelligence |
| 3 entities fit (Opportunity, Quote, Product) | 8 entities have no equivalent |

### Why Dataverse + Power Apps?

- Custom tables with relationships match KF's advisory lifecycle
- Business Process Flows (BPFs) support 8-stage deal workflow
- Security roles + Business Units enable country/service-line isolation
- Native Outlook, SharePoint, Power BI integration
- OData + custom API for Finance integration
- Mobile access for field brokers
- 7-year audit trail for compliance

## Application Components

### 1. Model-Driven Apps

| App | Layer | Purpose |
| ----- | ----- | ------- |
| KF CRM (Main) | L2-L7 | Unified client, property, deal management |
| KF Capital Markets | L5-L6 | 8-stage deal lifecycle with regulatory gates |
| KF Residential (Future) | L5 | Sales, lettings, property management |
| KF OSS (Future) | L5 | Occupier strategy and engagements |

### 2. Business Process Flows (BPFs)

| BPF | Layer | Stages |
| ----- | ----- | ------ |
| Capital Markets Deal | L5 | S1 Origination → S2 Pitch → S3 Instruction → S4 Marketing → S5 Bidding → S6 Exclusivity → S7 DD → S8 Completion |
| CM France Extension | L6 | Adds: City pre-emption, Notarial process, Notarial deed signing |
| CM Spain Extension | L6 | Adds: Right-of-refusal gate |
| CM EIT Extension | L7 | Adds: Multi-jurisdiction KYC, Conflict check, Intercompany billing |
| Finance Integration | L5 | Maps deal stage → Finance % complete |

### 3. Forms and Views

| Component | Purpose |
| --------- | ------- |
| Account forms | Brand/Group view, Legal Entity view, hierarchy |
| Contact forms | Individual profile, GDPR consent, activity history |
| Deal forms | 8-stage BPF, property sub-grid, fee schedule |
| Property forms | Commercial vs residential, site link, ESG data |
| Investor Profile forms | Strategy, target sectors, geographies, ticket size |

### 4. Dashboards

| Dashboard | Layer | Audience |
| --------- | ----- |---------- |
| Regional PBI | L3 | Europe leadership |
| Country PBI | L4 | Country managers |
| CM Pipeline | L5 | Capital Markets brokers |
| WIP Aging | L5 | Finance team |
| Cross-Border | L7 | EIT team |

## Integration Patterns

### Synchronous Integrations

| Pattern | Source → Target | Purpose |
| ------- | ---------------- | ------- |
| OData API | External → Dataverse | Real-time data queries |
| Custom API | Dataverse → External | Triggered operations |
| Plugin | Dataverse → Dataverse | Business rule enforcement |

### Asynchronous Integrations

| Pattern | Source → Target | Purpose |
| ------- | ---------------- | ------- |
| Power Automate | Outlook → Dataverse | Email sync, activity tracking |
| Power Automate | SharePoint → Dataverse | Document provisioning |
| Power Automate | Dataverse → CI-Journeys | Marketing handoff |
| Finance Bridge | Dataverse → D365 Finance | 9 integration flows |
| Loqate | Loqate → Dataverse | Address validation |
| ECS Publish | Dataverse → ECS | Change notification for Major entity updates |

### ECS Change Notification

Whenever a **Major entity** is created or updated in Dataverse, a change notification is published to the Knight Frank **ECS (Enterprise Connectivity Services)** platform.

- **What:** ECS is Knight Frank's internal notification and message bus. It notifies other systems that a change has happened — it is not a data replication service.
- **Trigger:** Create or update of a Major entity record.
- **Candidate Major entities:** [[architecture-data|Client]] (Account, Contact), [[architecture-data|Property]] (kf_Site, kf_Property), and [[architecture-data|Deal]] (kf_Deal) domains.
  - **Note:** the definitive Major entity list is not yet defined in the wiki — confirm with TDA / enterprise architecture before build.
- **Mechanism:** Dataverse plugin or Power Automate flow on entity create/update publish a change event (entity type, record ID, changed fields, timestamp, source) to ECS.
- **Consumers:** any enterprise system subscribed to ECS topics reacts to the notification (e.g. downstream registries, reporting, downstream workstreams).
- **Audit:** all publications are logged in `kf_IntegrationLog`.

### Finance Bridge — 9 Integration Flows

| Flow | Trigger | Purpose |
| ---- | ------- | ------- |
| Flow 1 | S3 stage change | Create Finance project |
| Flow 2 | Stage change | Update % complete in Finance |
| Flow 3 | Deal won | Raise draft invoice request |
| Flow 4 | Invoice posted | Return invoice and payment data |
| Flow 5 | Monthly batch | Refresh WIP balance and ageing |
| Flow 6 | Credit hold | Alert broker in Teams |
| Flow 7 | Fee schedule change | Sync budget/contract lines |
| Flow 8 | Deal closure | Final revenue recognition |
| Flow 9 | Monthly | Reconciliation report |

## Security Architecture

### Business Unit Hierarchy

```
KF Global
├── KF_Europe (L3)
│   ├── KF_France (L4)
│   │   ├── KF_CM_France (L6)
│   │   └── KF_OSS_France (L6)
│   ├── KF_Germany (L4)
│   ├── KF_Poland (L4)
│   └── KF_Spain (L4)
│       └── KF_CM_Spain (L6)
└── KF_EIT (L7)
```

### Security Roles

| Role | Scope | Permissions |
| ---- | ----- |------------ |
| CM Broker | Country BU | CRUD on deals, contacts, properties |
| CM Manager | Country BU | Approve deals, view all country data |
| EIT User | Cross-border | Read/write cross-border deals |
| Finance | Global | Read WIP, fee schedules, transaction reports |
| Compliance | Global | Read KYC, GDPR requests, audit logs |
| Admin | Global | Full access across all BUs |

## Data Access Patterns

| Operation | Pattern | Notes |
| --------- | ------- | ----- |
| Create deal | Form submission | BPF auto-creates child records |
| View pipeline | Dashboard | Aggregated across country BUs |
| Cross-border search | Advanced find | Queries across multiple BUs |
| Document upload | SharePoint integration | Auto-provisioned per deal |
| Email tracking | Outlook add-in | Links to deal/contact |
| Mobile access | Power Apps mobile | Offline capability |

## Deployment Architecture

### Managed Solutions

Each layer is a separate managed solution:

| Solution | Layer | Dependencies |
| -------- | ----- |------------- |
| KF_Core | L2 | Dataverse |
| KF_Europe | L3 | KF_Core |
| KF_France | L4 | KF_Europe |
| KF_Germany | L4 | KF_Europe |
| KF_Poland | L4 | KF_Europe |
| KF_Spain | L4 | KF_Europe |
| KF_CapitalMarkets_Core | L5 | KF_Core |
| KF_CM_France | L6 | KF_France + KF_CapitalMarkets_Core |
| KF_CM_Spain | L6 | KF_Spain + KF_CapitalMarkets_Core |
| KF_EIT | L7 | KF_Europe + KF_CapitalMarkets_Core |

### Environment Strategy

| Environment | Purpose | Solutions |
| ----------- | ------- |----------|
| DEV | Development | Unmanaged (L2-L6) |
| TEST | Integration testing | Managed |
| UAT | User acceptance | Managed |
| PROD | Production | Managed |

**Rule:** No unmanaged customisations in TEST, UAT, or PROD.

## Technical Rules

- KF_Core defines ALL option sets and custom tables as base
- No regional fork can create duplicate tables
- Layer 6 adds columns with country prefixes (`kf_fr_`, `kf_es_`), never renames standard stages
- Adding a country = new L4 + L6 solutions
- Adding a service line = new L5 solution
- Columns and relationships added by higher layers

## Related Documents

- [[power-apps-rationale]] — Platform selection analysis
- [[solution-package-model]] — Layer model details
- [[architecture-key-components]] — Component inventory
- [[architecture-dataflow]] — Integration flow diagram
- [[architecture-diagram]] — Visual component diagram
