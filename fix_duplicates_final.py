#!/usr/bin/env python3.11
"""
Final fix for duplicate event IDs - assign truly unique IDs
"""

import json
from pathlib import Path

BASE_DIR = Path('/home/ubuntu/revstream1')
events_file = BASE_DIR / 'data_models' / 'events' / 'events_refined_2025_11_19.json'

with open(events_file, 'r') as f:
    events = json.load(f)

# Find all existing event IDs to avoid conflicts
all_ids = {e['event_id'] for e in events['events']}

# Find next available EVENT_XXX number
max_num = 0
for event_id in all_ids:
    if event_id.startswith('EVENT_'):
        try:
            num = int(event_id.split('_')[1])
            max_num = max(max_num, num)
        except:
            pass

next_id = max_num + 1

print("Fixing duplicate event IDs...")
print(f"Next available ID: EVENT_{next_id:03d}")

# Fix EVENT_058 duplicate (keep first, rename second)
for i, event in enumerate(events['events']):
    if event['event_id'] == 'EVENT_058' and event.get('title') == 'Bantjies Learns of Criminal Matters':
        old_id = event['event_id']
        new_id = f'EVENT_{next_id:03d}'
        event['event_id'] = new_id
        print(f"✓ Renamed {old_id} (Bantjies Learns) to {new_id} at index {i}")
        next_id += 1

# Fix EVENT_060 duplicate (keep first, rename second)
for i, event in enumerate(events['events']):
    if event['event_id'] == 'EVENT_060' and 'Gee Email' in event.get('title', ''):
        old_id = event['event_id']
        new_id = f'EVENT_{next_id:03d}'
        event['event_id'] = new_id
        print(f"✓ Renamed {old_id} (Gee Email) to {new_id} at index {i}")
        next_id += 1

# Update metadata
events['metadata']['last_updated'] = '2025-11-19'
events['metadata']['changes'] = 'Refinement 2025-11-19: Fixed all duplicate event IDs with truly unique identifiers'

# Save
with open(events_file, 'w') as f:
    json.dump(events, f, indent=2)

print(f"\n✓ Saved: {events_file}")

# Verify
all_ids_after = [e['event_id'] for e in events['events']]
from collections import Counter
duplicates = [item for item, count in Counter(all_ids_after).items() if count > 1]

if duplicates:
    print(f"\n❌ Still have duplicates: {duplicates}")
else:
    print(f"\n✅ All {len(all_ids_after)} event IDs are now unique!")
