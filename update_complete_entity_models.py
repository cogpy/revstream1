#!/usr/bin/env python3
"""
Complete Entity Model Update:
1. Add Daniel Faucitt as Director of RWD with FNB mandate access
2. Add SLG mandate roles for all members
3. Complete juristic entity models with CIPC/Windeed data
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

# CIPC/Windeed verified company data
COMPANY_DATA = {
    "ORG_001": {  # RWD
        "registration_number": "2011/005722/07",
        "name": "Regima Worldwide Distribution (Pty) Ltd",
        "abbreviation": "RWD",
        "entity_type": "private_company",
        "incorporation_date": "2011-03-11",
        "origin": "shelf_company_acquisition",
        "directors": [
            {"person_id": "PERSON_001", "name": "Peter Andrew Faucitt", "role": "Director", "status": "active"},
            {"person_id": "PERSON_004", "name": "Jacqueline Faucitt", "role": "Director", "status": "active"},
            {"person_id": "PERSON_005", "name": "Daniel James Faucitt", "role": "Director", "status": "active"}
        ],
        "accounting_officer": {"person_id": "PERSON_007", "name": "Danie Bantjies"},
        "registered_address": "50 Van Buuren Road, Bedfordview, 2008",
        "postal_address": "PO Box 9523, Edenglen, 1613",
        "bank_accounts": [
            {
                "bank": "FNB",
                "account_number": "62323196362",
                "mandate_type": "INDEPENDENT_DIRECTOR_AUTHORITY",
                "description": "Any director may act independently of each other",
                "co_signature_required": False,
                "signatories": ["PERSON_001", "PERSON_004", "PERSON_005"],
                "confirmation_date": "2025-06-18",
                "confirmed_by": "Mpumi Netshipale (FNB Business Relationship Manager)",
                "evidence": "FNB_RESPONSE_EMAIL_2025_06_18"
            }
        ]
    },
    "ORG_002": {  # RST
        "registration_number": "1992/005371/23",
        "name": "Regima Skin Treatments CC",
        "abbreviation": "RST",
        "entity_type": "close_corporation",
        "incorporation_date": "1992-02-26",
        "members": [
            {"person_id": "PERSON_001", "name": "Peter Andrew Faucitt", "percentage": "50%", "role": "Member"},
            {"person_id": "PERSON_004", "name": "Jacqueline Faucitt", "percentage": "50%", "role": "Member/CEO"}
        ],
        "accounting_officer": {"person_id": "PERSON_007", "name": "Danie Bantjies"},
        "registered_address": "50 Van Buuren Road, Bedfordview, 2008",
        "postal_address": "PO Box 9523, Edenglen, 1613",
        "popia_information_officer": {"person_id": "PERSON_004", "name": "Jacqueline Faucitt"}
    },
    "ORG_004": {  # SLG
        "registration_number": "2008/136496/23",
        "name": "Strategic Logistics Group CC",
        "abbreviation": "SLG",
        "entity_type": "close_corporation",
        "incorporation_date": "2008-06-27",
        "founding_member": {"person_id": "PERSON_005", "name": "Daniel James Faucitt"},
        "members": [
            {"person_id": "PERSON_001", "name": "Peter Andrew Faucitt", "percentage": "33%", "role": "Member"},
            {"person_id": "PERSON_004", "name": "Jacqueline Faucitt", "percentage": "33%", "role": "Member"},
            {"person_id": "PERSON_005", "name": "Daniel James Faucitt", "percentage": "33%", "role": "Founding Member"}
        ],
        "accounting_officer": {"person_id": "PERSON_007", "name": "Danie Bantjies"},
        "registered_address": "50 Van Buuren Road, Bedfordview, 2008",
        "bank_accounts": [
            {
                "bank": "FNB",
                "account_number": "TBD",
                "mandate_type": "MEMBER_AUTHORITY",
                "description": "Members have authority based on CC agreement",
                "signatories": ["PERSON_001", "PERSON_004", "PERSON_005"],
                "director_loan_authority": True,
                "evidence": "JF-STRATEGIC-LOGISTICS-ANALYSIS.md"
            }
        ],
        "financial_notes": {
            "stock_loss": "R5,400,000",
            "stock_loss_type": "stock_adjustment_disappeared",
            "debt_to_RST": "R13,000,000",
            "interest_paid_to_RST": "R414,334.09",
            "interest_payment_date": "2020-02-28"
        }
    },
    "ORG_005": {  # Villa Via
        "registration_number": "TBD",
        "name": "Villa Via",
        "abbreviation": "VV",
        "entity_type": "company",
        "members": [
            {"person_id": "PERSON_001", "name": "Peter Andrew Faucitt", "percentage": "50%", "role": "Director"},
            {"person_id": "OTHER", "name": "Other", "percentage": "50%", "role": "Director"}
        ],
        "financial_notes": {
            "monthly_rental_income": "R4,400,000",
            "net_profit": "R3,700,000",
            "profit_margin": "86%",
            "members_loan_account": "R22,800,000",
            "financial_year": "May 1 - April 30",
            "role": "Rental property / wealth extraction vehicle"
        },
        "excluded_from_group": True,
        "exclusion_reason": "Strategically kept outside 'Group' framing to hide profit extraction"
    },
    "ORG_006": {  # RegimA SA
        "registration_number": "2017/087935/07",
        "name": "RegimA SA (Pty) Ltd",
        "abbreviation": "RSA",
        "entity_type": "private_company",
        "incorporation_date": "2017",
        "directors": [
            {"person_id": "PERSON_001", "name": "Peter Andrew Faucitt", "role": "Co-Director"},
            {"person_id": "PERSON_005", "name": "Daniel James Faucitt", "role": "Co-Director"}
        ],
        "diversion_start_date": "2025-03-01",
        "role": "Revenue stream victim"
    },
    "ORG_003": {  # RegimA Zone Ltd (UK)
        "registration_number": "UK Company",
        "name": "RegimA Zone Ltd",
        "abbreviation": "RZL",
        "entity_type": "uk_private_company",
        "jurisdiction": "United Kingdom",
        "directors": [
            {"person_id": "PERSON_005", "name": "Daniel James Faucitt", "role": "Managing Director", "percentage": "100%"}
        ],
        "role": "Infrastructure owner - Shopify platforms",
        "platforms_owned": [
            "RegimA Worldwide Distribution (ZA)",
            "RegimA Zone (ZA)",
            "RegimA SA (ZA)",
            "Other E-Commerce Automation Platforms"
        ],
        "investment": {
            "monthly_cost": "$1,000 - $2,000 USD",
            "duration_months": 28,
            "total_investment": "R140,000 - R280,000"
        }
    },
    "ORG_008": {  # ReZonance
        "registration_number": "2017/081396/07",
        "name": "ReZonance (Pty) Ltd",
        "abbreviation": "RZN",
        "entity_type": "private_company",
        "incorporation_date": "2017",
        "directors": [
            {"person_id": "PERSON_005", "name": "Daniel James Faucitt", "role": "Director", "percentage": "50%"}
        ],
        "role": "IT services provider and creditor",
        "debt_owed": "R1,035,361.34",
        "part_of_kayla_estate": True
    },
    "ORG_009": {  # Adderory
        "registration_number": "2021/TBD",
        "name": "Adderory (Pty) Ltd",
        "abbreviation": "ADD",
        "entity_type": "private_company",
        "incorporation_date": "2021-04-30",
        "directors": [
            {"person_id": "PERSON_003", "name": "Adderory (Rynette's Son)", "role": "Director", "percentage": "100%"}
        ],
        "role": "Stock supplier - connected to R5.4M stock adjustment fraud",
        "related_companies": ["Luxury Products Online", "Luxuré"]
    },
    "ORG_015": {  # Ketoni
        "registration_number": "TBD",
        "name": "Ketoni Investment Holdings",
        "abbreviation": "KET",
        "entity_type": "investment_company",
        "directors": [
            {"person_id": "PERSON_014", "name": "Kevin Michael Derrick", "role": "Director"}
        ],
        "payout_obligation": {
            "creditor": "TRUST_001",
            "creditor_name": "Faucitt Family Trust",
            "amount": "ZAR 18,750,000",
            "due_date": "May 2026"
        },
        "george_group_connection": {
            "ceo": "Kevin Michael Derrick",
            "cfo": "Danie Bantjies"
        }
    }
}

# Daniel Faucitt enhancements
DANIEL_ENHANCEMENTS = {
    "directorships": [
        {
            "entity_id": "ORG_001",
            "entity_name": "Regima Worldwide Distribution (Pty) Ltd",
            "role": "Director",
            "status": "active",
            "evidence": ["JF-DAN-WITNESS.md", "JF14-CIPC-2021", "FNB_RESPONSE_EMAIL_2025_06_18"]
        },
        {
            "entity_id": "ORG_003",
            "entity_name": "RegimA Zone Ltd",
            "role": "Managing Director",
            "status": "active",
            "jurisdiction": "United Kingdom",
            "evidence": ["UK company records"]
        },
        {
            "entity_id": "ORG_006",
            "entity_name": "RegimA SA (Pty) Ltd",
            "role": "Co-Director",
            "status": "active",
            "evidence": ["CIPC records", "2017/087935/07"]
        },
        {
            "entity_id": "ORG_008",
            "entity_name": "ReZonance (Pty) Ltd",
            "role": "Director",
            "status": "active",
            "evidence": ["CIPC records"]
        }
    ],
    "memberships": [
        {
            "entity_id": "ORG_004",
            "entity_name": "Strategic Logistics Group CC",
            "role": "Founding Member",
            "percentage": "33%",
            "status": "active",
            "founded": "2008",
            "evidence": ["JF-DAN-WITNESS.md", "JF14-CIPC-2021"]
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
        },
        {
            "entity_id": "ORG_004",
            "entity_name": "Strategic Logistics Group CC",
            "bank": "FNB",
            "authority_type": "MEMBER_AUTHORITY",
            "description": "Member authority based on CC agreement - 66% vote for director loans",
            "director_loan_authority": True,
            "evidence": ["JF-STRATEGIC-LOGISTICS-ANALYSIS.md"]
        },
        {
            "entity_id": "ORG_003",
            "entity_name": "RegimA Zone Ltd",
            "bank": "UK Bank",
            "authority_type": "SOLE_SIGNATORY",
            "description": "Full control as sole owner and director",
            "evidence": ["UK company records"]
        }
    ]
}

def update_daniel_faucitt(entities):
    """Update Daniel Faucitt (PERSON_005) with RWD directorship and mandates."""
    persons = entities.get("entities", {}).get("persons", [])
    
    for person in persons:
        if person.get("entity_id") == "PERSON_005":
            # Update directorships
            person["directorships"] = DANIEL_ENHANCEMENTS["directorships"]
            
            # Add memberships (CC)
            person["memberships"] = DANIEL_ENHANCEMENTS["memberships"]
            
            # Update account mandates
            person["account_mandates"] = DANIEL_ENHANCEMENTS["account_mandates"]
            
            # Update relationships
            person["relationships"] = [
                "second_respondent_in_case",
                "owner_regima_zone_ltd",
                "director_of_RWD_ZA",
                "director_of_RSA_ZA",
                "director_of_ReZonance",
                "founding_member_of_SLG",
                "shopify_platform_owner",
                "shopify_platform_operator",
                "beneficiary_of_TRUST_001"
            ]
            
            print(f"Updated: PERSON_005 - Daniel James Faucitt")
            print(f"  - Added 4 directorships (including RWD)")
            print(f"  - Added 1 membership (SLG)")
            print(f"  - Added 3 account mandates (including FNB RWD)")
            break
    
    return entities

def update_juristic_entities(entities):
    """Update all juristic entities with CIPC/Windeed data."""
    orgs = entities.get("entities", {}).get("organizations", [])
    
    for org in orgs:
        entity_id = org.get("entity_id")
        if entity_id in COMPANY_DATA:
            company = COMPANY_DATA[entity_id]
            
            # Update with CIPC data
            org["registration_number"] = company.get("registration_number", org.get("registration_number"))
            org["entity_type"] = company.get("entity_type", org.get("entity_type"))
            
            if "incorporation_date" in company:
                org["incorporation_date"] = company["incorporation_date"]
            
            if "directors" in company:
                org["directors"] = company["directors"]
            
            if "members" in company:
                org["members"] = company["members"]
            
            if "accounting_officer" in company:
                org["accounting_officer"] = company["accounting_officer"]
            
            if "bank_accounts" in company:
                org["bank_accounts"] = company["bank_accounts"]
            
            if "registered_address" in company:
                org["registered_address"] = company["registered_address"]
            
            if "postal_address" in company:
                org["postal_address"] = company["postal_address"]
            
            if "financial_notes" in company:
                org["financial_notes"] = company["financial_notes"]
            
            if "popia_information_officer" in company:
                org["popia_information_officer"] = company["popia_information_officer"]
            
            if "founding_member" in company:
                org["founding_member"] = company["founding_member"]
            
            print(f"Updated: {entity_id} - {org.get('name')}")
    
    return entities

def add_missing_organizations(entities):
    """Add any missing organizations from COMPANY_DATA."""
    orgs = entities.get("entities", {}).get("organizations", [])
    existing_ids = [o.get("entity_id") for o in orgs]
    
    for entity_id, company in COMPANY_DATA.items():
        if entity_id not in existing_ids:
            new_org = {
                "entity_id": entity_id,
                "name": company.get("name"),
                "abbreviation": company.get("abbreviation"),
                "registration_number": company.get("registration_number"),
                "entity_type": company.get("entity_type"),
                **{k: v for k, v in company.items() if k not in ["name", "abbreviation", "registration_number", "entity_type"]}
            }
            orgs.append(new_org)
            print(f"Added: {entity_id} - {company.get('name')}")
    
    return entities

def update_peter_and_jacqui_slg(entities):
    """Update Peter and Jacqui with SLG membership."""
    persons = entities.get("entities", {}).get("persons", [])
    
    for person in persons:
        entity_id = person.get("entity_id")
        
        if entity_id == "PERSON_001":  # Peter
            if "memberships" not in person:
                person["memberships"] = []
            
            # Check if SLG membership exists
            slg_exists = any(m.get("entity_id") == "ORG_004" for m in person.get("memberships", []))
            if not slg_exists:
                person["memberships"].append({
                    "entity_id": "ORG_004",
                    "entity_name": "Strategic Logistics Group CC",
                    "role": "Member",
                    "percentage": "33%",
                    "status": "active",
                    "evidence": ["JF14-CIPC-2021"]
                })
            
            # Add SLG account mandate
            if "account_mandates" not in person:
                person["account_mandates"] = []
            
            slg_mandate_exists = any(m.get("entity_id") == "ORG_004" for m in person.get("account_mandates", []))
            if not slg_mandate_exists:
                person["account_mandates"].append({
                    "entity_id": "ORG_004",
                    "entity_name": "Strategic Logistics Group CC",
                    "bank": "FNB",
                    "authority_type": "MEMBER_AUTHORITY",
                    "description": "Member authority based on CC agreement",
                    "evidence": ["CC agreement"]
                })
            
            print(f"Updated: PERSON_001 - Peter with SLG membership and mandate")
        
        elif entity_id == "PERSON_004":  # Jacqui
            if "memberships" not in person:
                person["memberships"] = []
            
            # Check if SLG membership exists
            slg_exists = any(m.get("entity_id") == "ORG_004" for m in person.get("memberships", []))
            if not slg_exists:
                person["memberships"].append({
                    "entity_id": "ORG_004",
                    "entity_name": "Strategic Logistics Group CC",
                    "role": "Member",
                    "percentage": "33%",
                    "status": "active",
                    "evidence": ["JF14-CIPC-2021"]
                })
            
            # Add SLG account mandate
            if "account_mandates" not in person:
                person["account_mandates"] = []
            
            slg_mandate_exists = any(m.get("entity_id") == "ORG_004" for m in person.get("account_mandates", []))
            if not slg_mandate_exists:
                person["account_mandates"].append({
                    "entity_id": "ORG_004",
                    "entity_name": "Strategic Logistics Group CC",
                    "bank": "FNB",
                    "authority_type": "MEMBER_AUTHORITY",
                    "description": "Member authority based on CC agreement - 66% vote for director loans",
                    "director_loan_authority": True,
                    "evidence": ["JF-STRATEGIC-LOGISTICS-ANALYSIS.md"]
                })
            
            print(f"Updated: PERSON_004 - Jacqui with SLG membership and mandate")
    
    return entities

def main():
    print("=" * 70)
    print("Complete Entity Model Update")
    print("=" * 70)
    
    # Load entities
    entities = load_json(ENTITIES_FILE)
    
    print("\n1. Updating Daniel Faucitt with RWD directorship and FNB mandate...")
    entities = update_daniel_faucitt(entities)
    
    print("\n2. Updating Peter and Jacqui with SLG memberships and mandates...")
    entities = update_peter_and_jacqui_slg(entities)
    
    print("\n3. Updating juristic entities with CIPC/Windeed data...")
    entities = update_juristic_entities(entities)
    
    print("\n4. Adding any missing organizations...")
    entities = add_missing_organizations(entities)
    
    # Update metadata
    entities["metadata"]["version"] = "v32.0_COMPLETE_CIPC_MANDATES_2026_01_29"
    entities["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entities["metadata"]["changes"] = "Added Daniel as RWD Director with FNB mandate, completed SLG mandates, updated all juristic entities with CIPC/Windeed data"
    
    # Save
    save_json(ENTITIES_FILE, entities)
    
    print("\n" + "=" * 70)
    print("Entity Model Update Complete")
    print("=" * 70)
    print("\nKey Updates:")
    print("  - Daniel Faucitt: Director of RWD with FNB mandate access")
    print("  - Peter Faucitt: SLG membership and mandate added")
    print("  - Jacqui Faucitt: SLG membership and mandate added")
    print("  - All juristic entities updated with CIPC registration data")
    print("  - Bank account mandates documented for RWD and SLG")

if __name__ == "__main__":
    main()
