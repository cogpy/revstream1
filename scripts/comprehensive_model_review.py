#!/usr/bin/env python3
"""
Comprehensive Model Review Script
Analyzes entities, relations, events, and timelines for completeness and quality
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_file):
    """Analyze entities model"""
    data = load_json(entities_file)
    
    analysis = {
        "file": str(entities_file),
        "metadata": data.get("metadata", {}),
        "statistics": {},
        "issues": [],
        "recommendations": []
    }
    
    entities = data.get("entities", {})
    
    # Count entities by type
    for entity_type, entity_list in entities.items():
        analysis["statistics"][entity_type] = len(entity_list)
    
    # Check for missing evidence references
    missing_evidence = []
    missing_ad_res = []
    
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            entity_id = entity.get("entity_id", entity.get("name", "unknown"))
            
            if not entity.get("evidence_files"):
                missing_evidence.append(f"{entity_type}/{entity_id}")
            
            if not entity.get("ad_res_j7_references"):
                missing_ad_res.append(f"{entity_type}/{entity_id}")
    
    if missing_evidence:
        analysis["issues"].append({
            "type": "missing_evidence_files",
            "count": len(missing_evidence),
            "entities": missing_evidence[:10]  # First 10
        })
    
    if missing_ad_res:
        analysis["issues"].append({
            "type": "missing_ad_res_j7_references",
            "count": len(missing_ad_res),
            "entities": missing_ad_res[:10]  # First 10
        })
    
    return analysis

def analyze_events(events_file):
    """Analyze events model"""
    data = load_json(events_file)
    
    analysis = {
        "file": str(events_file),
        "metadata": data.get("metadata", {}),
        "statistics": {},
        "issues": [],
        "recommendations": []
    }
    
    events = data.get("events", [])
    analysis["statistics"]["total_events"] = len(events)
    
    # Categorize events
    categories = defaultdict(int)
    phases = defaultdict(int)
    applications = defaultdict(int)
    
    missing_evidence = []
    missing_applications = []
    missing_categories = []
    
    for event in events:
        event_id = event.get("event_id", "unknown")
        
        # Count categories
        category = event.get("category")
        if category:
            categories[category] += 1
        else:
            missing_categories.append(event_id)
        
        # Count phases
        phase = event.get("timeline_phase")
        if phase:
            phases[phase] += 1
        
        # Count applications
        apps = event.get("related_applications", [])
        if apps:
            for app in apps:
                applications[app] += 1
        else:
            missing_applications.append(event_id)
        
        # Check evidence
        if not event.get("evidence_files"):
            missing_evidence.append(event_id)
    
    analysis["statistics"]["categories"] = dict(categories)
    analysis["statistics"]["phases"] = dict(phases)
    analysis["statistics"]["applications"] = dict(applications)
    
    if missing_evidence:
        analysis["issues"].append({
            "type": "missing_evidence_files",
            "count": len(missing_evidence),
            "events": missing_evidence[:10]
        })
    
    if missing_applications:
        analysis["issues"].append({
            "type": "missing_related_applications",
            "count": len(missing_applications),
            "events": missing_applications[:10]
        })
    
    if missing_categories:
        analysis["issues"].append({
            "type": "missing_categories",
            "count": len(missing_categories),
            "events": missing_categories
        })
    
    return analysis

def analyze_relations(relations_file):
    """Analyze relations model"""
    data = load_json(relations_file)
    
    analysis = {
        "file": str(relations_file),
        "metadata": data.get("metadata", {}),
        "statistics": {},
        "issues": [],
        "recommendations": []
    }
    
    relations = data.get("relations", {})
    
    # Count relations by type
    total_relations = 0
    for relation_type, relation_list in relations.items():
        count = len(relation_list)
        analysis["statistics"][relation_type] = count
        total_relations += count
    
    analysis["statistics"]["total_relations"] = total_relations
    
    # Check for missing evidence and applications
    missing_evidence = []
    missing_applications = []
    
    for relation_type, relation_list in relations.items():
        for relation in relation_list:
            relation_id = relation.get("relation_id", "unknown")
            
            if not relation.get("evidence"):
                missing_evidence.append(f"{relation_type}/{relation_id}")
            
            if not relation.get("related_applications"):
                missing_applications.append(f"{relation_type}/{relation_id}")
    
    if missing_evidence:
        analysis["issues"].append({
            "type": "missing_evidence",
            "count": len(missing_evidence),
            "relations": missing_evidence[:10]
        })
    
    if missing_applications:
        analysis["issues"].append({
            "type": "missing_related_applications",
            "count": len(missing_applications),
            "relations": missing_applications[:10]
        })
    
    return analysis

def analyze_timeline(timeline_file):
    """Analyze timeline model"""
    data = load_json(timeline_file)
    
    analysis = {
        "file": str(timeline_file),
        "metadata": data.get("metadata", {}),
        "statistics": {},
        "issues": [],
        "recommendations": []
    }
    
    phases = data.get("timeline_phases", {})
    analysis["statistics"]["total_phases"] = len(phases)
    
    # Analyze each phase
    phase_details = {}
    for phase_key, phase_data in phases.items():
        phase_id = phase_data.get("phase_id")
        phase_details[phase_id] = {
            "name": phase_data.get("phase_name"),
            "event_count": len(phase_data.get("events", [])),
            "duration_days": phase_data.get("duration_days"),
            "financial_impact": phase_data.get("financial_impact"),
            "has_applications": bool(phase_data.get("related_applications"))
        }
    
    analysis["statistics"]["phases"] = phase_details
    
    # Check for missing application mappings
    missing_apps = []
    for phase_key, phase_data in phases.items():
        if not phase_data.get("related_applications"):
            missing_apps.append(phase_data.get("phase_id"))
    
    if missing_apps:
        analysis["issues"].append({
            "type": "missing_application_mappings",
            "count": len(missing_apps),
            "phases": missing_apps
        })
    
    return analysis

def generate_recommendations(all_analyses):
    """Generate recommendations based on all analyses"""
    recommendations = []
    
    # Check entities
    entities_analysis = all_analyses.get("entities", {})
    for issue in entities_analysis.get("issues", []):
        if issue["type"] == "missing_evidence_files":
            recommendations.append({
                "priority": "HIGH",
                "category": "entities",
                "issue": "Missing evidence_files references",
                "affected_count": issue["count"],
                "action": "Add evidence_files arrays to all entities with references to ad-res-j7 repository"
            })
        if issue["type"] == "missing_ad_res_j7_references":
            recommendations.append({
                "priority": "HIGH",
                "category": "entities",
                "issue": "Missing ad_res_j7_references",
                "affected_count": issue["count"],
                "action": "Add ad_res_j7_references arrays to all entities with descriptive evidence notes"
            })
    
    # Check events
    events_analysis = all_analyses.get("events", {})
    for issue in events_analysis.get("issues", []):
        if issue["type"] == "missing_evidence_files":
            recommendations.append({
                "priority": "HIGH",
                "category": "events",
                "issue": "Missing evidence_files references",
                "affected_count": issue["count"],
                "action": "Add evidence_files arrays to all events with specific file paths from ad-res-j7"
            })
        if issue["type"] == "missing_related_applications":
            recommendations.append({
                "priority": "MEDIUM",
                "category": "events",
                "issue": "Missing related_applications mappings",
                "affected_count": issue["count"],
                "action": "Map each event to relevant applications (APPLICATION_1, APPLICATION_2, APPLICATION_3)"
            })
    
    # Check relations
    relations_analysis = all_analyses.get("relations", {})
    for issue in relations_analysis.get("issues", []):
        if issue["type"] == "missing_evidence":
            recommendations.append({
                "priority": "MEDIUM",
                "category": "relations",
                "issue": "Missing evidence references",
                "affected_count": issue["count"],
                "action": "Add evidence arrays to all relations"
            })
        if issue["type"] == "missing_related_applications":
            recommendations.append({
                "priority": "MEDIUM",
                "category": "relations",
                "issue": "Missing related_applications mappings",
                "affected_count": issue["count"],
                "action": "Map each relation to relevant applications"
            })
    
    # Check timeline
    timeline_analysis = all_analyses.get("timeline", {})
    for issue in timeline_analysis.get("issues", []):
        if issue["type"] == "missing_application_mappings":
            recommendations.append({
                "priority": "MEDIUM",
                "category": "timeline",
                "issue": "Missing application mappings in phases",
                "affected_count": issue["count"],
                "action": "Add related_applications to all timeline phases"
            })
    
    return recommendations

def main():
    """Main analysis function"""
    base_dir = Path("/home/ubuntu/revstream1/data_models")
    
    # Find latest versions
    entities_file = base_dir / "entities/entities_refined_2025_11_20_v5.json"
    events_file = base_dir / "events/events_refined_2025_11_20_v7.json"
    relations_file = base_dir / "relations/relations_refined_2025_11_19_v4.json"
    timeline_file = base_dir / "timelines/timeline_refined_2025_11_20_v5.json"
    
    print("=" * 80)
    print("COMPREHENSIVE MODEL REVIEW")
    print("=" * 80)
    print()
    
    all_analyses = {}
    
    # Analyze entities
    print("Analyzing entities...")
    all_analyses["entities"] = analyze_entities(entities_file)
    
    # Analyze events
    print("Analyzing events...")
    all_analyses["events"] = analyze_events(events_file)
    
    # Analyze relations
    print("Analyzing relations...")
    all_analyses["relations"] = analyze_relations(relations_file)
    
    # Analyze timeline
    print("Analyzing timeline...")
    all_analyses["timeline"] = analyze_timeline(timeline_file)
    
    # Generate recommendations
    print("Generating recommendations...")
    recommendations = generate_recommendations(all_analyses)
    all_analyses["recommendations"] = recommendations
    
    # Save analysis
    output_file = Path("/home/ubuntu/revstream1/COMPREHENSIVE_MODEL_REVIEW_2025_11_20.json")
    with open(output_file, 'w') as f:
        json.dump(all_analyses, f, indent=2)
    
    print(f"\nAnalysis saved to: {output_file}")
    print()
    
    # Print summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    
    print("ENTITIES:")
    for stat_key, stat_value in all_analyses["entities"]["statistics"].items():
        print(f"  {stat_key}: {stat_value}")
    print(f"  Issues: {len(all_analyses['entities']['issues'])}")
    print()
    
    print("EVENTS:")
    for stat_key, stat_value in all_analyses["events"]["statistics"].items():
        if isinstance(stat_value, dict):
            print(f"  {stat_key}:")
            for k, v in stat_value.items():
                print(f"    {k}: {v}")
        else:
            print(f"  {stat_key}: {stat_value}")
    print(f"  Issues: {len(all_analyses['events']['issues'])}")
    print()
    
    print("RELATIONS:")
    for stat_key, stat_value in all_analyses["relations"]["statistics"].items():
        print(f"  {stat_key}: {stat_value}")
    print(f"  Issues: {len(all_analyses['relations']['issues'])}")
    print()
    
    print("TIMELINE:")
    print(f"  Total phases: {all_analyses['timeline']['statistics']['total_phases']}")
    print(f"  Issues: {len(all_analyses['timeline']['issues'])}")
    print()
    
    print("=" * 80)
    print(f"RECOMMENDATIONS: {len(recommendations)}")
    print("=" * 80)
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. [{rec['priority']}] {rec['category'].upper()}")
        print(f"   Issue: {rec['issue']}")
        print(f"   Affected: {rec['affected_count']} items")
        print(f"   Action: {rec['action']}")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()
