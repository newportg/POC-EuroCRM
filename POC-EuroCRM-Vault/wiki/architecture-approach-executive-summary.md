---
parent:"[[solution-overview]]"
status: Draft
author: Gary Newport
date: 09/09/2026
tags:
  - executive
  - architecture
  - decisions
  - tda
  - board
---

# Architectural Approach Comparison — Executive Summary

> One-page version: [[architecture-approach-executive-summary-one-page]]

This document proposes four architectural approaches for the European CRM programme. All four deliver the same core outcome — a shared client, contact, property and engagement foundation across service lines and countries (see [[business-capabilities]]) — but with different cost, risk, and operating profiles. The pluses and minuses of each are set out below without preference; the choice is a business decision to be weighed by the programme stakeholders.

The four options are the current **Microsoft Power Platform / Dataverse** design, a hybrid **Power Platform with a SQL/PostgreSQL relational database**, the alternative **traditional C# / PostgreSQL** stack, and the packaged **Dynamics 365 Sales** application.

## The choice at a glance

| | Option A — Power Platform / Dataverse | Option B — Power Platform + SQL Database | Option C — C# / PostgreSQL | Option D — Dynamics 365 Sales |
| --- | ------------------------------------- | --------------------------------------- | -------------------------- | ----------------------------- |
| **What it is** | Build the custom CRM model on Microsoft's low-code platform (Dataverse + Power Apps) | Build the UI on Power Apps but store data in a relational database (SQL Server or PostgreSQL) via virtual tables or direct connectors | Build the same custom model as first-party code on the firm's existing .NET stack and PostgreSQL | Use the packaged Microsoft sales CRM (D365 Sales) on Dataverse as-is |
| **Cost profile** | Ongoing per-user / per-app licensing for Dataverse + Power Platform | No Dataverse data licensing; database hosting cost + Power Apps per-user for UI only | Infrastructure cost only; no per-user platform license | Ongoing per-user D365 Sales + Dataverse licensing |
| **Build effort** | Lower-code, faster to stand up | Medium — UI is low-code, database schema and integration layer require engineering | Full build/test/deploy cycle | Least config effort, but 8 of 11 core entities have no packaged equivalent |
| **Vendor lock-in** | High — Microsoft platform | Medium — Power Apps UI layer is Microsoft-owned, but data is portable | Low — first-party, portable code | High — Microsoft platform and packaged model |
| **Using existing skills** | New Power Platform skill set | Mixed — Power Platform for UI, existing DBA/.NET for database and integration | Existing in-house C# / .NET / database team | New Dynamics/Power Platform skill set |
| **Compliance posture** | EU data centres, platform-managed | EU database hosting, self-controlled data; platform layer Microsoft-managed | EU data centres, fully self-controlled | EU data centres, platform-managed |

All four options keep all data in EU regions to satisfy GDPR, CNIL, and BDSG.

## Option A — Microsoft Power Platform / Dataverse

The current design. The custom EuroCRM data model is built on Dataverse with Power Apps model-driven apps, Business Process Flows, Power Automate, and native Microsoft integrations.

**Pluses:**
- **Speed to value** — low-code configuration gets simple forms, workflows and a usable UI up much faster
- **Native integrations out of the box** — Outlook, SharePoint, Teams, Power BI, and an audit trail ship with the platform
- **Managed platform** — security, infrastructure, and capacity are Microsoft's responsibility
- **Mature ecosystem** — Copilot for Sales, Power BI analytics, broad Microsoft 365 alignment
- **Regional rollout** — Business Units + security roles map cleanly onto the country / service-line model

**Minuses:**
- **Ongoing licensing cost** — per-user / per-app / per-org fees that grow with adoption
- **Vendor lock-in** — data and logic sit on Microsoft's platform
- **New skill set** — Power Platform specialists, not the existing .NET team
- **Fit gap** — 8 of 11 core entities have no packaged equivalent, so a large part of the model is custom regardless
- **Platform constraints** — capacity and governance limits on what can be built, tuned, and debugged

