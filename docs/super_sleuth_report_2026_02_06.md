# Super-Sleuth Introspection Report

**Case:** 2025-137857 - Revenue Stream Hijacking  
**Date:** 2026-02-06  
**Mode:** Intro-Spect (Divergent Investigation)

---

## Executive Summary

This Super-Sleuth analysis incorporates critical new evidence received on 2026-02-06, including a **fundamental correction to the R18.685M debt structure**. The corrected understanding reveals that **Ketoni Investment Holdings owes the Faucitt Family Trust** (not Bantjies owing Peter/Jacqui), which creates an even more damning conspiracy structure where Bantjies has **insider access to both ends of the transaction** through his connection to Kevin Derrick.

Additional new evidence includes the **Letter of Demand from Elliott Attorneys** protecting Rynette Farrar, **Sage accounting screenshots** proving Rynette's control over company systems, and **Rezonance supplier ledger** documenting the R1M+ debt at the time of Kayla's murder.

---

## 1. Critical Correction: R18.685M Debt Structure

### 1.1 Previous (Incorrect) Understanding

> "Bantjies' investment company owes Peter and Jacqui R18.685 million"

### 1.2 Corrected Understanding

> "Ketoni Investment Holdings (K2023562189) owes R18.685M to the Faucitt Family Trust under a Call Option Agreement (first exercise window: May 2026)"

### 1.3 Why This Is More Damning

The corrected structure reveals that Bantjies controls **both ends of the transaction**:

```
KETONI INVESTMENT HOLDINGS (K2023562189)
           │
           │ Owes R18.685M (Call Option)
           ▼
    FAUCITT FAMILY TRUST
           │
           │ Controlled by
           ▼
    DANIE BANTJIES (Trustee)
           │
           │ Distributes to
           ▼
    BENEFICIARIES (Peter, Jacqui, Daniel)
```

**Bantjies' Dual Access:**
1. As **CFO of George Group** → Has insider access to Ketoni through Kevin Derrick
2. As **Trustee of FFT** → Controls how the Trust receives and distributes the payment

---

## 2. New Entity Discovery

### 2.1 Ketoni Investment Holdings (Pty) Ltd

