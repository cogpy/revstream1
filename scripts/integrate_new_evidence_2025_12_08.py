#!/usr/bin/env python3
"""
Integrate New Evidence into Data Models
Date: 2025-12-08
Purpose: Update entities, events, and timeline with 4 new evidence files (SF2A, SF2B, SF1A, SF9)
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
ENTITIES_PATH = REVSTREAM_PATH / "data_models" / "entities"
EVENTS_PATH = REVSTREAM_PATH / "data_models" / "events"
TIMELINES_PATH = REVSTREAM_PATH / "data_models" / "timelines"

def load_json_file(filepath):
    """Load JSON file with error handling"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def save_json_file(data, filepath):
    """Save JSON file with pretty formatting"""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error saving {filepath}: {e}")
        return False

def update_entities_with_new_evidence(entities_data):
    """Update entities with new evidence from SF2A, SF2B, SF1A, SF9"""
    if not entities_data or "entities" not in entities_data:
        return entities_data
    
    # Update PERSON_002 (Rynette Farrar) with SF2A, SF2B
    for entity in entities_data["entities"].get("persons", []):
        if entity.get("entity_id") == "PERSON_002":
            # Add new evidence references
            if "evidence_support" not in entity:
                entity["evidence_support"] = {}
            
            entity["evidence_support"]["evidence_refs"] = entity["evidence_support"].get("evidence_refs", []) + [
                "SF2A - Sage User Access showing Rynette's dual accounts (June 2025)",
                "SF2B - Sage Subscription Expiry showing Rynette as owner (August 2025)"
            ]
            
            entity["evidence_support"]["annexure_support"] = list(set(
                entity["evidence_support"].get("annexure_support", []) + ["SF2A", "SF2B"]
            ))
            
            # Add new primary actions
            entity["primary_actions"] = list(set(entity.get("primary_actions", []) + [
                "subscription_owner_control",
                "dual_account_access",
                "peter_email_impersonation",
                "obstruction_of_accounting_access"
            ]))
            
            # Update criminal liability
            if "criminal_liability" not in entity:
                entity["criminal_liability"] = {}
            
            entity["criminal_liability"]["identity_impersonation"] = {
                "elements": [
                    "using_peter_email_pete@regima.com",
                    "dual_account_access_to_sage_system",
                    "ability_to_act_as_peter_in_accounting"
                ],
                "evidence_available": [
                    "SF2A - Sage user access screenshot showing Pete@regima.com account",
                    "SF2A - Rynette has two accounts: Pete@regima.com and rynette@regima.zone"
                ],
                "evidence_strength": "strong",
                "burden_of_proof_met": "achievable_95_percent"
            }
            
            entity["criminal_liability"]["obstruction_of_access"] = {
                "elements": [
                    "sage_subscription_owner",
                    "controls_account_reactivation",
                    "denied_access_for_over_1_month"
                ],
                "evidence_available": [
                    "SF2B - Sage expiry notice identifying Rynette as subscription owner",
                    "SF2B - Account expired 23 July 2025, screenshot 25 August 2025 (over 1 month)"
                ],
                "evidence_strength": "strong",
                "burden_of_proof_met": "civil_50_percent_exceeded"
            }
            
            entity["evidence_strength"] = "strong"
            print("✓ Updated PERSON_002 (Rynette Farrar) with SF2A, SF2B")
    
    # Update PERSON_007 (Danie Bantjies) with SF1A
    for entity in entities_data["entities"].get("persons", []):
        if entity.get("entity_id") == "PERSON_007":
            # Add new evidence references
            if "evidence_support" not in entity:
                entity["evidence_support"] = {}
            
            entity["evidence_support"]["evidence_refs"] = entity["evidence_support"].get("evidence_refs", []) + [
                "SF1A - Bantjies Call Option Agreement excerpt showing payment schedule"
            ]
            
            entity["evidence_support"]["annexure_support"] = list(set(
                entity["evidence_support"].get("annexure_support", []) + ["SF1A"]
            ))
            
            # Add relationships
            entity["relationships"] = list(set(entity.get("relationships", []) + [
                "option_shareholder",
                "call_option_agreement_party"
            ]))
            
            # Add financial details
            if "financial_details" not in entity:
                entity["financial_details"] = {}
            
            entity["financial_details"]["call_option_schedule"] = {
                "year_1_may_2026": "R18,685,000 (R3,737 per share)",
                "year_2_may_2027": "R23,165,000 (R4,633 per share)",
                "year_3_may_2029": "R28,730,000 (R5,746 per share)",
                "note": "Amounts are NOT cumulative - represent total outstanding at each date",
                "evidence": "SF1A"
            }
            
            print("✓ Updated PERSON_007 (Danie Bantjies) with SF1A")
    
    # Update metadata
    entities_data["metadata"]["last_evidence_integration"] = datetime.now().isoformat()
    entities_data["metadata"]["version"] = "11.0_NEW_EVIDENCE_2025_12_08"
    entities_data["metadata"]["new_evidence_added"] = ["SF2A", "SF2B", "SF1A", "SF9"]
    
    return entities_data

