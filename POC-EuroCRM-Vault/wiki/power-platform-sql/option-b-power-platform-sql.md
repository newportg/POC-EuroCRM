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

# Option B — Power Platform + SQL/PostgreSQL Database

A hybrid approach: the Power Apps model-driven UI remains the front-end, but data is stored in a relational database (SQL Server or PostgreSQL) instead of Dataverse, connected via virtual tables, direct connectors, or a custom API layer.

This option is introduced (at a high level) in the [[architecture-approach-executive-summary]]. A detailed design note covering schema, integration, security, and cost for this option is currently **TBD**.

## Known Trade-offs (from the executive summary)

**Pluses:**
- No Dataverse data licensing — eliminates per-entity / per-user data storage cost while keeping the Power Apps UI
- Data portability — the relational database is fully portable and under the firm's control
- Reuses existing DBA skills for schema, indexing, and performance
- Lower platform cost than Option A — Power Apps per-user licensing only
- Faster UI than Option C — model-driven apps and forms ship without a full code build

**Minuses:**
- Hybrid complexity — two platforms to integrate: Power Platform UI layer + a separate database with its own hosting, backup, and DR
- Feature gaps — virtual tables and direct connectors do not support all Dataverse features (Business Process Flows, certain rollups, native audit, complex calculated fields may require workarounds)
- Power Automate limitations — Dataverse-specific triggers and actions do not fire against a SQL backend; flows must use SQL polling or custom connectors
- Mixed skill requirement — Power Platform capability plus database/integration engineering
- Partial lock-in — the UI layer remains Microsoft-owned; the data layer does not

## Open Questions for TDA

- Which relational engine — SQL Server or PostgreSQL — and who operates it (managed PaaS vs. existing DBA team)?
- Which connectivity approach — Dataverse virtual tables, direct connectors, or a custom API layer — is acceptable given the feature gaps?
- How do the 9-flow Finance bridge and ECS change notification map onto a SQL backend (SQL triggers/change data capture vs. Outbox pattern)?
- How are the Business Unit / security-role country and service-line isolations reproduced in the relational schema (row-level security)?

## Related

- [[architecture-approach-executive-summary]] — Three-way option comparison (parent decision material)
- [[solution-overview]] — Parent document; current (Dataverse) design