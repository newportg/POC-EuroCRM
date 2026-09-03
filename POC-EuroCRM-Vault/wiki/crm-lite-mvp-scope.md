---
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# CRM Lite — MVP Scope

## Key Principle

"The MVP is a shared client, contact, property and engagement foundation: a relationship and intelligence layer; not a full operational workflow system — which belongs to the Service Line deep build phase. Capital Markets is the first deeper workflow built on top."

## Shared Foundation

Designed to be reusable across service lines and countries:
- Accounts; Contacts; Properties; Engagement Tracking; Security
- Single Client Record
- Cross-SL Contact Intelligence
- Shared Property Records
- Outlook Integration
- SharePoint Auto-Provision
- Power BI Dashboards
- RBAC / Business Units
- Engagement History

Core question answered: "Who is this client to Knight Frank across every service line, every country?"

## First Service-Line Build

Capital Markets is the first vertical deployed on the shared foundation.

OSS, Valuations, etc. follow as separate Service Line solutions on the same backbone.

## Core Master Data Requirements

- Single trusted view of property and clients across service lines and countries
- International standards for property and client type definitions

## Pipeline & Relationships Requirements

- Engagement tracking and cross-border unified client view
- Full pipeline visibility with built-in WIP data

## Productivity Tools Requirements

- Outlook sync
- SharePoint libraries
- Power BI dashboards
- Copilot for Sales

## Data Architecture Requirements

- Layered Dataverse structure
- Layer 2 core, Layer 3 EUR defaults, Layer 4 country extensions, Layer 5 Service Line BPFs

## Security & Compliance Requirements

- Cross-border data sharing agreement, EU data centres, GDPR consent baseline
- Role-based security, 7-year audit retention
