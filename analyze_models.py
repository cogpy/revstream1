#!/usr/bin/env python3.11
"""
Comprehensive analysis of entities, relations, events, and timelines
for Case 2025-137857 Revenue Stream Hijacking
"""

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities model"""
    print("\n" + "="*80)
    print("ENTITIES ANALYSIS")
    print("="*80)
    
    metadata = entities_data.get('metadata', {})
    entities = entities_data.get('entities', {})
    
    print(f"\nVersion: {metadata.get('version')}")
    print(f"Last Updated: {metadata.get('last_updated')}")
    print(f"Total Entities: {metadata.get('total_entities')}")
    print(f"Changes: {metadata.get('changes')}")
    
    print("\n--- Entity Categories ---")
    for category, entity_list in entities.items():
        print(f"  {category}: {len(entity_list)} entities")
    
    # Analyze persons
    persons = entities.get('persons', [])
    print(f"\n--- Person Entities ({len(persons)}) ---")
    for person in persons:
        entity_id = person.get('entity_id')
        name = person.get('name')
        role = person.get('role')
        events = len(person.get('timeline_events', []))
        print(f"  {entity_id}: {name} ({role}) - {events} events")
    
    # Analyze organizations
    orgs = entities.get('organizations', [])
    print(f"\n--- Organization Entities ({len(orgs)}) ---")
    for org in orgs:
        entity_id = org.get('entity_id')
        name = org.get('name')
        org_type = org.get('type', 'N/A')
        events = len(org.get('timeline_events', []))
        print(f"  {entity_id}: {name} ({org_type}) - {events} events")
    
    # Check for entities with no events
    print("\n--- Entities with No Events ---")
    for category, entity_list in entities.items():
        for entity in entity_list:
            events = entity.get('timeline_events', [])
            if not events:
                entity_id = entity.get('entity_id', 'N/A')
                name = entity.get('name', 'N/A')
                print(f"  {entity_id}: {name} ({category})")
    
    return entities_data

def analyze_events(events_data):
    """Analyze events model"""
    print("\n" + "="*80)
    print("EVENTS ANALYSIS")
    print("="*80)
    
    metadata = events_data.get('metadata', {})
    events = events_data.get('events', [])
    
    print(f"\nVersion: {metadata.get('version')}")
    print(f"Last Updated: {metadata.get('last_updated')}")
    print(f"Total Events: {metadata.get('total_events')}")
    print(f"Changes: {metadata.get('changes')}")
    print(f"Extended Evidence Files: {metadata.get('extended_evidence_files')}")
    
    # Categorize events
    events_by_category = defaultdict(list)
    events_by_year = defaultdict(list)
    events_with_financial_impact = []
    events_without_entities = []
    
    for event in events:
        category = event.get('category', 'uncategorized')
        events_by_category[category].append(event)
        
        date = event.get('date', '')
        if date:
            year = date.split('-')[0]
            events_by_year[year].append(event)
        
        if event.get('financial_impact'):
            events_with_financial_impact.append(event)
        
        entities = event.get('entities_involved', [])
        if not entities:
            events_without_entities.append(event)
    
    print(f"\n--- Events by Category ---")
    for category, event_list in sorted(events_by_category.items()):
        print(f"  {category}: {len(event_list)} events")
    
    print(f"\n--- Events by Year ---")
    for year, event_list in sorted(events_by_year.items()):
        print(f"  {year}: {len(event_list)} events")
    
    print(f"\n--- Financial Impact ---")
    print(f"  Events with financial impact: {len(events_with_financial_impact)}")
    
    if events_without_entities:
        print(f"\n--- Events Without Entity Links ({len(events_without_entities)}) ---")
        for event in events_without_entities[:10]:  # Show first 10
            event_id = event.get('event_id')
            title = event.get('title')
            date = event.get('date')
            print(f"  {event_id} ({date}): {title}")
    
    # Timeline phases
    phases = defaultdict(list)
    for event in events:
        phase = event.get('timeline_phase', 'UNASSIGNED')
        phases[phase].append(event)
    
    print(f"\n--- Timeline Phases ---")
    for phase, event_list in sorted(phases.items()):
        print(f"  {phase}: {len(event_list)} events")
    
    return events_data

def analyze_relations(relations_data):
    """Analyze relations model"""
    print("\n" + "="*80)
    print("RELATIONS ANALYSIS")
    print("="*80)
    
    metadata = relations_data.get('metadata', {})
    relations = relations_data.get('relations', {})
    
    print(f"\nVersion: {metadata.get('version')}")
    print(f"Last Updated: {metadata.get('last_updated')}")
    print(f"Changes: {metadata.get('changes')}")
    
    print("\n--- Relation Categories ---")
    total_relations = 0
    for category, relation_list in relations.items():
        count = len(relation_list)
        total_relations += count
        print(f"  {category}: {count} relations")
    
    print(f"\nTotal Relations: {total_relations}")
    
    # Analyze ownership relations
    ownership = relations.get('ownership_relations', [])
    print(f"\n--- Ownership Relations ({len(ownership)}) ---")
    for rel in ownership[:10]:  # Show first 10
        rel_id = rel.get('relation_id')
        source = rel.get('source_entity')
        target = rel.get('target_entity')
        rel_type = rel.get('relation_type')
        status = rel.get('legal_status', 'N/A')
        print(f"  {rel_id}: {source} --[{rel_type}]--> {target} ({status})")
    
    # Analyze conspiracy relations
    conspiracy = relations.get('conspiracy_relations', [])
    print(f"\n--- Conspiracy Relations ({len(conspiracy)}) ---")
    for rel in conspiracy:
        rel_id = rel.get('relation_id')
        source = rel.get('source_entity')
        target = rel.get('target_entity')
        rel_type = rel.get('relation_type')
        print(f"  {rel_id}: {source} --[{rel_type}]--> {target}")
    
    return relations_data

def analyze_timeline(timeline_data):
    """Analyze timeline model"""
    print("\n" + "="*80)
    print("TIMELINE ANALYSIS")
    print("="*80)
    
    metadata = timeline_data.get('metadata', {})
    timeline = timeline_data.get('timeline', [])
    
    print(f"\nVersion: {metadata.get('version', 'N/A')}")
    print(f"Last Updated: {metadata.get('last_updated', 'N/A')}")
    print(f"Total Timeline Entries: {len(timeline)}")
    
    # Analyze phases
    phases = defaultdict(list)
    for entry in timeline:
        phase = entry.get('phase', 'UNASSIGNED')
        phases[phase].append(entry)
    
    print(f"\n--- Timeline Phases ---")
    for phase, entries in sorted(phases.items()):
        print(f"  {phase}: {len(entries)} entries")
    
    return timeline_data

def generate_recommendations(entities_data, events_data, relations_data, timeline_data):
    """Generate recommendations for improvements"""
    print("\n" + "="*80)
    print("RECOMMENDATIONS FOR IMPROVEMENT")
    print("="*80)
    
    recommendations = []
    
    # Check entities without events
    entities = entities_data.get('entities', {})
    for category, entity_list in entities.items():
        for entity in entity_list:
            events = entity.get('timeline_events', [])
            if not events:
                entity_id = entity.get('entity_id', 'N/A')
                name = entity.get('name', 'N/A')
                recommendations.append({
                    'priority': 'HIGH',
                    'category': 'entities',
                    'issue': f'Entity {entity_id} ({name}) has no linked events',
                    'action': 'Review events and link relevant ones to this entity'
                })
    
    # Check events without entities
    events = events_data.get('events', [])
    for event in events:
        entities_involved = event.get('entities_involved', [])
        if not entities_involved:
            event_id = event.get('event_id')
            title = event.get('title')
            recommendations.append({
                'priority': 'HIGH',
                'category': 'events',
                'issue': f'Event {event_id} ({title}) has no linked entities',
                'action': 'Review and link relevant entities to this event'
            })
    
    # Check for missing evidence files
    for event in events:
        evidence_files = event.get('evidence_files', [])
        if not evidence_files:
            event_id = event.get('event_id')
            recommendations.append({
                'priority': 'MEDIUM',
                'category': 'evidence',
                'issue': f'Event {event_id} has no evidence files',
                'action': 'Link evidence files from ad-res-j7 repository'
            })
    
    # Print recommendations
    print("\n--- HIGH PRIORITY ---")
    for rec in [r for r in recommendations if r['priority'] == 'HIGH']:
        print(f"  [{rec['category']}] {rec['issue']}")
        print(f"    Action: {rec['action']}")
    
    print(f"\n--- MEDIUM PRIORITY ---")
    for rec in [r for r in recommendations if r['priority'] == 'MEDIUM'][:10]:
        print(f"  [{rec['category']}] {rec['issue']}")
        print(f"    Action: {rec['action']}")
    
    print(f"\nTotal Recommendations: {len(recommendations)}")
    
    return recommendations

def main():
    """Main analysis function"""
    base_path = Path('/home/ubuntu/revstream1/data_models')
    
    # Load latest models
    entities_path = base_path / 'entities' / 'entities_refined_2025_12_04_v24.json'
    events_path = base_path / 'events' / 'events_refined_2025_12_04_v26.json'
    relations_path = base_path / 'relations' / 'relations_refined_2025_11_28_v20.json'
    
    # Check for timeline
    timeline_files = list((base_path / 'timelines').glob('*.json'))
    timeline_path = sorted(timeline_files)[-1] if timeline_files else None
    
    print("="*80)
    print("COMPREHENSIVE MODEL ANALYSIS")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("="*80)
    print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Load and analyze
    entities_data = load_json(entities_path)
    events_data = load_json(events_path)
    relations_data = load_json(relations_path)
    timeline_data = load_json(timeline_path) if timeline_path else {'timeline': []}
    
    # Run analyses
    analyze_entities(entities_data)
    analyze_events(events_data)
    analyze_relations(relations_data)
    if timeline_path:
        analyze_timeline(timeline_data)
    
    # Generate recommendations
    recommendations = generate_recommendations(entities_data, events_data, relations_data, timeline_data)
    
    # Save recommendations
    output_path = Path('/home/ubuntu/revstream1/MODEL_ANALYSIS_REPORT_2025_12_05.json')
    with open(output_path, 'w') as f:
        json.dump({
            'analysis_date': datetime.now().isoformat(),
            'entities_version': entities_data['metadata']['version'],
            'events_version': events_data['metadata']['version'],
            'relations_version': relations_data['metadata']['version'],
            'recommendations': recommendations
        }, f, indent=2)
    
    print(f"\n\nAnalysis report saved to: {output_path}")

if __name__ == '__main__':
    main()
