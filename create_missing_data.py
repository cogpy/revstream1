#!/usr/bin/env python3
"""
Create placeholder files for missing entities and events to resolve undefined references.
"""
import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def create_placeholder_entity(entity_id, base_path):
    """Create a placeholder JSON file for a missing entity."""
    entity_path = os.path.join(base_path, 'entities', f"{entity_id}.json")
    if not os.path.exists(entity_path):
        placeholder = {
            "entity_id": entity_id,
            "name": f"Placeholder for {entity_id}",
            "type": "Unknown",
            "description": "This is a placeholder entity created to resolve an undefined reference. Please update with accurate information.",
            "evidence": [],
            "ad_res_j7_references": [],
            "created_at": datetime.now().isoformat()
        }
        with open(entity_path, 'w') as f:
            json.dump(placeholder, f, indent=2)
        print(f"Created placeholder entity: {entity_path}")

def create_placeholder_event(event_id, base_path):
    """Create a placeholder JSON file for a missing event."""
    event_path = os.path.join(base_path, 'events', f"{event_id}.json")
    if not os.path.exists(event_path):
        placeholder = {
            "event_id": event_id,
            "date": "YYYY-MM-DD",
            "description": "This is a placeholder event created to resolve an undefined reference. Please update with accurate information.",
            "entities_involved": [],
            "evidence": [],
            "ad_res_j7_evidence": [],
            "created_at": datetime.now().isoformat()
        }
        with open(event_path, 'w') as f:
            json.dump(placeholder, f, indent=2)
        print(f"Created placeholder event: {event_path}")

def main():
    print("="*80)
    print("CREATING PLACEHOLDER FILES FOR MISSING DATA")
    print("="*80)

    base_path = "/home/ubuntu/revstream1/data_models"
    analysis_report_path = os.path.join(base_path, 'ANALYSIS_REPORT_2026_01_25.json')

    if not os.path.exists(analysis_report_path):
        print(f"Error: Analysis report not found at {analysis_report_path}")
        return

    analysis_report = load_json(analysis_report_path)

    # Create directories if they don't exist
    os.makedirs(os.path.join(base_path, 'entities'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'events'), exist_ok=True)

    # Create placeholder entities
    undefined_entities = analysis_report.get('cross_reference', {}).get('undefined_entities_in_events', [])
    print(f"\nFound {len(undefined_entities)} undefined entities. Creating placeholders...")
    for entity_id in undefined_entities:
        create_placeholder_entity(entity_id, base_path)

    # Create placeholder events
    undefined_events = analysis_report.get('cross_reference', {}).get('undefined_events_in_timeline', [])
    print(f"\nFound {len(undefined_events)} undefined events. Creating placeholders...")
    for event_id in undefined_events:
        create_placeholder_event(event_id, base_path)

    print("\n" + "="*80)
    print("PLACEHOLDER CREATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
