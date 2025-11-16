import json
import os
from datetime import datetime

def extract_timeline_events():
    """Extract key timeline events from ad-res-j7 evidence"""
    
    # New events discovered from ad-res-j7 timeline analysis
    new_events = [
        {
            "event_id": "EVENT_H018",
            "date": "2020-08-13",
            "title": "Bantjies Sends Trial Balance Email to Bernadine Wright",
            "category": "accounting_fraud",
            "event_type": "financial_system_control_documentation",
            "perpetrators": ["PERSON_007"],
            "entities_involved": ["PERSON_010", "ORG_001"],
            "description": "Bantjies sends trial balance email to Bernadine Wright for financial statement finalization meeting, demonstrating his control over financial systems and accounting records",
            "legal_significance": "demonstrates_bantjies_control_of_financial_systems",
            "evidence": ["trial_balance_email_2020_08_13"],
            "pattern": "historical_foundation"
        },
        {
            "event_id": "EVENT_054",
            "date": "2025-01-15",
            "title": "Chantal Delivers Letter About Kayla Estate Finalization",
            "category": "estate_fraud",
            "event_type": "estate_exploitation_communication",
            "perpetrators": [],
            "victims": ["PERSON_008"],
            "entities_involved": ["PERSON_011"],
            "description": "Chantal delivers letter to office regarding Kayla estate finalization, indicating ongoing exploitation of deceased victim's estate",
            "legal_significance": "continued_exploitation_of_deceased_victims_estate",
            "evidence": ["chantal_letter_january_2025"],
            "pattern": "debt_accumulation"
        },
        {
            "event_id": "EVENT_055",
            "date": "2025-04-22",
            "title": "Peter Orders Cloud IT Systems Removal",
            "category": "evidence_tampering",
            "event_type": "infrastructure_control_seizure",
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_005"],
            "entities_involved": ["ORG_001"],
            "description": "Peter instructs removal of all cloud IT systems, systematic dismantling of cloud-based infrastructure as preparation for evidence destruction",
            "financial_impact": "unknown_amount",
            "legal_significance": "evidence_tampering_preparation_obstruction_of_justice",
            "evidence": ["it_system_removal_instruction"],
            "pattern": "escalation_phase"
        },
        {
            "event_id": "EVENT_056",
            "date": "2025-04-30",
            "title": "Server Missing from Office",
            "category": "evidence_tampering",
            "event_type": "physical_evidence_removal",
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_005"],
            "entities_involved": ["ORG_001"],
            "description": "Physical server hardware disappears from office premises, potential evidence destruction or data harvesting in preparation for subsequent financial crimes",
            "legal_significance": "evidence_tampering_obstruction_of_justice",
            "evidence": ["office_inventory_records"],
            "pattern": "escalation_phase"
        },
        {
            "event_id": "EVENT_057",
            "date": "2025-06-06",
            "title": "Daniel Sends Comprehensive Reports to Bantjies",
            "category": "transparency",
            "event_type": "full_disclosure",
            "perpetrators": [],
            "victims": [],
            "entities_involved": ["PERSON_005", "PERSON_007"],
            "description": "Daniel sends comprehensive documentation to Bantjies including listing of all companies, Shopify store operations, and preliminary reports, demonstrating full transparency",
            "legal_significance": "evidence_of_full_disclosure_and_transparency",
            "evidence": ["email_to_bantjies_2025_06_06"],
            "pattern": "consolidation_phase"
        },
        {
            "event_id": "EVENT_058",
            "date": "2025-06-10",
            "title": "Bantjies Learns of Criminal Matters",
            "category": "knowledge_acquisition",
            "event_type": "fraud_and_murder_disclosure",
            "perpetrators": [],
            "victims": [],
            "entities_involved": ["PERSON_007", "PERSON_005"],
            "description": "Daniel reports to Bantjies about Kayla's murder (August 2023) and Peter stealing funds after murder, including over R1.8M owed to Rezonance. Bantjies acquires knowledge of criminal matters before signing confirmatory affidavit.",
            "legal_significance": "knowledge_before_perjury_confirmatory_affidavit",
            "evidence": ["email_received_thanks_daniel_2025_08_29"],
            "pattern": "consolidation_phase",
            "critical": True
        },
        {
            "event_id": "EVENT_059",
            "date": "2025-08-11",
            "title": "Settlement Agreement Signed",
            "category": "legal_manipulation",
            "event_type": "strategic_settlement_timing",
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_004", "PERSON_005"],
            "entities_involved": ["ORG_001"],
            "description": "Settlement agreement signed 2 days before interdict filing, demonstrating strategic coordination and timing to create leverage",
            "legal_significance": "strategic_litigation_tactic_not_genuine_business_protection",
            "evidence": ["settlement_agreement_2025_08_11"],
            "pattern": "cover_up_phase",
            "critical": True
        },
        {
            "event_id": "EVENT_060",
            "date": "2025-08-13",
            "title": "Peter Files Founding Affidavit with Material Non-Disclosures",
            "category": "perjury",
            "event_type": "false_court_filing",
            "perpetrators": ["PERSON_001"],
            "victims": ["PERSON_004", "PERSON_005"],
            "entities_involved": ["ORG_001"],
            "description": "Peter files founding affidavit containing material non-disclosures and perjury regarding email control, filed 2 days after settlement agreement",
            "legal_significance": "perjury_material_non_disclosure_manufactured_crisis",
            "evidence": ["founding_affidavit_2025_08_13"],
            "pattern": "cover_up_phase",
            "critical": True
        },
        {
            "event_id": "EVENT_061",
            "date": "2025-08-29",
            "title": "ENS Africa Acknowledges Criminal Matters Then Suppresses",
            "category": "legal_misconduct",
            "event_type": "evidence_suppression",
            "perpetrators": ["PERSON_007"],
            "victims": ["PERSON_004", "PERSON_005"],
            "entities_involved": [],
            "description": "ENS Africa acknowledges receipt of criminal matters information with 'Received, thanks Daniel' email, then suppresses this information from Court",
            "legal_significance": "professional_misconduct_evidence_suppression",
            "evidence": ["email_received_thanks_daniel_2025_08_29"],
            "pattern": "cover_up_phase",
            "critical": True
        }
    ]
    
    return new_events

