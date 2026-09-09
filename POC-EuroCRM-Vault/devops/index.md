---
parent:"[[solution-overview]]"
status: Index
author: Gary Newport
date: 09/09/2026
---

# EuroCRM Wiki Index

The master index for the European CRM solution wiki. This page links every note in `/wiki` under the appropriate topic heading. The authoritative parent document is [[solution-overview]]; this index is the navigation surface for that body of work.

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

## Solution Architecture

### Overview

| Note | Purpose |
| ---- | ------- |
| [[architecture-overview-diagrams]] | High-level architecture diagrams |
| [[architecture-key-components]] | Component inventory |
| [[solution-package-model]] | L0–L7 layered package model |
| [[architecture-business]] | Business architecture |
| [[architecture-application]] | Application architecture and integrations |
| [[architecture-data]] | Data architecture overview |
| [[architecture-technology]] | Technology, hosting, and security |

### Data Model

| Note | Purpose |
| ---- | ------- |
| [[data-model-overview]] | EU CRM data model overview |
| [[data-model-core-tables]] | Core data model tables |
| [[client-data-model]] | Client — one client, one view |
| [[property-data-model]] | Property — site, property, deal |
| [[capital-markets-data-model]] | Capital Markets deal lifecycle (8-stage) |
| [[wip-data-model]] | Work in progress and revenue tracking |

### Taxonomies

| Note | Purpose |
| ---- | ------- |
| [[taxonomy-mappings]] | Taxonomy mappings overview |
| [[taxonomy-sic-kf]] | SIC to KF client sector mapping |
| [[taxonomy-hilucs-kf]] | HILUCS to KF asset class mapping |

## Enterprise Alignment

| Note | Purpose |
| ---- | ------- |
| [[architecture-target-state]] | Target state alignment to standards/PADs |
| [[architecture-principles-compliance]] | Mapping to CTO architecture principles |

## Approach & Decision Material

| Note | Purpose |
| ---- | ------- |
| [[architecture-approach-executive-summary]] | Plus/minus of the approaches for a C-level read |
| [[power-apps-rationale]] | Platform decision — Power Apps / Dataverse rationale |
| [[alternative-architecture-traditional-csharp]] | Alternative — traditional C# / PostgreSQL stack |
| [[solution-options]] | Solution options and trade-offs analysis |
| [[architecture-patterns-comparison]] | Integration patterns to Golden Source |
| [[outlook-email-interception-engagement-history]] | Outlook email interception → engagement history |

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
