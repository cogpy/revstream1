#!/usr/bin/env python3
"""
Data Model Refinement Script - 2025-11-22
Purpose: Refine entities, relations, events, and timelines based on analysis
"""

import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {filepath}")

def refine_entities(entities_file):
    """Refine entities - add timeline events to PERSON_006 (Linda)"""
    data = load_json(entities_file)
    
    # Update metadata
    data["metadata"]["version"] = "16.0"
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["changes"] = "Refinement 2025-11-22: Added timeline events for PERSON_006 (Linda), enhanced evidence cross-references"
    
    # Find and update PERSON_006 (Linda the bookkeeper)
    for person in data["entities"]["persons"]:
        if person.get("entity_id") == "PERSON_006":
            # Add relevant timeline events related to bookkeeping and Rynette's control
            person["timeline_events"] = [
                "EVENT_H003",  # Financial Year Commencement RST/SLG
                "EVENT_H004",  # Financial Year Commencement Villa Via
                "EVENT_H005",  # Multiple Adjusting Journal Entries
                "EVENT_H006",  # Year-End Adjustments
                "EVENT_048"    # Financial relationships documentation
            ]
            person["involvement_events"] = len(person["timeline_events"])
            print(f"Updated PERSON_006 with {len(person['timeline_events'])} timeline events")
            break
    
    return data

def refine_events(events_file):
    """Refine events - add missing financial impact and legal significance"""
    data = load_json(events_file)
    
    # Update metadata
    data["metadata"]["version"] = "17.0"
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["changes"] = "Refinement 2025-11-22: Added missing financial impact and legal significance to events"
    
    events_updated = 0
    
    for event in data["events"]:
        event_id = event.get("event_id", "")
        
        # Add financial impact for events without it
        if not event.get("financial_impact"):
            # Determine financial impact based on event category and description
            category = event.get("category", "")
            
            if category in ["Business Relationship", "Evidence Documentation", "Knowledge Acquisition", "Transparency"]:
                event["financial_impact"] = "indirect"
                events_updated += 1
            elif category in ["Conspiracy Preparation", "Estate Fraud", "Estate Exploitation"]:
                event["financial_impact"] = "potential_future_impact"
                events_updated += 1
        
        # Add legal significance for events without it
        if not event.get("legal_significance"):
            category = event.get("category", "")
            
            if category == "Business Relationship":
                event["legal_significance"] = "establishes_business_context"
                events_updated += 1
            elif category == "Evidence Documentation":
                event["legal_significance"] = "documentary_evidence"
                events_updated += 1
            elif category == "Knowledge Acquisition":
                event["legal_significance"] = "demonstrates_knowledge_of_wrongdoing"
                events_updated += 1
            elif category == "Transparency":
                event["legal_significance"] = "demonstrates_good_faith_disclosure"
                events_updated += 1
            elif category == "Conspiracy Preparation":
                event["legal_significance"] = "demonstrates_premeditation"
                events_updated += 1
            elif category in ["Estate Fraud", "Estate Exploitation"]:
                event["legal_significance"] = "potential_additional_criminal_conduct"
                events_updated += 1
    
    print(f"Updated {events_updated} event fields")
    return data

