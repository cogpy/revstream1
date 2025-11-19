#!/usr/bin/env python3
"""
Comprehensive analysis of entities, relations, events, and timelines
to identify gaps, inconsistencies, and improvement opportunities.
"""

import json
from datetime import datetime
from collections import defaultdict, Counter

def load_json(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_entities(entities_data):
    """Analyze entities for completeness and consistency."""
    print("\n" + "="*80)
    print("ENTITIES ANALYSIS")
    print("="*80)
    
    issues = []
    stats = {
        'total_persons': 0,
        'total_organizations': 0,
        'missing_evidence': [],
        'missing_ad_res_j7_refs': [],
        'antagonists': 0,
        'victims': 0,
        'total_financial_impact': 0
    }
    
    if not entities_data or 'entities' not in entities_data:
        return issues, stats
    
    # Analyze persons
    if 'persons' in entities_data['entities']:
        stats['total_persons'] = len(entities_data['entities']['persons'])
        for person in entities_data['entities']['persons']:
            entity_id = person.get('entity_id', 'UNKNOWN')
            
            # Check for missing evidence files
            if not person.get('evidence_files'):
                issues.append(f"{entity_id}: Missing evidence_files")
                stats['missing_evidence'].append(entity_id)
            
            # Check for missing ad-res-j7 references
            if not person.get('ad_res_j7_references'):
                issues.append(f"{entity_id}: Missing ad_res_j7_references")
                stats['missing_ad_res_j7_refs'].append(entity_id)
            
            # Count agent types
            if person.get('agent_type') == 'antagonist':
                stats['antagonists'] += 1
            elif person.get('agent_type') == 'victim':
                stats['victims'] += 1
    
    # Analyze organizations
    if 'organizations' in entities_data['entities']:
        stats['total_organizations'] = len(entities_data['entities']['organizations'])
        for org in entities_data['entities']['organizations']:
            entity_id = org.get('entity_id', 'UNKNOWN')
            
            # Check for missing evidence files
            if not org.get('evidence_files'):
                issues.append(f"{entity_id}: Missing evidence_files")
                stats['missing_evidence'].append(entity_id)
    
    print(f"\nTotal Persons: {stats['total_persons']}")
    print(f"Total Organizations: {stats['total_organizations']}")
    print(f"Antagonists: {stats['antagonists']}")
    print(f"Victims: {stats['victims']}")
    print(f"\nEntities missing evidence_files: {len(stats['missing_evidence'])}")
    print(f"Entities missing ad_res_j7_references: {len(stats['missing_ad_res_j7_refs'])}")
    
    return issues, stats

def analyze_events(events_data):
    """Analyze events for completeness and consistency."""
    print("\n" + "="*80)
    print("EVENTS ANALYSIS")
    print("="*80)
    
    issues = []
    stats = {
        'total_events': 0,
        'events_by_category': Counter(),
        'events_by_phase': Counter(),
        'events_by_application': Counter(),
        'missing_perpetrators': [],
        'missing_evidence': [],
        'missing_application_mapping': [],
        'events_with_financial_impact': 0,
        'total_financial_mentions': 0
    }
    
    if not events_data or 'events' not in events_data:
        return issues, stats
    
    events = events_data['events']
    stats['total_events'] = len(events)
    
    for event in events:
        event_id = event.get('event_id', 'UNKNOWN')
        
        # Category analysis
        category = event.get('category', 'uncategorized')
        stats['events_by_category'][category] += 1
        
        # Phase analysis
        phase = event.get('timeline_phase', 'unassigned')
        stats['events_by_phase'][phase] += 1
        
        # Application mapping analysis
        related_apps = event.get('related_applications', [])
        if not related_apps:
            issues.append(f"{event_id}: Missing related_applications")
            stats['missing_application_mapping'].append(event_id)
        else:
            for app in related_apps:
                stats['events_by_application'][app] += 1
        
        # Perpetrator analysis
        perpetrators = event.get('perpetrators', [])
        if not perpetrators and category not in ['business_relationship', 'financial_structure']:
            issues.append(f"{event_id}: Missing perpetrators")
            stats['missing_perpetrators'].append(event_id)
        
        # Evidence analysis
        evidence = event.get('evidence', [])
        if not evidence:
            issues.append(f"{event_id}: Missing evidence")
            stats['missing_evidence'].append(event_id)
        
        # Financial impact analysis
        if event.get('financial_impact'):
            stats['events_with_financial_impact'] += 1
            stats['total_financial_mentions'] += 1
    
    print(f"\nTotal Events: {stats['total_events']}")
    print(f"Events with Financial Impact: {stats['events_with_financial_impact']}")
    print(f"\nEvents by Category:")
    for cat, count in stats['events_by_category'].most_common():
        print(f"  {cat}: {count}")
    
    print(f"\nEvents by Phase:")
    for phase, count in sorted(stats['events_by_phase'].items()):
        print(f"  {phase}: {count}")
    
    print(f"\nEvents by Application:")
    for app, count in sorted(stats['events_by_application'].items()):
        print(f"  {app}: {count}")
    
    print(f"\nEvents missing perpetrators: {len(stats['missing_perpetrators'])}")
    print(f"Events missing evidence: {len(stats['missing_evidence'])}")
    print(f"Events missing application mapping: {len(stats['missing_application_mapping'])}")
    
    return issues, stats

def analyze_relations(relations_data):
    """Analyze relations for completeness and consistency."""
    print("\n" + "="*80)
    print("RELATIONS ANALYSIS")
    print("="*80)
    
    issues = []
    stats = {
        'total_relations': 0,
        'relations_by_type': Counter(),
        'missing_evidence': [],
        'missing_application_mapping': []
    }
    
    if not relations_data or 'relations' not in relations_data:
        return issues, stats
    
    relations = relations_data['relations']
    
    # Count all relation types
    for rel_type, rel_list in relations.items():
        stats['total_relations'] += len(rel_list)
        stats['relations_by_type'][rel_type] = len(rel_list)
        
        for rel in rel_list:
            rel_id = rel.get('relation_id', 'UNKNOWN')
            
            # Check for missing evidence
            if not rel.get('evidence'):
                issues.append(f"{rel_id}: Missing evidence")
                stats['missing_evidence'].append(rel_id)
            
            # Check for missing application mapping
            if not rel.get('related_applications'):
                issues.append(f"{rel_id}: Missing related_applications")
                stats['missing_application_mapping'].append(rel_id)
    
    print(f"\nTotal Relations: {stats['total_relations']}")
    print(f"\nRelations by Type:")
    for rel_type, count in sorted(stats['relations_by_type'].items()):
        print(f"  {rel_type}: {count}")
    
    print(f"\nRelations missing evidence: {len(stats['missing_evidence'])}")
    print(f"Relations missing application mapping: {len(stats['missing_application_mapping'])}")
    
    return issues, stats

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and consistency."""
    print("\n" + "="*80)
    print("TIMELINE ANALYSIS")
    print("="*80)
    
    issues = []
    stats = {
        'total_phases': 0,
        'total_events_in_phases': 0,
        'events_per_phase': {},
        'phase_durations': {},
        'missing_application_mapping': []
    }
    
    if not timeline_data or 'timeline_phases' not in timeline_data:
        return issues, stats
    
    phases = timeline_data['timeline_phases']
    stats['total_phases'] = len(phases)
    
    for phase_key, phase in phases.items():
        phase_id = phase.get('phase_id', 'UNKNOWN')
        events = phase.get('events', [])
        
        stats['events_per_phase'][phase_id] = len(events)
        stats['total_events_in_phases'] += len(events)
        
        # Calculate duration
        if phase.get('start_date') and phase.get('end_date'):
            stats['phase_durations'][phase_id] = phase.get('duration_days', 0)
        
        # Check for missing application mapping
        if not phase.get('related_applications'):
            issues.append(f"{phase_id}: Missing related_applications")
            stats['missing_application_mapping'].append(phase_id)
    
    print(f"\nTotal Phases: {stats['total_phases']}")
    print(f"Total Events in Phases: {stats['total_events_in_phases']}")
    
    print(f"\nEvents per Phase:")
    for phase_id, count in sorted(stats['events_per_phase'].items()):
        duration = stats['phase_durations'].get(phase_id, 0)
        print(f"  {phase_id}: {count} events ({duration} days)")
    
    print(f"\nPhases missing application mapping: {len(stats['missing_application_mapping'])}")
    
    return issues, stats

def main():
    """Main analysis function."""
    print("\n" + "="*80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS")
    print("="*80)
    
    # Load data models
    entities = load_json('data_models/entities/entities_refined_2025_11_19_v3.json')
    events = load_json('data_models/events/events_refined_2025_11_19_v3.json')
    relations = load_json('data_models/relations/relations_refined_2025_11_19_v3.json')
    timeline = load_json('data_models/timelines/timeline_refined_2025_11_19_v3.json')
    
    all_issues = []
    
    # Analyze each component
    entity_issues, entity_stats = analyze_entities(entities)
    all_issues.extend(entity_issues)
    
    event_issues, event_stats = analyze_events(events)
    all_issues.extend(event_issues)
    
    relation_issues, relation_stats = analyze_relations(relations)
    all_issues.extend(relation_issues)
    
    timeline_issues, timeline_stats = analyze_timeline(timeline)
    all_issues.extend(timeline_issues)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY OF ISSUES")
    print("="*80)
    print(f"\nTotal Issues Found: {len(all_issues)}")
    
    if all_issues:
        print("\nTop 20 Issues:")
        for i, issue in enumerate(all_issues[:20], 1):
            print(f"  {i}. {issue}")
    
    # Save analysis report
    report = {
        'analysis_date': datetime.now().isoformat(),
        'entity_stats': entity_stats,
        'event_stats': dict(event_stats['events_by_category']),
        'relation_stats': dict(relation_stats['relations_by_type']),
        'timeline_stats': timeline_stats,
        'total_issues': len(all_issues),
        'issues': all_issues
    }
    
    with open('DATA_MODEL_ANALYSIS_REPORT.json', 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"\n\nDetailed report saved to: DATA_MODEL_ANALYSIS_REPORT.json")

if __name__ == '__main__':
    main()
