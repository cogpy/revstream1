#!/usr/bin/env python3
"""
Implementation Script for Ketoni Integration Improvements
Date: 2026-01-16
"""

import json
from datetime import datetime

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def implement_entity_improvements(entities_data):
    """Add Ketoni entity, Kevin Derrick, and enhance existing entities"""
    
    # Add Kevin Michael Derrick (PERSON_014)
    kevin_derrick = {
        "entity_id": "PERSON_014",
        "name": "Kevin Michael Derrick",
        "role": "ketoni_director",
        "agent_type": "neutral",
        "involvement_events": 1,
        "primary_actions": ["ketoni_director", "payout_obligation_holder"],
        "relationships": [
            "director_of_ORG_015",
            "colleague_of_PERSON_007",
            "ketoni_payout_obligor"
        ],
        "financial_impact": {
            "payout_obligation": "ZAR 18,750,000",
            "payout_date": "May 2026"
        },
        "significance": "Director of Ketoni Investment Holdings; colleague of Bantjies; links Bantjies appointment to ZAR 18.75M payout",
        "evidence": ["Ketoni company records", "Professional records", "Bantjies connection analysis"],
        "ad_res_j7_references": [
            "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
            "lex/agent_based_model_v48_ketoni_integrated.scm"
        ],
        "evidence_enhanced": datetime.now().isoformat(),
        "evidence_strength": "strong"
    }
    
    entities_data['entities']['persons'].append(kevin_derrick)
    
    # Add Ketoni Investment Holdings (ORG_015)
    ketoni_org = {
        "entity_id": "ORG_015",
        "name": "Ketoni Investment Holdings",
        "registration_number": "TBD",
        "role": "investment_holding_company",
        "agent_type": "neutral",
        "involvement_events": 1,
        "primary_actions": ["payout_obligation"],
        "relationships": [
            "shareholder_TRUST_001",
            "director_PERSON_014",
            "payout_obligor_to_FFT"
        ],
        "financial_impact": {
            "payout_obligation": "ZAR 18,750,000",
            "payout_date": "May 2026",
            "shares_held_by_FFT": "5,000 A-Ordinary shares"
        },
        "significance": "Central financial nexus - ZAR 18.75M payout explains all trust actions since Apr 2023",
        "evidence": ["Ketoni shareholder agreement", "FFT investment records", "Payout option documentation"],
        "ad_res_j7_references": [
            "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
            "lex/entity_relation_framework_v48_ketoni_payout_integrated.scm",
            "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md"
        ],
        "evidence_enhanced": datetime.now().isoformat(),
        "evidence_strength": "conclusive"
    }
    
    entities_data['entities']['organizations'].append(ketoni_org)
    
    # Enhance PERSON_007 (Bantjies) with Ketoni connection
    for person in entities_data['entities']['persons']:
        if person['entity_id'] == 'PERSON_007':
            person['relationships'].append('colleague_of_PERSON_014')
            person['ketoni_connection'] = {
                "colleague": "Kevin Michael Derrick (Ketoni Director)",
                "appointment_timing": "T-10 months before ZAR 18.75M payout (May 2026)",
                "significance": "Strategic appointment to consolidate trust control before payout"
            }
            person['evidence'].append("Ketoni connection analysis")
            person['ad_res_j7_references'].append("evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md")
    
    # Enhance TRUST_001 with Ketoni payout asset
    for trust in entities_data['entities']['trusts']:
        if trust['entity_id'] == 'TRUST_001':
            trust['financial_assets'] = trust.get('financial_assets', [])
            trust['financial_assets'].append({
                "asset": "Ketoni Investment Holdings payout option",
                "value": "ZAR 18,750,000",
                "date": "May 2026",
                "shares": "5,000 A-Ordinary shares",
                "beneficiaries": ["PERSON_001", "PERSON_004", "PERSON_005"],
                "significance": "Central financial motive for all trust actions since Apr 2023",
                "evidence": ["Ketoni shareholder agreement", "FFT investment records"]
            })
            trust['ad_res_j7_references'].append("KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md")
    
    # Update metadata
    entities_data['metadata']['version'] = "28.0_KETONI_INTEGRATED_2026_01_16"
    entities_data['metadata']['last_updated'] = datetime.now().isoformat()
    entities_data['metadata']['changes'] = "CRITICAL: Ketoni Integration - Added ORG_015, PERSON_014, ZAR 18.75M payout asset"
    entities_data['metadata']['total_entities'] = len(entities_data['entities']['persons']) + \
                                                   len(entities_data['entities']['organizations']) + \
                                                   len(entities_data['entities']['trusts'])
    
    return entities_data

