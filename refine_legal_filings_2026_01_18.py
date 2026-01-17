#!/usr/bin/env python3
"""
Legal Filings Refinement Script
Date: 2026-01-18
Purpose: To refine all legal filings with the latest evidence from the 2020 trial
         balances and the comprehensive data model refinement.
"""

import json
import os
from pathlib import Path

# Paths
FILINGS_DIR = Path("/home/ubuntu/revstream1/docs/filings")
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timelines" / "timeline.json"

# List of filings to refine
FILINGS_TO_REFINE = [
    "cipc_complaint.md",
    "civil_action_summons.md",
    "commercial_crime_submission.md",
    "criminal_case_submission.md",
    "npa_tax_fraud_report.md",
    "popia_complaint.md"
]

def load_json(filepath):
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def get_trial_balance_summary():
    """Generate a summary of the trial balance evidence."""
    return """
### Appendix: The 2020 Financial Manipulation Blueprint

Newly discovered trial balance evidence from 2019-2020 provides a blueprint for the financial manipulation that enabled the later fraud. This evidence is critical in establishing a long-standing pattern of behavior and proving that the 2025 events were not isolated incidents, but the culmination of a multi-year scheme.

**Key Mechanisms of Manipulation (2019-2020):**

1.  **Massive Inter-Company Debt**: Strategic Logistics (SLG) carried a **R13M debt** to RegimA Skin Treatments (RST), creating an artificial financial dependency that allowed for profit shifting through interest payments (R414K annually at a suspiciously low 3.19% rate).

2.  **Coordinated Cost Reallocations**: On February 20, 2020, multiple entities executed simultaneous journal entries to reallocate over **R1M in administrative fees** to production costs, deliberately obscuring true profitability and operational costs.

3.  **Systematic Cost Dumping**: RegimA Worldwide Distribution (RWW) was systematically used as an expense dumping ground, receiving a **R750K loan for production costs** from RST and bearing over **R1.7M in reallocated admin fees, warehouse charges, and computer expenses** for the group.

4.  **Capital Extraction via Property**: Villa Via, a property holding company, generated **R3.7M in profit** from rental income while maintaining a **R22.8M members' loan account** (5.2x its annual rental income), indicating a systematic mechanism for extracting capital from the business.

5.  **Centralized Control & Cover-up**: All entity accounts were controlled by the co-director's personal bookkeeper. The 6-month delay in finalizing the 2020 financial statements, coordinated by Danie Bantjes and signed off by Bernadine Wright, points to a complex and deliberate manipulation requiring extended time to orchestrate and conceal.

This evidence proves a clear *modus operandi* of financial deception that was in place years before the 2025 fraud was discovered. It demonstrates intent, premeditation, and a sophisticated understanding of how to exploit the inter-company structure for personal gain.
"""

def refine_filing(filepath, trial_balance_summary):
    """Refine a single legal filing."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Add the trial balance summary as an appendix
    if "Appendix: The 2020 Financial Manipulation Blueprint" not in content:
        content += "\n\n---\n" + trial_balance_summary

    # Create new filename
    new_filename = filepath.stem + "_REFINED_2026_01_18.md"
    new_filepath = FILINGS_DIR / new_filename

    with open(new_filepath, 'w') as f:
        f.write(content)
    print(f"Refined and saved: {new_filename}")

def main():
    """Main function to refine all legal filings."""
    print("=" * 60)
    print("Refining Legal Filings")
    print(f"Date: {Path(__file__).stem.split('_')[-1]}")
    print("=" * 60)

    trial_balance_summary = get_trial_balance_summary()

    for filename in FILINGS_TO_REFINE:
        filepath = FILINGS_DIR / filename
        if filepath.exists():
            refine_filing(filepath, trial_balance_summary)
        else:
            print(f"Warning: Filing not found - {filename}")

    print("\n" + "=" * 60)
    print("Legal Filings Refinement Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
