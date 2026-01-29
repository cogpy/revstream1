#!/usr/bin/env python3
"""
Update Master Entity Models with Account Mandates, Director Roles, and Holdings

This script adds comprehensive structured fields to all natural person entities:
1. shareholdings - entities they have shareholding in
2. directorships - entities they are directors of
3. account_mandates - bank account roles and authorities
4. trustee_positions - trust positions held
5. employment_roles - employment positions
6. fiduciary_duties - fiduciary responsibilities
"""

import json
from datetime import datetime
from pathlib import Path
from copy import deepcopy

# Paths
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
DATA_MODELS_DIR = DOCS_DIR / "data_models"
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    # Backup first
    backup_path = str(path) + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    with open(path, 'r') as f:
        with open(backup_path, 'w') as bf:
            bf.write(f.read())
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")

# Enhanced person data based on evidence
PERSON_ENHANCEMENTS = {
    "PERSON_001": {  # Peter Andrew Faucitt
        "shareholdings": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "percentage": "unknown",
                "status": "active",
                "evidence": ["CIPC records", "JF04"]
            },
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "percentage": "50%",
                "status": "active",
                "evidence": ["CIPC records", "JF04"]
            },
            {
                "entity_id": "ORG_004",
                "entity_name": "Strategic Logistics Group",
                "percentage": "33%",
                "status": "active",
                "evidence": ["CIPC records"]
            },
            {
                "entity_id": "ORG_005",
                "entity_name": "Villa Via",
                "percentage": "50%",
                "status": "active",
                "evidence": ["CIPC records"]
            }
        ],
        "directorships": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "status": "active",
                "appointment_date": "unknown",
                "evidence": ["CIPC records", "JF04", "FNB_RESPONSE_EMAIL_2025_06_18"]
            },
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "Member",
                "status": "active",
                "evidence": ["CIPC records"]
            },
            {
                "entity_id": "ORG_004",
                "entity_name": "Strategic Logistics Group",
                "role": "Director",
                "status": "active",
                "evidence": ["CIPC records"]
            },
            {
                "entity_id": "ORG_005",
                "entity_name": "Villa Via",
                "role": "Director",
                "status": "active",
                "evidence": ["CIPC records"]
            }
        ],
        "account_mandates": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "bank": "FNB",
                "account_number": "62323196362",
                "authority_type": "INDEPENDENT_DIRECTOR_AUTHORITY",
                "description": "Any director may act independently of each other",
                "co_signature_required": False,
                "evidence": ["FNB_RESPONSE_EMAIL_2025_06_18"],
                "fnb_confirmation_date": "2025-06-18",
                "fnb_contact": "Mpumi Netshipale (Business Relationship Manager)"
            }
        ],
        "trustee_positions": [
            {
                "trust_id": "TRUST_001",
                "trust_name": "Faucitt Family Trust",
                "role": "Main Trustee",
                "status": "active",
                "appointment_date": "2025-07-01",
                "backdated": True,
                "backdating_evidence": "Document signed 2025-08-11, backdated to 2025-07-01",
                "evidence": ["Trust documents", "JF06"]
            }
        ],
        "fiduciary_duties": [
            {
                "entity_id": "TRUST_001",
                "entity_name": "Faucitt Family Trust",
                "duty_type": "Trustee fiduciary duty",
                "beneficiaries": ["PERSON_001", "PERSON_004", "PERSON_005"],
                "status": "BREACHED",
                "breach_evidence": ["Interdict against beneficiaries", "Asset control actions"]
            },
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "duty_type": "Director fiduciary duty (Companies Act s76)",
                "status": "BREACHED",
                "breach_evidence": ["FNB fraud letter admission", "Revenue diversion"]
            }
        ]
    },
    "PERSON_002": {  # Rynette Farrar
        "shareholdings": [],
        "directorships": [],
        "account_mandates": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "bank": "FNB",
                "account_number": "62323196362",
                "authority_type": "OPERATIONAL_CONTROL",
                "description": "Controls accounting system (Sage) and email access",
                "co_signature_required": False,
                "evidence": ["SF2_Sage_Screenshots", "Email access evidence"],
                "sage_user_accounts": ["Pete@regima.com", "rynette@regima.zone"]
            },
            {
                "entity_id": "ABSA_ACCOUNTS",
                "entity_name": "Multiple ABSA Accounts",
                "bank": "ABSA",
                "account_number": "multiple",
                "authority_type": "SUSPECTED_UNAUTHORIZED",
                "description": "Potentially opened 8 ABSA accounts using stolen card",
                "evidence": ["Investigation pending"]
            }
        ],
        "trustee_positions": [],
        "employment_roles": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Financial Controller / Operations Manager",
                "status": "active",
                "evidence": ["SF2_Sage_Screenshots", "Email correspondence"]
            }
        ],
        "system_access": {
            "sage_accounting": {
                "subscription_owner": "RegimA Worldwide Distribution (Pty) Ltd",
                "user_accounts": ["Pete@regima.com", "rynette@regima.zone"],
                "expiry_date": "2025-07-23",
                "evidence": ["SF2_Sage_Screenshots"]
            },
            "email_access": {
                "pete_email": "Pete@regima.com",
                "own_email": "rynette@regima.zone",
                "evidence": "Sage screenshot 2025-06-20 shows Rynette with user account Pete@regima.com"
            }
        }
    },
    "PERSON_004": {  # Jacqueline Faucitt
        "shareholdings": [],
        "directorships": [
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "CEO",
                "status": "active",
                "evidence": ["CIPC records"]
            }
        ],
        "account_mandates": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "bank": "FNB",
                "account_number": "62323196362",
                "authority_type": "INDEPENDENT_DIRECTOR_AUTHORITY",
                "description": "Any director may act independently of each other",
                "co_signature_required": False,
                "evidence": ["FNB_RESPONSE_EMAIL_2025_06_18"],
                "fnb_confirmation_date": "2025-06-18"
            }
        ],
        "trustee_positions": [
            {
                "trust_id": "TRUST_001",
                "trust_name": "Faucitt Family Trust",
                "role": "Trustee",
                "status": "active",
                "evidence": ["Trust documents"]
            }
        ],
        "statutory_roles": [
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "Information Officer (POPIA)",
                "status": "active",
                "evidence": ["POPIA compliance records"]
            }
        ],
        "fiduciary_duties": [
            {
                "entity_id": "TRUST_001",
                "entity_name": "Faucitt Family Trust",
                "duty_type": "Trustee fiduciary duty",
                "beneficiaries": ["PERSON_001", "PERSON_004", "PERSON_005"],
                "status": "ACTIVE"
            },
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "duty_type": "CEO fiduciary duty",
                "status": "ACTIVE"
            }
        ]
    },
    "PERSON_005": {  # Daniel James Faucitt
        "shareholdings": [
            {
                "entity_id": "ORG_003",
                "entity_name": "RegimA Zone Ltd",
                "percentage": "100%",
                "status": "active",
                "jurisdiction": "United Kingdom",
                "evidence": ["UK company records", "JF01", "JF02"]
            },
            {
                "entity_id": "ORG_008",
                "entity_name": "ReZonance (Pty) Ltd",
                "percentage": "50%",
                "status": "active",
                "evidence": ["CIPC records"]
            }
        ],
        "directorships": [
            {
                "entity_id": "ORG_003",
                "entity_name": "RegimA Zone Ltd",
                "role": "Managing Director",
                "status": "active",
                "jurisdiction": "United Kingdom",
                "evidence": ["UK company records"]
            },
            {
                "entity_id": "ORG_008",
                "entity_name": "ReZonance (Pty) Ltd",
                "role": "Director",
                "status": "active",
                "evidence": ["CIPC records"]
            }
        ],
        "account_mandates": [
            {
                "entity_id": "ORG_003",
                "entity_name": "RegimA Zone Ltd",
                "bank": "UK Bank",
                "authority_type": "SOLE_SIGNATORY",
                "description": "Full control as sole owner and director",
                "evidence": ["UK company records"]
            }
        ],
        "trustee_positions": [],
        "beneficiary_positions": [
            {
                "trust_id": "TRUST_001",
                "trust_name": "Faucitt Family Trust",
                "role": "Beneficiary",
                "share": "1/3",
                "estimated_value": "ZAR 6,250,000 (from Ketoni payout)",
                "status": "UNDER_ATTACK",
                "attack_evidence": ["Interdict", "Curatorship fraud attempt"]
            }
        ],
        "platform_ownership": [
            {
                "platform": "Shopify Plus",
                "entity_id": "ORG_003",
                "role": "Owner and Payer",
                "monthly_cost": "$1,000 - $2,000 USD",
                "duration": "28 months",
                "total_investment": "R140,000 - R280,000",
                "evidence": ["JF01 - Shopify Plus email"]
            }
        ]
    },
    "PERSON_007": {  # Danie Bantjies
        "shareholdings": [],
        "directorships": [],
        "account_mandates": [],
        "trustee_positions": [
            {
                "trust_id": "TRUST_001",
                "trust_name": "Faucitt Family Trust",
                "role": "Trustee",
                "status": "active",
                "appointment_date": "2024-07",
                "appointed_by": "Rynette Farrar (unlawfully)",
                "appointment_timing": "T-10 months before ZAR 18.75M Ketoni payout",
                "evidence": ["Trust documents", "SF1_Bantjies_Debt_Documentation"]
            }
        ],
        "professional_roles": [
            {
                "role": "Accountant",
                "clients": ["ORG_001", "ORG_002", "ORG_004", "ORG_005", "ORG_006"],
                "duration": "30+ years with Faucitt family business",
                "evidence": ["JF03", "JF08"]
            },
            {
                "role": "Commissioner of Oaths",
                "status": "active",
                "misconduct": "Certified Peter's affidavit despite material omissions",
                "evidence": ["Court documents"]
            }
        ],
        "conflict_of_interest": {
            "triple_conflict": True,
            "roles": [
                "Trustee of Faucitt Family Trust",
                "Debtor to Trust (R18,685,000)",
                "Accountant for all RegimA companies",
                "Commissioner of Oaths"
            ],
            "motive": "Prevent discovery of R18,685,000 debt to trust",
            "ketoni_connection": {
                "colleague": "Kevin Michael Derrick (Ketoni Director)",
                "significance": "Links Bantjies appointment to ZAR 18.75M payout"
            }
        },
        "debts": [
            {
                "creditor_id": "TRUST_001",
                "creditor_name": "Faucitt Family Trust",
                "amount": "R18,685,000",
                "status": "outstanding",
                "significance": "Creates massive conflict of interest as Trustee",
                "evidence": ["SF1_Bantjies_Debt_Documentation", "Ketoni analysis"]
            }
        ]
    },
    "PERSON_003": {  # Adderory (Rynette's Son)
        "shareholdings": [
            {
                "entity_id": "ORG_009",
                "entity_name": "Adderory (Pty) Ltd",
                "percentage": "100%",
                "status": "active",
                "incorporation_date": "2021-04-30",
                "evidence": ["CIPC records", "SF5"]
            },
            {
                "entity_id": "ORG_010",
                "entity_name": "Luxury Products Online",
                "percentage": "100%",
                "status": "active",
                "incorporation_date": "2021-04-14",
                "evidence": ["CIPC records"]
            },
            {
                "entity_id": "ORG_011",
                "entity_name": "Luxuré",
                "percentage": "100%",
                "status": "active",
                "incorporation_date": "2021-04-29",
                "note": "Competitor to RégimA",
                "evidence": ["CIPC records"]
            }
        ],
        "directorships": [
            {
                "entity_id": "ORG_009",
                "entity_name": "Adderory (Pty) Ltd",
                "role": "Director",
                "status": "active",
                "evidence": ["CIPC records"]
            }
        ],
        "domain_ownership": [
            {
                "domain": "regimaskin.co.za",
                "registration_date": "2025-05-29",
                "purpose": "Customer hijacking infrastructure",
                "identity_fraud": "Registered using Daniel's identity",
                "evidence": ["Domain registration records", "JF08"]
            }
        ],
        "supply_relationships": [
            {
                "supplier_entity": "ORG_009",
                "customer_entity": "ORG_004",
                "product": "Stock (same type that disappeared)",
                "connection_to_fraud": "R5,400,000 stock adjustment",
                "evidence": ["SF3_Strategic_Logistics_Stock_Adjustment"]
            }
        ]
    },
    "PERSON_014": {  # Kevin Michael Derrick
        "shareholdings": [
            {
                "entity_id": "ORG_015",
                "entity_name": "Ketoni Investment Holdings",
                "percentage": "unknown",
                "status": "active",
                "evidence": ["Ketoni company records"]
            }
        ],
        "directorships": [
            {
                "entity_id": "ORG_015",
                "entity_name": "Ketoni Investment Holdings",
                "role": "Director",
                "status": "active",
                "evidence": ["Ketoni company records"]
            },
            {
                "entity_id": "ORG_GEORGE_GROUP",
                "entity_name": "George Group",
                "role": "CEO",
                "status": "active",
                "evidence": ["Company records"]
            }
        ],
        "professional_connections": [
            {
                "person_id": "PERSON_007",
                "person_name": "Danie Bantjies",
                "relationship": "Colleague at George Group",
                "significance": "Links Bantjies appointment to Ketoni payout"
            }
        ],
        "financial_obligations": [
            {
                "creditor_id": "TRUST_001",
                "creditor_name": "Faucitt Family Trust",
                "amount": "ZAR 18,750,000",
                "due_date": "May 2026",
                "type": "Ketoni payout obligation",
                "evidence": ["Ketoni investment documents"]
            }
        ]
    }
}

