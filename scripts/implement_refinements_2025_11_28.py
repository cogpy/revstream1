#!/usr/bin/env python3
"""
Implement Refinements for Revenue Stream Case 2025-137857
Based on comprehensive analysis, this script:
1. Adds missing phase classifications to events
2. Enhances cross-references to ad-res-j7 evidence
3. Updates version numbers
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = REVSTREAM_ROOT / "data_models"

# Latest data model files
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities_refined_2025_11_27_v22.json"
EVENTS_FILE = DATA_MODELS_DIR / "events" / "events_refined_2025_11_28_v24.json"
RELATIONS_FILE = DATA_MODELS_DIR / "relations" / "relations.json"

# Output files
ENTITIES_OUTPUT = DATA_MODELS_DIR / "entities" / "entities_refined_2025_11_28_v23.json"
EVENTS_OUTPUT = DATA_MODELS_DIR / "events" / "events_refined_2025_11_28_v25.json"
RELATIONS_OUTPUT = DATA_MODELS_DIR / "relations" / "relations_refined_2025_11_28_v20.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def classify_missing_events(events_data):
    """Classify events that are missing phase assignments"""
    
    # Events without phase that need classification
    unclassified_events = {
        'EVENT_070': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_071': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_072': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_073': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_074': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_075': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_076': {'phase': 'PHASE_006', 'reason': 'Post-application activity'},
        'EVENT_077': {'phase': 'PHASE_006', 'reason': 'Post-application activity'}
    }
    
    events = events_data.get('events', [])
    updated_count = 0
    
    for event in events:
        event_id = event.get('event_id')
        if event_id in unclassified_events and not event.get('phase'):
            event['phase'] = unclassified_events[event_id]['phase']
            updated_count += 1
            print(f"  Classified {event_id} as {unclassified_events[event_id]['phase']}")
    
    return updated_count

def enhance_ad_res_j7_references(data, entity_type):
    """Add ad-res-j7 cross-references to entities/relations"""
    
    # Standard ad-res-j7 references by entity type
    standard_references = {
        'persons': [
            "ANNEXURES directory with evidence files",
            "case_2025_137857 directory with case documentation",
            "FINAL_AFFIDAVIT_PACKAGE with supporting affidavits",
            "evidence directory with categorized evidence"
        ],
        'organizations': [
            "CIPC documentation in ANNEXURES",
            "Corporate records in case_2025_137857",
            "Financial evidence in evidence directory"
        ],
        'relations': [
            "Relationship evidence in ANNEXURES",
            "Supporting documentation in case_2025_137857",
            "Cross-referenced in COMPREHENSIVE_EVIDENCE_INDEX.md"
        ]
    }
    
    updated_count = 0
    
    if entity_type == 'entities':
        entities = data.get('entities', {})
        
        # Update persons
        for person in entities.get('persons', []):
            if not person.get('ad_res_j7_references'):
                person['ad_res_j7_references'] = standard_references['persons'].copy()
                updated_count += 1
        
        # Update organizations
        for org in entities.get('organizations', []):
            if not org.get('ad_res_j7_references'):
                org['ad_res_j7_references'] = standard_references['organizations'].copy()
                updated_count += 1
    
    elif entity_type == 'relations':
        relations_dict = data.get('relations', {})
        
        for category, relations_list in relations_dict.items():
            if isinstance(relations_list, list):
                for relation in relations_list:
                    if isinstance(relation, dict) and not relation.get('ad_res_j7_references'):
                        relation['ad_res_j7_references'] = standard_references['relations'].copy()
                        updated_count += 1
    
    return updated_count

def update_metadata(data, version, changes):
    """Update metadata with new version and changes"""
    if 'metadata' not in data:
        data['metadata'] = {}
    
    data['metadata']['version'] = version
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['metadata']['changes'] = changes
    
    return data

def main():
    """Main execution"""
    print("=" * 80)
    print("IMPLEMENTING REFINEMENTS")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("=" * 80)
    print()
    
    # Load data
    print("Loading data models...")
    entities = load_json(ENTITIES_FILE)
    events = load_json(EVENTS_FILE)
    relations = load_json(RELATIONS_FILE)
    
    # Implement refinements
    print("\n1. Classifying missing event phases...")
    events_updated = classify_missing_events(events)
    print(f"   Updated {events_updated} events")
    
    print("\n2. Enhancing ad-res-j7 references in entities...")
    entities_updated = enhance_ad_res_j7_references(entities, 'entities')
    print(f"   Updated {entities_updated} entities")
    
    print("\n3. Enhancing ad-res-j7 references in relations...")
    relations_updated = enhance_ad_res_j7_references(relations, 'relations')
    print(f"   Updated {relations_updated} relations")
    
    # Update metadata
    print("\n4. Updating metadata...")
    entities = update_metadata(
        entities,
        "23.0",
        "Enhanced ad-res-j7 cross-references (2025-11-28)"
    )
    
    events = update_metadata(
        events,
        "25.0",
        "Classified missing event phases (2025-11-28)"
    )
    
    relations = update_metadata(
        relations,
        "20.0",
        "Enhanced ad-res-j7 cross-references (2025-11-28)"
    )
    
    # Save refined data
    print("\n5. Saving refined data models...")
    save_json(entities, ENTITIES_OUTPUT)
    print(f"   Saved: {ENTITIES_OUTPUT}")
    
    save_json(events, EVENTS_OUTPUT)
    print(f"   Saved: {EVENTS_OUTPUT}")
    
    save_json(relations, RELATIONS_OUTPUT)
    print(f"   Saved: {RELATIONS_OUTPUT}")
    
    print("\n" + "=" * 80)
    print("REFINEMENT COMPLETE")
    print("=" * 80)
    print(f"\nSummary:")
    print(f"  Events classified: {events_updated}")
    print(f"  Entities enhanced: {entities_updated}")
    print(f"  Relations enhanced: {relations_updated}")
    print(f"\nNew versions:")
    print(f"  Entities: v23.0")
    print(f"  Events: v25.0")
    print(f"  Relations: v20.0")
    print()

if __name__ == "__main__":
    main()
