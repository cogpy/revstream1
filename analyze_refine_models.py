#!/usr/bin/env python3
"""
Analyze and refine entities, relations, events, and timelines for case 2025-137857
"""
import json
import os
from datetime import datetime
from collections import defaultdict

# Paths
BASE_DIR = "/home/ubuntu/revstream1"
ENTITIES_FILE = f"{BASE_DIR}/data_models/entities/entities_final_corrected_2025_12_05.json"
RELATIONS_FILE = f"{BASE_DIR}/data_models/relations/relations_refined_2025_12_05_v21.json"
EVENTS_FILE = f"{BASE_DIR}/data_models/events/events_refined_2025_12_06_v28.json"
TIMELINE_FILE = f"{BASE_DIR}/data_models/timelines/timeline_refined_2025_12_06_v19.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_financial_amount(financial_impact):
    """Extract financial amount from various formats"""
    if not financial_impact:
        return 0
    
    if isinstance(financial_impact, str):
        # Direct string amount
        try:
            return float(financial_impact.replace('R', '').replace(',', '').strip())
        except:
            return 0
    elif isinstance(financial_impact, dict):
        # Dictionary with amount field
        amount = financial_impact.get('amount', '0')
        if isinstance(amount, str):
            try:
                return float(amount.replace('R', '').replace(',', '').strip())
            except:
                return 0
        elif isinstance(amount, (int, float)):
            return float(amount)
    
    return 0

def analyze_entities(entities_data):
    """Analyze entities structure and completeness"""
    print("=" * 80)
    print("ENTITIES ANALYSIS")
    print("=" * 80)
    
    metadata = entities_data.get('metadata', {})
    print(f"\nVersion: {metadata.get('version', 'N/A')}")
    print(f"Last Updated: {metadata.get('last_updated', 'N/A')}")
    print(f"Case Number: {metadata.get('case_number', 'N/A')}")
    
    entities = entities_data.get('entities', {})
    persons = entities.get('persons', [])
    orgs = entities.get('organizations', [])
    
    print(f"\nTotal Persons: {len(persons)}")
    print(f"Total Organizations: {len(orgs)}")
    
    # Analyze key persons
    print("\n--- Key Persons ---")
    for person in persons[:5]:
        print(f"  {person.get('entity_id')}: {person.get('name')} - {person.get('role')}")
        print(f"    Events: {person.get('involvement_events', 0)}")
        print(f"    Financial Impact: {person.get('financial_impact', {}).get('direct_involvement', 'N/A')}")
    
    return {
        'total_persons': len(persons),
        'total_orgs': len(orgs),
        'persons': persons,
        'orgs': orgs
    }

