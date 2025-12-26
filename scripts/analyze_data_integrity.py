import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities structure"""
    analysis = {
        "total_entities": 0,
        "by_type": {},
        "missing_timeline_events": [],
        "entities_without_events": [],
        "financial_impact_summary": {}
    }
    
    for entity_type, entities_list in entities_data.get("entities", {}).items():
        if isinstance(entities_list, list):
            analysis["total_entities"] += len(entities_list)
            analysis["by_type"][entity_type] = len(entities_list)
            
            for entity in entities_list:
                entity_id = entity.get("entity_id", "UNKNOWN")
                
                # Check for entities without timeline events
                timeline_events = entity.get("timeline_events", [])
                if not timeline_events and entity.get("involvement_events", 0) > 0:
                    analysis["entities_without_events"].append({
                        "entity_id": entity_id,
                        "name": entity.get("name", "N/A"),
                        "involvement_events": entity.get("involvement_events", 0)
                    })
                
                # Collect financial impact
                if "financial_impact" in entity:
                    analysis["financial_impact_summary"][entity_id] = entity["financial_impact"]
    
    return analysis

def analyze_events(events_data):
    """Analyze events structure"""
    analysis = {
        "total_events": len(events_data.get("events", [])),
        "by_category": defaultdict(int),
        "by_phase": defaultdict(int),
        "events_without_evidence": [],
        "events_without_perpetrators": [],
        "duplicate_event_ids": [],
        "financial_impact_total": 0,
        "events_with_financial_impact": 0
    }
    
    event_ids = set()
    for event in events_data.get("events", []):
        event_id = event.get("event_id")
        
        # Check for duplicates
        if event_id in event_ids:
            analysis["duplicate_event_ids"].append(event_id)
        event_ids.add(event_id)
        
        # Category analysis
        category = event.get("category", "uncategorized")
        analysis["by_category"][category] += 1
        
        # Phase analysis
        phase = event.get("timeline_phase", "unassigned")
        analysis["by_phase"][phase] += 1
        
        # Evidence check
        evidence = event.get("evidence", [])
        if not evidence:
            analysis["events_without_evidence"].append({
                "event_id": event_id,
                "title": event.get("title", "N/A"),
                "date": event.get("date", "N/A")
            })
        
        # Perpetrators check
        perpetrators = event.get("perpetrators", [])
        if not perpetrators and event.get("category") not in ["business_relationship", "financial_structure"]:
            analysis["events_without_perpetrators"].append({
                "event_id": event_id,
                "title": event.get("title", "N/A")
            })
        
        # Financial impact
        if "financial_impact" in event and event["financial_impact"] != "unknown":
            analysis["events_with_financial_impact"] += 1
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations structure"""
    analysis = {
        "total_relations": 0,
        "by_type": defaultdict(int),
        "relations_without_evidence": [],
        "orphaned_relations": []
    }
    
    for relation_type, relations_list in relations_data.get("relations", {}).items():
        if isinstance(relations_list, list):
            analysis["total_relations"] += len(relations_list)
            
            for relation in relations_list:
                rel_id = relation.get("relation_id", "UNKNOWN")
                analysis["by_type"][relation_type] += 1
                
                # Evidence check
                evidence = relation.get("evidence", [])
                if not evidence:
                    analysis["relations_without_evidence"].append({
                        "relation_id": rel_id,
                        "type": relation.get("relation_type", "N/A"),
                        "source": relation.get("source_entity", "N/A"),
                        "target": relation.get("target_entity", "N/A")
                    })
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline structure"""
    analysis = {
        "total_phases": 0,
        "events_per_phase": {},
        "phase_durations": {},
        "unassigned_events": [],
        "phase_financial_impact": {}
    }
    
    phases = timeline_data.get("timeline_phases", {})
    for phase_key, phase_data in phases.items():
        if isinstance(phase_data, dict):
            analysis["total_phases"] += 1
            phase_id = phase_data.get("phase_id", phase_key)
            
            events = phase_data.get("events", [])
            analysis["events_per_phase"][phase_id] = len(events)
            
            duration = phase_data.get("duration_days", 0)
            analysis["phase_durations"][phase_id] = duration
            
            financial_impact = phase_data.get("financial_impact", "N/A")
            analysis["phase_financial_impact"][phase_id] = financial_impact
    
    return analysis

def main():
    """Main analysis function"""
    base_path = "/home/ubuntu/revstream1/data_models"
    
    # Load data
    entities = load_json(f"{base_path}/entities/entities_refined_2025_11_19.json")
    events = load_json(f"{base_path}/events/events_refined_2025_11_19.json")
    relations = load_json(f"{base_path}/relations/relations_refined_2025_11_19.json")
    timeline = load_json(f"{base_path}/timelines/timeline_refined_2025_11_19.json")
    
    # Perform analysis
    print("=" * 80)
    print("DATA MODEL INTEGRITY ANALYSIS - 2025-11-19")
    print("=" * 80)
    
    print("\n### ENTITIES ANALYSIS ###")
    entities_analysis = analyze_entities(entities)
    print(f"Total Entities: {entities_analysis['total_entities']}")
    print(f"By Type: {dict(entities_analysis['by_type'])}")
    print(f"Entities Without Timeline Events: {len(entities_analysis['entities_without_events'])}")
    if entities_analysis['entities_without_events']:
        for e in entities_analysis['entities_without_events'][:5]:
            print(f"  - {e['entity_id']}: {e['name']} (involvement: {e['involvement_events']})")
    
    print("\n### EVENTS ANALYSIS ###")
    events_analysis = analyze_events(events)
    print(f"Total Events: {events_analysis['total_events']}")
    print(f"Events with Financial Impact: {events_analysis['events_with_financial_impact']}")
    print(f"By Category: {dict(events_analysis['by_category'])}")
    print(f"Events Without Evidence: {len(events_analysis['events_without_evidence'])}")
    if events_analysis['events_without_evidence']:
        for e in events_analysis['events_without_evidence'][:5]:
            print(f"  - {e['event_id']}: {e['title']}")
    print(f"Events Without Perpetrators: {len(events_analysis['events_without_perpetrators'])}")
    print(f"Duplicate Event IDs: {len(events_analysis['duplicate_event_ids'])}")
    if events_analysis['duplicate_event_ids']:
        print(f"  - {events_analysis['duplicate_event_ids']}")
    
    print("\n### RELATIONS ANALYSIS ###")
    relations_analysis = analyze_relations(relations)
    print(f"Total Relations: {relations_analysis['total_relations']}")
    print(f"By Type: {dict(relations_analysis['by_type'])}")
    print(f"Relations Without Evidence: {len(relations_analysis['relations_without_evidence'])}")
    if relations_analysis['relations_without_evidence']:
        for r in relations_analysis['relations_without_evidence'][:5]:
            print(f"  - {r['relation_id']}: {r['type']} ({r['source']} -> {r['target']})")
    
    print("\n### TIMELINE ANALYSIS ###")
    timeline_analysis = analyze_timeline(timeline)
    print(f"Total Phases: {timeline_analysis['total_phases']}")
    print(f"Events Per Phase: {dict(timeline_analysis['events_per_phase'])}")
    print(f"Phase Durations (days): {dict(timeline_analysis['phase_durations'])}")
    
    # Save detailed analysis
    output = {
        "analysis_date": datetime.now().isoformat(),
        "entities": entities_analysis,
        "events": events_analysis,
        "relations": relations_analysis,
        "timeline": timeline_analysis
    }
    
    with open("/home/ubuntu/revstream1/DATA_INTEGRITY_ANALYSIS_2025_11_19.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print("\n" + "=" * 80)
    print("Analysis complete. Detailed report saved to DATA_INTEGRITY_ANALYSIS_2025_11_19.json")
    print("=" * 80)

if __name__ == "__main__":
    main()
