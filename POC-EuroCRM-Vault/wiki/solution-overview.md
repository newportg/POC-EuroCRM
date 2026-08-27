# EuroCRM Solution Overview Document

Status: Draft
Author: Gary Newport
Date: 26/08/2026
Version: 0.1
Sources: European CRM Architecture Review 2.pdf, EU CRM Data Model.xlsx, European_CRM_Client_Industry_Master_Taxonomy.xlsx, European_CRM_Property360_Master_Taxonomy.xlsx

## Version History

| Version | Comments      | Author       | Status | Date       |
| ------- | ------------- | ------------ | ------ | ---------- |
| 0.1     | Initial draft | Gary Newport | Draft  | 26/08/2026 |

## Executive Summary

European CRM solution covering France, Germany, Spain, and Poland. This document defines the architecture approach for review and approval by the Technical Design Authority (TDA).

See [[problem-statement]] for the business case driving this initiative.

## Business Context

See [[business-context]] for detailed background.

The EuroCRM initiative addresses the need for a unified CRM platform across four European offices. Client intelligence is fragmented across local brokers, manual reporting doesn't scale, and cross-sell opportunities are missed.

## Business Goals and Objectives

See [[business-goals]] for detailed objectives.

Key goals:
- Unified customer view across European operations
- Compliance with regional data regulations (GDPR, local requirements)
- Standardised business processes across all four markets
- Cross-border and cross-service-line collaboration
- Scalable reporting as deal volume grows

## Key Stakeholders

See [[key-stakeholders]] for the full stakeholder register.

Approvals required from identified stakeholders plus TDA sign-off.

## Business Capabilities

See [[business-capabilities]] for capability mapping.

The solution must support core CRM capabilities:
- Contact and account management
- Opportunity and pipeline management
- Activity tracking and reporting
- Regional compliance and data residency

## KPIs and Success

See [[kpis-and-success]] for measurable outcomes.

**MVP Success Criteria:**
- "Who is this client to Knight Frank across every service line, every country?"
- "What does our EU pipeline look like?"
- "How do we run CM deals?"

## Solution Scope

### In-Scope

See [[solution-scope-in-scope]].

- CRM platform deployment for France, Germany, Spain, Poland
- Core sales and contact management workflows
- Integration with existing enterprise systems (to be confirmed)

### Out-of-Scope

See [[solution-scope-out-of-scope]].

- Marketing automation (phase 2 consideration)
- Legacy system decommissioning
- Non-European regions

## Solution Architecture

### Overview Diagrams

See [[architecture-overview-diagrams]].

Architecture diagrams to be developed during design phase.

### Key Components

See [[architecture-key-components]].

**Platform Decision:** Power Apps model-driven apps on Dataverse — see [[power-apps-rationale]].

**Layered Architecture:** See [[solution-package-model]] for L0-L7 model.

Core components:
- Dataverse platform (L1)
- KF_Core with 40+ table shells (L2)
- Region and country layers (L3-L4)
- Service Line BPFs (L5-L6)

### Business Architecture

See [[architecture-business]].

Business process models and capability mapping to be completed.

### Application Architecture

See [[architecture-application]].

Application component design and integration patterns to be defined.

### Data Architecture

See [[architecture-data]].

**Core Data Domains:**
- [[client-data-model]] — One client, one view
- [[property-data-model]] — Site, Property, Deal
- [[capital-markets-data-model]] — 12 entities for deal lifecycle
- [[wip-data-model]] — Work in progress and revenue tracking

**Taxonomy Standards:** See [[taxonomy-mappings]]
- SIC to KF Client Sector mapping (66 sectors)
- HILUCS to KF Asset Class mapping

### Technology Architecture

See [[architecture-technology]].

Infrastructure, hosting, and technology stack decisions to be documented.

## Alignment with Enterprise Architecture

### Principles Compliance

The CTO Architecture Principles document is referenced as a dependency: "CTO Architecture Principles.pptx".

See [[architecture-principles-compliance]] for mapping of solution design to enterprise standards.

### Target State Alignment

See [[architecture-target-state]].

Standards, PADs, and Blueprints relevant to this SOD:

| Standard/Blueprint | Status | Notes |
| ------------------ | ------ | ----- |
| CTO Architecture Principles | Referenced | Pending review |
| Enterprise data residency standards | TBD | Regional compliance required |
| Security baseline | TBD | TDA alignment needed |

## Dependencies and Constraints

See [[dependencies-and-constraints]].

Key dependencies:
- TDA approval required before implementation
- CTO Architecture Principles review
- Regional legal and compliance review
- Enterprise integration platform availability

## Key Functional and Non-Functional Requirements

### Functional Requirements

See [[functional-requirements]].

Requirements to be gathered from business stakeholders across all four regions.

### Non-Functional Requirements

See [[functional-non-functional-requirements]].

Performance, security, and compliance requirements to be defined.

## Risks and Issues

See [[risks-and-issues]].

Risk register to be populated during design phase.

## Solution Options and Trade-offs

See [[solution-options]].

Options analysis to be completed with vendor evaluation and architecture assessment.

## Implementation Roadmap

### Phases

See [[roadmap-phases]].

Phasing approach to be defined based on regional priorities and dependencies.

### Timelines

See [[roadmap-timelines]].

Estimated timelines to be confirmed after options analysis.

### Key Dependencies

See [[roadmap-dependencies]].

Critical path items and external dependencies to be mapped.

## Cost and Benefits Summary

### Estimated Costs

CAPEX: N/A
OPEX: N/A

See [[cost-estimates]] for detailed cost modelling.

### Expected Benefits

See [[expected-benefits]].

Benefits realisation to be quantified during business case development.

## Governance and Approval

### Approval

Approvals are required from the identified Key Stakeholders along with TDA approval.

See [[governance-approval]] for the approval workflow.

### Governance Oversight

This solution is in the purview of the Technical Design Authority (TDA).

See [[governance-oversight]] for governance structure and reporting.

## Compliance

See [[compliance]].

Regulatory and compliance requirements across all four European jurisdictions.

## Glossary

See [[glossary]].

## Next steps

Outstanding work before formal approval:

- Complete cost and roadmap sections — costs and benefits are placeholder (CAPEX/OPEX N/A) and roadmap phasing/timelines to be defined; risk register now carries risk-of-inaction entries in [[risks-and-issues]]
- Confirm the relevant enterprise standards, PADs, and blueprints — target state table lists CTO Architecture Principles as pending review and data residency/security baseline as TBD
- Gather functional and non-functional requirements from stakeholders across all four regions
- Complete solution options and trade-offs analysis (vendor evaluation and architecture assessment)
- Quantify expected benefits for the business case

## References

- CTO Architecture Principles.pptx
- European CRM Architecture Review 2.pdf
- EU CRM Data Model.xlsx
- European_CRM_Client_Industry_Master_Taxonomy.xlsx
- European_CRM_Property360_Master_Taxonomy.xlsx
- [[problem-statement]]
- [[solution-package-model]]
- [[crm-lite-mvp-scope]]
- [[client-data-model]]
- [[property-data-model]]
- [[capital-markets-data-model]]
- [[wip-data-model]]
- [[taxonomy-mappings]]
- [[power-apps-rationale]]
- [[data-model-overview]]
- [[implementation-phases]]
- [[data-model-core-tables]]
