# EU CRM Data Model

Status: Draft
Parent: [[solution-overview]]
Source: EU CRM Data Model.xlsx

## Overview

Complete inventory of all data tables with service-line mapping and definitions. The data model is structured in layers following the [[solution-package-model]].

## Master Table Index

1302 rows covering all entities across 13 service lines.

### Service Lines Covered

| Code | Service Line | Layer |
| ---- | ------------ | ----- |
| CM | Capital Markets | Layer 5 – KF_CapitalMarkets_Core |
| Res | Residential (Sales, Lettings, Property Management, Buying Agency) | Layer 5 – KF_Residential_Core |
| OSS | Occupier Strategy & Solutions | Layer 5 – KF_OSS_Core |
| Val | Valuations | Layer 5 – KF_Valuations_Core |
| ESG | ESG Consultancy | Layer 5 – KF_ESG_Core |
| BC | Building Consultancy | Layer 5 – KF_BuildingConsultancy_Core |
| Dev | Development Consultancy | Layer 5 – KF_Development_Core |
| CA | Capital Advisory (Debt & Structured Finance) | Layer 5 – KF_CapitalAdvisory_Core |
| PM | Property Management | Layer 5 – KF_PropertyManagement_Core |
| IA | Investor Advisory | Layer 5 – KF_InvestorAdvisory_Core |
| WC | Workplace Consulting | Layer 5 – KF_Workplace_Core |
| Leasing | Leasing (Commercial Agency) | Layer 5 – KF_Leasing_Core |
| Mkt | Marketing | Cross-cutting |

## Core Shared Tables (Layer 2)

See [[data-model-core-tables]] for detailed schema definitions.

### MVP Tables

| Table | Category | Description |
| ----- | -------- | ----------- |
| Account | CRM Lite | OOB extended — Organisation, brand, legal entity, fund, SPV |
| Contact | CRM Lite | OOB extended — Individual person, always associated to Account |
| kf_Property | CRM Lite | Commercial property record |
| kf_Site | CRM Lite | Physical building or land parcel |
| kf_SICCode | Supporting | SIC code reference table |
| kf_Deal | CM Deep Build | Core deal record with full lifecycle tracking |
| kf_DealProperty | Core Shared | Junction record linking deals to properties |
| kf_Pitch | CM Deep Build | Competitive pitch tracking |
| kf_NDA | CM Deep Build | NDA management |
| kf_Bid | CM Deep Build | Multi-round bid management |
| kf_DDMilestone | CM Deep Build | Due diligence milestone tracking |
| kf_RedFlag | CM Deep Build | Risk and red flag tracking |
| kf_FeeSchedule | CM Deep Build | Fee structure management |
| kf_KYCRecord | CM Deep Build | KYC/AML compliance tracking |
| kf_InvestorProfile | CM Deep Build | Investor preferences and strategy |
| kf_DataRoomAccess | CM Deep Build | Data room access management |
| kf_TransactionReport | CM Deep Build | Auto-generated transaction reports |

## Tables by Activation Phase

| Phase | Tables Activated |
| ----- | ---------------- |
| MVP — Phase 0 | Account, Contact, kf_Property, kf_EnergyRating, kf_GDPRRequest, kf_AuditExport, kf_SICCode |
| MVP — Phase 1 | kf_Deal, kf_DealProperty, kf_Pitch, kf_NDA, kf_Bid, kf_DDMilestone, kf_RedFlag, kf_FeeSchedule, kf_KYCRecord, kf_InvestorProfile, kf_DataRoomAccess, kf_TransactionReport, kf_StageGateRule, kf_IntegrationLog, Lead |
| Future — Phase 3 | kf_Engagement, kf_Lease, kf_ValuationInstruction, kf_ESGAssessment, kf_BuildingSurvey, kf_DevelopmentProject, kf_DebtMandate, kf_PropertyMandate, kf_MaintenanceRequest, kf_InvestorMandate, kf_WorkplaceAssessment, kf_LocationSearch |
| Future — Phase 4 | kf_ResProperty, kf_SalesInstruction, kf_LettingsInstruction, kf_Tenancy, kf_Applicant, kf_Viewing, kf_Offer, kf_BuyingBrief |

## Category Legend

| Category | Description |
| -------- | ----------- |
| CRM Lite | Core shared tables deployed in Phase 0 — foundational entities used across all service lines |
| CM Deep Build | Capital Markets-specific tables with full BPF, Finance integration and complex workflows |
| OSS/Val | Occupier Strategy & Solutions and Valuations service line tables |
| Residential | Residential property services tables including sales, lettings, and property management |
| Compliance | Data governance and compliance tables (GDPR, Audit) — deployed in Phase 0 |
| Supporting | Infrastructure tables (Stage Gate Rules, Integration Logs) supporting process automation |
| Marketing | Marketing and lead generation tables (D365 Customer Insights - Journeys integration) |
| Finance | Finance integration tables for WIP, billing, and revenue recognition |

## Related Documents

- [[data-model-core-tables]] — Detailed schema for Layer 2 tables
- [[solution-package-model]] — Layer architecture (L0-L7)
- [[client-data-model]] — Client entity definitions
- [[property-data-model]] — Property entity definitions
- [[capital-markets-data-model]] — Capital Markets entity definitions
