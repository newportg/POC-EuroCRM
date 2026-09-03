---
status: Draft
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# Power Apps Model-Driven Apps Rationale

## Current Hypothesis

Power Apps model-driven apps on Dataverse are a better fit where the value sits in a custom Knight Frank data model rather than a packaged sales process.

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
