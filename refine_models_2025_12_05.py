#!/usr/bin/env python3.11
"""
Refine entities, relations, events, and timelines based on cross-reference analysis
Version: 25.0 (entities), 27.0 (events), 21.0 (relations)
Date: 2025-12-05
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def backup_file(filepath):
    """Create backup of file"""
    backup_path = Path(str(filepath) + '.backup_2025_12_05')
    shutil.copy(filepath, backup_path)
    print(f"  Backup created: {backup_path.name}")

def refine_entities(entities_data, cross_ref_report):
    """Refine entities based on cross-reference analysis"""
    print("\n" + "="*80)
    print("REFINING ENTITIES")
    print("="*80)
    
    # Update metadata
    entities_data['metadata']['version'] = '25.0'
    entities_data['metadata']['last_updated'] = '2025-12-05'
    entities_data['metadata']['changes'] = 'Linked bank accounts to events, enhanced evidence references (2025-12-05)'
    
    # Link bank accounts to relevant events
    bank_accounts = entities_data['entities'].get('bank_accounts', [])
    
    # Events related to bank accounts
    bank_related_events = [
        'EVENT_001',  # Payment redirection scheme
        'EVENT_004',  # Bank account change letter
        'EVENT_005',  # Unauthorized beneficiary changes
        'EVENT_012',  # Secret card cancellations
        'EVENT_014',  # Coordinated fund diversions
        'EVENT_022',  # R900,000 unauthorized transfers
        'EVENT_027',  # Account emptying
    ]
    
    for account in bank_accounts:
        account_id = account.get('entity_id')
        
        # Add timeline events if not present
        if 'timeline_events' not in account or not account['timeline_events']:
            account['timeline_events'] = bank_related_events
            print(f"  Linked {len(bank_related_events)} events to {account_id}")
        
        # Add evidence files from ad-res-j7
        if 'evidence_files' not in account or not account['evidence_files']:
            account['evidence_files'] = [
                'ANNEXURES/JF04/D_FAUCITT_PERSONAL_BANK_RECORDS_20250604.pdf',
                'ANNEXURES/JF04/D_FAUCITT_PERSONAL_BANK_RECORDS_20250704.pdf',
                'ANNEXURES/JF04/D_FAUCITT_PERSONAL_BANK_RECORDS_20250804.pdf',
                'evidence/bank-statements/regima-sa/',
                'evidence/bank_records/'
            ]
            print(f"  Added evidence files to {account_id}")
        
        # Add evidence URLs
        if 'evidence_urls' not in account or not account['evidence_urls']:
            account['evidence_urls'] = [
                'https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF04',
                'https://github.com/cogpy/ad-res-j7/tree/main/evidence/bank-statements',
                'https://github.com/cogpy/ad-res-j7/tree/main/evidence/bank_records'
            ]
    
    print(f"\n  Updated {len(bank_accounts)} bank account entities")
    
    return entities_data

def refine_events(events_data, cross_ref_report):
    """Refine events based on cross-reference analysis"""
    print("\n" + "="*80)
    print("REFINING EVENTS")
    print("="*80)
    
    # Update metadata
    events_data['metadata']['version'] = '27.0'
    events_data['metadata']['last_updated'] = '2025-12-05'
    events_data['metadata']['changes'] = 'Assigned phases to unassigned events, enhanced evidence links (2025-12-05)'
    
    events = events_data.get('events', [])
    
    # Phase assignments for unassigned events
    phase_assignments = {
        'EVENT_023': 'PHASE_000',  # Historical - Kayla estate
        'EVENT_054': 'PHASE_000',  # Historical - Kayla estate
        'EVENT_022': 'PHASE_002',  # Feb 2025 - Initial theft phase
        'EVENT_028': 'PHASE_002',  # Feb 2025 - Initial theft phase
        'EVT-063': 'PHASE_004',    # Jun 2025 - Consolidation phase
        'EVT-064': 'PHASE_004',    # Jun 2025 - Consolidation phase
        'EVT-065': 'PHASE_005',    # Jul 2025 - Control seizure phase
        'EVT-066': 'PHASE_005',    # Jul 2025 - Control seizure phase
        'EVT-067': 'PHASE_006',    # Aug 2025 - Cover-up phase
        'EVT-068': 'PHASE_000',    # Historical - 2024
    }
    
    updated_count = 0
    for event in events:
        event_id = event.get('event_id')
        
        # Assign phase if unassigned
        if event_id in phase_assignments:
            current_phase = event.get('timeline_phase', 'UNASSIGNED')
            if current_phase == 'UNASSIGNED' or 'UNASSIGNED' in current_phase:
                event['timeline_phase'] = phase_assignments[event_id]
                updated_count += 1
                print(f"  Assigned {event_id} to {phase_assignments[event_id]}")
        
        # Enhance bank-related events with bank account entities
        if event_id in ['EVENT_001', 'EVENT_004', 'EVENT_005', 'EVENT_012', 'EVENT_014', 'EVENT_022', 'EVENT_027']:
            entities_involved = event.get('entities_involved', [])
            if 'BANK_ACCOUNT_001' not in entities_involved:
                entities_involved.append('BANK_ACCOUNT_001')
                event['entities_involved'] = entities_involved
    
    print(f"\n  Assigned phases to {updated_count} events")
    print(f"  Enhanced entity links for bank-related events")
    
    return events_data

def refine_relations(relations_data, cross_ref_report):
    """Refine relations based on cross-reference analysis"""
    print("\n" + "="*80)
    print("REFINING RELATIONS")
    print("="*80)
    
    # Update metadata
    relations_data['metadata']['version'] = '21.0'
    relations_data['metadata']['last_updated'] = '2025-12-05'
    relations_data['metadata']['changes'] = 'Added bank account control relations, enhanced evidence links (2025-12-05)'
    
    relations = relations_data.get('relations', {})
    
    # Add bank account control relations if not present
    control_relations = relations.get('control_relations', [])
    
    new_relations = [
        {
            'relation_id': 'REL_CTRL_009',
            'relation_type': 'controls_bank_account',
            'source_entity': 'PERSON_002',  # Rynette
            'target_entity': 'BANK_ACCOUNT_001',
            'strength': 'unauthorized_control',
            'legal_status': 'fraudulent',
            'evidence': [
                'bank_account_change_letter',
                'unauthorized_beneficiary_changes'
            ],
            'ad_res_j7_references': [
                'Evidence in ANNEXURES/JF04',
                'Bank statement evidence',
                'Payment redirection documentation'
            ]
        },
        {
            'relation_id': 'REL_CTRL_010',
            'relation_type': 'controls_bank_account',
            'source_entity': 'PERSON_001',  # Peter
            'target_entity': 'BANK_ACCOUNT_002',
            'strength': 'unauthorized_control',
            'legal_status': 'fraudulent',
            'evidence': [
                'trust_account_manipulation',
                'unauthorized_transfers'
            ],
            'ad_res_j7_references': [
                'Trust account evidence',
                'Transfer documentation'
            ]
        }
    ]
    
    # Check if relations already exist
    existing_ids = [r.get('relation_id') for r in control_relations]
    added_count = 0
    
    for new_rel in new_relations:
        if new_rel['relation_id'] not in existing_ids:
            control_relations.append(new_rel)
            added_count += 1
            print(f"  Added {new_rel['relation_id']}: {new_rel['source_entity']} -> {new_rel['target_entity']}")
    
    relations['control_relations'] = control_relations
    
    print(f"\n  Added {added_count} new control relations")
    
    return relations_data

def update_timeline(events_data):
    """Update timeline based on refined events"""
    print("\n" + "="*80)
    print("UPDATING TIMELINE")
    print("="*80)
    
    events = events_data.get('events', [])
    
    # Sort events by date
    sorted_events = sorted(events, key=lambda x: x.get('date', '9999-99-99'))
    
    # Create timeline entries
    timeline_entries = []
    for event in sorted_events:
        entry = {
            'event_id': event.get('event_id'),
            'date': event.get('date'),
            'title': event.get('title'),
            'phase': event.get('timeline_phase', 'UNASSIGNED'),
            'category': event.get('category'),
            'financial_impact': event.get('financial_impact'),
            'entities_involved': event.get('entities_involved', []),
            'evidence_files': event.get('evidence_files', [])
        }
        timeline_entries.append(entry)
    
    timeline_data = {
        'metadata': {
            'version': '18.0',
            'created_date': '2025-11-10',
            'description': 'Enhanced timeline for Revenue Stream Hijacking case 2025-137857',
            'case_number': '2025-137857',
            'last_updated': '2025-12-05',
            'changes': 'Updated with refined phase assignments and entity links (2025-12-05)',
            'total_entries': len(timeline_entries)
        },
        'timeline': timeline_entries
    }
    
    print(f"  Created timeline with {len(timeline_entries)} entries")
    
    return timeline_data

def generate_refinement_summary(entities_data, events_data, relations_data, timeline_data):
    """Generate summary of refinements"""
    print("\n" + "="*80)
    print("REFINEMENT SUMMARY")
    print("="*80)
    
    summary = {
        'refinement_date': '2025-12-05',
        'entities': {
            'version': entities_data['metadata']['version'],
            'total_entities': entities_data['metadata']['total_entities'],
            'changes': entities_data['metadata']['changes']
        },
        'events': {
            'version': events_data['metadata']['version'],
            'total_events': events_data['metadata']['total_events'],
            'changes': events_data['metadata']['changes']
        },
        'relations': {
            'version': relations_data['metadata']['version'],
            'changes': relations_data['metadata']['changes']
        },
        'timeline': {
            'version': timeline_data['metadata']['version'],
            'total_entries': timeline_data['metadata']['total_entries'],
            'changes': timeline_data['metadata']['changes']
        }
    }
    
    print(f"\n  Entities: v{summary['entities']['version']} - {summary['entities']['total_entities']} entities")
    print(f"  Events: v{summary['events']['version']} - {summary['events']['total_events']} events")
    print(f"  Relations: v{summary['relations']['version']}")
    print(f"  Timeline: v{summary['timeline']['version']} - {summary['timeline']['total_entries']} entries")
    
    return summary

def main():
    """Main refinement function"""
    base_path = Path('/home/ubuntu/revstream1')
    
    # Load current models
    entities_path = base_path / 'data_models/entities/entities_refined_2025_12_04_v24.json'
    events_path = base_path / 'data_models/events/events_refined_2025_12_04_v26.json'
    relations_path = base_path / 'data_models/relations/relations_refined_2025_11_28_v20.json'
    cross_ref_path = base_path / 'CROSS_REFERENCE_ANALYSIS_2025_12_05.json'
    
    print("="*80)
    print("MODEL REFINEMENT PROCESS")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("="*80)
    print(f"\nRefinement Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create backups
    print("\n--- Creating Backups ---")
    backup_file(entities_path)
    backup_file(events_path)
    backup_file(relations_path)
    
    # Load data
    entities_data = load_json(entities_path)
    events_data = load_json(events_path)
    relations_data = load_json(relations_path)
    cross_ref_report = load_json(cross_ref_path)
    
    # Refine models
    entities_data = refine_entities(entities_data, cross_ref_report)
    events_data = refine_events(events_data, cross_ref_report)
    relations_data = refine_relations(relations_data, cross_ref_report)
    timeline_data = update_timeline(events_data)
    
    # Save refined models
    print("\n--- Saving Refined Models ---")
    
    entities_new_path = base_path / 'data_models/entities/entities_refined_2025_12_05_v25.json'
    events_new_path = base_path / 'data_models/events/events_refined_2025_12_05_v27.json'
    relations_new_path = base_path / 'data_models/relations/relations_refined_2025_12_05_v21.json'
    timeline_new_path = base_path / 'data_models/timelines/timeline_refined_2025_12_05_v18.json'
    
    save_json(entities_data, entities_new_path)
    print(f"  Saved: {entities_new_path.name}")
    
    save_json(events_data, events_new_path)
    print(f"  Saved: {events_new_path.name}")
    
    save_json(relations_data, relations_new_path)
    print(f"  Saved: {relations_new_path.name}")
    
    save_json(timeline_data, timeline_new_path)
    print(f"  Saved: {timeline_new_path.name}")
    
    # Generate summary
    summary = generate_refinement_summary(entities_data, events_data, relations_data, timeline_data)
    
    summary_path = base_path / 'REFINEMENT_SUMMARY_2025_12_05.json'
    save_json(summary, summary_path)
    print(f"\n  Summary saved: {summary_path.name}")
    
    print("\n" + "="*80)
    print("REFINEMENT COMPLETE")
    print("="*80)

if __name__ == '__main__':
    main()
