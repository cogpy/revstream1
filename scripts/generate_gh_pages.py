#!/usr/bin/env python3
"""
Generate GitHub Pages documentation from refined data models.
"""
import json
import os
from datetime import datetime

# --- Configuration ---
BASE_DIR = "/home/ubuntu/revstream1"
DOCS_DIR = f"{BASE_DIR}/docs"
DATA_MODELS_DIR = f"{BASE_DIR}/data_models"
AD_RES_J7_REPO_URL = "https://github.com/cogpy/ad-res-j7/blob/main/"

# --- File Paths ---
ENTITIES_FILE = f"{DATA_MODELS_DIR}/entities/entities_refined_2025_12_07_v27.json"
EVENTS_FILE = f"{DATA_MODELS_DIR}/events/events_refined_2025_12_07_v29.json"
TIMELINE_FILE = f"{DATA_MODELS_DIR}/timelines/timeline_refined_2025_12_07_v20.json"
RELATIONS_FILE = f"{DATA_MODELS_DIR}/relations/relations_refined_2025_12_07_v22.json"
MAPPING_FILE = f"{BASE_DIR}/AD_RES_J7_EVIDENCE_MAPPING_2025_12_07.json"

# --- Helper Functions ---
def load_json(filepath):
    """Loads a JSON file."""
    if not os.path.exists(filepath):
        print(f"Warning: File not found at {filepath}")
        return None
    with open(filepath, 'r') as f:
        return json.load(f)

def write_file(filepath, content):
    """Writes content to a file, creating directories if needed."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

def format_currency(amount):
    """Formats a number as South African Rand currency."""
    try:
        return f"R{float(amount):,.2f}"
    except (ValueError, TypeError):
        return "R0.00"

# --- Generation Functions ---

def generate_entity_pages(entities_data):
    """Generates individual markdown pages for each entity."""
    print("Generating entity pages...")
    if not entities_data or 'entities' not in entities_data:
        return

    all_entities = entities_data['entities'].get('persons', []) + entities_data['entities'].get('organizations', [])
    
    for entity in all_entities:
        entity_id = entity.get("entity_id")
        name = entity.get("name", "Unnamed Entity")
        content = f"---\nlayout: default\ntitle: {name}\n---\n"
        content += f"# {name} ({entity_id})\n\n"
        content += f"**Role:** {entity.get('role', 'N/A')}\n\n"
        content += f"## Details\n\n"
        content += "| Field | Value |\n"
        content += "|---|---|\n"
        for key, value in entity.items():
            if isinstance(value, (str, int, float)):
                content += f"| {key.replace('_', ' ').title()} | {value} |\n"
        
        content += "\n## Raw Data\n\n```json\n"
        content += json.dumps(entity, indent=2)
        content += "\n```\n"
        
        filepath = f"{DOCS_DIR}/entities/{entity_id}.md"
        write_file(filepath, content)
    print(f"  Generated {len(all_entities)} entity pages.")

def generate_event_pages(events_data, evidence_mapping):
    """Generates individual markdown pages for each event."""
    print("Generating event pages...")
    if not events_data or 'events' not in events_data:
        return

    for event in events_data['events']:
        event_id = event.get("event_id")
        title = event.get("title", "Unnamed Event")
        content = f"---\nlayout: default\ntitle: {title}\n---\n"
        content += f"# {title} ({event_id})\n\n"
        content += f"**Date:** {event.get('date', 'N/A')}\n\n"
        content += f"**Description:**\n{event.get('description', 'No description provided.')}\n\n"
        
        # Add evidence
        content += "## Evidence References\n\n"
        event_links = evidence_mapping.get('event_evidence_links', {}).get(event_id, {})
        locations = event_links.get('evidence_locations', [])
        if locations:
            for loc in locations:
                content += f"- [{loc}]({AD_RES_J7_REPO_URL}{loc})\n"
        else:
            content += "No specific evidence linked.\n"

        content += "\n## Raw Data\n\n```json\n"
        content += json.dumps(event, indent=2)
        content += "\n```\n"

        filepath = f"{DOCS_DIR}/events/{event_id}.md"
        write_file(filepath, content)
    print(f"  Generated {len(events_data['events'])} event pages.")

def generate_timeline_page(timeline_data):
    """Generates the main timeline.md page."""
    print("Generating timeline page...")
    if not timeline_data or 'timeline_events' not in timeline_data:
        return

    content = "---\nlayout: default\ntitle: Interactive Timeline\n---\n# Interactive Timeline of Events\n\n"
    content += "This timeline provides a chronological overview of all key events in case 2025-137857.\n\n"
    content += "| Date | Event ID | Title | Financial Impact | Categories |\n"
    content += "|---|---|---|---|---|\n"

    for event in sorted(timeline_data['timeline_events'], key=lambda x: x.get('date', '')):
        event_id = event.get('event_id')
        impact = event.get('financial_impact')
        
        # Correctly extract amount based on structure
        amount = 0
        if isinstance(impact, dict):
            amount_str = impact.get('amount', '0')
        elif isinstance(impact, str):
            amount_str = impact
        else:
            amount_str = '0'
        
        try:
            amount = float(str(amount_str).replace('R', '').replace(',', '').strip())
        except (ValueError, TypeError):
            amount = 0

        impact_formatted = format_currency(amount) if amount != 0 else "N/A"
        
        title = event.get('title', 'N/A')
        title_link = f"[{title}](./events/{event_id}.md)"
        categories = ", ".join(event.get('categories', []))
        content += f"| {event.get('date', 'N/A')} | [{event_id}](./events/{event_id}.md) | {title_link} | {impact_formatted} | {categories} |\n"

    write_file(f"{DOCS_DIR}/timeline.md", content)
    print(f"  Generated timeline page with {len(timeline_data['timeline_events'])} events.")

def generate_index_page(analysis_summary):
    """Generates the main index.md landing page."""
    print("Generating index page...")
    if not analysis_summary:
        return

    summary = analysis_summary.get('summary', {})
    total_loss = summary.get('total_financial_impact', 0)

    content = f"""---
