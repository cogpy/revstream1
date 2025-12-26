#!/usr/bin/env python3
"""
Apply corrections for RegimaSA vs RegimA SA confusion and integrate new findings
Date: 2025-11-19
"""

import json
from datetime import datetime
from copy import deepcopy

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def correct_regimasa_entity(entities_data):
    """Correct RegimaSA entity - it's legitimate, just clarify it's NOT RegimA SA"""
    
    # Find and update ORG_012
    for org in entities_data['entities']['organizations']:
        if org.get('entity_id') == 'ORG_012':
            org['note'] = "RegimaSA (lowercase 'a') - NOT the same as RegimA SA (capital 'A')"
            org['clarification'] = "This entity (2017/087935/07) is separate from RegimA SA (Pty) Ltd which was created in 2021"
            print("   Updated ORG_012 (RegimaSA) with clarification note")
            break
    
    return entities_data

def add_regima_sa_entity(entities_data):
    """Add RegimA SA (Pty) Ltd as new entity ORG_014"""
    
    regima_sa = {
        "entity_id": "ORG_014",
        "name": "RegimA SA (Pty) Ltd",
        "incorporation_date": "2021",
        "role": "RegimA Group entity",
        "agent_type": "unknown",
        "email": "d@rzo.io",
        "associated_person": "PERSON_005",
        "relationships": [
            "associated_with:PERSON_005"
        ],
        "significance": "Separate entity from RegimaSA (2017/087935/07); created in 2021; appears in Sage accounting system",
        "evidence": [
            "Sage screenshot 2025-06-20 - Control User Access",
            "User correction: RegimA SA didn't exist until 2021"
        ],
        "note": "Capital 'A' in RegimA - different from RegimaSA (lowercase 'a')"
    }
    
    entities_data['entities']['organizations'].append(regima_sa)
    print("   Added ORG_014 (RegimA SA) as new entity")
    
    return entities_data

def update_rynette_entity(entities_data):
    """Update Rynette Farrar with Sage control and email access evidence"""
    
    for person in entities_data['entities']['persons']:
        if person.get('entity_id') == 'PERSON_002':
            person['sage_control'] = {
                "subscription_owner": "RegimA Worldwide Distribution (Pty) Ltd",
                "expiry_date": "2025-07-23",
                "user_accounts": [
                    "Pete@regima.com",
                    "rynette@regima.zone"
                ]
            }
            person['email_access'] = {
                "pete_email": "Pete@regima.com",
                "evidence": "Sage screenshot 2025-06-20 shows Rynette with user account Pete@regima.com",
                "significance": "Direct proof of email control"
            }
            if 'relationships' not in person:
                person['relationships'] = []
            person['relationships'].extend([
                "controls_sage:ORG_001",
                "email_access:PERSON_001"
            ])
            print("   Updated PERSON_002 (Rynette) with Sage control and email access")
            break
    
    return entities_data

def update_bantjes_entity(entities_data):
    """Update Bantjes with 30-year involvement and R10M decline acknowledgment"""
    
    for person in entities_data['entities']['persons']:
        if person.get('entity_id') == 'PERSON_007':
            person['involvement_duration'] = "30-odd years with Faucitt family business"
            person['email_2025_06_10'] = {
                "subject": "The RegimA Group results and Computer Expense analysis",
                "key_statements": [
                    "30-odd year involvement with the Faucitt family business",
                    "R10m decline year-on-year for the Group, including Villa Via",
                    "First time in history made a substantial trading loss",
                    "Computer expenses in excess of 20% of revenue"
                ],
                "significance": "Acknowledges massive financial deterioration but dismisses detailed audit"
            }
            print("   Updated PERSON_007 (Bantjes) with 30-year involvement and R10M decline")
            break
    
    return entities_data

