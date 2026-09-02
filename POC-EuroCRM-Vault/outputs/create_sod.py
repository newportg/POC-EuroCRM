"""
Generate EuroCRM Solution Overview Document from wiki content,
using the Wibble.docx template structure.
"""

import copy
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

VAULT = r"C:\Source\Obsidian\Projects\POC-EuroCRM\POC-EuroCRM-Vault"
TEMPLATE = os.path.join(VAULT, "archive", "Wibble.docx")
OUTPUT = os.path.join(VAULT, "outputs", "EuroCRM_Domain_Architecture.docx")
PROJECT_NAME = "EuroCRM"

# ---------- helpers -----------------------------------------------------------

def set_cell_text(cell, text, bold=False, size=Pt(10)):
    """Clear cell and write text."""
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.font.size = size
    run.bold = bold


def add_heading(doc, text, level=1):
    """Add a heading paragraph."""
    p = doc.add_heading(text, level=level)
    return p


def add_para(doc, text, bold=False, size=Pt(11)):
    """Add a normal paragraph."""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = size
    run.bold = bold
    return p


def add_bullet(doc, text, level=0, size=Pt(11)):
    """Add a bullet-point paragraph using List Paragraph style with a bullet prefix."""
    p = doc.add_paragraph(style="List Paragraph")
    p.clear()
    bullet = "\u2022 "  # bullet character
    run = p.add_run(bullet + text)
    run.font.size = size
    p.paragraph_format.left_indent = Inches(0.25 + 0.25 * level)
    return p


