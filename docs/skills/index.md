# LEX Legal Skills Framework

**Last Updated:** 2026-01-25

The LEX Skills Framework provides 128 legal reasoning skills across 7 domains for systematic case analysis. The full implementation is maintained in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7/tree/main/lex/skills).

---

## 📊 Framework Overview

| Metric | Value |
|--------|-------|
| **Total Skills** | 128 |
| **Legal Domains** | 7 |
| **Skills Applied to Case** | 85 (66% coverage) |
| **Criminal Threshold** | ✅ 95% EXCEEDED |
| **Civil Threshold** | ✅ 50% EXCEEDED |

---

## 🏛️ Legal Domains

| Domain | Skills | Key Application to Case 2025-137857 |
|--------|--------|-------------------------------------|
| **Criminal Law (CRI)** | 18 | Fraud elements, money laundering, tax fraud |
| **Forensic Investigation (FRN)** | 18 | Pattern detection, timeline reconstruction |
| **Evidence Law (EVID)** | 18 | Evidence chains, burden of proof |
| **Company Law (CMP)** | 20 | Director duties, CIPC compliance |
| **Trust Law (TRS)** | 18 | Trustee duties, beneficiary rights |
| **Data Protection (DAT)** | 18 | POPIA compliance, breach detection |
| **Civil Law (CIV)** | 18 | Contract breach, damages calculation |

---

## 📈 Case Application Summary

### Application 1: Civil & Criminal Actions

| Domain | Skills Applied | Key Findings |
|--------|----------------|--------------|
| Criminal Law | 12 | Fraud elements established (95% threshold exceeded) |
| Evidence Law | 15 | Evidence chains validated, weight calculated |
| Civil Law | 10 | Contract breaches established, damages calculated |

### Application 2: CIPC & POPIA Complaints

| Domain | Skills Applied | Key Findings |
|--------|----------------|--------------|
| Company Law | 14 | Director breaches documented, CIPC violations confirmed |
| Data Protection | 8 | POPIA violations identified, criminal offenses documented |

### Application 3: Commercial Crime & Tax Fraud

| Domain | Skills Applied | Key Findings |
|--------|----------------|--------------|
| Forensic | 16 | Fraud patterns detected, timeline reconstructed |
| Trust Law | 10 | Trustee breaches established, beneficiary rights violated |

---

## 🔗 Key Skills Applied

### Fraud Element Analysis (`cri-fraud-elements`)

| Element | Evidence | Assessment |
|---------|----------|------------|
| Misrepresentation | Fabricated accounts (JF03), False CIPC filings (JF04) | ✅ Established |
| Prejudice | R10,269,727.90 loss, ZAR 18.75M trust control | ✅ Established |
| Unlawful Benefit | Revenue diversion to Rynette-controlled accounts | ✅ Established |
| Intent | Systematic pattern over 24+ months | ✅ Established |

### Timeline Reconstruction (`frn-timeline`)

| Date | Event | T-Months to Payout |
|------|-------|-------------------|
| 2023-04-24 | FFT invests in Ketoni | T-37 |
| 2024-07 | Bantjies appointed FFT Trustee | T-10 |
| 2025-08-11 | Main Trustee power backdated | T-9 |
| 2026-05 | Ketoni ZAR 18.75M payout due | T-0 |

### Manufactured Crisis Detection (`frn-manufactured-crisis`)

| Crisis | Timing | Purpose |
|--------|--------|---------|
| Curatorship Application | T-9 months | Control Dan's 1/3 share (ZAR 6.25M) |
| Card Cancellation | <24 hours after fraud exposure | Financial control |
| Interdict Filing | 48 hours after Main Trustee signing | Neutralize Dan before payout |

---

## 📁 Source Files

The skill implementations are located in the ad-res-j7 repository:

```
ad-res-j7/
├── lex/                             # Active LEX framework
│   └── skills/                      # 128 legal reasoning skills
└── lexarc/                          # Archived versioned files (234 files)

ad-res-j7/lex/skills/
├── core/
│   ├── skill_framework.scm      # Core skill definitions
│   └── skill_registry.scm       # Unified skill registration
├── civ/civil_law_skills.scm     # Civil law skills
├── cri/criminal_law_skills.scm  # Criminal law skills
├── evid/evidence_law_skills.scm # Evidence law skills
├── cmp/company_law_skills.scm   # Company law skills
├── trs/trust_law_skills.scm     # Trust law skills
├── dat/data_protection_skills.scm # Data protection skills
├── frn/forensic_skills.scm      # Forensic skills
├── integration/
│   ├── skill_entity_integration.scm    # Entity integration
│   └── skill_timeline_integration.scm  # Timeline integration
└── README.md                    # Framework documentation
```

---

## 🔗 Related Documentation

- **[Full Skills Documentation](https://github.com/cogpy/ad-res-j7/tree/main/docs/skills)** - Complete skills reference
- **[Entity-Relation Model](https://github.com/cogpy/ad-res-j7/tree/main/lex/core)** - Core legal reasoning framework
- **[Evidence Index](./evidence-index-enhanced.md)** - Comprehensive evidence catalog
- **[Timeline Analysis](./timeline/)** - Event timeline documentation

---

*This framework is part of the LEX Legal Reasoning System and is continuously refined based on case analysis requirements.*

**Version:** 1.0  
**Source:** [ad-res-j7/lex/skills](https://github.com/cogpy/ad-res-j7/tree/main/lex/skills)
