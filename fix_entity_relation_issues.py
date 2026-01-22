#!/usr/bin/env python3
"""
Fix Entity-Relation Model Issues
Based on audit findings from AUDIT_REPORT_2026_01_22.json
"""

import json
from datetime import datetime

def load_data():
    """Load all data models"""
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
    """Save all data models"""
    with open('data_models/entities/entities.json', 'w') as f:
        json.dump(entities, f, indent=2)
    with open('data_models/relations/relations.json', 'w') as f:
        json.dump(relations, f, indent=2)
    with open('data_models/events/events.json', 'w') as f:
        json.dump(events, f, indent=2)
    with open('data_models/timelines/timeline.json', 'w') as f:
        json.dump(timeline, f, indent=2)

def fix_duplicate_entities(entities):
    """Fix duplicate entity IDs and names"""
    fixes = []
    
    # Fix PERSON_012 duplicate (Jax vs Marisca Meyer)
    # Jax should be PERSON_012, Marisca Meyer needs new ID
    persons = entities['entities']['persons']
    
    # Find and fix Marisca Meyer
    for i, person in enumerate(persons):
        if person.get('name') == 'Marisca Meyer' and person.get('entity_id') == 'PERSON_012':
            person['entity_id'] = 'PERSON_039'  # New unique ID
            fixes.append(f"Changed Marisca Meyer from PERSON_012 to PERSON_039")
    
    # Fix Kayla Pretorius duplicate (PERSON_013 vs PERSON_024)
    # Keep PERSON_013, remove PERSON_024 or merge
    kayla_entries = [p for p in persons if p.get('name') == 'Kayla Pretorius']
    if len(kayla_entries) > 1:
        # Keep the one with more data, remove the other
        main_kayla = None
        for p in kayla_entries:
            if p.get('entity_id') == 'PERSON_013':
                main_kayla = p
        
        # Remove duplicate
        persons[:] = [p for p in persons if not (p.get('name') == 'Kayla Pretorius' and p.get('entity_id') == 'PERSON_024')]
        fixes.append("Removed duplicate Kayla Pretorius (PERSON_024), kept PERSON_013")
    
    # Fix Bernadine Wright duplicate (PERSON_010 vs PERSON_028)
    bernadine_entries = [p for p in persons if p.get('name') == 'Bernadine Wright']
    if len(bernadine_entries) > 1:
        persons[:] = [p for p in persons if not (p.get('name') == 'Bernadine Wright' and p.get('entity_id') == 'PERSON_028')]
        fixes.append("Removed duplicate Bernadine Wright (PERSON_028), kept PERSON_010")
    
    # Fix ORG_015 duplicate (SARS vs ALOECO)
    orgs = entities['entities']['organizations']
    for i, org in enumerate(orgs):
        if org.get('name') == 'ALOECO (SA)' and org.get('entity_id') == 'ORG_015':
            org['entity_id'] = 'ORG_042'  # New unique ID
            fixes.append("Changed ALOECO (SA) from ORG_015 to ORG_042")
    
    return fixes

def add_missing_entities(entities):
    """Add entities that are referenced but not defined"""
    fixes = []
    
    # Add missing platform entity
    platform_exists = any(
        org.get('entity_id') == 'PLATFORM_001' 
        for org in entities['entities'].get('organizations', [])
    )
    if not platform_exists:
        entities['entities']['organizations'].append({
            "entity_id": "PLATFORM_001",
            "name": "Shopify Plus Platform",
            "type": "platform",
            "description": "E-commerce platform used for RegimA online sales",
            "role": "sales_platform",
            "evidence": ["JF01 - Shopify Plus email evidence"]
        })
        fixes.append("Added PLATFORM_001 (Shopify Plus Platform)")
    
    # Add missing domain entities
    domain1_exists = any(
        org.get('entity_id') == 'DOMAIN_001' 
        for org in entities['entities'].get('organizations', [])
    )
    if not domain1_exists:
        entities['entities']['organizations'].append({
            "entity_id": "DOMAIN_001",
            "name": "regima.zone Domain",
            "type": "domain",
            "description": "Legitimate RegimA domain",
            "role": "legitimate_domain"
        })
        fixes.append("Added DOMAIN_001 (regima.zone Domain)")
    
    domain2_exists = any(
        org.get('entity_id') == 'DOMAIN_002' 
        for org in entities['entities'].get('organizations', [])
    )
    if not domain2_exists:
        entities['entities']['organizations'].append({
            "entity_id": "DOMAIN_002",
            "name": "regimaskin.co.za Domain",
            "type": "domain",
            "description": "Fraudulent domain registered by Adderory",
            "role": "fraudulent_domain",
            "registration_date": "2025-05-29"
        })
        fixes.append("Added DOMAIN_002 (regimaskin.co.za Domain)")
    
    # Add missing trust entity
    trust_exists = any(
        org.get('entity_id') == 'TRUST_001' 
        for org in entities['entities'].get('organizations', [])
    )
    if not trust_exists:
        entities['entities']['organizations'].append({
            "entity_id": "TRUST_001",
            "name": "Faucitt Family Trust",
            "type": "trust",
            "description": "Family trust with ZAR 18.75M Ketoni payout entitlement",
            "role": "central_asset_holder",
            "ketoni_investment": {
                "amount": "ZAR 18.75M",
                "payout_date": "2026-05"
            }
        })
        fixes.append("Added TRUST_001 (Faucitt Family Trust)")
    
    # Add Daniel Jacobus Bantjies if not exists
    bantjies_exists = any(
        p.get('name') == 'Daniel Jacobus Bantjies' or p.get('name') == 'Danie Bantjies'
        for p in entities['entities'].get('persons', [])
    )
    if not bantjies_exists:
        entities['entities']['persons'].append({
            "entity_id": "PERSON_040",
            "name": "Daniel Jacobus Bantjies",
            "role": "trustee",
            "agent_type": "antagonist",
            "description": "Trustee of Faucitt Family Trust, appointed July 2024 (T-10 months before Ketoni payout)",
            "primary_actions": [
                "trustee_appointment",
                "audit_dismissal",
                "financial_control"
            ],
            "ketoni_payout_context": {
                "role": "trustee",
                "appointment_date": "2024-07-01",
                "timing_significance": "T-10 months before ZAR 18.75M payout"
            }
        })
        fixes.append("Added PERSON_040 (Daniel Jacobus Bantjies - Trustee)")
    
    return fixes

