import json
import os
from collections import defaultdict
from datetime import datetime

def load_json(filepath):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_entities(entities_data):
    """Analyze entities structure"""
    analysis = {
        'total_entities': 0,
        'by_type': defaultdict(int),
        'by_agent_type': defaultdict(int),
        'by_role': defaultdict(list),
        'financial_impact_total': 0,
        'entities_missing_data': []
    }
    
    if not entities_data or 'entities' not in entities_data:
        return analysis
    
    for entity_type, entity_list in entities_data['entities'].items():
        analysis['by_type'][entity_type] = len(entity_list)
        analysis['total_entities'] += len(entity_list)
        
        for entity in entity_list:
            # Agent type analysis
            if 'agent_type' in entity:
                analysis['by_agent_type'][entity['agent_type']] += 1
            
            # Role analysis
            if 'role' in entity:
                analysis['by_role'][entity['role']].append(entity.get('entity_id', 'unknown'))
            
            # Check for missing critical data
            missing_fields = []
            if 'entity_id' not in entity:
                missing_fields.append('entity_id')
            if 'name' not in entity and 'organization_name' not in entity:
                missing_fields.append('name')
            if 'role' not in entity:
                missing_fields.append('role')
            
            if missing_fields:
                analysis['entities_missing_data'].append({
                    'entity': entity.get('entity_id', entity.get('name', 'unknown')),
                    'missing': missing_fields
                })
    
    return analysis

def analyze_events(events_data):
    """Analyze events structure"""
    analysis = {
        'total_events': 0,
        'by_category': defaultdict(int),
        'by_pattern': defaultdict(int),
        'timeline_coverage': {},
        'events_missing_data': [],
        'perpetrator_frequency': defaultdict(int),
        'victim_frequency': defaultdict(int),
        'financial_impact_events': []
    }
    
    if not events_data or 'events' not in events_data:
        return analysis
    
    dates = []
    for event in events_data['events']:
        analysis['total_events'] += 1
        
        # Category analysis
        if 'category' in event:
            analysis['by_category'][event['category']] += 1
        
        # Pattern analysis
        if 'pattern' in event:
            analysis['by_pattern'][event['pattern']] += 1
        
        # Date tracking
        if 'date' in event:
            dates.append(event['date'])
        
        # Perpetrator tracking
        if 'perpetrators' in event:
            for perp in event['perpetrators']:
                analysis['perpetrator_frequency'][perp] += 1
        
        # Victim tracking
        if 'victims' in event:
            for victim in event['victims']:
                analysis['victim_frequency'][victim] += 1
        
        # Financial impact
        if 'financial_impact' in event and event['financial_impact'] != 'unknown_amount':
            analysis['financial_impact_events'].append({
                'event_id': event.get('event_id'),
                'date': event.get('date'),
                'amount': event['financial_impact']
            })
        
        # Check for missing critical data
        missing_fields = []
        if 'event_id' not in event:
            missing_fields.append('event_id')
        if 'date' not in event:
            missing_fields.append('date')
        if 'category' not in event:
            missing_fields.append('category')
        if 'perpetrators' not in event or len(event.get('perpetrators', [])) == 0:
            missing_fields.append('perpetrators')
        
        if missing_fields:
            analysis['events_missing_data'].append({
                'event': event.get('event_id', 'unknown'),
                'missing': missing_fields
            })
    
    if dates:
        analysis['timeline_coverage'] = {
            'start_date': min(dates),
            'end_date': max(dates),
            'total_events': len(dates)
        }
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations structure"""
    analysis = {
        'total_relations': 0,
        'by_type': defaultdict(int),
        'entity_connections': defaultdict(int),
        'relations_missing_data': []
    }
    
    if not relations_data or 'relations' not in relations_data:
        return analysis
    
    for relation_type, relation_list in relations_data['relations'].items():
        analysis['by_type'][relation_type] = len(relation_list)
        analysis['total_relations'] += len(relation_list)
        
        for relation in relation_list:
            # Track entity connections
            if 'source_entity' in relation:
                analysis['entity_connections'][relation['source_entity']] += 1
            if 'target_entity' in relation:
                analysis['entity_connections'][relation['target_entity']] += 1
            
            # Check for missing critical data
            missing_fields = []
            if 'relation_id' not in relation:
                missing_fields.append('relation_id')
            if 'source_entity' not in relation:
                missing_fields.append('source_entity')
            if 'target_entity' not in relation:
                missing_fields.append('target_entity')
            
            if missing_fields:
                analysis['relations_missing_data'].append({
                    'relation': relation.get('relation_id', 'unknown'),
                    'missing': missing_fields
                })
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline structure"""
    analysis = {
        'total_phases': 0,
        'phases': {},
        'temporal_patterns': {},
        'timeline_missing_data': []
    }
    
    if not timeline_data or 'timeline_phases' not in timeline_data:
        return analysis
    
    for phase_key, phase_data in timeline_data['timeline_phases'].items():
        analysis['total_phases'] += 1
        analysis['phases'][phase_key] = {
            'name': phase_data.get('phase_name'),
            'start_date': phase_data.get('start_date'),
            'end_date': phase_data.get('end_date'),
            'duration_days': phase_data.get('duration_days'),
            'event_count': len(phase_data.get('events', [])),
            'financial_impact': phase_data.get('financial_impact')
        }
    
    if 'temporal_patterns' in timeline_data:
        analysis['temporal_patterns'] = {
            'escalation_triggers': len(timeline_data['temporal_patterns'].get('escalation_triggers', [])),
            'evidence_destruction': len(timeline_data['temporal_patterns'].get('evidence_destruction_sequence', []))
        }
    
    return analysis

def main():
    # Load all data models
    entities = load_json('data_models/entities/entities.json')
    events = load_json('data_models/events/events.json')
    relations = load_json('data_models/relations/relations.json')
    timeline = load_json('data_models/timelines/timeline_enhanced.json')
    
    # Analyze each component
    entities_analysis = analyze_entities(entities)
    events_analysis = analyze_events(events)
    relations_analysis = analyze_relations(relations)
    timeline_analysis = analyze_timeline(timeline)
    
    # Compile comprehensive report
    report = {
        'analysis_date': datetime.now().isoformat(),
        'entities': entities_analysis,
        'events': events_analysis,
        'relations': relations_analysis,
        'timeline': timeline_analysis,
        'cross_references': {
            'entities_in_events': len(set(
                [p for e in events.get('events', []) for p in e.get('perpetrators', [])] +
                [v for e in events.get('events', []) for v in e.get('victims', [])]
            )),
            'entities_in_relations': len(set(
                [r.get('source_entity') for rt in relations.get('relations', {}).values() for r in rt] +
                [r.get('target_entity') for rt in relations.get('relations', {}).values() for r in rt]
            ))
        }
    }
    
    # Save report
    with open('COMPREHENSIVE_ANALYSIS_REPORT.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("Comprehensive analysis complete!")
    print(f"Total Entities: {entities_analysis['total_entities']}")
    print(f"Total Events: {events_analysis['total_events']}")
    print(f"Total Relations: {relations_analysis['total_relations']}")
    print(f"Total Timeline Phases: {timeline_analysis['total_phases']}")

if __name__ == '__main__':
    main()
