# Evidence Index

**Last Updated:** 2026-01-11  
**Total Evidence Files:** 368+

This index provides a comprehensive catalog of all evidence files in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).

---

## Evidence Categories

### ANNEXURES

| Category | File Count | Description |
|----------|-----------|-------------|
| **JF01** | 2 files | Shopify platform ownership evidence |
| **JF02** | 3 files | UK company documentation |
| **JF03** | 5 files | Identity documents |
| **JF04** | 6 files | CIPC company records |
| **JF05** | 7 files | Sage accounting system control |
| **JF06** | 5 files | Platform investment evidence |
| **JF07** | 186 files | Bank statements and financial records |
| **JF08** | 38 files | Email correspondence and fraud evidence |
| **JF09** | 8 files | Court order interference documentation |
| **JF10** | 3 files | Trust documents |
| **JF11** | 1 file | Additional evidence |
| **JF12** | 1 file | Additional evidence |
| **JF13** | 3 files | Additional evidence |
| **JF14-CIPC-2021** | 19 files | CIPC WinDeed documents (2021 batch 1) |
| **JF15-CIPC-BATCH2-2021** | 19 files | CIPC WinDeed documents (2021 batch 2) |
| **JF16-DISTRIBUTORS** | 28 files | Distributor network CIPC documents |

### Applications

| Category | File Count | Description |
|----------|-----------|-------------|
| **1-CIVIL-RESPONSE** | 25 files | Civil case documentation |
| **2-CRIMINAL-CASE** | 5 files | Criminal case submissions |
| **3-EXTERNAL-VALIDATION** | 4 files | External validation packages |

---

## Evidence by Application

### Application 1: Civil Response

Evidence files supporting the civil litigation response, including:

- Answering affidavit documentation
- Response annexures
- Supporting evidence for civil burden of proof (50%+)

**Evidence Location:** `ad-res-j7/1-CIVIL-RESPONSE/`

### Application 2: Criminal Case

Evidence files meeting the criminal burden of proof (95%+), including:

- Criminal case submissions
- High-threshold evidence documentation
- Supporting materials for criminal prosecution

**Evidence Location:** `ad-res-j7/2-CRIMINAL-CASE/`

### Application 3: External Validation

Evidence files for external regulatory complaints and validation, including:

- CIPC Companies Act complaints
- POPIA criminal complaints
- NPA tax fraud reports
- Commercial crime case submissions

**Evidence Location:** `ad-res-j7/3-EXTERNAL-VALIDATION/`

---

## Key Evidence Highlights

### High-Value Evidence Files

The following categories contain the most critical evidence:

1. **JF07 (186 files):** Comprehensive bank statements and financial records documenting unauthorized transfers and revenue diversion.

2. **JF08 (38 files):** Email correspondence showing impersonation patterns, fraud coordination, and unauthorized communications.

3. **JF16-DISTRIBUTORS (28 files):** CIPC documents mapping the distributor network and revealing the R3,110,000 bond on Karen Avnit's property.

4. **JF14-CIPC-2021 & JF15-CIPC-BATCH2-2021 (38 files):** Company registration documents establishing the Louw-Rizzotto network and shelf company acquisition patterns.

5. **JF05 (7 files):** Sage accounting system screenshots proving dual access and system control by Rynette Farrar.

---

## Evidence Repository Structure

The complete evidence repository is organized as follows:

```
ad-res-j7/
├── ANNEXURES/
│   ├── JF01/ - Shopify platform ownership
│   ├── JF02/ - UK company documentation
│   ├── JF03/ - Identity documents
│   ├── JF04/ - CIPC company records
│   ├── JF05/ - Sage accounting control
│   ├── JF06/ - Platform investment
│   ├── JF07/ - Bank statements (186 files)
│   ├── JF08/ - Email evidence (38 files)
│   ├── JF09/ - Court order interference
│   ├── JF10/ - Trust documents
│   ├── JF11/ - Additional evidence
│   ├── JF12/ - Additional evidence
│   ├── JF13/ - Additional evidence
│   ├── JF14-CIPC-2021/ - CIPC batch 1 (19 files)
│   ├── JF15-CIPC-BATCH2-2021/ - CIPC batch 2 (19 files)
│   └── JF16-DISTRIBUTORS/ - Distributor network (28 files)
├── 1-CIVIL-RESPONSE/ (25 files)
├── 2-CRIMINAL-CASE/ (5 files)
└── 3-EXTERNAL-VALIDATION/ (4 files)
```

---

## Accessing Evidence

All evidence files are available in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7). Each data model entry (entities, relations, events, timeline) includes direct references to the relevant evidence files using the `ad_res_j7_references` field.

---

## Evidence Cross-Referencing

The data models in this repository have been programmatically cross-referenced with the ad-res-j7 evidence repository. Each entity, relation, and timeline event includes:

- **Evidence:** List of evidence items supporting the claim.
- **ad_res_j7_references:** Direct file paths to evidence in the ad-res-j7 repository.
- **Evidence Strength:** Rating of the evidence quality (conclusive, strong, moderate, weak).
- **Burden of Proof:** Assessment of whether the evidence meets civil (50%+) or criminal (95%+) standards.

---

**For detailed evidence analysis, refer to the [Comprehensive Evidence Index](https://github.com/cogpy/ad-res-j7/blob/main/docs/evidence/COMPREHENSIVE_EVIDENCE_INDEX.md) in the ad-res-j7 repository.**
