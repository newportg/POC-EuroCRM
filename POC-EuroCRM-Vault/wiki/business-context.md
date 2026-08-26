# Business Context

Status: Draft
Parent: [[solution-overview]]
Source: European CRM Architecture Review 2.pdf

## Current State

- Four separate European offices: France, Germany, Spain, Poland
- Existing CRM systems vary by region (to be confirmed)
- No unified customer data platform
- Client knowledge sits with individual brokers in email, Excel trackers, and shared folders
- Transaction reports are built manually in Excel

## Problem Statement

See [[problem-statement]] for detailed analysis.

**Core Problems:**
1. **Fragmented Client Intelligence** — If a broker in Madrid is tracking an investor whose strategy matches a Paris asset, neither side knows
2. **Manual Reporting** — Price, buyer, seller, asset, and fee data assembled manually after every close
3. **Missing Cross-Sell Opportunities** — Fragmented data means opportunities for cross-border and cross-service-line collaboration are lost

## Regional Requirements

| Region | Key Requirements | Regulatory Notes |
| ------ | ---------------- | ---------------- |
| France | City pre-emption, notarial deed requirements | CNIL, GDPR |
| Germany | TBD | BDSG, GDPR |
| Spain | Right-of-refusal on listed buildings | GDPR |
| Poland | TBD | GDPR |

## Drivers

- Need for consolidated customer view across service lines and countries
- Regulatory compliance across jurisdictions
- Operational efficiency across regions
- Ability to scale reporting as deal volume grows

## Constraints

- Regional data residency requirements
- Existing system integrations
- TDA governance oversight
- Cross-border data sharing agreements required
