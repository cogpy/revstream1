# Revenue Stream Hijacking: Case 2025-137857 Analysis

**Last Updated:** 2026-01-05

## Executive Summary

This repository provides a comprehensive, evidence-based analysis of the coordinated scheme to hijack the revenue stream of RegimA Zone Ltd (UK) and defraud the Faucitt Family Trust. The perpetrators, primarily **Peter Andrew Faucitt**, **Rynette Farrar**, and **Danie Bantjies**, executed a multi-faceted attack involving financial manipulation, identity fraud, trust violations, and evidence tampering.

**Key Statistics:**
- **Total Events Documented:** 77
- **Criminal Threshold Events (95% burden of proof):** 46
- **Civil Threshold Events (50% burden of proof):** 31
- **Entities Tracked:** 33
- **Relations Mapped:** 75
- **Timeline Span:** 2017-02-24 to 2025-10-23

---

## I. Core Data Models (Refined)

The investigation is built upon a rigorously maintained set of data models that define the entities, their relationships, and the sequence of events. These models are continuously refined as new evidence emerges.

| Data Model | Version | Last Updated | Description | Link |
| :--- | :--- | :--- | :--- | :--- |
| **Entities** | 22.1_REFINED_2026_01_05 | 2026-01-05 | Detailed profiles of all individuals, organizations, and assets involved. | [entities.json](../data_models/entities/entities.json) |
| **Relations** | 18.1_REFINED_2026_01_05 | 2026-01-05 | A hypergraph-compatible model of the connections and interactions between entities. | [relations.json](../data_models/relations/relations.json) |
| **Events** | 21.1_REFINED_2026_01_05 | 2026-01-05 | A catalog of all significant events, with 46 events meeting the 95% criminal burden of proof. | [events.json](../data_models/events/events.json) |
| **Timeline** | 18.1_ENHANCED_2026_01_05 | 2026-01-05 | A chronologically ordered timeline of events, enhanced with criminal threshold markers. | [timeline.json](../data_models/timelines/timeline.json) |

---

## II. Evidence Index & Cross-Reference

The evidence is sourced from two primary repositories:
- **revstream1** (this repository): Analysis, data models, and visualizations
- **ad-res-j7** (extended evidence): Primary source documents, annexures, and legal filings

### Key Evidence Directories in ad-res-j7

| Evidence Set | Description | File Count | Location |
| :--- | :--- | :--- | :--- |
| **ANNEXURES/JF01** | Shopify Plus email - THE FORENSIC TIME CAPSULE | 2 items | [ad-res-j7/ANNEXURES/JF01](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF01) |
| **ANNEXURES/JF02** | Business operations documentation | 3 items | [ad-res-j7/ANNEXURES/JF02](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF02) |
| **ANNEXURES/JF03** | Financial records and analysis | 5 items | [ad-res-j7/ANNEXURES/JF03](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF03) |
| **ANNEXURES/JF04** | CIPC company registration documents | 6 items | [ad-res-j7/ANNEXURES/JF04](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF04) |
| **ANNEXURES/JF05** | Correspondence evidence | 7 items | [ad-res-j7/ANNEXURES/JF05](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF05) |
| **ANNEXURES/JF06** | Court applications and filings | 5 items | [ad-res-j7/ANNEXURES/JF06](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF06) |
| **ANNEXURES/JF07** | Payment redirection documentation | 186 items | [ad-res-j7/ANNEXURES/JF07](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF07) |
| **ANNEXURES/JF08** | Evidence Package - Comprehensive fraud timeline | 43 items | [ad-res-j7/ANNEXURES/JF08](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF08) |
| **ANNEXURES/JF09** | Domain registration fraud evidence | 8 items | [ad-res-j7/ANNEXURES/JF09](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF09) |

### Special Findings (SF) Evidence

