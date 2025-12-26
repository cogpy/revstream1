#!/usr/bin/env python3
"""
Comprehensive analysis of entities, relations, events, and timelines
Identifies gaps, inconsistencies, and improvement opportunities
"""

import json
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities for completeness and consistency"""
    issues = []
    stats = {
        'total_persons': 0,
        'total_organizations': 0,
        'total_trusts': 0,
        'persons_with_timeline_events': 0,
        'persons_without_timeline_events': 0,
        'missing_evidence': 0
    }
    
    # Analyze persons
    if 'persons' in entities_data.get('entities', {}):
        persons = entities_data['entities']['persons']
        stats['total_persons'] = len(persons)
        
        for person in persons:
            entity_id = person.get('entity_id', 'UNKNOWN')
            
            # Check timeline events
            timeline_events = person.get('timeline_events', [])
            if timeline_events:
                stats['persons_with_timeline_events'] += 1
            else:
                stats['persons_without_timeline_events'] += 1
                if person.get('involvement_events', 0) > 0:
                    issues.append(f"{entity_id} ({person.get('name')}): Has involvement_events={person.get('involvement_events')} but no timeline_events listed")
            
            # Check for missing financial impact on antagonists
            if person.get('agent_type') == 'antagonist':
                if 'financial_impact' not in person:
                    issues.append(f"{entity_id} ({person.get('name')}): Antagonist missing financial_impact data")
    
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
        'total_events': 0,
        'events_by_phase': defaultdict(int),
        'events_by_category': defaultdict(int),
        'events_without_evidence': 0,
        'events_without_financial_impact': 0,
        'date_range': {'earliest': None, 'latest': None}
    }
    
    events = events_data.get('events', [])
    stats['total_events'] = len(events)
    
    dates = []
    for event in events:
        event_id = event.get('event_id', 'UNKNOWN')
        
        # Track phase distribution
        phase = event.get('timeline_phase', 'UNASSIGNED')
        stats['events_by_phase'][phase] += 1
        
        # Track category distribution
        category = event.get('category', 'UNCATEGORIZED')
        stats['events_by_category'][category] += 1
        
        # Check evidence
        evidence = event.get('evidence', [])
        if not evidence:
            stats['events_without_evidence'] += 1
            issues.append(f"{event_id}: Missing evidence references")
        
        # Check financial impact
        financial_impact = event.get('financial_impact', '')
        if not financial_impact or financial_impact == 'unknown':
            stats['events_without_financial_impact'] += 1
        
        # Track dates
        event_date = event.get('date')
        if event_date:
            dates.append(event_date)
    
    if dates:
        stats['date_range']['earliest'] = min(dates)
        stats['date_range']['latest'] = max(dates)
    
    return stats, issues

def analyze_relations(relations_data):
    """Analyze relations for completeness and consistency"""
    issues = []
    stats = {
        'total_relations': 0,
        'relations_by_type': defaultdict(int),
        'relations_without_evidence': 0,
        'conspiracy_relations': 0
    }
    
    relations = relations_data.get('relations', {})
    
    for relation_type, relation_list in relations.items():
        if isinstance(relation_list, list):
            stats['total_relations'] += len(relation_list)
            stats['relations_by_type'][relation_type] = len(relation_list)
            
            for relation in relation_list:
                relation_id = relation.get('relation_id', 'UNKNOWN')
                
                # Check evidence
                evidence = relation.get('evidence', [])
                if not evidence:
                    stats['relations_without_evidence'] += 1
                    issues.append(f"{relation_id}: Missing evidence references")
                
                # Count conspiracy relations
                if 'conspiracy' in relation_type or relation.get('relation_type') == 'co_conspirator':
                    stats['conspiracy_relations'] += 1
    
    return stats, issues

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and consistency"""
    issues = []
    stats = {
        'total_phases': 0,
        'phase_details': {},
        'total_events_in_phases': 0,
        'orphaned_events': []
    }
    
    phases = timeline_data.get('timeline_phases', {})
    stats['total_phases'] = len(phases)
    
    all_phase_events = set()
    
    for phase_key, phase_data in phases.items():
        phase_id = phase_data.get('phase_id', 'UNKNOWN')
        events = phase_data.get('events', [])
        event_count = len(events)
        
        stats['phase_details'][phase_id] = {
            'name': phase_data.get('phase_name', 'Unknown'),
            'event_count': event_count,
            'start_date': phase_data.get('start_date'),
            'end_date': phase_data.get('end_date'),
            'financial_impact': phase_data.get('financial_impact', 'unknown')
        }
        
        stats['total_events_in_phases'] += event_count
        all_phase_events.update(events)
        
        # Check for missing event count
        declared_count = phase_data.get('event_count', 0)
        if declared_count != event_count:
            issues.append(f"{phase_id}: Declared event_count={declared_count} but actual events={event_count}")
    
    return stats, issues

