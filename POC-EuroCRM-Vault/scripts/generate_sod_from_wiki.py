#!/usr/bin/env python3
"""Generate a completed EuroCRM SOD from the archived template and wiki."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


VAULT_ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = VAULT_ROOT / "wiki"
TEMPLATE_FILE = VAULT_ROOT / "archive" / "SOD template.docx"
OUTPUT_FILE = VAULT_ROOT / "outputs" / "EuroCRM_Solution_Overview_Document.docx"
OUTPUT_FILES = [
    VAULT_ROOT / "outputs" / "EuroCRM_Solution_Overview_Document.docx",
    VAULT_ROOT / "outputs" / "EuroCRM_Solution_Overview_Document_2026-09-01.docx",
    VAULT_ROOT / "projects" / "EuroCRM_Solution_Overview_Document_2026-08-27.docx",
]
PLANTUML_JAR = Path.home() / ".vscode" / "extensions" / "jebbs.plantuml-2.18.1" / "plantuml.jar"
diagram_paths: dict[str, Path] = {}

# Mermaid rendering via @mermaid-js/mermaid-cli (npx cache) + an installed browser
NPX = shutil.which("npx") or "npx"
CHROME_CANDIDATES = [
    Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Google" / "Chrome" / "Application" / "chrome.exe",
    Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Google" / "Chrome" / "Application" / "chrome.exe",
    Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
    Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
]
MERMAID_COUNT = 0


SECTION_SOURCES = {
    "Business Context": ["business-context.md", "problem-statement.md"],
    "Business Goals and Objectives": ["business-goals.md"],
    "Key Stakeholders": ["key-stakeholders.md"],
    "Business Capabilities": ["business-capabilities.md"],
    "KPIs and Success": ["kpis-and-success.md"],
    "Solution Scope": ["solution-scope-in-scope.md", "solution-scope-out-of-scope.md", "crm-lite-mvp-scope.md"],
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
        "solution-package-model.md",
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
    "Solution Options and Trade-offs": ["solution-options.md", "power-apps-rationale.md"],
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


def add_code_paragraph(doc: Document, text: str) -> None:
    """Add a monospaced code/ASCII-diagram line, preserving layout."""
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.left_indent = Inches(0.15)
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(text)
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:eastAsia"), "Consolas")


def find_chrome() -> Path | None:
    for candidate in CHROME_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def render_mermaid(block: str, output_png: Path, width_px: int = 1400) -> bool:
    """Render a Mermaid block to PNG using mermaid-cli + local Chrome."""
    chrome = find_chrome()
    if chrome is None:
        return False
    input_mmd = output_png.with_suffix(".mmd")
    input_mmd.write_text(block, encoding="utf-8")
    config = output_png.with_suffix(".json")
    config.write_text(json.dumps({
        "executablePath": str(chrome),
        "args": ["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"],
        "headless": True,
    }), encoding="utf-8")
    result = subprocess.run(
        [NPX, "--yes", "@mermaid-js/mermaid-cli",
         "-p", str(config), "-i", str(input_mmd), "-o", str(output_png),
         "-b", "white", "-w", str(width_px)],
        capture_output=True, text=True,
    )
    return output_png.exists() and result.returncode == 0


def parse_markdown(doc: Document, content: str, image_dir: Path) -> None:
    global MERMAID_COUNT
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
        fence_match = re.match(r"^```(\S*)\s*$", stripped)
        if fence_match:
            flush_paragraph()
            language = fence_match.group(1).strip().lower()
            index += 1
            code_lines = []
            while index < len(lines):
                line = lines[index]
                if line.strip().startswith("```"):
                    index += 1
                    break
                code_lines.append(line)
                index += 1
            if language == "mermaid":
                MERMAID_COUNT += 1
                png = image_dir / f"mermaid-{MERMAID_COUNT:03d}.png"
                if render_mermaid("\n".join(code_lines), png):
                    paragraph = doc.add_paragraph()
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    paragraph.add_run().add_picture(str(png), width=Inches(6.3))
                else:
                    for code_line in code_lines:
                        add_code_paragraph(doc, code_line)
            else:
                for code_line in code_lines:
                    add_code_paragraph(doc, code_line)
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
            list_style = "List Paragraph" if any(item.name == "List Paragraph" for item in doc.styles) else "Normal"
            paragraph = doc.add_paragraph(style=list_style)
            marker, item_text = list_match.group(1), list_match.group(2)
            prefix = "• " if not marker[0].isdigit() else f"{marker.strip()} "
            paragraph.add_run(prefix)
            add_inline(paragraph, item_text)
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


def extract_section(content: str, heading: str) -> str:
    """Return the body of a single '## Heading' section (heading line excluded)."""
    lines = content.replace("\r\n", "\n").splitlines()
    out: list[str] = []
    capture = False
    for line in lines:
        if line.startswith("## "):
            if capture:
                break
            capture = line[3:].strip().lower() == heading.lower()
            continue
        if capture:
            out.append(line)
    return "\n".join(out).strip()


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
        "26/08/2026": "01/09/2026",
        "27/08/2026": "01/09/2026",
        "0.1": "1.0",
        "0.2": "1.0",
    }
    for paragraph in doc.paragraphs:
        for old, new in replacements.items():
            if old in paragraph.text:
                for run in paragraph.runs:
                    if old in run.text:
                        run.text = run.text.replace(old, new)
    # Fill in bare cover labels with values (as in earlier document versions)
    cover_fields = {"Author:": "Gary Newport", "Date:": "01/09/2026", "Version:": "1.0", "Status:": "Draft"}
    for paragraph in doc.paragraphs:
        if paragraph.text.strip() in cover_fields:
            paragraph.add_run(f" {cover_fields[paragraph.text.strip()]}")


def add_source(doc: Document, filename: str, image_dir: Path, suppress_heading: str | None = None) -> None:
    source_path = WIKI_DIR / filename
    if not source_path.exists():
        return
    content = source_path.read_text(encoding="utf-8")
    if suppress_heading:
        lines = content.replace("\r\n", "\n").splitlines()
        for i, line in enumerate(lines):
            if line.startswith("#"):
                if line.lstrip("#").strip() == suppress_heading:
                    content = "\n".join(lines[:i] + lines[i+1:])
                break
    parse_markdown(doc, content, image_dir)


def create_document(image_dir: Path) -> Path:
    doc = Document(str(TEMPLATE_FILE))
    trim_template_to_cover(doc)
    replace_cover_placeholders(doc)
    doc.add_page_break()

    doc.add_heading("Version History", level=1)
    add_markdown_table(doc, [["Version", "Comments", "Author", "Status", "Date"], ["1.0", "Wiki content and diagrams consolidated into SOD", "Gary Newport", "Draft", "01/09/2026"]])
    doc.add_heading("Table of Contents", level=1)
    quote_style = "Intense Quote" if any(item.name == "Intense Quote" for item in doc.styles) else "Normal"
    doc.add_paragraph("Update this field in Word to generate the table of contents.", style=quote_style)
    doc.add_page_break()

    doc.add_heading("Executive Summary", level=1)
    overview_content = (WIKI_DIR / "solution-overview.md").read_text(encoding="utf-8")
    exec_content = extract_section(overview_content, "Executive Summary")
    if exec_content:
        parse_markdown(doc, exec_content, image_dir)

    used = {"solution-overview.md"}
    for section in TOP_LEVEL_SECTIONS[1:-1]:
        doc.add_heading(section, level=1)
        for filename in SECTION_SOURCES.get(section, []):
            add_source(doc, filename, image_dir, suppress_heading=section)
            used.add(filename)
        doc.add_page_break()

    doc.add_heading("References", level=1)
    doc.add_paragraph("The following wiki notes were used as the source of this document:")
    for filename in sorted(used):
        list_style = "List Paragraph" if any(item.name == "List Paragraph" for item in doc.styles) else "Normal"
        doc.add_paragraph(f"• {filename}", style=list_style)

    remaining = sorted(path.name for path in WIKI_DIR.glob("*.md") if path.name not in used)
    if remaining:
        doc.add_heading("Appendix: Additional Wiki Notes", level=1)
        for filename in remaining:
            add_source(doc, filename, image_dir)

    doc.core_properties.title = "EuroCRM Solution Overview Document"
    doc.core_properties.author = "Gary Newport"
    doc.core_properties.subject = "European CRM platform solution overview"

    for out_file in OUTPUT_FILES:
        out_file.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(out_file))
    return OUTPUT_FILE


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="eurocrm-sod-") as temp_dir:
        image_dir = Path(temp_dir)
        diagram_paths = render_diagrams(image_dir)
        create_document(image_dir)
    print(f"Created {OUTPUT_FILE}")
    print(f"Embedded PlantUML diagrams: {len(diagram_paths)}")
    print(f"Embedded Mermaid diagrams: {MERMAID_COUNT}")