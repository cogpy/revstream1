#!/usr/bin/env python3
"""
Legal Filings Refinement Script
Date: 2025-11-26
Purpose: Iteratively improve and refine legal filings based on the enhanced data models and evidence structure.
"""

import json
import os
from pathlib import Path

# Paths
REVSTREAM1_PATH = Path("/home/ubuntu/revstream1")
AD_RES_J7_PATH = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS_PATH = REVSTREAM1_PATH / "data_models"

# Input data models
EVENTS_PATH = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v21.json"

# Legal Filings Paths
CIVIL_RESPONSE_PATH = AD_RES_J7_PATH / "1-CIVIL-RESPONSE"
CRIMINAL_CASE_PATH = AD_RES_J7_PATH / "2-CRIMINAL-CASE"
OUTPUT_PATH = REVSTREAM1_PATH / "refined_legal_filings"

# Templates for new filings
CIPC_COMPLAINT_TEMPLATE = """
# CIPC Companies Act Complaint

**Date:** {date}
**Case Reference:** {case_number}

## 1. Complainant Details

- **Name:** [Complainant Name]
- **Contact:** [Complainant Contact]

## 2. Company/Director Details

- **Company Name:** Regma (Pty) Ltd (and related entities)
- **Director(s) Implicated:** Peter Andrew Faucitt, Rynette Farrar

## 3. Nature of Complaint

This complaint details breaches of the Companies Act, No. 71 of 2008, including but not limited to:

- **Section 76:** Director's standard of conduct (acting in bad faith, for personal gain).
- **Section 77:** Liability of directors (willful misconduct, breach of trust).
- **Section 22:** Reckless trading.

## 4. Summary of Evidence

The following events and evidence, cross-referenced from the project repository, support this complaint:

{evidence_summary}

## 5. Relief Sought

- Investigation into the conduct of the directors.
- Declaration of directors as delinquent under Section 162.
- Administrative penalties as deemed appropriate by the Commission.
"""

POPIA_COMPLAINT_TEMPLATE = """
# POPIA Criminal Complaint

**Date:** {date}
**Case Reference:** {case_number}

## 1. Complainant Details

- **Name:** Daniel James Faucitt / Jacqueline Faucitt
- **Contact:** [Complainant Contact]

## 2. Responsible Party Details

- **Name:** Peter Andrew Faucitt
- **Role:** Alleged controller of personal information.

## 3. Nature of Complaint

This complaint concerns the unlawful processing and distribution of personal information, in contravention of the Protection of Personal Information Act (POPIA), specifically:

- **Section 11 & 12:** Unlawful processing and collection of personal information.
- **Section 19:** Failure to implement security safeguards.
- **Section 21:** Unauthorized disclosure of personal information.

## 4. Summary of Evidence

The following events demonstrate clear violations of POPIA:

{evidence_summary}

## 5. Relief Sought

- Investigation by the Information Regulator.
- Enforcement action and potential criminal prosecution for the identified breaches.
"""

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_file(content, filepath):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {filepath}")

def get_relevant_events(events_data, keywords):
    """Filter events based on keywords in their description or title."""
    relevant_events = []
    for event in events_data.get("events", []):
        description = event.get("description", "").lower()
        title = event.get("title", "").lower()
        if any(keyword in description or keyword in title for keyword in keywords):
            relevant_events.append(event)
    return sorted(relevant_events, key=lambda x: x.get("date", ""))

def format_evidence_summary(events):
    """Format a list of events into a Markdown summary."""
    summary = ""
    for event in events:
        summary += f'### [{event.get("title")}]({event.get("github_pages_url")})\n'
        summary += f'*Date: {event.get("date")}*\n\n'
        summary += f'{event.get("description")}\n\n'
        if "evidence_references_enhanced" in event:
            summary += "**Evidence:**\n"
            for evidence in event["evidence_references_enhanced"]:
                summary += f'- [{evidence["reference"]}]({evidence["github_url"]})\n'
        summary += "\n---\n"
    return summary

def generate_cipc_complaint(events_data):
    """Generate the CIPC Companies Act Complaint."""
    print("\n=== Generating CIPC Complaint ===")
    keywords = ["cipc", "director", "company", "reckless", "fraud", "misconduct"]
    relevant_events = get_relevant_events(events_data, keywords)
    evidence_summary = format_evidence_summary(relevant_events)
    
    content = CIPC_COMPLAINT_TEMPLATE.format(
        date="2025-11-26",
        case_number="2025-137857-CIPC",
        evidence_summary=evidence_summary
    )
    
    filepath = OUTPUT_PATH / "CIPC_Companies_Act_Complaint.md"
    write_file(content, filepath)

def generate_popia_complaint(events_data):
    """Generate the POPIA Criminal Complaint."""
    print("\n=== Generating POPIA Complaint ===")
    keywords = ["popia", "personal information", "data breach", "privacy"]
    relevant_events = get_relevant_events(events_data, keywords)
    evidence_summary = format_evidence_summary(relevant_events)

    content = POPIA_COMPLAINT_TEMPLATE.format(
        date="2025-11-26",
        case_number="2025-137857-POPIA",
        evidence_summary=evidence_summary
    )

    filepath = OUTPUT_PATH / "POPIA_Criminal_Complaint.md"
    write_file(content, filepath)

def main():
    """Main generation process for legal filings."""
    print("=" * 60)
    print("Legal Filings Refinement - 2025-11-26")
    print("=" * 60)

    # Load refined events data
    events_data = load_json(EVENTS_PATH)

    # Generate new complaint documents
    generate_cipc_complaint(events_data)
    generate_popia_complaint(events_data)

    print("\n" + "=" * 60)
    print("LEGAL FILINGS REFINEMENT COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()
