#!/usr/bin/env python3.11
"""
Fix missing perpetrators/victims in events based on context and evidence
"""
import json
from datetime import datetime
from pathlib import Path

def fix_events():
    events_path = Path('/home/ubuntu/revstream1/data_models/events/events.json')
    
    with open(events_path, 'r') as f:
        data = json.load(f)
    
    events = data.get('events', [])
    
    # Define fixes for each event
    fixes = {
        'EVENT_091': {
            'entities_involved': ['PERSON_003', 'ORG_001', 'ORG_011'],
            'perpetrators': ['PERSON_003', 'PERSON_002'],
            'victims': ['PERSON_005', 'PERSON_004', 'ORG_001']
        },
        'EVENT_089': {
            'entities_involved': ['PERSON_007', 'TRUST_001', 'ORG_002'],
            'perpetrators': ['PERSON_007'],
            'victims': ['TRUST_001', 'PERSON_005', 'PERSON_004']
        },
        'EVENT_090': {
            'entities_involved': ['PERSON_002', 'ORG_001', 'PLATFORM_001'],
            'perpetrators': ['PERSON_002'],
            'victims': ['PERSON_005', 'PERSON_004', 'ORG_001']
        },
        'EVENT_088': {
            'entities_involved': ['ORG_001', 'ORG_002', 'ORG_004', 'ORG_012'],
            'perpetrators': [],
            'victims': []
        },
        'EVENT_086': {
            'entities_involved': ['PERSON_010', 'PERSON_005'],
            'perpetrators': [],
            'victims': ['PERSON_010']
        },
        'EVENT_087': {
            'entities_involved': ['PERSON_010', 'PERSON_001', 'PERSON_005'],
            'perpetrators': ['PERSON_001'],
            'victims': ['PERSON_010', 'PERSON_005']
        },
        'EVENT_067': {
            'entities_involved': ['ORG_001', 'ORG_008', 'PERSON_001'],
            'perpetrators': ['PERSON_001'],
            'victims': ['ORG_001']
        },
        'EVENT_SF2A': {
            'entities_involved': ['PERSON_002', 'ORG_001', 'PERSON_001'],
            'perpetrators': ['PERSON_002'],
            'victims': ['PERSON_005', 'PERSON_004', 'ORG_001']
        },
        'EVENT_SF2B': {
            'entities_involved': ['PERSON_002', 'ORG_001', 'PERSON_001'],
            'perpetrators': ['PERSON_002', 'PERSON_001'],
            'victims': ['PERSON_005', 'PERSON_004', 'ORG_001']
        },
        'EVENT_SF9': {
            'entities_involved': ['PERSON_001', 'PERSON_009', 'PERSON_005', 'PERSON_004'],
            'perpetrators': ['PERSON_001', 'PERSON_009'],
            'victims': ['PERSON_005', 'PERSON_004']
        }
    }
    
    # Apply fixes
    updated_count = 0
    for event in events:
        event_id = event.get('event_id')
        if event_id in fixes:
            fix = fixes[event_id]
            event['entities_involved'] = fix['entities_involved']
            event['perpetrators'] = fix['perpetrators']
            event['victims'] = fix['victims']
            updated_count += 1
            print(f"Fixed {event_id}")
    
    # Update metadata
    data['metadata']['last_updated'] = datetime.now().isoformat()
    data['metadata']['changes'] = f"Fixed perpetrators/victims for {updated_count} events"
    data['metadata']['version'] = "19.0_PERPETRATORS_FIXED_2026_01_02"
    
    # Save updated data
    with open(events_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nUpdated {updated_count} events")
    print(f"Saved to: {events_path}")

if __name__ == '__main__':
    fix_events()
