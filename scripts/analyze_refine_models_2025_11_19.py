#!/usr/bin/env python3
"""
Comprehensive analysis and refinement of entities, relations, events, and timelines
for Revenue Stream Hijacking case 2025-137857
Date: 2025-11-19
"""

import json
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def analyze_entities(entities_data):
    """Analyze entities for completeness and consistency"""
    issues = []
    stats = {
        'total_persons': 0,
        'total_organizations': 0,
        'total_trusts': 0,
        'persons_missing_timeline_events': [],
        'persons_with_incomplete_relationships': [],
        'entities_missing_evidence': []
    }
    
    # Analyze persons
    if 'persons' in entities_data.get('entities', {}):
        persons = entities_data['entities']['persons']
        stats['total_persons'] = len(persons)
        
        for person in persons:
            entity_id = person.get('entity_id', 'UNKNOWN')
            
            # Check for timeline events
            if person.get('involvement_events', 0) > 0 and not person.get('timeline_events'):
                stats['persons_missing_timeline_events'].append(entity_id)
                issues.append(f"{entity_id}: Has involvement_events > 0 but no timeline_events list")
            
            # Check for relationships
            if not person.get('relationships'):
                stats['persons_with_incomplete_relationships'].append(entity_id)
    
    # Analyze organizations
    if 'organizations' in entities_data.get('entities', {}):
        stats['total_organizations'] = len(entities_data['entities']['organizations'])
    
    # Analyze trusts
    if 'trusts' in entities_data.get('entities', {}):
        stats['total_trusts'] = len(entities_data['entities']['trusts'])
    
    return stats, issues

def analyze_events(events_data):
    """Analyze events for completeness and consistency"""
    issues = []
    stats = {
        'total_events': len(events_data.get('events', [])),
        'events_by_phase': defaultdict(int),
        'events_missing_evidence': [],
        'events_missing_perpetrators': [],
        'events_with_inconsistent_entities': []
    }
    
    for event in events_data.get('events', []):
        event_id = event.get('event_id', 'UNKNOWN')
        
        # Count by phase
        phase = event.get('timeline_phase', 'UNKNOWN')
        stats['events_by_phase'][phase] += 1
        
        # Check for evidence
        if not event.get('evidence') and not event.get('evidence_sources'):
            stats['events_missing_evidence'].append(event_id)
            issues.append(f"{event_id}: Missing evidence references")
        
        # Check for perpetrators
        if not event.get('perpetrators') and event.get('category') != 'business_relationship':
            stats['events_missing_perpetrators'].append(event_id)
    
    return stats, issues