def update_unicorn_dynamics(entities_data):
    """Update Unicorn Dynamics with transaction details"""
    
    for org in entities_data['entities']['organizations']:
        if org.get('entity_id') == 'ORG_013':
            org['transactions_regima_wwd'] = {
                "period": "2022-03-01 to 2023-02-03",
                "opening_balance": 7400.00,
                "total_invoices": 13129.03,
                "total_payments": -20529.03,
                "closing_balance": 0.00,
                "services": "IT/software services, including Sage accounting",
                "significance": "All debts cleared by Feb 2023"
            }
            if 'relationships' not in org:
                org['relationships'] = []
            org['relationships'].append("supplier_to:ORG_001")
            print("   Updated ORG_013 (Unicorn Dynamics) with transaction details")
            break
    
    return entities_data

def update_rezonance_entity(entities_data):
    """Update ReZonance with financial data and transactions"""
    
    for org in entities_data['entities']['organizations']:
        if org.get('entity_id') == 'ORG_008':
            org['profit_loss_2017_2025'] = {
                "total_income": 5974677.89,
                "total_expenses": 509851.24,
                "net_earnings": -220571.33,
                "gross_profit_2023_2024": 33713.47,
                "gross_profit_2024_2025": 0.00,
                "significance": "Zero profit in 2024-2025 coincides with fraud escalation"
            }
            org['transactions_regima_wwd_2022'] = {
                "period": "2022-03-01 to 2023-02-03",
                "opening_balance": 85565.60,
                "total_payments_received": 442378.05,
                "closing_balance": 22879.09,
                "major_payments": [
                    {"date": "2022-07-30", "amount": 7315.35},
                    {"date": "2022-09-30", "amount": 50000.00},
                    {"date": "2022-10-31", "amount": 50000.00},
                    {"date": "2022-12-29", "amount": 50000.00}
                ],
                "total_major_payments": 157315.35,
                "significance": "Debt reduced from R85k to R22k through large payments"
            }
            print("   Updated ORG_008 (ReZonance) with financial data and transactions")
            break
    
    return entities_data

def add_new_events(events_data):
    """Add new events from document analysis"""
    
    new_events = [
        {
            "event_id": "EVENT_065",
            "date": "2025-07-23",
            "event_type": "System control",
            "category": "Access control",
            "description": "RegimA WWD Sage accounting registration expired; Rynette Farrar controls reactivation",
            "entities_involved": ["ORG_001", "PERSON_002"],
            "perpetrators": ["PERSON_002"],
            "victims": ["PERSON_001", "PERSON_004"],
            "location": "South Africa",
            "financial_impact": 0,
            "significance": "Rynette can deny access to financial records by not renewing Sage subscription",
            "evidence": [
                "Sage screenshot 2025-08-25 - Accounting Registration Expired"
            ],
            "timeline_phase": "PHASE_006",
            "related_events": []
        },
        {
            "event_id": "EVENT_066",
            "date": "2025-06-10",
            "event_type": "Financial disclosure",
            "category": "Evidence documentation",
            "description": "Bantjes email confirms R10M bank balance decline year-on-year; first-ever substantial trading loss in RegimA Group history",
            "entities_involved": ["PERSON_007", "PERSON_001", "PERSON_004", "PERSON_005"],
            "perpetrators": [],
            "victims": ["PERSON_001", "PERSON_004"],
            "location": "South Africa",
            "financial_impact": -10000000,
            "significance": "Massive financial deterioration acknowledged by accountant; Bantjes dismisses detailed audit despite acknowledging losses",
            "evidence": [
                "Email: The RegimA Group results and Computer Expense analysis (2025-06-10)"
            ],
            "timeline_phase": "PHASE_006",
            "related_events": ["EVENT_065"],
            "key_statements": [
                "30-odd year involvement with the Faucitt family business",
                "R10m decline year-on-year for the Group, including Villa Via",
                "First time in history made a substantial trading loss",
                "Computer expenses in excess of 20% of revenue"
            ]
        },
        {
            "event_id": "EVENT_067",
            "date": "2022-07-30",
            "event_type": "Debt payment",
            "category": "Financial transactions",
            "description": "RegimA WWD paid R157k+ to ReZonance, reducing debt from R85k to R22k (July-December 2022)",
            "entities_involved": ["ORG_001", "ORG_008"],
            "perpetrators": [],
            "victims": [],
            "location": "South Africa",
            "financial_impact": -157315.35,
            "significance": "Large debt payments during pre-fraud period; debt reduction suggests legitimate business relationship or settlement strategy",
            "evidence": [
                "Rez-WWD.pdf - Supplier Transactions Report"
            ],
            "timeline_phase": "PHASE_000",
            "related_events": [],
            "payment_details": [
                {"date": "2022-07-30", "amount": 7315.35},
                {"date": "2022-09-30", "amount": 50000.00},
                {"date": "2022-10-31", "amount": 50000.00},
                {"date": "2022-12-29", "amount": 50000.00}
            ]
        }
    ]
    
    events_data['events'].extend(new_events)
    print(f"   Added 3 new events: EVENT_065, EVENT_066, EVENT_067")
    
    return events_data

