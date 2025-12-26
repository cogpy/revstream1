import json
from datetime import datetime

# Load current events
with open('/home/ubuntu/revstream1/data_models/events/events.json', 'r') as f:
    current_data = json.load(f)

# Create refined events structure
refined_data = {
    "metadata": {
        "version": "4.0",
        "created_date": "2025-11-10",
        "description": "Refined event model for Revenue Stream Hijacking case 2025-137857",
        "case_number": "2025-137857",
        "total_events": 46,
        "extended_evidence": "incorporated_from_ad_res_j7",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "changes": "Added 5 new events: Adderory registration (Apr 2021), Kayla murder (2023), Chantal letter (Jan 2025), SLG stock missing (Feb 25 2025), Cloud IT removal (Apr 22 2025)"
    },
    "events": []
}

# Copy all existing events
refined_data['events'] = current_data['events'].copy()

# Add EVENT_H009: Adderory Companies Registration (April 2021)
event_h009 = {
    "event_id": "EVENT_H009",
    "date": "2021-04-01",
    "title": "Adderory Companies Registration - Pre-Planning Phase",
    "category": "conspiracy_preparation",
    "event_type": "company_registration",
    "perpetrators": [
        "PERSON_003",
        "PERSON_002"
    ],
    "victims": [],
    "entities_involved": [
        "ORG_009",
        "ORG_010"
    ],
    "description": "Rynette's son registered Adderory (Pty) Ltd and Adderory Skin (Pty) Ltd, establishing competing business infrastructure 4 years before fraud escalation. Demonstrates long-term conspiracy planning.",
    "financial_impact": "unknown_amount",
    "legal_significance": "pre_planning_evidence_demonstrates_long_term_conspiracy",
    "evidence": [
        "company_registration_records",
        "cipc_documentation"
    ],
    "pattern": "pre_planning_phase",
    "additional_notes": "Registered April 2021, 4 years before May 2025 fraud escalation, demonstrates systematic pre-planning",
    "evidence_location": "ad-res-j7/1-CIVIL-RESPONSE/SUPPORTING_AFFIDAVIT_RYNETTE_SHOPIFY_EVIDENCE.md"
}
refined_data['events'].append(event_h009)

# Add EVENT_H010: Kayla Pretorius Murder (2023)
event_h010 = {
    "event_id": "EVENT_H010",
    "date": "2023-01-01",
    "title": "Kayla Pretorius Murder",
    "category": "criminal_event",
    "event_type": "murder",
    "perpetrators": [],
    "victims": [
        "PERSON_008"
    ],
    "entities_involved": [
        "ORG_008"
    ],
    "description": "Murder of Kayla Pretorius, creating estate complications, law enforcement investigation, and family trauma. Estate includes ReZonance debt of R1,035,000.",
    "financial_impact": "R1,035,000",
    "legal_significance": "estate_complications_law_enforcement_investigation",
    "evidence": [
        "police_reports_pending",
        "estate_documentation_pending"
    ],
    "pattern": "historical_foundation_phase",
    "additional_notes": "Account access complications, law enforcement investigation ongoing, referenced in criminal case documentation",
    "evidence_location": "ad-res-j7/2-CRIMINAL-CASE/README.md"
}
refined_data['events'].append(event_h010)

# Add EVENT_023: Chantal Letter - Estate Finalization (January 2025)
event_023 = {
    "event_id": "EVENT_023",
    "date": "2025-01-15",
    "title": "Chantal Letter - Kayla Estate Finalization",
    "category": "estate_exploitation",
    "event_type": "estate_communication",
    "perpetrators": [],
    "victims": [
        "estate_of_kayla"
    ],
    "entities_involved": [
        "PERSON_011",
        "ORG_008"
    ],
    "description": "Chantal delivered letter mentioning Kayla estate finalization, indicating ongoing exploitation of deceased victim's estate.",
    "financial_impact": "R1,035,000",
    "legal_significance": "ongoing_estate_exploitation_pattern",
    "evidence": [
        "estate_documentation_pending",
        "letter_from_chantal"
    ],
    "pattern": "pre_foundation_phase",
    "additional_notes": "Estate finalization timing correlates with revenue hijacking timeline, suggests coordination",
    "evidence_location": "ad-res-j7/jax-response/AD/1-Critical/KEY_TIMELINE_EVENTS_COMPREHENSIVE.md"
}
refined_data['events'].append(event_023)

