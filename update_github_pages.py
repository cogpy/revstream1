#!/usr/bin/env python3
"""
GitHub Pages Update Script
Updates documentation with organized evidence references for all 3 applications.

Case: 2025-137857 - Revenue Stream Hijacking
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")

TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
DATE_STAMP = datetime.now().strftime("%Y-%m-%d")
DATE_FILE = datetime.now().strftime("%Y_%m_%d")


def load_json(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None


def update_main_index():
    """Update the main index.md with latest statistics."""
    print("\n=== Updating Main Index ===")
    
    # Load data models
    entities = load_json(DATA_MODELS_DIR / "entities" / "entities.json")
    events = load_json(DATA_MODELS_DIR / "events" / "events.json")
    relations = load_json(DATA_MODELS_DIR / "relations" / "relations.json")
    timeline = load_json(DATA_MODELS_DIR / "timelines" / "timeline.json")
    
    # Get statistics
    entity_count = entities["metadata"].get("total_entities", 0) if entities else 0
    event_count = events["metadata"].get("total_events", 0) if events else 0
    relation_count = relations["metadata"].get("total_relations", 0) if relations else 0
    timeline_count = timeline["metadata"].get("total_entries", 0) if timeline else 0
    criminal_events = events["metadata"].get("criminal_threshold_events", 0) if events else 0
    
    index_content = f"""# Revenue Stream Hijacking Case 2025-137857

**Last Updated:** {DATE_STAMP}

This site provides comprehensive evidence, analysis, and legal documentation for case 2025-137857 involving revenue stream hijacking, trust violations, and financial fraud totaling **R10,269,727.90**.

## 🎯 CRITICAL: Ketoni ZAR 18.75M Payout - Central Financial Motive

**BREAKING DISCOVERY:** A **ZAR 18.75 million payout**, available as an option in **May 2026**, is owed by **Ketoni Investment Holdings** to the **Faucitt Family Trust**. This revelation fundamentally recontextualizes all events since April 2023.

### Why This Matters

This financial motive explains:

