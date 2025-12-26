import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def update_index_page():
    """Update the main index.md with latest data model versions"""
    
    # Load latest data models
    entities = load_json("data_models/entities/entities_refined_2025_11_23_v10.json")
    events = load_json("data_models/events/events_refined_2025_11_23_v11.json")
    relations = load_json("data_models/relations/relations_refined_2025_11_23_v8.json")
    timeline = load_json("data_models/timelines/timeline_refined_2025_11_23_v9.json")
    
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
| **Data Model Version** | {entities["metadata"]["version"]} |
| **Last Updated** | {datetime.now().strftime("%Y-%m-%d")} |
| **Total Entities** | {entities["metadata"].get("total_entities", 27)} |
| **Total Events** | {timeline["metadata"].get("total_events", 69)} |
| **Total Timeline Phases** | {len(timeline.get("timeline_phases", {}))} |
| **Total Relations** | {relations["metadata"].get("total_relations", 60)} |
| **Events with Financial Impact** | 54 |
| **Estimated Financial Impact** | R115,015,600+ |
| **Revenue Theft** | R3,141,647.70 |
| **Trust Violations** | R2,851,247.35 |
| **Financial Manipulation** | R4,276,832.85 |
| **Total Documented Losses** | R10,269,727.90 |

---

## Data Model Files

Access the latest refined data models:

- **[Entities v{entities["metadata"]["version"]}](../data_models/entities/entities_refined_2025_11_23_v10.json)** - {entities["metadata"].get("total_entities", 27)} entities across 7 types
- **[Events v{events["metadata"]["version"]}](../data_models/events/events_refined_2025_11_23_v11.json)** - {timeline["metadata"].get("total_events", 69)} events across 8 phases
- **[Relations v{relations["metadata"]["version"]}](../data_models/relations/relations_refined_2025_11_23_v8.json)** - {relations["metadata"].get("total_relations", 60)} relations across multiple types
- **[Timeline v{timeline["metadata"]["version"]}](../data_models/timelines/timeline_refined_2025_11_23_v9.json)** - {len(timeline.get("timeline_phases", {}))} phases spanning 2017-2025

**Extended Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)  
**Comprehensive Evidence Index:** [COMPREHENSIVE_EVIDENCE_INDEX.md](https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md)

---

## Three Sequential Interdict Applications

### [Application 1: Ex Parte Interdict (August 13, 2025)](application-1.md)

**Type:** Ex parte urgent application  
**Targets:** Both Jacqueline and Daniel Faucitt  
**Status:** Pending return date; notice of intention to oppose filed September 5, 2025  
**Events:** 45 events mapped to this application

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
**Events:** 50 events mapped to this application

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
**Events:** 20 events mapped to this application

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
- **Revenue Theft:** 7 events targeting business operations
- **Trust Violations:** 6 events manipulating family trust structure
- **Financial Manipulation:** 12 events diverting and concealing funds
- **Accounting Fraud:** 3 events concealing financial crimes
- **Evidence Tampering:** 2 events destroying audit trails

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
| **Phase 0: Historical Foundation** | Jun 2017 - Dec 2021 | 1,645 days | 14 | R25.1M+ |
| **Phase 1: Foundation** | Mar 2025 | 30 days | 5 | R8.75M+ |
| **Phase 2: Initial Theft** | Apr 2025 | 14 days | 5 | R7.42M |
| **Phase 3: Escalation** | May 2025 | 28 days | 6 | R1.85M+ |
| **Phase 4: Consolidation** | Jun 2025 | 25 days | 11 | R3.14M+ |
| **Phase 5: Control Seizure** | Jul 2025 | 18 days | 9 | Unknown |
| **Phase 6: Cover-up** | Aug-Sep 2025 | 33 days | 8 | Unknown |
| **Phase 7: Debt Accumulation** | 2023-2025 | 568 days | 0 | R1.04M+ |

**[📊 View Detailed Timeline Analysis](../data_models/timelines/timeline_refined_2025_11_23_v9.json)**

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

- **Entities Version:** {entities["metadata"]["version"]}
- **Events Version:** {events["metadata"]["version"]}
- **Relations Version:** {relations["metadata"]["version"]}
- **Timeline Version:** {timeline["metadata"]["version"]}
- **Last Updated:** {datetime.now().strftime("%Y-%m-%d")}
- **Total Entities:** {entities["metadata"].get("total_entities", 27)}
- **Total Events:** {timeline["metadata"].get("total_events", 69)}
- **Total Relations:** {relations["metadata"].get("total_relations", 60)}
- **Extended Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)

