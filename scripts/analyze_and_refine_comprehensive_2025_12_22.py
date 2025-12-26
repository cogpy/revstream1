#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script
Date: 2025-12-22
Purpose: Analyze entities, relations, events, timelines and cross-reference with ad-res-j7
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS = REVSTREAM_ROOT / "data_models"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved: {filepath}")

def analyze_entities():
    """Analyze entities for completeness and evidence coverage"""
    entities = load_json(DATA_MODELS / "entities" / "entities.json")
    
    analysis = {
        "total_persons": len(entities["entities"]["persons"]),
        "total_organizations": len(entities["entities"]["organizations"]),
        "total_trusts": len(entities["entities"]["trusts"]),
        "persons_with_evidence": 0,
        "persons_without_evidence": [],
        "persons_with_ad_res_j7_refs": 0,
        "missing_ad_res_j7_refs": [],
        "evidence_strength_distribution": defaultdict(int)
    }
    
    for person in entities["entities"]["persons"]:
        if "evidence" in person and person["evidence"]:
            analysis["persons_with_evidence"] += 1
        else:
            analysis["persons_without_evidence"].append(person.get("name", person.get("entity_id")))
        
        if "ad_res_j7_references" in person and person["ad_res_j7_references"]:
            analysis["persons_with_ad_res_j7_refs"] += 1
        else:
            analysis["missing_ad_res_j7_refs"].append(person.get("name", person.get("entity_id")))
        
        if "evidence_strength" in person:
            analysis["evidence_strength_distribution"][person["evidence_strength"]] += 1
    
    return analysis

def analyze_relations():
    """Analyze relations for completeness"""
    relations = load_json(DATA_MODELS / "relations" / "relations.json")
    
    analysis = {
        "total_relations": 0,
        "relations_with_evidence": 0,
        "relations_without_evidence": [],
        "relation_categories": defaultdict(int),
        "relation_types": defaultdict(int),
        "evidence_strength_distribution": defaultdict(int)
    }
    
    # Relations are organized by category
    for category, rels in relations["relations"].items():
        if isinstance(rels, list):
            analysis["relation_categories"][category] = len(rels)
            analysis["total_relations"] += len(rels)
            
            for rel in rels:
                rel_type = rel.get("relation_type", "unknown")
                analysis["relation_types"][rel_type] += 1
                
                if "evidence" in rel and rel["evidence"]:
                    analysis["relations_with_evidence"] += 1
                else:
                    rel_desc = f"{rel.get('source_entity')} -> {rel.get('target_entity')} ({rel_type})"
                    analysis["relations_without_evidence"].append(rel_desc)
                
                if "evidence_strength" in rel:
                    analysis["evidence_strength_distribution"][rel["evidence_strength"]] += 1
    
    return analysis

def analyze_events():
    """Analyze events for completeness"""
    events = load_json(DATA_MODELS / "events" / "events.json")
    
    analysis = {
        "total_events": len(events["events"]),
        "events_with_evidence": 0,
        "events_without_evidence": [],
        "events_by_category": defaultdict(int),
        "burden_of_proof_distribution": defaultdict(int),
        "events_missing_dates": []
    }
    
    for event in events["events"]:
        category = event.get("category", "uncategorized")
        analysis["events_by_category"][category] += 1
        
        if "evidence" in event and event["evidence"]:
            analysis["events_with_evidence"] += 1
        else:
            analysis["events_without_evidence"].append(event.get("event_id", "unknown"))
        
        if "burden_of_proof" in event:
            bop = event["burden_of_proof"]
            if isinstance(bop, dict):
                # Handle dict format with civil/criminal keys
                for key, value in bop.items():
                    analysis["burden_of_proof_distribution"][f"{key}: {value}"] += 1
            else:
                # Handle string format
                analysis["burden_of_proof_distribution"][str(bop)] += 1
        
        if not event.get("date"):
            analysis["events_missing_dates"].append(event.get("event_id", "unknown"))
    
    return analysis

def analyze_timeline():
    """Analyze timeline structure"""
    timeline = load_json(DATA_MODELS / "timelines" / "timeline.json")
    
    analysis = {
        "total_phases": len(timeline.get("timeline", [])),
        "phases": []
    }
    
    for phase in timeline.get("timeline", []):
        phase_info = {
            "phase_id": phase.get("phase_id"),
            "title": phase.get("title"),
            "event_count": len(phase.get("events", []))
        }
        analysis["phases"].append(phase_info)
    
    return analysis

def scan_ad_res_j7_evidence():
    """Scan ad-res-j7 repository for evidence files"""
    evidence_files = {
        "SF_files": [],
        "JF_files": [],
        "other_annexures": [],
        "civil_response": [],
        "criminal_case": []
    }
    
    annexures_path = AD_RES_J7_ROOT / "ANNEXURES"
    if annexures_path.exists():
        for item in annexures_path.iterdir():
            if item.is_file() and item.suffix == ".md":
                name = item.name
                if name.startswith("SF"):
                    evidence_files["SF_files"].append(name)
                elif name.startswith("JF"):
                    evidence_files["JF_files"].append(name)
                else:
                    evidence_files["other_annexures"].append(name)
    
    civil_path = AD_RES_J7_ROOT / "1-CIVIL-RESPONSE"
    if civil_path.exists():
        for item in civil_path.rglob("*.md"):
            evidence_files["civil_response"].append(str(item.relative_to(AD_RES_J7_ROOT)))
    
    criminal_path = AD_RES_J7_ROOT / "2-CRIMINAL-CASE"
    if criminal_path.exists():
        for item in criminal_path.rglob("*.md"):
            evidence_files["criminal_case"].append(str(item.relative_to(AD_RES_J7_ROOT)))
    
    return evidence_files

