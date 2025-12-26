#!/usr/bin/env python3
"""
Implement Improvements Script for Revenue Stream Hijacking Case
Date: 2025-12-09
Purpose: Apply all identified improvements to entities, relations, events, and timelines
"""

import json
import os
from datetime import datetime
from pathlib import Path
from copy import deepcopy

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = BASE_DIR / "data_models"
ENTITIES_DIR = DATA_MODELS_DIR / "entities"
RELATIONS_DIR = DATA_MODELS_DIR / "relations"
EVENTS_DIR = DATA_MODELS_DIR / "events"
TIMELINES_DIR = DATA_MODELS_DIR / "timelines"

# Latest files
ENTITIES_FILE = ENTITIES_DIR / "entities_refined_2025_12_09_v28.json"
RELATIONS_FILE = RELATIONS_DIR / "relations_refined_2025_12_07_v22.json"
EVENTS_FILE = EVENTS_DIR / "events_refined_2025_12_09_v32.json"
TIMELINE_FILE = TIMELINES_DIR / "timeline_refined_2025_12_09_v21.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_entities(entities_data):
    """Update entities with new evidence"""
    print("Updating entities...")
    
    # Find PERSON_001 (Peter) and update with SF9 evidence
    for person in entities_data["entities"]["persons"]:
        if person["entity_id"] == "PERSON_001":
            print("  - Updating PERSON_001 (Peter) with SF9 evidence...")
            person["financial_impact"]["total_debt_to_daniel"] = "R63,000,000+"
            person["financial_impact"]["sf9_quantum"] = {
                "rwd_revenue_outstanding": "R60,251,961.60",
                "platform_fees_outstanding": "$150,000 USD",
                "total_approximate": "R63,000,000",
                "source": "Emma Wallis (RegimA Zone UK)",
                "period": "July 2023 - October 2025 (27 months)",
                "evidence": "SF9 - Attorney Letter 23 October 2025"
            }
            if "evidence_support" not in person:
                person["evidence_support"] = {"evidence_refs": [], "annexure_support": []}
            person["evidence_support"]["evidence_refs"].append("SF9 - Attorney Letter demanding R63M payment")
            person["evidence_support"]["annexure_support"].append("SF9")
            person["evidence_strength"] = "strong"
        
        # Find PERSON_005 (Daniel) and update with SF9 evidence
        elif person["entity_id"] == "PERSON_005":
            print("  - Updating PERSON_005 (Daniel) with SF9 evidence...")
            person["financial_impact"]["victim_of_theft"] = "R63,000,000+"
            person["financial_impact"]["sf9_quantum"] = {
                "rwd_revenue_outstanding": "R60,251,961.60",
                "platform_fees_outstanding": "$150,000 USD",
                "total_approximate": "R63,000,000",
                "source": "Emma Wallis (RegimA Zone UK)",
                "period": "July 2023 - October 2025 (27 months)",
                "evidence": "SF9 - Attorney Letter 23 October 2025"
            }
            if "evidence_support" not in person:
                person["evidence_support"] = {"evidence_refs": [], "annexure_support": []}
            person["evidence_support"]["evidence_refs"].append("SF9 - Attorney Letter establishing R63M quantum")
            person["evidence_support"]["annexure_support"].append("SF9")
        
        # Find PERSON_002 (Rynette) - already has SF2A/SF2B in v28, verify
        elif person["entity_id"] == "PERSON_002":
            print("  - Verifying PERSON_002 (Rynette) SF2A/SF2B evidence...")
            # SF2A and SF2B already added in v28, ensure complete
            if "criminal_liability" in person:
                if "identity_impersonation" in person["criminal_liability"]:
                    print("    ✓ SF2A evidence already present")
                if "obstruction_of_access" in person["criminal_liability"]:
                    print("    ✓ SF2B evidence already present")
        
        # Find PERSON_007 (Bantjies) - already has SF1A in v28, verify
        elif person["entity_id"] == "PERSON_007":
            print("  - Verifying PERSON_007 (Bantjies) SF1A evidence...")
            if "financial_details" in person and "call_option_schedule" in person["financial_details"]:
                print("    ✓ SF1A evidence already present")
    
    # Update metadata
    entities_data["metadata"]["version"] = "29.0"
    entities_data["metadata"]["last_updated"] = datetime.now().isoformat()
    entities_data["metadata"]["changes"] = "Added SF9 R63M quantum to PERSON_001 and PERSON_005"
    
    return entities_data

