---
epoch: 1788876881899
mode: agent
backendId: opencode
sessionId: "ses_f7eed9fd3ffepOgTHiq2lDOuff"
agentLabel: "C# Postgres alternative to Dynamics Dataverse"
usage: '{"usedTokens":46690,"contextWindow":200000,"updatedAt":1788877071928}'
tags:
  - copilot-conversation
---

**user**: can you look at the wiki and create a single md page which shows an alternative to the current design, one that doesnt involve Dynamics/Dataverse or power platform, but one that takes a more traditional approach using our current stack of C#, postgres etc
[Timestamp: 2026/09/08 15:14:41]

**ai**: Let me read the current solution overview first to understand the Dynamics-centric design.Let me read the key architecture and data model notes to understand the current Dynamics design fully.I now have a thorough understanding of the existing Dynamics/Dataverse design. Let me also quickly check a couple more notes to ground the alternative in the current real stack context — the taxonomy, data-model-overview, and business-context.

I now have a comprehensive understanding of the current Dynamics/Dataverse design and the business context. Let me create the alternative architecture note. I'll build it as a proper wiki entry following the SOD format (single `# Heading 1`, PlantUML/Mermaid diagrams, kebab-case filename, one topic per file).

Let me create the note that lays out a traditional C#/.NET + PostgreSQL based alternative that preserves the same business capabilities but removes the Power Platform/Dataverse dependency.

Now let me link this into the parent `solution-overview.md` under the Solution Options section, where an alternative design naturally belongs.

Now let me commit these meaningful changes as per the hard rules.

Done — [[alternative-architecture-traditional-csharp]] has been created and linked from [[solution-overview]]. Here's what it covers:

**Architecture overview:** An ASP.NET Core web app serving a REST API on PostgreSQL 16, with Hangfire workers for background tasks and RabbitMQ for async messaging to the ECS bus. All hosted in an EU region.

**Component mapping:** Every Dataverse/Power Platform capability has a concrete equivalent laid out in a mapping table — BPFs become a .NET state-machine workflow engine, Power Automate flows become Hangfire background workers, Dataverse RLS becomes PostgreSQL row-level security, and the managed solution layers become EF Core migrations versioned in-repo.

**Data architecture:** The exact same schema — `accounts`, `contacts`, `sites`, `properties`, `deals`, `pitches`, `ndas`, `bids`, `wip` etc — as PostgreSQL tables, preserving the same `kf_*` naming. Country-specific fields use either additive nullable columns or `jsonb` extension payloads instead of Dataverse dotted columns.

**Security & compliance:** Identical — Entra ID, MFA, conditional access, PostgreSQL RLS for country/team isolation, audit triggers with 7-year retention, GDPR consent handling. EU data residency preserved.

**Key trade-offs called out for TDA review:**
- For: no per-user platform licensing, uses existing .NET/Postgres skills, fully portable first-party code, no Dataverse capacity/governance limits
- Against: no native Outlook/SharePoint/Teams integration out of the box, requires infrastructure provisioning and operations, lower-code UI is faster to stand up on Power Apps

The note is honest about what the Dataverse platform buys you (native integrations, no infra to manage) while making the case that the same custom model is simpler and more direct as first-party code — since the original rationale for Dataverse was that D365 Sales was a poor fit and a custom model was required anyway.
[Timestamp: 2026/09/08 15:14:41]