def update_person_entities(entities):
    """Update all person entities with enhanced fields."""
    persons = entities.get("entities", {}).get("persons", [])
    
    for person in persons:
        entity_id = person.get("entity_id")
        if entity_id in PERSON_ENHANCEMENTS:
            enhancements = PERSON_ENHANCEMENTS[entity_id]
            
            # Add new structured fields
            for field, value in enhancements.items():
                person[field] = value
            
            print(f"Enhanced: {entity_id} - {person.get('name')}")
    
    return entities

def add_account_mandates_summary(entities):
    """Add a summary of account mandates to metadata."""
    mandates_summary = {
        "fnb_rwd_mandate": {
            "entity": "Regima Worldwide Distribution (Pty) Ltd",
            "account": "62323196362",
            "bank": "FNB",
            "mandate_type": "INDEPENDENT_DIRECTOR_AUTHORITY",
            "description": "Any director may act independently of each other",
            "co_signature_required": False,
            "directors_with_authority": ["PERSON_001", "PERSON_004"],
            "confirmation_date": "2025-06-18",
            "confirmed_by": "Mpumi Netshipale (FNB Business Relationship Manager)",
            "evidence": "FNB_RESPONSE_EMAIL_2025_06_18"
        }
    }
    
    entities["metadata"]["account_mandates_summary"] = mandates_summary
    return entities

