#!/usr/bin/env python3
"""
Timeline Refinement Script - Update with Standardized Phases
Date: 2025-12-06
"""

import json
from datetime import datetime

# Load timeline
with open('data_models/timelines/timeline_refined_2025_12_05_v18.json', 'r') as f:
    timeline_data = json.load(f)

# Update metadata
timeline_data['metadata']['version'] = '19.0'
timeline_data['metadata']['last_updated'] = '2025-12-06'
timeline_data['metadata']['changes'] = 'Standardized phase naming across all timeline entries (2025-12-06)'

# Phase mapping for standardization
phase_mapping = {
    'Phase 0: Historical Foundation': 'PHASE_000',
    'Phase 6: Cover-up Phase': 'PHASE_006',
    'Phase 7: Debt Accumulation': 'PHASE_007'
}

# Standardize phase naming in timeline
timeline = timeline_data.get('timeline', [])
updated_count = 0

for entry in timeline:
    phase = entry.get('phase')
    
    if phase in phase_mapping:
        standardized_phase = phase_mapping[phase]
        entry['phase'] = standardized_phase
        updated_count += 1
        print(f"✓ Updated {entry.get('event_id')}: {phase} → {standardized_phase}")

# Save updated timeline
output_file = 'data_models/timelines/timeline_refined_2025_12_06_v19.json'
with open(output_file, 'w') as f:
    json.dump(timeline_data, f, indent=2)

print(f"\n✓ Timeline refined and saved to: {output_file}")
print(f"✓ Updated {updated_count} timeline entries with standardized phase naming")
print(f"✓ Version: 19.0")
print(f"✓ Date: 2025-12-06")
