---
parent:"[[solution-overview]]"
source: European CRM Architecture Review 2.pdf
---

# Client Data Model — One Client, One View

## Data Schema

![[client-data-model-schema.puml]]

## Core Entities

### Account

OOB extended | Layer 2 Core

Organisation, brand, legal entity, fund, SPV or investor platform. Shared across every service line.

**Core Fields:**
- `accountid` — GUID, primary key
- `name` — Organisation name
- `accounttype` — Investor, vendor, occupier
- `address1_*` — Composite address
- `telephone1` / `emailaddress1` — Primary contact details
- `owningbusinessunit` — Security ownership
- `parentaccountid` — Parent account hierarchy

### Contact

OOB extended | Layer 2 Core

The individual person, always associated to an Account.

**Core Fields:**
- `contactid` — GUID, primary key
- `firstname` / `lastname` — Person name
- `jobtitle` — Role at the organisation
- `emailaddress1` — Primary email
- `telephone1` — Primary phone
- `parentcustomerid` — Lookup to Account
- `kf_processingconsent` — GDPR basis, Layer 3 EU

## Brand / Group vs. Legal Entity

A two-tier hierarchy gives one client view across many funds, SPVs and joint ventures.

**Brand/Group:** Blackstone, Brookfield, AXA IM
- Relationship, reporting, cross-sell

**Legal Entity:** Blackstone Core Fund (Fund), Blackstone Logistics (SPV), Blackstone Resi JV (JV)
- KYC, NDAs, billing, counterparty

**Classification Fields:**
- `kf_accountclassification` — Brand/Group, Legal Entity, Individual
- `kf_entitytype` — Fund, SPV, JV, HoldCo, OpCo, Trust

## International Standards on Client Records

Two fields anchor every account to recognised classifications rather than free text.

### KF_INDUSTRY

Industry classification mapped to SIC codes.

### KF_REGISTRATIONNUMBER

Legal registration number from the national company register.

**National Registers:**
- France: SIREN / SIRET
- Germany: Handelsregister HRB
- Spain: Registro Mercantil
- Poland: KRS number

Standard codes make sector reporting comparable across Europe, and a validated registration number underpins KYC and invoicing.
