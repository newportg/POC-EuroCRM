---
status: Draft
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# Solution Package Model — Layered Architecture

## Layer Model

| Layer | Name | Description |
| ----- | ---- | ----------- |
| L0 | External Systems | D365 CI-Journeys (same env); Finance (future); ECS — change notification bus (Major entity events) |
| L1 | Dataverse Platform | System tables; security framework; audit log (Microsoft-managed) |
| L2 | KF_Core | 40+ table shells; option sets; BU hierarchy; base security; Outlook sync; SharePoint; BI |
| L3 | Region | KF_Europe — EUR default, GDPR baseline, Regional Power BI Dashboard |
| L4 | Country | KF_France; KF_Germany; KF_Poland; KF_Spain |
| L5 | Service Line Core | KF_CapitalMarkets_Core (8-stage BPF); KF_OSS_Core; KF_Valuations_Core (future); KF_Marketing_Core; KF_Finance_Integration |
| L6 | Service Line — Country | KF_CM_France; KF_CM_Spain; KF_OSS_France; ... |
| L7 | Cross-Border Overlays | KF_EIT; KF_Private_Office |

## Proposed Technical Rules

- KF_Core Layer defines ALL Option sets & ALL custom tables as base — schema name, primary key, and ownership model
- No regional fork can create a duplicate table
- Each layer is a separate managed solution
- No unmanaged customisations in TEST, UAT, or PROD

## Layer 6 Extension Rules

- Inherits the Service Line Core Layer BPF
- Adds country-specific columns with prefixes: `kf_fr_` (France); `kf_es_` (Spain)
- Adds regulatory stage gates that block BPF progression
- Provides country-specific form layouts and option set visibility rules
- NEVER renames or removes standard stages — only ADDs within them
- Adding a country = new L4 + L6 solutions | Adding a service line = new L5 solution
- Columns and relationships added by higher layers
