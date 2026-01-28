#!/usr/bin/env python3
"""
Generate and Refine Legal Filings Script

Generates CIPC, POPIA, NPA, and Commercial Crime filings based on the
refined data models from the LEX Investigation.

Case: 2025-137857 - Revenue Stream Hijacking
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
FILINGS_DIR = Path("/home/ubuntu/revstream1/docs/filings")

TIMESTAMP = datetime.now().isoformat()
DATE_STAMP = datetime.now().strftime("%Y-%m-%d")
DATE_FILE = datetime.now().strftime("%Y_%m_%d")

def load_json(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def get_entity(entities, entity_id):
    """Get entity by ID."""
    if not entities:
        return None
    for person in entities.get("entities", {}).get("persons", []):
        if person.get("entity_id") == entity_id:
            return person
    for org in entities.get("entities", {}).get("organizations", []):
        if org.get("entity_id") == entity_id:
            return org
    return None

def generate_cipc_complaint(entities, events):
    """Generate the CIPC complaint."""
    print("\n=== Generating CIPC Complaint ===")
    
    complainant = get_entity(entities, "PERSON_005") # Daniel Faucitt
    respondents = [
        get_entity(entities, "PERSON_001"), # Peter Faucitt
        get_entity(entities, "PERSON_002"), # Rynette Farrar
        get_entity(entities, "PERSON_007")  # Danie Bantjies
    ]
    
    violations = []
    for event in events.get("events", []):
        desc = str(event.get("description", "")).lower()
        if "cipc" in desc or "companies act" in desc:
            violations.append({
                "section": event.get("title", "N/A"),
                "description": event.get("description"),
                "evidence": event.get("evidence", [])
            })

    content = f"""# CIPC Complaint: Case 2025-137857

**Date of Filing:** {DATE_STAMP}

## 1. Complainant Details

- **Name:** {complainant.get('name') if complainant else 'N/A'}
- **Capacity:** Shareholder & Director

## 2. Respondent Details

"""
    for resp in respondents:
        if resp:
            content += f"""- **Name:** {resp.get('name')}
- **Position:** {resp.get('role')}
"""

    content += """## 3. Summary of Complaint

This complaint details numerous violations of the Companies Act, 2008, by the directors and officeholders of several related entities, primarily involving fraud, reckless trading, and breaches of fiduciary duty.

## 4. Violations of the Companies Act

"""

    # Add violations from events
    # This is a simplified representation. A real implementation would be more detailed.
    for violation in violations[:5]:
        content += f"""### {violation['section']}

**Description:** {violation['description']}

**Evidence:**
"""
        for ev in violation['evidence']:
            content += f"- {ev}\n"

    filing_path = FILINGS_DIR / f"CIPC_REFINED_{DATE_FILE}.md"
    with open(filing_path, 'w') as f:
        f.write(content)
    print(f"  Generated: {filing_path}")

def generate_popia_complaint(entities, events):
    """Generate the POPIA complaint."""
    print("\n=== Generating POPIA Complaint ===")
    
    complainant = get_entity(entities, "PERSON_005") # Daniel Faucitt
    respondents = [
        get_entity(entities, "PERSON_001"), # Peter Faucitt
        get_entity(entities, "PERSON_002"), # Rynette Farrar
    ]
    
    violations = []
    for event in events.get("events", []):
        desc = str(event.get("description", "")).lower()
        if "popia" in desc or "data protection" in desc:
            violations.append({
                "section": event.get("title", "N/A"),
                "description": event.get("description"),
                "evidence": event.get("evidence", [])
            })

    content = f"""# POPIA Complaint: Case 2025-137857\n\n**Date of Filing:** {DATE_STAMP}\n\n## 1. Complainant Details\n\n- **Name:** {complainant.get('name') if complainant else 'N/A'}\n- **Capacity:** Data Subject\n\n## 2. Respondent Details\n\n"""
    for resp in respondents:
        if resp:
            content += f"""- **Name:** {resp.get('name')}\n- **Position:** {resp.get('role')}\n"""

    content += """## 3. Summary of Complaint\n\nThis complaint outlines multiple breaches of the Protection of Personal Information Act (POPIA), including unlawful processing of personal information, identity fraud, and failure to secure data.\n\n## 4. Violations of POPIA\n\n"""

    for violation in violations[:5]:
        content += f"""### {violation['section']}\n\n**Description:** {violation['description']}\n\n**Evidence:**\n"""
        for ev in violation['evidence']:
            content += f"- {ev}\n"

    filing_path = FILINGS_DIR / f"POPIA_REFINED_{DATE_FILE}.md"
    with open(filing_path, 'w') as f:
        f.write(content)
    print(f"  Generated: {filing_path}")

