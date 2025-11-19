#!/usr/bin/env python3
import json
from pathlib import Path
from collections import defaultdict

def analyze_entities(filepath):
    """Analyze entities structure and completeness"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_entities': 0,
        'persons': 0,
        'organizations': 0,
        'platforms': 0,
        'domains': 0,
        'trusts': 0,
        'missing_evidence': [],
        'missing_ad_res_references': [],
        'entities_without_timeline_events': [],
        'entities_without_financial_impact': []
    }
    
    # Analyze persons
    if 'entities' in data and 'persons' in data['entities']:
        analysis['persons'] = len(data['entities']['persons'])
        for person in data['entities']['persons']:
            if not person.get('timeline_events') or len(person.get('timeline_events', [])) == 0:
                if person.get('involvement_events', 0) > 0:
                    analysis['entities_without_timeline_events'].append(person['entity_id'])
            
            # Check for evidence references
            if 'evidence' not in person and person.get('involvement_events', 0) > 0:
                analysis['missing_evidence'].append(person['entity_id'])
            
            # Check for financial impact on antagonists
            if person.get('agent_type') == 'antagonist' and 'financial_impact' not in person:
                analysis['entities_without_financial_impact'].append(person['entity_id'])
    
    # Analyze organizations
    if 'entities' in data and 'organizations' in data['entities']:
        analysis['organizations'] = len(data['entities']['organizations'])
        for org in data['entities']['organizations']:
            if not org.get('timeline_events') or len(org.get('timeline_events', [])) == 0:
                if org.get('involvement_events', 0) > 0:
                    analysis['entities_without_timeline_events'].append(org['entity_id'])
    
    # Count other entity types
    if 'entities' in data:
        for key in ['platforms', 'domains', 'trusts']:
            if key in data['entities']:
                analysis[key] = len(data['entities'][key])
    
    analysis['total_entities'] = sum([
        analysis['persons'],
        analysis['organizations'],
        analysis['platforms'],
        analysis['domains'],
        analysis['trusts']
    ])
    
    return analysis

def analyze_events(filepath):
    """Analyze events structure and completeness"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_events': len(data.get('events', [])),
        'events_with_perpetrators': 0,
        'events_with_victims': 0,
        'events_with_financial_impact': 0,
        'events_with_evidence': 0,
        'events_with_ad_res_reference': 0,
        'missing_perpetrators': [],
        'missing_evidence': [],
        'missing_ad_res_references': [],
        'events_by_category': defaultdict(int),
        'events_by_phase': defaultdict(int)
    }
    
    for event in data.get('events', []):
        # Check perpetrators
        if event.get('perpetrators') and len(event['perpetrators']) > 0:
            analysis['events_with_perpetrators'] += 1
        else:
            if event.get('category') not in ['business_relationship', 'financial_structure']:
                analysis['missing_perpetrators'].append(event['event_id'])
        
        # Check victims
        if event.get('victims') and len(event['victims']) > 0:
            analysis['events_with_victims'] += 1
        
        # Check financial impact
        if event.get('financial_impact'):
            analysis['events_with_financial_impact'] += 1
        
        # Check evidence
        if event.get('evidence') and len(event['evidence']) > 0:
            analysis['events_with_evidence'] += 1
        else:
            analysis['missing_evidence'].append(event['event_id'])
        
        # Check ad-res-j7 reference
        if 'extended_evidence_note' in event or 'ad_res_j7_reference' in event:
            analysis['events_with_ad_res_reference'] += 1
        else:
            analysis['missing_ad_res_references'].append(event['event_id'])
        
        # Count by category
        category = event.get('category', 'unknown')
        analysis['events_by_category'][category] += 1
        
        # Count by phase
        phase = event.get('timeline_phase', 'unknown')
        analysis['events_by_phase'][phase] += 1
    
    return analysis

