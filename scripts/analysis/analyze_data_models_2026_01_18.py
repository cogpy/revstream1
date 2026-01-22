#!/usr/bin/env python3
"""
Comprehensive Data Model Analysis Script
Analyzes entities, relations, events, and timeline for accuracy and completeness
"""

import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities for completeness and consistency"""
    issues = []
    stats = {
        'total_persons': 0,
        'total_organizations': 0,
        'missing_evidence': 0,
        'missing_ad_res_j7_refs': 0,
        'strong_evidence': 0,
        'conclusive_evidence': 0,
        'criminal_threshold_met': 0
    }
    
    persons = entities_data.get('entities', {}).get('persons', [])
    orgs = entities_data.get('entities', {}).get('organizations', [])
    
    stats['total_persons'] = len(persons)
    stats['total_organizations'] = len(orgs)
    
    # Check persons
    for person in persons:
        entity_id = person.get('entity_id', 'UNKNOWN')
        
        # Check for evidence
        if not person.get('evidence') or len(person.get('evidence', [])) == 0:
            stats['missing_evidence'] += 1
            issues.append(f"{entity_id}: Missing evidence field or empty")
        
        # Check for ad-res-j7 references
        if not person.get('ad_res_j7_references') or len(person.get('ad_res_j7_references', [])) == 0:
            stats['missing_ad_res_j7_refs'] += 1
            issues.append(f"{entity_id}: Missing ad_res_j7_references")
        
        # Count evidence strength
        evidence_strength = person.get('evidence_strength', '')
        if evidence_strength == 'strong':
            stats['strong_evidence'] += 1
        elif evidence_strength == 'conclusive':
            stats['conclusive_evidence'] += 1
        
        # Count criminal threshold
        if person.get('criminal_threshold') in ['95%_exceeded', '95%_likely', 'yes']:
            stats['criminal_threshold_met'] += 1
    
    # Check organizations
    for org in orgs:
        entity_id = org.get('entity_id', 'UNKNOWN')
        
        if not org.get('evidence') or len(org.get('evidence', [])) == 0:
            stats['missing_evidence'] += 1
            issues.append(f"{entity_id}: Missing evidence field or empty")
        
        if not org.get('ad_res_j7_references') or len(org.get('ad_res_j7_references', [])) == 0:
            stats['missing_ad_res_j7_refs'] += 1
            issues.append(f"{entity_id}: Missing ad_res_j7_references")
    
    return stats, issues

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    issues = []
    stats = {
        'total_relations': 0,
        'missing_evidence': 0,
        'missing_ad_res_j7_refs': 0,
        'verified_relations': 0
    }
    
    relations = relations_data.get('relations', {})
    
    for rel_type, rel_list in relations.items():
        stats['total_relations'] += len(rel_list)
        
        for rel in rel_list:
            rel_id = rel.get('relation_id', 'UNKNOWN')
            
            if not rel.get('evidence') or len(rel.get('evidence', [])) == 0:
                stats['missing_evidence'] += 1
                issues.append(f"{rel_id}: Missing evidence")
            
            if not rel.get('ad_res_j7_evidence') or len(rel.get('ad_res_j7_evidence', [])) == 0:
                stats['missing_ad_res_j7_refs'] += 1
                issues.append(f"{rel_id}: Missing ad_res_j7_evidence")
            
            if rel.get('evidence_verified'):
                stats['verified_relations'] += 1
    
    return stats, issues

def analyze_events(events_data):
    """Analyze events for completeness"""
    issues = []
    stats = {
        'total_events': 0,
        'missing_evidence': 0,
        'missing_ad_res_j7_refs': 0,
        'criminal_threshold': 0,
        'civil_threshold': 0,
        'phase_distribution': defaultdict(int)
    }
    
    events = events_data.get('events', [])
    stats['total_events'] = len(events)
    
    for event in events:
        event_id = event.get('event_id', 'UNKNOWN')
        
        if not event.get('evidence') or len(event.get('evidence', [])) == 0:
            stats['missing_evidence'] += 1
            issues.append(f"{event_id}: Missing evidence")
        
        if not event.get('ad_res_j7_evidence') or len(event.get('ad_res_j7_evidence', [])) == 0:
            stats['missing_ad_res_j7_refs'] += 1
            issues.append(f"{event_id}: Missing ad_res_j7_evidence")
        
        # Count burden of proof
        burden = event.get('burden_of_proof', '')
        if 'criminal' in burden or event.get('criminal_threshold') == 'yes':
            stats['criminal_threshold'] += 1
        if 'civil' in burden:
            stats['civil_threshold'] += 1
        
        # Phase distribution
        phase = event.get('phase', event.get('timeline_phase', 'UNKNOWN'))
        stats['phase_distribution'][phase] += 1
    
    return stats, issues

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness"""
    issues = []
    stats = {
        'total_entries': 0,
        'missing_evidence': 0,
        'missing_entities': 0,
        'criminal_threshold': 0,
        'civil_threshold': 0
    }
    
    timeline = timeline_data.get('timeline', [])
    stats['total_entries'] = len(timeline)
    
    for entry in timeline:
        entry_id = entry.get('entry_id', entry.get('date', 'UNKNOWN'))
        
        if not entry.get('evidence') and not entry.get('source'):
            stats['missing_evidence'] += 1
            issues.append(f"{entry_id}: Missing evidence/source")
        
        if not entry.get('entities_involved') and not entry.get('entity'):
            stats['missing_entities'] += 1
            issues.append(f"{entry_id}: Missing entities_involved")
        
        # Count burden of proof
        burden = entry.get('burden_of_proof', '')
        if 'criminal' in burden:
            stats['criminal_threshold'] += 1
        if 'civil' in burden:
            stats['civil_threshold'] += 1
    
    return stats, issues