def add_table_from_rows(doc, headers, rows):
    """Add a simple table."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    try:
        table.style = "Table Grid"
    except KeyError:
        table.style = "Normal Table"
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    # Header row
    for i, h in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], h, bold=True, size=Pt(10))
    # Data rows
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            set_cell_text(table.rows[r_idx + 1].cells[c_idx], val, size=Pt(10))
    return table


# ---------- document assembly -------------------------------------------------

doc = Document(TEMPLATE)

# Clear existing content (remove all paragraphs and tables)
for p in doc.paragraphs[:]:
    p._element.getparent().remove(p._element)
for t in doc.tables[:]:
    t._element.getparent().remove(t._element)

# ---- Title ----
add_heading(doc, f"7.X {PROJECT_NAME} Domain", level=0)

# ---- 7.X.1 Scope and Boundary ----
add_heading(doc, f"7.X.1 Scope and Boundary", level=1)

add_para(doc, (
    f"The {PROJECT_NAME} domain represents Knight Frank's European CRM business unit."
))

add_para(doc, (
    f"{PROJECT_NAME} provides advisory services relating to the acquisition, "
    "maintenance, valuation and optimisation of commercial and residential property "
    "across France, Germany, Spain and Poland."
))

add_para(doc, "The domain is responsible for:")

scope_items = [
    "Client management (Account, Contact, Brand/Group hierarchy)",
    "Property management (Site, Property, Residential Property, Energy Ratings)",
    "Deal management (8-stage BPF, NDA, Bid, Due Diligence, Red Flags)",
    "Financial management (WIP tracking, Fee management, D365 Finance bridge)",
    "Compliance and governance (KYC/AML, GDPR consent, Audit export)",
    "Integration and analytics (Outlook, SharePoint, CI-Journeys, Power BI)",
]
for item in scope_items:
    add_bullet(doc, item)

add_para(doc, (
    "The domain consumes enterprise client, property and employee data "
    "but does not own those entities."
))

# In-scope table
add_para(doc, "In-Scope Items:", bold=True)
add_table_from_rows(doc,
    ["Category", "Items"],
    [
        ["Platform", "Dataverse (EU-hosted), Power Apps, Power Automate, Power BI, Copilot for Sales"],
        ["Service Lines", "Capital Markets (MVP), OSS (Future), Valuations, Residential, Private Office"],
        ["Countries", "France (MVP), Germany, Spain, Poland (Phase 0 foundation)"],
        ["Integrations", "Outlook, SharePoint, D365 Finance (9 flows), CI-Journeys, Loqate"],
        ["Features", "8-stage BPF, Regulatory gates, WIP tracking, KYC/AML, GDPR, Audit trail"],
    ],
)

# ---- 7.X.2 Current State ----
add_heading(doc, f"7.X.2 Current State", level=1)

add_para(doc, (
    f"The {PROJECT_NAME} domain currently operates a collection of independent "
    "applications procured over time to support individual business requirements."
))

add_para(doc, (
    "These systems have been introduced to address local business requirements "
    "and have evolved independently."
))

add_para(doc, "Current challenges include:")

current_challenges = [
    "Client information duplicated across multiple platforms.",
    "Multiple representations of the same property asset.",
    "Manual reconciliation between systems.",
    "Point-to-point integrations.",
    "Limited visibility of enterprise-wide client relationships.",
    "Multiple reporting solutions generating different answers.",
    "Email-based deal tracking with no centralised pipeline.",
    "Ad-hoc compliance processes without automated gates.",
]
for item in current_challenges:
    add_bullet(doc, item)

add_para(doc, (
    "As a result, operational delivery remains possible but increasingly "
    "dependent upon manual intervention and local knowledge."
))

# Current state vs target state table
add_para(doc, "Current State vs Target State:", bold=True)
add_table_from_rows(doc,
    ["Capability", "Current State", "Target State", "Gap"],
    [
        ["Client data", "Manual spreadsheets", "Centralised Dataverse", "High"],
        ["Property data", "Fragmented systems", "Single source of truth", "High"],
        ["Deal tracking", "Email-based", "Automated BPF", "High"],
        ["Financial tracking", "Manual WIP", "Integrated bridge", "Medium"],
        ["Compliance", "Ad-hoc processes", "Automated gates", "High"],
        ["Reporting", "Siloed data", "Unified Power BI", "High"],
    ],
)

add_para(doc, "Current State Architecture", bold=True)

# ---- 7.X.3 Business Capabilities ----
add_heading(doc, f"7.X.3 Business Capabilities", level=1)

add_para(doc, "The EuroCRM domain provides the following core business capabilities:")

capabilities = {
    "Client Management": [
        "Account Management: Legal entity records with SIC-coded industry classification (66 KF sectors)",
        "Contact Management: Individual contacts linked to accounts with roles and preferences",
        "Brand/Group Hierarchy: Two-tier model: Brand/Group to Legal Entity",
        "Industry Classification: SIC codes mapped to KF sectors with gap analysis",
    ],
    "Property Management": [
        "Site Management: Canonical physical sites with addresses and coordinates",
        "Property Management: Commercial and residential properties linked to sites",
        "Residential Property: Sales, lettings, and property management",
        "Energy Ratings: EPC and energy performance data",
    ],
    "Deal Management": [
        "Pipeline Management: 8-stage BPF from lead generation to completion",
        "BPF Lifecycle: Stage-specific activities, documents, and regulatory gates",
        "Due Diligence: NDA, KYC, data room access, red flag tracking",
        "Regulatory Gates: City pre-emption (France), right-of-refusal (Spain), notarial deed",
    ],
    "Financial Management": [
        "WIP Tracking: Work-in-progress with % complete tied to BPF stage",
        "Fee Management: Fee schedules with agreed fees and billing triggers",
        "Integration Bridge: 9 flows to D365 Finance (project creation, WIP sync, transaction reports)",
        "Transaction Reports: Auto-generated reports for deal completion",
    ],
    "Compliance and Governance": [
        "KYC/AML: Know Your Customer checks at legal entity level",
        "GDPR Consent: Data processing consent tracking with audit trail",
        "Audit Export: 7-year retention with exportable audit logs",
        "Red Flag Tracking: Conflict checks and risk identification",
    ],
    "Integration and Analytics": [
        "Outlook Integration: Email tracking and activity logging",
        "SharePoint Integration: Deal folder auto-provisioning and document management",
        "Marketing Handoff: CI-Journeys integration for campaign automation",
        "Power BI Dashboards: Regional reporting and analytics",
    ],
}

for cap_name, items in capabilities.items():
    add_para(doc, cap_name, bold=True)
    for item in items:
        add_bullet(doc, item)

# Business capabilities table
add_para(doc, "Capability Summary:", bold=True)
add_table_from_rows(doc,
    ["Capability", "Description"],
    [
        ["Client Management", "Account, Contact, Brand/Group hierarchy with SIC classification"],
        ["Property Management", "Site, Property, Residential Property, Energy Ratings"],
        ["Deal Management", "8-stage BPF, NDA, Bid, Due Diligence, Red Flags"],
        ["Financial Management", "WIP tracking, Fee schedules, D365 Finance bridge"],
        ["Compliance and Governance", "KYC/AML, GDPR consent, Audit export, Red flags"],
        ["Integration and Analytics", "Outlook, SharePoint, CI-Journeys, Power BI"],
    ],
)

# ---- 7.X.4 Capability to System Mapping ----
add_heading(doc, f"7.X.4 Capability to System Mapping", level=1)

add_para(doc, (
    "This mapping highlights areas of duplication and identifies opportunities "
    "for future consolidation."
))

add_table_from_rows(doc,
    ["Capability", "Power Apps (Target)", "Legacy System 1", "Legacy System 2", "MS Excel"],
    [
        ["Client Management", "\u2714", "\u2718", "\u2718", "\u2718"],
        ["Property Management", "\u2714", "\u2714", "\u2718", "\u2718"],
        ["Deal Management", "\u2714", "\u2718", "\u2714", "\u2718"],
        ["Financial Management", "\u2714", "\u2718", "\u2718", "\u2714"],
        ["Compliance and Governance", "\u2714", "\u2718", "\u2718", "\u2718"],
        ["Integration and Analytics", "\u2714", "\u2718", "\u2718", "\u2718"],
    ],
)

# Capability maturity table
add_para(doc, "Capability Maturity:", bold=True)
add_table_from_rows(doc,
    ["Capability", "Current State", "Target State", "Gap"],
    [
        ["Client Management", "Manual spreadsheets", "Centralised Dataverse", "High"],
        ["Property Management", "Fragmented systems", "Single source of truth", "High"],
        ["Deal Management", "Email-based tracking", "Automated BPF", "High"],
        ["Financial Management", "Manual WIP tracking", "Integrated bridge", "Medium"],
        ["Compliance and Governance", "Ad-hoc processes", "Automated gates", "High"],
        ["Integration and Analytics", "Siloed data", "Unified platform", "High"],
    ],
)

# ---- 7.X.5 Desired Future State ----
add_heading(doc, f"7.X.5 Desired Future State", level=1)

add_para(doc, (
    "The future-state architecture aligns with the Enterprise Target Architecture "
    "and adopts the common architectural principles defined by the CTO office."
))

add_para(doc, (
    f"The {PROJECT_NAME} domain does not create an independent architecture. "
    "Instead it consumes and contributes to the common enterprise architecture."
))

add_para(doc, "The future state assumes:")

future_assumptions = [
    "Enterprise Connectivity Services (ECS) is used for system integration.",
    "Major entity changes are published to the ECS message bus to notify other systems.",
    "Client data is consumed from enterprise mastered entities.",
    "Property information is consumed from enterprise mastered entities.",
    "Enterprise identifiers are adopted.",
    "Reconciliation is automated where practical.",
    "New integrations conform to published enterprise contracts.",
    "Dataverse (EU-hosted) serves as the single source of truth.",
    "Power Apps model-driven apps provide the user interface.",
    "Copilot for Sales provides AI-powered client matching.",
]
for item in future_assumptions:
    add_bullet(doc, item)

add_para(doc, "Future State Architecture", bold=True)

add_para(doc, "In the future state:")

future_state_items = [
    f"{PROJECT_NAME} systems remain authoritative for {PROJECT_NAME}-specific operational processes.",
    "Shared business entities are consumed from enterprise services.",
    "Reporting is driven from governed enterprise data.",
    "AI capabilities consume governed enterprise information.",
    "New systems align to enterprise contracts and standards.",
]
for item in future_state_items:
    add_bullet(doc, item)

# Target state components
add_para(doc, "Target State Components:", bold=True)
add_table_from_rows(doc,
    ["Layer", "Components"],
    [
        ["Presentation", "Model-Driven Apps, Power BI Dashboards, Copilot for Sales, Outlook Integration"],
        ["Application", "KF_Core, KF_Europe, Country Solutions, Service Line Solutions"],
        ["Data", "Dataverse, SharePoint, Power BI"],
        ["Integration", "Outlook, SharePoint, D365 Finance, CI-Journeys, Loqate, ECS (change bus)"],
        ["Security", "Entra ID, MFA, Conditional Access, Audit Trails"],
    ],
)

# ECS change notification
add_para(doc, "ECS Change Notification:", bold=True)
add_para(doc, (
    "Whenever a Major entity is created or updated in Dataverse, a change notification "
    "is published to the Knight Frank ECS (Enterprise Connectivity Services) platform - "
    "the internal notification and message bus that notifies other systems that a change "
    "has happened. Candidate Major entities are the Client (Account, Contact), Property "
    "(kf_Site, kf_Property) and Deal (kf_Deal) domains; the definitive list is to be "
    "confirmed with the TDA. Notifications are logged in kf_IntegrationLog."
))

# Standards compliance
add_para(doc, "Standards, PADs, and Blueprints:", bold=True)
add_table_from_rows(doc,
    ["Standard/Blueprint", "Status", "Relevance", "Compliance"],
    [
        ["CTO Architecture Principles", "Referenced", "High", "Compliant"],
        ["Enterprise data residency standards", "TBD", "High", "Compliant (EU-hosted)"],
        ["Security baseline", "TBD", "High", "Compliant (Entra ID, MFA, encryption)"],
        ["Integration patterns", "TBD", "Medium", "Compliant (API-first, standard connectors)"],
        ["Power Platform Centre of Excellence", "Referenced", "Medium", "Aligned"],
    ],
)

# Target state capabilities
add_para(doc, "Target State Capabilities by Phase:", bold=True)

target_caps = {
    "Client Management (Phase 0)": [
        "Single source of truth for all client data",
        "Two-tier hierarchy: Brand/Group to Legal Entity",
        "SIC-coded industry classification (66 KF sectors)",
        "Multi-country, multi-service line view",
    ],
    "Property Management (Phase 0)": [
        "Canonical physical sites with addresses and coordinates",
        "Commercial and residential properties",
        "Energy ratings and EPC data",
        "10 service lines read same property record",
    ],
    "Deal Management (Phase 1)": [
        "8-stage BPF from lead generation to completion",
        "12 CM entities for full deal lifecycle",
        "Regulatory gates per market",
        "Cross-border portfolio management",
    ],
    "Financial Management (Phase 1)": [
        "WIP tracking with % complete tied to BPF stage",
        "Fee management with billing triggers",
        "9 integration flows to D365 Finance",
        "Transaction report automation",
    ],
    "Compliance and Governance (Phase 0)": [
        "KYC/AML checks at legal entity level",
        "GDPR consent tracking with audit trail",
        "7-year retention with exportable audit logs",
        "Red flag tracking and conflict checks",
    ],
    "Integration and Analytics (Phase 1)": [
        "Outlook email tracking and activity logging",
        "SharePoint deal folder auto-provisioning",
        "CI-Journeys marketing handoff",
        "Power BI dashboards and reports",
    ],
}

for cap_name, items in target_caps.items():
    add_para(doc, cap_name, bold=True)
    for item in items:
        add_bullet(doc, item)

# ---- 7.X.6 Transition States ----
add_heading(doc, f"7.X.6 Transition States", level=1)

add_para(doc, (
    "The implementation follows a phased approach, starting with a foundation "
    "layer and building toward full capability across all service lines and countries."
))

add_para(doc, "Implementation Roadmap:", bold=True)
add_table_from_rows(doc,
    ["Phase", "Scope", "Duration", "Status"],
    [
        ["Phase 0", "Foundation (L2-L4): Account, Contact, Property, Compliance", "8-10 weeks", "Planning"],
        ["Phase 1", "Paris CM Deep Build (L5-L6): Deal, WIP, Finance bridge", "12-16 weeks", "Planning"],
        ["Phase 2", "Madrid + EIT (L6-L7): Cross-border portfolios", "10-14 weeks", "Not started"],
        ["Phase 3", "Additional Service Lines: OSS, Valuations", "Future", "Not started"],
        ["Phase 4", "Residential / Private Office", "Future", "Not started"],
        ["Phase 5", "Regional Expansion", "Future", "Not started"],
        ["Phase 6", "Hub Replacement", "Future", "Not started"],
        ["Phase 7", "Consolidated Finance ERP", "Future", "Not started"],
    ],
)

# Regional scope
add_para(doc, "Regional Scope:", bold=True)
add_table_from_rows(doc,
    ["Region", "Included", "Phase", "Notes"],
    [
        ["France", "Yes", "Phase 0-1", "MVP, CM team pilot"],
        ["Germany", "Yes", "Phase 0", "Foundation only, CM in Phase 2"],
        ["Spain", "Yes", "Phase 0", "Foundation only, CM in Phase 2"],
        ["Poland", "Yes", "Phase 0", "Foundation only, CM in Phase 2"],
    ],
)

# Service line scope
add_para(doc, "Service Line Scope:", bold=True)
add_table_from_rows(doc,
    ["Service Line", "Included", "Phase", "Notes"],
    [
        ["Capital Markets", "Yes", "Phase 0-1", "MVP"],
        ["Occupier Strategy and Solutions", "Future", "Phase 3", "TBD"],
        ["Valuations", "Future", "Phase 3", "TBD"],
        ["Residential", "Future", "Phase 4", "TBD"],
        ["Private Office", "Future", "Phase 4", "TBD"],
    ],
)

# Key milestones
add_para(doc, "Key Milestones:", bold=True)

milestones = [
    "TDA approval required before implementation.",
    "Phase 0 delivers foundation entities across all four countries.",
    "Phase 1 delivers Paris Capital Markets deep build with 8-stage BPF.",
    "Phase 2 extends to Madrid and European Investment Team.",
    "Subsequent phases add service lines and countries incrementally.",
    "Each layer is a separate managed solution.",
    "No unmanaged customisations in TEST, UAT, or PROD.",
]
for item in milestones:
    add_bullet(doc, item)

# ---- Save ----
doc.save(OUTPUT)
print(f"Document saved to: {OUTPUT}")
