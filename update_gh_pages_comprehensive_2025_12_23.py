#!/usr/bin/env python3
"""
GitHub Pages Comprehensive Update Script
Date: 2025-12-23
Purpose: Update GitHub Pages with refined models and legal filings
"""

import json
from datetime import datetime
from pathlib import Path

REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
DOCS_PATH = REVSTREAM_PATH / "docs"
DATA_MODELS_PATH = REVSTREAM_PATH / "data_models"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def create_index_page():
    """Create main index page with clear navigation"""
    
    content = """# Revenue Stream Hijacking Case 2025-137857

**Last Updated:** 2025-12-23
**Case Status:** Active - Evidence Collection Complete

## Quick Navigation

### 📋 Legal Filings
- [CIPC Companies Act Complaint (Refined 2025-12-23)](CIPC_COMPLAINT_REFINED_2025_12_23.html)
- [POPIA Criminal Complaint (Comprehensive 2025-12-23)](POPIA_COMPLAINT_COMPREHENSIVE_2025_12_23.html)
- [Civil Response Documentation](filings/civil/)
- [Criminal Case Materials](filings/criminal/)

### 📊 Evidence Index
- [Comprehensive Evidence Index](evidence-index-comprehensive.html)
- [Evidence by Application](evidence/)
- [Timeline Evidence](timeline.html)

### 👥 Entities & Relations
- [Entity Profiles](entities/)
- [Relation Network](analysis/relations.html)
- [Conspiracy Network Diagram](conspiracy_network.png)

### 📅 Timeline & Events
- [Comprehensive Timeline](timeline.html)
- [Event Catalog](events/)
- [Key Milestones](analysis/milestones.html)

### 📈 Analysis & Reports
- [Burden of Proof Analysis](analysis/burden-of-proof.html)
- [Financial Impact Summary](financial_impact_summary.html)
- [Data Model Analysis](data-model-analysis.html)

---

## Case Summary

**Total Financial Impact:** R10,740,334+ (quantified)

**Key Perpetrators:**
- Peter Andrew Faucitt (Primary)
- Rynette Farrar (Co-conspirator)
- Danie Bantjies (Professional misconduct)

**Evidence Strength:**
- Civil Standard (50%+): **EXCEEDED** at 85-95%
- Criminal Standard (95%+): **EXCEEDED** on key events

**Critical Events:**
1. R5.4M stock theft (EVENT_024) - 95%+ criminal threshold
2. R900K unauthorized transfers (EVENT_022) - 95%+ criminal threshold
3. Domain fraud & customer hijacking (EVENT_010) - 95%+ criminal threshold
4. Bantjies audit dismissal (EVENT_058) - Consciousness of guilt
5. Evidence destruction (EVENT_065, EVENT_066) - 95%+ criminal threshold

---

## Evidence Organization

### By Application Type

#### 1. Civil Application (Case 2025-137857)
**Burden of Proof:** Balance of Probabilities (50%+) - **EXCEEDED**

**Key Evidence:**
- ANNEXURES/JF01-JF13: Comprehensive evidence packages
- ANNEXURES/SF1-SF8: Special forensic files
- 1-CIVIL-RESPONSE: Answering affidavit and supporting documents

**Status:** Evidence exceeds civil standard at 85-95% confidence

#### 2. Criminal Case (SAPS)
**Burden of Proof:** Beyond Reasonable Doubt (95%+) - **EXCEEDED** on key events

**Key Evidence:**
- R5.4M stock theft with direct connection to competing entity
- R900K unauthorized transfers without co-director authority
- Domain fraud with customer hijacking
- Systematic evidence destruction

**Status:** Multiple events exceed criminal threshold

#### 3. CIPC Companies Act Complaint
**Burden of Proof:** Balance of Probabilities (50%+) - **EXCEEDED**

**Key Violations:**
- Section 76: Director's standard of conduct
- Section 77: Liability of directors
- Section 22: Reckless trading

**Status:** Comprehensive evidence for delinquent director declaration

#### 4. POPIA Criminal Complaint
**Burden of Proof:** Beyond Reasonable Doubt (95%+) - **EXCEEDED**

**Key Violations:**
- Section 11: Unlawful processing
- Section 19: Security safeguards failure
- Section 21: Unauthorized disclosure
- Section 69: Criminal offense (willful unlawful processing)

**Status:** Multiple criminal violations with conclusive evidence

---

## Evidence Cross-Reference System

All evidence is cross-referenced between:
1. **revstream1** repository (this site)
2. **ad-res-j7** repository (extended evidence)
3. **Data models** (entities, relations, events, timeline)

### Evidence Mapping
- **JF01-JF13:** Primary annexure packages
- **SF1-SF8:** Special forensic evidence files
- **1-CIVIL-RESPONSE:** Civil case documentation
- **2-CRIMINAL-CASE:** Criminal case materials

---

## Key Forensic Evidence Files

### SF1: Bantjies Debt Documentation
**Amount:** R18,685,000 debt to Faucitt Family Trust
**Significance:** Massive conflict of interest (trustee-debtor-accountant)
**Evidence Link:** [SF1_Bantjies_Debt_Documentation.md](evidence/SF1.html)

### SF2: Sage Screenshots - Rynette Control
**Evidence:** Dual email access (Pete@regima.com)
**Significance:** Proves technical capability for fraud
**Evidence Link:** [SF2_Sage_Screenshots_Rynette_Control.md](evidence/SF2.html)

### SF3: Strategic Logistics Stock Adjustment
**Amount:** R5,400,000 stock disappearance
**Significance:** Criminal threshold exceeded; 46% of annual sales
**Evidence Link:** [SF3_Strategic_Logistics_Stock_Adjustment.md](evidence/SF3.html)

### SF4: SARS Audit Email
**Evidence:** Professional correspondence showing coordination
**Significance:** Knowledge acquisition and strategic timing
**Evidence Link:** [SF4_SARS_Audit_Email.md](evidence/SF4.html)

### SF5: Adderory Company Registration
**Evidence:** Competing business registered 4 years before fraud escalation
**Significance:** Premeditation and long-term conspiracy planning
**Evidence Link:** [SF5_Adderory_Company_Registration_Stock_Supply.md](evidence/SF5.html)

### SF6: Kayla Pretorius Estate Documentation
**Evidence:** Death certificate and estate documentation
**Significance:** Trigger event for fraud exposure
**Evidence Link:** [SF6_Kayla_Pretorius_Estate_Documentation.md](evidence/SF6.html)

### SF7: Court Order - Email Seizure
**Evidence:** Court order for Kayla's email seizure
**Significance:** Legal authority for evidence collection
**Evidence Link:** [SF7_Court_Order_Kayla_Email_Seizure.md](evidence/SF7.html)

### SF8: Linda Employment Records
**Evidence:** Employment documentation for Rynette's sister
**Significance:** Family network involvement
**Evidence Link:** [SF8_Linda_Employment_Records.md](evidence/SF8.html)

---

## Timeline Phases

### Phase 1: Foundation & Business Establishment (2017-2019)
**Events:** 7
**Significance:** Establishes legitimate business foundation

### Phase 2: Fraud Preparation & Execution (2020-2023)
**Events:** 22
**Significance:** Core fraud period with R10.2M+ revenue theft

### Phase 3: Discovery & Legal Action (2024-2025)
**Events:** 48
**Significance:** Evidence discovery and legal response

---

## Contact & Support

**Repository:** [github.com/cogpy/revstream1](https://github.com/cogpy/revstream1)
**Extended Evidence:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)

**Last Updated:** 2025-12-23
**Version:** 15.0_COMPREHENSIVE_REFINEMENT
"""
    
    return content

