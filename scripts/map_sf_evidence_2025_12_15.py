#!/usr/bin/env python3
"""
Map SF (Supplementary Files) evidence from ad-res-j7 to entities and events
Date: 2025-12-15
"""

import json
import os
from datetime import datetime

AD_RES_BASE = "/home/ubuntu/ad-res-j7"
REVSTREAM_BASE = "/home/ubuntu/revstream1"

# SF Evidence Files mapping
SF_EVIDENCE = {
    "SF1": {
        "file": "SF1_Bantjies_Debt_Documentation.md",
        "title": "Bantjies Debt Documentation",
        "entities": ["PERSON_001", "PERSON_002", "ORG_001"],  # Peter, Rynette, Bantjies
        "events": ["EVENT_010", "EVENT_011"],  # Debt-related events
        "legal_significance": "Demonstrates debt manipulation and financial engineering",
        "burden_of_proof": "civil_50_percent"
    },
    "SF2": {
        "file": "SF2_Sage_Screenshots_Rynette_Control.md",
        "title": "Sage Screenshots - Rynette Control",
        "entities": ["PERSON_002", "ORG_002", "ORG_003"],  # Rynette, RST, RWD
        "events": ["EVENT_003", "EVENT_007", "EVENT_008"],  # Accounting manipulation
        "legal_significance": "Direct evidence of unauthorized system access and control",
        "burden_of_proof": "civil_50_percent"
    },
    "SF3": {
        "file": "SF3_Strategic_Logistics_Stock_Adjustment.md",
        "title": "Strategic Logistics Stock Adjustment",
        "entities": ["ORG_009", "PERSON_002"],  # Strategic Logistics, Rynette
        "events": ["EVENT_012", "EVENT_013"],  # Stock manipulation
        "legal_significance": "Evidence of inventory fraud and transfer pricing manipulation",
        "burden_of_proof": "civil_50_percent"
    },
    "SF4": {
        "file": "SF4_SARS_Audit_Email.md",
        "title": "SARS Audit Email",
        "entities": ["PERSON_001", "PERSON_002", "ORG_002"],
        "events": ["EVENT_014"],  # Tax fraud
        "legal_significance": "Tax fraud evidence - potential criminal liability",
        "burden_of_proof": "criminal_95_percent"
    },
    "SF5": {
        "file": "SF5_Adderory_Company_Registration_Stock_Supply.md",
        "title": "Adderory Company Registration & Stock Supply",
        "entities": ["ORG_010", "PERSON_002"],  # Adderory, Rynette
        "events": ["EVENT_015"],  # Company registration fraud
        "legal_significance": "Shell company creation for fraud purposes",
        "burden_of_proof": "civil_50_percent"
    },
    "SF6": {
        "file": "SF6_Kayla_Pretorius_Estate_Documentation.md",
        "title": "Kayla Pretorius Estate Documentation",
        "entities": ["PERSON_003", "PERSON_005", "ORG_002"],  # Kayla, Daniel, RST
        "events": ["EVENT_H001", "EVENT_001"],  # Historical foundation
        "legal_significance": "Critical evidence of business appropriation after death",
        "burden_of_proof": "civil_50_percent"
    },
    "SF7": {
        "file": "SF7_Court_Order_Kayla_Email_Seizure.md",
        "title": "Court Order - Kayla Email Seizure",
        "entities": ["PERSON_003", "PERSON_001"],  # Kayla, Peter
        "events": ["EVENT_016"],  # Evidence destruction
        "legal_significance": "Evidence of post-mortem email account seizure",
        "burden_of_proof": "civil_50_percent"
    },
    "SF8": {
        "file": "SF8_Linda_Employment_Records.md",
        "title": "Linda Employment Records",
        "entities": ["PERSON_006", "ORG_002"],  # Linda, RST
        "events": ["EVENT_017"],  # Employment fraud
        "legal_significance": "Payroll fraud and employment manipulation",
        "burden_of_proof": "civil_50_percent"
    }
}

# Read SF files and extract key information
sf_analysis = {
    "metadata": {
        "analysis_date": datetime.now().isoformat(),
        "source_repository": "ad-res-j7",
        "total_sf_files": len(SF_EVIDENCE)
    },
    "sf_evidence": {}
}

print("Analyzing SF Evidence Files...")
print("="*60)

for sf_id, sf_data in SF_EVIDENCE.items():
    sf_path = f"{AD_RES_BASE}/ANNEXURES/{sf_data['file']}"
    
    if os.path.exists(sf_path):
        with open(sf_path, 'r') as f:
            content = f.read()
            
        sf_analysis["sf_evidence"][sf_id] = {
            "title": sf_data["title"],
            "file": sf_data["file"],
            "entities_involved": sf_data["entities"],
            "events_referenced": sf_data["events"],
            "legal_significance": sf_data["legal_significance"],
            "burden_of_proof": sf_data["burden_of_proof"],
            "content_length": len(content),
            "exists": True
        }
        
        print(f"\n{sf_id}: {sf_data['title']}")
        print(f"  Entities: {len(sf_data['entities'])}")
        print(f"  Events: {len(sf_data['events'])}")
        print(f"  Burden: {sf_data['burden_of_proof']}")
        print(f"  Size: {len(content)} bytes")
    else:
        sf_analysis["sf_evidence"][sf_id] = {
            "title": sf_data["title"],
            "file": sf_data["file"],
            "exists": False
        }
        print(f"\n{sf_id}: {sf_data['title']} - FILE NOT FOUND")

# Save SF analysis
output_path = f"{REVSTREAM_BASE}/SF_EVIDENCE_ANALYSIS_2025_12_15.json"
with open(output_path, 'w') as f:
    json.dump(sf_analysis, f, indent=2)

print("\n" + "="*60)
print(f"SF Evidence analysis saved to: {output_path}")
print("="*60)

# Generate recommendations for entity/event updates
recommendations = []

for sf_id, sf_data in SF_EVIDENCE.items():
    if sf_analysis["sf_evidence"][sf_id]["exists"]:
        recommendations.append({
            "sf_id": sf_id,
            "action": "enhance_entities",
            "entities": sf_data["entities"],
            "recommendation": f"Add {sf_id} reference to entities: {', '.join(sf_data['entities'])}"
        })
        recommendations.append({
            "sf_id": sf_id,
            "action": "enhance_events",
            "events": sf_data["events"],
            "recommendation": f"Add {sf_id} evidence to events: {', '.join(sf_data['events'])}"
        })

print(f"\nGenerated {len(recommendations)} enhancement recommendations")
