---
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# Power Apps Model-Driven Apps Rationale

This note underpins **Option B — Model-driven application on Dataverse**. It captures the original hypothesis (from the European CRM Architecture Review) that the value sits in a custom Knight Frank data model rather than a packaged sales process, together with the entity-fit assessment that the [[architecture-approach-executive-summary-one-page|validation stage]] must now test against Option A (extend Dynamics 365 Sales).

## Current Hypothesis

Power Apps model-driven apps on Dataverse are a better fit where the value sits in a custom Knight Frank data model rather than a packaged sales process. The validation stage must measure whether packaged Dynamics 365 Sales capability can be retained in sufficient measure to justify its licence cost (see the one-page summary's justification for Option A: "We should not reject Dynamics 365 Sales only because some advisory tables are custom").

## Where D365 Sales May Be a Poor Fit

- Packaged CRM assumes a lifecycle that differs from KF advisory
- D365 Sales entity fit — 11 core KF entities
- Unwanted features bundled in D365 Sales
- D365 model: Lead → Opportunity → Quote → Order → Invoice
- KF lifecycle (Capital Markets): Competitive pitching; NDA issuance; Multi-round bidding; Due diligence with milestone tracking; Regulatory gates per jurisdiction
- Product Catalogue; LinkedIn Sales Navigator

### Entity Fit Assessment

| Entity | D365 OOB Fit |
| ------ | ------------ |
| Opportunity, Quote, Product/Price List | Poor fit (3) |
| kf_Pitch, kf_NDA, kf_Bid, kf_DDMilestone, kf_RedFlag, kf_InvestorProfile, kf_DataRoomAccess, kf_KYCRecord | No equivalent (8) |

## What Dataverse Provides Natively

Core platform capabilities (to validate):
- Custom tables with relationships
- Business Process Flows (BPFs)
- Security roles + Business Units
- Power Automate
- Power BI
- Outlook / Teams integration
- SharePoint document management
- Dataverse audit trail
- API access (OData + custom)
- Mobile access