def generate_npa_report(entities, events):
    """Generate the NPA Tax Fraud report."""
    print("\n=== Generating NPA Tax Fraud Report ===")
    
    content = f"""# NPA Tax Fraud Report: Case 2025-137857\n\n**Date of Filing:** {DATE_STAMP}\n\n## 1. Subject of Report\n
- **Primary Individuals:** Peter Andrew Faucitt, Rynette Farrar
- **Primary Entities:** RegimA Skin Treatments, Strategic Logistics, Villa Via

## 2. Summary of Allegations\n
This report details suspected tax fraud, including income tax evasion, VAT fraud, and obstruction of a SARS audit, based on evidence gathered in case 2025-137857.\n\n## 3. Key Evidence of Tax Fraud\n\n"""
    tax_events = []
    for event in events.get("events", []):
        desc = str(event.get("description", "")).lower()
        if "tax" in desc or "sars" in desc:
            tax_events.append(event)
    
    for event in tax_events[:5]:
        content += f"""### {event.get('title', 'N/A')}\n\n**Description:** {event.get('description')}\n\n**Evidence:**\n"""
        for ev in event.get('evidence', []):
            content += f"- {ev}\n"

    filing_path = FILINGS_DIR / f"NPA_REFINED_{DATE_FILE}.md"
    with open(filing_path, 'w') as f:
        f.write(content)
    print(f"  Generated: {filing_path}")

def generate_commercial_crime_submission(entities, events):
    """Generate the Commercial Crime submission."""
    print("\n=== Generating Commercial Crime Submission ===")
    
    content = f"""# Commercial Crime Submission: Case 2025-137857\n\n**Date of Submission:** {DATE_STAMP}\n\n## 1. Suspects\n
- **Primary:** Peter Andrew Faucitt
- **Accomplice:** Rynette Farrar

## 2. Summary of Crimes\n
This submission outlines a complex commercial crime scheme involving fraud, theft, forgery, and money laundering, resulting in financial losses exceeding R10 million.\n\n## 3. Modus Operandi\n
1.  **Revenue Stream Hijacking:** Diverting company revenue to unauthorized accounts.
2.  **Trust Manipulation:** Abusing fiduciary duties to control trust assets.
3.  **Identity Fraud:** Registering domains and companies using fraudulent information.
4.  **Financial Manipulation:** Using inter-company loans and false accounting entries to conceal theft.

## 4. Key Criminal Events\n\n"""
    crime_events = []
    for event in events.get("events", []):
        if event.get("criminal_threshold"):
            crime_events.append(event)
            
    for event in crime_events[:5]:
        content += f"""### {event.get('title', 'N/A')}\n\n**Date:** {event.get('date')}\n
**Description:** {event.get('description')}\n
**Evidence:**\n"""
        for ev in event.get('evidence', []):
            content += f"- {ev}\n"

    filing_path = FILINGS_DIR / f"COMMERCIAL_CRIME_REFINED_{DATE_FILE}.md"
    with open(filing_path, 'w') as f:
        f.write(content)
    print(f"  Generated: {filing_path}")

def main():
    """Main execution."""
    print("\n" + "="*70)
    print("LEGAL FILING GENERATION")
    print(f"Timestamp: {TIMESTAMP}")
    print("="*70)
    
    FILINGS_DIR.mkdir(exist_ok=True)
    
    # Load data
    entities = load_json(DATA_MODELS_DIR / "entities" / "entities.json")
    events = load_json(DATA_MODELS_DIR / "events" / "events.json")
    
    # Generate filings
    generate_cipc_complaint(entities, events)
    generate_popia_complaint(entities, events)
    generate_npa_report(entities, events)
    generate_commercial_crime_submission(entities, events)
    
    print("\n" + "="*70)
    print("FILING GENERATION COMPLETE")
    print("="*70)

if __name__ == "__main__":
    main()
