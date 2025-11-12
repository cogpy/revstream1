import json
from datetime import datetime

# Load current entities
with open('/home/ubuntu/revstream1/data_models/entities/entities.json', 'r') as f:
    current_data = json.load(f)

# Create refined entities structure
refined_data = {
    "metadata": {
        "version": "4.0",
        "created_date": "2025-11-10",
        "description": "Refined entity model for Revenue Stream Hijacking case 2025-137857",
        "case_number": "2025-137857",
        "modeling_approach": "agentic_entity_modeling",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "changes": "Fixed ORG_007 duplication (separated ReZonance and Adderory), added PERSON_003 (Rynette's son), added PERSON_011 (Chantal), added ORG_009 and ORG_010 (Adderory companies), enhanced existing entities with ad-res-j7 evidence"
    },
    "entities": {
        "persons": [],
        "organizations": [],
        "platforms": [],
        "domains": [],
        "trust_entities": []
    }
}

# Copy existing persons (excluding duplicates)
for person in current_data['entities']['persons']:
    refined_data['entities']['persons'].append(person)

# Add PERSON_003 (Rynette's son - Adderory owner)
person_003 = {
    "entity_id": "PERSON_003",
    "name": "Adderory (Rynette's Son)",
    "role": "co_conspirator_family_member",
    "agent_type": "accomplice",
    "involvement_events": 5,
    "primary_actions": [
        "domain_registration_for_identity_fraud",
        "company_registration_for_competing_business",
        "stock_supply_fraud_facilitation",
        "customer_hijacking_infrastructure"
    ],
    "relationships": [
        "son_of_PERSON_002",
        "owner_of_ORG_009",
        "owner_of_ORG_010",
        "domain_owner_DOMAIN_002"
    ],
    "financial_impact": {
        "direct_involvement": "R5,400,000+",
        "primary_categories": [
            "identity_fraud",
            "revenue_theft",
            "stock_fraud",
            "customer_hijacking"
        ],
        "stock_fraud_connection": "R5,400,000"
    },
    "timeline_events": [
        "EVENT_H009",
        "EVENT_010",
        "EVENT_024",
        "EVENT_027"
    ],
    "additional_notes": "Rynette's son, registered Adderory companies April 2021 (pre-planning), registered fraudulent domain regimaskin.co.za May 29 2025, supplied same stock type that disappeared from SLG"
}
refined_data['entities']['persons'].append(person_003)

# Add PERSON_011 (Chantal - estate related)
person_011 = {
    "entity_id": "PERSON_011",
    "name": "Chantal",
    "role": "estate_related_party",
    "agent_type": "neutral",
    "involvement_events": 1,
    "primary_actions": [
        "estate_finalization_communication"
    ],
    "relationships": [
        "connected_to_kayla_estate",
        "letter_sender_january_2025"
    ],
    "timeline_events": [
        "EVENT_023"
    ],
    "additional_notes": "Delivered letter about Kayla estate finalization in January 2025, potential witness to estate exploitation"
}
refined_data['entities']['persons'].append(person_011)

# Process organizations - fix ORG_007 duplication
for org in current_data['entities']['organizations']:
    entity_id = org.get('entity_id')
    name = org.get('name', '')
    
    # Skip duplicate ORG_007 entries and Adderory mislabeled as ORG_007
    if entity_id == 'ORG_007':
        if 'ReZonance (Pty) Ltd' in name:
            # Keep this one as the proper ORG_008 (already exists)
            continue
        elif 'Adderory' in name:
            # Skip - will be added as ORG_009
            continue
        elif 'ReZonance' in name and 'Pty' not in name:
            # Skip duplicate, keep ORG_008
            continue
    
    # Keep ORG_008 (ReZonance Pty Ltd) as is
    if entity_id == 'ORG_008':
        refined_data['entities']['organizations'].append(org)
    elif entity_id != 'ORG_007':
        refined_data['entities']['organizations'].append(org)

