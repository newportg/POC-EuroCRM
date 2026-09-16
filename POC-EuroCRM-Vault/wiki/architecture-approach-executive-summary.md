---
parent:"[[solution-overview]]"
status: Draft
author: Gary Newport
date: 15/09/2026
tags:
  - executive
  - architecture
  - decisions
  - tda
  - board
---

# Architectural Approach Comparison — Executive Summary

> One-page version (recommended position and Board ask): [[architecture-approach-executive-summary-one-page]]

This document proposes three architectural approaches for the European CRM programme. All three deliver the same core outcome — a shared client, contact, property and engagement foundation across service lines and countries (see [[business-capabilities]]) — but with different cost, risk, and operating profiles.

The three options are:

- **Option A — Extend Dynamics 365 Sales**: adopt the packaged SaaS CRM and add Knight Frank domain extensions.
- **Option B — Model-driven application on Dataverse**: build a bespoke CRM application with Power Apps and Dataverse, without the packaged sales application.
- **Option C — Knight Frank-built application**: design, build and operate a custom CRM product and data platform on the enterprise engineering stack.

The choice is a business operating-model decision with its own cost envelope, delivery timeline and appetite for long-term platform commitment. The recommended position — Option A as baseline, Option B as main comparator, Option C retained only where strategic requirements justify full ownership — is set out in the [[architecture-approach-executive-summary-one-page|one-page summary]] for Board decision.

## The choice at a glance

