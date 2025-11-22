#!/usr/bin/env python3
"""
Comprehensive Analysis of revstream1 Data Models
Date: 2025-11-22
Purpose: Analyze entities, relations, events, and timelines for refinement
"""

import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_file):
    """Analyze entities for completeness and consistency"""
    data = load_json(entities_file)
    
    analysis = {
        "file": entities_file,
        "metadata": data.get("metadata", {}),
        "total_entities": 0,
        "entity_types": defaultdict(int),
        "entities_without_evidence": [],
        "entities_without_ad_res_j7": [],
        "entities_missing_timeline_events": [],
        "entities_by_role": defaultdict(list)
    }
    
    for entity_type, entities in data.get("entities", {}).items():
        if isinstance(entities, list):
            analysis["total_entities"] += len(entities)
            analysis["entity_types"][entity_type] = len(entities)
            
            for entity in entities:
                entity_id = entity.get("entity_id", "UNKNOWN")
                
                # Check for evidence files
                if not entity.get("evidence_files") or len(entity.get("evidence_files", [])) == 0:
                    analysis["entities_without_evidence"].append(entity_id)
                
                # Check for ad-res-j7 references
                if not entity.get("ad_res_j7_references") or len(entity.get("ad_res_j7_references", [])) == 0:
                    analysis["entities_without_ad_res_j7"].append(entity_id)
                
                # Check for timeline events
                if not entity.get("timeline_events") or len(entity.get("timeline_events", [])) == 0:
                    analysis["entities_missing_timeline_events"].append(entity_id)
                
                # Group by role
                role = entity.get("role", "unknown")
                analysis["entities_by_role"][role].append(entity_id)
    
    return analysis

def analyze_relations(relations_file):
    """Analyze relations for completeness"""
    data = load_json(relations_file)
    
    analysis = {
        "file": relations_file,
        "metadata": data.get("metadata", {}),
        "total_relations": 0,
        "relation_types": defaultdict(int),
        "relations_without_evidence": [],
        "relations_without_events": [],
        "relation_categories": defaultdict(int)
    }
    
    # Handle nested structure
    relations_data = data.get("relations", {})
    if isinstance(relations_data, dict):
        for category, relations_list in relations_data.items():
            if isinstance(relations_list, list):
                analysis["relation_categories"][category] = len(relations_list)
                analysis["total_relations"] += len(relations_list)
                
                for relation in relations_list:
                    if isinstance(relation, dict):
                        rel_type = relation.get("relation_type", "unknown")
                        analysis["relation_types"][rel_type] += 1
                        
                        rel_id = relation.get("relation_id", "UNKNOWN")
                        
                        if not relation.get("evidence") and not relation.get("evidence_files"):
                            analysis["relations_without_evidence"].append(rel_id)
                        
                        if not relation.get("related_events"):
                            analysis["relations_without_events"].append(rel_id)
    
    return analysis

def analyze_events(events_file):
    """Analyze events for completeness"""
    data = load_json(events_file)
    
    analysis = {
        "file": events_file,
        "metadata": data.get("metadata", {}),
        "total_events": len(data.get("events", [])),
        "events_by_category": defaultdict(int),
        "events_without_evidence": [],
        "events_without_financial_impact": [],
        "events_without_legal_significance": [],
        "events_by_phase": defaultdict(list)
    }
    
    for event in data.get("events", []):
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "unknown")
        analysis["events_by_category"][category] += 1
        
        if not event.get("evidence_files") or len(event.get("evidence_files", [])) == 0:
            analysis["events_without_evidence"].append(event_id)
        
        if not event.get("financial_impact"):
            analysis["events_without_financial_impact"].append(event_id)
        
        if not event.get("legal_significance"):
            analysis["events_without_legal_significance"].append(event_id)
        
        phase = event.get("timeline_phase", "unknown")
        analysis["events_by_phase"][phase].append(event_id)
    
    return analysis

def analyze_timeline(timeline_file):
    """Analyze timeline for completeness"""
    data = load_json(timeline_file)
    
    analysis = {
        "file": timeline_file,
        "metadata": data.get("metadata", {}),
        "total_phases": len(data.get("timeline_phases", {})),
        "phases": {}
    }
    
    for phase_key, phase_data in data.get("timeline_phases", {}).items():
        phase_id = phase_data.get("phase_id", "UNKNOWN")
        analysis["phases"][phase_id] = {
            "name": phase_data.get("phase_name", ""),
            "start_date": phase_data.get("start_date", ""),
            "end_date": phase_data.get("end_date", ""),
            "duration_days": phase_data.get("duration_days", 0),
            "event_count": phase_data.get("event_count", 0),
            "events": phase_data.get("events", []),
            "financial_impact": phase_data.get("financial_impact", ""),
            "missing_evidence_repo": not phase_data.get("evidence_repository"),
            "missing_applications": not phase_data.get("related_applications")
        }
    
    return analysis

def main():
    """Main analysis function"""
    base_dir = "/home/ubuntu/revstream1/data_models"
    
    # Latest files
    entities_file = f"{base_dir}/entities/entities_refined_2025_11_21_v8.json"
    relations_file = f"{base_dir}/relations/relations_refined_2025_11_21_v6.json"
    events_file = f"{base_dir}/events/events_refined_2025_11_21_v9.json"
    timeline_file = f"{base_dir}/timelines/timeline_refined_2025_11_21_v7.json"
    
    results = {
        "analysis_date": datetime.now().isoformat(),
        "entities_analysis": analyze_entities(entities_file),
        "relations_analysis": analyze_relations(relations_file),
        "events_analysis": analyze_events(events_file),
        "timeline_analysis": analyze_timeline(timeline_file)
    }
    
    # Save results
    output_file = "/home/ubuntu/revstream1/COMPREHENSIVE_ANALYSIS_2025_11_22.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Analysis complete. Results saved to {output_file}")
    
    # Print summary
    print("\n=== ANALYSIS SUMMARY ===\n")
    print(f"Entities: {results['entities_analysis']['total_entities']}")
    print(f"  - Without evidence: {len(results['entities_analysis']['entities_without_evidence'])}")
    print(f"  - Without ad-res-j7 refs: {len(results['entities_analysis']['entities_without_ad_res_j7'])}")
    print(f"  - Without timeline events: {len(results['entities_analysis']['entities_missing_timeline_events'])}")
    
    print(f"\nRelations: {results['relations_analysis']['total_relations']}")
    print(f"  - Without evidence: {len(results['relations_analysis']['relations_without_evidence'])}")
    print(f"  - Without events: {len(results['relations_analysis']['relations_without_events'])}")
    
    print(f"\nEvents: {results['events_analysis']['total_events']}")
    print(f"  - Without evidence: {len(results['events_analysis']['events_without_evidence'])}")
    print(f"  - Without financial impact: {len(results['events_analysis']['events_without_financial_impact'])}")
    print(f"  - Without legal significance: {len(results['events_analysis']['events_without_legal_significance'])}")
    
    print(f"\nTimeline Phases: {results['timeline_analysis']['total_phases']}")

if __name__ == "__main__":
    main()