def fix_relation_references(relations, entity_id_map):
    """Fix undefined entity references in relations"""
    fixes = []
    
    # Map of generic references to actual entity IDs
    reference_map = {
        'director': 'PERSON_001',  # Peter as default director
        'financial_systems': 'PLATFORM_001',
        'associates': 'PERSON_002',  # Rynette as associate
        'Family Trust': 'TRUST_001',
        'estate_of_kayla': 'PERSON_013',  # Kayla Pretorius
        'legitimate_beneficiaries': 'PERSON_005',  # Daniel
    }
    
    # Fix relations
    for category, rel_list in relations.get('relations', {}).items():
        if not isinstance(rel_list, list):
            continue
        for rel in rel_list:
            if not isinstance(rel, dict):
                continue
            
            source = rel.get('source_entity')
            target = rel.get('target_entity')
            
            if source in reference_map:
                rel['source_entity'] = reference_map[source]
                fixes.append(f"Fixed source '{source}' -> '{reference_map[source]}' in {rel.get('relation_id')}")
            
            if target in reference_map:
                rel['target_entity'] = reference_map[target]
                fixes.append(f"Fixed target '{target}' -> '{reference_map[target]}' in {rel.get('relation_id')}")
    
    return fixes

def add_missing_events(events):
    """Add events that are referenced but not defined"""
    fixes = []
    
    event_ids = {e.get('event_id') for e in events.get('events', [])}
    
    # Events to add
    missing_events = [
        {
            "event_id": "EVENT_H020",
            "title": "Jax Confronts Rynette About Debt",
            "date": "2025-05-15",
            "description": "Jacqui confronts Rynette about R1,035,000 debt to ReZonance",
            "category": "revenue_hijacking"
        },
        {
            "event_id": "EVENT_H021",
            "title": "Jax Discovers Payment Discrepancies",
            "date": "2025-05-16",
            "description": "Jacqui discovers false payment claims totaling R765,361.34",
            "category": "criminal_activity"
        },
        {
            "event_id": "EVENT_BANTJIES_DISMISSES_AUDIT",
            "title": "Bantjies Dismisses Audit Request",
            "date": "2025-06-10",
            "description": "Bantjies learns of criminal matters and dismisses audit request",
            "category": "trust_violations"
        }
    ]
    
    for event in missing_events:
        if event['event_id'] not in event_ids:
            events['events'].append(event)
            fixes.append(f"Added event {event['event_id']}: {event['title']}")
    
    return fixes

def normalize_actor_names(timeline, entity_name_map):
    """Normalize actor names in timeline to match entity names"""
    fixes = []
    
    # Map of actor references to proper entity names
    actor_map = {
        'Daniel Jacobus Bantjies': 'Daniel Jacobus Bantjies',
        'Jax': 'Jacqueline Faucitt',
        'ORG_004': 'RegimA Skin Treatments',
        'PERSON_017': 'Kevin Derrick',
        'customers': 'Customers',
        'ORG_012': 'Ketoni Investment Holdings',
        'Family Trust': 'Faucitt Family Trust',
        'PERSON_001': 'Peter Andrew Faucitt',
        'estate_of_kayla': 'Kayla Pretorius Estate',
        'legitimate_beneficiaries': 'FFT Beneficiaries',
    }
    
    for entry in timeline.get('timeline', []):
        actors = entry.get('actors', [])
        new_actors = []
        for actor in actors:
            if actor in actor_map:
                new_actors.append(actor_map[actor])
                fixes.append(f"Normalized actor '{actor}' -> '{actor_map[actor]}'")
            else:
                new_actors.append(actor)
        entry['actors'] = new_actors
    
    return fixes

