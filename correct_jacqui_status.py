#!/usr/bin/env python3
"""
Correct Jacqui's fiduciary status in entity models.

Key correction: Jacqui has NOT breached her fiduciary duties.
Everything was carried out in secret by Rynette allegedly acting on behalf of Peter
without Jacqui's knowledge or consent. She is a victim of the same information
asymmetry as Daniel.

Evidence:
- Jacqui confronted Rynette on 15 May 2025 about the R1,035,000 debt
- Jacqui was kept in the dark about Rynette's secret operations
- Jacqui was not informed of card cancellations, mandate changes, etc.
- Jacqui is also a beneficiary under attack alongside Daniel
"""

import json
from datetime import datetime
from pathlib import Path

ENTITIES_FILE = Path("/home/ubuntu/revstream1/docs/data_models/entities/entities.json")

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")

def correct_jacqui_status(entities):
    """Correct Jacqui's fiduciary status to reflect she was kept uninformed."""
    persons = entities.get("entities", {}).get("persons", [])
    
    for person in persons:
        if person.get("entity_id") == "PERSON_004":
            # Update agent_type to reflect victim status
            person["agent_type"] = "victim"
            person["victim_status"] = {
                "description": "Kept uninformed by Rynette's secret operations allegedly on Peter's behalf",
                "evidence": [
                    "Confronted Rynette on 15 May 2025 about R1,035,000 debt",
                    "Not informed of card cancellations (7 June 2025)",
                    "Not informed of mandate change attempts",
                    "Accounts existed solely on Rynette's computer - no visibility",
                    "Also a beneficiary of FFT under attack alongside Daniel"
                ],
                "key_event": {
                    "date": "2025-05-15",
                    "description": "Jacqui confronted Rynette about ZAR 1,035,000 owed by RST to Rezonance since Feb 2023",
                    "jacqui_statement": "These funds were part of Kayla's estate and keeping them would be profiting from the proceeds of murder"
                }
            }
            
            # Correct fiduciary_roles if present
            if "fiduciary_roles" in person:
                for role in person["fiduciary_roles"]:
                    if role.get("status") == "BREACHED":
                        role["status"] = "ACTIVE - UNINFORMED VICTIM"
                        role["status_note"] = "Jacqui was kept uninformed by Rynette's secret operations - no breach"
            
            # Correct fiduciary_duties
            if "fiduciary_duties" in person:
                for duty in person["fiduciary_duties"]:
                    if duty.get("status") == "BREACHED":
                        duty["status"] = "ACTIVE - UNINFORMED VICTIM"
                        duty["status_note"] = "Jacqui was kept uninformed by Rynette's secret operations - no breach"
            
            # Add clarification note
            person["fiduciary_status_clarification"] = {
                "has_breached": False,
                "reason": "Everything was carried out in secret by Rynette allegedly acting on behalf of Peter without Jacqui's knowledge or consent",
                "same_position_as_daniel": True,
                "evidence_of_good_faith": [
                    "Confronted Rynette about unpaid debt (15 May 2025)",
                    "Stated keeping funds would be 'profiting from proceeds of murder'",
                    "Was not informed of secret card cancellations",
                    "Had no access to accounts (existed only on Rynette's computer)"
                ]
            }
            
            print("Corrected PERSON_004 (Jacqueline Faucitt):")
            print("  - agent_type: victim")
            print("  - fiduciary_status: ACTIVE - UNINFORMED VICTIM (not BREACHED)")
            print("  - Added victim_status with evidence")
            print("  - Added fiduciary_status_clarification")
            
    return entities

def main():
    print("=" * 70)
    print("Correcting Jacqui's Fiduciary Status")
    print("=" * 70)
    
    entities = load_json(ENTITIES_FILE)
    
    print("\nCorrection: Jacqui has NOT breached her fiduciary duties.")
    print("She was kept uninformed by Rynette's secret operations.\n")
    
    entities = correct_jacqui_status(entities)
    
    # Update metadata
    entities["metadata"]["version"] = "v33.1_JACQUI_STATUS_CORRECTED_2026_01_29"
    entities["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entities["metadata"]["changes"] = "Corrected Jacqui's fiduciary status - she was kept uninformed by Rynette's secret operations, not a breacher"
    
    save_json(ENTITIES_FILE, entities)
    
    print("\n" + "=" * 70)
    print("Correction Complete")
    print("=" * 70)

if __name__ == "__main__":
    main()
