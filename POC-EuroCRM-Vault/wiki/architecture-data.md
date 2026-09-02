# Architecture — Data

Status: Draft
Parent: [[solution-overview]]
Sources: European CRM Architecture Review 2.pdf, EU CRM Data Model.xlsx, European_CRM_Client_Industry_Master_Taxonomy.xlsx, European_CRM_Property360_Master_Taxonomy.xlsx

## Data Architecture Overview

The EuroCRM data architecture is built on **Dataverse** with a layered schema model. All custom tables are defined at Layer 2 (KF_Core) as "shells" — higher layers add columns, relationships, and behaviour without duplicating table definitions.

## Core Data Domains

### 1. Client Domain

**Purpose:** Single trusted view of every client across service lines and countries.

| Entity | Layer | Purpose |
| ------ | ----- | ------- |
| Account | L2 | Organisation, brand, legal entity, fund, SPV |
| Contact | L2 | Individual person, always linked to Account |
| kf_InvestorProfile | L5 | Investment strategy per Brand/Group |

**Key Design Decisions:**
- Two-tier hierarchy: Brand/Group (relationship, reporting) → Legal Entity (KYC, billing, counterparty)
- Classification fields: `kf_accountclassification` (Brand/Group, Legal Entity, Individual), `kf_entitytype` (Fund, SPV, JV, HoldCo, OpCo, Trust)
- SIC-coded industry classification (`kf_industry`) mapped to 66 KF sectors
- National registration numbers (`kf_registrationnumber`) per country (SIREN/SIRET, Handelsregister, Registro Mercantil, KRS)

See [[client-data-model]] for full schema.

### 2. Property Domain

**Purpose:** Canonical property register shared across all service lines.

| Entity | Layer | Purpose |
| ------ | ----- | ------- |
| kf_Site | L2 | Physical building or land parcel |
| kf_Property | L2 | Commercial asset register |
| kf_ResProperty | L5 | Residential asset register |
| kf_DealProperty | L2 | Junction: deal ↔ property |

**Key Design Decisions:**
- `kf_Site` is the canonical physical asset — all other records hang off it
- Commercial vs residential split: different attributes, different audiences, different deal cycles (6-18 months vs days-weeks)
- Junction record (`kf_DealProperty`) holds deal-specific measures — never overwrites master asset
- Loqate auto-creates `kf_Site` records silently in background
- 10 service lines read the same property record (CM, OSS, Valuations, ESG, Building Consultancy, Development, Capital Advisory, Property Management, Leasing, Residential)

**Entity Relationships:**
- kf_Site (1) → (N) kf_Property
- kf_Site (1) → (N) kf_ResProperty
- kf_Deal (1:N) → kf_DealProperty (N:1) → kf_Property

See [[property-data-model]] for full schema.

### 3. Deal Domain (Capital Markets)

**Purpose:** End-to-end deal lifecycle tracking from origination to completion.

| Entity | Layer | Purpose |
| ------ | ----- | ------- |
| kf_Deal | L5 | Core deal record with 8-stage BPF |
| kf_Pitch | L5 | Competitive pitch tracking |
| kf_NDA | L5 | NDA management |
| kf_Bid | L5 | Multi-round bid management |
| kf_DDMilestone | L5 | Due diligence milestone tracking |
| kf_RedFlag | L5 | Risk and red flag tracking |

**Key Design Decisions:**
- 12 entities capture every stage of the deal lifecycle
- Portfolio model: one deal → many properties via kf_DealProperty junction
- Client touchpoints: Brand/Group for relationships, Legal Entity for compliance & billing
- Regulatory gates fire automatically per market (France: pre-emption; Spain: right-of-refusal)

See [[capital-markets-data-model]] for full schema.

### 4. Compliance Domain

**Purpose:** Regulatory and data governance across all jurisdictions.

| Entity | Layer | Purpose |
| ------ | ----- | ------- |
| kf_KYCRecord | L5 | KYC/AML at legal entity level |
| kf_NDA | L5 | NDA counterparty management |
| kf_GDPRRequest | L2 | GDPR data subject requests |
| kf_DataRoomAccess | L5 | Virtual data room access |
| kf_AuditExport | L2 | Audit trail export (7-year retention) |
| kf_StageGateRule | L5 | BPF stage gate configuration |

**Key Design Decisions:**
- KYC at legal entity level, not Brand/Group
- NDA explicitly excludes Brand/Group — only legal entities
- GDPR consent: `kf_processingconsent` (legitimate interest, consent, legal obligation, not assessed)
- 7-year audit retention for compliance

### 5. Finance Domain