def update_relations(relations_data):
    """Update relations with new evidence"""
    print("\nUpdating relations...")
    
    # Add relation for Rynette's control of Sage subscription
    print("  - Adding REL_CTRL_011: Rynette controls Sage subscription...")
    new_control_relation = {
        "relation_id": "REL_CTRL_011",
        "relation_type": "controls",
        "source_entity": "PERSON_002",
        "target_entity": "SAGE_SUBSCRIPTION",
        "control_type": "subscription_ownership",
        "legal_status": "obstruction_of_access",
        "evidence": [
            "SF2B - Sage Subscription Expiry notice showing Rynette as owner",
            "Account expired 23 July 2025, remained expired through 25 August 2025"
        ],
        "significance": "Rynette controls account activation, only she can restore access",
        "impact": "All parties denied access to financial records for over 1 month",
        "criminal_liability": "obstruction_of_access",
        "ad_res_j7_references": [
            "SF2B in ANNEXURES",
            "Cross-referenced in COMPREHENSIVE_EVIDENCE_INDEX.md"
        ]
    }
    relations_data["relations"]["control_relations"].append(new_control_relation)
    
    # Add relation for Rynette's dual account access (impersonation)
    print("  - Adding REL_ACCESS_001: Rynette impersonates Peter via email...")
    new_access_relation = {
        "relation_id": "REL_ACCESS_001",
        "relation_type": "impersonates",
        "source_entity": "PERSON_002",
        "target_entity": "PERSON_001",
        "access_type": "dual_account_email_impersonation",
        "legal_status": "identity_fraud",
        "evidence": [
            "SF2A - Sage User Access screenshot showing Pete@regima.com account",
            "Rynette has two accounts: Pete@regima.com AND rynette@regima.zone"
        ],
        "significance": "Rynette can act as Peter in accounting system without his knowledge",
        "criminal_liability": "identity_impersonation",
        "ad_res_j7_references": [
            "SF2A in ANNEXURES",
            "Cross-referenced in COMPREHENSIVE_EVIDENCE_INDEX.md"
        ]
    }
    
    # Add new relation type if it doesn't exist
    if "access_relations" not in relations_data["relations"]:
        relations_data["relations"]["access_relations"] = []
    relations_data["relations"]["access_relations"].append(new_access_relation)
    
    # Update metadata
    relations_data["metadata"]["version"] = "23.0"
    relations_data["metadata"]["last_updated"] = datetime.now().isoformat()
    relations_data["metadata"]["changes"] = "Added SF2A/SF2B relations for Rynette's control and impersonation"
    
    return relations_data

