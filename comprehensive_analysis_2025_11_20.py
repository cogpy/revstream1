#!/usr/bin/env python3
"""
Comprehensive Analysis of revstream1 Data Models
Version: 2025-11-20
Purpose: Analyze entities, relations, events, and timelines for refinement
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_json(filepath):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_entities(entities_data):
    """Analyze entities structure and completeness"""
    analysis = {
        "total_persons": len(entities_data["entities"]["persons"]),
        "total_organizations": len(entities_data["entities"]["organizations"]),
        "total_trusts": len(entities_data["entities"]["trusts"]),
        "persons_with_evidence": 0,
        "persons_without_evidence": [],
        "organizations_with_evidence": 0,
        "organizations_without_evidence": [],
        "missing_ad_res_j7_refs": []
    }
    
    # Analyze persons
    for person in entities_data["entities"]["persons"]:
        if person.get("evidence_files") and len(person["evidence_files"]) > 0:
            analysis["persons_with_evidence"] += 1
        else:
            analysis["persons_without_evidence"].append(person.get("name", person.get("entity_id")))
        
        if not person.get("ad_res_j7_references"):
            analysis["missing_ad_res_j7_refs"].append(person.get("name", person.get("entity_id")))
    
    # Analyze organizations
    for org in entities_data["entities"]["organizations"]:
        if org.get("evidence_files") and len(org["evidence_files"]) > 0:
            analysis["organizations_with_evidence"] += 1
        else:
            analysis["organizations_without_evidence"].append(org.get("name", org.get("entity_id")))
    
    return analysis

def analyze_events(events_data):
    """Analyze events structure and completeness"""
    analysis = {
        "total_events": len(events_data["events"]),
        "events_with_evidence": 0,
        "events_without_evidence": [],
        "events_by_category": defaultdict(int),
        "events_by_phase": defaultdict(int),
        "missing_ad_res_j7_refs": []
    }
    
    for event in events_data["events"]:
        # Count by category
        category = event.get("crime_category", "unknown")
        analysis["events_by_category"][category] += 1
        
        # Count by phase
        phase = event.get("phase", "unknown")
        analysis["events_by_phase"][phase] += 1
        
        # Check evidence
        if event.get("evidence_files") and len(event["evidence_files"]) > 0:
            analysis["events_with_evidence"] += 1
        else:
            analysis["events_without_evidence"].append(event.get("event_id"))
        
        # Check ad-res-j7 references
        if not event.get("ad_res_j7_references"):
            analysis["missing_ad_res_j7_refs"].append(event.get("event_id"))
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations structure and completeness"""
    analysis = {
        "total_relations": len(relations_data["relations"]),
        "relation_types": defaultdict(int),
        "relations_with_evidence": 0,
        "relations_without_evidence": []
    }
    
    for relation in relations_data["relations"]:
        rel_type = relation.get("relation_type", "unknown")
        analysis["relation_types"][rel_type] += 1
        
        if relation.get("evidence_files") and len(relation["evidence_files"]) > 0:
            analysis["relations_with_evidence"] += 1
        else:
            analysis["relations_without_evidence"].append(relation.get("relation_id"))
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline structure"""
    analysis = {
        "metadata": timeline_data.get("metadata", {}),
        "phases": list(timeline_data.get("timeline_phases", {}).keys()),
        "phase_count": len(timeline_data.get("timeline_phases", {})),
        "events_by_phase": {}
    }
    
    for phase_key, phase_data in timeline_data.get("timeline_phases", {}).items():
        events = phase_data.get("events", [])
        analysis["events_by_phase"][phase_key] = {
            "name": phase_data.get("phase_name"),
            "event_count": len(events),
            "events": events
        }
    
    return analysis

def main():
    base_path = Path("/home/ubuntu/revstream1/data_models")
    
    # Load all data models
    print("Loading data models...")
    entities = load_json(base_path / "entities/entities_refined_2025_11_20_v5.json")
    events = load_json(base_path / "events/events_refined_2025_11_20_v6.json")
    relations = load_json(base_path / "relations/relations_refined_2025_11_19_v4.json")
    timeline = load_json(base_path / "timelines/timeline_refined_2025_11_20_v5.json")
    
    # Perform analyses
    print("\n" + "="*80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS")
    print("="*80)
    
    if entities:
        print("\n### ENTITIES ANALYSIS ###")
        entity_analysis = analyze_entities(entities)
        print(f"Total Persons: {entity_analysis['total_persons']}")
        print(f"Total Organizations: {entity_analysis['total_organizations']}")
        print(f"Total Trusts: {entity_analysis['total_trusts']}")
        print(f"Persons with Evidence: {entity_analysis['persons_with_evidence']}")
        print(f"Organizations with Evidence: {entity_analysis['organizations_with_evidence']}")
        
        if entity_analysis['persons_without_evidence']:
            print(f"\nPersons WITHOUT Evidence Files: {entity_analysis['persons_without_evidence']}")
        
        if entity_analysis['organizations_without_evidence']:
            print(f"\nOrganizations WITHOUT Evidence Files: {entity_analysis['organizations_without_evidence']}")
        
        if entity_analysis['missing_ad_res_j7_refs']:
            print(f"\nEntities MISSING ad-res-j7 References: {entity_analysis['missing_ad_res_j7_refs']}")
    
    if events:
        print("\n### EVENTS ANALYSIS ###")
        event_analysis = analyze_events(events)
        print(f"Total Events: {event_analysis['total_events']}")
        print(f"Events with Evidence: {event_analysis['events_with_evidence']}")
        print(f"Events WITHOUT Evidence: {len(event_analysis['events_without_evidence'])}")
        
        print("\nEvents by Category:")
        for category, count in sorted(event_analysis['events_by_category'].items()):
            print(f"  {category}: {count}")
        
        print("\nEvents by Phase:")
        for phase, count in sorted(event_analysis['events_by_phase'].items()):
            print(f"  {phase}: {count}")
        
        if event_analysis['events_without_evidence']:
            print(f"\nFirst 10 Events WITHOUT Evidence: {event_analysis['events_without_evidence'][:10]}")
        
        if event_analysis['missing_ad_res_j7_refs']:
            print(f"\nEvents MISSING ad-res-j7 References: {len(event_analysis['missing_ad_res_j7_refs'])}")
    
    if relations:
        print("\n### RELATIONS ANALYSIS ###")
        relation_analysis = analyze_relations(relations)
        print(f"Total Relations: {relation_analysis['total_relations']}")
        print(f"Relations with Evidence: {relation_analysis['relations_with_evidence']}")
        
        print("\nRelation Types:")
        for rel_type, count in sorted(relation_analysis['relation_types'].items()):
            print(f"  {rel_type}: {count}")
        
        if relation_analysis['relations_without_evidence']:
            print(f"\nRelations WITHOUT Evidence: {relation_analysis['relations_without_evidence']}")
    
    if timeline:
        print("\n### TIMELINE ANALYSIS ###")
        timeline_analysis = analyze_timeline(timeline)
        print(f"Version: {timeline_analysis['metadata'].get('version')}")
        print(f"Total Events: {timeline_analysis['metadata'].get('total_events')}")
        print(f"Phase Count: {timeline_analysis['phase_count']}")
        
        print("\nEvents by Phase:")
        for phase_key, phase_info in timeline_analysis['events_by_phase'].items():
            print(f"  {phase_info['name']}: {phase_info['event_count']} events")
    
    # Save analysis to file
    output = {
        "analysis_date": datetime.now().isoformat(),
        "entities": entity_analysis if entities else None,
        "events": event_analysis if events else None,
        "relations": relation_analysis if relations else None,
        "timeline": timeline_analysis if timeline else None
    }
    
    output_path = Path("/home/ubuntu/revstream1/COMPREHENSIVE_ANALYSIS_2025_11_20.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n\nAnalysis saved to: {output_path}")

if __name__ == "__main__":
    main()
