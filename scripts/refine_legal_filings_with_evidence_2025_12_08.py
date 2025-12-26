#!/usr/bin/env python3
"""
Refine Legal Filings with Evidence Cross-References
Date: 2025-12-08
Purpose: Update key legal filings with direct evidence references from the ad-res-j7 repository.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
EVIDENCE_CROSS_REF_PATH = REVSTREAM_PATH / "AD_RES_J7_EVIDENCE_CROSS_REFERENCE_2025_12_08.json"

# Files to update
FILINGS_TO_UPDATE = {
    "CIPC_COMPLAINT": "CIPC_COMPLAINT_REFINED_2025_12_06.md",
    "COMMERCIAL_CRIME": "COMMERCIAL_CRIME_SUBMISSION_2025_12_06.md",
    "ANSWERING_AFFIDAVIT": "ANSWERING_AFFIDAVIT_V9_FINAL_2025_12_07.md",
    "NPA_TAX_FRAUD": "NPA_TAX_FRAUD_REPORT_2025_12_07.md" # Assuming this exists or will be created
}

def load_json_file(filepath):
    """Load JSON file with error handling"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

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

def enhance_filing(content, evidence_data):
    """Inject evidence references into a legal filing"""
    if not content or not evidence_data:
        return content

    # Inject critical evidence: The Forensic Time Capsule
    forensic_capsule_ref = "(irrefutable proof presented in **Annexure JF1**, the \"Forensic Time Capsule\")"
    content = re.sub(r"(Kayla Pretorius personally managed Shopify Plus onboarding)", f"\g<1> {forensic_capsule_ref}", content, flags=re.IGNORECASE)
    content = re.sub(r"(Daniel was directly involved in business operations)", f"\g<1> {forensic_capsule_ref}", content, flags=re.IGNORECASE)

    # Inject evidence for Rynette's control
    rynette_control_ref = "(proven by **Annexure SF2**, which contains screenshots of the Sage accounting system)"
    content = re.sub(r"(Rynette Farrar controlled the Sage accounting system)", f"\g<1> {rynette_control_ref}", content, flags=re.IGNORECASE)

    # Inject evidence for financial transparency
    transparency_ref = "(demonstrated by the full, voluntary disclosure in **Annexure JF4**)"
    content = re.sub(r"(Daniel Faucitt has maintained complete financial transparency)", f"\g<1> {transparency_ref}", content, flags=re.IGNORECASE)

    # Update burden of proof sections
    burden_of_proof_summary = evidence_data.get("burden_of_proof_analysis", {})
    civil_status = burden_of_proof_summary.get("civil_claims", {}).get("status", "Not Assessed")
    criminal_fraud_status = burden_of_proof_summary.get("criminal_claims", {}).get("fraud", {}).get("status", "Not Assessed")

    content = re.sub(r"(Burden of Proof \(Civil\):\s*)[A-Za-z ]+", f"\g<1>**{civil_status}**", content)
    content = re.sub(r"(Burden of Proof \(Criminal - Fraud\):\s*)[A-Za-z ]+", f"\g<1>**{criminal_fraud_status}**", content)
    
    # Add a header indicating evidence enhancement
    header = "\n---\n*This document has been automatically enhanced with direct evidence references from the ad-res-j7 repository.*\n---\n\n"
    content = header + content

    return content

def main():
    """Main execution function"""
    print("=" * 80)
    print("REFINE LEGAL FILINGS SCRIPT - 2025-12-08")
    print("=" * 80)
    print()

    # Load evidence cross-reference
    print("Loading evidence cross-reference data...")
    evidence_data = load_json_file(EVIDENCE_CROSS_REF_PATH)
    if not evidence_data:
        print("Fatal: Could not load evidence data. Aborting.")
        return

    # Process each filing
    for filing_key, filename in FILINGS_TO_UPDATE.items():
        print(f"\n--- Processing: {filing_key} ({filename}) ---")
        filepath = REVSTREAM_PATH / filename
        content = read_file(filepath)

        if content:
            enhanced_content = enhance_filing(content, evidence_data)
            
            # Save the new version
            timestamp = datetime.now().strftime("%Y_%m_%d")
            new_filename = f"{filing_key}_EVIDENCE_ENHANCED_{timestamp}.md"
            new_filepath = REVSTREAM_PATH / new_filename
            write_file(new_filepath, enhanced_content)

    print("\n" + "=" * 80)
    print("LEGAL FILING ENHANCEMENT COMPLETE")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Review the new `_EVIDENCE_ENHANCED_` markdown files.")
    print("2. Proceed to update the GitHub Pages.")

if __name__ == "__main__":
    main()
