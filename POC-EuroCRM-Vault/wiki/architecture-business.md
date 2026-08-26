# Architecture — Business

Status: Draft
Parent: [[solution-overview]]
Source: European CRM Architecture Review 2.pdf, EU CRM Data Model.xlsx

## Business Architecture Overview

The EuroCRM business architecture is structured around two layers:

1. **Shared Foundation (CRM Lite)** — Client, contact, property, and engagement tracking reusable across all service lines and countries
2. **Service Line Builds** — Vertical-specific workflows (Capital Markets first) built on top of the shared foundation

## Core Business Capabilities

### Client Management

| Capability | Description | Entities |
| ---------- | ----------- | -------- |
| Client Hierarchy | Brand/Group → Legal Entity relationship model | Account, Contact |
| Client Classification | SIC-coded industry sectors, entity type (Fund, SPV, JV) | Account |
| Client Intelligence | Cross-border, cross-service-line client view | Account, Contact, InvestorProfile |
| GDPR Compliance | Processing consent, data subject requests | Contact, kf_GDPRRequest |

### Property Management

| Capability | Description | Entities |
| ---------- | ----------- | -------- |
| Physical Asset Register | Canonical building/land parcel | kf_Site |
| Commercial Asset Register | Sector, type, status, tenure, areas, ESG | kf_Property |
| Residential Asset Register | Bedrooms, tenure, rent, guide price | kf_ResProperty |
| Address Validation | Loqate auto-lookup and kf_Site creation | kf_Site |

### Deal Management (Capital Markets)

| Capability | Description | Entities |
| ---------- | ----------- | -------- |
| 8-Stage Deal Lifecycle | Origination → Pitch → Instruction → Marketing → Bidding → Exclusivity → DD → Completion | kf_Deal |
| Pitch Tracking | Competitive pitch management | kf_Pitch |
| NDA Management | Counterparty legal entity and signatory | kf_NDA |
| Bid Management | Multi-round bidding with investor profiles | kf_Bid |
| Due Diligence | Milestone tracking with red flag management | kf_DDMilestone, kf_RedFlag |
| Portfolio Management | Junction record linking deals to multiple properties | kf_DealProperty |

### Compliance & Risk

| Capability | Description | Entities |
| ---------- | ----------- | -------- |
| KYC/AML | Legal entity level checks, multi-jurisdiction | kf_KYCRecord |
| Regulatory Gates | Country-specific gates (France: pre-emption; Spain: right-of-refusal) | kf_Deal, kf_StageGateRule |
| Data Room Access | Virtual data room access management | kf_DataRoomAccess |
| Audit Trail | 7-year retention, export capability | kf_AuditExport |

### Finance & Reporting

| Capability | Description | Entities |
| ---------- | ----------- | -------- |
| Fee Management | Fee structure per deal with schedule tracking | kf_FeeSchedule |
| WIP Tracking | Work in progress from deal creation to fee earned | kf_WIP |
| Transaction Reports | Auto-generated post-close reports | kf_TransactionReport |
| Finance Bridge | 9 integration flows to D365 Finance | kf_IntegrationLog |

## Business Process Flows

### Capital Markets — 8-Stage BPF

```mermaid
flowchart LR
    S1[S1: Origination] --> S2[S2: Pitch & Mandate]
    S2 --> S3[S3: Instruction]
    S3 --> S4[S4: Marketing]
    S4 --> S5[S5: Bidding]
    S5 --> S6[S6: Exclusivity]
    S6 --> S7[S7: Due Diligence]
    S7 --> S8[S8: Completion]
```

**Stage Gates:**
- S2: Conflict check (EIT)
- S3: Multi-jurisdiction KYC (EIT)
- S7: City pre-emption (France), Notarial process (France), Right of refusal (Spain), Pre-emption delegation (EIT)
- S8: Notarial deed signing (France), Intercompany billing (EIT)

**Finance Integration:**
- Each stage maps to a % complete in D365 Finance (S1=5%, S2=15%, ... S8=100%)
- S3 fires Flow 1: Finance project created
- Deal won raises draft invoice request
- Monthly batch refreshes WIP balance

### Client Onboarding

1. Account created (Brand/Group or Legal Entity)
2. Contact linked to Account
3. SIC classification assigned
4. National registration number validated
5. GDPR consent recorded (Layer 3)
6. KYC/AML checks (if Legal Entity)

### Property Registration

1. User types address in CRM form
2. Loqate type-ahead returns validated matches
3. User selects match → fields auto-fill
4. Power Automate creates/matches kf_Site silently
5. kf_Property or kf_ResProperty linked to Site

## Capability Map by Layer

| Layer | Business Capabilities |
| ----- | --------------------- |
| L2 (Core) | Client hierarchy, Property register, Activity tracking, Document management |
| L3 (Region) | GDPR compliance, EUR currency, Regional reporting |
| L4 (Country) | Local regulatory gates, Country-specific forms, National registration validation |
| L5 (Service Line) | Deal lifecycle (CM), Engagement tracking (OSS), Valuation workflow (Val) |
| L6 (SL + Country) | Country-specific BPF extensions, Regulatory stage gates |
| L7 (Cross-Border) | Multi-market portfolios, Cross-border KYC, Intercompany billing |

## Service Line Business Processes

| Service Line | Process | BPF | Status |
| ------------ | ------- | ----- | ------ |
| Capital Markets | Deal lifecycle (8-stage) | KF_CapitalMarkets_Core | MVP Phase 1 |
| Occupier Strategy & Solutions | Engagement workflow | KF_OSS_Core | Future Phase 3 |
| Valuations | Valuation instruction | KF_Valuations_Core | Future Phase 3 |
| Residential | Sales/Lettings pipeline | KF_Residential_Core | Future Phase 4 |
| Property Management | Mandate management | KF_PropertyManagement_Core | Future Phase 3 |
| Capital Advisory | Debt mandate | KF_CapitalAdvisory_Core | Future Phase 3 |
| Development | Project tracking | KF_Development_Core | Future Phase 3 |
| ESG Consultancy | Assessment workflow | KF_ESG_Core | Future Phase 3 |
| Building Consultancy | Survey workflow | KF_BuildingConsultancy_Core | Future Phase 3 |
| Investor Advisory | Mandate tracking | KF_InvestorAdvisory_Core | Future Phase 3 |
| Workplace Consulting | Assessment workflow | KF_Workplace_Core | Future Phase 3 |
| Leasing | Lease pipeline | KF_Leasing_Core | Future Phase 3 |

## Related Documents

- [[business-capabilities]] — Capability definitions
- [[client-data-model]] — Client entity schema
- [[property-data-model]] — Property entity schema
- [[capital-markets-data-model]] — Capital Markets entity schema
- [[wip-data-model]] — WIP and Finance integration
- [[implementation-phases]] — Phase definitions
