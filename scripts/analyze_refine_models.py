#!/usr/bin/env python3
"""
Analyze and refine entities, relations, events, and timelines
Cross-reference with ad-res-j7 evidence repository
"""
import json
import os
from datetime import datetime
from pathlib import Path

# Paths
ENTITIES_FILE = "data_models/entities/entities_sf10_integrated_2025_12_09.json"
RELATIONS_FILE = "data_models/relations/relations_refined_2025_12_09_v23.json"
EVENTS_FILE = "data_models/events/events_refined_2025_12_09_v33.json"
TIMELINE_FILE = "data_models/timelines/timeline_refined_2025_12_09_v22.json"
AD_RES_J7_PATH = "/home/ubuntu/ad-res-j7"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {filepath}")

def analyze_entities(entities_data):
    """Analyze entities for completeness and evidence support"""
    issues = []
    improvements = []
    
    persons = entities_data.get('entities', {}).get('persons', [])
    organizations = entities_data.get('entities', {}).get('organizations', [])
    
    print(f"\n=== ENTITIES ANALYSIS ===")
    print(f"Total Persons: {len(persons)}")
    print(f"Total Organizations: {len(organizations)}")
    
    # Check for missing evidence support
    for person in persons:
        entity_id = person.get('entity_id')
        name = person.get('name')
        evidence_support = person.get('evidence_support', {})
        
        if not evidence_support or not evidence_support.get('evidence_refs'):
            issues.append(f"{entity_id} ({name}): Missing evidence references")
        
        # Check for criminal liability documentation
        if person.get('agent_type') == 'antagonist':
            if not person.get('criminal_liability'):
                improvements.append(f"{entity_id} ({name}): Add criminal liability assessment")
    
    return issues, improvements

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    issues = []
    improvements = []
    
    print(f"\n=== RELATIONS ANALYSIS ===")
    
    for category, relations in relations_data.get('relations', {}).items():
        print(f"{category}: {len(relations)} relations")
        
        for rel in relations:
            rel_id = rel.get('relation_id')
            
            # Check for evidence
            if not rel.get('evidence') and not rel.get('ad_res_j7_references'):
                issues.append(f"{rel_id}: Missing evidence documentation")
            
            # Check for SF evidence integration
            evidence = rel.get('evidence', [])
            if not any('SF' in str(e) for e in evidence):
                improvements.append(f"{rel_id}: Consider adding SF evidence references")
    
    return issues, improvements

def analyze_events(events_data):
    """Analyze events for completeness and chronology"""
    issues = []
    improvements = []
    
    events = events_data.get('events', [])
    print(f"\n=== EVENTS ANALYSIS ===")
    print(f"Total Events: {len(events)}")
    
    # Check chronological order
    dates = []
    for event in events:
        event_id = event.get('event_id')
        date = event.get('date')
        
        if date:
            dates.append((date, event_id))
        else:
            issues.append(f"{event_id}: Missing date")
        
        # Check evidence support
        if not event.get('evidence') and not event.get('evidence_support'):
            issues.append(f"{event_id}: Missing evidence")
        
        # Check for financial impact quantification
        if event.get('category') in ['revenue_theft', 'financial_manipulation', 'transfer_pricing_fraud']:
            if event.get('financial_impact') == 'unknown_amount':
                improvements.append(f"{event_id}: Quantify financial impact if possible")
    
    # Check if sorted
    sorted_dates = sorted(dates, key=lambda x: x[0])
    if dates != sorted_dates:
        issues.append("Events not in chronological order")
    
    return issues, improvements

def analyze_timeline(timeline_data):
    """Analyze timeline for gaps and improvements"""
    issues = []
    improvements = []
    
    timeline_entries = timeline_data.get('timeline_entries', [])
    print(f"\n=== TIMELINE ANALYSIS ===")
    print(f"Total Timeline Entries: {len(timeline_entries)}")
    
    metadata = timeline_data.get('metadata', {})
    print(f"Date Range: {metadata.get('date_range', {}).get('start')} to {metadata.get('date_range', {}).get('end')}")
    
    # Check for evidence support in each entry
    for entry in timeline_entries:
        tl_id = entry.get('timeline_id')
        
        if not entry.get('evidence') and not entry.get('evidence_support'):
            issues.append(f"{tl_id}: Missing evidence support")
        
        # Check for actor identification
        if not entry.get('actors') and not entry.get('actor_names'):
            improvements.append(f"{tl_id}: Add actor identification")
    
    return issues, improvements

def check_sf_evidence_integration():
    """Check which SF evidence files exist in ad-res-j7"""
    sf_evidence = {}
    annexures_path = Path(AD_RES_J7_PATH) / "ANNEXURES"
    
    if annexures_path.exists():
        for item in annexures_path.iterdir():
            if item.name.startswith('SF'):
                sf_evidence[item.name] = str(item)
    
    print(f"\n=== SF EVIDENCE IN AD-RES-J7 ===")
    for sf_name in sorted(sf_evidence.keys()):
        print(f"  {sf_name}")
    
    return sf_evidence

def main():
    """Main analysis function"""
    print("=" * 80)
    print("REVSTREAM1 DATA MODEL ANALYSIS")
    print("=" * 80)
    
    # Load data
    entities_data = load_json(ENTITIES_FILE)
    relations_data = load_json(RELATIONS_FILE)
    events_data = load_json(EVENTS_FILE)
    timeline_data = load_json(TIMELINE_FILE)
    
    # Analyze each component
    entity_issues, entity_improvements = analyze_entities(entities_data)
    relation_issues, relation_improvements = analyze_relations(relations_data)
    event_issues, event_improvements = analyze_events(events_data)
    timeline_issues, timeline_improvements = analyze_timeline(timeline_data)
    
    # Check SF evidence
    sf_evidence = check_sf_evidence_integration()
    
    # Compile report
    report = {
        "analysis_date": datetime.now().isoformat(),
        "summary": {
            "total_issues": len(entity_issues) + len(relation_issues) + len(event_issues) + len(timeline_issues),
            "total_improvements": len(entity_improvements) + len(relation_improvements) + len(event_improvements) + len(timeline_improvements)
        },
        "entities": {
            "issues": entity_issues,
            "improvements": entity_improvements
        },
        "relations": {
            "issues": relation_issues,
            "improvements": relation_improvements
        },
        "events": {
            "issues": event_issues,
            "improvements": event_improvements
        },
        "timeline": {
            "issues": timeline_issues,
            "improvements": timeline_improvements
        },
        "sf_evidence_available": list(sf_evidence.keys())
    }
    
    # Save report
    save_json(report, "ANALYSIS_REPORT_2025_12_10.json")
    
    # Print summary
    print(f"\n{'=' * 80}")
    print("ANALYSIS SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total Issues: {report['summary']['total_issues']}")
    print(f"Total Improvement Opportunities: {report['summary']['total_improvements']}")
    print(f"\nDetailed report saved to: ANALYSIS_REPORT_2025_12_10.json")

if __name__ == "__main__":
    main()
