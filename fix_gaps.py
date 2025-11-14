import json
from datetime import datetime

# Load existing data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load data
entities = load_json('/home/ubuntu/revstream1/data_models/entities/entities_refined.json')
timeline = load_json('/home/ubuntu/revstream1/data_models/timelines/timeline_enhanced.json')

print("=== FIXING IDENTIFIED GAPS ===\n")

# 1. Add missing entities
print("1. Adding missing entities...")

# Add TRUST_001
trust_001 = {
    "entity_id": "TRUST_001",
    "name": "Family Trust",
    "entity_type": "trust",
    "agent_type": "victim",
    "role": "trust_entity",
    "trustees": ["PERSON_001", "PERSON_007"],
    "beneficiaries": ["legitimate_beneficiaries"],
    "financial_impact": {
        "trust_violations": "R2,851,247.35+",
        "asset_misappropriation": "unknown_amount"
    }
}

# Add PLATFORM_001
platform_001 = {
    "entity_id": "PLATFORM_001",
    "name": "Shopify Platform (regima.zone)",
    "entity_type": "digital_platform",
    "agent_type": "instrument_of_revenue",
    "role": "revenue_platform",
    "owner": "ORG_003",
    "operators": ["PERSON_004", "PERSON_005"],
    "financial_details": {
        "monthly_revenue": "R1,000,000+",
        "investment": "R140,000 - R280,000",
        "duration": "28_months"
    }
}

# Add DOMAIN_001 and DOMAIN_002
domain_001 = {
    "entity_id": "DOMAIN_001",
    "name": "regima.zone",
    "entity_type": "domain",
    "agent_type": "legitimate_asset",
    "role": "legitimate_domain",
    "owner": "ORG_003",
    "registration_date": "2023-07"
}

domain_002 = {
    "entity_id": "DOMAIN_002",
    "name": "regimaskin.co.za",
    "entity_type": "domain",
    "agent_type": "instrument_of_fraud",
    "role": "fraudulent_domain",
    "owner": "PERSON_003",
    "registration_date": "2025-05-29",
    "purpose": "identity_fraud_customer_hijacking"
}

# Check if organizations list exists, if not create it
if 'trusts' not in entities['entities']:
    entities['entities']['trusts'] = []
if 'platforms' not in entities['entities']:
    entities['entities']['platforms'] = []
if 'domains' not in entities['entities']:
    entities['entities']['domains'] = []

# Add new entities
entities['entities']['trusts'].append(trust_001)
entities['entities']['platforms'].append(platform_001)
entities['entities']['domains'].extend([domain_001, domain_002])

print(f"  - Added TRUST_001: Family Trust")
print(f"  - Added PLATFORM_001: Shopify Platform")
print(f"  - Added DOMAIN_001: regima.zone")
print(f"  - Added DOMAIN_002: regimaskin.co.za")

# 2. Fix duplicate timeline events
print("\n2. Fixing duplicate timeline events...")

phases = timeline['timeline_phases']
duplicates_removed = 0

for phase_key, phase_data in phases.items():
    events = phase_data.get('events', [])
    # Remove duplicates while preserving order
    unique_events = []
    seen = set()
    for event in events:
        if event not in seen:
            unique_events.append(event)
            seen.add(event)
        else:
            duplicates_removed += 1
    
    phase_data['events'] = unique_events

print(f"  - Removed {duplicates_removed} duplicate event entries from timeline")

# 3. Add orphaned events to appropriate phases
print("\n3. Adding orphaned events to timeline...")

orphaned_events = ['EVENT_H009', 'EVENT_029', 'EVENT_H010', 'EVENT_023', 'EVENT_028']

# EVENT_H009 - Adderory company registration (April 2021) -> Historical Foundation
if 'EVENT_H009' not in phases['phase_0_historical_foundation']['events']:
    phases['phase_0_historical_foundation']['events'].append('EVENT_H009')
    print(f"  - Added EVENT_H009 to Historical Foundation Phase")

# EVENT_023 - Chantal letter (Jan 2025) -> Debt Accumulation Phase
if 'EVENT_023' not in phases['phase_0_5_debt_accumulation']['events']:
    phases['phase_0_5_debt_accumulation']['events'].append('EVENT_023')
    print(f"  - Added EVENT_023 to Debt Accumulation Phase")

# EVENT_028 - Cloud IT removal (Apr 22 2025) -> Foundation Phase
if 'EVENT_028' not in phases['phase_1_foundation']['events']:
    phases['phase_1_foundation']['events'].append('EVENT_028')
    print(f"  - Added EVENT_028 to Foundation Phase")

# EVENT_029 - needs to be placed based on date
if 'EVENT_029' not in phases['phase_3_escalation']['events']:
    phases['phase_3_escalation']['events'].append('EVENT_029')
    print(f"  - Added EVENT_029 to Escalation Phase")

# EVENT_H010 - Historical event -> Historical Foundation
if 'EVENT_H010' not in phases['phase_0_historical_foundation']['events']:
    phases['phase_0_historical_foundation']['events'].append('EVENT_H010')
    print(f"  - Added EVENT_H010 to Historical Foundation Phase")

# 4. Update metadata
print("\n4. Updating metadata...")

today = datetime.now().strftime("%Y-%m-%d")
entities['metadata']['version'] = "5.0"
entities['metadata']['last_updated'] = today
entities['metadata']['changes'] = "Added missing entities (TRUST_001, PLATFORM_001, DOMAIN_001, DOMAIN_002), fixed timeline duplicates, added orphaned events"

timeline['metadata']['version'] = "4.0"
timeline['metadata']['last_updated'] = today
timeline['metadata']['changes'] = "Removed duplicate events, added orphaned events to appropriate phases"

print(f"  - Updated entities to version 5.0")
print(f"  - Updated timeline to version 4.0")
print(f"  - Set last_updated to {today}")

# Save updated data
save_json('/home/ubuntu/revstream1/data_models/entities/entities_refined.json', entities)
save_json('/home/ubuntu/revstream1/data_models/timelines/timeline_enhanced.json', timeline)

print("\n=== GAPS FIXED SUCCESSFULLY ===")
print(f"Files updated:")
print(f"  - /home/ubuntu/revstream1/data_models/entities/entities_refined.json")
print(f"  - /home/ubuntu/revstream1/data_models/timelines/timeline_enhanced.json")