## Option B — Power Platform + SQL/PostgreSQL Database

A hybrid approach: the Power Apps model-driven UI remains the front-end, but data is stored in a relational database (SQL Server or PostgreSQL) instead of Dataverse, connected via virtual tables, direct connectors, or a custom API layer.

**Pluses:**
- **No Dataverse data licensing** — eliminates the per-entity / per-user data storage cost while keeping the Power Apps UI
- **Data portability** — the relational database is fully portable and under the firm's control
- **Reuse existing DBA skills** — the database team manages schema, indexing, and performance directly
- **Lower platform cost than Option A** — Power Apps per-user licensing only; no Dataverse tier charges
- **Faster UI than Option C** — model-driven apps and forms ship without a full code build

**Minuses:**
- **Hybrid complexity** — two platforms to integrate: Power Platform UI layer + a separate database with its own hosting, backup, and DR
- **Feature gaps** — virtual tables and direct connectors do not support all Dataverse features (Business Process Flows, certain rollups, native audit, complex calculated fields may require workarounds)
- **Power Automate limitations** — Dataverse-specific triggers and actions do not fire against a SQL backend; flows must use SQL polling or custom connectors instead
- **Mixed skill requirement** — the team needs both Power Platform capability and database/integration engineering
- **Partial lock-in** — the UI layer remains Microsoft-owned; the data layer does not

## Option C — Traditional C# / PostgreSQL

An alternative to the same outcome using the firm's existing engineering stack — ASP.NET Core, PostgreSQL 16, and standard integration practices.

**Pluses:**
- **No per-user licensing** — infrastructure cost only; cheaper at scale
- **Reuses existing capability** — the current C#/.NET and database engineering team runs it
- **Full control and portability** — first-party code is debuggable, testable, and portable off the chosen host
- **Precise tenant isolation** — PostgreSQL row-level security gives exact country/service-line control
- **No platform limits** — schema, security model, and change capture are entirely under our control

**Minuses:**
- **Longer build** — real development effort, not low-code configuration
- **Rebuild the freebies** — Outlook/SharePoint/Teams integration and audit trail must be built rather than switched on
- **Operate the infrastructure** — provision, secure, and run servers/storage rather than leasing a platform
- **Selling the build** — the effort is a capital project to justify, not a per-seat subscription to buy

## Option D — Dynamics 365 Sales

The packaged Microsoft sales CRM, run on Dataverse as-is rather than building a custom model. The standard sales lifecycle applies directly.

**Pluses:**
- **Packaged sales process** — Lead → Opportunity → Quote → Order → Invoice works out of the box with zero build
- **Mature sales features** — pipeline management, product catalogue, LinkedIn Sales Navigator, Copilot for Sales
- **Native integrations** — Outlook, SharePoint, Teams, Power BI, audit trail ship with the product
- **Managed platform** — security, infrastructure, and capacity are Microsoft's responsibility
- **Fastest to a working system** — no model to build if the packaged process is acceptable

**Minuses:**
- **Lifecycle mismatch** — the KF advisory lifecycle (pitch → NDA → multi-round bid → due diligence → regulatory gates) does not match Lead → Opportunity → Quote → Order → Invoice
- **Fit gap remains** — 8 of 11 core entities (kf_Pitch, kf_NDA, kf_Bid, kf_DDMilestone, kf_RedFlag, kf_InvestorProfile, kf_DataRoomAccess, kf_KYCRecord) have no packaged equivalent; they must be custom-built on Dataverse anyway
- **Unwanted features** — packaged capabilities (product catalogue, transactional quotes) are bundled regardless of need
- **Ongoing licensing cost** — per-user D365 Sales licenses on top of Dataverse
- **Vendor lock-in** — data, model, and process sit on Microsoft's platform
- **New skill set** — Dynamics specialists, not the existing .NET team

## The key tension

