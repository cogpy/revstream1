import json
import os
from datetime import datetime
from collections import defaultdict

# Load existing data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Save JSON with pretty formatting
def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load all data models
entities = load_json('/home/ubuntu/revstream1/data_models/entities/entities_refined.json')
events = load_json('/home/ubuntu/revstream1/data_models/events/events_refined.json')
relations = load_json('/home/ubuntu/revstream1/data_models/relations/relations.json')
timeline = load_json('/home/ubuntu/revstream1/data_models/timelines/timeline_enhanced.json')

# Analysis results
analysis = {
    'entities_summary': {},
    'events_summary': {},
    'relations_summary': {},
    'timeline_summary': {},
    'gaps_identified': [],
    'improvements_needed': []
}

# Analyze entities
print("Analyzing entities...")
analysis['entities_summary'] = {
    'total_persons': len(entities['entities']['persons']),
    'total_organizations': len(entities['entities']['organizations']),
    'version': entities['metadata']['version'],
    'last_updated': entities['metadata']['last_updated']
}

# Count entity types by agent_type
agent_types = defaultdict(int)
for person in entities['entities']['persons']:
    agent_types[person.get('agent_type', 'unknown')] += 1
for org in entities['entities']['organizations']:
    agent_types[org.get('agent_type', 'unknown')] += 1

analysis['entities_summary']['agent_type_distribution'] = dict(agent_types)

# Analyze events
print("Analyzing events...")
event_categories = defaultdict(int)
event_patterns = defaultdict(int)
total_financial_impact = 0

for event in events['events']:
    event_categories[event.get('category', 'unknown')] += 1
    event_patterns[event.get('pattern', 'unknown')] += 1
    
    # Try to extract financial impact
    impact = event.get('financial_impact', '0')
    if isinstance(impact, str) and 'R' in impact:
        # Extract numeric value
        import re
        match = re.search(r'R([\d,]+)', impact)
        if match:
            try:
                amount = float(match.group(1).replace(',', ''))
                total_financial_impact += amount
            except:
                pass

analysis['events_summary'] = {
    'total_events': events['metadata']['total_events'],
    'version': events['metadata']['version'],
    'last_updated': events['metadata']['last_updated'],
    'event_categories': dict(event_categories),
    'event_patterns': dict(event_patterns),
    'estimated_financial_impact': f"R{total_financial_impact:,.2f}"
}

# Analyze relations
print("Analyzing relations...")
relation_types = {}
for rel_category in relations['relations']:
    relation_types[rel_category] = len(relations['relations'][rel_category])

analysis['relations_summary'] = {
    'version': relations['metadata']['version'],
    'last_updated': relations['metadata']['last_updated'],
    'relation_categories': relation_types,
    'total_relations': sum(relation_types.values())
}

# Analyze timeline
print("Analyzing timeline...")
phases = timeline['timeline_phases']
phase_summary = {}
for phase_key, phase_data in phases.items():
    phase_summary[phase_data['phase_name']] = {
        'duration_days': phase_data.get('duration_days', 0),
        'event_count': len(phase_data.get('events', [])),
        'financial_impact': phase_data.get('financial_impact', 'unknown')
    }

analysis['timeline_summary'] = {
    'version': timeline['metadata']['version'],
    'last_updated': timeline['metadata']['last_updated'],
    'total_phases': len(phases),
    'phase_details': phase_summary
}

# Identify gaps and improvements
print("Identifying gaps and improvements...")

# Check for events without corresponding entities
event_entities = set()
for event in events['events']:
    event_entities.update(event.get('perpetrators', []))
    event_entities.update(event.get('victims', []))
    event_entities.update(event.get('entities_involved', []))

entity_ids = set()
for person in entities['entities']['persons']:
    entity_ids.add(person['entity_id'])
for org in entities['entities']['organizations']:
    entity_ids.add(org['entity_id'])

missing_entities = event_entities - entity_ids
if missing_entities:
    analysis['gaps_identified'].append({
        'type': 'missing_entities',
        'description': f'Events reference entities that do not exist: {missing_entities}'
    })

# Check for duplicate event IDs in timeline phases
event_ids_in_timeline = []
for phase_key, phase_data in phases.items():
    event_ids_in_timeline.extend(phase_data.get('events', []))

from collections import Counter
duplicate_events = [k for k, v in Counter(event_ids_in_timeline).items() if v > 1]
if duplicate_events:
    analysis['gaps_identified'].append({
        'type': 'duplicate_timeline_events',
        'description': f'Events appear multiple times in timeline: {duplicate_events}'
    })

# Check for events not in timeline
timeline_event_ids = set(event_ids_in_timeline)
actual_event_ids = set([e['event_id'] for e in events['events']])
events_not_in_timeline = actual_event_ids - timeline_event_ids
if events_not_in_timeline:
    analysis['gaps_identified'].append({
        'type': 'events_not_in_timeline',
        'description': f'Events exist but are not placed in timeline: {events_not_in_timeline}'
    })

# Suggest improvements
analysis['improvements_needed'].extend([
    {
        'priority': 'high',
        'area': 'timeline_consistency',
        'description': 'Remove duplicate events from timeline phases',
        'action': 'Clean up duplicate EVENT_047, EVENT_048, EVENT_049, EVENT_050, EVENT_051, EVENT_052, EVENT_053 entries'
    },
    {
        'priority': 'high',
        'area': 'entity_relations',
        'description': 'Add missing entity relationships discovered in ad-res-j7',
        'action': 'Cross-reference evidence documents for additional connections'
    },
    {
        'priority': 'medium',
        'area': 'financial_tracking',
        'description': 'Standardize financial impact format across all events',
        'action': 'Convert all financial_impact fields to consistent numeric format'
    },
    {
        'priority': 'medium',
        'area': 'evidence_linking',
        'description': 'Link events to specific evidence files in ad-res-j7',
        'action': 'Add evidence_file_references to each event'
    },
    {
        'priority': 'low',
        'area': 'metadata_sync',
        'description': 'Ensure all data model versions are synchronized',
        'action': 'Update all metadata to version 5.0 with current date'
    }
])

# Save analysis report
save_json('/home/ubuntu/revstream1/ANALYSIS_REPORT.json', analysis)

print("\n=== ANALYSIS COMPLETE ===")
print(f"Total Persons: {analysis['entities_summary']['total_persons']}")
print(f"Total Organizations: {analysis['entities_summary']['total_organizations']}")
print(f"Total Events: {analysis['events_summary']['total_events']}")
print(f"Total Relations: {analysis['relations_summary']['total_relations']}")
print(f"Total Timeline Phases: {analysis['timeline_summary']['total_phases']}")
print(f"\nGaps Identified: {len(analysis['gaps_identified'])}")
print(f"Improvements Needed: {len(analysis['improvements_needed'])}")
print("\nFull report saved to: ANALYSIS_REPORT.json")
