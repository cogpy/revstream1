#!/usr/bin/env python3
"""
Add FNB Fraud Letter Event (2025-06-17) to the data models.
This letter from Peter Faucitt to FNB is critical evidence showing:
1. Peter's awareness of suspected fraud
2. His request to cancel 3 debit cards
3. His warning to FNB about being "accessory after the fact"
4. His acknowledgment of potential Exchange Control violations
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
EVENTS_PATH = Path("/home/ubuntu/revstream1/docs/data_models/events.json")
TIMELINE_PATH = Path("/home/ubuntu/revstream1/docs/data_models/timeline.json")
ENTITIES_PATH = Path("/home/ubuntu/revstream1/docs/data_models/entities/entities.json")
RELATIONS_PATH = Path("/home/ubuntu/revstream1/docs/data_models/relations.json")

def load_json(path):
    """Load JSON file."""
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    """Save JSON file with backup."""
    # Create backup
    backup_path = path.with_suffix(f'.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    if path.exists():
        with open(path, 'r') as f:
            backup_data = f.read()
        with open(backup_path, 'w') as f:
            f.write(backup_data)
    
    # Save new data
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")

def add_fnb_fraud_letter_event():
    """Add the FNB Fraud Letter event."""
    
    # New event
    new_event = {
        "event_id": "EVENT_FNB_001",
        "date": "2025-06-17",
        "title": "Peter Faucitt Writes FNB Fraud Letter - Acknowledges Suspected Fraud",
        "category": "fraud_acknowledgment",
        "event_type": "director_admission",
        "perpetrators": [],
        "victims": [],
        "entities_involved": [
            "PERSON_001",  # Peter Faucitt
            "ORG_001",     # RegimA Worldwide Distribution
            "BANK_001"     # FNB
        ],
        "description": "Peter Faucitt writes formal letter to FNB (Nondu Motlhala) regarding suspected fraud on RWD account 62323196362. Letter confirms: (1) Prior written request to cancel 3 debit cards due to suspected fraud, (2) Concern about 'perpetuation of suspected fraud', (3) Warning to FNB about being 'accessory after the fact', (4) Acknowledgment of potential Exchange Control Regulations violations due to 'dollar-based subscription expense'. This letter was written 11 days after Dan exposed fraud to Bantjies (2025-06-06) and 10 days after secret card cancellations (2025-06-07).",
        "financial_impact": "unknown_amount",
        "legal_significance": "CRITICAL: Director's written acknowledgment of suspected fraud on company account",
        "significance": "CRITICAL: Peter's own letter admits suspected fraud, contradicting his court filings where he claims Dan and Jax are perpetrators. Also acknowledges potential Exchange Control violations.",
        "evidence": [
            "PAF_FNB_FRAUD_LETTER_2025_06_17.jpg",
            "PAF_FNB_FRAUD_LETTER_2025_06_17_OCR.md"
        ],
        "evidence_location": "evidence/FNB_FRAUD_LETTER_2025_06_17/",
        "pattern": "fraud_acknowledgment_by_perpetrator",
        "timeline_phase": "PHASE_3",
        "phase": "PHASE_3",
        "ad_res_j7_evidence": [],
        "evidence_enhanced": datetime.now().isoformat(),
        "burden_of_proof": "civil_50%_exceeded",
        "criminal_threshold": "95%_strengthened",
        "related_events": [
            "EVENT_011",  # Daniel Finalizes Fraud Reports (2025-06-06)
            "EVENT_057",  # Daniel Sends Reports to Bantjies (2025-06-06)
            "EVENT_012"   # Secret Card Cancellations (2025-06-07)
        ],
        "key_admissions": [
            "Suspected fraud on RWD account",
            "Prior request to cancel 3 debit cards",
            "Concern about fraud perpetuation",
            "FNB could be accessory after the fact",
            "Potential Exchange Control violations",
            "Dollar-based subscription expenses"
        ],
        "contradictions_with_court_filings": [
            "Peter claims Dan and Jax are perpetrators in court",
            "This letter shows Peter was aware of fraud on RWD account",
            "Peter was taking action to stop fraud",
            "Peter acknowledged company may be transgressing Exchange Control"
        ],
        "letterhead_details": {
            "company": "RegimA Worldwide Distribution (Pty) Ltd",
            "co_reg": "2011/005722/07",
            "vat_no": "4320262621",
            "email": "rynette@regima.zone",
            "head_office": "50 Van Buuren Road, Bedfordview, 2008",
            "physical_address": "20 River Road, Morninghill, Bedfordview, 2007, RSA"
        },
        "recipient": {
            "name": "Nondu Motlhala",
            "organization": "FNB"
        },
        "account_number": "62323196362",
        "timing_analysis": {
            "days_after_fraud_exposure": 11,
            "days_after_card_cancellation": 10,
            "t_minus_ketoni_payout": "T-11 months"
        }
    }
    
    # Load and update events
    events_data = load_json(EVENTS_PATH)
    
    # Check if event already exists
    existing_ids = [e.get('event_id') for e in events_data.get('events', [])]
    if new_event['event_id'] not in existing_ids:
        events_data['events'].append(new_event)
        events_data['metadata']['total_events'] = len(events_data['events'])
        events_data['metadata']['last_updated'] = datetime.now().isoformat()
        events_data['metadata']['version'] = "27.0_FNB_FRAUD_LETTER_2026_01_29"
        events_data['metadata']['changes'] = "Added EVENT_FNB_001: Peter Faucitt FNB Fraud Letter (2025-06-17)"
        print(f"Added event: {new_event['event_id']}")
    else:
        print(f"Event {new_event['event_id']} already exists")
    
    save_json(EVENTS_PATH, events_data)
    
    return new_event

def add_timeline_entry():
    """Add timeline entry for the FNB Fraud Letter."""
    
    new_timeline_entry = {
        "date": "2025-06-17",
        "event_count": 1,
        "events": ["EVENT_FNB_001"],
        "primary_category": "fraud_acknowledgment",
        "description": "Peter Faucitt writes FNB letter acknowledging suspected fraud on RWD account",
        "key_actors": ["PERSON_001"],
        "legal_significance": "CRITICAL: Director's written admission of suspected fraud",
        "evidence_references": [
            "PAF_FNB_FRAUD_LETTER_2025_06_17.jpg",
            "PAF_FNB_FRAUD_LETTER_2025_06_17_OCR.md"
        ],
        "evidence": [
            "FNB Fraud Letter",
            "OCR Extraction"
        ],
        "phase": "PHASE_3",
        "timing": "T+11 days after fraud exposure to Bantjies",
        "financial_impact": "Acknowledges potential Exchange Control violations"
    }
    
    # Load and update timeline
    timeline_data = load_json(TIMELINE_PATH)
    
    # Check if entry already exists
    existing_dates = [t.get('date') for t in timeline_data.get('timeline', [])]
    if new_timeline_entry['date'] not in existing_dates:
        timeline_data['timeline'].append(new_timeline_entry)
        # Sort by date
        timeline_data['timeline'].sort(key=lambda x: x.get('date', ''))
        timeline_data['metadata']['last_updated'] = datetime.now().isoformat()
        timeline_data['metadata']['version'] = "25.0_FNB_FRAUD_LETTER_2026_01_29"
        timeline_data['metadata']['changes'] = "Added FNB Fraud Letter timeline entry (2025-06-17)"
        print(f"Added timeline entry for: {new_timeline_entry['date']}")
    else:
        print(f"Timeline entry for {new_timeline_entry['date']} already exists - updating")
        # Update existing entry
        for i, entry in enumerate(timeline_data['timeline']):
            if entry.get('date') == new_timeline_entry['date']:
                # Merge events
                existing_events = entry.get('events', [])
                if 'EVENT_FNB_001' not in existing_events:
                    existing_events.append('EVENT_FNB_001')
                    entry['events'] = existing_events
                    entry['event_count'] = len(existing_events)
                timeline_data['timeline'][i] = entry
                break
    
    save_json(TIMELINE_PATH, timeline_data)

def update_peter_entity():
    """Update Peter Faucitt entity with new evidence reference."""
    
    entities_data = load_json(ENTITIES_PATH)
    
    for person in entities_data.get('entities', {}).get('persons', []):
        if person.get('entity_id') == 'PERSON_001':
            # Add new evidence
            if 'evidence' not in person:
                person['evidence'] = []
            
            new_evidence = "PAF_FNB_FRAUD_LETTER_2025_06_17 - Director's letter acknowledging suspected fraud"
            if new_evidence not in person['evidence']:
                person['evidence'].append(new_evidence)
            
            # Add timeline event
            if 'timeline_events' not in person:
                person['timeline_events'] = []
            if 'EVENT_FNB_001' not in person['timeline_events']:
                person['timeline_events'].append('EVENT_FNB_001')
            
            # Update evidence strength
            person['evidence_enhanced'] = datetime.now().isoformat()
            person['fnb_fraud_letter_admission'] = {
                "date": "2025-06-17",
                "key_admissions": [
                    "Suspected fraud on RWD account",
                    "Prior request to cancel 3 debit cards",
                    "FNB could be accessory after the fact",
                    "Potential Exchange Control violations"
                ],
                "contradicts_court_position": True
            }
            
            print("Updated PERSON_001 (Peter Faucitt) with FNB Fraud Letter evidence")
            break
    
    entities_data['metadata']['last_updated'] = datetime.now().isoformat()
    entities_data['metadata']['version'] = "29.0_FNB_FRAUD_LETTER_2026_01_29"
    entities_data['metadata']['changes'] = "Added FNB Fraud Letter evidence to PERSON_001"
    
    save_json(ENTITIES_PATH, entities_data)

def add_fnb_relation():
    """Add relation between Peter and FNB regarding fraud letter."""
    
    relations_data = load_json(RELATIONS_PATH)
    
    new_relation = {
        "relation_id": "REL_FNB_001",
        "source_entity": "PERSON_001",
        "target_entity": "BANK_001",
        "relation_type": "fraud_acknowledgment_communication",
        "description": "Peter Faucitt wrote formal letter to FNB acknowledging suspected fraud on RWD account 62323196362",
        "date": "2025-06-17",
        "evidence": [
            "PAF_FNB_FRAUD_LETTER_2025_06_17.jpg",
            "PAF_FNB_FRAUD_LETTER_2025_06_17_OCR.md"
        ],
        "legal_significance": "Director's written admission of suspected fraud",
        "created": datetime.now().isoformat()
    }
    
    # Handle nested relations structure
    relations = relations_data.get('relations', {})
    
    # Check if it's a dict (nested) or list (flat)
    if isinstance(relations, dict):
        # Add to a new category or existing one
        if 'fraud_acknowledgment_relations' not in relations:
            relations['fraud_acknowledgment_relations'] = []
        
        existing_ids = [r.get('relation_id') for r in relations.get('fraud_acknowledgment_relations', [])]
        if new_relation['relation_id'] not in existing_ids:
            relations['fraud_acknowledgment_relations'].append(new_relation)
            relations_data['relations'] = relations
            relations_data['metadata']['last_updated'] = datetime.now().isoformat()
            relations_data['metadata']['version'] = "24.0_FNB_FRAUD_LETTER_2026_01_29"
            relations_data['metadata']['changes'] = "Added REL_FNB_001: Peter-FNB fraud acknowledgment relation"
            print(f"Added relation: {new_relation['relation_id']}")
        else:
            print(f"Relation {new_relation['relation_id']} already exists")
    else:
        # Flat list structure
        existing_ids = [r.get('relation_id') for r in relations]
        if new_relation['relation_id'] not in existing_ids:
            relations.append(new_relation)
            relations_data['relations'] = relations
            relations_data['metadata']['last_updated'] = datetime.now().isoformat()
            relations_data['metadata']['version'] = "24.0_FNB_FRAUD_LETTER_2026_01_29"
            relations_data['metadata']['changes'] = "Added REL_FNB_001: Peter-FNB fraud acknowledgment relation"
            print(f"Added relation: {new_relation['relation_id']}")
        else:
            print(f"Relation {new_relation['relation_id']} already exists")
    
    save_json(RELATIONS_PATH, relations_data)

def main():
    """Main function to add FNB Fraud Letter evidence to all models."""
    print("=" * 60)
    print("Adding FNB Fraud Letter Evidence (2025-06-17)")
    print("=" * 60)
    
    # Add event
    print("\n1. Adding Event...")
    add_fnb_fraud_letter_event()
    
    # Add timeline entry
    print("\n2. Adding Timeline Entry...")
    add_timeline_entry()
    
    # Update Peter entity
    print("\n3. Updating Peter Faucitt Entity...")
    update_peter_entity()
    
    # Add relation
    print("\n4. Adding FNB Relation...")
    add_fnb_relation()
    
    print("\n" + "=" * 60)
    print("FNB Fraud Letter Evidence Integration Complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