def add_new_events(events_data):
    """Add new events for SF2A, SF2B evidence"""
    if not events_data:
        events_data = {"metadata": {}, "events": []}
    
    if "events" not in events_data:
        events_data["events"] = []
    
    # EVENT_078: Sage Account Expiry
    event_078 = {
        "event_id": "EVENT_078",
        "date": "2025-07-23",
        "title": "Sage Accounting System Subscription Expired",
        "type": "system_access_denial",
        "description": "Sage accounting system subscription for RegimA Worldwide Distribution expired. Rynette Farrar identified as subscription owner with sole control over reactivation.",
        "entities_involved": ["PERSON_002"],
        "organizations_involved": ["ORG_001"],
        "evidence_support": {
            "primary_evidence": "SF2B - Sage expiry notice screenshot (25 August 2025)",
            "evidence_strength": "strong",
            "significance": "Demonstrates obstruction of access to financial records for over 1 month"
        },
        "legal_implications": {
            "oppression_s163": "Unfairly prejudicial conduct - denial of access to accounting system",
            "obstruction": "Preventing access to financial records",
            "fiduciary_breach": "Failing to maintain proper accounting records access"
        },
        "timeline_significance": "Account expired 23 July 2025, still expired 25 August 2025 (over 1 month denial)",
        "related_events": ["EVENT_079"]
    }
    
    # EVENT_079: Rynette Dual Account Access
    event_079 = {
        "event_id": "EVENT_079",
        "date": "2025-06-20",
        "title": "Rynette Farrar Dual Account Access - Peter Email Impersonation",
        "type": "system_control_evidence",
        "description": "Sage user access screenshot reveals Rynette Farrar has two user accounts with access to RegimA Worldwide Distribution: Pete@regima.com (Peter's email) and rynette@regima.zone (her own email).",
        "entities_involved": ["PERSON_002", "PERSON_001"],
        "organizations_involved": ["ORG_001"],
        "evidence_support": {
            "primary_evidence": "SF2A - Sage Control User Access screenshot (20 June 2025)",
            "evidence_strength": "strong",
            "significance": "Proves Rynette has access to Peter's email and can impersonate him in accounting system"
        },
        "legal_implications": {
            "fraud": "Identity impersonation in accounting system",
            "system_manipulation": "Dual account access enables fraudulent transactions",
            "fiduciary_breach": "Unauthorized use of director's credentials"
        },
        "timeline_significance": "Screenshot date 20 June 2025 - one month before account expiry",
        "related_events": ["EVENT_078"]
    }
    
    # Check if events already exist
    existing_event_ids = [e.get("event_id") for e in events_data["events"]]
    
    if "EVENT_078" not in existing_event_ids:
        events_data["events"].append(event_078)
        print("✓ Added EVENT_078 (Sage Account Expiry)")
    
    if "EVENT_079" not in existing_event_ids:
        events_data["events"].append(event_079)
        print("✓ Added EVENT_079 (Rynette Dual Account Access)")
    
    # Update metadata
    events_data["metadata"]["last_evidence_integration"] = datetime.now().isoformat()
    events_data["metadata"]["version"] = "31_NEW_EVIDENCE_2025_12_08"
    events_data["metadata"]["new_events_added"] = ["EVENT_078", "EVENT_079"]
    
    return events_data

