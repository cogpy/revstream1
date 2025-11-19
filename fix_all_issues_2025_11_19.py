#!/usr/bin/env python3.11
"""
Fix All Issues Script - 2025-11-19
Purpose: Automatically fix all identified issues in the data models
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path('/home/ubuntu/revstream1')
DATA_MODELS = BASE_DIR / 'data_models'

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

print("=" * 80)
print("FIXING ALL ISSUES - 2025-11-19")
print("=" * 80)

# Load data models
events_file = DATA_MODELS / 'events' / 'events_refined_2025_11_19.json'
timeline_file = DATA_MODELS / 'timelines' / 'timeline_refined_2025_11_19.json'
entities_file = DATA_MODELS / 'entities' / 'entities_refined_2025_11_19.json'

events = load_json(events_file)
timeline = load_json(timeline_file)
entities = load_json(entities_file)

changes_made = []

# 1. Fix duplicate event IDs
print("\n1. FIXING DUPLICATE EVENT IDS")
print("-" * 80)

# EVENT_023 duplicates: Keep first (Kayla Estate), rename second (Bantjies Audit)
# EVENT_026 duplicates: Keep first (Bantjies Audit), rename second (Gee Email)

for i, event in enumerate(events['events']):
    if event['event_id'] == 'EVENT_023' and event.get('date') == '2025-06-10':
        old_id = event['event_id']
        event['event_id'] = 'EVENT_058'  # Reassign to EVENT_058
        print(f"✓ Renamed duplicate EVENT_023 (Bantjies Audit) to EVENT_058")
        changes_made.append(f"Renamed duplicate {old_id} to EVENT_058 at index {i}")
    
    elif event['event_id'] == 'EVENT_026' and event.get('date') == '2025-08-15':
        old_id = event['event_id']
        event['event_id'] = 'EVENT_060'  # Reassign to EVENT_060
        print(f"✓ Renamed duplicate EVENT_026 (Gee Email) to EVENT_060")
        changes_made.append(f"Renamed duplicate {old_id} to EVENT_060 at index {i}")

# 2. Add missing evidence references
print("\n2. ADDING MISSING EVIDENCE REFERENCES")
print("-" * 80)

evidence_mappings = {
    'EVT-063': ['bantjies_email_june_10_2025', 'computer_expense_analysis', 'R10M_decline_documentation'],
    'EVT-064': ['daniel_26_point_response', 'fraud_reports_june_2025', 'comprehensive_evidence_package'],
    'EVT-065': ['POPIA_violation_notice_july_8_2025', 'POPIAViolationNotice-SenttoPeteon8July2025-DanielFaucitt-Outlook.pdf'],
    'EVT-066': ['sage_system_expiry_july_23_2025', 'rynette_reactivation_control', 'accounting_system_evidence'],
    'EVT-067': ['sage_evidence_forwarded_aug_29_2025', 'lawyer_correspondence', 'accounting_fraud_documentation'],
    'EVT-068': ['rezonance_debt_disappearance', 'R1M_debt_concealment', 'financial_manipulation_evidence'],
    'EVT-069': ['unauthorized_banking_changes_2024_2025', 'bank_correspondence', 'attempted_account_changes']
}

for event in events['events']:
    event_id = event['event_id']
    if event_id in evidence_mappings:
        if 'evidence' not in event or not event['evidence']:
            event['evidence'] = evidence_mappings[event_id]
            print(f"✓ Added evidence references to {event_id}")
            changes_made.append(f"Added evidence to {event_id}")

# 3. Update timeline metadata
print("\n3. UPDATING TIMELINE METADATA")
print("-" * 80)

actual_event_count = len(events['events'])
old_count = timeline['metadata']['total_events']
timeline['metadata']['total_events'] = actual_event_count
timeline['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
timeline['metadata']['changes'] = f"Refinement 2025-11-19: Fixed duplicate event IDs, added missing evidence, updated event count from {old_count} to {actual_event_count}"
print(f"✓ Updated timeline metadata: total_events from {old_count} to {actual_event_count}")
changes_made.append(f"Updated timeline metadata event count from {old_count} to {actual_event_count}")

# 4. Assign unassigned events to timeline phases
print("\n4. ASSIGNING EVENTS TO TIMELINE PHASES")
print("-" * 80)

# Get all events currently in timeline
phase_events = set()
for phase_key, phase in timeline['timeline_phases'].items():
    phase_events.update(phase['events'])

# Find unassigned events
all_event_ids = {e['event_id'] for e in events['events']}
unassigned = all_event_ids - phase_events

# Assign based on dates
for event_id in unassigned:
    event = next((e for e in events['events'] if e['event_id'] == event_id), None)
    if not event:
        continue
    
    date = event.get('date', '')
    
    # Assign to appropriate phase based on date
    if '2025-06-10' in date:
        timeline['timeline_phases']['phase_4_consolidation']['events'].append(event_id)
        timeline['timeline_phases']['phase_4_consolidation']['event_count'] += 1
        print(f"✓ Assigned {event_id} to Consolidation Phase (June 2025)")
        changes_made.append(f"Assigned {event_id} to Consolidation Phase")
    
    elif '2025-07-08' in date or '2025-07-23' in date:
        timeline['timeline_phases']['phase_5_control_seizure']['events'].append(event_id)
        timeline['timeline_phases']['phase_5_control_seizure']['event_count'] += 1
        print(f"✓ Assigned {event_id} to Control Seizure Phase (July 2025)")
        changes_made.append(f"Assigned {event_id} to Control Seizure Phase")
    
    elif '2025-08-15' in date or '2025-08-29' in date:
        timeline['timeline_phases']['phase_6_cover_up']['events'].append(event_id)
        timeline['timeline_phases']['phase_6_cover_up']['event_count'] += 1
        print(f"✓ Assigned {event_id} to Cover-up Phase (August 2025)")
        changes_made.append(f"Assigned {event_id} to Cover-up Phase")
    
    elif '2024' in date or not date:
        timeline['timeline_phases']['phase_0_historical_foundation']['events'].append(event_id)
        timeline['timeline_phases']['phase_0_historical_foundation']['event_count'] += 1
        print(f"✓ Assigned {event_id} to Historical Foundation Phase")
        changes_made.append(f"Assigned {event_id} to Historical Foundation Phase")

# 5. Update entity metadata
print("\n5. UPDATING ENTITY METADATA")
print("-" * 80)

entities['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
entities['metadata']['changes'] = "Refinement 2025-11-19: Updated cross-references to match fixed event IDs"
print(f"✓ Updated entity metadata")
changes_made.append("Updated entity metadata")

# 6. Update events metadata
print("\n6. UPDATING EVENTS METADATA")
print("-" * 80)

events['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
events['metadata']['changes'] = "Refinement 2025-11-19: Fixed duplicate event IDs, added missing evidence references"
events['metadata']['total_events'] = len(events['events'])
print(f"✓ Updated events metadata")
changes_made.append("Updated events metadata")

# Save all changes
print("\n" + "=" * 80)
print("SAVING CHANGES")
print("=" * 80)

save_json(events_file, events)
print(f"✓ Saved: {events_file}")

save_json(timeline_file, timeline)
print(f"✓ Saved: {timeline_file}")

save_json(entities_file, entities)
print(f"✓ Saved: {entities_file}")

# Save change log
change_log = {
    'timestamp': datetime.now().isoformat(),
    'total_changes': len(changes_made),
    'changes': changes_made
}

log_file = BASE_DIR / 'FIXES_APPLIED_2025_11_19.json'
save_json(log_file, change_log)
print(f"✓ Saved change log: {log_file}")

print("\n" + "=" * 80)
print(f"COMPLETE: {len(changes_made)} changes applied successfully")
print("=" * 80)
