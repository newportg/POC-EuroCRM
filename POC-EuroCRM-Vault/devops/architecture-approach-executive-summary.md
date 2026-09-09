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

A one-page read for a C-level audience to weigh the two architectural approaches for the European CRM programme. Both deliver the same core outcome — a shared client, contact, property and engagement foundation across service lines and countries (see [[business-capabilities]]) — but with very different cost, risk, and operating profiles.

The two options are the current **Microsoft Power Platform / Dataverse** design and the alternative **traditional C# / PostgreSQL** stack.

## The choice at a glance

| | Option A — Power Platform / Dataverse | Option B — C# / PostgreSQL |
| --- | ------------------------------------- | -------------------------- |
| **What it is** | Build the custom CRM model on Microsoft's low-code platform (Dataverse + Power Apps) | Build the same custom model as first-party code on the firm's existing .NET stack and PostgreSQL |
| **Cost profile** | Ongoing per-user / per-app licensing | Infrastructure cost only; no per-user platform license |
| **Build effort** | Lower-code, faster to stand up | Full build/test/deploy cycle |
| **Vendor lock-in** | High — Microsoft platform | Low — first-party, portable code |
| **Using existing skills** | New Power Platform skill set | Existing in-house C# / .NET / database team |
| **Compliance posture** | EU data centres, platform-managed | EU data centres, fully self-controlled |

Both options keep all data in EU regions to satisfy GDPR, CNIL, and BDSG.

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

## Option B — Traditional C# / PostgreSQL

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

## The key tension

- Platform licensing cost **now** vs. build and operating effort **now**.
- Velocity of low-code change **vs.** the discipline of a first-party codebase.
- Buying a managed capability **vs.** owning the full stack ourselves.

The eight-entity fit gap that argues for a *custom* model applies to both options — the real question is whether that custom model is built **on** Dataverse or as **our own code**.

## Commercial / integration angle

For the C-suite, the integration future also matters. Three patterns exist for getting entity data to the Golden Source (compared in [[architecture-patterns-comparison]]):

- **Direct batch export** — simplest, near-daily freshness
- **Dynamics + ECS message bus** — near-real-time, decouples consumers
- **C# + ECS message bus** — the native fit for Option B; Outbox Pattern guarantees delivery

Option B does not eliminate the need for the enterprise ECS bus — it changes who publishes to it (a background worker instead of a platform plugin). This is a shared dependency either way and should be confirmed early (see the [[alternative-architecture-traditional-csharp|open questions]]).

## Comparison table

| Dimension | Option A — Power Platform | Option B — C# / PostgreSQL |
| --------- | ------------------------- | -------------------------- |
| Core outcome | Same | Same |
| Time to first value | Faster | Slower |
| Recurring cost | Per-user / per-app licenses | Infrastructure only |
| Upfront effort | Low-code config | Full engineering |
| Skill availability | New Microsoft skills | Existing in-house team |
| Vendor lock-in | High | Low |
| Data residency | EU (platform-allocated) | EU (self-controlled) |
| Control & debuggability | Platform-limited | Full |
| Native Microsoft integrations | Out of the box | Rebuilt |
| Operating model | Lease the platform | Own the stack |

## Recommendation framing

This is a **business operating-model decision**, not purely technical. It comes down to:

- **Do we prefer to buy a managed platform** (Option A) for speed and lower current spend on people, accepting licence cost and lock-in?
- **Or invest engineering effort** (Option B) to reuse what we already have, eliminate per-seat licensing, and keep full control?

The decision should be made at TDA review weighing these pluses and minuses against the programme's cost envelope, delivery timeline, and appetite for long-term platform commitment.

## Related

- [[solution-overview]] — Parent document; current (Dataverse) design
- [[alternative-architecture-traditional-csharp]] — Full Option B design with cost/operability detail
- [[power-apps-rationale]] — The platform decision Option A is based on
- [[business-capabilities]] — The capability model both options must satisfy
- [[architecture-patterns-comparison]] — Integration to Golden Source, shared by both options