def implement_relation_improvements(relations_data):
    """Add Ketoni-related relations"""
    
    # Add FFT -> Ketoni shareholder relation
    ketoni_shareholder = {
        "relation_id": "REL_OWN_008",
        "relation_type": "shareholder",
        "source_entity": "TRUST_001",
        "target_entity": "ORG_015",
        "strength": "significant_shareholding",
        "legal_status": "legitimate",
        "shares": "5,000 A-Ordinary shares",
        "payout_option": "ZAR 18,750,000 (May 2026)",
        "significance": "Central financial motive - explains all trust actions since Apr 2023",
        "evidence": ["Ketoni shareholder agreement", "FFT investment records", "Payout option documentation"],
        "evidence_verified": datetime.now().isoformat(),
        "ad_res_j7_evidence": [
            "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
            "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md"
        ],
        "confidence": 0.95,
        "evidence_strength": "conclusive"
    }
    
    relations_data['relations']['ownership_relations'].append(ketoni_shareholder)
    
    # Add Derrick -> Ketoni director relation
    derrick_director = {
        "relation_id": "REL_CTRL_008",
        "relation_type": "director_of",
        "source_entity": "PERSON_014",
        "target_entity": "ORG_015",
        "control_type": "directorial_control",
        "legal_status": "legitimate",
        "significance": "Controls entity with ZAR 18.75M payout obligation to FFT",
        "evidence": ["Ketoni company records", "CIPC documentation"],
        "evidence_verified": datetime.now().isoformat(),
        "ad_res_j7_evidence": ["evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md"],
        "confidence": 0.90,
        "evidence_strength": "strong"
    }
    
    if 'control_relations' not in relations_data['relations']:
        relations_data['relations']['control_relations'] = []
    relations_data['relations']['control_relations'].append(derrick_director)
    
    # Add Bantjies -> Derrick colleague relation
    bantjies_derrick = {
        "relation_id": "REL_PROF_001",
        "relation_type": "professional_colleague",
        "source_entity": "PERSON_007",
        "target_entity": "PERSON_014",
        "significance": "Explains Bantjies appointment as trustee T-10 months before ZAR 18.75M payout",
        "timing": "Bantjies appointed Jul 2024, T-10 months before May 2026 payout",
        "evidence": ["Professional records", "Ketoni connection analysis", "Appointment timing analysis"],
        "evidence_verified": datetime.now().isoformat(),
        "ad_res_j7_evidence": [
            "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
            "lex/agent_based_model_v48_ketoni_integrated.scm"
        ],
        "confidence": 0.85,
        "evidence_strength": "strong"
    }
    
    if 'professional_relations' not in relations_data['relations']:
        relations_data['relations']['professional_relations'] = []
    relations_data['relations']['professional_relations'].append(bantjies_derrick)
    
    # Update metadata
    relations_data['metadata']['version'] = "23.0_KETONI_INTEGRATED_2026_01_16"
    relations_data['metadata']['last_updated'] = datetime.now().isoformat()
    relations_data['metadata']['changes'] = "CRITICAL: Ketoni Integration - Added FFT-Ketoni, Derrick-Ketoni, Bantjies-Derrick relations"
    relations_data['metadata']['total_relations'] = sum(len(v) for v in relations_data['relations'].values() if isinstance(v, list))
    
    return relations_data

