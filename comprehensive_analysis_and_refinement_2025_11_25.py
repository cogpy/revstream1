#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script
Analyzes entities, relations, events, and timelines
Identifies improvements based on timeline events and evidence
Cross-references with ad-res-j7 repository
"""

import json
import os
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS_DIR = BASE_DIR / "data_models"
DOCS_DIR = BASE_DIR / "docs"

# Load latest data models
def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_entities():
    """Analyze entities data model"""
    entities_file = DATA_MODELS_DIR / "entities" / "entities_refined_2025_11_25_v11.json"
    entities_data = load_json(entities_file)
    
    analysis = {
        "total_entities": 0,
        "entities_by_type": defaultdict(int),
        "entities_with_evidence": 0,
        "entities_with_github_pages": 0,
        "entities_with_ad_res_j7": 0,
        "entities_missing_evidence": [],
        "entities_missing_github_pages": [],
        "entities_missing_ad_res_j7": []
    }
    
    for entity_type, entities_list in entities_data.get("entities", {}).items():
        if isinstance(entities_list, list):
            for entity in entities_list:
                analysis["total_entities"] += 1
                analysis["entities_by_type"][entity_type] += 1
                
                # Check evidence
                if entity.get("evidence_files") or entity.get("evidence_urls"):
                    analysis["entities_with_evidence"] += 1
                else:
                    analysis["entities_missing_evidence"].append(entity.get("entity_id", "UNKNOWN"))
                
                # Check GitHub Pages reference
                if entity.get("github_pages_reference"):
                    analysis["entities_with_github_pages"] += 1
                else:
                    analysis["entities_missing_github_pages"].append(entity.get("entity_id", "UNKNOWN"))
                
                # Check ad-res-j7 reference
                if entity.get("ad_res_j7_references") or entity.get("evidence_repository"):
                    analysis["entities_with_ad_res_j7"] += 1
                else:
                    analysis["entities_missing_ad_res_j7"].append(entity.get("entity_id", "UNKNOWN"))
    
    return analysis

def analyze_events():
    """Analyze events data model"""
    events_file = DATA_MODELS_DIR / "events" / "events_refined_2025_11_25_v12.json"
    events_data = load_json(events_file)
    
    analysis = {
        "total_events": len(events_data.get("events", [])),
        "events_by_category": defaultdict(int),
        "events_by_phase": defaultdict(int),
        "events_with_financial_impact": 0,
        "events_with_evidence": 0,
        "events_with_github_pages": 0,
        "events_missing_evidence": [],
        "events_missing_github_pages": [],
        "total_financial_impact": 0,
        "financial_impact_by_category": defaultdict(float)
    }
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "unknown")
        phase = event.get("timeline_phase", "unknown")
        
        analysis["events_by_category"][category] += 1
        analysis["events_by_phase"][phase] += 1
        
        # Check financial impact
        if event.get("financial_impact"):
            analysis["events_with_financial_impact"] += 1
            # Try to extract numeric value
            impact_str = str(event.get("financial_impact", "0"))
            # Remove currency symbols and commas
            impact_str = impact_str.replace("R", "").replace(",", "").replace("+", "").strip()
            try:
                if "-" in impact_str:
                    # Handle ranges like "140,000 - 280,000"
                    parts = impact_str.split("-")
                    impact_value = float(parts[1].strip())
                else:
                    impact_value = float(impact_str)
                analysis["total_financial_impact"] += impact_value
                analysis["financial_impact_by_category"][category] += impact_value
            except (ValueError, IndexError):
                pass
        
        # Check evidence
        if event.get("evidence") or event.get("evidence_files"):
            analysis["events_with_evidence"] += 1
        else:
            analysis["events_missing_evidence"].append(event_id)
        
        # Check GitHub Pages reference
        if event.get("github_pages_reference"):
            analysis["events_with_github_pages"] += 1
        else:
            analysis["events_missing_github_pages"].append(event_id)
    
    return analysis

def analyze_relations():
    """Analyze relations data model"""
    relations_file = DATA_MODELS_DIR / "relations" / "relations_refined_2025_11_25_v9.json"
    relations_data = load_json(relations_file)
    
    analysis = {
        "total_relations": 0,
        "relations_by_type": defaultdict(int),
        "relations_with_evidence": 0,
        "relations_with_github_pages": 0,
        "relations_missing_evidence": [],
        "relations_missing_github_pages": []
    }
    
    for relation_type, relations_list in relations_data.get("relations", {}).items():
        if isinstance(relations_list, list):
            for relation in relations_list:
                analysis["total_relations"] += 1
                analysis["relations_by_type"][relation_type] += 1
                
                relation_id = relation.get("relation_id", "UNKNOWN")
                
                # Check evidence
                if relation.get("evidence"):
                    analysis["relations_with_evidence"] += 1
                else:
                    analysis["relations_missing_evidence"].append(relation_id)
                
                # Check GitHub Pages reference
                if relation.get("github_pages_reference"):
                    analysis["relations_with_github_pages"] += 1
                else:
                    analysis["relations_missing_github_pages"].append(relation_id)
    
    return analysis

def analyze_timeline():
    """Analyze timeline data model"""
    timeline_file = DATA_MODELS_DIR / "timelines" / "timeline_refined_2025_11_25_v10.json"
    timeline_data = load_json(timeline_file)
    
    analysis = {
        "total_phases": 0,
        "total_events_in_timeline": timeline_data.get("metadata", {}).get("total_events", 0),
        "period_start": timeline_data.get("metadata", {}).get("period_start", "unknown"),
        "period_end": timeline_data.get("metadata", {}).get("period_end", "unknown"),
        "phases": [],
        "total_financial_impact": 0
    }
    
    for phase_key, phase_data in timeline_data.get("timeline_phases", {}).items():
        if isinstance(phase_data, dict):
            analysis["total_phases"] += 1
            phase_info = {
                "phase_id": phase_data.get("phase_id"),
                "phase_name": phase_data.get("phase_name"),
                "duration_days": phase_data.get("duration_days", 0),
                "event_count": phase_data.get("event_count", 0),
                "financial_impact": phase_data.get("financial_impact", "Unknown"),
                "has_github_pages": bool(phase_data.get("github_pages_reference")),
                "has_evidence_index": bool(phase_data.get("comprehensive_evidence_index"))
            }
            analysis["phases"].append(phase_info)
            
            # Try to extract financial impact
            impact_str = str(phase_data.get("financial_impact", "0"))
            impact_str = impact_str.replace("R", "").replace(",", "").replace("+", "").strip()
            try:
                if impact_str and impact_str.lower() != "unknown":
                    impact_value = float(impact_str)
                    analysis["total_financial_impact"] += impact_value
            except ValueError:
                pass
    
    return analysis

def identify_improvements():
    """Identify improvements based on analysis"""
    improvements = {
        "entities": [],
        "events": [],
        "relations": [],
        "timeline": [],
        "github_pages": [],
        "cross_references": []
    }
    
    # Analyze each component
    entities_analysis = analyze_entities()
    events_analysis = analyze_events()
    relations_analysis = analyze_relations()
    timeline_analysis = analyze_timeline()
    
    # Entity improvements
    if entities_analysis["entities_missing_evidence"]:
        improvements["entities"].append({
            "type": "missing_evidence",
            "count": len(entities_analysis["entities_missing_evidence"]),
            "entities": entities_analysis["entities_missing_evidence"][:10],  # First 10
            "action": "Add evidence files and URLs from ad-res-j7 repository"
        })
    
    if entities_analysis["entities_missing_github_pages"]:
        improvements["entities"].append({
            "type": "missing_github_pages",
            "count": len(entities_analysis["entities_missing_github_pages"]),
            "entities": entities_analysis["entities_missing_github_pages"][:10],
            "action": "Add GitHub Pages references for entity documentation"
        })
    
    # Event improvements
    if events_analysis["events_missing_evidence"]:
        improvements["events"].append({
            "type": "missing_evidence",
            "count": len(events_analysis["events_missing_evidence"]),
            "events": events_analysis["events_missing_evidence"][:10],
            "action": "Add evidence files from ad-res-j7 repository"
        })
    
    if events_analysis["events_missing_github_pages"]:
        improvements["events"].append({
            "type": "missing_github_pages",
            "count": len(events_analysis["events_missing_github_pages"]),
            "events": events_analysis["events_missing_github_pages"][:10],
            "action": "Add GitHub Pages references for event documentation"
        })
    
    # Relation improvements
    if relations_analysis["relations_missing_evidence"]:
        improvements["relations"].append({
            "type": "missing_evidence",
            "count": len(relations_analysis["relations_missing_evidence"]),
            "relations": relations_analysis["relations_missing_evidence"][:10],
            "action": "Add evidence for relationship documentation"
        })
    
    # GitHub Pages improvements
    improvements["github_pages"].append({
        "type": "organization",
        "action": "Ensure all application pages have clear evidence references",
        "priority": "high"
    })
    
    improvements["github_pages"].append({
        "type": "cross_reference",
        "action": "Add direct links to ad-res-j7 evidence files in all documentation",
        "priority": "high"
    })
    
    # Cross-reference improvements
    improvements["cross_references"].append({
        "type": "evidence_validation",
        "action": "Validate all evidence file paths in ad-res-j7 repository",
        "priority": "high"
    })
    
    return {
        "timestamp": datetime.now().isoformat(),
        "entities_analysis": entities_analysis,
        "events_analysis": events_analysis,
        "relations_analysis": relations_analysis,
        "timeline_analysis": timeline_analysis,
        "improvements": improvements
    }

def main():
    """Main analysis function"""
    print("Starting comprehensive analysis...")
    
    # Run analysis
    results = identify_improvements()
    
    # Save results
    output_file = BASE_DIR / "COMPREHENSIVE_ANALYSIS_2025_11_25.json"
    save_json(results, output_file)
    
    print(f"\nAnalysis complete. Results saved to {output_file}")
    print(f"\nSummary:")
    print(f"  Total Entities: {results['entities_analysis']['total_entities']}")
    print(f"  Total Events: {results['events_analysis']['total_events']}")
    print(f"  Total Relations: {results['relations_analysis']['total_relations']}")
    print(f"  Total Timeline Phases: {results['timeline_analysis']['total_phases']}")
    print(f"\nImprovements Identified:")
    print(f"  Entity improvements: {len(results['improvements']['entities'])}")
    print(f"  Event improvements: {len(results['improvements']['events'])}")
    print(f"  Relation improvements: {len(results['improvements']['relations'])}")
    print(f"  GitHub Pages improvements: {len(results['improvements']['github_pages'])}")
    print(f"  Cross-reference improvements: {len(results['improvements']['cross_references'])}")

if __name__ == "__main__":
    main()