def update_events(events_data):
    """Update events with new evidence"""
    print("\nUpdating events...")
    
    # Verify EVENT_078 and EVENT_079 exist (they should from v32)
    event_078_exists = any(e["event_id"] == "EVENT_078" for e in events_data["events"])
    event_079_exists = any(e["event_id"] == "EVENT_079" for e in events_data["events"])
    
    if event_078_exists:
        print("  ✓ EVENT_078 (Sage expiry) already exists")
        # Update with evidence
        for event in events_data["events"]:
            if event["event_id"] == "EVENT_078":
                event["evidence"] = [
                    "SF2B - Sage Subscription Expiry notice",
                    "Account expired 23 July 2025",
                    "Screenshot taken 25 August 2025 (over 1 month later)"
                ]
                event["evidence_support"] = {
                    "evidence": ["SF2B - Sage Subscription Expiry"],
                    "significance": "Direct evidence of obstruction of access"
                }
    else:
        print("  - Adding EVENT_078: Sage Account Expiry...")
        new_event_078 = {
            "event_id": "EVENT_078",
            "date": "2025-07-23",
            "title": "Sage Accounting System Subscription Expired",
            "category": "obstruction_of_access",
            "event_type": "system_access_denial",
            "perpetrators": ["PERSON_002"],
            "victims": ["PERSON_004", "PERSON_005"],
            "entities_involved": ["ORG_001"],
            "description": "Sage accounting subscription expired on 23 July 2025. Rynette Farrar identified as subscription owner with sole control over reactivation. Account remained expired through at least 25 August 2025 (over 1 month), denying all parties access to financial records.",
            "financial_impact": "obstruction_of_financial_records_access",
            "legal_significance": "section_163_oppression_unfairly_prejudicial_conduct",
            "evidence": [
                "SF2B - Sage Subscription Expiry notice",
                "Account expired 23 July 2025",
                "Screenshot taken 25 August 2025 (over 1 month later)"
            ],
            "evidence_support": {
                "evidence": ["SF2B - Sage Subscription Expiry"],
                "significance": "Direct evidence of obstruction of access"
            },
            "pattern": "obstruction_phase",
            "actors": ["PERSON_002", "PERSON_004", "PERSON_005", "ORG_001"]
        }
        events_data["events"].append(new_event_078)
    
    if event_079_exists:
        print("  ✓ EVENT_079 (Rynette dual account) already exists")
        # Update with evidence
        for event in events_data["events"]:
            if event["event_id"] == "EVENT_079":
                event["evidence"] = [
                    "SF2A - Sage User Access screenshot",
                    "Pete@regima.com account controlled by Rynette",
                    "Dual accounts: Pete@regima.com AND rynette@regima.zone"
                ]
                event["evidence_support"] = {
                    "evidence": ["SF2A - Sage User Access"],
                    "significance": "Direct evidence of identity impersonation capability"
                }
    else:
        print("  - Adding EVENT_079: Rynette Dual Account Discovery...")
        new_event_079 = {
            "event_id": "EVENT_079",
            "date": "2025-06-20",
            "title": "Rynette Farrar Dual Account Access - Peter Email Impersonation",
            "category": "identity_fraud",
            "event_type": "identity_impersonation",
            "perpetrators": ["PERSON_002"],
            "victims": ["PERSON_001"],
            "entities_involved": ["ORG_001"],
            "description": "Discovery that Rynette Farrar has dual account access in Sage system: Pete@regima.com AND rynette@regima.zone. This enables her to impersonate Peter in the accounting system and act without his knowledge or authorization.",
            "financial_impact": "identity_fraud_capability",
            "legal_significance": "criminal_identity_impersonation",
            "evidence": [
                "SF2A - Sage User Access screenshot",
                "Pete@regima.com account controlled by Rynette",
                "Dual accounts: Pete@regima.com AND rynette@regima.zone"
            ],
            "evidence_support": {
                "evidence": ["SF2A - Sage User Access"],
                "significance": "Direct evidence of identity impersonation capability"
            },
            "pattern": "fraud_execution_phase",
            "actors": ["PERSON_002", "PERSON_001", "ORG_001"]
        }
        events_data["events"].append(new_event_079)
    
    # Add EVENT_080: SF9 Attorney Letter Demand
    print("  - Adding EVENT_080: R63M Formal Demand by Ian Levitt Attorneys...")
    new_event_080 = {
        "event_id": "EVENT_080",
        "date": "2025-10-23",
        "title": "R63M Formal Demand by Ian Levitt Attorneys",
        "category": "legal_action",
        "event_type": "attorney_demand",
        "perpetrators": [],
        "victims": ["PERSON_001"],
        "entities_involved": ["ORG_001", "ORG_003"],
        "description": "Ian Levitt Attorneys (representing Jacqui Faucitt) sent formal demand letter to Elliot Attorneys Inc (representing Peter Faucitt) demanding payment of R60,251,961.60 revenue outstanding from RegimA Worldwide Distribution plus $150,000 platform fees, totaling approximately R63M. Source: Emma Wallis (RegimA Zone UK). Period: July 2023 - October 2025 (27 months). 48-hour deadline given, demand ignored.",
        "financial_impact": "R63,000,000",
        "legal_significance": "attorney_documented_quantum_for_all_claims",
        "evidence": [
            "SF9 - Attorney Letter 23 October 2025",
            "Emma Wallis source documentation",
            "27-month revenue period"
        ],
        "evidence_support": {
            "evidence": ["SF9 - Attorney Letter"],
            "significance": "Establishes formal quantum for revenue hijacking claims"
        },
        "pattern": "legal_escalation_phase",
        "actors": ["PERSON_001", "PERSON_004", "ORG_001", "ORG_003"]
    }
    events_data["events"].append(new_event_080)
    
    # Update metadata
    events_data["metadata"]["version"] = "33.0"
    events_data["metadata"]["last_updated"] = datetime.now().isoformat()
    events_data["metadata"]["total_events"] = len(events_data["events"])
    events_data["metadata"]["changes"] = "Added/updated EVENT_078, EVENT_079, EVENT_080 with SF2A, SF2B, SF9 evidence"
    
    return events_data

