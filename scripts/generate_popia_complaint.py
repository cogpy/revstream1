#!/usr/bin/env python3
"""
POPIA Complaint Generator for Case 2025-137857
"""

import json
from datetime import datetime

# --- Configuration ---
BASE_DIR = "/home/ubuntu/revstream1"
DOCS_DIR = f"{BASE_DIR}/docs"
DATA_MODELS_DIR = f"{BASE_DIR}/data_models"

# --- File Paths ---
ENTITIES_FILE = f"{DATA_MODELS_DIR}/entities/entities.json"
EVENTS_FILE = f"{DATA_MODELS_DIR}/events/events.json"

# --- Helper Functions ---
def load_json(filepath):
    """Loads a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def write_file(filepath, content):
    """Writes content to a file."""
    with open(filepath, 'w') as f:
        f.write(content)

# --- Generation Functions ---

def generate_popia_complaint(entities, events):
    """Generates the POPIA complaint markdown file."""
    print("Generating POPIA complaint...")

    date_today = datetime.now().strftime("%Y-%m-%d")

    content = f"""
# POPIA CRIMINAL COMPLAINT: CASE 2025-137857

**Date of Complaint:** {date_today}

**Complainant:** Daniel James Faucitt

**Respondent(s):** Peter Andrew Faucitt, Rynette Farrar

## 1. Introduction

This complaint outlines serious violations of the Protection of Personal Information Act (POPIA) by Peter Andrew Faucitt and Rynette Farrar. The evidence demonstrates unlawful processing of personal information, failure to secure personal data, and unauthorized access to sensitive information.

## 2. Key Violations

### 2.1. Section 11 & 12: Unlawful Processing of Personal Information

**Violation:** The respondents unlawfully processed personal information, including identity numbers and financial data, without the consent of the data subjects.

**Evidence:**
- **EVENT_025:** Identity fraud in domain registration.
- **EVENT_026:** Impersonation and unauthorized use of personal details.
- **`ad-res-j7/ANNEXURES/JF09`:** Domain registration fraud evidence.

### 2.2. Section 19: Failure to Secure Personal Information

**Violation:** The respondents failed to implement reasonable security safeguards to protect personal information, leading to unauthorized access and misuse.

**Evidence:**
- **EVENT_015:** Unauthorized changes to bank beneficiaries.
- **`ad-res-j7/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md`:** Evidence of unauthorized access to the accounting system.

### 2.3. Section 21: Notification of Security Compromises

**Violation:** The respondents failed to notify the Information Regulator and the affected data subjects of the security breaches.

**Evidence:**
- No notification of the data breaches was ever issued by the respondents, despite the widespread misuse of personal information.

## 3. Conclusion

We urge the Information Regulator to investigate these serious violations of POPIA. The evidence supports the imposition of significant penalties and the referral of the matter for criminal prosecution.

---

*This document is automatically generated based on the refined data models in the `revstream1` repository.*
"""

    filepath = f"{DOCS_DIR}/POPIA_COMPLAINT_REFINED_{date_today}.md"
    write_file(filepath, content)
    print(f"  Generated POPIA complaint at {filepath}")

# --- Main Execution ---
def main():
    """Main function to generate the POPIA complaint."""
    print("Starting POPIA complaint generation...")

    # Load all necessary data
    entities = load_json(ENTITIES_FILE)
    events = load_json(EVENTS_FILE)

    # Generate the complaint
    generate_popia_complaint(entities, events)

    print("\nPOPIA complaint generation complete.")

if __name__ == "__main__":
    main()
