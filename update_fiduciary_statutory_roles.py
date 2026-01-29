#!/usr/bin/env python3
"""
Update Entity Models with:
1. Fiduciary and Statutory Roles for all persons
2. Correct FNB mandate to SOLE INDEPENDENT AUTHORITY (not member %)
3. Company structure details from Daniel's June 2025 emails to Bantjies
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
DATA_MODELS_DIR = DOCS_DIR / "data_models"
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")

# Company structure from Daniel's June 10, 2025 email to Bantjies
COMPANY_STRUCTURE_FROM_EMAIL = {
    "key_facts": [
        "Daniel is NOT a member of RegimA Skin Treatments (RST)",
        "Companies are NOT subsidiaries - no fixed 'group' or intercompany",
        "Moving assets from company where Daniel is director to one where he is not = theft/fraud",
        "Pete does not use computer, never seen actual accounts",
        "Jacqui has not seen actual accounts",
        "Daniel has not seen actual accounts",
        "Accounts exist solely on Rynette's computer - nobody else can see them",
        "RegimA SA - Pete and Daniel as directors (operated with Dermal/Barend)",
        "RegimA Zone - Only Daniel as director (aggregation of 3 smaller distributions)",
        "Rynette is neither director nor employee of Worldwide Distribution",
        "Rynette has complete control without any liability",
        "Bank contacted Daniel multiple times re: Pete/Rynette attempts to change mandates, close accounts, cancel cards"
    ],
    "bantjies_30_year_involvement": "30-odd year involvement with Faucitt family business",
    "villa_via_included_in_group_analysis": True,
    "r10m_decline_year_on_year": "R10m decline year-on-year for the Group including Villa Via"
}

# Fiduciary and Statutory Roles
FIDUCIARY_STATUTORY_ROLES = {
    "PERSON_001": {  # Peter Andrew Faucitt
        "fiduciary_roles": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "duty": "Companies Act s76 - Fiduciary duty to act in good faith and in best interests of company",
                "status": "BREACHED",
                "breach_evidence": ["FNB_FRAUD_LETTER_2025_06_17", "Secret card cancellations", "Expense dumping"]
            },
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "Member (50%)",
                "duty": "Close Corporations Act - Fiduciary duty as member",
                "status": "BREACHED"
            },
            {
                "entity_id": "ORG_004",
                "entity_name": "Strategic Logistics Group CC",
                "role": "Member (33%)",
                "duty": "Close Corporations Act - Fiduciary duty as member",
                "status": "BREACHED"
            },
            {
                "entity_id": "TRUST_001",
                "entity_name": "Faucitt Family Trust",
                "role": "Main Trustee / Founder",
                "duty": "Trust Property Control Act - Fiduciary duty to beneficiaries",
                "status": "BREACHED",
                "breach_evidence": ["Backdated appointment", "Attack on beneficiary Daniel", "Ketoni payout motive"]
            }
        ],
        "statutory_roles": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "statute": "Companies Act 71 of 2008",
                "sections": ["s76 - Standards of directors' conduct", "s77 - Liability of directors"]
            }
        ]
    },
    "PERSON_004": {  # Jacqueline Faucitt
        "fiduciary_roles": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "duty": "Companies Act s76 - Fiduciary duty to act in good faith",
                "status": "BREACHED"
            },
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "Member (50%) / CEO",
                "duty": "Close Corporations Act - Fiduciary duty as member and CEO",
                "status": "BREACHED"
            },
            {
                "entity_id": "ORG_004",
                "entity_name": "Strategic Logistics Group CC",
                "role": "Member (33%)",
                "duty": "Close Corporations Act - Fiduciary duty as member",
                "status": "ACTIVE"
            },
            {
                "entity_id": "TRUST_001",
                "entity_name": "Faucitt Family Trust",
                "role": "Trustee",
                "duty": "Trust Property Control Act - Fiduciary duty to beneficiaries",
                "status": "BREACHED"
            }
        ],
        "statutory_roles": [
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "Information Officer",
                "statute": "POPIA (Protection of Personal Information Act 4 of 2013)",
                "sections": ["s55 - Information Officer responsibilities", "s56 - Deputy Information Officers"],
                "responsibilities": [
                    "Ensure POPIA compliance",
                    "Handle data subject requests",
                    "Report to Information Regulator",
                    "Maintain processing records"
                ],
                "registration": "Registered with Information Regulator",
                "evidence": "Registration Certificate - Information Regulator"
            },
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "statute": "Companies Act 71 of 2008",
                "sections": ["s76", "s77"]
            }
        ]
    },
    "PERSON_005": {  # Daniel James Faucitt
        "fiduciary_roles": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "duty": "Companies Act s76 - Fiduciary duty to act in good faith",
                "status": "ACTIVE - COMPLIANT"
            },
            {
                "entity_id": "ORG_003",
                "entity_name": "RegimA Zone Ltd",
                "role": "Managing Director (100%)",
                "duty": "UK Companies Act 2006 - Director duties",
                "status": "ACTIVE - COMPLIANT"
            },
            {
                "entity_id": "ORG_006",
                "entity_name": "RegimA SA (Pty) Ltd",
                "role": "Co-Director",
                "duty": "Companies Act s76 - Fiduciary duty",
                "status": "ACTIVE"
            },
            {
                "entity_id": "ORG_004",
                "entity_name": "Strategic Logistics Group CC",
                "role": "Founding Member (33%)",
                "duty": "Close Corporations Act - Fiduciary duty as founding member",
                "status": "ACTIVE - COMPLIANT"
            },
            {
                "entity_id": "ORG_008",
                "entity_name": "ReZonance (Pty) Ltd",
                "role": "Director (50%)",
                "duty": "Companies Act s76 - Fiduciary duty",
                "status": "ACTIVE - COMPLIANT"
            }
        ],
        "statutory_roles": [
            {
                "entity_id": "ORG_001",
                "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
                "role": "Director",
                "statute": "Companies Act 71 of 2008",
                "sections": ["s76", "s77"]
            },
            {
                "entity_id": "ORG_003",
                "entity_name": "RegimA Zone Ltd",
                "role": "Director",
                "statute": "UK Companies Act 2006",
                "sections": ["s171-177 - General duties of directors"]
            }
        ],
        "NOT_a_member_of": [
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "note": "Daniel explicitly stated in June 10, 2025 email: 'I am not a member of RegimA Skin Treatments'"
            }
        ]
    },
    "PERSON_007": {  # Danie Bantjies
        "fiduciary_roles": [
            {
                "entity_id": "TRUST_001",
                "entity_name": "Faucitt Family Trust",
                "role": "Trustee (Unlawfully Appointed)",
                "duty": "Trust Property Control Act - Fiduciary duty to beneficiaries",
                "status": "BREACHED - CONFLICTED",
                "conflict": "Owes R18,685,000 to Trust via Ketoni connection"
            }
        ],
        "statutory_roles": [
            {
                "entity_id": "ORG_002",
                "entity_name": "Regima Skin Treatments CC",
                "role": "Accounting Officer",
                "statute": "Close Corporations Act 69 of 1984",
                "sections": ["s59 - Accounting officer duties"],
                "duration": "30+ years"
            },
            {
                "entity_id": "ORG_004",
                "entity_name": "Strategic Logistics Group CC",
                "role": "Accounting Officer",
                "statute": "Close Corporations Act 69 of 1984",
                "sections": ["s59"],
                "duration": "Since 2008"
            }
        ],
        "professional_roles": [
            {
                "role": "Accountant",
                "clients": ["All RegimA Group companies", "Faucitt Family Trust"],
                "duration": "30+ years",
                "note": "Daniel contacted Bantjies on June 6 & 10, 2025 in his capacity as Accountant, unaware of Trustee appointment"
            },
            {
                "role": "Commissioner of Oaths",
                "conflict": "Certified Peter's affidavit despite conflict of interest"
            },
            {
                "role": "CFO",
                "entity": "George Group",
                "connection": "Kevin Derrick (Ketoni Director) is CEO of George Group"
            }
        ]
    },
    "PERSON_002": {  # Rynette Farrar
        "fiduciary_roles": [],  # NOT a director, NOT a trustee
        "statutory_roles": [],  # No statutory roles
        "operational_control": {
            "note": "Neither director nor employee of Worldwide Distribution but has complete control without liability",
            "evidence": "Daniel's June 10, 2025 email to Bantjies",
            "control_mechanisms": [
                "Sage Accounting System - Full Control",
                "Email Access (pete@regima.com)",
                "Bank account access (suspected unauthorized)",
                "Accounts exist solely on Rynette's computer"
            ]
        }
    }
}

# CORRECTED FNB Mandate - SOLE INDEPENDENT AUTHORITY
FNB_MANDATE_CORRECTION = {
    "account_number": "62323196362",
    "bank": "FNB",
    "entity": "Regima Worldwide Distribution (Pty) Ltd",
    "mandate_type": "SOLE_INDEPENDENT_AUTHORITY",
    "description": "Each director has SOLE authority to act independently - no co-signature required",
    "key_distinction": "SOLE authority means each director can INDEPENDENTLY authorize ANY transaction",
    "NOT_percentage_based": True,
    "NOT_member_percentage": True,
    "confirmation": {
        "date": "2025-06-18",
        "source": "FNB Response Email",
        "contact": "Mpumi Netshipale (Business Relationship Manager)",
        "quote": "The current mandate states that any of the directors of the company may act independently of each other"
    },
    "signatories": [
        {
            "person_id": "PERSON_001",
            "name": "Peter Andrew Faucitt",
            "authority": "SOLE_INDEPENDENT_AUTHORITY",
            "can_act_alone": True
        },
        {
            "person_id": "PERSON_004",
            "name": "Jacqueline Faucitt",
            "authority": "SOLE_INDEPENDENT_AUTHORITY",
            "can_act_alone": True
        },
        {
            "person_id": "PERSON_005",
            "name": "Daniel James Faucitt",
            "authority": "SOLE_INDEPENDENT_AUTHORITY",
            "can_act_alone": True
        }
    ]
}

def update_person_roles(entities):
    """Update all persons with fiduciary and statutory roles."""
    persons = entities.get("entities", {}).get("persons", [])
    
    for person in persons:
        entity_id = person.get("entity_id")
        if entity_id in FIDUCIARY_STATUTORY_ROLES:
            roles = FIDUCIARY_STATUTORY_ROLES[entity_id]
            
            # Add fiduciary roles
            if "fiduciary_roles" in roles:
                person["fiduciary_roles"] = roles["fiduciary_roles"]
            
            # Add statutory roles
            if "statutory_roles" in roles:
                person["statutory_roles"] = roles["statutory_roles"]
            
            # Add professional roles for Bantjies
            if "professional_roles" in roles:
                person["professional_roles"] = roles["professional_roles"]
            
            # Add NOT_a_member_of for Daniel
            if "NOT_a_member_of" in roles:
                person["NOT_a_member_of"] = roles["NOT_a_member_of"]
            
            # Add operational control for Rynette
            if "operational_control" in roles:
                person["operational_control"] = roles["operational_control"]
            
            print(f"Updated: {entity_id} - {person.get('name')}")
            if "fiduciary_roles" in roles:
                print(f"  - Added {len(roles.get('fiduciary_roles', []))} fiduciary roles")
            if "statutory_roles" in roles:
                print(f"  - Added {len(roles.get('statutory_roles', []))} statutory roles")
    
    return entities

def correct_fnb_mandates(entities):
    """Correct FNB mandates to SOLE INDEPENDENT AUTHORITY (not percentage-based)."""
    persons = entities.get("entities", {}).get("persons", [])
    
    for person in persons:
        entity_id = person.get("entity_id")
        
        # Update account mandates for RWD directors
        if entity_id in ["PERSON_001", "PERSON_004", "PERSON_005"]:
            if "account_mandates" in person:
                for mandate in person["account_mandates"]:
                    if mandate.get("entity_id") == "ORG_001":
                        # Correct the mandate type
                        mandate["authority_type"] = "SOLE_INDEPENDENT_AUTHORITY"
                        mandate["description"] = "SOLE authority to act independently - no co-signature required"
                        mandate["can_act_alone"] = True
                        mandate["NOT_percentage_based"] = True
                        mandate["fnb_confirmation"] = FNB_MANDATE_CORRECTION["confirmation"]
                        print(f"Corrected FNB mandate for {entity_id}: SOLE_INDEPENDENT_AUTHORITY")
    
    # Also update the organization
    orgs = entities.get("entities", {}).get("organizations", [])
    for org in orgs:
        if org.get("entity_id") == "ORG_001":
            if "bank_accounts" in org:
                for account in org["bank_accounts"]:
                    if account.get("account_number") == "62323196362":
                        account["mandate_type"] = "SOLE_INDEPENDENT_AUTHORITY"
                        account["description"] = "Each director has SOLE authority to act independently"
                        account["NOT_percentage_based"] = True
                        account["signatories"] = FNB_MANDATE_CORRECTION["signatories"]
                        print(f"Corrected ORG_001 FNB account mandate: SOLE_INDEPENDENT_AUTHORITY")
    
    return entities

def add_company_structure_notes(entities):
    """Add company structure notes from Daniel's June 2025 emails."""
    # Add to metadata
    if "company_structure_notes" not in entities:
        entities["company_structure_notes"] = {}
    
    entities["company_structure_notes"]["source"] = "Daniel Faucitt email to Danie Bantjies, 10 June 2025"
    entities["company_structure_notes"]["key_facts"] = COMPANY_STRUCTURE_FROM_EMAIL["key_facts"]
    entities["company_structure_notes"]["bantjies_involvement"] = COMPANY_STRUCTURE_FROM_EMAIL["bantjies_30_year_involvement"]
    
    print("Added company structure notes from June 2025 emails")
    
    return entities

