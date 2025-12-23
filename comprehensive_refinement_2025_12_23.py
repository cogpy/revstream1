#!/usr/bin/env python3
"""
Comprehensive Refinement Script for Revenue Stream Hijacking Case
Date: 2025-12-23
Purpose: Analyze and refine entities, relations, events, and timelines based on ad-res-j7 evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
AD_RES_J7_PATH = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS_PATH = REVSTREAM_PATH / "data_models"

# Load current models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def backup_file(filepath):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = filepath.parent / f"{filepath.stem}.backup_{timestamp}{filepath.suffix}"
    if filepath.exists():
        import shutil
        shutil.copy(filepath, backup_path)
        print(f"Backed up {filepath.name} to {backup_path.name}")

# Analysis functions
def analyze_entities(entities_data):
    """Analyze entities for completeness and evidence quality"""
    issues = []
    recommendations = []
    
    persons = entities_data.get('entities', {}).get('persons', [])
    orgs = entities_data.get('entities', {}).get('organizations', [])
    
    print(f"\n=== ENTITY ANALYSIS ===")
    print(f"Total Persons: {len(persons)}")
    print(f"Total Organizations: {len(orgs)}")
    
    # Check for missing ad-res-j7 references
    for person in persons:
        entity_id = person.get('entity_id')
        name = person.get('name')
        ad_refs = person.get('ad_res_j7_references', [])
        
        if not ad_refs:
            issues.append(f"{entity_id} ({name}): Missing ad-res-j7 references")
        
        # Check evidence strength
        evidence_strength = person.get('evidence_strength')
        if not evidence_strength:
            issues.append(f"{entity_id} ({name}): Missing evidence strength assessment")
    
    # Check for entities without timeline events
    for person in persons:
        if person.get('agent_type') in ['antagonist', 'co_conspirator']:
            timeline_events = person.get('timeline_events', [])
            if not timeline_events:
                issues.append(f"{person.get('entity_id')}: Antagonist without timeline events")
    
    return {
        'total_persons': len(persons),
        'total_orgs': len(orgs),
        'issues': issues,
        'recommendations': recommendations
    }

def analyze_relations(relations_data):
    """Analyze relations for completeness and evidence quality"""
    issues = []
    recommendations = []
    
    print(f"\n=== RELATIONS ANALYSIS ===")
    
    relation_types = {}
    for rel_type, relations in relations_data.get('relations', {}).items():
        relation_types[rel_type] = len(relations)
        print(f"{rel_type}: {len(relations)} relations")
        
        # Check each relation for evidence
        for rel in relations:
            rel_id = rel.get('relation_id')
            evidence = rel.get('evidence', [])
            ad_evidence = rel.get('ad_res_j7_evidence', [])
            
            if not evidence:
                issues.append(f"{rel_id}: Missing evidence")
            if not ad_evidence:
                issues.append(f"{rel_id}: Missing ad-res-j7 evidence cross-reference")
    
    return {
        'relation_types': relation_types,
        'issues': issues,
        'recommendations': recommendations
    }

def analyze_events(events_data):
    """Analyze events for completeness and chronological accuracy"""
    issues = []
    recommendations = []
    
    events = events_data.get('events', [])
    print(f"\n=== EVENTS ANALYSIS ===")
    print(f"Total Events: {len(events)}")
    
    # Check chronological order
    dates = []
    for event in events:
        event_id = event.get('event_id')
        date = event.get('date')
        
        if date:
            dates.append((date, event_id))
        else:
            issues.append(f"{event_id}: Missing date")
        
        # Check for evidence
        evidence = event.get('evidence', [])
        ad_evidence = event.get('ad_res_j7_evidence', [])
        
        if not evidence:
            issues.append(f"{event_id}: Missing evidence")
        if not ad_evidence:
            issues.append(f"{event_id}: Missing ad-res-j7 evidence")
    
    # Check if dates are in order
    sorted_dates = sorted(dates, key=lambda x: x[0])
    if dates != sorted_dates:
        recommendations.append("Events should be sorted chronologically")
    
    # Categorize by year
    year_counts = {}
    for date, _ in dates:
        year = date[:4]
        year_counts[year] = year_counts.get(year, 0) + 1
    
    print("\nEvents by Year:")
    for year in sorted(year_counts.keys()):
        print(f"  {year}: {year_counts[year]} events")
    
    return {
        'total_events': len(events),
        'year_distribution': year_counts,
        'issues': issues,
        'recommendations': recommendations
    }

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and phase organization"""
    issues = []
    recommendations = []
    
    timeline = timeline_data.get('timeline', [])
    print(f"\n=== TIMELINE ANALYSIS ===")
    print(f"Total Phases: {len(timeline)}")
    
    for phase in timeline:
        phase_id = phase.get('phase_id')
        title = phase.get('title')
        events = phase.get('events', [])
        
        print(f"\n{phase_id}: {title}")
        print(f"  Events: {len(events)}")
        print(f"  Period: {phase.get('period')}")
        
        if not events:
            issues.append(f"{phase_id}: No events assigned")
    
    # Check for orphaned events (events not in any phase)
    all_phase_events = set()
    for phase in timeline:
        all_phase_events.update(phase.get('events', []))
    
    return {
        'total_phases': len(timeline),
        'issues': issues,
        'recommendations': recommendations
    }

