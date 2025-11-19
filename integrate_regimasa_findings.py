#!/usr/bin/env python3
"""
Integrate RegimaSA 2019 Financial Statements findings into data models
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

def add_new_entities(entities_data):
    """Add new entities from RegimaSA financial statements"""
    
    # Add ORG_012: RegimaSA (Pty) Ltd
    regimasa = {
        "entity_id": "ORG_012",
        "name": "RegimaSA (Pty) Ltd",
        "registration_number": "2017/087935/07",
        "tax_reference": "9746755165",
        "incorporation_date": "2017-02-24",
        "nature_of_business": "Collections Agent",
        "industry": "Financial Services",
        "role": "Shell company / Related party entity",
        "agent_type": "instrument",
        "directors": ["PERSON_001", "PERSON_005"],
        "registered_office": "50 Van Buuren Road, Bedfordview, Johannesburg, 2008",
        "bankers": "First National Bank",
        "secretary": "De Novo Business Services (Pty) Ltd",
        "financial_year_end": "2019-02-28",
        "total_assets_2019": 4912,
        "accumulated_loss_2019": -1589,
        "shareholder_loan_2019": 6000,
        "related_parties": ["ORG_008", "ORG_013", "PERSON_001", "PERSON_005"],
        "relationships": [
            "owned_by:PERSON_001,PERSON_005",
            "controlled_by:PERSON_001",
            "controlled_by:PERSON_005",
            "loan_to:ORG_008",
            "loan_from:PERSON_005",
            "loan_from:ORG_013"
        ],
        "significance": "Shell company with no revenue or operations; related party loans to ReZonance; financial statements prepared retrospectively in June 2025 (6+ years late)",
        "evidence": [
            "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf",
            "CIPC registration 2017/087935/07"
        ]
    }
    
    # Add ORG_013: Unicorn Dynamics (Pty) Ltd
    unicorn = {
        "entity_id": "ORG_013",
        "name": "Unicorn Dynamics (Pty) Ltd",
        "role": "Related party entity",
        "agent_type": "unknown",
        "nature_of_business": "Unknown",
        "related_parties": ["ORG_012"],
        "relationships": [
            "loan_to:ORG_012"
        ],
        "financial_relationship_2019": "R500 loan to RegimaSA",
        "significance": "Related party entity in Regima network; mentioned in CIPC warning July 2, 2025",
        "evidence": [
            "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf",
            "ad-res-j7 CIPC warning reference"
        ]
    }
    
    # Add PERSON_012: Marisca Meyer
    marisca = {
        "entity_id": "PERSON_012",
        "name": "Marisca Meyer",
        "full_name": "Marisca Meyer",
        "role": "Professional Accountant (SA)",
        "agent_type": "neutral",
        "profession": "Professional Accountant",
        "relationships": [
            "prepared_financials_for:ORG_012"
        ],
        "actions": [
            "Prepared RegimaSA 2019 financial statements (issued 25 June 2025)"
        ],
        "significance": "Prepared 6-year-old financial statements retrospectively in June 2025, timing coincides with legal proceedings",
        "evidence": [
            "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf"
        ]
    }
    
    # Add to entities data
    if 'entities' not in entities_data:
        entities_data['entities'] = {}
    
    if 'organizations' not in entities_data['entities']:
        entities_data['entities']['organizations'] = []
    
    if 'persons' not in entities_data['entities']:
        entities_data['entities']['persons'] = []
    
    entities_data['entities']['organizations'].append(regimasa)
    entities_data['entities']['organizations'].append(unicorn)
    entities_data['entities']['persons'].append(marisca)
    
    print(f"   Added 3 new entities: ORG_012 (RegimaSA), ORG_013 (Unicorn Dynamics), PERSON_012 (Marisca Meyer)")
    
    return entities_data

def add_new_events(events_data):
    """Add new events from RegimaSA financial statements"""
    
    new_events = [
        {
            "event_id": "EVENT_H011",
            "date": "2017-02-24",
            "event_type": "Company incorporation",
            "category": "Business structure",
            "description": "RegimaSA (Pty) Ltd incorporated as Collections Agent",
            "entities_involved": ["ORG_012", "PERSON_001", "PERSON_005"],
            "perpetrators": ["PERSON_001", "PERSON_005"],
            "victims": [],
            "location": "South Africa",
            "financial_impact": 0,
            "significance": "Establishment of shell company structure with no legitimate business operations",
            "evidence": [
                "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf",
                "CIPC registration 2017/087935/07"
            ],
            "timeline_phase": "PHASE_000",
            "related_events": ["EVENT_H012"]
        },
        {
            "event_id": "EVENT_H012",
            "date": "2019-02-28",
            "event_type": "Financial year end",
            "category": "Financial structure",
            "description": "RegimaSA first financial year end (15 months) showing zero revenue, R1,589 loss, minimal activity",
            "entities_involved": ["ORG_012", "ORG_008", "ORG_013", "PERSON_001", "PERSON_005"],
            "perpetrators": ["PERSON_001", "PERSON_005"],
            "victims": [],
            "location": "South Africa",
            "financial_impact": -1589,
            "related_party_transactions": {
                "loan_to_rezonance": 1853,
                "loan_from_daniel_faucitt": 6000,
                "loan_from_unicorn_dynamics": 500
            },
            "significance": "Evidence of shell company with no operations; related party loans to ReZonance during debt accumulation period",
            "evidence": [
                "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf"
            ],
            "timeline_phase": "PHASE_000",
            "related_events": ["EVENT_H011", "EVENT_064"]
        },
        {
            "event_id": "EVENT_064",
            "date": "2025-06-25",
            "event_type": "Retrospective financial statement preparation",
            "category": "Evidence documentation",
            "description": "RegimaSA 2019 financial statements prepared and issued by Marisca Meyer, 6+ years after period end",
            "entities_involved": ["ORG_012", "PERSON_001", "PERSON_005", "PERSON_012"],
            "perpetrators": ["PERSON_001", "PERSON_005", "PERSON_012"],
            "victims": [],
            "location": "South Africa",
            "financial_impact": 0,
            "significance": "Retrospective preparation timing coincides with legal proceedings in case 2025-137857; suggests strategic document preparation for legal defense",
            "evidence": [
                "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf"
            ],
            "timeline_phase": "PHASE_006",
            "related_events": ["EVENT_H011", "EVENT_H012"],
            "legal_significance": "Document preparation timing suggests response to legal proceedings; establishes Peter's directorship and control"
        }
    ]
    
    if 'events' not in events_data:
        events_data['events'] = []
    
    events_data['events'].extend(new_events)
    
    print(f"   Added 3 new events: EVENT_H011, EVENT_H012, EVENT_064")
    
    return events_data

def add_new_relations(relations_data):
    """Add new relations from RegimaSA financial statements"""
    
    new_relations = {
        "ownership_relations": [
            {
                "relation_id": "REL_OWN_007",
                "from_entity": "PERSON_001,PERSON_005",
                "to_entity": "ORG_012",
                "relation_type": "owns",
                "description": "Peter and Daniel Faucitt own RegimaSA (Pty) Ltd",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Directors and shareholders"
                ],
                "significance": "Joint ownership establishes both Peter and Daniel's control and fiduciary duties"
            }
        ],
        "control_relations": [
            {
                "relation_id": "REL_CTRL_006",
                "from_entity": "PERSON_001",
                "to_entity": "ORG_012",
                "relation_type": "controls_as_director",
                "description": "Peter Faucitt (P.A. Faucitt) is director of RegimaSA",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Directors' Report page 4"
                ],
                "significance": "Establishes Peter's control and fiduciary duties; contradicts claims of separation from Regima entities"
            },
            {
                "relation_id": "REL_CTRL_007",
                "from_entity": "PERSON_005",
                "to_entity": "ORG_012",
                "relation_type": "controls_as_director",
                "description": "Daniel Faucitt (D.J. Faucitt) is director of RegimaSA",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Directors' Report page 4"
                ],
                "significance": "Establishes Daniel's control and fiduciary duties"
            }
        ],
        "financial_relations": [
            {
                "relation_id": "REL_FIN_007",
                "from_entity": "ORG_012",
                "to_entity": "ORG_008",
                "relation_type": "loan_receivable",
                "description": "RegimaSA has R1,853 loan receivable from ReZonance (Pty) Ltd",
                "amount": 1853,
                "currency": "ZAR",
                "date": "2019-02-28",
                "terms": "Unsecured, no fixed repayment terms, interest at rates agreed upon from time to time",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Note 2, page 11"
                ],
                "significance": "Establishes financial relationship between RegimaSA and ReZonance during debt accumulation period"
            },
            {
                "relation_id": "REL_FIN_008",
                "from_entity": "ORG_012",
                "to_entity": "PERSON_005",
                "relation_type": "loan_payable_shareholder",
                "description": "RegimaSA owes R6,000 to Daniel Faucitt (D.A. Faucitt) as shareholder loan",
                "amount": 6000,
                "currency": "ZAR",
                "date": "2019-02-28",
                "terms": "Unsecured, no fixed repayment terms, interest at rates agreed upon from time to time",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Note 4, page 11"
                ],
                "significance": "Establishes Daniel's financial investment and interest in RegimaSA"
            },
            {
                "relation_id": "REL_FIN_009",
                "from_entity": "ORG_012",
                "to_entity": "ORG_013",
                "relation_type": "loan_payable",
                "description": "RegimaSA owes R500 to Unicorn Dynamics (Pty) Ltd",
                "amount": 500,
                "currency": "ZAR",
                "date": "2019-02-28",
                "terms": "Unsecured, no fixed repayment terms, interest at rates agreed upon from time to time",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Note 5, page 11"
                ],
                "significance": "Establishes financial relationship with Unicorn Dynamics, another related party entity"
            }
        ],
        "professional_relations": [
            {
                "relation_id": "REL_PROF_003",
                "from_entity": "PERSON_012",
                "to_entity": "ORG_012",
                "relation_type": "prepared_financial_statements",
                "description": "Marisca Meyer prepared RegimaSA 2019 financial statements (issued 25 June 2025)",
                "evidence": [
                    "RegimaSA(Pty)Ltd-2019-Financialstatements-SME.pdf - Preparer, page 1"
                ],
                "significance": "Retrospective preparation 6+ years after period end; timing coincides with legal proceedings"
            }
        ]
    }
    
    if 'relations' not in relations_data:
        relations_data['relations'] = {}
    
    # Add new relations to existing categories
    for category, new_rels in new_relations.items():
        if category not in relations_data['relations']:
            relations_data['relations'][category] = []
        relations_data['relations'][category].extend(new_rels)
    
    total_new = sum(len(rels) for rels in new_relations.values())
    print(f"   Added {total_new} new relations across 4 categories")
    
    return relations_data

def update_timeline(timeline_data, events_data):
    """Update timeline with new events"""
    
    # Add EVENT_H011 and EVENT_H012 to PHASE_000
    if 'timeline_phases' in timeline_data and 'PHASE_000' in timeline_data['timeline_phases']:
        phase_000 = timeline_data['timeline_phases']['PHASE_000']
        
        if 'events' not in phase_000:
            phase_000['events'] = []
        
        # Add new events
        phase_000['events'].extend(['EVENT_H011', 'EVENT_H012'])
        
        # Update event count
        phase_000['event_count'] = len(phase_000['events'])
        
        print(f"   Updated PHASE_000: added EVENT_H011 and EVENT_H012 (new count: {phase_000['event_count']})")
    
    # Add EVENT_064 to PHASE_006
    if 'timeline_phases' in timeline_data and 'PHASE_006' in timeline_data['timeline_phases']:
        phase_006 = timeline_data['timeline_phases']['PHASE_006']
        
        if 'events' not in phase_006:
            phase_006['events'] = []
        
        # Add new event
        phase_006['events'].append('EVENT_064')
        
        # Update event count
        phase_006['event_count'] = len(phase_006['events'])
        
        print(f"   Updated PHASE_006: added EVENT_064 (new count: {phase_006['event_count']})")
    
    return timeline_data

def update_metadata(data, data_type, version_increment=1):
    """Update metadata for data model"""
    
    if 'metadata' not in data:
        data['metadata'] = {}
    
    # Parse current version
    current_version = data['metadata'].get('version', '0.0')
    try:
        major, minor = map(int, current_version.split('.'))
        new_version = f"{major + version_increment}.0"
    except:
        new_version = "1.0"
    
    data['metadata']['version'] = new_version
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['metadata']['changes'] = f'Integration 2025-11-19: Added RegimaSA (Pty) Ltd 2019 financial statements findings'
    
    return data

def main():
    """Main integration function"""
    print("=" * 80)
    print("INTEGRATING REGIMASA 2019 FINANCIAL STATEMENTS FINDINGS")
    print("Date: 2025-11-19")
    print("=" * 80)
    print()
    
    # Load current data models
    base_path = '/home/ubuntu/revstream1/data_models'
    
    print("Loading current data models...")
    entities_data = load_json(f'{base_path}/entities/entities.json')
    events_data = load_json(f'{base_path}/events/events.json')
    relations_data = load_json(f'{base_path}/relations/relations.json')
    timeline_data = load_json(f'{base_path}/timelines/timeline_enhanced.json')
    
    # Integrate findings
    print("\n1. Adding new entities...")
    entities_data = add_new_entities(entities_data)
    
    print("\n2. Adding new events...")
    events_data = add_new_events(events_data)
    
    print("\n3. Adding new relations...")
    relations_data = add_new_relations(relations_data)
    
    print("\n4. Updating timeline...")
    timeline_data = update_timeline(timeline_data, events_data)
    
    print("\n5. Updating metadata...")
    entities_data = update_metadata(entities_data, 'entities')
    events_data = update_metadata(events_data, 'events')
    relations_data = update_metadata(relations_data, 'relations')
    timeline_data = update_metadata(timeline_data, 'timeline')
    
    # Save updated data models
    print("\n6. Saving updated data models...")
    save_json(entities_data, f'{base_path}/entities/entities.json')
    save_json(events_data, f'{base_path}/events/events.json')
    save_json(relations_data, f'{base_path}/relations/relations.json')
    save_json(timeline_data, f'{base_path}/timelines/timeline_enhanced.json')
    
    print("\n" + "=" * 80)
    print("INTEGRATION SUMMARY")
    print("=" * 80)
    print(f"\nNew entities added: 3 (ORG_012, ORG_013, PERSON_012)")
    print(f"New events added: 3 (EVENT_H011, EVENT_H012, EVENT_064)")
    print(f"New relations added: 7")
    print(f"Timeline phases updated: 2 (PHASE_000, PHASE_006)")
    
    print("\n" + "=" * 80)
    print("INTEGRATION COMPLETE")
    print("=" * 80)
    
    print(f"\nUpdated files:")
    print(f"  - {base_path}/entities/entities.json")
    print(f"  - {base_path}/events/events.json")
    print(f"  - {base_path}/relations/relations.json")
    print(f"  - {base_path}/timelines/timeline_enhanced.json")

if __name__ == '__main__':
    main()