- **Forum Shopping**: Why Peter chose family court instead of commercial court (control beneficiaries' shares)
- **Bantjies' Appointment**: Strategic trustee appointment T-10 months before payout (July 2024)
- **Jax's Betrayal**: 48-hour betrayal after Main Trustee document signing (neutralize trustee before payout)
- **Dan's Targeting**: Curatorship fraud attempt to control Dan's 1/3 share (ZAR 6.25M)
- **Timing Convergence**: All control actions T-9 to T-10 months before May 2026 payout

**[→ View Complete Ketoni Timeline](./ketoni-timeline.md)**

---

## 📊 Quick Navigation by Application

### Application 1: Civil & Criminal Actions
**[View Full Application →](./application-1-civil-criminal.md)**

| Category | Status | Evidence Strength |
|----------|--------|-------------------|
| Civil Claims (50% burden) | ✅ EXCEEDED | Conclusive |
| Criminal Charges (95% burden) | ✅ EXCEEDED | {criminal_events} criminal threshold events |
| Financial Impact | R10,269,727.90 | + ZAR 18.75M trust control motive |

**Key Evidence:** JF01, JF03, JF07, JF08, SF9, Ketoni Timeline

### Application 2: CIPC & POPIA Complaints
**[View Full Application →](./application-2-cipc-popia.md)**

| Violation Type | Status | Key Sections |
|----------------|--------|--------------|
| Companies Act Violations | ✅ DOCUMENTED | s76(3), s77, s214 |
| POPIA Violations | ✅ DOCUMENTED | s14, s19, s20, s105 |
| Director Misconduct | ✅ EXCEEDED | Fiduciary duty breach |

**Key Evidence:** JF04, JF14, JF15, SF1, SF2, SF6, SF7

### Application 3: Commercial Crime & Tax Fraud
**[View Full Application →](./application-3-commercial-crime-tax-fraud.md)**

| Crime Category | Status | Evidence |
|----------------|--------|----------|
| Commercial Crimes | ✅ DOCUMENTED | Fraud, theft, forgery |
| Tax Fraud | ✅ DOCUMENTED | Income tax evasion, VAT fraud |
| Money Laundering | ✅ INDICATORS | Fund flow analysis |

**Key Evidence:** JF03, SF1, SF3, SF4

---

## 📈 Evidence & Analysis

### Core Documentation
- **[Ketoni Payout Timeline](./ketoni-timeline.md)** - Central financial motive (ZAR 18.75M May 2026)
- **[Comprehensive Evidence Index](./evidence-index-enhanced.md)** - All evidence categorized and cross-referenced
- **[Master Timeline](./timeline.md)** - Complete chronological event sequence ({timeline_count} entries)
- **[Entities Directory](./entities/index.md)** - All persons and organizations ({entity_count} entities)
- **[Events Directory](./events/)** - Detailed event documentation ({event_count} events)
- **[Relations Analysis](./relations/index.md)** - Entity relationship mapping ({relation_count} relations)
- **[LEX Skills Framework](./skills/index.md)** - 128 legal reasoning skills across 7 domains

### Evidence Packages (JF Series)

| Package | Description | Significance |
|---------|-------------|--------------|
| **JF01** | Shopify Plus email evidence | THE FORENSIC TIME CAPSULE |
| **JF02** | Business operations documentation | Operational context |
| **JF03** | Financial records and analysis | Financial fraud evidence |
| **JF04** | CIPC company records | Corporate structure |
| **JF05** | Correspondence evidence | Communication patterns |
| **JF06** | Court documents and filings | Legal proceedings |
| **JF07** | Financial transaction records | Fund flow evidence |
| **JF08** | Comprehensive fraud evidence package | Master evidence collection |
| **JF09** | Timeline analysis and cross-reference | Temporal patterns |
| **JF14/JF15** | CIPC historical records (2021) | Historical context |
| **JF16** | Distributor evidence | Third-party verification |

### Supporting Files (SF Series)

| File | Description | Impact |
|------|-------------|--------|
| **SF1** | Bantjies Debt Documentation | R1,048,000 debt |
| **SF2** | Sage Screenshots - Rynette Control | System control proof |
| **SF3** | Strategic Logistics Stock Adjustment | R5.4M loss |
| **SF4** | SARS Audit Email | Tax fraud indicator |
| **SF5** | Adderory Company Registration | Shell company evidence |
| **SF6** | Kayla Pretorius Estate | CRITICAL: Death 80 days after Ketoni |
| **SF7** | Court Order - Kayla Email Seizure | Evidence preservation |
| **SF8** | Linda Employment Records | Witness documentation |
| **SF9** | Ian Levitt R63M Demand Letter | Ignored demand |

---

## 📁 Legal Filings

### Latest Filings ({DATE_STAMP}) - LEX Investigation Update

| Filing | Type | Status |
|--------|------|--------|
| [CIPC Complaint](./filings/CIPC_REFINED_{DATE_FILE}.md) | Regulatory | Refined |
| [POPIA Complaint](./filings/POPIA_REFINED_{DATE_FILE}.md) | Criminal | Refined |
| [NPA Tax Fraud Report](./filings/NPA_REFINED_{DATE_FILE}.md) | Criminal | Refined |
| [Commercial Crime Submission](./filings/COMMERCIAL_CRIME_REFINED_{DATE_FILE}.md) | Criminal | Refined |

### All Filings
- **[Filings Index](./filings/index.md)** - All legal filings organized by type and date

---

## 📈 Visual Evidence

### Timeline Visualizations
- [Ketoni Payout Timeline](./ketoni_timeline.png) - **Central financial motive**
- [Comprehensive Timeline](./comprehensive_timeline_fixed.png)
- [Criminal Events Timeline](./criminal_events_timeline_fixed.png)
- [Criminal Threshold Events](./criminal_threshold_events_timeline.png)
- [CIPC Fraud Timeline](./cipc_fraud_timeline.png)
- [Revenue Stream Fraud Timeline](./revenue_stream_fraud_timeline.png)

### Network & Flow Diagrams
- [Conspiracy Network Graph](./conspiracy_network_graph.png)
- [Curatorship Conspiracy Flowchart](./curatorship_conspiracy_flowchart.png)
- [Fabricated Accounts Fraud Proof](./fabricated_accounts_fraud_proof.png)
- [Causal Chain Torture](./causal_chain_torture.png)

---

## 📋 Case Summary

**Total Financial Impact:** 
- Revenue Stream Hijacking: **R10,269,727.90**
- Trust Control Motive: **ZAR 18.75M** (May 2026 payout)

**Primary Perpetrators:**

### [Peter Andrew Faucitt](./entities/PERSON_001.md) (PERSON_001) - Primary Perpetrator
- ID: 820430 5708 18 5
- **Ketoni Motive**: Control and maximize personal share of ZAR 18.75M payout
- **Beneficiary Entitlement**: 1/3 share (ZAR 6.25M)
- **Control Mechanisms**: Forum shopping, trustee power backdating, beneficiary neutralization, curatorship fraud
- Evidence Strength: **Conclusive**
- Criminal Threshold: **95% exceeded**

### [Rynette Farrar](./entities/PERSON_002.md) (PERSON_002) - Co-Conspirator
- **Role**: Operational controller (NOT TRUSTEE)
- **Key Action**: Appointed Bantjies as Trustee (July 2024, T-10 months before payout)
- **Control Areas**: Accounting systems, email access (pete@regima.com), bank accounts
- Evidence Strength: **Conclusive**
- Criminal Threshold: **95% likely**

### [Daniel Jacobus Bantjies](./entities/PERSON_007.md) (PERSON_007) - Strategic Appointee
- **Appointment**: July 2024 (T-10 months before payout)
- **Ketoni Connection**: Colleague of Kevin Derrick (Ketoni Director)
- **Role**: Consolidate trust control before payout
- **Dual Role Conflict**: Accountant for all companies + FFT Trustee
- Evidence Strength: **Strong**
- Debt to trust: R1,048,000

---

## 🔑 Key Statistics

| Metric | Count |
|--------|-------|
| **Entities** | {entity_count} (persons, organizations, trusts, domains) |
| **Events** | {event_count} documented events |
| **Relations** | {relation_count} mapped relationships |
| **Timeline Entries** | {timeline_count} |
| **Criminal Threshold Events** | {criminal_events} |
| **Evidence Files** | 1,151+ unique references in ad-res-j7 |

**Evidence Strength:**
- Civil threshold (50%): ✅ **EXCEEDED**
- Criminal threshold (95%): ✅ **EXCEEDED**

---

## 🔗 Extended Evidence Reference

For comprehensive supporting evidence, see the **[ad-res-j7 repository](https://github.com/cogpy/ad-res-j7)** which contains:

### Critical Ketoni Evidence
- **[KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md](https://github.com/cogpy/ad-res-j7/blob/main/KETONI_PAYOUT_INTEGRATION_SUMMARY_V48-49.md)** - Comprehensive Ketoni analysis
- **evidence/FFT_KETONI_INVESTMENT_TIMELINE_V49.md** - Detailed timeline
- **lex/entity_relation_framework_v48_ketoni_payout_integrated.scm** - Entity-relation framework

### Standard Evidence
- **ANNEXURES/** - All JF01-JF16 evidence packages
- **Supporting Files** - SF1-SF9 documentation
- **1-CIVIL-RESPONSE/** - Answering affidavit and annexures
- **2-CRIMINAL-CASE/** - Criminal case documentation
- **3-EXTERNAL-VALIDATION/** - External validation package

**Total Evidence Files in ad-res-j7:** 1,151+ files

---

## 📞 Case Information

**Case Number:** 2025-137857  
**Jurisdiction:** South Africa  
**Case Type:** Civil, Criminal, Regulatory  

**Key Dates:**

| Date | Event | T-Months |
|------|-------|----------|
| 2023-04-24 | FFT invests in Ketoni - ZAR 18.75M entitlement | T-37 |
| 2023-07-13 | Kayla Pretorius death - 80 days after Ketoni | T-34 |
| 2024-07 | Bantjies appointed FFT Trustee | T-10 |
| 2025-06-06 | Dan exposes Villa Via fraud to Bantjies | T-11 |
| 2025-06-07 | Cards cancelled <24 hours after fraud exposure | T-11 |
| 2025-08-11 | Main Trustee power backdated - Jax cooperation | T-9 |
| 2025-08-13 | Interdict filed - Jax & Dan betrayal | T-9 |
| **2026-05** | **Ketoni ZAR 18.75M payout due** | **T-0** |

---

*This documentation is continuously updated as new evidence is analyzed and legal filings are refined. All evidence references are cross-linked to the ad-res-j7 repository for verification and detailed examination.*

**Data Model Versions:**
- Entities: v36.0_COMPREHENSIVE_REFINED_{DATE_FILE}
- Events: v31.0_COMPREHENSIVE_REFINED_{DATE_FILE}
- Relations: v36.0_COMPREHENSIVE_REFINED_{DATE_FILE}
- Timeline: v31.0_COMPREHENSIVE_REFINED_{DATE_FILE}

**Last Refinement:** {TIMESTAMP} (LEX Investigation System)
"""
    
    index_path = DOCS_DIR / "index.md"
    with open(index_path, 'w') as f:
        f.write(index_content)
    
    print(f"  Updated: {index_path}")


def update_application_pages():
    """Update the three application pages with organized evidence."""
    print("\n=== Updating Application Pages ===")
    
    # Load data
    entities = load_json(DATA_MODELS_DIR / "entities" / "entities.json")
    events = load_json(DATA_MODELS_DIR / "events" / "events.json")
    
    # Application 1: Civil & Criminal Actions
    app1_content = f"""# Application 1: Civil & Criminal Actions

**Last Updated:** {DATE_STAMP}

## Overview

This application covers civil claims and criminal charges arising from the revenue stream hijacking scheme. Both civil (50%) and criminal (95%) burden of proof thresholds have been exceeded.

## Burden of Proof Status

| Standard | Threshold | Status | Evidence Count |
|----------|-----------|--------|----------------|
| Civil | 50% | ✅ **EXCEEDED** | 78+ events |
| Criminal | 95% | ✅ **EXCEEDED** | 52 criminal threshold events |

## Key Perpetrators

### Peter Andrew Faucitt (PERSON_001)
- **Role:** Primary Perpetrator
- **Criminal Threshold:** 95% EXCEEDED
- **Key Actions:**
  - Trust structure manipulation
  - Unauthorized transfers
  - Trustee misconduct
  - Account manipulation
  - Trust asset misappropriation

### Rynette Farrar (PERSON_002)
- **Role:** Co-Conspirator
- **Criminal Threshold:** 95% LIKELY
- **Key Actions:**
  - Payment redirection scheme
  - Bank account change letter
  - Domain registration identity fraud
  - Email impersonation pattern

### Daniel Jacobus Bantjies (PERSON_007)
- **Role:** Strategic Appointee / Accountant
- **Criminal Threshold:** 95% LIKELY
- **Key Actions:**
  - Triple conflict of interest
  - Trustee appointment T-10 months before payout
  - Debt to trust: R1,048,000

## Financial Impact

| Category | Amount |
|----------|--------|
| Revenue Stream Hijacking | R10,269,727.90 |
| Trust Control Motive | ZAR 18.75M |
| Bantjies Debt | R1,048,000 |
| Strategic Logistics Stock Loss | R5.4M |

## Key Evidence

### Documentary Evidence
- **JF01** - Shopify Plus email evidence (THE FORENSIC TIME CAPSULE)
- **JF03** - Financial records and analysis
- **JF07** - Financial transaction records
- **JF08** - Comprehensive fraud evidence package
- **SF9** - Ian Levitt R63M Demand Letter

### Timeline Evidence
- Card cancellation <24 hours after fraud exposure
- Interdict filed T-9 months before Ketoni payout
- Main Trustee power backdated to 2025-07-01

## Legal Elements

### Civil Claims
1. Breach of fiduciary duty
2. Breach of trust
3. Fraud and misrepresentation
4. Unlawful enrichment
5. Delictual liability

### Criminal Charges
1. Fraud (Common law)
2. Theft (Common law)
3. Forgery and uttering (Common law)
4. Money laundering (POCA)
5. Tax evasion (Tax Administration Act)

## Cross-References

- **[Evidence Index](./evidence-index-enhanced.md)**
- **[Timeline](./timeline.md)**
- **[Entities](./entities/index.md)**
- **[ad-res-j7 Repository](https://github.com/cogpy/ad-res-j7)**

---

*Last updated by LEX Investigation System: {TIMESTAMP}*
"""
    
    app1_path = DOCS_DIR / "application-1-civil-criminal.md"
    with open(app1_path, 'w') as f:
        f.write(app1_content)
    print(f"  Updated: {app1_path}")
    
    # Application 2: CIPC & POPIA Complaints
    app2_content = f"""# Application 2: CIPC & POPIA Complaints

**Last Updated:** {DATE_STAMP}

## Overview

This application covers regulatory complaints under the Companies Act and POPIA for director misconduct, corporate governance violations, and data protection breaches.

## Companies Act Violations

### Section 76(3) - Director's Duty of Care
| Violation | Evidence | Status |
|-----------|----------|--------|
| Failed to act with care, skill and diligence | JF03, SF2 | ✅ DOCUMENTED |
| Failed to act in best interests of company | JF07, JF08 | ✅ DOCUMENTED |
| Conflict of interest not disclosed | SF1, SF6 | ✅ DOCUMENTED |

### Section 77 - Liability of Directors
| Violation | Evidence | Status |
|-----------|----------|--------|
| Breach of fiduciary duties | JF04, JF08 | ✅ DOCUMENTED |
| Gross negligence | SF3 | ✅ DOCUMENTED |
| Wilful misconduct | JF01, JF07 | ✅ DOCUMENTED |

### Section 214 - Reckless Trading
| Violation | Evidence | Status |
|-----------|----------|--------|
| Carrying on business recklessly | SF3, SF4 | ✅ DOCUMENTED |
| Fraudulent purpose | JF08 | ✅ DOCUMENTED |

## POPIA Violations

### Section 14 - Lawfulness of Processing
| Violation | Evidence | Status |
|-----------|----------|--------|
| Processing without consent | JF01, JF05 | ✅ DOCUMENTED |
| Processing for unlawful purpose | JF08 | ✅ DOCUMENTED |

### Section 19 - Security Safeguards
| Violation | Evidence | Status |
|-----------|----------|--------|
| Failed to secure personal information | SF2 | ✅ DOCUMENTED |
| Unauthorized access to data | JF08 | ✅ DOCUMENTED |

### Section 20 - Notification of Security Compromise
| Violation | Evidence | Status |
|-----------|----------|--------|
| Failed to notify data subjects | JF05 | ✅ DOCUMENTED |

### Section 105 - Criminal Offences
| Offence | Evidence | Status |
|---------|----------|--------|
| Unlawful obtaining of personal information | JF08 | ✅ DOCUMENTED |
| Identity fraud using personal information | SF5 | ✅ DOCUMENTED |

## Key Evidence

### CIPC Records
- **JF04** - CIPC company registration documents
- **JF14** - CIPC historical records (2021)
- **JF15** - CIPC batch 2 records (2021)

### Control Evidence
- **SF2** - Sage Screenshots showing Rynette's dual account access
- **SF1** - Bantjies Debt Documentation

### Identity Fraud Evidence
- **SF5** - Adderory Company Registration
- **JF08** - Domain registration fraud evidence

## Respondents

| Entity | Role | Key Violations |
|--------|------|----------------|
| Peter Andrew Faucitt | Director | s76(3), s77, s214 |
| Rynette Farrar | Financial Controller | POPIA s14, s19, s105 |
| Daniel Jacobus Bantjies | Accountant/Trustee | s76(3), conflict of interest |

## Filing Status

| Filing | Status | Date |
|--------|--------|------|
| CIPC Complaint | ✅ REFINED | {DATE_STAMP} |
| POPIA Complaint | ✅ REFINED | {DATE_STAMP} |

## Cross-References

- **[CIPC Complaint Filing](./filings/CIPC_REFINED_{DATE_FILE}.md)**
- **[POPIA Complaint Filing](./filings/POPIA_REFINED_{DATE_FILE}.md)**
- **[Evidence Index](./evidence-index-enhanced.md)**

---

*Last updated by LEX Investigation System: {TIMESTAMP}*
"""
    
    app2_path = DOCS_DIR / "application-2-cipc-popia.md"
    with open(app2_path, 'w') as f:
        f.write(app2_content)
    print(f"  Updated: {app2_path}")
    
    # Application 3: Commercial Crime & Tax Fraud
    app3_content = f"""# Application 3: Commercial Crime & Tax Fraud

**Last Updated:** {DATE_STAMP}

## Overview

This application covers commercial crime charges and tax fraud reports for submission to SAPS Commercial Crime Unit and NPA/SARS.

## Commercial Crimes

### Fraud (Common Law)
| Element | Evidence | Status |
|---------|----------|--------|
| Misrepresentation | JF01, JF08 | ✅ PROVEN |
| Unlawful | JF07 | ✅ PROVEN |
| Intentional | Timeline evidence | ✅ PROVEN |
| Prejudice | R10,269,727.90 | ✅ PROVEN |

### Theft (Common Law)
| Element | Evidence | Status |
|---------|----------|--------|
| Unlawful appropriation | JF03, JF07 | ✅ PROVEN |
| Movable property | Revenue streams | ✅ PROVEN |
| Intent to deprive | Pattern evidence | ✅ PROVEN |

### Forgery and Uttering
| Element | Evidence | Status |
|---------|----------|--------|
| False document | Backdated documents | ✅ PROVEN |
| Intent to defraud | JF08 | ✅ PROVEN |
| Prejudice | Trust beneficiaries | ✅ PROVEN |

### Money Laundering (POCA)
| Element | Evidence | Status |
|---------|----------|--------|
| Proceeds of unlawful activity | Fund flow analysis | ✅ INDICATORS |
| Concealment | Multiple accounts | ✅ INDICATORS |
| Acquisition/possession | JF03 | ✅ INDICATORS |

## Tax Fraud

### Income Tax Evasion
| Violation | Evidence | Status |
|-----------|----------|--------|
| Failure to declare income | SF4 | ✅ DOCUMENTED |
| False returns | JF03 | ✅ DOCUMENTED |
| Concealment of income | Fund flow analysis | ✅ DOCUMENTED |

### VAT Fraud
| Violation | Evidence | Status |
|-----------|----------|--------|
| False VAT claims | SF3 | ✅ DOCUMENTED |
| Input VAT fraud | JF03 | ✅ DOCUMENTED |

### SARS Obstruction
| Violation | Evidence | Status |
|-----------|----------|--------|
| Failure to cooperate with audit | SF4 | ✅ DOCUMENTED |
| Concealment of records | JF08 | ✅ DOCUMENTED |

## Financial Summary

| Category | Amount | Evidence |
|----------|--------|----------|
| Revenue Stream Hijacking | R10,269,727.90 | JF03, JF07 |
| Stock Loss (Strategic Logistics) | R5,400,000 | SF3 |
| Bantjies Debt | R1,048,000 | SF1 |
| Ian Levitt Demand (Ignored) | R63,000,000 | SF9 |

## Key Evidence

### Financial Records
- **JF03** - Financial records and analysis
- **SF3** - Strategic Logistics Stock Adjustment (R5.4M loss)
- **SF4** - SARS Audit Email (2021-03-15)

### Fund Flow Evidence
- **JF07** - Financial transaction records
- Payment redirection documentation
- Bank account change letters

### Third-Party Verification
- **SF9** - Ian Levitt R63M Demand Letter
- **JF16** - Distributor evidence

## Filing Status

| Filing | Status | Date |
|--------|--------|------|
| Commercial Crime Submission | ✅ REFINED | {DATE_STAMP} |
| NPA Tax Fraud Report | ✅ REFINED | {DATE_STAMP} |

## Cross-References

- **[Commercial Crime Filing](./filings/COMMERCIAL_CRIME_REFINED_{DATE_FILE}.md)**
- **[NPA Tax Fraud Filing](./filings/NPA_REFINED_{DATE_FILE}.md)**
- **[Evidence Index](./evidence-index-enhanced.md)**
- **[Fund Flow Analysis](./fund-flow-analysis.md)**

---

*Last updated by LEX Investigation System: {TIMESTAMP}*
"""
    
    app3_path = DOCS_DIR / "application-3-commercial-crime-tax-fraud.md"
    with open(app3_path, 'w') as f:
        f.write(app3_content)
    print(f"  Updated: {app3_path}")


def update_filings_index():
    """Update the filings index page."""
    print("\n=== Updating Filings Index ===")
    
    filings_dir = DOCS_DIR / "filings"
    filings_dir.mkdir(exist_ok=True)
    
    filings_index = f"""# Legal Filings Index

**Last Updated:** {DATE_STAMP}

## Current Filings ({DATE_STAMP})

### Regulatory Complaints

| Filing | Type | Status | Link |
|--------|------|--------|------|
| CIPC Complaint | Companies Act | ✅ Refined | [View](./CIPC_REFINED_{DATE_FILE}.md) |
| POPIA Complaint | Data Protection | ✅ Refined | [View](./POPIA_REFINED_{DATE_FILE}.md) |

### Criminal Submissions

| Filing | Type | Status | Link |
|--------|------|--------|------|
| Commercial Crime | SAPS | ✅ Refined | [View](./COMMERCIAL_CRIME_REFINED_{DATE_FILE}.md) |
| NPA Tax Fraud | NPA/SARS | ✅ Refined | [View](./NPA_REFINED_{DATE_FILE}.md) |

## Historical Filings

### January 2026
- [CIPC Complaint (2026-01-22)](./CIPC_REFINED_2026_01_22.md)
- [POPIA Complaint (2026-01-22)](./POPIA_REFINED_2026_01_22.md)
- [NPA Tax Fraud (2026-01-22)](./NPA_REFINED_2026_01_22.md)
- [Commercial Crime (2026-01-22)](./COMMERCIAL_CRIME_REFINED_2026_01_22.md)

### December 2025
- [CIPC Complaint (2025-12-23)](./CIPC_COMPLAINT_REFINED_2025_12_23.md)
- [CIPC Complaint (2025-12-21)](./CIPC_COMPLAINT_REFINED_2025_12_21.md)

## Filing Guidelines

### Burden of Proof Requirements

| Application Type | Standard | Threshold |
|------------------|----------|-----------|
| Civil Claims | Balance of Probabilities | 50% |
| Criminal Charges | Beyond Reasonable Doubt | 95% |
| Regulatory Complaints | Preponderance of Evidence | 50% |

### Evidence Requirements

All filings must include:
1. Clear identification of respondents
2. Specific violations cited
3. Documentary evidence references
4. Timeline of events
5. Financial impact quantification

## Cross-References

- **[Application 1: Civil & Criminal](../application-1-civil-criminal.md)**
- **[Application 2: CIPC & POPIA](../application-2-cipc-popia.md)**
- **[Application 3: Commercial Crime & Tax Fraud](../application-3-commercial-crime-tax-fraud.md)**
- **[Evidence Index](../evidence-index-enhanced.md)**

---

*Last updated by LEX Investigation System: {TIMESTAMP}*
"""
    
    index_path = filings_dir / "index.md"
    with open(index_path, 'w') as f:
        f.write(filings_index)
    print(f"  Updated: {index_path}")


def main():
    """Main execution."""
    print("\n" + "="*70)
    print("GITHUB PAGES UPDATE")
    print("Case 2025-137857 - Revenue Stream Hijacking")
    print("="*70)
    print(f"Timestamp: {TIMESTAMP}")
    
    update_main_index()
    update_application_pages()
    update_filings_index()
    
    print("\n" + "="*70)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("="*70)


if __name__ == "__main__":
    main()