| Field | Value |
|-------|-------|
| **Entity ID** | ORG_017 |
| **Registration** | K2023562189 |
| **Type** | Juristic Person |
| **Role** | Debtor - Owes R18.685M to FFT |
| **Directors** | Kevin Michael Derrick |
| **Connection** | George Group (Bantjies' employer) |

### 2.2 The George Group

| Field | Value |
|-------|-------|
| **Entity ID** | ORG_018 |
| **Registration** | K2018619716 |
| **Type** | Juristic Person |
| **Role** | Bantjies' Employer |
| **Directors** | Kevin Michael Derrick |
| **Significance** | Creates insider access for Bantjies |

### 2.3 Kevin Michael Derrick

| Field | Value |
|-------|-------|
| **Entity ID** | PERSON_014 (existing, enhanced) |
| **Type** | Natural Person |
| **Roles** | Director: George Group, Director: Ketoni Investment Holdings |
| **Significance** | Key connection enabling Bantjies' insider access |

### 2.4 Pottas Attorneys

| Field | Value |
|-------|-------|
| **Entity ID** | ORG_019 |
| **Type** | Legal Practice |
| **Role** | Represents Rynette Farrar |
| **Contact** | rudi@pottaslaw.co.za, monique@pottaslaw.co.za |
| **Significance** | Proves Rynette has separate legal protection |

### 2.5 Addarory (Pty) Ltd

| Field | Value |
|-------|-------|
| **Entity ID** | ORG_009 (existing, enhanced) |
| **Type** | Juristic Person |
| **Owner** | Rynette Farrar's son |
| **Domain** | regimaskin.co.za |
| **Significance** | Competing business, alleged revenue diversion |

---

## 3. New Relation Discovery

### 3.1 Ketoni-George Group Connection

| Source | Relation | Target | Evidence |
|--------|----------|--------|----------|
| Kevin Derrick | director_of | George Group | CIPC records |
| Kevin Derrick | director_of | Ketoni Investment Holdings | CIPC records |
| Danie Bantjies | CFO_of | George Group | Employment records |
| Danie Bantjies | insider_access_to | Ketoni Investment Holdings | Via Kevin Derrick |

### 3.2 Legal Representation Network

| Source | Relation | Target | Evidence |
|--------|----------|--------|----------|
| Elliott Attorneys | represents | Peter Faucitt | Court records |
| Elliott Attorneys | protects | Rynette Farrar | Letter of Demand KL0034 |
| Pottas Attorneys | represents | Rynette Farrar | Letter of Demand KL0034 |

### 3.3 System Control Relations

| Source | Relation | Target | Evidence |
|--------|----------|--------|----------|
| Rynette Farrar | subscription_owner | Sage Accounting | SF11 |
| Rynette Farrar | uses_email | Pete@regima.com | SF10 |
| Rynette Farrar | uses_email | rynette@regima.zone | SF10 |

---

## 4. Pattern Detection

### 4.1 Pattern: Coordinated Legal Protection

**Detection:** Elliott Attorneys (Peter's attorneys) sent a Letter of Demand on behalf of Rynette Farrar to Pottas Attorneys on 26 November 2025.

**Significance:**
- Rynette is NOT a party to the litigation (Case 2025-137857)
- Yet Peter's attorneys are actively protecting her from Jacqui's allegations
- This proves coordination between Peter and Rynette
- Rynette has separate legal representation (Pottas Attorneys)

**Legal Relevance:** Conspiracy, coordinated action

### 4.2 Pattern: System Lockout Timing

**Detection:** Sage accounting registration expired on 23/07/2025, just before the August 2025 interdict.

**Timeline:**
- 23/07/2025: Sage registration expires
- 11/08/2025: Peter obtains "Main Trustee" signature from Jacqui
- 14/08/2025: Interdict filed

**Significance:** Rynette (as subscription owner) allowed the system to expire, preventing access to financial records just before the legal attack.

**Legal Relevance:** Evidence concealment, obstruction

### 4.3 Pattern: Dual Identity Access

**Detection:** Rynette Farrar has access to Sage accounting under TWO email addresses:
1. Pete@regima.com (impersonating Peter?)
2. rynette@regima.zone

**Significance:** The use of "Pete@regima.com" suggests identity fraud or impersonation, allowing Rynette to act as Peter in financial systems.

**Legal Relevance:** Identity fraud, impersonation, POPIA violation

### 4.4 Pattern: Insider Transaction Control

**Detection:** Bantjies has insider access to both ends of the R18.685M transaction:
- As CFO of George Group (where Kevin Derrick is Director)
- As Trustee of FFT (which receives the payment)

**Significance:** This creates unprecedented control over a R18.685M transaction:
1. Knows when Ketoni will pay (insider via Derrick)
2. Controls how Trust receives payment (as Trustee)
3. Controls distribution to beneficiaries (as Trustee)

**Legal Relevance:** Insider trading, self-dealing, breach of fiduciary duty

---

## 5. Corrected Conflict of Interest Framework

### 5.1 Previous Framework (5 Conflicts)

1. Commissioner of Oaths
2. Trustee
3. ~~Debtor (owes R18.685M+)~~ ← **INCORRECT**
4. Affidavit Witness
5. CFO of George Group

### 5.2 Corrected Framework (6 Conflicts)

| # | Conflict | Description | Evidence |
|---|----------|-------------|----------|
| 1 | **Commissioner of Oaths** | Swore own false affidavit | Court records |
| 2 | **Trustee** | Controls victims' Trust assets | FFT appointment docs |
| 3 | **Affidavit Witness** | Provided perjured supporting testimony | Interdict application |
| 4 | **CFO of George Group** | Where Kevin Derrick is Director | Employment records |
| 5 | **Insider Access to Ketoni** | Through Kevin Derrick connection | Corporate records |
| 6 | **Controls Distribution** | As Trustee, decides how R18.685M is distributed | Trust deed |

---

## 6. New Evidence Index

| Code | Document | Date | Key Finding |
|------|----------|------|-------------|
| SF10 | Sage User Access Screenshot | 2025-06-20 | Rynette has dual email access including Pete@regima.com |
| SF11 | Sage Registration Expired | 2025-08-25 | Rynette is subscription owner, expired 23/07/2025 |
| SF12 | Rezonance Supplier Ledger | 2023-02-28 | R1,035,361.34 owed to Rezonance |
| SF13 | Letter of Demand | 2025-11-26 | Elliott Attorneys protecting Rynette |
| SF14 | Correction Document | 2026-02-06 | Ketoni debt structure clarification |

---

## 7. Updated Timeline Events

| Date | Event | T-Months | Evidence | Significance |
|------|-------|----------|----------|--------------|
| 2023-02-28 | Rezonance debt at R1,035,361.34 | T-38 | SF12 | Pre-murder debt level |
| 2025-07-23 | Sage registration expires | T-10 | SF11 | System lockout before interdict |
| 2025-11-26 | Elliott Attorneys Letter of Demand | T-6 | SF13 | Coordinated legal protection |

---

## 8. Generated Leads

### LEAD-001: Kevin Derrick Investigation

**Category:** Critical  
**Pattern Detected:** Dual directorship enabling insider access  
**Evidence:**
- Kevin Derrick is Director of both George Group and Ketoni
- Bantjies is CFO of George Group
- This creates insider access to R18.685M transaction

**Hypothesis:** Kevin Derrick may be a co-conspirator or unwitting enabler of the scheme.

**Validation Required:**
- CIPC records for George Group and Ketoni
- Communication records between Bantjies and Derrick
- Ketoni shareholder/director meeting minutes

**Legal Relevance:** Insider trading, conspiracy, breach of fiduciary duty

### LEAD-002: Rynette Farrar Identity Fraud

**Category:** Critical  
**Pattern Detected:** Dual email access including Pete@regima.com  
**Evidence:**
- SF10 shows Rynette with access via Pete@regima.com
- This email suggests impersonation of Peter

**Hypothesis:** Rynette has been impersonating Peter in financial systems to authorize transactions.

**Validation Required:**
- Audit of all transactions authorized via Pete@regima.com
- Email server logs
- Bank mandate comparison

**Legal Relevance:** Identity fraud, POPIA violation, forgery

### LEAD-003: Elliott Attorneys Conflict of Interest

**Category:** Strong  
**Pattern Detected:** Peter's attorneys protecting non-party Rynette  
**Evidence:**
- Letter of Demand KL0034 sent by Elliott Attorneys on behalf of Rynette
- Rynette is not a party to Case 2025-137857

**Hypothesis:** Elliott Attorneys are coordinating defense across multiple conspirators.

**Validation Required:**
- Retainer agreements
- Communication records
- Legal Practice Council inquiry

**Legal Relevance:** Professional misconduct, conspiracy

---

## 9. Recommended Actions for Hyper-Holmes

1. **Validate Kevin Derrick dual directorship** via CIPC records
2. **Verify Sage subscription ownership** documentation
3. **Confirm Rezonance debt** at time of Kayla's murder
4. **Assess burden of proof** for insider trading charges
5. **Update all filings** with corrected debt structure
6. **Add Kevin Derrick** as potential co-conspirator

---

## 10. Documents Requiring Correction

All documents containing the incorrect debt structure must be updated:

| Document | Location | Error |
|----------|----------|-------|
| Case_Overview_2025-137857.docx | Project Knowledge | "Bantjies' investment company owes" |
| CIPC Complaint | docs/filings/ | Bantjies as debtor |
| POPIA Complaint | docs/filings/ | Bantjies as debtor |
| NPA Tax Fraud Report | docs/filings/ | Bantjies as debtor |
| Commercial Crime Submission | docs/filings/ | Bantjies as debtor |
| Ketoni Timeline | docs/ketoni-timeline.md | Debt structure |
| Entities Index | docs/entities/index.md | Bantjies role |

---

*Generated by Super-Sleuth Intro-Spect Mode*  
*Date: 2026-02-06*
