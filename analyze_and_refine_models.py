#!/usr/bin/env python3
"""
Comprehensive analysis and refinement of entities, relations, events, and timelines
for case 2025-137857 with evidence cross-referencing to ad-res-j7 repository
"""

import json
import os
from datetime import datetime
from collections import defaultdict

# Paths
REVSTREAM_PATH = "/home/ubuntu/revstream1"
AD_RES_J7_PATH = "/home/ubuntu/ad-res-j7"

# Load latest data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load current models
entities = load_json(f"{REVSTREAM_PATH}/data_models/entities/entities_refined_2025_11_28_v23.json")
events = load_json(f"{REVSTREAM_PATH}/data_models/events/events_refined_2025_11_28_v25.json")
relations = load_json(f"{REVSTREAM_PATH}/data_models/relations/relations_refined_2025_11_28_v20.json")

print("=" * 80)
print("COMPREHENSIVE DATA MODEL ANALYSIS - CASE 2025-137857")
print("=" * 80)
print()

# ENTITIES ANALYSIS
print("1. ENTITIES ANALYSIS")
print("-" * 80)
persons = [e for e in entities['entities'].get('persons', [])]
organizations = [e for e in entities['entities'].get('organizations', [])]
print(f"Total Persons: {len(persons)}")
print(f"Total Organizations: {len(organizations)}")
print()

# Analyze entity completeness
incomplete_entities = []
for person in persons:
    issues = []
    if not person.get('evidence_files'):
        issues.append("Missing evidence_files")
    if not person.get('ad_res_j7_references'):
        issues.append("Missing ad_res_j7_references")
    if not person.get('timeline_events'):
        issues.append("Missing timeline_events")
    if issues:
        incomplete_entities.append({
            'entity_id': person.get('entity_id'),
            'name': person.get('name'),
            'issues': issues
        })

print(f"Entities with incomplete data: {len(incomplete_entities)}")
for entity in incomplete_entities[:5]:
    print(f"  - {entity['entity_id']} ({entity['name']}): {', '.join(entity['issues'])}")
print()

# EVENTS ANALYSIS
print("2. EVENTS ANALYSIS")
print("-" * 80)
all_events = events.get('events', [])
print(f"Total Events: {len(all_events)}")

# Categorize events
events_by_phase = defaultdict(list)
events_by_category = defaultdict(list)
events_with_financial_impact = []
events_missing_evidence = []

for event in all_events:
    phase = event.get('timeline_phase', 'UNKNOWN')
    category = event.get('category', 'UNKNOWN')
    events_by_phase[phase].append(event)
    events_by_category[category].append(event)
    
    if event.get('financial_impact'):
        events_with_financial_impact.append(event)
    
    if not event.get('evidence_files') and not event.get('evidence'):
        events_missing_evidence.append(event)

print(f"Events by Phase:")
for phase, evts in sorted(events_by_phase.items()):
    print(f"  {phase}: {len(evts)} events")
print()

print(f"Events by Category:")
for cat, evts in sorted(events_by_category.items()):
    print(f"  {cat}: {len(evts)} events")
print()

print(f"Events with Financial Impact: {len(events_with_financial_impact)}")
print(f"Events Missing Evidence References: {len(events_missing_evidence)}")
if events_missing_evidence:
    print("  Sample events missing evidence:")
    for evt in events_missing_evidence[:3]:
        print(f"    - {evt.get('event_id')}: {evt.get('title')}")
print()

# RELATIONS ANALYSIS
print("3. RELATIONS ANALYSIS")
print("-" * 80)
all_relations = []
for rel_type, rels in relations.get('relations', {}).items():
    all_relations.extend(rels)
    print(f"{rel_type}: {len(rels)} relations")

print(f"Total Relations: {len(all_relations)}")
print()

# Check for missing ad_res_j7_references in relations
relations_missing_refs = []
for rel in all_relations:
    if not rel.get('ad_res_j7_references'):
        relations_missing_refs.append(rel)

print(f"Relations Missing ad_res_j7_references: {len(relations_missing_refs)}")
print()

# TIMELINE ANALYSIS
print("4. TIMELINE ANALYSIS")
print("-" * 80)
# Extract unique dates from events
event_dates = []
for event in all_events:
    if event.get('date'):
        event_dates.append(event['date'])

event_dates_sorted = sorted(set(event_dates))
print(f"Timeline Span: {event_dates_sorted[0] if event_dates_sorted else 'N/A'} to {event_dates_sorted[-1] if event_dates_sorted else 'N/A'}")
print(f"Total Unique Dates: {len(event_dates_sorted)}")
print()

# CROSS-REFERENCE ANALYSIS
print("5. CROSS-REFERENCE ANALYSIS (ad-res-j7)")
print("-" * 80)

# Check if evidence files exist in ad-res-j7
def check_evidence_exists(evidence_path):
    full_path = os.path.join(AD_RES_J7_PATH, evidence_path.lstrip('./'))
    return os.path.exists(full_path)

# Sample check for first 5 persons
print("Checking evidence file existence for sample entities:")
for person in persons[:5]:
    entity_id = person.get('entity_id')
    name = person.get('name')
    evidence_files = person.get('evidence_files', [])
    
    if evidence_files:
        exists_count = sum(1 for ef in evidence_files if check_evidence_exists(ef))
        print(f"  {entity_id} ({name}): {exists_count}/{len(evidence_files)} evidence files exist")
print()

# RECOMMENDATIONS
print("6. REFINEMENT RECOMMENDATIONS")
print("-" * 80)
recommendations = []

if incomplete_entities:
    recommendations.append(f"Complete missing data for {len(incomplete_entities)} entities")

if events_missing_evidence:
    recommendations.append(f"Add evidence references to {len(events_missing_evidence)} events")

if relations_missing_refs:
    recommendations.append(f"Add ad_res_j7_references to {len(relations_missing_refs)} relations")

# Check for orphaned events (events not referenced by any entity)
all_entity_events = set()
for person in persons:
    all_entity_events.update(person.get('timeline_events', []))
for org in organizations:
    all_entity_events.update(org.get('timeline_events', []))

all_event_ids = set(evt.get('event_id') for evt in all_events)
orphaned_events = all_event_ids - all_entity_events
if orphaned_events:
    recommendations.append(f"Link {len(orphaned_events)} orphaned events to entities")

print("Priority Recommendations:")
for i, rec in enumerate(recommendations, 1):
    print(f"  {i}. {rec}")
print()

# GENERATE REFINEMENT REPORT
report = {
    "analysis_date": datetime.now().isoformat(),
    "case_number": "2025-137857",
    "summary": {
        "total_entities": len(persons) + len(organizations),
        "total_persons": len(persons),
        "total_organizations": len(organizations),
        "total_events": len(all_events),
        "total_relations": len(all_relations),
        "events_with_financial_impact": len(events_with_financial_impact),
        "incomplete_entities": len(incomplete_entities),
        "events_missing_evidence": len(events_missing_evidence),
        "relations_missing_refs": len(relations_missing_refs),
        "orphaned_events": len(orphaned_events)
    },
    "recommendations": recommendations,
    "incomplete_entities": incomplete_entities,
    "events_missing_evidence": [
        {"event_id": e.get('event_id'), "title": e.get('title')} 
        for e in events_missing_evidence
    ],
    "orphaned_events": list(orphaned_events)
}

save_json(report, f"{REVSTREAM_PATH}/REFINEMENT_ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json")
print(f"✓ Analysis report saved: REFINEMENT_ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json")
print()
print("=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
