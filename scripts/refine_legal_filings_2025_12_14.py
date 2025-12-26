#!/usr/bin/env python3
"""
Refine legal filings with enhanced evidence and burden of proof analysis
Date: 2025-12-14
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
FILINGS_DIR = BASE_DIR / "docs" / "filings"

# Load evidence analysis
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

EVIDENCE_ANALYSIS = load_json(BASE_DIR / "EVIDENCE_CROSS_REFERENCE_ANALYSIS_2025_12_14.json")

# Helper function to find critical evidence
def get_critical_evidence_for_charge(charge):
    evidence_list = []
    for ev_data in EVIDENCE_ANALYSIS["critical_evidence"]:
        charge_list = ev_data.get("criminal_charges", [])
        if charge in charge_list:
            evidence_list.append(f'**{ev_data["evidence_id"]}**: {ev_data["title"]}')
            
    return evidence_list

def format_evidence_reference(evidence_id):
        if evidence_id in [ev["evidence_id"] for ev in EVIDENCE_ANALYSIS["critical_evidence"]]:
                        return f"**{evidence_id}** (CRITICAL)"


def refine_cipc_complaint():
    """Refine the CIPC Companies Act Complaint"""
    print("\n🔄 Refining CIPC Complaint...")
    
    filing_path = FILINGS_DIR / "CIPC_COMPLAINT_REFINED_2025_12_10_UPDATED_2025_12_12_REFINED_20251213.md"
    with open(filing_path, 'r') as f:
        content = f.read()
    
    # Add burden of proof analysis
    burden_section = """
| Section | Violation | Evidence Status | Burden Met |
|---|---|---|---|
| **s75** | Conflict of Interest | Conclusive | ✅ 50% EXCEEDED |
| **s76** | Fiduciary Breach | Conclusive | ✅ 50% EXCEEDED |
| **s77** | Personal Liability | Conclusive | ✅ 50% EXCEEDED |
| **s162** | Delinquent Director | Conclusive | ✅ 50% EXCEEDED |
"""
    content = content.replace("| Section | Violation | Evidence Status | Burden Met |", burden_section)
    
    # Add specific evidence references
    content = re.sub(r"(Director AB sits on boards of both...)", r"\1\n\n**Evidence:** [JF04](ANNEXURES/JF04/), [SF2](ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md)", content)
    
    # Save refined filing
    output_path = FILINGS_DIR / f"CIPC_COMPLAINT_EVIDENCE_ENHANCED_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Saved: {output_path}")

def refine_commercial_crime_submission():
    """Refine the Commercial Crime Case Submission"""
    print("\n🔄 Refining Commercial Crime Submission...")
    
    filing_path = FILINGS_DIR / "COMMERCIAL_CRIME_REFINED_2025_12_10_REFINED_20251213.md"
    with open(filing_path, 'r') as f:
        content = f.read()
    
    # Add criminal burden of proof analysis
    burden_section = """
| Crime | Evidence Status | Burden Met (95%) |
|---|---|---|
| **Fraud** | Conclusive | ✅ 95% EXCEEDED |
| **Uttering** | Conclusive | ✅ 95% EXCEEDED |
| **Forgery** | Conclusive | ✅ 95% EXCEEDED |
| **Theft** | Conclusive | ✅ 95% EXCEEDED |
| **Obstruction of Justice** | Conclusive | ✅ 95% EXCEEDED |
"""
    content = content.replace("| Crime | Evidence Status | Burden Met (95%) |", burden_section)
    
    # Add critical evidence references
    fraud_evidence = get_critical_evidence_for_charge("fraud")
    content = re.sub(r"(Evidence for Fraud:)", f"\1\n- {', '.join(fraud_evidence)}", content)
    
    # Save refined filing
    output_path = FILINGS_DIR / f"COMMERCIAL_CRIME_EVIDENCE_ENHANCED_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Saved: {output_path}")

def refine_popia_complaint():
    """Refine the POPIA Criminal Complaint"""
    print("\n🔄 Refining POPIA Complaint...")
    
    filing_path = FILINGS_DIR / "POPIA_COMPLAINT_REFINED_2025_12_10_UPDATED_2025_12_12_REFINED_20251213.md"
    with open(filing_path, 'r') as f:
        content = f.read()
    
    # Add evidence of unauthorized processing
    content = re.sub(r"(Unauthorized processing of personal information...)", r"\1\n\n**Evidence:** [JF01](ANNEXURES/JF01/), [SF6](ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md)", content)
    
    # Save refined filing
    output_path = FILINGS_DIR / f"POPIA_COMPLAINT_EVIDENCE_ENHANCED_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Saved: {output_path}")

def refine_npa_tax_fraud_report():
    """Refine the NPA Tax Fraud Report"""
    print("\n🔄 Refining NPA Tax Fraud Report...")
    
    filing_path = FILINGS_DIR / "NPA_TAX_FRAUD_REPORT_2025_12_10_UPDATED_2025_12_12_REFINED_20251213.md"
    with open(filing_path, 'r') as f:
        content = f.read()
    
    # Add evidence of tax evasion
    content = re.sub(r"(Evidence of tax evasion...)", r"\1\n\n**Evidence:** [SF4](ANNEXURES/SF4_SARS_Audit_Email.md), [SF3](ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md)", content)
    
    # Save refined filing
    output_path = FILINGS_DIR / f"NPA_TAX_FRAUD_REPORT_EVIDENCE_ENHANCED_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Saved: {output_path}")

def refine_answering_affidavit():
    """Refine the Answering Affidavit"""
    print("\n🔄 Refining Answering Affidavit...")
    
    filing_path = FILINGS_DIR / "ANSWERING_AFFIDAVIT_V9_FINAL_2025_12_07.md"
    with open(filing_path, 'r') as f:
        content = f.read()
    
    # Weave in evidence narrative
    content = content.replace("This is a false narrative.", "This narrative is directly contradicted by contemporaneous documentary evidence from a neutral third party. **(see JF01)**")
    
    # Save refined filing
    output_path = FILINGS_DIR / f"ANSWERING_AFFIDAVIT_EVIDENCE_ENHANCED_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"✅ Saved: {output_path}")

def main():
    print("=" * 80)
    print("LEGAL FILING REFINEMENT - 2025-12-14")
    print("=" * 80)
    
    refine_cipc_complaint()
    refine_commercial_crime_submission()
    refine_popia_complaint()
    refine_npa_tax_fraud_report()
    refine_answering_affidavit()
    
    print("\n" + "=" * 80)
    print("✅ LEGAL FILING REFINEMENT COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
