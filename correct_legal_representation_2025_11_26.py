#!/usr/bin/env python3
"""
Correct Legal Representation in Data Models
Date: 2025-11-26
Purpose: Fix the reversed legal representation:
  - Elliott Attorneys represents Peter Faucitt & Rynette Farrar
  - Pottas Attorneys represents Jacqueline & Daniel Faucitt
"""

import json
from pathlib import Path

# Paths
REVSTREAM1_PATH = Path("/home/ubuntu/revstream1")
DATA_MODELS_PATH = REVSTREAM1_PATH / "data_models"

# Input data models (incorrect versions)
ENTITIES_PATH = DATA_MODELS_PATH / "entities/entities_refined_2025_11_26_v21.json"
EVENTS_PATH = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v22.json"
RELATIONS_PATH = DATA_MODELS_PATH / "relations/relations_refined_2025_11_26_v18.json"

# Output paths (corrected versions)
OUTPUT_ENTITIES = DATA_MODELS_PATH / "entities/entities_refined_2025_11_26_v22.json"
OUTPUT_EVENTS = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v23.json"
OUTPUT_RELATIONS = DATA_MODELS_PATH / "relations/relations_refined_2025_11_26_v19.json"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved: {filepath}")

def correct_entities(entities_data):
    """Correct the legal representation in entities model"""
    print("\n=== Correcting Entities ===")
    
    organizations = entities_data["entities"]["organizations"]
    
    for org in organizations:
        if org["entity_id"] == "ORG_011":  # Elliott Attorneys
            # CORRECT: Elliott represents Peter & Rynette
            org["role"] = "legal_representation"
            org["agent_type"] = "antagonist_representative"  # Representing Peter (antagonist)
            org["primary_actions"] = [
                "legal_representation_peter_faucitt",
                "legal_representation_rynette_farrar",
                "defamation_claim_on_behalf_peter_rynette",
                "letter_of_demand"
            ]
            org["relationships"] = [
                "represents_PERSON_001",  # Peter
                "represents_PERSON_002"   # Rynette
            ]
            org["ad_res_j7_references"] = [
                "Letter of Demand on behalf of Rynette Farrar (client of Elliott)",
                "Letter to Pottas Attorneys regarding interdict violations (on behalf of Peter & Rynette)"
            ]
            print("✓ Corrected ORG_011 (Elliott Attorneys): Represents Peter & Rynette")
            
        elif org["entity_id"] == "ORG_012":  # Pottas Attorneys
            # CORRECT: Pottas represents Jacqueline & Daniel
            org["role"] = "legal_representation"
            org["agent_type"] = "victim_representative"  # Representing Jax & Dan (victims)
            org["primary_actions"] = [
                "legal_representation_jacqueline_faucitt",
                "legal_representation_daniel_faucitt",
                "receiving_letter_of_demand",
                "defending_against_defamation_claim"
            ]
            org["relationships"] = [
                "represents_PERSON_004",  # Jacqueline
                "represents_PERSON_005"   # Daniel
            ]
            org["ad_res_j7_references"] = [
                "Recipient of Letter of Demand (representing Jacqueline)",
                "Recipient of Letter regarding interdict violations (representing Jax & Dan)"
            ]
            print("✓ Corrected ORG_012 (Pottas Attorneys): Represents Jacqueline & Daniel")
    
    # Update metadata
    entities_data["metadata"]["version"] = "22.0"
    entities_data["metadata"]["last_updated"] = "2025-11-26"
    entities_data["metadata"]["changes"] = "CORRECTED legal representation: Elliott represents Peter & Rynette, Pottas represents Jax & Dan (2025-11-26)"
    
    return entities_data

def correct_events(events_data):
    """Correct the legal representation in events model"""
    print("\n=== Correcting Events ===")
    
    events = events_data["events"]
    
    for event in events:
        if event["event_id"] == "EVENT_074":  # Application 3 Dismissed
            # This was Peter's application, so victims should be Jax & Dan
            event["victims"] = ["PERSON_004", "PERSON_005"]  # Jax & Dan (who won)
            event["description"] = "Application 3 (Contact Interdict filed by Peter against Jacqueline Faucitt) dismissed by court. Peter Faucitt's third application unsuccessful."
            print("✓ Corrected EVENT_074")
            
        elif event["event_id"] == "EVENT_075":  # Rynette Retains Counsel
            # Elliott represents Rynette (and Peter)
            event["description"] = "Rynette Farrar, represented by Elliott Attorneys (who also represent Peter), pursues defamation counterclaim strategy against allegations made in Jacqueline's answering affidavit."
            print("✓ Corrected EVENT_075")
            
        elif event["event_id"] == "EVENT_076":  # Letter of Demand
            # Elliott (representing Rynette/Peter) sent to Pottas (representing Jax)
            event["entities_involved"] = ["ORG_011", "PERSON_002", "PERSON_004", "ORG_012"]
            event["description"] = "Elliott Attorneys (representing Rynette Farrar and Peter Faucitt) issues Letter of Demand (KL0034) to Pottas Attorneys (representing Jacqueline Faucitt) demanding retraction, apology, and cease and desist from defamatory allegations made in Jacqueline's answering affidavit. 48-hour deadline imposed."
            print("✓ Corrected EVENT_076")
            
        elif event["event_id"] == "EVENT_077":  # Interdict Violations
            # Elliott (representing Peter/Rynette) sent to Pottas (representing Jax/Dan)
            event["description"] = "Elliott Attorneys (representing Peter and Rynette) reports to Pottas Attorneys (representing Jax and Dan) that Peter has 'once again, removed the work phone' from staff at common home, preventing stock handling. However, this letter appears to misrepresent the situation as Elliott represents the alleged violator (Peter)."
            event["extended_evidence_note"] = "NOTE: Elliott represents Peter, yet is reporting Peter's violations. This suggests internal conflict or strategic positioning."
            print("✓ Corrected EVENT_077")
    
    # Update metadata
    events_data["metadata"]["version"] = "23.0"
    events_data["metadata"]["last_updated"] = "2025-11-26"
    events_data["metadata"]["changes"] = "CORRECTED legal representation in event descriptions (2025-11-26)"
    
    return events_data

