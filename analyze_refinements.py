#!/usr/bin/env python3
"""
Comprehensive analysis script to identify refinement opportunities for:
- Entities
- Relations
- Events
- Timelines
- Legal filings
Based on evidence from ad-res-j7 repository
"""

import json
import os
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_path):
    """Analyze entities for refinement opportunities"""
    entities = load_json(entities_path)
    
    refinements = {
        "missing_evidence_refs": [],
        "weak_evidence_strength": [],
        "missing_criminal_threshold": [],
        "incomplete_ad_res_j7_refs": []
    }
    
    for person in entities.get('entities', {}).get('persons', []):
        entity_id = person.get('entity_id')
        
        # Check for weak evidence
        if person.get('evidence_strength') in ['moderate', 'weak', None]:
            refinements['weak_evidence_strength'].append({
                'entity_id': entity_id,
                'name': person.get('name'),
                'current_strength': person.get('evidence_strength')
            })
        
        # Check for missing criminal threshold
        if person.get('role') in ['primary_perpetrator', 'co_conspirator']:
            if not person.get('criminal_threshold'):
                refinements['missing_criminal_threshold'].append({
                    'entity_id': entity_id,
                    'name': person.get('name'),
                    'role': person.get('role')
                })
        
        # Check for incomplete ad-res-j7 references
        ad_refs = person.get('ad_res_j7_references', [])
        if len(ad_refs) < 3:
            refinements['incomplete_ad_res_j7_refs'].append({
                'entity_id': entity_id,
                'name': person.get('name'),
                'current_refs': len(ad_refs)
            })
    
    return refinements

def analyze_relations(relations_path):
    """Analyze relations for refinement opportunities"""
    relations = load_json(relations_path)
    
    refinements = {
        "weak_confidence": [],
        "missing_evidence": [],
        "incomplete_ad_res_j7_refs": []
    }
    
    for rel_type, rel_list in relations.get('relations', {}).items():
        for rel in rel_list:
            rel_id = rel.get('relation_id')
            
            # Check for weak confidence
            confidence = rel.get('confidence', 0)
            if confidence < 0.75:
                refinements['weak_confidence'].append({
                    'relation_id': rel_id,
                    'type': rel.get('relation_type'),
                    'confidence': confidence
                })
            
            # Check for missing evidence
            evidence = rel.get('evidence', [])
            if len(evidence) < 2:
                refinements['missing_evidence'].append({
                    'relation_id': rel_id,
                    'type': rel.get('relation_type'),
                    'evidence_count': len(evidence)
                })
            
            # Check for incomplete ad-res-j7 references
            ad_refs = rel.get('ad_res_j7_evidence', [])
            if len(ad_refs) < 2:
                refinements['incomplete_ad_res_j7_refs'].append({
                    'relation_id': rel_id,
                    'type': rel.get('relation_type'),
                    'current_refs': len(ad_refs)
                })
    
    return refinements

def analyze_events(events_path):
    """Analyze events for refinement opportunities"""
    events = load_json(events_path)
    
    refinements = {
        "missing_burden_of_proof": [],
        "weak_evidence": [],
        "missing_financial_impact": [],
        "incomplete_ad_res_j7_refs": []
    }
    
    for event in events.get('events', []):
        event_id = event.get('event_id')
        
        # Check for missing burden of proof
        if not event.get('burden_of_proof'):
            refinements['missing_burden_of_proof'].append({
                'event_id': event_id,
                'date': event.get('date'),
                'description': event.get('description', '')[:80]
            })
        
        # Check for weak evidence
        evidence = event.get('evidence', [])
        if len(evidence) < 2:
            refinements['weak_evidence'].append({
                'event_id': event_id,
                'date': event.get('date'),
                'evidence_count': len(evidence)
            })
        
        # Check for missing financial impact on significant events
        if event.get('category') in ['fraud', 'theft', 'unauthorized_transfer']:
            if not event.get('financial_impact') or event.get('financial_impact') == 0:
                refinements['missing_financial_impact'].append({
                    'event_id': event_id,
                    'date': event.get('date'),
                    'category': event.get('category')
                })
        
        # Check for incomplete ad-res-j7 references
        ad_refs = event.get('ad_res_j7_references', [])
        if len(ad_refs) < 2:
            refinements['incomplete_ad_res_j7_refs'].append({
                'event_id': event_id,
                'date': event.get('date'),
                'current_refs': len(ad_refs)
            })
    
    return refinements

