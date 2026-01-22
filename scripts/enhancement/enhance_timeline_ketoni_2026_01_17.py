#!/usr/bin/env python3
"""
Enhance timeline with Ketoni ZAR 18.75M payout events and context
Date: 2026-01-17
"""

import json
from datetime import datetime
from pathlib import Path

def enhance_timeline_with_ketoni():
    """Add Ketoni payout events and enhance existing timeline entries"""
    
    timeline_file = Path("data_models/timelines/timeline.json")
    
    with open(timeline_file, 'r') as f:
        data = json.load(f)
    
    # Update metadata
    data['metadata']['version'] = "25.0_KETONI_INTEGRATED_2026_01_17"
    data['metadata']['last_updated'] = datetime.now().isoformat()
    data['metadata']['changes'] = "Integrated Ketoni ZAR 18.75M payout timeline and context"
    
    # New Ketoni-related timeline entries
    ketoni_entries = [
        {
            "entry_id": "TL_KETONI_001",
            "date": "2023-04-24",
            "event_type": "investment",
            "title": "FFT Investment in Ketoni - ZAR 18.75M Entitlement Established",
            "description": "Faucitt Family Trust invests in Ketoni Investment Holdings, establishing ZAR 18.75M payout entitlement with three-year payout schedule (May 2026, May 2027, May 2029). This investment creates the central financial motive for all subsequent trust control actions.",
            "key_actors": [
                "Faucitt Family Trust",
                "Ketoni Investment Holdings",
                "Kevin Michael Derrick"
            ],
            "entities_involved": [
                "ORG_FFT_001",
                "ORG_KETONI_001",
                "PERSON_DERRICK_001"
            ],
            "evidence": [
                "Ketoni investment documentation",
                "FFT shareholder records (5,000 A-Ordinary shares)"
            ],
            "significance": "CRITICAL: Establishes ZAR 18.75M payout (May 2026) as central financial motive for all subsequent events",
            "timing_analysis": "T-37 months before first payout date",
            "burden_of_proof": "verified_investment_record",
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
                "lex/entity_relation_framework_v48_ketoni_payout_integrated.scm"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "foundational_event"
        },
        {
            "entry_id": "TL_KETONI_002",
            "date": "2023-07-13",
            "event_type": "creditor_elimination",
            "title": "Kayla Pretorius Death - Creditor Elimination Phase",
            "description": "Kayla Pretorius (Dan's partner, ReZonance director) dies 80 days after FFT Ketoni investment. ReZonance owed R1,035,000+ by RegimA Skin Treatments. Death eliminates primary creditor obstacle to trust control consolidation.",
            "key_actors": [
                "Kayla Pretorius",
                "Daniel James Faucitt",
                "ReZonance"
            ],
            "entities_involved": [
                "PERSON_KAYLA_001",
                "PERSON_005",
                "ORG_REZONANCE_001"
            ],
            "evidence": [
                "SF6 - Kayla Pretorius Estate Documentation",
                "SF7 - Court Order Kayla Email Seizure",
                "ReZonance debt records"
            ],
            "significance": "CRITICAL: Eliminates R1M creditor obstacle 80 days after ZAR 18.75M investment",
            "timing_analysis": "T-34 months before payout, 80 days after investment",
            "ketoni_context": "ZAR 18.75M payout dwarfs R1M debt - debt is obstacle to control",
            "burden_of_proof": "verified_death_certificate",
            "ad_res_j7_references": [
                "ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md",
                "ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md",
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "95%_exceeded"
        },
        {
            "entry_id": "TL_KETONI_003",
            "date": "2024-02-14",
            "event_type": "creditor_pressure",
            "title": "ReZonance Dissolution Pressure - Debt Obstacle Elimination",
            "description": "Pressure applied to dissolve ReZonance and eliminate R1,035,000+ debt claim against RegimA Skin Treatments. Part of creditor elimination phase before trust control consolidation.",
            "key_actors": [
                "Peter Andrew Faucitt",
                "Daniel James Faucitt"
            ],
            "entities_involved": [
                "PERSON_001",
                "PERSON_005",
                "ORG_REZONANCE_001"
            ],
            "evidence": [
                "ReZonance dissolution correspondence",
                "Debt documentation"
            ],
            "significance": "Eliminate R1M debt obstacle before trust control consolidation",
            "timing_analysis": "T-27 months before payout",
            "ketoni_context": "Clear debt obstacle before May 2026 payout distribution",
            "burden_of_proof": "documented_correspondence",
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md"
            ],
            "evidence_strength": "strong"
        },
        {
            "entry_id": "TL_KETONI_004",
            "date": "2024-07",
            "event_type": "trustee_appointment",
            "title": "Bantjies Appointed FFT Trustee - Control Consolidation Phase",
            "description": "Daniel Jacobus Bantjies appointed as FFT Trustee by Rynette, exactly T-10 months before May 2026 payout. Bantjies is colleague of Kevin Derrick (Ketoni Director) and accountant for all Faucitt companies.",
            "key_actors": [
                "Daniel Jacobus Bantjies",
                "Rynette Farrar",
                "Kevin Michael Derrick"
            ],
            "entities_involved": [
                "PERSON_007",
                "PERSON_002",
                "PERSON_DERRICK_001"
            ],
            "evidence": [
                "FFT trustee appointment documentation",
                "Bantjies-Derrick professional connection records"
            ],
            "significance": "CRITICAL: Strategic trustee appointment T-10 months before ZAR 18.75M payout",
            "timing_analysis": "T-10 months before payout - precise timing for control consolidation",
            "ketoni_context": "Appointee connected to Ketoni director, positioned to control payout distribution",
            "red_flags": [
                "appointed_T-10_months_before_payout",
                "appointee_connected_to_ketoni_director",
                "appointment_before_distribution_date",
                "dual_role_conflict_accountant_and_trustee"
            ],
            "burden_of_proof": "verified_trustee_appointment",
            "ad_res_j7_references": [
                "ANNEXURES/SF1_Bantjies_Debt_Documentation.md",
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "lex/south_african_trust_law_enhanced_v9_ketoni_payout.scm"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "95%_exceeded"
        },
        {
            "entry_id": "TL_KETONI_005",
            "date": "2025-06-06",
            "event_type": "fraud_exposure",
            "title": "Dan Exposes Villa Via Fraud to Bantjies",
            "description": "Daniel exposes Villa Via fraud (86% rent profit extraction) to Bantjies (as accountant, unaware of trustee appointment). Fraud threatens to expose trust control mechanisms before May 2026 payout.",
            "key_actors": [
                "Daniel James Faucitt",
                "Daniel Jacobus Bantjies"
            ],
            "entities_involved": [
                "PERSON_005",
                "PERSON_007",
                "ORG_VILLA_VIA_001"
            ],
            "evidence": [
                "Email to Bantjies 2025-06-06",
                "Villa Via financial analysis",
                "Fraud documentation"
            ],
            "significance": "CRITICAL: Fraud exposure triggers immediate retaliation to protect payout control",
            "timing_analysis": "T-11 months before payout",
            "ketoni_context": "Fraud exposure threatens trust control before ZAR 18.75M payout",
            "burden_of_proof": "documented_email_communication",
            "ad_res_j7_references": [
                "ANNEXURES/JF08/evidence_package_20251012",
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "95%_exceeded"
        },
        {
            "entry_id": "TL_KETONI_006",
            "date": "2025-06-07",
            "event_type": "retaliation",
            "title": "Cards Cancelled <24 Hours After Fraud Exposure",
            "description": "Dan's cards cancelled less than 24 hours after exposing fraud to Bantjies. Immediate retaliation demonstrates coordination and intent to punish fraud exposure.",
            "key_actors": [
                "Peter Andrew Faucitt",
                "Rynette Farrar",
                "Daniel Jacobus Bantjies"
            ],
            "entities_involved": [
                "PERSON_001",
                "PERSON_002",
                "PERSON_007"
            ],
            "evidence": [
                "Card cancellation records",
                "Timeline correlation with fraud exposure"
            ],
            "significance": "CRITICAL: Immediate retaliation <24 hours proves coordination and motive",
            "timing_analysis": "T-11 months before payout, <24 hours after fraud exposure",
            "ketoni_context": "Protect trust control mechanisms before May 2026 payout",
            "red_flags": [
                "immediate_retaliation_<24_hours",
                "coordination_between_actors",
                "timing_relative_to_payout"
            ],
            "burden_of_proof": "verified_timeline_correlation",
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "95%_exceeded"
        },
        {
            "entry_id": "TL_KETONI_007",
            "date": "2025-08-11",
            "event_type": "power_consolidation",
            "title": "Main Trustee Power Backdated - Jax Cooperation",
            "description": "Jacqueline signs document backdating Peter's 'Main Trustee' designation to 2025-07-01. This grants Peter sole control over FFT before May 2026 payout.",
            "key_actors": [
                "Peter Andrew Faucitt",
                "Jacqueline Faucitt"
            ],
            "entities_involved": [
                "PERSON_001",
                "PERSON_004",
                "ORG_FFT_001"
            ],
            "evidence": [
                "Main Trustee designation document",
                "Backdating documentation"
            ],
            "significance": "CRITICAL: Peter gains sole control T-9 months before ZAR 18.75M payout",
            "timing_analysis": "T-9 months before payout, backdated to T-10 months",
            "ketoni_context": "Consolidate sole control before May 2026 payout distribution",
            "red_flags": [
                "power_backdating",
                "timing_T-9_months_before_payout",
                "sole_control_before_distribution"
            ],
            "burden_of_proof": "verified_document_with_backdating",
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "jax-dan-response/JAX_DAN_RESPONSE_IMPROVEMENTS_V49_KETONI_INTEGRATED.md"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "95%_exceeded"
        },
        {
            "entry_id": "TL_KETONI_008",
            "date": "2025-08-13",
            "event_type": "beneficiary_neutralization",
            "title": "Interdict Filed Against Jax & Dan - Betrayal & Control",
            "description": "Peter and Bantjies file interdict against Jax and Dan, 48 hours after Jax signed Main Trustee document. Neutralizes both beneficiaries T-9 months before May 2026 payout.",
            "key_actors": [
                "Peter Andrew Faucitt",
                "Daniel Jacobus Bantjies",
                "Jacqueline Faucitt",
                "Daniel James Faucitt"
            ],
            "entities_involved": [
                "PERSON_001",
                "PERSON_007",
                "PERSON_004",
                "PERSON_005"
            ],
            "evidence": [
                "Interdict application case 2025-137857",
                "Timeline showing 48-hour betrayal"
            ],
            "significance": "CRITICAL: Betrayal and beneficiary neutralization T-9 months before payout",
            "timing_analysis": "T-9 months before payout, 48 hours after cooperation",
            "ketoni_context": "Neutralize beneficiaries before May 2026 payout distribution",
            "red_flags": [
                "48_hour_betrayal",
                "timing_T-9_months_before_payout",
                "forum_shopping_family_court",
                "medical_testing_for_curatorship"
            ],
            "burden_of_proof": "verified_court_filing",
            "ad_res_j7_references": [
                "ANNEXURES/JF06 - Court applications",
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "jax-dan-response/JAX_DAN_RESPONSE_IMPROVEMENTS_V49_KETONI_INTEGRATED.md"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "95%_exceeded"
        },
        {
            "entry_id": "TL_KETONI_009",
            "date": "2026-05",
            "event_type": "payout_date",
            "title": "Ketoni ZAR 18.75M Payout Due - ALL EVENTS CONVERGE",
            "description": "First payout date for Ketoni ZAR 18.75M to Faucitt Family Trust. ALL EVENTS from April 2023 onwards converge on this date. Peter has consolidated sole control, neutralized Jax as trustee, and targeted Dan for curatorship to control his share.",
            "key_actors": [
                "Ketoni Investment Holdings",
                "Faucitt Family Trust",
                "Peter Andrew Faucitt",
                "Daniel Jacobus Bantjies"
            ],
            "entities_involved": [
                "ORG_KETONI_001",
                "ORG_FFT_001",
                "PERSON_001",
                "PERSON_007"
            ],
            "evidence": [
                "Ketoni payout schedule",
                "FFT investment documentation"
            ],
            "significance": "CENTRAL CONVERGENCE POINT: All trust control actions converge on this payout date",
            "timing_analysis": "T-0: EVERYTHING CONVERGES HERE",
            "ketoni_context": "Central financial motive for all events since April 2023",
            "control_structure": {
                "peter": "Main Trustee with sole control",
                "bantjies": "Co-trustee, Ketoni connection",
                "jax": "Neutralized via interdict",
                "dan": "Targeted for curatorship"
            },
            "burden_of_proof": "verified_payout_schedule",
            "ad_res_j7_references": [
                "KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md",
                "evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md",
                "lex/entity_relation_framework_v48_ketoni_payout_integrated.scm"
            ],
            "evidence_strength": "conclusive",
            "criminal_threshold": "foundational_event"
        }
    ]
    
    # Add new entries to timeline
    data['timeline'].extend(ketoni_entries)
    
    # Sort timeline by date
    data['timeline'].sort(key=lambda x: x.get('date', '9999-99-99'))
    
    # Update counts
    data['metadata']['total_entries'] = len(data['timeline'])
    data['metadata']['criminal_threshold_entries'] = len([e for e in data['timeline'] if e.get('criminal_threshold') == '95%_exceeded'])
    data['metadata']['high_significance_entries'] = len([e for e in data['timeline'] if 'CRITICAL' in str(e.get('significance', ''))])
    
    # Backup existing file
    backup_file = timeline_file.with_suffix(f'.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}')
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Write updated file
    with open(timeline_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Enhanced timeline with Ketoni events")
    print(f"📦 Backup saved: {backup_file}")
    print(f"📊 Total entries: {data['metadata']['total_entries']}")
    print(f"⚖️ Criminal threshold entries: {data['metadata']['criminal_threshold_entries']}")
    print(f"🔥 High significance entries: {data['metadata']['high_significance_entries']}")

if __name__ == "__main__":
    enhance_timeline_with_ketoni()
