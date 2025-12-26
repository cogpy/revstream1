#!/usr/bin/env python3
"""
GitHub Pages Generation Script
Date: 2025-11-26
Purpose: Generate well-organized GitHub Pages with clear evidence references from refined data models.
"""

import json
from pathlib import Path

# Paths
REVSTREAM1_PATH = Path("/home/ubuntu/revstream1")
DOCS_PATH = REVSTREAM1_PATH / "docs"
DATA_MODELS_PATH = REVSTREAM1_PATH / "data_models"

# Input data models
ENTITIES_PATH = DATA_MODELS_PATH / "entities/entities_refined_2025_11_26_v20.json"
EVENTS_PATH = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v21.json"
TIMELINE_PATH = DATA_MODELS_PATH / "timelines/timeline_refined_2025_11_26_v11.json"

# Output directories
ENTITIES_DOCS_PATH = DOCS_PATH / "entities"
EVENTS_DOCS_PATH = DOCS_PATH / "events"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def write_md_file(content, filepath):
    """Write content to a Markdown file"""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {filepath}")

def generate_entity_pages(entities_data):
    """Generate individual Markdown pages for each entity."""
    print("\n=== Generating Entity Pages ===")
    entities_list = []
    for category in entities_data.get("entities", {}).values():
        entities_list.extend(category)

    for entity in entities_list:
        entity_id = entity.get("entity_id")
        if not entity_id:
            continue

        content = f'''---
layout: default
title: "{entity.get("name", entity_id)}"
---
# {entity.get("name", entity_id)}

| Field | Value |
|---|---|
| **Entity ID** | `{entity_id}` |
| **Name** | {entity.get("name", "N/A")} |
| **Role** | {entity.get("role", "N/A")} |
| **Agent Type** | {entity.get("agent_type", "N/A")} |
| **Involvement Events** | {entity.get("involvement_events", "N/A")} |

## Evidence References

'''
        if "evidence_files_enhanced" in entity:
            for evidence in entity["evidence_files_enhanced"]:
                content += f'- [{evidence["reference"]}]({evidence["github_url"]})\n'
        else:
            content += "No direct evidence files linked.\n"
        
        content += f'\n[View in Comprehensive Evidence Index]({entity.get("comprehensive_evidence_index")})\n'

        filepath = ENTITIES_DOCS_PATH / f"{entity_id}.md"
        write_md_file(content, filepath)

def generate_event_pages(events_data):
    """Generate individual Markdown pages for each event."""
    print("\n=== Generating Event Pages ===")
    for event in events_data.get("events", []):
        event_id = event.get("event_id")
        if not event_id:
            continue

        content = f'''---
layout: default
title: "Event: {event.get("title", event_id)}"
---
# {event.get("title", event_id)}

| Field | Value |
|---|---|
| **Event ID** | `{event_id}` |
| **Date** | {event.get("date", "N/A")} |
| **Category** | {event.get("category", "N/A")} |
| **Related Application** | [{event.get("related_application", "N/A")}]({event.get("application_url", "#")}) |

## Description

{event.get("description", "No description provided.")}

## Evidence References

'''
        if "evidence_references_enhanced" in event:
            for evidence in event["evidence_references_enhanced"]:
                content += f'- [{evidence["reference"]}]({evidence["github_url"]})\n'
        else:
            content += "No direct evidence files linked.\n"

        filepath = EVENTS_DOCS_PATH / f"{event_id}.md"
        write_md_file(content, filepath)

