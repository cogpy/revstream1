#!/usr/bin/env python3
"""
Add new entities from Rynette Organogram 2025-04-12 (How Sales Work)
This document reveals the sales process flow and key personnel: Kent and EL
"""

import json
from datetime import datetime

# Load current entities
with open('data_models/entities/entities.json', 'r') as f:
    entities_data = json.load(f)

# Backup current file
backup_path = f'data_models/entities/entities.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open(backup_path, 'w') as f:
    json.dump(entities_data, f, indent=2)
print(f"Backup created: {backup_path}")

# New entities from Rynette Organogram 2025-04-12
new_persons = [
    {
        "entity_id": "PERSON_037",
        "name": "Kent (Unknown Surname)",
        "email": "kent@regima.zone",
        "role": "sales_order_processor",
        "agent_type": "operational_staff",
        "involvement_events": 1,
        "primary_actions": [
            "order_receipt_phone_email",
            "proforma_invoice_creation",
            "pop_receipt_processing",
            "order_fulfillment_marking"
        ],
        "relationships": [
            "employee_of_regima_group",
            "sage_user_rwd",
            "works_with_PERSON_038"
        ],
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work",
            "Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.md - kent@regima.zone user",
            "POPIA violation letters sent to Kent"
        ],
        "ad_res_j7_references": [
            "ANNEXURES/JF07/Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.md",
            "ANNEXURES/JF09/APR-SEP-2025.md - POPIA letters to Kent",
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "significance": "Key sales personnel handling customer orders, proforma invoices, and POP processing. Named in sales process flow diagram.",
        "evidence_enhanced": datetime.now().isoformat(),
        "evidence_strength": "moderate",
        "organogram_source": {
            "document": "Powerpoint-howsaleswork.pdf",
            "date": "2025-04-12",
            "role_in_flow": "Order receipt (phone/email), Proforma invoice creation in Shopify, POP receipt, Order fulfillment marking"
        }
    },
    {
        "entity_id": "PERSON_038",
        "name": "EL (Unknown Surname)",
        "email": "el@regimazone",
        "role": "sales_order_processor",
        "agent_type": "operational_staff",
        "involvement_events": 1,
        "primary_actions": [
            "order_receipt_phone_email",
            "proforma_invoice_creation",
            "pop_receipt_processing",
            "order_fulfillment_marking"
        ],
        "relationships": [
            "employee_of_regima_group",
            "sage_user_rwd",
            "works_with_PERSON_037"
        ],
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work",
            "Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.json - el@regimazone user"
        ],
        "ad_res_j7_references": [
            "ANNEXURES/JF07/Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.json",
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "significance": "Key sales personnel handling customer orders alongside Kent. Named in sales process flow diagram.",
        "evidence_enhanced": datetime.now().isoformat(),
        "evidence_strength": "moderate",
        "organogram_source": {
            "document": "Powerpoint-howsaleswork.pdf",
            "date": "2025-04-12",
            "role_in_flow": "Order receipt (phone/email), Proforma invoice creation in Shopify, POP receipt, Order fulfillment marking"
        }
    }
]

# New platform entities
new_platforms = [
    {
        "entity_id": "PLATFORM_002",
        "name": "Courier Guy",
        "type": "logistics_platform",
        "role": "delivery_service",
        "services": [
            "shipment_loading_portal",
            "tracking_number_generation",
            "parcel_collection",
            "delivery_notification",
            "return_handling"
        ],
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work"
        ],
        "ad_res_j7_references": [
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "significance": "Third-party logistics provider used for order fulfillment. Provides tracking and delivery verification.",
        "evidence_enhanced": datetime.now().isoformat(),
        "evidence_strength": "moderate",
        "organogram_source": {
            "document": "Powerpoint-howsaleswork.pdf",
            "date": "2025-04-12",
            "role_in_flow": "Shipment loading, tracking, collection, delivery, return handling"
        }
    }
]

# Add new persons
entities_data['entities']['persons'].extend(new_persons)

# Add new platforms (check if platforms key exists)
if 'platforms' not in entities_data['entities']:
    entities_data['entities']['platforms'] = []
entities_data['entities']['platforms'].extend(new_platforms)

# Update metadata
entities_data['metadata']['version'] = "38.0_ORGANOGRAM_INTEGRATION_2026_01_28"
entities_data['metadata']['last_updated'] = datetime.now().isoformat()
entities_data['metadata']['changes'] = "Added Kent (PERSON_037), EL (PERSON_038), and Courier Guy (PLATFORM_002) from Rynette Organogram 2025-04-12"
entities_data['metadata']['total_entities'] = entities_data['metadata'].get('total_entities', 86) + 3
entities_data['metadata']['total_persons'] = entities_data['metadata'].get('total_persons', 36) + 2

# Save updated entities
with open('data_models/entities/entities.json', 'w') as f:
    json.dump(entities_data, f, indent=2)

print(f"Added {len(new_persons)} new persons and {len(new_platforms)} new platforms")
print(f"New version: {entities_data['metadata']['version']}")
print(f"Total entities: {entities_data['metadata']['total_entities']}")
