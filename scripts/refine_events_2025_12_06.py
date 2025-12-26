#!/usr/bin/env python3
"""
Event Refinement Script - Standardize Phase Naming
Date: 2025-12-06
"""

import json
from datetime import datetime

# Load events
with open('data_models/events/events_refined_2025_12_05_v27.json', 'r') as f:
    events_data = json.load(f)

# Update metadata
events_data['metadata']['version'] = '28.0'
events_data['metadata']['last_updated'] = '2025-12-06'
events_data['metadata']['changes'] = 'Standardized phase naming across all events (2025-12-06)'

# Phase mapping for standardization
phase_mapping = {
    'Phase 0: Historical Foundation': 'PHASE_000',
    'Phase 6: Cover-up Phase': 'PHASE_006',
    'Phase 7: Debt Accumulation': 'PHASE_007'
}

# Standardize phase naming
events = events_data.get('events', [])
updated_count = 0

for event in events:
    # Check both possible phase field names
    phase = event.get('timeline_phase') or event.get('phase')
    
    if phase in phase_mapping:
        standardized_phase = phase_mapping[phase]
        
        # Update both fields to ensure consistency
        if 'timeline_phase' in event:
            event['timeline_phase'] = standardized_phase
        if 'phase' in event:
            event['phase'] = standardized_phase
        
        updated_count += 1
        print(f"✓ Updated {event.get('event_id')}: {phase} → {standardized_phase}")

# Save updated events
output_file = 'data_models/events/events_refined_2025_12_06_v28.json'
with open(output_file, 'w') as f:
    json.dump(events_data, f, indent=2)

print(f"\n✓ Events refined and saved to: {output_file}")
print(f"✓ Updated {updated_count} events with standardized phase naming")
print(f"✓ Version: 28.0")
print(f"✓ Date: 2025-12-06")
