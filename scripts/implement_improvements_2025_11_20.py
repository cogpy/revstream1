#!/usr/bin/env python3
"""
Implement Improvements Based on Timeline Analysis
Version: 2025-11-20
Purpose: Fix event categorization and enhance GitHub Pages
"""

import json
from pathlib import Path
from datetime import datetime

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def categorize_event(event):
    """Categorize events based on description and characteristics"""
    description = event.get("description", "").lower()
    title = event.get("title", "").lower()
    
    # Determine crime category
    if "theft" in description or "stolen" in description or "hijack" in description:
        crime_category = "revenue_theft"
    elif "trust" in description or "trustee" in description or "fiduciary" in description:
        crime_category = "trust_violations"
    elif "fraud" in description or "fabricat" in description or "false" in description:
        crime_category = "fraud"
    elif "account" in description or "bank" in description or "transfer" in description:
        crime_category = "financial_manipulation"
    elif "email" in description or "popia" in description or "data" in description:
        crime_category = "data_violations"
    elif "evidence" in description and ("destroy" in description or "conceal" in description):
        crime_category = "evidence_destruction"
    elif "invoice" in description or "payment" in description or "business" in description:
        crime_category = "business_relationship"
    else:
        crime_category = "other"
    
    # Determine phase based on timeline_phase or date
    phase = event.get("timeline_phase", "PHASE_001")
    
    return crime_category, phase

def enhance_events(events_data):
    """Enhance events with proper categorization"""
    updated_count = 0
    
    for event in events_data["events"]:
        crime_category, phase = categorize_event(event)
        
        # Update if currently unknown
        if event.get("crime_category") == "unknown" or not event.get("crime_category"):
            event["crime_category"] = crime_category
            updated_count += 1
        
        if event.get("phase") == "unknown" or not event.get("phase"):
            event["phase"] = phase
            updated_count += 1
    
    events_data["metadata"]["last_updated"] = datetime.now().isoformat()
    events_data["metadata"]["changes"] = f"Updated categorization for {updated_count} fields"
    
    return events_data, updated_count

def create_application_evidence_pages(base_path, ad_res_j7_path):
    """Create application-specific evidence pages"""
    
    pages = {}
    
    # Application 1 Evidence Page
    app1_content = """---
layout: default
title: Application 1 Evidence
---

# Application 1: Ex Parte Interdict - Evidence Index

[← Back to Application 1](application-1.md) | [Home](index.md)

## POPIA Violations Evidence

### Primary Evidence Files
- **POPIA Violation Notice (July 8, 2025)** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - File: `POPIAViolationNotice-SenttoPeteon8July2025-DanielFaucitt-Outlook.pdf`
  - Significance: Demonstrates retaliatory motive for interdict filing
  - Timeline: Filed 36 days before Application 1

- **SA Legislation Compliance Guide** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - File: `SALegislation-DanielFaucitt-Outlook.pdf`
  - Significance: Shows Daniel's compliance efforts

## Shopify Platform Ownership Evidence

### Platform Ownership Documentation
- **Shopify Payment Records (28+ months)** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - Evidence of continuous UK company funding (R140K-R280K total)
  - Platform owned by RegimA Zone Ltd (UK) since July 2023
  - **Critical Implication:** RWD ZA has no independent revenue stream

### Related Evidence
- Revenue stream analysis documents
- Company registration (UK)
- Payment invoices and receipts

## Trustee Misconduct Evidence

### Email Correspondence
- **Trustee Correspondence - ID Copy Request** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - File: `TrusteeCorrespondence-IDCopyRequest-DanielFaucitt-Outlook.pdf`
  
- **Operating Entity Lists** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - Files: `OperatingEntityLists-DanielFaucitt-Outlook.pdf`
  - Shows corporate structure and relationships

## ReZonance Payment System Evidence

### Payment System Documentation
- ReZonance invoice history
- Payment redirection evidence
- Bank account manipulation records

---

**Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    # Application 2 Evidence Page
    app2_content = """---
layout: default
title: Application 2 Evidence
---

# Application 2: Settlement Agreement Enforcement - Evidence Index

[← Back to Application 2](application-2.md) | [Home](index.md)

## Mediation Documentation

### Mediation Records
- **Mediation Agreement (September 18, 2025)** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - Agreements reached at mediation
  - Medical assessments (drug screening, psychiatric evaluation)
  - Forensic investigations into entity affairs

### Withdrawal Documentation
- **Respondents Withdrawal (September 22, 2025)** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
- **ENS Attorneys Withdrawal (September 23, 2025)** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)

## Corporate Records (CIPC)

### Company Registration Evidence
- CIPC registration documents
- Director information
- Company status records

## Accounting Evidence

### Financial Records
- Trial balance documents
- Accounting system access logs
- Financial statement analysis

---

**Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    # Application 3 Evidence Page
    app3_content = """---
layout: default
title: Application 3 Evidence
---

# Application 3: Contact Interdict - Evidence Index

[← Back to Application 3](application-3.md) | [Home](index.md)

## Email Correspondence Evidence

### Harassment Timeline
- **End of September 2025:** Harassment allegations begin
- **September 30, 2025:** Training session dispute
- **October 1, 2025:** Correspondence demanding desistance

### Email Evidence Files
- Email correspondence showing harassment pattern
- Training session documentation
- Desistance demand letters

## Sage Control Analysis

### Sage System Evidence
- **Sage Account Screenshots** - [View in ad-res-j7](https://github.com/cogpy/ad-res-j7)
  - File: `Screenshot-2025-08-25-Sage-Account-RegimA-Worldwide-Distribution.jpg`
  - File: `Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.json`

### Control Analysis
- System access logs
- Account manipulation evidence
- Control timeline

## Trademark Documentation

### Trademark Evidence
- Trademark registration documents
- Usage evidence
- Ownership documentation

---

**Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    pages["application-1-evidence.md"] = app1_content
    pages["application-2-evidence.md"] = app2_content
    pages["application-3-evidence.md"] = app3_content
    
    return pages

def main():
    base_path = Path("/home/ubuntu/revstream1")
    data_models_path = base_path / "data_models"
    docs_path = base_path / "docs"
    ad_res_j7_path = Path("/home/ubuntu/ad-res-j7")
    
    print("="*80)
    print("IMPLEMENTING IMPROVEMENTS")
    print("="*80)
    
    # Load and enhance events
    print("\n1. Enhancing event categorization...")
    events = load_json(data_models_path / "events/events_refined_2025_11_20_v6.json")
    enhanced_events, update_count = enhance_events(events)
    
    # Save enhanced events
    output_path = data_models_path / "events/events_refined_2025_11_20_v7.json"
    save_json(enhanced_events, output_path)
    print(f"   ✓ Updated {update_count} event fields")
    print(f"   ✓ Saved to: {output_path}")
    
    # Create application evidence pages
    print("\n2. Creating application-specific evidence pages...")
    evidence_pages = create_application_evidence_pages(base_path, ad_res_j7_path)
    
    for filename, content in evidence_pages.items():
        page_path = docs_path / filename
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✓ Created: {page_path}")
    
    print("\n" + "="*80)
    print("IMPROVEMENTS COMPLETED")
    print("="*80)
    print(f"\nSummary:")
    print(f"  - Enhanced events: {update_count} fields updated")
    print(f"  - Created {len(evidence_pages)} application evidence pages")
    print(f"\nNext steps:")
    print(f"  - Review the enhanced events file")
    print(f"  - Update application pages to link to evidence pages")
    print(f"  - Sync changes to GitHub repository")

if __name__ == "__main__":
    main()
