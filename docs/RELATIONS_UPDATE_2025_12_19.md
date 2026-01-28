# Entity Relations Update - 2025-12-19

**Repository:** cogpy/revstream1  
**Evidence Source:** cogpy/ad-res-j7  
**Date:** December 19, 2025

---

## New Relations Identified

### Relation 1: Bantjies → Faucitt Family Trust (DEBTOR)

**Source Entity:** PERSON_007 (Danie Bantjies)  
**Target Entity:** TRUST_001 (Faucitt Family Trust)  
**Relation Type:** DEBTOR  
**Amount:** R18.75M (Ketoni debt to FFT)

**Evidence:** SF1 - Ketoni R18.75M Payout to FFT Documentation

**Burden of Proof Assessment:**
- **Civil Standard:** HIGH
- **Criminal Standard:** MEDIUM
- **Evidence Type:** Documentary, financial records

**Significance:**

This debt creates a fundamental conflict of interest. Bantjies simultaneously held three incompatible positions:

1. **As Trustee:** Fiduciary duty to maximize trust assets and collect debts
2. **As Debtor:** Personal interest in avoiding debt collection
3. **As Accountant:** Control over financial systems and records

The R18.75M (Ketoni debt to FFT) debt provides clear motive for Bantjies to:
- Dismiss Daniel's audit request (June 10, 2025)
- Support Peter's interdict application
- Certify Peter's affidavit despite material omissions
- Prevent discovery of fraud that would expose the debt

**Timeline Events:**
- EVENT_086: Daniel reports fraud to Bantjies (2025-06-06)
- EVENT_087: Bantjies dismisses audit request (2025-06-10)
- EVENT_088: Bantjies certifies Peter's affidavit (2025-08-01)

---

### Relation 2: Bantjies → Faucitt Family Trust (UNDISCLOSED_TRUSTEE)

**Source Entity:** PERSON_007 (Danie Bantjies)  
**Target Entity:** TRUST_001 (Faucitt Family Trust)  
**Relation Type:** UNDISCLOSED_TRUSTEE  

**Evidence:** SF1 - Ketoni R18.75M Payout to FFT Documentation, Trust deed amendments

**Burden of Proof Assessment:**
- **Civil Standard:** HIGH
- **Criminal Standard:** HIGH
- **Evidence Type:** Official trust documents, court records

**Significance:**

Bantjies was appointed as trustee in July 2024 but this status was:
- Not disclosed to Daniel when he reported fraud (June 6, 2025)
- Not disclosed in Peter's founding affidavit (certified by Bantjies)
- Not disclosed during the interdict proceedings
- Concealed while Bantjies acted as "independent" accountant

This non-disclosure constitutes:
1. **Breach of fiduciary duty** - Trustee must disclose conflicts
2. **Fraud** - Material omission in legal proceedings
3. **Professional misconduct** - Certifying affidavit omitting own status

**Legal Implications:**
- Interdict application may be voidable due to material non-disclosure
- Commissioner of Oaths certification was obtained through deception
- All actions taken as "accountant" were actually trustee actions

---

### Relation 3: SARS → RegimA (TAX_AUDIT)

**Source Entity:** ORG_015 (SARS - South African Revenue Service)  
**Target Entity:** ORG_002 (RegimA)  
**Relation Type:** TAX_AUDIT  

**Evidence:** SF4 - SARS Audit Email

**Burden of Proof Assessment:**
- **Civil Standard:** HIGH
- **Criminal Standard:** N/A (regulatory matter)
- **Evidence Type:** Official government correspondence

**Significance:**

Independent third-party verification of irregularities. SARS audit provides:

1. **Regulatory scrutiny** - Official government investigation
2. **Independent verification** - Third-party confirmation of problems
3. **Tax fraud implications** - Criminal penalties for tax fraud
4. **Chain of command evidence** - Rynette claiming Bantjies instructed payments

**Cross-References:**
- SF4: SARS audit email showing Rynette's claims
- SF1: Bantjies's conflict of interest
- SF3: Strategic Logistics stock adjustments

**Timeline Context:**

The SARS audit occurred during the same period as:
- Villa Via fraud discovery
- Bantjies's dismissal of audit request
- Interdict application against Jacqui and Daniel

This demonstrates multiple independent parties identifying irregularities simultaneously.

---

## Impact on Legal Filings

### Civil Applications (50% Burden of Proof)

All three relations meet or exceed the civil burden of proof:

1. **Ketoni R18.75M debt to FFT (Bantjies conflict as George Group CFO)M debt
2. **Undisclosed Trustee:** Trust deed and Master's Office records
3. **SARS Audit:** Official government correspondence

**Application Strengthening:**
- Demonstrates clear motive for obstruction
- Establishes conflict of interest
- Provides independent verification
- Shows pattern of non-disclosure

### Criminal Complaints (95% Burden of Proof)

Two relations approach criminal burden of proof:

1. **Undisclosed Trustee:** HIGH - Material omission in legal proceedings
2. **Bantjies Debt:** MEDIUM - Motive for fraud facilitation

**Criminal Charges Supported:**
- Fraud (material non-disclosure)
- Breach of fiduciary duty
- Obstruction of justice
- Professional misconduct

### Regulatory Complaints

All three relations support regulatory complaints:

1. **CIPC Complaint:** Bantjies's undisclosed trustee status
2. **POPIA Complaint:** System access and control issues
3. **Tax Fraud Report:** SARS audit findings
4. **Professional Conduct:** Commissioner of Oaths misconduct

---

## Evidence Organization

### SF File Cross-References

- **SF1 - Ketoni R18.75M Payout Documentation Documentation → Relations 1 & 2
- **SF4:** SARS Audit Email → Relation 3
- **SF2:** Sage Screenshots → Supporting evidence for control structure
- **SF3:** Stock Adjustments → Fraud Bantjies had motive to conceal

### Timeline Integration

New events documenting these relations:
- EVENT_086: Daniel reports to Bantjies (2025-06-06)
- EVENT_087: Bantjies dismisses audit (2025-06-10)
- EVENT_088: Bantjies certifies affidavit (2025-08-01)

---

## Next Steps

1. ✓ Create entity files for new entities
2. ✓ Create event files for new timeline events
3. ⧗ Update timeline.md with new events
4. ⧗ Update legal filings with new evidence
5. ⧗ Update GitHub Pages with relations documentation
6. ⧗ Commit and push changes to repository

---

**Document Version:** 1.0  
**Last Updated:** 2025-12-19  
**Status:** Implementation in progress
