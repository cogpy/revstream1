#!/usr/bin/env python3.11
"""
Current State Analysis for RevStream1 Repository
Analyzes entities, relations, events, and timelines
"""
import json
from datetime import datetime
from collections import defaultdict

def analyze_current_state():
    # Load the comprehensive analysis
    with open('COMPREHENSIVE_ANALYSIS_2025_12_25.json', 'r') as f:
        data = json.load(f)
    
    print("=" * 80)
    print("CURRENT STATE ANALYSIS - REVSTREAM1")
    print("=" * 80)
    print(f"\nTimestamp: {data['timestamp']}")
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Entities Analysis
    entities = data['entities']
    print(f"\n{'ENTITIES':-^80}")
    print(f"Version: {entities['version']}")
    print(f"Total Count: {entities['total_count']}")
    print(f"  - Persons: {entities['persons']}")
    print(f"  - Organizations: {entities['organizations']}")
    
    # List all persons with key details
    persons = entities['data']['entities']['persons']
    print(f"\nPersons ({len(persons)}):")
    for p in persons:
        print(f"  {p['entity_id']}: {p['name']}")
        print(f"    Role: {p['role']}, Events: {p.get('involvement_events', 0)}")
        print(f"    Evidence Strength: {p.get('evidence_strength', 'N/A')}")
        if 'financial_impact' in p:
            print(f"    Financial Impact: {p['financial_impact'].get('direct_involvement', 'N/A')}")
    
    # List all organizations
    orgs = entities['data']['entities']['organizations']
    print(f"\nOrganizations ({len(orgs)}):")
    for o in orgs:
        print(f"  {o['entity_id']}: {o['name']}")
        print(f"    Role: {o['role']}, Events: {o.get('involvement_events', 0)}")
    
    # Relations Analysis
    relations = data['relations']
    print(f"\n{'RELATIONS':-^80}")
    print(f"Version: {relations['version']}")
    print(f"Total Count: {relations['total_count']}")
    print(f"Relation Types: {len(relations['by_type'])}")
    
    # Count relations by type
    rels_data = relations['data']['relations']
    print(f"\nRelations by Type:")
    for rel_type, rel_list in rels_data.items():
        print(f"  {rel_type}: {len(rel_list)} relations")
    
    # Show sample relations
    print(f"\nSample Relations (first 5):")
    count = 0
    for rel_type, rel_list in rels_data.items():
        for r in rel_list[:2]:
            if count >= 5:
                break
            print(f"  {r.get('relation_id', 'N/A')}: {r.get('source_entity', r.get('from_entity', 'N/A'))} -> {r.get('target_entity', r.get('to_entity', 'N/A'))}")
            print(f"    Type: {r.get('relation_type', 'N/A')}, Strength: {r.get('strength', 'N/A')}")
            count += 1
        if count >= 5:
            break
    
    # Events Analysis
    events = data['events']
    print(f"\n{'EVENTS':-^80}")
    print(f"Version: {events['version']}")
    print(f"Total Count: {events['total_count']}")
    
    events_data = events['data']['events']
    print(f"\nEvent Categories:")
    categories = defaultdict(int)
    for e in events_data:
        categories[e.get('category', 'unknown')] += 1
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
    
    # Show critical events
    print(f"\nCritical Events (first 10):")
    for e in events_data[:10]:
        title = e.get('title', e.get('description', 'N/A'))
        print(f"  {e['event_id']}: {e['date']} - {title}")
        print(f"    Category: {e.get('category', 'N/A')}, Impact: {e.get('impact_level', 'N/A')}")
    
    # Timeline Analysis
    timelines = data['timelines']
    print(f"\n{'TIMELINES':-^80}")
    print(f"Version: {timelines['version']}")
    print(f"Total Phases: {timelines['total_phases']}")
    print(f"Phases: {', '.join(timelines['phases'])}")
    
    tl_data = timelines['data']
    print(f"\nTimeline Components:")
    for key in tl_data.keys():
        if key != 'metadata':
            val = tl_data[key]
            if isinstance(val, list):
                print(f"  - {key}: {len(val)} items")
            elif isinstance(val, dict):
                print(f"  - {key}: {len(val)} keys")
            else:
                print(f"  - {key}")
    
    # Evidence Mapping
    evidence = data.get('evidence_mapping', {})
    print(f"\n{'EVIDENCE MAPPING':-^80}")
    print(f"Total Evidence Items: {evidence.get('total_evidence_items', 0)}")
    if 'evidence_categories' in evidence:
        print(f"Evidence Categories: {len(evidence['evidence_categories'])} categories")
        for cat, items in list(evidence['evidence_categories'].items())[:5]:
            print(f"  - {cat}: {len(items) if isinstance(items, list) else 'N/A'} items")
    
    # Burden of Proof
    burden = data.get('burden_of_proof_analysis', {})
    print(f"\n{'BURDEN OF PROOF':-^80}")
    if burden:
        print(f"Civil Threshold (50%): {burden.get('civil_threshold_met', 'N/A')}")
        print(f"Criminal Threshold (95%): {burden.get('criminal_threshold_met', 'N/A')}")
        if 'summary' in burden:
            print(f"Summary: {burden['summary']}")
    
    # Filing Recommendations
    filings = data.get('filing_recommendations', {})
    print(f"\n{'FILING RECOMMENDATIONS':-^80}")
    if filings:
        for filing_type in list(filings.keys())[:10]:
            details = filings[filing_type]
            if isinstance(details, dict):
                print(f"  {filing_type}:")
                print(f"    Status: {details.get('status', 'N/A')}")
                print(f"    Priority: {details.get('priority', 'N/A')}")
    
    print("\n" + "=" * 80)
    
    # Return summary for further processing
    return {
        'entities_count': entities['total_count'],
        'persons_count': len(persons),
        'organizations_count': len(orgs),
        'relations_count': relations['total_count'],
        'events_count': events['total_count'],
        'timeline_phases': timelines['total_phases'],
        'evidence_items': evidence.get('total_evidence_items', 0)
    }

if __name__ == '__main__':
    summary = analyze_current_state()
    print(f"\nSummary: {summary}")
