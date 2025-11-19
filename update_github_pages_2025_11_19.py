#!/usr/bin/env python3
"""
Update GitHub Pages with enhanced evidence organization and clear references
for all 3 applications
"""
import json
from pathlib import Path

def load_latest_models():
    """Load the latest refined models"""
    base_path = Path('/home/ubuntu/revstream1/data_models')
    
    with open(base_path / 'entities' / 'entities_refined_2025_11_19_v3.json', 'r') as f:
        entities = json.load(f)
    
    with open(base_path / 'events' / 'events_refined_2025_11_19_v3.json', 'r') as f:
        events = json.load(f)
    
    with open(base_path / 'timelines' / 'timeline_refined_2025_11_19_v3.json', 'r') as f:
        timeline = json.load(f)
    
    with open(base_path / 'relations' / 'relations_refined_2025_11_19_v3.json', 'r') as f:
        relations = json.load(f)
    
    return entities, events, timeline, relations

def create_enhanced_evidence_index():
    """Create enhanced evidence index with application-specific organization"""
    
    content = """---
layout: default
title: Enhanced Evidence Index
---

**Navigation:** [Home](index.md) → Enhanced Evidence Index

---

# Enhanced Evidence Index

## Overview

This enhanced evidence index provides comprehensive organization of all evidence across the **three sequential interdict applications** in Case 2025-137857. Each piece of evidence is mapped to specific entities, events, and applications with direct references to the extended evidence repository.

**Extended Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)  
**Total Files:** 2,866 files (226.78 MB)  
**Last Updated:** 2025-11-19

---

## Evidence Organization by Application

### Application 1: Ex Parte Interdict (August 13, 2025)

**Primary Focus:** POPIA violations, trustee misconduct, revenue theft

#### Key Evidence Categories

##### 1. Trust Violations & Trustee Misconduct

**Entity:** PERSON_001 (Peter Andrew Faucitt)

**Evidence Files:**
- `ad-res-j7/ANNEXURES/JF01/trust_documents/`
- `ad-res-j7/evidence/trust_violations/trustee_misconduct/`
- `ad-res-j7/case_2025_137857/affidavits/peter_affidavit/`

**Related Events:**
- EVENT_001: Trust structure establishment (March 15, 2025)
- EVENT_002: Beneficiary manipulation (March 20, 2025)
- EVENT_006: Beneficiary exclusion (May 2, 2025)

**Key Findings:**
- Trust deed manipulation evidence
- Unauthorized beneficiary changes
- Trustee misconduct documentation

##### 2. POPIA Violations & Data Breaches

**Entity:** PERSON_001 (Peter Andrew Faucitt)

**Evidence Files:**
- `ad-res-j7/ANNEXURES/JF03/popia_violations/`
- `ad-res-j7/evidence/popia/warehouse_violations/`

**Related Events:**
- EVENT_016: POPIA violations (July 8, 2025)
- EVENT_017: Warehouse data breach (July 8, 2025)

**Key Findings:**
- Official POPIA violation notice sent to Peter (July 8, 2025)
- Warehouse data security breaches
- Personal information misuse

##### 3. Payment Redirection & Revenue Theft

**Entity:** PERSON_002 (Rynette Farrar)

**Evidence Files:**
- `ad-res-j7/ANNEXURES/JF05/correspondence/rynette_emails/`
- `ad-res-j7/evidence/payment_redirection/bank_account_changes/`
- `ad-res-j7/evidence/financial_manipulation/accounts_system_control/`

**Related Events:**
- EVENT_004: Payment redirection scheme (April 1, 2025)
- EVENT_005: Bank account change letter (April 14, 2025)
- EVENT_013: Fund diversion R2,851,247.35 (June 6, 2025)

**Key Findings:**
- Payment redirection scheme documentation
- Bank account change letters
- Accounts system control evidence
- R7,418,480.55 in revenue theft

---

### Application 2: Settlement Enforcement (October 2025)

**Primary Focus:** Corporate fraud, accounting manipulation, mediation enforcement

#### Key Evidence Categories

##### 1. Accounting Fraud & Financial Manipulation

**Entity:** PERSON_007 (Danie Bantjies)

**Evidence Files:**
- `ad-res-j7/evidence/accounting/trial_balances/`
- `ad-res-j7/evidence/trust_violations/unknown_trustee/`
- `ad-res-j7/evidence/conflict_of_interest/R18_685M_debt/`
- `ad-res-j7/ANNEXURES/accounting/bantjies_emails/`

**Related Events:**
- EVENT_H018: Trial balance email to Bernadine Wright (Aug 13, 2020)
- EVENT_058: Audit request dismissal (June 10, 2025)
- EVENT_061: R18.685M debt discovery

**Key Findings:**
- Triple conflict of interest (trustee/debtor/accountant)
- R18.685M debt to trust creating massive motive
- Stock adjustment fraud concealment (R5.4M)
- Commissioner of Oaths misconduct

##### 2. Shell Company Creation & Identity Fraud

**Entity:** PERSON_003 (Adderory - Rynette's Son)

**Evidence Files:**
- `ad-res-j7/evidence/domain_registration/regimaskin_co_za/`
- `ad-res-j7/evidence/cipc/shell_companies/`
- `ad-res-j7/evidence/stock_fraud/R5_4M_scheme/`
- `ad-res-j7/ANNEXURES/cipc/company_registrations/`

**Related Events:**
- EVENT_H009: Domain registration for identity fraud (May 29, 2025)
- EVENT_010: Shell company registration
- EVENT_024: R5.4M stock fraud scheme

**Key Findings:**
- Domain registration for identity fraud (regimaskin.co.za)
- CIPC registration of fraudulent shell companies
- Stock supply fraud facilitation
- Customer hijacking infrastructure

##### 3. Mediation & Legal Proceedings

**Evidence Files:**
- `ad-res-j7/ANNEXURES/JF06/mediation_notes/`
- `ad-res-j7/ANNEXURES/JF06/ens_withdrawal/`
- `ad-res-j7/evidence/legal_misconduct/criminal_suppression/`

**Related Events:**
- Mediation held September 18, 2025
- Respondents withdraw from agreements September 22, 2025
- ENS Attorneys withdraw September 23, 2025

**Key Findings:**
- Mediation documentation
- Withdrawal from settlement agreements
- Attorney withdrawal after learning of criminal matters
- Suppression of criminal information from Court (Aug 29, 2025)

---

### Application 3: Contact Interdict (November 4, 2025)

**Primary Focus:** Harassment prevention, customer diversion, operational interference

#### Key Evidence Categories

##### 1. Customer Diversion & Domain Hijacking

**Entities:** PERSON_009 (Gee), PERSON_012 (Jax)

**Evidence Files:**
- `ad-res-j7/ANNEXURES/JF05/correspondence/domain_switch_emails/`
- `ad-res-j7/evidence/customer_diversion/email_instructions/`
- `ad-res-j7/jax-response/`

**Related Events:**
- EVENT_027: Domain switch instruction email (June 20, 2025)
- EVENT_H009: Fraudulent domain registration (May 29, 2025)

**Key Findings:**
- Email to Jax explaining domain switch instruction
- Customer diversion scheme witness evidence
- Coordinated customer hijacking operation

##### 2. Estate Fraud & Debt Manipulation

**Entity:** PERSON_008 (Kayla - deceased)

**Evidence Files:**
- `ad-res-j7/evidence/estate_fraud/kayla_estate/`
- `ad-res-j7/evidence/court_orders/email_account_seizure/`
- `ad-res-j7/evidence/debt/R1_035M_unpaid/`

**Related Events:**
- EVENT_023: Court order for email account seizure
- EVENT_054: R1,035,000 debt to Kayla's estate

**Key Findings:**
- Estate debt documentation R1,035,000 (unpaid since Feb 2023)
- Court order for email account seizure
- Law enforcement investigation interference

---

## Cross-Application Evidence

### Critical Evidence Supporting All Applications

#### 1. Shopify Platform Ownership

**Central Revelation:** The Shopify platform has been owned and paid for since **July 2023** by Daniel Faucitt's independent UK entity **RegimA Zone Ltd** (28+ months, R140K-R280K total investment).

**Evidence Location:** `ad-res-j7/ANNEXURES/shopify/platform_ownership/`

**Implication:** RWD ZA has no independent revenue stream - all revenues were generated through infrastructure owned, paid for, and operated by Daniel's UK company.

**Related Events:**
- EVENT_009: Shopify audit trail destruction (May 22, 2025)
- EVENT_011: Platform ownership revelation

**Applications:** 1, 2, 3

#### 2. Bantjies' Conflict of Interest

**Triple Conflict:** Trustee + R18.685M Debtor + Accountant

**Evidence Location:** `ad-res-j7/evidence/conflict_of_interest/R18_685M_debt/`

**Implication:** Massive financial motive to conceal fraud and prevent discovery of debt.

**Related Events:**
- EVENT_H018: Trial balance email (Aug 13, 2020)
- EVENT_058: Audit dismissal (June 10, 2025)
- EVENT_061: Debt discovery

**Applications:** 1, 2

#### 3. Fabricated Accounts & R5.4M Stock Fraud

**Evidence Location:** `ad-res-j7/ANNEXURES/accounting/fabricated_accounts/`

**Related Events:**
- EVENT_H005: R500K stock provision fabrication (Feb 20, 2020)
- EVENT_024: R5.4M stock fraud scheme (March 30, 2025)

**Applications:** 1, 2

---

## Evidence Access Guide

### Direct Repository Access

All evidence is available in the extended repository:

**Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)

**Key Directories:**
- `ANNEXURES/` - Formal evidence annexures organized by code (JF01-JF07)
- `evidence/` - Categorized evidence by type
- `case_2025_137857/` - Case-specific documentation
- `jax-response/` - Jax correspondence (394 files)
- `FINAL_AFFIDAVIT_PACKAGE/` - Complete affidavit package (270 files)

### Evidence Codes

| Code | Description | File Count |
|------|-------------|------------|
| JF | Jacqueline Faucitt evidence | 978 |
| JAX | Jax correspondence | 927 |
| JF01-JF07 | Formal annexure categories | 266 |
| DJF | Daniel James Faucitt evidence | 4 |

---

## Navigation

- **[Home](index.md)** - Case overview
- **[Application 1 Details](application-1.md)** - Ex Parte Interdict
- **[Application 2 Details](application-2.md)** - Settlement Enforcement
- **[Application 3 Details](application-3.md)** - Contact Interdict
- **[Data Model Analysis](data-model-analysis.md)** - Data integrity report

---

**Last Updated:** 2025-11-19  
**Data Model Version:** 11.0  
**Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    output_file = Path('/home/ubuntu/revstream1/evidence-index-enhanced.md')
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✓ Enhanced evidence index created: {output_file}")
    return output_file

def update_main_index():
    """Update the main index.md with links to enhanced evidence index"""
    
    index_file = Path('/home/ubuntu/revstream1/index.md')
    
    with open(index_file, 'r') as f:
        content = f.read()
    
    # Add link to enhanced evidence index in the Evidence Resources section
    if 'evidence-index-enhanced.md' not in content:
        content = content.replace(
            '### [📁 Complete Evidence Index](evidence-index.md)',
            '### [📁 Complete Evidence Index](evidence-index.md)\n### [📁 Enhanced Evidence Index (NEW)](evidence-index-enhanced.md)'
        )
        
        # Update the data model version reference
        content = content.replace(
            'This case is supported by a robust and comprehensive data model.',
            'This case is supported by a robust and comprehensive data model (Version 11.0, updated 2025-11-19).'
        )
    
    with open(index_file, 'w') as f:
        f.write(content)
    
    print(f"✓ Main index updated: {index_file}")

def create_data_model_update_notice():
    """Create a notice about the data model updates"""
    
    content = """# Data Model Updates - 2025-11-19

