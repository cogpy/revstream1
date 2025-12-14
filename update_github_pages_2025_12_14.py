#!/usr/bin/env python3
"""
Update and organize GitHub Pages for clear evidence references
Date: 2025-12-14
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DOCS_DIR = BASE_DIR / "docs"
FILINGS_DIR = DOCS_DIR / "filings"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Load evidence index
EVIDENCE_INDEX = load_json(BASE_DIR / "APPLICATIONS_EVIDENCE_INDEX_2025_12_14.json")

def update_index_page():
    """Update the main index page with improved organization"""
    print("\n🔄 Updating index page...")
    
    index_content = """---
layout: default
title: Home
---

# Revenue Stream Hijacking Case 2025-137857

## Executive Summary

This documentation repository provides comprehensive evidence and analysis of the systematic hijacking of revenue streams in the RegimA business operations case. The case involves **three sequential interdict applications** filed over a 6-month period (March-November 2025), documenting **R10,269,727.90** in total losses.

### Critical Evidence Overview

The case is supported by **17 evidence sources** from the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7), including:

- **JF01 (CRITICAL)**: Shopify Plus Email (26 July 2017) - Forensic time capsule proving independent business operations
- **SF2 (CRITICAL)**: Sage Screenshots - Direct evidence of Rynette Farrar's system control
- **SF6 (CRITICAL)**: Kayla Pretorius Estate Documentation - Trigger event for business appropriation

**Evidence Strength**: 
- Civil burden (50%): ✅ **EXCEEDED** (2 critical sources)
- Criminal burden (95%): ✅ **EXCEEDED** (2 critical sources)

---

## Case Overview

| **Metric** | **Value** |
|------------|-----------|
| **Case Number** | 2025-137857 |
| **Case Name** | Peter Faucitt v. Jacqueline Faucitt et al. |
| **Period** | March 15, 2025 - August 20, 2025 |
| **Duration** | 158 days of documented criminal activity |
| **Total Events** | 44 (refined 2025-12-14) |
| **Events with Financial Impact** | 54 |
| **Total Documented Losses** | R10,269,727.90 |

---

## Three Sequential Interdict Applications

### Application 1: Ex Parte Interdict (August 13, 2025)

**Type:** Ex parte urgent application  
**Targets:** Both Jacqueline and Daniel Faucitt  
**Status:** Pending return date; notice of intention to oppose filed September 5, 2025

