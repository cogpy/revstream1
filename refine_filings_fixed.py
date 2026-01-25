#!/usr/bin/env python3
"""Refines legal filings based on evidence analysis and burden of proof."""
import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_entity_details(entity_id, entities_data):
    """Get entity details from entity ID."""
    for person in entities_data.get('entities', {}).get('persons', []):
        if person.get('entity_id') == entity_id:
            return person
    for org in entities_data.get('entities', {}).get('organizations', []):
        if org.get('entity_id') == entity_id:
            return org
    return None

def refine_filing(filing_path, output_path, entities_data, events_data, evidence_quality_data):
    """Refines a single legal filing with enhanced evidence and analysis."""
    with open(filing_path, 'r') as f:
        content = f.read()

    # Add a summary of evidence strength at the top
    summary = "\n## Evidence Strength Summary\n\n"
    summary += "| Entity | Role/Type | Evidence Score | Burden of Proof Met |\n"
    summary += "|---|---|---|---|\n"

    # Get relevant entities from the evidence quality analysis
    for entity in evidence_quality_data['burden_of_proof_analysis']['criminal_standard']['entities_exceeding']:
        role_or_type = entity.get('role', entity.get('type', 'unknown'))
        summary += f"| {entity['name']} | {role_or_type} | {entity['evidence_score']}% | **Criminal (95%)** |\n"
    for entity in evidence_quality_data['burden_of_proof_analysis']['civil_standard']['entities_meeting']:
        role_or_type = entity.get('role', entity.get('type', 'unknown'))
        summary += f"| {entity['name']} | {role_or_type} | {entity['evidence_score']}% | **Civil (50%)** |\n"

    content = summary + "\n" + content

    # Add a section with critical recommendations
    recommendations = "\n## Critical Issues to Address\n\n"
    for rec in evidence_quality_data.get('recommendations', []):
        if rec.get('priority') == 'CRITICAL':
            recommendations += f"- **{rec['category']}:** {rec['issue']}. **Action:** {rec['action']}\n"

    content += recommendations

    with open(output_path, 'w') as f:
        f.write(content)
    print(f"Refined filing saved to: {output_path}")

def main():
    print("="*80)
    print("REFINING LEGAL FILINGS")
    print("="*80)

    base_path = "/home/ubuntu/revstream1"
    docs_path = os.path.join(base_path, 'docs')
    filings_path = os.path.join(docs_path, 'filings')
    data_models_path = os.path.join(base_path, 'data_models')

    entities_data = load_json(os.path.join(data_models_path, 'entities', 'entities.json'))
    events_data = load_json(os.path.join(data_models_path, 'events', 'events.json'))
    evidence_quality_data = load_json(os.path.join(data_models_path, 'EVIDENCE_QUALITY_ANALYSIS_2026_01_25.json'))

    filings_to_refine = [
        'CIPC_REFINED_2026_01_22.md',
        'POPIA_REFINED_2026_01_22.md',
        'NPA_REFINED_2026_01_22.md',
        'COMMERCIAL_CRIME_REFINED_2026_01_22.md'
    ]

    for filing in filings_to_refine:
        filing_path = os.path.join(filings_path, filing)
        if os.path.exists(filing_path):
            output_filename = filing.replace('2026_01_22', datetime.now().strftime('%Y_%m_%d'))
            output_path = os.path.join(filings_path, output_filename)
            refine_filing(filing_path, output_path, entities_data, events_data, evidence_quality_data)
        else:
            print(f"Warning: Filing not found at {filing_path}")

    print("\n" + "="*80)
    print("FILING REFINEMENT COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
