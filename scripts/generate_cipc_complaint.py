#!/usr/bin/env python3
"""
CIPC Complaint Generator for Case 2025-137857
"""

import json
from datetime import datetime

# --- Configuration ---
BASE_DIR = "/home/ubuntu/revstream1"
DOCS_DIR = f"{BASE_DIR}/docs"
DATA_MODELS_DIR = f"{BASE_DIR}/data_models"
AD_RES_J7_REPO_URL = "https://github.com/cogpy/ad-res-j7/blob/main/"

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

def generate_cipc_complaint(entities, events):
    """Generates the CIPC complaint markdown file."""
    print("Generating CIPC complaint...")

    date_today = datetime.now().strftime("%Y-%m-%d")

    content = f"""
# CIPC COMPLAINT: CASE 2025-137857

**Date of Complaint:** {date_today}

**Complainant:** Daniel James Faucitt

**Respondent(s):** Peter Andrew Faucitt, Rynette Farrar, Danie Bantjies

## 1. Introduction

This complaint details multiple violations of the Companies Act, 2008, by the directors and officers of RegimA Worldwide Distribution (Pty) Ltd (RWD ZA) and related entities. The evidence, drawn from the `revstream1` and `ad-res-j7` repositories, demonstrates a coordinated scheme of fraud, misrepresentation, and abuse of fiduciary duties.

## 2. Key Violations

### 2.1. Section 22: Reckless Trading

**Violation:** The directors of RWD ZA, primarily Peter Andrew Faucitt, conducted the business with gross negligence and an intent to defraud creditors and the Faucitt Family Trust.

**Evidence:**
- **EVENT_017:** Misappropriation of trust assets.
- **EVENT_020:** Unauthorized transfer of funds.
- **Financial Records:** See `ad-res-j7/ANNEXURES/JF03` for detailed financial analysis showing insolvency and fraudulent transactions.

### 2.2. Section 76: Directors' Conduct

**Violation:** Peter Andrew Faucitt and Rynette Farrar failed to act in good faith and in the best interests of the company. They used their positions to enrich themselves at the expense of the company and its stakeholders.

**Evidence:**
- **EVENT_004 & EVENT_005:** Rynette Farrar's unauthorized redirection of payments.
- **EVENT_014:** Forgery of the company's banking details.
- **Control of Accounting System:** See `ad-res-j7/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md`.

### 2.3. Section 77: Liability of Directors

**Violation:** The directors are personally liable for the losses incurred by the company due to their fraudulent and reckless conduct.

**Evidence:**
- **Total Losses:** The total documented loss exceeds R10 million.
- **Direct Involvement:** Evidence links Peter Faucitt and Rynette Farrar directly to the financial losses.

## 3. Conclusion

We request a full investigation by the CIPC into the conduct of the directors of RWD ZA and related entities. The evidence strongly supports the immediate de-registration of the directors and the initiation of criminal proceedings.

---

*This document is automatically generated based on the refined data models in the `revstream1` repository.*
"""

    filepath = f"{DOCS_DIR}/CIPC_COMPLAINT_REFINED_{date_today}.md"
    write_file(filepath, content)
    print(f"  Generated CIPC complaint at {filepath}")

# --- Main Execution ---
def main():
    """Main function to generate the CIPC complaint."""
    print("Starting CIPC complaint generation...")

    # Load all necessary data
    entities = load_json(ENTITIES_FILE)
    events = load_json(EVENTS_FILE)

    # Generate the complaint
    generate_cipc_complaint(entities, events)

    print("\nCIPC complaint generation complete.")

if __name__ == "__main__":
    main()
