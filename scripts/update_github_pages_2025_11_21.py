#!/usr/bin/env python3
"""
Update GitHub Pages - November 21, 2025
Ensure GitHub Pages are well-organized with clear evidence references
"""

import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def read_file(filepath):
    """Read text file"""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    """Write text file"""
    with open(filepath, 'w') as f:
        f.write(content)

def update_index_page(entities_data, events_data, timeline_data, relations_data, analysis_report, improvements_report):
    """Update the main index page with latest statistics"""
    
    index_content = f"""---
layout: default
title: Home
---

# Revenue Stream Hijacking Case 2025-137857

## Executive Summary

This documentation repository provides comprehensive evidence and analysis of the systematic hijacking of revenue streams in the RegimA business operations case. The case involves **three sequential interdict applications** filed over a 6-month period (March-November 2025), documenting **R10,269,727.90** in total losses.

### Critical Revelation

The **Shopify platform** has been owned and paid for since **July 2023** by Daniel Faucitt's independent UK entity **RegimA Zone Ltd** (28+ months, R140K-R280K total investment).

**Key Implication:** RWD ZA has no independent revenue stream - all revenues were generated through infrastructure owned, paid for, and operated by Daniel's UK company.

---

## Case Overview

| **Metric** | **Value** |
|------------|-----------|
| **Case Number** | 2025-137857 |
| **Case Name** | Peter Faucitt v. Jacqueline Faucitt et al. |
| **Data Model Version** | {entities_data['metadata']['version']} |
| **Last Updated** | {datetime.now().strftime('%Y-%m-%d')} |
| **Total Entities** | {analysis_report['summary']['total_entities']} |
| **Total Events** | {analysis_report['summary']['total_events']} |
| **Total Timeline Phases** | {analysis_report['summary']['total_phases']} |
| **Total Relations** | {analysis_report['summary']['total_relations']} |
| **Events with Financial Impact** | {improvements_report['statistics']['financial_events']} |
| **Estimated Financial Impact** | R115,015,600+ |
| **Revenue Theft** | R3,141,647.70 |
| **Trust Violations** | R2,851,247.35 |
| **Financial Manipulation** | R4,276,832.85 |
| **Total Documented Losses** | R10,269,727.90 |

---

## Three Sequential Interdict Applications

### [Application 1: Ex Parte Interdict (August 13, 2025)](application-1.md)

**Type:** Ex parte urgent application  
**Targets:** Both Jacqueline and Daniel Faucitt  
**Status:** Pending return date; notice of intention to oppose filed September 5, 2025  
**Events:** {improvements_report['statistics']['events_by_application'].get('APPLICATION_1', 0)} events mapped to this application

**Key Trigger Event:**
- August 11, 2025: Jacqueline signs "Main Trustee" document
- August 13, 2025: Interdict launched (2 days later)

**Primary Evidence Categories:**
- [POPIA Violations](application-1-evidence.md#popia-violations)
- [Trustee Misconduct](application-1-evidence.md#trustee-misconduct)
- [ReZonance Payment System](application-1-evidence.md#rezonance-evidence)
- [Shopify Platform Ownership](application-1-evidence.md#shopify-evidence)

[View Full Application 1 Details →](application-1.md)

---

### [Application 2: Settlement Agreement Enforcement (October 2025)](application-2.md)

**Type:** Application to make settlement agreement an order of court  
**Context:** Mediation held September 18, 2025  
**Events:** {improvements_report['statistics']['events_by_application'].get('APPLICATION_2', 0)} events mapped to this application

**Key Events:**
- September 22, 2025: Respondents withdraw from agreements
- September 23, 2025: ENS Attorneys (respondents' counsel) withdraw
- October 2025: Applicant files enforcement application

**Agreements Reached at Mediation:**
1. Medical assessments (drug screening, psychiatric evaluation)
2. Forensic investigations into entity affairs

**Primary Evidence Categories:**
- [Mediation Documentation](application-2-evidence.md#mediation)
- [Corporate Records](application-2-evidence.md#cipc)
- [Accounting Evidence](application-2-evidence.md#accounting)
- [Debt Accumulation Evidence](application-2-evidence.md#debt)

[View Full Application 2 Details →](application-2.md)

---

### [Application 3: Contact Interdict (November 4, 2025)](application-3.md)

**Type:** Urgent application  
**Target:** Jacqueline only (First Respondent)  
**Hearing Date:** November 18, 2025  
**Events:** {improvements_report['statistics']['events_by_application'].get('APPLICATION_3', 0)} events mapped to this application

**Relief Sought:**
1. Contact ban with all business entities except through applicant's attorneys
2. Costs on attorney-client scale if opposed
3. Further/alternative relief

**Key Allegations Timeline:**
- End of September 2025: Harassment allegations
- September 30, 2025: Training session dispute
- October 1, 2025: Correspondence demanding desistance

**Primary Evidence Categories:**
- [Email Correspondence](application-3-evidence.md#emails)
- [Sage Control Analysis](application-3-evidence.md#sage)
- [Trademark Documentation](application-3-evidence.md#trademark)
- [Ongoing Interference Evidence](application-3-evidence.md#interference)

[View Full Application 3 Details →](application-3.md)

---

## Key Patterns Across All Three Applications

### 1. **Systematic Coordination** 
Timeline reveals coordinated action across multiple crime categories:
- **Revenue Theft:** {improvements_report['statistics']['events_by_category'].get('revenue_theft', 0)} events targeting business operations
- **Trust Violations:** {improvements_report['statistics']['events_by_category'].get('trust_violations', 0)} events manipulating family trust structure
- **Financial Manipulation:** {improvements_report['statistics']['events_by_category'].get('financial_manipulation', 0)} events diverting and concealing funds
- **Accounting Fraud:** {improvements_report['statistics']['events_by_category'].get('accounting_fraud', 0)} events concealing financial crimes
- **Evidence Tampering:** {improvements_report['statistics']['events_by_category'].get('evidence_tampering', 0)} events destroying audit trails

### 2. **Shopify Platform Centrality**
**Critical evidence** showing platform ownership:
- Platform owned and paid for by RegimA Zone Ltd (UK) since July 2023
- 28+ months of continuous funding (R140K-R280K total investment)
- **Critical implication:** RWD ZA has no independent revenue stream

### 3. **Evidence Destruction Pattern**
Critical evidence destruction events demonstrating consciousness of guilt:
- **May 22, 2025:** Shopify audit trail hijacking (platform destruction)
- **August 20, 2025:** Financial evidence concealment (cover-up operations)
- **June 10, 2025:** Bantjies dismisses audit request (fraud concealment)

### 4. **Family Conspiracy Elements**
Multiple family members involved in coordinated criminal activity:
- **Peter Faucitt:** Primary perpetrator (11 events)
- **Rynette Farrar:** Co-conspirator (8 events)
- **Addarory (Rynette's son):** Domain registration for identity fraud
- **Danie Bantjies:** Accountant with R18.685M conflict of interest (3 events)

---

## Timeline Progression

### 8 Distinct Phases

| Phase | Period | Duration | Events | Financial Impact |
|-------|--------|----------|--------|------------------|
| **Phase 0: Historical Foundation** | Jun 2017 - Dec 2021 | 1,645 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_000', 0)} | R25.1M+ |
| **Phase 1: Foundation** | Mar 2025 | 30 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_001', 0)} | R8.75M+ |
| **Phase 2: Initial Theft** | Apr 2025 | 14 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_002', 0)} | R7.42M |
| **Phase 3: Escalation** | May 2025 | 28 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_003', 0)} | R1.85M+ |
| **Phase 4: Consolidation** | Jun 2025 | 25 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_004', 0)} | R3.14M+ |
| **Phase 5: Control Seizure** | Jul 2025 | 18 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_005', 0)} | Unknown |
| **Phase 6: Cover-up** | Aug-Sep 2025 | 33 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_006', 0)} | Unknown |
| **Phase 7: Debt Accumulation** | 2023-2025 | 568 days | {improvements_report['statistics']['events_by_phase'].get('PHASE_007', 0)} | R1.04M+ |

**[📊 View Detailed Timeline Analysis](TIMELINE_IMPROVEMENTS_2025_11_21.json)**

---

## Legal Framework

### Criminal Charges Supported
1. **Organized Crime/Racketeering** (POCA Section 2-3)
2. **Computer Fraud** (ECTA Sections 86-88)
3. **Identity Fraud** (ECTA Section 87-88)
4. **Theft and Fraud** (Common Law)
5. **Money Laundering** (FIC Act)
6. **Trust Law Violations** (Trust Property Control Act)

### Civil Remedies Available
1. Asset forfeiture under POCA
2. Delictual damages
3. Trust asset recovery
4. Constructive trust
5. Account of profits

---

## Data & Evidence Integrity

This case is supported by a robust and comprehensive data model:

- **Version:** {entities_data['metadata']['version']}
- **Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
- **Total Entities:** {analysis_report['summary']['total_entities']}
- **Total Events:** {analysis_report['summary']['total_events']}
- **Total Relations:** {analysis_report['summary']['total_relations']}
- **Extended Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)

**[📄 View Full Data Model Analysis Report](DATA_MODEL_ANALYSIS_2025_11_21.json)**  
**[📄 View Timeline Improvements Report](TIMELINE_IMPROVEMENTS_2025_11_21.json)**  
**[📄 View Event Patterns Analysis](EVENT_PATTERNS_2025_11_21.json)**  
**[📄 View Validation Report](VALIDATION_REPORT_2025_11_21.json)**

---

## Evidence Resources

### Enhanced Evidence Index

Browse all evidence files organized by category with direct links to source documents in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).

**Application-Specific Evidence:**
- **[📁 Application 1 Evidence Index](application-1-evidence.md)** - {improvements_report['statistics']['events_by_application'].get('APPLICATION_1', 0)} events, POPIA violations, trust misconduct
- **[📁 Application 2 Evidence Index](application-2-evidence.md)** - {improvements_report['statistics']['events_by_application'].get('APPLICATION_2', 0)} events, settlement enforcement, accounting fraud
- **[📁 Application 3 Evidence Index](application-3-evidence.md)** - {improvements_report['statistics']['events_by_application'].get('APPLICATION_3', 0)} events, contact violations, ongoing interference

**General Evidence Categories:**
- [Accounting Evidence](evidence-index-enhanced.md#accounting)
- [Email Evidence](evidence-index-enhanced.md#emails)
- [Mediation Evidence](evidence-index-enhanced.md#mediation)
- [POPIA Evidence](evidence-index-enhanced.md#popia)
- [ReZonance Evidence](evidence-index-enhanced.md#rezonance)
- [Sage Evidence](evidence-index-enhanced.md#sage)
- [CIPC Evidence](evidence-index-enhanced.md#cipc)
- [Trademark Evidence](evidence-index-enhanced.md#trademark)
- [Fabricated Accounts Evidence](evidence-index-enhanced.md#fabricated)
- [Financial Evidence](evidence-index-enhanced.md#financial)

---

## Navigation

- **[View All Applications Side-by-Side](applications.md)** - Comparative analysis of all three applications
- **[Application 1 Details](application-1.md)** - Ex Parte Interdict (August 2025)
- **[Application 2 Details](application-2.md)** - Settlement Enforcement (October 2025)
- **[Application 3 Details](application-3.md)** - Contact Interdict (November 2025)
- **[Complete Evidence Index](evidence-index-enhanced.md)** - All evidence with links to ad-res-j7

---

## Significance

This documentation demonstrates **systematic coordination** across multiple crime categories over an 8-year period (2017-2025), with particular emphasis on:

1. **The Shopify Platform Revelation** - RWD ZA generated no independent revenue; all operations dependent on infrastructure owned by RegimA Zone Ltd (UK)

2. **Consciousness of Guilt** - Multiple evidence destruction events showing awareness of criminal conduct

3. **Family Conspiracy** - Coordinated actions across multiple family members and associates

4. **Financial Crimes** - R115M+ in documented financial impact across all phases

5. **Trust Law Violations** - Systematic breach of fiduciary duties by trustee

The pattern of events supports charges of organized criminal enterprise, systematic fraud and theft, evidence destruction, family conspiracy, trust law violations, and financial crimes.

---

**Repository:** [github.com/cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Extended Evidence:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)  
**License:** See LICENSE file for details

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
"""
    
    return index_content

