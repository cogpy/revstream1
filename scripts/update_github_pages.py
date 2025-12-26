#!/usr/bin/env python3
"""
Update GitHub Pages documentation with latest evidence and filings
"""
from datetime import datetime
from pathlib import Path

def write_file(filepath, content):
    """Write text file"""
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated: {filepath}")

def update_index():
    """Update main index page"""
    
    content = f"""# Revenue Stream Hijacking Case 2025-137857
## Evidence-Based Legal Documentation Portal

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Case Status:** Active Legal Proceedings  
**Evidence Strength:** STRONG (Civil 50%+ / Criminal 95%+)

---

## 🎯 Quick Navigation

### Evidence & Analysis
- [**Legal Filings Summary**](../LEGAL_FILINGS_SUMMARY_2025_12_10.md) - Comprehensive overview of all filings
- [**Burden of Proof Assessment**](../BURDEN_OF_PROOF_ASSESSMENT_2025_12_10.json) - Detailed threshold analysis
- [**Evidence Index**](evidence-index-enhanced.html) - Complete evidence catalog
- [**Timeline Visualization**](timeline.html) - Interactive case timeline

### Data Models (Updated 2025-12-10)
- [**Entities**](../data_models/entities/entities_refined_2025_12_10_v14.json) - All persons and organizations (v14)
- [**Relations**](../data_models/relations/relations_refined_2025_12_10_v24.json) - Entity relationships (v24)
- [**Events**](../data_models/events/events_refined_2025_12_10_v34.json) - Chronological events (v34)
- [**Timeline**](../data_models/timelines/timeline_refined_2025_12_10_v23.json) - Timeline entries (v23)

### Legal Filings (Updated 2025-12-10)

#### Civil Actions (50% Burden of Proof - EXCEEDED)
- [**Answering Affidavit**](../ANSWERING_AFFIDAVIT_REFINED_2025_12_10.md) - Main civil response
- [**CIPC Complaint**](../CIPC_COMPLAINT_REFINED_2025_12_10.md) - Companies Act violations

#### Criminal Actions (95% Burden of Proof - ACHIEVABLE)
- [**Commercial Crime Submission**](../COMMERCIAL_CRIME_REFINED_2025_12_10.md) - Theft R63M + Identity Impersonation
- [**POPIA Complaint**](../POPIA_COMPLAINT_REFINED_2025_12_10.md) - Data protection violations
- [**NPA Tax Fraud Report**](../NPA_TAX_FRAUD_REPORT_2025_12_10.md) - R63M+ undeclared revenue

---

## 📊 Case Overview

### Key Perpetrators

| Perpetrator | Criminal Claims (95%) | Civil Claims (50%) | Evidence Strength |
|-------------|----------------------|-------------------|-------------------|
| **Peter Faucitt** | Theft R63M | Trust breach, Unauthorized transfers | **STRONG** |
| **Rynette Farrar** | Identity impersonation | Payment redirection, Obstruction | **STRONG** |
| **Danie Bantjies** | - | Conspiracy, Conflict of interest | **MODERATE** |

### Financial Impact

| Category | Amount | Evidence |
|----------|--------|----------|
| **Revenue Theft** | R63M+ | SF9, JF1, JF2 |
| **Unauthorized Transfers** | R900K | Bank records |
| **Payment Redirection** | R4.3M | SF2, JF7, JF9 |
| **Total Documented** | **R68M+** | Multiple sources |

---

## 🔍 Evidence Classification

### CRITICAL Evidence (Must-Review)
| Annexure | Description | Impact | Size |
|----------|-------------|--------|------|
| **JF1** | Shopify Plus Email (26 July 2017) - THE FORENSIC TIME CAPSULE | Proves ownership | 100 KB |
| **SF2A** | Sage User Access - Rynette Dual Accounts (June 2025) | Identity impersonation | 53 KB |
| **SF2B** | Sage Subscription Expiry - Rynette Owner (August 2025) | Obstruction of access | 51 KB |
| **SF9** | Attorney Letter to KEIRO re R63M Payment (October 2025) | Theft quantum | 1.4 MB |

### HIGH Priority Evidence
| Annexure | Description | Priority | Size |
|----------|-------------|----------|------|
| **JF2** | Shopify Sales Reports | HIGH | 3.3 MB |
| **JF3** | Financial Records and Analysis | HIGH | 572 KB |
| **JF4** | Daniel Faucitt Personal Bank Records | HIGH | 812 KB |
| **JF6** | Court Documents and Filings | HIGH | 7.4 MB |
| **JF8** | Evidence Packages (May-October 2025) | HIGH | 5.8 MB |
| **JF9** | Timeline Analysis | HIGH | 128 KB |
| **JF10** | Legal Analysis and Opinions | HIGH | - |
| **SF6** | Kayla Pretorius Estate Documentation | HIGH | - |
| **SF7** | Court Order - Kayla Email Seizure | HIGH | - |

### MEDIUM Priority Evidence
| Annexure | Description | Priority | Size |
|----------|-------------|----------|------|
| **JF5** | Correspondence Evidence (JF8 Series) | MEDIUM | 132 KB |
| **JF7** | Screenshots and Visual Evidence | MEDIUM | 22 MB |
| **JF11** | Supporting Documentation | MEDIUM | - |
| **JF12** | Additional Evidence | MEDIUM | - |
| **SF1** | Bantjies Debt Documentation | MEDIUM | - |
| **SF1A** | Bantjies Call Option Agreement Excerpt | MEDIUM | 181 KB |
| **SF3** | Strategic Logistics Stock Adjustment | MEDIUM | - |
| **SF4** | SARS Audit Email | MEDIUM | - |
| **SF5** | Adderory Company Registration & Stock Supply | MEDIUM | - |
| **SF8** | Linda Employment Records | MEDIUM | - |
| **SF10** | Sales Workflow PowerPoint | MEDIUM | - |

---

## 📈 Burden of Proof Analysis

### Civil Claims (50% Standard - Balance of Probabilities)
✅ **5 of 6 claims EXCEED 50% threshold**

1. **Trust Breach** - 90%+ confidence
2. **Unauthorized Transfers (R900K)** - 85%+ confidence
3. **Payment Redirection (R4.3M)** - 80%+ confidence
4. **Obstruction of Access** - 90%+ confidence
5. **Conflict of Interest (Bantjies)** - 80%+ confidence

### Criminal Claims (95% Standard - Beyond Reasonable Doubt)
✅ **2 of 2 claims ACHIEVE 95% threshold**

1. **Theft (R63M)** - Peter Faucitt - 95%+ confidence
   - Evidence: SF9, JF1, JF2
   - Quantum: R60,251,961.60 + $150,000

2. **Identity Impersonation** - Rynette Farrar - 95%+ confidence
   - Evidence: SF2A (dual account access)
   - Criminal element: Using Pete@regima.com

---

## 🗂️ Repository Statistics

**revstream1 Repository:**
- Data Models: 4 components (entities, relations, events, timelines)
- Legal Filings: 6 major documents
- Evidence Cross-References: 100+ references
- Total Analysis Files: 50+

**ad-res-j7 Evidence Repository:**
- Total Files: 2,866
- Total Size: 226.78 MB
- Annexures: 12 (JF1-JF12, SF1-SF10)
- Evidence Documents: 536 files

---

## 🔗 External Resources

- [**ad-res-j7 Repository**](https://github.com/cogpy/ad-res-j7) - Full evidence repository
- [**Comprehensive Evidence Index**](https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md) - Complete file catalog
- [**Annexures Index**](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/ANNEXURES_INDEX.md) - Evidence package details

---

## 📋 Application Tracking

### Civil Application (Case 2025-137857)
- **Court:** High Court
- **Applicant:** Peter Andrew Faucitt
- **First Respondent:** Jacqueline Faucitt
- **Second Respondent:** Daniel James Faucitt
- **Status:** Answering affidavit filed

### Criminal Complaints
1. **Commercial Crime** - Theft R63M + Identity Impersonation
2. **POPIA Violation** - Unauthorized data access and processing
3. **Tax Fraud** - R63M+ undeclared revenue

### Regulatory Complaints
1. **CIPC** - Companies Act violations (director misconduct)

---

## 🎓 How to Use This Portal

1. **Start with the [Legal Filings Summary](../LEGAL_FILINGS_SUMMARY_2025_12_10.md)** for an overview
2. **Review [Burden of Proof Assessment](../BURDEN_OF_PROOF_ASSESSMENT_2025_12_10.json)** for detailed analysis
3. **Explore specific evidence** using the annexure quick reference above
4. **Dive into data models** for entity-relation-event mapping
5. **Cross-reference with [ad-res-j7](https://github.com/cogpy/ad-res-j7)** for full evidence

---

## 📝 Document Versions

All documents are version-controlled with dates:
- **2025-12-10:** Latest refinement with burden of proof assessments
- **2025-12-09:** SF9 integration (R63M payment demand)
- **2025-12-08:** SF2A/SF2B integration (Rynette impersonation)
- **2025-12-07:** Enhanced evidence cross-references
- **Earlier versions:** Available in repository history

---

## ⚖️ Legal Notice

This documentation portal contains evidence and legal filings for active legal proceedings. All information is based on documented evidence and factual analysis. The burden of proof assessments are professional opinions based on available evidence and legal standards.

**Case Number:** 2025-137857  
**Jurisdiction:** South Africa  
**Legal Standards Applied:** South African law (civil and criminal)

---

*This portal is automatically maintained and updated as new evidence and analysis becomes available.*

**Last Evidence Integration:** 2025-12-10 (SF1-SF10, JF1-JF12)  
**Next Scheduled Update:** As evidence emerges

---

## Entity Relationship Diagram

```mermaid
graph TD;
    subgraph "Ownership Relations"
        PERSON_005[Daniel Faucitt] -->|owns| ORG_003[RegimA Zone UK Ltd];
        ORG_003 -->|owns| PLATFORM_001[Shopify Platform];
        ORG_003 -->|owns| DOMAIN_001[regima.zone];
        PERSON_003[Rynette's Daughter] -->|fraudulent_ownership| DOMAIN_002[regimazone.com];
    end
    
    subgraph "Control Relations"
        PERSON_001[Peter Faucitt] -->|directorial_control| ORG_001[RWW];
        PERSON_002[Rynette Farrar] -->|financial_controller| SYSTEMS[Sage/Accounting];
        PERSON_002 -->|subscription_owner| SAGE[Sage Subscription];
        PERSON_002 -->|impersonates| PERSON_001;
    end
    
    subgraph "Conspiracy Relations"
        PERSON_001 ---|co-conspirators| PERSON_002;
        PERSON_002 ---|co-conspirators| PERSON_003;
        PERSON_007[Danie Bantjies] ---|co-conspirators| PERSON_001;
    end
    
    subgraph "Financial Impact"
        PERSON_001 -->|theft_R63M| PERSON_005;
        PERSON_001 -->|unauthorized_R900K| PERSON_005;
        PERSON_002 -->|redirection_R4.3M| PERSON_005;
    end
    
    style PERSON_001 fill:#ff6b6b
    style PERSON_002 fill:#ff6b6b
    style PERSON_007 fill:#ffa500
    style PERSON_005 fill:#51cf66
```

---

**Maintained by:** Case 2025-137857 Legal Team  
**Repository:** [cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Evidence Repository:** [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    write_file("docs/index.md", content)

def main():
    """Main update function"""
    print("=" * 80)
    print("UPDATING GITHUB PAGES DOCUMENTATION")
    print("=" * 80)
    
    # Ensure docs directory exists
    Path("docs").mkdir(exist_ok=True)
    
    print("\n[1/1] Updating main index page...")
    update_index()
    
    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)
    print("\nUpdated files:")
    print("  - docs/index.md")
    print("\nGitHub Pages will be automatically deployed on push.")

if __name__ == "__main__":
    main()