def generate_analysis_report():
    """Generate comprehensive analysis report"""
    print("=" * 80)
    print("COMPREHENSIVE ANALYSIS REPORT - 2025-12-22")
    print("=" * 80)
    
    # Entities Analysis
    print("\n### ENTITIES ANALYSIS ###")
    entities_analysis = analyze_entities()
    print(f"Total Persons: {entities_analysis['total_persons']}")
    print(f"Total Organizations: {entities_analysis['total_organizations']}")
    print(f"Total Trusts: {entities_analysis['total_trusts']}")
    print(f"Persons with Evidence: {entities_analysis['persons_with_evidence']}")
    print(f"Persons with ad-res-j7 References: {entities_analysis['persons_with_ad_res_j7_refs']}")
    print(f"\nEvidence Strength Distribution:")
    for strength, count in entities_analysis['evidence_strength_distribution'].items():
        print(f"  {strength}: {count}")
    
    if entities_analysis['missing_ad_res_j7_refs']:
        print(f"\n⚠ Entities Missing ad-res-j7 References ({len(entities_analysis['missing_ad_res_j7_refs'])}):")
        for entity in entities_analysis['missing_ad_res_j7_refs'][:10]:
            print(f"  - {entity}")
    
    # Relations Analysis
    print("\n### RELATIONS ANALYSIS ###")
    relations_analysis = analyze_relations()
    print(f"Total Relations: {relations_analysis['total_relations']}")
    print(f"Relations with Evidence: {relations_analysis['relations_with_evidence']}")
    print(f"\nRelation Categories:")
    for category, count in sorted(relations_analysis['relation_categories'].items()):
        print(f"  {category}: {count}")
    print(f"\nRelation Types:")
    for rel_type, count in sorted(relations_analysis['relation_types'].items()):
        print(f"  {rel_type}: {count}")
    
    if relations_analysis['relations_without_evidence']:
        print(f"\n⚠ Relations Without Evidence ({len(relations_analysis['relations_without_evidence'])}):")
        for rel in relations_analysis['relations_without_evidence'][:10]:
            print(f"  - {rel}")
    
    # Events Analysis
    print("\n### EVENTS ANALYSIS ###")
    events_analysis = analyze_events()
    print(f"Total Events: {events_analysis['total_events']}")
    print(f"Events with Evidence: {events_analysis['events_with_evidence']}")
    print(f"\nEvents by Category:")
    for category, count in sorted(events_analysis['events_by_category'].items()):
        print(f"  {category}: {count}")
    print(f"\nBurden of Proof Distribution:")
    for proof, count in sorted(events_analysis['burden_of_proof_distribution'].items()):
        print(f"  {proof}: {count}")
    
    if events_analysis['events_missing_dates']:
        print(f"\n⚠ Events Missing Dates ({len(events_analysis['events_missing_dates'])}):")
        for event_id in events_analysis['events_missing_dates'][:10]:
            print(f"  - {event_id}")
    
    # Timeline Analysis
    print("\n### TIMELINE ANALYSIS ###")
    timeline_analysis = analyze_timeline()
    print(f"Total Timeline Phases: {timeline_analysis['total_phases']}")
    for phase in timeline_analysis['phases']:
        print(f"  Phase {phase['phase_id']}: {phase['title']} ({phase['event_count']} events)")
    
    # Evidence Files Scan
    print("\n### AD-RES-J7 EVIDENCE SCAN ###")
    evidence_files = scan_ad_res_j7_evidence()
    print(f"SF Files (Smoking Gun): {len(evidence_files['SF_files'])}")
    for sf in sorted(evidence_files['SF_files']):
        print(f"  - {sf}")
    print(f"\nJF Files (Jacqui Faucitt): {len(evidence_files['JF_files'])}")
    print(f"Other Annexures: {len(evidence_files['other_annexures'])}")
    print(f"Civil Response Documents: {len(evidence_files['civil_response'])}")
    print(f"Criminal Case Documents: {len(evidence_files['criminal_case'])}")
    
    # Save analysis
    analysis_data = {
        "timestamp": datetime.now().isoformat(),
        "entities": entities_analysis,
        "relations": relations_analysis,
        "events": events_analysis,
        "timeline": timeline_analysis,
        "ad_res_j7_evidence": evidence_files
    }
    
    save_json(analysis_data, REVSTREAM_ROOT / "COMPREHENSIVE_ANALYSIS_2025_12_22.json")
    
    return analysis_data

if __name__ == "__main__":
    analysis = generate_analysis_report()
    print("\n" + "=" * 80)
    print("Analysis complete. Report saved to COMPREHENSIVE_ANALYSIS_2025_12_22.json")
    print("=" * 80)
