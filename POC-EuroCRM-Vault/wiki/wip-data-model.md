# WIP Data Model — Work in Progress

Status: Draft
Parent: [[solution-overview]]
Source: European CRM Architecture Review 2.pdf

## Data Schema

![[wip-data-model-schema.puml]]

## What is WIP?

WIP is the period from deal creation to fee earned: delivered, not yet billed.

**Example Timeline:**
- Month 1: Deal created in CRM
- Month 2: Due diligence in progress
- Month 3: Negotiation ongoing
- Month 4: Deal closes, fee earned

This is all WIP Revenue at Knight Frank.

## WIP Data Model: CRM to Finance

Every CRM deal becomes a project in D365 Finance, and that bridge enables WIP reconciliation.

| CRM Concept | Finance Concept | Why They Map |
| ----------- | --------------- | ------------ |
| kf_WIP line | Project | Both track the same billable engagement |
| kf_FeeSchedule | Project budget / contract line | Both define expected revenue |
| BPF stage % complete | Both measure progress to completion | |
| Deal status = Won | Milestone / invoice request | Both trigger billing |
| Account (client) | Customer (debtor) | Both identify who pays |

### KF_WIP Entity

**Key Fields:**
- `kf_wipid`
- `kf_parenttype`
- `kf_instructionid`
- `kf_netfeetogroup`
- `kf_officeretained`
- `kf_probability`
- `kf_grossfee`
- `kf_reportingmonth`
- `kf_wipstatus`
- `kf_invoicenumber`
- `kf_fin_localsystemref`

## The 8-Stage Process Drives WIP

Each deal stage maps to a finance percentage complete that automates the WIP calculation.

| Stage | % Complete |
| ----- | ---------- |
| S1 | 5% |
| S2 | 15% |
| S3 | 25% |
| S4 | 35% |
| S5 | 50% |
| S6 | 65% |
| S7 | 85% |
| S8 | 100% |

## Integration Flows

1. S3 fires Flow 1: the Finance project is created
2. Each stage change updates % complete in Finance
3. Deal won raises a draft invoice request
4. Invoice and payment data returns within hours
5. A monthly batch refreshes WIP balance and ageing
6. A credit hold alerts the broker in Teams