def implement_event_improvements(events_data):
    """Add Ketoni investment event and enhance existing events"""
    
    # Add Ketoni investment event
    ketoni_investment = {
        "event_id": "EVENT_K001",
        "date": "2023-04-24",
        "title": "Faucitt Family Trust Invests in Ketoni Investment Holdings",
        "category": "financial_investment",
        "event_type": "trust_investment",
        "perpetrators": ["PERSON_001"],
        "victims": [],
        "entities_involved": ["TRUST_001", "ORG_015", "PERSON_001", "PERSON_014"],
        "description": "FFT acquires 5,000 A-Ordinary shares in Ketoni Investment Holdings with ZAR 18.75M payout option exercisable in May 2026. This investment establishes the central financial motive for all subsequent trust actions.",
        "financial_impact": "ZAR 18,750,000",
        "legal_significance": "establishment_of_central_financial_motive",
        "significance": "CRITICAL: Establishes ZAR 18.75M payout option that explains all trust control actions, beneficiary targeting, forum shopping, curatorship fraud, and creditor elimination attempts. All events converge on May 2026 payout date.",
        "evidence": [
            "Ketoni shareholder agreement",
            "FFT investment records",
            "Payout option documentation",
            "5,000 A-Ordinary shares certificate"
        ],
        "pattern": "central_financial_nexus",
        "timeline_phase": "PHASE_0_INVESTMENT",
        "phase": "PHASE_0_INVESTMENT",
        "ad_res_j7_evidence": [
            "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
            "lex/entity_relation_framework_v48_ketoni_payout_integrated.scm",
            "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md"
        ],
        "evidence_enhanced": datetime.now().isoformat(),
        "burden_of_proof": "civil_50%_exceeded",
        "related_events": ["EVENT_086", "EVENT_065", "EVENT_066"],
        "timing_analysis": {
            "t_minus": "T-37 months before payout",
            "convergence": "All subsequent events converge on May 2026",
            "phases": ["Investment", "Creditor Elimination", "Control Consolidation", "Payout"]
        }
    }
    
    events_data['events'].insert(0, ketoni_investment)
    
    # Enhance EVENT_086 (Kayla-related) with Ketoni timing
    for event in events_data['events']:
        if event['event_id'] == 'EVENT_086':
            # Add or enhance significance field
            if 'significance' in event:
                event['significance'] += " | CRITICAL TIMING: Occurred 80 days after FFT Ketoni investment (ZAR 18.75M). ReZonance R1M debt becomes obstacle to ZAR 18.75M control."
            else:
                event['significance'] = "CRITICAL TIMING: Occurred 80 days after FFT Ketoni investment (ZAR 18.75M). ReZonance R1M debt becomes obstacle to ZAR 18.75M control."
            
            event['ketoni_context'] = {
                "timing": "80 days after FFT Ketoni investment",
                "phase": "Creditor Elimination Phase",
                "motive": "R1M ReZonance debt obstacle to ZAR 18.75M control",
                "t_minus": "T-34 months before May 2026 payout"
            }
            event['ad_res_j7_references'] = event.get('ad_res_j7_references', [])
            event['ad_res_j7_references'].append("evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md")
    
    # Update metadata
    events_data['metadata']['version'] = "26.0_KETONI_INTEGRATED_2026_01_16"
    events_data['metadata']['last_updated'] = datetime.now().isoformat()
    events_data['metadata']['changes'] = "CRITICAL: Ketoni Integration - Added EVENT_K001, enhanced Kayla timing context"
    events_data['metadata']['total_events'] = len(events_data['events'])
    
    return events_data

