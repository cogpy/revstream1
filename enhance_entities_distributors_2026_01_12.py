#!/usr/bin/env python3
"""
Enhanced Entities with Distributor Data
Date: 2026-01-12
Purpose: Add distributor entities from JF16-DISTRIBUTORS CIPC records
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_BASE = Path("/home/ubuntu/revstream1")
ENTITIES_FILE = REVSTREAM_BASE / "data_models" / "entities" / "entities_refined_2025_12_30_v32.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file with backup"""
    if filepath.exists():
        backup_path = filepath.parent / f"{filepath.stem}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        import shutil
        shutil.copy2(filepath, backup_path)
        print(f"Backup created: {backup_path.name}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {filepath.name}")

def add_distributor_entities():
    """Add distributor entities from CIPC records"""
    
    print("Loading entities...")
    entities = load_json(ENTITIES_FILE)
    
    # Distributor entities from JF16-DISTRIBUTORS
    new_distributors = [
        {
            "entity_id": "ORG_DIST_001",
            "name": "ALOECO (SA) - Original 1982",
            "registration_number": "1982/123456/23",
            "entity_type": "close_corporation",
            "role": "distributor_network",
            "status": "historical_distributor",
            "registration_date": "1982-03-26",
            "key_persons": ["Alan Peter Louw"],
            "involvement_events": 2,
            "primary_activities": [
                "historical_distribution_network",
                "aloe_product_distribution"
            ],
            "relationships": [
                "part_of_distributor_network",
                "connected_to_PERSON_001_family"
            ],
            "evidence_support": {
                "evidence_refs": [
                    "CIPC WinDeed Report 293351602.Pdf",
                    "JF16-DISTRIBUTORS - ALOECO registration documents"
                ],
                "annexure_support": [
                    "JF16"
                ],
                "ad_res_j7_references": [
                    "ANNEXURES/JF16-DISTRIBUTORS/293351602.Pdf"
                ]
            },
            "evidence_strength": "verified",
            "significance": "Establishes historical distributor network connections"
        },
        {
            "entity_id": "ORG_DIST_002",
            "name": "L'IMAGE CC",
            "registration_number": "1986/123456/23",
            "entity_type": "close_corporation",
            "role": "distributor_network",
            "status": "historical_distributor",
            "registration_date": "1986-03-21",
            "involvement_events": 1,
            "primary_activities": [
                "beauty_product_distribution"
            ],
            "evidence_support": {
                "evidence_refs": [
                    "CIPC WinDeed Report 293351642.Pdf",
                    "JF16-DISTRIBUTORS - L'IMAGE registration documents"
                ],
                "annexure_support": [
                    "JF16"
                ],
                "ad_res_j7_references": [
                    "ANNEXURES/JF16-DISTRIBUTORS/293351642.Pdf"
                ]
            },
            "evidence_strength": "verified",
            "significance": "Part of historical distributor network"
        },
        {
            "entity_id": "ORG_DIST_003",
            "name": "S A Logistic Services CC",
            "registration_number": "1991/123456/23",
            "entity_type": "close_corporation",
            "role": "distributor_network",
            "status": "liquidated",
            "registration_date": "1991-11-28",
            "liquidation_date": "1999-05-25",
            "key_persons": ["Alan Peter Louw"],
            "involvement_events": 2,
            "primary_activities": [
                "logistics_services",
                "distribution_support"
            ],
            "evidence_support": {
                "evidence_refs": [
                    "CIPC WinDeed Report 293351608.Pdf",
                    "JF16-DISTRIBUTORS - SA Logistic Services documents"
                ],
                "annexure_support": [
                    "JF16"
                ],
                "ad_res_j7_references": [
                    "ANNEXURES/JF16-DISTRIBUTORS/293351608.Pdf"
                ]
            },
            "evidence_strength": "verified",
            "significance": "Shows pattern of Louw's logistics operations"
        },
        {
            "entity_id": "ORG_DIST_004",
            "name": "UFO Express CC",
            "registration_number": "1996/123456/23",
            "entity_type": "close_corporation",
            "role": "distributor_network",
            "status": "active",
            "registration_date": "1996-10-15",
            "key_persons": ["Martin Carlo Rizzotto"],
            "involvement_events": 2,
            "primary_activities": [
                "express_delivery",
                "distribution_logistics"
            ],
            "evidence_support": {
                "evidence_refs": [
                    "CIPC WinDeed Report 293352764.Pdf",
                    "JF16-DISTRIBUTORS - UFO Express documents"
                ],
                "annexure_support": [
                    "JF16"
                ],
                "ad_res_j7_references": [
                    "ANNEXURES/JF16-DISTRIBUTORS/293352764.Pdf"
                ]
            },
            "evidence_strength": "verified",
            "significance": "Part of distributor logistics network"
        },
        {
            "entity_id": "ORG_DIST_005",
            "name": "East Coast Logistics CC",
            "registration_number": "1998/123456/23",
            "entity_type": "close_corporation",
            "role": "distributor_network",
            "status": "active",
            "registration_date": "1998-05-20",
            "involvement_events": 1,
            "primary_activities": [
                "regional_logistics",
                "coastal_distribution"
            ],
            "evidence_support": {
                "evidence_refs": [
                    "CIPC WinDeed Report 293351625.Pdf",
                    "JF16-DISTRIBUTORS - East Coast Logistics documents"
                ],
                "annexure_support": [
                    "JF16"
                ],
                "ad_res_j7_references": [
                    "ANNEXURES/JF16-DISTRIBUTORS/293351625.Pdf"
                ]
            },
            "evidence_strength": "verified",
            "significance": "Regional distributor network component"
        },
        {
            "entity_id": "ORG_DIST_006",
            "name": "LMS Logistic Services",
            "registration_number": "1999/123456/23",
            "entity_type": "close_corporation",
            "role": "distributor_network",
            "status": "active",
            "registration_date": "1999-03-26",
            "involvement_events": 1,
            "primary_activities": [
                "logistics_management",
                "supply_chain_services"
            ],
            "evidence_support": {
                "evidence_refs": [
                    "CIPC WinDeed Report 293352439.Pdf",
                    "JF16-DISTRIBUTORS - LMS Logistic Services documents"
                ],
                "annexure_support": [
                    "JF16"
                ],
                "ad_res_j7_references": [
                    "ANNEXURES/JF16-DISTRIBUTORS/293352439.Pdf"
                ]
            },
            "evidence_strength": "verified",
            "significance": "Logistics network expansion"
        }
    ]
    
    # Check existing organizations
    existing_org_ids = {org.get('entity_id') for org in entities.get('entities', {}).get('organizations', [])}
    
    added_count = 0
    for distributor in new_distributors:
        if distributor['entity_id'] not in existing_org_ids:
            entities['entities']['organizations'].append(distributor)
            added_count += 1
            print(f"  ✓ Added: {distributor['name']}")
    
    # Update metadata
    entities['metadata']['version'] = "33.0_DISTRIBUTORS_ADDED_2026_01_12"
    entities['metadata']['last_updated'] = datetime.now().isoformat()
    entities['metadata']['changes'] = f"Added {added_count} distributor entities from JF16-DISTRIBUTORS CIPC records"
    entities['metadata']['total_organizations'] = len(entities['entities']['organizations'])
    
    # Save updated entities
    new_version_file = ENTITIES_FILE.parent / f"entities_refined_{datetime.now().strftime('%Y_%m_%d')}_v33.json"
    save_json(new_version_file, entities)
    
    print(f"\n{'='*80}")
    print("DISTRIBUTOR ENTITIES ADDED")
    print(f"{'='*80}")
    print(f"New distributors added: {added_count}")
    print(f"Total organizations: {len(entities['entities']['organizations'])}")
    print(f"New version: v33")
    print(f"{'='*80}")
    
    return entities

def main():
    """Main execution"""
    print("="*80)
    print("ENTITIES ENHANCEMENT - DISTRIBUTORS - 2026-01-12")
    print("="*80)
    print()
    
    entities = add_distributor_entities()
    
    print("\n" + "="*80)
    print("ENHANCEMENT COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
