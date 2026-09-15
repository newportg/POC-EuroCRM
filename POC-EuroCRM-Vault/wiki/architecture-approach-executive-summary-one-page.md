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

# Architectural Approaches — One-Page Summary

Four options can deliver the European CRM programme's core outcome — a shared client, contact, property and engagement foundation across service lines and countries (see [[business-capabilities]]). All keep data in EU regions (GDPR, CNIL, BDSG). All four require building a **custom** model: 8 of 11 core entities have no packaged equivalent. The difference is where that custom model lives.

|                     | Option A, Power Platform / Dataverse                  | Option B,  Power Platform + SQL                            | Option C, C# / PostgreSQL                | Option D, Dynamics 365 Sales                                                      |
| ------------------- | ----------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------- |
| **What it is**      | Custom model on Dataverse, Power Apps UI              | Power Apps UI on a relational DB (SQL Server / PostgreSQL) | First-party .NET code on PostgreSQL 16   | Packaged sales CRM on Dataverse, used as-is                                       |
| **Cost**            | Per-user/per-app licensing; grows with adoption       | Power Apps per-user + DB hosting; no Dataverse licence     | Infrastructure only; no per-user licence | Per-user D365 Sales + Dataverse licensing                                         |
| **Build effort**    | Low-code; fastest to first value                      | Medium; DB schema + integration to engineer                | Full engineering cycle; slowest          | Least config, but 8 of 11 core entities still custom                              |
| **Lock-in**         | High,  platform, data, and logic                      | Medium, UI only; data is portable                          | Low, portable first-party code           | High, platform and packaged model                                                 |
| **Skills**          | New Power Platform specialists                        | Mixed: Power Platform + existing DBA/.NET                  | Existing in-house C#/.NET team           | New Dynamics/Power Platform skills                                                |
| **Integration**     | Outlook, SharePoint, Teams, Power BI out of the box   | Partial, some Microsoft integrations need workarounds      | Microsoft integrations rebuilt in code   | Out of the box incl. sales-specific (LinkedIn Sales Navigator, Copilot for Sales) |
| **Control**         | Platform-limited; capacity and governance constraints | Full control of data; UI remains platform-limited          | Full control of stack and schema         | Platform-limited + packaged sales process                                         |
| **Operating model** | Lease the platform                                    | Lease the UI, own the data layer                           | Own the stack                            | Lease the packaged product                                                        |

## Key trade-offs

- **Cost now vs. cost later**, licensing (A, D) and hybrid (B) cost less upfront than engineering (C), but per-seat fees recur.
- **Speed vs. control**, low-code gets to first value fastest (A), a packaged app (D) fastest if the sales lifecycle fits, but a first-party codebase (C) is fully debuggable, testable, and portable.
- **Lock-in**, Microsoft platforms (A, B UI layer, D) trade control and portability for managed capability.
- **Lifecycle fit (D)**, the packaged Lead → Opportunity → Quote → Order → Invoice model does not match KF advisory (pitch → NDA → multi-round bid → due diligence → regulatory gates); the custom entities still need building either way.
- **Integration to the Golden Source**, batch export, Dynamics + ECS bus (A, D), or C# + ECS bus (C) (see [[architecture-patterns-comparison]]); the ECS bus is a shared dependency in all cases.
- **Tenant isolation** — Business Units + security roles (A, D), same model behind a relational schema (B), or PostgreSQL row-level security (C).

## Decision

This is a **business operating-model decision**: buy a managed platform for speed (A), adopt a packaged product if the standard sales lifecycle is acceptable (D), take a middle path that reduces platform cost while keeping the low-code UI (B), or invest in engineering to reuse in-house capability and keep full control (C). The choice should be weighed at TDA review against the cost envelope, delivery timeline, and appetite for long-term platform commitment.

## Related

- [[architecture-approach-executive-summary]] — Full comparison with detailed pluses and minuses
- [[solution-overview]] — Parent document; current (Dataverse) design
- [[csharp-postgresql/alternative-architecture-traditional-csharp]] — Full Option C design
- [[power-platform-dataverse/power-apps-rationale]] — The platform decision Option A is based on; covers D365 Sales fit
- [[architecture-patterns-comparison]] — Integration patterns to Golden Source