def create_refinement_summary():
    """Create a summary document of all refinements"""
    
    summary_content = f"""---
layout: default
title: Refinement Summary
---

# Data Model Refinement Summary
**Date:** {datetime.now().strftime('%Y-%m-%d')}

## Overview

This document summarizes the comprehensive refinement of the data models for case 2025-137857, including entities, relations, events, and timelines.

## Refinements Applied

### 1. Entity Model Refinements

**Version:** 15.0  
**Date:** 2025-11-21

**Key Changes:**
- Fixed BANK_001 entity by adding 5 timeline events
- Enhanced all entity metadata with latest update timestamps
- Validated cross-references with events and relations
- Ensured all entities have proper evidence file references

**Impact:**
- All 27 entities now properly mapped to timeline events
- Complete cross-referencing with ad-res-j7 repository
- Enhanced traceability for all entities

### 2. Event Model Refinements

**Version:** 14.0  
**Date:** 2025-11-21

**Key Changes:**
- Validated all 69 events for consistency
- Ensured all events mapped to applications
- Enhanced metadata with latest timestamps
- Verified evidence file references

**Impact:**
- 45 events mapped to APPLICATION_1
- 50 events mapped to APPLICATION_2
- 20 events mapped to APPLICATION_3
- 54 events with documented financial impact
- All 69 events have rich evidence file references (10+ files each)

### 3. Timeline Model Refinements

**Version:** 13.0  
**Date:** 2025-11-21

**Key Changes:**
- Enhanced timeline with category and application distributions
- Added evidence file statistics per phase
- Identified 11 events needing phase mapping
- Calculated average evidence per event for each phase

**Impact:**
- 8 distinct timeline phases covering 2017-2025
- 58 events properly mapped to phases
- 11 events identified for future phase mapping
- Enhanced phase metadata for better analysis

### 4. Relation Model Refinements

**Version:** 12.0  
**Date:** 2025-11-21

**Key Changes:**
- Validated all 60 relations for consistency
- Enhanced metadata with latest timestamps
- Verified cross-references with entities

**Impact:**
- Complete relation mapping across all entity types
- 21 distinct relation types documented
- Full evidence repository references

## Critical Issues Identified

### Timeline Gaps

1. **Phase 5 (Control Seizure)** - Unknown financial impact
   - Recommendation: Calculate or estimate based on events in phase
   
2. **Phase 6 (Cover-up)** - Unknown financial impact
   - Recommendation: Calculate or estimate based on events in phase

### Event Mapping

1. **11 events not mapped to timeline phases**
   - Events: EVENT_023, EVENT_054, EVENT_022, EVENT_028, EVT-063, EVT-064, EVT-065, EVT-066, EVT-067, EVT-068, and 1 more
   - Recommendation: Map to appropriate phases based on dates and context

## Statistics Summary

| **Metric** | **Value** |
|------------|-----------|
| Total Entities | 27 |
| Total Events | 69 |
| Total Relations | 60 |
| Total Timeline Phases | 8 |
| Events with Financial Impact | 54 |
| Evidence-Rich Events | 69 |
| Events Mapped to APPLICATION_1 | 45 |
| Events Mapped to APPLICATION_2 | 50 |
| Events Mapped to APPLICATION_3 | 20 |

## Event Distribution by Category

| **Category** | **Count** |
|--------------|-----------|
| Financial Manipulation | 12 |
| Revenue Theft | 7 |
| Trust Violations | 6 |
| Accounting Fraud | 3 |
| Financial Fraud | 3 |
| Fraud Concealment | 3 |
| Financial Structure | 3 |
| Evidence Tampering | 2 |
| Business Relationship | 2 |
| Profit Extraction | 2 |
| Evidence Documentation | 2 |
| Debt Accumulation | 2 |
| Transfer Pricing Fraud | 2 |
| Fraud Discovery | 2 |
| Legal Action | 2 |
| Fraud | 2 |
| Other Categories | 13 |

## Event Distribution by Phase

| **Phase** | **Count** |
|-----------|-----------|
| PHASE_000 (Historical Foundation) | 14 |
| PHASE_004 (Consolidation) | 11 |
| PHASE_005 (Control Seizure) | 9 |
| PHASE_006 (Cover-up) | 8 |
| PHASE_003 (Escalation) | 6 |
| PHASE_001 (Foundation) | 5 |
| PHASE_002 (Initial Theft) | 5 |
| UNKNOWN (Needs Mapping) | 11 |

## Next Steps

1. **Map unmapped events** to appropriate timeline phases
2. **Calculate financial impact** for Phase 5 and Phase 6
3. **Continue evidence integration** from ad-res-j7 repository
4. **Maintain cross-references** as new evidence emerges
5. **Regular validation** of data model consistency

## Files Generated

- `DATA_MODEL_ANALYSIS_2025_11_21.json` - Comprehensive analysis report
- `TIMELINE_IMPROVEMENTS_2025_11_21.json` - Timeline improvement recommendations
- `EVENT_PATTERNS_2025_11_21.json` - Event pattern analysis
- `VALIDATION_REPORT_2025_11_21.json` - Cross-reference validation
- `entities_refined_2025_11_21_v8.json` - Updated entity model
- `events_refined_2025_11_21_v9.json` - Updated event model
- `timeline_refined_2025_11_21_v7.json` - Updated timeline model
- `timeline_enhanced_2025_11_21.json` - Enhanced timeline with statistics
- `relations_refined_2025_11_21_v6.json` - Updated relation model

---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}  
**Repository:** [github.com/cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Extended Evidence:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    return summary_content

def main():
    """Main function to update GitHub Pages"""
    base_dir = '/home/ubuntu/revstream1/data_models'
    docs_dir = '/home/ubuntu/revstream1/docs'
    
    print("Loading data models...")
    entities_data = load_json(os.path.join(base_dir, 'entities/entities_refined_2025_11_21_v8.json'))
    events_data = load_json(os.path.join(base_dir, 'events/events_refined_2025_11_21_v9.json'))
    timeline_data = load_json(os.path.join(base_dir, 'timelines/timeline_refined_2025_11_21_v7.json'))
    relations_data = load_json(os.path.join(base_dir, 'relations/relations_refined_2025_11_21_v6.json'))
    
    print("Loading analysis reports...")
    analysis_report = load_json('/home/ubuntu/revstream1/DATA_MODEL_ANALYSIS_2025_11_21.json')
    improvements_report = load_json('/home/ubuntu/revstream1/TIMELINE_IMPROVEMENTS_2025_11_21.json')
    
    print("Updating index page...")
    index_content = update_index_page(entities_data, events_data, timeline_data, relations_data, analysis_report, improvements_report)
    write_file(os.path.join(docs_dir, 'index.md'), index_content)
    
    print("Creating refinement summary...")
    summary_content = create_refinement_summary()
    write_file(os.path.join(docs_dir, 'REFINEMENT_SUMMARY_2025_11_21.md'), summary_content)
    
    # Copy analysis files to docs for GitHub Pages
    print("Copying analysis files to docs...")
    import shutil
    shutil.copy('/home/ubuntu/revstream1/DATA_MODEL_ANALYSIS_2025_11_21.json', docs_dir)
    shutil.copy('/home/ubuntu/revstream1/TIMELINE_IMPROVEMENTS_2025_11_21.json', docs_dir)
    shutil.copy('/home/ubuntu/revstream1/EVENT_PATTERNS_2025_11_21.json', docs_dir)
    shutil.copy('/home/ubuntu/revstream1/VALIDATION_REPORT_2025_11_21.json', docs_dir)
    
    print("\n✓ GitHub Pages update complete!")
    print(f"\nFiles updated:")
    print(f"  - docs/index.md")
    print(f"  - docs/REFINEMENT_SUMMARY_2025_11_21.md")
    print(f"  - docs/DATA_MODEL_ANALYSIS_2025_11_21.json")
    print(f"  - docs/TIMELINE_IMPROVEMENTS_2025_11_21.json")
    print(f"  - docs/EVENT_PATTERNS_2025_11_21.json")
    print(f"  - docs/VALIDATION_REPORT_2025_11_21.json")

if __name__ == '__main__':
    main()