def update_timeline_with_new_evidence(timeline_data):
    """Update timeline with new critical dates from SF2A, SF2B, SF1A"""
    if not timeline_data:
        timeline_data = {"metadata": {}, "timeline": []}
    
    # Add critical dates
    new_dates = {
        "2025-06-20": {
            "event": "Rynette Dual Account Access Revealed",
            "evidence": "SF2A - Sage Control User Access screenshot",
            "significance": "Proves Rynette has access to Peter's email (Pete@regima.com) and can impersonate him",
            "parties": ["Rynette Farrar", "Peter Faucitt"],
            "proof_strength": "STRONG - System screenshot evidence",
            "legal_implications": ["identity_impersonation", "fraud", "system_manipulation"]
        },
        "2025-07-23": {
            "event": "Sage Accounting Subscription Expired",
            "evidence": "SF2B - Sage expiry notice",
            "significance": "Rynette Farrar identified as subscription owner - controls access to accounting system",
            "parties": ["Rynette Farrar"],
            "proof_strength": "STRONG - System notification",
            "legal_implications": ["obstruction_of_access", "oppression_s163", "denial_of_financial_records"]
        },
        "2025-08-25": {
            "event": "Sage Expiry Screenshot - Over 1 Month Without Access",
            "evidence": "SF2B - Sage expiry screenshot",
            "significance": "Account expired 23 July, still expired 25 August (over 1 month denial of access)",
            "parties": ["Rynette Farrar"],
            "proof_strength": "STRONG - Demonstrates prolonged obstruction",
            "legal_implications": ["obstruction", "oppression", "unfairly_prejudicial_conduct"]
        },
        "2025-10-23": {
            "event": "Attorney Letter to KEIRO re Payment",
            "evidence": "SF9 - MAT4719 letter",
            "significance": "Legal correspondence regarding payment obligations",
            "parties": ["MAT4719 (Attorney)", "KEIRO (Opposing counsel)"],
            "proof_strength": "MEDIUM - Requires full text extraction",
            "legal_implications": ["litigation_timeline", "payment_demands"]
        },
        "2026-05-01_to_2027-04-30": {
            "event": "Bantjies Call Option Year 1 Window",
            "evidence": "SF1A - Call Option Agreement",
            "significance": "First year call option window - R18,685,000 payment if exercised",
            "parties": ["Danie Bantjies", "Company (Strategic Logistics)"],
            "proof_strength": "STRONG - Contractual obligation",
            "financial_impact": "R18,685,000"
        },
        "2027-05-01_to_2029-04-30": {
            "event": "Bantjies Call Option Year 2 Window",
            "evidence": "SF1A - Call Option Agreement",
            "significance": "Second year call option window - R23,165,000 payment if exercised",
            "parties": ["Danie Bantjies", "Company (Strategic Logistics)"],
            "proof_strength": "STRONG - Contractual obligation",
            "financial_impact": "R23,165,000"
        },
        "2029-05-01_to_2029-04-30": {
            "event": "Bantjies Call Option Year 3 Window",
            "evidence": "SF1A - Call Option Agreement",
            "significance": "Final year call option window - R28,730,000 payment if exercised",
            "parties": ["Danie Bantjies", "Company (Strategic Logistics)"],
            "proof_strength": "STRONG - Contractual obligation",
            "financial_impact": "R28,730,000"
        }
    }
    
    # Update metadata
    if "metadata" not in timeline_data:
        timeline_data["metadata"] = {}
    
    if "critical_evidence_dates" not in timeline_data["metadata"]:
        timeline_data["metadata"]["critical_evidence_dates"] = {}
    
    timeline_data["metadata"]["critical_evidence_dates"].update(new_dates)
    timeline_data["metadata"]["last_evidence_integration"] = datetime.now().isoformat()
    timeline_data["metadata"]["version"] = "22_NEW_EVIDENCE_2025_12_08"
    timeline_data["metadata"]["new_evidence_dates_added"] = list(new_dates.keys())
    
    print(f"✓ Added {len(new_dates)} new critical dates to timeline")
    
    return timeline_data

def main():
    """Main execution function"""
    print("=" * 80)
    print("INTEGRATE NEW EVIDENCE SCRIPT - 2025-12-08")
    print("=" * 80)
    print()
    print("New Evidence Files:")
    print("  - SF2A: Sage User Access (June 2025)")
    print("  - SF2B: Sage Subscription Expiry (August 2025)")
    print("  - SF1A: Bantjies Call Option Agreement")
    print("  - SF9: Attorney Letter to KEIRO (October 2025)")
    print()
    
    # Load latest data models
    print("Loading latest data models...")
    entities_file = ENTITIES_PATH / "entities_evidence_enhanced_2025_12_08.json"
    events_file = EVENTS_PATH / "events_evidence_enhanced_2025_12_08.json"
    timeline_file = TIMELINES_PATH / "timeline_evidence_enhanced_2025_12_08.json"
    
    entities = load_json_file(entities_file)
    events = load_json_file(events_file)
    timeline = load_json_file(timeline_file)
    
    # Update with new evidence
    print("\nUpdating entities with new evidence...")
    entities_updated = update_entities_with_new_evidence(entities)
    
    print("\nAdding new events...")
    events_updated = add_new_events(events)
    
    print("\nUpdating timeline with new evidence dates...")
    timeline_updated = update_timeline_with_new_evidence(timeline)
    
    # Save updated data
    timestamp = datetime.now().strftime("%Y_%m_%d")
    
    print("\nSaving updated data models...")
    save_json_file(entities_updated, ENTITIES_PATH / f"entities_new_evidence_{timestamp}.json")
    save_json_file(events_updated, EVENTS_PATH / f"events_new_evidence_{timestamp}.json")
    save_json_file(timeline_updated, TIMELINES_PATH / f"timeline_new_evidence_{timestamp}.json")
    
    print("\n" + "=" * 80)
    print("NEW EVIDENCE INTEGRATION COMPLETE")
    print("=" * 80)
    print("\nKey Updates:")
    print("✓ PERSON_002 (Rynette): Added SF2A, SF2B - identity impersonation & obstruction")
    print("✓ PERSON_007 (Bantjies): Added SF1A - call option payment schedule")
    print("✓ EVENT_078: Sage account expiry (23 July 2025)")
    print("✓ EVENT_079: Rynette dual account access (20 June 2025)")
    print("✓ Timeline: Added 7 new critical dates")
    print("\nNext steps:")
    print("1. Update legal filings with SF2A, SF2B references")
    print("2. Update GitHub Pages with new evidence")
    print("3. Commit and push changes")

if __name__ == "__main__":
    main()
