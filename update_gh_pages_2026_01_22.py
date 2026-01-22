#!/usr/bin/env python3
"""
GitHub Pages Update Script - 2026-01-22
Updates GitHub Pages with organized evidence references for all 3 applications.
"""

import json
import os
from datetime import datetime

REVSTREAM_PATH = "/home/ubuntu/revstream1"
DOCS_PATH = f"{REVSTREAM_PATH}/docs"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def update_index_md(entities_data, events_data, relations_data, timeline_data):
    """Update the main index.md for GitHub Pages"""
    content = f"""# Revenue Stream Hijacking Case 2025-137857

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

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

- **Civil Claims** (50% burden) - ✅ EXCEEDED
- **Criminal Charges** (95% burden) - ✅ EXCEEDED
- **Financial Impact:** R10,269,727.90 + ZAR 18.75M trust control motive
- **Key Evidence:** JF01, JF03, JF07, JF08, SF9, Ketoni Timeline

### Application 2: CIPC & POPIA Complaints
**[View Full Application →](./application-2-cipc-popia.md)**

- **Companies Act Violations** - Director misconduct, financial fraud, fiduciary duty breach
- **POPIA Violations** - Data breaches, identity fraud
- **Key Evidence:** JF04, JF14, JF15, SF1, SF2, SF6, SF7

### Application 3: Commercial Crime & Tax Fraud
**[View Full Application →](./application-3-commercial-crime-tax-fraud.md)**

- **Commercial Crimes** - Fraud, theft, forgery, money laundering
- **Tax Fraud** - Income tax evasion, VAT fraud, SARS obstruction
- **Key Evidence:** JF03, SF1, SF3, SF4

---

## 📈 Evidence & Analysis

### Core Documentation
- **[Ketoni Payout Timeline](./ketoni-timeline.md)** - Central financial motive (ZAR 18.75M May 2026)
- **[Comprehensive Evidence Index](./evidence-index-enhanced.md)** - All evidence categorized and cross-referenced
- **[Master Timeline](./timeline.md)** - Complete chronological event sequence ({timeline_data['metadata']['total_entries']} entries)
- **[Entities Directory](./entities/index.md)** - All persons and organizations ({entities_data['metadata']['total_entities']} entities)
- **[Events Directory](./events/)** - Detailed event documentation ({events_data['metadata']['total_events']} events)
- **[Relations Analysis](./relations/index.md)** - Entity relationship mapping ({relations_data['metadata']['total_relations']} relations)

### Evidence Packages (JF Series)
- **JF01** - Shopify Plus email evidence (THE FORENSIC TIME CAPSULE)
- **JF02** - Business operations documentation
- **JF03** - Financial records and analysis
- **JF04** - CIPC company records
- **JF05** - Correspondence evidence
- **JF06** - Court documents and filings
- **JF07** - Financial transaction records
- **JF08** - Comprehensive fraud evidence package
- **JF09** - Timeline analysis and cross-reference
- **JF14/JF15** - CIPC historical records (2021)
- **JF16** - Distributor evidence

### Supporting Files (SF Series)
- **SF1** - Bantjies Debt Documentation (R1,048,000)
- **SF2** - Sage Screenshots - Rynette Control (2020-08-15)
- **SF3** - Strategic Logistics Stock Adjustment (R5.4M loss)
- **SF4** - SARS Audit Email (2021-03-15)
- **SF5** - Adderory Company Registration & Stock Supply
- **SF6** - Kayla Pretorius Estate Documentation (CRITICAL: Death 80 days after Ketoni investment)
- **SF7** - Court Order - Kayla Email Seizure
- **SF8** - Linda Employment Records
- **SF9** - Ian Levitt R63M Demand Letter (ignored)

---

## 📁 Legal Filings

### Latest Filings (2026-01-22) - Comprehensive Update
- **[CIPC Complaint (Refined)](./filings/CIPC_REFINED_2026_01_22.md)**
- **[POPIA Complaint (Refined)](./filings/POPIA_REFINED_2026_01_22.md)**
- **[NPA Tax Fraud Report (Refined)](./filings/NPA_REFINED_2026_01_22.md)**
- **[Commercial Crime Submission (Refined)](./filings/COMMERCIAL_CRIME_REFINED_2026_01_22.md)**

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

- **Entities:** {entities_data['metadata']['total_entities']} (persons, organizations, trusts, domains)
- **Events:** {events_data['metadata']['total_events']} documented events
- **Relations:** {relations_data['metadata']['total_relations']} mapped relationships
- **Timeline Entries:** {timeline_data['metadata']['total_entries']}
- **Evidence Files:** 1,151+ unique references in ad-res-j7

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
- **2023-04-24:** FFT invests in Ketoni - ZAR 18.75M entitlement established (T-37 months)
- **2023-07-13:** Kayla Pretorius death - 80 days after Ketoni investment (T-34 months)
- **2024-07:** Bantjies appointed FFT Trustee (T-10 months before payout)
- **2025-06-06:** Dan exposes Villa Via fraud to Bantjies (T-11 months)
- **2025-06-07:** Cards cancelled <24 hours after fraud exposure (T-11 months)
- **2025-08-11:** Main Trustee power backdated - Jax cooperation (T-9 months)
- **2025-08-13:** Interdict filed - Jax & Dan betrayal (T-9 months)
- **2026-05:** **Ketoni ZAR 18.75M payout due - ALL EVENTS CONVERGE HERE (T-0)**

---

*This documentation is continuously updated as new evidence is analyzed and legal filings are refined. All evidence references are cross-linked to the ad-res-j7 repository for verification and detailed examination.*

**Data Model Versions:**
- Entities: v{entities_data['metadata']['version']}
- Events: v{events_data['metadata']['version']}
- Relations: v{relations_data['metadata']['version']}
- Timeline: v{timeline_data['metadata']['version']}

**Last Refinement:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    filepath = f"{DOCS_PATH}/index.md"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated: {filepath}")

def update_filings_index():
    """Update the filings index.md"""
    content = f"""# Organized Legal Filings

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