# Add ORG_009 (Adderory Pty Ltd)
org_009 = {
    "entity_id": "ORG_009",
    "name": "Adderory (Pty) Ltd",
    "registration_date": "2021-04",
    "entity_type": "company",
    "agent_type": "accomplice",
    "role": "competing_business_fraud_vehicle",
    "ownership": {
        "owner": "PERSON_003",
        "relationship_to_PERSON_002": "son"
    },
    "involvement_events": 5,
    "primary_actions": [
        "domain_registration_for_identity_fraud",
        "stock_supply_fraud",
        "transfer_pricing_manipulation",
        "customer_hijacking",
        "revenue_redirection"
    ],
    "relationships": [
        "owned_by_PERSON_003",
        "controlled_by_PERSON_002",
        "domain_owner_DOMAIN_002",
        "stock_supplier_to_regima",
        "beneficiary_of_slg_stock_disappearance",
        "revenue_recipient_from_hijacking"
    ],
    "financial_impact": {
        "direct_involvement": "R5,400,000+",
        "primary_categories": [
            "identity_fraud",
            "revenue_theft",
            "stock_fraud",
            "customer_hijacking"
        ],
        "stock_fraud_connection": "R5,400,000"
    },
    "timeline_events": [
        "EVENT_H009",
        "EVENT_010",
        "EVENT_024",
        "EVENT_027"
    ],
    "additional_notes": "Registered April 2021 (4 years before fraud escalation), demonstrates long-term conspiracy planning, supplied same stock type that disappeared from SLG, registered fraudulent domain regimaskin.co.za"
}
refined_data['entities']['organizations'].append(org_009)

# Add ORG_010 (Adderory Skin Pty Ltd)
org_010 = {
    "entity_id": "ORG_010",
    "name": "Adderory Skin (Pty) Ltd",
    "registration_date": "2021-04",
    "entity_type": "company",
    "agent_type": "accomplice",
    "role": "competing_business_fraud_vehicle",
    "ownership": {
        "owner": "PERSON_003",
        "relationship_to_PERSON_002": "son"
    },
    "involvement_events": 3,
    "primary_actions": [
        "customer_hijacking",
        "revenue_redirection",
        "brand_impersonation"
    ],
    "relationships": [
        "owned_by_PERSON_003",
        "controlled_by_PERSON_002",
        "part_of_adderory_group",
        "revenue_recipient_from_hijacking"
    ],
    "financial_impact": {
        "direct_involvement": "unknown_amount",
        "primary_categories": [
            "identity_fraud",
            "revenue_theft",
            "customer_hijacking"
        ]
    },
    "timeline_events": [
        "EVENT_H009",
        "EVENT_027"
    ],
    "additional_notes": "Registered April 2021 alongside Adderory (Pty) Ltd, part of Adderory group for customer hijacking, used RegimA brand for fraud"
}
refined_data['entities']['organizations'].append(org_010)

# Copy platforms, domains, and trusts as is
refined_data['entities']['platforms'] = current_data['entities']['platforms']
refined_data['entities']['domains'] = current_data['entities']['domains']
refined_data['entities']['trust_entities'] = current_data['entities']['trust_entities']

# Save refined entities
with open('/home/ubuntu/revstream1/data_models/entities/entities_refined.json', 'w') as f:
    json.dump(refined_data, f, indent=2)

print("✓ Refined entities model created successfully")
print(f"  - Total persons: {len(refined_data['entities']['persons'])}")
print(f"  - Total organizations: {len(refined_data['entities']['organizations'])}")
print(f"  - Added PERSON_003 (Rynette's son)")
print(f"  - Added PERSON_011 (Chantal)")
print(f"  - Added ORG_009 (Adderory Pty Ltd)")
print(f"  - Added ORG_010 (Adderory Skin Pty Ltd)")
print(f"  - Fixed ORG_007 duplication")
