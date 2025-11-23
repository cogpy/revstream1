import json
import os
from datetime import datetime
from collections import defaultdict

def analyze_json_file(filepath):
    """Load and return JSON data from file"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_entities(entities_file):
    """Analyze entities structure"""
    data = analyze_json_file(entities_file)
    if not data:
        return None
    
    analysis = {
        "file": entities_file,
        "metadata": data.get("metadata", {}),
        "total_entities": 0,
        "entity_types": {},
        "entities_by_role": defaultdict(list),
        "entities_with_timeline_events": 0,
        "entities_with_evidence": 0,
        "entities_with_ad_res_j7": 0,
        "issues": []
    }
    
    entities = data.get("entities", {})
    
    for entity_type, entity_list in entities.items():
        analysis["entity_types"][entity_type] = len(entity_list)
        analysis["total_entities"] += len(entity_list)
        
        for entity in entity_list:
            entity_id = entity.get("entity_id", "UNKNOWN")
            role = entity.get("role", "UNKNOWN")
            analysis["entities_by_role"][role].append(entity_id)
            
            # Check for timeline events
            if entity.get("timeline_events"):
                analysis["entities_with_timeline_events"] += 1
            else:
                analysis["issues"].append(f"{entity_id} missing timeline_events")
            
            # Check for evidence files
            if entity.get("evidence_files"):
                analysis["entities_with_evidence"] += 1
            else:
                analysis["issues"].append(f"{entity_id} missing evidence_files")
            
            # Check for ad-res-j7 references
            if entity.get("ad_res_j7_references"):
                analysis["entities_with_ad_res_j7"] += 1
            else:
                analysis["issues"].append(f"{entity_id} missing ad_res_j7_references")
    
    return analysis

def analyze_events(events_file):
    """Analyze events structure"""
    data = analyze_json_file(events_file)
    if not data:
        return None
    
    analysis = {
        "file": events_file,
        "metadata": data.get("metadata", {}),
        "total_events": 0,
        "events_by_category": defaultdict(int),
        "events_by_phase": defaultdict(int),
        "events_with_evidence": 0,
        "events_with_financial_impact": 0,
        "events_with_ad_res_j7": 0,
        "issues": []
    }
    
    events = data.get("events", [])
    analysis["total_events"] = len(events)
    
    for event in events:
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "UNKNOWN")
        phase = event.get("phase", "UNKNOWN")
        
        analysis["events_by_category"][category] += 1
        analysis["events_by_phase"][phase] += 1
        
        # Check for evidence
        if event.get("evidence_files"):
            analysis["events_with_evidence"] += 1
        else:
            analysis["issues"].append(f"{event_id} missing evidence_files")
        
        # Check for financial impact
        if event.get("financial_impact"):
            analysis["events_with_financial_impact"] += 1
        
        # Check for ad-res-j7 references
        if event.get("ad_res_j7_references"):
            analysis["events_with_ad_res_j7"] += 1
        else:
            analysis["issues"].append(f"{event_id} missing ad_res_j7_references")
    
    return analysis

def analyze_relations(relations_file):
    """Analyze relations structure"""
    data = analyze_json_file(relations_file)
    if not data:
        return None
    
    analysis = {
        "file": relations_file,
        "metadata": data.get("metadata", {}),
        "total_relations": 0,
        "relations_by_type": defaultdict(int),
        "relations_with_evidence": 0,
        "relations_with_ad_res_j7": 0,
        "issues": []
    }
    
    relations = data.get("relations", {})
    
    # Handle nested structure
    for relation_category, relation_list in relations.items():
        if isinstance(relation_list, list):
            analysis["total_relations"] += len(relation_list)
            
            for relation in relation_list:
                if isinstance(relation, dict):
                    relation_id = relation.get("relation_id", "UNKNOWN")
                    relation_type = relation.get("relation_type", "UNKNOWN")
                    
                    analysis["relations_by_type"][relation_type] += 1
                    
                    # Check for evidence
                    if relation.get("evidence") or relation.get("evidence_files"):
                        analysis["relations_with_evidence"] += 1
                    else:
                        analysis["issues"].append(f"{relation_id} missing evidence")
                    
                    # Check for ad-res-j7 references
                    if relation.get("evidence_repository"):
                        analysis["relations_with_ad_res_j7"] += 1
                    else:
                        analysis["issues"].append(f"{relation_id} missing evidence_repository")
    
    return analysis

def analyze_timeline(timeline_file):
    """Analyze timeline structure"""
    data = analyze_json_file(timeline_file)
    if not data:
        return None
    
    analysis = {
        "file": timeline_file,
        "metadata": data.get("metadata", {}),
        "total_phases": 0,
        "phases": {},
        "issues": []
    }
    
    phases = data.get("timeline_phases", {})
    analysis["total_phases"] = len(phases)
    
    for phase_key, phase_data in phases.items():
        phase_id = phase_data.get("phase_id", "UNKNOWN")
        analysis["phases"][phase_id] = {
            "name": phase_data.get("phase_name"),
            "start_date": phase_data.get("start_date"),
            "end_date": phase_data.get("end_date"),
            "duration_days": phase_data.get("duration_days"),
            "event_count": phase_data.get("event_count", 0),
            "events": phase_data.get("events", []),
            "financial_impact": phase_data.get("financial_impact"),
            "has_evidence_repo": "evidence_repository" in phase_data
        }
        
        # Check for issues
        if not phase_data.get("events"):
            analysis["issues"].append(f"{phase_id} has no events")
        
        if not phase_data.get("evidence_repository"):
            analysis["issues"].append(f"{phase_id} missing evidence_repository")
    
    return analysis

def main():
    # Analyze latest versions
    entities_analysis = analyze_entities("data_models/entities/entities_refined_2025_11_22_v9.json")
    events_analysis = analyze_events("data_models/events/events_refined_2025_11_22_v10.json")
    relations_analysis = analyze_relations("data_models/relations/relations_refined_2025_11_22_v7.json")
    timeline_analysis = analyze_timeline("data_models/timelines/timeline_refined_2025_11_22_v8.json")
    
    # Compile comprehensive report
    report = {
        "analysis_date": datetime.now().isoformat(),
        "entities": entities_analysis,
        "events": events_analysis,
        "relations": relations_analysis,
        "timeline": timeline_analysis,
        "summary": {
            "total_entities": entities_analysis["total_entities"] if entities_analysis else 0,
            "total_events": events_analysis["total_events"] if events_analysis else 0,
            "total_relations": relations_analysis["total_relations"] if relations_analysis else 0,
            "total_phases": timeline_analysis["total_phases"] if timeline_analysis else 0,
            "total_issues": (
                len(entities_analysis.get("issues", [])) +
                len(events_analysis.get("issues", [])) +
                len(relations_analysis.get("issues", [])) +
                len(timeline_analysis.get("issues", []))
            )
        }
    }
    
    # Save report
    with open("DATA_MODEL_COMPREHENSIVE_ANALYSIS_2025_11_23.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print("Analysis complete!")
    print(f"Total Entities: {report['summary']['total_entities']}")
    print(f"Total Events: {report['summary']['total_events']}")
    print(f"Total Relations: {report['summary']['total_relations']}")
    print(f"Total Phases: {report['summary']['total_phases']}")
    print(f"Total Issues: {report['summary']['total_issues']}")

if __name__ == "__main__":
    main()