## Summary

The data models for Case 2025-137857 have been comprehensively refined and updated to version 11.0.

## Changes Made

### Entities (Version 11.0)
- ✓ Added evidence references to 9 key entities
- ✓ Enhanced ad-res-j7 cross-references
- ✓ Added evidence repository links
- ✓ New fields: `evidence_files`, `ad_res_j7_references`, `evidence_repository`

### Events (Version 11.0)
- ✓ Added perpetrators to 7 events (EVT-063 through EVT-069)
- ✓ Enhanced application mappings for all events
- ✓ New field: `related_applications`

### Timeline (Version 10.0)
- ✓ Resolved PHASE_005 duplication
- ✓ Renamed second PHASE_005 to PHASE_007 (Debt Accumulation Phase)
- ✓ Enhanced application mappings

### Relations (Version 9.0)
- ✓ Enhanced application mappings for all 24 relations
- ✓ Added evidence repository links
- ✓ New fields: `related_applications`, `evidence_repository`

## Files Updated

- `data_models/entities/entities_refined_2025_11_19_v3.json`
- `data_models/events/events_refined_2025_11_19_v3.json`
- `data_models/timelines/timeline_refined_2025_11_19_v3.json`
- `data_models/relations/relations_refined_2025_11_19_v3.json`

## GitHub Pages Updates

