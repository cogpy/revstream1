#!/usr/bin/env python3
"""
Comprehensive Data Model Refinement Script
Analyzes and refines entities, relations, events, and timelines based on ad-res-j7 evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_ROOT = Path("/home/ubuntu/ad-res-j7")
DOCS_ROOT = REVSTREAM_ROOT / "docs"
DATA_MODELS_ROOT = DOCS_ROOT / "data_models"

# Data model files
ENTITIES_FILE = DATA_MODELS_ROOT / "entities" / "entities.json"
RELATIONS_FILE = DATA_MODELS_ROOT / "relations.json"
EVENTS_FILE = DATA_MODELS_ROOT / "events.json"
TIMELINE_FILE = DATA_MODELS_ROOT / "timeline.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file with formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_evidence_repository():
    """Analyze the ad-res-j7 repository structure"""
    evidence_structure = {
        "annexures": {},
        "applications": {},
        "total_files": 0
    }
    
    # Analyze ANNEXURES
    annexures_path = AD_RES_ROOT / "ANNEXURES"
    if annexures_path.exists():
        for annexure_dir in annexures_path.iterdir():
            if annexure_dir.is_dir():
                files = list(annexure_dir.glob("*"))
                evidence_structure["annexures"][annexure_dir.name] = len(files)
                evidence_structure["total_files"] += len(files)
    
    # Analyze applications
    for app_dir in ["1-CIVIL-RESPONSE", "2-CRIMINAL-CASE", "3-EXTERNAL-VALIDATION"]:
        app_path = AD_RES_ROOT / app_dir
        if app_path.exists():
            files = list(app_path.rglob("*"))
            evidence_structure["applications"][app_dir] = len([f for f in files if f.is_file()])
            evidence_structure["total_files"] += len([f for f in files if f.is_file()])
    
    return evidence_structure

def get_current_versions():
    """Get current versions of all data models"""
    versions = {}
    
    if ENTITIES_FILE.exists():
        entities = load_json(ENTITIES_FILE)
        versions["entities"] = entities.get("metadata", {}).get("version", "unknown")
    
    if RELATIONS_FILE.exists():
        relations = load_json(RELATIONS_FILE)
        versions["relations"] = relations.get("metadata", {}).get("version", "unknown")
    
    if EVENTS_FILE.exists():
        events = load_json(EVENTS_FILE)
        versions["events"] = events.get("metadata", {}).get("version", "unknown")
    
    if TIMELINE_FILE.exists():
        timeline = load_json(TIMELINE_FILE)
        versions["timeline"] = timeline.get("metadata", {}).get("version", "unknown")
    
    return versions

def analyze_entities_needing_enhancement():
    """Analyze entities that need evidence enhancement"""
    entities = load_json(ENTITIES_FILE)
    
    needs_enhancement = {
        "weak_evidence": [],
        "missing_ad_res_refs": [],
        "outdated_timestamps": []
    }
    
    for person in entities["entities"]["persons"]:
        entity_id = person.get("entity_id")
        evidence_strength = person.get("evidence_strength", "unknown")
        ad_res_refs = person.get("ad_res_j7_references", [])
        
        if evidence_strength in ["weak", "moderate"]:
            needs_enhancement["weak_evidence"].append({
                "id": entity_id,
                "name": person.get("name"),
                "strength": evidence_strength
            })
        
        if len(ad_res_refs) < 2:
            needs_enhancement["missing_ad_res_refs"].append({
                "id": entity_id,
                "name": person.get("name"),
                "refs_count": len(ad_res_refs)
            })
    
    for org in entities["entities"]["organizations"]:
        entity_id = org.get("entity_id")
        evidence_strength = org.get("evidence_strength", "unknown")
        ad_res_refs = org.get("ad_res_j7_references", [])
        
        if evidence_strength in ["weak", "moderate"]:
            needs_enhancement["weak_evidence"].append({
                "id": entity_id,
                "name": org.get("name"),
                "strength": evidence_strength
            })
        
        if len(ad_res_refs) < 2:
            needs_enhancement["missing_ad_res_refs"].append({
                "id": entity_id,
                "name": org.get("name"),
                "refs_count": len(ad_res_refs)
            })
    
    return needs_enhancement

def analyze_timeline_gaps():
    """Analyze timeline for gaps and missing evidence"""
    timeline = load_json(TIMELINE_FILE)
    
    gaps = {
        "missing_evidence": [],
        "missing_actors": [],
        "weak_entries": []
    }
    
    for entry in timeline.get("timeline", []):
        entry_id = entry.get("id")
        evidence = entry.get("evidence", [])
        key_actors = entry.get("key_actors", [])
        
        if len(evidence) < 2:
            gaps["missing_evidence"].append({
                "id": entry_id,
                "date": entry.get("date"),
                "title": entry.get("title"),
                "evidence_count": len(evidence)
            })
        
        if len(key_actors) == 0:
            gaps["missing_actors"].append({
                "id": entry_id,
                "date": entry.get("date"),
                "title": entry.get("title")
            })
    
    return gaps

def generate_analysis_report():
    """Generate comprehensive analysis report"""
    print("=" * 80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS")
    print("=" * 80)
    print()
    
    # Evidence repository analysis
    print("1. EVIDENCE REPOSITORY ANALYSIS")
    print("-" * 80)
    evidence_structure = analyze_evidence_repository()
    print(f"Total Evidence Files: {evidence_structure['total_files']}")
    print()
    print("Annexures:")
    for annexure, count in sorted(evidence_structure["annexures"].items()):
        print(f"  {annexure}: {count} files")
    print()
    print("Applications:")
    for app, count in evidence_structure["applications"].items():
        print(f"  {app}: {count} files")
    print()
    
    # Current versions
    print("2. CURRENT DATA MODEL VERSIONS")
    print("-" * 80)
    versions = get_current_versions()
    for model, version in versions.items():
        print(f"  {model.capitalize()}: {version}")
    print()
    
    # Entities needing enhancement
    print("3. ENTITIES NEEDING ENHANCEMENT")
    print("-" * 80)
    entity_needs = analyze_entities_needing_enhancement()
    print(f"Weak Evidence Strength: {len(entity_needs['weak_evidence'])} entities")
    for entity in entity_needs['weak_evidence']:
        print(f"  - {entity['id']}: {entity['name']} ({entity['strength']})")
    print()
    print(f"Missing ad-res-j7 References: {len(entity_needs['missing_ad_res_refs'])} entities")
    for entity in entity_needs['missing_ad_res_refs']:
        print(f"  - {entity['id']}: {entity['name']} ({entity['refs_count']} refs)")
    print()
    
    # Timeline gaps
    print("4. TIMELINE GAPS ANALYSIS")
    print("-" * 80)
    timeline_gaps = analyze_timeline_gaps()
    print(f"Entries with Weak Evidence: {len(timeline_gaps['missing_evidence'])}")
    for entry in timeline_gaps['missing_evidence'][:5]:  # Show first 5
        print(f"  - {entry['id']}: {entry['title']} ({entry['evidence_count']} evidence items)")
    print()
    print(f"Entries Missing Key Actors: {len(timeline_gaps['missing_actors'])}")
    for entry in timeline_gaps['missing_actors'][:5]:  # Show first 5
        print(f"  - {entry['id']}: {entry['title']}")
    print()
    
    # Save detailed report
    report = {
        "timestamp": datetime.now().isoformat(),
        "evidence_structure": evidence_structure,
        "current_versions": versions,
        "entities_needing_enhancement": entity_needs,
        "timeline_gaps": timeline_gaps
    }
    
    report_file = REVSTREAM_ROOT / f"ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(report_file, report)
    print(f"Detailed report saved to: {report_file}")
    print()
    
    return report

if __name__ == "__main__":
    report = generate_analysis_report()