| Evidence ID | Description | Significance | Burden of Proof | Location |
| :--- | :--- | :--- | :--- | :--- |
| **SF1** | Bantjies Debt Documentation | Establishes Danie Bantjies' R18.685M debt and conflict of interest. | Civil (50%) & Criminal (95%) | [SF1_Bantjies_Debt_Documentation.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md) |
| **SF2** | Rynette Sage Control | Proves Rynette's control of the accounting system and Pete's email. | Criminal (95%) | [SF2_Sage_Screenshots_Rynette_Control.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md) |
| **SF3** | Strategic Logistics Stock Adjustment | Documents R5.4M stock fraud concealment. | Criminal (95%) | [SF3_Strategic_Logistics_Stock_Adjustment.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md) |
| **SF4** | SARS Audit Email | Evidence of tax fraud coordination. | Criminal (95%) | [SF4_SARS_Audit_Email.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF4_SARS_Audit_Email.md) |
| **SF5** | Adderory Company Registration | Identity fraud and stock supply manipulation. | Criminal (95%) | [SF5_Adderory_Company_Registration_Stock_Supply.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md) |
| **SF6** | Kayla Pretorius Estate | **CRITICAL:** Death of Kayla triggered estate exploitation. | Civil (50%) & Criminal (95%) | [SF6_Kayla_Pretorius_Estate_Documentation.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md) |
| **SF7** | Court Order Kayla Email Seizure | Email seizure order evidence. | Civil (50%) | [SF7_Court_Order_Kayla_Email_Seizure.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md) |
| **SF8** | Linda Employment Records | Employment documentation for bookkeeper. | Moderate | [SF8_Linda_Employment_Records.md](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF8_Linda_Employment_Records.md) |
| **SF9** | Ian Levitt Attorney Memo | Attorney memo documenting case issues and timeline. | Strong | [IanLevittAttorneysMemo_2025-11-09.txt](https://github.com/cogpy/ad-res-j7/blob/main/archive/legal-analysis-nov2025/attorney_correspondence/IanLevittAttorneysMemo_2025-11-09.txt) |

---

## III. Three Legal Applications

This evidence supports three distinct legal applications, each with specific evidence requirements and burden of proof standards.

### Application 1: Civil Response (1-CIVIL-RESPONSE)

**Purpose:** Answering affidavit in response to Peter Faucitt's interdict application (Case 2025-137857)

**Burden of Proof:** Balance of probabilities (50%)

**Key Evidence:**
- All JF annexures (JF01-JF09)
- All SF evidence (SF1-SF9)
- Comprehensive timeline of events
- Financial impact analysis

**Status:** Evidence organized and indexed  
**Location:** [ad-res-j7/1-CIVIL-RESPONSE](https://github.com/cogpy/ad-res-j7/tree/main/1-CIVIL-RESPONSE)

### Application 2: Criminal Case (2-CRIMINAL-CASE)

**Purpose:** Criminal complaints for fraud, theft, POPIA violations, and Companies Act violations

**Burden of Proof:** Beyond reasonable doubt (95%)

**Key Evidence Focus:**
- 46 events meeting criminal threshold
- SF1 (Bantjies debt/conflict), SF2 (Rynette control), SF3 (stock fraud)
- SF4 (tax fraud), SF5 (identity fraud), SF6 (estate exploitation)
- JF07 (payment redirection), JF08 (comprehensive fraud timeline)

**Status:** Evidence refined and categorized  
**Location:** [ad-res-j7/2-CRIMINAL-CASE](https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE)

### Application 3: External Validation (3-EXTERNAL-VALIDATION)

**Purpose:** Independent verification and external expert review package

**Burden of Proof:** Professional standards (varies by discipline)

**Key Evidence:**
- Complete data models (entities, relations, events, timeline)
- All visualizations and timelines
- Cross-referenced evidence catalog
- Methodology documentation

**Status:** Comprehensive package prepared  
**Location:** [ad-res-j7/3-EXTERNAL-VALIDATION](https://github.com/cogpy/ad-res-j7/tree/main/3-EXTERNAL-VALIDATION)

---

## IV. Visualizations

Visualizations provide an intuitive understanding of the complex timelines and networks of conspiracy.

### Timelines

| Visualization | Description | Link |
| :--- | :--- | :--- |
| **Comprehensive Timeline** | Full timeline of all events (2017-2025) | [comprehensive_timeline.png](comprehensive_timeline.png) |
| **Criminal Events Timeline** | Highlights events meeting the criminal burden of proof | [criminal_events_timeline_fixed.png](criminal_events_timeline_fixed.png) |
| **Criminal Threshold Events** | Detailed view of 95% threshold events | [criminal_threshold_events_timeline.png](criminal_threshold_events_timeline.png) |
| **Card Cancellation Timeline** | Timeline of card cancellations and financial control | [card_cancellation_timeline.png](card_cancellation_timeline.png) |
| **Revenue Stream Fraud Timeline** | Specific timeline of revenue hijacking events | [revenue_stream_fraud_timeline.png](revenue_stream_fraud_timeline.png) |
| **CIPC Fraud Timeline** | Timeline of Companies Act violations | [cipc_fraud_timeline.png](cipc_fraud_timeline.png) |
| **Curatorship Conspiracy Timeline** | Timeline of suspected curatorship fraud plot | [curatorship_conspiracy_timeline.mmd](curatorship_conspiracy_timeline.mmd) |

### Network Graphs & Flowcharts

| Visualization | Description | Link |
| :--- | :--- | :--- |
| **Conspiracy Network Graph** | Maps the relationships and coordination between the primary perpetrators | [conspiracy_network_graph.png](conspiracy_network_graph.png) |
| **Curatorship Conspiracy Flowchart** | Illustrates the suspected plot to commit curatorship fraud | [curatorship_conspiracy_flowchart.png](curatorship_conspiracy_flowchart.png) |
| **Fabricated Accounts Fraud Proof** | Flowchart showing evidence of fabricated financial accounts | [fabricated_accounts_fraud_proof.png](fabricated_accounts_fraud_proof.png) |
| **Causal Chain - Torture** | Causal chain analysis of psychological harm | [causal_chain_torture.png](causal_chain_torture.png) |

---

## V. Legal Filings (Latest Versions)

This section contains the most recently refined legal filings based on the comprehensive body of evidence.

| Filing | Version | Last Updated | Link |
| :--- | :--- | :--- | :--- |
| **CIPC Companies Act Complaint** | 2026-01-03 | 2026-01-03 | [CIPC_COMPLAINT_REFINED_2026_01_03.md](CIPC_COMPLAINT_REFINED_2026_01_03.md) |
| **POPIA Criminal Complaint** | 2026-01-03 | 2026-01-03 | [POPIA_COMPLAINT_REFINED_2026_01_03.md](POPIA_COMPLAINT_REFINED_2026_01_03.md) |
| **NPA Tax Fraud Report** | 2026-01-03 | 2026-01-03 | [NPA_TAX_FRAUD_REPORT_REFINED_2026_01_03.md](NPA_TAX_FRAUD_REPORT_REFINED_2026_01_03.md) |

### Filing Status

All filings have been refined based on:
- 46 criminal threshold events
- 33 tracked entities
- 75 mapped relations
- Comprehensive evidence from both revstream1 and ad-res-j7 repositories

---

## VI. Analysis Reports

| Report | Date | Description | Link |
| :--- | :--- | :--- | :--- |
| **Comprehensive Refinement Report** | 2026-01-04 | Latest comprehensive analysis and refinement summary | [COMPREHENSIVE_REFINEMENT_REPORT_2026_01_04.md](COMPREHENSIVE_REFINEMENT_REPORT_2026_01_04.md) |
| **Timeline Improvement Suggestions** | 2026-01-05 | Analysis of timeline gaps and improvement recommendations | [../TIMELINE_IMPROVEMENT_SUGGESTIONS_2026_01_05.json](../TIMELINE_IMPROVEMENT_SUGGESTIONS_2026_01_05.json) |
| **Evidence Index (Enhanced)** | Current | Comprehensive evidence catalog with cross-references | [evidence-index-enhanced.md](evidence-index-enhanced.md) |

---

## VII. Repository Structure

```
revstream1/
├── data_models/          # Core data models (entities, relations, events, timeline)
├── docs/                 # GitHub Pages content (this site)
├── evidence/             # Local evidence files
├── scripts/              # Analysis and processing scripts
└── *.mmd, *.png          # Visualizations and diagrams

ad-res-j7/
├── ANNEXURES/            # Primary evidence annexures (JF01-JF09, SF1-SF9)
├── 1-CIVIL-RESPONSE/     # Civil response application evidence
├── 2-CRIMINAL-CASE/      # Criminal case evidence and filings
├── 3-EXTERNAL-VALIDATION/# External validation package
└── evidence/             # Additional evidence files
```

---

## VIII. How to Navigate This Evidence

### For Legal Professionals
1. Start with **Section III** (Three Legal Applications) to understand the case structure
2. Review **Section II** (Evidence Index) for specific evidence references
3. Examine **Section I** (Core Data Models) for detailed entity and event information
4. Use **Section IV** (Visualizations) for timeline and network analysis

### For Technical Analysts
1. Begin with **Section I** (Core Data Models) for structured data
2. Review **Section VI** (Analysis Reports) for methodology and findings
3. Examine **Section VII** (Repository Structure) for data organization
4. Use the data models directly from the `data_models/` directory

### For External Validators
1. Start with **Application 3** in **Section III** (External Validation)
2. Review **Section II** (Evidence Index) for evidence completeness
3. Examine **Section VI** (Analysis Reports) for analysis methodology
4. Use **Section IV** (Visualizations) to verify timeline accuracy

---

*This page is automatically generated and updated based on the latest analysis of the `revstream1` and `ad-res-j7` repositories.*

**Repository:** [cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Extended Evidence:** [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)  
**Last Generated:** 2026-01-05 05:40:00 UTC
