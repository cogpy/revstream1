#!/usr/bin/env python3
"""
Update models with FNB Response Email evidence (2025-06-18)

This script adds the FNB response email to the evidence chain, showing that:
1. FNB's legal department reviewed the matter
2. The bank mandate allows any director to act independently
3. FNB declined to hold a meeting as they are protected by the mandate
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
DATA_MODELS_DIR = DOCS_DIR / "data_models"
EVENTS_FILE = DATA_MODELS_DIR / "events.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timeline.json"
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"
RELATIONS_FILE = DATA_MODELS_DIR / "relations.json"

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")

def add_fnb_response_event():
    """Add the FNB response email event."""
    events = load_json(EVENTS_FILE)
    
    new_event = {
        "event_id": "EVENT_FNB_002",
        "date": "2025-06-18",
        "title": "FNB Declines Meeting - Bank Mandate Allows Independent Director Action",
        "description": "FNB's Business Relationship Manager Mpumi Netshipale responds to Peter and Jacqui, stating that following engagement with FNB's legal department, no meeting is necessary as FNB cannot be held liable for acting in accordance with a validly signed mandate. The email reveals that 'the current mandate states that any of the directors of the company may act independently of each other.'",
        "category": "BANKING_MANDATE",
        "severity": "HIGH",
        "evidence_strength": "CONCLUSIVE",
        "actors": ["PERSON_001", "PERSON_003", "ORG_FNB"],
        "evidence_refs": ["FNB_RESPONSE_EMAIL_2025_06_18"],
        "related_events": ["EVENT_FNB_001", "EVENT_012"],
        "legal_implications": [
            "Bank mandate confirms independent director authority",
            "FNB legal department reviewed and approved their position",
            "Directors must pass resolution to change mandate",
            "Corporate governance structure documented"
        ],
        "cross_references": {
            "entities": ["PERSON_001", "PERSON_003", "ORG_FNB", "ORG_RWD"],
            "relations": ["REL_FNB_001", "REL_FNB_002"],
            "timeline": "2025-06-18"
        }
    }
    
    # Check if event already exists
    existing_ids = [e.get("event_id") for e in events.get("events", [])]
    if "EVENT_FNB_002" not in existing_ids:
        events["events"].append(new_event)
        events["metadata"]["total_events"] = len(events["events"])
        events["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        events["metadata"]["version"] = "v28.0_FNB_RESPONSE_2026_01_29"
        save_json(EVENTS_FILE, events)
    else:
        print("EVENT_FNB_002 already exists")

def add_timeline_entry():
    """Add the FNB response to the timeline."""
    timeline = load_json(TIMELINE_FILE)
    
    new_entry = {
        "date": "2025-06-18",
        "event_count": 1,
        "events": ["EVENT_FNB_002"],
        "primary_category": "Banking Mandate",
        "description": "FNB's legal department confirms bank mandate allows any director to act independently. Meeting declined as FNB protected by validly signed mandate.",
        "key_actors": ["PERSON_001", "PERSON_003", "ORG_FNB"],
        "legal_significance": "high",
        "evidence_references": ["FNB_RESPONSE_EMAIL_2025_06_18"],
        "evidence": ["SF10 - FNB Response Email"]
    }
    
    # Check if entry already exists
    existing_dates = [e.get("date") for e in timeline.get("timeline", []) if "EVENT_FNB_002" in e.get("events", [])]
    if not existing_dates:
        timeline["timeline"].append(new_entry)
        timeline["timeline"].sort(key=lambda x: x.get("date", ""))
        timeline["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timeline["metadata"]["version"] = "v26.0_FNB_RESPONSE_2026_01_29"
        save_json(TIMELINE_FILE, timeline)
    else:
        print("Timeline entry for EVENT_FNB_002 already exists")

def add_fnb_entity():
    """Add FNB as an entity and Mpumi Netshipale."""
    entities = load_json(ENTITIES_FILE)
    
    # Add FNB entity if not exists
    fnb_entity = {
        "entity_id": "ORG_FNB",
        "name": "First National Bank (FNB)",
        "description": "Commercial bank providing banking services to RegimA Worldwide Distribution",
        "role": "banking_institution",
        "agent_type": "neutral",
        "key_contacts": [
            {
                "name": "Mpumi Netshipale",
                "role": "Business Relationship Manager",
                "email": "Mpumi.Netshipale@fnb.co.za",
                "phone": ["+27 87 030 0801", "+27 64 523 1839"]
            },
            {
                "name": "Michelle Habig",
                "role": "Relationship Analyst",
                "email": "mhabig@fnb.co.za",
                "phone": "+27 87 335 6829"
            },
            {
                "name": "Nondu Motlhala",
                "role": "FNB Staff",
                "email": "NMotlhala@fnb.co.za"
            }
        ],
        "evidence_refs": ["FNB_RESPONSE_EMAIL_2025_06_18", "PAF_FNB_FRAUD_LETTER_2025_06_17"]
    }
    
    # Check in organizations list
    orgs = entities.get("entities", {}).get("organizations", [])
    existing_ids = [e.get("entity_id") for e in orgs]
    if "ORG_FNB" not in existing_ids:
        if "organizations" not in entities["entities"]:
            entities["entities"]["organizations"] = []
        entities["entities"]["organizations"].append(fnb_entity)
        entities["metadata"]["total_entities"] = entities["metadata"].get("total_entities", 0) + 1
        entities["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entities["metadata"]["version"] = "v30.0_FNB_RESPONSE_2026_01_29"
        save_json(ENTITIES_FILE, entities)
    else:
        print("ORG_FNB already exists")

def add_fnb_relation():
    """Add the FNB response relation."""
    relations = load_json(RELATIONS_FILE)
    
    new_relation = {
        "relation_id": "REL_FNB_002",
        "relation_type": "bank_mandate_confirmation",
        "source_entity": "ORG_FNB",
        "target_entity": "ORG_RWD",
        "description": "FNB confirms bank mandate allows any director of RWD to act independently",
        "date": "2025-06-18",
        "evidence": ["FNB_RESPONSE_EMAIL_2025_06_18"],
        "strength": "conclusive",
        "legal_status": "documented",
        "legal_implications": [
            "Directors have independent authority on bank account",
            "No co-signature required for transactions",
            "FNB protected by validly signed mandate"
        ],
        "confidence": 1.0
    }
    
    # Add to banking_relations category
    if "banking_relations" not in relations["relations"]:
        relations["relations"]["banking_relations"] = []
    
    existing_ids = [r.get("relation_id") for r in relations["relations"].get("banking_relations", [])]
    if "REL_FNB_002" not in existing_ids:
        relations["relations"]["banking_relations"].append(new_relation)
        relations["metadata"]["total_relations"] = relations["metadata"].get("total_relations", 0) + 1
        relations["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        relations["metadata"]["version"] = "v25.0_FNB_RESPONSE_2026_01_29"
        save_json(RELATIONS_FILE, relations)
    else:
        print("REL_FNB_002 already exists")

def create_evidence_chain_update():
    """Create an evidence chain update document."""
    chain = {
        "title": "FNB Response Email Evidence Chain",
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "evidence_id": "FNB_RESPONSE_EMAIL_2025_06_18",
        "timeline_sequence": [
            {
                "date": "2025-06-06",
                "event": "Daniel exposes fraud to Bantjies",
                "days_offset": 0
            },
            {
                "date": "2025-06-07",
                "event": "Secret card cancellations",
                "days_offset": 1
            },
            {
                "date": "2025-06-17",
                "event": "Peter writes FNB fraud letter",
                "days_offset": 11
            },
            {
                "date": "2025-06-17",
                "event": "FNB schedules meeting (1:42 PM)",
                "days_offset": 11
            },
            {
                "date": "2025-06-18",
                "event": "Pete requests meeting time change (08:17)",
                "days_offset": 12
            },
            {
                "date": "2025-06-18",
                "event": "FNB declines meeting - cites mandate (4:51 PM)",
                "days_offset": 12
            }
        ],
        "key_revelation": {
            "quote": "The current mandate states that any of the directors of the company may act independently of each other.",
            "source": "Mpumi Netshipale, FNB Business Relationship Manager",
            "implications": [
                "Each director has independent authority to act on the account",
                "No co-signature required for transactions",
                "FNB cannot be held liable for following the mandate",
                "Directors must pass a resolution to change this arrangement"
            ]
        },
        "legal_significance": {
            "civil_threshold": "EXCEEDED",
            "criminal_threshold": "STRENGTHENED",
            "corporate_governance": "DOCUMENTED"
        }
    }
    
    save_json(DATA_MODELS_DIR / "FNB_RESPONSE_EVIDENCE_CHAIN.json", chain)

def main():
    print("=" * 60)
    print("Updating Models with FNB Response Email Evidence")
    print("=" * 60)
    
    print("\n1. Adding FNB Response Event...")
    add_fnb_response_event()
    
    print("\n2. Adding Timeline Entry...")
    add_timeline_entry()
    
    print("\n3. Adding FNB Entity...")
    add_fnb_entity()
    
    print("\n4. Adding FNB Relation...")
    add_fnb_relation()
    
    print("\n5. Creating Evidence Chain Update...")
    create_evidence_chain_update()
    
    print("\n" + "=" * 60)
    print("Model Update Complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
