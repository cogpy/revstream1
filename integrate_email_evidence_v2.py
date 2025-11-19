#!/usr/bin/env python3
"""
Integrate email archive evidence into data models (Version 2 - Fixed)
Date: 2025-11-19
"""

import json
from datetime import datetime
from pathlib import Path

def load_current_data_models():
    """Load current data models"""
    base_path = Path('/home/ubuntu/revstream1/data_models')
    
    with open(base_path / 'entities/entities_refined_2025_11_18.json', 'r') as f:
        entities = json.load(f)
    
    with open(base_path / 'events/events_refined_2025_11_18.json', 'r') as f:
        events = json.load(f)
    
    with open(base_path / 'relations/relations_refined_2025_11_18.json', 'r') as f:
        relations = json.load(f)
    
    with open(base_path / 'timelines/timeline_refined_2025_11_18.json', 'r') as f:
        timeline = json.load(f)
    
    return entities, events, relations, timeline

def add_new_events_from_emails(events_data):
    """Add new events discovered from email analysis"""
    events = events_data.get('events', [])
    new_events = [
        {
            "event_id": f"EVT-{len(events) + 1:03d}",
            "date": "2025-06-10",
            "title": "Bantjes Email: R10M Decline and Computer Expense Analysis",
            "description": "Danie Bantjes sends email acknowledging his '30-odd year involvement with the Faucitt family business' and confirming the RegimA Group made its first-ever substantial trading loss with a R10M year-on-year bank balance decline. Notes computer expenses exceed 20% of revenue.",
            "category": "financial_fraud",
            "participants": ["Danie Bantjes", "Peter Faucitt", "Jacqui Faucitt", "Daniel Faucitt"],
            "evidence_source": "Email: The RegimA Group results and Computer Expense analysis",
            "significance": "Accountant confirms massive financial losses and excessive IT expenses",
            "legal_impact": "high"
        },
        {
            "event_id": f"EVT-{len(events) + 2:03d}",
            "date": "2025-06-10",
            "title": "Daniel's Comprehensive 26-Point Response to Bantjes",
            "description": "Daniel sends detailed response documenting: (1) Kayla's murder Aug 2023 and card expiry, (2) ReZonance R1.8M director loan, (3) Rynette's unauthorized control of all accounts, (4) Pete/Rynette breaking automations despite warning, (5) Unauthorized banking changes, (6) Rynette making R1M+ debt disappear through fraudulent allocation, (7) Accounts exist only on Rynette's computer, (8) Pattern of theft (Kachan precedent), (9) Need for urgent internal audit.",
            "category": "evidence_documentation",
            "participants": ["Daniel Faucitt", "Danie Bantjes", "Peter Faucitt", "Jacqui Faucitt"],
            "evidence_source": "Email: Re: The RegimA Group results and Computer Expense analysis",
            "significance": "Comprehensive documentation of entire fraud scheme with 26 specific claims",
            "legal_impact": "very_high"
        },
        {
            "event_id": f"EVT-{len(events) + 3:03d}",
            "date": "2025-07-08",
            "title": "POPIA Violation Notice Sent to Pete",
            "description": "Daniel sends formal legal notice to Pete regarding POPIA violation. Discovered Pete had instructed staff to use new system only accessible to him and Rynette, redirected revenue streams such that audit trail disappeared.",
            "category": "legal_action",
            "participants": ["Daniel Faucitt", "Peter Faucitt"],
            "evidence_source": "Email: POPIA Violation Notice - Sent to Pete on 8 July 2025",
            "attachment": "FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.docx",
            "significance": "Formal legal notice of privacy violation and criminal instructions",
            "legal_impact": "very_high"
        },
        {
            "event_id": f"EVT-{len(events) + 4:03d}",
            "date": "2025-07-23",
            "title": "Sage Accounting System Expires - Rynette Controls Reactivation",
            "description": "RegimA Worldwide Distribution's Sage accounting registration expires. Rynette Farrar is the subscription owner and only she can reactivate. System shows message: 'Your Accounting registration expired on 23/07/2025. You will no longer be able to access your company data in Accounting.'",
            "category": "system_control",
            "participants": ["Rynette Farrar"],
            "evidence_source": "Screenshot: Sage Account RegimA Worldwide Distribution (2025-08-25)",
            "significance": "Rynette can deny all users access to financial records by not renewing subscription",
            "legal_impact": "high"
        },
        {
            "event_id": f"EVT-{len(events) + 5:03d}",
            "date": "2025-08-29",
            "title": "Daniel Forwards Sage Evidence to Lawyer",
            "description": "Daniel forwards Sage screenshots to lawyer (smunga@ensafrica.com) showing Rynette using Pete@regima.com email account. Includes screenshots from June 20 and August 25, 2025.",
            "category": "legal_action",
            "participants": ["Daniel Faucitt", "ENS Africa lawyer"],
            "evidence_source": "Email: RegimA Worldwide - Sage - Rynette using Pete@regima.com",
            "significance": "Smoking gun evidence of email control shared with legal counsel",
            "legal_impact": "very_high"
        },
        {
            "event_id": f"EVT-{len(events) + 6:03d}",
            "date": "2024",
            "title": "Rynette Makes R1M+ Debt to ReZonance 'Disappear'",
            "description": "Rynette fraudulently eliminates over R1M debt owed by RegimA Skin Treatments to ReZonance by misallocating international GoDaddy payments as though they were local payments made to ReZonance. ReZonance never received these payments; amounts remain outstanding.",
            "category": "financial_fraud",
            "participants": ["Rynette Farrar"],
            "evidence_source": "Email: Daniel's comprehensive response (2025-06-10)",
            "significance": "Provable fraud - bank records will show ReZonance never received payments",
            "legal_impact": "very_high"
        },
        {
            "event_id": f"EVT-{len(events) + 7:03d}",
            "date": "2024-2025",
            "title": "Pete and Rynette Attempt Unauthorized Banking Changes",
            "description": "Over the past year, bank contacts Daniel multiple times to ask for approval where Pete and Rynette attempted to draft mandates to change ownership structure, close Daniel's accounts, and cancel his cards - all without his knowledge or consent. Daniel informs bank these are errors and tells Pete/Rynette to cease immediately.",
            "category": "financial_fraud",
            "participants": ["Peter Faucitt", "Rynette Farrar", "Daniel Faucitt"],
            "evidence_source": "Email: Daniel's comprehensive response (2025-06-10)",
            "significance": "Multiple attempted unauthorized banking changes; bank recognized irregularities",
            "legal_impact": "very_high"
        }
    ]
    
    events_data['events'] = events + new_events
    events_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    events_data['metadata']['total_events'] = len(events_data['events'])
    return events_data

