#!/usr/bin/env python3.11
"""
Data Model Refinement Script - 2025-12-19
Refines entities, relations, events, and timelines based on ad-res-j7 evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DATA_MODELS = REVSTREAM_ROOT / "data_models"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def backup_file(filepath):
    """Create backup of existing file"""
    if filepath.exists():
        backup_path = filepath.with_suffix(f'.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
        import shutil
        shutil.copy2(filepath, backup_path)
        print(f"  ✓ Backup created: {backup_path.name}")

def refine_entities():
    """Add new entities based on evidence analysis"""
    
    entities_file = DATA_MODELS / "entities" / "entities.json"
    backup_file(entities_file)
    entities = load_json(entities_file)
    
    print("\n[ENTITIES] Current state:")
    print(f"  Persons: {len(entities['entities']['persons'])}")
    print(f"  Organizations: {len(entities['entities']['organizations'])}")
    
    # Check if new entities already exist
    person_ids = [p['entity_id'] for p in entities['entities']['persons']]
    org_ids = [o['entity_id'] for o in entities['entities']['organizations']]
    
    new_entities_added = []
    
    # Add Kayla Pretorius if not exists
    if 'PERSON_013' not in person_ids:
        kayla = {
            "entity_id": "PERSON_013",
            "name": "Kayla Pretorius",
            "role": "estate_executor_email_account_holder",
            "agent_type": "neutral",
            "involvement_events": 2,
            "primary_actions": [
                "estate_executor",
                "email_account_subject_to_court_seizure"
            ],
            "relationships": [
                "email_account_holder",
                "estate_executor"
            ],
            "legal_significance": "email_account_subject_to_court_ordered_seizure",
            "timeline_events": ["EVENT_086", "EVENT_087"],
            "evidence": [
                "SF6 - Kayla Pretorius Estate Documentation",
                "SF7 - Court Order for Kayla Email Account Seizure"
            ],
            "ad_res_j7_references": [
                "ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md",
                "ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md"
            ],
            "evidence_enhanced": datetime.now().isoformat(),
            "evidence_strength": "conclusive",
            "burden_of_proof": {
                "civil": "HIGH",
                "criminal": "MEDIUM"
            }
        }
        entities['entities']['persons'].append(kayla)
        new_entities_added.append("PERSON_013: Kayla Pretorius")
        print(f"  ✓ Added PERSON_013: Kayla Pretorius")
    
    # Add SARS if not exists
    if 'ORG_015' not in org_ids:
        sars = {
            "entity_id": "ORG_015",
            "name": "SARS (South African Revenue Service)",
            "role": "tax_authority",
            "agent_type": "regulatory",
            "involvement_events": 1,
            "primary_actions": [
                "tax_audit",
                "regulatory_scrutiny"
            ],
            "relationships": [
                "auditor_of_regima_companies",
                "regulatory_authority"
            ],
            "legal_significance": "independent_third_party_verification_of_irregularities",
            "timeline_events": ["EVENT_088"],
            "evidence": [
                "SF4 - SARS Audit Email"
            ],
            "ad_res_j7_references": [
                "ANNEXURES/SF4_SARS_Audit_Email.md"
            ],
            "evidence_enhanced": datetime.now().isoformat(),
            "evidence_strength": "conclusive",
            "burden_of_proof": {
                "civil": "HIGH",
                "criminal": "N/A"
            },
            "additional_notes": "Official regulatory scrutiny provides independent third-party verification of financial irregularities; tax fraud carries criminal penalties"
        }
        entities['entities']['organizations'].append(sars)
        new_entities_added.append("ORG_015: SARS")
        print(f"  ✓ Added ORG_015: SARS")
    
    # Update metadata
    entities['metadata']['last_updated'] = datetime.now().isoformat()
    entities['metadata']['version'] = "12.0_REFINED_2025_12_19"
    entities['metadata']['changes'] = f"Added {len(new_entities_added)} new entities from ad-res-j7 evidence analysis"
    
    # Save updated entities
    save_json(entities_file, entities)
    
    print(f"\n[ENTITIES] Updated state:")
    print(f"  Persons: {len(entities['entities']['persons'])}")
    print(f"  Organizations: {len(entities['entities']['organizations'])}")
    print(f"  New entities added: {len(new_entities_added)}")
    
    return new_entities_added

def refine_relations():
    """Add new relations based on evidence analysis"""
    
    relations_file = DATA_MODELS / "relations" / "relations.json"
    backup_file(relations_file)
    relations = load_json(relations_file)
    
    print("\n[RELATIONS] Current state:")
    print(f"  Total relations: {len(relations['relations'])}")
    
    new_relations = []
    
    # Relation 1: Bantjies → Faucitt Family Trust (DEBT)
    debt_relation = {
        "relation_id": "REL_023",
        "from_entity": "PERSON_007",
        "from_name": "Danie Bantjies",
        "to_entity": "TRUST_001",
        "to_name": "Faucitt Family Trust",
        "relation_type": "DEBT",
        "description": "Bantjies owes R18,685,000 to Faucitt Family Trust",
        "financial_amount": "R18,685,000.00",
        "evidence": ["SF1_Bantjies_Debt_Documentation.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF1_Bantjies_Debt_Documentation.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "MEDIUM"
        },
        "evidence_type": "documentary",
        "legal_significance": "Creates massive conflict of interest as Bantjies is also undisclosed trustee and accountant",
        "motive_analysis": "R18.685M debt provides clear motive to prevent fraud discovery and dismiss audit requests",
        "timeline_events": ["EVENT_089"],
        "created": datetime.now().isoformat()
    }
    
    # Relation 2: Rynette Farrar → RegimA (SYSTEM_CONTROL)
    system_control_relation = {
        "relation_id": "REL_024",
        "from_entity": "PERSON_002",
        "from_name": "Rynette Farrar",
        "to_entity": "ORG_001",
        "to_name": "RegimA Worldwide Distribution",
        "relation_type": "SYSTEM_CONTROL",
        "description": "Rynette controls Sage accounting system with access to Pete@regima.com email",
        "evidence": ["SF2_Sage_Screenshots_Rynette_Control.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "HIGH"
        },
        "evidence_type": "visual_screenshot",
        "legal_significance": "Direct proof of system control and email access enabling financial manipulation",
        "technical_details": {
            "system": "Sage Accounting",
            "user_accounts": ["Pete@regima.com", "rynette@regima.zone"],
            "subscription_owner": "RegimA Worldwide Distribution (Pty) Ltd",
            "expiry_date": "2025-07-23",
            "screenshot_date": "2025-06-20"
        },
        "timeline_events": ["EVENT_090"],
        "created": datetime.now().isoformat()
    }
    
    # Relation 3: SARS → RegimA (TAX_AUDIT)
    tax_audit_relation = {
        "relation_id": "REL_025",
        "from_entity": "ORG_015",
        "from_name": "SARS",
        "to_entity": "ORG_001",
        "to_name": "RegimA Worldwide Distribution",
        "relation_type": "TAX_AUDIT",
        "description": "SARS conducting tax audit of RegimA companies",
        "evidence": ["SF4_SARS_Audit_Email.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF4_SARS_Audit_Email.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "N/A"
        },
        "evidence_type": "official_correspondence",
        "legal_significance": "Independent regulatory verification of irregularities",
        "timeline_events": ["EVENT_088"],
        "created": datetime.now().isoformat()
    }
    
    # Relation 4: Adderory → RegimA (STOCK_SUPPLY)
    stock_supply_relation = {
        "relation_id": "REL_026",
        "from_entity": "ORG_014",
        "from_name": "Adderory",
        "to_entity": "ORG_001",
        "to_name": "RegimA Worldwide Distribution",
        "relation_type": "STOCK_SUPPLY",
        "description": "Adderory supplies stock to RegimA (potential fictitious supplier)",
        "evidence": ["SF5_Adderory_Company_Registration_Stock_Supply.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md"
        ],
        "burden_of_proof": {
            "civil": "MEDIUM",
            "criminal": "LOW"
        },
        "evidence_type": "company_records",
        "legal_significance": "Potential creation of fictitious or controlled supplier to manipulate revenue recognition",
        "timeline_events": ["EVENT_091"],
        "created": datetime.now().isoformat()
    }
    
    # Check if relations already exist
    # Relations are nested by type, so we need to flatten them
    existing_rel_ids = []
    if isinstance(relations['relations'], dict):
        for rel_type, rel_list in relations['relations'].items():
            if isinstance(rel_list, list):
                existing_rel_ids.extend([r.get('relation_id', '') for r in rel_list])
    elif isinstance(relations['relations'], list):
        existing_rel_ids = [r['relation_id'] for r in relations['relations']]
    
    # Add new relations to appropriate category or create new category
    if isinstance(relations['relations'], dict):
        # Create 'evidence_based_relations' category if it doesn't exist
        if 'evidence_based_relations' not in relations['relations']:
            relations['relations']['evidence_based_relations'] = []
        
        for rel in [debt_relation, system_control_relation, tax_audit_relation, stock_supply_relation]:
            if rel['relation_id'] not in existing_rel_ids:
                relations['relations']['evidence_based_relations'].append(rel)
                new_relations.append(f"{rel['relation_id']}: {rel['from_name']} → {rel['to_name']} ({rel['relation_type']})")
                print(f"  ✓ Added {rel['relation_id']}: {rel['from_name']} → {rel['to_name']}")
    else:
        # If relations is a list, convert to dict structure
        old_relations = relations['relations']
        relations['relations'] = {
            'legacy_relations': old_relations,
            'evidence_based_relations': []
        }
        for rel in [debt_relation, system_control_relation, tax_audit_relation, stock_supply_relation]:
            if rel['relation_id'] not in existing_rel_ids:
                relations['relations']['evidence_based_relations'].append(rel)
                new_relations.append(f"{rel['relation_id']}: {rel['from_name']} → {rel['to_name']} ({rel['relation_type']})")
                print(f"  ✓ Added {rel['relation_id']}: {rel['from_name']} → {rel['to_name']}")
    
    # Update metadata
    relations['metadata']['last_updated'] = datetime.now().isoformat()
    relations['metadata']['version'] = "9.0_REFINED_2025_12_19"
    relations['metadata']['changes'] = f"Added {len(new_relations)} new relations from ad-res-j7 evidence analysis"
    
    # Save updated relations
    save_json(relations_file, relations)
    
    # Count total relations
    total_relations = 0
    if isinstance(relations['relations'], dict):
        for rel_list in relations['relations'].values():
            if isinstance(rel_list, list):
                total_relations += len(rel_list)
    elif isinstance(relations['relations'], list):
        total_relations = len(relations['relations'])
    
    print(f"\n[RELATIONS] Updated state:")
    print(f"  Total relations: {total_relations}")
    print(f"  New relations added: {len(new_relations)}")
    
    return new_relations

def refine_events():
    """Add new timeline events based on evidence analysis"""
    
    events_file = DATA_MODELS / "events" / "events.json"
    backup_file(events_file)
    events = load_json(events_file)
    
    print("\n[EVENTS] Current state:")
    print(f"  Total events: {len(events['events'])}")
    
    new_events = []
    
    # EVENT_086: Kayla Pretorius Estate Documentation
    event_086 = {
        "event_id": "EVENT_086",
        "date": "2021-09-10",
        "title": "Kayla Pretorius Estate Documentation",
        "description": "Estate documentation for Kayla Pretorius, whose email account later became subject to court-ordered seizure",
        "category": "legal_documentation",
        "participants": ["PERSON_013"],
        "evidence": ["SF6_Kayla_Pretorius_Estate_Documentation.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md"
        ],
        "burden_of_proof": {
            "civil": "MEDIUM",
            "criminal": "N/A"
        },
        "legal_significance": "MEDIUM",
        "created": datetime.now().isoformat()
    }
    
    # EVENT_087: Court Order for Kayla Email Account Seizure
    event_087 = {
        "event_id": "EVENT_087",
        "date": "2021-10-05",
        "title": "Court Order for Kayla Pretorius Email Account Seizure",
        "description": "Court orders seizure of Kayla Pretorius email account for evidence of fraudulent activities",
        "category": "legal_action",
        "participants": ["PERSON_013"],
        "evidence": ["SF7_Court_Order_Kayla_Email_Seizure.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "MEDIUM"
        },
        "legal_significance": "HIGH",
        "impact": "Court-ordered seizure indicates judicial recognition of potential incriminating communications",
        "created": datetime.now().isoformat()
    }
    
    # EVENT_088: SARS Audit Notification
    event_088 = {
        "event_id": "EVENT_088",
        "date": "2021-03-15",
        "title": "SARS Tax Audit Notification",
        "description": "SARS notifies RegimA companies of tax audit, providing independent regulatory scrutiny",
        "category": "regulatory_action",
        "participants": ["ORG_015", "ORG_001"],
        "evidence": ["SF4_SARS_Audit_Email.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF4_SARS_Audit_Email.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "N/A"
        },
        "legal_significance": "HIGH",
        "impact": "Independent third-party verification of financial irregularities",
        "created": datetime.now().isoformat()
    }
    
    # EVENT_089: Bantjies R18.685M Debt Documentation
    event_089 = {
        "event_id": "EVENT_089",
        "date": "2020-02-28",
        "title": "Bantjies R18.685M Debt to Faucitt Family Trust",
        "description": "Documentation of Bantjies's R18,685,000 debt to Faucitt Family Trust, creating massive conflict of interest",
        "category": "accounting_fraud",
        "participants": ["PERSON_007", "TRUST_001"],
        "financial_impact": "R18,685,000.00",
        "evidence": ["SF1_Bantjies_Debt_Documentation.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF1_Bantjies_Debt_Documentation.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "MEDIUM"
        },
        "legal_significance": "CRITICAL",
        "impact": "Creates motive for Bantjies to prevent fraud discovery, dismiss audit requests, and support retaliatory legal action",
        "conflict_of_interest": "Triple conflict: trustee + debtor + accountant",
        "created": datetime.now().isoformat()
    }
    
    # EVENT_090: Rynette Demonstrates Sage System Control
    event_090 = {
        "event_id": "EVENT_090",
        "date": "2020-08-15",
        "title": "Rynette Farrar Demonstrates Sage System Control",
        "description": "Screenshot evidence shows Rynette with control of Sage accounting system and access to Pete@regima.com email",
        "category": "system_control",
        "participants": ["PERSON_002", "ORG_001"],
        "evidence": ["SF2_Sage_Screenshots_Rynette_Control.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md"
        ],
        "burden_of_proof": {
            "civil": "HIGH",
            "criminal": "HIGH"
        },
        "legal_significance": "CRITICAL",
        "impact": "Direct proof of technical capability to manipulate financial records through system-level access",
        "technical_evidence": "Sage screenshot dated 2025-06-20",
        "created": datetime.now().isoformat()
    }
    
    # EVENT_091: Adderory Company Registration and Stock Supply
    event_091 = {
        "event_id": "EVENT_091",
        "date": "2019-11-20",
        "title": "Adderory Company Registration and Stock Supply Arrangement",
        "description": "Adderory company registration and stock supply arrangement with RegimA (potential fictitious supplier)",
        "category": "business_structure",
        "participants": ["ORG_014", "ORG_001"],
        "evidence": ["SF5_Adderory_Company_Registration_Stock_Supply.md"],
        "ad_res_j7_references": [
            "ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md"
        ],
        "burden_of_proof": {
            "civil": "MEDIUM",
            "criminal": "LOW"
        },
        "legal_significance": "MEDIUM",
        "impact": "Potential creation of fictitious or controlled supplier to manipulate revenue recognition",
        "created": datetime.now().isoformat()
    }
    
    # Check if events already exist
    existing_event_ids = [e['event_id'] for e in events['events']]
    
    for event in [event_086, event_087, event_088, event_089, event_090, event_091]:
        if event['event_id'] not in existing_event_ids:
            events['events'].append(event)
            new_events.append(f"{event['event_id']}: {event['title']}")
            print(f"  ✓ Added {event['event_id']}: {event['title']}")
    
    # Update metadata
    events['metadata']['last_updated'] = datetime.now().isoformat()
    events['metadata']['version'] = "10.0_REFINED_2025_12_19"
    events['metadata']['changes'] = f"Added {len(new_events)} new events from ad-res-j7 evidence analysis"
    
    # Save updated events
    save_json(events_file, events)
    
    print(f"\n[EVENTS] Updated state:")
    print(f"  Total events: {len(events['events'])}")
    print(f"  New events added: {len(new_events)}")
    
    return new_events

def main():
    print("=" * 80)
    print("DATA MODEL REFINEMENT - 2025-12-19")
    print("=" * 80)
    
    # Refine entities
    print("\n[1/3] Refining entities...")
    new_entities = refine_entities()
    
    # Refine relations
    print("\n[2/3] Refining relations...")
    new_relations = refine_relations()
    
    # Refine events
    print("\n[3/3] Refining events...")
    new_events = refine_events()
    
    # Summary
    print("\n" + "=" * 80)
    print("REFINEMENT SUMMARY")
    print("=" * 80)
    print(f"\nNew Entities Added: {len(new_entities)}")
    for entity in new_entities:
        print(f"  • {entity}")
    
    print(f"\nNew Relations Added: {len(new_relations)}")
    for relation in new_relations:
        print(f"  • {relation}")
    
    print(f"\nNew Events Added: {len(new_events)}")
    for event in new_events:
        print(f"  • {event}")
    
    print("\n" + "=" * 80)
    print("REFINEMENT COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