def analyze_relations(relations_data):
    """Analyze relations for completeness and consistency"""
    issues = []
    stats = {
        'total_relations': 0,
        'relations_by_type': defaultdict(int),
        'relations_missing_evidence': [],
        'relations_with_undefined_entities': []
    }
    
    for rel_type, relations in relations_data.get('relations', {}).items():
        stats['total_relations'] += len(relations)
        
        for relation in relations:
            rel_id = relation.get('relation_id', 'UNKNOWN')
            stats['relations_by_type'][rel_type] += 1
            
            # Check for evidence
            if not relation.get('evidence'):
                stats['relations_missing_evidence'].append(rel_id)
                issues.append(f"{rel_id}: Missing evidence references")
    
    return stats, issues

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and consistency"""
    issues = []
    stats = {
        'total_phases': len(timeline_data.get('timeline_phases', {})),
        'phase_event_counts': {},
        'phases_with_incorrect_counts': []
    }
    
    for phase_key, phase in timeline_data.get('timeline_phases', {}).items():
        phase_id = phase.get('phase_id', 'UNKNOWN')
        events = phase.get('events', [])
        declared_count = phase.get('event_count', 0)
        actual_count = len(events)
        
        stats['phase_event_counts'][phase_id] = {
            'declared': declared_count,
            'actual': actual_count
        }
        
        if declared_count != actual_count:
            stats['phases_with_incorrect_counts'].append(phase_id)
            issues.append(f"{phase_id}: Declared count {declared_count} != actual count {actual_count}")
    
    return stats, issues

def cross_reference_check(entities_data, events_data, relations_data, timeline_data):
    """Check cross-references between data models"""
    issues = []
    
    # Extract all entity IDs
    entity_ids = set()
    if 'entities' in entities_data:
        for entity_type, entities in entities_data['entities'].items():
            for entity in entities:
                entity_ids.add(entity.get('entity_id', ''))
    
    # Extract all event IDs
    event_ids = set()
    for event in events_data.get('events', []):
        event_ids.add(event.get('event_id', ''))
    
    # Check entity timeline_events references
    if 'entities' in entities_data and 'persons' in entities_data['entities']:
        for person in entities_data['entities']['persons']:
            entity_id = person.get('entity_id', 'UNKNOWN')
            for event_id in person.get('timeline_events', []):
                if event_id not in event_ids:
                    issues.append(f"{entity_id}: References non-existent event {event_id}")
    
    # Check timeline phase event references
    for phase_key, phase in timeline_data.get('timeline_phases', {}).items():
        phase_id = phase.get('phase_id', 'UNKNOWN')
        for event_id in phase.get('events', []):
            if event_id not in event_ids:
                issues.append(f"{phase_id}: References non-existent event {event_id}")
    
    return issues

def generate_improvements(all_stats, all_issues):
    """Generate improvement recommendations"""
    improvements = {
        'priority_high': [],
        'priority_medium': [],
        'priority_low': [],
        'summary': {}
    }
    
    # High priority: Missing evidence
    if all_stats['events']['events_missing_evidence']:
        improvements['priority_high'].append({
            'issue': 'Events missing evidence references',
            'count': len(all_stats['events']['events_missing_evidence']),
            'affected_items': all_stats['events']['events_missing_evidence'][:5],
            'recommendation': 'Add evidence references from ad-res-j7 repository'
        })
    
    if all_stats['relations']['relations_missing_evidence']:
        improvements['priority_high'].append({
            'issue': 'Relations missing evidence references',
            'count': len(all_stats['relations']['relations_missing_evidence']),
            'affected_items': all_stats['relations']['relations_missing_evidence'][:5],
            'recommendation': 'Add evidence references to strengthen relations'
        })
    
    # Medium priority: Timeline inconsistencies
    if all_stats['timeline']['phases_with_incorrect_counts']:
        improvements['priority_medium'].append({
            'issue': 'Timeline phases with incorrect event counts',
            'count': len(all_stats['timeline']['phases_with_incorrect_counts']),
            'affected_items': all_stats['timeline']['phases_with_incorrect_counts'],
            'recommendation': 'Update event_count to match actual events list'
        })
    
    # Low priority: Missing timeline events
    if all_stats['entities']['persons_missing_timeline_events']:
        improvements['priority_low'].append({
            'issue': 'Persons with involvement but no timeline_events',
            'count': len(all_stats['entities']['persons_missing_timeline_events']),
            'affected_items': all_stats['entities']['persons_missing_timeline_events'],
            'recommendation': 'Add timeline_events list to track involvement'
        })
    
    improvements['summary'] = {
        'total_issues': len(all_issues),
        'high_priority_count': len(improvements['priority_high']),
        'medium_priority_count': len(improvements['priority_medium']),
        'low_priority_count': len(improvements['priority_low'])
    }
    
    return improvements

def main():
    print("Loading data models...")
    
    # Load all data models
    entities_data = load_json('data_models/entities/entities_refined_2025_11_18.json')
    events_data = load_json('data_models/events/events_refined_2025_11_18.json')
    relations_data = load_json('data_models/relations/relations_refined_2025_11_18.json')
    timeline_data = load_json('data_models/timelines/timeline_refined_2025_11_18.json')
    
    print("\nAnalyzing entities...")
    entities_stats, entities_issues = analyze_entities(entities_data)
    
    print("Analyzing events...")
    events_stats, events_issues = analyze_events(events_data)
    
    print("Analyzing relations...")
    relations_stats, relations_issues = analyze_relations(relations_data)
    
    print("Analyzing timeline...")
    timeline_stats, timeline_issues = analyze_timeline(timeline_data)
    
    print("Checking cross-references...")
    cross_ref_issues = cross_reference_check(entities_data, events_data, relations_data, timeline_data)
    
    # Combine all stats and issues
    all_stats = {
        'entities': entities_stats,
        'events': events_stats,
        'relations': relations_stats,
        'timeline': timeline_stats
    }
    
    all_issues = entities_issues + events_issues + relations_issues + timeline_issues + cross_ref_issues
    
    print("\nGenerating improvements...")
    improvements = generate_improvements(all_stats, all_issues)
    
    # Create comprehensive report
    report = {
        'metadata': {
            'analysis_date': '2025-11-19',
            'case_number': '2025-137857',
            'analyst': 'automated_analysis',
            'version': '10.0'
        },
        'statistics': all_stats,
        'issues': all_issues,
        'improvements': improvements
    }
    
    # Save report
    save_json(report, 'ANALYSIS_REPORT_2025_11_19.json')
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"\nTotal Issues Found: {len(all_issues)}")
    print(f"High Priority: {improvements['summary']['high_priority_count']}")
    print(f"Medium Priority: {improvements['summary']['medium_priority_count']}")
    print(f"Low Priority: {improvements['summary']['low_priority_count']}")
    print(f"\nReport saved to: ANALYSIS_REPORT_2025_11_19.json")
    
    # Print key statistics
    print("\n" + "="*80)
    print("KEY STATISTICS")
    print("="*80)
    print(f"\nEntities:")
    print(f"  - Persons: {entities_stats['total_persons']}")
    print(f"  - Organizations: {entities_stats['total_organizations']}")
    print(f"  - Trusts: {entities_stats['total_trusts']}")
    
    print(f"\nEvents:")
    print(f"  - Total: {events_stats['total_events']}")
    print(f"  - By Phase:")
    for phase, count in sorted(events_stats['events_by_phase'].items()):
        print(f"    - {phase}: {count}")
    
    print(f"\nRelations:")
    print(f"  - Total: {relations_stats['total_relations']}")
    print(f"  - By Type:")
    for rel_type, count in sorted(relations_stats['relations_by_type'].items()):
        print(f"    - {rel_type}: {count}")
    
    print(f"\nTimeline:")
    print(f"  - Total Phases: {timeline_stats['total_phases']}")
    
    return report

if __name__ == '__main__':
    main()