| | Option A — Extend Dynamics 365 Sales | Option B — Model-driven app on Dataverse | Option C — Knight Frank-built application |
| --- | ------------------------------------- | ---------------------------------------- | ----------------------------------------- |
| **What it is** | Packaged Microsoft sales CRM (D365 Sales) on Dataverse, extended with Knight Frank domain tables | Build a separate CRM application with Power Apps on Dataverse; no packaged sales app | Build a custom CRM product and data platform (e.g. existing C# / PostgreSQL stack) |
| **Cost profile** | Ongoing per-user D365 Sales + Dataverse licensing | Power Apps per-user + Dataverse capacity licensing | Infrastructure and engineering cost; no per-user platform licence |
| **Build effort** | Least config effort, but 8 of 11 core entities have no packaged equivalent | Low-code configuration of the custom model | Full build/test/deploy cycle |
| **Vendor lock-in** | High — Microsoft platform and packaged model | High — Microsoft platform | Low — first-party, portable code |
| **Using existing skills** | New Dynamics/Power Platform skill set | New Power Platform skill set | Existing C# / .NET / database team |
| **Compliance posture** | EU data centres, platform-managed | EU data centres, platform-managed | EU data centres, fully self-controlled |

All three options keep all data in EU regions to satisfy GDPR, CNIL, and BDSG.

## Option A — Extend Dynamics 365 Sales

Use Dynamics 365 Sales as the CRM and relationship management application, retaining packaged account, contact, lead and activity capabilities where they meet the requirements, and adding Knight Frank domain extensions (property, instruction, deal, bid, NDA, KYC, due diligence, reference data).

**Pluses:**
- **Packaged capability** — Microsoft supplies and supports the standard application, entities and CRM capabilities; Knight Frank configures, extends and integrates rather than building application behaviour
- **Native integrations out of the box** — Outlook, SharePoint, Teams, Power BI, and an audit trail ship with the product
- **Managed platform** — security, infrastructure, and capacity are Microsoft's responsibility
- **Product-specific Copilot** — Dynamics 365 Sales provides Copilot capabilities for sales records (record summaries, recent changes, meeting preparation)
- **Supported roadmap** — Microsoft develops the Sales agent across Dynamics 365 Sales, Outlook, Teams and other Microsoft 365 applications

**Minuses:**
- **Licence cost can exceed value** — if users make little use of the packaged capabilities
- **Lifecycle mismatch** — the KF advisory lifecycle (pitch → NDA → multi-round bid → due diligence → regulatory gates) does not match the packaged sales pipeline
- **Fit gap remains** — 8 of 11 core entities have no packaged equivalent and must be custom-built on Dataverse anyway
- **Unwanted features** — packaged capabilities (product catalogue, transactional quotes) are bundled regardless of need
- **Vendor lock-in + roadmap** — Microsoft controls the release schedule; Knight Frank must assess changes and maintain compatibility with extensions
- **New skill set** — Dynamics specialists, not the existing .NET team

## Option B — Model-driven application on Dataverse

Build a separate Knight Frank CRM application with Power Apps and Dataverse, designed around Knight Frank's own terminology, navigation and advisory processes. No packaged Dynamics 365 Sales application.

**Pluses:**
- **Custom by design** — the application is built around the specialist property, instruction, deal and taxonomy model rather than a packaged sales process
- **Platform services retained** — security, audit, data management and application services ship with Dataverse
- **Faster than a code build** — tables, forms, views and processes are configured on a common platform
- **Regional rollout** — Business Units + security roles map cleanly onto the country / service-line model

**Minuses:**
- **Knight Frank owns the CRM application** — navigation, forms, views, processes and application behaviour, including design, testing, release and support responsibilities
- **Fit gap applies here too** — the custom model must be built in full; no packaged capability offsets it
- **Licensing** — Power Apps per-user plus Dataverse capacity, automation, platform governance and support dependencies
- **Platform constraints** — capacity and governance limits on what can be built, tuned, and debugged; service protection limits require retry discipline
- **New skill set** — Power Platform specialists, not the existing .NET team

## Option C — Knight Frank-built application

A custom CRM product and data platform built with the enterprise engineering stack (existing C# / .NET and PostgreSQL capability), detailed in [[csharp-postgresql/alternative-architecture-traditional-csharp]].

**Pluses:**
- **Full control** — user experience, domain behaviour, data architecture, release strategy and release pace are Knight Frank's
- **No per-user platform licensing** — infrastructure cost only; cheaper at scale
- **Reuses existing capability** — the current C#/.NET and database engineering team runs it
- **Precise tenant isolation** — row-level security gives exact country/service-line control
- **No platform limits** — schema, security model, and change capture are entirely under Knight Frank's control

**Minuses:**
- **Complete application lifecycle** — product management, architecture, engineering, testing, security, deployment, monitoring, support and continual improvement
- **Build the freebies** — Outlook/SharePoint/Teams integration, audit and security must be built, integrated or omitted rather than switched on
- **Operate the infrastructure** — provision, secure, and run servers/storage rather than leasing a platform
- **Largest engineering and operational capability** — skills must be retained for as long as the application remains in use
- **Longer build** — real development effort, not low-code configuration

## The key tension

- Platform licensing cost vs. build and operating effort.
- Velocity of low-code change vs. the discipline of a first-party codebase.
- Buying a managed capability vs. owning the full stack.
- The eight-entity fit gap applies to all three options — the question is whether the custom model is built **on Dataverse under a packaged sales app** (A), **on Dataverse as a bespoke app** (B), or **as first-party code** (C).

## Commercial / integration angle

Integration to the Golden Source varies by option, and three patterns exist for getting entity data there (compared in [[architecture-patterns-comparison]]):

- **Direct batch export** — simplest, near-daily freshness
- **Dynamics/Dataverse + ECS message bus** — near-real-time, decouples consumers; applies to Options A and B (Dataverse-based)
- **C# + ECS message bus** — the native fit for a code-built application; Outbox Pattern guarantees delivery

None of the options eliminate the need for the enterprise ECS bus — they change who publishes to it (a platform plugin, a packaged-app plugin, or a background worker). This is a shared dependency either way and should be confirmed early.

## Recommended position

- Fund a defined **validation stage**.
- Use **Option A, extending Dynamics 365 Sales, as the baseline**. Compare it with **Option B, a separate model-driven application on Dataverse**.
- Retain **Option C, a Knight Frank-built application**, only where strategic, scale, performance or integration requirements justify full product ownership (unlikely in this case).

The validation stage must produce: a fit assessment with Dynamics 365 Sales, a total cost of ownership model, an integration requirements assessment, and a validation test of one representative end-to-end scenario.

## Related

- [[architecture-approach-executive-summary-one-page]] — One-page summary with the Board recommendation
- [[solution-overview]] — Parent document
- [[dynamics-365-sales/option-a-dynamics-365-sales]] — Option A detail (recommended baseline)
- [[power-platform-dataverse/power-apps-rationale]] — Dataverse platform rationale underlying Option B
- [[csharp-postgresql/alternative-architecture-traditional-csharp]] — Full Option C design with cost/operability detail
- [[business-capabilities]] — The capability model all three options must satisfy
- [[architecture-patterns-comparison]] — Integration to Golden Source, shared by all options