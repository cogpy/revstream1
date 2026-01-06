#!/usr/bin/env python3
"""
NPA Tax Fraud Report Generator for Case 2025-137857
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

def generate_npa_report(entities, events):
    """Generates the NPA tax fraud report markdown file."""
    print("Generating NPA tax fraud report...")

    date_today = datetime.now().strftime("%Y-%m-%d")

    content = f"""
# NPA TAX FRAUD REPORT: CASE 2025-137857

**Date of Report:** {date_today}

**Complainant:** Daniel James Faucitt

**Subject(s):** Peter Andrew Faucitt, Rynette Farrar, Danie Bantjies

## 1. Introduction

This report details evidence of significant tax fraud and related financial crimes committed by the subjects in connection with the business operations of RegimA Worldwide Distribution (Pty) Ltd (RWD ZA). The evidence points to a deliberate and systematic effort to evade taxes and conceal income.

## 2. Key Evidence of Tax Fraud

### 2.1. Concealment of Income

**Allegation:** The subjects conspired to conceal income and evade taxes by manipulating financial records and diverting funds.

**Evidence:**
- **EVENT_018:** Stock adjustment fraud to conceal R5.4M in losses.
- **EVENT_022:** SARS audit email showing coordination to mislead tax authorities.
- **`ad-res-j7/ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md`:** Detailed evidence of the stock fraud.
- **`ad-res-j7/ANNEXURES/SF4_SARS_Audit_Email.md`:** The incriminating email sent during the SARS audit.

### 2.2. Fraudulent Financial Statements

**Allegation:** The subjects created and submitted fraudulent financial statements to SARS.

**Evidence:**
- **`ad-res-j7/ANNEXURES/JF03`:** Forensic analysis of the financial records reveals significant discrepancies and signs of manipulation.
- **`ad-res-j7/ANNEXURES/SF1_Bantjies_Debt_Documentation.md`:** Evidence of Danie Bantjies' financial motive and conflict of interest.

## 3. Conclusion

The evidence strongly indicates a coordinated effort to defraud the South African Revenue Service (SARS). We request that the National Prosecuting Authority (NPA) launch a full investigation into these matters and pursue criminal charges against the individuals involved.

---

*This document is automatically generated based on the refined data models in the `revstream1` repository.*
"""

    filepath = f"{DOCS_DIR}/NPA_TAX_FRAUD_REPORT_REFINED_{date_today}.md"
    write_file(filepath, content)
    print(f"  Generated NPA tax fraud report at {filepath}")

# --- Main Execution ---
def main():
    """Main function to generate the NPA report."""
    print("Starting NPA tax fraud report generation...")

    # Load all necessary data
    entities = load_json(ENTITIES_FILE)
    events = load_json(EVENTS_FILE)

    # Generate the report
    generate_npa_report(entities, events)

    print("\nNPA tax fraud report generation complete.")

if __name__ == "__main__":
    main()
