#!/usr/bin/env python3
"""
Legal Filing Refinement Script

Refines the Answering Affidavit and Criminal Complaint by embedding direct, specific evidence links
from the ad-res-j7 repository, strengthening the arguments for different burdens of proof.
"""

import json
import os
import re
from pathlib import Path

# --- Configuration ---
BASE_DIR = Path("/home/ubuntu/revstream1")
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")
AD_RES_J7_BASE_URL = "https://github.com/cogpy/ad-res-j7/blob/main"

# --- File Paths ---
AFFIDAVIT_PATH = BASE_DIR / "ANSWERING_AFFIDAVIT_V7_FINAL_COMPLETE.md"
CRIMINAL_COMPLAINT_PATH = BASE_DIR / "CRIMINAL_COMPLAINT_TORTURE_PERJURY_FRAUD.md"

NEW_AFFIDAVIT_PATH = BASE_DIR / "ANSWERING_AFFIDAVIT_V8_EVIDENCE_ENHANCED.md"
NEW_CRIMINAL_COMPLAINT_PATH = BASE_DIR / "CRIMINAL_COMPLAINT_EVIDENCE_ENHANCED.md"

# --- Helper Functions ---
def read_file(filepath):
    """Reads a file and returns its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Writes content to a file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def find_specific_evidence(keyword, file_list):
    """Finds the most relevant evidence file for a keyword."""
    # Prioritize files with the keyword in the filename
    for f in file_list:
        if keyword.lower() in Path(f).name.lower():
            return f
    # Fallback to finding keyword anywhere in the path
    for f in file_list:
        if keyword.lower() in f.lower():
            return f
    return None

# --- Main Refinement Logic ---
def refine_filings():
    """Refines the legal filings with specific evidence links."""
    print("Starting legal filing refinement...")

    # 1. Gather all evidence files from ad-res-j7
    print(f"Scanning {AD_RES_J7_DIR} for evidence files...")
    all_evidence_files = [str(p.relative_to(AD_RES_J7_DIR)) for p in AD_RES_J7_DIR.rglob('*') if p.is_file()]
    print(f"Found {len(all_evidence_files)} total files.")

    # 2. Refine the Answering Affidavit
    print(f"Refining Answering Affidavit: {AFFIDAVIT_PATH}")
    affidavit_content = read_file(AFFIDAVIT_PATH)

    # Replace generic annexure placeholders with specific, hyperlinked evidence
    # Example: Replace Annexure JF_BANTJIES_DEBT with a direct link
    bantjies_debt_evidence = find_specific_evidence("BANTJIES_DEBT", all_evidence_files) or find_specific_evidence("call_option", all_evidence_files)
    if bantjies_debt_evidence:
        affidavit_content = affidavit_content.replace(
            "Annexure JF_BANTJIES_DEBT: Call option agreement showing payment schedule.",
            f'**Annexure JF_BANTJIES_DEBT:** [Call option agreement showing payment schedule.]({AD_RES_J7_BASE_URL}/{bantjies_debt_evidence}) - This document outlines the R18.685M debt obligation, establishing a clear financial motive for the curatorship conspiracy.'
        )

    # Fabricated Accounts Evidence (Civil - 50% burden)
    fake_accounts_evidence = find_specific_evidence("RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf", all_evidence_files)
    cipc_records_evidence = find_specific_evidence("CIPC_records", all_evidence_files) or find_specific_evidence("cipc", all_evidence_files)
    if fake_accounts_evidence and cipc_records_evidence:
        affidavit_content = affidavit_content.replace(
            "Annexure JF_FAKE_ACCOUNTS: Fabricated 2019 financial statements.",
            f'**Annexure JF_FAKE_ACCOUNTS:** [Fabricated 2019 Financial Statements]({AD_RES_J7_BASE_URL}/{fake_accounts_evidence}) - These statements for \'RegimA SA (Pty) Ltd\' are dated 2019, yet the company name only changed in 2021, proving fraudulent backdating.'
        )
        affidavit_content = affidavit_content.replace(
            "Annexure JF_CIPC_RECORDS: Official CIPC records proving the fraud.",
            f'**Annexure JF_CIPC_RECORDS:** [Official CIPC Records]({AD_RES_J7_BASE_URL}/{cipc_records_evidence}) - These records confirm the company was named \'K OZ CREATIVE\' in 2019 and that P.A. Faucitt was not a director, directly contradicting the fabricated statements.'
        )

    # R500k "Birthday Gift" Lie
    bank_statements_evidence = find_specific_evidence("D_FAUCITT_PERSONAL_BANK_RECORDS", all_evidence_files)
    expenditure_analysis_evidence = find_specific_evidence("expenditure_analysis", all_evidence_files)
    if bank_statements_evidence and expenditure_analysis_evidence:
        affidavit_content = affidavit_content.replace(
            "Annexure JF_BANK_STATEMENTS: Daniel's personal bank statements (May-October 2025).",
            f'**Annexure JF_BANK_STATEMENTS:** [Daniel Faucitt Personal Bank Statements]({AD_RES_J7_BASE_URL}/{bank_statements_evidence}) - These statements show the R500,000 transfer originated from Strategic Logistics, not Jacqueline, and detail the business expenses covered.'
        )
        affidavit_content = affidavit_content.replace(
            "Annexure JF_EXPENDITURE_ANALYSIS: Detailed breakdown of R1.06M in expenditures.",
            f'**Annexure JF_EXPENDITURE_ANALYSIS:** [Detailed R1.06M Expenditure Analysis]({AD_RES_J7_BASE_URL}/{expenditure_analysis_evidence}) - This document itemizes the corporate expenses involuntarily forced onto Daniel Faucitt\'s personal card.'
        )

    write_file(NEW_AFFIDAVIT_PATH, affidavit_content)
    print(f"Successfully created enhanced affidavit: {NEW_AFFIDAVIT_PATH}")

    # 3. Refine the Criminal Complaint
    print(f"Refining Criminal Complaint: {CRIMINAL_COMPLAINT_PATH}")
    complaint_content = read_file(CRIMINAL_COMPLAINT_PATH)

    # Strengthen Perjury claim (Criminal - 95% burden)
    complaint_content = complaint_content.replace(
        "Peter had these bank statements at the time he made the false statement, proving he knew it was false.",
        f'''**Proof of Knowledge (Mens Rea):** The Applicant was in possession of these bank statements when he deposed his affidavit. His decision to omit the source of the R500,000 and the nature of the expenditures constitutes a deliberate, willful, and material falsehood intended to mislead the Court. This act satisfies the high burden of proof for perjury.\n\n**Evidence:**\n- [Daniel Faucitt Personal Bank Statements]({AD_RES_J7_BASE_URL}/{bank_statements_evidence})\n- [Applicant\'s Founding Affidavit containing the false claim (Ref: case_2025_137857/affidavits/peter_affidavit/founding_affidavit.pdf)]({AD_RES_J7_BASE_URL}/case_2025_137857/affidavits/peter_affidavit/founding_affidavit.pdf)'''
    )

    # Strengthen Fraud claim against Rynette
    denovo_correspondence = find_specific_evidence("De_Novo_correspondence", all_evidence_files) or find_specific_evidence("AF10", all_evidence_files)
    if denovo_correspondence:
        complaint_content = complaint_content.replace(
            "De Novo correspondence (Annexure AF10 from Peter's own papers) shows Rynette instructing accountants to fabricate accounts and remove Daniel's records.",
            f'''**Evidence of Conspiracy and Fraud:** Correspondence with De Novo accountants (see **Annexure AF10** from the Applicant\'s own papers) provides direct, documentary proof of Rynette Farrar Bantjies instructing the fabrication of financial statements and the destruction of evidence (removal of QuickBooks records). This written instruction is irrefutable evidence of a criminal conspiracy to commit fraud.\n\n**Evidence Link:** [De Novo Accountant Correspondence]({AD_RES_J7_BASE_URL}/{denovo_correspondence})'''
        )

    write_file(NEW_CRIMINAL_COMPLAINT_PATH, complaint_content)
    print(f"Successfully created enhanced criminal complaint: {NEW_CRIMINAL_COMPLAINT_PATH}")

if __name__ == "__main__":
    refine_filings()
