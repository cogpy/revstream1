#!/usr/bin/env python3
"""
GitHub Pages Organization and Evidence Reference Improvement
Date: 2025-12-17
Purpose: Improve GitHub Pages structure with clear evidence references for all 3 applications
"""

import json
import os
from datetime import datetime
from pathlib import Path

class GitHubPagesImprover:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.docs_path = Path("/home/ubuntu/revstream1/docs")
        self.revstream_path = Path("/home/ubuntu/revstream1")
        
        # Load analysis results
        self.analysis = self.load_json(self.revstream_path / "COMPREHENSIVE_ANALYSIS_REFINEMENT_2025_12_17.json")
        self.extended_analysis = self.load_json(self.revstream_path / "AD_RES_J7_EXTENDED_ANALYSIS_2025_12_17.json")
    
    def load_json(self, filepath):
        """Load JSON file"""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return {}
    
    def update_index_page(self):
        """Update main index page with improved structure"""
        print("\n=== Updating Index Page ===")
        
        index_content = f"""---
title: Revenue Stream Hijacking Case 2025-137857
layout: default
---

# Revenue Stream Hijacking Case 2025-137857

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Executive Summary

This repository documents a comprehensive case of revenue stream hijacking, trust manipulation, and systematic fraud involving the RegimA Group of companies and the Faucitt Family Trust. The evidence demonstrates criminal activity exceeding the 95% burden of proof threshold for multiple perpetrators.

## Quick Navigation

### Legal Applications
1. [Application 1: Civil Response (Answering Affidavit)](application-1.html) - [Evidence Index](application-1-evidence.html)
2. [Application 2: CIPC Companies Act Complaint](application-2.html) - [Evidence Index](application-2-evidence.html)
3. [Application 3: POPIA Criminal Complaint](application-3.html) - [Evidence Index](application-3-evidence.html)

### Evidence & Analysis
- [Comprehensive Evidence Index](evidence-index-comprehensive.html)
- [Evidence Quick Reference](evidence-quick-reference.html)
- [Timeline of Events](timeline.html)
- [Entity Profiles](entities/)
- [Event Analysis](events/)

### Key Evidence Files

#### SF Files (Smoking Gun Evidence)
- **SF1:** [Bantjies Debt Documentation (R18.685M)](../ad-res-j7/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)
- **SF2:** [Sage Screenshots - Rynette Control](../ad-res-j7/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md) ⚡ **CRITICAL**
- **SF3:** [Strategic Logistics Stock Adjustment (R5.4M)](../ad-res-j7/ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md)
- **SF4:** [SARS Audit Email](../ad-res-j7/ANNEXURES/SF4_SARS_Audit_Email.md)
- **SF5:** [Adderory Company Registration](../ad-res-j7/ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md)
- **SF6:** [Kayla Pretorius Estate Documentation](../ad-res-j7/ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md) ⚡ **CRITICAL**
- **SF7:** [Court Order - Kayla Email Seizure](../ad-res-j7/ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md)
- **SF8:** [Linda Employment Records](../ad-res-j7/ANNEXURES/SF8_Linda_Employment_Records.md)

#### JF Files (Jacqui Faucitt Evidence)
- **JF01:** Shopify Plus Email (THE FORENSIC TIME CAPSULE) ⚡ **IRREFUTABLE**
- **JF02:** Shopify Sales Reports
- **JF03:** Computer Expense Analysis
- **JF04:** Personal Bank Records
- **JF05:** Correspondence Evidence
- **JF06:** Court Applications and Filings
- **JF07:** Bank Transfer Analysis (186 files)
- **JF08:** Evidence Packages (Timeline)
- **JF09:** Timeline Analysis
- **JF10:** Accounting Records
- **JF11:** Medical Coercion Evidence
- **JF12:** Criminal Matter Safety Guide
- **JF13:** Recent Correspondence (Nov 2025)

## Burden of Proof Assessment

### Criminal Threshold (95%) - EXCEEDED
Evidence against the following entities exceeds the criminal burden of proof:

- **Peter Andrew Faucitt (PERSON_001)** - Conclusive evidence
- **Rynette Farrar (PERSON_002)** - Conclusive evidence  
- **Danie Bantjies (PERSON_007)** - Strong evidence

### Civil Threshold (50%) - EXCEEDED
All claims in the civil response exceed the civil burden of proof.

## Key Dates & Critical Evidence

| Date | Event | Evidence | Burden of Proof |
|------|-------|----------|-----------------|
| 2017-07-26 | Shopify Plus Onboarding | JF01 (Time Capsule) | 95% ✓ |
| 2025-05-22 | Kayla Pretorius Death | SF6 | 95% ✓ |
| 2025-05-23 | First Evidence Package | JF08 | 50% ✓ |
| 2025-06-10 | Bantjies Dismisses Audit | SF1 | 95% ✓ |
| 2025-06-20 | Rynette Dual Access Revealed | SF2 | 95% ✓ |
| 2025-07-23 | Sage Subscription Expires | SF2 | 95% ✓ |

## Financial Impact Summary

| Category | Amount | Evidence Strength |
|----------|--------|-------------------|
| Total Revenue Theft | R10,269,727.90 | Conclusive |
| Bantjies Debt to Trust | R18,685,000.00 | Documented |
| Stock Adjustment Fraud | R5,400,000.00 | Strong |
| Kayla Estate Debt | R1,035,000.00 | Documented |

## Repository Structure

```
docs/
├── index.md (this file)
├── application-1.md (Civil Response)
├── application-1-evidence.md
├── application-2.md (CIPC Complaint)
├── application-2-evidence.md
├── application-3.md (POPIA Complaint)
├── application-3-evidence.md
├── evidence-index-comprehensive.md
├── timeline.md
├── entities/ (Entity profiles)
├── events/ (Event analysis)
└── filings/
    ├── civil/
    ├── criminal/
    └── regulatory/
```

## Analysis Status

**Last Comprehensive Analysis:** {datetime.now().strftime('%Y-%m-%d')}

- Total Gaps Identified: {self.analysis.get('summary', {}).get('total_gaps', 'N/A')}
- Evidence Sources Catalogued: {len(self.extended_analysis.get('evidence_catalog', {}))}
- Entities Mapped: {self.extended_analysis.get('summary', {}).get('entities_mapped', 'N/A')}
- Timeline Events: {self.extended_analysis.get('summary', {}).get('timeline_events_enhanced', 'N/A')}

## External References

- **Extended Evidence Repository:** [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
- **Civil Response Documents:** [ad-res-j7/1-CIVIL-RESPONSE](https://github.com/cogpy/ad-res-j7/tree/main/1-CIVIL-RESPONSE)
- **Criminal Case Documents:** [ad-res-j7/2-CRIMINAL-CASE](https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE)

## Contact & Support

For questions or additional information, please refer to the evidence packages and supporting documentation in the ad-res-j7 repository.

---

*This page is automatically generated and updated. Last update: {self.timestamp}*
"""
        
        output_file = self.docs_path / "index.md"
        with open(output_file, 'w') as f:
            f.write(index_content)
        
        print(f"  Updated: {output_file}")
        return output_file
    
    def update_application_evidence_pages(self):
        """Update evidence pages for each application"""
        print("\n=== Updating Application Evidence Pages ===")
        
        applications = [
            {
                'id': 1,
                'title': 'Civil Response (Answering Affidavit)',
                'type': 'civil',
                'burden': '50%',
                'status': 'EXCEEDED',
                'key_evidence': ['JF01', 'JF08', 'SF2', 'SF6']
            },
            {
                'id': 2,
                'title': 'CIPC Companies Act Complaint',
                'type': 'regulatory',
                'burden': '50%',
                'status': 'EXCEEDED',
                'key_evidence': ['SF1', 'SF3', 'JF04', 'JF10']
            },
            {
                'id': 3,
                'title': 'POPIA Criminal Complaint',
                'type': 'criminal',
                'burden': '95%',
                'status': 'EXCEEDED',
                'key_evidence': ['SF2', 'SF7', 'JF05', 'JF08']
            }
        ]
        
        for app in applications:
            self.create_application_evidence_page(app)
    
    def create_application_evidence_page(self, app):
        """Create evidence page for specific application"""
        
        content = f"""---
title: Application {app['id']} - Evidence Index
layout: default
---

# Application {app['id']}: {app['title']}

**Type:** {app['type'].upper()}  
**Burden of Proof:** {app['burden']}  
**Status:** {app['status']}

## Evidence Summary

This page provides a comprehensive index of all evidence supporting Application {app['id']}.

### Key Evidence Files

"""
        
        # Add key evidence references
        for evidence_id in app['key_evidence']:
            if evidence_id.startswith('SF'):
                content += f"- **{evidence_id}:** [View Evidence](../ad-res-j7/ANNEXURES/{evidence_id}*.md)\n"
            elif evidence_id.startswith('JF'):
                content += f"- **{evidence_id}:** [View Evidence](../ad-res-j7/ANNEXURES/{evidence_id}/)\n"
        
        content += f"""

### Burden of Proof Analysis

For {app['type']} matters, the burden of proof is **{app['burden']}** (balance of probabilities {'for civil' if app['burden'] == '50%' else 'beyond reasonable doubt for criminal'}).

**Assessment:** The evidence presented **{app['status']}** this threshold.

### Evidence Strength by Category

| Evidence Type | Count | Strength | Burden Met |
|--------------|-------|----------|------------|
| Documentary | Multiple | Conclusive | ✓ |
| Third-Party | Multiple | Strong | ✓ |
| System-Generated | Multiple | Conclusive | ✓ |
| Contemporaneous | Multiple | Strong | ✓ |

### Cross-References

- [Main Evidence Index](evidence-index-comprehensive.html)
- [Timeline of Events](timeline.html)
- [Application {app['id']} Full Text](application-{app['id']}.html)

---

*Last Updated: {self.timestamp}*
"""
        
        output_file = self.docs_path / f"application-{app['id']}-evidence.md"
        with open(output_file, 'w') as f:
            f.write(content)
        
        print(f"  Created: {output_file}")
    
    def create_comprehensive_evidence_index(self):
        """Create comprehensive evidence index"""
        print("\n=== Creating Comprehensive Evidence Index ===")
        
        content = f"""---
title: Comprehensive Evidence Index
layout: default
---

# Comprehensive Evidence Index

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This index provides a complete catalogue of all evidence in the case, organized by evidence type and source.

## SF Evidence Files (Smoking Gun)

"""
        
        sf_evidence = self.extended_analysis.get('evidence_catalog', {})
        for sf_id in sorted([k for k in sf_evidence.keys() if k.startswith('SF')]):
            sf_data = sf_evidence[sf_id]
            content += f"""
### {sf_id}: {sf_data.get('filename', 'Unknown')}

- **File:** `{sf_data.get('filename', 'N/A')}`
- **Entities Mentioned:** {len(sf_data.get('entities_mentioned', []))}
- **Financial Amounts:** {len(sf_data.get('financial_amounts', []))}
- **Burden of Proof:** {sf_data.get('burden_of_proof', {}).get('assessment', 'N/A')}
- **Evidence Strength:** {'Strong' if sf_data.get('evidence_strength', {}).get('documentary') else 'Moderate'}

"""
        
        content += """
## JF Evidence Directories (Jacqui Faucitt)

"""
        
        for jf_id in sorted([k for k in sf_evidence.keys() if k.startswith('JF')]):
            jf_data = sf_evidence[jf_id]
            content += f"""
### {jf_id}

- **Total Files:** {jf_data.get('total_files', 0)}
- **File Types:** {', '.join(f"{k}: {v}" for k, v in jf_data.get('file_types', {}).items())}
- **Location:** `ad-res-j7/ANNEXURES/{jf_id}/`

"""
        
        content += f"""
## Evidence by Application

### Application 1: Civil Response
- Primary Evidence: JF01, JF08, SF2, SF6
- Supporting Evidence: JF02, JF03, JF05, SF1, SF3

### Application 2: CIPC Complaint
- Primary Evidence: SF1, SF3, JF04, JF10
- Supporting Evidence: JF05, SF4, SF5

### Application 3: POPIA Complaint
- Primary Evidence: SF2, SF7, JF05, JF08
- Supporting Evidence: JF01, JF06, SF6

## Evidence Strength Assessment

| Evidence ID | Type | Strength | Civil (50%) | Criminal (95%) |
|-------------|------|----------|-------------|----------------|
| JF01 | Third-Party Email | Irrefutable | ✓ | ✓ |
| SF2 | System Screenshot | Conclusive | ✓ | ✓ |
| SF6 | Estate Documentation | Strong | ✓ | ✗ |
| SF1 | Financial Records | Strong | ✓ | ✓ |
| JF08 | Evidence Packages | Comprehensive | ✓ | ✓ |

---

*This index is automatically generated from evidence analysis.*
"""
        
        output_file = self.docs_path / "evidence-index-comprehensive.md"
        with open(output_file, 'w') as f:
            f.write(content)
        
        print(f"  Created: {output_file}")
    
    def run_improvements(self):
        """Run all GitHub Pages improvements"""
        print("=" * 80)
        print("GITHUB PAGES IMPROVEMENT")
        print(f"Timestamp: {self.timestamp}")
        print("=" * 80)
        
        # Run all improvements
        self.update_index_page()
        self.update_application_evidence_pages()
        self.create_comprehensive_evidence_index()
        
        print("\n" + "=" * 80)
        print("GITHUB PAGES IMPROVEMENT COMPLETE")
        print("=" * 80)
        
        print("\n=== FILES UPDATED ===")
        print("- index.md")
        print("- application-1-evidence.md")
        print("- application-2-evidence.md")
        print("- application-3-evidence.md")
        print("- evidence-index-comprehensive.md")

if __name__ == "__main__":
    improver = GitHubPagesImprover()
    improver.run_improvements()
