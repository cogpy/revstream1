#!/usr/bin/env python3
"""
GitHub Pages Update Script - 2025-11-22
Purpose: Update docs/ to reflect the latest analysis and data models.
"""

import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def write_file(filepath, content):
    """Write content to a file"""
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated: {filepath}")

def update_index_md(docs_dir, new_data_files, improvements_report):
    """Update the main index.md file"""
    index_path = os.path.join(docs_dir, "index.md")
    with open(index_path, 'r') as f:
        content = f.read()

    # Update data model version and date
    content = content.replace("Data Model Version** | 15.0", "Data Model Version** | 16.0")
    content = content.replace("Last Updated** | 2025-11-21", f"Last Updated** | {datetime.now().strftime('%Y-%m-%d')}")

    # Update links to data model files
    content = content.replace("DATA_MODEL_ANALYSIS_2025_11_21.json", os.path.basename(new_data_files['analysis']))
    content = content.replace("TIMELINE_IMPROVEMENTS_2025_11_21.json", os.path.basename(improvements_report))
    content = content.replace("EVENT_PATTERNS_2025_11_21.json", "EVENT_PATTERNS_2025_11_22.json") # Placeholder for now
    content = content.replace("VALIDATION_REPORT_2025_11_21.json", "VALIDATION_REPORT_2025_11_22.json") # Placeholder for now

    # Add a new section for the improvements report
    improvements_link = f"[IMPROVEMENTS_REPORT_2025_11_22.json]({os.path.basename(improvements_report)})"
    if improvements_link not in content:
        content = content.replace(
            "**[📄 View Validation Report]",
            f"**[📄 View Improvements Report]({os.path.basename(improvements_report)})**  \n**[📄 View Validation Report]"
        )

    write_file(index_path, content)

def create_financial_summary(docs_dir, timeline_data):
    """Create a consolidated financial impact summary page"""
    filepath = os.path.join(docs_dir, "financial_impact_summary.md")
    content = "---\nlayout: default\ntitle: Financial Impact Summary\n---\n\n"
    content += "# Consolidated Financial Impact Summary\n\n"
    content += "**Generated:** " + datetime.now().strftime('%Y-%m-%d') + "\n\n"
    content += "This document provides a consolidated summary of the financial impact across all phases of the revenue stream hijacking scheme.\n\n"

    total_impact = 0
    table = "| Phase | Period | Financial Impact (ZAR) | Notes |\n"
    table += "|-------|--------|------------------------|-------|\n"

    phases = sorted(timeline_data["timeline_phases"].items(), key=lambda x: x[1]['start_date'])

    for phase_key, phase in phases:
        impact_str = phase.get("financial_impact", "0").replace('R', '').replace('+', '').replace(',', '')
        try:
            # Handle ranges and unknown values
            if 'M' in impact_str:
                impact_val = float(impact_str.split('M')[0]) * 1_000_000
            elif '-' in impact_str:
                impact_val = float(impact_str.split('-')[0].strip())
            elif 'unknown' in impact_str.lower():
                impact_val = 0
            else:
                impact_val = float(impact_str)
            total_impact += impact_val
            impact_display = f"R {impact_val:,.2f}"
        except ValueError:
            impact_display = phase.get("financial_impact", "N/A")

        table += f"| {phase['phase_name']} | {phase['start_date']} to {phase['end_date']} | {impact_display} | {phase.get('pattern_analysis', '')[:100]}... |\n"

    content += f"## Total Estimated Financial Impact: R {total_impact:,.2f}\n\n"
    content += table
    write_file(filepath, content)

def create_visualizations(docs_dir, improvements):
    """Create Mermaid diagrams for key findings"""
    # Evidence Destruction Timeline
    destruction_mmd = "---\ntitle: Evidence Destruction Timeline\n---\n\ntimeline\n    title Consciousness of Guilt - Evidence Destruction\n"
    destruction_events = ["EVENT_055", "EVENT_056", "EVENT_009", "EVENT_020"]
    for finding in improvements['critical_findings']:
        if finding['finding_id'] == 'CF_001':
            for event_id in finding['events']:
                destruction_mmd += f"    section {event_id}\n        : {event_id}\n"
    write_file(os.path.join(docs_dir, "evidence_destruction_timeline.mmd"), destruction_mmd)

    # Conspiracy Network
    conspiracy_mmd = "---\ntitle: Family Conspiracy Network\n---\n\ngraph TD\n"
    conspiracy_mmd += "    subgraph Perpetrators\n        P001[PERSON_001 Peter Faucitt]:::perpetrator\n        P002[PERSON_002 Rynette Farrar]:::perpetrator\n        P003[PERSON_003 Addarory]:::perpetrator\n    end\n"
    conspiracy_mmd += "    subgraph Professional Enablers\n        P007[PERSON_007 Danie Bantjies]:::enabler\n    end\n"
    conspiracy_mmd += "    subgraph Victims\n        P004[PERSON_004 Jacqueline Faucitt]:::victim\n        P005[PERSON_005 Daniel Faucitt]:::victim\n    end\n"
    conspiracy_mmd += "    P001 -- Co-conspirator --> P002\n"
    conspiracy_mmd += "    P002 -- Mother of --> P003\n"
    conspiracy_mmd += "    P001 -- Controls --> P007\n"
    conspiracy_mmd += "    P002 -- Controls --> P007\n"
    conspiracy_mmd += "    P001 -- Victimizes --> P004\n"
    conspiracy_mmd += "    P001 -- Victimizes --> P005\n"
    conspiracy_mmd += "    classDef perpetrator fill:#f9f,stroke:#333,stroke-width:2px;\n"
    conspiracy_mmd += "    classDef enabler fill:#fce,stroke:#333,stroke-width:2px;\n"
    conspiracy_mmd += "    classDef victim fill:#ccf,stroke:#333,stroke-width:2px;\n"
    write_file(os.path.join(docs_dir, "conspiracy_network.mmd"), conspiracy_mmd)

def main():
    """Main function"""
    docs_dir = "/home/ubuntu/revstream1/docs"
    data_models_dir = "/home/ubuntu/revstream1/data_models"

    # File paths
    new_data_files = {
        "entities": f"{data_models_dir}/entities/entities_refined_2025_11_22_v9.json",
        "relations": f"{data_models_dir}/relations/relations_refined_2025_11_22_v7.json",
        "events": f"{data_models_dir}/events/events_refined_2025_11_22_v10.json",
        "timeline": f"{data_models_dir}/timelines/timeline_refined_2025_11_22_v8.json",
        "analysis": "/home/ubuntu/revstream1/COMPREHENSIVE_ANALYSIS_2025_11_22.json"
    }
    improvements_report_path = "/home/ubuntu/revstream1/IMPROVEMENTS_REPORT_2025_11_22.json"

    # Load data
    timeline_data = load_json(new_data_files['timeline'])
    improvements_data = load_json(improvements_report_path)

    # Update GitHub Pages
    print("=== Updating GitHub Pages ===\n")
    update_index_md(docs_dir, new_data_files, improvements_report_path)
    create_financial_summary(docs_dir, timeline_data)
    create_visualizations(docs_dir, improvements_data)

    print("\n=== GitHub Pages Update Complete ===")
    print("New/updated files in docs/:")
    print("  - index.md")
    print("  - financial_impact_summary.md")
    print("  - evidence_destruction_timeline.mmd")
    print("  - conspiracy_network.mmd")

if __name__ == "__main__":
    main()