def add_new_relations(relations_data):
    """Add new relations from document analysis"""
    
    new_relations = {
        "control_relations": [
            {
                "relation_id": "REL_CTRL_008",
                "from_entity": "PERSON_002",
                "to_entity": "ORG_001",
                "relation_type": "controls_sage_accounting",
                "description": "Rynette Farrar is Sage subscription owner for RegimA WWD; controls access to financial records",
                "evidence": [
                    "Sage screenshot 2025-08-25 - Accounting Registration Expired",
                    "Subscription owner: Rynette Farrar"
                ],
                "significance": "Can deny access to financial records by not renewing subscription; system expired July 23, 2025"
            }
        ],
        "email_control_relations": [
            {
                "relation_id": "REL_EMAIL_002",
                "from_entity": "PERSON_002",
                "to_entity": "PERSON_001",
                "relation_type": "email_access",
                "description": "Rynette Farrar has user account with Pete@regima.com in Sage system",
                "evidence": [
                    "Sage screenshot 2025-06-20 - Control User Access",
                    "User list shows: Rynette Farrar - Pete@regima.com"
                ],
                "significance": "Direct proof of Rynette's access to Peter's email; explains how she could send emails as Peter"
            }
        ],
        "financial_relations": [
            {
                "relation_id": "REL_FIN_010",
                "from_entity": "ORG_001",
                "to_entity": "ORG_008",
                "relation_type": "debt_payment",
                "description": "RegimA WWD paid R157,315.35 to ReZonance (July-December 2022)",
                "amount": 157315.35,
                "currency": "ZAR",
                "period": "2022-07-30 to 2022-12-29",
                "evidence": [
                    "Rez-WWD.pdf - Supplier Transactions Report"
                ],
                "significance": "Large debt payments reducing ReZonance debt from R85k to R22k"
            },
            {
                "relation_id": "REL_FIN_011",
                "from_entity": "ORG_001",
                "to_entity": "ORG_013",
                "relation_type": "supplier_payment",
                "description": "RegimA WWD paid R20,529.03 to Unicorn Dynamics (March 2022 - February 2023)",
                "amount": 20529.03,
                "currency": "ZAR",
                "period": "2022-03-01 to 2023-02-03",
                "evidence": [
                    "Unicorn-WWD.pdf - Supplier Transactions Report"
                ],
                "significance": "Cleared all Unicorn Dynamics debts by Feb 2023"
            }
        ]
    }
    
    if 'relations' not in relations_data:
        relations_data['relations'] = {}
    
    for category, new_rels in new_relations.items():
        if category not in relations_data['relations']:
            relations_data['relations'][category] = []
        relations_data['relations'][category].extend(new_rels)
    
    total_new = sum(len(rels) for rels in new_relations.values())
    print(f"   Added {total_new} new relations")
    
    return relations_data

