#!/usr/bin/env python3
"""
Comprehensive Legal Filings Generation Script - 2026-01-22
Generates all required legal filings based on the latest enhanced data models.
"""

import json
import os
from datetime import datetime

REVSTREAM_PATH = "/home/ubuntu/revstream1"
FILINGS_PATH = f"{REVSTREAM_PATH}/docs/filings"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_filing_header(title, version):
    return f"""# {title}

**Version:** {version}  
**Date:** {datetime.now().strftime('%Y-%m-%d')}  
**Case Reference:** 2025-137857  

---
"""

def generate_popia_complaint(events_data):
    title = "POPIA Criminal Complaint"
    version = f"POPIA_REFINED_{datetime.now().strftime('%Y_%m_%d')}"
    content = generate_filing_header(title, version)
    content += """## 1. Complaint Details

This complaint is filed against Peter Andrew Faucitt and Rynette Farrar for severe breaches of the Protection of Personal Information Act (POPIA), 4 of 2013.

"""
    content += """## 2. Core Allegations

*   **Section 86(1):** Unauthorized access to and modification of personal information.
*   **Section 86(3):** Unauthorized disclosure of personal information.
*   **Identity Fraud:** Use of personal information to commit identity fraud.

"""
    content += """## 3. Evidence of POPIA Breaches

"""
    for event in sorted(events_data.get('events', []), key=lambda x: x.get('date', '')):
        if "POPIA" in event.get("significance", "") or "identity_fraud" in event.get("description", ""):
            content += f"### {event.get('title', event.get('event_id'))}\n"
            content += f"*   **Date:** {event.get('date')}\n"
            content += f"*   **Description:** {event.get('description')}\n"
            content += f"*   **Evidence:** {', '.join(event.get('evidence', []))}\n\n"

    filepath = f"{FILINGS_PATH}/{version}.md"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Generated: {filepath}")

def generate_npa_tax_fraud_report(events_data):
    title = "NPA Tax Fraud Report"
    version = f"NPA_REFINED_{datetime.now().strftime('%Y_%m_%d')}"
    content = generate_filing_header(title, version)
    content += """## 1. Report Details

This report outlines evidence of systematic tax fraud and evasion by Peter Andrew Faucitt and associated entities.

"""
    content += """## 2. Core Allegations

*   **Income Tax Evasion:** Deliberate misrepresentation of income and expenses to evade income tax.
*   **VAT Fraud:** Manipulation of VAT returns and claims.
*   **SARS Obstruction:** Deliberate actions to obstruct SARS audits and investigations.

"""
    content += """## 3. Evidence of Tax Fraud

"""
    for event in sorted(events_data.get('events', []), key=lambda x: x.get('date', '')):
        if "tax" in event.get("significance", "").lower() or "sars" in event.get("description", "").lower():
            content += f"### {event.get('title', event.get('event_id'))}\n"
            content += f"*   **Date:** {event.get('date')}\n"
            content += f"*   **Description:** {event.get('description')}\n"
            content += f"*   **Evidence:** {', '.join(event.get('evidence', []))}\n\n"

    filepath = f"{FILINGS_PATH}/{version}.md"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Generated: {filepath}")

def generate_commercial_crime_submission(events_data):
    title = "Commercial Crime Case Submission"
    version = f"COMMERCIAL_CRIME_REFINED_{datetime.now().strftime('%Y_%m_%d')}"
    content = generate_filing_header(title, version)
    content += """## 1. Submission Details

This submission details evidence of commercial crimes, including fraud, theft, and forgery.

"""
    content += """## 2. Core Allegations

*   **Fraud:** Misrepresentation with the intent to deceive, resulting in financial loss.
*   **Theft:** Unlawful appropriation of funds and assets.
*   **Forgery:** Creation of false documents to perpetrate fraud.

"""
    content += """## 3. Evidence of Commercial Crimes

"""
    for event in sorted(events_data.get('events', []), key=lambda x: x.get('date', '')):
        if "fraud" in event.get("significance", "").lower() or "theft" in event.get("description", "").lower():
            content += f"### {event.get('title', event.get('event_id'))}\n"
            content += f"*   **Date:** {event.get('date')}\n"
            content += f"*   **Description:** {event.get('description')}\n"
            content += f"*   **Evidence:** {', '.join(event.get('evidence', []))}\n\n"

    filepath = f"{FILINGS_PATH}/{version}.md"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Generated: {filepath}")

def main():
    print("=" * 60)
    print("Comprehensive Legal Filings Generation - 2026-01-22")
    print("=" * 60)

    events_data = load_json(f"{REVSTREAM_PATH}/data_models/events/events.json")

    print("\n[1/3] Generating POPIA Complaint...")
    generate_popia_complaint(events_data)

    print("\n[2/3] Generating NPA Tax Fraud Report...")
    generate_npa_tax_fraud_report(events_data)

    print("\n[3/3] Generating Commercial Crime Submission...")
    generate_commercial_crime_submission(events_data)

    print("\n" + "=" * 60)
    print("All Legal Filings Generated Successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
