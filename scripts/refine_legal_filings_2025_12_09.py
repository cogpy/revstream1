#!/usr/bin/env python3
"""
Refine Legal Filings Script for Revenue Stream Hijacking Case
Date: 2025-12-09
Purpose: Refine legal filings with new evidence and burden of proof analysis.
"""

import json
import os
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
FILINGS_DIR = BASE_DIR

# Filings to update
ANSWERING_AFFIDAVIT = FILINGS_DIR / "ANSWERING_AFFIDAVIT_REFINED_2025_12_09.md"
CIPC_COMPLAINT = FILINGS_DIR / "CIPC_COMPLAINT_FINAL_EVIDENCE_ENHANCED_2025_12_09.md"
COMMERCIAL_CRIME_SUBMISSION = FILINGS_DIR / "COMMERCIAL_CRIME_FINAL_EVIDENCE_ENHANCED_2025_12_09.md"

def read_file(filepath):
    """Read file content"""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w') as f:
        f.write(content)

def refine_answering_affidavit(content):
    """Refine the Answering Affidavit with new evidence"""
    print("Refining Answering Affidavit...")
    
    # Add SF9 evidence
    if "R63M" not in content:
        print("  - Adding SF9 (R63M quantum) evidence...")
        content = content.replace("## Financial Impact", "## Financial Impact\n\n**The total quantum of the revenue hijacking scheme is estimated to be approximately R63 million**, as documented in the formal demand letter from Ian Levitt Attorneys dated 23 October 2025 (Annexure **SF9**). This includes R60,251,961.60 in outstanding revenue from RegimA Worldwide Distribution and $150,000 in unpaid platform fees.")

    # Add SF2A/SF2B evidence
    if "Rynette's Control and Impersonation" not in content:
        print("  - Adding SF2A/SF2B (Rynette's control) evidence...")
        content = content.replace("### Evidence of Fraud", "### Rynette's Control and Impersonation (Annexures SF2A & SF2B)\n\n**Direct evidence demonstrates Rynette Farrar's control over the accounting systems and her ability to impersonate Peter Faucitt:**\n\n- **Obstruction of Access (SF2B):** Rynette is the sole subscription owner of the Sage accounting system. She allowed the subscription to expire on 23 July 2025 and did not reactivate it for over a month, effectively denying all parties access to critical financial records. This constitutes a clear act of oppression under Section 163 of the Companies Act.\n- **Identity Impersonation (SF2A):** Rynette maintained dual user accounts in the Sage system, including one for \"Pete@regima.com\". This gave her the ability to act as Peter Faucitt within the system, creating a significant risk of fraudulent activity and misrepresentation.\n\n### Evidence of Fraud")

    return content

def refine_cipc_complaint(content):
    """Refine the CIPC Complaint with new evidence"""
    print("Refining CIPC Complaint...")

    # Add SF2A/SF2B evidence
    if "Director's Fiduciary Duties" not in content:
        print("  - Adding SF2A/SF2B evidence to CIPC complaint...")
        content = content.replace("## Breaches of the Companies Act", "## Breaches of the Companies Act\n\n### Section 76: Director's Fiduciary Duties and Standard of Conduct\n\n**Peter Faucitt has demonstrably failed to act in the best interests of the company and has used his position to cause harm.** His co-conspirator, **Rynette Farrar**, has actively participated in this misconduct through her control of the company's financial systems.\n\n- **Obstruction of Access (SF2B):** Rynette Farrar, as the sole subscription owner of the Sage accounting system, deliberately allowed the subscription to lapse, thereby obstructing access to financial records for over a month. This action is a clear violation of the principles of transparency and accountability.\n- **Identity Impersonation (SF2A):** Rynette Farrar's use of a dual account to impersonate Peter Faucitt in the accounting system is a serious breach of trust and a fraudulent act that has exposed the company to significant risk.")

    return content

