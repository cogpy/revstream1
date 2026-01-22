#!/usr/bin/env python3
"""
Enhance relations with Ketoni ZAR 18.75M payout context
Date: 2026-01-17
"""

import json
from datetime import datetime
from pathlib import Path

def enhance_relations_with_ketoni():
    """Add Ketoni-related relations and enhance existing relations"""
    
    relations_file = Path("data_models/relations/relations.json")
    
    with open(relations_file, 'r') as f:
        data = json.load(f)
    
    # Update metadata
    data['metadata']['version'] = "23.0_KETONI_INTEGRATED_2026_01_17"
    data['metadata']['last_updated'] = datetime.now().isoformat()
    data['metadata']['changes'] = "Integrated Ketoni ZAR 18.75M payout relations and context"
    
    # New Ketoni-related relations
    ketoni_relations = [
        {
            "relation_id": "REL_KETONI_001",
            "relation_type": "financial_obligation",
            "source_entity": "ORG_KETONI_001",
            "source_name": "Ketoni Investment Holdings",
            "target_entity": "ORG_FFT_001",
            "target_name": "Faucitt Family Trust",
            "description": "Ketoni owes ZAR 18.75M to FFT with three-year payout schedule (May 2026, May 2027, May 2029)",
            "relationship_details": {
                "obligation_amount": "ZAR 18,750,000",
                "first_payout_date": "2026-05",
                "investment_date": "2023-04-24",
                "structure": "Three-year payout schedule"
            },
            "significance": "CENTRAL FINANCIAL MOTIVE for all trust control actions",
            "evidence": [
                "Ketoni investment documentation",
                "FFT shareholder records"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_KETONI_002",
            "relation_type": "beneficiary_entitlement",
            "source_entity": "PERSON_001",
            "source_name": "Peter Andrew Faucitt",
            "target_entity": "ORG_FFT_001",
            "target_name": "Faucitt Family Trust",
            "description": "Peter is FFT beneficiary entitled to 1/3 share of ZAR 18.75M Ketoni payout",
            "relationship_details": {
                "entitlement": "1/3 share of ZAR 18.75M",
                "estimated_share": "ZAR 6,250,000",
                "payout_date": "2026-05",
                "control_motive": "Maximize personal share by controlling other beneficiaries"
            },
            "significance": "Peter's financial motive for trust control consolidation",
            "ketoni_context": "Explains forum shopping, trustee power backdating, beneficiary neutralization",
            "evidence": [
                "FFT trust deed",
                "Beneficiary records"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "lex/agent_based_model_v48_ketoni_integrated.scm"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_KETONI_003",
            "relation_type": "beneficiary_entitlement",
            "source_entity": "PERSON_004",
            "source_name": "Jacqueline Faucitt",
            "target_entity": "ORG_FFT_001",
            "target_name": "Faucitt Family Trust",
            "description": "Jax is FFT beneficiary entitled to 1/3 share of ZAR 18.75M Ketoni payout",
            "relationship_details": {
                "entitlement": "1/3 share of ZAR 18.75M",
                "estimated_share": "ZAR 6,250,000",
                "payout_date": "2026-05",
                "status": "NEUTRALIZED via interdict 2025-08-13"
            },
            "significance": "Jax neutralized as trustee to prevent opposition to Peter's payout decisions",
            "ketoni_context": "48-hour betrayal after Main Trustee document signing",
            "evidence": [
                "FFT trust deed",
                "Interdict application"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "jax-dan-response/JAX_DAN_RESPONSE_IMPROVEMENTS_V49_KETONI_INTEGRATED.md"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_KETONI_004",
            "relation_type": "beneficiary_entitlement",
            "source_entity": "PERSON_005",
            "source_name": "Daniel James Faucitt",
            "target_entity": "ORG_FFT_001",
            "target_name": "Faucitt Family Trust",
            "description": "Dan is FFT beneficiary entitled to 1/3 share of ZAR 18.75M Ketoni payout",
            "relationship_details": {
                "entitlement": "1/3 share of ZAR 18.75M",
                "estimated_share": "ZAR 6,250,000",
                "payout_date": "2026-05",
                "threat": "Curatorship = Peter controls Dan's entire share"
            },
            "significance": "Dan targeted for curatorship fraud to control his ZAR 6.25M share",
            "ketoni_context": "Medical testing rushed T-9 months before payout after fraud exposure",
            "evidence": [
                "FFT trust deed",
                "Interdict application",
                "Medical testing documentation"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "jax-dan-response/JAX_DAN_RESPONSE_IMPROVEMENTS_V49_KETONI_INTEGRATED.md"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_KETONI_005",
            "relation_type": "professional_connection",
            "source_entity": "PERSON_007",
            "source_name": "Daniel Jacobus Bantjies",
            "target_entity": "PERSON_DERRICK_001",
            "target_name": "Kevin Michael Derrick",
            "description": "Bantjies (FFT Trustee) is professional colleague of Kevin Derrick (Ketoni Director)",
            "relationship_details": {
                "connection_type": "Professional colleagues (both accountants)",
                "bantjies_role": "FFT Trustee appointed July 2024",
                "derrick_role": "Ketoni Director",
                "timing": "Bantjies appointed T-10 months before Ketoni payout"
            },
            "significance": "Connection between Ketoni payout and Bantjies' strategic trustee appointment",
            "ketoni_context": "Appointee connected to Ketoni director positioned to control payout",
            "red_flags": [
                "trustee_connected_to_payout_source",
                "appointment_timing_T-10_months",
                "conflict_of_interest"
            ],
            "evidence": [
                "Professional connection records",
                "Trustee appointment documentation"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "lex/south_african_trust_law_enhanced_v9_ketoni_payout.scm"
            ],
            "evidence_strength": "strong"
        },
        {
            "relation_id": "REL_KETONI_006",
            "relation_type": "director",
            "source_entity": "PERSON_DERRICK_001",
            "source_name": "Kevin Michael Derrick",
            "target_entity": "ORG_KETONI_001",
            "target_name": "Ketoni Investment Holdings",
            "description": "Kevin Derrick is Director of Ketoni Investment Holdings",
            "relationship_details": {
                "role": "Director",
                "obligation": "Ketoni owes ZAR 18.75M to FFT (May 2026)",
                "connection": "Colleague of Bantjies (FFT Trustee)"
            },
            "significance": "Links Ketoni payout to FFT trustee through professional connection",
            "evidence": [
                "CIPC director records",
                "Ketoni company documentation"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md"
            ],
            "evidence_strength": "verified_cipc_record"
        },
        {
            "relation_id": "REL_KETONI_007",
            "relation_type": "shareholder",
            "source_entity": "ORG_FFT_001",
            "source_name": "Faucitt Family Trust",
            "target_entity": "ORG_KETONI_001",
            "target_name": "Ketoni Investment Holdings",
            "description": "FFT holds 5,000 A-Ordinary shares in Ketoni Investment Holdings",
            "relationship_details": {
                "shares": "5,000 A-Ordinary shares",
                "investment_date": "2023-04-24",
                "payout_entitlement": "ZAR 18.75M (May 2026, May 2027, May 2029)"
            },
            "significance": "Establishes FFT's financial interest in Ketoni",
            "evidence": [
                "Share certificates",
                "Investment documentation"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_KETONI_008",
            "relation_type": "trustee_appointment",
            "source_entity": "PERSON_002",
            "source_name": "Rynette Farrar",
            "target_entity": "PERSON_007",
            "target_name": "Daniel Jacobus Bantjies",
            "description": "Rynette appointed Bantjies as FFT Trustee in July 2024",
            "relationship_details": {
                "appointment_date": "2024-07",
                "timing": "T-10 months before Ketoni payout",
                "rynette_role": "Operational controller (NOT TRUSTEE)",
                "significance": "Strategic appointment before payout"
            },
            "significance": "Rynette facilitated control consolidation by appointing Ketoni-connected trustee",
            "ketoni_context": "Precise timing T-10 months before ZAR 18.75M payout",
            "red_flags": [
                "timing_T-10_months_before_payout",
                "appointee_connected_to_ketoni",
                "control_consolidation_before_distribution"
            ],
            "evidence": [
                "Trustee appointment documentation"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "lex/agent_based_model_v48_ketoni_integrated.scm"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "relation_id": "REL_KETONI_009",
            "relation_type": "co_trustee",
            "source_entity": "PERSON_001",
            "source_name": "Peter Andrew Faucitt",
            "target_entity": "PERSON_007",
            "target_name": "Daniel Jacobus Bantjies",
            "description": "Peter and Bantjies are co-trustees of FFT with control before May 2026 payout",
            "relationship_details": {
                "peter_role": "Main Trustee (backdated to 2025-07-01)",
                "bantjies_role": "Co-trustee (appointed July 2024)",
                "control_structure": "Peter + Bantjies control trust before May 2026",
                "jax_status": "Neutralized via interdict",
                "dan_status": "Targeted for curatorship"
            },
            "significance": "Control structure consolidated before ZAR 18.75M payout distribution",
            "ketoni_context": "Ensures Peter controls payout distribution with Bantjies' support",
            "evidence": [
                "Main Trustee designation document",
                "Trustee appointment records",
                "Interdict application"
            ],
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "lex/entity_relation_framework_v48_ketoni_payout_integrated.scm"
            ],
            "evidence_strength": "conclusive"
        }
    ]
    
    # Add new relations
    if 'relations' not in data:
        data['relations'] = {}
    if 'ketoni_relations' not in data['relations']:
        data['relations']['ketoni_relations'] = []
    data['relations']['ketoni_relations'].extend(ketoni_relations)
    
    # Update counts
    total_count = sum(len(v) for v in data['relations'].values() if isinstance(v, list))
    data['metadata']['total_relations'] = total_count
    
    # Backup existing file
    backup_file = relations_file.with_suffix(f'.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Write updated file
    with open(relations_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Enhanced relations with Ketoni context")
    print(f"📦 Backup saved: {backup_file}")
    print(f"📊 Total relations: {data['metadata']['total_relations']}")

if __name__ == "__main__":
    enhance_relations_with_ketoni()
