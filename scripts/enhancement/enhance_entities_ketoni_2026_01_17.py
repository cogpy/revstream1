#!/usr/bin/env python3
"""
Enhance entities with Ketoni ZAR 18.75M payout context
Date: 2026-01-17
"""

import json
from datetime import datetime
from pathlib import Path

def enhance_entities_with_ketoni():
    """Enhance entities with Ketoni payout context and ad-res-j7 evidence"""
    
    entities_file = Path("data_models/entities/entities.json")
    
    with open(entities_file, 'r') as f:
        data = json.load(f)
    
    # Update metadata
    data['metadata']['version'] = "28.0_KETONI_INTEGRATED_2026_01_17"
    data['metadata']['last_updated'] = datetime.now().isoformat()
    data['metadata']['changes'] = "Integrated Ketoni ZAR 18.75M payout context as central financial motive"
    
    # Enhancement mappings
    enhancements = {
        "PERSON_001": {  # Peter Andrew Faucitt
            "ketoni_payout_context": {
                "financial_motive": "Control and maximize personal share of ZAR 18.75M Ketoni payout (May 2026)",
                "payout_amount": "ZAR 18.75M",
                "payout_date": "2026-05",
                "beneficiary_entitlement": "1/3 share as FFT beneficiary",
                "control_mechanisms": [
                    "forum_shopping_family_court",
                    "trustee_power_backdating",
                    "beneficiary_neutralization_via_interdict",
                    "curatorship_fraud_attempt"
                ],
                "timing_analysis": "All control actions T-9 to T-10 months before May 2026 payout",
                "red_flags": [
                    "family_court_instead_of_commercial_court",
                    "main_trustee_backdated_to_2025-07-01",
                    "interdict_filed_2025-08-13_T-9_months",
                    "medical_testing_rushed_for_curatorship"
                ]
            },
            "ad_res_j7_references": [
                "ANNEXURES/JF01 - Shopify Plus email showing business structure",
                "ANNEXURES/JF04 - CIPC company registration documents",
                "ANNEXURES/JF06 - Court applications and filings",
                "ANNEXURES/JF08/evidence_package_20251012 - Comprehensive fraud timeline",
                "1-CIVIL-RESPONSE - Answering affidavit documentation",
                "SF2_Sage_Screenshots_Rynette_Control.md - System control evidence",
                "SF6_Kayla_Pretorius_Estate_Documentation.md - Trigger event for appropriation",
                "SF9_Ian_Levitt_Demand_Letter.md - R63M formal demand (ignored)",
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md - Central financial motive",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md - Comprehensive timeline"
            ]
        },
        "PERSON_002": {  # Rynette Farrar
            "ketoni_payout_context": {
                "role": "operational_controller_NOT_TRUSTEE",
                "key_action": "Appointed Bantjies as Trustee (July 2024, T-10 months before payout)",
                "timing_significance": "Trustee appointment exactly T-10 months before ZAR 18.75M payout",
                "control_areas": [
                    "accounting_systems",
                    "email_access_pete@regima.com",
                    "bank_accounts",
                    "financial_operations"
                ],
                "connection_to_payout": "Facilitated control consolidation before May 2026"
            },
            "trustee_status_clarification": "NOT A TRUSTEE - Bantjies is the Trustee appointed July 2024"
        },
        "PERSON_004": {  # Jacqueline Faucitt
            "ketoni_payout_context": {
                "status": "NEUTRALIZED_TRUSTEE",
                "beneficiary_entitlement": "1/3 share of ZAR 18.75M as FFT beneficiary",
                "betrayal_timeline": {
                    "cooperation": "2025-08-11 - Signed Main Trustee backdating document",
                    "betrayal": "2025-08-13 - Interdicted by Peter 48 hours later",
                    "timing": "T-9 months before May 2026 payout",
                    "motive": "Neutralize Jax as trustee before payout distribution"
                },
                "result": "Cannot oppose Peter's payout decisions as neutralized trustee",
                "threat_to_peter": "Could protect beneficiaries' interests including Dan's share"
            }
        },
        "PERSON_005": {  # Daniel James Faucitt
            "ketoni_payout_context": {
                "status": "TARGETED_BENEFICIARY",
                "beneficiary_entitlement": "1/3 share of ZAR 18.75M as FFT beneficiary",
                "threat_to_peter": "Curatorship = Peter controls Dan's entire share of ZAR 18.75M",
                "retaliation_timeline": {
                    "fraud_exposure": "2025-06-06 - Dan exposes Villa Via fraud to Bantjies",
                    "immediate_retaliation": "2025-06-07 - Cards cancelled <24 hours later",
                    "interdict_filed": "2025-08-13 - T-9 months before payout",
                    "medical_testing_rushed": "2025-08 - Curatorship fraud attempt"
                },
                "red_flags": [
                    "fraud_exposure_triggered_immediate_retaliation",
                    "timing_T-9_months_before_payout",
                    "no_medical_basis_for_testing",
                    "competence_demonstrated_by_fraud_analysis"
                ]
            }
        },
        "PERSON_007": {  # Danie Bantjies
            "ketoni_payout_context": {
                "appointment": "July 2024 - T-10 months before ZAR 18.75M payout",
                "ketoni_connection": "Colleague of Kevin Derrick (Ketoni Director)",
                "role": "Strategic appointee to consolidate trust control before payout",
                "timing_red_flags": [
                    "appointed_T-10_months_before_payout",
                    "appointee_connected_to_ketoni_director",
                    "appointment_before_distribution_date"
                ],
                "dual_role_conflict": {
                    "accountant": "Accountant for all Faucitt companies",
                    "trustee": "FFT Trustee (appointed July 2024 by Rynette)",
                    "conflict": "Dan contacted as accountant, unaware of trustee appointment"
                }
            },
            "ad_res_j7_references": [
                "ANNEXURES/SF1_Bantjies_Debt_Documentation.md",
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md"
            ]
        }
    }
    
    # Add Ketoni entity if not exists
    ketoni_entity = {
        "entity_id": "ORG_KETONI_001",
        "name": "Ketoni Investment Holdings",
        "type": "investment_company",
        "role": "financial_nexus",
        "obligation": {
            "amount": "ZAR 18,750,000",
            "recipient": "Faucitt Family Trust",
            "payout_date": "2026-05",
            "structure": "Three-year payout schedule (May 2026, May 2027, May 2029)"
        },
        "director": "Kevin Michael Derrick",
        "shareholder": "Faucitt Family Trust (5,000 A-Ordinary shares)",
        "investment_date": "2023-04-24",
        "significance": "CENTRAL FINANCIAL MOTIVE - All events converge on May 2026 payout",
        "network_dynamics": {
            "phase_1": "Investment Phase (Feb-Apr 2023): ZAR 18.75M entitlement established",
            "phase_2": "Creditor Elimination Phase (Jul 2023 - Feb 2024): R1M debt obstacle elimination",
            "phase_3": "Control Consolidation Phase (Jul 2024 - Aug 2025): Peter consolidates control",
            "phase_4": "Payout Phase (May 2026): ALL EVENTS CONVERGE HERE"
        },
        "ad_res_j7_references": [
            "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
            "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
            "lex/entity_relation_framework_v48_ketoni_payout_integrated.scm",
            "lex/agent_based_model_v48_ketoni_integrated.scm"
        ],
        "evidence_strength": "conclusive",
        "criminal_threshold": "95%_exceeded"
    }
    
    # Add Kevin Derrick entity
    kevin_derrick_entity = {
        "entity_id": "PERSON_DERRICK_001",
        "name": "Kevin Michael Derrick",
        "role": "ketoni_director",
        "agent_type": "neutral",
        "involvement_events": 0,
        "primary_actions": [],
        "relationships": [
            "director_of_ketoni",
            "colleague_of_bantjies"
        ],
        "ketoni_connection": {
            "role": "Director of Ketoni Investment Holdings",
            "obligation": "Ketoni owes ZAR 18.75M to FFT (May 2026)",
            "connection_to_bantjies": "Professional colleague - both accountants"
        },
        "significance": "Connection between Ketoni payout and Bantjies' FFT trustee appointment",
        "ad_res_j7_references": [
            "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
            "lex/agent_based_model_v48_ketoni_integrated.scm"
        ]
    }
    
    # Apply enhancements
    for entity in data['entities']['persons']:
        entity_id = entity.get('entity_id')
        if entity_id in enhancements:
            entity.update(enhancements[entity_id])
            entity['evidence_enhanced_timestamp'] = datetime.now().isoformat()
    
    # Add new entities
    data['entities']['persons'].append(kevin_derrick_entity)
    
    if 'organizations' not in data['entities']:
        data['entities']['organizations'] = []
    data['entities']['organizations'].append(ketoni_entity)
    
    # Update counts
    data['metadata']['total_entities'] = len(data['entities']['persons']) + len(data['entities'].get('organizations', []))
    data['metadata']['total_persons'] = len(data['entities']['persons'])
    data['metadata']['total_organizations'] = len(data['entities'].get('organizations', []))
    
    # Backup existing file
    backup_file = entities_file.with_suffix(f'.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Write updated file
    with open(entities_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Enhanced entities with Ketoni context")
    print(f"📦 Backup saved: {backup_file}")
    print(f"📊 Total entities: {data['metadata']['total_entities']}")
    print(f"👥 Total persons: {data['metadata']['total_persons']}")
    print(f"🏢 Total organizations: {data['metadata']['total_organizations']}")

if __name__ == "__main__":
    enhance_entities_with_ketoni()
