#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script - 2025-11-27
Analyzes entities, relations, events, and timelines for improvements
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
    """Analyze entities for completeness and improvements"""
    issues = []
    improvements = []
    
    total_entities = entities_data['metadata']['total_entities']
    entities = entities_data['entities']
    
    # Check each entity type
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            entity_id = entity.get('entity_id', 'UNKNOWN')
            
            # Check for missing evidence references
            if 'evidence_files' not in entity or not entity['evidence_files']:
                issues.append(f"{entity_id}: Missing evidence_files")
            
            # Check for missing ad_res_j7_references
            if 'ad_res_j7_references' not in entity or not entity['ad_res_j7_references']:
                issues.append(f"{entity_id}: Missing ad_res_j7_references")
            
            # Check for timeline_events
            if 'timeline_events' not in entity or not entity['timeline_events']:
                issues.append(f"{entity_id}: Missing timeline_events")
            
            # Check for financial impact where relevant
            if entity_type in ['persons', 'companies'] and 'financial_impact' not in entity:
                improvements.append(f"{entity_id}: Could add financial_impact analysis")
    
    return {
        'total_entities': total_entities,
        'entity_types': len(entities),
        'issues': issues,
        'improvements': improvements
    }

def analyze_events(events_data):
    """Analyze events for completeness and improvements"""
    issues = []
    improvements = []
    
    events = events_data.get('events', [])
    
    # Group events by phase
    phase_distribution = defaultdict(int)
    events_with_evidence = 0
    events_with_financial = 0
    
    for event in events:
        event_id = event.get('event_id', 'UNKNOWN')
        
        # Track phase distribution
        phase = event.get('phase', 'unknown')
        phase_distribution[phase] += 1
        
        # Check for evidence
        if 'evidence' in event and event['evidence']:
            events_with_evidence += 1
        else:
            issues.append(f"{event_id}: Missing evidence references")
        
        # Check for financial impact
        if 'financial_impact' in event and event['financial_impact']:
            events_with_financial += 1
        
        # Check for ad_res_j7_evidence
        if 'ad_res_j7_evidence' not in event or not event['ad_res_j7_evidence']:
            improvements.append(f"{event_id}: Could add ad_res_j7_evidence links")
    
    return {
        'total_events': len(events),
        'phase_distribution': dict(phase_distribution),
        'events_with_evidence': events_with_evidence,
        'events_with_financial': events_with_financial,
        'issues': issues,
        'improvements': improvements
    }

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    issues = []
    improvements = []
    
    relations = relations_data.get('relations', {})
    
    # Group by relation type
    type_distribution = defaultdict(int)
    relations_with_evidence = 0
    total_relations = 0
    
    # Relations are organized by category
    for category, relation_list in relations.items():
        if isinstance(relation_list, list):
            for relation in relation_list:
                total_relations += 1
                rel_id = relation.get('relation_id', 'UNKNOWN')
                rel_type = relation.get('relation_type', 'unknown')
                
                type_distribution[rel_type] += 1
                
                # Check for evidence
                if 'evidence' in relation and relation['evidence']:
                    relations_with_evidence += 1
                else:
                    issues.append(f"{rel_id}: Missing evidence references")
                
                # Check for ad_res_j7_evidence
                if 'ad_res_j7_evidence' not in relation:
                    improvements.append(f"{rel_id}: Could add ad_res_j7_evidence links")
    
    return {
        'total_relations': total_relations,
        'type_distribution': dict(type_distribution),
        'relations_with_evidence': relations_with_evidence,
        'issues': issues,
        'improvements': improvements
    }

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness"""
    issues = []
    improvements = []
    
    phases = timeline_data.get('phases', [])
    
    total_events = 0
    phases_with_evidence = 0
    
    for phase in phases:
        phase_id = phase.get('phase_id', 'UNKNOWN')
        events = phase.get('events', [])
        total_events += len(events)
        
        # Check for evidence links
        if 'evidence_summary' in phase and phase['evidence_summary']:
            phases_with_evidence += 1
        else:
            improvements.append(f"{phase_id}: Could add evidence_summary")
        
        # Check for ad_res_j7_links
        if 'ad_res_j7_links' not in phase:
            improvements.append(f"{phase_id}: Could add ad_res_j7_links")
    
    return {
        'total_phases': len(phases),
        'total_events_in_timeline': total_events,
        'phases_with_evidence': phases_with_evidence,
        'issues': issues,
        'improvements': improvements
    }

def main():
    """Main analysis function"""
    base_dir = '/home/ubuntu/revstream1/data_models'
    
    # Load latest data models
    entities_file = f'{base_dir}/entities/entities_refined_2025_11_26_v21.json'
    events_file = f'{base_dir}/events/events_refined_2025_11_26_v22.json'
    relations_file = f'{base_dir}/relations/relations_refined_2025_11_26_v18.json'
    timeline_file = f'{base_dir}/timelines/timeline_refined_2025_11_26_v11.json'
    
    print("Loading data models...")
    entities_data = load_json(entities_file)
    events_data = load_json(events_file)
    relations_data = load_json(relations_file)
    timeline_data = load_json(timeline_file)
    
    print("\nAnalyzing entities...")
    entities_analysis = analyze_entities(entities_data)
    
    print("Analyzing events...")
    events_analysis = analyze_events(events_data)
    
    print("Analyzing relations...")
    relations_analysis = analyze_relations(relations_data)
    
    print("Analyzing timeline...")
    timeline_analysis = analyze_timeline(timeline_data)
    
    # Compile comprehensive report
    report = {
        'analysis_date': datetime.now().isoformat(),
        'entities': entities_analysis,
        'events': events_analysis,
        'relations': relations_analysis,
        'timeline': timeline_analysis,
        'summary': {
            'total_issues': (
                len(entities_analysis['issues']) +
                len(events_analysis['issues']) +
                len(relations_analysis['issues']) +
                len(timeline_analysis['issues'])
            ),
            'total_improvements': (
                len(entities_analysis['improvements']) +
                len(events_analysis['improvements']) +
                len(relations_analysis['improvements']) +
                len(timeline_analysis['improvements'])
            )
        }
    }
    
    # Save report
    output_file = '/home/ubuntu/revstream1/ANALYSIS_REPORT_2025_11_27.json'
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✓ Analysis complete. Report saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total Issues: {report['summary']['total_issues']}")
    print(f"  Total Improvements: {report['summary']['total_improvements']}")
    
    return report

if __name__ == '__main__':
    main()
