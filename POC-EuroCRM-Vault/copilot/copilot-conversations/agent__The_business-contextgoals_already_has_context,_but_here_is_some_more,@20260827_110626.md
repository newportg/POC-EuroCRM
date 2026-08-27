---
epoch: 1787825186672
mode: agent
backendId: opencode
sessionId: "ses_fbdb0fa83ffeb48rJhTKQohw6q"
usage: '{"usedTokens":47454,"contextWindow":200000,"updatedAt":1787828043287}'
tags:
  - copilot-conversation
---

**user**: The business-context/goals already has context, but here is some more, can you add where it is appropiate. From a business perspective, the scope is to create a common client, contact and property data foundation across Europe that helps our teams win more business, collaborate more effectively across borders, and reduce operational risk. In practical terms, the programme is intended to:
Create a single, trusted view of clients, contacts, properties and opportunities.
Improve lead and deal management from origination through to completion.
Enable better cross-border visibility and collaboration across the region.
Centralised fragmented data currently on spreadsheets, local databases and reduce reliance on manual reporting processes.
Strengthen compliance, KYC and risk management controls.
Provide a foundation for reporting, analytics and future AI-driven insights.
[Timestamp: 2026/08/27 11:06:26]

**ai**: I'll look at the existing note to understand its current structure before adding this context.

The note already has a good structure. The user's new content provides business-level framing for the programme's scope and practical intentions. Let me integrate it appropriately — the overall scope framing fits at the top, and the practical points map onto the existing sections.

Let me add:
1. A "Scope" section near the top capturing the overall business framing
2. The practical programme points mapped against existing goals

The best approach is to add a dedicated "Programme Scope & Intended Outcomes" section that captures the business case, keeping the existing structure intact (merging, not overwriting).

The edit applied cleanly. The note has been updated with the new business context.

I added two new sections while preserving everything that was there:

**Programme Scope** — captures the headline framing: a common client, contact and property data foundation across Europe, driving more wins, better cross-border collaboration, and lower operational risk.

**Intended Outcomes** — the six practical programme points, kept in your original phrasing as a clean list. These complement the existing "Primary Goals" rather than duplicating them (the goals are more outcome-focused; the outcomes list the concrete deliverables).

A few mapping notes on how the new content relates to what was already there:
- "Single, trusted view" and lead/deal management align with the existing **Unified Customer View** and MVP success criteria.
- Cross-border visibility ties to **Cross-Sell Enablement**.
- Centralising spreadsheets/local databases strengthens **Operational Efficiency** and **Scalable Reporting**.
- Compliance/KYC reinforces **Regulatory Compliance**.
- AI-driven insights aligns with the existing **Future Phase Goals** AI line.

I deliberately kept the new sections separate rather than folding them into "Primary Goals" so no existing intent is lost or blurred — that fits the vault's read-then-merge rule. If you'd prefer the intended outcomes consolidated into the primary goals list instead, say the word and I'll restructure it.

Since this is a meaningful change to a `/wiki` entry, per your rules I can commit it. Want me to go ahead with a commit (e.g. `wiki: expand business-goals with programme scope`)?
[Timestamp: 2026/08/27 11:06:26]

**user**: does these changes satisfy the dashboard task
[Timestamp: 2026/08/27 11:10:45]

**ai**: I need to understand what "the dashboard task" refers to before I can say whether the changes satisfy it. Let me look for context on this task.

The "dashboard task" refers to the `dashboard.md` file that tracks outstanding tasks. Let me read it to understand what's being asked.

Now I understand the context. Let me look at the outstanding task that's most relevant to what I just did:

> `- [ ] Populate the business context and goals with the actual EuroCRM scope #task`

This is exactly what my edit to `business-goals.md` addresses. The user is asking whether the changes satisfy this dashboard task.

Let me evaluate this carefully. The task says "Populate the business context and goals with the actual EuroCRM scope." My edit added programme scope and intended outcomes to `business-goals.md`, which goes some way toward this.

However, there's an important distinction: the task mentions **both** "business context" AND "goals." Let me check the business-context note to see whether it also needs the scope content, since the user's message was framed primarily as business context.

Now I have the full picture. Let me answer the user's question directly.

The dashboard task is:

> `- [ ] Populate the business context and goals with the actual EuroCRM scope #task`

**Partially.** My edit moved `business-goals.md` toward completion, but it does not fully satisfy the task because the task spans **two** notes — *business context* **and** *goals* — and I only touched the goals note.

Here's the breakdown:

