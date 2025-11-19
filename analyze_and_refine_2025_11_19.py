#!/usr/bin/env python3.11
"""
Comprehensive Analysis and Refinement Script for revstream1
Date: 2025-11-19
Purpose: Analyze entities, relations, events, timelines and suggest improvements
"""

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# Load all data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Paths
BASE_DIR = Path('/home/ubuntu/revstream1')
DATA_MODELS = BASE_DIR / 'data_models'

entities = load_json(DATA_MODELS / 'entities' / 'entities_refined_2025_11_19.json')
events = load_json(DATA_MODELS / 'events' / 'events_refined_2025_11_19.json')
relations = load_json(DATA_MODELS / 'relations' / 'relations_refined_2025_11_19.json')
timeline = load_json(DATA_MODELS / 'timelines' / 'timeline_refined_2025_11_19.json')

# Analysis results
issues = {
    'critical': [],
    'high': [],
    'medium': [],
    'low': []
}

improvements = []

print("=" * 80)
print("COMPREHENSIVE ANALYSIS REPORT - 2025-11-19")
print("=" * 80)

# 1. Check for duplicate event IDs
print("\n1. DUPLICATE EVENT IDS")
print("-" * 80)
event_ids = [e['event_id'] for e in events['events']]
duplicates = [item for item, count in Counter(event_ids).items() if count > 1]

if duplicates:
    issues['critical'].append({
        'type': 'duplicate_event_ids',
        'count': len(duplicates),
        'details': duplicates
    })
    print(f"❌ CRITICAL: Found {len(duplicates)} duplicate event IDs")
    for dup_id in duplicates:
        matching = [e for e in events['events'] if e['event_id'] == dup_id]
        print(f"  - {dup_id}: {len(matching)} occurrences")
        for e in matching:
            print(f"    * {e.get('date', 'no date')} - {e.get('title', e.get('description', 'no title')[:60])}")
    
    improvements.append({
        'priority': 'critical',
        'issue': 'duplicate_event_ids',
        'action': 'Renumber duplicate event IDs to ensure uniqueness',
        'affected_ids': duplicates
    })
else:
    print("✓ No duplicate event IDs found")

# 2. Check for missing evidence references
print("\n2. MISSING EVIDENCE REFERENCES")
print("-" * 80)
missing_evidence = []
for event in events['events']:
    if 'evidence' not in event or not event['evidence']:
        missing_evidence.append({
            'event_id': event['event_id'],
            'date': event.get('date', 'no date'),
            'title': event.get('title', event.get('description', 'no title')[:60])
        })

if missing_evidence:
    issues['high'].append({
        'type': 'missing_evidence',
        'count': len(missing_evidence),
        'events': [e['event_id'] for e in missing_evidence]
    })
    print(f"⚠ HIGH: {len(missing_evidence)} events missing evidence references")
    for e in missing_evidence[:5]:
        print(f"  - {e['event_id']}: {e['title']}")
    if len(missing_evidence) > 5:
        print(f"  ... and {len(missing_evidence) - 5} more")
    
    improvements.append({
        'priority': 'high',
        'issue': 'missing_evidence',
        'action': 'Add evidence references to all events',
        'affected_count': len(missing_evidence)
    })
else:
    print("✓ All events have evidence references")

# 3. Check timeline metadata consistency
print("\n3. TIMELINE METADATA CONSISTENCY")
print("-" * 80)
timeline_meta = timeline['metadata']
actual_event_count = len(events['events'])
timeline_event_count = timeline_meta['total_events']

if actual_event_count != timeline_event_count:
    issues['medium'].append({
        'type': 'timeline_event_count_mismatch',
        'timeline_says': timeline_event_count,
        'actual_count': actual_event_count
    })
    print(f"⚠ MEDIUM: Timeline metadata says {timeline_event_count} events, but actual count is {actual_event_count}")
    improvements.append({
        'priority': 'medium',
        'issue': 'timeline_event_count_mismatch',
        'action': f'Update timeline metadata total_events from {timeline_event_count} to {actual_event_count}'
    })
else:
    print(f"✓ Timeline event count matches: {actual_event_count}")

# 4. Check for orphaned event references in timeline
print("\n4. ORPHANED EVENT REFERENCES IN TIMELINE")
print("-" * 80)
all_event_ids = set(event_ids)
orphaned_refs = []

for phase_key, phase in timeline['timeline_phases'].items():
    for event_id in phase['events']:
        if event_id not in all_event_ids:
            orphaned_refs.append({
                'phase': phase['phase_name'],
                'event_id': event_id
            })

if orphaned_refs:
    issues['high'].append({
        'type': 'orphaned_timeline_references',
        'count': len(orphaned_refs),
        'details': orphaned_refs
    })
    print(f"⚠ HIGH: {len(orphaned_refs)} orphaned event references in timeline")
    for ref in orphaned_refs[:5]:
        print(f"  - {ref['phase']}: {ref['event_id']}")
    
    improvements.append({
        'priority': 'high',
        'issue': 'orphaned_timeline_references',
        'action': 'Remove or correct orphaned event references in timeline phases'
    })
else:
    print("✓ No orphaned event references in timeline")

