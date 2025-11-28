#!/usr/bin/env python3
"""
Comprehensive Refinement Script for Revenue Stream Case 2025-137857
Analyzes and refines entities, relations, events, and timelines
Cross-references with ad-res-j7 extended evidence repository
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS_DIR = REVSTREAM_ROOT / "data_models"

# Latest data model files
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities_refined_2025_11_27_v22.json"
EVENTS_FILE = DATA_MODELS_DIR / "events" / "events_refined_2025_11_28_v24.json"
RELATIONS_FILE = DATA_MODELS_DIR / "relations" / "relations.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timelines" / "timeline_refined_2025_11_26_v11.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_entities(entities_data):
    """Analyze entities for completeness and consistency"""
    issues = []
    improvements = []
    
    persons = entities_data.get('entities', {}).get('persons', [])
    organizations = entities_data.get('entities', {}).get('organizations', [])
    
    # Check for missing evidence references
    for person in persons:
        if not person.get('ad_res_j7_references'):
            issues.append(f"Person {person.get('name')} missing ad_res_j7_references")
            improvements.append({
                'entity_id': person.get('entity_id'),
                'type': 'add_ad_res_j7_references',
                'suggestion': 'Add cross-references to ad-res-j7 evidence'
            })
        
        if not person.get('evidence_files'):
            issues.append(f"Person {person.get('name')} missing evidence_files")
    
    for org in organizations:
        if not org.get('ad_res_j7_references'):
            issues.append(f"Organization {org.get('name')} missing ad_res_j7_references")
            improvements.append({
                'entity_id': org.get('entity_id'),
                'type': 'add_ad_res_j7_references',
                'suggestion': 'Add cross-references to ad-res-j7 evidence'
            })
    
    return {
        'total_persons': len(persons),
        'total_organizations': len(organizations),
        'issues': issues,
        'improvements': improvements
    }

def analyze_events(events_data):
    """Analyze events for timeline coherence and evidence links"""
    issues = []
    improvements = []
    
    events = events_data.get('events', [])
    
    # Group events by phase
    events_by_phase = defaultdict(list)
    events_without_phase = []
    
    for event in events:
        phase = event.get('phase')
        event_id = event.get('event_id')
        
        if phase:
            events_by_phase[phase].append(event_id)
        else:
            events_without_phase.append(event_id)
            issues.append(f"Event {event_id} missing phase classification")
        
        # Check for evidence references
        if not event.get('evidence_files') and not event.get('ad_res_j7_references'):
            issues.append(f"Event {event_id} missing evidence references")
            improvements.append({
                'event_id': event_id,
                'type': 'add_evidence_references',
                'suggestion': 'Add evidence file references and ad-res-j7 cross-references'
            })
        
        # Check for financial impact where applicable
        if event.get('financial_impact') and event['financial_impact'] != 'TBD':
            try:
                # Validate financial impact format
                impact = event['financial_impact']
                if isinstance(impact, str) and impact.startswith('R'):
                    # Valid format
                    pass
            except:
                issues.append(f"Event {event_id} has invalid financial_impact format")
    
    return {
        'total_events': len(events),
        'events_by_phase': dict(events_by_phase),
        'events_without_phase': events_without_phase,
        'issues': issues,
        'improvements': improvements
    }

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    issues = []
    improvements = []
    
    # Relations data has nested structure with categories
    relations_dict = relations_data.get('relations', {})
    all_relations = []
    
    # Flatten all relation categories
    for category, relations_list in relations_dict.items():
        if isinstance(relations_list, list):
            all_relations.extend(relations_list)
    
    # Check for evidence support
    for relation in all_relations:
        if isinstance(relation, dict):
            rel_id = relation.get('relation_id')
            if not relation.get('evidence_files') and not relation.get('evidence'):
                issues.append(f"Relation {rel_id} missing evidence references")
                improvements.append({
                    'relation_id': rel_id,
                    'type': 'add_evidence_files',
                    'suggestion': 'Add supporting evidence files'
                })
            
            if not relation.get('ad_res_j7_references'):
                improvements.append({
                    'relation_id': rel_id,
                    'type': 'add_ad_res_j7_references',
                    'suggestion': 'Add cross-references to ad-res-j7 evidence'
                })
    
    return {
        'total_relations': len(all_relations),
        'relation_categories': list(relations_dict.keys()),
        'issues': issues,
        'improvements': improvements
    }

def analyze_timeline(timeline_data):
    """Analyze timeline for coherence and completeness"""
    issues = []
    improvements = []
    
    phases = timeline_data.get('phases', [])
    
    for phase in phases:
        phase_id = phase.get('phase_id')
        events = phase.get('events', [])
        
        if not events:
            issues.append(f"Phase {phase_id} has no events")
        
        # Check date ranges
        start_date = phase.get('start_date')
        end_date = phase.get('end_date')
        
        if not start_date or not end_date:
            issues.append(f"Phase {phase_id} missing date range")
    
    return {
        'total_phases': len(phases),
        'issues': issues,
        'improvements': improvements
    }

def cross_reference_with_ad_res_j7():
    """Cross-reference with ad-res-j7 evidence repository"""
    evidence_index_file = AD_RES_J7_ROOT / "COMPREHENSIVE_EVIDENCE_INDEX.json"
    
    if not evidence_index_file.exists():
        return {
            'status': 'evidence_index_not_found',
            'message': 'COMPREHENSIVE_EVIDENCE_INDEX.json not found in ad-res-j7'
        }
    
    evidence_index = load_json(evidence_index_file)
    
    # Extract key evidence categories
    evidence_summary = {
        'total_files': evidence_index.get('total_files', 0),
        'total_size': evidence_index.get('total_size', 0),
        'categories': evidence_index.get('categories', {}),
        'key_directories': [
            'ANNEXURES',
            'case_2025_137857',
            'FINAL_AFFIDAVIT_PACKAGE',
            'evidence'
        ]
    }
    
    return evidence_summary

def generate_refinement_recommendations():
    """Generate comprehensive refinement recommendations"""
    
    print("Loading data models...")
    entities = load_json(ENTITIES_FILE)
    events = load_json(EVENTS_FILE)
    relations = load_json(RELATIONS_FILE)
    timeline = load_json(TIMELINE_FILE)
    
    print("Analyzing entities...")
    entities_analysis = analyze_entities(entities)
    
    print("Analyzing events...")
    events_analysis = analyze_events(events)
    
    print("Analyzing relations...")
    relations_analysis = analyze_relations(relations)
    
    print("Analyzing timeline...")
    timeline_analysis = analyze_timeline(timeline)
    
    print("Cross-referencing with ad-res-j7...")
    ad_res_j7_summary = cross_reference_with_ad_res_j7()
    
    # Compile comprehensive report
    report = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'revstream_version': {
                'entities': entities.get('metadata', {}).get('version', 'unknown'),
                'events': events.get('metadata', {}).get('version', 'unknown'),
                'relations': relations.get('metadata', {}).get('version', 'unknown'),
                'timeline': timeline.get('metadata', {}).get('version', 'unknown')
            }
        },
        'entities_analysis': entities_analysis,
        'events_analysis': events_analysis,
        'relations_analysis': relations_analysis,
        'timeline_analysis': timeline_analysis,
        'ad_res_j7_cross_reference': ad_res_j7_summary,
        'overall_recommendations': []
    }
    
    # Generate overall recommendations
    total_issues = (
        len(entities_analysis['issues']) +
        len(events_analysis['issues']) +
        len(relations_analysis['issues']) +
        len(timeline_analysis['issues'])
    )
    
    if total_issues > 0:
        report['overall_recommendations'].append({
            'priority': 'high',
            'category': 'data_quality',
            'recommendation': f'Address {total_issues} identified data quality issues',
            'action': 'Review and fix all identified issues in entities, events, relations, and timeline'
        })
    
    # Evidence cross-referencing recommendation
    report['overall_recommendations'].append({
        'priority': 'high',
        'category': 'evidence_integration',
        'recommendation': 'Enhance cross-references to ad-res-j7 evidence repository',
        'action': 'Add ad_res_j7_references to all entities, events, and relations'
    })
    
    # Timeline coherence recommendation
    if events_analysis['events_without_phase']:
        report['overall_recommendations'].append({
            'priority': 'medium',
            'category': 'timeline_coherence',
            'recommendation': f'Classify {len(events_analysis["events_without_phase"])} events without phase',
            'action': 'Assign appropriate phase classifications to all events'
        })
    
    return report

def main():
    """Main execution"""
    print("=" * 80)
    print("COMPREHENSIVE REFINEMENT ANALYSIS")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("=" * 80)
    print()
    
    report = generate_refinement_recommendations()
    
    # Save report
    output_file = REVSTREAM_ROOT / "COMPREHENSIVE_REFINEMENT_REPORT_2025_11_28.json"
    save_json(report, output_file)
    
    print(f"\nReport saved to: {output_file}")
    print()
    print("SUMMARY:")
    print(f"  Entities: {report['entities_analysis']['total_persons']} persons, "
          f"{report['entities_analysis']['total_organizations']} organizations")
    print(f"  Events: {report['events_analysis']['total_events']}")
    print(f"  Relations: {report['relations_analysis']['total_relations']}")
    print(f"  Timeline Phases: {report['timeline_analysis']['total_phases']}")
    print()
    print(f"  Total Issues: {len(report['entities_analysis']['issues']) + len(report['events_analysis']['issues']) + len(report['relations_analysis']['issues']) + len(report['timeline_analysis']['issues'])}")
    print(f"  Recommendations: {len(report['overall_recommendations'])}")
    print()
    
    return report

if __name__ == "__main__":
    main()
