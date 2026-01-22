#!/usr/bin/env python3
"""
Trial Balance Evidence Integration Script
Date: 2026-01-18
Purpose: Integrate new insights from FinalTBsandCaseAnalysisInstructions.zip into
         revstream1 data models (entities, relations, events, timeline)
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities.json"
RELATIONS_FILE = DATA_MODELS_DIR / "relations" / "relations.json"
EVENTS_FILE = DATA_MODELS_DIR / "events" / "events.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timelines" / "timeline.json"

# New insights from trial balance analysis
TRIAL_BALANCE_INSIGHTS = {
    "analysis_date": "2026-01-18",
    "source": "FinalTBsandCaseAnalysisInstructions.zip",
    "period_covered": "2019-03-01 to 2020-04-30",
    
    "new_entities": [
        {
            "entity_id": "PERSON_TB_001",
            "name": "Bernadine Wright",
            "role": "financial_decision_maker",
            "agent_type": "key_witness",
            "email_domain": "regima.zone",
            "significance": "Primary recipient of 2020 financial statements, key financial decision-maker",
            "investigation_priority": "CRITICAL",
            "evidence": ["Email from Danie Bantjes 2020-08-13", "Trial balance documentation"],
            "investigation_leads": [
                "Identify Bernadine Wright's role and authority",
                "Determine current status and location",
                "Subpoena for testimony regarding financial structures"
            ]
        },
        {
            "entity_id": "PERSON_TB_002",
            "name": "Danie Bantjes",
            "role": "external_accountant",
            "agent_type": "key_witness",
            "significance": "Prepared final trial balances and AJEs, 6-month delay in finalization",
            "investigation_priority": "HIGH",
            "evidence": ["Email 2020-08-13", "Trial balance AJE documentation"],
            "red_flags": [
                "6-month delay between year-end (Feb 2020) and finalization (Aug 2020)",
                "Mentions 'disclosure changes promulgated during the past year'",
                "Coordinates meeting with Bernadine Wright for sign-off"
            ],
            "investigation_leads": [
                "Why 6-month delay in financial statement finalization?",
                "What disclosure changes were implemented?",
                "Subpoena Danie Bantjes records and communications"
            ],
            "trustee_connection": "Later appointed as Trustee by Rynette (July 2024, T-10 months before Ketoni payout)"
        },
        {
            "entity_id": "ORG_TB_001",
            "name": "DERM",
            "full_name": "DERM (Entity)",
            "entity_type": "missing_entity",
            "significance": "Operates RSA Shopify store, costs dumped on RWW",
            "investigation_priority": "HIGH",
            "evidence": ["Knowledge base references", "Cost allocation patterns"],
            "investigation_need": "Full financial analysis of DERM entity required"
        },
        {
            "entity_id": "ORG_TB_002",
            "name": "RSA",
            "full_name": "RegimA South Africa",
            "entity_type": "operating_entity",
            "significance": "Purchases from RST at 62% COS, separate from RWW",
            "investigation_priority": "MEDIUM",
            "evidence": ["Cost of sales structure analysis"]
        },
        {
            "entity_id": "ORG_TB_003",
            "name": "REU",
            "full_name": "RegimA Europe",
            "entity_type": "international_entity",
            "significance": "Smallest Shopify payments, part of payment hierarchy",
            "investigation_priority": "MEDIUM",
            "evidence": ["Shopify payment hierarchy analysis"]
        }
    ],
    
    "new_events": [
        {
            "entry_id": "TL_TB_001",
            "date": "2019-03-01",
            "event_type": "financial_year_start",
            "title": "RST/SLG Financial Year Commencement",
            "description": "Beginning of financial year for RegimA Skin Treatments (RST) and Strategic Logistics (SLG). This marks the start of the period covered by trial balance evidence showing systematic financial manipulation.",
            "key_actors": ["RegimA Skin Treatments", "Strategic Logistics"],
            "entities_involved": ["ORG_002", "ORG_003"],
            "evidence": ["REG-TRIALBALANCE.xlsx", "SL-TRIALBALANCE2020.xlsx"],
            "significance": "Beginning of documented manipulation period",
            "burden_of_proof": "verified_financial_record",
            "criminal_threshold": "supporting_evidence"
        },
        {
            "entry_id": "TL_TB_002",
            "date": "2019-05-01",
            "event_type": "financial_year_start",
            "title": "Villa Via Financial Year Commencement",
            "description": "Beginning of financial year for Villa Via. Different year-end from RST/SLG creates complexity in group reporting and opportunities for manipulation.",
            "key_actors": ["Villa Via"],
            "entities_involved": ["ORG_VV"],
            "evidence": ["VV-TRIALBALANCEAPR20202.xlsx"],
            "significance": "Staggered year-end enables timing manipulation",
            "burden_of_proof": "verified_financial_record"
        },
        {
            "entry_id": "TL_TB_003",
            "date": "2020-02-20",
            "event_type": "financial_manipulation",
            "title": "Coordinated Inter-Company Cost Reallocations",
            "description": "Multiple adjusting journal entries across entities on same date: RWW R500K stock provision write-back, RWW R810K admin fee reallocation to production costs, SLG R252K admin fee reallocation to production costs, SLG R80K production cost transfer to RST. Coordinated timing suggests deliberate manipulation.",
            "key_actors": ["Co-director's bookkeeper", "Rynette Farrar"],
            "entities_involved": ["ORG_001", "ORG_003", "ORG_002"],
            "evidence": ["WW-TrialBalanceFEB20.xlsx AJEs", "SL-TRIALBALANCE2020.xlsx AJEs"],
            "significance": "CRITICAL - Coordinated manipulation across entities",
            "financial_impact": {
                "rww_stock_write_back": 500000.00,
                "rww_admin_reallocation": 810097.70,
                "slg_admin_reallocation": 252041.73,
                "slg_production_transfer": 80000.00
            },
            "burden_of_proof": "verified_financial_record",
            "criminal_threshold": "pattern_evidence"
        },
        {
            "entry_id": "TL_TB_004",
            "date": "2020-02-28",
            "event_type": "financial_manipulation",
            "title": "Year-End Inter-Company Interest and Loan Transactions",
            "description": "Critical year-end adjustments: SLG pays R414,334.09 interest to RST per loan agreement (3.19% rate on R13M debt), RST advances R750K loan to RWW for production costs, Directors' fee adjustment of R784K in RST. These transactions demonstrate profit shifting from SLG to RST.",
            "key_actors": ["Peter Andrew Faucitt", "Co-director's bookkeeper"],
            "entities_involved": ["ORG_002", "ORG_003", "ORG_001"],
            "evidence": ["REG-TRIALBALANCE.xlsx", "SL-TRIALBALANCE2020.xlsx"],
            "significance": "CRITICAL - Profit extraction mechanism documented",
            "financial_impact": {
                "slg_to_rst_interest": 414334.09,
                "rst_to_rww_loan": 750000.00,
                "directors_fee_adjustment": 784000.00,
                "slg_debt_to_rst": 12971390.13
            },
            "burden_of_proof": "verified_financial_record",
            "criminal_threshold": "pattern_evidence"
        },
        {
            "entry_id": "TL_TB_005",
            "date": "2020-04-30",
            "event_type": "financial_year_end",
            "title": "Villa Via Year-End - Capital Extraction Evidence",
            "description": "Villa Via financial year-end showing R3.7M profit from R4.4M rental income, while maintaining R22.8M members loan account. Members loan is 5.2x annual rental income, indicating systematic capital extraction over multiple years.",
            "key_actors": ["Villa Via shareholders"],
            "entities_involved": ["ORG_VV"],
            "evidence": ["VV-TRIALBALANCEAPR20202.xlsx"],
            "significance": "Capital extraction vehicle documented",
            "financial_impact": {
                "monthly_rental_income": 4384701.36,
                "net_profit": 3727475.50,
                "members_loan_account": 22806538.74,
                "extraction_ratio": "5.2x annual income"
            },
            "burden_of_proof": "verified_financial_record",
            "criminal_threshold": "supporting_evidence"
        },
        {
            "entry_id": "TL_TB_006",
            "date": "2020-08-13",
            "event_type": "communication",
            "title": "Danie Bantjes Email - Financial Statement Finalization",
            "description": "Email from Danie Bantjes to Bernadine Wright, Jacqui Faucitt (Jax), Peter Andrew Faucitt, Rynette Farrar, and Daniel Faucitt with final trial balances. 6-month delay from year-end suggests complex manipulation requiring extended finalization. Meeting scheduled with Bernadine Wright for sign-off.",
            "key_actors": ["Danie Bantjes", "Bernadine Wright", "Jacqui Faucitt", "Peter Andrew Faucitt", "Rynette Farrar", "Daniel Faucitt"],
            "entities_involved": ["PERSON_TB_002", "PERSON_TB_001", "PERSON_004", "PERSON_001", "PERSON_002", "PERSON_005"],
            "evidence": ["email-body.html"],
            "significance": "CRITICAL - Links Rynette to 2020 financial access, establishes Bernadine Wright as key decision-maker",
            "red_flags": [
                "6-month delay in finalization",
                "Disclosure changes mentioned",
                "Rynette present in financial discussions (later led 2025 cover-up)"
            ],
            "burden_of_proof": "verified_communication",
            "criminal_threshold": "pattern_evidence"
        }
    ],
    
    "new_relations": [
        {
            "relation_id": "REL_TB_001",
            "type": "financial_control",
            "source_entity": "PERSON_TB_001",
            "target_entity": "ORG_002",
            "description": "Bernadine Wright as financial decision-maker for RST",
            "evidence": ["2020-08-13 email coordination"],
            "significance": "Establishes financial authority structure"
        },
        {
            "relation_id": "REL_TB_002",
            "type": "inter_company_debt",
            "source_entity": "ORG_003",
            "target_entity": "ORG_002",
            "description": "SLG owes RST R12,971,390.13 (87% of SLG annual sales)",
            "evidence": ["SL-TRIALBALANCE2020.xlsx"],
            "significance": "Creates financial dependency and control mechanism",
            "financial_impact": 12971390.13
        },
        {
            "relation_id": "REL_TB_003",
            "type": "cost_dumping",
            "source_entity": "ORG_002",
            "target_entity": "ORG_001",
            "description": "RST dumps production costs on RWW via R750K loan mechanism",
            "evidence": ["REG-TRIALBALANCE.xlsx AJEs"],
            "significance": "Cost dumping mechanism documented",
            "financial_impact": 750000.00
        },
        {
            "relation_id": "REL_TB_004",
            "type": "interest_extraction",
            "source_entity": "ORG_003",
            "target_entity": "ORG_002",
            "description": "SLG pays 3.19% interest to RST (R414K annually on R13M debt)",
            "evidence": ["SL-TRIALBALANCE2020.xlsx"],
            "significance": "Profit shifting via artificially low interest rate",
            "financial_impact": 414334.09
        },
        {
            "relation_id": "REL_TB_005",
            "type": "financial_access_continuity",
            "source_entity": "PERSON_002",
            "target_entity": "ORG_001",
            "description": "Rynette Farrar had financial access in 2020 (email recipient) and led 2025 cover-up",
            "evidence": ["2020-08-13 email", "2025 fraud timeline"],
            "significance": "CRITICAL - Establishes continuity of access from 2020 to 2025 fraud",
            "timeline_span": "2020-08-13 to 2025-05-29"
        },
        {
            "relation_id": "REL_TB_006",
            "type": "trustee_appointment",
            "source_entity": "PERSON_002",
            "target_entity": "PERSON_TB_002",
            "description": "Rynette appointed Danie Bantjes as Trustee in July 2024 (T-10 months before Ketoni payout)",
            "evidence": ["Trust documentation", "Ketoni timeline"],
            "significance": "CRITICAL - Links 2020 accountant to 2024 trust control consolidation"
        }
    ],
    
    "financial_manipulation_patterns": {
        "year_end_manipulation": {
            "pattern_type": "Year-end Manipulation",
            "description": "Critical adjustments made in final days of financial year",
            "evidence": "Feb 20-28, 2020: 8-day window for major inter-company adjustments",
            "significance": "Suggests deliberate timing to avoid scrutiny"
        },
        "cover_up_acceleration": {
            "pattern_type": "Cover-up Acceleration",
            "description": "Systematic evidence destruction following confrontation",
            "evidence": "May 15-29, 2025: 14-day evidence destruction sequence",
            "significance": "Indicates pre-planned contingency for discovery"
        },
        "suspicious_interest_rate": {
            "pattern_type": "Suspicious Interest Rate",
            "description": "SLG pays 3.19% interest to RST",
            "analysis": "Rate appears artificially low for inter-company loan",
            "implication": "Possible benefit transfer to RST at SLG expense"
        },
        "coordinated_cost_reallocations": {
            "pattern_type": "Coordinated Cost Reallocations",
            "description": "Multiple entities reallocate admin fees to production costs simultaneously",
            "evidence": "RWW: R810K, SLG: R252K on same date (2020-02-20)",
            "implication": "Coordinated effort to obscure true cost structures"
        },
        "excessive_capital_extraction": {
            "pattern_type": "Excessive Capital Extraction",
            "description": "Villa Via members loan is 5.2x annual rental income",
            "analysis": "Suggests systematic capital extraction over multiple years",
            "implication": "Villa Via used as vehicle for wealth extraction"
        }
    },
    
    "control_mechanisms": {
        "centralized_bookkeeping": {
            "mechanism": "Centralized Bookkeeping Control",
            "controller": "Co-director's personal bookkeeper",
            "scope": "All entity financial records",
            "vulnerability": "Single point of control enables manipulation"
        },
        "staggered_year_ends": {
            "mechanism": "Staggered Financial Year-Ends",
            "entities": "RST/SLG: Feb 28, Villa Via: Apr 30",
            "vulnerability": "Creates reporting gaps and complexity",
            "manipulation_potential": "Allows timing of transactions between periods"
        },
        "inter_company_debt_leverage": {
            "mechanism": "Inter-company Debt Leverage",
            "description": "SLG owes RST R13M (87% of SLG annual sales)",
            "control_effect": "Creates financial dependency and control"
        }
    },
    
    "strategic_implications": {
        "jax_vindication": {
            "insight": "Evidence shows Jax as fraud detector, not perpetrator",
            "implication": "Supports defense narrative of Jax as victim",
            "strategic_value": "Undermines prosecution claims of Jax involvement",
            "action_required": "Emphasize Jax's role in confronting fraud (May 15, 2025)"
        },
        "pre_fraud_baseline": {
            "insight": "Trial balance evidence provides pre-fraud baseline",
            "implication": "Demonstrates systematic manipulation before 2025 events",
            "strategic_value": "Shows pattern of behavior, not isolated incident",
            "action_required": "Integrate 2020 evidence into current case narrative"
        },
        "rynette_continuity": {
            "insight": "Rynette had financial access in 2020 and led 2025 cover-up",
            "implication": "Establishes long-term involvement in financial manipulation",
            "strategic_value": "Proves pattern of access and control over 5 years",
            "action_required": "Map Rynette's access evolution from 2020 to 2025"
        },
        "bantjes_connection": {
            "insight": "Danie Bantjes: 2020 accountant → 2024 Trustee appointment",
            "implication": "Links financial manipulation expertise to trust control",
            "strategic_value": "Explains why Bantjes was chosen as Trustee",
            "action_required": "Investigate Bantjes' role in both capacities"
        }
    }
}

def load_json(filepath):
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def save_json(filepath, data):
    """Save JSON file with backup."""
    backup_path = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    if os.path.exists(filepath):
        os.rename(filepath, backup_path)
        print(f"Backup created: {backup_path}")
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    print(f"Saved: {filepath}")

def integrate_entities(entities_data):
    """Integrate new entities from trial balance analysis."""
    if not entities_data:
        return None
    
    # Update metadata
    entities_data['metadata']['version'] = "29.0_TRIAL_BALANCE_INTEGRATED_2026_01_18"
    entities_data['metadata']['last_updated'] = datetime.now().isoformat()
    entities_data['metadata']['changes'] = "Integrated trial balance evidence (2020) - new entities, financial patterns, control mechanisms"
    
    # Add new persons
    new_persons = [e for e in TRIAL_BALANCE_INSIGHTS['new_entities'] if e['entity_id'].startswith('PERSON_')]
    for new_person in new_persons:
        # Check if already exists
        existing = [p for p in entities_data['entities']['persons'] if p.get('name') == new_person['name']]
        if not existing:
            entities_data['entities']['persons'].append(new_person)
            print(f"Added new person: {new_person['name']}")
        else:
            # Update existing with new information
            for p in entities_data['entities']['persons']:
                if p.get('name') == new_person['name']:
                    p.update({
                        'trial_balance_evidence': new_person,
                        'evidence_enhanced_timestamp': datetime.now().isoformat()
                    })
                    print(f"Updated existing person: {new_person['name']}")
    
    # Add new organizations
    new_orgs = [e for e in TRIAL_BALANCE_INSIGHTS['new_entities'] if e['entity_id'].startswith('ORG_')]
    for new_org in new_orgs:
        existing = [o for o in entities_data['entities']['organizations'] if o.get('name') == new_org['name']]
        if not existing:
            entities_data['entities']['organizations'].append(new_org)
            print(f"Added new organization: {new_org['name']}")
    
    # Update Rynette Farrar with 2020 financial access evidence
    for person in entities_data['entities']['persons']:
        if person.get('name') == 'Rynette Farrar':
            person['trial_balance_2020_access'] = {
                'date': '2020-08-13',
                'evidence': 'Email recipient for final trial balances',
                'significance': 'Establishes financial access 5 years before 2025 fraud',
                'continuity_to_2025': 'Same person led May 2025 cover-up'
            }
            person['evidence'].append('Trial Balance Email 2020-08-13 - Financial access evidence')
            print("Updated Rynette Farrar with 2020 financial access evidence")
    
    # Update total counts
    entities_data['metadata']['total_entities'] = len(entities_data['entities']['persons']) + len(entities_data['entities']['organizations'])
    entities_data['metadata']['total_persons'] = len(entities_data['entities']['persons'])
    entities_data['metadata']['total_organizations'] = len(entities_data['entities']['organizations'])
    
    return entities_data

def integrate_relations(relations_data):
    """Integrate new relations from trial balance analysis."""
    if not relations_data:
        return None
    
    # Update metadata
    relations_data['metadata']['version'] = "29.0_TRIAL_BALANCE_INTEGRATED_2026_01_18"
    relations_data['metadata']['last_updated'] = datetime.now().isoformat()
    relations_data['metadata']['changes'] = "Integrated trial balance evidence - inter-company debt, cost dumping, financial control relations"
    
    # Handle nested relations structure (relations is a dict with categories)
    if isinstance(relations_data.get('relations'), dict):
        # Add new category for trial balance relations
        if 'trial_balance_relations' not in relations_data['relations']:
            relations_data['relations']['trial_balance_relations'] = []
        
        for new_rel in TRIAL_BALANCE_INSIGHTS['new_relations']:
            existing = [r for r in relations_data['relations']['trial_balance_relations'] 
                       if r.get('relation_id') == new_rel['relation_id']]
            if not existing:
                relations_data['relations']['trial_balance_relations'].append(new_rel)
                print(f"Added new relation: {new_rel['relation_id']} - {new_rel['description']}")
    else:
        # Handle flat relations structure
        for new_rel in TRIAL_BALANCE_INSIGHTS['new_relations']:
            existing = [r for r in relations_data['relations'] if r.get('relation_id') == new_rel['relation_id']]
            if not existing:
                relations_data['relations'].append(new_rel)
                print(f"Added new relation: {new_rel['relation_id']} - {new_rel['description']}")
    
    # Add financial manipulation patterns as relation metadata
    relations_data['financial_manipulation_patterns'] = TRIAL_BALANCE_INSIGHTS['financial_manipulation_patterns']
    relations_data['control_mechanisms'] = TRIAL_BALANCE_INSIGHTS['control_mechanisms']
    
    return relations_data

def integrate_timeline(timeline_data):
    """Integrate new timeline events from trial balance analysis."""
    if not timeline_data:
        return None
    
    # Update metadata
    timeline_data['metadata']['version'] = "26.0_TRIAL_BALANCE_INTEGRATED_2026_01_18"
    timeline_data['metadata']['last_updated'] = datetime.now().isoformat()
    timeline_data['metadata']['changes'] = "Integrated trial balance evidence (2020) - 6 new financial manipulation events"
    
    # Add new events
    for new_event in TRIAL_BALANCE_INSIGHTS['new_events']:
        existing = [e for e in timeline_data['timeline'] if e.get('entry_id') == new_event['entry_id']]
        if not existing:
            timeline_data['timeline'].append(new_event)
            print(f"Added new timeline event: {new_event['entry_id']} - {new_event['title']}")
    
    # Sort timeline by date
    timeline_data['timeline'] = sorted(timeline_data['timeline'], key=lambda x: x.get('date', ''))
    
    # Update counts
    timeline_data['metadata']['total_entries'] = len(timeline_data['timeline'])
    
    # Add strategic implications
    timeline_data['strategic_implications'] = TRIAL_BALANCE_INSIGHTS['strategic_implications']
    
    return timeline_data

def integrate_events(events_data):
    """Integrate new events from trial balance analysis."""
    if not events_data:
        return None
    
    # Update metadata
    events_data['metadata']['version'] = "37.0_TRIAL_BALANCE_INTEGRATED_2026_01_18"
    events_data['metadata']['last_updated'] = datetime.now().isoformat()
    events_data['metadata']['changes'] = "Integrated trial balance evidence - financial manipulation events from 2020"
    
    # Add new events
    for new_event in TRIAL_BALANCE_INSIGHTS['new_events']:
        event_entry = {
            'event_id': new_event['entry_id'],
            'date': new_event['date'],
            'event_type': new_event['event_type'],
            'title': new_event['title'],
            'description': new_event['description'],
            'key_actors': new_event.get('key_actors', []),
            'entities_involved': new_event.get('entities_involved', []),
            'evidence': new_event.get('evidence', []),
            'significance': new_event.get('significance', ''),
            'burden_of_proof': new_event.get('burden_of_proof', ''),
            'criminal_threshold': new_event.get('criminal_threshold', ''),
            'financial_impact': new_event.get('financial_impact', {}),
            'source': 'Trial Balance Evidence Package August 2020',
            'added_date': datetime.now().isoformat()
        }
        
        existing = [e for e in events_data['events'] if e.get('event_id') == event_entry['event_id']]
        if not existing:
            events_data['events'].append(event_entry)
            print(f"Added new event: {event_entry['event_id']} - {event_entry['title']}")
    
    return events_data

def main():
    """Main integration function."""
    print("=" * 60)
    print("Trial Balance Evidence Integration")
    print(f"Date: {datetime.now().isoformat()}")
    print("=" * 60)
    
    # Load existing data
    print("\nLoading existing data models...")
    entities_data = load_json(ENTITIES_FILE)
    relations_data = load_json(RELATIONS_FILE)
    timeline_data = load_json(TIMELINE_FILE)
    
    # Find latest events file
    events_files = sorted(DATA_MODELS_DIR.glob("events/events*.json"), reverse=True)
    events_file = events_files[0] if events_files else None
    events_data = load_json(events_file) if events_file else None
    
    # Integrate new insights
    print("\nIntegrating trial balance insights...")
    
    if entities_data:
        entities_data = integrate_entities(entities_data)
        save_json(ENTITIES_FILE, entities_data)
    
    if relations_data:
        relations_data = integrate_relations(relations_data)
        save_json(RELATIONS_FILE, relations_data)
    
    if timeline_data:
        timeline_data = integrate_timeline(timeline_data)
        save_json(TIMELINE_FILE, timeline_data)
    
    if events_data and events_file:
        events_data = integrate_events(events_data)
        save_json(events_file, events_data)
    
    # Save insights summary
    insights_summary_path = DATA_MODELS_DIR / "TRIAL_BALANCE_INSIGHTS_2026_01_18.json"
    save_json(insights_summary_path, TRIAL_BALANCE_INSIGHTS)
    
    print("\n" + "=" * 60)
    print("Integration Complete!")
    print("=" * 60)
    print(f"\nNew entities added: {len(TRIAL_BALANCE_INSIGHTS['new_entities'])}")
    print(f"New events added: {len(TRIAL_BALANCE_INSIGHTS['new_events'])}")
    print(f"New relations added: {len(TRIAL_BALANCE_INSIGHTS['new_relations'])}")
    print(f"Financial patterns documented: {len(TRIAL_BALANCE_INSIGHTS['financial_manipulation_patterns'])}")
    print(f"Control mechanisms documented: {len(TRIAL_BALANCE_INSIGHTS['control_mechanisms'])}")
    
    return True

if __name__ == "__main__":
    main()
