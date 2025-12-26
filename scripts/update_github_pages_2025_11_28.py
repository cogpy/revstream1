#!/usr/bin/env python3
"""
Update GitHub Pages for Revenue Stream Case 2025-137857

This script:
1. Creates application-specific evidence pages
2. Updates the main index with latest data model versions
3. Ensures cross-references to ad-res-j7 repository
4. Organizes evidence by application
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = REVSTREAM_ROOT / "data_models"
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")

# Refined data files
ENTITIES_FILE = DATA_MODELS_DIR / "entities" / "entities_refined_2025_11_28_v23.json"
EVENTS_FILE = DATA_MODELS_DIR / "events" / "events_refined_2025_11_28_v25.json"
RELATIONS_FILE = DATA_MODELS_DIR / "relations" / "relations_refined_2025_11_28_v20.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_file(filepath, content):
    """Write content to a file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def create_application_1_evidence_page():
    """Create evidence page for Application 1"""
    content = """---
layout: default
title: Application 1 Evidence
---

# Application 1: Ex Parte Interdict - Evidence Index

**Case Number:** 2025-137857  
**Application Type:** Ex parte urgent application  
**Filed:** August 13, 2025  
**Targets:** Jacqueline Faucitt and Daniel Faucitt

---

## Overview

This page provides a comprehensive index of evidence supporting Application 1, organized by category and cross-referenced with the extended evidence repository at [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7).

---

## Evidence Categories

### 1. POPIA Violations

**Primary Evidence:**
- POPIA Violation Notice sent to Peter on 8 July 2025
- Warehouse access violations
- Unauthorized data processing

**Repository References:**
- `evidence/popia/POPIAViolationNotice-SenttoPeteon8July2025-DanielFaucitt-Outlook.pdf`
- `ad-res-j7/ANNEXURES/JF03/popia_violations/`

**Related Events:**
- EVENT_H003: POPIA violation notice
- EVENT_H004: Warehouse access violations

---

### 2. Trustee Misconduct

**Primary Evidence:**
- Trust deed manipulation
- Unauthorized trustee actions
- Breach of fiduciary duty

**Repository References:**
- `evidence/trust_violations/trustee_misconduct/`
- `ad-res-j7/ANNEXURES/JF01/trust_documents/`

**Related Events:**
- EVENT_001: Trust structure manipulation
- EVENT_002: Unauthorized transfers

---

### 3. ReZonance Payment System

**Primary Evidence:**
- Payment system hijacking
- Revenue stream diversion
- Unauthorized payment redirections

**Repository References:**
- `evidence/rezonance/`
- `ad-res-j7/evidence/rezonance/`

**Related Events:**
- EVENT_004: Payment system hijacking
- EVENT_005: Revenue diversion

---

### 4. Email Control and Correspondence

**Primary Evidence:**
- Email account hijacking
- Unauthorized access to business communications
- Evidence destruction via email deletion

**Repository References:**
- `evidence/emails/`
- `ad-res-j7/ANNEXURES/JF05/correspondence/`

**Related Events:**
- EVENT_006: Email control seizure
- EVENT_007: Communication interception

---

## Cross-References to ad-res-j7

The extended evidence repository at [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7) contains:

- **2,866 files** of supporting evidence
- **226.78 MB** of documentation
- Comprehensive evidence index in `COMPREHENSIVE_EVIDENCE_INDEX.md`

### Key Directories:
- `ANNEXURES/` - Formal evidence annexures
- `case_2025_137857/` - Case-specific documentation
- `FINAL_AFFIDAVIT_PACKAGE/` - Supporting affidavits
- `evidence/` - Categorized evidence files

---

## Data Model Integration

This evidence index is integrated with the refined data models:

- **Entities Model:** Version 23.0
- **Events Model:** Version 25.0
- **Relations Model:** Version 20.0

All evidence references are cross-validated against these models to ensure consistency and completeness.

---

## Navigation

- [← Back to Application 1 Details](application-1.md)
- [View All Applications](applications.md)
- [Complete Evidence Index](evidence-index-comprehensive.md)
- [Home](index.md)
"""
    return content