layout: default
title: Home
---
# Revenue Stream Hijacking Case 2025-137857

**Last Updated:** {datetime.now().strftime('%B %d, %Y')}

## Executive Summary
This documentation repository provides a comprehensively refined, evidence-based analysis of the systematic hijacking of revenue streams in the RegimA business operations case. All data models have been cross-referenced with the `ad-res-j7` evidence repository to ensure factual accuracy and legal integrity.

**Critical Revelation:** The **Shopify platform** has been owned and paid for since **July 2023** by Daniel Faucitt's independent UK entity **RegimA Zone Ltd**. RWD ZA has no independent revenue stream—all revenues were generated through infrastructure owned, paid for, and operated by Daniel's UK company.

---
## Case Overview at a Glance

| Metric | Value |
|---|---|
| **Case Number** | 2025-137857 |
| **Total Documented Losses** | **{format_currency(10269727.90)}** |
| **Total Events** | {summary.get('total_events', 'N/A')} |
| **Entities Profiled** | {summary.get('total_entities', 'N/A')} |
| **Relations Mapped** | {load_json(RELATIONS_FILE)['metadata'].get('version', 'N/A')} |
| **Evidence Files** | 2,866+ files in `ad-res-j7` |

---
## Navigation

### 📋 Core Documentation
- **[Interactive Timeline](timeline.md)** - A complete, chronological timeline of all {summary.get('total_events', 'N/A')} events with evidence links.
- **[Entity Profiles](entities/)** - Detailed profiles of all {summary.get('total_entities', 'N/A')} key persons and organizations.
- **[Event Details](events/)** - Individual pages for each of the {summary.get('total_events', 'N/A')} timeline events.
- **[Evidence Index](evidence-index.md)** - An index of evidence categories and their locations within the `ad-res-j7` repository.

"""
    write_file(f"{DOCS_DIR}/index.md", content)
    print("  Generated index page.")

def generate_evidence_index_page(evidence_mapping):
    """Generates the evidence-index.md page."""
    print("Generating evidence index page...")
    if not evidence_mapping:
        return

    content = "---\nlayout: default\ntitle: Evidence Index\n---\n# Evidence Index\n\n"
    content += "This page provides a high-level overview of the evidence categories and their primary locations within the [ad-res-j7](https://github.com/cogpy/ad-res-j7) repository.\n\n"
    content += "| Category | Description | Primary Location | Key Annexures |\n"
    content += "|---|---|---|---|\n"

    for cat, details in evidence_mapping.get('evidence_categories', {}).items():
        location = f"[{details['location']}]({AD_RES_J7_REPO_URL}{details['location']})"
        annexures = ", ".join(details.get('annexures', []))
        content += f"| {cat.title()} | {details['description']} | {location} | {annexures} |\n"

    write_file(f"{DOCS_DIR}/evidence-index.md", content)
    print("  Generated evidence index page.")

# --- Main Execution ---
def main():
    """Main function to generate all documentation."""
    print("Starting GitHub Pages generation...")

    # Load all necessary data
    entities = load_json(ENTITIES_FILE)
    events = load_json(EVENTS_FILE)
    timeline = load_json(TIMELINE_FILE)
    evidence_map = load_json(MAPPING_FILE)
    analysis_summary = load_json(f"{BASE_DIR}/ANALYSIS_REPORT_2025_12_07.json")

    # Generate all pages
    generate_entity_pages(entities)
    generate_event_pages(events, evidence_map)
    generate_timeline_page(timeline)
    generate_index_page(analysis_summary)
    generate_evidence_index_page(evidence_map)

    print("\nGitHub Pages generation complete.")

if __name__ == "__main__":
    main()