def generate_application_evidence_pages(events_data):
    """Generate dedicated evidence summary pages for each application."""
    print("\n=== Generating Application Evidence Pages ===")
    apps = {"APPLICATION_1": [], "APPLICATION_2": [], "APPLICATION_3": []}
    for event in events_data.get("events", []):
        app = event.get("related_application")
        if app in apps:
            apps[app].append(event)

    for app_name, app_events in apps.items():
        app_num = app_name.split("_")[1]
        content = f'''---
layout: default
title: "Evidence for Application {app_num}"
---
# Evidence Summary for Application {app_num}

This page summarizes the key events and evidence related to Application {app_num}.

'''
        for event in sorted(app_events, key=lambda x: x.get("date", "")):
            event_id = event.get("event_id")
            content += f'## [{event.get("title")}]({event.get("github_pages_url")})\n'
            content += f'*Date: {event.get("date")}*\n\n'
            content += f'{event.get("description")}\n\n'
            if "evidence_references_enhanced" in event:
                content += "**Evidence:**\n"
                for evidence in event["evidence_references_enhanced"]:
                    content += f'- [{evidence["reference"]}]({evidence["github_url"]})\n'
            content += "\n---\n"

        filepath = DOCS_PATH / f"application-{app_num}-evidence.md"
        write_md_file(content, filepath)

def generate_interactive_timeline(timeline_data, events_data):
    """Generate an HTML page for the interactive timeline."""
    print("\n=== Generating Interactive Timeline Page ===")
    events_dict = {event['event_id']: event for event in events_data.get("events", [])}
    
    html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Interactive Case Timeline</title>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<style>
body { font-family: sans-serif; }
.timeline-event { border-left: 3px solid #4285F4; padding-left: 15px; margin-bottom: 20px; }
.timeline-event h3 { margin-top: 0; }
</style>
</head>
<body>
<h1>Interactive Case Timeline</h1>
"""

    for phase_key, phase in sorted(timeline_data.get("timeline_phases", {}).items(), key=lambda item: item[1]['start_date']):
        html_content += f'<h2 id="{phase.get("phase_id")}">{phase.get("phase_name")} ({phase.get("start_date")} to {phase.get("end_date")})</h2>\n'
        for event_id in phase.get("events", []):
            event = events_dict.get(event_id)
            if event:
                html_content += f'''
<div class="timeline-event" id="{event_id}">
    <h3><a href="./events/{event_id}.html">{event.get("title")}</a></h3>
    <p><strong>Date:</strong> {event.get("date")}</p>
    <p>{event.get("description")}</p>
'''
                if "evidence_references_enhanced" in event:
                    html_content += "<p><strong>Evidence:</strong></p><ul>"
                    for evidence in event["evidence_references_enhanced"]:
                        html_content += f'<li><a href="{evidence["github_url"]}" target="_blank">{evidence["reference"]}</a></li>'
                    html_content += "</ul>"
                html_content += "</div>\n"

    html_content += "</body>\n</html>"
    filepath = DOCS_PATH / "timeline.html"
    write_md_file(html_content, filepath)

def update_main_index():
    """Update the main index.md to link to the new pages."""
    print("\n=== Updating Main Index Page ===")
    index_path = REVSTREAM1_PATH / "index.md"
    with open(index_path, 'r') as f:
        content = f.read()

    # Update links to application evidence
    content = content.replace("](application-1.md)", "](application-1.md)\n[View Evidence for Application 1 →](application-1-evidence.md)")
    content = content.replace("](application-2.md)", "](application-2.md)\n[View Evidence for Application 2 →](application-2-evidence.md)")
    content = content.replace("](application-3.md)", "](application-3.md)\n[View Evidence for Application 3 →](application-3-evidence.md)")

    # Update timeline link
    content = content.replace("[Detailed Timeline](timeline.md)", "[Interactive Timeline](timeline.html)")

    with open(index_path, 'w') as f:
        f.write(content)
    print("✓ Updated index.md")

def main():
    """Main generation process"""
    print("=" * 60)
    print("GitHub Pages Generation - 2025-11-26")
    print("=" * 60)

    # Load refined data models
    entities_data = load_json(ENTITIES_PATH)
    events_data = load_json(EVENTS_PATH)
    timeline_data = load_json(TIMELINE_PATH)

    # Generate pages
    generate_entity_pages(entities_data)
    generate_event_pages(events_data)
    generate_application_evidence_pages(events_data)
    generate_interactive_timeline(timeline_data, events_data)
    
    # Update main index
    update_main_index()

    print("\n" + "=" * 60)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()
