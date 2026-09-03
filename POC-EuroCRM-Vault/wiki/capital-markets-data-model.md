---
status: Draft
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# Capital Markets Data Model

## Data Schema

![[capital-markets-data-model-schema.puml]]

## Core Entities

Twelve entities capture every stage of the deal lifecycle, from pitch to completion.

### Origination & Agreement

| Entity | Description |
| ------ | ----------- |
| kf_Deal | Core deal record with full lifecycle tracking |
| kf_Pitch | Competitive pitch tracking |
| kf_NDA | NDA management |

### Bidding & Due Diligence

| Entity | Description |
| ------ | ----------- |
| kf_Bid | Multi-round bid management |
| kf_DDMilestone | Due diligence milestone tracking |
| kf_RedFlag | Risk and red flag tracking |

### Compliance & Investors

| Entity | Description |
| ------ | ----------- |
| kf_KYCRecord | KYC/AML compliance tracking |
| kf_InvestorProfile | Investor preferences and strategy |
| kf_DataRoomAccess | Data room access management |

### Commercials & Reporting

| Entity | Description |
| ------ | ----------- |
| kf_FeeSchedule | Fee structure management |
| kf_TransactionReport | Auto-generated transaction reports |
| kf_DealProperty | Portfolio property-level tracking |

## Portfolio Data Model & Workflow

A junction record links one deal to many assets, so a portfolio stays a single transaction.

**Key Relationships:**
- `kf_Deal` (1) → (N) `kf_DealProperty` → (N:1) `kf_Property`
- `kf_dealid` (FK), `kf_propertyid` (FK), `kf_allocationpct`

**Tracked Per Property:** Comparables, Due diligence, Regulatory gates, Bidding, Fee allocation

**Why It Stays Simple for Brokers:**
- Sub-grid only on multi-asset deals
- Gates fire automatically per market
- DD status rolls up to deal level
- Portfolios close as one transaction

## Client Touchpoints Across the Lifecycle

Each entity points at the right level: the group for relationships, the legal entity for compliance & billing.

### Deal

- `kf_accountid` — Brand/Group client organisation
- `kf_contactid` — Primary deal contact
- `kf_legalentityaccountid` — Contractual counterparty, required at mandate

### Compliance

- `kf_NDA` — Counterparty legal entity plus signatory
- `kf_KYCRecord` — AML checks at legal entity level
- Brand/Group explicitly excluded from NDA records

### Bid

- `kf_investoraccountid` — The fund, SPV or JV bidding
- `kf_investorcontactid` — The individual contact
- `kf_investorprofileid` — Investment profile behind the bid

**Contact Roles:** Contacts play contextual roles through entity lookups: deal contact, NDA signatory, vendor, buyer, landlord, tenant.

**GDPR Layer, Europe:** Contacts carry consent, subscription and segmentation data. `kf_processingconsent` covers legitimate interest, consent, legal obligation or not assessed.

## kf_InvestorProfile: Knowing What Clients Want

Investment strategy sits on the Brand/Group account, so one group can hold several profiles.

**Sample Profile: Blackstone Value Add**
- Strategy: Core / Core-Plus / Value-Add / Opportunistic
- Target sectors: Offices, Logistics, Residential, Data Centres
- Geographies: UK, France, Germany, Nordics, Iberia, CEE
- Ticket size: `kf_ticketsizemin` to `kf_ticketsizemax`
- Yield & ESG: Target yield, ESG mandatory flag
- Status: Active buyer / Watching / Paused / Inactive

**Relationship Tracking:** Owner and last contact date; Rollups: deals and total invested

**Client Strategy:** Becomes the formal investor strategy repository for the region.

## Capital Markets Regulatory Gates

Local approval gates sit inside the standard eight-stage deal lifecycle.

### Country-Specific Gates

- **France:** city pre-emption and notarial deed
- **Spain:** right-of-refusal on listed buildings

### EIT (Cross-Border Team)

- Multi-jurisdiction KYC and conflict checks
- Intercompany billing across markets

### Eight-Stage Deal Lifecycle with Gates

| Stage | Gate | Owner |
| ----- | ---- | ----- |
| S1 Origination | — | — |
| S2 Pitch & Mandate | Conflict check | EIT |
| S3 Instruction | Multi-jurisdiction KYC | EIT |
| S4 Marketing | — | — |
| S5 Bidding | — | — |
| S6 Exclusivity | — | — |
| S7 Due Diligence | City pre-emption | France |
| | Notarial process | France |
| | Right of refusal | Spain |
| | Pre-emption delegation | EIT |
| S8 Completion | Notarial deed signing | France |
| | Intercompany billing | EIT |
