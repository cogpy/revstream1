#!/usr/bin/env python3
"""
Cross-Reference Analysis with ad-res-j7
Date: 2025-12-22
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS = REVSTREAM_ROOT / "data_models"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved: {filepath}")

def scan_evidence_files():
    """Comprehensive scan of ad-res-j7 evidence"""
    evidence = {
        "SF_files": {},
        "JF_directories": {},
        "civil_response": [],
        "criminal_case": [],
        "regulatory": []
    }
    
    # Scan SF files
    annexures = AD_RES_J7_ROOT / "ANNEXURES"
    for sf_file in annexures.glob("SF*.md"):
        key = sf_file.stem
        evidence["SF_files"][key] = {
            "path": str(sf_file.relative_to(AD_RES_J7_ROOT)),
            "name": sf_file.name,
            "size": sf_file.stat().st_size
        }
    
    # Scan JF directories
    for jf_dir in sorted(annexures.glob("JF*")):
        if jf_dir.is_dir():
            files = list(jf_dir.rglob("*"))
            evidence["JF_directories"][jf_dir.name] = {
                "path": str(jf_dir.relative_to(AD_RES_J7_ROOT)),
                "file_count": len([f for f in files if f.is_file()]),
                "total_size": sum(f.stat().st_size for f in files if f.is_file())
            }
    
    # Scan civil response
    civil_path = AD_RES_J7_ROOT / "1-CIVIL-RESPONSE"
    if civil_path.exists():
        for doc in civil_path.rglob("*.md"):
            evidence["civil_response"].append(str(doc.relative_to(AD_RES_J7_ROOT)))
    
    # Scan criminal case
    criminal_path = AD_RES_J7_ROOT / "2-CRIMINAL-CASE"
    if criminal_path.exists():
        for doc in criminal_path.rglob("*.md"):
            evidence["criminal_case"].append(str(doc.relative_to(AD_RES_J7_ROOT)))
    
    # Scan regulatory
    regulatory_path = AD_RES_J7_ROOT / "3-REGULATORY"
    if regulatory_path.exists():
        for doc in regulatory_path.rglob("*.md"):
            evidence["regulatory"].append(str(doc.relative_to(AD_RES_J7_ROOT)))
    
    return evidence

def identify_missing_evidence_refs():
    """Identify entities/events missing ad-res-j7 references"""
    entities = load_json(DATA_MODELS / "entities" / "entities.json")
    events = load_json(DATA_MODELS / "events" / "events.json")
    
    missing = {
        "entities_without_refs": [],
        "events_without_refs": [],
        "entities_with_weak_evidence": [],
        "events_with_weak_evidence": []
    }
    
    # Check persons
    for person in entities["entities"]["persons"]:
        if not person.get("ad_res_j7_references"):
            missing["entities_without_refs"].append({
                "id": person["entity_id"],
                "name": person.get("name", "Unknown"),
                "role": person.get("role", "Unknown")
            })
        
        if person.get("evidence_strength") not in ["conclusive", "strong"]:
            missing["entities_with_weak_evidence"].append({
                "id": person["entity_id"],
                "name": person.get("name", "Unknown"),
                "strength": person.get("evidence_strength", "none")
            })
    
    # Check events
    for event in events["events"]:
        if not event.get("ad_res_j7_evidence"):
            missing["events_without_refs"].append({
                "id": event["event_id"],
                "description": event.get("description", "Unknown")[:80]
            })
    
    return missing

def suggest_improvements():
    """Suggest specific improvements based on analysis"""
    suggestions = {
        "timestamp": datetime.now().isoformat(),
        "entity_improvements": [],
        "relation_improvements": [],
        "event_improvements": [],
        "timeline_improvements": [],
        "github_pages_improvements": [],
        "legal_filing_improvements": []
    }
    
    # Entity improvements
    suggestions["entity_improvements"] = [
        {
            "priority": "HIGH",
            "action": "Add ad-res-j7 references for 5 entities missing them",
            "entities": ["Gee", "Bernadine Wright", "Chantal", "Jax", "Marisca Meyer"],
            "evidence_sources": ["JF08", "JF13", "SF files"]
        },
        {
            "priority": "MEDIUM",
            "action": "Enhance evidence strength documentation for entities with weak evidence",
            "count": 8
        }
    ]
    
    # Relation improvements
    suggestions["relation_improvements"] = [
        {
            "priority": "HIGH",
            "action": "Add temporal relations between key events",
            "current_count": 6,
            "target_count": 15
        },
        {
            "priority": "MEDIUM",
            "action": "Document evidence for all 75 relations with ad-res-j7 cross-references"
        }
    ]
    
    # Event improvements
    suggestions["event_improvements"] = [
        {
            "priority": "CRITICAL",
            "action": "Fix events missing dates",
            "affected_events": "Multiple events lack specific dates"
        },
        {
            "priority": "HIGH",
            "action": "Enhance burden of proof documentation",
            "detail": "Ensure all events have both civil and criminal burden assessments"
        }
    ]
    
    # Timeline improvements
    suggestions["timeline_improvements"] = [
        {
            "priority": "CRITICAL",
            "action": "Rebuild timeline structure - only 3 phases with 0 events each",
            "detail": "Timeline should organize 77 events into chronological phases"
        },
        {
            "priority": "HIGH",
            "action": "Create visual timeline with key milestones",
            "format": "Mermaid diagram or interactive HTML"
        }
    ]
    
    # GitHub Pages improvements
    suggestions["github_pages_improvements"] = [
        {
            "priority": "HIGH",
            "action": "Update evidence index with all SF and JF files",
            "current_sf_count": 8,
            "current_jf_count": 13
        },
        {
            "priority": "HIGH",
            "action": "Create entity profile pages in docs/entities/",
            "detail": "Individual pages for each of 14 persons and 14 organizations"
        },
        {
            "priority": "MEDIUM",
            "action": "Create event analysis pages in docs/events/",
            "detail": "Categorized event documentation with evidence links"
        },
        {
            "priority": "MEDIUM",
            "action": "Update index.md with latest statistics",
            "updates": ["Entity counts", "Evidence file counts", "Timeline status"]
        }
    ]
    
    # Legal filing improvements
    suggestions["legal_filing_improvements"] = [
        {
            "priority": "CRITICAL",
            "action": "Review and update CIPC complaint with latest evidence",
            "file": "CIPC_COMPLAINT_REFINED_2025_12_21.md",
            "new_evidence": ["SF1-SF8", "JF13"]
        },
        {
            "priority": "HIGH",
            "action": "Create POPIA criminal complaint",
            "evidence": ["Email control", "System access violations", "Data breaches"]
        },
        {
            "priority": "HIGH",
            "action": "Create Commercial Crime case submission",
            "evidence": ["R10.2M revenue theft", "Trust violations", "Financial fraud"]
        },
        {
            "priority": "MEDIUM",
            "action": "Create NPA Tax Fraud report",
            "evidence": ["SARS audit evidence", "Transfer pricing fraud", "Stock adjustments"]
        }
    ]
    
    return suggestions

def generate_cross_reference_report():
    """Generate comprehensive cross-reference report"""
    print("=" * 80)
    print("AD-RES-J7 CROSS-REFERENCE ANALYSIS - 2025-12-22")
    print("=" * 80)
    
    # Scan evidence
    print("\n### EVIDENCE SCAN ###")
    evidence = scan_evidence_files()
    print(f"SF Files: {len(evidence['SF_files'])}")
    for sf, details in sorted(evidence['SF_files'].items()):
        print(f"  {sf}: {details['name']} ({details['size']:,} bytes)")
    
    print(f"\nJF Directories: {len(evidence['JF_directories'])}")
    for jf, details in sorted(evidence['JF_directories'].items()):
        print(f"  {jf}: {details['file_count']} files ({details['total_size']:,} bytes)")
    
    print(f"\nCivil Response Documents: {len(evidence['civil_response'])}")
    print(f"Criminal Case Documents: {len(evidence['criminal_case'])}")
    print(f"Regulatory Documents: {len(evidence['regulatory'])}")
    
    # Identify missing references
    print("\n### MISSING EVIDENCE REFERENCES ###")
    missing = identify_missing_evidence_refs()
    print(f"Entities without ad-res-j7 refs: {len(missing['entities_without_refs'])}")
    for entity in missing['entities_without_refs']:
        print(f"  - {entity['name']} ({entity['role']})")
    
    print(f"\nEvents without ad-res-j7 refs: {len(missing['events_without_refs'])}")
    for event in missing['events_without_refs'][:10]:
        print(f"  - {event['id']}: {event['description']}")
    
    # Generate suggestions
    print("\n### IMPROVEMENT SUGGESTIONS ###")
    suggestions = suggest_improvements()
    
    print("\nEntity Improvements:")
    for imp in suggestions['entity_improvements']:
        print(f"  [{imp['priority']}] {imp['action']}")
    
    print("\nRelation Improvements:")
    for imp in suggestions['relation_improvements']:
        print(f"  [{imp['priority']}] {imp['action']}")
    
    print("\nEvent Improvements:")
    for imp in suggestions['event_improvements']:
        print(f"  [{imp['priority']}] {imp['action']}")
    
    print("\nTimeline Improvements:")
    for imp in suggestions['timeline_improvements']:
        print(f"  [{imp['priority']}] {imp['action']}")
    
    print("\nGitHub Pages Improvements:")
    for imp in suggestions['github_pages_improvements']:
        print(f"  [{imp['priority']}] {imp['action']}")
    
    print("\nLegal Filing Improvements:")
    for imp in suggestions['legal_filing_improvements']:
        print(f"  [{imp['priority']}] {imp['action']}")
    
    # Save report
    report = {
        "timestamp": datetime.now().isoformat(),
        "evidence_scan": evidence,
        "missing_references": missing,
        "improvement_suggestions": suggestions
    }
    
    save_json(report, REVSTREAM_ROOT / "AD_RES_J7_CROSS_REFERENCE_2025_12_22.json")
    
    return report

if __name__ == "__main__":
    report = generate_cross_reference_report()
    print("\n" + "=" * 80)
    print("Cross-reference analysis complete")
    print("=" * 80)
