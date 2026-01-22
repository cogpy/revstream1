#!/usr/bin/env python3
"""
Fix Remaining Entity-Relation Model Issues
Second pass after initial fixes
"""

import json
from datetime import datetime

def load_data():
    with open('data_models/entities/entities.json', 'r') as f:
        entities = json.load(f)
    with open('data_models/relations/relations.json', 'r') as f:
        relations = json.load(f)
    with open('data_models/events/events.json', 'r') as f:
        events = json.load(f)
    with open('data_models/timelines/timeline.json', 'r') as f:
        timeline = json.load(f)
    return entities, relations, events, timeline

def save_data(entities, relations, events, timeline):
    with open('data_models/entities/entities.json', 'w') as f:
        json.dump(entities, f, indent=2)
    with open('data_models/relations/relations.json', 'w') as f:
        json.dump(relations, f, indent=2)
    with open('data_models/events/events.json', 'w') as f:
        json.dump(events, f, indent=2)
    with open('data_models/timelines/timeline.json', 'w') as f:
        json.dump(timeline, f, indent=2)

def add_abstract_entities(entities):
    """Add abstract/system entities referenced in relations"""
    fixes = []
    
    abstract_entities = [
        {"entity_id": "SYS_BANK_ACCOUNTS", "name": "Bank Accounts", "type": "system", "description": "Banking system accounts"},
        {"entity_id": "SYS_ACCOUNTS", "name": "Accounting System", "type": "system", "description": "Financial accounting records"},
        {"entity_id": "SYS_STOCK", "name": "Stock/Inventory", "type": "system", "description": "Physical inventory and stock"},
        {"entity_id": "SYS_REGIMA_GROUP", "name": "RegimA Group", "type": "system", "description": "Collective RegimA company group"},
        {"entity_id": "SYS_FINANCIAL_RECORDS", "name": "Financial Records", "type": "system", "description": "Financial documentation"},
    ]
    
    existing_ids = {o.get('entity_id') for o in entities['entities'].get('organizations', [])}
    
    for entity in abstract_entities:
        if entity['entity_id'] not in existing_ids:
            entities['entities']['organizations'].append(entity)
            fixes.append(f"Added abstract entity: {entity['entity_id']}")
    
    return fixes

def add_missing_events_from_timeline(events, timeline):
    """Add events referenced in timeline but not in events list"""
    fixes = []
    
    event_ids = {e.get('event_id') for e in events.get('events', [])}
    
    # Events to add based on timeline references
    missing_events = [
        {"event_id": "EVENT_REG_20000531", "title": "Company Registration 2000-05-31", "date": "2000-05-31", "category": "company_registration"},
        {"event_id": "EVENT_REG_20050929", "title": "Company Registration 2005-09-29", "date": "2005-09-29", "category": "company_registration"},
        {"event_id": "EVENT_REG_20060316", "title": "Company Registration 2006-03-16", "date": "2006-03-16", "category": "company_registration"},
        {"event_id": "EVENT_PROP_20060605", "title": "Property Transaction 2006-06-05", "date": "2006-06-05", "category": "property_transaction"},
        {"event_id": "EVENT_DIR_20070717", "title": "Directorship Change 2007-07-17", "date": "2007-07-17", "category": "directorship_change"},
        {"event_id": "EVENT_REG_20150708", "title": "Company Registration 2015-07-08", "date": "2015-07-08", "category": "company_registration"},
        {"event_id": "EVENT_DIR_20160705", "title": "Directorship Change 2016-07-05", "date": "2016-07-05", "category": "directorship_change"},
        {"event_id": "EVENT_REG_20170927", "title": "Company Registration 2017-09-27", "date": "2017-09-27", "category": "company_registration"},
        {"event_id": "EVENT_BOND_20191122", "title": "Bond Registration 2019-11-22", "date": "2019-11-22", "category": "bond_registration"},
        {"event_id": "EVENT_GEE_DOMAIN_SWITCH_EMAIL", "title": "Gee Email Domain Switch Instruction", "date": "2025-08-15", "description": "Email from Gee explaining she was instructed to send domain switch communication", "category": "digital_fraud"},
        {"event_id": "diversion_started_2025_03_01", "title": "RegimA SA Revenue Diversion Started", "date": "2025-03-01", "description": "Beginning of revenue diversion from RegimA SA", "category": "revenue_hijacking"},
        {"event_id": "first_invoice_2017_06_30", "title": "First ReZonance Invoice", "date": "2017-06-30", "description": "First invoice from ReZonance to RegimA Skin Treatments", "category": "general"},
        {"event_id": "service_expansion_2017_09_30", "title": "ReZonance Service Expansion", "date": "2017-09-30", "description": "Major service expansion with multiple enterprise services", "category": "general"},
        {"event_id": "debt_accumulation_2022_03_01", "title": "ReZonance Debt Accumulation", "date": "2022-03-01", "description": "Opening balance showing substantial accumulated debt to ReZonance", "category": "revenue_hijacking"},
        {"event_id": "false_payment_claims_2023", "title": "False Payment Claims to ReZonance", "date": "2023-04-01", "description": "RegimA claims payment not reflected in ReZonance records", "category": "criminal_activity"},
        {"event_id": "jax_confrontation_2025_05_15", "title": "Jax Confronts Rynette About Debt", "date": "2025-05-15", "description": "Jacqui confronts Rynette about R1,035,000 debt to ReZonance", "category": "revenue_hijacking"},
    ]
    
    for event in missing_events:
        if event['event_id'] not in event_ids:
            events['events'].append(event)
            fixes.append(f"Added event: {event['event_id']}")
    
    return fixes

