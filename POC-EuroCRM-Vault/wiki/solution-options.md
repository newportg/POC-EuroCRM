---
parent:"[[solution-overview]]"
---

# Solution Options and Trade-offs

Three application options are presented to the Board. All deliver the same core outcome — a shared client, contact, property and engagement foundation across service lines and countries — with different cost, risk, and operating profiles. Full detail is in [[architecture-approach-executive-summary]]; the concise decision version is [[architecture-approach-executive-summary-one-page]].

## Option A — Extend Dynamics 365 Sales

- **What it is:** the packaged Microsoft sales CRM on Dataverse, extended with Knight Frank domain tables (property, instruction, deal, bid, NDA, KYC, due diligence, reference data).
- **Pros:** packaged capability, native Microsoft 365 integrations, managed platform, product-specific Copilot.
- **Cons:** licence cost can exceed value; lifecycle mismatch with the KF advisory model; 8 of 11 core entities still need custom building; roadmap controlled by Microsoft.
- **Cost:** per-user D365 Sales + Dataverse licensing.
- **Status in validation:** recommended baseline for the fit and cost assessment.

## Option B — Model-driven application on Dataverse

- **What it is:** a separate Knight Frank CRM application built with Power Apps and Dataverse; no packaged Dynamics 365 Sales application.
- **Pros:** application designed around KF terminology and advisory processes; Dataverse platform services retained; faster than a code build.
- **Cons:** Knight Frank owns the whole CRM application layer and its test/release/support burden; Dataverse capacity and governance limits; Power Platform skill set required.
- **Cost:** Power Apps per-user + Dataverse capacity licensing.
- **Status in validation:** main comparator.

## Option C — Knight Frank-built application

- **What it is:** a custom CRM product and data platform on the enterprise engineering stack (existing C#/.NET and PostgreSQL capability). Full design: [[csharp-postgresql/alternative-architecture-traditional-csharp]].
- **Pros:** full control over behaviour, release strategy and data architecture; no per-user platform licence; reuses existing engineering capability.
- **Cons:** complete application lifecycle to fund and operate; Microsoft 365 integrations and audit must be built; largest engineering requirement; longest build.
- **Cost:** infrastructure and engineering cost only.
- **Status in validation:** retained only if strategic, scale, performance or integration requirements justify full product ownership (unlikely in this case).

## Recommendation

The recommended position ([[architecture-approach-executive-summary-one-page]]) is to fund a defined validation stage:

- Use **Option A as the baseline**, compared against **Option B**.
- Retain **Option C** only where full ownership is justified.
- The validation stage must produce a fit assessment, a total cost of ownership model, an integration requirements assessment, and a validation test of one representative end-to-end scenario.