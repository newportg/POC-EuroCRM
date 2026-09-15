---
parent:"[[solution-overview]]"
status: Draft
author: Gary Newport
date: 15/09/2026
tags:
  - architecture
  - decisions
  - tda
---

# Option D — Dynamics 365 Sales

The packaged Microsoft sales CRM, run on Dataverse as-is rather than building a custom model. The standard sales lifecycle (Lead → Opportunity → Quote → Order → Invoice) applies directly.

This option is introduced (at a high level) in the [[architecture-approach-executive-summary]]. Detail is currently captured in the fit assessment within [[power-platform-dataverse/power-apps-rationale]]; a full design note is **TBD** if this option is pursued.

## Known Trade-offs (from the executive summary)

**Pluses:**
- Packaged sales process — Lead → Opportunity → Quote → Order → Invoice works out of the box with zero build
- Mature sales features — pipeline management, product catalogue, LinkedIn Sales Navigator, Copilot for Sales
- Native integrations — Outlook, SharePoint, Teams, Power BI, audit trail ship with the product
- Managed platform — security, infrastructure, and capacity are Microsoft's responsibility

**Minuses:**
- Lifecycle mismatch — the KF advisory lifecycle (pitch → NDA → multi-round bid → due diligence → regulatory gates) does not match the packaged sales pipeline
- Fit gap remains — 8 of 11 core entities (kf_Pitch, kf_NDA, kf_Bid, kf_DDMilestone, kf_RedFlag, kf_InvestorProfile, kf_DataRoomAccess, kf_KYCRecord) have no packaged equivalent; they must be custom-built on Dataverse anyway
- Unwanted features — packaged capabilities (product catalogue, transactional quotes) are bundled regardless of need
- Ongoing licensing cost — per-user D365 Sales licenses on top of Dataverse
- Vendor lock-in — data, model, and process sit on Microsoft's platform

## Open Questions for TDA

- Is the standard sales lifecycle acceptable for any service line, or is the lifecycle mismatch a blocker?
- Do the 8 custom entities change the value proposition enough that a custom app (Option A) dominates this option on the same platform?
- How does D365 Sales licensing compare against Power Apps per-user for the intended user base?

## Related

- [[architecture-approach-executive-summary]] — Four-way option comparison (parent decision material)
- [[power-platform-dataverse/power-apps-rationale]] — Entity fit assessment (D365 Sales vs. custom model)
- [[solution-overview]] — Parent document; current (Dataverse) design