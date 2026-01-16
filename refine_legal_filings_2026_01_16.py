#!/usr/bin/env python3
"""
Legal Filings Refinement Script for revstream1
Date: 2026-01-16
Purpose: Refine legal filings with the Ketoni payout motive.
"""

import os
import re
from datetime import datetime

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

def refine_cipc_complaint(content, version):
    """Refine the CIPC complaint with the Ketoni motive."""
    # Add Ketoni motive to the introduction
    intro_pattern = r"(This complaint details a sophisticated scheme of corporate and financial misconduct)"
    ketoni_intro = "This complaint details a sophisticated scheme of corporate and financial misconduct, driven by the ultimate goal of controlling an ZAR 18.75 million payout from Ketoni Investment Holdings to the Faucitt Family Trust, due in May 2026."
    content = re.sub(intro_pattern, ketoni_intro, content, 1)

    # Add specific section on Ketoni
    ketoni_section = """\n## 3. The Ketoni Payout: Central Financial Motive\n
The primary motive for the corporate misconduct detailed herein is the control of a ZAR 18.75 million payout from Ketoni Investment Holdings (ORG_015), due in May 2026. The Faucitt Family Trust (TRUST_001) is a shareholder in Ketoni, and the actions of Peter Faucitt (PERSON_001) and his co-conspirators appear to be a concerted effort to consolidate control over the Trust and its assets prior to this significant liquidity event.\n"""
    content = content.replace("## 3. Timeline of Misconduct", f"{ketoni_section}\n## 4. Timeline of Misconduct")

    # Update version
    version_string = f"Version: {version}"
    if re.search(r"Version: .+", content):
        content = re.sub(r"Version: .+", version_string, content)
    else:
        content = f"{version_string}\n\n{content}"
    return content

def refine_npa_report(content, version):
    """Refine the NPA Tax Fraud Report with the Ketoni motive."""
    # Add Ketoni motive to the summary
    summary_pattern = r"(This report outlines a complex case of suspected tax fraud)"
    ketoni_summary = "This report outlines a complex case of suspected tax fraud, which appears to be a component of a larger scheme to unlawfully control a ZAR 18.75 million payout from Ketoni Investment Holdings, due to the Faucitt Family Trust in May 2026."
    content = re.sub(summary_pattern, ketoni_summary, content, 1)

    # Add Ketoni section
    ketoni_section = """\n### The Ketoni Payout Motive\n
The financial manipulations and suspected tax evasion detailed in this report must be viewed in the context of the upcoming ZAR 18.75 million payout from Ketoni Investment Holdings. The perpetrators\' actions suggest a coordinated effort to misappropriate funds and conceal assets in anticipation of this event.\n"""
    content = content.replace("### Evidence Summary", f"{ketoni_section}\n### Evidence Summary")

    # Update version
    version_string = f"Version: {version}"
    if re.search(r"Version: .+", content):
        content = re.sub(r"Version: .+", version_string, content)
    else:
        content = f"{version_string}\n\n{content}"
    return content

def refine_popia_complaint(content, version):
    """Refine the POPIA complaint with the Ketoni motive."""
    # Add Ketoni motive to the background
    background_pattern = r"(This complaint concerns multiple violations of the Protection of Personal Information Act)"
    ketoni_background = "This complaint concerns multiple violations of the Protection of Personal Information Act (POPIA), which were instrumental in a broader scheme to gain control over the Faucitt Family Trust and its primary asset: a ZAR 18.75 million payout from Ketoni Investment Holdings due in May 2026."
    content = re.sub(background_pattern, ketoni_background, content, 1)

    # Update version
    version_string = f"Version: {version}"
    if re.search(r"Version: .+", content):
        content = re.sub(r"Version: .+", version_string, content)
    else:
        content = f"{version_string}\n\n{content}"
    return content

def main():
    print("Refining legal filings with Ketoni motive...")
    filings_path = '/home/ubuntu/revstream1/docs/filings'
    today = datetime.now().strftime('%Y_%m_%d')

    # Refine CIPC Complaint
    latest_cipc = max([f for f in os.listdir(filings_path) if f.startswith('CIPC_COMPLAINT_REFINED') and f.endswith('.md')])
    cipc_content = read_file(os.path.join(filings_path, latest_cipc))
    new_cipc_version = f"CIPC_COMPLAINT_REFINED_{today}.md"
    refined_cipc = refine_cipc_complaint(cipc_content, f"v3.0-ketoni-{today}")
    write_file(os.path.join(filings_path, new_cipc_version), refined_cipc)
    print(f"Created refined CIPC complaint: {new_cipc_version}")

    # Refine NPA Tax Fraud Report
    latest_npa = max([f for f in os.listdir(filings_path) if f.startswith('NPA_TAX_FRAUD_REPORT_REFINED') and f.endswith('.md')])
    npa_content = read_file(os.path.join(filings_path, latest_npa))
    new_npa_version = f"NPA_TAX_FRAUD_REPORT_REFINED_{today}.md"
    refined_npa = refine_npa_report(npa_content, f"v3.0-ketoni-{today}")
    write_file(os.path.join(filings_path, new_npa_version), refined_npa)
    print(f"Created refined NPA report: {new_npa_version}")

    # Refine POPIA Complaint
    latest_popia = max([f for f in os.listdir(filings_path) if f.startswith('POPIA_COMPLAINT_REFINED') and f.endswith('.md')])
    popia_content = read_file(os.path.join(filings_path, latest_popia))
    new_popia_version = f"POPIA_COMPLAINT_REFINED_{today}.md"
    refined_popia = refine_popia_complaint(popia_content, f"v3.0-ketoni-{today}")
    write_file(os.path.join(filings_path, new_popia_version), refined_popia)
    print(f"Created refined POPIA complaint: {new_popia_version}")

    print("\nLegal filings successfully refined.")

if __name__ == '__main__':
    main()
