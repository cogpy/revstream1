#!/usr/bin/env python3
"""
Legal Framework Integration Script
Maps the 4 major legal theories to entities, relations, and events
Creates juristic timeline matrix
"""

import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Legal theories from the framework document
LEGAL_THEORIES = {
    "THEORY_001": {
        "id": "THEORY_001",
        "name": "Abuse of Ex Parte Procedure",
        "legal_foundation": [
            "Schlesinger v Schlesinger 1979 (4) SA 342 (W)",
            "NDPP v Basson",
            "Powell v Van der Merwe",
            "Uniform Rule 6(4)"
        ],
        "elements": [
            "Duty of utmost good faith (uberrima fides)",
            "Material non-disclosure",
            "Suppression of adverse facts",
            "Facts discoverable with minimal diligence"
        ],
        "narrative_omissions": [
            "Actual control structure (Bantjies financial control)",
            "Jacqui reacting to debt owed to Kayla's estate",
            "Retaliation chronology (card cancellations, sabotage)",
            "UK → SA payment flows (not SA → UK)",
            "Revenues outweighed IT expenses",
            "Daniel's role in UK compliance, logistics, operations"
        ]
    },
    "THEORY_002": {
        "id": "THEORY_002",
        "name": "Retaliatory Motive (Malice)",
        "legal_foundation": [
            "Beinash v Wixley 1997 (3) SA 721 (SCA)",
            "Phillips v Botha",
            "Abuse of process doctrine",
            "Interim interdict requirements"
        ],
        "elements": [
            "Litigation for ulterior purpose",
            "Temporal proximity as evidence",
            "Chronological inference of malice",
            "Retaliation not bona fide corporate protection"
        ],
        "temporal_patterns": [
            {
                "trigger": "Confrontation re debt",
                "response": "Data wiped",
                "days_later": 5
            },
            {
                "trigger": "Daniel's fraud report",
                "response": "Cards cancelled",
                "days_later": 1
            },
            {
                "trigger": "Exposing Villa Via",
                "response": "Audit blocked",
                "days_later": 5
            },
            {
                "trigger": "Signing Main Trustee document",
                "response": "Interdict launched",
                "days_later": 2
            }
        ]
    },
    "THEORY_003": {
        "id": "THEORY_003",
        "name": "Corporate Misconduct (Companies Act)",
        "legal_foundation": [
            "Companies Act s 76(3) - Duty to act with care, good faith, proper purpose",
            "Companies Act s 162 - Delinquency of directors"
        ],
        "elements": [
            "Duty to act with care",
            "Duty to act in good faith",
            "Duty to act for proper purpose",
            "Duty to act in best interests of company",
            "Gross abuse",
            "Dishonesty",
            "Wilful misconduct"
        ],
        "misconduct_types": [
            "Sabotage",
            "Unauthorised payments",
            "Asset dissipation",
            "Operational destruction",
            "Misrepresentations in affidavits"
        ]
    },
    "THEORY_004": {
        "id": "THEORY_004",
        "name": "Trustee Misconduct (Trust Property Control Act)",
        "legal_foundation": [
            "Trust Property Control Act",
            "Common law fiduciary duties"
        ],
        "elements": [
            "Utmost good faith",
            "Duty to avoid conflicts",
            "Duty to act impartially",
            "Duty to account",
            "Duty not to profit improperly",
            "Duty to preserve trust assets",
            "Duty to disclose material facts"
        ],
        "misconduct_types": [
            "Trustee deception",
            "Hidden trustee roles",
            "Debts owed to trust",
            "Actions harming beneficiaries",
            "Retaliation against accountability demands"
        ]
    }
}

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def map_events_to_legal_theories(events_data):
    """Map events to legal theories based on event characteristics"""
    
    theory_event_mapping = {
        "THEORY_001": [],  # Ex Parte Abuse
        "THEORY_002": [],  # Retaliatory Motive
        "THEORY_003": [],  # Corporate Misconduct
        "THEORY_004": []   # Trustee Misconduct
    }
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id")
        event_type = event.get("event_type", "")
        crime_type = event.get("crime_type", "")
        description = event.get("description", "").lower()
        
        # Map to THEORY_001 (Ex Parte Abuse) - events showing material non-disclosure
        if any(keyword in description for keyword in [
            "concealment", "suppression", "omission", "misrepresentation",
            "control structure", "payment flow", "financial control"
        ]):
            theory_event_mapping["THEORY_001"].append(event_id)
        
        # Map to THEORY_002 (Retaliatory Motive) - events showing retaliation pattern
        if any(keyword in description for keyword in [
            "retaliation", "sabotage", "cancellation", "destruction",
            "confrontation", "response to", "following"
        ]) or event_type in [
            "evidence_tampering", "operational_sabotage", "system_sabotage"
        ]:
            theory_event_mapping["THEORY_002"].append(event_id)
        
        # Map to THEORY_003 (Corporate Misconduct) - Companies Act violations
        if event_type in [
            "financial_manipulation", "accounting_fraud", "unauthorized_transfer",
            "profit_extraction", "asset_dissipation", "operational_sabotage"
        ] or crime_type in [
            "fraud", "theft", "financial_crime"
        ]:
            theory_event_mapping["THEORY_003"].append(event_id)
        
        # Map to THEORY_004 (Trustee Misconduct) - Trust law violations
        if "trust" in description or event_type in [
            "trust_violations", "fiduciary_breach", "beneficiary_manipulation"
        ]:
            theory_event_mapping["THEORY_004"].append(event_id)
    
    return theory_event_mapping

