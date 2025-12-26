#!/usr/bin/env python3
"""
Comprehensive analysis of current data models state
"""
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
        "entities_by_type": defaultdict(int),
        "entities_with_evidence": 0,
        "entities_with_ad_res_j7": 0,
        "entities_with_github_pages": 0,
        "entities_missing_evidence": [],
        "entities_missing_cross_refs": []
    }
    
    for entity_type, entities in entities_data.get("entities", {}).items():
        if isinstance(entities, list):
            for entity in entities:
                analysis["total_entities"] += 1
                analysis["entities_by_type"][entity_type] += 1
                
                entity_id = entity.get("entity_id", "UNKNOWN")
                
                # Check evidence files
                if entity.get("evidence_files"):
                    analysis["entities_with_evidence"] += 1
                else:
                    analysis["entities_missing_evidence"].append(entity_id)
                
                # Check ad-res-j7 references
                if entity.get("ad_res_j7_references"):
                    analysis["entities_with_ad_res_j7"] += 1
                else:
                    analysis["entities_missing_cross_refs"].append(entity_id)
                
                # Check GitHub Pages reference
                if entity.get("github_pages_reference"):
                    analysis["entities_with_github_pages"] += 1
    
    return analysis

def analyze_events(events_data):
    """Analyze events structure"""
    analysis = {
        "total_events": 0,
        "events_by_category": defaultdict(int),
        "events_with_evidence": 0,
        "events_with_financial_impact": 0,
        "events_missing_evidence": [],
        "events_missing_cross_refs": [],
        "timeline_coverage": defaultdict(int)
    }
    
    for event in events_data.get("events", []):
        analysis["total_events"] += 1
        
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "uncategorized")
        analysis["events_by_category"][category] += 1
        
        # Check evidence
        if event.get("evidence_files") or event.get("evidence_repository"):
            analysis["events_with_evidence"] += 1
        else:
            analysis["events_missing_evidence"].append(event_id)
        
        # Check financial impact
        if event.get("financial_impact"):
            analysis["events_with_financial_impact"] += 1
        
        # Check cross-references
        if not event.get("ad_res_j7_references"):
            analysis["events_missing_cross_refs"].append(event_id)
        
        # Timeline coverage
        date = event.get("date", "unknown")
        if date != "unknown":
            year_month = date[:7] if len(date) >= 7 else date
            analysis["timeline_coverage"][year_month] += 1
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations structure"""
    analysis = {
        "total_relations": 0,
        "relations_by_type": defaultdict(int),
        "relations_with_evidence": 0,
        "relations_missing_evidence": []
    }
    
    # Relations are organized by type
    for relation_type, relations in relations_data.get("relations", {}).items():
        if isinstance(relations, list):
            for relation in relations:
                if isinstance(relation, dict):
                    analysis["total_relations"] += 1
                    
                    rel_type = relation.get("relation_type", "unknown")
                    analysis["relations_by_type"][rel_type] += 1
                    
                    relation_id = relation.get("relation_id", "UNKNOWN")
                    
                    # Check evidence
                    if relation.get("evidence") or relation.get("evidence_repository"):
                        analysis["relations_with_evidence"] += 1
                    else:
                        analysis["relations_missing_evidence"].append(relation_id)
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline structure"""
    analysis = {
        "total_phases": 0,
        "phases": [],
        "total_events_in_phases": 0,
        "phase_gaps": [],
        "phases_missing_evidence": []
    }
    
    phases = timeline_data.get("timeline_phases", {})
    for phase_key, phase_data in phases.items():
        analysis["total_phases"] += 1
        
        phase_info = {
            "phase_id": phase_data.get("phase_id"),
            "phase_name": phase_data.get("phase_name"),
            "start_date": phase_data.get("start_date"),
            "end_date": phase_data.get("end_date"),
            "event_count": len(phase_data.get("events", [])),
            "financial_impact": phase_data.get("financial_impact", "Unknown")
        }
        analysis["phases"].append(phase_info)
        analysis["total_events_in_phases"] += phase_info["event_count"]
        
        # Check for evidence references
        if not phase_data.get("evidence_repository"):
            analysis["phases_missing_evidence"].append(phase_data.get("phase_id"))
    
    return analysis

def main():
    """Main analysis function"""
    base_path = "/home/ubuntu/revstream1/data_models"
    
    # Load latest data models
    entities_path = f"{base_path}/entities/entities_refined_2025_11_23_v10.json"
    events_path = f"{base_path}/events/events_refined_2025_11_23_v11.json"
    relations_path = f"{base_path}/relations/relations_refined_2025_11_23_v8.json"
    timeline_path = f"{base_path}/timelines/timeline_refined_2025_11_23_v9.json"
    
    print("Loading data models...")
    entities_data = load_json(entities_path)
    events_data = load_json(events_path)
    relations_data = load_json(relations_path)
    timeline_data = load_json(timeline_path)
    
    print("\n=== ANALYZING ENTITIES ===")
    entities_analysis = analyze_entities(entities_data)
    print(json.dumps(entities_analysis, indent=2, default=str))
    
    print("\n=== ANALYZING EVENTS ===")
    events_analysis = analyze_events(events_data)
    print(json.dumps(events_analysis, indent=2, default=str))
    
    print("\n=== ANALYZING RELATIONS ===")
    relations_analysis = analyze_relations(relations_data)
    print(json.dumps(relations_analysis, indent=2, default=str))
    
    print("\n=== ANALYZING TIMELINE ===")
    timeline_analysis = analyze_timeline(timeline_data)
    print(json.dumps(timeline_analysis, indent=2, default=str))
    
    # Generate comprehensive report
    report = {
        "analysis_date": datetime.now().isoformat(),
        "entities": entities_analysis,
        "events": events_analysis,
        "relations": relations_analysis,
        "timeline": timeline_analysis,
        "metadata": {
            "entities_version": entities_data.get("metadata", {}).get("version"),
            "events_version": events_data.get("metadata", {}).get("version"),
            "relations_version": relations_data.get("metadata", {}).get("version"),
            "timeline_version": timeline_data.get("metadata", {}).get("version")
        }
    }
    
    # Save report
    report_path = "/home/ubuntu/revstream1/CURRENT_STATE_ANALYSIS_2025_11_24.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"\n✅ Report saved to: {report_path}")

if __name__ == "__main__":
    main()
