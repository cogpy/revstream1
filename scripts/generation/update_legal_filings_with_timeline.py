#!/usr/bin/env python3
"""Update legal filings with the corrected timeline information"""

import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
FILINGS_DOCS_PATH = REVSTREAM_ROOT / "docs" / "filings"

# Corrected dates
KAYLA_DEATH_DATE = "13 July 2023"
ESTATE_DOCS_DATE = "1 August 2023"
EMAIL_SEIZURE_DATE = "1 September 2023"

def update_filing(filepath):
    """Update a single legal filing with corrected timeline"""
    print(f"Updating {filepath.name}...")
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace incorrect dates and clarify events
    content = content.replace("2021-09-10", ESTATE_DOCS_DATE)
    content = content.replace("2021-10-05", EMAIL_SEIZURE_DATE)
    content = content.replace("2023-01-01", KAYLA_DEATH_DATE)
    content = content.replace("Kayla resigned", "Kayla resigned as director of K-Oz Creative")

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  ✓ {filepath.name} updated.")

def main():
    """Main function to update all legal filings"""
    print("=" * 80)
    print("UPDATING LEGAL FILINGS WITH CORRECTED TIMELINE")
    print("=" * 80)

    for filing in FILINGS_DOCS_PATH.glob("*.md"):
        update_filing(filing)

    print("\nLegal filings updated successfully.")

if __name__ == "__main__":
    main()
