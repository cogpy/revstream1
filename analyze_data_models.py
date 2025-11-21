#!/usr/bin/env python3
"""
Comprehensive Data Model Analysis Script
Analyzes entities, relations, events, and timelines for consistency and improvements
"""

import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities for completeness and consistency"""
    issues = []
    stats = {
        'total_entities': 0,
        'persons': 0,
        'organizations': 0,
        'platforms': 0,
        'accounts': 0,
        'domains': 0,
        'missing_evidence': [],
        'missing_ad_res_references': [],
        'entities_without_events': []
    }
    
    for category, entities in entities_data.get('entities', {}).items():
        stats['total_entities'] += len(entities)
        if category == 'persons':
            stats['persons'] = len(entities)
        elif category == 'organizations':
            stats['organizations'] = len(entities)
        elif category == 'platforms':
            stats['platforms'] = len(entities)
        elif category == 'accounts':
            stats['accounts'] = len(entities)
        elif category == 'domains':
            stats['domains'] = len(entities)
        
        for entity in entities:
            entity_id = entity.get('entity_id', 'UNKNOWN')
            
            # Check for missing evidence files
            if not entity.get('evidence_files') or len(entity.get('evidence_files', [])) == 0:
                stats['missing_evidence'].append(entity_id)
            
            # Check for missing ad-res-j7 references
            if not entity.get('ad_res_j7_references') or len(entity.get('ad_res_j7_references', [])) == 0:
                stats['missing_ad_res_references'].append(entity_id)
            
            # Check for entities without timeline events
            if not entity.get('timeline_events') or len(entity.get('timeline_events', [])) == 0:
                if entity.get('agent_type') != 'neutral':
                    stats['entities_without_events'].append(entity_id)
    
    return stats, issues

def analyze_events(events_data):
    """Analyze events for completeness and consistency"""
    issues = []
    stats = {
        'total_events': events_data.get('metadata', {}).get('total_events', 0),
        'events_by_category': defaultdict(int),
        'events_by_phase': defaultdict(int),
        'events_with_financial_impact': 0,
        'missing_evidence': [],
        'missing_ad_res_files': [],
        'events_without_applications': []
    }
    
    for event in events_data.get('events', []):
        event_id = event.get('event_id', 'UNKNOWN')
        category = event.get('category', 'uncategorized')
        phase = event.get('timeline_phase', 'UNKNOWN')
        
        stats['events_by_category'][category] += 1
        stats['events_by_phase'][phase] += 1
        
        if event.get('financial_impact'):
            stats['events_with_financial_impact'] += 1
        
        # Check for missing evidence
        if not event.get('evidence') or len(event.get('evidence', [])) == 0:
            stats['missing_evidence'].append(event_id)
        
        # Check for missing evidence files
        if not event.get('evidence_files') or len(event.get('evidence_files', [])) == 0:
            stats['missing_ad_res_files'].append(event_id)
        
        # Check for events without application mapping
        if not event.get('related_applications') or len(event.get('related_applications', [])) == 0:
            stats['events_without_applications'].append(event_id)
    
    return stats, issues

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and consistency"""
    issues = []
    stats = {
        'total_phases': 0,
        'total_events': timeline_data.get('metadata', {}).get('total_events', 0),
        'phase_details': [],
        'orphaned_events': [],
        'duplicate_events': []
    }
    
    all_phase_events = set()
    event_counts = defaultdict(int)
    
    for phase_key, phase_data in timeline_data.get('timeline_phases', {}).items():
        stats['total_phases'] += 1
        phase_events = phase_data.get('events', [])
        
        stats['phase_details'].append({
            'phase_id': phase_data.get('phase_id'),
            'phase_name': phase_data.get('phase_name'),
            'event_count': len(phase_events),
            'duration_days': phase_data.get('duration_days', 0),
            'financial_impact': phase_data.get('financial_impact', 'Unknown')
        })
        
        for event_id in phase_events:
            all_phase_events.add(event_id)
            event_counts[event_id] += 1
    
    # Find duplicate events
    for event_id, count in event_counts.items():
        if count > 1:
            stats['duplicate_events'].append(f"{event_id} (appears {count} times)")
    
    return stats, issues

def analyze_relations(relations_data):
    """Analyze relations for completeness and consistency"""
    issues = []
    stats = {
        'total_relations': relations_data.get('metadata', {}).get('total_relations', 0),
        'relations_by_type': defaultdict(int),
        'missing_evidence': [],
        'missing_ad_res_references': []
    }
    
    for relation_type, relations in relations_data.get('relations', {}).items():
        for relation in relations:
            relation_id = relation.get('relation_id', 'UNKNOWN')
            stats['relations_by_type'][relation_type] += 1
            
            # Check for missing evidence
            if not relation.get('evidence') or len(relation.get('evidence', [])) == 0:
                stats['missing_evidence'].append(relation_id)
            
            # Check for missing ad-res-j7 references
            if not relation.get('evidence_repository'):
                stats['missing_ad_res_references'].append(relation_id)
    
    return stats, issues

