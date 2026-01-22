#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script for RevStream1
Date: 2026-01-12
Purpose: Analyze entities, relations, events, and timelines; cross-reference with ad-res-j7 evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Paths
REVSTREAM_BASE = Path("/home/ubuntu/revstream1")
AD_RES_J7_BASE = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS = REVSTREAM_BASE / "data_models"

# Load current data models
def load_json(filepath):
    """Load JSON file with error handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_entities():
    """Analyze current entities model"""
    entities_file = DATA_MODELS / "entities" / "entities_refined_2025_12_30_v32.json"
    entities = load_json(entities_file)
    
    if not entities:
        return None
    
    analysis = {
        "total_persons": len(entities.get("entities", {}).get("persons", [])),
        "total_organizations": len(entities.get("entities", {}).get("organizations", [])),
        "total_trusts": len(entities.get("entities", {}).get("trusts", [])),
        "evidence_coverage": entities.get("metadata", {}).get("evidence_coverage", "unknown"),
        "version": entities.get("metadata", {}).get("version", "unknown"),
        "persons": [],
        "organizations": [],
        "trusts": []
    }
    
    # Analyze persons
    for person in entities.get("entities", {}).get("persons", []):
        analysis["persons"].append({
            "entity_id": person.get("entity_id"),
            "name": person.get("name"),
            "role": person.get("role"),
            "involvement_events": person.get("involvement_events", 0),
            "evidence_strength": person.get("evidence_strength", "unknown"),
            "evidence_refs_count": len(person.get("evidence_support", {}).get("evidence_refs", [])),
            "annexure_count": len(person.get("evidence_support", {}).get("annexure_support", []))
        })
    
    # Analyze organizations
    for org in entities.get("entities", {}).get("organizations", []):
        analysis["organizations"].append({
            "entity_id": org.get("entity_id"),
            "name": org.get("name"),
            "registration_number": org.get("registration_number"),
            "role": org.get("role"),
            "evidence_refs_count": len(org.get("evidence_support", {}).get("evidence_refs", [])),
            "annexure_count": len(org.get("evidence_support", {}).get("annexure_support", []))
        })
    
    # Analyze trusts
    for trust in entities.get("entities", {}).get("trusts", []):
        analysis["trusts"].append({
            "entity_id": trust.get("entity_id"),
            "name": trust.get("name"),
            "role": trust.get("role"),
            "evidence_refs_count": len(trust.get("evidence_support", {}).get("evidence_refs", [])),
            "annexure_count": len(trust.get("evidence_support", {}).get("annexure_support", []))
        })
    
    return analysis

def analyze_relations():
    """Analyze current relations model"""
    relations_file = DATA_MODELS / "relations" / "relations_refined_2025_12_27_v31.json"
    relations = load_json(relations_file)
    
    if not relations:
        return None
    
    analysis = {
        "total_relations": 0,
        "version": relations.get("metadata", {}).get("version", "unknown"),
        "relation_types": defaultdict(int),
        "relations_by_strength": defaultdict(int),
        "relations": []
    }
    
    # Handle nested structure (relations is a dict with categories)
    relations_data = relations.get("relations", {})
    if isinstance(relations_data, dict):
        for category, relation_list in relations_data.items():
            if isinstance(relation_list, list):
                for relation in relation_list:
                    if isinstance(relation, dict):
                        analysis["total_relations"] += 1
                        rel_type = relation.get("relation_type", "unknown")
                        analysis["relation_types"][rel_type] += 1
                        
                        strength = relation.get("strength", relation.get("evidence_strength", "unknown"))
                        analysis["relations_by_strength"][strength] += 1
                        
                        analysis["relations"].append({
                            "relation_id": relation.get("relation_id"),
                            "relation_type": rel_type,
                            "source_entity": relation.get("source_entity"),
                            "target_entity": relation.get("target_entity"),
                            "strength": strength,
                            "evidence_count": len(relation.get("evidence", []))
                        })
    
    return analysis

def analyze_events():
    """Analyze current events model"""
    events_file = DATA_MODELS / "events" / "events_refined_2025_12_14_v30.json"
    events = load_json(events_file)
    
    if not events:
        return None
    
    analysis = {
        "total_events": len(events.get("events", [])),
        "version": events.get("metadata", {}).get("version", "unknown"),
        "event_types": defaultdict(int),
        "events_by_significance": defaultdict(int),
        "events": []
    }
    
    for event in events.get("events", []):
        event_type = event.get("event_type", "unknown")
        analysis["event_types"][event_type] += 1
        
        significance = event.get("significance", "unknown")
        analysis["events_by_significance"][significance] += 1
        
        analysis["events"].append({
            "event_id": event.get("event_id"),
            "date": event.get("date"),
            "event_type": event_type,
            "title": event.get("title"),
            "significance": significance,
            "burden_of_proof": event.get("burden_of_proof", "unknown"),
            "evidence_refs_count": len(event.get("evidence", []))
        })
    
    return analysis

def analyze_timeline():
    """Analyze current timeline"""
    timeline_file = DATA_MODELS / "timelines" / "timeline.json"
    timeline = load_json(timeline_file)
    
    if not timeline:
        return None
    
    analysis = {
        "total_entries": timeline.get("metadata", {}).get("total_entries", 0),
        "criminal_threshold_entries": timeline.get("metadata", {}).get("criminal_threshold_entries", 0),
        "high_significance_entries": timeline.get("metadata", {}).get("high_significance_entries", 0),
        "version": timeline.get("metadata", {}).get("version", "unknown"),
        "date_range": {},
        "entries_by_year": defaultdict(int),
        "entries_with_evidence": 0,
        "entries_without_evidence": 0
    }
    
    dates = []
    for entry in timeline.get("timeline", []):
        date = entry.get("date")
        if date:
            dates.append(date)
            year = date.split("-")[0]
            analysis["entries_by_year"][year] += 1
        
        # Check evidence
        if entry.get("evidence") or entry.get("source"):
            analysis["entries_with_evidence"] += 1
        else:
            analysis["entries_without_evidence"] += 1
    
    if dates:
        analysis["date_range"] = {
            "earliest": min(dates),
            "latest": max(dates)
        }
    
    return analysis

def check_ad_res_j7_evidence():
    """Check available evidence in ad-res-j7"""
    annexures_path = AD_RES_J7_BASE / "ANNEXURES"
    
    analysis = {
        "annexures": {},
        "supplementary_filings": []
    }
    
    # Check ANNEXURES
    if annexures_path.exists():
        for item in annexures_path.iterdir():
            if item.is_dir() and item.name.startswith("JF"):
                file_count = len(list(item.rglob("*")))
                analysis["annexures"][item.name] = {
                    "path": str(item),
                    "file_count": file_count
                }
            elif item.is_file() and item.name.startswith("SF"):
                analysis["supplementary_filings"].append({
                    "name": item.name,
                    "path": str(item)
                })
    
    return analysis

def generate_recommendations():
    """Generate recommendations for improvements"""
    recommendations = {
        "entities": [],
        "relations": [],
        "events": [],
        "timeline": [],
        "github_pages": [],
        "legal_filings": []
    }
    
    # Entity recommendations
    recommendations["entities"].extend([
        "Verify all entity IDs are consistently used across all models",
        "Ensure all entities have complete evidence references from ad-res-j7",
        "Add missing distributor entities from JF16-DISTRIBUTORS",
        "Cross-reference all persons with CIPC records in JF14 and JF15"
    ])
    
    # Relations recommendations
    recommendations["relations"].extend([
        "Map all company director relationships from CIPC records",
        "Add temporal aspects to relations (start_date, end_date)",
        "Verify all relations have supporting evidence from ANNEXURES",
        "Add conspiracy network relations based on timeline patterns"
    ])
    
    # Events recommendations
    recommendations["events"].extend([
        "Ensure all events reference specific evidence files",
        "Add event significance ratings based on burden of proof",
        "Link events to specific legal violations",
        "Cross-reference events with timeline entries for consistency"
    ])
    
    # Timeline recommendations
    recommendations["timeline"].extend([
        "Add missing CIPC registration events from JF14, JF15, JF16",
        "Ensure all criminal threshold events are properly marked",
        "Add evidence file paths for all entries",
        "Create phase markers for different conspiracy stages"
    ])
    
    # GitHub Pages recommendations
    recommendations["github_pages"].extend([
        "Create clear navigation structure for 3 applications",
        "Add evidence index with direct links to ANNEXURES",
        "Create visual timelines for each application",
        "Add burden of proof analysis for each claim",
        "Organize filings by type and date",
        "Create cross-reference tables linking claims to evidence"
    ])
    
    # Legal filings recommendations
    recommendations["legal_filings"].extend([
        "Update CIPC complaint with latest evidence from v32 entities",
        "Enhance POPIA complaint with specific data breach instances",
        "Strengthen NPA Tax Fraud Report with financial calculations",
        "Create Commercial Crime Case submission with timeline",
        "Add civil claim calculations based on verified losses",
        "Ensure all filings meet 50% (civil) or 95% (criminal) burden of proof"
    ])
    
    return recommendations

def main():
    """Main analysis function"""
    print("=" * 80)
    print("REVSTREAM1 COMPREHENSIVE ANALYSIS - 2026-01-12")
    print("=" * 80)
    print()
    
    # Analyze entities
    print("Analyzing Entities...")
    entities_analysis = analyze_entities()
    if entities_analysis:
        print(f"  Total Persons: {entities_analysis['total_persons']}")
        print(f"  Total Organizations: {entities_analysis['total_organizations']}")
        print(f"  Total Trusts: {entities_analysis['total_trusts']}")
        print(f"  Evidence Coverage: {entities_analysis['evidence_coverage']}")
        print(f"  Version: {entities_analysis['version']}")
    print()
    
    # Analyze relations
    print("Analyzing Relations...")
    relations_analysis = analyze_relations()
    if relations_analysis:
        print(f"  Total Relations: {relations_analysis['total_relations']}")
        print(f"  Version: {relations_analysis['version']}")
        print(f"  Relation Types: {dict(relations_analysis['relation_types'])}")
    print()
    
    # Analyze events
    print("Analyzing Events...")
    events_analysis = analyze_events()
    if events_analysis:
        print(f"  Total Events: {events_analysis['total_events']}")
        print(f"  Version: {events_analysis['version']}")
        print(f"  Event Types: {dict(events_analysis['event_types'])}")
    print()
    
    # Analyze timeline
    print("Analyzing Timeline...")
    timeline_analysis = analyze_timeline()
    if timeline_analysis:
        print(f"  Total Entries: {timeline_analysis['total_entries']}")
        print(f"  Criminal Threshold Entries: {timeline_analysis['criminal_threshold_entries']}")
        print(f"  High Significance Entries: {timeline_analysis['high_significance_entries']}")
        print(f"  Date Range: {timeline_analysis['date_range']}")
        print(f"  Entries with Evidence: {timeline_analysis['entries_with_evidence']}")
        print(f"  Entries without Evidence: {timeline_analysis['entries_without_evidence']}")
    print()
    
    # Check ad-res-j7 evidence
    print("Checking ad-res-j7 Evidence...")
    evidence_analysis = check_ad_res_j7_evidence()
    print(f"  ANNEXURES Found: {len(evidence_analysis['annexures'])}")
    print(f"  Supplementary Filings: {len(evidence_analysis['supplementary_filings'])}")
    for annexure, info in evidence_analysis['annexures'].items():
        print(f"    {annexure}: {info['file_count']} files")
    print()
    
    # Generate recommendations
    print("Generating Recommendations...")
    recommendations = generate_recommendations()
    print()
    
    # Save comprehensive analysis
    output = {
        "analysis_date": datetime.now().isoformat(),
        "entities_analysis": entities_analysis,
        "relations_analysis": relations_analysis,
        "events_analysis": events_analysis,
        "timeline_analysis": timeline_analysis,
        "evidence_analysis": evidence_analysis,
        "recommendations": recommendations
    }
    
    output_file = REVSTREAM_BASE / f"COMPREHENSIVE_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"Analysis saved to: {output_file}")
    print()
    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    
    return output

if __name__ == "__main__":
    main()
