#!/usr/bin/env python3
"""
Refine legal filings based on new evidence and analysis.
"""

import json
from pathlib import Path

def load_refinement_data():
    """Load the refinement data from the JSON file."""
    refinement_file = Path("/home/ubuntu/revstream1/REFINEMENT_DATA_2025_12_18.json")
    with open(refinement_file, 'r') as f:
        return json.load(f)

def refine_civil_filing(filing_path, refinement_data):
    """Refine a civil action filing."""
    with open(filing_path, 'r') as f:
        content = f.read()

    new_evidence_section = """\n## Addendum: New Evidence and Refined Arguments (2025-12-18)\n
Subsequent analysis and cross-referencing with newly available evidence from the ad-res-j7 repository has uncovered additional proof supporting the claims in this filing. The following new evidence strengthens the case on the balance of probabilities (50% burden of proof):\n
"""

    for event in refinement_data['new_events']:
        if 'burden_of_proof' in event and event['burden_of_proof']['civil'] in ['HIGH', 'MEDIUM']:
            new_evidence_section += f"- **{event['id']} ({event['date']}): {event['title']}**\n"
            new_evidence_section += f"  - **Evidence:** {', '.join(event['evidence'])}\n"
            new_evidence_section += f"  - **Description:** {event['description']}\n"
            new_evidence_section += f"  - **Civil Burden of Proof:** Meets the standard based on {event['burden_of_proof']['evidence_type']}.\n\n"

    content += new_evidence_section

    with open(filing_path, 'w') as f:
        f.write(content)
    print(f"Refined civil filing: {filing_path.name}")

def refine_criminal_filing(filing_path, refinement_data):
    """Refine a criminal action filing."""
    with open(filing_path, 'r') as f:
        content = f.read()

    new_evidence_section = """\n## Addendum: New Evidence for Criminal Complaint (2025-12-18)\n
The following new evidence has been identified that meets the criminal burden of proof (beyond a reasonable doubt, 95%) or provides strong indicators of criminal intent:\n
"""

    for event in refinement_data['new_events']:
        if 'burden_of_proof' in event and event['burden_of_proof']['criminal'] in ['HIGH', 'MEDIUM']:
            new_evidence_section += f"- **{event['id']} ({event['date']}): {event['title']}**\n"
            new_evidence_section += f"  - **Evidence:** {', '.join(event['evidence'])}\n"
            new_evidence_section += f"  - **Description:** {event['description']}\n"
            new_evidence_section += f"  - **Criminal Burden of Proof:** Strong indicator of criminal conduct based on {event['burden_of_proof']['evidence_type']}.\n\n"

    content += new_evidence_section

    with open(filing_path, 'w') as f:
        f.write(content)
    print(f"Refined criminal filing: {filing_path.name}")

def main():
    """Main function to refine all legal filings."""
    print("=" * 80)
    print("REFINING LEGAL FILINGS")
    print("=" * 80)
    print()

    refinement_data = load_refinement_data()
    filings_dir = Path("/home/ubuntu/revstream1/docs/filings")

    # Refine Civil Filings
    civil_dir = filings_dir / 'civil'
    for filing in civil_dir.glob('*.md'):
        refine_civil_filing(filing, refinement_data)

    # Refine Criminal Filings
    criminal_dir = filings_dir / 'criminal'
    for filing in criminal_dir.glob('*.md'):
        refine_criminal_filing(filing, refinement_data)

    # You can add more refinement functions for other filing types here
    # (e.g., CIPC, POPIA, etc.) following the same pattern.

    print()
    print("LEGAL FILINGS REFINED SUCCESSFULLY")
    print("=" * 80)
    print()

if __name__ == "__main__":
    main()