def extract_new_entity_details():
    """Extract additional entity details from ad-res-j7"""
    
    entity_updates = {
        "PERSON_007": {
            "additional_events": ["EVENT_H018", "EVENT_058", "EVENT_061"],
            "additional_notes": "Sent trial balance email Aug 13, 2020 to Bernadine Wright; learned of criminal matters June 10, 2025; ENS Africa suppressed criminal information from Court Aug 29, 2025",
            "email_correspondent_bernadine_wright": True
        },
        "PERSON_010": {
            "additional_events": ["EVENT_H018"],
            "role_clarification": "Recipient of trial balance email from Bantjies, witness to his financial system control"
        },
        "PERSON_011": {
            "additional_events": ["EVENT_054"],
            "role_clarification": "Delivered letter about Kayla estate finalization January 2025"
        }
    }
    
    return entity_updates

def extract_new_relations():
    """Extract new relations discovered from ad-res-j7"""
    
    new_relations = [
        {
            "relation_id": "REL_PROF_001",
            "relation_type": "professional_correspondence",
            "source_entity": "PERSON_007",
            "target_entity": "PERSON_010",
            "correspondence_type": "financial_statement_finalization",
            "evidence": ["trial_balance_email_2020_08_13"],
            "legal_status": "demonstrates_control",
            "additional_notes": "Bantjies sent trial balance to Bernadine Wright for financial statement finalization meeting"
        },
        {
            "relation_id": "REL_KNOWLEDGE_001",
            "relation_type": "knowledge_acquisition",
            "source_entity": "PERSON_007",
            "target_entity": "criminal_matters",
            "knowledge_type": "fraud_and_murder_disclosure",
            "acquisition_date": "2025-06-10",
            "evidence": ["email_received_thanks_daniel_2025_08_29"],
            "legal_status": "knowledge_before_perjury",
            "critical_significance": "Bantjies knew of criminal matters before signing confirmatory affidavit"
        },
        {
            "relation_id": "REL_LEGAL_001",
            "relation_type": "strategic_coordination",
            "source_entity": "PERSON_001",
            "target_entity": "settlement_and_interdict",
            "coordination_type": "timing_manipulation",
            "timing_gap_days": 2,
            "evidence": ["settlement_agreement_2025_08_11", "founding_affidavit_2025_08_13"],
            "legal_status": "strategic_litigation_tactic",
            "critical_significance": "Settlement signed 2 days before interdict filing demonstrates premeditation"
        }
    ]
    
    return new_relations

def main():
    # Extract all new data
    new_events = extract_timeline_events()
    entity_updates = extract_new_entity_details()
    new_relations = extract_new_relations()
    
    # Create comprehensive extraction report
    extraction_report = {
        "extraction_date": datetime.now().isoformat(),
        "source_repository": "ad-res-j7",
        "new_events_count": len(new_events),
        "entity_updates_count": len(entity_updates),
        "new_relations_count": len(new_relations),
        "new_events": new_events,
        "entity_updates": entity_updates,
        "new_relations": new_relations,
        "critical_findings": [
            "EVENT_058: Bantjies learned of criminal matters June 10, 2025 before confirmatory affidavit",
            "EVENT_059: Settlement agreement signed 2 days before interdict (strategic timing)",
            "EVENT_060: Peter's founding affidavit contains material non-disclosures and perjury",
            "EVENT_061: ENS Africa acknowledged then suppressed criminal matters from Court"
        ]
    }
    
    # Save extraction report
    with open('/home/ubuntu/revstream1/ad_res_j7_extraction_report.json', 'w') as f:
        json.dump(extraction_report, f, indent=2)
    
    print("Extraction complete!")
    print(f"\nNew Events: {len(new_events)}")
    print(f"Entity Updates: {len(entity_updates)}")
    print(f"New Relations: {len(new_relations)}")
    print(f"\nCritical Findings:")
    for finding in extraction_report['critical_findings']:
        print(f"  - {finding}")

if __name__ == '__main__':
    main()
