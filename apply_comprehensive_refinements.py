#!/usr/bin/env python3
"""
Apply comprehensive refinements to entities, relations, events, and timelines
based on analysis findings and ad-res-j7 evidence repository.
"""

import json
from datetime import datetime

def load_json(filepath):
    """Load JSON file safely."""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with proper formatting."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved: {filepath}")

def refine_entities(entities_data):
    """Add missing evidence_files and ad_res_j7_references to entities."""
    print("\n" + "="*80)
    print("REFINING ENTITIES")
    print("="*80)
    
    # Evidence mappings for persons
    person_evidence_map = {
        'PERSON_004': {  # Jacqueline Faucitt
            'evidence_files': [
                'ANNEXURES/JF01/correspondence/',
                'ANNEXURES/JF02/shopify_operations/',
                'case_2025_137857/respondent_1/jacqueline_evidence/',
                'evidence/shopify/platform_operations/'
            ],
            'ad_res_j7_references': [
                'Shopify platform operational records',
                'RegimA Zone Ltd business operations',
                'Email correspondence as first respondent',
                'POPIA compliance documentation'
            ]
        },
        'PERSON_005': {  # Daniel James Faucitt
            'evidence_files': [
                'ANNEXURES/JF02/regima_zone_ltd/',
                'ANNEXURES/JF03/shopify_ownership/',
                'case_2025_137857/respondent_2/daniel_evidence/',
                'evidence/shopify/platform_ownership/',
                'evidence/popia/violation_notices/'
            ],
            'ad_res_j7_references': [
                'RegimA Zone Ltd ownership documentation',
                'Shopify platform payment records 28+ months',
                'POPIA violation notice July 8, 2025',
                'UK company registration and operations'
            ]
        },
        'PERSON_006': {  # Linda (bookkeeper)
            'evidence_files': [
                'ANNEXURES/JF05/accounting/bookkeeper_records/',
                'evidence/accounting/linda_bookkeeping/',
                'evidence/financial_manipulation/bookkeeper_role/'
            ],
            'ad_res_j7_references': [
                'Bookkeeping records while Rynette controlled accounts',
                'Employment documentation',
                'Accounting system access logs'
            ]
        }
    }
    
    # Organization evidence mappings
    org_evidence_map = {
        'ORG_001': {  # RWD ZA
            'evidence_files': [
                'ANNEXURES/JF01/rwd_za/',
                'evidence/cipc/rwd_za_registration/',
                'evidence/financial/rwd_za_accounts/',
                'case_2025_137857/entities/rwd_za/'
            ]
        },
        'ORG_002': {  # RegimA Skin Treatments
            'evidence_files': [
                'ANNEXURES/JF01/rst/',
                'evidence/accounting/rst_trial_balances/',
                'evidence/financial/rst_accounts/',
                'case_2025_137857/entities/rst/'
            ]
        },
        'ORG_003': {  # RegimA Zone Ltd (UK)
            'evidence_files': [
                'ANNEXURES/JF02/regima_zone_ltd/',
                'evidence/shopify/platform_ownership/',
                'evidence/uk_company/registration/',
                'case_2025_137857/entities/regima_zone_ltd/'
            ]
        },
        'ORG_004': {  # Strategic Logistics
            'evidence_files': [
                'ANNEXURES/JF01/slg/',
                'evidence/accounting/slg_trial_balances/',
                'evidence/financial/slg_accounts/',
                'case_2025_137857/entities/slg/'
            ]
        },
        'ORG_005': {  # Villa Via
            'evidence_files': [
                'ANNEXURES/JF01/villa_via/',
                'evidence/accounting/villa_via_trial_balances/',
                'evidence/financial/villa_via_accounts/',
                'case_2025_137857/entities/villa_via/'
            ]
        },
        'ORG_006': {  # Family Trust
            'evidence_files': [
                'ANNEXURES/JF01/trust_documents/',
                'evidence/trust_violations/trust_deed/',
                'evidence/trust_violations/trustee_misconduct/',
                'case_2025_137857/trust/family_trust/'
            ]
        },
        'ORG_008': {  # ReZonance
            'evidence_files': [
                'ANNEXURES/JF04/rezonance/',
                'evidence/rezonance/invoices/',
                'evidence/rezonance/payment_analysis/',
                'case_2025_137857/entities/rezonance/'
            ]
        },
        'ORG_009': {  # Unicorn
            'evidence_files': [
                'ANNEXURES/JF04/unicorn/',
                'evidence/payment_routing/unicorn/',
                'case_2025_137857/entities/unicorn/'
            ]
        },
        'ORG_010': {  # Joziway
            'evidence_files': [
                'ANNEXURES/JF04/joziway/',
                'evidence/payment_routing/joziway/',
                'case_2025_137857/entities/joziway/'
            ]
        }
    }
    
    # Apply refinements to persons
    if 'persons' in entities_data['entities']:
        for person in entities_data['entities']['persons']:
            entity_id = person.get('entity_id')
            if entity_id in person_evidence_map:
                person['evidence_files'] = person_evidence_map[entity_id]['evidence_files']
                person['ad_res_j7_references'] = person_evidence_map[entity_id]['ad_res_j7_references']
                person['evidence_repository'] = 'https://github.com/cogpy/ad-res-j7'
                print(f"  ✓ Updated {entity_id}")
    
    # Apply refinements to organizations
    if 'organizations' in entities_data['entities']:
        for org in entities_data['entities']['organizations']:
            entity_id = org.get('entity_id')
            if entity_id in org_evidence_map:
                org['evidence_files'] = org_evidence_map[entity_id]['evidence_files']
                org['evidence_repository'] = 'https://github.com/cogpy/ad-res-j7'
                print(f"  ✓ Updated {entity_id}")
    
    # Update metadata
    entities_data['metadata']['version'] = '12.0'
    entities_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    entities_data['metadata']['changes'] = 'Comprehensive refinement v12: Added all missing evidence_files and ad_res_j7_references'
    
    return entities_data