# 5. Check entity-event cross-references
print("\n5. ENTITY-EVENT CROSS-REFERENCES")
print("-" * 80)
entity_event_refs = defaultdict(list)

for entity_type in ['persons', 'organizations', 'trusts']:
    if entity_type in entities['entities']:
        for entity in entities['entities'][entity_type]:
            if 'timeline_events' in entity:
                entity_id = entity['entity_id']
                for event_id in entity['timeline_events']:
                    if event_id not in all_event_ids:
                        entity_event_refs[entity_id].append(event_id)

if entity_event_refs:
    issues['medium'].append({
        'type': 'invalid_entity_event_refs',
        'count': sum(len(v) for v in entity_event_refs.values()),
        'entities': len(entity_event_refs)
    })
    print(f"⚠ MEDIUM: {len(entity_event_refs)} entities reference non-existent events")
    for entity_id, event_ids in list(entity_event_refs.items())[:3]:
        print(f"  - {entity_id}: {len(event_ids)} invalid references")
    
    improvements.append({
        'priority': 'medium',
        'issue': 'invalid_entity_event_refs',
        'action': 'Clean up entity timeline_events references to match actual event IDs'
    })
else:
    print("✓ All entity event references are valid")

# 6. Analyze timeline phase coverage
print("\n6. TIMELINE PHASE COVERAGE")
print("-" * 80)
phase_events = set()
for phase_key, phase in timeline['timeline_phases'].items():
    phase_events.update(phase['events'])

events_not_in_timeline = all_event_ids - phase_events
if events_not_in_timeline:
    issues['medium'].append({
        'type': 'events_not_in_timeline',
        'count': len(events_not_in_timeline),
        'event_ids': list(events_not_in_timeline)
    })
    print(f"⚠ MEDIUM: {len(events_not_in_timeline)} events not assigned to any timeline phase")
    for event_id in list(events_not_in_timeline)[:5]:
        event = next((e for e in events['events'] if e['event_id'] == event_id), None)
        if event:
            print(f"  - {event_id}: {event.get('date', 'no date')} - {event.get('title', event.get('description', 'no title')[:50])}")
    
    improvements.append({
        'priority': 'medium',
        'issue': 'events_not_in_timeline',
        'action': 'Assign all events to appropriate timeline phases'
    })
else:
    print("✓ All events are assigned to timeline phases")

# 7. Check for financial impact consistency
print("\n7. FINANCIAL IMPACT CONSISTENCY")
print("-" * 80)
events_with_financial = [e for e in events['events'] if 'financial_impact' in e and e['financial_impact'] and e['financial_impact'] != 'unknown']
print(f"Events with financial impact: {len(events_with_financial)} / {len(events['events'])}")

# 8. Check GitHub Pages structure
print("\n8. GITHUB PAGES STRUCTURE")
print("-" * 80)
gh_pages_files = [
    'index.md',
    'application-1.md',
    'application-2.md',
    'application-3.md',
    'applications.md',
    'evidence-index.md'
]

missing_pages = []
for page in gh_pages_files:
    if not (BASE_DIR / page).exists():
        missing_pages.append(page)

if missing_pages:
    issues['high'].append({
        'type': 'missing_gh_pages',
        'files': missing_pages
    })
    print(f"⚠ HIGH: {len(missing_pages)} GitHub Pages files missing")
    for page in missing_pages:
        print(f"  - {page}")
else:
    print(f"✓ All {len(gh_pages_files)} GitHub Pages files present")

# 9. Summary of issues
print("\n" + "=" * 80)
print("ISSUES SUMMARY")
print("=" * 80)
total_issues = sum(len(v) for v in issues.values())
print(f"Total issues found: {total_issues}")
print(f"  - Critical: {len(issues['critical'])}")
print(f"  - High: {len(issues['high'])}")
print(f"  - Medium: {len(issues['medium'])}")
print(f"  - Low: {len(issues['low'])}")

# 10. Improvements summary
print("\n" + "=" * 80)
print("IMPROVEMENTS RECOMMENDED")
print("=" * 80)
print(f"Total improvements: {len(improvements)}")
for i, improvement in enumerate(improvements, 1):
    print(f"\n{i}. [{improvement['priority'].upper()}] {improvement['issue']}")
    print(f"   Action: {improvement['action']}")

# Save analysis report
report = {
    'timestamp': datetime.now().isoformat(),
    'issues': issues,
    'improvements': improvements,
    'statistics': {
        'total_entities': sum(len(entities['entities'].get(k, [])) for k in ['persons', 'organizations', 'trusts', 'platforms', 'domains']),
        'total_events': len(events['events']),
        'total_relations': sum(len(v) for v in relations['relations'].values()),
        'timeline_phases': len(timeline['timeline_phases']),
        'events_with_evidence': len(events['events']) - len(missing_evidence),
        'events_missing_evidence': len(missing_evidence)
    }
}

output_file = BASE_DIR / 'ANALYSIS_REPORT_2025_11_19_DETAILED.json'
with open(output_file, 'w') as f:
    json.dump(report, f, indent=2)

print(f"\n✓ Detailed analysis report saved to: {output_file}")
print("\n" + "=" * 80)
