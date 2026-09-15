#!/usr/bin/env python3
"""
Generate EuroCRM Solution Overview Document (SOD) as a Word document.
Consolidates all wiki content into a single formatted .docx file.
"""

import os
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT

# Configuration
VAULT_ROOT = Path(r"C:\Source\Obsidian\Projects\POC-EuroCRM-sb\POC-EuroCRM-sb-Vault")
WIKI_DIR = VAULT_ROOT / "wiki"
OUTPUT_FILE = VAULT_ROOT / "archive" / "EuroCRM_Solution_Overview_Document_v2.docx"


def read_wiki_file(filename):
    """Read a wiki file and return its content."""
    filepath = WIKI_DIR / filename
    if not filepath.exists():
        # Notes may live in approach sub-folders; resolve by filename across the wiki tree
        matches = list(WIKI_DIR.rglob(filename))
        if not matches:
            return ""
        filepath = matches[0]
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def parse_markdown_table(content, table_name):
    """Extract a markdown table from content by name."""
    lines = content.split("\n")
    in_table = False
    table_lines = []
    
    for line in lines:
        if table_name.lower() in line.lower():
            in_table = True
            continue
        if in_table:
            if line.strip().startswith("|"):
                table_lines.append(line)
            elif table_lines:
                break
    
    if not table_lines:
        return None
    
    # Parse table
    rows = []
    for line in table_lines:
        if "---" in line:
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if cells:
            rows.append(cells)
    
    return rows if rows else None


def add_heading(doc, text, level):
    """Add a heading to the document."""
    heading = doc.add_heading(text, level=level)
    return heading


def add_paragraph(doc, text, bold=False, italic=False):
    """Add a paragraph to the document."""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = bold
    run.italic = italic
    return para


def add_table(doc, rows, headers=True):
    """Add a table to the document."""
    if not rows:
        return
    
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    for i, row in enumerate(rows):
        for j, cell_text in enumerate(row):
            cell = table.cell(i, j)
            cell.text = cell_text
            if i == 0 and headers:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True
    
    return table