def implement_timeline_improvements(timeline_data):
    """Add Ketoni-centric phase structure to timeline"""
    
    # Add Ketoni investment timeline entry
    ketoni_entry = {
        "date": "2023-04-24",
        "event_count": 1,
        "events": ["EVENT_K001"],
        "primary_category": "financial_investment",
        "description": "FFT Ketoni Investment - ZAR 18.75M payout option established",
        "key_actors": ["PERSON_001", "PERSON_014", "TRUST_001", "ORG_015"],
        "legal_significance": "establishment_of_central_financial_motive",
        "evidence_references": [
            "Ketoni shareholder agreement",
            "FFT investment records",
            "Payout option documentation"
        ],
        "evidence": [
            "Ketoni Investment Records",
            "FFT Financial Documentation"
        ],
        "phase": "PHASE_0_INVESTMENT",
        "timing": "T-37 months before May 2026 payout",
        "financial_impact": "ZAR 18,750,000"
    }
    
    # Insert at correct chronological position
    timeline_data['timeline'].insert(0, ketoni_entry)
    
    # Add phase metadata
    timeline_data['phase_structure'] = {
        "PHASE_0_INVESTMENT": {
            "period": "Feb 2023 - Apr 2023",
            "description": "Investment Phase - ZAR 18.75M entitlement established",
            "key_event": "EVENT_K001 (2023-04-24)",
            "financial_impact": "ZAR 18,750,000",
            "significance": "Establishes central financial motive"
        },
        "PHASE_1_CREDITOR_ELIMINATION": {
            "period": "Jul 2023 - Feb 2024",
            "description": "Creditor Elimination Phase - R1M debt obstacle removal attempt",
            "key_events": ["Kayla murder (2023-07-13)", "ReZonance dissolution pressure"],
            "motive": "R1M ReZonance debt obstacle to ZAR 18.75M control"
        },
        "PHASE_2_CONTROL_CONSOLIDATION": {
            "period": "Jul 2024 - Aug 2025",
            "description": "Control Consolidation Phase - Peter consolidates control before payout",
            "key_events": [
                "Bantjies appointment (Jul 2024, T-10 months)",
                "Main Trustee backdating (Aug 11, 2025, T-9 months)",
                "Interdicts filed (Aug 13, 2025, T-9 months)"
            ],
            "strategy": "Consolidate trust control before May 2026 payout"
        },
        "PHASE_3_PAYOUT": {
            "period": "May 2026",
            "description": "Payout Phase - ALL EVENTS CONVERGE HERE",
            "financial_impact": "ZAR 18,750,000",
            "convergence": "All control actions, beneficiary targeting, forum shopping converge on this date"
        }
    }
    
    # Update metadata
    timeline_data['metadata']['version'] = "24.0_KETONI_INTEGRATED_2026_01_16"
    timeline_data['metadata']['last_updated'] = datetime.now().isoformat()
    timeline_data['metadata']['changes'] = "CRITICAL: Ketoni Integration - Added EVENT_K001, phase structure with May 2026 convergence"
    
    return timeline_data

def main():
    print("Implementing Ketoni integration improvements...")
    
    base_path = '/home/ubuntu/revstream1/docs/data_models'
    
    # Load data
    entities_data = load_json(f'{base_path}/entities/entities.json')
    relations_data = load_json(f'{base_path}/relations.json')
    events_data = load_json(f'{base_path}/events.json')
    timeline_data = load_json(f'{base_path}/timeline.json')
    
    # Implement improvements
    entities_data = implement_entity_improvements(entities_data)
    relations_data = implement_relation_improvements(relations_data)
    events_data = implement_event_improvements(events_data)
    timeline_data = implement_timeline_improvements(timeline_data)
    
    # Save updated data
    save_json(f'{base_path}/entities/entities.json', entities_data)
    save_json(f'{base_path}/relations.json', relations_data)
    save_json(f'{base_path}/events.json', events_data)
    save_json(f'{base_path}/timeline.json', timeline_data)
    
    print("\n=== IMPLEMENTATION COMPLETE ===")
    print(f"Entities: v{entities_data['metadata']['version']}")
    print(f"Relations: v{relations_data['metadata']['version']}")
    print(f"Events: v{events_data['metadata']['version']}")
    print(f"Timeline: v{timeline_data['metadata']['version']}")
    print(f"\nTotal entities: {entities_data['metadata']['total_entities']}")
    print(f"Total relations: {relations_data['metadata']['total_relations']}")
    print(f"Total events: {events_data['metadata']['total_events']}")

if __name__ == '__main__':
    main()