- Platform licensing cost vs. build and operating effort.
- Velocity of low-code change vs. the discipline of a first-party codebase.
- Buying a managed capability vs. owning the full stack.
- Option B sits between the two: it avoids Dataverse data licensing but requires running two platforms and working around feature limits.
- Option D buys a packaged process but must still custom-build most of the core model on the same Dataverse platform.

The eight-entity fit gap that argues for a *custom* model applies to all four options — the real question is whether that custom model is built **on** Dataverse with a bespoke app (A), on a **relational database behind Power Apps** (B), as **our own code** (C), or **on Dataverse but under a packaged sales app** (D), which still leaves most entities custom.

## Commercial / integration angle

Integration to the Golden Source also varies by option, and three patterns exist for getting entity data there (compared in [[architecture-patterns-comparison]]):

- **Direct batch export** — simplest, near-daily freshness
- **Dynamics + ECS message bus** — near-real-time, decouples consumers; applies to A and D (Dataverse-based)
- **C# + ECS message bus** — the native fit for Option C; Outbox Pattern guarantees delivery

None of the options eliminate the need for the enterprise ECS bus — they change who publishes to it (a platform plugin, a packaged-app plugin, or a background worker). This is a shared dependency either way and should be confirmed early (see the [[csharp-postgresql/alternative-architecture-traditional-csharp|open questions]]).

## Comparison table

| Dimension | Option A — Power Platform | Option B — Power Platform + SQL | Option C — C# / PostgreSQL | Option D — Dynamics 365 Sales |
| --------- | ------------------------- | ------------------------------- | -------------------------- | ----------------------------- |
| Core outcome | Same | Same | Same | Same |
| Time to first value | Fastest (custom model) | Medium | Slowest | Fastest if packaged process fits; custom entities still needed |
| Recurring cost | Per-user / per-app licenses + Dataverse | Power Apps per-user + database hosting | Infrastructure only | Per-user D365 Sales + Dataverse |
| Upfront effort | Low-code config | UI config + DB schema & integration | Full engineering | Config of packaged app + custom entities |
| Skill availability | New Microsoft skills | Mixed: Power Platform + existing DBA | Existing in-house team | New Dynamics/Power Platform skills |
| Vendor lock-in | High | Medium | Low | High |
| Data residency | EU (platform-allocated) | EU (self-controlled DB, platform layer MS) | EU (self-controlled) | EU (platform-allocated) |
| Control & debuggability | Platform-limited | Partial — DB full, UI platform-limited | Full | Platform-limited + packaged process |
| Native Microsoft integrations | Out of the box | Partial — some require workarounds | Rebuilt | Out of the box incl. sales-specific |
| Operating model | Lease the platform | Lease UI, own data layer | Own the stack | Lease the packaged product |

## Decision framing

This is a **business operating-model decision**, not purely technical. It comes down to:

- **Buy a managed platform** (Option A) for speed and lower current spend on people, accepting licence cost and lock-in.
- **Take the middle path** (Option B) — keeping the Power Apps UI but moving data to a relational database the firm controls, accepting hybrid complexity and feature gaps in exchange for lower platform cost and data portability.
- **Invest engineering effort** (Option C) to reuse existing capability, eliminate per-seat licensing, and keep full control.
- **Adopt the packaged product** (Option D) if the standard sales lifecycle is acceptable — but the 8-entity fit gap means most of the core model would still be custom-built on the same Dataverse platform.

The decision should be made at TDA review weighing these pluses and minuses against the programme's cost envelope, delivery timeline, and appetite for long-term platform commitment.

## Related

- [[solution-overview]] — Parent document; current (Dataverse) design
- [[csharp-postgresql/alternative-architecture-traditional-csharp]] — Full Option C design with cost/operability detail
- [[power-platform-dataverse/power-apps-rationale]] — The platform decision Option A is based on; covers D365 Sales fit
- [[business-capabilities]] — The capability model all four options must satisfy
- [[architecture-patterns-comparison]] — Integration to Golden Source, shared by all options