def analyze_relations(filepath):
    """Analyze relations structure and completeness"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_relations': 0,
        'ownership_relations': 0,
        'control_relations': 0,
        'financial_relations': 0,
        'conspiracy_relations': 0,
        'missing_evidence': [],
        'relations_by_type': defaultdict(int)
    }
    
    # Count relations by category
    for category in ['ownership_relations', 'control_relations', 'financial_relations', 'conspiracy_relations']:
        if category in data.get('relations', {}):
            count = len(data['relations'][category])
            analysis[category] = count
            analysis['total_relations'] += count
            
            # Check for evidence
            for rel in data['relations'][category]:
                if not rel.get('evidence') or len(rel['evidence']) == 0:
                    analysis['missing_evidence'].append(rel['relation_id'])
                
                # Count by relation type
                rel_type = rel.get('relation_type', 'unknown')
                analysis['relations_by_type'][rel_type] += 1
    
    return analysis

def analyze_timeline(filepath):
    """Analyze timeline structure and completeness"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    analysis = {
        'total_phases': 0,
        'total_events_in_timeline': 0,
        'phases': [],
        'events_per_phase': {},
        'financial_impact_per_phase': {},
        'missing_evidence_repository_refs': []
    }
    
    if 'timeline_phases' in data:
        for phase_key, phase_data in data['timeline_phases'].items():
            analysis['total_phases'] += 1
            phase_id = phase_data.get('phase_id', phase_key)
            event_count = len(phase_data.get('events', []))
            
            analysis['phases'].append({
                'phase_id': phase_id,
                'phase_name': phase_data.get('phase_name'),
                'event_count': event_count,
                'financial_impact': phase_data.get('financial_impact', 'unknown')
            })
            
            analysis['events_per_phase'][phase_id] = event_count
            analysis['total_events_in_timeline'] += event_count
            analysis['financial_impact_per_phase'][phase_id] = phase_data.get('financial_impact', 'unknown')
            
            # Check for evidence repository references
            if 'evidence_repository' not in phase_data:
                analysis['missing_evidence_repository_refs'].append(phase_id)
    
    return analysis

