#!/usr/bin/env python3
"""
Comprehensive analysis of current revstream1 state
Identifies gaps, inconsistencies, and improvement opportunities
"""
import json
import os
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_entities(entities_data):
    """Analyze entities for completeness and evidence strength"""
    issues = []
    stats = {
        'total': 0,
        'with_ad_res_j7': 0,
        'evidence_strength': {},
        'missing_evidence': []
    }
    
    if not entities_data or 'entities' not in entities_data:
        return stats, ["Could not load entities data"]
    
    for category, entities_list in entities_data['entities'].items():
        if not isinstance(entities_list, list):
            continue
            
        for entity in entities_list:
            stats['total'] += 1
            entity_id = entity.get('entity_id', 'UNKNOWN')
            
            # Check for ad-res-j7 references
            if 'ad_res_j7_references' in entity and entity['ad_res_j7_references']:
                stats['with_ad_res_j7'] += 1
            else:
                issues.append(f"{entity_id}: Missing ad-res-j7 references")
            
            # Check evidence strength
            strength = entity.get('evidence_strength', 'unknown')
            stats['evidence_strength'][strength] = stats['evidence_strength'].get(strength, 0) + 1
            
            # Check for evidence array
            if not entity.get('evidence') or len(entity.get('evidence', [])) == 0:
                stats['missing_evidence'].append(entity_id)
    
    return stats, issues

def analyze_timeline(timeline_data):
    """Analyze timeline for gaps and evidence coverage"""
    issues = []
    stats = {
        'total_events': 0,
        'events_with_evidence': 0,
        'events_with_ad_res_j7': 0,
        'criminal_threshold_events': 0,
        'date_gaps': []
    }
    
    if not timeline_data or 'timeline' not in timeline_data:
        return stats, ["Could not load timeline data"]
    
    timeline = timeline_data['timeline']
    stats['total_events'] = len(timeline)
    
    prev_date = None
    for entry in timeline:
        date = entry.get('date')
        
        # Check evidence
        if entry.get('evidence_references') and len(entry.get('evidence_references', [])) > 0:
            stats['events_with_evidence'] += 1
        
        if entry.get('evidence') and len(entry.get('evidence', [])) > 0:
            stats['events_with_ad_res_j7'] += 1
        else:
            issues.append(f"{date}: Missing ad-res-j7 evidence references")
        
        # Check criminal threshold
        if entry.get('criminal_threshold') == 'yes':
            stats['criminal_threshold_events'] += 1
        
        # Check for large date gaps (>90 days)
        if prev_date and date:
            from datetime import datetime
            try:
                d1 = datetime.strptime(prev_date, '%Y-%m-%d')
                d2 = datetime.strptime(date, '%Y-%m-%d')
                gap = (d2 - d1).days
                if gap > 90:
                    stats['date_gaps'].append(f"{prev_date} to {date}: {gap} days")
            except:
                pass
        prev_date = date
    
    return stats, issues

def analyze_events(events_data):
    """Analyze events for completeness"""
    issues = []
    stats = {
        'total': 0,
        'with_ad_res_j7': 0,
        'by_phase': {},
        'burden_of_proof': {}
    }
    
    if not events_data or 'events' not in events_data:
        return stats, ["Could not load events data"]
    
    for event in events_data['events']:
        stats['total'] += 1
        event_id = event.get('event_id', 'UNKNOWN')
        
        # Check ad-res-j7 references
        if 'ad_res_j7_references' in event and event['ad_res_j7_references']:
            stats['with_ad_res_j7'] += 1
        else:
            issues.append(f"{event_id}: Missing ad-res-j7 references")
        
        # Phase distribution
        phase = event.get('phase', 'UNKNOWN')
        stats['by_phase'][phase] = stats['by_phase'].get(phase, 0) + 1
        
        # Burden of proof
        burden = event.get('burden_of_proof', 'not_specified')
        stats['burden_of_proof'][burden] = stats['burden_of_proof'].get(burden, 0) + 1
    
    return stats, issues

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    issues = []
    stats = {
        'total': 0,
        'with_ad_res_j7': 0,
        'by_type': {},
        'evidence_strength': {}
    }
    
    if not relations_data or 'relations' not in relations_data:
        return stats, ["Could not load relations data"]
    
    for rel_type, relations_list in relations_data['relations'].items():
        if not isinstance(relations_list, list):
            continue
            
        for relation in relations_list:
            stats['total'] += 1
            rel_id = relation.get('relation_id', 'UNKNOWN')
            
            # Check ad-res-j7 evidence
            if 'ad_res_j7_evidence' in relation and relation['ad_res_j7_evidence']:
                stats['with_ad_res_j7'] += 1
            else:
                issues.append(f"{rel_id}: Missing ad-res-j7 evidence")
            
            # Type distribution
            r_type = relation.get('relation_type', 'unknown')
            stats['by_type'][r_type] = stats['by_type'].get(r_type, 0) + 1
            
            # Evidence strength
            strength = relation.get('evidence_strength', 'unknown')
            stats['evidence_strength'][strength] = stats['evidence_strength'].get(strength, 0) + 1
    
    return stats, issues

