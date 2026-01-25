#!/usr/bin/env python3
"""Links relations to events based on shared entities and temporal proximity."""
import json
import os
from datetime import datetime, timedelta

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with backup"""
    if os.path.exists(filepath):
        backup_path = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.rename(filepath, backup_path)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def parse_date(date_str):
    """Parse date string, handling various formats and returning a datetime object."""
    if not date_str or date_str == "YYYY-MM-DD":
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        try:
            return datetime.strptime(date_str, '%Y-%m')
        except ValueError:
            return None

def main():
    print("="*80)
    print("LINKING RELATIONS TO EVENTS")
    print("="*80)

    base_path = "/home/ubuntu/revstream1/data_models"
    relations_path = os.path.join(base_path, 'relations', 'relations.json')
    events_path = os.path.join(base_path, 'events', 'events.json')

    relations_data = load_json(relations_path)
    events_data = load_json(events_path)

    updated_relations_count = 0
    total_relations = 0

    # Create a lookup for events by entity
    events_by_entity = {}
    for event in events_data.get('events', []):
        for entity_id in event.get('entities_involved', []):
            if entity_id not in events_by_entity:
                events_by_entity[entity_id] = []
            events_by_entity[entity_id].append(event)

    # Iterate through each category of relations
    for category, relations_list in relations_data.get('relations', {}).items():
        if isinstance(relations_list, list):
            total_relations += len(relations_list)
            for i, relation in enumerate(relations_list):
                if not relation.get('related_events'):
                    relation['related_events'] = []

                source_entity = relation.get('source_entity')
                target_entity = relation.get('target_entity')
                relation_entities = {source_entity, target_entity}

                # Find events involving both entities
                candidate_events = []
                if source_entity in events_by_entity:
                    for event in events_by_entity[source_entity]:
                        if target_entity in event.get('entities_involved', []):
                            candidate_events.append(event)
                
                if candidate_events:
                    for event in candidate_events:
                        if event['event_id'] not in relation['related_events']:
                            relation['related_events'].append(event['event_id'])
                            print(f"Linked relation {relation.get('relation_id')} to event {event['event_id']} (shared entities)")
                    updated_relations_count += 1
                relations_list[i] = relation

    print(f"\nProcessed {total_relations} relations.")
    print(f"Updated {updated_relations_count} relations with event links.")

    # Save the updated relations data
    save_json(relations_data, relations_path)
    print(f"\nUpdated relations data saved to: {relations_path}")

    print("\n" + "="*80)
    print("RELATION-EVENT LINKING COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