- ✓ Created enhanced evidence index with application-specific organization
- ✓ Updated main index with version information
- ✓ Improved evidence navigation and cross-referencing

## Evidence Integration

All entities now have direct references to evidence files in the ad-res-j7 repository:

- **Total evidence files:** 2,866 (226.78 MB)
- **Evidence codes:** JF (978), JAX (927), JF01-JF07 (266)
- **Repository:** https://github.com/cogpy/ad-res-j7

## Next Steps

1. Review the enhanced evidence index
2. Verify all cross-references are accurate
3. Sync changes to GitHub repository
4. Update GitHub Pages deployment

---

**Date:** 2025-11-19  
**Version:** 11.0  
**Status:** Complete
"""
    
    output_file = Path('/home/ubuntu/revstream1/DATA_MODEL_UPDATES_2025_11_19.md')
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✓ Data model update notice created: {output_file}")

def main():
    print("=" * 80)
    print("GITHUB PAGES UPDATE - 2025-11-19")
    print("=" * 80)
    print()
    
    print("Loading latest refined models...")
    entities, events, timeline, relations = load_latest_models()
    print(f"✓ Loaded: {len(entities['entities']['persons'])} persons, {len(events['events'])} events")
    print()
    
    print("Creating enhanced evidence index...")
    create_enhanced_evidence_index()
    print()
    
    print("Updating main index...")
    update_main_index()
    print()
    
    print("Creating data model update notice...")
    create_data_model_update_notice()
    print()
    
    print("=" * 80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)
    print()
    print("Files created/updated:")
    print("  • evidence-index-enhanced.md (NEW)")
    print("  • index.md (UPDATED)")
    print("  • DATA_MODEL_UPDATES_2025_11_19.md (NEW)")
    print()
    print("=" * 80)

if __name__ == '__main__':
    main()