def create_juristic_timeline_matrix(events_data, timeline_data, theory_event_mapping):
    """Create timeline matrix showing legal element mapping"""
    
    juristic_matrix = []
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id")
        date = event.get("date")
        
        # Find which legal theories this event supports
        supporting_theories = []
        for theory_id, event_list in theory_event_mapping.items():
            if event_id in event_list:
                supporting_theories.append({
                    "theory_id": theory_id,
                    "theory_name": LEGAL_THEORIES[theory_id]["name"]
                })
        
        if supporting_theories:  # Only include events that map to legal theories
            juristic_matrix.append({
                "event_id": event_id,
                "date": date,
                "event_type": event.get("event_type"),
                "description": event.get("description"),
                "financial_impact": event.get("financial_impact"),
                "crime_type": event.get("crime_type"),
                "legal_theories_supported": supporting_theories,
                "evidence_references": event.get("evidence", []),
                "involved_entities": event.get("involved_entities", [])
            })
    
    # Sort by date
    juristic_matrix.sort(key=lambda x: x["date"] if x["date"] else "9999-99-99")
    
    return juristic_matrix

def create_interim_interdict_test_mapping(events_data, entities_data, relations_data):
    """Map events to the 4 elements of interim interdict test"""
    
    interdict_test = {
        "prima_facie_right": {
            "element": "Prima facie right",
            "counter_argument": "Applicant had no operational role; systems controlled by third parties",
            "supporting_events": [],
            "supporting_entities": [],
            "supporting_relations": []
        },
        "irreparable_harm": {
            "element": "Reasonable apprehension of irreparable harm",
            "counter_argument": "Harm flowed from applicant's side; applicant manufactured harm",
            "supporting_events": [],
            "supporting_entities": [],
            "supporting_relations": []
        },
        "balance_of_convenience": {
            "element": "Balance of convenience",
            "counter_argument": "Jacqui is only Responsible Person for EU compliance; interdict caused greater harm",
            "supporting_events": [],
            "supporting_entities": [],
            "supporting_relations": []
        },
        "no_alternative_remedy": {
            "element": "No adequate alternative remedy",
            "counter_argument": "Internal remedies available; mediation underway",
            "supporting_events": [],
            "supporting_entities": [],
            "supporting_relations": []
        }
    }
    
    # Map events to interdict test elements
    for event in events_data.get("events", []):
        event_id = event.get("event_id")
        event_type = event.get("event_type", "")
        description = event.get("description", "").lower()
        
        # Prima facie right - events showing control by others
        if "control" in description or "bantjies" in description or "rynette" in description:
            interdict_test["prima_facie_right"]["supporting_events"].append(event_id)
        
        # Irreparable harm - events showing harm from applicant
        if event_type in ["operational_sabotage", "system_sabotage", "evidence_tampering"]:
            interdict_test["irreparable_harm"]["supporting_events"].append(event_id)
        
        # Balance of convenience - events showing operational necessity
        if "shopify" in description or "revenue" in description or "compliance" in description:
            interdict_test["balance_of_convenience"]["supporting_events"].append(event_id)
        
        # No alternative remedy - events showing mediation/internal processes
        if "mediation" in description or "report" in description or "confrontation" in description:
            interdict_test["no_alternative_remedy"]["supporting_events"].append(event_id)
    
    return interdict_test

