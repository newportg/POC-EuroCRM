# Implementation Phases

Status: Draft
Parent: [[solution-overview]]
Source: EU CRM Data Model.xlsx

## Phase Overview

8 phases from foundation to full ERP integration. MVP is Phases 0-1 (20-26 weeks).

| Phase | Label | Duration | Layers | Status |
| ----- | ----- | -------- | ------ | ------ |
| Phase 0 | Foundation ("CRM Lite") | 8-10 weeks | L2-L4 | Planning |
| Phase 1 | Paris CM Deep Build | 12-16 weeks | L5-L6 | Planning |
| Phase 2 | Madrid + EIT CM Deep Build | 10-14 weeks | L6-L7 | Not started |
| Phase 3 | Additional Service Lines | Future | L5 | Not started |
| Phase 4 | Residential / Private Office | Future | L5-L7 | Not started |
| Phase 5 | Regional Expansion | Future | L3 | Not started |
| Phase 6 | Hub Replacement | Future | Integration | Not started |
| Phase 7 | Consolidated Finance ERP | Future | Integration | Not started |

---

## Phase 0: Foundation ("CRM Lite")

**Duration:** 8-10 weeks
**Layers:** L2 (KF_Core), L3 (KF_Europe), L4 (Country)
**Dependencies:** TDA approval, Environment provisioning

### Scope

- Dataverse environment setup (DEV, TEST, UAT, PROD)
- KF_Core layer: 40+ table shells, option sets, BU hierarchy
- KF_Europe layer: EUR defaults, GDPR baseline
- Country layers: KF_France, KF_Germany, KF_Poland, KF_Spain
- Security roles and BU configuration
- SharePoint integration (deal folder auto-provision)
- Power BI foundation (regional dashboard)

### Tables Activated

| Table | Category |
| ----- | -------- |
| Account | CRM Lite |
| Contact | CRM Lite |
| kf_Property | CRM Lite |
| kf_EnergyRating | Compliance |
| kf_GDPRRequest | Compliance |
| kf_AuditExport | Compliance |
| kf_SICCode | Supporting |

### Deliverables

- [ ] Dataverse environments provisioned
- [ ] KF_Core solution deployed
- [ ] KF_Europe solution deployed
- [ ] Country solutions deployed (FR, DE, PL, ES)
- [ ] Security roles configured
- [ ] BU hierarchy established
- [ ] SharePoint integration tested
- [ ] Power BI regional dashboard created

### Acceptance Criteria

- Users can create/view Account and Contact records
- BU-based security isolation working
- GDPR consent fields visible and functional
- SIC code lookup operational
- SharePoint folders auto-provision on record creation

---

## Phase 1: Paris CM Deep Build

**Duration:** 12-16 weeks
**Layers:** L5 (KF_CapitalMarkets_Core), L6 (KF_CM_France)
**Dependencies:** Phase 0 complete, Finance integration design, Copilot licensing

### Scope

- Capital Markets 8-stage BPF
- All 12 CM entities (Deal, Pitch, NDA, Bid, etc.)
- French regulatory gates (city pre-emption, notarial deed)
- Finance integration bridge (9 flows to D365 Finance)
- Marketing handoff to CI-Journeys
- Copilot for Sales pilot
- WIP tracking and fee management

### Tables Activated

| Table | Category |
| ----- | -------- |
| kf_Deal | CM Deep Build |
| kf_DealProperty | Core Shared |
| kf_Pitch | CM Deep Build |
| kf_NDA | CM Deep Build |
| kf_Bid | CM Deep Build |
| kf_DDMilestone | CM Deep Build |
| kf_RedFlag | CM Deep Build |
| kf_FeeSchedule | CM Deep Build |
| kf_KYCRecord | CM Deep Build |
| kf_InvestorProfile | CM Deep Build |
| kf_DataRoomAccess | CM Deep Build |
| kf_TransactionReport | CM Deep Build |
| kf_StageGateRule | Supporting |
| kf_IntegrationLog | Supporting |
| Lead | Marketing |

### Deliverables

- [ ] 8-stage BPF configured and tested
- [ ] All 12 CM entities deployed
- [ ] French regulatory gates implemented
- [ ] Finance bridge (9 flows) tested
- [ ] WIP tracking operational
- [ ] Marketing handoff to CI-Journeys working
- [ ] Copilot for Sales pilot completed
- [ ] UAT with Paris CM team

### Acceptance Criteria

- Brokers can manage deals through 8-stage lifecycle
- French regulatory gates fire at correct stages
- Finance project created at S3
- WIP % complete updates on stage change
- Transaction reports auto-generated
- Copilot matching provides actionable suggestions

---

## Phase 2: Madrid + EIT CM Deep Build

**Duration:** 10-14 weeks
**Layers:** L6 (KF_CM_Spain), L7 (KF_EIT)
**Dependencies:** Phase 1 complete, EIT team onboarded, Hub coexistence design

### Scope

- Spanish CM extension (right-of-refusal gate)
- EIT cross-border overlay
- Cross-border portfolio management
- Hub coexistence (manual CRM ↔ Hub transition during Phase 6)
- Multi-jurisdiction KYC and conflict checks

### Deliverables