def normalize_remaining_actors(timeline):
    """Normalize remaining actor references"""
    fixes = []
    
    actor_map = {
        'PERSON_004': 'Jacqueline Faucitt',
        'PERSON_007': 'Peter Andrew Faucitt',
        'PERSON_003': 'Rynette Farrar',
        'Daniel Faucitt': 'Daniel James Faucitt',
        'Jacqui Faucitt': 'Jacqueline Faucitt',
        'Villa Via shareholders': 'Villa Via Members',
        'beneficiaries': 'FFT Beneficiaries',
        'coordinated_action': 'Coordinated Action',
        'Kevin Derrick': 'Kevin Derrick',
        'Daniel Jacobus Bantjies': 'Daniel Jacobus Bantjies',
    }
    
    for entry in timeline.get('timeline', []):
        actors = entry.get('actors', [])
        new_actors = []
        for actor in actors:
            if actor in actor_map:
                new_actors.append(actor_map[actor])
                if actor != actor_map[actor]:
                    fixes.append(f"Normalized '{actor}' -> '{actor_map[actor]}'")
            else:
                new_actors.append(actor)
        entry['actors'] = new_actors
    
    return fixes

def fix_relation_abstract_refs(relations):
    """Fix relations referencing abstract concepts"""
    fixes = []
    
    ref_map = {
        'bank_accounts': 'SYS_BANK_ACCOUNTS',
        'accounts': 'SYS_ACCOUNTS',
        'stock': 'SYS_STOCK',
        'regima_group': 'SYS_REGIMA_GROUP',
        'financial_records': 'SYS_FINANCIAL_RECORDS',
        'coordinated_action': 'PERSON_001',  # Peter as coordinator
        'coordinated_network': 'PERSON_002',  # Rynette as network
        'payment_redirection_scheme': 'PERSON_002',
        'trust_structure_establishment': 'TRUST_001',
        'bank_account_change': 'SYS_BANK_ACCOUNTS',
    }
    
    for category, rel_list in relations.get('relations', {}).items():
        if not isinstance(rel_list, list):
            continue
        for rel in rel_list:
            if not isinstance(rel, dict):
                continue
            
            source = rel.get('source_entity')
            target = rel.get('target_entity')
            
            if source in ref_map:
                rel['source_entity'] = ref_map[source]
                fixes.append(f"Fixed source '{source}' -> '{ref_map[source]}'")
            
            if target in ref_map:
                rel['target_entity'] = ref_map[target]
                fixes.append(f"Fixed target '{target}' -> '{ref_map[target]}'")
    
    return fixes

def update_metadata(entities, relations, events, timeline):
    timestamp = datetime.now().isoformat()
    
    entities['metadata']['version'] = "34.0_FINAL_REFINED_2026_01_22"
    entities['metadata']['last_updated'] = timestamp
    
    relations['metadata']['version'] = "34.0_FINAL_REFINED_2026_01_22"
    relations['metadata']['last_updated'] = timestamp
    
    events['metadata']['version'] = "29.0_FINAL_REFINED_2026_01_22"
    events['metadata']['last_updated'] = timestamp
    
    timeline['metadata']['version'] = "29.0_FINAL_REFINED_2026_01_22"
    timeline['metadata']['last_updated'] = timestamp
    
    # Update counts
    person_count = len(entities['entities'].get('persons', []))
    org_count = len(entities['entities'].get('organizations', []))
    entities['metadata']['total_entities'] = person_count + org_count
    entities['metadata']['total_persons'] = person_count
    entities['metadata']['total_organizations'] = org_count

def main():
    print("=" * 80)
    print("REMAINING ISSUES FIX SCRIPT")
    print(f"Date: {datetime.now().isoformat()}")
    print("=" * 80)
    
    entities, relations, events, timeline = load_data()
    all_fixes = []
    
    print("\n=== Adding abstract entities ===")
    fixes = add_abstract_entities(entities)
    all_fixes.extend(fixes)
    for f in fixes:
        print(f"  ✓ {f}")
    
    print("\n=== Adding missing events from timeline ===")
    fixes = add_missing_events_from_timeline(events, timeline)
    all_fixes.extend(fixes)
    for f in fixes[:10]:
        print(f"  ✓ {f}")
    if len(fixes) > 10:
        print(f"  ... and {len(fixes) - 10} more")
    
    print("\n=== Normalizing remaining actors ===")
    fixes = normalize_remaining_actors(timeline)
    all_fixes.extend(fixes)
    unique_fixes = list(set(fixes))
    for f in unique_fixes[:10]:
        print(f"  ✓ {f}")
    if len(unique_fixes) > 10:
        print(f"  ... and {len(unique_fixes) - 10} more")
    
    print("\n=== Fixing abstract relation references ===")
    fixes = fix_relation_abstract_refs(relations)
    all_fixes.extend(fixes)
    unique_fixes = list(set(fixes))
    for f in unique_fixes[:10]:
        print(f"  ✓ {f}")
    if len(unique_fixes) > 10:
        print(f"  ... and {len(unique_fixes) - 10} more")
    
    print("\n=== Updating metadata ===")
    update_metadata(entities, relations, events, timeline)
    print("  ✓ Updated all metadata to FINAL_REFINED versions")
    
    print("\n=== Saving data ===")
    save_data(entities, relations, events, timeline)
    print("  ✓ All data models saved")
    
    print("\n" + "=" * 80)
    print(f"FIX COMPLETE: {len(all_fixes)} fixes applied")
    print("=" * 80)

if __name__ == '__main__':
    main()
