# Architecture — Technology

Status: Draft
Parent: [[solution-overview]]
Source: European CRM Architecture Review 2.pdf, EU CRM Data Model.xlsx

## Technology Architecture Overview

EuroCRM runs on the **Microsoft Power Platform** with **Dataverse** as the data store. The technology stack is cloud-native, EU-hosted, and integrated with Microsoft 365.

## Infrastructure

### Hosting

| Component | Hosting | Region |
| --------- | ------- | ------ |
| Dataverse | Microsoft Cloud | EU (West Europe / France Central) |
| D365 Finance | Microsoft Cloud | EU |
| D365 CI-Journeys | Microsoft Cloud | EU (same environment as Dataverse) |
| SharePoint | Microsoft Cloud | EU |
| Power BI | Microsoft Cloud | EU |

**Data Residency:** All customer data resides in EU data centres to meet GDPR, CNIL, BDSG, and local regulatory requirements.

### Environment Strategy

| Environment | Purpose | Solutions | Data |
| ----------- | ------- |---------- | ---- |
| DEV | Development | Unmanaged (L2-L6) | Synthetic |
| TEST | Integration testing | Managed | Synthetic |
| UAT | User acceptance | Managed | Anonymised production |
| PROD | Production | Managed | Live |

## Technology Stack

### Platform Layer

| Component | Technology | Purpose |
| --------- | ---------- | ------- |
| Data Store | Dataverse | Relational data, custom tables, security |
| App Framework | Power Apps Model-Driven | UI, forms, views, dashboards |
| Process Automation | Power Automate | Workflows, approvals, integrations |
| Reporting | Power BI | Dashboards, analytics, KPIs |
| AI | Copilot for Sales | AI-powered client matching |

### Integration Layer

| Component | Technology | Purpose |
| --------- | ---------- |------- |
| Outlook Integration | Power Automate + Outlook Add-in | Email sync, activity tracking |
| Document Management | SharePoint | Auto-provision deal folders |
| Marketing | D365 Customer Insights - Journeys | Marketing handoff, lead nurture |
| Finance | D365 Finance (9 integration flows) | WIP, billing, revenue recognition |
| Address Validation | Loqate | Auto-address lookup for kf_Site |
| APIs | OData v4 + Custom API | External system integration |

### Productivity Layer

| Component | Technology | Purpose |
| --------- | ---------- | ------- |
| Email | Outlook | Email sync, tracking |
| Documents | SharePoint | Deal folders, NDA storage |
| Collaboration | Teams | Alerts, notifications |
| Analytics | Power BI | Regional/country dashboards |
| Mobile | Power Apps Mobile | Field broker access |

## Security Architecture

### Authentication

| Method | Scope |
| ------ | ----- |
| Microsoft Entra ID (Azure AD) | All users |
| Multi-Factor Authentication | Enforced |
| Conditional Access | Risk-based policies |
| Service Principal | System integrations |

### Authorisation

| Mechanism | Description |
| --------- | ----------- |
| Business Units | Country and service-line isolation |
| Security Roles | 6 roles (CM Broker, CM Manager, EIT User, Finance, Compliance, Admin) |
| Field-Level Security | Sensitive fields (GDPR consent, fee data) |
| Record Ownership | BU-based ownership model |

### Encryption

| Type | Standard |
| ---- | -------- |
| At Rest | Microsoft-managed encryption (AES-256) |
| In Transit | TLS 1.2+ |
| Customer-Managed Keys | Available via Azure Key Vault |

### Audit

| Feature | Retention |
| ------- | --------- |
| Dataverse Audit | 7-year retention |
| kf_AuditExport | Exportable for compliance |
| Login Auditing | Entra ID sign-in logs |

## Scalability & Performance

| Metric | Target | Notes |
| ------ | ------ | ----- |
| Concurrent Users | TBD | Per country BU |
| Data Volume | TBD | 40+ tables, 1,302 rows in master index |
| API Throughput | Dataverse limits | Per-org and per-user |
| Storage | Dataverse capacity | Managed via Azure |

## High Availability

| Feature | Status |
| ------- | ------ |
| Dataverse SLA | 99.9% uptime (Microsoft-managed) |
| Backup | Microsoft自动 daily backups |
| Disaster Recovery | Microsoft geo-redundant |
| RTO/RPO | Microsoft SLA |

## Monitoring & Observability

| Tool | Purpose |
| ---- | ------- |
| Dataverse Analytics | Usage, performance, errors |
| Power Platform Admin Centre | Environment health, capacity |
| Azure Monitor | Integration flow monitoring |
| kf_IntegrationLog | CRM-specific integration tracking |

## Compliance & Governance

| Requirement | Implementation |
| ----------- | --------------- |
| GDPR | kf_processingconsent, kf_GDPRRequest, data residency |
| CNIL (France) | EU data residency, consent management |
| BDSG (Germany) | EU data residency, audit trail |
| 7-Year Retention | Dataverse audit, kf_AuditExport |
| TDA Oversight | Managed solutions, no unmanaged in PROD |

## Cost Considerations

| Component | Licensing Model |
| --------- | --------------- |
| Dataverse | Per-user/per-app or per-org |
| Power Apps | Per-user or per-app |
| Power Automate | Per-user or per-flow |
| Power BI | Per-user or capacity-based |
| D365 Finance | Per-user |
| CI-Journeys | Per-contact |
| Loqate | Per-lookup |

**Note:** Detailed cost modelling to be completed during business case phase.

## Technical Rules

- Each layer is a separate managed solution
- No unmanaged customisations in TEST, UAT, or PROD
- KF_Core defines ALL option sets and custom tables as base
- No regional fork can create duplicate tables
- Layer 6 adds columns with country prefixes (`kf_fr_`, `kf_es_`), never renames standard stages
- Adding a country = new L4 + L6 | Adding a service line = new L5

## Related Documents

- [[architecture-key-components]] — Component inventory
- [[architecture-application]] — Application layer details
- [[architecture-data]] — Data model details
- [[solution-package-model]] — Layer model
- [[power-apps-rationale]] — Platform selection
