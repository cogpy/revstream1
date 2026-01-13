#!/usr/bin/env python3
"""
Comprehensive analysis and refinement script for revstream1 data models
Date: 2026-01-13
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = BASE_DIR / "data_models"
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")

# Load data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath, backup=True):
    if backup and os.path.exists(filepath):
        backup_path = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.rename(filepath, backup_path)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Analysis functions
def analyze_entities(entities_data):
    """Analyze entities for completeness and evidence strength"""
    analysis = {
        "total_persons": len([e for e in entities_data.get("entities", {}).get("persons", [])]),
        "total_organizations": len([e for e in entities_data.get("entities", {}).get("organizations", [])]),
        "missing_evidence": [],
        "weak_evidence": [],
        "incomplete_entities": []
    }
    
    # Check persons
    for person in entities_data.get("entities", {}).get("persons", []):
        entity_id = person.get("entity_id", "UNKNOWN")
        
        # Check for missing evidence
        if not person.get("evidence") or len(person.get("evidence", [])) == 0:
            analysis["missing_evidence"].append(entity_id)
        
        # Check for weak evidence strength
        if person.get("evidence_strength") in ["weak", "moderate"]:
            analysis["weak_evidence"].append({
                "entity_id": entity_id,
                "name": person.get("name"),
                "strength": person.get("evidence_strength")
            })
        
        # Check for incomplete entities
        if not person.get("id_number") and person.get("role") not in ["witness", "bookkeeper"]:
            analysis["incomplete_entities"].append({
                "entity_id": entity_id,
                "name": person.get("name"),
                "missing": "id_number"
            })
    
    return analysis

def analyze_events(events_data):
    """Analyze events for timeline consistency and evidence"""
    analysis = {
        "total_events": len(events_data.get("events", [])),
        "missing_dates": [],
        "missing_evidence": [],
        "phase_distribution": {},
        "burden_of_proof_distribution": {}
    }
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id", "UNKNOWN")
        
        # Check for missing dates
        if not event.get("date"):
            analysis["missing_dates"].append(event_id)
        
        # Check for missing evidence
        if not event.get("evidence") or len(event.get("evidence", [])) == 0:
            analysis["missing_evidence"].append(event_id)
        
        # Phase distribution
        phase = event.get("phase", "UNKNOWN")
        analysis["phase_distribution"][phase] = analysis["phase_distribution"].get(phase, 0) + 1
        
        # Burden of proof distribution
        burden = event.get("burden_of_proof", "UNKNOWN")
        analysis["burden_of_proof_distribution"][burden] = analysis["burden_of_proof_distribution"].get(burden, 0) + 1
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    analysis = {
        "total_relations": relations_data.get("metadata", {}).get("total_relations", 0),
        "missing_evidence": [],
        "weak_relations": []
    }
    
    # Check all relation categories
    for category, relations in relations_data.get("relations", {}).items():
        for relation in relations:
            relation_id = relation.get("relation_id", "UNKNOWN")
            
            # Check for missing evidence
            if not relation.get("evidence") or len(relation.get("evidence", [])) == 0:
                analysis["missing_evidence"].append(relation_id)
            
            # Check for weak evidence
            if relation.get("evidence_strength") in ["weak", "moderate"]:
                analysis["weak_relations"].append({
                    "relation_id": relation_id,
                    "type": relation.get("relation_type"),
                    "strength": relation.get("evidence_strength")
                })
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and consistency"""
    analysis = {
        "total_entries": len(timeline_data.get("timeline", [])),
        "missing_evidence": [],
        "missing_entities": [],
        "date_gaps": []
    }
    
    prev_date = None
    for entry in timeline_data.get("timeline", []):
        entry_id = entry.get("entry_id", entry.get("date", "UNKNOWN"))
        
        # Check for missing evidence
        if not entry.get("evidence") and not entry.get("source"):
            analysis["missing_evidence"].append(entry_id)
        
        # Check for missing entities
        if not entry.get("entities_involved") and not entry.get("entity"):
            analysis["missing_entities"].append(entry_id)
        
        # Check for date consistency
        current_date = entry.get("date")
        if current_date and prev_date:
            # Could add date gap analysis here
            pass
        prev_date = current_date
    
    return analysis