**What the edit satisfies:**
- The "goals" half. The new **Programme Scope** and **Intended Outcomes** sections in [[wiki/business-goals.md]] directly populate the note with the actual EuroCRM business scope. So the goals half of the task is now done.

**What's not yet satisfied:**
- The "business context" half. The task also calls for populating **[[wiki/business-context.md]]** with the actual scope. Looking at that note, some of your message's intent does map onto what's already there:
  - "Common client, contact and property data foundation" and the fragmented-data point align with the existing **Current State** (client knowledge in Excel trackers, no unified platform).
  - "Centralise fragmented data... reduce reliance on manual reporting" aligns with the existing **Problem Statement** (Manual Reporting) and **Drivers**.
  - "Strengthen compliance, KYC and risk management" maps to **Drivers** (regulatory compliance).
  
  So the *concept* is reflected, but the explicit framing you gave — the del/lead management from origination to completion, cross-border visibility, and the AI-driven insights foundation — isn't explicitly stated in `business-context.md` in your words.

So the honest answer: **not yet, fully.** To mark that dashboard task complete, I'd recommend adding the scope framing to `business-context.md` as well (e.g. a short "Programme Scope" or augmented "Drivers" reflecting the stated business intent). If you leave it only in the goals note, I'd keep the task open — it explicitly calls out "business context and goals" together.

Want me to extend the same framing into `business-context.md`? If I do, that outstanding dashboard item becomes genuinely satisfiable.
[Timestamp: 2026/08/27 11:10:45]

**user**: please extend
[Timestamp: 2026/08/27 11:13:30]

**ai**: I'll extend the programme scope into `business-context.md`. The user's message gives clear business framing that fits the "Drivers" and "Current State" areas of that note.

I've extended `business-context.md` with a **Programme Scope** section that mirrors the framing in `business-goals.md` — the common data foundation across Europe, plus the six intended outcomes in your original phrasing.

This now means the dashboard task:

> `- [ ] Populate the business context and goals with the actual EuroCRM scope #task`

...is genuinely satisfied on both halves — the scope is now explicitly present in both [[wiki/business-context]] and [[wiki/business-goals]].

You've asked about the dashboard explicitly, so I'd also make sure the `#task` is reflected as done. That dashboard is a hand-maintained list, not an auto-generated one — it has a Mermaid pie chart and a summary table, both of which count that item among the 10 outstanding (84% progress). If I tick that one task off, it'd become 51 → but the item's phrasing is a combined item ("context and goals"), so completing it moves the numbers accordingly.

Since I don't have a clear yes/no on whether you want me to update the dashboard counts now, here's what I'd propose:

- **The content work is done** — both notes now carry the actual EuroCRM scope.
- To fully close the loop on the dashboard, I can update `dashboard.md` (move that task into Completed, adjust the pie chart from 10→9 outstanding / 51→52 completed, update the "Next steps" row from 3→2 outstanding, and recalculate the 84% → ~85%).

Want me to make that dashboard update too? And should I also fold the FAQ-language into anywhere else — e.g. is there a solution-overview "Next steps" section I should sync so the source of truth stays consistent? I'll hold off on those unless you confirm.
[Timestamp: 2026/08/27 11:13:30]

**user**: please update the dashboard
[Timestamp: 2026/08/27 11:14:16]

**ai**: I'll update the dashboard to reflect that the "Populate the business context and goals with the actual EuroCRM scope" task is now complete. Let me carefully recalculate the numbers.

Current state in `dashboard.md`:
- Pie chart: Outstanding 10, Completed 51
- Total: 61 tasks
- Progress: 84% (51/61)
- Table row "Next steps": Outstanding 3, Completed 2 (40%)

The task I'm completing is in the "Solution overview document — next steps" section: `- [ ] Populate the business context and goals with the actual EuroCRM scope #task`

So this moves from outstanding to completed:
- Outstanding: 10 → 9
- Completed: 51 → 52
- Total stays 61
- Progress: 52/61 = 85.2% → 85%
- "Next steps" row: Outstanding 3 → 2, Completed 2 → 3 (60%)

Let me verify the "Next steps" row: it has 3 outstanding (populate business context/goals, complete cost/risk/roadmap, confirm enterprise standards) and 2 completed... wait, the section shows only outstanding tasks in "### Solution overview document — next steps". The "Completed 2" in the table refers to something else. Let me just look at the structure.