def cross_reference_analysis(entities_data, events_data, relations_data, timeline_data):
    """Cross-reference entities, events, relations, and timeline"""
    issues = []
    
    # Extract all entity IDs
    entity_ids = set()
    if 'persons' in entities_data.get('entities', {}):
        entity_ids.update([p.get('entity_id') for p in entities_data['entities']['persons']])
    if 'organizations' in entities_data.get('entities', {}):
        entity_ids.update([o.get('entity_id') for o in entities_data['entities']['organizations']])
    if 'trusts' in entities_data.get('entities', {}):
        entity_ids.update([t.get('entity_id') for t in entities_data['entities']['trusts']])
    
    # Extract all event IDs
    event_ids = set([e.get('event_id') for e in events_data.get('events', [])])
    
    # Check entity timeline events exist
    if 'persons' in entities_data.get('entities', {}):
        for person in entities_data['entities']['persons']:
            entity_id = person.get('entity_id')
            timeline_events = person.get('timeline_events', [])
            for event_id in timeline_events:
                if event_id not in event_ids:
                    issues.append(f"{entity_id}: References non-existent event {event_id}")
    
    # Check timeline phase events exist
    phases = timeline_data.get('timeline_phases', {})
    for phase_key, phase_data in phases.items():
        phase_id = phase_data.get('phase_id')
        for event_id in phase_data.get('events', []):
            if event_id not in event_ids:
                issues.append(f"{phase_id}: References non-existent event {event_id}")
    
    return issues

def generate_recommendations(all_stats, all_issues):
    """Generate improvement recommendations"""
    recommendations = []
    
    # Entity recommendations
    if all_stats['entities']['persons_without_timeline_events'] > 0:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'entities',
            'issue': f"{all_stats['entities']['persons_without_timeline_events']} persons without timeline_events",
            'action': 'Review persons with involvement_events > 0 and add timeline_events references'
        })
    
    # Event recommendations
    if all_stats['events']['events_without_evidence'] > 0:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'events',
            'issue': f"{all_stats['events']['events_without_evidence']} events without evidence",
            'action': 'Add evidence references from ad-res-j7 repository'
        })
    
    if all_stats['events']['events_without_financial_impact'] > 0:
        recommendations.append({
            'priority': 'MEDIUM',
            'category': 'events',
            'issue': f"{all_stats['events']['events_without_financial_impact']} events without financial_impact",
            'action': 'Calculate and add financial impact where applicable'
        })
    
    # Relations recommendations
    if all_stats['relations']['relations_without_evidence'] > 0:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'relations',
            'issue': f"{all_stats['relations']['relations_without_evidence']} relations without evidence",
            'action': 'Add evidence references to strengthen relation claims'
        })
    
    return recommendations

