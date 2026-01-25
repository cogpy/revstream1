#!/usr/bin/env python3
"""
Analyze and refine entities, relations, events, and timelines based on evidence
"""
import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with backup"""
    # Create backup
    if os.path.exists(filepath):
        backup_path = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.rename(filepath, backup_path)
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_entities(entities_data):
    """Analyze entity data for completeness and quality"""
    issues = []
    stats = {
        'total': len(entities_data['entities']['persons']) + len(entities_data['entities']['organizations']),
        'persons': len(entities_data['entities']['persons']),
        'organizations': len(entities_data['entities']['organizations']),
        'missing_evidence': 0,
        'missing_ad_res_j7': 0,
        'weak_evidence': 0
    }
    
    # Check persons
    for person in entities_data['entities']['persons']:
        if not person.get('evidence') or len(person.get('evidence', [])) == 0:
            stats['missing_evidence'] += 1
            issues.append(f"PERSON {person['entity_id']} ({person['name']}): No evidence references")
        
        if not person.get('ad_res_j7_references') or len(person.get('ad_res_j7_references', [])) == 0:
            stats['missing_ad_res_j7'] += 1
            issues.append(f"PERSON {person['entity_id']} ({person['name']}): No ad-res-j7 references")
        
        if person.get('evidence_strength') in ['weak', 'circumstantial']:
            stats['weak_evidence'] += 1
    
    # Check organizations
    for org in entities_data['entities']['organizations']:
        if not org.get('evidence') or len(org.get('evidence', [])) == 0:
            stats['missing_evidence'] += 1
            issues.append(f"ORG {org['entity_id']} ({org['name']}): No evidence references")
        
        if not org.get('ad_res_j7_references') or len(org.get('ad_res_j7_references', [])) == 0:
            stats['missing_ad_res_j7'] += 1
            issues.append(f"ORG {org['entity_id']} ({org['name']}): No ad-res-j7 references")
    
    return stats, issues

def analyze_events(events_data):
    """Analyze event data for completeness and quality"""
    issues = []
    stats = {
        'total': len(events_data['events']),
        'missing_evidence': 0,
        'missing_ad_res_j7': 0,
        'missing_entities': 0,
        'criminal_threshold': 0,
        'civil_threshold': 0
    }
    
    for event in events_data['events']:
        if not event.get('evidence') or len(event.get('evidence', [])) == 0:
            stats['missing_evidence'] += 1
            issues.append(f"EVENT {event['event_id']}: No evidence references")
        
        if not event.get('ad_res_j7_evidence') or len(event.get('ad_res_j7_evidence', [])) == 0:
            stats['missing_ad_res_j7'] += 1
            issues.append(f"EVENT {event['event_id']}: No ad-res-j7 references")
        
        if not event.get('entities_involved') or len(event.get('entities_involved', [])) == 0:
            stats['missing_entities'] += 1
            issues.append(f"EVENT {event['event_id']}: No entities linked")
        
        if event.get('criminal_threshold'):
            stats['criminal_threshold'] += 1
        
        if event.get('civil_threshold'):
            stats['civil_threshold'] += 1
    
    return stats, issues

def analyze_relations(relations_data):
    """Analyze relation data for completeness and quality"""
    issues = []
    stats = {
        'total': 0,
        'missing_evidence': 0,
        'missing_events': 0,
        'by_type': defaultdict(int)
    }
    
    # Relations are organized by category
    for category, relations_list in relations_data['relations'].items():
        if isinstance(relations_list, list):
            for relation in relations_list:
                stats['total'] += 1
                
                if not relation.get('evidence') or len(relation.get('evidence', [])) == 0:
                    stats['missing_evidence'] += 1
                    issues.append(f"RELATION {relation.get('relation_id', 'UNKNOWN')}: No evidence references")
                
                if not relation.get('related_events') or len(relation.get('related_events', [])) == 0:
                    stats['missing_events'] += 1
                
                rel_type = relation.get('relation_type', 'unknown')
                stats['by_type'][rel_type] += 1
    
    return stats, issues

def analyze_timeline(timeline_data):
    """Analyze timeline data for completeness and quality"""
    issues = []
    stats = {
        'total': len(timeline_data['timeline']),
        'missing_evidence': 0,
        'missing_entities': 0,
        'missing_event_ref': 0,
        'by_year': defaultdict(int)
    }
    
    for entry in timeline_data['timeline']:
        if not entry.get('ad_res_j7_evidence_enhanced') or len(entry.get('ad_res_j7_evidence_enhanced', [])) == 0:
            stats['missing_evidence'] += 1
        
        if not entry.get('entities_involved') or len(entry.get('entities_involved', [])) == 0:
            stats['missing_entities'] += 1
        
        if not entry.get('event_ref'):
            stats['missing_event_ref'] += 1
            issues.append(f"TIMELINE {entry['date']}: No event reference")
        
        year = entry['date'][:4]
        stats['by_year'][year] += 1
    
    return stats, issues

def main():
    print("="*80)
    print("ENTITY-RELATION-EVENT-TIMELINE ANALYSIS")
    print("="*80)
    
    base_path = "/home/ubuntu/revstream1/data_models"
    
    # Load data models
    entities_data = load_json(f"{base_path}/entities/entities.json")
    events_data = load_json(f"{base_path}/events/events.json")
    relations_data = load_json(f"{base_path}/relations/relations.json")
    timeline_data = load_json(f"{base_path}/timelines/timeline.json")
    
    print("\n1. ENTITIES ANALYSIS")
    print("-" * 80)
    entity_stats, entity_issues = analyze_entities(entities_data)
    print(f"Total Entities: {entity_stats['total']}")
    print(f"  - Persons: {entity_stats['persons']}")
    print(f"  - Organizations: {entity_stats['organizations']}")
    print(f"Missing Evidence: {entity_stats['missing_evidence']}")
    print(f"Missing ad-res-j7 References: {entity_stats['missing_ad_res_j7']}")
    print(f"Weak Evidence: {entity_stats['weak_evidence']}")
    
    print("\n2. EVENTS ANALYSIS")
    print("-" * 80)
    event_stats, event_issues = analyze_events(events_data)
    print(f"Total Events: {event_stats['total']}")
    print(f"Missing Evidence: {event_stats['missing_evidence']}")
    print(f"Missing ad-res-j7 References: {event_stats['missing_ad_res_j7']}")
    print(f"Missing Entity Links: {event_stats['missing_entities']}")
    print(f"Criminal Threshold Events: {event_stats['criminal_threshold']}")
    print(f"Civil Threshold Events: {event_stats['civil_threshold']}")
    
    print("\n3. RELATIONS ANALYSIS")
    print("-" * 80)
    relation_stats, relation_issues = analyze_relations(relations_data)
    print(f"Total Relations: {relation_stats['total']}")
    print(f"Missing Evidence: {relation_stats['missing_evidence']}")
    print(f"Missing Event Links: {relation_stats['missing_events']}")
    print("\nRelations by Type:")
    for rel_type, count in sorted(relation_stats['by_type'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  - {rel_type}: {count}")
    
    print("\n4. TIMELINE ANALYSIS")
    print("-" * 80)
    timeline_stats, timeline_issues = analyze_timeline(timeline_data)
    print(f"Total Timeline Entries: {timeline_stats['total']}")
    print(f"Missing Evidence: {timeline_stats['missing_evidence']}")
    print(f"Missing Entity Links: {timeline_stats['missing_entities']}")
    print(f"Missing Event References: {timeline_stats['missing_event_ref']}")
    print("\nEntries by Year:")
    for year, count in sorted(timeline_stats['by_year'].items()):
        print(f"  - {year}: {count}")
    
    print("\n5. CROSS-REFERENCE VALIDATION")
    print("-" * 80)
    
    # Check event-entity consistency
    event_entities = set()
    for event in events_data['events']:
        event_entities.update(event.get('entities_involved', []))
    
    defined_entities = set()
    for person in entities_data['entities']['persons']:
        defined_entities.add(person['entity_id'])
    for org in entities_data['entities']['organizations']:
        defined_entities.add(org['entity_id'])
    
    undefined_entities = event_entities - defined_entities
    if undefined_entities:
        print(f"⚠️  Events reference {len(undefined_entities)} undefined entities:")
        for ent in list(undefined_entities)[:10]:
            print(f"  - {ent}")
    else:
        print("✅ All event entities are properly defined")
    
    # Check timeline-event consistency
    timeline_events = set()
    for entry in timeline_data['timeline']:
        if entry.get('event_ref'):
            timeline_events.add(entry['event_ref'])
    
    defined_events = set(event['event_id'] for event in events_data['events'])
    undefined_timeline_events = timeline_events - defined_events
    
    if undefined_timeline_events:
        print(f"⚠️  Timeline references {len(undefined_timeline_events)} undefined events:")
        for evt in list(undefined_timeline_events)[:10]:
            print(f"  - {evt}")
    else:
        print("✅ All timeline events are properly defined")
    
    # Save analysis report
    report = {
        'timestamp': datetime.now().isoformat(),
        'entities': entity_stats,
        'events': event_stats,
        'relations': relation_stats,
        'timeline': timeline_stats,
        'cross_reference': {
            'undefined_entities_in_events': list(undefined_entities),
            'undefined_events_in_timeline': list(undefined_timeline_events)
        },
        'issues': {
            'entities': entity_issues[:20],  # Top 20
            'events': event_issues[:20],
            'relations': relation_issues[:20],
            'timeline': timeline_issues[:20]
        }
    }
    
    report_path = f"{base_path}/ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(report, report_path)
    print(f"\n📊 Full analysis report saved to: {report_path}")
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