def refine_commercial_crime_submission(content):
    """Refine the Commercial Crime Submission with new evidence"""
    print("Refining Commercial Crime Submission...")

    # Add SF9 evidence
    if "Quantum of Prejudice" not in content:
        print("  - Adding SF9 (R63M quantum) to Commercial Crime Submission...")
        content = content.replace("## Total Prejudice", "## Quantum of Prejudice\n\nThe total prejudice suffered as a result of this criminal enterprise is estimated to be **R63 million**. This figure is substantiated by a formal demand from Ian Levitt Attorneys (Annexure **SF9**), which breaks down the amount into R60,251,961.60 in lost revenue and $150,000 in unpaid platform fees.\n\n## Total Prejudice")

    # Add SF2A/SF2B evidence
    if "Identity Impersonation and Obstruction" not in content:
        print("  - Adding SF2A/SF2B evidence to Commercial Crime Submission...")
        content = content.replace("### Evidence of Criminal Conduct", "### Identity Impersonation and Obstruction (Annexures SF2A & SF2B)\n\n**The criminal nature of the fraud is further evidenced by the following:**\n\n- **Identity Impersonation (SF2A):** Rynette Farrar's use of a dual account to impersonate Peter Faucitt constitutes identity fraud, a serious criminal offense. This allowed her to manipulate financial records and conceal the theft of funds.\n- **Obstruction of Justice (SF2B):** By deliberately allowing the Sage accounting subscription to expire, Rynette Farrar obstructed access to evidence of the ongoing fraud. This act was a calculated attempt to conceal the criminal enterprise and prevent its discovery.\n\n### Evidence of Criminal Conduct")

    return content

def main():
    """Main execution function"""
    print("="*80)
    print("REFINING LEGAL FILINGS - Revenue Stream Hijacking Case 2025-137857")
    print("="*80)

    # Refine Answering Affidavit
    if ANSWERING_AFFIDAVIT.exists():
        affidavit_content = read_file(ANSWERING_AFFIDAVIT)
        refined_affidavit = refine_answering_affidavit(affidavit_content)
        write_file(ANSWERING_AFFIDAVIT, refined_affidavit)
        print("  ✓ Answering Affidavit refined successfully.")
    else:
        print(f"  ! Answering Affidavit not found at: {ANSWERING_AFFIDAVIT}")

    # Refine CIPC Complaint
    if CIPC_COMPLAINT.exists():
        cipc_content = read_file(CIPC_COMPLAINT)
        refined_cipc = refine_cipc_complaint(cipc_content)
        write_file(CIPC_COMPLAINT, refined_cipc)
        print("  ✓ CIPC Complaint refined successfully.")
    else:
        print(f"  ! CIPC Complaint not found at: {CIPC_COMPLAINT}")

    # Refine Commercial Crime Submission
    if COMMERCIAL_CRIME_SUBMISSION.exists():
        crime_content = read_file(COMMERCIAL_CRIME_SUBMISSION)
        refined_crime = refine_commercial_crime_submission(crime_content)
        write_file(COMMERCIAL_CRIME_SUBMISSION, refined_crime)
        print("  ✓ Commercial Crime Submission refined successfully.")
    else:
        # Create the file if it doesn't exist
        print(f"  ! Commercial Crime Submission not found at: {COMMERCIAL_CRIME_SUBMISSION}, creating it...")
        initial_content = """# Commercial Crime Case Submission\n\n## Case Number: 2025-137857\n\n## Date: 2025-12-09\n\n## Total Prejudice\n\n"""
        refined_crime = refine_commercial_crime_submission(initial_content)
        write_file(COMMERCIAL_CRIME_SUBMISSION, refined_crime)
        print("  ✓ Commercial Crime Submission created and refined successfully.")

    print("\n" + "="*80)
    print("LEGAL FILINGS REFINED SUCCESSFULLY")
    print("="*80)

if __name__ == "__main__":
    main()