def analyze_relations(relations_data):
    """Analyze relations structure and completeness"""
    print("\n" + "=" * 80)
    print("RELATIONS ANALYSIS")
    print("=" * 80)
    
    metadata = relations_data.get('metadata', {})
    print(f"\nVersion: {metadata.get('version', 'N/A')}")
    print(f"Last Updated: {metadata.get('last_updated', 'N/A')}")
    
    relations = relations_data.get('relations', {})
    
    # Count relations by type
    relation_types = {}
    total_relations = 0
    
    for rel_type, rel_list in relations.items():
        count = len(rel_list) if isinstance(rel_list, list) else 0
        relation_types[rel_type] = count
        total_relations += count
    
    print(f"\nTotal Relations: {total_relations}")
    print("\n--- Relations by Type ---")
    for rel_type, count in sorted(relation_types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {rel_type}: {count}")
    
    return {
        'total_relations': total_relations,
        'relation_types': relation_types,
        'relations': relations
    }

def analyze_events(events_data):
    """Analyze events structure and completeness"""
    print("\n" + "=" * 80)
    print("EVENTS ANALYSIS")
    print("=" * 80)
    
    metadata = events_data.get('metadata', {})
    print(f"\nVersion: {metadata.get('version', 'N/A')}")
    print(f"Last Updated: {metadata.get('last_updated', 'N/A')}")
    
    events = events_data.get('events', [])
    print(f"\nTotal Events: {len(events)}")
    
    # Analyze event categories
    categories = defaultdict(int)
    financial_events = 0
    total_financial_impact = 0
    
    for event in events:
        for cat in event.get('categories', []):
            categories[cat] += 1
        
        if event.get('financial_impact'):
            financial_events += 1
            amount = extract_financial_amount(event.get('financial_impact'))
            total_financial_impact += amount
    
    print(f"\nEvents with Financial Impact: {financial_events}")
    print(f"Total Financial Impact: R{total_financial_impact:,.2f}")
    
    print("\n--- Top Event Categories ---")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {cat}: {count}")
    
    # Check evidence references
    events_with_evidence = sum(1 for e in events if e.get('evidence_references'))
    events_with_ad_res_j7 = sum(1 for e in events if e.get('ad_res_j7_cross_references'))
    
    print(f"\nEvents with Evidence References: {events_with_evidence}/{len(events)}")
    print(f"Events with ad-res-j7 Cross-References: {events_with_ad_res_j7}/{len(events)}")
    
    return {
        'total_events': len(events),
        'financial_events': financial_events,
        'total_financial_impact': total_financial_impact,
        'events': events,
        'categories': dict(categories)
    }

def analyze_timeline(timeline_data):
    """Analyze timeline structure and completeness"""
    print("\n" + "=" * 80)
    print("TIMELINE ANALYSIS")
    print("=" * 80)
    
    metadata = timeline_data.get('metadata', {})
    print(f"\nVersion: {metadata.get('version', 'N/A')}")
    print(f"Last Updated: {metadata.get('last_updated', 'N/A')}")
    
    timeline_events = timeline_data.get('timeline_events', [])
    print(f"\nTotal Timeline Events: {len(timeline_events)}")
    
    # Analyze date ranges
    dates = []
    for event in timeline_events:
        date_str = event.get('date')
        if date_str:
            try:
                dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
            except:
                pass
    
    if dates:
        print(f"Date Range: {min(dates).strftime('%Y-%m-%d')} to {max(dates).strftime('%Y-%m-%d')}")
        print(f"Duration: {(max(dates) - min(dates)).days} days")
    
    return {
        'total_timeline_events': len(timeline_events),
        'timeline_events': timeline_events
    }

def main():
    """Main analysis function"""
    print("Starting comprehensive data model analysis...")
    print(f"Timestamp: {datetime.now().isoformat()}\n")
    
    # Load all data
    entities_data = load_json(ENTITIES_FILE)
    relations_data = load_json(RELATIONS_FILE)
    events_data = load_json(EVENTS_FILE)
    timeline_data = load_json(TIMELINE_FILE)
    
    # Analyze each component
    entities_analysis = analyze_entities(entities_data)
    relations_analysis = analyze_relations(relations_data)
    events_analysis = analyze_events(events_data)
    timeline_analysis = analyze_timeline(timeline_data)
    
    # Generate summary report
    print("\n" + "=" * 80)
    print("SUMMARY REPORT")
    print("=" * 80)
    print(f"\nTotal Entities: {entities_analysis['total_persons'] + entities_analysis['total_orgs']}")
    print(f"  - Persons: {entities_analysis['total_persons']}")
    print(f"  - Organizations: {entities_analysis['total_orgs']}")
    print(f"\nTotal Relations: {relations_analysis['total_relations']}")
    print(f"Total Events: {events_analysis['total_events']}")
    print(f"Total Timeline Events: {timeline_analysis['total_timeline_events']}")
    print(f"\nFinancial Impact: R{events_analysis['total_financial_impact']:,.2f}")
    
    # Save analysis report
    report = {
        'timestamp': datetime.now().isoformat(),
        'case_number': '2025-137857',
        'summary': {
            'total_entities': entities_analysis['total_persons'] + entities_analysis['total_orgs'],
            'total_persons': entities_analysis['total_persons'],
            'total_orgs': entities_analysis['total_orgs'],
            'total_relations': relations_analysis['total_relations'],
            'total_events': events_analysis['total_events'],
            'total_timeline_events': timeline_analysis['total_timeline_events'],
            'total_financial_impact': events_analysis['total_financial_impact']
        }
    }
    
    report_file = f"{BASE_DIR}/ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nAnalysis report saved to: {report_file}")
    return report

if __name__ == "__main__":
    main()
