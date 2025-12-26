#!/usr/bin/env python3
"""
Comprehensive refinement of entities, relations, events, and timelines
Based on ad-res-j7 evidence and burden of proof analysis
Date: 2025-12-24
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = BASE_DIR / "data_models"
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def backup_file(filepath):
    """Create backup of file"""
    if filepath.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = filepath.parent / f"{filepath.stem}.backup_{timestamp}{filepath.suffix}"
        os.system(f"cp {filepath} {backup_path}")
        print(f"✓ Backed up: {backup_path.name}")

def analyze_timeline_events():
    """Analyze timeline events and suggest improvements"""
    print("\n=== TIMELINE ANALYSIS ===")
    
    # Load timeline and events
    timeline_path = DATA_MODELS_DIR / "timelines" / "timeline.json"
    events_path = DATA_MODELS_DIR / "events" / "events.json"
    
    timeline = load_json(timeline_path)
    events = load_json(events_path)
    
    # Get all event IDs from timeline
    timeline_event_ids = set()
    for phase in timeline['timeline']:
        timeline_event_ids.update(phase['events'])
    
    # Get all event IDs from events
    event_ids = {event['event_id'] for event in events['events']}
    
    # Find missing events
    missing_in_timeline = event_ids - timeline_event_ids
    missing_in_events = timeline_event_ids - event_ids
    
    print(f"\n📊 Timeline Statistics:")
    print(f"  Total events in timeline: {len(timeline_event_ids)}")
    print(f"  Total events in events.json: {len(event_ids)}")
    print(f"  Events missing from timeline: {len(missing_in_timeline)}")
    print(f"  Invalid event IDs in timeline: {len(missing_in_events)}")
    
    if missing_in_timeline:
        print(f"\n⚠️  Events not in timeline: {sorted(missing_in_timeline)}")
    
    if missing_in_events:
        print(f"\n⚠️  Invalid event IDs in timeline: {sorted(missing_in_events)}")
    
    # Analyze events by date and phase
    events_by_date = {}
    for event in events['events']:
        if 'date' in event:
            date = event['date']
            year = date.split('-')[0] if date else 'unknown'
            if year not in events_by_date:
                events_by_date[year] = []
            events_by_date[year].append(event)
    
    print(f"\n📅 Events by Year:")
    for year in sorted(events_by_date.keys()):
        print(f"  {year}: {len(events_by_date[year])} events")
    
    # Check for events with high evidence strength
    high_evidence_events = []
    for event in events['events']:
        if event.get('evidence_strength') in ['conclusive', 'criminal_threshold']:
            high_evidence_events.append(event)
    
    print(f"\n🎯 High Evidence Strength Events: {len(high_evidence_events)}")
    for event in high_evidence_events[:10]:
        print(f"  {event['event_id']}: {event.get('title', event.get('description', 'N/A')[:50])}")
    
    return {
        'missing_in_timeline': list(missing_in_timeline),
        'missing_in_events': list(missing_in_events),
        'events_by_year': {k: len(v) for k, v in events_by_date.items()},
        'high_evidence_count': len(high_evidence_events)
    }

def refine_timeline():
    """Refine timeline with missing events"""
    print("\n=== REFINING TIMELINE ===")
    
    timeline_path = DATA_MODELS_DIR / "timelines" / "timeline.json"
    events_path = DATA_MODELS_DIR / "events" / "events.json"
    
    backup_file(timeline_path)
    
    timeline = load_json(timeline_path)
    events = load_json(events_path)
    
    # Create event lookup by ID
    event_lookup = {event['event_id']: event for event in events['events']}
    
    # Get all event IDs from timeline
    timeline_event_ids = set()
    for phase in timeline['timeline']:
        timeline_event_ids.update(phase['events'])
    
    # Find missing events
    event_ids = set(event_lookup.keys())
    missing_in_timeline = event_ids - timeline_event_ids
    
    if not missing_in_timeline:
        print("✓ No missing events in timeline")
        return
    
    print(f"\n📝 Adding {len(missing_in_timeline)} missing events to timeline...")
    
    # Sort missing events by date
    missing_events = []
    for event_id in missing_in_timeline:
        event = event_lookup[event_id]
        if 'date' in event:
            missing_events.append(event)
    
    missing_events.sort(key=lambda x: x['date'])
    
    # Add events to appropriate phases
    for event in missing_events:
        date = event['date']
        year = int(date.split('-')[0])
        
        # Determine phase
        if year <= 2019:
            phase_idx = 0  # Foundation
        elif year <= 2023:
            phase_idx = 1  # Fraud
        else:
            phase_idx = 2  # Discovery
        
        # Add to phase if not already there
        if event['event_id'] not in timeline['timeline'][phase_idx]['events']:
            timeline['timeline'][phase_idx]['events'].append(event['event_id'])
            print(f"  ✓ Added {event['event_id']} to {timeline['timeline'][phase_idx]['title']}")
    
    # Update metadata
    timeline['metadata']['last_updated'] = datetime.now().isoformat()
    timeline['metadata']['version'] = "15.0_REFINED_2025_12_24"
    timeline['metadata']['changes'] = "Added missing events from events.json"
    
    # Save
    save_json(timeline, timeline_path)
    print(f"\n✅ Timeline updated: {timeline_path}")

def enhance_entities_with_sf9():
    """Enhance entities with SF9 Ian Levitt R63M demand letter"""
    print("\n=== ENHANCING ENTITIES WITH SF9 ===")
    
    entities_path = DATA_MODELS_DIR / "entities" / "entities.json"
    backup_file(entities_path)
    
    entities = load_json(entities_path)
    
    # Check if SF9 already referenced
    sf9_count = 0
    for person in entities['entities']['persons']:
        if 'SF9' in str(person.get('evidence', [])):
            sf9_count += 1
    
    print(f"  Current SF9 references: {sf9_count}")
    
    # Add SF9 to Peter Faucitt if not present
    for person in entities['entities']['persons']:
        if person['entity_id'] == 'PERSON_001':
            if 'SF9 - Ian Levitt R63M demand letter' not in person.get('evidence', []):
                person['evidence'].append('SF9 - Ian Levitt R63M demand letter')
                print(f"  ✓ Added SF9 to PERSON_001 (Peter Faucitt)")
            
            # Add to ad_res_j7_references if not present
            sf9_ref = "SF9_Ian_Levitt_Demand_Letter.md - R63M formal demand (ignored)"
            if sf9_ref not in person.get('ad_res_j7_references', []):
                if 'ad_res_j7_references' not in person:
                    person['ad_res_j7_references'] = []
                person['ad_res_j7_references'].append(sf9_ref)
                print(f"  ✓ Added SF9 ad-res-j7 reference to PERSON_001")
    
    # Update metadata
    entities['metadata']['last_updated'] = datetime.now().isoformat()
    entities['metadata']['version'] = "16.0_REFINED_2025_12_24"
    entities['metadata']['changes'] = "Enhanced with SF9 Ian Levitt R63M demand letter"
    
    save_json(entities, entities_path)
    print(f"\n✅ Entities updated: {entities_path}")

def analyze_evidence_coverage():
    """Analyze evidence coverage across entities, relations, and events"""
    print("\n=== EVIDENCE COVERAGE ANALYSIS ===")
    
    entities_path = DATA_MODELS_DIR / "entities" / "entities.json"
    relations_path = DATA_MODELS_DIR / "relations" / "relations.json"
    events_path = DATA_MODELS_DIR / "events" / "events.json"
    
    entities = load_json(entities_path)
    relations = load_json(relations_path)
    events = load_json(events_path)
    
    # Count evidence references
    entities_with_evidence = 0
    entities_with_ad_res = 0
    for person in entities['entities']['persons']:
        if person.get('evidence'):
            entities_with_evidence += 1
        if person.get('ad_res_j7_references'):
            entities_with_ad_res += 1
    
    for org in entities['entities']['organizations']:
        if org.get('evidence'):
            entities_with_evidence += 1
        if org.get('ad_res_j7_references'):
            entities_with_ad_res += 1
    
    # Relations are organized by type, need to iterate through all types
    all_relations = []
    for rel_type, rel_list in relations['relations'].items():
        if isinstance(rel_list, list):
            all_relations.extend(rel_list)
    
    relations_with_evidence = sum(1 for rel in all_relations if rel.get('evidence'))
    relations_with_ad_res = sum(1 for rel in all_relations if rel.get('ad_res_j7_evidence'))
    
    events_with_evidence = sum(1 for event in events['events'] if event.get('evidence'))
    events_with_ad_res = sum(1 for event in events['events'] if event.get('ad_res_j7_evidence'))
    
    total_entities = len(entities['entities']['persons']) + len(entities['entities']['organizations'])
    total_relations = len(all_relations)
    total_events = len(events['events'])
    
    print(f"\n📊 Evidence Coverage:")
    print(f"\n  Entities ({total_entities} total):")
    print(f"    With evidence: {entities_with_evidence} ({entities_with_evidence/total_entities*100:.1f}%)")
    print(f"    With ad-res-j7 refs: {entities_with_ad_res} ({entities_with_ad_res/total_entities*100:.1f}%)")
    
    print(f"\n  Relations ({total_relations} total):")
    print(f"    With evidence: {relations_with_evidence} ({relations_with_evidence/total_relations*100:.1f}%)")
    print(f"    With ad-res-j7 refs: {relations_with_ad_res} ({relations_with_ad_res/total_relations*100:.1f}%)")
    
    print(f"\n  Events ({total_events} total):")
    print(f"    With evidence: {events_with_evidence} ({events_with_evidence/total_events*100:.1f}%)")
    print(f"    With ad-res-j7 refs: {events_with_ad_res} ({events_with_ad_res/total_events*100:.1f}%)")
    
    return {
        'entities': {
            'total': total_entities,
            'with_evidence': entities_with_evidence,
            'with_ad_res': entities_with_ad_res
        },
        'relations': {
            'total': total_relations,
            'with_evidence': relations_with_evidence,
            'with_ad_res': relations_with_ad_res
        },
        'events': {
            'total': total_events,
            'with_evidence': events_with_evidence,
            'with_ad_res': events_with_ad_res
        }
    }

def main():
    """Main execution"""
    print("=" * 80)
    print("COMPREHENSIVE DATA MODEL REFINEMENT")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 80)
    
    # Analyze timeline
    timeline_analysis = analyze_timeline_events()
    
    # Refine timeline
    refine_timeline()
    
    # Enhance entities with SF9
    enhance_entities_with_sf9()
    
    # Analyze evidence coverage
    evidence_analysis = analyze_evidence_coverage()
    
    # Save analysis report
    report = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'case_number': '2025-137857'
        },
        'timeline_analysis': timeline_analysis,
        'evidence_coverage': evidence_analysis
    }
    
    report_path = BASE_DIR / f"REFINEMENT_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(report, report_path)
    print(f"\n✅ Analysis report saved: {report_path}")
    
    print("\n" + "=" * 80)
    print("REFINEMENT COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