# Add EVENT_028: SLG Stock Missing & Large Invoice (February 25, 2025)
event_028 = {
    "event_id": "EVENT_028",
    "date": "2025-02-25",
    "title": "R5.2M SLG Stock Missing & Large Invoice",
    "category": "transfer_pricing_fraud",
    "event_type": "stock_theft_and_invoice",
    "perpetrators": [
        "PERSON_001",
        "PERSON_002",
        "PERSON_007",
        "PERSON_003"
    ],
    "victims": [
        "ORG_004",
        "TRUST_001"
    ],
    "entities_involved": [
        "ORG_004",
        "ORG_002",
        "ORG_009"
    ],
    "description": "R5.2M SLG stock missing with simultaneous R5.2M invoice from SLG to RST. Stock physically disappeared, same type later supplied by Adderory to RegimA. Systematic asset stripping begins.",
    "financial_impact": "R5,200,000",
    "legal_significance": "systematic_asset_stripping_transfer_pricing_fraud",
    "evidence": [
        "financial_records",
        "invoice_documentation",
        "stock_reconciliation"
    ],
    "pattern": "foundation_phase",
    "critical": True,
    "additional_notes": "Same stock type supplied by Adderory (Rynette's son), demonstrates coordinated transfer pricing fraud",
    "evidence_location": "ad-res-j7/jax-response/AD/1-Critical/KEY_TIMELINE_EVENTS_COMPREHENSIVE.md"
}
refined_data['events'].append(event_028)

# Add EVENT_029: Cloud IT Systems Removal Order (April 22, 2025)
event_029 = {
    "event_id": "EVENT_029",
    "date": "2025-04-22",
    "title": "Cloud IT Systems Removal Order",
    "category": "infrastructure_seizure",
    "event_type": "it_systems_removal",
    "perpetrators": [
        "PERSON_001"
    ],
    "victims": [
        "PERSON_005",
        "ORG_003"
    ],
    "entities_involved": [
        "PLATFORM_001"
    ],
    "description": "Peter ordered Cloud IT systems removal, seizing infrastructure control from legitimate operators.",
    "financial_impact": "unknown_amount",
    "legal_significance": "infrastructure_control_seizure",
    "evidence": [
        "system_access_logs_pending",
        "it_documentation"
    ],
    "pattern": "initial_theft_phase",
    "additional_notes": "Infrastructure control seizure between bank letter (Apr 14) and audit trail destruction (May 22)",
    "evidence_location": "ad-res-j7/jax-response/AD/1-Critical/KEY_TIMELINE_EVENTS_COMPREHENSIVE.md"
}
refined_data['events'].append(event_029)

# Update metadata
refined_data['metadata']['total_events'] = len(refined_data['events'])

# Save refined events
with open('/home/ubuntu/revstream1/data_models/events/events_refined.json', 'w') as f:
    json.dump(refined_data, f, indent=2)

print("✓ Refined events model created successfully")
print(f"  - Total events: {len(refined_data['events'])}")
print(f"  - Added EVENT_H009 (Adderory registration, April 2021)")
print(f"  - Added EVENT_H010 (Kayla murder, 2023)")
print(f"  - Added EVENT_023 (Chantal letter, January 2025)")
print(f"  - Added EVENT_028 (SLG stock missing, February 25 2025)")
print(f"  - Added EVENT_029 (Cloud IT removal, April 22 2025)")
