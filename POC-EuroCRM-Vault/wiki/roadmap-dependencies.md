# Implementation Roadmap — Key Dependencies

Status: Draft
Parent: [[solution-overview]]

## Dependency Overview

Dependencies categorised by type: Governance, Technical, Compliance, Resource, and External.

## Pre-Implementation Dependencies

| Dependency | Type | Owner | Status | Impact if Blocked |
| ---------- | ------ | ----- | ------ | ----------------- |
| TDA Approval | Governance | TDA | Pending | Cannot start any phase |
| CTO Architecture Principles Review | Governance | CTO | Referenced | Architecture decisions blocked |
| Budget Approval | Governance | Finance | TBD | Cannot procure resources |
| Environment Provisioning | Technical | IT | TBD | Phase 0 blocked |

## Phase 0 Dependencies

| Dependency | Type | Owner | Status | Impact if Blocked |
| ---------- | ------ | ----- | ------ | ----------------- |
| Dataverse Tenant | Technical | IT | TBD | Cannot provision environments |
| Microsoft 365 Licensing | Licensing | IT | TBD | No Outlook/SharePoint integration |
| Power Platform Licensing | Licensing | IT | TBD | No Power Apps access |
| BU Hierarchy Design | Governance | Business | TBD | Security model blocked |
| SIC Code Reference Data | Data | Business | TBD | Industry classification incomplete |
| Country Legal Review | Compliance | Legal | TBD | GDPR fields may be incorrect |

## Phase 1 Dependencies

| Dependency | Type | Owner | Status | Impact if Blocked |
| ---------- | ------ | ----- | ------ | ----------------- |
| Phase 0 Complete | Technical | Project | TBD | Cannot start Phase 1 |
| Finance Integration Design | Technical | Finance + IT | TBD | WIP bridge blocked |
| D365 Finance Environment | Technical | IT | TBD | Integration flows cannot be tested |
| D365 CI-Journeys Licensing | Licensing | Marketing | TBD | Marketing handoff blocked |
| Copilot Licensing | Licensing | IT | TBD | AI features unavailable |
| Loqate API Key | Integration | IT | TBD | Address validation blocked |
| CM Requirements Sign-off | Business | CM Team | TBD | BPF design may be wrong |
| French Regulatory Review | Compliance | Legal | TBD | Regulatory gates may be incorrect |

## Phase 2 Dependencies

| Dependency | Type | Owner | Status | Impact if Blocked |
| ---------- | ------ | ----- | ------ | ----------------- |
| Phase 1 Complete | Technical | Project | TBD | Cannot start Phase 2 |
| Spanish Regulatory Review | Compliance | Legal | TBD | Right-of-refusal gate blocked |
| EIT Team Onboarded | Resource | Business | TBD | Cross-border features untested |
| Hub Coexistence Design | Technical | IT | TBD | Migration strategy unclear |
| Cross-Border Data Agreement | Compliance | Legal | TBD | Multi-jurisdiction KYC blocked |

## Phase 3-4 Dependencies

| Dependency | Type | Owner | Status | Impact if Blocked |
| ---------- | ------ | ----- | ------ | ----------------- |
| Phase 2 Complete | Technical | Project | TBD | Cannot start Phase 3 |
| OSS Requirements Gathered | Business | OSS Team | TBD | OSS BPF design blocked |
| Valuations Requirements Gathered | Business | Val Team | TBD | Valuations BPF design blocked |
| Residential Requirements Gathered | Business | Resi Team | TBD | Residential pipeline blocked |
| Private Office Requirements Gathered | Business | PO Team | TBD | UHNW features blocked |

## Phase 5-7 Dependencies

| Dependency | Type | Owner | Status | Impact if Blocked |
| ---------- | ------ | ----- | ------ | ----------------- |
| Phase 4 Complete | Technical | Project | TBD | Cannot start Phase 5 |
| Regional Business Cases | Governance | Regional MDs | TBD | Expansion blocked |
| Hub API Availability | Technical | IT | TBD | Phase 6 blocked |
| Finance ERP Selection | Decision | Finance | TBD | Phase 7 blocked |
| Regional Compliance Review | Compliance | Legal | TBD | Region-specific requirements unknown |

## Critical Path

```
TDA Approval → Environment Provisioning → Phase 0 → Phase 1 → Phase 2
                                                        ↓
                                            Finance Integration Design
                                                        ↓
                                            D365 Finance Environment
```

## Dependency Risk Register

| Risk | Likelihood | Impact | Mitigation |
| ---- | ---------- | ------ | ---------- |
| TDA approval delayed | Medium | High | Early engagement, pre-approval meetings |
| Finance integration design delayed | High | High | Start design in Phase 0, parallel workstream |
| Licensing procurement delayed | Medium | Medium | Early engagement with Microsoft |
| Resource availability across regions | High | Medium | Phased approach, shared resources where possible |
| Regulatory requirements change | Low | High | Regular legal review, flexible configuration |
| Hub roadmap changes | Medium | Medium | Design for API integration; Hub is an internal system |

## External Dependencies

| Dependency | Type | Owner | Notes |
| ---------- | ------ | ----- | ----- |
| Microsoft Platform Updates | External | Microsoft | Dataverse, Power Platform updates |
| Hub Roadmap | External | Internal Hub team | API availability and support |
| Regional Data Residency | External | Microsoft | EU data centre availability |
| SIC/HILUCS Standards | External | Regulatory | Standard updates and revisions |

## Related Documents

- [[dependencies-and-constraints]] — Full dependency register
- [[implementation-phases]] — Phase definitions
- [[roadmap-timelines]] — Timeline view