def add_new_relations_from_emails(relations_data):
    """Add new relations discovered from email analysis"""
    relations = relations_data.get('relations', {})
    
    # Ensure categories exist
    if 'email_control_relations' not in relations:
        relations['email_control_relations'] = []
    if 'system_control_relations' not in relations:
        relations['system_control_relations'] = []
    if 'employment_relations' not in relations:
        relations['employment_relations'] = []
    if 'financial_relations' not in relations:
        relations['financial_relations'] = []
    if 'conspiracy_relations' not in relations:
        relations['conspiracy_relations'] = []
    
    # Add email control relation
    relations['email_control_relations'].append({
        "source_entity": "Rynette Farrar",
        "target_entity": "Pete@regima.com",
        "relation_type": "has_unauthorized_access_to",
        "description": "Rynette has access to and uses Pete's email account Pete@regima.com",
        "evidence_source": "Sage screenshot (2025-06-20)",
        "date_established": "2025-06-20",
        "significance": "Smoking gun evidence of email control",
        "legal_impact": "very_high"
    })
    
    # Add system control relation
    relations['system_control_relations'].append({
        "source_entity": "Rynette Farrar",
        "target_entity": "Sage Accounting System",
        "relation_type": "subscription_owner",
        "description": "Rynette is the subscription owner for RegimA Worldwide Distribution's Sage accounting system",
        "evidence_source": "Sage screenshot (2025-08-25)",
        "date_established": "2025-08-25",
        "significance": "Controls access to all financial records",
        "legal_impact": "high"
    })
    
    # Add employment relation
    relations['employment_relations'].append({
        "source_entity": "Danie Bantjes",
        "target_entity": "Rynette Farrar",
        "relation_type": "drafted_employment_contract",
        "description": "Bantjes drafted Rynette's employment offer letter and advised on notice periods",
        "evidence_source": "Email: OFFER OF EMPLOYMENT LETTER - RYNETTE FARRAR (2020-03-19)",
        "date_established": "2020-03-19",
        "significance": "Bantjes involved in Rynette's employment from the start",
        "legal_impact": "medium"
    })
    
    # Add financial relations
    relations['financial_relations'].extend([
        {
            "source_entity": "Daniel Faucitt",
            "target_entity": "ReZonance",
            "relation_type": "director_loan",
            "description": "ReZonance owes Daniel R1.8 million as director from his investments over the years",
            "evidence_source": "Email: Daniel's comprehensive response (2025-06-10)",
            "amount": "R1,800,000",
            "date_established": "2025-06-10",
            "significance": "Substantial director loan; motive to preserve company",
            "legal_impact": "high"
        },
        {
            "source_entity": "RegimA Skin Treatments",
            "target_entity": "ReZonance",
            "relation_type": "owes_debt",
            "description": "RegimA Skin Treatments owes over R1M to ReZonance (as of Feb 2023)",
            "evidence_source": "Email: Daniel's comprehensive response (2025-06-10); Rezonance Febr 2023.PDF",
            "amount": "R1,000,000+",
            "date_established": "2023-02",
            "significance": "Legitimate unpaid debt",
            "legal_impact": "high"
        }
    ])
    
    # Add conspiracy relation
    relations['conspiracy_relations'].append({
        "source_entity": "Peter Faucitt",
        "target_entity": "Kachan",
        "relation_type": "previous_theft_victim",
        "description": "Pete previously took revenue from Kachan by instructing people to pay into another account - same pattern as with Daniel",
        "evidence_source": "Email: Daniel's comprehensive response (2025-06-10)",
        "date_established": "2025-06-10",
        "significance": "Pattern of theft behavior; prior bad acts",
        "legal_impact": "high"
    })
    
    relations_data['relations'] = relations
    relations_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    
    # Count total relations
    total = sum(len(v) for v in relations.values() if isinstance(v, list))
    relations_data['metadata']['total_relations'] = total
    
    return relations_data

