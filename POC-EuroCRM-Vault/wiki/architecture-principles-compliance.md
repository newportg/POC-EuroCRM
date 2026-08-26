# Architecture — Principles Compliance

Status: Draft
Parent: [[solution-overview]]

## Reference Document

CTO Architecture Principles.pptx

## Principles Compliance Mapping

| Principle | Compliance Status | Evidence | Notes |
| --------- | ----------------- | -------- | ----- |
| Cloud-first | ✅ Compliant | Dataverse (EU-hosted), Power Platform | All components are cloud-native |
| Security by design | ✅ Compliant | Entra ID, MFA, encryption, audit trails | Security embedded in architecture |
| Data residency | ✅ Compliant | EU-hosted Dataverse, regional BUs | Data stays within EU jurisdictions |
| Scalability | ✅ Compliant | Power Platform autoscaling, Dataverse | Platform handles growth automatically |
| Integration-first | ✅ Compliant | 9 Finance flows, Outlook, SharePoint, CI-Journeys | Designed for integration from day one |
| Modularity | ✅ Compliant | L0-L7 layer model, managed solutions | Components can be deployed independently |
| Compliance | ✅ Compliant | KYC, GDPR, audit trails, regulatory gates | Built-in compliance mechanisms |
| User experience | ✅ Compliant | Model-driven apps, Copilot for Sales | Modern, intuitive interface |
| Cost optimisation | ✅ Compliant | Power Platform licensing, phased rollout | Pay-as-you-grow model |
| Future-proofing | ✅ Compliant | Layer model supports new regions/service lines | Extensible architecture |

## Detailed Compliance Analysis

### Cloud-first

- **Requirement:** Prefer cloud solutions over on-premises
- **Implementation:** Dataverse (EU-hosted), Power Platform, Microsoft 365 integration
- **Evidence:** No on-premises components, all services are SaaS/PaaS
- **Status:** ✅ Fully compliant

### Security by design

- **Requirement:** Embed security in architecture from the start
- **Implementation:** Entra ID authentication, MFA, Conditional Access, encryption at rest/transit, audit trails
- **Evidence:** Security roles, BU-based isolation, field-level security, 7-year audit retention
- **Status:** ✅ Fully compliant

### Data residency

- **Requirement:** Keep data within legal jurisdictions
- **Implementation:** EU-hosted Dataverse, country-specific BUs, regional data isolation
- **Evidence:** West Europe/France Central regions, BU hierarchy by country
- **Status:** ✅ Fully compliant

### Scalability

- **Requirement:** Architecture must support growth
- **Implementation:** Power Platform autoscaling, Dataverse storage tiers, phased rollout
- **Evidence:** 8 phases, new regions/service lines added via layer model
- **Status:** ✅ Fully compliant

### Integration-first

- **Requirement:** Design for integration from day one
- **Implementation:** 9 Finance flows, Outlook, SharePoint, CI-Journeys, Loqate
- **Evidence:** Integration bridge, API-first design, standard connectors
- **Status:** ✅ Fully compliant

### Modularity

- **Requirement:** Components should be independently deployable
- **Implementation:** L0-L7 layer model, managed solutions per layer
- **Evidence:** Each layer is a separate managed solution, can be deployed independently
- **Status:** ✅ Fully compliant

### Compliance

- **Requirement:** Build compliance into the platform
- **Implementation:** KYC/AML, GDPR consent, audit trails, regulatory gates
- **Evidence:** Automated gates, consent tracking, 7-year retention, exportable audit logs
- **Status:** ✅ Fully compliant

### User experience

- **Requirement:** Modern, intuitive interface
- **Implementation:** Model-driven apps, Copilot for Sales, Outlook integration
- **Evidence:** Familiar Microsoft interface, AI-assisted features, seamless integration
- **Status:** ✅ Fully compliant

### Cost optimisation

- **Requirement:** Optimise costs while delivering value
- **Implementation:** Power Platform licensing, phased rollout, shared foundation
- **Evidence:** Pay-as-you-grow, reuse across service lines, no custom code
- **Status:** ✅ Fully compliant

### Future-proofing

- **Requirement:** Architecture must support future changes
- **Implementation:** Layer model, managed solutions, extensible data model
- **Evidence:** New regions (L3), new service lines (L5), new countries (L4) can be added without rework
- **Status:** ✅ Fully compliant

## Gaps and Remediation

| Gap | Impact | Remediation | Timeline |
| --- | ------ | ----------- | -------- |
| CTO Principles document not available | Medium | Request from CTO office | Pre-implementation |
| Enterprise data residency standards not documented | Medium | Align with legal team | Phase 0 |
| Security baseline not documented | Medium | Align with security team | Phase 0 |
| Integration patterns not documented | Low | Document during Phase 0 | Phase 0 |

## Related Documents

- [[architecture-target-state]] — Target state architecture
- [[architecture-technology]] — Technology stack
- [[architecture-application]] — Application components