- [ ] KF_CM_Spain solution deployed
- [ ] Spanish regulatory gate implemented
- [ ] KF_EIT solution deployed
- [ ] Cross-border portfolio view working
- [ ] Multi-jurisdiction KYC functional
- [ ] Intercompany billing flows tested
- [ ] Hub coexistence strategy documented
- [ ] UAT with Madrid CM team

### Acceptance Criteria

- Spanish brokers can manage deals with local gates
- EIT team can view and manage cross-border portfolios
- KYC checks work across jurisdictions
- Intercompany billing generates correctly

---

## Phase 3: Additional Service Lines

**Duration:** Future (TBD)
**Layers:** L5 (new service line cores)
**Dependencies:** Phase 2 complete, Service line requirements gathered

### Scope

- KF_OSS_Core (Occupier Strategy & Solutions)
- KF_Valuations_Core
- New Layer 5 solutions with their own BPFs
- OSS engagement workflow
- Valuation instruction workflow

### Tables Activated (Future)

| Table | Service Line |
| ----- | ------------ |
| kf_Engagement | OSS |
| kf_Lease | OSS |
| kf_WorkplaceAssessment | OSS |
| kf_LocationSearch | OSS |
| kf_ValuationInstruction | Valuations |

### Deliverables

- [ ] KF_OSS_Core solution deployed
- [ ] KF_Valuations_Core solution deployed
- [ ] OSS BPF configured
- [ ] Valuations BPF configured
- [ ] Integration with shared foundation tested

---

## Phase 4: Residential / Private Office

**Duration:** Future (TBD)
**Layers:** L5 (KF_Residential_Core), L7 (KF_Private_Office)
**Dependencies:** Phase 3 complete, Residential requirements gathered

### Scope

- KF_Residential_Core (Sales, Lettings, Property Management)
- KF_Private_Office at Layer 7 (cross-service-line for UHNW)
- Residential pipeline (Sales/Lettings instruction → Tenancy)
- Private Office spanning CM, Residential, Valuations

### Tables Activated (Future)

| Table | Service Line |
| ----- | ------------ |
| kf_ResProperty | Residential |
| kf_SalesInstruction | Residential |
| kf_LettingsInstruction | Residential |
| kf_Tenancy | Residential |
| kf_Applicant | Residential |
| kf_Viewing | Residential |
| kf_Offer | Residential |
| kf_BuyingBrief | Residential |

### Deliverables

- [ ] KF_Residential_Core solution deployed
- [ ] KF_Private_Office solution deployed
- [ ] Residential pipeline BPF configured
- [ ] Private Office cross-SL view working

---

## Phase 5: Regional Expansion

**Duration:** Future (TBD)
**Layers:** L3 (new regions)
**Dependencies:** Phase 4 complete, Regional business cases approved

### Scope

- KF_APAC (Asia-Pacific)
- KF_Americas
- KF_MiddleEast
- New Layer 3 regional solutions
- Country layers within each region

### Deliverables

- [ ] Regional solutions designed
- [ ] Regional compliance requirements gathered
- [ ] Regional deployments planned

---

## Phase 6: Hub Replacement

**Duration:** Future (TBD)
**Layers:** Integration
**Dependencies:** Phase 2 complete, Hub roadmap evaluation

### Scope

- Full API integration replacing manual CRM ↔ Hub transition
- Real-time data sync between CRM and Hub
- Eliminate manual data entry

### Deliverables

- [ ] Hub API integration designed
- [ ] Real-time sync implemented
- [ ] Manual transition process deprecated

---

## Phase 7: Consolidated Finance ERP

**Duration:** Future (TBD)
**Layers:** Integration
**Dependencies:** Phase 2 complete, Finance ERP selection

### Scope

- Consolidated Finance ERP
- Activates all 9 integration flows
- Full WIP reconciliation
- Automated billing and revenue recognition

### Deliverables

- [ ] Finance ERP selected
- [ ] 9 integration flows fully operational
- [ ] WIP reconciliation automated
- [ ] Billing process streamlined

---

## MVP Summary (Phases 0-1)

**Total Duration:** 20-26 weeks
**Total Tables:** 22
**Service Lines:** Capital Markets (France)
**Countries:** France (primary), others (foundation only)

### Critical Path

```
Phase 0 (8-10 weeks) → Phase 1 (12-16 weeks) → MVP Complete
```

### Key Milestones

| Milestone | Target | Phase |
| --------- | ------ | ----- |
| Environments Ready | Week 2 | Phase 0 |
| Core Tables Deployed | Week 4 | Phase 0 |
| Security Configured | Week 6 | Phase 0 |
| Country Layers Deployed | Week 8 | Phase 0 |
| BPF Configured | Week 12 | Phase 1 |
| CM Entities Deployed | Week 16 | Phase 1 |
| Finance Bridge Tested | Week 20 | Phase 1 |
| UAT Complete | Week 24 | Phase 1 |
| Go-Live | Week 26 | Phase 1 |

## Related Documents

- [[roadmap-timelines]] — Detailed timeline view
- [[roadmap-dependencies]] — Dependency register
- [[solution-package-model]] — Layer architecture
- [[data-model-overview]] — Table inventory
