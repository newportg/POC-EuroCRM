---
parent:"[[solution-overview]]"
status: Draft
author: Gary Newport
date: 09/09/2026
tags:
  - architecture
  - integration
  - outlook
  - engagement
  - email
---

# Outlook Email Interception — Updating CRM Engagement History

This note sets out how email sent and received in Microsoft Outlook can be intercepted and written back into the CRM as **engagement history** — the running record of interactions between a broker and a client, contact, or property deal.

It maps onto the capability "**Outlook Integration: Email tracking and activity logging**" in [[business-capabilities]], the `Outlook → Dataverse` integration in [[architecture-application]], and the email-sync worker in the [[alternative-architecture-traditional-csharp|traditional C# stack]].

## Objectives

Capture the email engagement that currently sits in individual mailboxes and make it part of the shared client/contact view (the problem stated in [[problem-statement]]). Specifically:

- Record every relevant email against the correct Account, Contact, and Deal
- Build a searchable engagement history per client and per deal
- Support relationship tracking (last contact date, interaction volume) without brokers manually logging emails
- Respect GDPR — email content is personal data and must be handled under the same consent/retention rules as the rest of [[architecture-data]]

## The Engagement History Store

Email is logged against the CRM as an *activity* rather than as an attachment or copy of the message body. The entry stores metadata plus a link to the source message, not the full body:

| Field | Purpose |
| ----- | ------- |
| Subject | Displayable title of the interaction |
| Participants (From / To / CC) | Resolved to CRM Contact / Account records |
| Timestamp | When the message was sent or received |
| Direction | Inbound / outbound |
| Thread ID | Groups replies into a single engagement thread |
| Linked records | Deal, Contact, Account, Property |
| Message link | Back-reference to the original in Exchange (Graph `messageId`) |
| Consent basis | GDPR basis for processing / retention |

In the Dataverse design this maps to a Dataverse **Email activity** entity linked to the relevant records. In the [[alternative-architecture-traditional-csharp|C#/PostgreSQL]] design it maps to an `email_activity` / `engagement` table with the same linking and retention rules.

## Interception Options

There are three ways to intercept Outlook email. They can be combined — automatic capture as the baseline, with an add-in for user-triggered actions.

![[outlook-email-intercept-to-engagement-history]]

### Path A — Outlook Add-in (user-triggered)

An Outlook add-in runs in context on a selected message (read or compose). The broker clicks "Log to CRM" and the message is correlated and saved.

- **Pros:** explicit user intent, low false-positive rate, lets the broker choose the linked Deal
- **Cons:** relies on user action — silent capture requires the other paths
- **Implementation:** Office Add-in (or existing Outlook integration on Dataverse) that calls the CRM API with the message metadata

### Path B — Microsoft Graph Webhook (automatic)

Subscribe to change notifications on the mailbox via **Microsoft Graph**. Graph raises a notification whenever an email matches criteria (e.g. from/to a tracked domain, or on a deal thread), and a worker ingests it.

- **Pros:** fully automatic, no user effort, catches all inbound/outbound mail
- **Cons:** needs careful filtering and correlation to avoid logging noise; must handle a high message volume
- **Implementation:** Graph `createSubscription` on `message` changes → notification handler pushes to CRM. This is the mechanism referenced in [[alternative-architecture-traditional-csharp|Email sync — Graph API (webhooks) + inbox worker]].

### Path C — Mailbox Worker (scheduled / triggered)

A background worker (Power Automate flow in the Dataverse design; a .NET/Hangfire worker in the C# design) periodically polls mail via Graph and processes rules.

- **Pros:** deterministic, easy to throttle and batch, works without real-time webhooks
- **Cons:** latency between send and capture
- **Implementation:** Power Automate `When a new email arrives` → Dataverse; or Hangfire job polling Graph → PostgreSQL `email_activity`

## Correlation and Matching

The hard part is deciding which Deal / Contact / Account each email belongs to. The correlation pipeline:

1. **Participant resolution** — match sender/recipients against CRM Contact and Account email addresses (including alternate domains per legal entity).
2. **Deal thread matching** — match subject/thread against active deals; a known deal thread is the strongest signal.
3. **Entity resolution** — where a participant resolves to a Contact, inherit the parent Account and any linked Deal.
4. **Deduplication** — collapse replies into one thread; skip messages already logged (idempotent via the Graph `messageId` / thread ID).

## GDPR and Retention

Email logging is personal-data processing and must comply with the GDPR measures in [[architecture-principles-compliance]]:

- **Consent basis:** capture the legitimate-interest basis per message; record it on the engagement entry
- **Retention:** email activity follows the same 7-year retention as the rest of [[architecture-data]], with erasure/export handled as data-subject requests
- **Storage:** log metadata + link to source in Exchange; do not duplicate full message bodies into the CRM unless retention requires it
- **Audit:** the interceptor and any matching decisions are recorded, giving a traceable audit trail

## OpenAI decision notes

This is a design proposal for review — it is not yet built. Open items to confirm with the team:

- Which interception path(s) to adopt (add-in only, or automatic Graph ingestion with add-in override)
- Whether to log full message bodies or metadata + link only
- The definitive matched-entity list and correlation rules (Deal/Contact/Account/property)
- Retention period for email activity against the 7-year baseline

## Related

- [[business-capabilities]] — Outlook Integration capability
- [[architecture-application]] — Current Dataverse integration patterns (Power Automate Outlook → Dataverse)
- [[alternative-architecture-traditional-csharp]] — C#/PostgreSQL path (Graph webhooks + inbox worker)
- [[architecture-principles-compliance]] — GDPR, CNIL, BDSG requirements
- [[architecture-data]] — Data domains the engagement links to
- [[problem-statement]] — The fragmented-email problem this addresses
