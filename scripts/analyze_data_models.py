#!/usr/bin/env python3
"""
Analyze entities, relations, events, and timelines for refinement opportunities.
"""
import json
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities for completeness and evidence strength."""
    results = {
        "total_entities": 0,
        "by_type": {},
        "evidence_gaps": [],
        "missing_ad_res_j7_refs": [],
        "weak_evidence": []
    }
    
    for entity_type, entities in entities_data.get("entities", {}).items():
        results["by_type"][entity_type] = len(entities)
        results["total_entities"] += len(entities)
        
        for entity in entities:
            entity_id = entity.get("entity_id", "UNKNOWN")
            
            # Check evidence support
            evidence_support = entity.get("evidence_support", {})
            if not evidence_support or not evidence_support.get("evidence_refs"):
                results["evidence_gaps"].append({
                    "entity_id": entity_id,
                    "name": entity.get("name", "UNKNOWN"),
                    "type": entity_type
                })
            
            # Check ad-res-j7 references
            if not evidence_support.get("ad_res_j7_references"):
                results["missing_ad_res_j7_refs"].append({
                    "entity_id": entity_id,
                    "name": entity.get("name", "UNKNOWN")
                })
            
            # Check evidence strength
            if entity.get("evidence_strength") in ["weak", "moderate"]:
                results["weak_evidence"].append({
                    "entity_id": entity_id,
                    "name": entity.get("name", "UNKNOWN"),
                    "strength": entity.get("evidence_strength")
                })
    
    return results

def analyze_events(events_data):
    """Analyze events for timeline consistency and evidence."""
    results = {
        "total_events": len(events_data.get("events", [])),
        "by_category": {},
        "missing_evidence": [],
        "missing_dates": [],
        "missing_ad_res_j7_refs": []
    }
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "uncategorized")
        
        # Count by category
        results["by_category"][category] = results["by_category"].get(category, 0) + 1
        
        # Check for missing dates
        if not event.get("date"):
            results["missing_dates"].append({
                "event_id": event_id,
                "title": event.get("title", "UNKNOWN")
            })
        
        # Check evidence support
        evidence_support = event.get("evidence_support", {})
        if not event.get("evidence") and not evidence_support.get("evidence"):
            results["missing_evidence"].append({
                "event_id": event_id,
                "title": event.get("title", "UNKNOWN")
            })
        
        # Check ad-res-j7 references
        if not evidence_support.get("ad_res_j7_references"):
            results["missing_ad_res_j7_refs"].append({
                "event_id": event_id,
                "title": event.get("title", "UNKNOWN")
            })
    
    return results

def analyze_relations(relations_data):
    """Analyze relations for completeness."""
    results = {
        "total_relations": 0,
        "by_type": {},
        "missing_evidence": [],
        "missing_ad_res_j7_refs": []
    }
    
    for relation_type, relations in relations_data.get("relations", {}).items():
        results["by_type"][relation_type] = len(relations)
        results["total_relations"] += len(relations)
        
        for relation in relations:
            relation_id = relation.get("relation_id", "UNKNOWN")
            
            # Check evidence
            if not relation.get("evidence"):
                results["missing_evidence"].append({
                    "relation_id": relation_id,
                    "type": relation_type
                })
            
            # Check ad-res-j7 references
            if not relation.get("ad_res_j7_references"):
                results["missing_ad_res_j7_refs"].append({
                    "relation_id": relation_id,
                    "type": relation_type
                })
    
    return results

def main():
    # Load latest data models
    entities_file = Path("data_models/entities/entities_refined_2025_12_11_v15.json")
    events_file = Path("data_models/events/events_refined_2025_12_11_v35.json")
    relations_file = Path("data_models/relations/relations_refined_2025_12_11_v25.json")
    
    print("Loading data models...")
    entities_data = load_json(entities_file)
    events_data = load_json(events_file)
    relations_data = load_json(relations_file)
    
    print("\n=== ENTITIES ANALYSIS ===")
    entities_analysis = analyze_entities(entities_data)
    print(f"Total entities: {entities_analysis['total_entities']}")
    print(f"By type: {json.dumps(entities_analysis['by_type'], indent=2)}")
    print(f"Evidence gaps: {len(entities_analysis['evidence_gaps'])}")
    print(f"Missing ad-res-j7 refs: {len(entities_analysis['missing_ad_res_j7_refs'])}")
    print(f"Weak evidence: {len(entities_analysis['weak_evidence'])}")
    
    print("\n=== EVENTS ANALYSIS ===")
    events_analysis = analyze_events(events_data)
    print(f"Total events: {events_analysis['total_events']}")
    print(f"By category: {json.dumps(events_analysis['by_category'], indent=2)}")
    print(f"Missing evidence: {len(events_analysis['missing_evidence'])}")
    print(f"Missing dates: {len(events_analysis['missing_dates'])}")
    print(f"Missing ad-res-j7 refs: {len(events_analysis['missing_ad_res_j7_refs'])}")
    
    print("\n=== RELATIONS ANALYSIS ===")
    relations_analysis = analyze_relations(relations_data)
    print(f"Total relations: {relations_analysis['total_relations']}")
    print(f"By type: {json.dumps(relations_analysis['by_type'], indent=2)}")
    print(f"Missing evidence: {len(relations_analysis['missing_evidence'])}")
    print(f"Missing ad-res-j7 refs: {len(relations_analysis['missing_ad_res_j7_refs'])}")
    
    # Save analysis report
    report = {
        "generated": datetime.now().isoformat(),
        "entities": entities_analysis,
        "events": events_analysis,
        "relations": relations_analysis,
        "recommendations": [
            "Add missing ad-res-j7 references to all entities, events, and relations",
            "Strengthen evidence for weak/moderate entities",
            "Fill evidence gaps for entities without evidence_refs",
            "Add dates to events missing temporal information",
            "Cross-reference all data with COMPREHENSIVE_EVIDENCE_INDEX.md from ad-res-j7"
        ]
    }
    
    with open("DATA_MODEL_ANALYSIS_2025_12_13.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("\n✓ Analysis complete. Report saved to DATA_MODEL_ANALYSIS_2025_12_13.json")

if __name__ == "__main__":
    main()
