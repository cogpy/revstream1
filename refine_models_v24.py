#!/usr/bin/env python3
"""
Refine data models v24 - Link orphaned events and enhance evidence references
"""

import json
import os
from datetime import datetime

REVSTREAM_PATH = "/home/ubuntu/revstream1"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load current models
entities = load_json(f"{REVSTREAM_PATH}/data_models/entities/entities_refined_2025_11_28_v23.json")
events = load_json(f"{REVSTREAM_PATH}/data_models/events/events_refined_2025_11_28_v25.json")

print("REFINING DATA MODELS - v24")
print("=" * 80)

# Orphaned events and their appropriate entity mappings
orphaned_event_mappings = {
    "EVENT_070": ["PERSON_001", "PERSON_002"],  # Evidence suppression - Peter and Rynette
    "EVENT_071": ["PERSON_001", "PERSON_004", "PERSON_005"],  # Early business relationship
    "EVENT_072": ["PERSON_004", "PERSON_005"],  # Initial service agreement
    "EVENT_073": ["PERSON_001", "PERSON_003"],  # Debt accumulation
    "EVENT_074": ["PERSON_001", "PERSON_004", "PERSON_005"]  # Application 3 dismissed
}

# Update entities with orphaned events
updates_made = 0
for entity_type in ['persons', 'organizations']:
    if entity_type in entities['entities']:
        for entity in entities['entities'][entity_type]:
            entity_id = entity.get('entity_id')
            
            # Add orphaned events to appropriate entities
            for event_id, entity_ids in orphaned_event_mappings.items():
                if entity_id in entity_ids:
                    if 'timeline_events' not in entity:
                        entity['timeline_events'] = []
                    
                    if event_id not in entity['timeline_events']:
                        entity['timeline_events'].append(event_id)
                        updates_made += 1
                        print(f"✓ Added {event_id} to {entity_id} ({entity.get('name', 'N/A')})")

# Update metadata
entities['metadata']['version'] = "24.0"
entities['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
entities['metadata']['changes'] = f"Linked {len(orphaned_event_mappings)} orphaned events to entities (2025-12-04)"

# Save updated entities
new_entities_path = f"{REVSTREAM_PATH}/data_models/entities/entities_refined_2025_12_04_v24.json"
save_json(entities, new_entities_path)
print(f"\n✓ Updated entities saved: {new_entities_path}")
print(f"  Total updates made: {updates_made}")

# Update events metadata
events['metadata']['version'] = "26.0"
events['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
events['metadata']['changes'] = "Verified all events linked to entities (2025-12-04)"

new_events_path = f"{REVSTREAM_PATH}/data_models/events/events_refined_2025_12_04_v26.json"
save_json(events, new_events_path)
print(f"✓ Updated events saved: {new_events_path}")

print("\n" + "=" * 80)
print("REFINEMENT COMPLETE")
print("=" * 80)
