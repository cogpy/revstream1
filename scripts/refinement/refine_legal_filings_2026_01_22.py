#!/usr/bin/env python3
"""
Legal Filings Refinement Script - 2026-01-22
Refines legal filings based on the latest enhanced data models and evidence.
"""

import json
import os
from datetime import datetime

REVSTREAM_PATH = "/home/ubuntu/revstream1"
FILINGS_PATH = f"{REVSTREAM_PATH}/docs/filings"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_filing_header(title, version):
    """Generate a standardized header for legal filings"""
    return f"""# {title}

**Version:** {version}  
**Date:** {datetime.now().strftime('%Y-%m-%d')}  
**Case Reference:** 2025-137857  

---
"""

def generate_cipc_complaint(entities_data, events_data):
    """Generate the CIPC Companies Act Complaint"""
    title = "CIPC Companies Act Complaint"
    version = f"CIPC_REFINED_{datetime.now().strftime('%Y_%m_%d')}"
    content = generate_filing_header(title, version)

    content += """## 1. Complainant Details

*   **Name:** Daniel James Faucitt
*   **ID Number:** [REDACTED]
*   **Contact:** [REDACTED]

"""
    content += """## 2. Implicated Directors and Companies

| Director/Company | Role | Registration/ID |
|---|---|---|
| **Peter Andrew Faucitt** | Primary Perpetrator | 820430 5708 18 5 |
| **Rynette Farrar** | Co-Conspirator | [ID REDACTED] |
| **RegimA Worldwide Distribution (Pty) Ltd** | Vehicle for Fraud | 2013/168495/07 |
| **RegimA Skin Treatments (Pty) Ltd** | Vehicle for Fraud | 1992/005371/23 |
| **Strategic Logistics (Pty) Ltd** | Vehicle for Fraud | 2003/004863/07 |
| **Villa Via (Pty) Ltd** | Vehicle for Fraud | 2003/004863/07 |
| **Adderory (Pty) Ltd** | Competing Infrastructure | 2021/601219/07 |

"""

    content += """## 3. Nature of Complaint: Breaches of the Companies Act, 71 of 2008

This complaint details severe breaches of the Companies Act by the implicated directors, primarily focusing on:

*   **Section 22: Reckless Trading:** Operating the companies recklessly, with gross negligence, and with intent to defraud creditors and beneficiaries.
*   **Section 76: Director's Standard of Conduct:** Failure to act in good faith and for a proper purpose; using their position for personal gain; and communicating company information to unauthorized persons.
*   **Section 77: Liability of Directors:** Willful misconduct and breach of trust leading to significant financial loss.

"""

    content += """## 4. Core Allegation: The Ketoni Payout Motive

The central motive for the fraudulent activities is the **ZAR 18.75 million payout** from Ketoni Investment Holdings to the Faucitt Family Trust, due in May 2026. All actions by the implicated directors from mid-2024 onwards were aimed at consolidating control over the Trust and its assets to seize this payout.

"""

    content += """## 5. Chronological Evidence of Misconduct

"""

    # Sort events chronologically
    sorted_events = sorted(events_data.get('events', []), key=lambda x: x.get('date', ''))

    for event in sorted_events:
        # Include events that have been verified and are significant
        if event.get('burden_of_proof', '').startswith('verified') and 'CRITICAL' in event.get('significance', ''):
            content += f"### {event.get('title', event.get('event_id'))}\n"
            content += f"*   **Date:** {event.get('date')}\n"
            content += f"*   **Description:** {event.get('description')}\n"
            content += f"*   **Significance:** {event.get('significance')}\n"
            content += f"*   **Evidence:** {', '.join(event.get('evidence', []))}\n"
            content += f"*   **Breach:** Sections 22, 76, 77 of the Companies Act\n\n"

    content += """## 6. Relief Sought

*   An immediate and thorough investigation into the conduct of the directors and the financial affairs of the implicated companies.
*   A declaration of the directors as delinquent under Section 162 of the Companies Act.
*   The imposition of the maximum administrative penalties as deemed appropriate by the Commission.
"""

    filepath = f"{FILINGS_PATH}/{version}.md"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Generated: {filepath}")

def main():
    print("=" * 60)
    print("Legal Filings Refinement - 2026-01-22")
    print("=" * 60)

    # Load data models
    entities_data = load_json(f"{REVSTREAM_PATH}/data_models/entities/entities.json")
    events_data = load_json(f"{REVSTREAM_PATH}/data_models/events/events.json")

    # Generate CIPC Complaint
    print("\n[1/1] Generating CIPC Complaint...")
    generate_cipc_complaint(entities_data, events_data)

    print("\n" + "=" * 60)
    print("Legal Filings Refinement Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
