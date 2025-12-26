#!/usr/bin/env python3
"""
Update GitHub Pages with New Legal Correspondence Data
Date: 2025-11-26
Purpose: Generate new entity and event pages based on updated data models.
"""

import json
from pathlib import Path

# Paths
REVSTREAM1_PATH = Path("/home/ubuntu/revstream1")
DATA_MODELS_PATH = REVSTREAM1_PATH / "data_models"
DOCS_PATH = REVSTREAM1_PATH / "docs"
ENTITIES_DOCS_PATH = DOCS_PATH / "entities"
EVENTS_DOCS_PATH = DOCS_PATH / "events"

# Input data models (latest versions)
ENTITIES_PATH = DATA_MODELS_PATH / "entities/entities_refined_2025_11_26_v21.json"
EVENTS_PATH = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v22.json"

# Ensure output directories exist
ENTITIES_DOCS_PATH.mkdir(exist_ok=True)
EVENTS_DOCS_PATH.mkdir(exist_ok=True)

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_markdown(content, filepath):
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✓ Saved: {filepath}")

def generate_entity_pages(entities_data):
    """Generate pages for the two new law firm entities."""
    print("\n=== Generating New Entity Pages ===")
    organizations = entities_data["entities"]["organizations"]
    new_org_ids = ["ORG_011", "ORG_012"]
    
    for org in organizations:
        if org["entity_id"] in new_org_ids:
            entity_id = org["entity_id"]
            name = org["name"]
            
            content = f"# Entity Profile: {name}\n\n"
            content += f"**Entity ID:** {entity_id}\n"
            content += f"**Type:** {org.get('type', 'N/A')}\n"
            content += f"**Role:** {org.get('role', 'N/A')}\n\n"
            content += "## Contact Details\n"
            content += f"- **Email:** {org['contact_details'].get('email', 'N/A')}\n"
            content += f"- **Phone:** {org['contact_details'].get('phone', 'N/A')}\n"
            content += f"- **Address:** {org['contact_details'].get('address', 'N/A')}\n"
            content += f"- **Website:** {org['contact_details'].get('website', 'N/A')}\n\n"
            content += "## Involvement\n"
            content += f"**Involvement Events:** {org.get('involvement_events', 0)}\n"
            content += f"**Timeline Events:** {', '.join(org.get('timeline_events', []))}\n\n"
            content += "## Evidence\n"
            for file in org.get('evidence_files', []):
                content += f"- [{file}](https://github.com/cogpy/ad-res-j7/blob/main/{file})\n"
            
            filepath = ENTITIES_DOCS_PATH / f"{entity_id}.md"
            save_markdown(content, filepath)

def generate_event_pages(events_data):
    """Generate pages for the four new legal events."""
    print("\n=== Generating New Event Pages ===")
    events = events_data["events"]
    new_event_ids = ["EVENT_074", "EVENT_075", "EVENT_076", "EVENT_077"]
    
    for event in events:
        if event["event_id"] in new_event_ids:
            event_id = event["event_id"]
            title = event["title"]
            
            content = f"# Event: {title}\n\n"
            content += f"**Event ID:** {event_id}\n"
            content += f"**Date:** {event['date']}\n"
            content += f"**Category:** {event['category']}\n\n"
            content += "## Description\n"
            content += f"{event['description']}\n\n"
            content += "## Details\n"
            content += f"- **Legal Significance:** {event.get('legal_significance', 'N/A')}\n"
            content += f"- **Related Application:** [{event['related_application']}](https://cogpy.github.io/revstream1/{event['related_application'].lower()}.html)\n\n"
            content += "## Evidence\n"
            for file in event.get('evidence_files', []):
                # Correcting the path for the link
                clean_file = file.lstrip('./')
                content += f"- [{clean_file}](https://github.com/cogpy/ad-res-j7/blob/main/{clean_file})\n"

            filepath = EVENTS_DOCS_PATH / f"{event_id}.md"
            save_markdown(content, filepath)

def main():
    """Main update process"""
    print("=" * 60)
    print("GitHub Pages Update - New Legal Correspondence (2025-11-26)")
    print("=" * 60)
    
    # Load updated data models
    print("\n=== Loading Updated Data Models ===")
    entities_data = load_json(ENTITIES_PATH)
    events_data = load_json(EVENTS_PATH)
    print("✓ All data models loaded")
    
    # Generate new pages
    generate_entity_pages(entities_data)
    generate_event_pages(events_data)
    
    print("\n" + "=" * 60)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 60)
    print("\nNew Pages Generated:")
    print("  ✓ 2 new entity pages (ORG_011, ORG_012)")
    print("  ✓ 4 new event pages (EVENT_074 to EVENT_077)")

if __name__ == "__main__":
    main()