The table counts for "Next steps": Outstanding 3, Completed 2. The 3 outstanding are the three `- [ ]` items in that section. The 2 completed correspond to tasks done previously. Moving one outstanding → completed gives Outstanding 2, Completed 3.

Let me make the edits.

Now I need to move the completed task from the outstanding section into the completed section. Let me move it to a logical place — the "Solution Overview Document — Completed" section, since it's a solution overview next-steps item.

Now add it to the completed section under "Solution Overview Document — Completed":

Let me verify the final result of the dashboard.

The dashboard update is complete and consistent. Here's what changed:

**Content changes:**
- Moved `Populate the business context and goals with the actual EuroCRM scope #task` from the outstanding list into the **Solution Overview Document — Completed** section.

**Numbers updated consistently:**
- Pie chart: Outstanding 10 → **9**, Completed 51 → **52**
- Overall progress: 84% → **85%** (52/61)
- "Next steps" row: Outstanding 3 → **2**, Completed 2 → **3** (60%)

The Mermaid pie chart, the overall progress line, and the summary table all now agree with the task list itself — no stale counts left behind.

The two remaining items in the "next steps" section are:
- Complete cost, risk, and roadmap sections before formal approval
- Confirm the relevant enterprise standards, PADs, and blueprints

Couple of open items I'll leave to you before calling this fully closed:
- The dashboard's "Solution overview document — next steps" section still points back to a **Next steps** block in [[wiki/solution-overview]]. That source note still lists the "populate business context and goals" step as open — worth a quick sync so the source of truth and the dashboard don't disagree.
- Per your AGENTS.md rules, this was a meaningful `/wiki` change (both notes + dashboard), so a commit with a message like `wiki: add EuroCRM programme scope to business context and goals` would fit house style.

Want me to sync the solution-overview Next steps section and/or commit?
[Timestamp: 2026/08/27 11:14:16]

**user**: please sync
[Timestamp: 2026/08/27 11:17:17]

**ai**: I'll sync the solution-overview note's Next steps section. Let me find and read it first.

The dashboard's quote block references `[[wiki/solution-overview#Next steps|solution-overview — Next steps]]`, so there should be a "Next steps" heading in `solution-overview.md`. The grep only found the copilot conversation files and dashboard, not the solution-overview note. Let me check whether that anchor actually exists.

Interesting — the grep results are odd (it returned matches from other files, which suggests the path handling treated it as a directory search). But importantly, `solution-overview.md` has no "Next steps" heading. Let me read the actual file to see its full structure.

Now I understand the state. The `solution-overview.md` note does **not** actually have a "Next steps" heading — the dashboard's quote block anchor `[[wiki/solution-overview#Next steps|...]]` points to a heading that doesn't exist.

The dashboard's outstanding "next steps" items were derived from the solution overview document's outstanding work. The dashboard's quote references "solution-overview — Next steps" but no such section exists in the note.

Looking at the solution overview, there is **no explicit "Next steps" section**. The relevant outstanding work in the dashboard maps to gaps in this document:
- Cost, risk and roadmap sections (Cost and Benefits have "N/A" placeholders, Risks & Issues say "to be populated", roadmap says "to be defined")
- Enterprise standards, PADs, blueprints (Target State table shows "TBD"/"Pending review")

So the sync here is twofold:
1. The dashboard's [[wiki/solution-overview]] content is already reflected — business context/goals now sync via the wikilinked notes.
2. There's no "Next steps" section in solution-overview to update. The source of truth for these outstanding items is the document's gaps themselves.

The cleanest way to "sync" is to add a **Next steps** section to `solution-overview.md` that explicitly lists the remaining work — which would both make the dashboard's anchor valid and give the document a proper record of what's outstanding. Let me do that, reflecting the two remaining dashboard items plus the requirement/risk/options items.

Let me add a "Next steps" section before "Governance and Approval" (or at the end after References). The dashboard's outstanding items are:
1. Complete cost, risk, and roadmap sections before formal approval
2. Confirm the relevant enterprise standards, PADs, and blueprints

Plus the "sections needing expansion": functional/non-functional requirements, risks and issues, solution options and trade-offs, cost and benefits.

I'll add a concise Next steps section near the end of the document that captures these.

Now the dashboard's anchor `#Next steps` resolves to a real heading in `solution-overview.md`, and the two remaining outstanding next-steps items (cost/risk/roadmap, enterprise standards) plus the expansion items are explicitly captured as the source of truth.

Let me verify the dashboard's outstanding tasks still align with the new Next steps section I created:

Dashboard outstanding items:
- "Complete cost, risk, and roadmap sections before formal approval" → matches bullet 1
- "Confirm the relevant enterprise standards, PADs, and blueprints" → matches bullet 2
- Functional and non-functional requirements → matches bullet 3
- Risks and issues → matches bullet 4
- Solution options and trade-offs → matches bullet 5
- Cost and benefits — expected benefits → matches bullet 6 (I included quantification)

The sync is now clean and consistent. Both the dashboard and the source note align.

Here's what I did to sync the source of truth:

**The discovery:** [[wiki/solution-overview]] didn't actually have a "Next steps" heading — yet the dashboard's quote block anchored to `[[wiki/solution-overview#Next steps|...]]`. That anchor was dangling. So the sync meant creating the section the dashboard already assumed existed.

**What I added** to `solution-overview.md`, a **Next steps** section capturing all the outstanding work in the dashboard's own words:
- Complete cost, risk, and roadmap sections (costs are placeholder, risk register and roadmap unpopulated)
- Confirm the relevant enterprise standards, PADs, and blueprints (target state table shows pending/TBD)
- Gather functional and non-functional requirements
- Populate the risk register
- Complete solution options and trade-offs analysis
- Quantify expected benefits for the business case

Now the chain is fully aligned in one direction: dashboard → solution-overview's Next steps, and solution-overview's Business Context/Goals → [[wiki/business-context]] and [[wiki/business-goals]] (which now carry the EuroCRM scope).

One thing worth noting: the dashboard also lists the expansion items (functional/non-functional requirements, risks, solution options, expected benefits) under a separate "Document sections" row in its summary table. Those weren't touched — they map correctly to the new Next steps bullets, and their counts in the table (6 outstanding) are unchanged, which is correct since I didn't complete any of them.

That's the sync done. The only remaining loose end is the git commit, per your house rule to commit after meaningful changes. Want me to commit these three files (business-context, business-goals, solution-overview, dashboard) with a clear message?
[Timestamp: 2026/08/27 11:17:17]

**user**: commit
[Timestamp: 2026/08/27 11:19:43]

**ai**: I'll check the git state first, then commit the relevant files.

I'll stage only the four wiki/dashboard files that reflect my meaningful changes, not the `.obsidian` config noise or untracked artifacts (Untitled.canvas, the copilot conversation log — though I'll leave those out to keep the commit clean).

Let me check what changed in the diffs to make sure I'm committing the right content.

The diffs look exactly as expected. I'll stage and commit the four files.

Committed successfully.

**Commit `757b18f`** — `wiki: add EuroCRM programme scope and sync solution-overview next steps`