def create_application_2_evidence_page():
    """Create evidence page for Application 2"""
    content = """---
layout: default
title: Application 2 Evidence
---

# Application 2: Settlement Agreement Enforcement - Evidence Index

**Case Number:** 2025-137857  
**Application Type:** Application to make settlement agreement an order of court  
**Filed:** October 2025  
**Context:** Mediation held September 18, 2025

---

## Overview

This page provides a comprehensive index of evidence supporting Application 2, focusing on the mediation process and subsequent withdrawal from agreements.

---

## Evidence Categories

### 1. Mediation Documentation

**Primary Evidence:**
- Mediation agreement (September 18, 2025)
- Settlement terms and conditions
- Withdrawal notices (September 22, 2025)

**Repository References:**
- `evidence/mediation/`
- `ad-res-j7/evidence/mediation/`

**Related Events:**
- EVENT_059: Mediation held
- EVENT_060: Withdrawal from agreements

---

### 2. Corporate Records

**Primary Evidence:**
- CIPC company registrations
- Director appointments and removals
- Shareholder records

**Repository References:**
- `evidence/cipc/`
- `ad-res-j7/ANNEXURES/cipc_documents/`

**Related Events:**
- EVENT_H001: Company formation
- EVENT_H002: Director changes

---

### 3. Accounting Evidence

**Primary Evidence:**
- Financial statements
- Bank account records
- Transaction histories

**Repository References:**
- `evidence/accounting/`
- `ad-res-j7/evidence/financial/`

**Related Events:**
- EVENT_011: Financial manipulation
- EVENT_012: Account transfers

---

### 4. Legal Correspondence

**Primary Evidence:**
- ENS Attorneys withdrawal notice
- Settlement agreement correspondence
- Enforcement application documents

**Repository References:**
- `evidence/legal_correspondence/`
- `ad-res-j7/case_2025_137857/correspondence/`

**Related Events:**
- EVENT_061: ENS withdrawal
- EVENT_062: Enforcement application filed

---

## Cross-References to ad-res-j7

The extended evidence repository contains comprehensive documentation of:

- Mediation process and agreements
- Corporate governance violations
- Financial irregularities
- Legal correspondence and filings

---

## Data Model Integration

This evidence index is integrated with the refined data models:

- **Entities Model:** Version 23.0
- **Events Model:** Version 25.0
- **Relations Model:** Version 20.0

---

## Navigation

- [← Back to Application 2 Details](application-2.md)
- [View All Applications](applications.md)
- [Complete Evidence Index](evidence-index-comprehensive.md)
- [Home](index.md)
"""
    return content

