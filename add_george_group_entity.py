#!/usr/bin/env python3
"""
Add George Group entity and update Ketoni/Bantjies relationship structure.
"""

import json
from pathlib import Path
from datetime import datetime

REPO_DIR = Path("/home/ubuntu/revstream1")

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def update_entities():
    """Update entities.json with George Group and corrected relationships."""
    entities_path = REPO_DIR / "data_models/entities/entities.json"
    data = load_json(entities_path)
    
    george_group_entity = {
        "entity_id": "ORG_GEORGE_GROUP",
        "name": "The George Group",
        "type": "holding_company",
        "role": "corporate_nexus",
        "significance": "Links Bantjies to Ketoni through corporate hierarchy",
        "key_personnel": {
            "ceo": {
                "name": "Kevin Michael Derrick",
                "also_director_of": "Ketoni Investment Holdings",
                "also_shareholder_of": "Ketoni Investment Holdings"
            },
            "cfo": {
                "name": "Danie Bantjies",
                "also_trustee_of": "Faucitt Family Trust (unlawfully appointed July 2024)",
                "also_accountant_for": "RegimA Group companies"
            }
        },
        "conflict_of_interest": {
            "description": "Bantjies as CFO reports to Kevin Derrick (CEO) who owns Ketoni which owes R18.75M to FFT where Bantjies is Trustee",
            "financial_stake": "R18.75M Ketoni payout to FFT",
            "loyalty_conflict": "Professional loyalty to Ketoni owner vs fiduciary duty to FFT beneficiaries"
        },
        "evidence": ["Company registration records", "Director appointment records"],
        "evidence_strength": "conclusive",
        "refinement_date": datetime.now().isoformat()
    }
    
    orgs = data["entities"]["organizations"]
    exists = any(org.get("entity_id") == "ORG_GEORGE_GROUP" for org in orgs)
    if not exists:
        orgs.append(george_group_entity)
        print("Added George Group entity")
    
    for org in orgs:
        if org.get("name") == "Ketoni Investment Holdings":
            org["owner_director"] = {
                "name": "Kevin Michael Derrick",
                "position": "Director and Shareholder",
                "also_ceo_of": "The George Group"
            }
            org["debt_to_fft"] = {
                "amount": "R18.75M",
                "payout_date": "May 2026",
                "note": "This is NOT Bantjies personal debt - Ketoni owes FFT"
            }
            org["bantjies_connection"] = {
                "relationship": "Bantjies is CFO of George Group where Kevin Derrick is CEO",
                "conflict": "Bantjies owes professional loyalty to Ketoni owner while being FFT Trustee"
            }
            print("Updated Ketoni entity with owner/director info")
    
    for person in data["entities"]["persons"]:
        if "Bantjies" in person.get("name", ""):
            person["conflict_of_interest"] = {
                "type": "CFO-Trustee conflict",
                "description": "As CFO of George Group, Bantjies reports to Kevin Derrick who owns Ketoni which owes R18.75M to FFT where Bantjies is Trustee",
                "note": "The R18.75M is NOT Bantjies personal debt - it is Ketoni debt to FFT",
                "professional_loyalty": "To Kevin Derrick (George Group CEO, Ketoni owner)",
                "fiduciary_duty": "To FFT beneficiaries (Daniel, Jacqui)"
            }
            person["corporate_positions"] = {
                "george_group": "CFO",
                "regima_group": "Accountant",
                "fft": "Trustee (unlawfully appointed by Rynette July 2024)"
            }
            if "debt_to_trust" in person:
                del person["debt_to_trust"]
            print("Updated Bantjies entity with corrected conflict structure")
    
    data["metadata"]["version"] = "37.0_KETONI_CORRECTION_2026_01_28"
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["changes"] = "Critical correction: R18.75M is Ketoni debt to FFT, not Bantjies personal debt. Added George Group entity."
    data["metadata"]["total_organizations"] = len(data["entities"]["organizations"])
    
    save_json(entities_path, data)
    print("Saved updated entities.json (v37.0)")

def update_relations():
    """Update relations.json with corrected debt relationships."""
    relations_path = REPO_DIR / "data_models/relations/relations.json"
    data = load_json(relations_path)
    
    new_relations = [
        {
            "relation_id": "REL_KETONI_FFT_DEBT",
            "relation_type": "financial_obligation",
            "source_entity": "ORG_KETONI",
            "target_entity": "ORG_FFT",
            "description": "Ketoni owes R18.75M payout to FFT (May 2026) - NOT Bantjies personal debt",
            "amount": "R18.75M",
            "payout_date": "2026-05",
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_BANTJIES_GEORGE_GROUP",
            "relation_type": "employment",
            "source_entity": "PERSON_BANTJIES",
            "target_entity": "ORG_GEORGE_GROUP",
            "description": "Bantjies is CFO of George Group",
            "significance": "Creates conflict with FFT Trustee role",
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_DERRICK_GEORGE_GROUP",
            "relation_type": "executive",
            "source_entity": "PERSON_DERRICK",
            "target_entity": "ORG_GEORGE_GROUP",
            "description": "Kevin Derrick is CEO of George Group",
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_DERRICK_KETONI",
            "relation_type": "ownership",
            "source_entity": "PERSON_DERRICK",
            "target_entity": "ORG_KETONI",
            "description": "Kevin Derrick is Director and Shareholder of Ketoni",
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_BANTJIES_CONFLICT",
            "relation_type": "conflict_of_interest",
            "source_entity": "PERSON_BANTJIES",
            "target_entity": "ORG_FFT",
            "description": "Bantjies has CFO-Trustee conflict: reports to Ketoni owner while being FFT Trustee",
            "financial_stake": "R18.75M Ketoni payout to FFT",
            "evidence_strength": "conclusive"
        }
    ]
    
    # Add to financial_relations if exists, otherwise create
    if "financial_relations" not in data["relations"]:
        data["relations"]["financial_relations"] = []
    
    # Get existing IDs
    existing_ids = set()
    for category in data["relations"].values():
        if isinstance(category, list):
            for r in category:
                if isinstance(r, dict) and "relation_id" in r:
                    existing_ids.add(r["relation_id"])
    
    for rel in new_relations:
        if rel["relation_id"] not in existing_ids:
            data["relations"]["financial_relations"].append(rel)
            print(f"Added relation: {rel['relation_id']}")
    
    data["metadata"]["version"] = "37.0_KETONI_CORRECTION_2026_01_28"
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["total_relations"] = sum(
        len(v) for v in data["relations"].values() if isinstance(v, list)
    )
    
    save_json(relations_path, data)
    print("Saved updated relations.json")

def main():
    print("=" * 70)
    print("GEORGE GROUP ENTITY AND KETONI RELATIONSHIP UPDATE")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    print("\n[1/2] Updating entities.json...")
    update_entities()
    
    print("\n[2/2] Updating relations.json...")
    update_relations()
    
    print("\n" + "=" * 70)
    print("UPDATE COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
