#!/usr/bin/env python3
"""
Analyze evidence quality and map to burden of proof standards
Civil: 50% (balance of probabilities)
Criminal: 95% (beyond reasonable doubt)
"""
import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def assess_evidence_strength(entity):
    """Assess evidence strength for an entity"""
    score = 0
    factors = []
    
    # Check for evidence references
    evidence = entity.get('evidence', [])
    ad_res_j7 = entity.get('ad_res_j7_references', []) or entity.get('ad_res_j7_evidence_enhanced', [])
    
    if len(evidence) > 0:
        score += 20
        factors.append(f"Has {len(evidence)} evidence references")
    
    if len(ad_res_j7) > 0:
        score += 20
        factors.append(f"Has {len(ad_res_j7)} ad-res-j7 references")
    
    # Check for documented evidence strength
    evidence_strength = entity.get('evidence_strength', '')
    if evidence_strength == 'conclusive':
        score += 40
        factors.append("Marked as conclusive evidence")
    elif evidence_strength == 'strong':
        score += 30
        factors.append("Marked as strong evidence")
    elif evidence_strength == 'moderate':
        score += 20
        factors.append("Marked as moderate evidence")
    elif evidence_strength == 'weak':
        score += 10
        factors.append("Marked as weak evidence")
    
    # Check for criminal threshold
    if entity.get('criminal_threshold') or entity.get('criminal_threshold_exceeded'):
        score += 20
        factors.append("Criminal threshold marked")
    
    return min(score, 100), factors

def analyze_burden_of_proof(entities_data, events_data):
    """Analyze evidence against burden of proof standards"""
    
    civil_threshold = 50  # Balance of probabilities
    criminal_threshold = 95  # Beyond reasonable doubt
    
    results = {
        'civil_standard': {
            'threshold': civil_threshold,
            'entities_exceeding': [],
            'entities_meeting': [],
            'entities_below': []
        },
        'criminal_standard': {
            'threshold': criminal_threshold,
            'entities_exceeding': [],
            'entities_meeting': [],
            'entities_below': []
        },
        'events': {
            'criminal_threshold_events': [],
            'civil_threshold_events': [],
            'insufficient_evidence': []
        }
    }
    
    # Analyze persons
    for person in entities_data['entities']['persons']:
        score, factors = assess_evidence_strength(person)
        
        entity_info = {
            'entity_id': person['entity_id'],
            'name': person['name'],
            'role': person.get('role', 'unknown'),
            'evidence_score': score,
            'factors': factors
        }
        
        if score >= criminal_threshold:
            results['criminal_standard']['entities_exceeding'].append(entity_info)
        elif score >= civil_threshold:
            results['civil_standard']['entities_meeting'].append(entity_info)
        else:
            results['civil_standard']['entities_below'].append(entity_info)
    
    # Analyze organizations
    for org in entities_data['entities']['organizations']:
        score, factors = assess_evidence_strength(org)
        
        entity_info = {
            'entity_id': org['entity_id'],
            'name': org['name'],
            'type': org.get('type', 'unknown'),
            'evidence_score': score,
            'factors': factors
        }
        
        if score >= criminal_threshold:
            results['criminal_standard']['entities_exceeding'].append(entity_info)
        elif score >= civil_threshold:
            results['civil_standard']['entities_meeting'].append(entity_info)
        else:
            results['civil_standard']['entities_below'].append(entity_info)
    
    # Analyze events
    for event in events_data['events']:
        event_info = {
            'event_id': event['event_id'],
            'date': event.get('date', 'unknown'),
            'description': event.get('description', 'No description'),
            'category': event.get('category', 'unknown')
        }
        
        if event.get('criminal_threshold'):
            results['events']['criminal_threshold_events'].append(event_info)
        elif event.get('civil_threshold'):
            results['events']['civil_threshold_events'].append(event_info)
        else:
            # Check if event has sufficient evidence
            evidence = event.get('evidence', [])
            ad_res_j7 = event.get('ad_res_j7_evidence', [])
            if len(evidence) == 0 and len(ad_res_j7) == 0:
                results['events']['insufficient_evidence'].append(event_info)
    
    return results

