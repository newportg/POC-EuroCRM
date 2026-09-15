---
epoch: 1789460158005
mode: agent
backendId: opencode
sessionId: "ses_f5bdd2b75ffeVnV8N13nDT8nnX"
agentLabel: "Switch to csuite document"
usage: '{"usedTokens":55731,"contextWindow":200000,"updatedAt":1789460627634}'
tags:
  - copilot-conversation
---

**user**: can you switch to the csuite document
[Timestamp: 2026/09/15 09:15:58]

**ai**: I found the C-suite document. It's [[architecture-approach-executive-summary]]. Let me read it:Here's the C-suite document: **[[architecture-approach-executive-summary]]** — the executive-level comparison of the two architectural approaches.

It's a one-pager covering:

- **Option A** (Power Platform / Dataverse) vs **Option B** (C# / PostgreSQL) at a glance
- Pluses and minuses of each
- The key tension: platform licensing cost vs. build effort
- Commercial/integration angle for the Golden Source
- Comparison table across 9 dimensions
- Recommendation framing as a business operating-model decision

What would you like to do with it? Some options:
- Edit or update the content
- View how it fits in the wiki (it's a child of [[solution-overview]])
- Export it or regenerate the SOD
- Something else?
[Timestamp: 2026/09/15 09:15:58]

**user**: its missing the option of Power Platform talking directly to a SQL/relational database, can you update it
[Timestamp: 2026/09/15 09:17:37]

**ai**: Let me read the alternative architecture note for more context on the hybrid option:Good catch — Power Platform with a direct SQL backend is a real hybrid option. Let me update the document to add it as Option C.There's a mirrored copy in `devops/`. Let me check how that folder is used before updating it:

The `devops/` folder is a mirror of wiki notes. Let me check the README to understand the folder structure:The generator (`generate_sod_from_wiki.py`) reads from `wiki/`, and `devops/` looks like a mirror copy. Let me check if anything syncs between them:The `devops/` mirror isn't referenced by any script — it's a stale copy of `wiki/`. Let me check git history to understand:The `devops/` folder is just a stale mirror from an automated backup — the generator reads `wiki/` only, so the wiki note is the canonical source. My edits are done. Let me verify the final result:Let me check whether this note is part of the SOD and commit the changes:The note isn't in the SOD's `SECTION_SOURCES` (it's a standalone decision doc, not part of the generated Solution Overview), so no SOD regeneration is needed. Let me commit the change:Done. [[architecture-approach-executive-summary]] now covers the Power Platform + SQL/PostgreSQL hybrid as **Option B** (the old C# option is now Option C). Here's what was added:

**New Option B section — Power Platform + SQL/PostgreSQL Database**
- Power Apps model-driven UI kept as the front-end, data stored in a relational database (SQL Server or PostgreSQL) via virtual tables, direct connectors, or a custom API layer.

**Pluses:**
- No Dataverse data licensing — kills per-entity storage cost while keeping the Power Apps UI
- Data is portable and under firm control
- Reuses existing DBA skills
- Cheaper than Option A
- UI ships without a full code build

**Minuses:**
- Hybrid complexity — two platforms to integrate, run, back up
- Feature gaps — virtual tables don't support all Dataverse features (BPFs, some rollups, native audit, complex calculated fields)
- Power Automate loses Dataverse triggers — needs SQL polling/custom connectors
- Mixed skills required
- Partial lock-in (UI layer stays Microsoft-owned)

**Updated throughout to match:**
- "Choice at a glance" and comparison tables now show three columns
- Key tension section reframed as a 3-way (buy managed / middle path / own it)
- Recommendation framing adds the middle-path question
- Integration angle and Related links updated (Option references corrected, previous "Option B" → "Option C")

One thing to flag: the hybrid option's feature-gap claims (BPFs, rollups, audit on virtual tables) are directionally right but worth validating against current Microsoft docs before it goes to TDA — Platform capabilities in this area change fairly often. Want me to do a quick web check on what's supported with Dataverse virtual tables today?
[Timestamp: 2026/09/15 09:17:37]

**user**: the document is for the c-suite/level, its shouldnt refer to them. It should be a busines document proposing the three options, highlighting the plusses and minuses without preference
[Timestamp: 2026/09/15 09:22:23]

**ai**: The user wants the document reframed: keep the C-suite as the audience, but stop referring to them in the text, and keep it a neutral business proposal. Let me make those edits:Let me also check the comparison table and index references for neutral language:Now let me update the index description to match the new neutral framing:Now let me commit the changes:Done. [[architecture-approach-executive-summary]] is now a neutral business proposal. Changes made:

**Removed all references to the C-suite audience:**
- Intro: "A one-page read for a C-level audience..." → "This document proposes three architectural approaches... The pluses and minuses of each are set out below without preference; the choice is a business decision to be weighed by the programme stakeholders."
- Integration section: "For the C-suite, the integration future also matters" → "Integration to the Golden Source also varies by option..."

**Removed any sense of preference or recommendation:**
- "Recommendation framing" → **"Decision framing"**, and the three bullets rewritten from "Do we prefer to buy...?" questions to neutral statements ("Buy a managed platform...", "Take the middle path...", "Invest engineering effort...")
- Key tension section stripped of value-loaded phrasing ("lower platform cost than Dataverse" → "it avoids Dataverse data licensing but requires running two platforms")
- "Selling the build" retained as a factual minus for Option C, no recommendation made anywhere

**Updated the wiki index** entry to match: "Plus/minus of the three architectural approaches without preference"

The document now reads as a straight business proposal: three options, plusses and minuses for each, comparison table, and a decision-framing section that lays out the trade-offs without pointing at a preferred choice. The tags (`executive`, `board`, `tda`) still identify its audience for navigation without the body text referencing them.

One thing worth confirming: the title still says "Executive Summary". Fine to keep, or would you prefer something like "Architectural Approach Options — Business Comparison" to reinforce the neutral framing?
[Timestamp: 2026/09/15 09:22:23]