def main():
    print("=" * 80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS - 2026-01-13")
    print("=" * 80)
    
    # Load data models
    print("\n[1/4] Loading data models...")
    entities_path = DATA_MODELS_DIR / "entities" / "entities.json"
    events_path = DATA_MODELS_DIR / "events" / "events.json"
    relations_path = DATA_MODELS_DIR / "relations" / "relations.json"
    timeline_path = DATA_MODELS_DIR / "timelines" / "timeline.json"
    
    entities_data = load_json(entities_path)
    events_data = load_json(events_path)
    relations_data = load_json(relations_path)
    timeline_data = load_json(timeline_path)
    
    # Analyze each model
    print("\n[2/4] Analyzing entities...")
    entities_analysis = analyze_entities(entities_data)
    print(f"  - Total persons: {entities_analysis['total_persons']}")
    print(f"  - Total organizations: {entities_analysis['total_organizations']}")
    print(f"  - Missing evidence: {len(entities_analysis['missing_evidence'])}")
    print(f"  - Weak evidence: {len(entities_analysis['weak_evidence'])}")
    
    print("\n[3/4] Analyzing events...")
    events_analysis = analyze_events(events_data)
    print(f"  - Total events: {events_analysis['total_events']}")
    print(f"  - Missing dates: {len(events_analysis['missing_dates'])}")
    print(f"  - Missing evidence: {len(events_analysis['missing_evidence'])}")
    print(f"  - Phase distribution: {events_analysis['phase_distribution']}")
    
    print("\n[4/4] Analyzing relations...")
    relations_analysis = analyze_relations(relations_data)
    print(f"  - Total relations: {relations_analysis['total_relations']}")
    print(f"  - Missing evidence: {len(relations_analysis['missing_evidence'])}")
    print(f"  - Weak relations: {len(relations_analysis['weak_relations'])}")
    
    print("\n[5/5] Analyzing timeline...")
    timeline_analysis = analyze_timeline(timeline_data)
    print(f"  - Total entries: {timeline_analysis['total_entries']}")
    print(f"  - Missing evidence: {len(timeline_analysis['missing_evidence'])}")
    print(f"  - Missing entities: {len(timeline_analysis['missing_entities'])}")
    
    # Save comprehensive analysis
    comprehensive_analysis = {
        "analysis_date": datetime.now().isoformat(),
        "entities": entities_analysis,
        "events": events_analysis,
        "relations": relations_analysis,
        "timeline": timeline_analysis,
        "recommendations": []
    }
    
    # Generate recommendations
    if entities_analysis['missing_evidence']:
        comprehensive_analysis["recommendations"].append({
            "priority": "HIGH",
            "category": "entities",
            "issue": f"{len(entities_analysis['missing_evidence'])} entities missing evidence",
            "action": "Cross-reference with ad-res-j7 evidence files"
        })
    
    if events_analysis['missing_evidence']:
        comprehensive_analysis["recommendations"].append({
            "priority": "HIGH",
            "category": "events",
            "issue": f"{len(events_analysis['missing_evidence'])} events missing evidence",
            "action": "Add evidence references from timeline and ad-res-j7"
        })
    
    if timeline_analysis['missing_evidence']:
        comprehensive_analysis["recommendations"].append({
            "priority": "MEDIUM",
            "category": "timeline",
            "issue": f"{len(timeline_analysis['missing_evidence'])} timeline entries missing evidence",
            "action": "Link to specific evidence files in ad-res-j7"
        })
    
    # Save analysis
    analysis_path = BASE_DIR / f"COMPREHENSIVE_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(comprehensive_analysis, analysis_path, backup=False)
    print(f"\n✓ Analysis saved to: {analysis_path}")
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
