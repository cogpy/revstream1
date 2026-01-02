#!/usr/bin/env python3.11
"""
Comprehensive analysis script to identify improvements for revstream1 repository
"""
import json
import os
from datetime import datetime
from pathlib import Path

def analyze_entities(entities_path):
    """Analyze entities for completeness and evidence strength"""
    with open(entities_path, 'r') as f:
        data = json.load(f)
    
    entities = data.get('entities', {})
    issues = []
    recommendations = []
    
    # Check each entity category
    for category, items in entities.items():
        if not isinstance(items, list):
            continue
            
        for entity in items:
            entity_id = entity.get('entity_id', 'UNKNOWN')
            
            # Check for evidence
            if not entity.get('evidence') and not entity.get('ad_res_j7_references'):
                issues.append(f"{entity_id}: Missing evidence references")
                recommendations.append(f"Add evidence for {entity_id} from ad-res-j7")
            
            # Check evidence strength
            if not entity.get('evidence_strength'):
                issues.append(f"{entity_id}: Missing evidence strength assessment")
                recommendations.append(f"Assess evidence strength for {entity_id}")
            
            # Check for timeline events
            if entity.get('agent_type') == 'antagonist' and not entity.get('timeline_events'):
                issues.append(f"{entity_id}: Antagonist missing timeline events")
                recommendations.append(f"Link {entity_id} to relevant timeline events")
    
    return {
        'total_entities': data['metadata']['total_entities'],
        'issues': issues,
        'recommendations': recommendations
    }

def analyze_relations(relations_path):
    """Analyze relations for completeness and evidence"""
    with open(relations_path, 'r') as f:
        data = json.load(f)
    
    relations = data.get('relations', {})
    issues = []
    recommendations = []
    total_relations = 0
    
    for category, items in relations.items():
        if not isinstance(items, list):
            continue
        total_relations += len(items)
        
        for relation in items:
            rel_id = relation.get('relation_id', 'UNKNOWN')
            
            # Check for evidence
            if not relation.get('evidence') and not relation.get('ad_res_j7_evidence'):
                issues.append(f"{rel_id}: Missing evidence")
                recommendations.append(f"Add evidence for {rel_id}")
            
            # Check confidence score
            if 'confidence' not in relation:
                issues.append(f"{rel_id}: Missing confidence score")
                recommendations.append(f"Add confidence score for {rel_id}")
    
    return {
        'total_relations': total_relations,
        'issues': issues,
        'recommendations': recommendations
    }

def analyze_events(events_path):
    """Analyze events for evidence and burden of proof"""
    with open(events_path, 'r') as f:
        data = json.load(f)
    
    events = data.get('events', [])
    issues = []
    recommendations = []
    
    criminal_events = []
    civil_exceeded_events = []
    
    for event in events:
        event_id = event.get('event_id', 'UNKNOWN')
        burden = event.get('burden_of_proof', '')
        
        # Track burden of proof
        if 'criminal' in burden.lower() or '95%' in burden:
            criminal_events.append(event_id)
        elif 'exceeded' in burden.lower():
            civil_exceeded_events.append(event_id)
        
        # Check for evidence
        if not event.get('evidence') and not event.get('ad_res_j7_references'):
            issues.append(f"{event_id}: Missing evidence")
            recommendations.append(f"Add evidence for {event_id}")
        
        # Check for phase classification
        if not event.get('phase'):
            issues.append(f"{event_id}: Missing phase classification")
            recommendations.append(f"Classify {event_id} into appropriate phase")
        
        # Check for perpetrators/victims
        if not event.get('perpetrators') and not event.get('victims'):
            issues.append(f"{event_id}: Missing perpetrators/victims")
            recommendations.append(f"Identify perpetrators/victims for {event_id}")
    
    return {
        'total_events': len(events),
        'criminal_threshold': len(criminal_events),
        'civil_exceeded': len(civil_exceeded_events),
        'issues': issues,
        'recommendations': recommendations
    }

def main():
    base_path = Path('/home/ubuntu/revstream1')
    
    # Analyze data models
    entities_analysis = analyze_entities(base_path / 'data_models/entities/entities.json')
    relations_analysis = analyze_relations(base_path / 'data_models/relations/relations.json')
    events_analysis = analyze_events(base_path / 'data_models/events/events.json')
    
    # Compile report
    report = {
        'analysis_date': datetime.now().isoformat(),
        'entities': entities_analysis,
        'relations': relations_analysis,
        'events': events_analysis,
        'summary': {
            'total_issues': len(entities_analysis['issues']) + len(relations_analysis['issues']) + len(events_analysis['issues']),
            'total_recommendations': len(entities_analysis['recommendations']) + len(relations_analysis['recommendations']) + len(events_analysis['recommendations'])
        }
    }
    
    # Save report
    output_path = base_path / f'ANALYSIS_IMPROVEMENTS_{datetime.now().strftime("%Y_%m_%d")}.json'
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Analysis complete. Report saved to: {output_path}")
    print(f"\nSummary:")
    print(f"  Entities: {entities_analysis['total_entities']}")
    print(f"  Relations: {relations_analysis['total_relations']}")
    print(f"  Events: {events_analysis['total_events']}")
    print(f"  Criminal Threshold Events: {events_analysis['criminal_threshold']}")
    print(f"  Civil Exceeded Events: {events_analysis['civil_exceeded']}")
    print(f"  Total Issues: {report['summary']['total_issues']}")
    print(f"  Total Recommendations: {report['summary']['total_recommendations']}")

if __name__ == '__main__':
    main()
