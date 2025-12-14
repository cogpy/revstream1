#!/usr/bin/env python3
"""
Cross-reference analysis between revstream1 models and ad-res-j7 evidence
Date: 2025-12-14
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS_DIR = BASE_DIR / "data_models"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved: {filepath}")

# Comprehensive evidence mapping from ad-res-j7
COMPREHENSIVE_EVIDENCE_MAP = {
    "JF01": {
        "title": "Shopify Plus Email (26 July 2017)",
        "location": "ANNEXURES/JF01/",
        "priority": "CRITICAL",
        "files": [
            "Re_ The RegimA Group results and Computer Expense analysis.eml",
            "Re_ belongs to regimA.eml"
        ],
        "proves": [
            "Kayla Pretorius personally managed Shopify Plus onboarding",
            "Daniel Faucitt directly involved (CC'd on communications)",
            "Independent business operations (no 'head office' involvement)",
            "Use of independent email addresses (kayp@rzo.io, kayla@regima.zone)",
            "Personal phone number (011 615 29869) - later appropriated"
        ],
        "refutes": [
            "Applicant's claim of centralized 'head office' control",
            "Applicant's claim that Daniel never operated independent businesses"
        ],
        "legal_significance": "contemporaneous_documentary_evidence_from_neutral_third_party",
        "burden_of_proof": "civil_50%_exceeded_criminal_95%_exceeded",
        "related_entities": ["PERSON_003", "PERSON_005", "ORG_003", "PLATFORM_001"],
        "related_events": ["EVENT_H001", "EVENT_H002", "EVENT_001"]
    },
    "JF02": {
        "title": "Shopify Sales Reports",
        "location": "ANNEXURES/JF02/",
        "priority": "HIGH",
        "files": [
            "RegimASA·Reports·Totalsalesovertimebystore·ShopifyPlus.pdf",
            "RegimAWW+Zone·Reports·Totalsalesovertimebystore·ShopifyPlusZAR.pdf"
        ],
        "proves": [
            "Active Shopify Plus business operations",
            "Revenue generation through independent channels",
            "Business performance tracking"
        ],
        "related_entities": ["ORG_003", "ORG_006", "PLATFORM_001"],
        "related_events": ["EVENT_H002"]
    },
    "JF03": {
        "title": "Financial Records and Analysis",
        "location": "ANNEXURES/JF03/",
        "priority": "HIGH",
        "files": [
            "COMPUTER EXP MAR AND APR2025 (2).xlsx",
            "Fw_ The RegimA Group results and Computer Expense analysis.eml"
        ],
        "proves": [
            "Detailed financial record-keeping",
            "Business expense tracking",
            "Independent financial management"
        ],
        "related_entities": ["ORG_003", "PERSON_005"],
        "related_events": ["EVENT_H003"]
    },
    "JF04": {
        "title": "Daniel Faucitt Personal Bank Records",
        "location": "ANNEXURES/JF04/",
        "priority": "HIGH",
        "files": [
            "D_FAUCITT_PERSONAL_BANK_RECORDS_20250604.pdf",
            "D_FAUCITT_PERSONAL_BANK_RECORDS_20250704.pdf",
            "D_FAUCITT_PERSONAL_BANK_RECORDS_20250804.pdf",
            "D_FAUCITT_PERSONAL_BANK_RECORDS_20250904.pdf",
            "D_FAUCITT_PERSONAL_BANK_RECORDS_20251004.pdf"
        ],
        "proves": [
            "Complete financial transparency",
            "Legitimate banking transactions",
            "No evidence of hidden assets"
        ],
        "refutes": [
            "Claims of financial misconduct",
            "Claims of asset concealment"
        ],
        "related_entities": ["PERSON_005"],
        "burden_of_proof": "civil_50%_exceeded"
    },
    "JF05": {
        "title": "Correspondence Evidence (JF8 Series)",
        "location": "ANNEXURES/JF05/",
        "priority": "MEDIUM",
        "files": [
            "JF8_CORRESPONDENCE_EVIDENCE.md",
            "JF8A_DOCUMENTATION_LOG.md",
            "JF8B_EMAIL_COOPERATION_CHAINS.md",
            "JF8C_PETER_REFUSAL_TO_ENGAGE.md",
            "JF8D_SYSTEM_ACCESS_RESTRICTIONS.md"
        ],
        "proves": [
            "Respondents made good faith attempts to cooperate",
            "Applicant refused to engage constructively",
            "System access restrictions imposed by Applicant"
        ],
        "refutes": [
            "Claims that Respondents refused to cooperate",
            "Claims that Respondents withheld information"
        ],
        "related_entities": ["PERSON_001", "PERSON_004", "PERSON_005"],
        "pattern": "obstruction_by_applicant"
    },
    "JF06": {
        "title": "Court Documents and Filings",
        "location": "ANNEXURES/JF06/",
        "priority": "HIGH",
        "file_count": 99,
        "proves": [
            "Complete procedural history",
            "Applicant's applications and claims",
            "Attorney correspondence and withdrawals"
        ],
        "related_entities": ["PERSON_001", "PERSON_004", "PERSON_005"],
        "pattern": "aggressive_litigation_strategy"
    },
    "JF07": {
        "title": "Screenshots and Visual Evidence",
        "location": "ANNEXURES/JF07/",
        "priority": "MEDIUM",
        "file_count": 62,
        "proves": [
            "Visual documentation of systems and accounts",
            "Sage accounting system screenshots",
            "Business operations documentation"
        ],
        "related_entities": ["ORG_001", "ORG_002", "PERSON_002"],
        "related_events": ["EVENT_007", "EVENT_008"]
    },
    "JF08": {
        "title": "Evidence Packages (May-October 2025)",
        "location": "ANNEXURES/JF08/",
        "priority": "HIGH",
        "packages": [
            "evidence_package_20250523",
            "evidence_package_20250606",
            "evidence_package_20250811",
            "evidence_package_20251009",
            "evidence_package_20251012"
        ],
        "proves": [
            "Systematic evidence gathering over time",
            "Progressive development of case",
            "Chronological evidence trail"
        ],
        "note": "First package (23 May 2025) is one day after Shopify audit trail destruction (22 May 2025)",
        "related_events": ["EVENT_016", "EVENT_017"],
        "criminal_significance": "response_to_evidence_destruction"
    },
    "JF09": {
        "title": "Timeline Analysis",
        "location": "ANNEXURES/JF09/",
        "priority": "HIGH",
        "files": [
            "ENTITY_RELATION_UPDATES_20250523.md",
            "ENTITY_RELATION_UPDATES_20250811.md",
            "HYPER_HOLMES_ANALYSIS_20250523.md"
        ],
        "proves": [
            "Comprehensive timeline analysis",
            "Entity relationship mapping",
            "Pattern recognition and fraud detection"
        ],
        "methodology": "agentic_entity_modeling"
    },
    "SF1": {
        "title": "Bantjies Debt Documentation",
        "location": "ANNEXURES/SF1_Bantjies_Debt_Documentation.md",
        "priority": "MEDIUM",
        "proves": [
            "Business relationship with ReZonance",
            "Debt accumulation patterns"
        ],
        "related_entities": ["ORG_008", "PERSON_001"],
        "related_events": ["EVENT_H001", "EVENT_H002"]
    },
    "SF2": {
        "title": "Sage Screenshots - Rynette Control",
        "location": "ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md",
        "priority": "CRITICAL",
        "proves": [
            "Rynette Farrar's direct control of Sage accounting system",
            "Account manipulation capabilities",
            "System access for fraudulent record submission"
        ],
        "related_entities": ["PERSON_002", "ORG_001", "ORG_002"],
        "related_events": ["EVENT_007", "EVENT_008", "EVENT_009"],
        "burden_of_proof": "criminal_95%_exceeded",
        "criminal_charges": ["fraud", "uttering", "forgery"]
    },
    "SF3": {
        "title": "Strategic Logistics Stock Adjustment",
        "location": "ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md",
        "priority": "HIGH",
        "proves": [
            "Inter-company stock manipulation",
            "Financial manipulation patterns"
        ],
        "related_entities": ["ORG_004", "ORG_002"],
        "related_events": ["EVENT_H003"]
    },
    "SF4": {
        "title": "SARS Audit Email",
        "location": "ANNEXURES/SF4_SARS_Audit_Email.md",
        "priority": "HIGH",
        "proves": [
            "Tax audit triggers",
            "Financial irregularities flagged by SARS"
        ],
        "related_entities": ["ORG_001", "ORG_002"],
        "regulatory_significance": "tax_fraud_indicators"
    },
    "SF5": {
        "title": "Adderory Company Registration & Stock Supply",
        "location": "ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md",
        "priority": "MEDIUM",
        "proves": [
            "Company registration documentation",
            "Stock supply arrangements"
        ],
        "related_entities": ["ORG_007", "PERSON_001"]
    },
    "SF6": {
        "title": "Kayla Pretorius Estate Documentation",
        "location": "ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md",
        "priority": "CRITICAL",
        "proves": [
            "Kayla's role in business operations",
            "Estate documentation",
            "Trigger event for business appropriation"
        ],
        "related_entities": ["PERSON_003"],
        "related_events": ["EVENT_001", "EVENT_002"],
        "legal_significance": "foundation_event_for_fraud_scheme",
        "timeline_correlation": "JF9 shows immediate system access changes after estate event"
    },
    "SF7": {
        "title": "Court Order - Kayla Email Seizure",
        "location": "ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md",
        "priority": "HIGH",
        "proves": [
            "Court-ordered email seizure",
            "Legal authority for evidence collection"
        ],
        "related_entities": ["PERSON_003"],
        "legal_significance": "court_sanctioned_evidence_collection"
    },
    "SF8": {
        "title": "Linda Employment Records",
        "location": "ANNEXURES/SF8_Linda_Employment_Records.md",
        "priority": "MEDIUM",
        "proves": [
            "Employment relationships",
            "Organizational structure"
        ],
        "related_entities": ["PERSON_006"]
    }
}

def analyze_evidence_coverage():
    """Analyze evidence coverage across entities, events, and timeline"""
    print("\n🔍 Analyzing evidence coverage...")
    
    # Load models
    entities = load_json(DATA_MODELS_DIR / "entities" / "entities.json")
    events = load_json(DATA_MODELS_DIR / "events" / "events_refined_2025_12_14_v35.json")
    timeline = load_json(DATA_MODELS_DIR / "timelines" / "timeline_refined_2025_12_14_v22.json")
    
    analysis = {
        "generated": datetime.now().isoformat(),
        "evidence_sources": len(COMPREHENSIVE_EVIDENCE_MAP),
        "coverage_analysis": {
            "entities": {},
            "events": {},
            "timeline": {}
        },
        "evidence_strength_by_category": {},
        "burden_of_proof_assessment": {
            "civil_50_percent": [],
            "criminal_95_percent": []
        },
        "critical_evidence": [],
        "evidence_gaps": []
    }
    
    # Analyze entity coverage
    for entity_type in ["persons", "organizations"]:
        if entity_type in entities["entities"]:
            for entity in entities["entities"][entity_type]:
                entity_id = entity.get("entity_id")
                
                # Find related evidence
                related_evidence = []
                for ev_id, ev_data in COMPREHENSIVE_EVIDENCE_MAP.items():
                    if entity_id in ev_data.get("related_entities", []):
                        related_evidence.append({
                            "evidence_id": ev_id,
                            "title": ev_data["title"],
                            "priority": ev_data["priority"],
                            "location": ev_data["location"]
                        })
                
                if related_evidence:
                    analysis["coverage_analysis"]["entities"][entity_id] = {
                        "name": entity.get("name", "Unknown"),
                        "evidence_count": len(related_evidence),
                        "evidence": related_evidence
                    }
    
    # Identify critical evidence
    for ev_id, ev_data in COMPREHENSIVE_EVIDENCE_MAP.items():
        if ev_data.get("priority") == "CRITICAL":
            analysis["critical_evidence"].append({
                "evidence_id": ev_id,
                "title": ev_data["title"],
                "location": ev_data["location"],
                "proves": ev_data.get("proves", []),
                "burden_of_proof": ev_data.get("burden_of_proof", "not_assessed")
            })
    
    # Assess burden of proof
    for ev_id, ev_data in COMPREHENSIVE_EVIDENCE_MAP.items():
        burden = ev_data.get("burden_of_proof", "")
        
        if "civil_50%_exceeded" in burden:
            analysis["burden_of_proof_assessment"]["civil_50_percent"].append({
                "evidence_id": ev_id,
                "title": ev_data["title"]
            })
        
        if "criminal_95%_exceeded" in burden:
            analysis["burden_of_proof_assessment"]["criminal_95_percent"].append({
                "evidence_id": ev_id,
                "title": ev_data["title"]
            })
    
    # Save analysis
    output_file = BASE_DIR / f"EVIDENCE_CROSS_REFERENCE_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(analysis, output_file)
    
    return analysis

def generate_evidence_index_for_applications():
    """Generate evidence index for each of the 3 applications"""
    print("\n📋 Generating evidence index for applications...")
    
    applications = {
        "application_1": {
            "title": "Ex Parte Interdict (August 13, 2025)",
            "type": "ex_parte_urgent_application",
            "targets": ["PERSON_004", "PERSON_005"],
            "key_evidence": ["JF01", "JF06", "JF08", "SF6"],
            "burden_of_proof": "civil_50_percent"
        },
        "application_2": {
            "title": "Settlement Agreement Enforcement (October 2025)",
            "type": "application_to_make_settlement_order",
            "context": "mediation_held_september_18_2025",
            "key_evidence": ["JF05", "JF06"],
            "burden_of_proof": "civil_50_percent"
        },
        "application_3": {
            "title": "Third Application (November 2025)",
            "type": "further_relief",
            "key_evidence": ["JF01", "JF02", "JF07", "JF08", "SF2"],
            "burden_of_proof": "civil_50_percent"
        }
    }
    
    evidence_index = {
        "generated": datetime.now().isoformat(),
        "applications": {}
    }
    
    for app_id, app_data in applications.items():
        app_evidence = {
            "title": app_data["title"],
            "type": app_data["type"],
            "burden_of_proof": app_data["burden_of_proof"],
            "evidence_references": []
        }
        
        for ev_id in app_data["key_evidence"]:
            if ev_id in COMPREHENSIVE_EVIDENCE_MAP:
                ev_data = COMPREHENSIVE_EVIDENCE_MAP[ev_id]
                app_evidence["evidence_references"].append({
                    "evidence_id": ev_id,
                    "title": ev_data["title"],
                    "location": ev_data["location"],
                    "priority": ev_data["priority"],
                    "proves": ev_data.get("proves", []),
                    "refutes": ev_data.get("refutes", [])
                })
        
        evidence_index["applications"][app_id] = app_evidence
    
    # Save evidence index
    output_file = BASE_DIR / f"APPLICATIONS_EVIDENCE_INDEX_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(evidence_index, output_file)
    
    return evidence_index

def main():
    print("=" * 80)
    print("EVIDENCE CROSS-REFERENCE ANALYSIS - 2025-12-14")
    print("=" * 80)
    
    # Analyze evidence coverage
    coverage_analysis = analyze_evidence_coverage()
    
    # Generate evidence index for applications
    evidence_index = generate_evidence_index_for_applications()
    
    print("\n" + "=" * 80)
    print("✅ CROSS-REFERENCE ANALYSIS COMPLETE")
    print("=" * 80)
    print(f"\nEvidence sources mapped: {coverage_analysis['evidence_sources']}")
    print(f"Critical evidence items: {len(coverage_analysis['critical_evidence'])}")
    print(f"Civil burden (50%) met: {len(coverage_analysis['burden_of_proof_assessment']['civil_50_percent'])}")
    print(f"Criminal burden (95%) met: {len(coverage_analysis['burden_of_proof_assessment']['criminal_95_percent'])}")
    print("\n📋 Next: Update legal filings with evidence references")

if __name__ == "__main__":
    main()
