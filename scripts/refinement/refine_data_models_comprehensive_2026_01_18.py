#!/usr/bin/env python3
"""
Comprehensive Data Model Refinement Script
Date: 2026-01-18
Purpose: To refine and enhance the entities, relations, events, and timeline models
         in the revstream1 repository, ensuring consistency, accuracy, and depth.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"
RELATIONS_FILE = DATA_MODELS_DIR / "relations" / "relations.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timelines" / "timeline.json"

# Load all data models
def load_json(filepath):
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def save_json(filepath, data):
    """Save JSON file with backup."""
    backup_path = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    if os.path.exists(filepath):
        os.rename(filepath, backup_path)
        print(f"Backup created: {backup_path}")
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    print(f"Saved: {filepath}")

def refine_entities(entities_data, relations_data, timeline_data):
    """Refine the entities model."""
    if not entities_data:
        return None

    print("\nRefining entities...")
    # Example refinement: Cross-reference entity involvement in events
    for person in entities_data.get('entities', {}).get('persons', []):
        person_id = person.get('entity_id')
        event_count = 0
        if timeline_data and 'timeline' in timeline_data:
            for event in timeline_data['timeline']:
                if person_id in event.get('entities_involved', []):
                    event_count += 1
        person['involvement_events'] = event_count
        print(f"Updated event count for {person.get('name')}: {event_count}")

    entities_data['metadata']['version'] = "30.0_COMPREHENSIVE_REFINEMENT_2026_01_18"
    entities_data['metadata']['last_updated'] = datetime.now().isoformat()
    entities_data['metadata']['changes'] = "Comprehensive refinement of entities, relations, and timeline."

    return entities_data

def refine_relations(relations_data, entities_data):
    """Refine the relations model."""
    if not relations_data:
        return None

    print("\nRefining relations...")
    # Example refinement: Ensure all related entities exist
    all_entity_ids = [p.get('entity_id') for p in entities_data.get('entities', {}).get('persons', [])] + \
                     [o.get('entity_id') for o in entities_data.get('entities', {}).get('organizations', [])]

    for category, rel_list in relations_data.get('relations', {}).items():
        for rel in rel_list:
            if rel.get('source_entity') not in all_entity_ids:
                print(f"Warning: Source entity {rel.get('source_entity')} in relation {rel.get('relation_id')} not found in entities.")
            if rel.get('target_entity') not in all_entity_ids:
                print(f"Warning: Target entity {rel.get('target_entity')} in relation {rel.get('relation_id')} not found in entities.")

    relations_data['metadata']['version'] = "30.0_COMPREHENSIVE_REFINEMENT_2026_01_18"
    relations_data['metadata']['last_updated'] = datetime.now().isoformat()
    relations_data['metadata']['changes'] = "Comprehensive refinement of relations."

    return relations_data

def refine_timeline(timeline_data, entities_data):
    """Refine the timeline model."""
    if not timeline_data:
        return None

    print("\nRefining timeline...")
    # Example refinement: Add entity names to events for readability
    entity_map = {p.get('entity_id'): p.get('name') for p in entities_data.get('entities', {}).get('persons', [])} \
               | {o.get('entity_id'): o.get('name') for o in entities_data.get('entities', {}).get('organizations', [])}

    for event in timeline_data.get('timeline', []):
        actor_names = [entity_map.get(actor_id, actor_id) for actor_id in event.get('key_actors', [])]
        event['key_actor_names'] = actor_names

    timeline_data['metadata']['version'] = "27.0_COMPREHENSIVE_REFINEMENT_2026_01_18"
    timeline_data['metadata']['last_updated'] = datetime.now().isoformat()
    timeline_data['metadata']['changes'] = "Comprehensive refinement of timeline, added entity names to events."

    return timeline_data

def main():
    """Main refinement function."""
    print("=" * 60)
    print("Comprehensive Data Model Refinement")
    print(f"Date: {datetime.now().isoformat()}")
    print("=" * 60)

    # Load existing data
    print("\nLoading existing data models...")
    entities_data = load_json(ENTITIES_FILE)
    relations_data = load_json(RELATIONS_FILE)
    timeline_data = load_json(TIMELINE_FILE)

    # Refine models
    if entities_data and relations_data and timeline_data:
        entities_data = refine_entities(entities_data, relations_data, timeline_data)
        relations_data = refine_relations(relations_data, entities_data)
        timeline_data = refine_timeline(timeline_data, entities_data)

        # Save refined models
        save_json(ENTITIES_FILE, entities_data)
        save_json(RELATIONS_FILE, relations_data)
        save_json(TIMELINE_FILE, timeline_data)

        print("\n" + "=" * 60)
        print("Refinement Complete!")
        print("=" * 60)
    else:
        print("\nError: Could not load all data models. Aborting refinement.")

if __name__ == "__main__":
    main()
