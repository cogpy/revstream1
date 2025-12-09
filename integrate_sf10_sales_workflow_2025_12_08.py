#!/usr/bin/env python3
"""
Integrate SF10 Sales Workflow PowerPoint into Data Models
Date: 2025-12-08
Purpose: Update entities with SF10 sales workflow evidence (Shopify-Sage-Courier Guy integration)
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
ENTITIES_PATH = REVSTREAM_PATH / "data_models" / "entities"

def load_json_file(filepath):
    """Load JSON file with error handling"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def save_json_file(data, filepath):
    """Save JSON file with pretty formatting"""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error saving {filepath}: {e}")
        return False

def update_entities_with_sf10(entities_data):
    """Update entities with SF10 sales workflow evidence"""
    if not entities_data or "entities" not in entities_data:
        return entities_data
    
    # Update PERSON_004 (Kent) with operational role
    kent_found = False
    for entity in entities_data["entities"].get("persons", []):
        if entity.get("entity_id") == "PERSON_004" or entity.get("full_name") == "Kent":
            kent_found = True
            entity["entity_id"] = "PERSON_004"
            entity["full_name"] = "Kent"
            
            # Add SF10 evidence reference
            if "evidence_support" not in entity:
                entity["evidence_support"] = {}
            
            entity["evidence_support"]["evidence_refs"] = entity["evidence_support"].get("evidence_refs", []) + [
                "SF10 - Sales workflow PowerPoint showing Kent's role in order processing"
            ]
            
            entity["evidence_support"]["annexure_support"] = list(set(
                entity["evidence_support"].get("annexure_support", []) + ["SF10"]
            ))
            
            # Add operational role
            entity["role"] = "Customer Order Handler"
            entity["responsibilities"] = [
                "Receive customer orders via phone/email",
                "Create proforma invoices in Shopify",
                "Verify proof of payment",
                "Trigger order fulfillment in Shopify"
            ]
            
            # Add system access
            entity["system_access"] = ["Shopify"]
            
            print("✓ Updated PERSON_004 (Kent) with SF10 operational role")
    
    if not kent_found:
        # Create Kent entity
        kent_entity = {
            "entity_id": "PERSON_004",
            "full_name": "Kent",
            "role": "Customer Order Handler",
            "responsibilities": [
                "Receive customer orders via phone/email",
                "Create proforma invoices in Shopify",
                "Verify proof of payment",
                "Trigger order fulfillment in Shopify"
            ],
            "system_access": ["Shopify"],
            "evidence_support": {
                "evidence_refs": ["SF10 - Sales workflow PowerPoint"],
                "annexure_support": ["SF10"]
            }
        }
        entities_data["entities"]["persons"].append(kent_entity)
        print("✓ Created PERSON_004 (Kent) with SF10 operational role")
    
    # Update PERSON_005 (Eldridge Davids / EL) with operational role
    el_found = False
    for entity in entities_data["entities"].get("persons", []):
        if entity.get("entity_id") == "PERSON_005" or "Eldridge" in entity.get("full_name", ""):
            el_found = True
            entity["entity_id"] = "PERSON_005"
            if "full_name" not in entity:
                entity["full_name"] = "Eldridge Davids"
            entity["aliases"] = list(set(entity.get("aliases", []) + ["EL"]))
            
            # Add SF10 evidence reference
            if "evidence_support" not in entity:
                entity["evidence_support"] = {}
            
            entity["evidence_support"]["evidence_refs"] = entity["evidence_support"].get("evidence_refs", []) + [
                "SF10 - Sales workflow PowerPoint showing EL's role in order processing"
            ]
            
            entity["evidence_support"]["annexure_support"] = list(set(
                entity["evidence_support"].get("annexure_support", []) + ["SF10", "SF2A"]
            ))
            
            # Add operational role
            entity["role"] = "Customer Order Handler"
            entity["responsibilities"] = [
                "Receive customer orders via phone/email",
                "Create proforma invoices in Shopify",
                "Verify proof of payment",
                "Trigger order fulfillment in Shopify"
            ]
            
            # Add system access
            entity["system_access"] = list(set(entity.get("system_access", []) + ["Shopify", "Sage"]))
            
            # Cross-reference with SF2A
            entity["cross_reference_sf2a"] = "Eldridge Davids shown in Sage user access screenshot (SF2A)"
            
            print("✓ Updated PERSON_005 (Eldridge Davids / EL) with SF10 operational role")
    
    if not el_found:
        # Create EL entity
        el_entity = {
            "entity_id": "PERSON_005",
            "full_name": "Eldridge Davids",
            "aliases": ["EL"],
            "role": "Customer Order Handler",
            "responsibilities": [
                "Receive customer orders via phone/email",
                "Create proforma invoices in Shopify",
                "Verify proof of payment",
                "Trigger order fulfillment in Shopify"
            ],
            "system_access": ["Shopify", "Sage"],
            "cross_reference_sf2a": "Eldridge Davids shown in Sage user access screenshot (SF2A)",
            "evidence_support": {
                "evidence_refs": [
                    "SF10 - Sales workflow PowerPoint",
                    "SF2A - Sage user access screenshot"
                ],
                "annexure_support": ["SF10", "SF2A"]
            }
        }
        entities_data["entities"]["persons"].append(el_entity)
        print("✓ Created PERSON_005 (Eldridge Davids / EL) with SF10 operational role")
    
    # Update ORG_001 (RegimA Worldwide Distribution) with system integration
    for entity in entities_data["entities"].get("organizations", []):
        if entity.get("entity_id") == "ORG_001":
            # Add SF10 evidence reference
            if "evidence_support" not in entity:
                entity["evidence_support"] = {}
            
            entity["evidence_support"]["evidence_refs"] = entity["evidence_support"].get("evidence_refs", []) + [
                "SF10 - Sales workflow PowerPoint showing Shopify-Sage-Courier Guy integration"
            ]
            
            entity["evidence_support"]["annexure_support"] = list(set(
                entity["evidence_support"].get("annexure_support", []) + ["SF10"]
            ))
            
            # Add systems integration
            if "systems_integration" not in entity:
                entity["systems_integration"] = {}
            
            entity["systems_integration"]["shopify_sage_courier_guy"] = {
                "description": "Automated three-system integration for e-commerce operations",
                "shopify": {
                    "function": "E-commerce platform",
                    "capabilities": [
                        "Order management",
                        "Proforma invoice generation",
                        "Order fulfillment tracking"
                    ]
                },
                "sage": {
                    "function": "Accounting system",
                    "capabilities": [
                        "Automatic order pull from Shopify",
                        "Tax invoice generation",
                        "Automated email to customers"
                    ],
                    "integration": "Automatic data transfer when order marked as fulfilled"
                },
                "courier_guy": {
                    "function": "Logistics and delivery",
                    "capabilities": [
                        "Shipment tracking",
                        "Delivery notifications",
                        "Return management"
                    ]
                },
                "workflow": "Customer → Shopify → Sage → Customer (Tax Invoice) + Courier Guy → Customer (Delivery)",
                "evidence": "SF10"
            }
            
            # Add professional operations evidence
            entity["professional_operations"] = {
                "automated_accounting": "Shopify-Sage integration for tax invoice generation",
                "tax_compliance": "Automated tax invoice generation and email",
                "logistics_integration": "Courier Guy tracking and notifications",
                "evidence": "SF10"
            }
            
            print("✓ Updated ORG_001 (RegimA Worldwide Distribution) with SF10 systems integration")
    
    # Update metadata
    entities_data["metadata"]["last_sf10_integration"] = datetime.now().isoformat()
    entities_data["metadata"]["version"] = "13.0_SF10_INTEGRATED_2025_12_08"
    entities_data["metadata"]["sf10_key_findings"] = "Shopify-Sage-Courier Guy automated integration"
    
    return entities_data

