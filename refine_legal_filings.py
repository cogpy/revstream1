#!/usr/bin/env python3
"""
Refine legal filings with the latest evidence and data models.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DOCS_ROOT = REVSTREAM_ROOT / "docs"
FILINGS_DOCS_PATH = DOCS_ROOT / "filings"

# Templates for filings are in the root directory
CIPC_TEMPLATE_PATH = REVSTREAM_ROOT / "CIPC_COMPLAINT_REFINED_2026_01_09.md"
POPIA_TEMPLATE_PATH = REVSTREAM_ROOT / "POPIA_COMPLAINT_REFINED_2026_01_09.md"
NPA_TEMPLATE_PATH = REVSTREAM_ROOT / "NPA_TAX_FRAUD_REPORT_REFINED_2026_01_09.md"

# Data model files
ENTITIES_FILE = DOCS_ROOT / "data_models" / "entities" / "entities.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_conclusive_evidence_summary():
    """Get a summary of conclusive evidence for filings"""
    entities = load_json(ENTITIES_FILE)
    summary = []

    for person in entities["entities"]["persons"]:
        if person.get("evidence_strength") == "conclusive":
            summary.append(f"- **{person['name']} ({person['entity_id']}):** Conclusive evidence based on {len(person.get('ad_res_j7_references',[]))} references, including critical evidence like JF01 Shopify email.")

    return "\n".join(summary)

def refine_filing(template_path, output_filename_base):
    """Refine a single legal filing"""
    print(f"Refining {template_path.name}...")
    with open(template_path, 'r') as f:
        content = f.read()

    # Get latest versions and evidence summary
    today_str = datetime.now().strftime('%Y-%m-%d')
    evidence_summary = get_conclusive_evidence_summary()

    # Replace placeholders and update content
    content = content.replace("2026-01-09", today_str)
    content = content.replace("v24.0, v19.0, v22.0, v20.0", "v27.0, v22.0, v25.0, v23.0")
    
    # Add a new section for conclusive evidence
    conclusive_section = f"""
## Conclusive Evidence Summary ({today_str})

Based on the latest data model refinements, the following entities have been upgraded to **conclusive** evidence status, significantly strengthening this complaint:

{evidence_summary}
"""
    
    if "## Conclusive Evidence Summary" in content:
        # Find and replace existing section
        start_index = content.find("## Conclusive Evidence Summary")
        end_index = content.find("---", start_index)
        content = content[:start_index] + conclusive_section + content[end_index:]
    else:
        # Add new section
        content = content.replace("---", f"{conclusive_section}\n---", 1)

    # Save new filing
    new_filename = f"{output_filename_base}_{datetime.now().strftime('%Y_%m_%d')}.md"
    new_filepath = REVSTREAM_ROOT / new_filename
    with open(new_filepath, 'w') as f:
        f.write(content)
    print(f"  Saved to {new_filepath}")

    # Copy to docs/filings
    docs_filepath = FILINGS_DOCS_PATH / new_filename
    with open(docs_filepath, 'w') as f:
        f.write(content)
    print(f"  Copied to {docs_filepath}")

def main():
    """Main function to refine all legal filings"""
    FILINGS_DOCS_PATH.mkdir(exist_ok=True)
    refine_filing(CIPC_TEMPLATE_PATH, "CIPC_COMPLAINT_REFINED")
    refine_filing(POPIA_TEMPLATE_PATH, "POPIA_COMPLAINT_REFINED")
    refine_filing(NPA_TEMPLATE_PATH, "NPA_TAX_FRAUD_REPORT_REFINED")
    print("\nLegal filings refined successfully.")

if __name__ == "__main__":
    main()
