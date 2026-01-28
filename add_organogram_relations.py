#!/usr/bin/env python3
"""
Add new relations from Rynette Organogram 2025-04-12 (How Sales Work)
This document reveals the sales process flow and system integrations
"""

import json
from datetime import datetime

# Load current relations
with open('data_models/relations/relations.json', 'r') as f:
    relations_data = json.load(f)

# Backup current file
backup_path = f'data_models/relations/relations.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open(backup_path, 'w') as f:
    json.dump(relations_data, f, indent=2)
print(f"Backup created: {backup_path}")

# New relations from Rynette Organogram 2025-04-12
new_operational_relations = [
    {
        "relation_id": "REL_OP_ORG_001",
        "relation_type": "operates_within",
        "source_entity": "PERSON_037",  # Kent
        "target_entity": "ORG_001",  # RWD
        "description": "Kent operates within RegimA Worldwide Distribution sales process",
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work",
            "Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.md"
        ],
        "ad_res_j7_evidence": [
            "ANNEXURES/JF07/Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.md"
        ],
        "evidence_verified": datetime.now().isoformat(),
        "confidence": 0.85,
        "evidence_strength": "strong"
    },
    {
        "relation_id": "REL_OP_ORG_002",
        "relation_type": "operates_within",
        "source_entity": "PERSON_038",  # EL
        "target_entity": "ORG_001",  # RWD
        "description": "EL operates within RegimA Worldwide Distribution sales process",
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work",
            "Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.json"
        ],
        "ad_res_j7_evidence": [
            "ANNEXURES/JF07/Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.json"
        ],
        "evidence_verified": datetime.now().isoformat(),
        "confidence": 0.75,
        "evidence_strength": "moderate"
    },
    {
        "relation_id": "REL_OP_ORG_003",
        "relation_type": "uses_system",
        "source_entity": "PERSON_037",  # Kent
        "target_entity": "PLATFORM_001",  # Shopify
        "description": "Kent uses Shopify for proforma invoice creation and order fulfillment",
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work"
        ],
        "ad_res_j7_evidence": [
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "evidence_verified": datetime.now().isoformat(),
        "confidence": 0.85,
        "evidence_strength": "strong"
    },
    {
        "relation_id": "REL_OP_ORG_004",
        "relation_type": "uses_system",
        "source_entity": "PERSON_038",  # EL
        "target_entity": "PLATFORM_001",  # Shopify
        "description": "EL uses Shopify for proforma invoice creation and order fulfillment",
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work"
        ],
        "ad_res_j7_evidence": [
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "evidence_verified": datetime.now().isoformat(),
        "confidence": 0.85,
        "evidence_strength": "strong"
    },
    {
        "relation_id": "REL_OP_ORG_005",
        "relation_type": "integrates_with",
        "source_entity": "PLATFORM_001",  # Shopify
        "target_entity": "PLATFORM_SAGE",  # Sage
        "description": "Shopify automatically pulls orders through to Sage for tax invoice generation",
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work"
        ],
        "ad_res_j7_evidence": [
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "evidence_verified": datetime.now().isoformat(),
        "confidence": 0.90,
        "evidence_strength": "conclusive",
        "significance": "Critical automation link - once order fulfilled in Shopify, tax invoice auto-created in Sage"
    },
    {
        "relation_id": "REL_OP_ORG_006",
        "relation_type": "uses_service",
        "source_entity": "ORG_001",  # RWD
        "target_entity": "PLATFORM_002",  # Courier Guy
        "description": "RWD uses Courier Guy for shipment and delivery",
        "evidence": [
            "Rynette Organogram 2025-04-12 - How Sales Work"
        ],
        "ad_res_j7_evidence": [
            "evidence_analysis/rynette_organogram_2025-04-12.md"
        ],
        "evidence_verified": datetime.now().isoformat(),
        "confidence": 0.90,
        "evidence_strength": "strong"
    }
]

# Add to control_relations or create new category
if 'operational_relations' not in relations_data:
    relations_data['operational_relations'] = []
relations_data['operational_relations'].extend(new_operational_relations)

# Update metadata
relations_data['metadata']['version'] = "16.0_ORGANOGRAM_INTEGRATION_2026_01_28"
relations_data['metadata']['last_updated'] = datetime.now().isoformat()
relations_data['metadata']['changes'] = "Added operational relations from Rynette Organogram 2025-04-12 showing sales process flow"

# Save updated relations
with open('data_models/relations/relations.json', 'w') as f:
    json.dump(relations_data, f, indent=2)

print(f"Added {len(new_operational_relations)} new operational relations")
print(f"New version: {relations_data['metadata']['version']}")
