#!/usr/bin/env python3.11
"""
GitHub Pages Index Generator
Generates a comprehensive index.md for the revstream1 GitHub Pages site.
"""

import json
from datetime import datetime
from pathlib import Path

def load_data():
    """Load all necessary data models"""
    base_path = Path("/home/ubuntu/revstream1/data_models")
    
    with open(base_path / "entities/entities.json") as f:
        entities = json.load(f)
    with open(base_path / "relations/relations.json") as f:
        relations = json.load(f)
    with open(base_path / "events/events.json") as f:
        events = json.load(f)
    with open(base_path / "timelines/timeline.json") as f:
        timeline = json.load(f)
    
    return entities, relations, events, timeline

def generate_executive_summary(entities, relations, events, timeline):
    """Generate the executive summary section"""
    
    last_updated = datetime.now().strftime("%Y-%m-%d")
    total_events = events["metadata"]["total_events"]
    criminal_events = events["metadata"]["criminal_threshold_events"]
    civil_events = events["metadata"]["civil_threshold_events"]
    total_entities = entities["metadata"]["total_entities"]
    total_relations = relations["metadata"]["total_relations"]
    timeline_start = min([e["date"] for e in timeline["timeline"]])
    timeline_end = max([e["date"] for e in timeline["timeline"]])
    
    summary = f"""# Revenue Stream Hijacking: Case 2025-137857 Analysis

**Last Updated:** {last_updated}

## Executive Summary

This repository provides a comprehensive, evidence-based analysis of the coordinated scheme to hijack the revenue stream of RegimA Zone Ltd (UK) and defraud the Faucitt Family Trust. The perpetrators, primarily **Peter Andrew Faucitt**, **Rynette Farrar**, and **Danie Bantjies**, executed a multi-faceted attack involving financial manipulation, identity fraud, trust violations, and evidence tampering.

**Key Statistics:**
- **Total Events Documented:** {total_events}
- **Criminal Threshold Events (95% burden of proof):** {criminal_events}
- **Civil Threshold Events (50% burden of proof):** {civil_events}
- **Entities Tracked:** {total_entities}
- **Relations Mapped:** {total_relations}
- **Timeline Span:** {timeline_start} to {timeline_end}
"""
    return summary

def generate_data_models_section(entities, relations, events, timeline):
    """Generate the data models section"""
    
    models = [
        {
            "name": "Entities",
            "version": entities["metadata"]["version"],
            "updated": entities["metadata"]["last_updated"].split("T")[0],
            "desc": "Detailed profiles of all individuals, organizations, and assets involved.",
            "link": "../data_models/entities/entities.json"
        },
        {
            "name": "Relations",
            "version": relations["metadata"]["version"],
            "updated": relations["metadata"]["last_updated"].split("T")[0],
            "desc": "A hypergraph-compatible model of the connections and interactions between entities.",
            "link": "../data_models/relations/relations.json"
        },
        {
            "name": "Events",
            "version": events["metadata"]["version"],
            "updated": events["metadata"]["last_updated"].split("T")[0],
            "desc": f"A catalog of all significant events, with {events['metadata']['criminal_threshold_events']} events meeting the 95% criminal burden of proof.",
            "link": "../data_models/events/events.json"
        },
        {
            "name": "Timeline",
            "version": timeline["metadata"]["version"],
            "updated": timeline["metadata"]["last_updated"].split("T")[0],
            "desc": "A chronologically ordered timeline of events, enhanced with criminal threshold markers.",
            "link": "../data_models/timelines/timeline.json"
        }
    ]
    
    section = """## I. Core Data Models (Refined)

The investigation is built upon a rigorously maintained set of data models that define the entities, their relationships, and the sequence of events. These models are continuously refined as new evidence emerges.

| Data Model | Version | Last Updated | Description | Link |
| :--- | :--- | :--- | :--- | :--- |
"""
    
    for model in models:
        section += f'| **{model["name"]}** | {model["version"]} | {model["updated"]} | {model["desc"]} | [{model["link"].split("/")[-1]}]({model["link"]}) |\n'
        
    return section

