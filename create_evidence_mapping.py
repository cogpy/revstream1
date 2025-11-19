#!/usr/bin/env python3
"""
Create comprehensive evidence mapping between ad-res-j7 repository and revstream1 entities/events
"""
import json
from pathlib import Path

# Evidence mapping based on ad-res-j7 structure and case facts
ENTITY_EVIDENCE_MAP = {
    "PERSON_001": {  # Peter Andrew Faucitt
        "evidence_files": [
            "ANNEXURES/JF01/trust_documents/",
            "ANNEXURES/JF03/popia_violations/",
            "ANNEXURES/JF05/correspondence/peter_emails/",
            "case_2025_137857/affidavits/peter_affidavit/",
            "evidence/trust_violations/trustee_misconduct/"
        ],
        "ad_res_j7_references": [
            "Trust deed manipulation evidence",
            "POPIA violation documentation",
            "Email correspondence showing control",
            "Affidavit with material omissions"
        ]
    },
    "PERSON_002": {  # Rynette Farrar
        "evidence_files": [
            "ANNEXURES/JF05/correspondence/rynette_emails/",
            "evidence/payment_redirection/bank_account_changes/",
            "evidence/financial_manipulation/accounts_system_control/",
            "case_2025_137857/financial_analysis/rynette_control/"
        ],
        "ad_res_j7_references": [
            "Payment redirection scheme documentation",
            "Bank account change letters",
            "Accounts system control evidence",
            "Email impersonation patterns"
        ]
    },
    "PERSON_003": {  # Adderory (Rynette's Son)
        "evidence_files": [
            "evidence/domain_registration/regimaskin_co_za/",
            "evidence/cipc/shell_companies/",
            "evidence/stock_fraud/R5_4M_scheme/",
            "ANNEXURES/cipc/company_registrations/"
        ],
        "ad_res_j7_references": [
            "Domain registration for identity fraud (regimaskin.co.za)",
            "CIPC registration of shell companies",
            "Stock supply fraud facilitation",
            "Customer hijacking infrastructure"
        ]
    },
    "PERSON_007": {  # Danie Bantjies
        "evidence_files": [
            "evidence/accounting/trial_balances/",
            "evidence/trust_violations/unknown_trustee/",
            "evidence/conflict_of_interest/R18_685M_debt/",
            "ANNEXURES/accounting/bantjies_emails/",
            "evidence/commissioner_of_oaths/affidavit_certification/"
        ],
        "ad_res_j7_references": [
            "Trial balance email Aug 13, 2020 to Bernadine Wright",
            "Audit request dismissal June 10, 2025",
            "R18.685M debt to trust documentation",
            "Commissioner of Oaths misconduct",
            "Stock adjustment fraud concealment"
        ]
    },
    "PERSON_008": {  # Kayla (deceased)
        "evidence_files": [
            "evidence/estate_fraud/kayla_estate/",
            "evidence/court_orders/email_account_seizure/",
            "evidence/debt/R1_035M_unpaid/"
        ],
        "ad_res_j7_references": [
            "Estate debt documentation R1,035,000",
            "Court order for email account seizure",
            "Law enforcement investigation interference"
        ]
    },
    "PERSON_009": {  # Gee
        "evidence_files": [
            "ANNEXURES/JF05/correspondence/domain_switch_emails/",
            "evidence/customer_diversion/email_instructions/"
        ],
        "ad_res_j7_references": [
            "Email to Jax explaining domain switch instruction",
            "Customer diversion scheme witness evidence"
        ]
    },
    "PERSON_010": {  # Bernadine Wright
        "evidence_files": [
            "evidence/accounting/trial_balance_recipients/",
            "ANNEXURES/accounting/bernadine_correspondence/"
        ],
        "ad_res_j7_references": [
            "Recipient of trial balance email Aug 13, 2020",
            "Financial statement finalization meeting witness"
        ]
    },
    "PERSON_011": {  # ENS Africa Attorney
        "evidence_files": [
            "ANNEXURES/JF06/ens_withdrawal/",
            "evidence/legal_misconduct/criminal_suppression/"
        ],
        "ad_res_j7_references": [
            "Withdrawal as attorneys Sept 23, 2025",
            "Suppression of criminal information from Court Aug 29, 2025"
        ]
    },
    "PERSON_012": {  # Jax
        "evidence_files": [
            "jax-response/",
            "ANNEXURES/JF05/correspondence/jax_emails/"
        ],
        "ad_res_j7_references": [
            "Recipient of domain switch instruction",
            "Witness to customer diversion scheme"
        ]
    }
}

# Events that need perpetrator assignment
EVENTS_NEEDING_PERPETRATORS = {
    "EVT-063": ["PERSON_001", "PERSON_007"],  # Likely trust/accounting related
    "EVT-064": ["PERSON_001", "PERSON_002"],  # Likely financial manipulation
    "EVT-065": ["PERSON_002"],  # Likely payment redirection
    "EVT-066": ["PERSON_001"],  # Likely trust violation
    "EVT-067": ["PERSON_007"],  # Likely accounting fraud
    "EVT-068": ["PERSON_001", "PERSON_002", "PERSON_003"],  # Likely conspiracy
    "EVT-069": ["PERSON_001"]  # Likely trust/control
}

def save_evidence_mapping():
    """Save the evidence mapping to JSON file"""
    mapping = {
        "metadata": {
            "version": "1.0",
            "created_date": "2025-11-19",
            "description": "Evidence mapping between ad-res-j7 repository and revstream1 entities",
            "ad_res_j7_total_files": 2866,
            "ad_res_j7_total_size": "226.78 MB"
        },
        "entity_evidence_mapping": ENTITY_EVIDENCE_MAP,
        "events_perpetrator_assignments": EVENTS_NEEDING_PERPETRATORS
    }
    
    output_file = Path('/home/ubuntu/revstream1/EVIDENCE_MAPPING_2025_11_19.json')
    with open(output_file, 'w') as f:
        json.dump(mapping, f, indent=2)
    
    print(f"Evidence mapping saved to: {output_file}")
    print(f"Total entities mapped: {len(ENTITY_EVIDENCE_MAP)}")
    print(f"Total events needing perpetrators: {len(EVENTS_NEEDING_PERPETRATORS)}")

if __name__ == '__main__':
    save_evidence_mapping()
