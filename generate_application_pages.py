#!/usr/bin/env python3
"""Generates detailed application pages for GitHub Pages."""
import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_entity_name(entity_id, entities_data):
    """Get entity name from entity ID."""
    for person in entities_data.get('entities', {}).get('persons', []):
        if person.get('entity_id') == entity_id:
            return person.get('name')
    for org in entities_data.get('entities', {}).get('organizations', []):
        if org.get('entity_id') == entity_id:
            return org.get('name')
    return entity_id

def generate_application_page(app_id, title, description, entities, events, evidence, filings, output_path, entities_data):
    """Generates a markdown page for a single application."""
    content = f"# {title}\n\n"
    content += f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
    content += f"{description}\n\n"

    content += "## Key Entities Involved\n\n"
    for entity_id in entities:
        entity_name = get_entity_name(entity_id, entities_data)
        content += f"- **{entity_name}** ([{entity_id}](./entities/{entity_id}.md))\n"

    content += "\n## Key Events\n\n"
    for event_id in events:
        content += f"- [{event_id}](./events/{event_id}.md)\n"

    content += "\n## Core Evidence\n\n"
    for ev in evidence:
        content += f"- {ev}\n"

    content += "\n## Relevant Filings\n\n"
    for filing in filings:
        content += f"- [{os.path.basename(filing)}]({filing})\n"

    with open(output_path, 'w') as f:
        f.write(content)
    print(f"Generated application page: {output_path}")

def main():
    print("="*80)
    print("GENERATING DETAILED APPLICATION PAGES")
    print("="*80)

    base_path = "/home/ubuntu/revstream1"
    docs_path = os.path.join(base_path, 'docs')
    data_models_path = os.path.join(base_path, 'data_models')

    entities_data = load_json(os.path.join(data_models_path, 'entities', 'entities.json'))

    # Application 1: Civil & Criminal Actions
    generate_application_page(
        app_id='1',
        title='Application 1: Civil & Criminal Actions',
        description='This application covers civil claims related to financial damages and criminal charges for fraud, theft, and other offenses.',
        entities=['PERSON_001', 'PERSON_002', 'PERSON_007'],
        events=['EVENT_001', 'EVENT_002', 'EVENT_003', 'EVENT_006', 'EVENT_007', 'EVENT_008', 'EVENT_016', 'EVENT_017', 'EVENT_018', 'EVENT_019', 'EVENT_020'],
        evidence=['JF01', 'JF03', 'JF07', 'JF08', 'SF9', 'Ketoni Timeline'],
        filings=['./filings/CIPC_REFINED_2026_01_22.md', './filings/POPIA_REFINED_2026_01_22.md'],
        output_path=os.path.join(docs_path, 'application-1-civil-criminal-detailed.md'),
        entities_data=entities_data
    )

    # Application 2: CIPC & POPIA Complaints
    generate_application_page(
        app_id='2',
        title='Application 2: CIPC & POPIA Complaints',
        description='This application addresses violations of the Companies Act and the Protection of Personal Information Act.',
        entities=['PERSON_001', 'PERSON_002', 'ORG_001', 'ORG_002'],
        events=['EVENT_CIPC_001', 'EVENT_CIPC_002', 'EVENT_CIPC_003', 'EVENT_CIPC_004', 'EVENT_CIPC_005'],
        evidence=['JF04', 'JF14', 'JF15', 'SF1', 'SF2', 'SF6', 'SF7'],
        filings=['./filings/CIPC_REFINED_2026_01_22.md', './filings/POPIA_REFINED_2026_01_22.md'],
        output_path=os.path.join(docs_path, 'application-2-cipc-popia-detailed.md'),
        entities_data=entities_data
    )

    # Application 3: Commercial Crime & Tax Fraud
    generate_application_page(
        app_id='3',
        title='Application 3: Commercial Crime & Tax Fraud',
        description='This application details commercial crimes such as fraud and theft, as well as tax evasion and related offenses.',
        entities=['PERSON_001', 'PERSON_002', 'ORG_001', 'ORG_002'],
        events=['EVENT_092', 'EVENT_093', 'EVENT_094', 'EVENT_095', 'EVENT_096', 'EVENT_097', 'EVENT_098', 'EVENT_99', 'EVENT_100', 'EVENT_101', 'EVENT_102', 'EVENT_103', 'EVENT_104'],
        evidence=['JF03', 'SF1', 'SF3', 'SF4'],
        filings=['./filings/COMMERCIAL_CRIME_REFINED_2026_01_22.md', './filings/NPA_REFINED_2026_01_22.md'],
        output_path=os.path.join(docs_path, 'application-3-commercial-crime-tax-fraud-detailed.md'),
        entities_data=entities_data
    )

    print("\n" + "="*80)
    print("APPLICATION PAGE GENERATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