This section contains all legal filings, organized by type and date.

---

## Latest Filings (2026-01-22)

| Filing | Type | Status |
|---|---|---|
| [CIPC Complaint](./CIPC_REFINED_2026_01_22.md) | Companies Act | ✅ Refined |
| [POPIA Complaint](./POPIA_REFINED_2026_01_22.md) | Data Protection | ✅ Refined |
| [NPA Tax Fraud Report](./NPA_REFINED_2026_01_22.md) | Tax Fraud | ✅ Refined |
| [Commercial Crime Submission](./COMMERCIAL_CRIME_REFINED_2026_01_22.md) | Commercial Crime | ✅ Refined |

---

## Civil/Criminal Actions

*   [Civil Action Summons](./civil_action_summons_REFINED_2026_01_18.md)
*   [Criminal Case Submission](./criminal_case_submission_REFINED_2026_01_18.md)

## CIPC/POPIA Complaints

*   [CIPC Companies Act Complaint (Latest)](./CIPC_REFINED_2026_01_22.md)
*   [POPIA Criminal Complaint (Latest)](./POPIA_REFINED_2026_01_22.md)

## Commercial Crime/Tax Fraud

*   [Commercial Crime Case Submission (Latest)](./COMMERCIAL_CRIME_REFINED_2026_01_22.md)
*   [NPA Tax Fraud Report (Latest)](./NPA_REFINED_2026_01_22.md)

---

## Historical Filings

### January 2026
- CIPC_REFINED_2026_01_18.md
- POPIA_REFINED_2026_01_18.md
- NPA_REFINED_2026_01_18.md

### Earlier Versions
- See archive for historical filings.
"""
    filepath = f"{DOCS_PATH}/filings/index.md"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated: {filepath}")

def update_application_pages():
    """Update the application-specific pages"""
    
    # Application 1: Civil & Criminal Actions
    app1_content = f"""# Application 1: Civil & Criminal Actions

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

---

## Overview

This application covers the civil claims and criminal charges arising from the revenue stream hijacking and trust violations.

## Burden of Proof Analysis

| Claim Type | Burden | Status |
|---|---|---|
| Civil Claims | 50% (Balance of Probabilities) | ✅ **EXCEEDED** |
| Criminal Charges | 95% (Beyond Reasonable Doubt) | ✅ **EXCEEDED** |

## Key Evidence

### Primary Evidence
- **JF01** - Shopify Plus email evidence (THE FORENSIC TIME CAPSULE)
- **JF03** - Financial records and analysis
- **JF07** - Financial transaction records
- **JF08** - Comprehensive fraud evidence package
- **SF9** - Ian Levitt R63M Demand Letter (ignored)

### Ketoni Evidence
- **Share Certificate J246** - FFT's 5,000 A-Ordinary shares in Ketoni
- **Ketoni Timeline** - All events converging on May 2026 payout

## Financial Impact

| Category | Amount |
|---|---|
| Revenue Stream Hijacking | R10,269,727.90 |
| Trust Control Motive | ZAR 18.75M |
| **Total** | **R29,019,727.90** |

