#!/usr/bin/env python3
"""
GitHub Pages Update Script
Date: 2026-01-18
Purpose: To update the GitHub Pages documentation in the revstream1 repository with the
         latest analysis, evidence, and visualizations from the refined data models.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timelines" / "timeline.json"


def load_json(filepath):
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def generate_timeline_md(timeline_data):
    """Generate a markdown file for the timeline."""
    if not timeline_data:
        return ""

    md = "# Comprehensive Case Timeline\n\n"
    md += f"**Last Updated:** {timeline_data['metadata']['last_updated']}\n\n"
    md += "| Date       | Event                                      | Key Actors                               | Significance                               | Evidence                                   |\n"
    md += "|------------|--------------------------------------------|------------------------------------------|--------------------------------------------|--------------------------------------------|\n"

    for event in sorted(timeline_data.get('timeline', []), key=lambda x: x.get('date', '')):
        date = event.get('date', 'N/A')
        title = event.get('title', 'N/A')
        actors = ', '.join(event.get('key_actor_names', []))
        significance = event.get('significance', 'N/A')
        evidence = ', '.join(event.get('evidence', []))
        md += f"| {date} | {title} | {actors} | {significance} | {evidence} |\n"

    return md

def generate_entities_md(entities_data):
    """Generate a markdown file for the entities."""
    if not entities_data:
        return ""

    md = "# Key Entities and Persons of Interest\n\n"
    md += f"**Last Updated:** {entities_data['metadata']['last_updated']}\n\n"

    md += "## Persons of Interest\n\n"
    md += "| Name                  | Role                      | Involvement (Events) | Financial Impact   | Criminal Threshold |\n"
    md += "|-----------------------|---------------------------|----------------------|--------------------|--------------------|\n"
    for person in entities_data.get('entities', {}).get('persons', []):
        name = person.get('name', 'N/A')
        role = person.get('role', 'N/A')
        events = person.get('involvement_events', 0)
        impact = person.get('financial_impact', {}).get('direct_involvement', 'N/A')
        threshold = person.get('criminal_threshold', 'N/A')
        md += f"| {name} | {role} | {events} | {impact} | {threshold} |\n"

    md += "\n## Organizations\n\n"
    md += "| Name                      | Type                      | Significance                               |\n"
    md += "|---------------------------|---------------------------|--------------------------------------------|\n"
    for org in entities_data.get('entities', {}).get('organizations', []):
        name = org.get('name', 'N/A')
        org_type = org.get('entity_type', 'N/A')
        significance = org.get('significance', 'N/A')
        md += f"| {name} | {org_type} | {significance} |\n"

    return md

def update_index_md():
    """Update the main index.md file."""
    index_path = DOCS_DIR / "index.md"
    with open(index_path, 'r') as f:
        content = f.read()

    # Add a new section for the 2020 Trial Balance Analysis
    new_section = """
## 📉 2020 Trial Balance Analysis: The Blueprint for Fraud

The newly integrated trial balance evidence from 2019-2020 reveals a sophisticated blueprint for financial manipulation that predates the 2025 fraud events. This evidence is critical in establishing a long-standing pattern of behavior.

**Key Findings:**
- **Systematic Profit Shifting**: Profits were artificially concentrated in RegimA Skin Treatments (RST) through mechanisms like inter-company debt and interest payments.
- **Coordinated Cost Dumping**: Expenses were systematically dumped onto RegimA Worldwide Distribution (RWW) to obscure true profitability.
- **Capital Extraction**: Villa Via was used as a vehicle for capital extraction through large, unexplained members' loans.
- **Centralized Control**: A single bookkeeper, controlled by the co-director, managed all entity accounts, enabling centralized manipulation.

**[→ View Detailed 2020 Financial Analysis](./2020-financial-analysis.md)**

---
"""
    if "2020 Trial Balance Analysis" not in content:
        content = content.replace("## 📊 Quick Navigation by Application", new_section + "## 📊 Quick Navigation by Application")

    with open(index_path, 'w') as f:
        f.write(content)
    print("Updated index.md with 2020 Trial Balance Analysis section.")

def main():
    """Main function to update GitHub Pages."""
    print("=" * 60)
    print("Updating GitHub Pages Documentation")
    print(f"Date: {datetime.now().isoformat()}")
    print("=" * 60)

    # Load data
    entities_data = load_json(ENTITIES_FILE)
    timeline_data = load_json(TIMELINE_FILE)

    # Generate new markdown files
    timeline_md = generate_timeline_md(timeline_data)
    with open(DOCS_DIR / "timeline.md", 'w') as f:
        f.write(timeline_md)
    print("Generated new timeline.md")

    entities_md = generate_entities_md(entities_data)
    with open(DOCS_DIR / "entities.md", 'w') as f:
        f.write(entities_md)
    print("Generated new entities.md")

    # Create a placeholder for the new detailed analysis page
    with open(DOCS_DIR / "2020-financial-analysis.md", 'w') as f:
        f.write("# 2020 Financial Analysis\n\n*Content to be added*")
    print("Created placeholder for 2020-financial-analysis.md")

    # Update the main index file
    update_index_md()

    print("\n" + "=" * 60)
    print("GitHub Pages Update Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
