#!/usr/bin/env python3
"""
Refine Legal Filings with New Evidence (SF2A, SF2B)
Date: 2025-12-08
Purpose: Update key legal filings with new critical evidence from Sage screenshots.
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")

# Files to update (using the previously enhanced versions as a base)
FILINGS_TO_UPDATE = {
    "CIPC_COMPLAINT": "CIPC_COMPLAINT_EVIDENCE_ENHANCED_2025_12_08.md",
    "COMMERCIAL_CRIME": "COMMERCIAL_CRIME_EVIDENCE_ENHANCED_2025_12_08.md",
    "ANSWERING_AFFIDAVIT": "ANSWERING_AFFIDAVIT_EVIDENCE_ENHANCED_2025_12_08.md",
}

def read_file(filepath):
    """Read a file and return its content"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: File not found, skipping: {filepath}")
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def write_file(filepath, content):
    """Write content to a file"""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✓ Saved enhanced file: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error writing {filepath}: {e}")
        return False

def enhance_filing_with_new_evidence(content):
    """Inject new evidence references (SF2A, SF2B) into a legal filing"""
    if not content:
        return content

    # Inject SF2B: Rynette as Subscription Owner (Oppression & Obstruction)
    oppression_ref = "This is further proven by **Annexure SF2B**, which shows Rynette Farrar is the sole 'subscription owner' for the Sage Accounting system and let the subscription expire, denying all parties access to financial records for over a month (from 23 July to 25 August 2025). This act constitutes a clear mechanism of control and obstruction, directly supporting the Section 163 Oppression claim."
    content = re.sub(r"(pattern of obstruction from Applicant)", f"\g<1>. {oppression_ref}", content, flags=re.IGNORECASE)
    content = re.sub(r"(Unfairly prejudicial conduct toward Daniel)", f"\g<1>. {oppression_ref}", content, flags=re.IGNORECASE)

    # Inject SF2A: Rynette's Dual Accounts (Fraud & Impersonation)
    impersonation_ref = "Furthermore, **Annexure SF2A** reveals that Rynette Farrar operated two user accounts within the Sage system, including one using Peter Faucitt's email address (Pete@regima.com). This demonstrates her ability to impersonate Peter Faucitt within the accounting system, a critical component of the fraudulent scheme."
    content = re.sub(r"(Coordinated fraud pattern)", f"\g<1>. {impersonation_ref}", content, flags=re.IGNORECASE)
    content = re.sub(r"(instructing Rynette to commit fraud for RegimA SA)", f"\g<1>, a fact corroborated by her ability to act as Peter within the system as shown in **Annexure SF2A**", content, flags=re.IGNORECASE)

    # Add a header indicating further evidence enhancement
    header = "\n---\n*This document has been further enhanced with new critical evidence (SF2A, SF2B) dated 2025-12-08.*\n---\n\n"
    content = header + content

    return content

def main():
    """Main execution function"""
    print("=" * 80)
    print("REFINE LEGAL FILINGS WITH NEW EVIDENCE SCRIPT - 2025-12-08")
    print("=" * 80)
    print()

    # Process each filing
    for filing_key, filename in FILINGS_TO_UPDATE.items():
        print(f"--- Processing: {filing_key} ({filename}) ---")
        filepath = REVSTREAM_PATH / filename
        content = read_file(filepath)

        if content:
            enhanced_content = enhance_filing_with_new_evidence(content)
            
            # Save the new version
            timestamp = datetime.now().strftime("%Y_%m_%d")
            new_filename = f"{filing_key}_FINAL_EVIDENCE_ENHANCED_{timestamp}.md"
            new_filepath = REVSTREAM_PATH / new_filename
            write_file(new_filepath, enhanced_content)

    print("\n" + "=" * 80)
    print("LEGAL FILING ENHANCEMENT WITH NEW EVIDENCE COMPLETE")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Review the new `_FINAL_EVIDENCE_ENHANCED_` markdown files.")
    print("2. Proceed to update the GitHub Pages with the new evidence.")

if __name__ == "__main__":
    main()