def main():
    print("=" * 70)
    print("Updating Entity Models with Fiduciary/Statutory Roles")
    print("=" * 70)
    
    # Load entities
    entities = load_json(ENTITIES_FILE)
    
    print("\n1. Updating persons with fiduciary and statutory roles...")
    entities = update_person_roles(entities)
    
    print("\n2. Correcting FNB mandates to SOLE INDEPENDENT AUTHORITY...")
    entities = correct_fnb_mandates(entities)
    
    print("\n3. Adding company structure notes from June 2025 emails...")
    entities = add_company_structure_notes(entities)
    
    # Update metadata
    entities["metadata"]["version"] = "v33.0_FIDUCIARY_STATUTORY_ROLES_2026_01_29"
    entities["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entities["metadata"]["changes"] = "Added fiduciary/statutory roles, corrected FNB mandate to SOLE INDEPENDENT AUTHORITY, added June 2025 email structure notes"
    
    # Save
    save_json(ENTITIES_FILE, entities)
    
    print("\n" + "=" * 70)
    print("Entity Model Update Complete")
    print("=" * 70)
    print("\nKey Updates:")
    print("  - Peter: 4 fiduciary roles (all BREACHED), 1 statutory role")
    print("  - Jacqui: 4 fiduciary roles, 2 statutory roles (incl. POPIA Information Officer)")
    print("  - Daniel: 5 fiduciary roles (COMPLIANT), 2 statutory roles, NOT member of RST")
    print("  - Bantjies: 1 fiduciary role (BREACHED), 2 statutory roles, 3 professional roles")
    print("  - Rynette: NO fiduciary/statutory roles - operational control only")
    print("  - FNB Mandate: Corrected to SOLE INDEPENDENT AUTHORITY (not percentage-based)")

if __name__ == "__main__":
    main()