def refine_events(events_data):
    """Add missing application mappings to events."""
    print("\n" + "="*80)
    print("REFINING EVENTS")
    print("="*80)
    
    # Events missing application mappings
    event_app_map = {
        'EVENT_023': ['APPLICATION_1', 'APPLICATION_2'],  # ReZonance debt
        'EVENT_054': ['APPLICATION_1', 'APPLICATION_2'],  # Kayla estate
        'EVENT_022': ['APPLICATION_1'],  # Stock fraud
        'EVENT_028': ['APPLICATION_1'],  # Expense dumping
        'EVT-063': ['APPLICATION_2'],
        'EVT-064': ['APPLICATION_2'],
        'EVT-065': ['APPLICATION_2'],
        'EVT-066': ['APPLICATION_2'],
        'EVT-067': ['APPLICATION_2', 'APPLICATION_3'],
        'EVT-068': ['APPLICATION_2', 'APPLICATION_3'],
        'EVT-069': ['APPLICATION_3']
    }
    
    if 'events' in events_data:
        for event in events_data['events']:
            event_id = event.get('event_id')
            if event_id in event_app_map:
                event['related_applications'] = event_app_map[event_id]
                print(f"  ✓ Updated {event_id}: {event_app_map[event_id]}")
    
    # Update metadata
    events_data['metadata']['version'] = '12.0'
    events_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    events_data['metadata']['changes'] = 'Comprehensive refinement v12: Added all missing application mappings'
    
    return events_data

def refine_relations(relations_data):
    """Add missing application mappings to relations."""
    print("\n" + "="*80)
    print("REFINING RELATIONS")
    print("="*80)
    
    # Default application mappings for relation types
    default_apps = {
        'dependency_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'victim_perpetrator_relations': ['APPLICATION_1', 'APPLICATION_2', 'APPLICATION_3'],
        'employment_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'evidence_destruction_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'temporal_relations': ['APPLICATION_1', 'APPLICATION_2', 'APPLICATION_3'],
        'debt_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'estate_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'witness_relations': ['APPLICATION_1', 'APPLICATION_2', 'APPLICATION_3'],
        'conflict_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'email_control_relations': ['APPLICATION_1', 'APPLICATION_3'],
        'trustee_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'beneficiary_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'professional_correspondence_relations': ['APPLICATION_1', 'APPLICATION_2', 'APPLICATION_3'],
        'capital_extraction_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'inter_company_loan_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'knowledge_acquisition_relations': ['APPLICATION_1', 'APPLICATION_2'],
        'strategic_coordination_relations': ['APPLICATION_1', 'APPLICATION_2', 'APPLICATION_3'],
        'system_control_relations': ['APPLICATION_1', 'APPLICATION_3']
    }
    
    if 'relations' in relations_data:
        for rel_type, rel_list in relations_data['relations'].items():
            for rel in rel_list:
                if not rel.get('related_applications'):
                    if rel_type in default_apps:
                        rel['related_applications'] = default_apps[rel_type]
                        rel['evidence_repository'] = 'https://github.com/cogpy/ad-res-j7'
                        print(f"  ✓ Updated {rel.get('relation_id', 'UNKNOWN')} in {rel_type}")
    
    # Update metadata
    relations_data['metadata']['version'] = '10.0'
    relations_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    relations_data['metadata']['changes'] = 'Comprehensive refinement v10: Added all missing application mappings'
    
    return relations_data

def refine_timeline(timeline_data):
    """Add missing application mapping to PHASE_000."""
    print("\n" + "="*80)
    print("REFINING TIMELINE")
    print("="*80)
    
    if 'timeline_phases' in timeline_data:
        for phase_key, phase in timeline_data['timeline_phases'].items():
            if phase.get('phase_id') == 'PHASE_000':
                phase['related_applications'] = ['APPLICATION_1', 'APPLICATION_2']
                print(f"  ✓ Updated PHASE_000 with application mappings")
    
    # Update metadata
    timeline_data['metadata']['version'] = '11.0'
    timeline_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    timeline_data['metadata']['changes'] = 'Comprehensive refinement v11: Added missing PHASE_000 application mapping'
    
    return timeline_data

def main():
    """Main refinement function."""
    print("\n" + "="*80)
    print("COMPREHENSIVE DATA MODEL REFINEMENT")
    print("="*80)
    
    # Load current data models
    entities = load_json('data_models/entities/entities_refined_2025_11_19_v3.json')
    events = load_json('data_models/events/events_refined_2025_11_19_v3.json')
    relations = load_json('data_models/relations/relations_refined_2025_11_19_v3.json')
    timeline = load_json('data_models/timelines/timeline_refined_2025_11_19_v3.json')
    
    # Apply refinements
    entities_refined = refine_entities(entities)
    events_refined = refine_events(events)
    relations_refined = refine_relations(relations)
    timeline_refined = refine_timeline(timeline)
    
    # Save refined models
    save_json(entities_refined, 'data_models/entities/entities_refined_2025_11_19_v4.json')
    save_json(events_refined, 'data_models/events/events_refined_2025_11_19_v4.json')
    save_json(relations_refined, 'data_models/relations/relations_refined_2025_11_19_v4.json')
    save_json(timeline_refined, 'data_models/timelines/timeline_refined_2025_11_19_v4.json')
    
    print("\n" + "="*80)
    print("REFINEMENT COMPLETE")
    print("="*80)
    print("\nAll data models have been refined and saved as v4.")

if __name__ == '__main__':
    main()