def generate_evidence_index_section():
    """Generate the evidence index section"""
    
    return """## II. Evidence Index & Cross-Reference

The evidence is sourced from two primary repositories:
- **revstream1** (this repository): Analysis, data models, and visualizations
- **ad-res-j7** (extended evidence): Primary source documents, annexures, and legal filings

### Key Evidence Directories in ad-res-j7

| Evidence Set | Description | File Count | Location |
| :--- | :--- | :--- | :--- |
| **ANNEXURES/JF01** | Shopify Plus email - THE FORENSIC TIME CAPSULE | 2 items | [ad-res-j7/ANNEXURES/JF01](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF01) |
| **ANNEXURES/JF02** | Business operations documentation | 3 items | [ad-res-j7/ANNEXURES/JF02](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF02) |
| **ANNEXURES/JF03** | Financial records and analysis | 5 items | [ad-res-j7/ANNEXURES/JF03](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF03) |
| **ANNEXURES/JF04** | CIPC company registration documents | 6 items | [ad-res-j7/ANNEXURES/JF04](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF04) |
| **ANNEXURES/JF05** | Correspondence evidence | 7 items | [ad-res-j7/ANNEXURES/JF05](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF05) |
| **ANNEXURES/JF06** | Court applications and filings | 5 items | [ad-res-j7/ANNEXURES/JF06](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF06) |
| **ANNEXURES/JF07** | Payment redirection documentation | 186 items | [ad-res-j7/ANNEXURES/JF07](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF07) |
| **ANNEXURES/JF08** | Evidence Package - Comprehensive fraud timeline | 43 items | [ad-res-j7/ANNEXURES/JF08](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF08) |
| **ANNEXURES/JF09** | Domain registration fraud evidence | 8 items | [ad-res-j7/ANNEXURES/JF09](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF09) |

### Special Findings (SF) Evidence

| Evidence ID | Description | Significance | Burden of Proof | Location |
| :--- | :--- | :--- | :--- | :--- |
| **SF1** | Bantjies Debt Documentation | Establishes Danie Bantjies\\' R18.685M debt and conflict of interest. | Civil (50%) & Criminal (95%) | [SF1_Bantjies_Debt_Documentation.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md) |
| **SF2** | Rynette Sage Control | Proves Rynette\\'s control of the accounting system and Pete\\'s email. | Criminal (95%) | [SF2_Sage_Screenshots_Rynette_Control.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md) |
| **SF3** | Strategic Logistics Stock Adjustment | Documents R5.4M stock fraud concealment. | Criminal (95%) | [SF3_Strategic_Logistics_Stock_Adjustment.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md) |
| **SF4** | SARS Audit Email | Evidence of tax fraud coordination. | Criminal (95%) | [SF4_SARS_Audit_Email.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF4_SARS_Audit_Email.md) |
| **SF5** | Adderory Company Registration | Identity fraud and stock supply manipulation. | Criminal (95%) | [SF5_Adderory_Company_Registration_Stock_Supply.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md) |
| **SF6** | Kayla Pretorius Estate | **CRITICAL:** Death of Kayla triggered estate exploitation. | Civil (50%) & Criminal (95%) | [SF6_Kayla_Pretorius_Estate_Documentation.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md) |
| **SF7** | Court Order Kayla Email Seizure | Email seizure order evidence. | Civil (50%) | [SF7_Court_Order_Kayla_Email_Seizure.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md) |
| **SF8** | Linda Employment Records | Employment documentation for bookkeeper. | Moderate | [SF8_Linda_Employment_Records.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF8_Linda_Employment_Records.md) |
| **SF9** | Ian Levitt Attorney Memo | Attorney memo documenting case issues and timeline. | Strong | [IanLevittAttorneysMemo_2025-11-09.txt](https://github.com/cogpy/ad-res-j7/blob/main/archive/legal-analysis-nov2025/attorney_correspondence/IanLevittAttorneysMemo_2025-11-09.txt) |
"""