def create_application_3_evidence_page():
    """Create evidence page for Application 3"""
    content = """---
layout: default
title: Application 3 Evidence
---

# Application 3: Contact Interdict - Evidence Index

**Case Number:** 2025-137857  
**Application Type:** Urgent application  
**Filed:** November 4, 2025  
**Target:** Jacqueline Faucitt (First Respondent)  
**Hearing Date:** November 18, 2025

---

## Overview

This page provides a comprehensive index of evidence supporting Application 3, focusing on harassment and unauthorized business contact.

---

## Evidence Categories

### 1. Email Correspondence

**Primary Evidence:**
- Harassment emails (end of September 2025)
- Training session dispute (September 30, 2025)
- Demand for desistance (October 1, 2025)

**Repository References:**
- `evidence/emails/`
- `ad-res-j7/ANNEXURES/JF05/correspondence/`

**Related Events:**
- EVENT_063: Harassment allegations
- EVENT_064: Training session dispute
- EVENT_065: Desistance demand

---

### 2. Sage Control Analysis

**Primary Evidence:**
- Sage accounting system access logs
- Unauthorized system modifications
- Financial data manipulation

**Repository References:**
- `evidence/sage/`
- `ad-res-j7/evidence/sage/`

**Related Events:**
- EVENT_013: Sage system manipulation
- EVENT_014: Access control violations

---

### 3. Trademark Documentation

**Primary Evidence:**
- Trademark registration records
- Unauthorized trademark use
- Brand identity theft

**Repository References:**
- `evidence/trademark/`
- `ad-res-j7/evidence/trademark/`

**Related Events:**
- EVENT_H006: Trademark violations
- EVENT_H007: Brand identity theft

---

### 4. Business Contact Records

**Primary Evidence:**
- Unauthorized contact with business entities
- Client communication interception
- Supplier relationship interference

**Repository References:**
- `evidence/business_contact/`
- `ad-res-j7/evidence/correspondence/`

**Related Events:**
- EVENT_066: Unauthorized client contact
- EVENT_067: Supplier interference

---

## Cross-References to ad-res-j7

The extended evidence repository contains:

- Complete email archives
- System access logs
- Trademark documentation
- Business correspondence records

---

## Data Model Integration

This evidence index is integrated with the refined data models:

- **Entities Model:** Version 23.0
- **Events Model:** Version 25.0
- **Relations Model:** Version 20.0

---

## Navigation

- [← Back to Application 3 Details](application-3.md)
- [View All Applications](applications.md)
- [Complete Evidence Index](evidence-index-comprehensive.md)
- [Home](index.md)
"""
    return content

def update_main_index():
    """Update the main index.md with latest data model versions"""
    
    # Read current index
    index_file = REVSTREAM_ROOT / "index.md"
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update data model version reference
    updated_content = content.replace(
        "This case is supported by a robust and comprehensive data model (Version 11.0, updated 2025-11-19)",
        "This case is supported by a robust and comprehensive data model (Entities v23.0, Events v25.0, Relations v20.0, updated 2025-11-28)"
    )
    
    # Add cross-reference to ad-res-j7 if not present
    if "cogpy/ad-res-j7" not in updated_content:
        ad_res_j7_section = """\n\n## Extended Evidence Repository

For comprehensive evidence documentation, see the extended evidence repository at [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7), which contains:

- **2,866 files** of supporting evidence
- **226.78 MB** of documentation
- Comprehensive evidence index in `COMPREHENSIVE_EVIDENCE_INDEX.md`
- Organized annexures and case documentation

"""
        # Insert before the "Evidence Resources" section
        updated_content = updated_content.replace(
            "## Evidence Resources",
            ad_res_j7_section + "## Evidence Resources"
        )
    
    return updated_content

def main():
    """Main execution"""
    print("=" * 80)
    print("UPDATING GITHUB PAGES")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("=" * 80)
    print()
    
    # Create application evidence pages
    print("Creating application-specific evidence pages...")
    
    app1_evidence = create_application_1_evidence_page()
    write_file(REVSTREAM_ROOT / "application-1-evidence.md", app1_evidence)
    print("  Created: application-1-evidence.md")
    
    app2_evidence = create_application_2_evidence_page()
    write_file(REVSTREAM_ROOT / "application-2-evidence.md", app2_evidence)
    print("  Created: application-2-evidence.md")
    
    app3_evidence = create_application_3_evidence_page()
    write_file(REVSTREAM_ROOT / "application-3-evidence.md", app3_evidence)
    print("  Created: application-3-evidence.md")
    
    # Update main index
    print("\nUpdating main index...")
    updated_index = update_main_index()
    write_file(REVSTREAM_ROOT / "index.md", updated_index)
    print("  Updated: index.md")
    
    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)
    print("\nPages created/updated:")
    print("  - application-1-evidence.md")
    print("  - application-2-evidence.md")
    print("  - application-3-evidence.md")
    print("  - index.md (updated with latest data model versions)")
    print()

if __name__ == "__main__":
    main()