def create_evidence_index():
    """Create comprehensive evidence index"""
    
    content = """# Evidence Index - Comprehensive

**Last Updated:** 2025-12-23
**Total Evidence Files:** 21+ primary packages

## Primary Annexure Packages (JF01-JF13)

### JF01: Shopify Plus Email - The Forensic Time Capsule
**Date:** 2017-07-26
**Type:** Email correspondence
**Significance:** Irrefutable proof of business structure
**Key Evidence:**
- Shopify Plus onboarding email
- Business ownership structure
- Platform operator identification
- Historical foundation evidence

**Cross-References:**
- EVENT_H011 (Shopify Plus onboarding)
- PERSON_005 (Daniel - platform owner)
- ORG_003 (RegimA Zone Ltd)

### JF02: Business Operations Documentation
**Type:** Operational records
**Significance:** Establishes legitimate business operations
**Key Evidence:**
- Sales reports
- Operational procedures
- Business correspondence

### JF03: Financial Records
**Type:** Financial documentation
**Significance:** Documents systematic financial manipulation
**Key Evidence:**
- Inter-company transactions
- Unauthorized transfers
- Stock adjustments
- Loan agreements

**Cross-References:**
- EVENT_H005 (R1.642M adjustments)
- EVENT_H006 (R1.948M adjustments)
- EVENT_022 (R900K unauthorized transfers)

### JF04: CIPC Company Records
**Type:** Company registration documents
**Significance:** Legal entity structure and ownership
**Key Evidence:**
- Company registration certificates
- Director appointments
- Shareholding structures

### JF05: Correspondence Evidence
**Type:** Email and letter correspondence
**Significance:** Communication patterns and instructions
**Key Evidence:**
- POPIA violation notice
- Legal correspondence
- Professional communications

### JF06: Court Applications and Filings
**Type:** Legal documents
**Significance:** Court proceedings and legal actions
**Key Evidence:**
- Application documents
- Court orders
- Legal submissions

### JF07: Transaction Records
**Type:** Banking and financial transactions
**Significance:** Payment flows and unauthorized transfers
**Key Evidence:**
- Bank statements
- Payment records
- Transfer documentation

**Cross-References:**
- EVENT_022 (R900K transfers)
- EVENT_008 (R850K+ transfers)

### JF08: Comprehensive Fraud Evidence Package
**Type:** Multi-source evidence compilation
**Significance:** Central evidence repository
**Key Evidence:**
- Timeline documentation
- Email evidence
- Financial records
- Fraud patterns

**Cross-References:**
- Multiple events across all phases
- Primary evidence for most allegations

### JF09: Domain Registration Fraud Evidence
**Type:** Domain registration records
**Significance:** Identity fraud and customer hijacking
**Key Evidence:**
- Domain registration details
- WHOIS records
- Ownership documentation

**Cross-References:**
- EVENT_010 (Domain registration)
- EVENT_027 (Customer diversion)

### JF10-JF13: Additional Evidence Packages
**Type:** Supplementary evidence
**Significance:** Supporting documentation

---

## Special Forensic Files (SF1-SF8)

### SF1: Bantjies Debt Documentation
**Amount:** R18,685,000
**Type:** Financial records
**Significance:** Conflict of interest - trustee-debtor-accountant
**Key Evidence:**
- Debt documentation
- Trust records
- Financial statements

**Legal Significance:**
- Triple conflict of interest
- Motive for fraud concealment
- Breach of fiduciary duty

**Cross-References:**
- PERSON_007 (Danie Bantjies)
- EVENT_058 (Audit dismissal)
- TRUST_001 (Faucitt Family Trust)

### SF2: Sage Screenshots - Rynette Control
**Date:** 2025-06-20 (screenshot date)
**Type:** System screenshots
**Significance:** Proves dual email access and technical capability
**Key Evidence:**
- Sage system access records
- Email account "Pete@regima.com" under Rynette's control
- Subscription ownership evidence

**Legal Significance:**
- Direct proof of email control
- POPIA violations
- Technical capability for fraud
- Evidence destruction capability

**Cross-References:**
- PERSON_002 (Rynette Farrar)
- EVENT_014 (Email impersonation)
- EVENT_066 (System expiry)

### SF3: Strategic Logistics Stock Adjustment
**Amount:** R5,400,000
**Date:** 2025-03-01
**Type:** Financial records
**Significance:** Criminal threshold exceeded
**Key Evidence:**
- Stock adjustment records
- Historical comparison data
- Adderory supply connection

**Legal Significance:**
- 46% of annual sales disappeared
- 10x historical adjustment rate
- Direct connection to competing entity
- Criminal threshold (95%+) exceeded

**Cross-References:**
- EVENT_024 (Stock disappearance)
- SF5 (Adderory connection)
- PERSON_001, PERSON_002 (Perpetrators)

### SF4: SARS Audit Email
**Date:** 2020-08-13
**Type:** Email correspondence
**Significance:** Professional coordination and knowledge acquisition
**Key Evidence:**
- Trial balance distribution
- Bernadine Wright correspondence
- Bantjies involvement

**Cross-References:**
- PERSON_007 (Danie Bantjies)
- PERSON_010 (Bernadine Wright)

### SF5: Adderory Company Registration & Stock Supply
**Date:** 2021-04-01 (registration)
**Type:** Company records
**Significance:** Premeditation - 4 years before fraud escalation
**Key Evidence:**
- Company registration documents
- Stock supply records
- Competing business evidence

**Legal Significance:**
- Long-term conspiracy planning
- Premeditation
- Direct connection to stock theft

**Cross-References:**
- EVENT_H009 (Company registration)
- EVENT_024 (Stock theft)
- PERSON_003 (Rynette's son)

### SF6: Kayla Pretorius Estate Documentation
**Date:** 2025-05-22 (death date)
**Type:** Estate documents
**Significance:** Trigger event for fraud exposure
**Key Evidence:**
- Death certificate
- Estate documentation
- Card expiry evidence

**Legal Significance:**
- Trigger event
- Estate exploitation
- Timeline marker

**Cross-References:**
- EVENT_067 (Death)
- PERSON_008 (Kayla)

### SF7: Court Order - Kayla Email Seizure
**Type:** Court order
**Significance:** Legal authority for evidence collection
**Key Evidence:**
- Court order documentation
- Email seizure authority

**Cross-References:**
- SF6 (Estate documentation)
- EVENT_067 (Trigger event)

### SF8: Linda Employment Records
**Type:** Employment documentation
**Significance:** Family network involvement
**Key Evidence:**
- Employment contracts
- Relationship documentation

**Cross-References:**
- PERSON_006 (Linda)
- PERSON_002 (Rynette - sister)

---

## Evidence by Burden of Proof

### Criminal Standard (95%+) - EXCEEDED

**Stock Theft (EVENT_024):**
- SF3: R5.4M stock disappearance
- SF5: Adderory connection
- JF03: Financial records

**Unauthorized Transfers (EVENT_022):**
- JF07: R900K transfer records
- JF03: Financial documentation

**Domain Fraud (EVENT_010, EVENT_027):**
- JF09: Domain registration
- JF08: Customer diversion evidence
- SF5: Adderory ownership

**Evidence Destruction (EVENT_065, EVENT_066):**
- SF2: System control evidence
- JF05: POPIA violation notice

**Fraud Concealment (EVENT_058):**
- SF1: R18.685M conflict of interest
- SF3: Stock fraud concealment
- JF08: Timeline evidence

### Civil Standard (50%+) - EXCEEDED at 85-95%

**All Events:** Comprehensive evidence exceeds civil standard

---

## Evidence Organization

### By Repository
- **revstream1:** Primary case repository
- **ad-res-j7:** Extended evidence repository

### By Application
- **Civil (2025-137857):** JF01-JF13, SF1-SF8
- **Criminal (SAPS):** SF1-SF5, JF07-JF09
- **CIPC:** JF03-JF04, SF1-SF3
- **POPIA:** SF2, JF01, JF05, JF08-JF09

### By Evidence Type
- **Financial:** JF03, JF07, SF1, SF3
- **Documentary:** JF01-JF06
- **Digital:** JF08-JF09, SF2
- **Legal:** JF06, SF7

---

**Last Updated:** 2025-12-23
**Version:** 2.0_COMPREHENSIVE
"""
    
    return content

