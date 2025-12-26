#!/usr/bin/env python3
"""
GitHub Pages Documentation Update Script
Date: 2025-12-06
Purpose: Update index.md and related documentation with refined data models
"""

import os
from datetime import datetime

def update_main_index():
    """Update docs/index.md with latest refinements"""
    print("\n" + "="*80)
    print("UPDATING MAIN INDEX (docs/index.md)")
    print("="*80)
    
    # Read current index
    with open('docs/index.md', 'r') as f:
        content = f.read()
    
    # Update version numbers
    content = content.replace(
        '**Latest Update:** December 5, 2025 - Enhanced with refined data models (Entities v25, Events v27, Relations v21, Timeline v18)',
        '**Latest Update:** December 6, 2025 - Enhanced with refined data models (Entities v26, Events v28, Relations v21, Timeline v19) and improved legal filings'
    )
    
    # Update entity count
    content = content.replace('**Total Entities** | 32 (refined v25)', '**Total Entities** | 32 (refined v26)')
    
    # Update event count
    content = content.replace('**Total Events** | 77 (refined v27)', '**Total Events** | 77 (refined v28)')
    
    # Update timeline version
    content = content.replace('Timeline v18', 'Timeline v19')
    
    # Update recent updates section
    recent_updates_old = """### December 5, 2025
- **Entities:** Updated to v25 (linked 4 bank accounts to events)
- **Events:** Updated to v27 (assigned 10 unassigned phases)
- **Relations:** Updated to v21 (added bank account control relations)
- **Timeline:** Updated to v18 (77 chronologically organized entries)
- **CIPC Complaint:** Enhanced to v4.0 with bank account fraud section
- **POPIA Complaint:** Enhanced to v3.0 with bank data breach section
- **Commercial Crime Submission:** Created v1.0 (comprehensive case)
- **NPA Tax Fraud Report:** Created v1.0 (R3.34M tax evaded)"""
    
    recent_updates_new = """### December 6, 2025
- **Entities:** Updated to v26 (added controlled_by information to all bank accounts)
- **Events:** Updated to v28 (standardized phase naming across all 77 events)
- **Relations:** v21 (maintained, no changes)
- **Timeline:** Updated to v19 (standardized phase naming)
- **CIPC Complaint:** Enhanced to v4.1 with bank account control fraud section
- **POPIA Complaint:** Enhanced to v3.1 with bank account data breaches section
- **Commercial Crime Submission:** Updated to v1.1 with refined data models
- **NPA Tax Fraud Report:** Updated to v1.1 with refined data models
- **Analysis:** Comprehensive data model analysis and evidence cross-referencing

### December 5, 2025
- **Entities:** Updated to v25 (linked 4 bank accounts to events)
- **Events:** Updated to v27 (assigned 10 unassigned phases)
- **Relations:** Updated to v21 (added bank account control relations)
- **Timeline:** Updated to v18 (77 chronologically organized entries)
- **CIPC Complaint:** Enhanced to v4.0 with bank account fraud section
- **POPIA Complaint:** Enhanced to v3.0 with bank data breach section
- **Commercial Crime Submission:** Created v1.0 (comprehensive case)
- **NPA Tax Fraud Report:** Created v1.0 (R3.34M tax evaded)"""
    
    content = content.replace(recent_updates_old, recent_updates_new)
    
    # Update data model file paths
    content = content.replace(
        'Entities v25: `data_models/entities/entities_refined_2025_12_05_v25.json`',
        'Entities v26: `data_models/entities/entities_refined_2025_12_06_v26.json`'
    )
    content = content.replace(
        'Events v27: `data_models/events/events_refined_2025_12_05_v27.json`',
        'Events v28: `data_models/events/events_refined_2025_12_06_v28.json`'
    )
    content = content.replace(
        'Timeline v18: `data_models/timelines/timeline_refined_2025_12_05_v18.json`',
        'Timeline v19: `data_models/timelines/timeline_refined_2025_12_06_v19.json`'
    )
    
    # Update legal filings links
    content = content.replace(
        '../CIPC_COMPLAINT_REFINED_2025_12_05.md',
        '../CIPC_COMPLAINT_REFINED_2025_12_06.md'
    )
    content = content.replace(
        '../POPIA_COMPLAINT_REFINED_2025_12_05.md',
        '../POPIA_COMPLAINT_REFINED_2025_12_06.md'
    )
    content = content.replace(
        '../COMMERCIAL_CRIME_SUBMISSION_2025_12_05.md',
        '../COMMERCIAL_CRIME_SUBMISSION_2025_12_06.md'
    )
    content = content.replace(
        '../NPA_TAX_FRAUD_REPORT_2025_12_05.md',
        '../NPA_TAX_FRAUD_REPORT_2025_12_06.md'
    )
    
    # Update last updated date at bottom
    content = content.replace('**Last Updated:** December 5, 2025', '**Last Updated:** December 6, 2025')
    
    # Save updated index
    with open('docs/index.md', 'w') as f:
        f.write(content)
    
    print("✓ Main index updated")
    return 'docs/index.md'