def generate_recommendations(analysis_results, analysis_report):
    """Generate recommendations for improving evidence quality"""
    
    recommendations = []
    
    # Check entities below civil threshold
    below_civil = len(analysis_results['civil_standard']['entities_below'])
    if below_civil > 0:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'Entity Evidence',
            'issue': f'{below_civil} entities below civil threshold (50%)',
            'action': 'Add evidence references and ad-res-j7 documentation for entities with weak evidence'
        })
    
    # Check events with missing entity links
    missing_entity_links = analysis_report['events']['missing_entities']
    if missing_entity_links > 0:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'Event-Entity Linkage',
            'issue': f'{missing_entity_links} events missing entity links',
            'action': 'Link all events to relevant entities for complete causal chain'
        })
    
    # Check relations missing event links
    missing_relation_events = analysis_report['relations']['missing_events']
    if missing_relation_events > 0:
        recommendations.append({
            'priority': 'CRITICAL',
            'category': 'Relation-Event Linkage',
            'issue': f'{missing_relation_events} relations missing event links',
            'action': 'Link all relations to supporting events to establish temporal context'
        })
    
    # Check timeline missing evidence
    missing_timeline_evidence = analysis_report['timeline']['missing_evidence']
    if missing_timeline_evidence > 0:
        recommendations.append({
            'priority': 'HIGH',
            'category': 'Timeline Evidence',
            'issue': f'{missing_timeline_evidence} timeline entries missing evidence',
            'action': 'Add ad-res-j7 evidence references to all timeline entries'
        })
    
    # Check undefined entities
    undefined_entities = len(analysis_report['cross_reference']['undefined_entities_in_events'])
    if undefined_entities > 0:
        recommendations.append({
            'priority': 'CRITICAL',
            'category': 'Entity Definitions',
            'issue': f'{undefined_entities} undefined entities referenced in events',
            'action': 'Define all entities or remove invalid references',
            'entities': analysis_report['cross_reference']['undefined_entities_in_events']
        })
    
    # Check undefined events
    undefined_events = len(analysis_report['cross_reference']['undefined_events_in_timeline'])
    if undefined_events > 0:
        recommendations.append({
            'priority': 'CRITICAL',
            'category': 'Event Definitions',
            'issue': f'{undefined_events} undefined events referenced in timeline',
            'action': 'Define all events or remove invalid references',
            'events': analysis_report['cross_reference']['undefined_events_in_timeline'][:10]
        })
    
    return recommendations

def main():
    print("="*80)
    print("EVIDENCE QUALITY & BURDEN OF PROOF ANALYSIS")
    print("="*80)
    
    base_path = "/home/ubuntu/revstream1/data_models"
    
    # Load data models
    entities_data = load_json(f"{base_path}/entities/entities.json")
    events_data = load_json(f"{base_path}/events/events.json")
    analysis_report = load_json(f"{base_path}/ANALYSIS_REPORT_2026_01_25.json")
    
    # Analyze burden of proof
    print("\nAnalyzing evidence against burden of proof standards...")
    proof_analysis = analyze_burden_of_proof(entities_data, events_data)
    
    print("\n1. CIVIL STANDARD (50% - Balance of Probabilities)")
    print("-" * 80)
    print(f"Entities Exceeding: {len(proof_analysis['civil_standard']['entities_exceeding'])}")
    print(f"Entities Meeting: {len(proof_analysis['civil_standard']['entities_meeting'])}")
    print(f"Entities Below: {len(proof_analysis['civil_standard']['entities_below'])}")
    
    if proof_analysis['civil_standard']['entities_below']:
        print("\nTop 10 entities below civil threshold:")
        for entity in proof_analysis['civil_standard']['entities_below'][:10]:
            print(f"  - {entity['entity_id']} ({entity['name']}): {entity['evidence_score']}%")
    
    print("\n2. CRIMINAL STANDARD (95% - Beyond Reasonable Doubt)")
    print("-" * 80)
    print(f"Entities Exceeding: {len(proof_analysis['criminal_standard']['entities_exceeding'])}")
    print(f"Entities Below: {len(proof_analysis['criminal_standard']['entities_below'])}")
    
    if proof_analysis['criminal_standard']['entities_exceeding']:
        print("\nEntities exceeding criminal threshold:")
        for entity in proof_analysis['criminal_standard']['entities_exceeding']:
            print(f"  ✅ {entity['entity_id']} ({entity['name']}): {entity['evidence_score']}%")
    
    print("\n3. EVENT EVIDENCE QUALITY")
    print("-" * 80)
    print(f"Criminal Threshold Events: {len(proof_analysis['events']['criminal_threshold_events'])}")
    print(f"Civil Threshold Events: {len(proof_analysis['events']['civil_threshold_events'])}")
    print(f"Insufficient Evidence: {len(proof_analysis['events']['insufficient_evidence'])}")
    
    # Generate recommendations
    print("\n4. RECOMMENDATIONS FOR IMPROVEMENT")
    print("-" * 80)
    recommendations = generate_recommendations(proof_analysis, analysis_report)
    
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. [{rec['priority']}] {rec['category']}")
        print(f"   Issue: {rec['issue']}")
        print(f"   Action: {rec['action']}")
    
    # Save results
    output = {
        'timestamp': datetime.now().isoformat(),
        'burden_of_proof_analysis': proof_analysis,
        'recommendations': recommendations,
        'summary': {
            'civil_threshold_met': len(proof_analysis['civil_standard']['entities_meeting']) + 
                                   len(proof_analysis['civil_standard']['entities_exceeding']),
            'criminal_threshold_met': len(proof_analysis['criminal_standard']['entities_exceeding']),
            'total_entities': len(proof_analysis['civil_standard']['entities_exceeding']) + 
                            len(proof_analysis['civil_standard']['entities_meeting']) + 
                            len(proof_analysis['civil_standard']['entities_below']),
            'criminal_threshold_events': len(proof_analysis['events']['criminal_threshold_events']),
            'civil_threshold_events': len(proof_analysis['events']['civil_threshold_events'])
        }
    }
    
    output_path = f"{base_path}/EVIDENCE_QUALITY_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(output, output_path)
    print(f"\n📊 Evidence quality analysis saved to: {output_path}")
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