def generate_improvements(all_stats):
    """Generate improvement recommendations based on analysis"""
    improvements = {
        'critical': [],
        'important': [],
        'minor': []
    }
    
    # Critical improvements
    if all_stats['entities']['entities_without_events']:
        improvements['critical'].append({
            'area': 'Entities',
            'issue': f"{len(all_stats['entities']['entities_without_events'])} entities have no timeline events",
            'recommendation': 'Map entities to relevant events or mark as inactive',
            'affected_entities': all_stats['entities']['entities_without_events']
        })
    
    if all_stats['events']['events_without_applications']:
        improvements['critical'].append({
            'area': 'Events',
            'issue': f"{len(all_stats['events']['events_without_applications'])} events not mapped to applications",
            'recommendation': 'Map all events to at least one application (APPLICATION_1, APPLICATION_2, or APPLICATION_3)',
            'affected_events': all_stats['events']['events_without_applications'][:10]  # Show first 10
        })
    
    if all_stats['timeline']['duplicate_events']:
        improvements['critical'].append({
            'area': 'Timeline',
            'issue': f"{len(all_stats['timeline']['duplicate_events'])} events appear in multiple phases",
            'recommendation': 'Ensure each event appears in only one timeline phase',
            'duplicates': all_stats['timeline']['duplicate_events']
        })
    
    # Important improvements
    if all_stats['entities']['missing_ad_res_references']:
        improvements['important'].append({
            'area': 'Entities',
            'issue': f"{len(all_stats['entities']['missing_ad_res_references'])} entities missing ad-res-j7 references",
            'recommendation': 'Add ad_res_j7_references array with specific evidence descriptions',
            'affected_entities': all_stats['entities']['missing_ad_res_references'][:10]
        })
    
    if all_stats['events']['missing_ad_res_files']:
        improvements['important'].append({
            'area': 'Events',
            'issue': f"{len(all_stats['events']['missing_ad_res_files'])} events missing evidence_files from ad-res-j7",
            'recommendation': 'Add evidence_files array with specific file paths from ad-res-j7 repository',
            'affected_events': all_stats['events']['missing_ad_res_files'][:10]
        })
    
    # Minor improvements
    if all_stats['entities']['missing_evidence']:
        improvements['minor'].append({
            'area': 'Entities',
            'issue': f"{len(all_stats['entities']['missing_evidence'])} entities missing evidence_files",
            'recommendation': 'Add evidence_files array for better traceability',
            'affected_entities': all_stats['entities']['missing_evidence'][:10]
        })
    
    return improvements

def main():
    """Main analysis function"""
    base_dir = '/home/ubuntu/revstream1/data_models'
    
    # Load latest data models
    entities_file = os.path.join(base_dir, 'entities/entities_refined_2025_11_20_v7.json')
    events_file = os.path.join(base_dir, 'events/events_refined_2025_11_20_v8.json')
    timeline_file = os.path.join(base_dir, 'timelines/timeline_refined_2025_11_20_v6.json')
    relations_file = os.path.join(base_dir, 'relations/relations_refined_2025_11_20_v5.json')
    
    print("Loading data models...")
    entities_data = load_json(entities_file)
    events_data = load_json(events_file)
    timeline_data = load_json(timeline_file)
    relations_data = load_json(relations_file)
    
    print("Analyzing entities...")
    entities_stats, entities_issues = analyze_entities(entities_data)
    
    print("Analyzing events...")
    events_stats, events_issues = analyze_events(events_data)
    
    print("Analyzing timeline...")
    timeline_stats, timeline_issues = analyze_timeline(timeline_data)
    
    print("Analyzing relations...")
    relations_stats, relations_issues = analyze_relations(relations_data)
    
    all_stats = {
        'entities': entities_stats,
        'events': events_stats,
        'timeline': timeline_stats,
        'relations': relations_stats
    }
    
    print("Generating improvements...")
    improvements = generate_improvements(all_stats)
    
    # Create comprehensive report
    report = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'case_number': '2025-137857',
            'data_model_version': entities_data.get('metadata', {}).get('version', 'Unknown')
        },
        'statistics': all_stats,
        'improvements': improvements,
        'summary': {
            'total_entities': entities_stats['total_entities'],
            'total_events': events_stats['total_events'],
            'total_phases': timeline_stats['total_phases'],
            'total_relations': relations_stats['total_relations'],
            'critical_issues': len(improvements['critical']),
            'important_issues': len(improvements['important']),
            'minor_issues': len(improvements['minor'])
        }
    }
    
    # Save report
    output_file = '/home/ubuntu/revstream1/DATA_MODEL_ANALYSIS_2025_11_21.json'
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nAnalysis complete! Report saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total Entities: {entities_stats['total_entities']}")
    print(f"  Total Events: {events_stats['total_events']}")
    print(f"  Total Phases: {timeline_stats['total_phases']}")
    print(f"  Total Relations: {relations_stats['total_relations']}")
    print(f"\nIssues Found:")
    print(f"  Critical: {len(improvements['critical'])}")
    print(f"  Important: {len(improvements['important'])}")
    print(f"  Minor: {len(improvements['minor'])}")

if __name__ == '__main__':
    main()
