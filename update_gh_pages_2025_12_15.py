#!/usr/bin/env python3
"""
Update GitHub Pages with a comprehensive evidence index and refined application pages.
Date: 2025-12-15
"""

import json
import os
from datetime import datetime

# Paths
REVSTREAM_BASE = "/home/ubuntu/revstream1"
AD_RES_BASE = "/home/ubuntu/ad-res-j7"
DOCS_DIR = f"{REVSTREAM_BASE}/docs"

# Load analysis files
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

sf_analysis = load_json(f"{REVSTREAM_BASE}/SF_EVIDENCE_ANALYSIS_2025_12_15.json")
data_model_analysis = load_json(f"{REVSTREAM_BASE}/DATA_MODEL_ANALYSIS_2025_12_15.json")

# --- 1. Create Comprehensive Evidence Index ---
print("Creating comprehensive evidence index...")

annexures_index_path = f"{AD_RES_BASE}/ANNEXURES/ANNEXURES_INDEX.md"
with open(annexures_index_path, 'r') as f:
    annexures_content = f.read()

comprehensive_index = """
# Comprehensive Evidence Index
**Case 2025-137857**
*Last Updated: {date}*

This index provides a centralized reference for all evidence presented in the applications, linking claims to specific annexures from the `ad-res-j7` repository.

---

## Applications Overview

- **[Application 1: Delinquent Director Application (s162)](./application-1.md)**
- **[Application 2: Oppression Application (s163)](./application-2.md)**
- **[Application 3: CIPC & POPIA Complaints](./application-3.md)**

---

## Supplementary Evidence Files (SF Series)

This section details the supplementary evidence files (SF series) that provide critical context and support for the claims made.

| SF ID | Title | Legal Significance | Burden of Proof | Entities | Events |
|---|---|---|---|---|---|
""".format(date=datetime.now().strftime("%Y-%m-%d"))

for sf_id, data in sf_analysis["sf_evidence"].items():
    if data["exists"]:
        comprehensive_index += f"| {sf_id} | {data['title']} | {data['legal_significance']} | {data['burden_of_proof']} | {len(data['entities_involved'])} | {len(data['events_referenced'])} |\n"

comprehensive_index += "\n---\n\n## Main Annexures (JF Series)\n\n"
comprehensive_index += annexures_content

# Save the new index
new_index_path = f"{DOCS_DIR}/EVIDENCE_INDEX_COMPREHENSIVE_2025_12_15.md"
with open(new_index_path, 'w') as f:
    f.write(comprehensive_index)

print(f"Comprehensive evidence index saved to: {new_index_path}")

# --- 2. Update Application Pages ---
print("\nUpdating application pages...")

for i in range(1, 4):
    app_path = f"{DOCS_DIR}/application-{i}.md"
    with open(app_path, 'r') as f:
        app_content = f.read()

    # Add a link to the new comprehensive index
    updated_content = f"**[<< Back to Comprehensive Evidence Index](./EVIDENCE_INDEX_COMPREHENSIVE_2025_12_15.md)**\n\n---\n\n{app_content}"

    with open(app_path, 'w') as f:
        f.write(updated_content)
    print(f"Updated application-{i}.md")

# --- 3. Update Main Index.md ---
print("\nUpdating main index.md...")

index_path = f"{DOCS_DIR}/index.md"
with open(index_path, 'r') as f:
    index_content = f.read()

# Replace old evidence index link with the new one
updated_index_content = index_content.replace("evidence-index.md", "EVIDENCE_INDEX_COMPREHENSIVE_2025_12_15.md")

with open(index_path, 'w') as f:
    f.write(updated_index_content)

print("Updated index.md")

print("\nGitHub Pages update process complete.")