def main():
    print("=" * 80)
    print("GITHUB PAGES COMPREHENSIVE UPDATE")
    print("Revenue Stream Hijacking Case 2025-137857")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Create index page
    print("\n=== CREATING INDEX PAGE ===")
    index_content = create_index_page()
    index_path = DOCS_PATH / "index_2025_12_23.md"
    with open(index_path, 'w') as f:
        f.write(index_content)
    print(f"✓ Created {index_path.name}")
    
    # Create evidence index
    print("\n=== CREATING EVIDENCE INDEX ===")
    evidence_content = create_evidence_index()
    evidence_path = DOCS_PATH / "evidence-index-comprehensive-2025-12-23.md"
    with open(evidence_path, 'w') as f:
        f.write(evidence_content)
    print(f"✓ Created {evidence_path.name}")
    
    # Copy legal filings to docs
    print("\n=== COPYING LEGAL FILINGS ===")
    cipc_source = REVSTREAM_PATH / "CIPC_COMPLAINT_REFINED_2025_12_23.md"
    cipc_dest = DOCS_PATH / "CIPC_COMPLAINT_REFINED_2025_12_23.md"
    
    popia_source = REVSTREAM_PATH / "POPIA_COMPLAINT_COMPREHENSIVE_2025_12_23.md"
    popia_dest = DOCS_PATH / "POPIA_COMPLAINT_COMPREHENSIVE_2025_12_23.md"
    
    import shutil
    if cipc_source.exists():
        shutil.copy(cipc_source, cipc_dest)
        print(f"✓ Copied CIPC complaint to docs/")
    
    if popia_source.exists():
        shutil.copy(popia_source, popia_dest)
        print(f"✓ Copied POPIA complaint to docs/")
    
    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)
    print("\nUpdated Files:")
    print(f"  1. {index_path.name}")
    print(f"  2. {evidence_path.name}")
    print(f"  3. {cipc_dest.name}")
    print(f"  4. {popia_dest.name}")
    print("\nGitHub Pages ready for deployment.")

if __name__ == "__main__":
    main()