def generate_legal_applications_section():
    """Generate the legal applications section"""
    
    return """## III. Three Legal Applications

This evidence supports three distinct legal applications, each with specific evidence requirements and burden of proof standards.

### Application 1: Civil Response (1-CIVIL-RESPONSE)

**Purpose:** Answering affidavit in response to Peter Faucitt\\'s interdict application (Case 2025-137857)

**Burden of Proof:** Balance of probabilities (50%)

**Key Evidence:**
- All JF annexures (JF01-JF09)
- All SF evidence (SF1-SF9)
- Comprehensive timeline of events
- Financial impact analysis

**Status:** Evidence organized and indexed  
**Location:** [ad-res-j7/1-CIVIL-RESPONSE](https://github.com/cogpy/ad-res-j7/tree/main/1-CIVIL-RESPONSE)

### Application 2: Criminal Case (2-CRIMINAL-CASE)
**Purpose:** Criminal complaints for fraud, theft, POPIA violations, and Companies Act violations

**Burden of Proof:** Beyond reasonable doubt (95%)

**Key Evidence Focus:**
- 46 events meeting criminal threshold
- SF1 (Bantjies debt/conflict), SF2 (Rynette control), SF3 (stock fraud)
- SF4 (tax fraud), SF5 (identity fraud), SF6 (estate exploitation)
- JF07 (payment redirection), JF08 (comprehensive fraud timeline)

**Status:** Evidence refined and categorized  
**Location:** [ad-res-j7/2-CRIMINAL-CASE](https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE)

### Application 3: External Validation (3-EXTERNAL-VALIDATION)

**Purpose:** Independent verification and external expert review package

**Burden of Proof:** Professional standards (varies by discipline)

**Key Evidence:**
- Complete data models (entities, relations, events, timeline)
- All visualizations and timelines
- Cross-referenced evidence catalog
- Methodology documentation

**Status:** Comprehensive package prepared  
**Location:** [ad-res-j7/3-EXTERNAL-VALIDATION](https://github.com/cogpy/ad-res-j7/tree/main/3-EXTERNAL-VALIDATION)
"""

def generate_visualizations_section():
    """Generate the visualizations section"""
    
    return """## IV. Visualizations

Visualizations provide an intuitive understanding of the complex timelines and networks of conspiracy.

### Timelines

| Visualization | Description | Link |
| :--- | :--- | :--- |
| **Comprehensive Timeline** | Full timeline of all events (2017-2025) | [comprehensive_timeline.png](comprehensive_timeline.png) |
| **Criminal Events Timeline** | Highlights events meeting the criminal burden of proof | [criminal_events_timeline_fixed.png](criminal_events_timeline_fixed.png) |
| **Criminal Threshold Events** | Detailed view of 95% threshold events | [criminal_threshold_events_timeline.png](criminal_threshold_events_timeline.png) |
| **Card Cancellation Timeline** | Timeline of card cancellations and financial control | [card_cancellation_timeline.png](card_cancellation_timeline.png) |
| **Revenue Stream Fraud Timeline** | Specific timeline of revenue hijacking events | [revenue_stream_fraud_timeline.png](revenue_stream_fraud_timeline.png) |
| **CIPC Fraud Timeline** | Timeline of Companies Act violations | [cipc_fraud_timeline.png](cipc_fraud_timeline.png) |
| **Curatorship Conspiracy Timeline** | Timeline of suspected curatorship fraud plot | [curatorship_conspiracy_timeline.mmd](curatorship_conspiracy_timeline.mmd) |

### Network Graphs & Flowcharts

| Visualization | Description | Link |
| :--- | :--- | :--- |
| **Conspiracy Network Graph** | Maps the relationships and coordination between the primary perpetrators | [conspiracy_network_graph.png](conspiracy_network_graph.png) |
| **Curatorship Conspiracy Flowchart** | Illustrates the suspected plot to commit curatorship fraud | [curatorship_conspiracy_flowchart.png](curatorship_conspiracy_flowchart.png) |
| **Fabricated Accounts Fraud Proof** | Flowchart showing evidence of fabricated financial accounts | [fabricated_accounts_fraud_proof.png](fabricated_accounts_fraud_proof.png) |
| **Causal Chain - Torture** | Causal chain analysis of psychological harm | [causal_chain_torture.png](causal_chain_torture.png) |
"""

