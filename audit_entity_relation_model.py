#!/usr/bin/env python3
"""
Comprehensive Entity-Relation Model Audit Script
Performs rigorous checks and cross-checks to identify inconsistencies
"""

import json
from datetime import datetime
from collections import defaultdict

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

def extract_entity_ids(entities):
    """Extract all entity IDs from the entities structure"""
    entity_ids = {}
    
    # Handle persons
    for person in entities.get('entities', {}).get('persons', []):
        eid = person.get('entity_id')
        if eid:
            entity_ids[eid] = {
                'name': person.get('name'),
                'type': 'person',
                'data': person
            }
    
    # Handle organizations
    for org in entities.get('entities', {}).get('organizations', []):
        eid = org.get('entity_id')
        if eid:
            entity_ids[eid] = {
                'name': org.get('name'),
                'type': 'organization',
                'data': org
            }
    
    return entity_ids

def extract_event_ids(events):
    """Extract all event IDs"""
    event_ids = {}
    for event in events.get('events', []):
        eid = event.get('event_id')
        if eid:
            event_ids[eid] = event
    return event_ids

def audit_relations(relations, entity_ids):
    """Audit relations for undefined entity references"""
    issues = []
    
    # Handle nested relations structure
    relations_data = relations.get('relations', {})
    
    # Flatten all relation categories
    all_relations = []
    if isinstance(relations_data, dict):
        for category, rel_list in relations_data.items():
            if isinstance(rel_list, list):
                all_relations.extend(rel_list)
    elif isinstance(relations_data, list):
        all_relations = relations_data
    
    for r in all_relations:
        if not isinstance(r, dict):
            continue
        source = r.get('source_entity') or r.get('source')
        target = r.get('target_entity') or r.get('target')
        rel_id = r.get('relation_id', 'UNKNOWN')
        
        if source and source not in entity_ids:
            issues.append({
                'type': 'undefined_source',
                'relation_id': rel_id,
                'entity_ref': source,
                'relation_type': r.get('relation_type', r.get('type'))
            })
        
        if target and target not in entity_ids:
            issues.append({
                'type': 'undefined_target',
                'relation_id': rel_id,
                'entity_ref': target,
                'relation_type': r.get('relation_type', r.get('type'))
            })
    
    return issues

def audit_entity_events(entities, event_ids):
    """Check that entity timeline_events reference valid events"""
    issues = []
    
    # Check persons
    for person in entities.get('entities', {}).get('persons', []):
        eid = person.get('entity_id')
        name = person.get('name')
        for event_ref in person.get('timeline_events', []):
            if event_ref not in event_ids:
                issues.append({
                    'type': 'undefined_event_reference',
                    'entity_id': eid,
                    'entity_name': name,
                    'event_ref': event_ref
                })
    
    # Check organizations
    for org in entities.get('entities', {}).get('organizations', []):
        eid = org.get('entity_id')
        name = org.get('name')
        for event_ref in org.get('timeline_events', []):
            if event_ref not in event_ids:
                issues.append({
                    'type': 'undefined_event_reference',
                    'entity_id': eid,
                    'entity_name': name,
                    'event_ref': event_ref
                })
    
    return issues

def audit_timeline_events(timeline, event_ids):
    """Check timeline entries reference valid events"""
    issues = []
    
    for entry in timeline.get('timeline', []):
        event_ref = entry.get('event_ref')
        date = entry.get('date')
        
        # Check if event_ref exists in events
        if event_ref and event_ref.startswith('EVENT_') and event_ref not in event_ids:
            # Only flag if it looks like a formal event reference
            if not event_ref.startswith('EVENT_GEN_') and not event_ref.startswith('EVENT_CIPC_'):
                issues.append({
                    'type': 'timeline_undefined_event',
                    'event_ref': event_ref,
                    'date': date,
                    'title': entry.get('title', 'No title')
                })
    
    return issues

def audit_date_consistency(timeline):
    """Check for date inconsistencies in timeline"""
    issues = []
    
    # Known date constraints
    constraints = {
        'kayla_death': '2023-07-13',  # Kayla died on this date
        'ketoni_incorporation': '2023-02-20',  # Ketoni incorporated
        'fft_ketoni_investment': '2023-04-24',  # FFT invested in Ketoni
    }
    
    for entry in timeline.get('timeline', []):
        date = entry.get('date')
        title = entry.get('title', '').lower()
        description = entry.get('description', '').lower()
        
        # Check Kayla-related events
        if 'kayla' in title or 'kayla' in description:
            if 'estate' in title or 'estate' in description:
                # Estate events must be after death
                if date and date < constraints['kayla_death']:
                    issues.append({
                        'type': 'date_logic_error',
                        'event_ref': entry.get('event_ref'),
                        'date': date,
                        'title': entry.get('title'),
                        'issue': f"Kayla estate event before death ({constraints['kayla_death']})"
                    })
    
    return issues

