#!/usr/bin/env python3
"""
Refine legal filings based on the latest evidence analysis from both repositories.
Date: 2025-12-15
"""

import json
import os
from datetime import datetime

# Paths
REVSTREAM_BASE = "/home/ubuntu/revstream1"
FILINGS_DIR = f"{REVSTREAM_BASE}/docs/filings"

# Load analysis files
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

sf_analysis = load_json(f"{REVSTREAM_BASE}/SF_EVIDENCE_ANALYSIS_2025_12_15.json")

# Filings to be refined
FILINGS = {
    "CIPC_COMPLAINT": "CIPC_COMPLAINT_EVIDENCE_ENHANCED_20251214.md",
    "COMMERCIAL_CRIME": "COMMERCIAL_CRIME_EVIDENCE_ENHANCED_20251214.md",
    "NPA_TAX_FRAUD": "NPA_TAX_FRAUD_REPORT_EVIDENCE_ENHANCED_20251214.md",
    "POPIA_COMPLAINT": "POPIA_COMPLAINT_EVIDENCE_ENHANCED_20251214.md"
}

print("Refining legal filings...")
print("="*60)

# Refine each filing
for filing_key, filename in FILINGS.items():
    filepath = f"{FILINGS_DIR}/{filename}"
    
    if not os.path.exists(filepath):
        print(f"\nSKIPPING: {filename} not found.")
        continue

    with open(filepath, 'r') as f:
        content = f.read()

    # Add a header indicating the refinement
    refined_content = f"""<!-- 
This document has been automatically refined on {datetime.now().strftime("%Y-%m-%d")} to integrate the latest evidence analysis.
-->\n
""" + content

    # Add a new section for supplementary evidence
    evidence_section = "\n\n---\n\n## Supplementary Evidence Cross-Reference\n\nThis section cross-references the claims made in this complaint with the supplementary evidence files (SF series) from the `ad-res-j7` repository. Each SF file provides detailed, verifiable proof supporting the allegations.\n\n| SF ID | Title | Relevance to this Complaint | Burden of Proof Met |\n|---|---|---|---|\n"

    # Find relevant SF files for this filing
    relevant_sf_files = []
    for sf_id, data in sf_analysis["sf_evidence"].items():
        # Simple check to see if the filing type is mentioned in the significance
        if filing_key.split('_')[0].lower() in data["legal_significance"].lower():
            relevant_sf_files.append(sf_id)
        elif "fraud" in filing_key.lower() and "fraud" in data["legal_significance"].lower():
            relevant_sf_files.append(sf_id)

    for sf_id in relevant_sf_files:
        sf_data = sf_analysis["sf_evidence"][sf_id]
        evidence_section += f"| {sf_id} | {sf_data['title']} | {sf_data['legal_significance']} | **{sf_data['burden_of_proof']}** |\n"

    refined_content += evidence_section

    # Save the refined filing
    new_filename = filename.replace("20251214", "20251215_REFINED")
    new_filepath = f"{FILINGS_DIR}/{new_filename}"
    
    with open(new_filepath, 'w') as f:
        f.write(refined_content)

    print(f"\nRefined {filename} -> {new_filename}")
    print(f"  - Added {len(relevant_sf_files)} supplementary evidence references.")

print("\n" + "="*60)
print("Legal filings refinement process complete.")

