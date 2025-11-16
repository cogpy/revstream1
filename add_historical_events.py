import json
from datetime import datetime

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load events model
events = load_json('/home/ubuntu/revstream1/data_models/events/events_refined.json')

print("=== ADDING NEW HISTORICAL EVENTS ===\n")

# New historical events from ad-res-j7 evidence
new_events = [
    {
        "event_id": "EVENT_H011",
        "date": "2020-02-20",
        "title": "Inter-company Cost Reallocations",
        "category": "financial_structure",
        "event_type": "cost_manipulation",
        "perpetrators": ["PERSON_001", "PERSON_007"],
        "victims": ["ORG_001", "ORG_002", "ORG_004"],
        "entities_involved": ["ORG_001", "ORG_002", "ORG_004"],
        "description": "Multiple adjusting journal entries across entities: RWW R500K stock provision write-back, RWW R810K admin fee reallocation to production costs, SLG R252K admin fee reallocation to production costs, SLG R80K production cost transfer to RST",
        "financial_impact": "R1,642,000",
        "legal_significance": "establishment_of_cost_manipulation_infrastructure",
        "evidence": [
            "trial_balance_documentation",
            "adjusting_journal_entries"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/comprehensive_fraud_timeline_2017_2025.md",
                "evidence_type": "timeline_documentation",
                "relevance": "primary"
            }
        ]
    },
    {
        "event_id": "EVENT_H012",
        "date": "2020-02-28",
        "title": "SLG Interest Payment to RST",
        "category": "inter_company_loan",
        "event_type": "interest_payment",
        "perpetrators": [],
        "victims": [],
        "entities_involved": ["ORG_004", "ORG_002"],
        "description": "SLG pays R414,334.09 interest to RST per loan agreement, documenting inter-company financial interdependencies",
        "financial_impact": "R414,334.09",
        "legal_significance": "evidence_of_inter_company_loan_structure",
        "evidence": [
            "trial_balance_records",
            "loan_agreement_documentation"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/REG-TRIALBALANCE.xlsx",
                "evidence_type": "financial_document",
                "relevance": "primary"
            },
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/SL-TRIALBALANCE2020.xlsx",
                "evidence_type": "financial_document",
                "relevance": "primary"
            }
        ]
    },
    {
        "event_id": "EVENT_H013",
        "date": "2020-02-28",
        "title": "RST Loan to RWW",
        "category": "inter_company_loan",
        "event_type": "loan_advance",
        "perpetrators": [],
        "victims": [],
        "entities_involved": ["ORG_002", "ORG_001"],
        "description": "RST advances R750,000 loan to RWW for production costs, creating financial dependency structure",
        "financial_impact": "R750,000",
        "legal_significance": "financial_dependency_creation",
        "evidence": [
            "trial_balance_records",
            "loan_documentation"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/REG-TRIALBALANCE.xlsx",
                "evidence_type": "financial_document",
                "relevance": "primary"
            }
        ]
    },
    {
        "event_id": "EVENT_H014",
        "date": "2020-04-30",
        "title": "Villa Via Capital Extraction",
        "category": "profit_extraction",
        "event_type": "capital_extraction",
        "perpetrators": ["PERSON_001"],
        "victims": ["ORG_005"],
        "entities_involved": ["ORG_005"],
        "description": "Villa Via financial year-end showing R22.8M members loan account, indicating major capital extraction mechanism. Monthly rental income R4.4M, net profit R3.7M",
        "financial_impact": "R22,800,000",
        "legal_significance": "major_profit_extraction_mechanism",
        "evidence": [
            "villa_via_trial_balance",
            "financial_year_end_statements"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/VV-TRIALBALANCEAPR20202.xlsx",
                "evidence_type": "financial_document",
                "relevance": "primary"
            }
        ]
    },
    {
        "event_id": "EVENT_H015",
        "date": "2020-08-13",
        "title": "Bantjes Trial Balance Distribution",
        "category": "evidence_documentation",
        "event_type": "financial_system_control",
        "perpetrators": ["PERSON_007"],
        "victims": [],
        "entities_involved": ["PERSON_007", "PERSON_010", "PERSON_004", "PERSON_001", "PERSON_002", "PERSON_005"],
        "description": "Email from Danie Bantjes with final trial balances to Bernadine Wright, Jacqui, Peter, Rynette, and Daniel. Preparation for financial statement finalization meeting, demonstrating Bantjes' control over financial systems",
        "financial_impact": "unknown_amount",
        "legal_significance": "evidence_of_financial_system_control",
        "evidence": [
            "email_correspondence",
            "trial_balance_attachments"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/Email-body.html",
                "evidence_type": "email_correspondence",
                "relevance": "primary"
            }
        ]
    },
    {
        "event_id": "EVENT_H016",
        "date": "2017-06-30",
        "title": "First ReZonance Invoice",
        "category": "business_relationship",
        "event_type": "relationship_establishment",
        "perpetrators": [],
        "victims": [],
        "entities_involved": ["ORG_007", "ORG_002"],
        "description": "First invoice to RegimA Skin Treatments for Google GSuite services (R250.80), marking beginning of business relationship between ReZonance and RegimA Group",
        "financial_impact": "R250.80",
        "legal_significance": "beginning_of_business_relationship",
        "evidence": [
            "invoice_records",
            "service_agreements"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/comprehensive_fraud_timeline_2017_2025.md",
                "evidence_type": "timeline_documentation",
                "relevance": "primary"
            }
        ]
    },
    {
        "event_id": "EVENT_H017",
        "date": "2017-09-30",
        "title": "Major Service Expansion",
        "category": "business_relationship",
        "event_type": "service_expansion",
        "perpetrators": [],
        "victims": [],
        "entities_involved": ["ORG_007", "ORG_002", "ORG_001"],
        "description": "Major service expansion with multiple enterprise services (R100,000+), substantial increase in service provision and financial exposure establishing trust and operational dependency",
        "financial_impact": "R100,000",
        "legal_significance": "trust_establishment_phase",
        "evidence": [
            "service_contracts",
            "invoice_records"
        ],
        "pattern": "historical_foundation_phase",
        "evidence_files": [
            {
                "repository": "ad-res-j7",
                "file_path": "ANNEXURES/JF08/evidence_package_20251012/comprehensive_fraud_timeline_2017_2025.md",
                "evidence_type": "timeline_documentation",
                "relevance": "primary"
            }
        ]
    }
]

# Add new events to the events list
events['events'].extend(new_events)

# Update metadata
events['metadata']['version'] = "5.0"
events['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
events['metadata']['total_events'] = len(events['events'])
events['metadata']['changes'] = "Added 7 new historical events (EVENT_H011-H017) from ad-res-j7 evidence, added evidence_files schema to all new events"

# Save updated events
save_json('/home/ubuntu/revstream1/data_models/events/events_refined.json', events)

print(f"✅ Added {len(new_events)} new historical events")
print(f"   Total events now: {events['metadata']['total_events']}")
print(f"   Version updated to: {events['metadata']['version']}")
print("\nNew events added:")
for event in new_events:
    print(f"   - {event['event_id']}: {event['title']} ({event['date']})")

print("\n=== HISTORICAL EVENTS ADDITION COMPLETE ===")
