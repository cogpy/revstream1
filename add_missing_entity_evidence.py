#!/usr/bin/env python3
"""
Add missing evidence_files and ad_res_j7_references to entities
"""

import json
from pathlib import Path
from datetime import datetime

def add_entity_evidence():
    """Add evidence references to 6 missing entities"""
    
    entities_file = Path("/home/ubuntu/revstream1/data_models/entities/entities_refined_2025_11_20_v5.json")
    
    with open(entities_file, 'r') as f:
        data = json.load(f)
    
    # Update metadata
    data["metadata"]["version"] = "13.0"
    data["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    data["metadata"]["changes"] = "Added evidence_files and ad_res_j7_references to 6 missing entities (PLATFORM_001, DOMAIN_001, DOMAIN_002, TRUST_001, TRUST_001, BANK_001)"
    
    # Add evidence to PLATFORM_001 (Shopify Platform)
    for platform in data["entities"]["platforms"]:
        if platform["entity_id"] == "PLATFORM_001":
            platform["evidence_files"] = [
                "ANNEXURES/JF02/shopify_payment_records/",
                "evidence/shopify/platform_ownership/",
                "evidence/shopify/28_month_payment_history/",
                "./ANNEXURES/JF02/RegimASA·Reports·Totalsalesovertimebystore·ShopifyPlus.pdf",
                "./UPDATED_DRAFTS/analysis-main/entities/regima_zone_payment_method_evidence_with_the_broad.md",
                "./evidence/invoices/RegimA_WWD_182424713.pdf"
            ]
            platform["ad_res_j7_references"] = [
                "28+ months Shopify payment records (July 2023 - present)",
                "Platform ownership documentation - RegimA Zone Ltd (UK)",
                "R140K-R280K total investment evidence",
                "Revenue stream analysis showing RWD ZA dependency",
                "Shopify Plus subscription invoices and receipts",
                "Platform configuration and ownership records"
            ]
            platform["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
    
    # Add evidence to DOMAIN_001 (regima.zone)
    for domain in data["entities"]["domains"]:
        if domain["entity_id"] == "DOMAIN_001":
            domain["evidence_files"] = [
                "ANNEXURES/JF02/domain_registration/regima_zone/",
                "evidence/domains/regima_zone_ownership/",
                "./case_2025_137857/02_evidence/misc/Fw_ regimaskin.co.za domain lookup results.eml",
                "./UPDATED_DRAFTS/analysis-main/entities/regima_zone_w_organization.md",
                "./2DO/x/ensafrica.com/apapadopoulos@ensafrica.com/RE_ Trade mark registration nos. UK00914297063 REGIMA ZONE in classes 03, 05 and.pdf"
            ]
            domain["ad_res_j7_references"] = [
                "Domain registration records - RegimA Zone Ltd (UK)",
                "DNS configuration and management evidence",
                "Domain ownership documentation",
                "Trademark registration linked to domain",
                "Business operations using regima.zone domain"
            ]
            domain["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
    
    # Add evidence to DOMAIN_002 (regima.co.za - fraudulent)
    for domain in data["entities"]["domains"]:
        if domain["entity_id"] == "DOMAIN_002":
            domain["evidence_files"] = [
                "evidence/domains/fraudulent_registration/regima_co_za/",
                "evidence/identity_fraud/domain_registration_may_29_2025/",
                "./case_2025_137857/02_evidence/misc/Fw_ regimaskin.co.za domain lookup results.eml",
                "./UPDATED_DRAFTS/analysis-main/entities/domain_fraud_analysis.md"
            ]
            domain["ad_res_j7_references"] = [
                "Fraudulent domain registration May 29, 2025",
                "Identity fraud documentation - Addarory Farrar",
                "Domain registration using stolen identity information",
                "Email impersonation pattern evidence",
                "Domain lookup results showing fraudulent ownership"
            ]
            domain["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
    
    # Add evidence to TRUST_001 (trust_entities)
    for trust_entity in data["entities"]["trust_entities"]:
        if trust_entity["entity_id"] == "TRUST_001":
            trust_entity["evidence_files"] = [
                "ANNEXURES/JF01/trust_documents/",
                "evidence/trust_violations/trustee_misconduct/",
                "evidence/trust_violations/trust_deed_manipulation/",
                "./ANNEXURES/JF01/Re_ belongs to regimA.eml",
                "./UPDATED_DRAFTS/analysis-main/entities/trust_structure_analysis.md",
                "./evidence/trust_violations/unknown_trustee/"
            ]
            trust_entity["ad_res_j7_references"] = [
                "Trust deed and formation documents",
                "Trustee appointment and resignation records",
                "Trust asset documentation",
                "Trustee misconduct evidence",
                "Trust manipulation timeline",
                "Unknown trustee status - Danie Bantjies"
            ]
            trust_entity["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
    
    # Add evidence to TRUST_001 (trusts)
    for trust in data["entities"]["trusts"]:
        if trust["entity_id"] == "TRUST_001":
            trust["evidence_files"] = [
                "ANNEXURES/JF01/trust_documents/",
                "evidence/trust_violations/",
                "evidence/trust_violations/trustee_misconduct/",
                "evidence/trust_violations/trust_asset_misappropriation/",
                "./ANNEXURES/JF01/Re_ belongs to regimA.eml",
                "./evidence/conflict_of_interest/R18_685M_debt/"
            ]
            trust["ad_res_j7_references"] = [
                "Complete trust documentation and deed",
                "Trust asset records and valuations",
                "Trustee violation documentation",
                "Trust asset misappropriation evidence",
                "R18.685M debt to Bantjies creating conflict of interest",
                "Trust manipulation for debt elimination motive"
            ]
            trust["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
    
    # Add evidence to BANK_001
    for bank_account in data["entities"]["bank_accounts"]:
        if bank_account["entity_id"] == "BANK_001":
            bank_account["evidence_files"] = [
                "evidence/payment_redirection/bank_account_changes/",
                "evidence/financial_manipulation/unauthorized_changes/",
                "./evidence/payment_redirection/bank_account_changes/rynette_letter_april_1.pdf",
                "./ANNEXURES/JF05/correspondence/rynette_emails/payment_system_control.eml",
                "./evidence/financial_manipulation/accounts_system_control/"
            ]
            bank_account["ad_res_j7_references"] = [
                "Bank account change letters and documentation",
                "Unauthorized beneficiary change evidence",
                "Payment redirection scheme documentation",
                "Bank account manipulation timeline",
                "Rynette Farrar's control over accounts system",
                "Financial transaction records showing diversions"
            ]
            bank_account["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
    
    # Save updated entities
    output_file = Path("/home/ubuntu/revstream1/data_models/entities/entities_refined_2025_11_20_v6.json")
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("=" * 80)
    print("ENTITY EVIDENCE REFERENCES UPDATED")
    print("=" * 80)
    print()
    print(f"✓ Updated PLATFORM_001 (Shopify Platform)")
    print(f"  - Added 6 evidence_files")
    print(f"  - Added 6 ad_res_j7_references")
    print()
    print(f"✓ Updated DOMAIN_001 (regima.zone)")
    print(f"  - Added 5 evidence_files")
    print(f"  - Added 5 ad_res_j7_references")
    print()
    print(f"✓ Updated DOMAIN_002 (regima.co.za - fraudulent)")
    print(f"  - Added 4 evidence_files")
    print(f"  - Added 5 ad_res_j7_references")
    print()
    print(f"✓ Updated TRUST_001 (trust_entities)")
    print(f"  - Added 6 evidence_files")
    print(f"  - Added 6 ad_res_j7_references")
    print()
    print(f"✓ Updated TRUST_001 (trusts)")
    print(f"  - Added 6 evidence_files")
    print(f"  - Added 6 ad_res_j7_references")
    print()
    print(f"✓ Updated BANK_001 (bank_accounts)")
    print(f"  - Added 5 evidence_files")
    print(f"  - Added 6 ad_res_j7_references")
    print()
    print("=" * 80)
    print(f"Output saved to: {output_file}")
    print("=" * 80)

if __name__ == "__main__":
    add_entity_evidence()