def audit_duplicate_entities(entities):
    """Check for duplicate entity names or IDs"""
    issues = []
    
    seen_ids = {}
    seen_names = {}
    
    for person in entities.get('entities', {}).get('persons', []):
        eid = person.get('entity_id')
        name = person.get('name')
        
        if eid in seen_ids:
            issues.append({
                'type': 'duplicate_entity_id',
                'entity_id': eid,
                'names': [seen_ids[eid], name]
            })
        seen_ids[eid] = name
        
        if name in seen_names:
            issues.append({
                'type': 'duplicate_entity_name',
                'name': name,
                'ids': [seen_names[name], eid]
            })
        seen_names[name] = eid
    
    for org in entities.get('entities', {}).get('organizations', []):
        eid = org.get('entity_id')
        name = org.get('name')
        
        if eid in seen_ids:
            issues.append({
                'type': 'duplicate_entity_id',
                'entity_id': eid,
                'names': [seen_ids[eid], name]
            })
        seen_ids[eid] = name
    
    return issues

def audit_missing_fields(entities):
    """Check for entities missing required fields"""
    issues = []
    
    required_person_fields = ['entity_id', 'name', 'role']
    required_org_fields = ['entity_id', 'name']
    
    for person in entities.get('entities', {}).get('persons', []):
        for field in required_person_fields:
            if not person.get(field):
                issues.append({
                    'type': 'missing_required_field',
                    'entity_id': person.get('entity_id', 'UNKNOWN'),
                    'entity_type': 'person',
                    'missing_field': field
                })
    
    for org in entities.get('entities', {}).get('organizations', []):
        for field in required_org_fields:
            if not org.get(field):
                issues.append({
                    'type': 'missing_required_field',
                    'entity_id': org.get('entity_id', 'UNKNOWN'),
                    'entity_type': 'organization',
                    'missing_field': field
                })
    
    return issues

def audit_relation_symmetry(relations):
    """Check for asymmetric relations that should be symmetric"""
    issues = []
    
    # Flatten all relation categories
    relations_data = relations.get('relations', {})
    all_relations = []
    if isinstance(relations_data, dict):
        for category, rel_list in relations_data.items():
            if isinstance(rel_list, list):
                all_relations.extend(rel_list)
    elif isinstance(relations_data, list):
        all_relations = relations_data
    
    # Build relation map
    relation_map = defaultdict(list)
    for r in all_relations:
        if not isinstance(r, dict):
            continue
        source = r.get('source_entity') or r.get('source')
        target = r.get('target_entity') or r.get('target')
        rtype = r.get('relation_type') or r.get('type')
        relation_map[(source, target)].append(rtype)
    
    # Check for family relations that should be bidirectional
    for r in all_relations:
        if not isinstance(r, dict):
            continue
        source = r.get('source_entity') or r.get('source')
        target = r.get('target_entity') or r.get('target')
        rtype = r.get('relation_type') or r.get('type')
        
        if rtype == 'parent_of':
            # Should have corresponding child_of
            if 'child_of' not in relation_map.get((target, source), []):
                issues.append({
                    'type': 'missing_inverse_relation',
                    'relation': f"{source} parent_of {target}",
                    'expected_inverse': f"{target} child_of {source}"
                })
    
    return issues

def cross_check_actors_in_timeline(timeline, entity_ids):
    """Cross-check actors referenced in timeline against entities"""
    issues = []
    all_actors = set()
    
    for entry in timeline.get('timeline', []):
        actors = entry.get('actors', [])
        for actor in actors:
            all_actors.add(actor)
    
    # Check if actors are defined as entities
    entity_names = {v['name'] for v in entity_ids.values()}
    
    for actor in all_actors:
        if actor not in entity_names:
            # Check if it's a partial match
            matches = [n for n in entity_names if actor.lower() in n.lower() or n.lower() in actor.lower()]
            if not matches:
                issues.append({
                    'type': 'undefined_actor',
                    'actor': actor,
                    'suggestion': 'Add as new entity or correct spelling'
                })
            elif len(matches) == 1 and matches[0] != actor:
                issues.append({
                    'type': 'actor_name_mismatch',
                    'actor': actor,
                    'suggested_match': matches[0]
                })
    
    return issues

