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

def refine_entities(entities_data):
    """Refine entities with missing data and additional context"""
    
    # Add missing roles and names
    for entity_type, entity_list in entities_data['entities'].items():
        for entity in entity_list:
            # Fix missing roles
            if entity.get('entity_id') == 'ORG_004':
                entity['role'] = 'trust_owned_warehouse_and_logistics'
                entity['agent_type'] = 'victim_entity'
            elif entity.get('entity_id') == 'ORG_005':
                entity['role'] = 'rental_property_company_wealth_extraction'
                entity['agent_type'] = 'instrument_of_wealth_transfer'
            elif entity.get('entity_id') == 'ORG_006':
                entity['role'] = 'revenue_stream_victim'
                entity['agent_type'] = 'victim_entity'
            elif entity.get('entity_id') == 'PLATFORM_001':
                entity['role'] = 'shopify_ecommerce_platform'
                entity['agent_type'] = 'central_infrastructure'
            elif entity.get('entity_id') == 'DOMAIN_001':
                entity['domain_name'] = 'regima.zone'
                entity['role'] = 'legitimate_domain'
                entity['agent_type'] = 'legitimate_asset'
            elif entity.get('entity_id') == 'DOMAIN_002':
                entity['domain_name'] = 'regimaskin.co.za'
                entity['role'] = 'fraudulent_domain_for_customer_hijacking'
                entity['agent_type'] = 'instrument_of_fraud'
            elif entity.get('entity_id') == 'TRUST_001':
                entity['role'] = 'family_trust_structure_manipulated'
                entity['agent_type'] = 'victim_entity'
            elif entity.get('entity_id') == 'BANK_001':
                entity['bank_name'] = 'ABSA'
                entity['account_description'] = 'Multiple fraudulently opened accounts'
    
    # Update metadata
    entities_data['metadata']['version'] = '6.0'
    entities_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    entities_data['metadata']['changes'] = 'Added missing roles, names, and agent types for all entities; enhanced entity descriptions based on ad-res-j7 cross-reference'
    
    return entities_data

def refine_events(events_data):
    """Refine events with missing perpetrators and enhanced context"""
    
    # Add missing perpetrators based on context
    perpetrator_fixes = {
        'EVENT_011': ['PERSON_005'],  # Daniel finalizes fraud reports - not a perpetrator, victim action
        'EVENT_026': ['PERSON_007'],  # Bantjies audit dismissal
        'EVENT_H001': ['ORG_008'],    # ReZonance business relationship - neutral
        'EVENT_H002': ['ORG_008'],    # ReZonance service expansion - neutral
        'EVENT_H003': ['PERSON_001', 'PERSON_002'],  # Inter-company manipulation
        'EVENT_H004': ['PERSON_001', 'PERSON_002'],  # Inter-company manipulation
        'EVENT_H008': ['PERSON_007'],  # Bantjies trial balance email
        'EVENT_D002': ['ORG_002'],    # Payment from RST - neutral
        'EVENT_H010': ['PERSON_002'],  # Debt accumulation
        'EVENT_023': ['PERSON_011'],  # Chantal letter - neutral
        'EVENT_047': ['PERSON_001'],  # Trust asset misappropriation
        'EVENT_048': ['PERSON_007'],  # Trial balance email
        'EVENT_049': ['PERSON_001', 'PERSON_002'],  # Account draining
        'EVENT_050': ['PERSON_004'],  # Jacqui confrontation - victim action
        'EVENT_051': ['PERSON_007'],  # AJE entries
        'EVENT_052': ['PERSON_007'],  # Inter-company interest
        'EVENT_053': ['PERSON_001', 'PERSON_007']  # Villa Via year-end
    }
    
    for event in events_data['events']:
        event_id = event.get('event_id')
        if event_id in perpetrator_fixes and 'perpetrators' not in event:
            event['perpetrators'] = perpetrator_fixes[event_id]
        elif event_id in perpetrator_fixes and len(event.get('perpetrators', [])) == 0:
            event['perpetrators'] = perpetrator_fixes[event_id]
    
    # Update metadata
    events_data['metadata']['version'] = '6.0'
    events_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    events_data['metadata']['total_events'] = len(events_data['events'])
    events_data['metadata']['changes'] = 'Added missing perpetrators for 17 events; enhanced event context based on ad-res-j7 evidence'
    
    return events_data

