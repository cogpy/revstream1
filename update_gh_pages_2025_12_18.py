#!/usr/bin/env python3
"""
Update and organize GitHub Pages for clearer evidence presentation.
"""

import os
import re
from pathlib import Path


def create_evidence_index():
    """Create a new evidence index page"""
    evidence_index_file = Path("/home/ubuntu/revstream1/docs/evidence_index.md")
    
    content = """---
layout: default
title: Evidence Index
---

# Evidence Index

This page provides a comprehensive index of all evidence files from the ad-res-j7 repository, which are cross-referenced throughout this site.

## Smoking Gun Evidence Files (SF Series)

| Evidence ID | Description                                      | Link to Evidence File in ad-res-j7 |
|-------------|--------------------------------------------------|------------------------------------|
| SF1         | Bantjies Debt Documentation                      | [SF1_Bantjies_Debt_Documentation.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md) |
| SF2         | Sage Screenshots - Rynette Control               | [SF2_Sage_Screenshots_Rynette_Control.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md) |
| SF3         | Strategic Logistics Stock Adjustment             | [SF3_Strategic_Logistics_Stock_Adjustment.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md) |
| SF4         | SARS Audit Email                                 | [SF4_SARS_Audit_Email.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF4_SARS_Audit_Email.md) |
| SF5         | Adderory Company Registration & Stock Supply     | [SF5_Adderory_Company_Registration_Stock_Supply.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md) |
| SF6         | Kayla Pretorius Estate Documentation             | [SF6_Kayla_Pretorius_Estate_Documentation.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md) |
| SF7         | Court Order - Kayla Email Seizure                | [SF7_Court_Order_Kayla_Email_Seizure.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md) |
| SF8         | Linda Employment Records                         | [SF8_Linda_Employment_Records.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF8_Linda_Employment_Records.md) |

---

*Generated: 2025-12-18*
"""
    
    with open(evidence_index_file, 'w') as f:
        f.write(content)
    
    print(f"Created {evidence_index_file}")

def update_main_index():
    """Update the main index.md file"""
    index_file = Path("/home/ubuntu/revstream1/docs/index.md")
    
    with open(index_file, 'r') as f:
        content = f.read()
    
    # Add links to new pages
    new_links = """- [Evidence Index](evidence_index.md)
- [Entity Relations Update (2025-12-18)](RELATIONS_UPDATE_2025_12_18.md)
"""
    
    content = content.replace("- [Timeline](timeline.md)", f"- [Timeline](timeline.md)\n{new_links}")
    
    with open(index_file, 'w') as f:
        f.write(content)
    
    print(f"Updated {index_file}")

def update_application_pages():
    """Update application pages with new evidence"""
    app_files = [
        Path("/home/ubuntu/revstream1/docs/application-1.md"),
        Path("/home/ubuntu/revstream1/docs/application-2.md"),
        Path("/home/ubuntu/revstream1/docs/application-3.md"),
    ]
    
    new_evidence_section = """## New Evidence (2025-12-18 Refinement)

The following new evidence has been identified and cross-referenced, strengthening the application:

- **SF1: Bantjies Debt Documentation:** Documents the fraudulent R18.68M debt structure.
- **SF2: Rynette Sage Control:** Shows Rynette Farrar's administrative control over the accounting system.
- **SF4: SARS Audit Email:** Indicates official regulatory scrutiny of the companies' tax affairs.
- **SF5: Adderory Registration:** Shows the creation of a new entity for potential revenue manipulation.
- **SF7: Court Order for Email Seizure:** Legal action to seize potentially incriminating email communications.

These new evidence points significantly strengthen the case for financial fraud, conspiracy, and manipulation of accounting records.
"""
    
    for app_file in app_files:
        with open(app_file, 'r') as f:
            content = f.read()
        
        # Append new evidence section
        content += "\n\n" + new_evidence_section
        
        with open(app_file, 'w') as f:
            f.write(content)
        
        print(f"Updated {app_file}")

def generate_diagrams():
    """Generate PNG diagrams from MMD files"""
    docs_dir = Path("/home/ubuntu/revstream1/docs")
    mmd_files = list(docs_dir.glob("*.mmd"))
    
    for mmd_file in mmd_files:
        output_file = mmd_file.with_suffix(".png")
        command = f"manus-render-diagram {mmd_file} {output_file}"
        os.system(command)
        print(f"Generated diagram: {output_file}")

def main():
    print("=" * 80)
    print("UPDATING GITHUB PAGES")
    print("=" * 80)
    print()
    
    create_evidence_index()
    update_main_index()
    update_application_pages()
    generate_diagrams()
    
    print()
    print("=" * 80)
    print("GITHUB PAGES UPDATED SUCCESSFULLY")
    print("=" * 80)
    print()

if __name__ == "__main__":
    main()
