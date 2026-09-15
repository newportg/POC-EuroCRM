---
parent:"[[solution-overview]]"
status: Index
author: Gary Newport
date: 15/09/2026
---

# EuroCRM Wiki Index

The master index for the European CRM solution wiki. The wiki is split between **general business material** (business case, scope, requirements, governance, roadmap, and the shared data models) at the top level, and **three architecture-implementation sub-folders** — one per approach proposed in the [[architecture-approach-executive-summary]].

- `wiki/power-platform-dataverse/` — Option A: Power Platform / Dataverse (the current design)
- `wiki/power-platform-sql/` — Option B: Power Platform + SQL/PostgreSQL database (hybrid)
- `wiki/csharp-postgresql/` — Option C: Traditional C# / PostgreSQL (alternative)
- `wiki/dynamics-365-sales/` — Option D: Packaged Dynamics 365 Sales (considered, detailed design TBD)

The authoritative parent document is [[solution-overview]]; this index is the navigation surface for that body of work.

## Overview & Entry

| Note | Purpose |
| ---- | ------- |
| [[solution-overview]] | Parent / authoritative Solution Overview Document (SOD) |
| [[problem-statement]] | Why the initiative exists — the business problem |
| [[business-context]] | Background across the four European offices |
| [[glossary]] | Definition of terms |

## Business Case

| Note | Purpose |
| ---- | ------- |
| [[business-goals]] | Goals and objectives |
| [[business-capabilities]] | Capability model the solution must satisfy |
| [[expected-benefits]] | Benefits realisation for the business case |
| [[key-stakeholders]] | Stakeholder register |
| [[kpis-and-success]] | Measurable success criteria and KPIs |

## Scope

| Note | Purpose |
| ---- | ------- |
| [[solution-scope-in-scope]] | What is in scope |
| [[solution-scope-out-of-scope]] | What is explicitly out of scope |
| [[crm-lite-mvp-scope]] | CRM Lite MVP scope definition |
| [[implementation-phases]] | The full implementation phases |

## Requirements

| Note | Purpose |
| ---- | ------- |
| [[functional-requirements]] | Functional requirements |
| [[functional-non-functional-requirements]] | Non-functional requirements |
| [[dependencies-and-constraints]] | Dependencies and constraints |
| [[risks-and-issues]] | Risk register and issues log |

## Business Architecture

| Note | Purpose |
| ---- | ------- |
| [[architecture-business]] | Business architecture — shared foundation and service-line builds |

## Shared Data Model

| Note | Purpose |
| ---- | ------- |
| [[data-model-overview]] | EU CRM data model overview |
| [[data-model-core-tables]] | Core data model tables |
| [[client-data-model]] | Client — one client, one view |
| [[property-data-model]] | Property — site, property, deal |
| [[capital-markets-data-model]] | Capital Markets deal lifecycle (8-stage) |
| [[wip-data-model]] | Work in progress and revenue tracking |
| [[taxonomy-mappings]] | Taxonomy mappings overview |
| [[taxonomy-sic-kf]] | SIC to KF client sector mapping |
| [[taxonomy-hilucs-kf]] | HILUCS to KF asset class mapping |

## Architecture Approaches

### Option A — Power Platform / Dataverse

The current design, detailed in `wiki/power-platform-dataverse/`.

| Note | Purpose |
| ---- | ------- |
| [[power-platform-dataverse/architecture-overview-diagrams]] | High-level architecture diagrams |
| [[power-platform-dataverse/architecture-key-components]] | Component inventory |
| [[power-platform-dataverse/solution-package-model]] | L0–L7 layered package model |
| [[power-platform-dataverse/architecture-application]] | Application architecture and integrations |
| [[power-platform-dataverse/architecture-data]] | Data architecture overview |
| [[power-platform-dataverse/architecture-technology]] | Technology, hosting, and security |
| [[power-platform-dataverse/architecture-target-state]] | Target state alignment to standards/PADs |
| [[power-platform-dataverse/architecture-principles-compliance]] | Mapping to CTO architecture principles |
| [[power-platform-dataverse/power-apps-rationale]] | Platform decision — Power Apps / Dataverse rationale |
| [[power-platform-dataverse/outlook-email-interception-engagement-history]] | Outlook email interception → engagement history |

### Option B — Power Platform + SQL Database

Hybrid approach, tracked in `wiki/power-platform-sql/`.

| Note | Purpose |
| ---- | ------- |
| [[power-platform-sql/option-b-power-platform-sql]] | Option B overview and open questions (detailed design TBD) |

### Option C — C# / PostgreSQL

Alternative stack, detailed in `wiki/csharp-postgresql/`.

| Note | Purpose |
| ---- | ------- |
| [[csharp-postgresql/alternative-architecture-traditional-csharp]] | Full Option C design with cost/operability detail |

### Option D — Dynamics 365 Sales

Packaged product, tracked in `wiki/dynamics-365-sales/`.

| Note | Purpose |
| ---- | ------- |
| [[dynamics-365-sales/option-d-dynamics-365-sales]] | Option D overview, trade-offs, and open questions (detailed design TBD) |

## Approach & Decision Material

| Note | Purpose |
| ---- | ------- |
| [[architecture-approach-executive-summary]] | Plus/minus of the four architectural approaches without preference |
| [[architecture-approach-executive-summary-one-page]] | One-page A4 summary of the four approaches for decision review |
| [[architecture-patterns-comparison]] | Integration patterns to Golden Source |
| [[solution-options]] | Solution options and trade-offs analysis |

## Compliance & Governance

| Note | Purpose |
| ---- | ------- |
| [[compliance]] | Regulatory and compliance requirements |
| [[governance-approval]] | Approval workflow |
| [[governance-oversight]] | Governance structure (TDA oversight) |

## Implementation Roadmap

| Note | Purpose |
| ---- | ------- |
| [[roadmap-phases]] | Roadmap phases |
| [[roadmap-timelines]] | Roadmap timelines |
| [[roadmap-dependencies]] | Roadmap key dependencies |

## Cost & Benefits

| Note | Purpose |
| ---- | ------- |
| [[cost-estimates]] | Cost modelling |

> [[expected-benefits]] (covered under Business Case above) quantifies the benefits against the [[cost-estimates]].

This index follows the wiki structure defined in the repository's `AGENTS.md`: one topic per file, kebab-case filenames, and `parent:` frontmatter pointing back to [[solution-overview]] (or to a grouping note such as [[data-model-overview]] or [[taxonomy-mappings]]). When a new wiki note is added, it should be linked under the matching heading above.