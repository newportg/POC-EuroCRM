#!/usr/bin/env python3
"""Generate a completed EuroCRM SOD from the archived template and wiki."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Inches, Pt


VAULT_ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = VAULT_ROOT / "wiki"
TEMPLATE_FILE = VAULT_ROOT / "archive" / "SOD template.docx"
OUTPUT_FILE = VAULT_ROOT / "projects" / "EuroCRM_Solution_Overview_Document_2026-08-27.docx"
PLANTUML_JAR = Path.home() / ".vscode" / "extensions" / "jebbs.plantuml-2.18.1" / "plantuml.jar"


SECTION_SOURCES = {
    "Business Context": ["business-context.md", "problem-statement.md"],
    "Business Goals and Objectives": ["business-goals.md"],
    "Key Stakeholders": ["key-stakeholders.md"],
    "Business Capabilities": ["business-capabilities.md"],
    "KPIs and Success": ["kpis-and-success.md"],
    "Solution Scope": ["solution-scope-in-scope.md", "solution-scope-out-of-scope.md"],
    "Solution Architecture": [
        "architecture-overview-diagrams.md",
        "architecture-key-components.md",
        "architecture-business.md",
        "architecture-application.md",
        "architecture-data.md",
        "architecture-technology.md",
        "client-data-model.md",
        "property-data-model.md",
        "capital-markets-data-model.md",
        "wip-data-model.md",
        "data-model-overview.md",
        "data-model-core-tables.md",
        "taxonomy-mappings.md",
        "taxonomy-hilucs-kf.md",
        "taxonomy-sic-kf.md",
    ],
    "Alignment with Enterprise Architecture": [
        "architecture-principles-compliance.md",
        "architecture-target-state.md",
        "dependencies-and-constraints.md",
    ],
    "Key Functional and Non-Functional Requirements": [
        "functional-requirements.md",
        "functional-non-functional-requirements.md",
    ],
    "Risks and Issues": ["risks-and-issues.md"],
    "Solution Options and Trade-offs": ["solution-options.md"],
    "Implementation Roadmap": ["roadmap-phases.md", "roadmap-timelines.md", "roadmap-dependencies.md", "implementation-phases.md"],
    "Cost and Benefits Summary": ["cost-estimates.md", "expected-benefits.md"],
    "Governance and Approval": ["governance-approval.md", "governance-oversight.md", "compliance.md"],
    "Glossary": ["glossary.md"],
}

TOP_LEVEL_SECTIONS = [
    "Executive Summary",
    "Business Context",
    "Business Goals and Objectives",
    "Key Stakeholders",
    "Business Capabilities",
    "KPIs and Success",
    "Solution Scope",
    "Solution Architecture",
    "Alignment with Enterprise Architecture",
    "Key Functional and Non-Functional Requirements",
    "Risks and Issues",
    "Solution Options and Trade-offs",
    "Implementation Roadmap",
    "Cost and Benefits Summary",
    "Governance and Approval",
    "Glossary",
    "References",
]


def normalise_link(text: str) -> str:
    text = re.sub(r"!?(?:\[\[)([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or Path(m.group(1)).stem.replace("-", " "), text)
    return re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)


def add_inline(paragraph, text: str) -> None:
    """Add a small Markdown inline subset without losing emphasis."""
    text = normalise_link(text)
    pattern = re.compile(r"(\*\*[^*]+\*\*|__[^_]+__|\*[^*]+\*|_[^_]+_|`[^`]+`)")
    cursor = 0
    for match in pattern.finditer(text):
        if match.start() > cursor:
            paragraph.add_run(text[cursor:match.start()])
        token = match.group(0)
        run = paragraph.add_run(token.strip("*_`"))
        run.bold = token.startswith(("**", "__"))
        run.italic = token.startswith(("*", "_")) and not run.bold
        if token.startswith("`"):
            run.font.name = "Consolas"
        cursor = match.end()
    if cursor < len(text):
        paragraph.add_run(text[cursor:])


def add_markdown_table(doc: Document, rows: list[list[str]]) -> None:
    if not rows:
        return
    width = max(len(row) for row in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    if any(style.name == "Table Grid" for style in doc.styles):
        table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for row_index, row in enumerate(rows):
        for col_index in range(width):
            cell = table.cell(row_index, col_index)
            cell.text = row[col_index] if col_index < len(row) else ""
            if row_index == 0:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True


def parse_markdown(doc: Document, content: str, image_dir: Path) -> None:
    lines = content.replace("\r\n", "\n").splitlines()
    index = 0
    paragraph_buffer: list[str] = []

    def flush_paragraph() -> None:
        if paragraph_buffer:
            paragraph = doc.add_paragraph()
            add_inline(paragraph, " ".join(part.strip() for part in paragraph_buffer))
            paragraph_buffer.clear()

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        image_match = re.fullmatch(r"!\[\[(.+?)\]\]", stripped)
        if image_match:
            flush_paragraph()
            image_name = Path(image_match.group(1)).name
            image_path = diagram_paths.get(image_name, image_dir / f"{Path(image_name).stem}.png")
            if image_path.exists():
                paragraph = doc.add_paragraph()
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                paragraph.add_run().add_picture(str(image_path), width=Inches(6.3))
            index += 1
            continue
        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", stripped)
        if heading_match:
            flush_paragraph()
            level = min(3, max(2, len(heading_match.group(1))))
            doc.add_heading(normalise_link(heading_match.group(2)), level=level)
            index += 1
            continue
        if stripped.startswith("|") and "|" in stripped[1:]:
            flush_paragraph()
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index].strip())
                index += 1
            rows = []
            for table_line in table_lines:
                cells = [cell.strip() for cell in table_line.split("|")[1:-1]]
                if cells and not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    rows.append([normalise_link(cell) for cell in cells])
            add_markdown_table(doc, rows)
            continue
        list_match = re.match(r"^([-*+] |\d+[.] )(.*)$", stripped)
        if list_match:
            flush_paragraph()
            style = "List Number" if list_match.group(1)[0].isdigit() else "List Bullet"
            paragraph = doc.add_paragraph(style=style if any(item.name == style for item in doc.styles) else "Normal")
            add_inline(paragraph, list_match.group(2))
            index += 1
            continue
        if stripped.startswith("> "):
            flush_paragraph()
            quote_style = "Intense Quote" if any(item.name == "Intense Quote" for item in doc.styles) else "Normal"
            paragraph = doc.add_paragraph(style=quote_style)
            add_inline(paragraph, stripped[2:])
            index += 1
            continue
        if stripped.startswith("---"):
            flush_paragraph()
            index += 1
            continue
        paragraph_buffer.append(stripped)
        index += 1
    flush_paragraph()


def render_diagrams(output_dir: Path) -> dict[str, Path]:
    if not PLANTUML_JAR.exists():
        raise FileNotFoundError(f"PlantUML jar not found: {PLANTUML_JAR}")
    puml_files = sorted(WIKI_DIR.glob("*.puml"))
    if not puml_files:
        return {}
    subprocess.run(
        ["java", "-jar", str(PLANTUML_JAR), "-tpng", "-charset", "UTF-8", "-o", str(output_dir), *map(str, puml_files)],
        check=True,
        capture_output=True,
        text=True,
    )
    rendered = {}
    for source in puml_files:
        startuml = next((line.strip()[9:].strip() for line in source.read_text(encoding="utf-8").splitlines() if line.strip().lower().startswith("@startuml")), source.stem)
        rendered[source.name] = output_dir / f"{startuml}.png"
    return rendered


def trim_template_to_cover(doc: Document) -> None:
    first_heading = next((paragraph._p for paragraph in doc.paragraphs if paragraph.style.name == "Heading 1"), None)
    if first_heading is None:
        return
    element = first_heading
    while element is not None and element.tag.rsplit("}", 1)[-1] != "sectPr":
        next_element = element.getnext()
        element.getparent().remove(element)
        element = next_element


def replace_cover_placeholders(doc: Document) -> None:
    replacements = {
        "Solution Overview Document": "EuroCRM Solution Overview Document",
        "X to the Y": "Knight Frank European CRM Platform",
        "26/08/2026": "27/08/2026",
        "0.1": "0.2",
    }
    for paragraph in doc.paragraphs:
        for old, new in replacements.items():
            if old in paragraph.text:
                for run in paragraph.runs:
                    if old in run.text:
                        run.text = run.text.replace(old, new)


def add_source(doc: Document, filename: str, image_dir: Path) -> None:
    source_path = WIKI_DIR / filename
    if not source_path.exists():
        return
    doc.add_heading(source_path.stem.replace("-", " ").title(), level=2)
    parse_markdown(doc, source_path.read_text(encoding="utf-8"), image_dir)


def create_document() -> Path:
    doc = Document(str(TEMPLATE_FILE))
    trim_template_to_cover(doc)
    replace_cover_placeholders(doc)
    doc.add_page_break()

    doc.add_heading("Version History", level=1)
    add_markdown_table(doc, [["Version", "Comments", "Author", "Status", "Date"], ["0.2", "Wiki content and diagrams consolidated", "Gary Newport", "Draft", "27/08/2026"]])
    doc.add_heading("Table of Contents", level=1)
    quote_style = "Intense Quote" if any(item.name == "Intense Quote" for item in doc.styles) else "Normal"
    doc.add_paragraph("Update this field in Word to generate the table of contents.", style=quote_style)
    doc.add_page_break()

    doc.add_heading("Executive Summary", level=1)
    add_source(doc, "solution-overview.md", Path())

    used = {"solution-overview.md"}
    for section in TOP_LEVEL_SECTIONS[1:-1]:
        doc.add_heading(section, level=1)
        for filename in SECTION_SOURCES.get(section, []):
            add_source(doc, filename, image_dir)
            used.add(filename)
        doc.add_page_break()

    doc.add_heading("References", level=1)
    doc.add_paragraph("The following wiki notes were used as the source of this document:")
    for filename in sorted(used):
        list_style = "List Bullet" if any(item.name == "List Bullet" for item in doc.styles) else "Normal"
        doc.add_paragraph(filename, style=list_style)

    remaining = sorted(path.name for path in WIKI_DIR.glob("*.md") if path.name not in used)
    if remaining:
        doc.add_heading("Appendix: Additional Wiki Notes", level=1)
        for filename in remaining:
            add_source(doc, filename, image_dir)

    doc.core_properties.title = "EuroCRM Solution Overview Document"
    doc.core_properties.author = "Gary Newport"
    doc.core_properties.subject = "European CRM platform solution overview"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUTPUT_FILE))
    return OUTPUT_FILE


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="eurocrm-sod-") as temp_dir:
        image_dir = Path(temp_dir)
        diagram_paths = render_diagrams(image_dir)
        create_document()
    print(f"Created {OUTPUT_FILE}")
    print(f"Embedded diagrams: {len(diagram_paths)}")