**[📄 View Comprehensive Analysis Report](DATA_MODEL_COMPREHENSIVE_ANALYSIS_2025_11_23.json)**  
**[📄 View Improvements Report](IMPROVEMENTS_REPORT_2025_11_23.json)**

---

## Evidence Resources

### Enhanced Evidence Index

Browse all evidence files organized by category with direct links to source documents in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).

**Application-Specific Evidence:**
- **[📁 Application 1 Evidence Index](application-1-evidence.md)** - 45 events, POPIA violations, trust misconduct
- **[📁 Application 2 Evidence Index](application-2-evidence.md)** - 50 events, settlement enforcement, accounting fraud
- **[📁 Application 3 Evidence Index](application-3-evidence.md)** - 20 events, contact violations, ongoing interference

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

**Last Updated:** {datetime.now().strftime("%Y-%m-%d")}
"""
    
    # Write updated index
    with open("docs/index.md", "w") as f:
        f.write(index_content)
    
    print("✓ Updated docs/index.md")

def create_data_model_readme():
    """Create a README for the data_models directory"""
    
    readme_content = """# Data Models Directory

This directory contains the refined data models for Case 2025-137857.

## Latest Versions (2025-11-23)

- **[entities_refined_2025_11_23_v10.json](entities/entities_refined_2025_11_23_v10.json)** - v17.0
  - 27 entities across 7 types
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

- **[events_refined_2025_11_23_v11.json](events/events_refined_2025_11_23_v11.json)** - v18.0
  - 69 events across 8 phases
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

- **[relations_refined_2025_11_23_v8.json](relations/relations_refined_2025_11_23_v8.json)** - v14.0
  - 60 relations across multiple types
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

- **[timeline_refined_2025_11_23_v9.json](timelines/timeline_refined_2025_11_23_v9.json)** - v15.0
  - 8 phases spanning 2017-2025
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

## Structure

Each data model file contains:

1. **Metadata** - Version, creation date, description, case number, last updated
2. **Data** - Entities, events, relations, or timeline phases
3. **Cross-References** - Links to evidence files, GitHub Pages, and ad-res-j7 repository

## Evidence Integration

All data models now include:

- `evidence_files` - Direct paths to evidence files
- `evidence_repository` - Link to ad-res-j7 repository
- `comprehensive_evidence_index` - Link to comprehensive evidence catalog
- `github_pages_reference` - Link to relevant GitHub Pages documentation
- `ad_res_j7_references` - Specific references to evidence in ad-res-j7

## Extended Evidence Repository

For complete evidence files and documentation, see:
- **Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
- **Evidence Index:** [COMPREHENSIVE_EVIDENCE_INDEX.md](https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md)

## Version History

- **v17.0 (2025-11-23)** - Entities: Enhanced evidence cross-references, improved GitHub Pages links
- **v18.0 (2025-11-23)** - Events: Enhanced evidence cross-references, improved GitHub Pages links
- **v14.0 (2025-11-23)** - Relations: Enhanced evidence cross-references, improved GitHub Pages links
- **v15.0 (2025-11-23)** - Timeline: Enhanced evidence cross-references, improved GitHub Pages links

## Usage

These JSON files can be:
- Loaded into analysis tools
- Used for hypergraph visualization
- Imported into databases (Supabase, Neon)
- Referenced in legal documentation
- Used for timeline visualization

## Maintenance

Data models are regularly refined and updated. Check the `last_updated` field in the metadata for the most recent modification date.
"""
    
    with open("data_models/README.md", "w") as f:
        f.write(readme_content)
    
    print("✓ Created data_models/README.md")

def main():
    print("Updating GitHub Pages organization...")
    print("=" * 80)
    
    update_index_page()
    create_data_model_readme()
    
    print("\n✓ GitHub Pages Update Complete!")
    print("=" * 80)
    print("\nUpdated files:")
    print("  - docs/index.md")
    print("  - data_models/README.md")
    print("\nAll pages now include:")
    print("  ✓ Latest data model version numbers")
    print("  ✓ Direct links to JSON data files")
    print("  ✓ Enhanced evidence cross-references")
    print("  ✓ Links to ad-res-j7 repository")
    print("  ✓ Comprehensive evidence index references")

if __name__ == "__main__":
    main()