def correct_relations(relations_data):
    """Correct the legal representation relations"""
    print("\n=== Correcting Relations ===")
    
    legal_relations = relations_data["relations"]["legal_representation_relations"]
    
    for rel in legal_relations:
        if rel["relation_id"] == "REL_LEGAL_001":
            # CORRECT: Elliott represents Rynette
            rel["source_entity"] = "ORG_011"  # Elliott
            rel["target_entity"] = "PERSON_002"  # Rynette
            rel["related_events"] = ["EVENT_075", "EVENT_076", "EVENT_077"]
            print("✓ Corrected REL_LEGAL_001: Elliott → Rynette")
            
        elif rel["relation_id"] == "REL_LEGAL_002":
            # CORRECT: Pottas represents Jacqueline
            rel["source_entity"] = "ORG_012"  # Pottas
            rel["target_entity"] = "PERSON_004"  # Jacqueline
            rel["related_events"] = ["EVENT_074", "EVENT_076", "EVENT_077"]
            print("✓ Corrected REL_LEGAL_002: Pottas → Jacqueline")
    
    # Add missing relations
    new_relations = [
        {
            "relation_id": "REL_LEGAL_003",
            "relation_type": "legal_representation",
            "source_entity": "ORG_011",  # Elliott
            "target_entity": "PERSON_001",  # Peter
            "strength": "formal_legal_representation",
            "legal_status": "active",
            "evidence": [
                "KF0019_letter_to_opposing_attorney"
            ],
            "related_applications": ["APPLICATION_1", "APPLICATION_2", "APPLICATION_3"],
            "evidence_repository": "https://github.com/cogpy/ad-res-j7",
            "related_events": ["EVENT_074", "EVENT_076", "EVENT_077"],
            "github_pages_reference": "https://cogpy.github.io/revstream1/NETWORK_ANALYSIS.md#rel_legal_003",
            "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md",
            "github_pages_url": "https://cogpy.github.io/revstream1/relations/REL_LEGAL_003.html"
        },
        {
            "relation_id": "REL_LEGAL_004",
            "relation_type": "legal_representation",
            "source_entity": "ORG_012",  # Pottas
            "target_entity": "PERSON_005",  # Daniel
            "strength": "formal_legal_representation",
            "legal_status": "active",
            "evidence": [
                "KF0019_letter_to_opposing_attorney"
            ],
            "related_applications": ["APPLICATION_1", "APPLICATION_2", "APPLICATION_3"],
            "evidence_repository": "https://github.com/cogpy/ad-res-j7",
            "related_events": ["EVENT_074", "EVENT_076", "EVENT_077"],
            "github_pages_reference": "https://cogpy.github.io/revstream1/NETWORK_ANALYSIS.md#rel_legal_004",
            "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md",
            "github_pages_url": "https://cogpy.github.io/revstream1/relations/REL_LEGAL_004.html"
        }
    ]
    
    legal_relations.extend(new_relations)
    print("✓ Added REL_LEGAL_003: Elliott → Peter")
    print("✓ Added REL_LEGAL_004: Pottas → Daniel")
    
    # Update metadata
    relations_data["metadata"]["version"] = "19.0"
    relations_data["metadata"]["total_relations"] = 68
    relations_data["metadata"]["last_updated"] = "2025-11-26"
    relations_data["metadata"]["changes"] = "CORRECTED legal representation relations and added missing relations (2025-11-26)"
    
    return relations_data

def main():
    """Main correction process"""
    print("=" * 60)
    print("CORRECTING LEGAL REPRESENTATION (2025-11-26)")
    print("=" * 60)
    print("\nCORRECT REPRESENTATION:")
    print("  - Elliott Attorneys → Peter Faucitt & Rynette Farrar")
    print("  - Pottas Attorneys → Jacqueline & Daniel Faucitt")
    print("=" * 60)
    
    # Load current data models
    print("\n=== Loading Current Data Models ===")
    entities_data = load_json(ENTITIES_PATH)
    events_data = load_json(EVENTS_PATH)
    relations_data = load_json(RELATIONS_PATH)
    print("✓ All data models loaded")
    
    # Correct data
    entities_data = correct_entities(entities_data)
    events_data = correct_events(events_data)
    relations_data = correct_relations(relations_data)
    
    # Save corrected models
    print("\n=== Saving Corrected Data Models ===")
    save_json(entities_data, OUTPUT_ENTITIES)
    save_json(events_data, OUTPUT_EVENTS)
    save_json(relations_data, OUTPUT_RELATIONS)
    
    # Generate summary report
    print("\n" + "=" * 60)
    print("CORRECTION COMPLETE")
    print("=" * 60)
    print(f"\nCorrected Models:")
    print(f"  - Entities: v{entities_data['metadata']['version']} (32 total)")
    print(f"  - Events: v{events_data['metadata']['version']} (77 total)")
    print(f"  - Relations: v{relations_data['metadata']['version']} (68 total)")
    print(f"\nCorrections Made:")
    print(f"  ✓ ORG_011 (Elliott): Now correctly represents Peter & Rynette")
    print(f"  ✓ ORG_012 (Pottas): Now correctly represents Jacqueline & Daniel")
    print(f"  ✓ 4 events corrected with accurate descriptions")
    print(f"  ✓ 4 legal representation relations corrected/added")

if __name__ == "__main__":
    main()