def generate_legal_filings_section():
    """Generate the legal filings section"""
    
    filings = [
        {
            "name": "CIPC Companies Act Complaint",
            "version": "2026-01-06",
            "link": "CIPC_COMPLAINT_REFINED_2026_01_06.md"
        },
        {
            "name": "POPIA Criminal Complaint",
            "version": "2026-01-06",
            "link": "POPIA_COMPLAINT_REFINED_2026_01_06.md"
        },
        {
            "name": "NPA Tax Fraud Report",
            "version": "2026-01-06",
            "link": "NPA_TAX_FRAUD_REPORT_REFINED_2026_01_06.md"
        }
    ]
    
    section = """## V. Legal Filings (Latest Versions)

This section contains the most recently refined legal filings based on the comprehensive body of evidence.

| Filing | Version | Last Updated | Link |
| :--- | :--- | :--- | :--- |
"""
    
    for filing in filings:
        section += f'| **{filing["name"]}** | {filing["version"]} | {filing["version"]} | [{filing["link"]}]({filing["link"]}) |\n'
        
    section += """\n### Filing Status

All filings have been refined based on:
- 46 criminal threshold events
- 33 tracked entities
- 75 mapped relations
- Comprehensive evidence from both revstream1 and ad-res-j7 repositories
"""
    
    return section

def generate_analysis_reports_section():
    """Generate the analysis reports section"""
    
    return """## VI. Analysis Reports

| Report | Date | Description | Link |
| :--- | :--- | :--- | :--- |
| **Comprehensive Refinement Report** | 2026-01-06 | Latest comprehensive analysis and refinement summary | [COMPREHENSIVE_REFINEMENT_REPORT_2026_01_06.md](COMPREHENSIVE_REFINEMENT_REPORT_2026_01_06.md) |
| **Timeline Improvement Suggestions** | 2026-01-05 | Analysis of timeline gaps and improvement recommendations | [../TIMELINE_IMPROVEMENT_SUGGESTIONS_2026_01_05.json](../TIMELINE_IMPROVEMENT_SUGGESTIONS_2026_01_05.json) |
| **Evidence Index (Enhanced)** | Current | Comprehensive evidence catalog with cross-references | [evidence-index-enhanced.md](evidence-index-enhanced.md) |
"""

def generate_footer():
    """Generate the footer section"""
    
    last_generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    return f"""---

*This page is automatically generated and updated based on the latest analysis of the `revstream1` and `ad-res-j7` repositories.*

**Repository:** [cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Extended Evidence:** [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)  
**Last Generated:** {last_generated}
"""


def main():
    print("Loading data models...")
    entities, relations, events, timeline = load_data()
    
    print("Generating index.md content...")
    
    # Generate all sections
    summary = generate_executive_summary(entities, relations, events, timeline)
    data_models = generate_data_models_section(entities, relations, events, timeline)
    evidence_index = generate_evidence_index_section()
    legal_apps = generate_legal_applications_section()
    visualizations = generate_visualizations_section()
    legal_filings = generate_legal_filings_section()
    analysis_reports = generate_analysis_reports_section()
    footer = generate_footer()
    
    # Combine all sections
    full_content = "\n---\n".join([
        summary,
        data_models,
        evidence_index,
        legal_apps,
        visualizations,
        legal_filings,
        analysis_reports,
        footer
    ])
    
    # Save to file
    output_path = Path("/home/ubuntu/revstream1/docs/index.md")
    with open(output_path, "w") as f:
        f.write(full_content)
    
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()

