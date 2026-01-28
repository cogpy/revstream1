#!/usr/bin/env python3
"""
Generate the Master Record for Entities (Entities.md).
"""

import json
from pathlib import Path
from datetime import datetime

REPO_DIR = Path("/home/ubuntu/revstream1")

def load_json(filepath):
    """Load a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def format_person(person):
    """Format a single person entity into Markdown."""
    md = []
    md.append(f"### {person.get('name', 'N/A')} (`{person.get('entity_id', 'N/A')}`)")
    md.append("")
    
    md.append("| Attribute | Details |")
    md.append("|---|---|")
    md.append(f"| **Role** | {person.get('role', 'N/A')} |")
    md.append(f"| **Agent Type** | {person.get('agent_type', 'N/A')} |")
    md.append(f"| **Involvement** | {person.get('involvement_events', 0)} events |")
    
    if 'financial_impact' in person:
        impact = person['financial_impact']
        md.append(f"| **Financial Impact** | {impact.get('direct_involvement', 'N/A')} |")
    
    if 'conflict_of_interest' in person:
        conflict = person['conflict_of_interest']
        md.append(f"| **Conflict of Interest** | {conflict.get('type', 'N/A')}: {conflict.get('description', 'N/A')} |")

    md.append("")
    md.append("**Primary Actions:**")
    md.append("")
    for action in person.get('primary_actions', []):
        md.append(f"- {action.replace('_', ' ').title()}")
    md.append("")

    return "\n".join(md)

def format_organization(org):
    """Format a single organization entity into Markdown."""
    md = []
    md.append(f"### {org.get('name', 'N/A')} (`{org.get('entity_id', 'N/A')}`)")
    md.append("")
    
    md.append("| Attribute | Details |")
    md.append("|---|---|")
    md.append(f"| **Type** | {org.get('type', 'N/A').replace('_', ' ').title()} |")
    md.append(f"| **Role** | {org.get('role', 'N/A').replace('_', ' ').title()} |")
    
    if 'obligation' in org:
        obligation = org['obligation']
        if isinstance(obligation, dict):
             md.append(f"| **Obligation** | {obligation.get('amount', 'N/A')} to {obligation.get('recipient', 'N/A')} by {obligation.get('payout_date', 'N/A')} |")
        else:
            md.append(f"| **Obligation** | {obligation} |")

    if 'owner_director' in org:
        owner = org['owner_director']
        md.append(f"| **Owner/Director** | {owner.get('name', 'N/A')} ({owner.get('position', 'N/A')}) |")

    md.append("")
    return "\n".join(md)

def main():
    """Main function to generate the Entities.md file."""
    entities_path = REPO_DIR / "data_models/entities/entities.json"
    entities_data = load_json(entities_path)
    
    output_path = REPO_DIR / "MR/Entities.md"
    
    md_content = []
    md_content.append("# Master Record: Entities")
    md_content.append("## Agent-Based Natural & Juristic Persons")
    md_content.append("--- ")
    md_content.append(f"*Version: {entities_data['metadata']['version']}* ")
    md_content.append(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}* ")
    md_content.append("")

    # Process Persons
    md_content.append("## Natural Persons (Agents)")
    md_content.append("")
    persons = sorted(entities_data['entities']['persons'], key=lambda x: x.get('name', ''))
    for person in persons:
        md_content.append(format_person(person))
        md_content.append("---")

    # Process Organizations
    md_content.append("## Juristic Persons (Organizations)")
    md_content.append("")
    organizations = sorted(entities_data['entities']['organizations'], key=lambda x: x.get('name', ''))
    for org in organizations:
        md_content.append(format_organization(org))
        md_content.append("---")

    with open(output_path, 'w') as f:
        f.write("\n".join(md_content))
    
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