def main():
    """Main analysis function"""
    base_dir = '/home/ubuntu/revstream1/data_models'
    
    print("=" * 80)
    print("DATA MODEL COMPREHENSIVE ANALYSIS")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    # Load data models
    entities_data = load_json(f'{base_dir}/entities/entities.json')
    relations_data = load_json(f'{base_dir}/relations/relations.json')
    events_data = load_json(f'{base_dir}/events/events.json')
    timeline_data = load_json(f'{base_dir}/timelines/timeline.json')
    
    # Analyze each model
    print("ENTITIES ANALYSIS")
    print("-" * 80)
    entity_stats, entity_issues = analyze_entities(entities_data)
    for key, value in entity_stats.items():
        print(f"  {key}: {value}")
    print()
    
    print("RELATIONS ANALYSIS")
    print("-" * 80)
    relation_stats, relation_issues = analyze_relations(relations_data)
    for key, value in relation_stats.items():
        print(f"  {key}: {value}")
    print()
    
    print("EVENTS ANALYSIS")
    print("-" * 80)
    event_stats, event_issues = analyze_events(events_data)
    for key, value in event_stats.items():
        print(f"  {key}: {value}")
    print()
    
    print("TIMELINE ANALYSIS")
    print("-" * 80)
    timeline_stats, timeline_issues = analyze_timeline(timeline_data)
    for key, value in timeline_stats.items():
        print(f"  {key}: {value}")
    print()
    
    # Summary of issues
    print("=" * 80)
    print("ISSUES SUMMARY")
    print("=" * 80)
    print(f"Total Issues Found: {len(entity_issues) + len(relation_issues) + len(event_issues) + len(timeline_issues)}")
    print()
    
    if entity_issues:
        print(f"Entity Issues ({len(entity_issues)}):")
        for issue in entity_issues[:10]:  # Show first 10
            print(f"  - {issue}")
        if len(entity_issues) > 10:
            print(f"  ... and {len(entity_issues) - 10} more")
        print()
    
    if relation_issues:
        print(f"Relation Issues ({len(relation_issues)}):")
        for issue in relation_issues[:10]:
            print(f"  - {issue}")
        if len(relation_issues) > 10:
            print(f"  ... and {len(relation_issues) - 10} more")
        print()
    
    if event_issues:
        print(f"Event Issues ({len(event_issues)}):")
        for issue in event_issues[:10]:
            print(f"  - {issue}")
        if len(event_issues) > 10:
            print(f"  ... and {len(event_issues) - 10} more")
        print()
    
    if timeline_issues:
        print(f"Timeline Issues ({len(timeline_issues)}):")
        for issue in timeline_issues[:10]:
            print(f"  - {issue}")
        if len(timeline_issues) > 10:
            print(f"  ... and {len(timeline_issues) - 10} more")
        print()
    
    # Recommendations
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    recommendations = []
    
    if entity_stats['missing_evidence'] > 0:
        recommendations.append(f"Add evidence references to {entity_stats['missing_evidence']} entities")
    
    if entity_stats['missing_ad_res_j7_refs'] > 0:
        recommendations.append(f"Add ad-res-j7 references to {entity_stats['missing_ad_res_j7_refs']} entities")
    
    if relation_stats['missing_evidence'] > 0:
        recommendations.append(f"Add evidence to {relation_stats['missing_evidence']} relations")
    
    if event_stats['missing_evidence'] > 0:
        recommendations.append(f"Add evidence to {event_stats['missing_evidence']} events")
    
    if timeline_stats['missing_evidence'] > 0:
        recommendations.append(f"Add evidence to {timeline_stats['missing_evidence']} timeline entries")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
    
    print()
    print("=" * 80)
    print("Analysis complete. Review issues and implement recommendations.")
    print("=" * 80)

if __name__ == '__main__':
    main()