def analyze_timeline(timeline_path):
    """Analyze timeline for refinement opportunities"""
    timeline = load_json(timeline_path)
    
    refinements = {
        "missing_key_actors": [],
        "missing_cumulative_impact": [],
        "weak_evidence_refs": []
    }
    
    for entry in timeline.get('timeline', []):
        date = entry.get('date')
        
        # Check for missing key actors
        if not entry.get('key_actors') or len(entry.get('key_actors', [])) == 0:
            refinements['missing_key_actors'].append({
                'date': date,
                'events': entry.get('events', [])
            })
        
        # Check for missing cumulative impact
        if entry.get('financial_impact') and not entry.get('cumulative_financial_impact'):
            refinements['missing_cumulative_impact'].append({
                'date': date,
                'financial_impact': entry.get('financial_impact')
            })
        
        # Check for weak evidence references
        evidence_refs = entry.get('evidence_references', [])
        if len(evidence_refs) < 2:
            refinements['weak_evidence_refs'].append({
                'date': date,
                'evidence_count': len(evidence_refs)
            })
    
    return refinements

def main():
    """Main analysis function"""
    base_path = Path('/home/ubuntu/revstream1')
    
    print("=" * 80)
    print("COMPREHENSIVE REFINEMENT ANALYSIS")
    print("=" * 80)
    print()
    
    # Analyze entities
    print("1. ENTITIES ANALYSIS")
    print("-" * 80)
    entities_path = base_path / 'data_models' / 'entities' / 'entities.json'
    entity_refinements = analyze_entities(entities_path)
    
    print(f"Weak evidence strength: {len(entity_refinements['weak_evidence_strength'])} entities")
    print(f"Missing criminal threshold: {len(entity_refinements['missing_criminal_threshold'])} entities")
    print(f"Incomplete ad-res-j7 refs: {len(entity_refinements['incomplete_ad_res_j7_refs'])} entities")
    print()
    
    # Analyze relations
    print("2. RELATIONS ANALYSIS")
    print("-" * 80)
    relations_path = base_path / 'data_models' / 'relations' / 'relations.json'
    relation_refinements = analyze_relations(relations_path)
    
    print(f"Weak confidence: {len(relation_refinements['weak_confidence'])} relations")
    print(f"Missing evidence: {len(relation_refinements['missing_evidence'])} relations")
    print(f"Incomplete ad-res-j7 refs: {len(relation_refinements['incomplete_ad_res_j7_refs'])} relations")
    print()
    
    # Analyze events
    print("3. EVENTS ANALYSIS")
    print("-" * 80)
    events_path = base_path / 'data_models' / 'events' / 'events.json'
    event_refinements = analyze_events(events_path)
    
    print(f"Missing burden of proof: {len(event_refinements['missing_burden_of_proof'])} events")
    print(f"Weak evidence: {len(event_refinements['weak_evidence'])} events")
    print(f"Missing financial impact: {len(event_refinements['missing_financial_impact'])} events")
    print(f"Incomplete ad-res-j7 refs: {len(event_refinements['incomplete_ad_res_j7_refs'])} events")
    print()
    
    # Analyze timeline
    print("4. TIMELINE ANALYSIS")
    print("-" * 80)
    timeline_path = base_path / 'data_models' / 'timelines' / 'timeline.json'
    timeline_refinements = analyze_timeline(timeline_path)
    
    print(f"Missing key actors: {len(timeline_refinements['missing_key_actors'])} entries")
    print(f"Missing cumulative impact: {len(timeline_refinements['missing_cumulative_impact'])} entries")
    print(f"Weak evidence refs: {len(timeline_refinements['weak_evidence_refs'])} entries")
    print()
    
    # Save detailed report
    report = {
        'timestamp': datetime.now().isoformat(),
        'entities': entity_refinements,
        'relations': relation_refinements,
        'events': event_refinements,
        'timeline': timeline_refinements
    }
    
    report_path = base_path / 'REFINEMENT_ANALYSIS_2026_01_09.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Detailed report saved to: {report_path}")
    print()
    print("=" * 80)

if __name__ == '__main__':
    main()