def main():
    base_path = Path('/home/ubuntu/revstream1/docs/data_models')
    
    # Load data
    entities_data = load_json(base_path / 'entities/entities.json')
    timeline_data = load_json(base_path / 'timeline.json')
    events_data = load_json(base_path / 'events.json')
    relations_data = load_json(base_path / 'relations.json')
    
    # Analyze each component
    print("=" * 80)
    print("REVSTREAM1 CURRENT STATE ANALYSIS")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 80)
    
    print("\n### ENTITIES ANALYSIS ###")
    entity_stats, entity_issues = analyze_entities(entities_data)
    print(f"Total entities: {entity_stats['total']}")
    print(f"With ad-res-j7 references: {entity_stats['with_ad_res_j7']} ({entity_stats['with_ad_res_j7']/max(entity_stats['total'],1)*100:.1f}%)")
    print(f"Evidence strength distribution: {entity_stats['evidence_strength']}")
    print(f"Missing evidence: {len(entity_stats['missing_evidence'])} entities")
    if entity_issues[:5]:
        print(f"\nTop issues (showing 5/{len(entity_issues)}):")
        for issue in entity_issues[:5]:
            print(f"  - {issue}")
    
    print("\n### TIMELINE ANALYSIS ###")
    timeline_stats, timeline_issues = analyze_timeline(timeline_data)
    print(f"Total timeline entries: {timeline_stats['total_events']}")
    print(f"With evidence references: {timeline_stats['events_with_evidence']} ({timeline_stats['events_with_evidence']/max(timeline_stats['total_events'],1)*100:.1f}%)")
    print(f"With ad-res-j7 evidence: {timeline_stats['events_with_ad_res_j7']} ({timeline_stats['events_with_ad_res_j7']/max(timeline_stats['total_events'],1)*100:.1f}%)")
    print(f"Criminal threshold events: {timeline_stats['criminal_threshold_events']}")
    print(f"Date gaps >90 days: {len(timeline_stats['date_gaps'])}")
    if timeline_issues[:5]:
        print(f"\nTop issues (showing 5/{len(timeline_issues)}):")
        for issue in timeline_issues[:5]:
            print(f"  - {issue}")
    
    print("\n### EVENTS ANALYSIS ###")
    event_stats, event_issues = analyze_events(events_data)
    print(f"Total events: {event_stats['total']}")
    print(f"With ad-res-j7 references: {event_stats['with_ad_res_j7']} ({event_stats['with_ad_res_j7']/max(event_stats['total'],1)*100:.1f}%)")
    print(f"Phase distribution: {event_stats['by_phase']}")
    print(f"Burden of proof distribution: {event_stats['burden_of_proof']}")
    if event_issues[:5]:
        print(f"\nTop issues (showing 5/{len(event_issues)}):")
        for issue in event_issues[:5]:
            print(f"  - {issue}")
    
    print("\n### RELATIONS ANALYSIS ###")
    relation_stats, relation_issues = analyze_relations(relations_data)
    print(f"Total relations: {relation_stats['total']}")
    print(f"With ad-res-j7 evidence: {relation_stats['with_ad_res_j7']} ({relation_stats['with_ad_res_j7']/max(relation_stats['total'],1)*100:.1f}%)")
    print(f"Type distribution: {relation_stats['by_type']}")
    print(f"Evidence strength: {relation_stats['evidence_strength']}")
    if relation_issues[:5]:
        print(f"\nTop issues (showing 5/{len(relation_issues)}):")
        for issue in relation_issues[:5]:
            print(f"  - {issue}")
    
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    recommendations = []
    
    # Evidence coverage
    entity_coverage = entity_stats['with_ad_res_j7'] / max(entity_stats['total'], 1) * 100
    if entity_coverage < 90:
        recommendations.append(f"1. Improve entity evidence coverage: Currently {entity_coverage:.1f}%, target 95%+")
    
    timeline_coverage = timeline_stats['events_with_ad_res_j7'] / max(timeline_stats['total_events'], 1) * 100
    if timeline_coverage < 90:
        recommendations.append(f"2. Enhance timeline evidence: Currently {timeline_coverage:.1f}%, target 95%+")
    
    event_coverage = event_stats['with_ad_res_j7'] / max(event_stats['total'], 1) * 100
    if event_coverage < 90:
        recommendations.append(f"3. Add event evidence references: Currently {event_coverage:.1f}%, target 95%+")
    
    relation_coverage = relation_stats['with_ad_res_j7'] / max(relation_stats['total'], 1) * 100
    if relation_coverage < 90:
        recommendations.append(f"4. Strengthen relation evidence: Currently {relation_coverage:.1f}%, target 95%+")
    
    # Burden of proof
    if 'not_specified' in event_stats['burden_of_proof']:
        recommendations.append(f"5. Specify burden of proof for {event_stats['burden_of_proof']['not_specified']} events")
    
    # Criminal threshold
    if timeline_stats['criminal_threshold_events'] < 10:
        recommendations.append(f"6. Review and mark additional criminal threshold events (currently {timeline_stats['criminal_threshold_events']})")
    
    for rec in recommendations:
        print(f"\n{rec}")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
