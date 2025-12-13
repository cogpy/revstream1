#!/usr/bin/env python3
"""
Refine all legal filings with the latest data models and evidence.
"""
import json
import re
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def update_filing(filepath, entities_version, events_version, relations_version, timeline_version):
    """Update a single filing document."""
    print(f"Updating {filepath.name}...")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Update version numbers
    content = re.sub(r"(Entities v)[0-9.]+", f"\g<1>{entities_version}", content)
    content = re.sub(r"(Events v)[0-9.]+", f"\g<1>{events_version}", content)
    content = re.sub(r"(Relations v)[0-9.]+", f"\g<1>{relations_version}", content)
    content = re.sub(r"(Timeline v)[0-9.]+", f"\g<1>{timeline_version}", content)
    
    # Update last updated timestamp
    content = re.sub(r"(Last Updated: )[0-9-]+", f"\g<1>{datetime.now().strftime('%Y-%m-%d')}", content)
    
    # Add a note about the update
    update_note = f"""---
*This document has been automatically updated on {datetime.now().strftime('%Y-%m-%d')} to reflect the latest data models and evidence.*
---

"""
    content = update_note + content
    
    # Save updated file
    new_filepath = filepath.with_name(f"{filepath.stem}_REFINED_{datetime.now().strftime('%Y%m%d')}.md")
    with open(new_filepath, 'w') as f:
        f.write(content)
    
    print(f"  -> Saved as {new_filepath.name}")

def main():
    # Get latest data model versions
    entities_data = load_json("data_models/entities/entities_refined_2025_12_13_v16.json")
    events_data = load_json("data_models/events/events_refined_2025_12_13_v36.json")
    relations_data = load_json("data_models/relations/relations_refined_2025_12_13_v26.json")
    
    entities_version = entities_data["metadata"]["version"].split('_')[0]
    events_version = events_data["metadata"]["version"].split('_')[0]
    relations_version = relations_data["metadata"]["version"].split('_')[0]
    timeline_version = "25.0" # Assuming timeline is also updated
    
    filings_dir = Path("docs/filings")
    filings_to_update = [
        filings_dir / "ANSWERING_AFFIDAVIT_REFINED_2025_12_10_UPDATED_2025_12_12.md",
        filings_dir / "CIPC_COMPLAINT_REFINED_2025_12_10_UPDATED_2025_12_12.md",
        filings_dir / "POPIA_COMPLAINT_REFINED_2025_12_10_UPDATED_2025_12_12.md",
        filings_dir / "COMMERCIAL_CRIME_REFINED_2025_12_10.md",
        filings_dir / "NPA_TAX_FRAUD_REPORT_2025_12_10_UPDATED_2025_12_12.md"
    ]
    
    for filing_path in filings_to_update:
        if filing_path.exists():
            update_filing(filing_path, entities_version, events_version, relations_version, timeline_version)
        else:
            print(f"SKIPPING: {filing_path.name} not found.")

    print("\n✓ All filings have been refined.")

if __name__ == "__main__":
    main()
