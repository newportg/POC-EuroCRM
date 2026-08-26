# Key Stakeholders

Status: Draft
Parent: [[solution-overview]]

## Stakeholder Register

| Name             | Role                                 | Region                         | Interest | Influence |
| ---------------- | ------------------------------------ | ------------------------------ | -------- | --------- |
| Gary Newport     | Author/Solution Lead                 | Europe                         | High     | High      |
| TDA              | Technical Design Authority           | Enterprise                     | High     | High      |
| CTO              | Chief Technology Officer             | Enterprise                     | High     | High      |
| European MDs     | Regional Managing Directors          | France, Germany, Spain, Poland | High     | High      |
| CM Team Heads    | Capital Markets Service Line Leaders | Europe                         | High     | Medium    |
| Legal/Compliance | Data Protection Officers             | Europe                         | High     | Medium    |
| Finance Team     | Financial Controllers                | Europe                         | Medium   | Medium    |
| IT Operations    | Infrastructure & Support             | Enterprise                     | Medium   | Medium    |
| End Users        | Brokers, Analysts, Support Staff     | Europe                         | High     | Low       |

## RACI Matrix

| Activity | Solution Lead | TDA | CTO | Regional MDs | CM Team | Legal | Finance | IT Ops |
| -------- | ------------- | --- | --- | ------------- | ------- | ----- | ------- | ------ |
| Architecture Design | R | A | C | C | C | C | C | C |
| Environment Setup | R | A | C | I | I | I | I | R |
| Data Model Design | R | A | C | C | C | C | C | I |
| Security Configuration | R | A | C | I | I | C | I | R |
| Integration Design | R | A | C | I | I | I | C | R |
| UAT Coordination | R | A | I | C | R | C | C | I |
| Go-Live Approval | C | A | R | C | C | C | C | C |
| Post-Go-Live Support | C | I | I | I | I | I | I | R |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

## Key Roles

### Solution Lead (Gary Newport)

- Owns overall solution design and delivery
- Coordinates across all workstreams
- Primary point of contact for TDA

### Technical Design Authority (TDA)

- Approves architecture decisions
- Ensures compliance with enterprise standards
- Final sign-off on technical design

### Chief Technology Officer (CTO)

- Sets enterprise architecture principles
- Approves technology stack decisions
- Escalation point for technical blockers

### Regional Managing Directors

- Approve regional scope and priorities
- Provide business requirements
- Accept regional deliverables

### Capital Markets Team Heads

- Define CM-specific requirements
- Validate BPF design
- Accept CM features during UAT

### Legal/Compliance

- Review GDPR and regulatory requirements
- Approve data residency and audit features
- Validate compliance gates

### Finance Team

- Define Finance integration requirements
- Validate WIP and billing flows
- Accept Finance bridge during UAT

### IT Operations

- Provision environments and infrastructure
- Configure security and networking
- Provide ongoing support

### End Users

- Participate in UAT
- Provide feedback on usability
- Adopt the system post-go-live

## Communication Plan

| Audience | Frequency | Format | Owner |
| -------- | --------- | ------ | ----- |
| TDA | Weekly | Architecture review meeting | Solution Lead |
| CTO | Monthly | Steering committee | Solution Lead |
| Regional MDs | Bi-weekly | Progress report | Solution Lead |
| CM Team | Weekly | Sprint review | Solution Lead |
| Legal/Compliance | Bi-weekly | Compliance review | Solution Lead |
| Finance | Weekly | Integration sync | Integration Lead |
| IT Ops | Daily | Stand-up | Project Lead |
| End Users | Bi-weekly | Demo and feedback | Change Lead |

## Approval Requirements

- All identified stakeholders must approve
- TDA approval is mandatory
- See [[governance-approval]] for workflow
