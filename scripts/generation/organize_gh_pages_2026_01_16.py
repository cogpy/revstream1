#!/usr/bin/env python3
"""
GitHub Pages Organization Script for revstream1
Date: 2026-01-16
Purpose: Regenerate GitHub Pages documentation from updated data models.
"""

import json
import os
from datetime import datetime

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

def generate_entity_pages(entities_data, base_path):
    print("Generating entity pages...")
    # Generate individual entity pages
    for entity_type, entity_list in entities_data['entities'].items():
        for entity in entity_list:
            entity_id = entity['entity_id']
            content = f"# {entity['name']} ({entity_id})\n\n"
            content += f"**Role:** {entity.get('role', 'N/A')}\n\n"
            content += f"```json\n{json.dumps(entity, indent=2)}\n```\n"
            write_file(f"{base_path}/entities/{entity_id}.md", content)

    # Generate entity index page
    index_content = "# Entities Index\n\n"
    for entity_type, entity_list in entities_data['entities'].items():
        index_content += f"## {entity_type.capitalize()}\n\n"
        for entity in entity_list:
            index_content += f"- [{entity['name']} ({entity['entity_id']})](./{entity['entity_id']}.md)\n"
        index_content += "\n"
    write_file(f"{base_path}/entities/index.md", index_content)
    print(f"Generated {len(entities_data['entities']['persons']) + len(entities_data['entities']['organizations']) + len(entities_data['entities']['trusts'])} entity pages and index.")

def generate_event_pages(events_data, base_path):
    print("Generating event pages...")
    # Generate individual event pages
    for event in events_data['events']:
        event_id = event['event_id']
        content = f"# {event.get('title', event_id)} ({event_id})\n\n"
        content += f"**Date:** {event.get('date', 'N/A')}\n\n"
        content += f"**Description:** {event.get('description', 'N/A')}\n\n"
        content += f"```json\n{json.dumps(event, indent=2)}\n```\n"
        write_file(f"{base_path}/events/{event_id}.md", content)

    # Generate event index page
    index_content = "# Events Index\n\n"
    for event in sorted(events_data['events'], key=lambda x: x.get('date', '')):
        index_content += f"- **{event.get('date', 'N/A')}**: [{event.get('title', event['event_id'])}](./{event['event_id']}.md)\n"
    write_file(f"{base_path}/events/index.md", index_content)
    print(f"Generated {len(events_data['events'])} event pages and index.")

def generate_timeline_page(timeline_data, base_path):
    print("Generating timeline page...")
    content = "# Comprehensive Timeline\n\n"
    if 'phase_structure' in timeline_data:
        content += "## Timeline Phases (Ketoni-Centric)\n\n"
        for phase, details in timeline_data['phase_structure'].items():
            content += f"### {phase}: {details['description']}\n"
            content += f"- **Period:** {details['period']}\n"
            content += f"- **Key Events:** {details.get('key_events', details.get('key_event'))}\n\n"

    content += "## Event Log\n\n"
    for entry in sorted(timeline_data['timeline'], key=lambda x: x.get('date', '')):
        content += f"### {entry['date']}\n"
        content += f"{entry['description']}\n"
        content += "<details>\n"
        content += "<summary>Details</summary>\n\n"
        content += f"```json\n{json.dumps(entry, indent=2)}\n```\n"
        content += "</details>\n\n"
    write_file(f"{base_path}/timeline.md", content)
    print("Generated timeline page.")

def main():
    print("Starting GitHub Pages regeneration...")
    data_model_path = '/home/ubuntu/revstream1/docs/data_models'
    docs_path = '/home/ubuntu/revstream1/docs'

    entities = load_json(f"{data_model_path}/entities/entities.json")
    events = load_json(f"{data_model_path}/events.json")
    timeline = load_json(f"{data_model_path}/timeline.json")

    generate_entity_pages(entities, docs_path)
    generate_event_pages(events, docs_path)
    generate_timeline_page(timeline, docs_path)

    print("\nGitHub Pages documentation successfully regenerated.")

if __name__ == '__main__':
    main()