def main():
    """Main integration function"""
    print("=" * 80)
    print("LEGAL FRAMEWORK INTEGRATION")
    print("=" * 80)
    
    # Load data models
    print("\n1. Loading data models...")
    events_data = load_json("data_models/events/events.json")
    entities_data = load_json("data_models/entities/entities.json")
    relations_data = load_json("data_models/relations/relations.json")
    timeline_data = load_json("data_models/timelines/timeline_enhanced.json")
    
    # Map events to legal theories
    print("2. Mapping events to legal theories...")
    theory_event_mapping = map_events_to_legal_theories(events_data)
    
    print(f"\n   Legal Theory Mapping:")
    for theory_id, event_list in theory_event_mapping.items():
        theory_name = LEGAL_THEORIES[theory_id]["name"]
        print(f"   - {theory_name}: {len(event_list)} events")
    
    # Create juristic timeline matrix
    print("\n3. Creating juristic timeline matrix...")
    juristic_matrix = create_juristic_timeline_matrix(
        events_data, timeline_data, theory_event_mapping
    )
    
    print(f"   Created matrix with {len(juristic_matrix)} legally significant events")
    
    # Create interim interdict test mapping
    print("\n4. Mapping to interim interdict test...")
    interdict_test_mapping = create_interim_interdict_test_mapping(
        events_data, entities_data, relations_data
    )
    
    # Create comprehensive output
    legal_integration_output = {
        "metadata": {
            "created": datetime.now().isoformat(),
            "case_id": "2025-137857",
            "framework_version": "1.0"
        },
        "legal_theories": LEGAL_THEORIES,
        "theory_event_mapping": theory_event_mapping,
        "juristic_timeline_matrix": juristic_matrix,
        "interim_interdict_test_mapping": interdict_test_mapping,
        "summary": {
            "total_legally_significant_events": len(juristic_matrix),
            "theory_001_events": len(theory_event_mapping["THEORY_001"]),
            "theory_002_events": len(theory_event_mapping["THEORY_002"]),
            "theory_003_events": len(theory_event_mapping["THEORY_003"]),
            "theory_004_events": len(theory_event_mapping["THEORY_004"])
        }
    }
    
    # Save output
    output_file = "LEGAL_FRAMEWORK_INTEGRATION.json"
    with open(output_file, 'w') as f:
        json.dump(legal_integration_output, f, indent=2)
    
    print(f"\n{'=' * 80}")
    print(f"Integration complete. Output saved to: {output_file}")
    print(f"{'=' * 80}")
    
    print(f"\nSummary:")
    print(f"  Total legally significant events: {len(juristic_matrix)}")
    print(f"  Ex Parte Abuse events: {len(theory_event_mapping['THEORY_001'])}")
    print(f"  Retaliatory Motive events: {len(theory_event_mapping['THEORY_002'])}")
    print(f"  Corporate Misconduct events: {len(theory_event_mapping['THEORY_003'])}")
    print(f"  Trustee Misconduct events: {len(theory_event_mapping['THEORY_004'])}")

if __name__ == "__main__":
    main()