def add_corporate_structure_summary(entities):
    """Add a summary of corporate structure to metadata."""
    structure = {
        "trust": {
            "TRUST_001": {
                "name": "Faucitt Family Trust",
                "trustees": [
                    {"id": "PERSON_001", "name": "Peter Andrew Faucitt", "role": "Main Trustee", "status": "active"},
                    {"id": "PERSON_004", "name": "Jacqueline Faucitt", "role": "Trustee", "status": "active"},
                    {"id": "PERSON_007", "name": "Danie Bantjies", "role": "Trustee", "status": "active", "appointment": "unlawful"}
                ],
                "beneficiaries": [
                    {"id": "PERSON_001", "name": "Peter Andrew Faucitt", "share": "1/3"},
                    {"id": "PERSON_004", "name": "Jacqueline Faucitt", "share": "1/3"},
                    {"id": "PERSON_005", "name": "Daniel James Faucitt", "share": "1/3"}
                ],
                "assets": ["ORG_001", "ORG_005"],
                "pending_payout": {
                    "source": "Ketoni Investment Holdings",
                    "amount": "ZAR 18,750,000",
                    "due_date": "May 2026"
                }
            }
        },
        "companies": {
            "ORG_001": {
                "name": "Regima Worldwide Distribution (Pty) Ltd",
                "directors": ["PERSON_001", "PERSON_004"],
                "bank_mandate": "Independent director authority (FNB)"
            },
            "ORG_002": {
                "name": "Regima Skin Treatments CC",
                "members": [
                    {"id": "PERSON_001", "share": "50%"},
                    {"id": "PERSON_004", "share": "50%", "role": "CEO"}
                ]
            },
            "ORG_003": {
                "name": "RegimA Zone Ltd",
                "jurisdiction": "United Kingdom",
                "owner": "PERSON_005",
                "role": "Infrastructure owner (Shopify)"
            },
            "ORG_004": {
                "name": "Strategic Logistics Group",
                "directors": ["PERSON_001"],
                "shareholding": [
                    {"id": "PERSON_001", "share": "33%"}
                ]
            },
            "ORG_005": {
                "name": "Villa Via",
                "directors": ["PERSON_001"],
                "shareholding": [
                    {"id": "PERSON_001", "share": "50%"}
                ],
                "role": "Rental property / wealth extraction"
            }
        }
    }
    
    entities["metadata"]["corporate_structure_summary"] = structure
    return entities