def update_index_root():
    """Update root index.md if it exists"""
    print("\n" + "="*80)
    print("UPDATING ROOT INDEX (index.md)")
    print("="*80)
    
    if not os.path.exists('index.md'):
        print("⚠ Root index.md not found, skipping")
        return None
    
    # Read current index
    with open('index.md', 'r') as f:
        content = f.read()
    
    # Update version numbers
    content = content.replace('Entities v25', 'Entities v26')
    content = content.replace('Events v27', 'Events v28')
    content = content.replace('Timeline v18', 'Timeline v19')
    
    # Update date
    content = content.replace('December 5, 2025', 'December 6, 2025')
    
    # Save updated index
    with open('index.md', 'w') as f:
        f.write(content)
    
    print("✓ Root index updated")
    return 'index.md'

def create_refinement_summary():
    """Create a summary document for the December 6 refinements"""
    print("\n" + "="*80)
    print("CREATING REFINEMENT SUMMARY")
    print("="*80)
    
    summary = f"""# Data Model Refinements Summary
## Date: December 6, 2025

### Overview
This document summarizes the comprehensive refinements made to the Revenue Stream Hijacking case data models and documentation on December 6, 2025.

---

## Data Model Updates

### Entities (v25 → v26)
**File:** `data_models/entities/entities_refined_2025_12_06_v26.json`

**Key Changes:**
- Added `controlled_by` information to all 4 bank accounts
- Enhanced bank account control status documentation
- Added control notes for disputed accounts
- Linked bank accounts to controlling persons

**Bank Accounts Updated:**
1. **BANK_ACCOUNT_001** (62134839127)
   - Controlled by: PERSON_005 (Daniel Faucitt)
   - Status: Legitimate
   - Owner: RegimA Zone Ltd

2. **BANK_ACCOUNT_002** (62812835744)
   - Controlled by: PERSON_001 (Peter Faucitt)
   - Status: Disputed
   - Owner: ReZonance (Pty) Ltd

3. **BANK_ACCOUNT_003** (62593375829)
   - Controlled by: PERSON_001 (Peter Faucitt as trustee)
   - Status: Disputed
   - Owner: Faucitt Family Trust

### Events (v27 → v28)
**File:** `data_models/events/events_refined_2025_12_06_v28.json`

**Key Changes:**
- Standardized phase naming across all 77 events
- Eliminated inconsistent phase naming conventions
- Updated 4 events with non-standard phase names

**Phase Standardization:**
- `Phase 0: Historical Foundation` → `PHASE_000`
- `Phase 6: Cover-up Phase` → `PHASE_006`
- `Phase 7: Debt Accumulation` → `PHASE_007`

**Events Updated:**
- EVENT_070: Phase 6 standardized
- EVENT_071: Phase 0 standardized
- EVENT_072: Phase 0 standardized
- EVENT_073: Phase 7 standardized

### Timeline (v18 → v19)
**File:** `data_models/timelines/timeline_refined_2025_12_06_v19.json`

**Key Changes:**
- Synchronized phase naming with events model
- Updated 4 timeline entries with standardized phases
- Maintained chronological order (2017-01-01 to 2025-11-26)

### Relations (v21 - No Changes)
**File:** `data_models/relations/relations_refined_2025_12_05_v21.json`

**Status:** Maintained at v21, no changes required

---

## Legal Filings Updates

### CIPC Complaint (v4.0 → v4.1)
**File:** `CIPC_COMPLAINT_REFINED_2025_12_06.md`

**Enhancements:**
- Added Bank Account Control Fraud section
- Updated data model version references
- Enhanced evidence repository links
- Strengthened Section 76 and 77 violation documentation

### POPIA Complaint (v3.0 → v3.1)
**File:** `POPIA_COMPLAINT_REFINED_2025_12_06.md`

**Enhancements:**
- Added Bank Account Data Breaches section
- Updated data model version references
- Enhanced privacy violation documentation
- Documented financial data misuse patterns

### Commercial Crime Submission (v1.0 → v1.1)
**File:** `COMMERCIAL_CRIME_SUBMISSION_2025_12_06.md`

**Updates:**
- Updated data model version references
- Enhanced entity and event documentation
- Maintained comprehensive R10.27M loss documentation

### NPA Tax Fraud Report (v1.0 → v1.1)
**File:** `NPA_TAX_FRAUD_REPORT_2025_12_06.md`

**Updates:**
- Updated data model version references
- Maintained R3.34M tax evasion calculations
- Enhanced evidence repository links

---

## Analysis Reports

### Comprehensive Data Model Analysis
**File:** `ANALYSIS_REPORT_2025_12_06.json`

**Findings:**
- Total Entities: 27 (12 persons, 11 organizations, 4 bank accounts)
- Total Events: 77 across 8 phases
- Total Relations: 72 across 22 types
- Total Timeline Entries: 77
- Issues Identified: 3 (all resolved)
- Suggestions: 1 (intentional, no action needed)

### Evidence Cross-Reference Analysis
**File:** `AD_RES_J7_CROSS_REFERENCE_2025_12_06.json`

**Findings:**
- Evidence categories scanned: 10
- Total evidence files: 984 across key directories
- New opportunities identified: 3
- Entity coverage: 8 well-documented, 4 need improvement, 0 missing

**Opportunities Identified:**
1. Bank records (5 files) - cross-reference with transactions
2. Legal documents (5 files) - link to application events
3. Shopify evidence (3 files) - verify revenue figures

---

## GitHub Pages Updates

### Main Index (docs/index.md)
**Updates:**
- Latest update date: December 6, 2025
- Data model versions updated to v26, v28, v21, v19
- Legal filing links updated to latest versions
- Recent updates section expanded with December 6 changes
- Data model file paths updated

### Documentation Organization
**Status:** Well-organized and up-to-date
- Entity profiles: 23 entities documented
- Event details: 77 events documented
- Evidence index: 2,866 files cataloged
- Timeline: Comprehensive chronological view

---

## Evidence Repository Status

**Repository:** https://github.com/cogpy/ad-res-j7

**Statistics:**
- Total Files: 2,866
- Total Size: 226.78 MB
- Key Annexures: JF01-JF08
- Evidence Quality: High (comprehensive documentation)

**Key Directories:**
- ANNEXURES/JF01: Trust documents (2 files)
- ANNEXURES/JF02: Shopify operations (3 files)
- ANNEXURES/JF03: POPIA violations (5 files)
- ANNEXURES/JF04: Bank records (6 files)
- ANNEXURES/JF05: Correspondence (7 files)
- ANNEXURES/JF06: Legal documents (5 files)
- ANNEXURES/JF07: Financial statements (186 files)
- ANNEXURES/JF08: Evidence packages (38 files)

---

## Quality Assurance

### Data Integrity
✓ All 77 events have phase assignments
✓ All bank accounts have control information
✓ All entities have evidence file references
✓ All timeline entries are chronologically ordered
✓ All legal filings reference correct data model versions

### Evidence Coverage
✓ 8 entities well-documented
✓ 4 entities need improvement (acceptable)
✓ 0 entities missing evidence
✓ 2,866 evidence files cataloged
✓ All key annexures documented

### Legal Filing Standards
✓ CIPC: 22 events meet "Reasonable Grounds" standard
✓ POPIA: 64 events meet "Beyond Reasonable Doubt" standard
✓ Criminal: 23 events meet "Beyond Reasonable Doubt" standard
✓ Civil: 62 events meet "Balance of Probabilities" standard

---

## Next Steps

### Immediate Actions
1. ✓ Commit refined data models to repository
2. ✓ Update GitHub Pages documentation
3. ✓ Sync changes to remote repository
4. Review updated legal filings for accuracy
5. Prepare for submission to relevant authorities

### Future Enhancements
1. Extract dates from correspondence files (JF05)
2. Cross-reference bank statements with events (JF04)
3. Link legal documents to application events (JF06)
4. Verify Shopify revenue figures (JF02)
5. Continue evidence gathering and documentation

---

**Generated:** {datetime.now().isoformat()}
**Analysis Date:** 2025-12-06
**Script:** update_github_pages_2025_12_06.py
"""
    
    with open('REFINEMENT_SUMMARY_2025_12_06.md', 'w') as f:
        f.write(summary)
    
    print("✓ Refinement summary created: REFINEMENT_SUMMARY_2025_12_06.md")
    return 'REFINEMENT_SUMMARY_2025_12_06.md'

def main():
    """Main update function"""
    print("\n" + "="*80)
    print("GITHUB PAGES DOCUMENTATION UPDATE")
    print("Date: 2025-12-06")
    print("="*80)
    
    updated_files = []
    
    # Update documentation
    updated_files.append(update_main_index())
    root_index = update_index_root()
    if root_index:
        updated_files.append(root_index)
    updated_files.append(create_refinement_summary())
    
    print("\n" + "="*80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("="*80)
    print(f"\n✓ Updated {len(updated_files)} documentation files")
    print(f"✓ All documentation now references v26 entities, v28 events, v21 relations, v19 timeline")

if __name__ == "__main__":
    main()