def update_timeline(timeline_data):
    """Update timeline with new entries"""
    print("\nUpdating timeline...")
    
    # Check if timeline has entries
    if "timeline" not in timeline_data or not timeline_data["timeline"]:
        print("  ! Timeline is empty, initializing...")
        timeline_data["timeline"] = []
    
    # Add timeline entry for EVENT_079 (Rynette dual account)
    print("  - Adding timeline entry for Rynette dual account discovery...")
    timeline_079 = {
        "date": "2025-06-20",
        "event_id": "EVENT_079",
        "title": "Rynette Dual Account Access Discovered",
        "description": "Discovery of Rynette's dual account access in Sage (Pete@regima.com AND rynette@regima.zone)",
        "category": "identity_fraud",
        "significance": "criminal",
        "evidence": ["SF2A"]
    }
    timeline_data["timeline"].append(timeline_079)
    
    # Add timeline entry for EVENT_078 (Sage expiry)
    print("  - Adding timeline entry for Sage subscription expiry...")
    timeline_078 = {
        "date": "2025-07-23",
        "event_id": "EVENT_078",
        "title": "Sage Subscription Expired - Access Obstruction",
        "description": "Sage accounting subscription expired, Rynette controls reactivation, all parties denied access for over 1 month",
        "category": "obstruction_of_access",
        "significance": "section_163_oppression",
        "evidence": ["SF2B"]
    }
    timeline_data["timeline"].append(timeline_078)
    
    # Add timeline entry for EVENT_080 (SF9 attorney letter)
    print("  - Adding timeline entry for R63M attorney demand...")
    timeline_080 = {
        "date": "2025-10-23",
        "event_id": "EVENT_080",
        "title": "R63M Formal Demand by Ian Levitt Attorneys",
        "description": "Attorney letter demanding R60.25M revenue + $150K platform fees, total ~R63M, 48-hour deadline (ignored)",
        "category": "legal_action",
        "significance": "quantum_establishment",
        "evidence": ["SF9"]
    }
    timeline_data["timeline"].append(timeline_080)
    
    # Sort timeline by date
    timeline_data["timeline"].sort(key=lambda x: x["date"])
    
    # Update metadata
    timeline_data["metadata"]["version"] = "22.0"
    timeline_data["metadata"]["last_updated"] = datetime.now().isoformat()
    timeline_data["metadata"]["total_entries"] = len(timeline_data["timeline"])
    timeline_data["metadata"]["changes"] = "Added timeline entries for EVENT_078, EVENT_079, EVENT_080"
    
    return timeline_data

def main():
    """Main execution function"""
    print("="*80)
    print("IMPLEMENTING IMPROVEMENTS - Revenue Stream Hijacking Case 2025-137857")
    print("="*80)
    
    # Load data
    print("\nLoading data models...")
    entities = load_json(ENTITIES_FILE)
    relations = load_json(RELATIONS_FILE)
    events = load_json(EVENTS_FILE)
    timeline = load_json(TIMELINE_FILE)
    
    # Update each model
    entities = update_entities(entities)
    relations = update_relations(relations)
    events = update_events(events)
    timeline = update_timeline(timeline)
    
    # Save updated models
    print("\nSaving updated models...")
    new_entities_file = ENTITIES_DIR / "entities_refined_2025_12_09_v29.json"
    new_relations_file = RELATIONS_DIR / "relations_refined_2025_12_09_v23.json"
    new_events_file = EVENTS_DIR / "events_refined_2025_12_09_v33.json"
    new_timeline_file = TIMELINES_DIR / "timeline_refined_2025_12_09_v22.json"
    
    save_json(entities, new_entities_file)
    save_json(relations, new_relations_file)
    save_json(events, new_events_file)
    save_json(timeline, new_timeline_file)
    
    print(f"  ✓ Entities saved: {new_entities_file}")
    print(f"  ✓ Relations saved: {new_relations_file}")
    print(f"  ✓ Events saved: {new_events_file}")
    print(f"  ✓ Timeline saved: {new_timeline_file}")
    
    print("\n" + "="*80)
    print("IMPROVEMENTS IMPLEMENTED SUCCESSFULLY")
    print("="*80)
    print(f"\nNew versions:")
    print(f"  - Entities: v29 (added SF9 R63M quantum)")
    print(f"  - Relations: v23 (added SF2A/SF2B relations)")
    print(f"  - Events: v33 (added/updated EVENT_078, EVENT_079, EVENT_080)")
    print(f"  - Timeline: v22 (added 3 new entries)")
    print("\n" + "="*80)

if __name__ == "__main__":
    main()