def create_sod():
    """Create the Solution Overview Document."""
    doc = Document()
    
    # Set default font
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Calibri"
    font.size = Pt(11)
    
    # Title page
    doc.add_paragraph()
    doc.add_paragraph()
    title = doc.add_heading("EuroCRM Solution Overview Document", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph()
    subtitle = doc.add_paragraph("Knight Frank European CRM Platform")
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].bold = True
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    # Document info
    info_table = doc.add_table(rows=6, cols=2)
    info_table.style = "Table Grid"
    info_data = [
        ("Document Title", "EuroCRM Solution Overview Document"),
        ("Author", "Gary Newport"),
        ("Version", "0.1"),
        ("Status", "Draft"),
        ("Date", "26/08/2026"),
        ("Classification", "Internal - Confidential"),
    ]
    for i, (label, value) in enumerate(info_data):
        info_table.cell(i, 0).text = label
        info_table.cell(i, 1).text = value
        for paragraph in info_table.cell(i, 0).paragraphs:
            for run in paragraph.runs:
                run.bold = True
    
    doc.add_page_break()
    
    # Version History
    add_heading(doc, "Version History", 1)
    version_rows = [
        ["Version", "Comments", "Author", "Status", "Date"],
        ["0.1", "Initial draft", "Gary Newport", "Draft", "26/08/2026"],
    ]
    add_table(doc, version_rows)
    
    doc.add_paragraph()
    
    # Table of Contents placeholder
    add_heading(doc, "Table of Contents", 1)
    add_paragraph(doc, "[Table of Contents to be generated in Word]", italic=True)
    
    doc.add_page_break()
    
    # Executive Summary
    add_heading(doc, "Executive Summary", 1)
    add_paragraph(doc, 
        "European CRM solution covering France, Germany, Spain, and Poland. "
        "This document defines the architecture approach for review and approval "
        "by the Technical Design Authority (TDA)."
    )
    add_paragraph(doc,
        "The EuroCRM initiative addresses the need for a unified CRM platform "
        "across four European offices. Client intelligence is fragmented across "
        "local brokers, manual reporting doesn't scale, and cross-sell opportunities "
        "are missed."
    )
    
    doc.add_page_break()
    
    # Business Context
    add_heading(doc, "Business Context", 1)
    
    business_context = read_wiki_file("business-context.md")
    if business_context:
        add_heading(doc, "Current State", 2)
        add_paragraph(doc, "Four separate European offices: France, Germany, Spain, Poland")
        add_paragraph(doc, "Existing CRM systems vary by region")
        add_paragraph(doc, "No unified customer data platform")
        add_paragraph(doc, "Client knowledge sits with individual brokers in email, Excel trackers, and shared folders")
        add_paragraph(doc, "Transaction reports are built manually in Excel")
        
        add_heading(doc, "Problem Statement", 2)
        add_paragraph(doc, "Core Problems:", bold=True)
        doc.add_paragraph("Fragmented Client Intelligence — If a broker in Madrid is tracking an investor whose strategy matches a Paris asset, neither side knows", style="List Number")
        doc.add_paragraph("Manual Reporting — Price, buyer, seller, asset, and fee data assembled manually after every close", style="List Number")
        doc.add_paragraph("Missing Cross-Sell Opportunities — Fragmented data means opportunities for cross-border and cross-service-line collaboration are lost", style="List Number")
        
        add_heading(doc, "Regional Requirements", 2)
        regional_rows = [
            ["Region", "Key Requirements", "Regulatory Notes"],
            ["France", "City pre-emption, notarial deed requirements", "CNIL, GDPR"],
            ["Germany", "TBD", "BDSG, GDPR"],
            ["Spain", "Right-of-refusal on listed buildings", "GDPR"],
            ["Poland", "TBD", "GDPR"],
        ]
        add_table(doc, regional_rows)
        
        add_heading(doc, "Drivers", 2)
        doc.add_paragraph("Need for consolidated customer view across service lines and countries", style="List Bullet")
        doc.add_paragraph("Regulatory compliance across jurisdictions", style="List Bullet")
        doc.add_paragraph("Operational efficiency across regions", style="List Bullet")
        doc.add_paragraph("Ability to scale reporting as deal volume grows", style="List Bullet")
        
        add_heading(doc, "Constraints", 2)
        doc.add_paragraph("Regional data residency requirements", style="List Bullet")
        doc.add_paragraph("Existing system integrations", style="List Bullet")
        doc.add_paragraph("TDA governance oversight", style="List Bullet")
        doc.add_paragraph("Cross-border data sharing agreements required", style="List Bullet")
    
    doc.add_page_break()
    
    # Business Goals and Objectives
    add_heading(doc, "Business Goals and Objectives", 1)
    
    business_goals = read_wiki_file("business-goals.md")
    if business_goals:
        add_heading(doc, "MVP Success Criteria", 2)
        add_paragraph(doc, '"Who is this client to Knight Frank across every service line, every country?"', italic=True)
        add_paragraph(doc, '"What does our EU pipeline look like?"', italic=True)
        add_paragraph(doc, '"How do we run CM deals?"', italic=True)
        
        add_heading(doc, "Strategic Objectives", 2)
        doc.add_paragraph("Unified customer view across European operations", style="List Bullet")
        doc.add_paragraph("Compliance with regional data regulations (GDPR, local requirements)", style="List Bullet")
        doc.add_paragraph("Standardised business processes across all four markets", style="List Bullet")
        doc.add_paragraph("Cross-border and cross-service-line collaboration", style="List Bullet")
        doc.add_paragraph("Scalable reporting as deal volume grows", style="List Bullet")
    
    doc.add_page_break()
    
    # Key Stakeholders
    add_heading(doc, "Key Stakeholders", 1)
    
    stakeholders = read_wiki_file("key-stakeholders.md")
    if stakeholders:
        stakeholder_rows = [
            ["Name", "Role", "Region", "Interest", "Influence"],
            ["Gary Newport", "Author/Solution Lead", "Europe", "High", "High"],
            ["TDA", "Technical Design Authority", "Enterprise", "High", "High"],
            ["CTO", "Chief Technology Officer", "Enterprise", "High", "High"],
            ["European MDs", "Regional Managing Directors", "France, Germany, Spain, Poland", "High", "High"],
            ["CM Team Heads", "Capital Markets Service Line Leaders", "Europe", "High", "Medium"],
            ["Legal/Compliance", "Data Protection Officers", "Europe", "High", "Medium"],
            ["Finance Team", "Financial Controllers", "Europe", "Medium", "Medium"],
            ["IT Operations", "Infrastructure & Support", "Enterprise", "Medium", "Medium"],
            ["End Users", "Brokers, Analysts, Support Staff", "Europe", "High", "Low"],
        ]
        add_table(doc, stakeholder_rows)
        
        add_heading(doc, "RACI Matrix", 2)
        raci_rows = [
            ["Activity", "Solution Lead", "TDA", "CTO", "Regional MDs", "CM Team", "Legal", "Finance", "IT Ops"],
            ["Architecture Design", "R", "A", "C", "C", "C", "C", "C", "C"],
            ["Environment Setup", "R", "A", "C", "I", "I", "I", "I", "R"],
            ["Data Model Design", "R", "A", "C", "C", "C", "C", "C", "I"],
            ["Security Configuration", "R", "A", "C", "I", "I", "C", "I", "R"],
            ["Integration Design", "R", "A", "C", "I", "I", "I", "C", "R"],
            ["UAT Coordination", "R", "A", "I", "C", "R", "C", "C", "I"],
            ["Go-Live Approval", "C", "A", "R", "C", "C", "C", "C", "C"],
            ["Post-Go-Live Support", "C", "I", "I", "I", "I", "I", "I", "R"],
        ]
        add_table(doc, raci_rows)
        add_paragraph(doc, "R = Responsible, A = Accountable, C = Consulted, I = Informed", italic=True)
    
    doc.add_page_break()
    
    # Business Capabilities
    add_heading(doc, "Business Capabilities", 1)
    
    capabilities = read_wiki_file("business-capabilities.md")
    if capabilities:
        add_heading(doc, "Core CRM Capabilities", 2)
        
        add_heading(doc, "Client Management", 3)
        doc.add_paragraph("Account Management: Legal entity records with SIC-coded industry classification (66 KF sectors)", style="List Bullet")
        doc.add_paragraph("Contact Management: Individual contacts linked to accounts with roles and preferences", style="List Bullet")
        doc.add_paragraph("Brand/Group Hierarchy: Two-tier model: Brand/Group → Legal Entity", style="List Bullet")
        doc.add_paragraph("Industry Classification: SIC codes mapped to KF sectors with gap analysis", style="List Bullet")
        
        add_heading(doc, "Property Management", 3)
        doc.add_paragraph("Site Management: Canonical physical sites with addresses and coordinates", style="List Bullet")
        doc.add_paragraph("Property Management: Commercial and residential properties linked to sites", style="List Bullet")
        doc.add_paragraph("Residential Property: Sales, lettings, and property management", style="List Bullet")
        doc.add_paragraph("Energy Ratings: EPC and energy performance data", style="List Bullet")
        
        add_heading(doc, "Deal Management", 3)
        doc.add_paragraph("Pipeline Management: 8-stage BPF from lead generation to completion", style="List Bullet")
        doc.add_paragraph("BPF Lifecycle: Stage-specific activities, documents, and regulatory gates", style="List Bullet")
        doc.add_paragraph("Due Diligence: NDA, KYC, data room access, red flag tracking", style="List Bullet")
        doc.add_paragraph("Regulatory Gates: City pre-emption (France), right-of-refusal (Spain), notarial deed", style="List Bullet")
        
        add_heading(doc, "Financial Management", 3)
        doc.add_paragraph("WIP Tracking: Work-in-progress with % complete tied to BPF stage", style="List Bullet")
        doc.add_paragraph("Fee Management: Fee schedules with agreed fees and billing triggers", style="List Bullet")
        doc.add_paragraph("Integration Bridge: 9 flows to D365 Finance (project creation, WIP sync, transaction reports)", style="List Bullet")
        doc.add_paragraph("Transaction Reports: Auto-generated reports for deal completion", style="List Bullet")
        
        add_heading(doc, "Compliance & Governance", 3)
        doc.add_paragraph("KYC/AML: Know Your Customer checks at legal entity level", style="List Bullet")
        doc.add_paragraph("GDPR Consent: Data processing consent tracking with audit trail", style="List Bullet")
        doc.add_paragraph("Audit Export: 7-year retention with exportable audit logs", style="List Bullet")
        doc.add_paragraph("Red Flag Tracking: Conflict checks and risk identification", style="List Bullet")
        
        add_heading(doc, "Integration & Analytics", 3)
        doc.add_paragraph("Outlook Integration: Email tracking and activity logging", style="List Bullet")
        doc.add_paragraph("SharePoint Integration: Deal folder auto-provisioning and document management", style="List Bullet")
        doc.add_paragraph("Marketing Handoff: CI-Journeys integration for campaign automation", style="List Bullet")
        doc.add_paragraph("Power BI Dashboards: Regional reporting and analytics", style="List Bullet")
    
    doc.add_page_break()
    
    # KPIs and Success
    add_heading(doc, "KPIs and Success Metrics", 1)
    
    kpis = read_wiki_file("kpis-and-success.md")
    if kpis:
        add_heading(doc, "Data Quality", 2)
        kpi_rows = [
            ["KPI", "Target", "Measurement", "Frequency"],
            ["Client data accuracy", "98%", "Data quality reports", "Weekly"],
            ["Property data completeness", "95%", "Completeness checks", "Weekly"],
            ["Duplicate account rate", "<2%", "Duplicate detection", "Monthly"],
            ["Industry classification accuracy", "99%", "SIC code validation", "Monthly"],
        ]
        add_table(doc, kpi_rows)
        
        add_heading(doc, "User Adoption", 2)
        adoption_rows = [
            ["KPI", "Target", "Measurement", "Frequency"],
            ["Active users", "80% of licensed users", "System login/activity", "Weekly"],
            ["Daily active users", "70% of licensed users", "System login/activity", "Daily"],
            ["User satisfaction score", "4.0/5.0", "Survey feedback", "Monthly"],
            ["Training completion rate", "100%", "Training records", "Per phase"],
        ]
        add_table(doc, adoption_rows)
        
        add_heading(doc, "Process Efficiency", 2)
        efficiency_rows = [
            ["KPI", "Target", "Measurement", "Frequency"],
            ["Deal cycle time", "20% reduction", "BPF analytics", "Monthly"],
            ["Time to create deal record", "<5 minutes", "Activity tracking", "Monthly"],
            ["Document retrieval time", "<30 seconds", "SharePoint metrics", "Monthly"],
            ["Report generation time", "<2 minutes", "Power BI metrics", "Monthly"],
        ]
        add_table(doc, efficiency_rows)
    
    doc.add_page_break()
    
    # Solution Scope
    add_heading(doc, "Solution Scope", 1)
    
    add_heading(doc, "In-Scope", 2)
    scope_in = read_wiki_file("solution-scope-in-scope.md")
    if scope_in:
        add_heading(doc, "Platform", 3)
        doc.add_paragraph("Dataverse (EU-hosted)", style="List Bullet")
        doc.add_paragraph("Power Apps Model-Driven Apps", style="List Bullet")
        doc.add_paragraph("Power Automate (Cloud Flows)", style="List Bullet")
        doc.add_paragraph("Power BI (Dashboards and Reports)", style="List Bullet")
        doc.add_paragraph("Copilot for Sales (Pilot)", style="List Bullet")
        doc.add_paragraph("Outlook Integration", style="List Bullet")
        doc.add_paragraph("SharePoint Integration", style="List Bullet")
        
        add_heading(doc, "Service Lines", 3)
        doc.add_paragraph("Capital Markets (MVP)", style="List Bullet")
        doc.add_paragraph("Occupier Strategy & Solutions (Future)", style="List Bullet")
        doc.add_paragraph("Valuations (Future)", style="List Bullet")
        doc.add_paragraph("Residential (Future)", style="List Bullet")
        doc.add_paragraph("Private Office (Future)", style="List Bullet")
        
        add_heading(doc, "Countries", 3)
        doc.add_paragraph("France (MVP)", style="List Bullet")
        doc.add_paragraph("Germany (Phase 0 foundation)", style="List Bullet")
        doc.add_paragraph("Spain (Phase 0 foundation)", style="List Bullet")
        doc.add_paragraph("Poland (Phase 0 foundation)", style="List Bullet")
        
        add_heading(doc, "Entities", 3)
        entity_rows = [
            ["Entity", "Phase", "Category"],
            ["Account", "Phase 0", "CRM Lite"],
            ["Contact", "Phase 0", "CRM Lite"],
            ["kf_Property", "Phase 0", "CRM Lite"],
            ["kf_EnergyRating", "Phase 0", "Compliance"],
            ["kf_GDPRRequest", "Phase 0", "Compliance"],
            ["kf_AuditExport", "Phase 0", "Compliance"],
            ["kf_SICCode", "Phase 0", "Supporting"],
            ["kf_Deal", "Phase 1", "CM Deep Build"],
            ["kf_DealProperty", "Phase 1", "Core Shared"],
            ["kf_Pitch", "Phase 1", "CM Deep Build"],
            ["kf_NDA", "Phase 1", "CM Deep Build"],
            ["kf_Bid", "Phase 1", "CM Deep Build"],
            ["kf_DDMilestone", "Phase 1", "CM Deep Build"],
            ["kf_RedFlag", "Phase 1", "CM Deep Build"],
            ["kf_FeeSchedule", "Phase 1", "CM Deep Build"],
            ["kf_KYCRecord", "Phase 1", "CM Deep Build"],
            ["kf_InvestorProfile", "Phase 1", "CM Deep Build"],
            ["kf_DataRoomAccess", "Phase 1", "CM Deep Build"],
            ["kf_TransactionReport", "Phase 1", "CM Deep Build"],
            ["kf_StageGateRule", "Phase 1", "Supporting"],
            ["kf_IntegrationLog", "Phase 1", "Supporting"],
            ["Lead", "Phase 1", "Marketing"],
        ]
        add_table(doc, entity_rows)
    
    add_heading(doc, "Out-of-Scope", 2)
    scope_out = read_wiki_file("solution-scope-out-of-scope.md")
    if scope_out:
        add_heading(doc, "Service Lines", 3)
        doc.add_paragraph("Occupier Strategy & Solutions (Phase 3)", style="List Bullet")
        doc.add_paragraph("Valuations (Phase 3)", style="List Bullet")
        doc.add_paragraph("Residential (Phase 4)", style="List Bullet")
        doc.add_paragraph("Private Office (Phase 4)", style="List Bullet")
        
        add_heading(doc, "Regions", 3)
        doc.add_paragraph("APAC (Phase 5)", style="List Bullet")
        doc.add_paragraph("Americas (Phase 5)", style="List Bullet")
        doc.add_paragraph("Middle East (Phase 5)", style="List Bullet")
        
        add_heading(doc, "Features", 3)
        doc.add_paragraph("Marketing automation (CI-Journeys integration only)", style="List Bullet")
        doc.add_paragraph("Legacy system decommissioning", style="List Bullet")
        doc.add_paragraph("Custom development beyond platform capabilities", style="List Bullet")
        doc.add_paragraph("Third-party system replacements", style="List Bullet")
        doc.add_paragraph("Mobile app development (Phase 2 consideration)", style="List Bullet")
        doc.add_paragraph("Advanced AI/ML beyond Copilot for Sales", style="List Bullet")
    
    doc.add_page_break()
    
    # Solution Architecture
    add_heading(doc, "Solution Architecture", 1)
    
    add_heading(doc, "Overview Diagrams", 2)
    add_paragraph(doc, "See [[wiki/architecture-overview-diagrams]] for PlantUML diagrams.")
    add_paragraph(doc, "Architecture diagrams include:", bold=True)
    doc.add_paragraph("Solution Architecture — Full component view showing layers, data domains, and integrations", style="List Bullet")
    doc.add_paragraph("Layered Solution Model — L0-L7 layer hierarchy and extension rules", style="List Bullet")
    doc.add_paragraph("Data Flow & Integrations — How data flows through the system and external integrations", style="List Bullet")
    
    add_heading(doc, "Key Components", 2)
    arch_key = read_wiki_file("architecture-key-components.md")
    if arch_key:
        add_paragraph(doc, "Platform Decision: Power Apps model-driven apps on Dataverse", bold=True)
        
        add_heading(doc, "Layered Architecture", 3)
        add_paragraph(doc, "See [[wiki/solution-package-model]] for L0-L7 model.")
        layer_rows = [
            ["Layer", "Name", "Purpose"],
            ["L0", "Platform", "Dataverse foundation"],
            ["L1", "KF_Core", "40+ table shells, option sets"],
            ["L2", "KF_Europe", "EUR defaults, GDPR baseline"],
            ["L3", "Country", "KF_France, KF_Germany, KF_Poland, KF_Spain"],
            ["L4", "Region", "KF_CapitalMarkets_Core"],
            ["L5", "Service Line", "KF_CM_France, KF_CM_Spain"],
            ["L6", "Cross-Border", "KF_EIT"],
        ]
        add_table(doc, layer_rows)
        
        add_heading(doc, "Data Domains", 3)
        domain_rows = [
            ["Domain", "Key Entities", "Purpose"],
            ["Client", "Account, Contact, InvestorProfile", "Single view across service lines/countries"],
            ["Property", "kf_Site, kf_Property, kf_ResProperty", "Canonical physical asset with commercial/residential split"],
            ["Deal", "kf_Deal, kf_Pitch, kf_NDA, kf_Bid", "12 entities for 8-stage lifecycle"],
            ["Compliance", "kf_KYCRecord, kf_NDA, kf_GDPRRequest", "KYC at legal entity level"],
            ["Finance", "kf_FeeSchedule, kf_WIP, kf_TransactionReport", "CRM deal → Finance project"],
        ]
        add_table(doc, domain_rows)
    
    add_heading(doc, "Business Architecture", 2)
    arch_biz = read_wiki_file("architecture-business.md")
    if arch_biz:
        add_paragraph(doc, "Business process models and capability mapping.")
        add_paragraph(doc, "See [[wiki/architecture-business]] for detailed process flows.")
    
    add_heading(doc, "Application Architecture", 2)
    arch_app = read_wiki_file("architecture-application.md")
    if arch_app:
        add_paragraph(doc, "Application component design and integration patterns.")
        add_paragraph(doc, "See [[wiki/architecture-application]] for detailed component design.")
    
    add_heading(doc, "Data Architecture", 2)
    arch_data = read_wiki_file("architecture-data.md")
    if arch_data:
        add_paragraph(doc, "Core Data Domains:", bold=True)
        doc.add_paragraph("[[wiki/client-data-model]] — One client, one view", style="List Bullet")
        doc.add_paragraph("[[wiki/property-data-model]] — Site, Property, Deal", style="List Bullet")
        doc.add_paragraph("[[wiki/capital-markets-data-model]] — 12 entities for deal lifecycle", style="List Bullet")
        doc.add_paragraph("[[wiki/wip-data-model]] — Work in progress and revenue tracking", style="List Bullet")
        
        add_paragraph(doc, "Taxonomy Standards:", bold=True)
        doc.add_paragraph("SIC to KF Client Sector mapping (66 sectors)", style="List Bullet")
        doc.add_paragraph("HILUCS to KF Asset Class mapping", style="List Bullet")
    
    add_heading(doc, "Technology Architecture", 2)
    arch_tech = read_wiki_file("architecture-technology.md")
    if arch_tech:
        add_paragraph(doc, "Infrastructure, hosting, and technology stack decisions.")
        add_paragraph(doc, "See [[wiki/architecture-technology]] for detailed technology stack.")
    
    doc.add_page_break()
    
    # Alignment with Enterprise Architecture
    add_heading(doc, "Alignment with Enterprise Architecture", 1)
    
    add_heading(doc, "Principles Compliance", 2)
    arch_principles = read_wiki_file("architecture-principles-compliance.md")
    if arch_principles:
        add_paragraph(doc, "The CTO Architecture Principles document is referenced as a dependency.")
        add_paragraph(doc, "See [[wiki/architecture-principles-compliance]] for mapping of solution design to enterprise standards.")
        
        principles_rows = [
            ["Principle", "Compliance Status", "Notes"],
            ["Cloud-first", "✅ Compliant", "Dataverse (EU-hosted), Power Platform"],
            ["Security by design", "✅ Compliant", "Entra ID, MFA, encryption, audit trails"],
            ["Data residency", "✅ Compliant", "EU-hosted Dataverse, regional BUs"],
            ["Scalability", "✅ Compliant", "Power Platform autoscaling, Dataverse"],
            ["Integration-first", "✅ Compliant", "9 Finance flows, Outlook, SharePoint, CI-Journeys"],
            ["Modularity", "✅ Compliant", "L0-L7 layer model, managed solutions"],
            ["Compliance", "✅ Compliant", "KYC, GDPR, audit trails, regulatory gates"],
            ["User experience", "✅ Compliant", "Model-driven apps, Copilot for Sales"],
            ["Cost optimisation", "✅ Compliant", "Power Platform licensing, phased rollout"],
            ["Future-proofing", "✅ Compliant", "Layer model supports new regions/service lines"],
        ]
        add_table(doc, principles_rows)
    
    add_heading(doc, "Target State Alignment", 2)
    arch_target = read_wiki_file("architecture-target-state.md")
    if arch_target:
        add_paragraph(doc, "Standards, PADs, and Blueprints relevant to this SOD:")
        target_rows = [
            ["Standard/Blueprint", "Status", "Notes"],
            ["CTO Architecture Principles", "Referenced", "Pending review"],
            ["Enterprise data residency standards", "TBD", "Regional compliance required"],
            ["Security baseline", "TBD", "TDA alignment needed"],
            ["Power Platform Centre of Excellence", "Referenced", "Aligned"],
        ]
        add_table(doc, target_rows)
    
    doc.add_page_break()
    
    # Dependencies and Constraints
    add_heading(doc, "Dependencies and Constraints", 1)
    
    deps = read_wiki_file("dependencies-and-constraints.md")
    if deps:
        add_paragraph(doc, "Key dependencies:", bold=True)
        doc.add_paragraph("TDA approval required before implementation", style="List Bullet")
        doc.add_paragraph("CTO Architecture Principles review", style="List Bullet")
        doc.add_paragraph("Regional legal and compliance review", style="List Bullet")
        doc.add_paragraph("Enterprise integration platform availability", style="List Bullet")
        
        add_heading(doc, "Constraints", 2)
        doc.add_paragraph("Regional data residency requirements", style="List Bullet")
        doc.add_paragraph("Existing system integrations", style="List Bullet")
        doc.add_paragraph("TDA governance oversight", style="List Bullet")
        doc.add_paragraph("Budget and resource limitations (TBD)", style="List Bullet")
    
    doc.add_page_break()
    
    # Functional and Non-Functional Requirements
    add_heading(doc, "Functional and Non-Functional Requirements", 1)
    
    add_heading(doc, "Functional Requirements", 2)
    add_paragraph(doc, "Requirements to be gathered from business stakeholders across all four regions.")
    add_paragraph(doc, "See [[wiki/functional-requirements]] for detailed requirements.")
    
    add_heading(doc, "Non-Functional Requirements", 2)
    add_paragraph(doc, "Performance, security, and compliance requirements to be defined.")
    add_paragraph(doc, "See [[wiki/functional-non-functional-requirements]] for detailed requirements.")
    
    doc.add_page_break()
    
    # Risks and Issues
    add_heading(doc, "Risks and Issues", 1)
    
    risks = read_wiki_file("risks-and-issues.md")
    if risks:
        add_paragraph(doc, "Risk register to be populated during design phase.")
        add_paragraph(doc, "See [[wiki/risks-and-issues]] for detailed risk register.")
    
    doc.add_page_break()
    
    # Solution Options and Trade-offs
    add_heading(doc, "Solution Options and Trade-offs", 1)
    
    options = read_wiki_file("solution-options.md")
    if options:
        add_paragraph(doc, "Options analysis to be completed with vendor evaluation and architecture assessment.")
        add_paragraph(doc, "See [[wiki/solution-options]] for detailed options analysis.")
    
    doc.add_page_break()
    
    # Implementation Roadmap
    add_heading(doc, "Implementation Roadmap", 1)
    
    add_heading(doc, "Phases", 2)
    roadmap_phases = read_wiki_file("roadmap-phases.md")
    if roadmap_phases:
        phase_rows = [
            ["Phase", "Label", "Duration", "Layers", "Status"],
            ["Phase 0", "Foundation", "8-10 weeks", "L2-L4", "Planning"],
            ["Phase 1", "Paris CM Deep Build", "12-16 weeks", "L5-L6", "Planning"],
            ["Phase 2", "Madrid + EIT CM Deep Build", "10-14 weeks", "L6-L7", "Not started"],
            ["Phase 3", "Additional Service Lines", "Future", "L5", "Not started"],
            ["Phase 4", "Residential / Private Office", "Future", "L5-L7", "Not started"],
            ["Phase 5", "Regional Expansion", "Future", "L3", "Not started"],
            ["Phase 6", "Hub Replacement", "Future", "Integration", "Not started"],
            ["Phase 7", "Consolidated Finance ERP", "Future", "Integration", "Not started"],
        ]
        add_table(doc, phase_rows)
    
    add_heading(doc, "Timelines", 2)
    roadmap_timelines = read_wiki_file("roadmap-timelines.md")
    if roadmap_timelines:
        add_paragraph(doc, "MVP Timeline (Phases 0-1): 20-26 weeks")
        add_paragraph(doc, "See [[wiki/roadmap-timelines]] for detailed timeline view and Gantt chart.")
    
    add_heading(doc, "Key Dependencies", 2)
    roadmap_deps = read_wiki_file("roadmap-dependencies.md")
    if roadmap_deps:
        add_paragraph(doc, "See [[wiki/roadmap-dependencies]] for full dependency register.")
    
    doc.add_page_break()
    
    # Cost and Benefits Summary
    add_heading(doc, "Cost and Benefits Summary", 1)
    
    add_heading(doc, "Estimated Costs", 2)
    add_paragraph(doc, "CAPEX: N/A")
    add_paragraph(doc, "OPEX: N/A")
    add_paragraph(doc, "See [[wiki/cost-estimates]] for detailed cost modelling.")
    
    add_heading(doc, "Expected Benefits", 2)
    add_paragraph(doc, "Benefits realisation to be quantified during business case development.")
    add_paragraph(doc, "See [[wiki/expected-benefits]] for detailed benefits analysis.")
    
    doc.add_page_break()
    
    # Governance and Approval
    add_heading(doc, "Governance and Approval", 1)
    
    add_heading(doc, "Approval", 2)
    add_paragraph(doc, "Approvals are required from the identified Key Stakeholders along with TDA approval.")
    add_paragraph(doc, "See [[wiki/governance-approval]] for the approval workflow.")
    
    add_heading(doc, "Governance Oversight", 2)
    add_paragraph(doc, "This solution is in the purview of the Technical Design Authority (TDA).")
    add_paragraph(doc, "See [[wiki/governance-oversight]] for governance structure and reporting.")
    
    doc.add_page_break()
    
    # Compliance
    add_heading(doc, "Compliance", 1)
    
    compliance = read_wiki_file("compliance.md")
    if compliance:
        add_paragraph(doc, "Regulatory and compliance requirements across all four European jurisdictions.")
        add_paragraph(doc, "See [[wiki/compliance]] for detailed compliance requirements.")
    
    doc.add_page_break()
    
    # Glossary
    add_heading(doc, "Glossary", 1)
    
    glossary = read_wiki_file("glossary.md")
    if glossary:
        add_paragraph(doc, "See [[wiki/glossary]] for complete glossary.")
    
    doc.add_page_break()
    
    # References
    add_heading(doc, "References", 1)
    
    add_paragraph(doc, "Source Documents:", bold=True)
    doc.add_paragraph("CTO Architecture Principles.pptx", style="List Bullet")
    doc.add_paragraph("European CRM Architecture Review 2.pdf", style="List Bullet")
    doc.add_paragraph("EU CRM Data Model.xlsx", style="List Bullet")
    doc.add_paragraph("European_CRM_Client_Industry_Master_Taxonomy.xlsx", style="List Bullet")
    doc.add_paragraph("European_CRM_Property360_Master_Taxonomy.xlsx", style="List Bullet")
    
    add_paragraph(doc, "Wiki Entries:", bold=True)
    doc.add_paragraph("[[wiki/problem-statement]]", style="List Bullet")
    doc.add_paragraph("[[wiki/solution-package-model]]", style="List Bullet")
    doc.add_paragraph("[[wiki/crm-lite-mvp-scope]]", style="List Bullet")
    doc.add_paragraph("[[wiki/client-data-model]]", style="List Bullet")
    doc.add_paragraph("[[wiki/property-data-model]]", style="List Bullet")
    doc.add_paragraph("[[wiki/capital-markets-data-model]]", style="List Bullet")
    doc.add_paragraph("[[wiki/wip-data-model]]", style="List Bullet")
    doc.add_paragraph("[[wiki/taxonomy-mappings]]", style="List Bullet")
    doc.add_paragraph("[[wiki/power-apps-rationale]]", style="List Bullet")
    doc.add_paragraph("[[wiki/data-model-overview]]", style="List Bullet")
    doc.add_paragraph("[[wiki/implementation-phases]]", style="List Bullet")
    doc.add_paragraph("[[wiki/data-model-core-tables]]", style="List Bullet")
    
    # Save document
    doc.save(OUTPUT_FILE)
    print(f"Document saved to: {OUTPUT_FILE}")
    return OUTPUT_FILE


if __name__ == "__main__":
    create_sod()