def update_timeline_with_email_events(timeline):
    """Update timeline with events from email analysis"""
    new_phase = {
        "phase_id": len(timeline.get("phases", [])) + 1,
        "title": "Email Evidence and Legal Action (2025)",
        "date_range": "2025-06-10 to 2025-08-29",
        "description": "Period of comprehensive evidence documentation through emails, formal legal notices, and system lockouts. Includes Bantjes' acknowledgment of R10M decline, Daniel's 26-point fraud documentation, POPIA violation notice, Sage system expiry, and evidence sharing with legal counsel.",
        "key_events": [
            "2025-06-10: Bantjes email confirming R10M decline",
            "2025-06-10: Daniel's comprehensive 26-point response",
            "2025-07-08: POPIA violation notice sent to Pete",
            "2025-07-23: Sage accounting system expires (Rynette controls reactivation)",
            "2025-08-29: Daniel forwards Sage evidence to lawyer"
        ],
        "significance": "Smoking gun evidence documented and shared with legal counsel",
        "legal_impact": "very_high"
    }
    
    if "phases" not in timeline:
        timeline["phases"] = []
    
    timeline["phases"].append(new_phase)
    
    return timeline

def save_updated_data_models(entities, events, relations, timeline):
    """Save updated data models with new date"""
    base_path = Path('/home/ubuntu/revstream1/data_models')
    date_str = '2025_11_19'
    
    with open(base_path / f'entities/entities_refined_{date_str}.json', 'w') as f:
        json.dump(entities, f, indent=2)
    
    with open(base_path / f'events/events_refined_{date_str}.json', 'w') as f:
        json.dump(events, f, indent=2)
    
    with open(base_path / f'relations/relations_refined_{date_str}.json', 'w') as f:
        json.dump(relations, f, indent=2)
    
    with open(base_path / f'timelines/timeline_refined_{date_str}.json', 'w') as f:
        json.dump(timeline, f, indent=2)
    
    return date_str

def main():
    print("=" * 80)
    print("INTEGRATE EMAIL EVIDENCE INTO DATA MODELS")
    print("Date: 2025-11-19")
    print("=" * 80)
    print()
    
    print("Loading current data models...")
    entities, events, relations, timeline = load_current_data_models()
    
    print(f"Current counts:")
    print(f"  Entities: {len(entities.get('entities', []))}")
    print(f"  Events: {len(events.get('events', []))}")
    rels = relations.get('relations', {})
    total_rels = sum(len(v) for v in rels.values() if isinstance(v, list))
    print(f"  Relations: {total_rels}")
    print(f"  Timeline phases: {len(timeline.get('phases', []))}")
    
    print("\nAdding new events from email analysis...")
    events = add_new_events_from_emails(events)
    
    print("Adding new relations from email analysis...")
    relations = add_new_relations_from_emails(relations)
    
    print("Updating timeline with email events...")
    timeline = update_timeline_with_email_events(timeline)
    
    print("\nNew counts:")
    print(f"  Entities: {len(entities.get('entities', []))}")
    print(f"  Events: {len(events.get('events', []))}")
    rels = relations.get('relations', {})
    total_rels = sum(len(v) for v in rels.values() if isinstance(v, list))
    print(f"  Relations: {total_rels}")
    print(f"  Timeline phases: {len(timeline.get('phases', []))}")
    
    print("\nSaving updated data models...")
    date_str = save_updated_data_models(entities, events, relations, timeline)
    
    print("\n" + "=" * 80)
    print("INTEGRATION COMPLETE")
    print("=" * 80)
    print(f"\nUpdated data models saved with date: {date_str}")
    print(f"  - entities_refined_{date_str}.json")
    print(f"  - events_refined_{date_str}.json")
    print(f"  - relations_refined_{date_str}.json")
    print(f"  - timeline_refined_{date_str}.json")

if __name__ == '__main__':
    main()
