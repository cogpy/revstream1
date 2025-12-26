#!/usr/bin/env python3
"""
Comprehensive Data Model Refinement Script
Version: 2025-11-20
Purpose: Refine entities, relations, events, and timelines with ad-res-j7 cross-references
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_timeline_events(timeline_data, events_data):
    """Analyze timeline events and suggest improvements"""
    improvements = {
        "metadata": {
            "analysis_date": datetime.now().isoformat(),
            "version": "1.0"
        },
        "timeline_analysis": {},
        "event_improvements": [],
        "phase_recommendations": []
    }
    
    # Analyze each phase
    for phase_key, phase_data in timeline_data.get("timeline_phases", {}).items():
        phase_events = phase_data.get("events", [])
        
        analysis = {
            "phase_name": phase_data.get("phase_name"),
            "event_count": len(phase_events),
            "date_range": f"{phase_data.get('start_date')} to {phase_data.get('end_date')}",
            "financial_impact": phase_data.get("financial_impact"),
            "key_characteristics": phase_data.get("key_characteristics", []),
            "related_applications": phase_data.get("related_applications", [])
        }
        
        improvements["timeline_analysis"][phase_key] = analysis
    
    # Check for events without proper categorization
    events_dict = {e["event_id"]: e for e in events_data.get("events", [])}
    
    for event_id, event in events_dict.items():
        if event.get("crime_category") == "unknown" or not event.get("crime_category"):
            improvements["event_improvements"].append({
                "event_id": event_id,
                "issue": "missing_crime_category",
                "recommendation": "Assign appropriate crime category based on event description"
            })
        
        if event.get("phase") == "unknown" or not event.get("phase"):
            improvements["event_improvements"].append({
                "event_id": event_id,
                "issue": "missing_phase",
                "recommendation": "Assign to appropriate timeline phase"
            })
    
    return improvements

def enhance_evidence_references(data_models_path, ad_res_j7_path):
    """Enhance evidence references with ad-res-j7 cross-references"""
    
    # Check what evidence exists in ad-res-j7
    evidence_dirs = []
    if ad_res_j7_path.exists():
        for item in ad_res_j7_path.iterdir():
            if item.is_dir():
                evidence_dirs.append(item.name)
    
    return {
        "ad_res_j7_evidence_directories": evidence_dirs[:20],  # First 20
        "total_directories": len(evidence_dirs),
        "repository_url": "https://github.com/cogpy/ad-res-j7"
    }

def generate_github_pages_structure():
    """Generate improved GitHub Pages structure"""
    
    structure = {
        "index.md": {
            "purpose": "Main landing page with case overview",
            "sections": [
                "Executive Summary",
                "Case Overview",
                "Three Sequential Applications",
                "Key Patterns",
                "Timeline Progression",
                "Evidence Resources",
                "Navigation"
            ],
            "improvements": [
                "Add clear evidence links to ad-res-j7",
                "Improve cross-references between applications",
                "Add visual timeline diagrams"
            ]
        },
        "application-1.md": {
            "purpose": "Ex Parte Interdict details",
            "evidence_categories": [
                "POPIA Violations",
                "Trustee Misconduct",
                "ReZonance Payment System",
                "Shopify Platform Ownership"
            ],
            "improvements": [
                "Add direct links to specific evidence files in ad-res-j7",
                "Include timeline visualization for this application",
                "Cross-reference related events from events.json"
            ]
        },
        "application-2.md": {
            "purpose": "Settlement Agreement Enforcement",
            "evidence_categories": [
                "Mediation Documentation",
                "Corporate Records",
                "Accounting Evidence"
            ],
            "improvements": [
                "Add mediation timeline",
                "Link to CIPC evidence in ad-res-j7",
                "Include financial analysis documents"
            ]
        },
        "application-3.md": {
            "purpose": "Contact Interdict details",
            "evidence_categories": [
                "Email Correspondence",
                "Sage Control Analysis",
                "Trademark Documentation"
            ],
            "improvements": [
                "Add email timeline",
                "Link to Sage system evidence",
                "Include harassment pattern analysis"
            ]
        },
        "evidence-index-enhanced.md": {
            "purpose": "Comprehensive evidence catalog",
            "improvements": [
                "Organize by application (1, 2, 3)",
                "Add direct GitHub links to ad-res-j7 files",
                "Include file descriptions and relevance",
                "Add evidence type tags (email, financial, legal, etc.)"
            ]
        }
    }
    
    return structure

def main():
    base_path = Path("/home/ubuntu/revstream1")
    data_models_path = base_path / "data_models"
    ad_res_j7_path = Path("/home/ubuntu/ad-res-j7")
    
    print("="*80)
    print("COMPREHENSIVE DATA MODEL REFINEMENT")
    print("="*80)
    
    # Load current data models
    print("\nLoading data models...")
    entities = load_json(data_models_path / "entities/entities_refined_2025_11_20_v5.json")
    events = load_json(data_models_path / "events/events_refined_2025_11_20_v6.json")
    relations = load_json(data_models_path / "relations/relations_refined_2025_11_19_v4.json")
    timeline = load_json(data_models_path / "timelines/timeline_refined_2025_11_20_v5.json")
    
    # Analyze timeline events
    print("\nAnalyzing timeline events...")
    timeline_improvements = analyze_timeline_events(timeline, events)
    
    # Enhance evidence references
    print("\nEnhancing evidence references...")
    evidence_refs = enhance_evidence_references(data_models_path, ad_res_j7_path)
    
    # Generate GitHub Pages structure
    print("\nGenerating GitHub Pages structure recommendations...")
    gh_pages_structure = generate_github_pages_structure()
    
    # Compile comprehensive report
    report = {
        "metadata": {
            "report_date": datetime.now().isoformat(),
            "version": "1.0",
            "purpose": "Comprehensive refinement and improvement recommendations"
        },
        "current_state": {
            "entities": {
                "total": len(entities["entities"]["persons"]) + len(entities["entities"]["organizations"]) + len(entities["entities"]["trusts"]),
                "persons": len(entities["entities"]["persons"]),
                "organizations": len(entities["entities"]["organizations"]),
                "trusts": len(entities["entities"]["trusts"])
            },
            "events": {
                "total": len(events["events"])
            },
            "relations": {
                "total": relations["metadata"]["total_relations"]
            },
            "timeline": {
                "phases": len(timeline.get("timeline_phases", {})),
                "total_events": timeline["metadata"]["total_events"]
            }
        },
        "timeline_improvements": timeline_improvements,
        "evidence_references": evidence_refs,
        "github_pages_structure": gh_pages_structure,
        "recommendations": {
            "high_priority": [
                "Add crime_category to all events (currently 69 events marked as 'unknown')",
                "Add phase assignment to all events (currently 69 events marked as 'unknown')",
                "Enhance GitHub Pages with direct ad-res-j7 evidence links",
                "Create application-specific evidence pages",
                "Add timeline visualizations to each application page"
            ],
            "medium_priority": [
                "Cross-reference events with timeline phases",
                "Add more detailed evidence descriptions",
                "Create entity relationship diagrams",
                "Add financial impact visualizations"
            ],
            "low_priority": [
                "Add more metadata to entities",
                "Enhance relation descriptions",
                "Create additional timeline views (by entity, by category)"
            ]
        }
    }
    
    # Save report
    output_path = base_path / "REFINEMENT_REPORT_2025_11_20.json"
    save_json(report, output_path)
    
    print(f"\n✓ Refinement report saved to: {output_path}")
    
    # Print summary
    print("\n" + "="*80)
    print("REFINEMENT SUMMARY")
    print("="*80)
    print(f"\nCurrent State:")
    print(f"  - Entities: {report['current_state']['entities']['total']}")
    print(f"  - Events: {report['current_state']['events']['total']}")
    print(f"  - Relations: {report['current_state']['relations']['total']}")
    print(f"  - Timeline Phases: {report['current_state']['timeline']['phases']}")
    
    print(f"\nHigh Priority Recommendations:")
    for rec in report['recommendations']['high_priority']:
        print(f"  - {rec}")
    
    print(f"\nEvidence References:")
    print(f"  - ad-res-j7 directories found: {evidence_refs['total_directories']}")
    print(f"  - Repository: {evidence_refs['repository_url']}")

if __name__ == "__main__":
    main()
