import json
import os
from collections import defaultdict

def analyze_entities(entities_file):
    """Analyze entities.json and extract insights"""
    with open(entities_file, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_persons': len(data['entities']['persons']),
        'total_organizations': len(data['entities']['organizations']),
        'total_platforms': len(data['entities']['platforms']),
        'total_domains': len(data['entities']['domains']),
        'total_trusts': len(data['entities']['trust_entities']),
        'agent_types': defaultdict(int),
        'issues': []
    }
    
    # Check for duplicates
    seen_ids = set()
    seen_names = set()
    
    for category in ['persons', 'organizations', 'platforms', 'domains', 'trust_entities']:
        if category in data['entities']:
            for entity in data['entities'][category]:
                entity_id = entity.get('entity_id')
                name = entity.get('name')
                agent_type = entity.get('agent_type')
                
                if entity_id in seen_ids:
                    analysis['issues'].append(f"Duplicate entity_id: {entity_id}")
                seen_ids.add(entity_id)
                
                if agent_type:
                    analysis['agent_types'][agent_type] += 1
    
    # Check for duplicate ORG_007 entries
    org_entities = data['entities']['organizations']
    org_007_count = sum(1 for org in org_entities if org.get('entity_id') == 'ORG_007')
    if org_007_count > 1:
        analysis['issues'].append(f"ORG_007 appears {org_007_count} times (duplicate entries)")
    
    # Check for ReZonance vs Adderory confusion
    rezonance_entries = [org for org in org_entities if 'ReZonance' in org.get('name', '') or org.get('entity_id') == 'ORG_007']
    adderory_entries = [org for org in org_entities if 'Adderory' in org.get('name', '')]
    
    analysis['rezonance_entries'] = len(rezonance_entries)
    analysis['adderory_entries'] = len(adderory_entries)
    
    # Check for missing PERSON_003 details
    person_003 = next((p for p in data['entities']['persons'] if p.get('entity_id') == 'PERSON_003'), None)
    if not person_003:
        analysis['issues'].append("PERSON_003 (Adderory/Rynette's son) is missing from persons list")
    
    return analysis

def analyze_relations(relations_file):
    """Analyze relations.json and extract insights"""
    with open(relations_file, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'relation_types': {},
        'total_relations': 0,
        'issues': []
    }
    
    for rel_type, relations in data['relations'].items():
        analysis['relation_types'][rel_type] = len(relations)
        analysis['total_relations'] += len(relations)
    
    return analysis

def analyze_events(events_file):
    """Analyze events.json and extract insights"""
    with open(events_file, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_events': len(data['events']),
        'categories': defaultdict(int),
        'event_types': defaultdict(int),
        'events_by_year': defaultdict(int),
        'financial_impact_total': 0,
        'issues': []
    }
    
    for event in data['events']:
        category = event.get('category')
        event_type = event.get('event_type')
        date = event.get('date', '')
        
        if category:
            analysis['categories'][category] += 1
        if event_type:
            analysis['event_types'][event_type] += 1
        if date:
            year = date.split('-')[0]
            analysis['events_by_year'][year] += 1
    
    return analysis

def analyze_timeline(timeline_file):
    """Analyze timeline_enhanced.json and extract insights"""
    with open(timeline_file, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_phases': len(data['timeline_phases']),
        'phases': {},
        'issues': []
    }
    
    for phase_key, phase_data in data['timeline_phases'].items():
        phase_id = phase_data.get('phase_id')
        phase_name = phase_data.get('phase_name')
        event_count = len(phase_data.get('events', []))
        
        analysis['phases'][phase_name] = {
            'phase_id': phase_id,
            'event_count': event_count,
            'duration_days': phase_data.get('duration_days'),
            'financial_impact': phase_data.get('financial_impact')
        }
    
    return analysis

def main():
    base_path = '/home/ubuntu/revstream1/data_models'
    
    print("=" * 80)
    print("REVSTREAM1 DATA MODEL ANALYSIS")
    print("=" * 80)
    
    # Analyze entities
    print("\n### ENTITIES ANALYSIS ###")
    entities_analysis = analyze_entities(os.path.join(base_path, 'entities/entities.json'))
    print(f"Total Persons: {entities_analysis['total_persons']}")
    print(f"Total Organizations: {entities_analysis['total_organizations']}")
    print(f"Total Platforms: {entities_analysis['total_platforms']}")
    print(f"Total Domains: {entities_analysis['total_domains']}")
    print(f"Total Trusts: {entities_analysis['total_trusts']}")
    print(f"\nAgent Types Distribution:")
    for agent_type, count in entities_analysis['agent_types'].items():
        print(f"  - {agent_type}: {count}")
    print(f"\nReZonance entries found: {entities_analysis['rezonance_entries']}")
    print(f"Adderory entries found: {entities_analysis['adderory_entries']}")
    if entities_analysis['issues']:
        print("\n⚠️  ISSUES FOUND:")
        for issue in entities_analysis['issues']:
            print(f"  - {issue}")
    
    # Analyze relations
    print("\n### RELATIONS ANALYSIS ###")
    relations_analysis = analyze_relations(os.path.join(base_path, 'relations/relations.json'))
    print(f"Total Relations: {relations_analysis['total_relations']}")
    print(f"\nRelation Types:")
    for rel_type, count in relations_analysis['relation_types'].items():
        print(f"  - {rel_type}: {count}")
    
    # Analyze events
    print("\n### EVENTS ANALYSIS ###")
    events_analysis = analyze_events(os.path.join(base_path, 'events/events.json'))
    print(f"Total Events: {events_analysis['total_events']}")
    print(f"\nEvents by Year:")
    for year, count in sorted(events_analysis['events_by_year'].items()):
        print(f"  - {year}: {count}")
    print(f"\nEvent Categories:")
    for category, count in sorted(events_analysis['categories'].items()):
        print(f"  - {category}: {count}")
    
    # Analyze timeline
    print("\n### TIMELINE ANALYSIS ###")
    timeline_analysis = analyze_timeline(os.path.join(base_path, 'timelines/timeline_enhanced.json'))
    print(f"Total Phases: {timeline_analysis['total_phases']}")
    print(f"\nPhases:")
    for phase_name, phase_info in timeline_analysis['phases'].items():
        print(f"  - {phase_name}:")
        print(f"    Events: {phase_info['event_count']}, Duration: {phase_info['duration_days']} days")
        print(f"    Financial Impact: {phase_info['financial_impact']}")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