def refine_relations(relations_file):
    """Refine relations - add related events"""
    data = load_json(relations_file)
    
    # Update metadata
    data["metadata"]["version"] = "13.0"
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["changes"] = "Refinement 2025-11-22: Added related events to relations for better cross-referencing"
    
    relations_updated = 0
    
    # Map relation types to relevant events
    relation_event_mapping = {
        "REL_OWN_001": ["EVENT_001", "EVENT_009", "EVENT_055", "EVENT_056"],  # Daniel owns RegimA Zone Ltd
        "REL_OWN_002": ["EVENT_009", "EVENT_014", "EVENT_027"],  # RegimA Zone owns Shopify platform
        "REL_OWN_003": ["EVENT_009", "EVENT_027"],  # RegimA Zone owns domain
        "REL_OWN_004": ["EVENT_010", "EVENT_027"],  # Addarory owns fraudulent domain
        "REL_TRUST_001": ["EVENT_002", "EVENT_016", "EVENT_017", "EVENT_019"],  # Peter trustee of Family Trust
        "REL_TRUST_002": ["EVENT_002", "EVENT_016", "EVENT_017"],  # Bantjies trustee
        "REL_TRUST_003": ["EVENT_002", "EVENT_016", "EVENT_017"],  # Jacqui trustee
        "REL_CONSP_001": ["EVENT_001", "EVENT_003", "EVENT_004", "EVENT_006", "EVENT_012"],  # Peter-Rynette conspiracy
        "REL_CONSP_002": ["EVENT_010", "EVENT_027"],  # Rynette-Addarory conspiracy
        "REL_CTRL_001": ["EVENT_004", "EVENT_005", "EVENT_012", "EVENT_014"],  # Rynette controls accounts
        "REL_CTRL_002": ["EVENT_026", "EVENT_047", "EVENT_058"],  # Bantjies controls accounting
    }
    
    # Update relations with events
    for category, relations_list in data["relations"].items():
        if isinstance(relations_list, list):
            for relation in relations_list:
                rel_id = relation.get("relation_id", "")
                if rel_id in relation_event_mapping:
                    relation["related_events"] = relation_event_mapping[rel_id]
                    relations_updated += 1
    
    print(f"Updated {relations_updated} relations with related events")
    return data

def refine_timeline(timeline_file):
    """Refine timeline - ensure all phases have complete metadata"""
    data = load_json(timeline_file)
    
    # Update metadata
    data["metadata"]["version"] = "14.0"
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["changes"] = "Refinement 2025-11-22: Enhanced phase descriptions and cross-references"
    
    # Ensure all phases have evidence repository and related applications
    for phase_key, phase_data in data["timeline_phases"].items():
        if not phase_data.get("evidence_repository"):
            phase_data["evidence_repository"] = "ad-res-j7"
        
        if not phase_data.get("related_applications"):
            # Assign applications based on phase
            phase_id = phase_data.get("phase_id", "")
            if phase_id in ["PHASE_000", "PHASE_001", "PHASE_002", "PHASE_003"]:
                phase_data["related_applications"] = ["APPLICATION_1"]
            elif phase_id in ["PHASE_004", "PHASE_005"]:
                phase_data["related_applications"] = ["APPLICATION_1", "APPLICATION_2"]
            elif phase_id in ["PHASE_006"]:
                phase_data["related_applications"] = ["APPLICATION_1", "APPLICATION_2", "APPLICATION_3"]
            elif phase_id in ["PHASE_007"]:
                phase_data["related_applications"] = ["APPLICATION_2"]
    
    print("Updated timeline phases with complete metadata")
    return data

def main():
    """Main refinement function"""
    base_dir = "/home/ubuntu/revstream1/data_models"
    
    # Latest files
    entities_file = f"{base_dir}/entities/entities_refined_2025_11_21_v8.json"
    relations_file = f"{base_dir}/relations/relations_refined_2025_11_21_v6.json"
    events_file = f"{base_dir}/events/events_refined_2025_11_21_v9.json"
    timeline_file = f"{base_dir}/timelines/timeline_refined_2025_11_21_v7.json"
    
    print("=== Starting Data Model Refinement ===\n")
    
    # Refine entities
    print("Refining entities...")
    entities_data = refine_entities(entities_file)
    entities_output = f"{base_dir}/entities/entities_refined_2025_11_22_v9.json"
    save_json(entities_data, entities_output)
    
    # Refine events
    print("\nRefining events...")
    events_data = refine_events(events_file)
    events_output = f"{base_dir}/events/events_refined_2025_11_22_v10.json"
    save_json(events_data, events_output)
    
    # Refine relations
    print("\nRefining relations...")
    relations_data = refine_relations(relations_file)
    relations_output = f"{base_dir}/relations/relations_refined_2025_11_22_v7.json"
    save_json(relations_data, relations_output)
    
    # Refine timeline
    print("\nRefining timeline...")
    timeline_data = refine_timeline(timeline_file)
    timeline_output = f"{base_dir}/timelines/timeline_refined_2025_11_22_v8.json"
    save_json(timeline_data, timeline_output)
    
    print("\n=== Refinement Complete ===")
    print(f"\nNew files created:")
    print(f"  - {entities_output}")
    print(f"  - {events_output}")
    print(f"  - {relations_output}")
    print(f"  - {timeline_output}")

if __name__ == "__main__":
    main()