**Purpose:** WIP tracking, fee management, and D365 Finance integration.

| Entity | Layer | Purpose |
| ------ | ----- | ------- |
| kf_FeeSchedule | L5 | Fee structure per deal |
| kf_WIP | L5 | Work in progress tracking |
| kf_TransactionReport | L5 | Auto-generated transaction reports |
| kf_IntegrationLog | L5 | Integration transaction logging |

**Key Design Decisions:**
- Every CRM deal becomes a Finance project in D365 Finance
- BPF stage maps to % complete (S1=5%, S2=15%, ... S8=100%)
- 9 integration flows bridge CRM → Finance
- WIP = deal creation to fee earned (delivered, not yet billed)

See [[wip-data-model]] for full schema.

### 6. Supporting Domain

**Purpose:** Reference data and infrastructure tables.

| Entity | Layer | Purpose |
| ------ | ----- | ------- |
| kf_SICCode | L2 | SIC code reference (21 sections, 66 KF sectors) |
| kf_HILUCSCode | L2 | HILUCS reference (43 KF asset classes) |
| kf_EnergyRating | L2 | EPC energy performance ratings |
| Lead | L5 | Marketing lead (D365 CI-Journeys integration) |

## Major Entity Change Publishing (ECS)

Whenever a **Major entity** is created or updated, a change notification is sent to the Knight Frank **ECS (Enterprise Connectivity Services)** platform — the internal notification and message bus that informs other systems a change has happened.

| Aspect | Design |
| ------ | ------ |
| Trigger | Create/update of a Major entity in Dataverse |
| Publish | Plugin / Power Automate flow → ECS topic |
| Payload | Entity type, record ID, changed fields, timestamp, source system |
| Candidates | Client (Account, Contact), Property (kf_Site, kf_Property), Deal (kf_Deal) |
| Audit | Logged in `kf_IntegrationLog` |
| Contract | Confirm definitive Major entity list and ECS topic/contract with TDA and enterprise architecture |

The change events are notifications only — consumers query Dataverse (or enterprise mastered sources) for the full record; ECS does not replicate data.

## Taxonomy Standards

### Client Industry — SIC to KF Mapping

21 SIC sections → 66 KF client sectors and sub-segments. See [[taxonomy-sic-kf]].

**Strategic Sectors:** Private Equity & Funds, Sovereign Wealth, Banking & Financial Services, Insurance & Pensions, Real Estate, Technology, Logistics & Distribution

**SIC Gaps:** Sovereign Wealth Funds, Family Offices, SPVs, REITs, PropTech, Co-Working, Infrastructure Funds, RE-focused PE — none have explicit SIC codes.

### Asset Class — HILUCS to KF Mapping

HILUCS L1/L2 → KF enterprise sectors and asset classes. See [[taxonomy-hilucs-kf]].

**Strategic Sectors:** Office, Retail, Industrial, Logistics, Data Centres, Life Sciences, Healthcare, Living, PBSA

**HILUCS Gaps:** Data Centres, Life Sciences, BTR, PBSA, Self Storage, Senior Living, Co-Living, Multifamily, Cold Storage — none have explicit HILUCS codes.

## Data Residency & Compliance

| Region | Requirements | Regulatory Body |
| ------ | ------------ | --------------- |
| France | Data in EU, CNIL compliance, SIREN/SIRET registration | CNIL |
| Germany | BDSG compliance, Handelsregister HRB registration | BfDI |
| Spain | GDPR, right-of-refusal on listed buildings, Registro Mercantil | AEPD |
| Poland | GDPR, KRS number registration | UODO |

## Data Quality

| Mechanism | Purpose |
| --------- | ------- |
| Loqate auto-lookup | Address validation and kf_Site creation |
| SIC code validation | Standardised industry classification |
| National registration validation | Cross-reference with company registers |
| Duplicate detection | TBD — to be implemented |
| Master data management | TBD — approach to be defined |

## Data Model Statistics

| Metric | Count |
| ------ | ----- |
| Total tables | 40+ (L2 shells) |
| MVP tables (Phase 0-1) | 22 |
| Future tables (Phase 3-4) | 20 |
| Service lines | 13 |
| Rows in master index | 1,302 |

## Related Documents

- [[client-data-model]] — Client entity schema
- [[property-data-model]] — Property entity schema
- [[capital-markets-data-model]] — Capital Markets entity schema
- [[wip-data-model]] — WIP and Finance integration
- [[taxonomy-mappings]] — SIC and HILUCS mappings
- [[data-model-overview]] — Complete table inventory
- [[data-model-core-tables]] — Layer 2 table definitions
