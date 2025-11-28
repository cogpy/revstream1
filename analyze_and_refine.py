#!/usr/bin/env python3
"""
Comprehensive analysis and refinement script for revstream1 repository
Analyzes entities, relations, events, and timelines with cross-reference to ad-res-j7
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")

# Data model paths
ENTITIES_FILE = REVSTREAM_ROOT / "data_models/entities/entities_refined_2025_11_27_v22.json"
EVENTS_FILE = REVSTREAM_ROOT / "data_models/events/events_refined_2025_11_27_v23.json"
RELATIONS_FILE = REVSTREAM_ROOT / "data_models/relations/relations_refined_2025_11_27_v19.json"
TIMELINE_FILE = REVSTREAM_ROOT / "data_models/timelines/timeline_refined_2025_11_26_v11.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty printing"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_entities(entities_data):
    """Analyze entities for completeness and improvements"""
    issues = []
    improvements = []
    
    metadata = entities_data.get('metadata', {})
    entities = entities_data.get('entities', {})
    
    # Check persons
    persons = entities.get('persons', [])
    for person in persons:
        entity_id = person.get('entity_id')
        
        # Check for missing evidence URLs
        if not person.get('evidence_urls') or len(person.get('evidence_urls', [])) == 0:
            issues.append(f"{entity_id}: Missing evidence URLs")
        
        # Check for missing timeline events
        if not person.get('timeline_events') or len(person.get('timeline_events', [])) == 0:
            issues.append(f"{entity_id}: No timeline events linked")
        
        # Check for missing financial impact
        if person.get('role') in ['primary_perpetrator', 'co_conspirator']:
            if not person.get('financial_impact'):
                issues.append(f"{entity_id}: Missing financial impact data")
    
    # Check organizations
    organizations = entities.get('organizations', [])
    for org in organizations:
        entity_id = org.get('entity_id')
        
        # Check for missing evidence
        if not org.get('evidence_files') or len(org.get('evidence_files', [])) == 0:
            issues.append(f"{entity_id}: Missing evidence files")
    
    return {
        'total_persons': len(persons),
        'total_organizations': len(organizations),
        'total_entities': len(persons) + len(organizations),
        'issues': issues,
        'improvements': improvements
    }

def analyze_events(events_data):
    """Analyze events for completeness and timeline coherence"""
    issues = []
    improvements = []
    
    metadata = events_data.get('metadata', {})
    events = events_data.get('events', [])
    
    # Track event dates for timeline coherence
    event_dates = []
    events_by_phase = defaultdict(list)
    
    for event in events:
        event_id = event.get('event_id')
        event_date = event.get('date')
        
        if event_date:
            event_dates.append((event_date, event_id))
        else:
            issues.append(f"{event_id}: Missing date")
        
        # Check for missing evidence
        if not event.get('evidence') or len(event.get('evidence', [])) == 0:
            issues.append(f"{event_id}: Missing evidence")
        
        # Check for missing entities involved
        if not event.get('entities_involved') or len(event.get('entities_involved', [])) == 0:
            issues.append(f"{event_id}: No entities involved")
        
        # Group by phase
        phase = event.get('timeline_phase', 'UNKNOWN')
        events_by_phase[phase].append(event_id)
    
    # Sort events by date
    event_dates.sort()
    
    return {
        'total_events': len(events),
        'events_by_phase': dict(events_by_phase),
        'earliest_event': event_dates[0] if event_dates else None,
        'latest_event': event_dates[-1] if event_dates else None,
        'issues': issues,
        'improvements': improvements
    }

def analyze_relations(relations_data):
    """Analyze relations for network completeness"""
    issues = []
    improvements = []
    
    metadata = relations_data.get('metadata', {})
    relations = relations_data.get('relations', {})
    
    total_relations = 0
    relations_by_type = defaultdict(int)
    
    for rel_type, rel_list in relations.items():
        total_relations += len(rel_list)
        relations_by_type[rel_type] = len(rel_list)
        
        for rel in rel_list:
            rel_id = rel.get('relation_id')
            
            # Check for missing evidence
            if not rel.get('evidence') or len(rel.get('evidence', [])) == 0:
                issues.append(f"{rel_id}: Missing evidence")
            
            # Check for missing source/target
            if not rel.get('source_entity'):
                issues.append(f"{rel_id}: Missing source entity")
            if not rel.get('target_entity'):
                issues.append(f"{rel_id}: Missing target entity")
    
    return {
        'total_relations': total_relations,
        'relations_by_type': dict(relations_by_type),
        'issues': issues,
        'improvements': improvements
    }

def cross_reference_evidence():
    """Cross-reference with ad-res-j7 evidence repository"""
    evidence_index = AD_RES_J7_ROOT / "COMPREHENSIVE_EVIDENCE_INDEX.md"
    
    if not evidence_index.exists():
        return {'error': 'Evidence index not found'}
    
    # Count evidence files in ad-res-j7
    evidence_files = []
    for ext in ['.pdf', '.PDF', '.eml', '.msg', '.jpg', '.png', '.json', '.md']:
        evidence_files.extend(AD_RES_J7_ROOT.rglob(f'*{ext}'))
    
    return {
        'total_evidence_files': len(evidence_files),
        'evidence_index_exists': True,
        'evidence_repository': str(AD_RES_J7_ROOT)
    }

def generate_improvements_report():
    """Generate comprehensive improvements report"""
    
    print("Loading data models...")
    entities_data = load_json(ENTITIES_FILE)
    events_data = load_json(EVENTS_FILE)
    relations_data = load_json(RELATIONS_FILE)
    
    print("Analyzing entities...")
    entities_analysis = analyze_entities(entities_data)
    
    print("Analyzing events...")
    events_analysis = analyze_events(events_data)
    
    print("Analyzing relations...")
    relations_analysis = analyze_relations(relations_data)
    
    print("Cross-referencing evidence...")
    evidence_analysis = cross_reference_evidence()
    
    report = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'revstream_version': {
                'entities': entities_data.get('metadata', {}).get('version'),
                'events': events_data.get('metadata', {}).get('version'),
                'relations': relations_data.get('metadata', {}).get('version')
            }
        },
        'entities_analysis': entities_analysis,
        'events_analysis': events_analysis,
        'relations_analysis': relations_analysis,
        'evidence_analysis': evidence_analysis,
        'summary': {
            'total_issues': (
                len(entities_analysis['issues']) + 
                len(events_analysis['issues']) + 
                len(relations_analysis['issues'])
            ),
            'total_improvements_suggested': (
                len(entities_analysis['improvements']) + 
                len(events_analysis['improvements']) + 
                len(relations_analysis['improvements'])
            )
        }
    }
    
    # Save report
    report_file = REVSTREAM_ROOT / f"ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(report, report_file)
    
    print(f"\nReport saved to: {report_file}")
    print(f"\nSummary:")
    print(f"  Entities: {entities_analysis['total_entities']}")
    print(f"  Events: {events_analysis['total_events']}")
    print(f"  Relations: {relations_analysis['total_relations']}")
    print(f"  Evidence Files: {evidence_analysis.get('total_evidence_files', 0)}")
    print(f"  Total Issues: {report['summary']['total_issues']}")
    
    return report

if __name__ == '__main__':
    report = generate_improvements_report()
