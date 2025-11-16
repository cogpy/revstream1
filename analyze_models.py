import json
import os

def load_json(filepath):
    """Load JSON file and return data"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities structure"""
    metadata = entities_data.get('metadata', {})
    entities = entities_data.get('entities', {})
    
    analysis = {
        'metadata': metadata,
        'total_persons': len(entities.get('persons', [])),
        'total_organizations': len(entities.get('organizations', [])),
        'total_trusts': len(entities.get('trusts', [])),
        'total_platforms': len(entities.get('platforms', [])),
        'total_domains': len(entities.get('domains', [])),
        'persons': entities.get('persons', []),
        'organizations': entities.get('organizations', []),
        'trusts': entities.get('trusts', []),
        'platforms': entities.get('platforms', []),
        'domains': entities.get('domains', [])
    }
    return analysis

def analyze_events(events_data):
    """Analyze events structure"""
    metadata = events_data.get('metadata', {})
    events = events_data.get('events', [])
    
    # Group events by category
    by_category = {}
    by_date = {}
    events_missing_perpetrators = []
    
    for event in events:
        category = event.get('category', 'unknown')
        date = event.get('date', 'unknown')
        
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(event)
        
        if date not in by_date:
            by_date[date] = []
        by_date[date].append(event)
        
        # Check for missing perpetrators
        if not event.get('perpetrators') or len(event.get('perpetrators', [])) == 0:
            events_missing_perpetrators.append(event.get('event_id'))
    
    analysis = {
        'metadata': metadata,
        'total_events': len(events),
        'events_by_category': {k: len(v) for k, v in by_category.items()},
        'events_by_date_count': len(by_date),
        'events_missing_perpetrators': events_missing_perpetrators,
        'all_events': events
    }
    return analysis

def analyze_relations(relations_data):
    """Analyze relations structure"""
    metadata = relations_data.get('metadata', {})
    relations = relations_data.get('relations', {})
    
    analysis = {
        'metadata': metadata,
        'relation_categories': list(relations.keys()),
        'category_counts': {k: len(v) for k, v in relations.items()},
        'total_relations': sum(len(v) for v in relations.values()),
        'all_relations': relations
    }
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline structure"""
    metadata = timeline_data.get('metadata', {})
    phases = timeline_data.get('timeline_phases', {})
    
    phase_summary = {}
    for phase_key, phase_data in phases.items():
        phase_summary[phase_key] = {
            'phase_name': phase_data.get('phase_name'),
            'start_date': phase_data.get('start_date'),
            'end_date': phase_data.get('end_date'),
            'duration_days': phase_data.get('duration_days'),
            'event_count': len(phase_data.get('events', [])),
            'financial_impact': phase_data.get('financial_impact')
        }
    
    analysis = {
        'metadata': metadata,
        'total_phases': len(phases),
        'phase_summary': phase_summary,
        'all_phases': phases
    }
    return analysis

def main():
    base_path = '/home/ubuntu/revstream1/data_models'
    
    # Load all data models
    entities_data = load_json(f'{base_path}/entities/entities.json')
    events_data = load_json(f'{base_path}/events/events.json')
    relations_data = load_json(f'{base_path}/relations/relations.json')
    timeline_data = load_json(f'{base_path}/timelines/timeline_enhanced.json')
    
    # Analyze each model
    entities_analysis = analyze_entities(entities_data)
    events_analysis = analyze_events(events_data)
    relations_analysis = analyze_relations(relations_data)
    timeline_analysis = analyze_timeline(timeline_data)
    
    # Create comprehensive analysis
    comprehensive_analysis = {
        'entities': entities_analysis,
        'events': events_analysis,
        'relations': relations_analysis,
        'timeline': timeline_analysis
    }
    
    # Save analysis
    with open('/home/ubuntu/revstream1/model_analysis_output.json', 'w') as f:
        json.dump(comprehensive_analysis, f, indent=2)
    
    print("Analysis complete. Output saved to model_analysis_output.json")
    print(f"\nSummary:")
    print(f"  Entities: {entities_analysis['total_persons']} persons, {entities_analysis['total_organizations']} orgs, {entities_analysis['total_trusts']} trusts")
    print(f"  Events: {events_analysis['total_events']} total events")
    print(f"  Relations: {relations_analysis['total_relations']} total relations")
    print(f"  Timeline: {timeline_analysis['total_phases']} phases")
    print(f"  Events missing perpetrators: {len(events_analysis['events_missing_perpetrators'])}")

if __name__ == '__main__':
    main()
