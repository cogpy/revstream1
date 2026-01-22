#!/usr/bin/env python3.11
"""
Refine Legal Filings Script

This script updates the legal filings with the latest data from the enhanced data models.

Date: 2026-01-11
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DOCS_ROOT = REVSTREAM_ROOT / "docs"
FILINGS_DIR = DOCS_ROOT / "filings"

# Data model paths
ENTITIES_FILE = REVSTREAM_ROOT / "data_models/entities/entities_enhanced_2025_12_12.json"
TIMELINE_FILE = REVSTREAM_ROOT / "data_models/timelines/timeline.json"

# Load data models
def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def refine_filing(filepath, entities_data, timeline_data):
    """Refine a single legal filing."""
    with open(filepath, "r") as f:
        content = f.read()

    # Update stats
    person_count = len(entities_data.get("entities", {}).get("persons", []))
    org_count = len(entities_data.get("entities", {}).get("organizations", []))
    timeline_entries = len(timeline_data.get("timeline", []))
    criminal_entries = timeline_data.get("metadata", {}).get("criminal_threshold_entries", 0)

    content = re.sub(r"(\d+) persons", f"{person_count} persons", content)
    content = re.sub(r"(\d+) organizations", f"{org_count} organizations", content)
    content = re.sub(r"(\d+) timeline entries", f"{timeline_entries} timeline entries", content)
    content = re.sub(r"(\d+) criminal threshold entries", f"{criminal_entries} criminal threshold entries", content)

    # Update date
    update_str = f'Last Updated: {datetime.now().strftime("%Y-%m-%d")}'
    content = re.sub(r"Last Updated:.*", update_str, content)

    # Create new filename
    new_filename = f'{filepath.stem.split("_")[0]}_REFINED_{datetime.now().strftime("%Y_%m_%d")}.md'
    new_filepath = FILINGS_DIR / new_filename

    with open(new_filepath, "w") as f:
        f.write(content)

    print(f"Refined filing saved to: {new_filepath}")

def main():
    print("Refining legal filings...")
    FILINGS_DIR.mkdir(exist_ok=True)

    entities_data = load_json(ENTITIES_FILE)
    timeline_data = load_json(TIMELINE_FILE)

    # Find the latest versions of the filings
    filing_prefixes = ["CIPC_COMPLAINT", "POPIA_COMPLAINT", "NPA_TAX_FRAUD_REPORT"]
    for prefix in filing_prefixes:
        try:
            latest_filing = sorted(list(REVSTREAM_ROOT.glob(f"**/{prefix}*.md")), reverse=True)[0]
            refine_filing(latest_filing, entities_data, timeline_data)
        except IndexError:
            print(f"Warning: No filing found for prefix: {prefix}")

    print("Legal filings refinement complete.")

if __name__ == "__main__":
    main()
