#!/usr/bin/env python3
"""
GitHub Pages Organization Improvement Script
Improves evidence references and organization across all application pages
"""

import json
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("/home/ubuntu/revstream1")
DOCS_DIR = BASE_DIR / "docs"
AD_RES_J7_BASE_URL = "https://github.com/cogpy/ad-res-j7/blob/main"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_file(filepath):
    """Read text file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write text file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def improve_application_evidence_pages():
    """Improve application evidence pages with better organization"""
    
    improvements = []
    
    # Application 1 Evidence Page
    app1_evidence_file = DOCS_DIR / "application-1-evidence.md"
    if app1_evidence_file.exists():
        content = read_file(app1_evidence_file)
        
        # Add comprehensive evidence index reference at top if not present
        if "COMPREHENSIVE_EVIDENCE_INDEX.md" not in content:
            header_addition = f"""
**Complete Evidence Repository:** [ad-res-j7](https://github.com/cogpy/ad-res-j7) (22,872 files, 226.78 MB)  
**Comprehensive Evidence Index:** [COMPREHENSIVE_EVIDENCE_INDEX.md]({AD_RES_J7_BASE_URL}/COMPREHENSIVE_EVIDENCE_INDEX.md)

---

"""
            # Find the first heading after the front matter
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('# ') and i > 5:  # Skip front matter
                    insert_pos = i
                    break
            
            if insert_pos > 0:
                lines.insert(insert_pos + 1, header_addition)
                content = '\n'.join(lines)
                write_file(app1_evidence_file, content)
                improvements.append("Added comprehensive evidence index to Application 1 evidence page")
    
    # Application 2 Evidence Page
    app2_evidence_file = DOCS_DIR / "application-2-evidence.md"
    if app2_evidence_file.exists():
        content = read_file(app2_evidence_file)
        
        if "COMPREHENSIVE_EVIDENCE_INDEX.md" not in content:
            header_addition = f"""
**Complete Evidence Repository:** [ad-res-j7](https://github.com/cogpy/ad-res-j7) (22,872 files, 226.78 MB)  
**Comprehensive Evidence Index:** [COMPREHENSIVE_EVIDENCE_INDEX.md]({AD_RES_J7_BASE_URL}/COMPREHENSIVE_EVIDENCE_INDEX.md)

---

"""
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('# ') and i > 5:
                    insert_pos = i
                    break
            
            if insert_pos > 0:
                lines.insert(insert_pos + 1, header_addition)
                content = '\n'.join(lines)
                write_file(app2_evidence_file, content)
                improvements.append("Added comprehensive evidence index to Application 2 evidence page")
    
    # Application 3 Evidence Page
    app3_evidence_file = DOCS_DIR / "application-3-evidence.md"
    if app3_evidence_file.exists():
        content = read_file(app3_evidence_file)
        
        if "COMPREHENSIVE_EVIDENCE_INDEX.md" not in content:
            header_addition = f"""
**Complete Evidence Repository:** [ad-res-j7](https://github.com/cogpy/ad-res-j7) (22,872 files, 226.78 MB)  
**Comprehensive Evidence Index:** [COMPREHENSIVE_EVIDENCE_INDEX.md]({AD_RES_J7_BASE_URL}/COMPREHENSIVE_EVIDENCE_INDEX.md)

---

"""
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('# ') and i > 5:
                    insert_pos = i
                    break
            
            if insert_pos > 0:
                lines.insert(insert_pos + 1, header_addition)
                content = '\n'.join(lines)
                write_file(app3_evidence_file, content)
                improvements.append("Added comprehensive evidence index to Application 3 evidence page")
    
    return improvements

def create_evidence_quick_reference():
    """Create a quick reference guide for evidence access"""
    
    quick_ref_content = """---
layout: default
title: Evidence Quick Reference
---

# Evidence Quick Reference Guide

This page provides quick access to all evidence organized by category and application.

**Last Updated:** 2025-11-25  
**Total Evidence Files:** 22,872 files (226.78 MB)  
**Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)

---

## Quick Links

### By Application

- **[Application 1 Evidence](application-1-evidence.md)** - Ex Parte Interdict (45 events)
- **[Application 2 Evidence](application-2-evidence.md)** - Settlement Enforcement (50 events)
- **[Application 3 Evidence](application-3-evidence.md)** - Contact Interdict (20 events)

### By Evidence Category

#### Primary Evidence Collections

| Category | Files | Direct Link |
|----------|-------|-------------|
| **ANNEXURES** | 274 | [Browse ANNEXURES](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES) |
| **FINAL_AFFIDAVIT_PACKAGE** | 270 | [Browse Package](https://github.com/cogpy/ad-res-j7/tree/main/FINAL_AFFIDAVIT_PACKAGE) |
| **case_2025_137857** | 259 | [Browse Case Files](https://github.com/cogpy/ad-res-j7/tree/main/case_2025_137857) |
| **evidence** | 492 | [Browse Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence) |
| **docs** | 578 | [Browse Documentation](https://github.com/cogpy/ad-res-j7/tree/main/docs) |

#### Evidence by Type

**Financial Evidence:**
- [Shopify Invoices](https://github.com/cogpy/ad-res-j7/tree/main/evidence/shopify_invoices)
- [Bank Statements](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF04)
- [Accounting Records](https://github.com/cogpy/ad-res-j7/tree/main/evidence/accounting)
- [Fabricated Accounts](https://github.com/cogpy/ad-res-j7/tree/main/evidence/fake_accounts)

**Corporate Evidence:**
- [CIPC Records](https://github.com/cogpy/ad-res-j7/tree/main/evidence/cipc)
- [Company Documents](https://github.com/cogpy/ad-res-j7/tree/main/evidence/company_docs)
- [Trust Documents](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF01)

**Communication Evidence:**
- [Email Archives](https://github.com/cogpy/ad-res-j7/tree/main/evidence/emails)
- [Correspondence](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF05)

**Legal Evidence:**
- [Court Applications](https://github.com/cogpy/ad-res-j7/tree/main/case_2025_137857)
- [Affidavits](https://github.com/cogpy/ad-res-j7/tree/main/FINAL_AFFIDAVIT_PACKAGE)
- [Legal Analysis](https://github.com/cogpy/ad-res-j7/tree/main/docs)

**Technical Evidence:**
- [Shopify Platform](https://github.com/cogpy/ad-res-j7/tree/main/evidence/shopify)
- [IT Services](https://github.com/cogpy/ad-res-j7/tree/main/evidence/it_services)
- [POPIA Violations](https://github.com/cogpy/ad-res-j7/tree/main/evidence/popia)

---

## Evidence by Event Timeline

### Phase 0: Historical Foundation (2017-2021)
- [Business Relationship Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/business_relationship)
- [Financial Structure Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/financial_structure)

### Phase 1: Foundation Phase (March 2025)
- [Trust Manipulation Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/trust_violations)
- [Revenue Diversion Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/revenue_theft)

### Phase 2: Initial Theft Phase (April 2025)
- [Payment Redirection Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/payment_redirection)
- [Bank Account Changes](https://github.com/cogpy/ad-res-j7/tree/main/evidence/banking)

### Phase 3: Escalation Phase (May 2025)
- [Evidence Destruction](https://github.com/cogpy/ad-res-j7/tree/main/evidence/evidence_destruction)
- [Domain Fraud](https://github.com/cogpy/ad-res-j7/tree/main/evidence/domain_fraud)

### Phase 4: Consolidation Phase (June 2025)
- [Card Cancellation Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/card_cancellation)
- [Fabricated Accounts](https://github.com/cogpy/ad-res-j7/tree/main/evidence/fake_accounts)

### Phase 5: Control Seizure Phase (July 2025)
- [POPIA Violations](https://github.com/cogpy/ad-res-j7/tree/main/evidence/popia)
- [System Control Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/system_control)

### Phase 6: Cover-up Phase (August-September 2025)
- [Interdict Applications](https://github.com/cogpy/ad-res-j7/tree/main/case_2025_137857)
- [Mediation Evidence](https://github.com/cogpy/ad-res-j7/tree/main/evidence/mediation)

---

## Evidence by Legal Standard

### Criminal Evidence (95% Burden of Proof)

**Fraud Evidence:**
- Fabricated 2019 financial statements
- CIPC records proving impossibility
- Accountant correspondence

**Theft Evidence:**
- R10.27M documented losses
- Payment diversion records
- Bank account manipulation

**POPIA Violations:**
- Unauthorized data access
- System control seizure
- Privacy breaches

### Civil Evidence (50% Balance of Probabilities)

**Trust Violations:**
- Trustee misconduct
- Beneficiary exclusion
- Asset misappropriation

**Delictual Claims:**
- Financial harm quantification
- Business interruption
- Reputational damage

---

## Comprehensive Evidence Index

**Full Catalog:** [COMPREHENSIVE_EVIDENCE_INDEX.md](https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md)

The comprehensive evidence index provides:
- Complete file listing (22,872 files)
- Evidence code references (JF, JAX, DJF)
- File categorization and metadata
- Size and format information

---

## Evidence Statistics

### Files by Category

| Category | File Count | Total Size |
|----------|------------|------------|
| Documents | 1,080 | 50.61 MB |
| Evidence | 536 | 79.27 MB |
| Configuration/Data | 356 | 8.90 MB |
| Jax Response | 302 | 2.60 MB |
| Scripts/Tools | 184 | 2.66 MB |
| Images | 138 | 46.45 MB |
| Analysis | 121 | 2.71 MB |
| Other | 69 | 3.17 MB |
| Civil Response | 21 | 422.59 KB |
| Email Correspondence | 17 | 27.46 MB |

### Top File Extensions

| Extension | File Count | Total Size |
|-----------|------------|------------|
| .md | 1,492 | 15.08 MB |
| .json | 618 | 10.54 MB |
| .jpg | 252 | 87.03 MB |
| .pdf | 92 | 70.93 MB |
| .PDF | 44 | 1.61 MB |

---

**Repository:** [github.com/cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Extended Evidence:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)  
**Last Updated:** 2025-11-25
"""
    
    quick_ref_file = DOCS_DIR / "evidence-quick-reference.md"
    write_file(quick_ref_file, quick_ref_content)
    
    return "Created evidence quick reference guide"

def main():
    """Main improvement function"""
    print("Improving GitHub Pages organization...")
    
    improvements = []
    
    # Improve application evidence pages
    app_improvements = improve_application_evidence_pages()
    improvements.extend(app_improvements)
    
    # Create evidence quick reference
    quick_ref_improvement = create_evidence_quick_reference()
    improvements.append(quick_ref_improvement)
    
    # Update index.md to include quick reference link
    index_file = DOCS_DIR / "index.md"
    if index_file.exists():
        content = read_file(index_file)
        if "evidence-quick-reference.md" not in content:
            # Add link in evidence resources section
            content = content.replace(
                "## Evidence Resources",
                "## Evidence Resources\n\n**[📚 Evidence Quick Reference Guide](evidence-quick-reference.md)** - Fast access to all evidence by category, application, and timeline phase\n"
            )
            write_file(index_file, content)
            improvements.append("Added evidence quick reference link to index.md")
    
    print(f"\n{'='*60}")
    print("GITHUB PAGES IMPROVEMENTS COMPLETE")
    print(f"{'='*60}")
    print(f"\nImprovements Made:")
    for i, improvement in enumerate(improvements, 1):
        print(f"  {i}. {improvement}")
    
    print(f"\nTotal Improvements: {len(improvements)}")

if __name__ == "__main__":
    main()