**Key Evidence:**
- [JF01 - Shopify Plus Email](evidence-index.md#jf01)
- [JF06 - Court Documents](evidence-index.md#jf06)
- [JF08 - Evidence Packages](evidence-index.md#jf08)
- [SF6 - Kayla Pretorius Estate](evidence-index.md#sf6)

[**→ View Application 1 Details**](application-1.md) | [**→ View Application 1 Evidence**](application-1-evidence.md)

---

### Application 2: Settlement Agreement Enforcement (October 2025)

**Type:** Application to make settlement agreement an order of court  
**Context:** Mediation held September 18, 2025

**Key Evidence:**
- [JF05 - Correspondence Evidence](evidence-index.md#jf05)
- [JF06 - Court Documents](evidence-index.md#jf06)

[**→ View Application 2 Details**](application-2.md) | [**→ View Application 2 Evidence**](application-2-evidence.md)

---

### Application 3: Third Application (November 2025)

**Type:** Further relief

**Key Evidence:**
- [JF01 - Shopify Plus Email](evidence-index.md#jf01)
- [JF02 - Shopify Sales Reports](evidence-index.md#jf02)
- [JF07 - Screenshots](evidence-index.md#jf07)
- [JF08 - Evidence Packages](evidence-index.md#jf08)
- [SF2 - Sage Screenshots](evidence-index.md#sf2)

[**→ View Application 3 Details**](application-3.md) | [**→ View Application 3 Evidence**](application-3-evidence.md)

---

## Legal Framework

### Companies Act 71 of 2008 Violations

| Section | Violation | Evidence Status | Burden Met |
|---------|-----------|-----------------|------------|
| **s75** | Conflict of Interest | Conclusive | ✅ 50% EXCEEDED |
| **s76** | Fiduciary Breach | Conclusive | ✅ 50% EXCEEDED |
| **s77** | Personal Liability | Conclusive | ✅ 50% EXCEEDED |
| **s162** | Delinquent Director | Conclusive | ✅ 50% EXCEEDED |
| **s163** | Oppression | Moderate | ⚠️ 50% ACHIEVABLE |

[**→ View Complete Legal Framework Analysis**](legal-framework.md)

---

## Evidence Index

### Critical Evidence (PRIORITY: CRITICAL)

1. **[JF01 - Shopify Plus Email (26 July 2017)](evidence-index.md#jf01)**
   - Forensic time capsule proving independent business operations
   - Burden: Civil 50% ✅ | Criminal 95% ✅

2. **[SF2 - Sage Screenshots - Rynette Control](evidence-index.md#sf2)**
   - Direct evidence of Sage accounting system control
   - Burden: Criminal 95% ✅

3. **[SF6 - Kayla Pretorius Estate Documentation](evidence-index.md#sf6)**
   - Trigger event for business appropriation
   - Timeline correlation with JF9

### High Priority Evidence

4. **[JF02 - Shopify Sales Reports](evidence-index.md#jf02)**
5. **[JF03 - Financial Records and Analysis](evidence-index.md#jf03)**
6. **[JF04 - Daniel Faucitt Personal Bank Records](evidence-index.md#jf04)**
7. **[JF06 - Court Documents and Filings](evidence-index.md#jf06)**
8. **[JF08 - Evidence Packages (May-October 2025)](evidence-index.md#jf08)**
9. **[JF09 - Timeline Analysis](evidence-index.md#jf09)**

[**→ View Complete Evidence Index**](evidence-index-comprehensive.md)

---

## Legal Filings

### Civil Actions

- [Answering Affidavit (Evidence Enhanced)](filings/ANSWERING_AFFIDAVIT_EVIDENCE_ENHANCED_20251214.md)
- [Application 1 - Ex Parte Interdict](application-1.md)
- [Application 2 - Settlement Enforcement](application-2.md)
- [Application 3 - Further Relief](application-3.md)

### Criminal Complaints

- [Commercial Crime Case Submission (Evidence Enhanced)](filings/COMMERCIAL_CRIME_EVIDENCE_ENHANCED_20251214.md)
- [POPIA Criminal Complaint (Evidence Enhanced)](filings/POPIA_COMPLAINT_EVIDENCE_ENHANCED_20251214.md)

### Regulatory Complaints

- [CIPC Companies Act Complaint (Evidence Enhanced)](filings/CIPC_COMPLAINT_EVIDENCE_ENHANCED_20251214.md)
- [NPA Tax Fraud Report (Evidence Enhanced)](filings/NPA_TAX_FRAUD_REPORT_EVIDENCE_ENHANCED_20251214.md)

[**→ View All Filings**](filings/)

---

## Data Models

### Entities, Relations, Events & Timeline

- **Entities**: 25 entities (refined 2025-12-14)
- **Relations**: 70 relations (refined 2025-12-14)
- **Events**: 44 events (refined 2025-12-14)
- **Timeline**: 43 entries (refined 2025-12-14)

All data models have been enhanced with comprehensive ad-res-j7 evidence cross-references.

[**→ View Data Model Analysis**](data-model-analysis.md)

---

## Timeline

[**→ View Interactive Timeline**](timeline.html) | [**→ View Timeline Markdown**](timeline.md)

---

## Quick Links

- [Evidence Index](evidence-index-comprehensive.md)
- [Legal Framework](legal-framework.md)
- [Timeline](timeline.md)
- [Applications](applications.md)
- [Filings](filings/)
- [Entity Profiles](entity-profiles/)
- [Events](events/)

---

**Last Updated:** 2025-12-14  
**Repository:** [cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Evidence Repository:** [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    with open(DOCS_DIR / "index.md", 'w') as f:
        f.write(index_content)
    print("✅ Updated: docs/index.md")

def update_evidence_index():
    """Update the evidence index with comprehensive cross-references"""
    print("\n🔄 Updating evidence index...")
    
    evidence_index_content = """---
layout: default
title: Evidence Index
---

# Comprehensive Evidence Index

## Overview

This index provides a complete mapping of all evidence sources from the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7) to the three applications in Case 2025-137857.

**Total Evidence Sources:** 17  
**Critical Evidence:** 3  
**High Priority Evidence:** 6  
**Medium Priority Evidence:** 8

---

## Critical Evidence

<a name="jf01"></a>
### JF01: Shopify Plus Email (26 July 2017)
**THE "FORENSIC TIME CAPSULE" - IRREFUTABLE PROOF**

**Location:** `ANNEXURES/JF01/`  
**Priority:** **CRITICAL**  
**Burden of Proof:** Civil 50% ✅ EXCEEDED | Criminal 95% ✅ EXCEEDED

#### Contents
1. Re_ The RegimA Group results and Computer Expense analysis.eml (64,715 bytes)
2. Re_ belongs to regimA.eml (32,155 bytes)

#### Proves
- ✅ Kayla Pretorius personally managed Shopify Plus onboarding
- ✅ Daniel Faucitt directly involved (CC'd on communications)
- ✅ Independent business operations (no "head office" involvement)
- ✅ Use of independent email addresses (kayp@rzo.io, kayla@regima.zone)
- ✅ Personal phone number (011 615 29869) - later appropriated

#### Refutes
- ❌ Applicant's claim of centralized "head office" control
- ❌ Applicant's claim that Daniel never operated independent businesses

#### Legal Significance
Contemporaneous documentary evidence from neutral third party (Shopify Inc.) - unalterable historical record that completely demolishes Applicant's false narrative.

#### Related Entities
- PERSON_003 (Kayla Pretorius)
- PERSON_005 (Daniel James Faucitt)
- ORG_003 (RegimA Zone Ltd)
- PLATFORM_001 (Shopify Platform)

#### Related Events
- EVENT_H001 (First ReZonance Invoice)
- EVENT_H002 (ReZonance Service Expansion)
- EVENT_001 (Shopify Plus Onboarding)

---

<a name="sf2"></a>
### SF2: Sage Screenshots - Rynette Control
**DIRECT EVIDENCE OF SYSTEM CONTROL**

**Location:** `ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md`  
**Priority:** **CRITICAL**  
**Burden of Proof:** Criminal 95% ✅ EXCEEDED

#### Proves
- ✅ Rynette Farrar's direct control of Sage accounting system
- ✅ Account manipulation capabilities
- ✅ System access for fraudulent record submission

#### Criminal Charges Supported
- Fraud
- Uttering
- Forgery

#### Related Entities
- PERSON_002 (Rynette Farrar)
- ORG_001 (RWD ZA)
- ORG_002 (Regima Skin Treatments CC)

#### Related Events
- EVENT_007 (Account Manipulation)
- EVENT_008 (Fraudulent Record Submission)
- EVENT_009 (Revenue Hijacking)

---

<a name="sf6"></a>
### SF6: Kayla Pretorius Estate Documentation
**TRIGGER EVENT FOR BUSINESS APPROPRIATION**

**Location:** `ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md`  
**Priority:** **CRITICAL**

#### Proves
- ✅ Kayla's role in business operations
- ✅ Estate documentation
- ✅ Trigger event for business appropriation

#### Legal Significance
Foundation event for fraud scheme - JF9 timeline shows immediate system access changes after estate event.

#### Related Entities
- PERSON_003 (Kayla Pretorius)

#### Related Events
- EVENT_001 (Shopify Plus Onboarding)
- EVENT_002 (Business Appropriation Begins)

---

## High Priority Evidence

<a name="jf02"></a>
### JF02: Shopify Sales Reports
**Location:** `ANNEXURES/JF02/`  
**Priority:** HIGH

#### Proves
- ✅ Active Shopify Plus business operations
- ✅ Revenue generation through independent channels
- ✅ Business performance tracking

---

<a name="jf03"></a>
### JF03: Financial Records and Analysis
**Location:** `ANNEXURES/JF03/`  
**Priority:** HIGH

#### Proves
- ✅ Detailed financial record-keeping
- ✅ Business expense tracking
- ✅ Independent financial management

---

<a name="jf04"></a>
### JF04: Daniel Faucitt Personal Bank Records
**Location:** `ANNEXURES/JF04/`  
**Priority:** HIGH  
**Burden of Proof:** Civil 50% ✅ EXCEEDED

#### Proves
- ✅ Complete financial transparency
- ✅ Legitimate banking transactions
- ✅ No evidence of hidden assets

#### Refutes
- ❌ Claims of financial misconduct
- ❌ Claims of asset concealment

---

<a name="jf06"></a>
### JF06: Court Documents and Filings
**Location:** `ANNEXURES/JF06/`  
**Priority:** HIGH  
**File Count:** 99 PDF files

#### Proves
- ✅ Complete procedural history
- ✅ Applicant's applications and claims
- ✅ Attorney correspondence and withdrawals

---

<a name="jf08"></a>
### JF08: Evidence Packages (May-October 2025)
**Location:** `ANNEXURES/JF08/`  
**Priority:** HIGH

#### Packages
1. evidence_package_20250523 (23 May 2025)
2. evidence_package_20250606 (6 June 2025)
3. evidence_package_20250811 (11 August 2025)
4. evidence_package_20251009 (9 October 2025)
5. evidence_package_20251012 (12 October 2025)

**Note:** First package (23 May 2025) is one day after Shopify audit trail destruction (22 May 2025).

#### Criminal Significance
Response to evidence destruction - demonstrates systematic evidence gathering.

---

<a name="jf09"></a>
### JF09: Timeline Analysis
**Location:** `ANNEXURES/JF09/`  
**Priority:** HIGH

#### Proves
- ✅ Comprehensive timeline analysis
- ✅ Entity relationship mapping
- ✅ Pattern recognition and fraud detection

#### Methodology
Agentic entity modeling

---

## Medium Priority Evidence

<a name="jf05"></a>
### JF05: Correspondence Evidence (JF8 Series)
**Location:** `ANNEXURES/JF05/`  
**Priority:** MEDIUM

---

<a name="jf07"></a>
### JF07: Screenshots and Visual Evidence
**Location:** `ANNEXURES/JF07/`  
**Priority:** MEDIUM  
**File Count:** 62 screenshot images

---

<a name="sf1"></a>
### SF1: Bantjies Debt Documentation
**Location:** `ANNEXURES/SF1_Bantjies_Debt_Documentation.md`  
**Priority:** MEDIUM

---

<a name="sf3"></a>
### SF3: Strategic Logistics Stock Adjustment
**Location:** `ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md`  
**Priority:** MEDIUM

---

<a name="sf4"></a>
### SF4: SARS Audit Email
**Location:** `ANNEXURES/SF4_SARS_Audit_Email.md`  
**Priority:** HIGH  
**Regulatory Significance:** Tax fraud indicators

---

<a name="sf5"></a>
### SF5: Adderory Company Registration & Stock Supply
**Location:** `ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md`  
**Priority:** MEDIUM

---

<a name="sf7"></a>
### SF7: Court Order - Kayla Email Seizure
**Location:** `ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md`  
**Priority:** HIGH  
**Legal Significance:** Court-sanctioned evidence collection

---

<a name="sf8"></a>
### SF8: Linda Employment Records
**Location:** `ANNEXURES/SF8_Linda_Employment_Records.md`  
**Priority:** MEDIUM

---

## Evidence by Application

### Application 1: Ex Parte Interdict
- JF01 (CRITICAL)
- JF06 (HIGH)
- JF08 (HIGH)
- SF6 (CRITICAL)

### Application 2: Settlement Enforcement
- JF05 (MEDIUM)
- JF06 (HIGH)

### Application 3: Further Relief
- JF01 (CRITICAL)
- JF02 (HIGH)
- JF07 (MEDIUM)
- JF08 (HIGH)
- SF2 (CRITICAL)

---

**Last Updated:** 2025-12-14  
**Evidence Repository:** [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    with open(DOCS_DIR / "evidence-index-comprehensive.md", 'w') as f:
        f.write(evidence_index_content)
    print("✅ Updated: docs/evidence-index-comprehensive.md")

def update_application_evidence_pages():
    """Update evidence pages for each application"""
    print("\n🔄 Updating application evidence pages...")
    
    for app_id, app_data in EVIDENCE_INDEX["applications"].items():
        app_num = app_id.split("_")[1]
        
        evidence_page_content = f"""---
layout: default
title: Application {app_num} Evidence
---

# Application {app_num}: {app_data["title"]}

## Evidence References

**Type:** {app_data["type"]}  
**Burden of Proof:** {app_data["burden_of_proof"]}

---

"""
        
        for ev_ref in app_data["evidence_references"]:
            evidence_page_content += f"""### {ev_ref["evidence_id"]}: {ev_ref["title"]}

**Location:** `{ev_ref["location"]}`  
**Priority:** {ev_ref["priority"]}

#### Proves
"""
            for proof in ev_ref.get("proves", []):
                evidence_page_content += f"- ✅ {proof}\n"
            
            if ev_ref.get("refutes"):
                evidence_page_content += "\n#### Refutes\n"
                for refute in ev_ref["refutes"]:
                    evidence_page_content += f"- ❌ {refute}\n"
            
            evidence_page_content += "\n---\n\n"
        
        evidence_page_content += f"""
[**← Back to Application {app_num}**](application-{app_num}.md) | [**View Evidence Index**](evidence-index-comprehensive.md)
"""
        
        with open(DOCS_DIR / f"application-{app_num}-evidence.md", 'w') as f:
            f.write(evidence_page_content)
        print(f"✅ Updated: docs/application-{app_num}-evidence.md")

def main():
    print("=" * 80)
    print("GITHUB PAGES UPDATE - 2025-12-14")
    print("=" * 80)
    
    update_index_page()
    update_evidence_index()
    update_application_evidence_pages()
    
    print("\n" + "=" * 80)
    print("✅ GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)
    print("\n📋 Next: Sync and push changes to repository")

if __name__ == "__main__":
    main()