4 files, 40 insertions, 5 deletions:
- `wiki/business-goals.md` — added Programme Scope + Intended Outcomes
- `wiki/business-context.md` — added Programme Scope
- `wiki/solution-overview.md` — added Next steps section (fixes the dashboard's dangling anchor)
- `dashboard.md` — task moved to completed, counts/pie/progress updated

I left the `.obsidian` config changes, `Untitled.canvas`, and the copilot conversation log unstaged — those aren't part of this content change and shouldn't be in the wiki commit. Note there's also an untracked `obsidian-git/data.json`; I didn't touch it.

Everything's now in place: the scope is captured in both context/goals notes, the solution overview is synced, the dashboard is accurate, and it's committed per your workflow.
[Timestamp: 2026/08/27 11:19:43]

**user**: can you update the risks and issues, this following section should express the risk of not doing anything. Missed cross-border opportunities because relationship and client/market intelligence sits locally and aren't visible across Europe - or if it does, it requires tremendous manual efforts to unlock
Virtually no institutionalised client knowledge where knowledge sits with individuals in their excel / mailboxes / black books
Feedback from our HR surveys has highlighted frustration with the current technology landscape and the amount of manual effort required. Modernising these processes is important not only for efficiency, but also for improving employee satisfaction and supporting talent retention.
From a data management perspective, reconciling information and putting together regional reports consumes huge amount of time and efforts
Missed opportunities with leveraging AI / Advanced Analytics due to fragmented data
[Timestamp: 2026/08/27 11:23:39]

**ai**: I'll look at the existing risks-and-issues note first to follow the read-then-merge rule and match its structure.

The risks-and-issues note is a placeholder — the risk register is empty ("TBD") and the dashboard literally lists "Risks and issues — needs risk register populated" as outstanding. This content the user provided is exactly what's needed to populate it: the **risk of doing nothing** (the "do nothing" / status quo risk).

The user's five points are the business consequences of maintaining the status quo. I'll structure them as a risk register section capturing these as **risk-of-inaction** entries. The mitigation column should reflect what the EuroCRM programme does to address each.

Let me populate the risk register. I'll rewrite the risk register table with the five risks, adding likelihood/impact assessments (the user didn't specify these, so per the vault's "when uncertain, log it" rule I should be careful — I'll use reasonable professional estimates but note they're to be confirmed with stakeholders). Actually, let me preserve the user's own phrasing in the risk descriptions and provide sensible ratings flagged as provisional.

Let me build the updated entries:

1. **Missed cross-border opportunities** — relationship and client/market intelligence sits locally, not visible across Europe; where it is, unlocking it requires tremendous manual effort.
2. **No institutionalised client knowledge** — knowledge sits with individuals in Excel/mailboxes/black books.
3. **Employee frustration and attrition** — HR surveys flag frustration with the current technology landscape and manual effort; modernising matters for efficiency, employee satisfaction, and talent retention.
4. **Reconciling data and reporting cost** — data management, reconciliation, and regional reporting consume huge amounts of time and effort.
5. **Missed AI/advanced analytics value** — fragmented data blocks leveraging AI/analytics.

I'll add a framing line that these are the risks of **not doing anything** (status quo), and fill the register. For likelihood/impact I'll use reasonable values but flag them as provisional for stakeholder confirmation, in keeping with the "log it rather than guess" rule.

Now, since this populates the "Risks and issues — needs risk register populated" task that the dashboard lists under outstanding "sections needing expansion" (Document sections row), let me also update the dashboard to reflect that this outstanding item is now done.

The outstanding item is:
> `- [ ] Risks and issues — needs risk register populated #task`

Let me check the current dashboard state to update counts properly.

The dashboard currently shows:
- Pie: Outstanding 9, Completed 52
- "Document sections" row: Outstanding 6, Completed 25 (81%)
- Total 61, progress 85%

The "Risks and issues — needs risk register populated" item sits in the "Document sections" outstanding group. Completing it:
- Outstanding: 9 → 8
- Completed: 52 → 53
- Document sections: Outstanding 6 → 5, Completed 25 → 26
- Progress: 53/61 = 86.9% → 87%

Let me update the dashboard. First move the task to completed, then update the counts.

Now add it to the completed section. Let me add it to a suitable completed group. The "Solution Overview Document — Completed" section has the document sections. Let me add it there.

Now update the summary counts.

Let me verify the dashboard summary updates and check the progress arithmetic. 53/61 = 86.9% → 87%. Document sections: 26/31 = 83.9% → 84%. Both correct.

Let me verify the final dashboard state.

The dashboard is consistent. Let me also update the `solution-overview.md` Next steps section, which I created earlier and which still says "Populate the risk register" as an outstanding step — that's now done. Let me check.

The Next steps section I added had:
- "Complete cost, risk, and roadmap sections — costs and benefits are placeholder (CAPEX/OPEX N/A), risk register and roadmap phasing/timelines to be defined"
- "Populate the risk register"

The risk register is now populated (with the risk-of-inaction entries). However, the "Complete cost, risk, and roadmap sections" bullet still stands because costs/roadmap remain open, and the risk register being populated is captured in my new bullet "Populate the risk register". Let me remove the now-done "Populate the risk register" bullet and adjust the first bullet slightly since the risk portion is now begun (though combined with costs/roadmap it's still partly open).

Let me re-read the current Next steps section to be precise.

I'll update the Next steps section in solution-overview to reflect that the risk register is now populated. The first bullet's "risk register ... to be defined" wording is now outdated, and the standalone "Populate the risk register" bullet is done. Let me update both.

Now the changes are complete and consistent across the three files. Let me clean up my earlier provisional "populate the risk register" dashboard item reference — actually, I already handled the dashboard. Let me record my reasoning about the provisional ratings.

Here's a summary of what I did:

**[[wiki/risks-and-issues]] — populated the risk register with the risk of doing nothing.** I structured your five points as status-quo risks, each mapped to a mitigation that the EuroCRM programme delivers:

| Risk (from your input) | Likelihood | Impact |
| --- | --- | --- |
| Missed cross-border opportunities — intelligence sits locally, not visible across Europe (or requires huge manual effort to unlock) | Medium | High |
| No institutionalised client knowledge — knowledge sits in Excel, mailboxes, black books | High | High |
| HR survey feedback — frustration with tech landscape and manual effort; hurts efficiency, satisfaction, and talent retention | High | Medium |
| Data management/reporting effort — reconciling data and building regional reports is time-consuming | High | Medium |
| Missed AI/advanced-analytics value — fragmented data blocks leveraging AI | Medium | High |

I preserved your wording in the risk descriptions rather than sanding it into neutral prose, per your voice preference. The `Likelihood`/`Impact`/`Owner` values are provisional — I flagged them in a "Risk of Inaction" intro note that ratings are to be confirmed with stakeholders in the requirements phase (following your "log it rather than guess" rule; owners are TBD).

**Dashboard** — the previously outstanding task "Risks and issues — needs risk register populated" is now marked complete:
- Outstanding 9 → **8**, Completed 52 → **53**
- Progress 85% → **87%** (53/61)
- "Document sections" row 6→5 outstanding / 25→26 completed (84%)

**[[wiki/solution-overview]] Next steps** — removed the now-done "Populate the risk register" bullet and updated the wording to note the risk register now carries the risk-of-inaction entries (without closing the cost/roadmap item, which is still outstanding).

Two things worth flagging:
- I assigned provisional likelihood/impact ratings that you didn't specify. If you have different views (e.g. a particular risk is more likely or more severe), tell me and I'll adjust.
- The "Complete cost, risk, and roadmap sections before formal approval" dashboard item is still correctly open — only the risk register portion is done; cost modelling and roadmap remain.

Want me to commit these changes (risks-and-issues, dashboard, solution-overview)?
[Timestamp: 2026/08/27 11:23:39]

**user**: commit
[Timestamp: 2026/08/27 11:25:24]

**ai**: I'll stage and commit only the three content files for this change (dashboard, risks-and-issues, solution-overview).

Committed successfully.

**Commit `6e74a1a`** — `wiki: populate risk register with risk-of-inaction entries`

3 files:
- `wiki/risks-and-issues.md` — risk register populated with the five risk-of-inaction entries
- `dashboard.md` — "Risks and issues" task marked complete, counts/progress updated (87%)
- `wiki/solution-overview.md` — Next steps synced to reflect the risk register is now populated

The `.obsidian` config, `Untitled.canvas`, and copilot conversation log remain unstaged as before. Let me know if you'd like me to adjust any of the provisional likelihood/impact ratings or add owners to the register.
[Timestamp: 2026/08/27 11:25:24]

**user**: what items of third party software in this project needs to be purchased
[Timestamp: 2026/08/27 11:48:33]

**ai**: I'll look into the project's architecture and technology notes to identify third-party software that needs to be purchased. Let me search the relevant wiki notes.

I have a good picture of the technology stack. Let me also check the cost-estimates note and the out-of-scope note for the Loqate mention, plus the dependencies note about the "Hub" vendor, to give a complete answer.

I now have a comprehensive picture. Let me also check the out-of-scope note's Loqate detail and the solution-options note to be thorough, then answer.

Based on what I've gathered, this is a Microsoft Power Platform architecture. The key finding is that most of the software is **Microsoft licensing** (Power Apps, Dataverse, Power Automate, Power BI, D365 Finance, D365 Customer Insights — Journeys, Copilot), which is procured via Microsoft subscription rather than typically "purchased" as third party. There are two genuine **third-party** items: **Loqate** (address validation) and the **"Hub" vendor** (external system integration in Phase 6).

Let me check solution-options to see if there's an explicit vendor list.

I now have a complete, evidence-based picture. Let me answer.

Based on the vault's architecture, technology, dependencies, and scope notes, here's what needs to be purchased for this project.

## Overview

The EuroCRM solution is built almost entirely on the **Microsoft Power Platform** ecosystem. That means the bulk of the "software" is **Microsoft licensing** procured via subscription — not third-party purchases. There are only **two genuine third-party purchases** and one identified external dependency.

## Genuine third-party software (needs purchase)

**1. Loqate — address validation** `[[architecture-technology]]`, `[[roadmap-dependencies]]`
- Purpose: auto-address lookup for `kf_Site` records.
- Licensing model: per-lookup.
- Status: in-scope for MVP (the out-of-scope note explicitly says "Loqate only for MVP"). An API key is a Phase 1 dependency, currently marked TBD / to be provided by IT.

**2. The "Hub" vendor — external system integration** `[[roadmap-dependencies]]`, `[[solution-scope-out-of-scope]]`
- The project integrates with an external "Hub" system in **Phase 6** (currently deferred — manual transition for MVP).
- This is a third-party commercial dependency; the notes flag that the vendor selection and API availability aren't confirmed, and explicitly design for "API integration, not specific vendor."
- **Not a current purchase** — deferred, but on the horizon.

## Microsoft licensing to procure (subscription, not third-party purchase)

These aren't "third party" but they are the licensed items that need procurement, and `roadmap-dependencies` flags that **licensing procurement is a known risk** (mitigation: early engagement with Microsoft). From `[[architecture-technology]]` and `[[roadmap-dependencies]]`:

| Component | Licensing model |
| --- | --- |
| Dataverse | Per-user/per-app or per-org |
| Power Apps | Per-user or per-app |
| Power Automate | Per-user or per-flow |
| Power BI | Per-user or capacity-based |
| D365 Finance | Per-user |
| D365 Customer Insights — Journeys | Per-contact |
| Copilot for Sales | AI licensing (Phase 1 dependency) |
| Microsoft 365 (Outlook/SharePoint) | Assumed existing per assumptions |

## Where the answer is incomplete

The vault explicitly hasn't quantified any of this yet:
- `[[cost-estimates]]` — all **TBD**, "pending vendor selection," to be modelled in the business case.
- `[[solution-options]]` — options analysis "to be completed with vendor evaluation," all costs TBD.
- `[[solution-overview]]` cost/benefit section is placeholder.
- `[[roadmap-dependencies]]` lists licensing procurement as a Phase 0/1 gate with risk of delay.

## Bottom line

- **Actual third-party purchases today:** Loqate (address validation) — the only MVP, in-scope, third-party spend.
- **Future third-party:** the Hub system integration (Phase 6), vendor not yet selected.
- **Everything else** is Microsoft platform licensing to be procured via subscription.

If you'd like, I can capture this as a dedicated "third-party software / licensing" register note in the wiki (e.g. consolidating the Loqate and Hub items plus the Microsoft licensing list) so the purchase decisions are visible in one place — since `cost-estimates` currently just says "TBD." Just say the word.
[Timestamp: 2026/08/27 11:48:33]

**user**: Hub is a internal company system, so the only costs would be software integration
[Timestamp: 2026/08/27 11:50:57]

**ai**: Good correction — thanks for that. If the Hub is an internal company system rather than a third-party vendor, then it's an **integration effort**, not a software purchase. That removes the "Hub vendor" as a third-party software cost and reframes it as an internal integration project.

Let me reconcile this against what's currently in the notes, because there are a few places that describe the Hub as vendor-facing and would now be inaccurate:

- `[[roadmap-dependencies]]` — lists "Hub Vendor" as the owner of "Hub API Availability," has a "Hub Vendor Roadmap" external dependency, and a "Hub API integration, not specific vendor" risk.
- `[[solution-scope-out-of-scope]]` — lists "Full Hub API integration (Phase 6)" as deferred.

Since this reframes things, I want to confirm the scope of what you'd like me to do before editing. Two options:

1. **Update the existing notes** to reflect that the Hub is internal (so cost = integration effort, and there's no third-party vendor to procure). This touches `roadmap-dependencies.md`, `solution-scope-out-of-scope.md`, and possibly the cost/technology notes.

2. **Capture the revised cost picture** in a dedicated note (a licensing/third-party cost register) so the purchase decisions are documented in one place — Loqate being the only true third-party spend, plus the Microsoft licensing, plus the internal Hub integration effort.

On the actual answer to your question, the corrected view is:

## Third-party software to purchase
- **Loqate** (address validation) — the only genuine third-party software purchase, and it's in-scope for MVP. Per-lookup licensing.

## Not third-party purchases
- **Hub** — internal company system. Cost is **software/framework integration** (build effort + Power Platform connectors/API), not a purchase. The API availability is an internal dependency, and the out-of-scope note treats full integration as a Phase 6 deferral (manual transition for MVP).
- **Everything else** — Microsoft Power Platform licensing (Dataverse, Power Apps, Power Automate, Power BI, D365 Finance, CI-Journeys, Copilot), procured via subscription, not third-party.

So the "purchase" answer collapses to essentially just **Loqate**, with the Hub being an internal integration cost.

Want me to go ahead and update the notes so they correctly describe the Hub as an internal system (and no longer as a third-party vendor), and/or create a consolidated licensing/cost register? I'll wait for your go-ahead on scope before editing.
[Timestamp: 2026/08/27 11:50:57]

**user**: please go ahead and describe Hub as a internal system
[Timestamp: 2026/08/27 11:53:05]

**ai**: I'll update the notes that currently describe the Hub as a vendor to reflect that it's an internal company system. Let me find all references to the Hub first.

I need to update the references that describe the Hub as a **vendor** (third-party) rather than an internal system. The key places are in `roadmap-dependencies.md`:

1. Line 69: `| Hub API Availability | Technical | Hub Vendor | TBD | Phase 6 blocked |`
2. Line 92: `| Hub roadmap changes | Medium | Medium | Design for API integration, not specific vendor |`
3. Line 99: `| Hub Vendor Roadmap | External | Hub Vendor | API availability and support |`

The other references (Hub Replacement, Hub coexistence) are already neutral/fine. Let me update the vendor-specific ones in roadmap-dependencies.

Now let me check the implementation-phases note which references "Hub roadmap evaluation" — this is neutral but could be refined. Let me also check architecture-target-state. First let me look at the relevant section of implementation-phases around the Hub references.

The implementation-phases references are all neutral ("Hub Replacement", "Hub coexistence") and don't mention a vendor, so they're fine. But let me double-check there are no other "vendor" descriptors tied to Hub elsewhere. Let me grep for "vendor" across the wiki to see if any remaining reference implies Hub is third-party.

The remaining "vendor" mentions are unrelated to the Hub (they're about the property data model's "vendor" contact role, and generic vendor-selection placeholders for the platform). None incorrectly describe the Hub as a vendor. The `cost-estimates` "Pending vendor selection" is about the platform software, not the Hub.

The Hub-specific vendor references are now all corrected. Let me verify the roadmap-dependencies changes are clean.

The roadmap-dependencies changes are clean. Now there's a subtle consideration: the "External Dependencies" section still lists "Hub Roadmap" as an **External** type, but since the Hub is an internal system, the dependency isn't "external" in the third-party sense. However, from the EuroCRM project's perspective, a dependency on another internal company team is still effectively "external" to this project (owned by a different internal team). 

Given the user just wants the Hub described as internal, the owner change to "Internal Hub team" and the type "External" is defensible (external to the project, not external to the company). But to be precise and avoid confusion, I could relabel the type to clarify it's an internal-but-independent dependency. Let me reconsider — the section is titled "External Dependencies," and keeping "External" type with "Internal Hub team" owner is a slight tension. 

I'll keep it minimal and consistent with the user's request: the Hub is now owned by the internal Hub team, which reflects reality. The "External" type here at least means external to the EuroCRM project, which is accurate. I won't over-engineer this.

Now, should I also reflect the cost framing? The user previously noted "the only costs would be software integration." The notes don't currently have a place that explicitly captures the Hub as integration-effort-only. But the user's current instruction was specifically "describe Hub as a internal system" — which I've done. I'll keep scope tight to that instruction and offer the cost-register capture as a follow-up.

Let me also verify the implementation-phases "Hub roadmap evaluation" reference — it says "Phase 6: Hub Replacement" with "Dependencies: Phase 2 complete, Hub roadmap evaluation." That's neutral, no vendor implication, so it's fine.

The changes are complete. Let me summarize.

I've updated `[[wiki/roadmap-dependencies]]` to describe the Hub as an internal system:

- **Hub API Availability** — owner changed from "Hub Vendor" → **IT**
- **Hub roadmap changes** (risk register) — mitigation changed from "not specific vendor" → "Hub is an internal system"; integration using its API
- **Hub Vendor Roadmap** (external dependencies) → **Hub Roadmap**, owner → **Internal Hub team**

The other Hub references across the vault (Hub Replacement, Hub coexistence, Hub API integration in `implementation-phases`, `architecture-target-state`, `roadmap-timelines`, `kpis-and-success`, `solution-scope-out-of-scope`) were already neutral and don't describe the Hub as a vendor, so I left those untouched.

One note on the "External Dependencies" section: the Hub Roadmap still sits under it, typed "External." That's defensible because the Hub team is an internal-but-independent team *external to this project's delivery* — but if you'd prefer it relabelled to make the internal nature unmistakable (e.g. a separate "Internal System Dependencies" section), I can do that.

The practical consequence for your original question stands confirmed: the Hub is **not a software purchase** — its cost is integration effort only. **Loqate** remains the only genuine third-party software purchase for the MVP.

Want me to:
1. Relabel the Hub dependency out of "External" into an internal-systems section for clarity, and/or
2. Commit these changes?
[Timestamp: 2026/08/27 11:53:05]