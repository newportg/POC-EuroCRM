---
status: Draft
parent:"[[data-model-overview]]"
source: EU CRM Data Model.xlsx
---

# Core Data Model Tables

## Data Schema

![[data-model-core-tables-schema.puml]]

## Layer 2: KF_Core

Layer 2 (Global Core) defines every data table used across the business (deals, properties, investors, NDAs, bids, KYC records) as empty "shells." All custom table definitions are born at this layer. Columns and relationships are added by higher layers.

## Core Entities

### Account (OOB — Extended)

The canonical client organisation record.

**Key Fields:**
- `accountid` — GUID, primary key
- `name` — Organisation name
- `accounttype` — Investor, vendor, occupier
- `address1_*` — Composite address
- `telephone1` / `emailaddress1` — Primary contact details
- `owningbusinessunit` — Security ownership
- `parentaccountid` — Parent account hierarchy

### Contact (OOB — Extended)

The individual person, always associated to an Account.

**Key Fields:**
- `contactid` — GUID, primary key
- `firstname` / `lastname` — Person name
- `jobtitle` — Role at the organisation
- `emailaddress1` — Primary email
- `telephone1` — Primary phone
- `parentcustomerid` — Lookup to Account
- `kf_processingconsent` — GDPR basis, Layer 3 EU

### kf_Property

The shared asset register that every commercial service line reads.

**Key Fields:**
- Identity and address, geocoded
- Sector, type, status, tenure
- Areas, floors, parking, planning
- Asking price, owner, ESG

### kf_Site

The canonical building or land parcel that every other record hangs off.

**Key Fields:**
- Country-neutral address elements (UPU S42a-6 / ISO 19773) — see [[property-data-model]]
- `kf_addressfull` — single-line address rendered per international format
- `kf_uprn` — UK reference
- `kf_cadastralref` — EU registry
- `kf_landregistrytitle` — deed
- `kf_loqateid` — verified address

### kf_DealProperty

Junction record linking one deal to many assets.

**Key Fields:**
- `kf_allocationpercent`, `kf_lotstatus`
- `kf_passingrent`, `kf_erv`
- `kf_occupancy`, `kf_wault`
- `kf_capitalvalue_psm`, `kf_tenantid`

## Service Line Tables

### Capital Markets (Layer 5)

See [[capital-markets-data-model]] for detailed definitions.

| Entity | Description |
| ------ | ----------- |
| kf_Deal | Core deal record with full lifecycle tracking |
| kf_Pitch | Competitive pitch tracking |
| kf_NDA | NDA management |
| kf_Bid | Multi-round bid management |
| kf_DDMilestone | Due diligence milestone tracking |
| kf_RedFlag | Risk and red flag tracking |
| kf_FeeSchedule | Fee structure management |
| kf_KYCRecord | KYC/AML compliance tracking |
| kf_InvestorProfile | Investor preferences and strategy |
| kf_DataRoomAccess | Data room access management |
| kf_TransactionReport | Auto-generated transaction reports |

### Residential (Layer 5)

See [[property-data-model]] for detailed definitions.

| Entity | Description |
| ------ | ----------- |
| kf_ResProperty | Residential property record |
| kf_SalesInstruction | Sales instruction tracking |
| kf_LettingsInstruction | Lettings instruction tracking |
| kf_Tenancy | Tenancy management |
| kf_Applicant | Applicant tracking |
| kf_Viewing | Viewing scheduling |
| kf_Offer | Offer management |
| kf_BuyingBrief | Buying brief tracking |

### Other Service Lines (Future Phases)

| Service Line | Entities |
| ------------ | -------- |
| OSS | kf_Engagement, kf_Lease, kf_WorkplaceAssessment, kf_LocationSearch |
| Valuations | kf_ValuationInstruction |
| ESG | kf_ESGAssessment |
| Building Consultancy | kf_BuildingSurvey |
| Development | kf_DevelopmentProject |
| Capital Advisory | kf_DebtMandate |
| Property Management | kf_PropertyMandate, kf_MaintenanceRequest |
| Investor Advisory | kf_InvestorMandate |

## Supporting Tables

| Table | Purpose |
| ----- | ------- |
| kf_SICCode | SIC code reference table |
| kf_EnergyRating | Energy performance ratings |
| kf_GDPRRequest | GDPR data subject requests |
| kf_AuditExport | Audit trail export |
| kf_StageGateRule | Configuration table for BPF stage gate validation rules |
| kf_IntegrationLog | Integration transaction logging |