def main():
    """Main execution function"""
    print("=" * 80)
    print("INTEGRATE SF10 SALES WORKFLOW POWERPOINT SCRIPT - 2025-12-08")
    print("=" * 80)
    print()
    print("SF10 Key Findings:")
    print("  - Automated Shopify-Sage-Courier Guy integration")
    print("  - Tax invoices generated automatically when orders fulfilled")
    print("  - Professional e-commerce operations")
    print("  - Kent and EL identified as customer order handlers")
    print("  - Demonstrates impact of Sage expiry (SF2B) on operations")
    print()
    
    # Load latest data models
    print("Loading latest data models...")
    entities_file = ENTITIES_PATH / "entities_sf9_integrated_2025_12_09.json"
    
    entities = load_json_file(entities_file)
    
    # Update with SF10 evidence
    print("\nUpdating entities with SF10 evidence...")
    entities_updated = update_entities_with_sf10(entities)
    
    # Save updated data
    timestamp = datetime.now().strftime("%Y_%m_%d")
    
    print("\nSaving updated data models...")
    save_json_file(entities_updated, ENTITIES_PATH / f"entities_sf10_integrated_{timestamp}.json")
    
    print("\n" + "=" * 80)
    print("SF10 SALES WORKFLOW INTEGRATION COMPLETE")
    print("=" * 80)
    print("\nKey Updates:")
    print("✓ PERSON_004 (Kent): Added operational role and Shopify access")
    print("✓ PERSON_005 (EL): Added operational role, Shopify/Sage access, SF2A cross-ref")
    print("✓ ORG_001 (RWW): Added Shopify-Sage-Courier Guy integration details")
    print("\nNext steps:")
    print("1. Update GitHub Pages with SF10 analysis")
    print("2. Commit and push changes")

if __name__ == "__main__":
    main()