def main():
    print("=" * 70)
    print("Updating Master Entity Models with Mandates, Roles, and Holdings")
    print("=" * 70)
    
    # Load entities
    entities = load_json(ENTITIES_FILE)
    
    print("\n1. Updating person entities with enhanced fields...")
    entities = update_person_entities(entities)
    
    print("\n2. Adding account mandates summary...")
    entities = add_account_mandates_summary(entities)
    
    print("\n3. Adding corporate structure summary...")
    entities = add_corporate_structure_summary(entities)
    
    # Update metadata
    entities["metadata"]["version"] = "v31.0_MANDATES_ROLES_HOLDINGS_2026_01_29"
    entities["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entities["metadata"]["changes"] = "Added comprehensive shareholdings, directorships, account mandates, trustee positions, and fiduciary duties to all natural person entities"
    
    # Save
    save_json(ENTITIES_FILE, entities)
    
    print("\n" + "=" * 70)
    print("Entity Model Update Complete")
    print("=" * 70)
    print(f"\nEnhanced persons: {len(PERSON_ENHANCEMENTS)}")
    print("New fields added:")
    print("  - shareholdings")
    print("  - directorships")
    print("  - account_mandates")
    print("  - trustee_positions")
    print("  - beneficiary_positions")
    print("  - fiduciary_duties")
    print("  - professional_roles")
    print("  - system_access")
    print("  - conflict_of_interest")
    print("  - debts")

if __name__ == "__main__":
    main()