## Related Filings

- [Civil Action Summons](./filings/civil_action_summons_REFINED_2026_01_18.md)
- [Criminal Case Submission](./filings/criminal_case_submission_REFINED_2026_01_18.md)

---

[← Back to Index](./index.md)
"""
    with open(f"{DOCS_PATH}/application-1-civil-criminal.md", 'w') as f:
        f.write(app1_content)
    print(f"Updated: {DOCS_PATH}/application-1-civil-criminal.md")

    # Application 2: CIPC & POPIA
    app2_content = f"""# Application 2: CIPC & POPIA Complaints

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

---

## Overview

This application covers the Companies Act violations and POPIA breaches by the implicated directors.

## Companies Act Violations

| Section | Description | Status |
|---|---|---|
| Section 22 | Reckless Trading | ✅ Documented |
| Section 76 | Director's Standard of Conduct | ✅ Documented |
| Section 77 | Liability of Directors | ✅ Documented |

## POPIA Violations

| Section | Description | Status |
|---|---|---|
| Section 86(1) | Unauthorized Access | ✅ Documented |
| Section 86(3) | Unauthorized Disclosure | ✅ Documented |

## Key Evidence

- **JF04** - CIPC company records
- **JF14/JF15** - CIPC historical records (2021)
- **SF1** - Bantjies Debt Documentation
- **SF2** - Sage Screenshots - Rynette Control
- **SF6** - Kayla Pretorius Estate Documentation
- **SF7** - Court Order - Kayla Email Seizure

## Related Filings

- [CIPC Complaint (Latest)](./filings/CIPC_REFINED_2026_01_22.md)
- [POPIA Complaint (Latest)](./filings/POPIA_REFINED_2026_01_22.md)

---

[← Back to Index](./index.md)
"""
    with open(f"{DOCS_PATH}/application-2-cipc-popia.md", 'w') as f:
        f.write(app2_content)
    print(f"Updated: {DOCS_PATH}/application-2-cipc-popia.md")

    # Application 3: Commercial Crime & Tax Fraud
    app3_content = f"""# Application 3: Commercial Crime & Tax Fraud

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

---

## Overview

This application covers the commercial crimes and tax fraud perpetrated by the implicated parties.

## Commercial Crimes

| Crime | Description | Status |
|---|---|---|
| Fraud | Misrepresentation with intent to deceive | ✅ Documented |
| Theft | Unlawful appropriation of funds | ✅ Documented |
| Forgery | Creation of false documents | ✅ Documented |
| Money Laundering | Concealment of proceeds of crime | ✅ Documented |

## Tax Fraud

| Type | Description | Status |
|---|---|---|
| Income Tax Evasion | Deliberate misrepresentation of income | ✅ Documented |
| VAT Fraud | Manipulation of VAT returns | ✅ Documented |
| SARS Obstruction | Obstruction of SARS audits | ✅ Documented |

## Key Evidence

- **JF03** - Financial records and analysis
- **SF1** - Bantjies Debt Documentation
- **SF3** - Strategic Logistics Stock Adjustment (R5.4M loss)
- **SF4** - SARS Audit Email (2021-03-15)

## Related Filings

- [Commercial Crime Submission (Latest)](./filings/COMMERCIAL_CRIME_REFINED_2026_01_22.md)
- [NPA Tax Fraud Report (Latest)](./filings/NPA_REFINED_2026_01_22.md)

---

[← Back to Index](./index.md)
"""
    with open(f"{DOCS_PATH}/application-3-commercial-crime-tax-fraud.md", 'w') as f:
        f.write(app3_content)
    print(f"Updated: {DOCS_PATH}/application-3-commercial-crime-tax-fraud.md")

def main():
    print("=" * 60)
    print("GitHub Pages Update - 2026-01-22")
    print("=" * 60)

    # Load data models
    entities_data = load_json(f"{REVSTREAM_PATH}/data_models/entities/entities.json")
    events_data = load_json(f"{REVSTREAM_PATH}/data_models/events/events.json")
    relations_data = load_json(f"{REVSTREAM_PATH}/data_models/relations/relations.json")
    timeline_data = load_json(f"{REVSTREAM_PATH}/data_models/timelines/timeline.json")

    print("\n[1/4] Updating main index.md...")
    update_index_md(entities_data, events_data, relations_data, timeline_data)

    print("\n[2/4] Updating filings index...")
    update_filings_index()

    print("\n[3/4] Updating application pages...")
    update_application_pages()

    print("\n[4/4] Complete!")

    print("\n" + "=" * 60)
    print("GitHub Pages Update Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
