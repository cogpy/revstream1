#!/usr/bin/env python3
"""
Enhance timeline with additional evidence and actor information
"""

import json
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def enhance_timeline():
    """Enhance timeline with additional evidence references and key actors"""
    timeline_path = Path('/home/ubuntu/revstream1/data_models/timelines/timeline.json')
    events_path = Path('/home/ubuntu/revstream1/data_models/events/events.json')
    
    timeline = load_json(timeline_path)
    events = load_json(events_path)
    
    # Create event lookup
    event_lookup = {event['event_id']: event for event in events.get('events', [])}
    
    # Track updates
    updated_count = 0
    
    # Iterate through timeline entries
    for entry in timeline.get('timeline', []):
        date = entry.get('date')
        event_ids = entry.get('events', [])
        
        # Add missing key actors
        if not entry.get('key_actors') or len(entry.get('key_actors', [])) == 0:
            # Extract actors from events
            actors = set()
            for event_id in event_ids:
                event = event_lookup.get(event_id)
                if event:
                    # Add perpetrators
                    for perp in event.get('perpetrators', []):
                        if isinstance(perp, str):
                            actors.add(perp)
                    # Add entities involved
                    for entity in event.get('entities_involved', []):
                        if isinstance(entity, str):
                            actors.add(entity)
            
            if actors:
                entry['key_actors'] = list(actors)
                updated_count += 1
        
        # Add evidence references if weak
        if len(entry.get('evidence_references', [])) < 2:
            # Collect evidence from events
            evidence_refs = set(entry.get('evidence_references', []))
            for event_id in event_ids:
                event = event_lookup.get(event_id)
                if event:
                    for evidence in event.get('evidence', [])[:2]:  # Take first 2
                        evidence_refs.add(evidence)
            
            entry['evidence_references'] = list(evidence_refs)[:5]  # Limit to 5
            updated_count += 1
    
    # Update metadata
    timeline['metadata']['last_updated'] = datetime.now().isoformat()
    timeline['metadata']['version'] = '20.0_ENHANCED_2026_01_09'
    timeline['metadata']['changes'] = f'Enhanced key actors and evidence references for {updated_count} entries'
    
    # Save enhanced timeline
    save_json(timeline_path, timeline)
    
    print(f"Total timeline entries enhanced: {updated_count}")
    print(f"Saved to: {timeline_path}")

if __name__ == '__main__':
    enhance_timeline()
