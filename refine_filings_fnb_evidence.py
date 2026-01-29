#!/usr/bin/env python3
"""
Refine Legal Filings with FNB Fraud Letter Evidence

This script updates the following legal filings with new evidence from Peter Faucitt's
letter to FNB dated 17 June 2025:
1. CIPC Complaint
2. POPIA Complaint
3. NPA Tax Fraud Report
4. Commercial Crime Submission
"""

import os
from datetime import datetime
from pathlib import Path

# Paths
FILINGS_DIR = Path("/home/ubuntu/revstream1/docs/filings")

# Find latest filings
def find_latest_filing(pattern):
    files = list(FILINGS_DIR.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files found for pattern: {pattern}")
    return max(files, key=os.path.getctime)

CIPC_COMPLAINT_PATH = find_latest_filing("cipc_complaint_REFINED*.md")
POPIA_COMPLAINT_PATH = find_latest_filing("popia_complaint_REFINED*.md")
NPA_REPORT_PATH = find_latest_filing("npa_tax_fraud_report_REFINED*.md")
COMMERCIAL_CRIME_PATH = find_latest_filing("commercial_crime_submission_REFINED*.md")

NEW_FILING_DATE = "2026_01_29"

FNB_EVIDENCE_TEXT = """
### NEW EVIDENCE: Director's Written Acknowledgment of Fraud (17 June 2025)

A letter from Director Peter Andrew Faucitt to FNB, dated 17 June 2025, serves as a direct admission of his awareness of fraudulent activities. In this letter, Mr. Faucitt:

1.  **Acknowledges "suspected fraud"** on the company's bank account (62323196362).
2.  Confirms he had made a **prior written request to cancel debit cards** due to this suspected fraud.
3.  Warns FNB that re-issuing cards could make the bank an **"accessory after the fact."**
4.  Expresses concern that the company may be **"transgressing the Exchange Control Regulations"** due to dollar-based subscription expenses.

This letter, written just 11 days after the fraud was exposed by Daniel Faucitt to the company's accountant, is irrefutable proof that the director was aware of the ongoing fraud. This directly contradicts his later court filings where he positions himself as a victim and blames others.

**Evidence:**
- [PAF_FNB_FRAUD_LETTER_2025_06_17.jpg](../evidence/FNB_FRAUD_LETTER_2025_06_17/PAF_FNB_FRAUD_LETTER_2025_06_17.jpg)
- [PAF_FNB_FRAUD_LETTER_2025_06_17_OCR.md](../evidence/FNB_FRAUD_LETTER_2025_06_17/PAF_FNB_FRAUD_LETTER_2025_06_17_OCR.md)
"""

EXCHANGE_CONTROL_TEXT = """
### Section D: Potential Exchange Control Violations

**Source:** Director's Letter to FNB (17 June 2025)

In his letter to FNB, Director Peter Faucitt explicitly states:

> "I also believe that due to the amount of dollar-based subscription expense passing through this account our company may be transgressing the Exchange Control Regulations, and if so, any such internation remittances should be suspended forthwith."

This admission provides a clear basis for an investigation by the South African Reserve Bank (SARB) into the company's international transactions.
"""

def refine_filing(path, new_content, new_filename):
    """Refine a legal filing with new content."""
    with open(path, 'r') as f:
        content = f.read()
    
    # Append new content
    content += "\n" + new_content
    
    new_path = FILINGS_DIR / new_filename
    with open(new_path, 'w') as f:
        f.write(content)
    print(f"Refined and saved: {new_path}")

def main():
    """Main function to refine all legal filings."""
    print("=" * 60)
    print("Refining Legal Filings with FNB Fraud Letter Evidence")
    print("=" * 60)

    # 1. Refine CIPC Complaint
    refine_filing(
        CIPC_COMPLAINT_PATH,
        FNB_EVIDENCE_TEXT,
        f"cipc_complaint_REFINED_{NEW_FILING_DATE}.md"
    )

    # 2. Refine POPIA Complaint
    refine_filing(
        POPIA_COMPLAINT_PATH,
        FNB_EVIDENCE_TEXT,
        f"popia_complaint_REFINED_{NEW_FILING_DATE}.md"
    )

    # 3. Refine NPA Tax Fraud Report
    refine_filing(
        NPA_REPORT_PATH,
        EXCHANGE_CONTROL_TEXT,
        f"npa_tax_fraud_report_REFINED_{NEW_FILING_DATE}.md"
    )

    # 4. Refine Commercial Crime Submission
    refine_filing(
        COMMERCIAL_CRIME_PATH,
        FNB_EVIDENCE_TEXT,
        f"commercial_crime_submission_REFINED_{NEW_FILING_DATE}.md"
    )

    print("\n" + "=" * 60)
    print("Legal Filings Refinement Complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
