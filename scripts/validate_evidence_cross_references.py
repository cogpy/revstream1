#!/usr/bin/env python3
"""
Evidence Cross-Reference Validation Script
Validates evidence file paths between revstream1 and ad-res-j7
Identifies missing evidence and suggests improvements
"""

import json
import os
from pathlib import Path
from collections import defaultdict

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS_DIR = BASE_DIR / "data_models"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_all_files_in_ad_res_j7():
    """Get all files in ad-res-j7 repository"""
    all_files = []
    for root, dirs, files in os.walk(AD_RES_J7_DIR):
        for file in files:
            file_path = Path(root) / file
            relative_path = file_path.relative_to(AD_RES_J7_DIR)
            all_files.append(str(relative_path))
    return all_files

def validate_evidence_references():
    """Validate evidence references in data models"""
    
    # Get all files in ad-res-j7
    print("Scanning ad-res-j7 repository...")
    ad_res_j7_files = get_all_files_in_ad_res_j7()
    print(f"Found {len(ad_res_j7_files)} files in ad-res-j7")
    
    # Create a set for fast lookup
    ad_res_j7_files_set = set(ad_res_j7_files)
    
    validation_results = {
        "total_files_in_ad_res_j7": len(ad_res_j7_files),
        "entities_validation": {},
        "events_validation": {},
        "missing_evidence_files": [],
        "evidence_coverage": {},
        "recommendations": []
    }
    
    # Load entities
    entities_file = DATA_MODELS_DIR / "entities" / "entities_refined_2025_11_25_v11.json"
    entities_data = load_json(entities_file)
    
    # Validate entity evidence
    print("\nValidating entity evidence references...")
    entities_missing = []
    entities_found = []
    
    for entity_type, entities_list in entities_data.get("entities", {}).items():
        if isinstance(entities_list, list):
            for entity in entities_list:
                entity_id = entity.get("entity_id", "UNKNOWN")
                evidence_files = entity.get("evidence_files", [])
                
                for evidence_file in evidence_files:
                    # Clean up the path
                    clean_path = evidence_file.strip("./").strip("/")
                    
                    # Check if file exists in ad-res-j7
                    found = False
                    for ad_file in ad_res_j7_files:
                        if clean_path in ad_file or ad_file.endswith(clean_path):
                            found = True
                            entities_found.append({
                                "entity_id": entity_id,
                                "reference": evidence_file,
                                "actual_path": ad_file
                            })
                            break
                    
                    if not found:
                        # Check if it's a directory reference
                        matching_files = [f for f in ad_res_j7_files if clean_path in f]
                        if matching_files:
                            entities_found.append({
                                "entity_id": entity_id,
                                "reference": evidence_file,
                                "actual_path": f"{len(matching_files)} files in directory"
                            })
                        else:
                            entities_missing.append({
                                "entity_id": entity_id,
                                "reference": evidence_file
                            })
    
    validation_results["entities_validation"] = {
        "total_references": len(entities_found) + len(entities_missing),
        "found": len(entities_found),
        "missing": len(entities_missing),
        "missing_details": entities_missing[:20]  # First 20
    }
    
    # Load events
    events_file = DATA_MODELS_DIR / "events" / "events_refined_2025_11_25_v12.json"
    events_data = load_json(events_file)
    
    # Validate event evidence
    print("Validating event evidence references...")
    events_missing = []
    events_found = []
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id", "UNKNOWN")
        evidence_files = event.get("evidence_files", [])
        
        for evidence_file in evidence_files:
            # Clean up the path
            clean_path = evidence_file.strip("./").strip("/")
            
            # Check if file exists in ad-res-j7
            found = False
            for ad_file in ad_res_j7_files:
                if clean_path in ad_file or ad_file.endswith(clean_path):
                    found = True
                    events_found.append({
                        "event_id": event_id,
                        "reference": evidence_file,
                        "actual_path": ad_file
                    })
                    break
            
            if not found:
                # Check if it's a directory reference
                matching_files = [f for f in ad_res_j7_files if clean_path in f]
                if matching_files:
                    events_found.append({
                        "event_id": event_id,
                        "reference": evidence_file,
                        "actual_path": f"{len(matching_files)} files in directory"
                    })
                else:
                    events_missing.append({
                        "event_id": event_id,
                        "reference": evidence_file
                    })
    
    validation_results["events_validation"] = {
        "total_references": len(events_found) + len(events_missing),
        "found": len(events_found),
        "missing": len(events_missing),
        "missing_details": events_missing[:20]  # First 20
    }
    
    # Evidence coverage analysis
    print("\nAnalyzing evidence coverage...")
    
    # Key evidence categories
    evidence_categories = {
        "ANNEXURES": [f for f in ad_res_j7_files if f.startswith("ANNEXURES/")],
        "FINAL_AFFIDAVIT_PACKAGE": [f for f in ad_res_j7_files if f.startswith("FINAL_AFFIDAVIT_PACKAGE/")],
        "case_2025_137857": [f for f in ad_res_j7_files if f.startswith("case_2025_137857/")],
        "evidence": [f for f in ad_res_j7_files if f.startswith("evidence/")],
        "docs": [f for f in ad_res_j7_files if f.startswith("docs/")]
    }
    
    validation_results["evidence_coverage"] = {
        category: len(files) for category, files in evidence_categories.items()
    }
    
    # Recommendations
    validation_results["recommendations"] = [
        {
            "priority": "high",
            "category": "evidence_validation",
            "action": "Update evidence file paths to match actual ad-res-j7 structure",
            "affected_entities": len(entities_missing),
            "affected_events": len(events_missing)
        },
        {
            "priority": "high",
            "category": "github_pages",
            "action": "Add direct GitHub URLs for all evidence files",
            "benefit": "Improved accessibility and verification"
        },
        {
            "priority": "medium",
            "category": "evidence_index",
            "action": "Create comprehensive evidence index linking all data model references to actual files",
            "benefit": "Better evidence tracking and legal filing support"
        }
    ]
    
    return validation_results

def main():
    """Main validation function"""
    print("Starting evidence cross-reference validation...")
    
    results = validate_evidence_references()
    
    # Save results
    output_file = BASE_DIR / "EVIDENCE_VALIDATION_RESULTS_2025_11_25.json"
    save_json(results, output_file)
    
    print(f"\n{'='*60}")
    print("VALIDATION COMPLETE")
    print(f"{'='*60}")
    print(f"\nResults saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total files in ad-res-j7: {results['total_files_in_ad_res_j7']}")
    print(f"\nEntities Validation:")
    print(f"  Total references: {results['entities_validation']['total_references']}")
    print(f"  Found: {results['entities_validation']['found']}")
    print(f"  Missing: {results['entities_validation']['missing']}")
    print(f"\nEvents Validation:")
    print(f"  Total references: {results['events_validation']['total_references']}")
    print(f"  Found: {results['events_validation']['found']}")
    print(f"  Missing: {results['events_validation']['missing']}")
    print(f"\nEvidence Coverage by Category:")
    for category, count in results['evidence_coverage'].items():
        print(f"  {category}: {count} files")
    print(f"\nRecommendations: {len(results['recommendations'])}")
    for i, rec in enumerate(results['recommendations'], 1):
        print(f"  {i}. [{rec['priority'].upper()}] {rec['action']}")

if __name__ == "__main__":
    main()