def main():
    print("=" * 80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS - 2025-11-19")
    print("=" * 80)
    print()
    
    # Load all data models
    entities_data = load_json('data_models/entities/entities_refined_2025_11_19.json')
    events_data = load_json('data_models/events/events_refined_2025_11_19.json')
    relations_data = load_json('data_models/relations/relations_refined_2025_11_19.json')
    timeline_data = load_json('data_models/timelines/timeline_refined_2025_11_19.json')
    
    all_stats = {}
    all_issues = []
    
    # Analyze entities
    print("ANALYZING ENTITIES...")
    entity_stats, entity_issues = analyze_entities(entities_data)
    all_stats['entities'] = entity_stats
    all_issues.extend(entity_issues)
    print(f"  Total Persons: {entity_stats['total_persons']}")
    print(f"  Total Organizations: {entity_stats['total_organizations']}")
    print(f"  Total Trusts: {entity_stats['total_trusts']}")
    print(f"  Persons with timeline events: {entity_stats['persons_with_timeline_events']}")
    print(f"  Persons without timeline events: {entity_stats['persons_without_timeline_events']}")
    print()
    
    # Analyze events
    print("ANALYZING EVENTS...")
    event_stats, event_issues = analyze_events(events_data)
    all_stats['events'] = event_stats
    all_issues.extend(event_issues)
    print(f"  Total Events: {event_stats['total_events']}")
    print(f"  Date Range: {event_stats['date_range']['earliest']} to {event_stats['date_range']['latest']}")
    print(f"  Events without evidence: {event_stats['events_without_evidence']}")
    print(f"  Events without financial impact: {event_stats['events_without_financial_impact']}")
    print(f"  Events by phase:")
    for phase, count in sorted(event_stats['events_by_phase'].items()):
        print(f"    {phase}: {count}")
    print()
    
    # Analyze relations
    print("ANALYZING RELATIONS...")
    relation_stats, relation_issues = analyze_relations(relations_data)
    all_stats['relations'] = relation_stats
    all_issues.extend(relation_issues)
    print(f"  Total Relations: {relation_stats['total_relations']}")
    print(f"  Conspiracy Relations: {relation_stats['conspiracy_relations']}")
    print(f"  Relations without evidence: {relation_stats['relations_without_evidence']}")
    print(f"  Relations by type:")
    for rel_type, count in sorted(relation_stats['relations_by_type'].items()):
        print(f"    {rel_type}: {count}")
    print()
    
    # Analyze timeline
    print("ANALYZING TIMELINE...")
    timeline_stats, timeline_issues = analyze_timeline(timeline_data)
    all_stats['timeline'] = timeline_stats
    all_issues.extend(timeline_issues)
    print(f"  Total Phases: {timeline_stats['total_phases']}")
    print(f"  Total Events in Phases: {timeline_stats['total_events_in_phases']}")
    print(f"  Phase details:")
    for phase_id, details in sorted(timeline_stats['phase_details'].items()):
        print(f"    {phase_id} ({details['name']}): {details['event_count']} events, {details['financial_impact']}")
    print()
    
    # Cross-reference analysis
    print("CROSS-REFERENCING...")
    cross_ref_issues = cross_reference_analysis(entities_data, events_data, relations_data, timeline_data)
    all_issues.extend(cross_ref_issues)
    print(f"  Cross-reference issues found: {len(cross_ref_issues)}")
    print()
    
    # Generate recommendations
    print("GENERATING RECOMMENDATIONS...")
    recommendations = generate_recommendations(all_stats, all_issues)
    print(f"  Total recommendations: {len(recommendations)}")
    print()
    
    # Output detailed issues
    print("=" * 80)
    print("ISSUES FOUND")
    print("=" * 80)
    for i, issue in enumerate(all_issues[:20], 1):  # Show first 20
        print(f"{i}. {issue}")
    if len(all_issues) > 20:
        print(f"... and {len(all_issues) - 20} more issues")
    print()
    
    # Output recommendations
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. [{rec['priority']}] {rec['category'].upper()}")
        print(f"   Issue: {rec['issue']}")
        print(f"   Action: {rec['action']}")
        print()
    
    # Save analysis to file
    analysis_report = {
        'timestamp': datetime.now().isoformat(),
        'statistics': all_stats,
        'issues': all_issues,
        'recommendations': recommendations
    }
    
    with open('COMPREHENSIVE_ANALYSIS_REPORT_2025_11_19.json', 'w') as f:
        json.dump(analysis_report, f, indent=2)
    
    print("=" * 80)
    print("Analysis complete. Report saved to COMPREHENSIVE_ANALYSIS_REPORT_2025_11_19.json")
    print("=" * 80)

if __name__ == '__main__':
    main()
