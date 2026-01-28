#!/usr/bin/env python3
"""
Add new events from Rynette Organogram 2025-04-12 (How Sales Work)
This document reveals the sales process flow and operational structure
"""

import json
from datetime import datetime

# Load current events
with open('data_models/events/events.json', 'r') as f:
    events_data = json.load(f)

# Backup current file
backup_path = f'data_models/events/events.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open(backup_path, 'w') as f:
    json.dump(events_data, f, indent=2)
print(f"Backup created: {backup_path}")

# New event from Rynette Organogram 2025-04-12
new_events = [
    {
        "event_id": "EVENT_ORG_001",
        "date": "2025-04-12",
        "title": "Rynette Organogram - Sales Process Documentation",
        "event_type": "operational_documentation",
        "category": "business_operations",
        "description": "Rynette creates/distributes 'How Sales Work' organogram documenting the complete sales process flow from customer order through delivery. Document reveals Kent and EL as key sales personnel, Shopify-to-Sage automation, and Courier Guy logistics integration.",
        "entities_involved": [
            "PERSON_002",  # Rynette
            "PERSON_037",  # Kent
            "PERSON_038",  # EL
            "ORG_001",     # RWD
            "PLATFORM_001", # Shopify
            "PLATFORM_002"  # Courier Guy
        ],
        "perpetrators": [],
        "victims": [],
        "location": "South Africa",
        "financial_impact": 0,
        "significance": "Documents operational structure showing dual personnel control (Kent/EL), system automation (Shopify→Sage), and third-party verification (Courier Guy). Reveals paper trail: Proforma Invoice → POP → Tax Invoice.",
        "evidence": [
            "Powerpoint-howsaleswork.pdf",
            "rynette_organogram_2025-04-12.md"
        ],
        "ad_res_j7_references": [
            "evidence_analysis/rynette_organogram_2025-04-12.md",
            "evidence_analysis/images/rynette_organogram_howsaleswork_2025-04-12.webp"
        ],
        "timeline_phase": "PHASE_3",
        "phase": "PHASE_3",
        "burden_of_proof": "civil_50%_exceeded",
        "evidence_enhanced": datetime.now().isoformat(),
        "refinement_date": datetime.now().isoformat(),
        "legal_relevance": {
            "companies_act": "Demonstrates operational structure and personnel roles",
            "popia": "Shows customer data handling through email, phone, delivery addresses",
            "tax_fraud": "Documents tax invoice generation process via Sage automation",
            "commercial_crime": "Establishes revenue flow documentation and paper trail"
        },
        "key_findings": [
            "Kent and EL handle all customer orders via phone/email",
            "Proforma invoices created in Shopify before payment",
            "POP (Proof of Payment) required before order fulfillment",
            "Shopify automatically syncs to Sage for tax invoice generation",
            "Courier Guy provides independent tracking and delivery verification"
        ]
    }
]

# Add new events
events_data['events'].extend(new_events)

# Update metadata
events_data['metadata']['version'] = "32.0_ORGANOGRAM_INTEGRATION_2026_01_28"
events_data['metadata']['last_updated'] = datetime.now().isoformat()
events_data['metadata']['changes'] = "Added EVENT_ORG_001 from Rynette Organogram 2025-04-12 documenting sales process flow"
events_data['metadata']['total_events'] = events_data['metadata'].get('total_events', 130) + len(new_events)

# Save updated events
with open('data_models/events/events.json', 'w') as f:
    json.dump(events_data, f, indent=2)

print(f"Added {len(new_events)} new events")
print(f"New version: {events_data['metadata']['version']}")
print(f"Total events: {events_data['metadata']['total_events']}")
