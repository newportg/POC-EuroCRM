This is a second brain — a knowledge management system, not a code project. Your job is to keep the wiki current, useful, and well-organized based on the raw notes the user captures.

Read `README.md` first. This the source of truth for the system. This file gives you the additional context you need to do good work here.

---

## About the User

- **Name:** Gary Newport
- **Role:** Solution Architect
- **Topics I think about:** &lt;comma-separated list — e.g. "product strategy, AI agents, longevity, sales"&gt;
- **Voice preference:** clear, factual, terse.
- **Things I don't want in the wiki:** &lt;e.g. "no motivational filler", "no executive summaries on short entries", "no emojis"&gt;

---

## Common Tasks

- **Translate raw** → run the prompt in `translate.md` against `/raw`.
- **SOD regeneration** → run `python scripts/generate_sod_from_wiki.py` to rebuild `outputs/EuroCRM_Solution_Overview_Document.docx`.
- **Project digest** → summarize a `/projects/<name>/` folder into its README.
- **Answer questions** → read `/wiki` and `/archive` to answer ad-hoc questions about my own past thinking.
- Diagrams: Archimate or Plantuml only

---

## EuroCRM SOD Format

Hard rule for keeping the generated Solution Overview Document (SOD) clean. `scripts/generate_sod_from_wiki.py` reads `/wiki` notes and concatenates them into a Word document. To keep the output formatted:

- Use one `# Heading 1` per wiki note — this is the note's title and becomes the section heading. Do **not** duplicate it in the enclosing SOD section (e.g. `business-context.md` starts `# Business Context` which matches its section; the generator suppresses that match).
- Sub-sections use `##` / `###` — never introduce a `# Heading 1` in the middle of a note's body.
- Lists use `- ` bullets; the generator renders them with a literal `• `.
- Diagrams: PlantUML (`.puml` in `/wiki`) renders to images; use ` ```mermaid ```` fences for Mermaid and the generator renders them to images. ASCII art / code goes in plain ` ``` ` fences.
- Keep kebab-case filenames and one topic per file.

If in doubt whether a wiki note follows this, read the note and the generator's `SECTION_SOURCES` mapping first, then merge — never guess.

---

## Hard Rules

1. **Never delete** anything from `/raw` or `/archive`. Move only, never delete.
2. **Never overwrite** a `/wiki` entry blindly. Always read it first, then merge.
3. **Never modify** `/archive` after a file lands there — it is a permanent record.
4. **Commit after meaningful changes** with a clear message (e.g. `translate: 4 inbox files processed`).
5. **When uncertain, log it in the entry** rather than guessing.

---

## Wiki Voice and Structure

&lt;!-- CUSTOMIZE if needed --&gt;

- Default tone: clear, factual, terse.
- Preserve my own phrasing when it carries signal — don't sand everything into neutral encyclopedia tone.
- Headings only when the entry is long enough to need them.
- Bullets only when the content is genuinely a list.
- One topic per file. Kebab-case filenames.

---

## Out of Scope

- Web browsing unless I explicitly ask.
- External API calls outside of declared automations.
- Anything touching accounts, payments, or auth.
- Editing files in `/raw` or `/archive`.