def scan_ad_res_j7_evidence():
    """Scan ad-res-j7 repository for available evidence"""
    print(f"\n=== AD-RES-J7 EVIDENCE SCAN ===")
    
    evidence_map = {
        'annexures': [],
        'civil_response': [],
        'criminal_case': [],
        'special_files': []
    }
    
    # Scan ANNEXURES
    annexures_path = AD_RES_J7_PATH / "ANNEXURES"
    if annexures_path.exists():
        for item in annexures_path.iterdir():
            if item.is_dir():
                evidence_map['annexures'].append(item.name)
    
    # Scan civil response
    civil_path = AD_RES_J7_PATH / "1-CIVIL-RESPONSE"
    if civil_path.exists():
        for item in civil_path.rglob("*.md"):
            evidence_map['civil_response'].append(str(item.relative_to(AD_RES_J7_PATH)))
    
    # Scan criminal case
    criminal_path = AD_RES_J7_PATH / "2-CRIMINAL-CASE"
    if criminal_path.exists():
        for item in criminal_path.rglob("*.md"):
            evidence_map['criminal_case'].append(str(item.relative_to(AD_RES_J7_PATH)))
    
    # Look for special files (SF*)
    for item in AD_RES_J7_PATH.rglob("SF*.md"):
        evidence_map['special_files'].append(str(item.relative_to(AD_RES_J7_PATH)))
    
    print(f"Annexures found: {len(evidence_map['annexures'])}")
    print(f"Civil response docs: {len(evidence_map['civil_response'])}")
    print(f"Criminal case docs: {len(evidence_map['criminal_case'])}")
    print(f"Special files: {len(evidence_map['special_files'])}")
    
    return evidence_map

def generate_improvement_recommendations(analysis_results):
    """Generate specific improvement recommendations"""
    recommendations = []
    
    # Entity improvements
    entity_issues = analysis_results['entities']['issues']
    if entity_issues:
        recommendations.append({
            'category': 'entities',
            'priority': 'high',
            'action': 'Add missing ad-res-j7 references to all entities',
            'affected_count': len([i for i in entity_issues if 'ad-res-j7' in i])
        })
    
    # Relations improvements
    relation_issues = analysis_results['relations']['issues']
    if relation_issues:
        recommendations.append({
            'category': 'relations',
            'priority': 'high',
            'action': 'Add evidence cross-references to all relations',
            'affected_count': len([i for i in relation_issues if 'evidence' in i])
        })
    
    # Events improvements
    event_issues = analysis_results['events']['issues']
    if event_issues:
        recommendations.append({
            'category': 'events',
            'priority': 'critical',
            'action': 'Add missing dates and evidence to events',
            'affected_count': len(event_issues)
        })
    
    # Timeline improvements
    timeline_issues = analysis_results['timeline']['issues']
    if timeline_issues:
        recommendations.append({
            'category': 'timeline',
            'priority': 'medium',
            'action': 'Reorganize timeline phases and assign orphaned events',
            'affected_count': len(timeline_issues)
        })
    
    return recommendations

def main():
    print("=" * 80)
    print("COMPREHENSIVE REFINEMENT ANALYSIS")
    print("Revenue Stream Hijacking Case 2025-137857")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Load current models
    entities_path = DATA_MODELS_PATH / "entities" / "entities.json"
    relations_path = DATA_MODELS_PATH / "relations" / "relations.json"
    events_path = DATA_MODELS_PATH / "events" / "events.json"
    timeline_path = DATA_MODELS_PATH / "timelines" / "timeline.json"
    
    entities_data = load_json(entities_path)
    relations_data = load_json(relations_path)
    events_data = load_json(events_path)
    timeline_data = load_json(timeline_path)
    
    # Run analyses
    analysis_results = {
        'entities': analyze_entities(entities_data),
        'relations': analyze_relations(relations_data),
        'events': analyze_events(events_data),
        'timeline': analyze_timeline(timeline_data),
        'evidence_map': scan_ad_res_j7_evidence()
    }
    
    # Generate recommendations
    recommendations = generate_improvement_recommendations(analysis_results)
    
    # Save analysis report
    report = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'case_number': '2025-137857',
            'repositories': ['revstream1', 'ad-res-j7']
        },
        'analysis_results': analysis_results,
        'recommendations': recommendations
    }
    
    report_path = REVSTREAM_PATH / f"COMPREHENSIVE_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(report, report_path)
    
    print(f"\n{'=' * 80}")
    print("ANALYSIS COMPLETE")
    print(f"Report saved to: {report_path.name}")
    print(f"\n=== RECOMMENDATIONS ===")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. [{rec['priority'].upper()}] {rec['category']}: {rec['action']}")
        print(f"   Affected items: {rec['affected_count']}")
    print("=" * 80)

if __name__ == "__main__":
    main()
