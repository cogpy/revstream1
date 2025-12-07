#!/usr/bin/env python3
"""
Refine legal filings with updated evidence and analysis.
"""
import json
import os
from datetime import datetime

# --- Configuration ---
BASE_DIR = "/home/ubuntu/revstream1"
DOCS_DIR = f"{BASE_DIR}/docs"
DATA_MODELS_DIR = f"{BASE_DIR}/data_models"
AD_RES_J7_REPO_URL = "https://github.com/cogpy/ad-res-j7/blob/main/"

# --- File Paths ---
TIMELINE_FILE = f"{DATA_MODELS_DIR}/timelines/timeline_refined_2025_12_07_v20.json"
MAPPING_FILE = f"{BASE_DIR}/AD_RES_J7_EVIDENCE_MAPPING_2025_12_07.json"

# --- Draft Files ---
DRAFT_CIPC_COMPLAINT = f"{BASE_DIR}/CIPC_COMPLAINT_REFINED_2025_12_06.md"
DRAFT_COMMERCIAL_CRIME = f"{BASE_DIR}/COMMERCIAL_CRIME_SUBMISSION_2025_12_06.md"
DRAFT_AFFIDAVIT = f"{BASE_DIR}/ANSWERING_AFFIDAVIT_V8_EVIDENCE_ENHANCED.md"

# --- Helper Functions ---
def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        return json.load(f)

def read_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

def get_financial_amount(impact):
    if not impact:
        return 0.0
    if isinstance(impact, dict):
        amount_str = impact.get('amount', '0')
    elif isinstance(impact, str):
        amount_str = impact
    else:
        amount_str = '0'
    
    try:
        return float(str(amount_str).replace('R', '').replace(',', '').strip() or 0)
    except (ValueError, TypeError):
        return 0.0

def generate_evidence_summary(timeline_data, evidence_mapping):
    """Generates a summary of key events and their evidence."""
    summary = "\n## Summary of Key Events and Evidence\n\n"
    summary += "| Date | Event | Key Evidence Link |\n"
    summary += "|---|---|---|\n"

    if not timeline_data or not evidence_mapping:
        return summary

    # Get top 5 events with financial impact
    sorted_events = sorted(
        [e for e in timeline_data.get("timeline_events", []) if e.get("financial_impact")],
        key=lambda x: get_financial_amount(x.get("financial_impact")),
        reverse=True
    )

    for event in sorted_events[:5]:
        event_id = event.get("event_id")
        title = event.get("title", "N/A")
        date = event.get("date", "N/A")
        
        event_links = evidence_mapping.get("event_evidence_links", {}).get(event_id, {})
        locations = event_links.get("evidence_locations", [])
        
        if locations:
            # Create a markdown link to the first piece of evidence
            evidence_link = f"[{locations[0]}]({AD_RES_J7_REPO_URL}{locations[0]})"
        else:
            evidence_link = "See Annexures"

        summary += f"| {date} | {title} | {evidence_link} |\n"
    
    return summary

# --- Refinement Functions ---

def refine_cipc_complaint(evidence_summary):
    """Refines the CIPC complaint with new evidence."""
    print("Refining CIPC Complaint...")
    content = read_file(DRAFT_CIPC_COMPLAINT)
    if not content:
        print("  Draft not found.")
        return

    # Append the evidence summary
    content += "\n---\n"
    content += "**Evidence Summary (Generated from refined data models)**\n"
    content += evidence_summary

    # Update title and version
    new_title = "CIPC Companies Act Complaint (Evidence-Enhanced)"
    content = content.replace("CIPC Complaint (Refined)", new_title)
    
    header = f"""---
title: {new_title}
version: 2025.12.07
last_updated: {datetime.now().isoformat()}
---
"""
    final_content = header + content

    output_file = f"{BASE_DIR}/CIPC_COMPLAINT_EVIDENCE_ENHANCED_2025_12_07.md"
    write_file(output_file, final_content)
    print(f"  Saved refined CIPC complaint to: {output_file}")

def refine_commercial_crime_submission(evidence_summary):
    """Refines the Commercial Crime submission."""
    print("Refining Commercial Crime Submission...")
    content = read_file(DRAFT_COMMERCIAL_CRIME)
    if not content:
        print("  Draft not found.")
        return

    content += "\n---\n"
    content += "**Evidence Summary (Generated from refined data models)**\n"
    content += evidence_summary

    new_title = "Commercial Crime Case Submission (Evidence-Enhanced)"
    content = content.replace("Commercial Crime Case Submission", new_title)

    header = f"""---
title: {new_title}
version: 2025.12.07
last_updated: {datetime.now().isoformat()}
---
"""
    final_content = header + content

    output_file = f"{BASE_DIR}/COMMERCIAL_CRIME_SUBMISSION_ENHANCED_2025_12_07.md"
    write_file(output_file, final_content)
    print(f"  Saved refined submission to: {output_file}")

def refine_answering_affidavit(evidence_summary):
    """Refines the Answering Affidavit."""
    print("Refining Answering Affidavit...")
    content = read_file(DRAFT_AFFIDAVIT)
    if not content:
        print("  Draft not found.")
        return

    content += "\n---\n"
    content += "**SCHEDULE A: Summary of Key Events and Evidence**\n"
    content += evidence_summary

    new_title = "Answering Affidavit (Version 9 - Final Evidence Integration)"
    content = content.replace("ANSWERING AFFIDAVIT (V8 EVIDENCE ENHANCED)", new_title)

    header = f"""---
title: {new_title}
version: 9.0
case_number: 2025-137857
last_updated: {datetime.now().isoformat()}
---
"""
    final_content = header + content

    output_file = f"{BASE_DIR}/ANSWERING_AFFIDAVIT_V9_FINAL_2025_12_07.md"
    write_file(output_file, final_content)
    print(f"  Saved refined affidavit to: {output_file}")

# --- Main Execution ---
def main():
    """Main function to refine all legal filings."""
    print("Starting legal filing refinement...")

    # Load data
    timeline = load_json(TIMELINE_FILE)
    evidence_map = load_json(MAPPING_FILE)

    # Generate evidence summary to be appended
    evidence_summary = generate_evidence_summary(timeline, evidence_map)

    # Refine each document
    refine_cipc_complaint(evidence_summary)
    refine_commercial_crime_submission(evidence_summary)
    refine_answering_affidavit(evidence_summary)

    print("\nLegal filing refinement complete.")

if __name__ == "__main__":
    main()