def update_metadata(data, data_type):
    """Update metadata"""
    
    if 'metadata' not in data:
        data['metadata'] = {}
    
    current_version = data['metadata'].get('version', '0.0')
    try:
        major, minor = map(int, current_version.split('.'))
        new_version = f"{major + 1}.0"
    except:
        new_version = "1.0"
    
    data['metadata']['version'] = new_version
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['metadata']['changes'] = 'Correction 2025-11-19: Clarified RegimaSA vs RegimA SA; added new findings from financial documents, Sage screenshots, and Bantjes email'
    
    return data

def main():
    """Main correction and integration function"""
    print("=" * 80)
    print("APPLYING CORRECTIONS AND NEW FINDINGS")
    print("Date: 2025-11-19")
    print("=" * 80)
    print()
    
    # Load current data models
    base_path = '/home/ubuntu/revstream1/data_models'
    
    print("Loading current data models...")
    entities_data = load_json(f'{base_path}/entities/entities.json')
    events_data = load_json(f'{base_path}/events/events.json')
    relations_data = load_json(f'{base_path}/relations/relations.json')
    
    # Apply corrections and updates
    print("\n1. Correcting RegimaSA entity (ORG_012)...")
    entities_data = correct_regimasa_entity(entities_data)
    
    print("\n2. Adding RegimA SA entity (ORG_014)...")
    entities_data = add_regima_sa_entity(entities_data)
    
    print("\n3. Updating Rynette Farrar (PERSON_002)...")
    entities_data = update_rynette_entity(entities_data)
    
    print("\n4. Updating Danie Bantjes (PERSON_007)...")
    entities_data = update_bantjes_entity(entities_data)
    
    print("\n5. Updating Unicorn Dynamics (ORG_013)...")
    entities_data = update_unicorn_dynamics(entities_data)
    
    print("\n6. Updating ReZonance (ORG_008)...")
    entities_data = update_rezonance_entity(entities_data)
    
    print("\n7. Adding new events...")
    events_data = add_new_events(events_data)
    
    print("\n8. Adding new relations...")
    relations_data = add_new_relations(relations_data)
    
    print("\n9. Updating metadata...")
    entities_data = update_metadata(entities_data, 'entities')
    events_data = update_metadata(events_data, 'events')
    relations_data = update_metadata(relations_data, 'relations')
    
    # Save updated data models
    print("\n10. Saving updated data models...")
    save_json(entities_data, f'{base_path}/entities/entities.json')
    save_json(events_data, f'{base_path}/events/events.json')
    save_json(relations_data, f'{base_path}/relations/relations.json')
    
    print("\n" + "=" * 80)
    print("CORRECTION AND INTEGRATION SUMMARY")
    print("=" * 80)
    print(f"\nCorrected: ORG_012 (RegimaSA) - clarified it's NOT RegimA SA")
    print(f"Added: ORG_014 (RegimA SA) - new entity created 2021")
    print(f"Updated: PERSON_002 (Rynette) - Sage control + email access")
    print(f"Updated: PERSON_007 (Bantjes) - 30-year involvement + R10M decline")
    print(f"Updated: ORG_013 (Unicorn Dynamics) - transaction details")
    print(f"Updated: ORG_008 (ReZonance) - financial data + transactions")
    print(f"New events added: 3 (EVENT_065, EVENT_066, EVENT_067)")
    print(f"New relations added: 4")
    
    print("\n" + "=" * 80)
    print("CORRECTION COMPLETE")
    print("=" * 80)
    
    print(f"\nUpdated files:")
    print(f"  - {base_path}/entities/entities.json")
    print(f"  - {base_path}/events/events.json")
    print(f"  - {base_path}/relations/relations.json")

if __name__ == '__main__':
    main()
