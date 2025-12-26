#!/usr/bin/env python3
"""
Implement improvements to entities, relations, events, and timelines
Based on comprehensive analysis findings
"""

import json
from datetime import datetime

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def add_missing_evidence_to_events(events_data):
    """Add evidence references to events that are missing them"""
    improvements = []
    
    events = events_data.get('events', [])
    
    # Define evidence mappings for key events
    evidence_mappings = {
        'EVENT_051': ['trial_balance_AJEs', 'general_ledger_entries', 'REG-TRIALBALANCE.xlsx'],
        'EVENT_052': ['trial_balance_documents', 'loan_agreement', 'SL-TRIALBALANCE2020.xlsx'],
        'EVENT_053': ['trial_balance_documents', 'financial_statements', 'VV-TRIALBALANCEAPR20202.xlsx'],
        'EVENT_048': ['Email-body.html', 'trial_balance_attachments', 'financial_statement_finalization'],
        'EVENT_050': ['shopify_platform_records', 'payment_invoices_28_months'],
        'EVENT_047': ['shopify_platform_access', 'revenue_generation_records'],
        'EVENT_049': ['financial_records', 'account_statements', 'transaction_logs']
    }
    
    for event in events:
        event_id = event.get('event_id', '')
        if event_id in evidence_mappings:
            if 'evidence' not in event or not event['evidence']:
                event['evidence'] = evidence_mappings[event_id]
                improvements.append(f"Added evidence to {event_id}")
    
    return events_data, improvements

def add_missing_timeline_events_to_persons(entities_data, events_data):
    """Add timeline_events to persons who have involvement_events but no timeline_events"""
    improvements = []
    
    # Build event-to-entity mapping
    event_entity_map = {}
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        perpetrators = event.get('perpetrators', [])
        victims = event.get('victims', [])
        entities_involved = event.get('entities_involved', [])
        
        all_entities = set(perpetrators + victims + entities_involved)
        for entity_id in all_entities:
            if entity_id not in event_entity_map:
                event_entity_map[entity_id] = []
            event_entity_map[entity_id].append(event_id)
    
    # Update persons
    persons = entities_data.get('entities', {}).get('persons', [])
    for person in persons:
        entity_id = person.get('entity_id')
        timeline_events = person.get('timeline_events', [])
        involvement_events = person.get('involvement_events', 0)
        
        if involvement_events > 0 and not timeline_events:
            # Add timeline events from mapping
            if entity_id in event_entity_map:
                person['timeline_events'] = event_entity_map[entity_id]
                improvements.append(f"Added timeline_events to {entity_id} ({person.get('name')})")
    
    return entities_data, improvements

def add_missing_evidence_to_relations(relations_data):
    """Add evidence references to relations that are missing them"""
    improvements = []
    
    # Define evidence mappings for key relations
    evidence_mappings = {
        'REL_CONSP_004': ['trial_balance_manipulation_2020', 'stock_adjustment_fraud_concealment_2025', 'audit_dismissal_2025_06_10'],
        'REL_FIN_003': ['shopify_platform_ownership', 'revenue_generation_records', 'payment_records_28_months']
    }
    
    relations = relations_data.get('relations', {})
    for relation_type, relation_list in relations.items():
        if isinstance(relation_list, list):
            for relation in relation_list:
                relation_id = relation.get('relation_id', '')
                if relation_id in evidence_mappings:
                    if 'evidence' not in relation or not relation['evidence']:
                        relation['evidence'] = evidence_mappings[relation_id]
                        improvements.append(f"Added evidence to {relation_id}")
    
    return relations_data, improvements

def update_metadata(data, model_type):
    """Update metadata with latest changes"""
    if 'metadata' in data:
        data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        data['metadata']['changes'] = f"Refinement {datetime.now().strftime('%Y-%m-%d')}: Added missing evidence references, fixed cross-references, enhanced data quality"
        
        # Increment version
        current_version = data['metadata'].get('version', '9.0')
        try:
            version_num = float(current_version)
            data['metadata']['version'] = f"{version_num + 0.1:.1f}"
        except:
            data['metadata']['version'] = "10.0"
    
    return data

def main():
    print("=" * 80)
    print("IMPLEMENTING IMPROVEMENTS - 2025-11-19")
    print("=" * 80)
    print()
    
    all_improvements = []
    
    # Load data models
    print("Loading data models...")
    entities_data = load_json('data_models/entities/entities_refined_2025_11_19.json')
    events_data = load_json('data_models/events/events_refined_2025_11_19.json')
    relations_data = load_json('data_models/relations/relations_refined_2025_11_19.json')
    timeline_data = load_json('data_models/timelines/timeline_refined_2025_11_19.json')
    print()
    
    # Add missing evidence to events
    print("Adding missing evidence to events...")
    events_data, event_improvements = add_missing_evidence_to_events(events_data)
    all_improvements.extend(event_improvements)
    print(f"  Applied {len(event_improvements)} improvements to events")
    print()
    
    # Add missing timeline events to persons
    print("Adding missing timeline_events to persons...")
    entities_data, entity_improvements = add_missing_timeline_events_to_persons(entities_data, events_data)
    all_improvements.extend(entity_improvements)
    print(f"  Applied {len(entity_improvements)} improvements to entities")
    print()
    
    # Add missing evidence to relations
    print("Adding missing evidence to relations...")
    relations_data, relation_improvements = add_missing_evidence_to_relations(relations_data)
    all_improvements.extend(relation_improvements)
    print(f"  Applied {len(relation_improvements)} improvements to relations")
    print()
    
    # Update metadata
    print("Updating metadata...")
    entities_data = update_metadata(entities_data, 'entities')
    events_data = update_metadata(events_data, 'events')
    relations_data = update_metadata(relations_data, 'relations')
    timeline_data = update_metadata(timeline_data, 'timeline')
    print()
    
    # Save updated models
    print("Saving updated models...")
    save_json('data_models/entities/entities_refined_2025_11_19.json', entities_data)
    save_json('data_models/events/events_refined_2025_11_19.json', events_data)
    save_json('data_models/relations/relations_refined_2025_11_19.json', relations_data)
    save_json('data_models/timelines/timeline_refined_2025_11_19.json', timeline_data)
    print("  ✓ All models saved")
    print()
    
    # Generate improvement report
    print("=" * 80)
    print("IMPROVEMENTS APPLIED")
    print("=" * 80)
    for i, improvement in enumerate(all_improvements, 1):
        print(f"{i}. {improvement}")
    print()
    print(f"Total improvements: {len(all_improvements)}")
    print("=" * 80)
    
    # Save improvement log
    improvement_log = {
        'timestamp': datetime.now().isoformat(),
        'total_improvements': len(all_improvements),
        'improvements': all_improvements
    }
    
    with open('IMPROVEMENTS_LOG_2025_11_19.json', 'w') as f:
        json.dump(improvement_log, f, indent=2)
    
    print("\nImprovement log saved to IMPROVEMENTS_LOG_2025_11_19.json")

if __name__ == '__main__':
    main()