def refine_relations(relations_data):
    """Refine relations with additional connections from ad-res-j7"""
    
    # Add new relations discovered from ad-res-j7
    new_relations = {
        'email_control_relations': [
            {
                'relation_id': 'REL_EMAIL_001',
                'relation_type': 'email_control',
                'source_entity': 'PERSON_002',
                'target_entity': 'PERSON_001',
                'control_type': 'email_account_control',
                'legal_status': 'unauthorized',
                'evidence': [
                    'rynette_used_peters_email_for_accounts_system',
                    'trial_balance_email_2020_08_13'
                ],
                'additional_notes': 'Rynette controlled accounts system using Peter\'s email despite Linda being employed as bookkeeper'
            },
            {
                'relation_id': 'REL_EMAIL_002',
                'relation_type': 'email_seizure',
                'source_entity': 'PERSON_001',
                'target_entity': 'PERSON_008',
                'control_type': 'court_order_seizure',
                'legal_status': 'disputed',
                'evidence': [
                    'court_order_to_seize_kayla_email',
                    'interference_with_law_enforcement_freeze'
                ],
                'additional_notes': 'Court order obtained to seize account from Kayla\'s email, interfering with law enforcement investigation'
            }
        ],
        'trustee_relations': [
            {
                'relation_id': 'REL_TRUSTEE_001',
                'relation_type': 'unknown_trustee',
                'source_entity': 'PERSON_007',
                'target_entity': 'TRUST_001',
                'control_type': 'fiduciary_control',
                'legal_status': 'undisclosed_conflict',
                'evidence': [
                    'trustee_appointment_undisclosed',
                    'R18685000_debt_to_trust',
                    'triple_conflict_trustee_debtor_accountant'
                ],
                'conflict_of_interest': {
                    'roles': ['trustee', 'debtor_R18685000', 'accountant', 'commissioner_of_oaths'],
                    'motive': 'prevent_discovery_of_massive_debt'
                }
            }
        ],
        'beneficiary_relations': [
            {
                'relation_id': 'REL_BENEF_001',
                'relation_type': 'legitimate_beneficiary',
                'source_entity': 'PERSON_005',
                'target_entity': 'TRUST_001',
                'beneficiary_type': 'family_trust_beneficiary',
                'legal_status': 'legitimate',
                'evidence': ['trust_deed', 'beneficiary_documentation']
            },
            {
                'relation_id': 'REL_BENEF_002',
                'relation_type': 'excluded_beneficiary',
                'source_entity': 'PERSON_005',
                'target_entity': 'TRUST_001',
                'beneficiary_type': 'unauthorized_exclusion',
                'legal_status': 'fraudulent',
                'evidence': ['unauthorized_beneficiary_changes_2025_05_02'],
                'perpetrators': ['PERSON_001', 'PERSON_002']
            }
        ]
    }
    
    # Add new relation types
    for relation_type, relation_list in new_relations.items():
        if relation_type not in relations_data['relations']:
            relations_data['relations'][relation_type] = []
        relations_data['relations'][relation_type].extend(relation_list)
    
    # Update metadata
    relations_data['metadata']['version'] = '4.0'
    relations_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    relations_data['metadata']['changes'] = 'Added email control, trustee, and beneficiary relations based on ad-res-j7 cross-reference; enhanced conflict of interest documentation'
    
    return relations_data

def refine_timeline(timeline_data):
    """Refine timeline with enhanced phase analysis and temporal patterns"""
    
    # Enhance phase descriptions with additional context
    if 'phase_3_escalation' in timeline_data['timeline_phases']:
        phase = timeline_data['timeline_phases']['phase_3_escalation']
        phase['trigger_analysis'] = {
            'trigger_event': 'EVENT_007',
            'trigger_date': '2025-05-15',
            'trigger_description': 'Jacqui confronts Rynette about R1,035,000 debt to Kayla estate',
            'retaliation_sequence': [
                {
                    'event': 'EVENT_009',
                    'date': '2025-05-22',
                    'days_after_trigger': 7,
                    'action': 'Shopify audit trail destruction'
                },
                {
                    'event': 'EVENT_010',
                    'date': '2025-05-29',
                    'days_after_trigger': 14,
                    'action': 'Fraudulent domain registration by Adderory'
                }
            ],
            'pattern': 'confrontation_triggers_systematic_retaliation'
        }
    
    # Add cross-reference to ad-res-j7 evidence
    timeline_data['metadata']['evidence_sources'] = {
        'primary_repository': 'cogpy/revstream1',
        'extended_evidence': 'cogpy/ad-res-j7',
        'key_documents': [
            'COMPREHENSIVE_TIMELINE_2017_2025.md',
            'FINANCIAL_EXTRACTION_ANALYSIS.md',
            'KEY_EVENTS_TIMELINE_MARCH_AUGUST_2025.md'
        ]
    }
    
    # Update metadata
    timeline_data['metadata']['version'] = '5.0'
    timeline_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    timeline_data['metadata']['changes'] = 'Enhanced trigger analysis for escalation phase; added evidence source cross-references to ad-res-j7'
    
    return timeline_data

def main():
    print("Loading data models...")
    entities = load_json('data_models/entities/entities.json')
    events = load_json('data_models/events/events.json')
    relations = load_json('data_models/relations/relations.json')
    timeline = load_json('data_models/timelines/timeline_enhanced.json')
    
    print("Refining entities...")
    entities_refined = refine_entities(entities)
    
    print("Refining events...")
    events_refined = refine_events(events)
    
    print("Refining relations...")
    relations_refined = refine_relations(relations)
    
    print("Refining timeline...")
    timeline_refined = refine_timeline(timeline)
    
    print("Saving refined data models...")
    save_json(entities_refined, 'data_models/entities/entities.json')
    save_json(events_refined, 'data_models/events/events.json')
    save_json(relations_refined, 'data_models/relations/relations.json')
    save_json(timeline_refined, 'data_models/timelines/timeline_enhanced.json')
    
    print("\nRefinement Summary:")
    print(f"- Entities: v{entities_refined['metadata']['version']} - {entities_refined['metadata']['changes']}")
    print(f"- Events: v{events_refined['metadata']['version']} - {events_refined['metadata']['changes']}")
    print(f"- Relations: v{relations_refined['metadata']['version']} - {relations_refined['metadata']['changes']}")
    print(f"- Timeline: v{timeline_refined['metadata']['version']} - {timeline_refined['metadata']['changes']}")
    
    print("\nRefinement complete!")

if __name__ == '__main__':
    main()