def main():
    base_path = Path('/home/ubuntu/revstream1/data_models')
    
    # Analyze latest versions
    entities_file = base_path / 'entities' / 'entities_refined_2025_11_19_v2.json'
    events_file = base_path / 'events' / 'events_refined_2025_11_19_v2.json'
    relations_file = base_path / 'relations' / 'relations_refined_2025_11_19_v2.json'
    timeline_file = base_path / 'timelines' / 'timeline_refined_2025_11_19_v2.json'
    
    print("=" * 80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS")
    print("=" * 80)
    print()
    
    # Entities Analysis
    print("ENTITIES ANALYSIS")
    print("-" * 80)
    entities_analysis = analyze_entities(entities_file)
    print(f"Total Entities: {entities_analysis['total_entities']}")
    print(f"  - Persons: {entities_analysis['persons']}")
    print(f"  - Organizations: {entities_analysis['organizations']}")
    print(f"  - Platforms: {entities_analysis['platforms']}")
    print(f"  - Domains: {entities_analysis['domains']}")
    print(f"  - Trusts: {entities_analysis['trusts']}")
    print()
    print(f"Entities without timeline events: {len(entities_analysis['entities_without_timeline_events'])}")
    if entities_analysis['entities_without_timeline_events']:
        print(f"  {', '.join(entities_analysis['entities_without_timeline_events'][:10])}")
    print(f"Entities missing evidence: {len(entities_analysis['missing_evidence'])}")
    if entities_analysis['missing_evidence']:
        print(f"  {', '.join(entities_analysis['missing_evidence'][:10])}")
    print(f"Antagonists without financial impact: {len(entities_analysis['entities_without_financial_impact'])}")
    if entities_analysis['entities_without_financial_impact']:
        print(f"  {', '.join(entities_analysis['entities_without_financial_impact'][:10])}")
    print()
    
    # Events Analysis
    print("EVENTS ANALYSIS")
    print("-" * 80)
    events_analysis = analyze_events(events_file)
    print(f"Total Events: {events_analysis['total_events']}")
    print(f"Events with perpetrators: {events_analysis['events_with_perpetrators']}")
    print(f"Events with victims: {events_analysis['events_with_victims']}")
    print(f"Events with financial impact: {events_analysis['events_with_financial_impact']}")
    print(f"Events with evidence: {events_analysis['events_with_evidence']}")
    print(f"Events with ad-res-j7 reference: {events_analysis['events_with_ad_res_reference']}")
    print()
    print(f"Events missing perpetrators: {len(events_analysis['missing_perpetrators'])}")
    if events_analysis['missing_perpetrators']:
        print(f"  {', '.join(events_analysis['missing_perpetrators'][:10])}")
    print(f"Events missing evidence: {len(events_analysis['missing_evidence'])}")
    if events_analysis['missing_evidence']:
        print(f"  {', '.join(events_analysis['missing_evidence'][:10])}")
    print(f"Events missing ad-res-j7 references: {len(events_analysis['missing_ad_res_references'])}")
    if events_analysis['missing_ad_res_references']:
        print(f"  {', '.join(events_analysis['missing_ad_res_references'][:10])}")
    print()
    print("Events by Category:")
    for category, count in sorted(events_analysis['events_by_category'].items()):
        print(f"  {category}: {count}")
    print()
    print("Events by Phase:")
    for phase, count in sorted(events_analysis['events_by_phase'].items()):
        print(f"  {phase}: {count}")
    print()
    
    # Relations Analysis
    print("RELATIONS ANALYSIS")
    print("-" * 80)
    relations_analysis = analyze_relations(relations_file)
    print(f"Total Relations: {relations_analysis['total_relations']}")
    print(f"  - Ownership: {relations_analysis['ownership_relations']}")
    print(f"  - Control: {relations_analysis['control_relations']}")
    print(f"  - Financial: {relations_analysis['financial_relations']}")
    print(f"  - Conspiracy: {relations_analysis['conspiracy_relations']}")
    print()
    print(f"Relations missing evidence: {len(relations_analysis['missing_evidence'])}")
    if relations_analysis['missing_evidence']:
        print(f"  {', '.join(relations_analysis['missing_evidence'][:10])}")
    print()
    print("Relations by Type:")
    for rel_type, count in sorted(relations_analysis['relations_by_type'].items()):
        print(f"  {rel_type}: {count}")
    print()
    
    # Timeline Analysis
    print("TIMELINE ANALYSIS")
    print("-" * 80)
    timeline_analysis = analyze_timeline(timeline_file)
    print(f"Total Phases: {timeline_analysis['total_phases']}")
    print(f"Total Events in Timeline: {timeline_analysis['total_events_in_timeline']}")
    print()
    print("Phases Overview:")
    for phase in timeline_analysis['phases']:
        print(f"  {phase['phase_id']}: {phase['phase_name']}")
        print(f"    Events: {phase['event_count']}, Financial Impact: {phase['financial_impact']}")
    print()
    print(f"Phases missing evidence repository refs: {len(timeline_analysis['missing_evidence_repository_refs'])}")
    if timeline_analysis['missing_evidence_repository_refs']:
        print(f"  {', '.join(timeline_analysis['missing_evidence_repository_refs'][:10])}")
    print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY OF ISSUES TO ADDRESS")
    print("=" * 80)
    issues = []
    
    if entities_analysis['entities_without_timeline_events']:
        issues.append(f"- {len(entities_analysis['entities_without_timeline_events'])} entities with involvement but no timeline events")
    
    if entities_analysis['missing_evidence']:
        issues.append(f"- {len(entities_analysis['missing_evidence'])} entities missing evidence references")
    
    if events_analysis['missing_perpetrators']:
        issues.append(f"- {len(events_analysis['missing_perpetrators'])} events missing perpetrators")
    
    if events_analysis['missing_evidence']:
        issues.append(f"- {len(events_analysis['missing_evidence'])} events missing evidence")
    
    if events_analysis['missing_ad_res_references']:
        issues.append(f"- {len(events_analysis['missing_ad_res_references'])} events missing ad-res-j7 references")
    
    if relations_analysis['missing_evidence']:
        issues.append(f"- {len(relations_analysis['missing_evidence'])} relations missing evidence")
    
    if timeline_analysis['missing_evidence_repository_refs']:
        issues.append(f"- {len(timeline_analysis['missing_evidence_repository_refs'])} phases missing evidence repository refs")
    
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("No critical issues found!")
    
    print()
    print("=" * 80)

if __name__ == '__main__':
    main()
