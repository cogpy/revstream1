#!/usr/bin/env python3
"""
Update Data Models with New Legal Correspondence
Date: 2025-11-26
Purpose: Integrate new legal documents (Letter of Demand, Letter to Opposing Attorney) into data models
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
REVSTREAM1_PATH = Path("/home/ubuntu/revstream1")
DATA_MODELS_PATH = REVSTREAM1_PATH / "data_models"

# Input data models (latest versions)
ENTITIES_PATH = DATA_MODELS_PATH / "entities/entities_refined_2025_11_26_v20.json"
EVENTS_PATH = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v21.json"
RELATIONS_PATH = DATA_MODELS_PATH / "relations/relations_refined_2025_11_26_v17.json"

# Output paths (new versions)
OUTPUT_ENTITIES = DATA_MODELS_PATH / "entities/entities_refined_2025_11_26_v21.json"
OUTPUT_EVENTS = DATA_MODELS_PATH / "events/events_refined_2025_11_26_v22.json"
OUTPUT_RELATIONS = DATA_MODELS_PATH / "relations/relations_refined_2025_11_26_v18.json"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved: {filepath}")

def add_new_entities(entities_data):
    """Add Elliott Attorneys and Pottas Attorneys to entities model"""
    print("\n=== Adding New Entities ===")
    
    # Elliott Attorneys
    elliott_attorneys = {
        "entity_id": "ORG_011",
        "name": "Elliott Attorneys",
        "type": "law_firm",
        "role": "legal_representation",
        "agent_type": "neutral_third_party",
        "involvement_events": 3,
        "primary_actions": [
            "legal_representation_rynette_farrar",
            "defamation_claim",
            "letter_of_demand"
        ],
        "relationships": [
            "represents_PERSON_002"
        ],
        "contact_details": {
            "email": "keegan@elliottattorneys.co.za",
            "phone": "012 012 5067 / 012 012 5068",
            "address": "Office 12, Garsfontein Office Park, 645 Jacqueline Drive, Garsfontein, Pretoria",
            "website": "http://www.elliottattorneys.co.za"
        },
        "director": "KR Elliott (LLB)",
        "legal_status": "active",
        "timeline_events": [
            "EVENT_075",
            "EVENT_076",
            "EVENT_077"
        ],
        "evidence_files": [
            "ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf",
            "ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"
        ],
        "ad_res_j7_references": [
            "Letter of Demand on behalf of Rynette Farrar",
            "Letter to Pottas Attorneys regarding interdict violations"
        ],
        "github_pages_profile": "https://cogpy.github.io/revstream1/entities/ORG_011.html",
        "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md"
    }
    
    # Pottas Attorneys
    pottas_attorneys = {
        "entity_id": "ORG_012",
        "name": "Pottas Attorneys",
        "type": "law_firm",
        "role": "legal_representation",
        "agent_type": "antagonist_representative",
        "involvement_events": 2,
        "primary_actions": [
            "legal_representation_peter_faucitt",
            "application_filing"
        ],
        "relationships": [
            "represents_PERSON_001"
        ],
        "contact_details": {
            "email": "rudi@pottaslaw.co.za, monique@pottaslaw.co.za"
        },
        "legal_status": "active",
        "timeline_events": [
            "EVENT_076",
            "EVENT_077"
        ],
        "evidence_files": [
            "ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf",
            "ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"
        ],
        "ad_res_j7_references": [
            "Recipient of Letter of Demand",
            "Recipient of Letter regarding interdict violations"
        ],
        "github_pages_profile": "https://cogpy.github.io/revstream1/entities/ORG_012.html",
        "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md"
    }
    
    # Add to organizations
    entities_data["entities"]["organizations"].append(elliott_attorneys)
    entities_data["entities"]["organizations"].append(pottas_attorneys)
    
    # Update metadata
    entities_data["metadata"]["version"] = "21.0"
    entities_data["metadata"]["total_entities"] = 32
    entities_data["metadata"]["last_updated"] = "2025-11-26"
    entities_data["metadata"]["changes"] = "Added Elliott Attorneys and Pottas Attorneys entities (2025-11-26)"
    
    print(f"✓ Added 2 new entities (Elliott Attorneys, Pottas Attorneys)")
    return entities_data

def add_new_events(events_data):
    """Add 4 new events related to legal correspondence"""
    print("\n=== Adding New Events ===")
    
    new_events = [
        {
            "event_id": "EVENT_074",
            "date": "2025-11-25",
            "title": "Application 3 Dismissed by Court",
            "category": "legal_proceedings",
            "event_type": "court_decision",
            "perpetrators": [],
            "victims": ["PERSON_001"],
            "entities_involved": ["PERSON_001", "PERSON_004", "PERSON_005"],
            "description": "Application 3 (Contact Interdict against Jacqueline Faucitt) dismissed by court. Peter Faucitt's third application unsuccessful.",
            "financial_impact": "N/A",
            "legal_significance": "peter_third_application_unsuccessful",
            "evidence": [
                "court_order_dismissal",
                "KF0019_letter_reference"
            ],
            "pattern": "legal_response",
            "timeline_phase": "PHASE_007",
            "extended_evidence_note": "Referenced in Elliott Attorneys letter KF0019",
            "related_applications": ["APPLICATION_3"],
            "evidence_files": [
                "./ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"
            ],
            "github_pages_url": "https://cogpy.github.io/revstream1/events/EVENT_074.html",
            "timeline_reference": "https://cogpy.github.io/revstream1/timeline.html#EVENT_074",
            "related_application": "APPLICATION_3",
            "application_url": "https://cogpy.github.io/revstream1/application-3.html"
        },
        {
            "event_id": "EVENT_075",
            "date": "2025-11-26",
            "title": "Rynette Farrar Retains Legal Counsel",
            "category": "legal_response",
            "event_type": "legal_representation",
            "perpetrators": [],
            "victims": [],
            "entities_involved": ["PERSON_002", "ORG_011"],
            "description": "Rynette Farrar retains Elliott Attorneys to represent her interests and pursue defamation counterclaim strategy against allegations made in Jacqueline's answering affidavit.",
            "financial_impact": "N/A",
            "legal_significance": "defamation_counterclaim_strategy",
            "evidence": [
                "KL0034_letter_of_demand",
                "KF0019_letter_to_opposing_attorney"
            ],
            "pattern": "legal_escalation",
            "timeline_phase": "PHASE_007",
            "extended_evidence_note": "Elliott Attorneys retained on behalf of Rynette Farrar",
            "related_applications": ["APPLICATION_1"],
            "evidence_files": [
                "./ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf",
                "./ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"
            ],
            "github_pages_url": "https://cogpy.github.io/revstream1/events/EVENT_075.html",
            "timeline_reference": "https://cogpy.github.io/revstream1/timeline.html#EVENT_075",
            "related_application": "APPLICATION_1",
            "application_url": "https://cogpy.github.io/revstream1/application-1.html"
        },
        {
            "event_id": "EVENT_076",
            "date": "2025-11-26",
            "title": "Letter of Demand Issued (Defamation)",
            "category": "legal_correspondence",
            "event_type": "letter_of_demand",
            "perpetrators": [],
            "victims": ["PERSON_004"],
            "entities_involved": ["ORG_011", "PERSON_002", "PERSON_004", "ORG_012"],
            "description": "Elliott Attorneys issues Letter of Demand (KL0034) on behalf of Rynette Farrar demanding retraction, apology, and cease and desist from defamatory allegations made in Jacqueline's answering affidavit. 48-hour deadline imposed.",
            "financial_impact": "Potential punitive costs",
            "legal_significance": "defamation_claim_formal_demand",
            "evidence": [
                "KL0034_letter_of_demand"
            ],
            "pattern": "legal_escalation",
            "timeline_phase": "PHASE_007",
            "extended_evidence_note": "Seven specific allegations identified as defamatory",
            "related_applications": ["APPLICATION_1"],
            "evidence_files": [
                "./ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf"
            ],
            "allegations_addressed": [
                "payment_diversion",
                "bank_account_control",
                "uk_business_revenue_theft",
                "domain_unlawful_competition",
                "customer_redirection",
                "false_photos_brand_damage",
                "stock_theft_risk"
            ],
            "deadline": "48 hours from receipt",
            "github_pages_url": "https://cogpy.github.io/revstream1/events/EVENT_076.html",
            "timeline_reference": "https://cogpy.github.io/revstream1/timeline.html#EVENT_076",
            "related_application": "APPLICATION_1",
            "application_url": "https://cogpy.github.io/revstream1/application-1.html"
        },
        {
            "event_id": "EVENT_077",
            "date": "2025-11-26",
            "title": "Ongoing Interdict Violations Reported",
            "category": "interdict_violation",
            "event_type": "contempt_of_court",
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_004", "PERSON_005"],
            "entities_involved": ["PERSON_001", "ORG_011", "ORG_012"],
            "description": "Elliott Attorneys reports that Peter has 'once again, removed the work phone' from staff at common home, preventing stock handling. Potential contempt of court violation of initial interdict order.",
            "financial_impact": "Business disruption",
            "legal_significance": "contempt_of_court_ongoing_violations",
            "evidence": [
                "KF0019_letter_to_opposing_attorney"
            ],
            "pattern": "interdict_violation",
            "timeline_phase": "PHASE_007",
            "extended_evidence_note": "Ongoing violations of August 19, 2025 interdict order",
            "related_applications": ["APPLICATION_1"],
            "evidence_files": [
                "./ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"
            ],
            "github_pages_url": "https://cogpy.github.io/revstream1/events/EVENT_077.html",
            "timeline_reference": "https://cogpy.github.io/revstream1/timeline.html#EVENT_077",
            "related_application": "APPLICATION_1",
            "application_url": "https://cogpy.github.io/revstream1/application-1.html"
        }
    ]
    
    # Add new events to events list
    events_data["events"].extend(new_events)
    
    # Update metadata
    events_data["metadata"]["version"] = "22.0"
    events_data["metadata"]["total_events"] = 77
    events_data["metadata"]["last_updated"] = "2025-11-26"
    events_data["metadata"]["changes"] = "Added 4 new events: Application 3 dismissal, Rynette legal counsel, Letter of Demand, interdict violations (2025-11-26)"
    
    print(f"✓ Added 4 new events (EVENT_074 to EVENT_077)")
    return events_data

def add_new_relations(relations_data):
    """Add new legal representation relations"""
    print("\n=== Adding New Relations ===")
    
    new_relations = [
        {
            "relation_id": "REL_LEGAL_001",
            "relation_type": "legal_representation",
            "source_entity": "ORG_011",
            "target_entity": "PERSON_002",
            "strength": "formal_legal_representation",
            "legal_status": "active",
            "evidence": [
                "KL0034_letter_of_demand",
                "KF0019_letter_to_opposing_attorney"
            ],
            "start_date": "2025-11-26",
            "related_applications": ["APPLICATION_1"],
            "evidence_repository": "https://github.com/cogpy/ad-res-j7",
            "related_events": ["EVENT_075", "EVENT_076", "EVENT_077"],
            "github_pages_reference": "https://cogpy.github.io/revstream1/NETWORK_ANALYSIS.md#rel_legal_001",
            "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md",
            "github_pages_url": "https://cogpy.github.io/revstream1/relations/REL_LEGAL_001.html"
        },
        {
            "relation_id": "REL_LEGAL_002",
            "relation_type": "legal_representation",
            "source_entity": "ORG_012",
            "target_entity": "PERSON_001",
            "strength": "formal_legal_representation",
            "legal_status": "active",
            "evidence": [
                "KL0034_letter_of_demand",
                "KF0019_letter_to_opposing_attorney"
            ],
            "related_applications": ["APPLICATION_1", "APPLICATION_2", "APPLICATION_3"],
            "evidence_repository": "https://github.com/cogpy/ad-res-j7",
            "related_events": ["EVENT_074", "EVENT_076", "EVENT_077"],
            "github_pages_reference": "https://cogpy.github.io/revstream1/NETWORK_ANALYSIS.md#rel_legal_002",
            "comprehensive_evidence_index": "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md",
            "github_pages_url": "https://cogpy.github.io/revstream1/relations/REL_LEGAL_002.html"
        }
    ]
    
    # Add new relation category if it doesn't exist
    if "legal_representation_relations" not in relations_data["relations"]:
        relations_data["relations"]["legal_representation_relations"] = []
    
    relations_data["relations"]["legal_representation_relations"].extend(new_relations)
    
    # Update metadata
    relations_data["metadata"]["version"] = "18.0"
    relations_data["metadata"]["total_relations"] = 66
    relations_data["metadata"]["last_updated"] = "2025-11-26"
    relations_data["metadata"]["changes"] = "Added legal representation relations for Elliott Attorneys and Pottas Attorneys (2025-11-26)"
    
    print(f"✓ Added 2 new relations (REL_LEGAL_001, REL_LEGAL_002)")
    return relations_data

def main():
    """Main update process"""
    print("=" * 60)
    print("Data Model Update - New Legal Correspondence (2025-11-26)")
    print("=" * 60)
    
    # Load current data models
    print("\n=== Loading Current Data Models ===")
    entities_data = load_json(ENTITIES_PATH)
    events_data = load_json(EVENTS_PATH)
    relations_data = load_json(RELATIONS_PATH)
    print("✓ All data models loaded")
    
    # Add new data
    entities_data = add_new_entities(entities_data)
    events_data = add_new_events(events_data)
    relations_data = add_new_relations(relations_data)
    
    # Save updated models
    print("\n=== Saving Updated Data Models ===")
    save_json(entities_data, OUTPUT_ENTITIES)
    save_json(events_data, OUTPUT_EVENTS)
    save_json(relations_data, OUTPUT_RELATIONS)
    
    # Generate summary report
    print("\n" + "=" * 60)
    print("UPDATE COMPLETE")
    print("=" * 60)
    print(f"\nUpdated Models:")
    print(f"  - Entities: v{entities_data['metadata']['version']} (32 total)")
    print(f"  - Events: v{events_data['metadata']['version']} (77 total)")
    print(f"  - Relations: v{relations_data['metadata']['version']} (66 total)")
    print(f"\nNew Additions:")
    print(f"  ✓ 2 new entities (Elliott Attorneys, Pottas Attorneys)")
    print(f"  ✓ 4 new events (EVENT_074 to EVENT_077)")
    print(f"  ✓ 2 new relations (REL_LEGAL_001, REL_LEGAL_002)")
    print(f"  ✓ New annexure JF13 with 2 legal documents")

if __name__ == "__main__":
    main()