def update_metadata(entities, relations, events, timeline):
    """Update metadata with refinement information"""
    timestamp = datetime.now().isoformat()
    
    entities['metadata']['version'] = "33.0_AUDIT_REFINED_2026_01_22"
    entities['metadata']['last_updated'] = timestamp
    entities['metadata']['changes'] = "Audit-based refinement: fixed duplicates, added missing entities, normalized references"
    
    relations['metadata']['version'] = "33.0_AUDIT_REFINED_2026_01_22"
    relations['metadata']['last_updated'] = timestamp
    relations['metadata']['changes'] = "Audit-based refinement: fixed undefined entity references"
    
    events['metadata']['version'] = "28.0_AUDIT_REFINED_2026_01_22"
    events['metadata']['last_updated'] = timestamp
    events['metadata']['changes'] = "Audit-based refinement: added missing events"
    
    timeline['metadata']['version'] = "28.0_AUDIT_REFINED_2026_01_22"
    timeline['metadata']['last_updated'] = timestamp
    timeline['metadata']['changes'] = "Audit-based refinement: normalized actor names"

def main():
    print("=" * 80)
    print("ENTITY-RELATION MODEL FIX SCRIPT")
    print(f"Date: {datetime.now().isoformat()}")
    print("=" * 80)
    
    # Load data
    entities, relations, events, timeline = load_data()
    
    all_fixes = []
    
    # Fix duplicate entities
    print("\n=== Fixing duplicate entities ===")
    fixes = fix_duplicate_entities(entities)
    all_fixes.extend(fixes)
    for f in fixes:
        print(f"  ✓ {f}")
    
    # Add missing entities
    print("\n=== Adding missing entities ===")
    fixes = add_missing_entities(entities)
    all_fixes.extend(fixes)
    for f in fixes:
        print(f"  ✓ {f}")
    
    # Build entity ID map
    entity_id_map = {}
    for p in entities['entities'].get('persons', []):
        entity_id_map[p.get('entity_id')] = p.get('name')
    for o in entities['entities'].get('organizations', []):
        entity_id_map[o.get('entity_id')] = o.get('name')
    
    # Fix relation references
    print("\n=== Fixing relation references ===")
    fixes = fix_relation_references(relations, entity_id_map)
    all_fixes.extend(fixes)
    for f in fixes[:10]:
        print(f"  ✓ {f}")
    if len(fixes) > 10:
        print(f"  ... and {len(fixes) - 10} more")
    
    # Add missing events
    print("\n=== Adding missing events ===")
    fixes = add_missing_events(events)
    all_fixes.extend(fixes)
    for f in fixes:
        print(f"  ✓ {f}")
    
    # Normalize actor names
    print("\n=== Normalizing actor names ===")
    fixes = normalize_actor_names(timeline, entity_id_map)
    all_fixes.extend(fixes)
    unique_fixes = list(set(fixes))
    for f in unique_fixes[:10]:
        print(f"  ✓ {f}")
    if len(unique_fixes) > 10:
        print(f"  ... and {len(unique_fixes) - 10} more")
    
    # Update metadata
    print("\n=== Updating metadata ===")
    update_metadata(entities, relations, events, timeline)
    print("  ✓ Updated all metadata versions to 33.0/28.0 AUDIT_REFINED")
    
    # Recount entities
    person_count = len(entities['entities'].get('persons', []))
    org_count = len(entities['entities'].get('organizations', []))
    entities['metadata']['total_entities'] = person_count + org_count
    entities['metadata']['total_persons'] = person_count
    entities['metadata']['total_organizations'] = org_count
    
    # Save data
    print("\n=== Saving refined data ===")
    save_data(entities, relations, events, timeline)
    print("  ✓ All data models saved")
    
    print("\n" + "=" * 80)
    print(f"FIX COMPLETE: {len(all_fixes)} fixes applied")
    print("=" * 80)
    
    # Save fix report
    with open('data_models/FIX_REPORT_2026_01_22.json', 'w') as f:
        json.dump({
            'fix_date': datetime.now().isoformat(),
            'total_fixes': len(all_fixes),
            'fixes': all_fixes
        }, f, indent=2)
    
    print(f"\nFix report saved to: data_models/FIX_REPORT_2026_01_22.json")

if __name__ == '__main__':
    main()