def main():
    print("=" * 80)
    print("ENTITY-RELATION MODEL COMPREHENSIVE AUDIT")
    print(f"Date: {datetime.now().isoformat()}")
    print("=" * 80)
    
    # Load data
    entities, relations, events, timeline = load_data()
    
    # Extract IDs
    entity_ids = extract_entity_ids(entities)
    event_ids = extract_event_ids(events)
    
    print(f"\n=== DATA SUMMARY ===")
    print(f"Persons: {len(entities.get('entities', {}).get('persons', []))}")
    print(f"Organizations: {len(entities.get('entities', {}).get('organizations', []))}")
    print(f"Total Entities: {len(entity_ids)}")
    print(f"Relations: {len(relations.get('relations', []))}")
    print(f"Events: {len(event_ids)}")
    print(f"Timeline Entries: {len(timeline.get('timeline', []))}")
    
    all_issues = []
    
    # Run audits
    print("\n=== AUDIT 1: Relations referencing undefined entities ===")
    issues = audit_relations(relations, entity_ids)
    all_issues.extend(issues)
    if issues:
        for i in issues[:10]:
            print(f"  [{i['type']}] {i['relation_id']}: {i['entity_ref']}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("  ✓ All relations reference defined entities")
    
    print("\n=== AUDIT 2: Entity event references ===")
    issues = audit_entity_events(entities, event_ids)
    all_issues.extend(issues)
    if issues:
        for i in issues[:10]:
            print(f"  [{i['type']}] {i['entity_name']}: {i['event_ref']}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("  ✓ All entity event references are valid")
    
    print("\n=== AUDIT 3: Timeline event references ===")
    issues = audit_timeline_events(timeline, event_ids)
    all_issues.extend(issues)
    if issues:
        for i in issues[:10]:
            print(f"  [{i['type']}] {i['event_ref']}: {i['title'][:50]}...")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("  ✓ All timeline event references are valid")
    
    print("\n=== AUDIT 4: Date consistency ===")
    issues = audit_date_consistency(timeline)
    all_issues.extend(issues)
    if issues:
        for i in issues:
            print(f"  [{i['type']}] {i['date']}: {i['issue']}")
    else:
        print("  ✓ All dates are logically consistent")
    
    print("\n=== AUDIT 5: Duplicate entities ===")
    issues = audit_duplicate_entities(entities)
    all_issues.extend(issues)
    if issues:
        for i in issues:
            print(f"  [{i['type']}] {i}")
    else:
        print("  ✓ No duplicate entities found")
    
    print("\n=== AUDIT 6: Missing required fields ===")
    issues = audit_missing_fields(entities)
    all_issues.extend(issues)
    if issues:
        for i in issues[:10]:
            print(f"  [{i['type']}] {i['entity_id']}: missing {i['missing_field']}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("  ✓ All required fields present")
    
    print("\n=== AUDIT 7: Relation symmetry ===")
    issues = audit_relation_symmetry(relations)
    all_issues.extend(issues)
    if issues:
        for i in issues[:10]:
            print(f"  [{i['type']}] {i['relation']}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("  ✓ All relations properly symmetric")
    
    print("\n=== AUDIT 8: Actor cross-check ===")
    issues = cross_check_actors_in_timeline(timeline, entity_ids)
    all_issues.extend(issues)
    if issues:
        for i in issues[:10]:
            print(f"  [{i['type']}] {i['actor']}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    else:
        print("  ✓ All actors are defined entities")
    
    print("\n" + "=" * 80)
    print(f"AUDIT COMPLETE: {len(all_issues)} issues found")
    print("=" * 80)
    
    # Save issues to file
    with open('data_models/AUDIT_REPORT_2026_01_22.json', 'w') as f:
        json.dump({
            'audit_date': datetime.now().isoformat(),
            'total_issues': len(all_issues),
            'issues': all_issues
        }, f, indent=2)
    
    print(f"\nDetailed report saved to: data_models/AUDIT_REPORT_2026_01_22.json")
    
    return all_issues

if __name__ == '__main__':
    main()
