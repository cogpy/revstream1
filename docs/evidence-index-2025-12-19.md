# Evidence Index - 2025-12-19 Refinement

**Repository**: cogpy/revstream1  
**Cross-Reference**: cogpy/ad-res-j7  
**Last Updated**: 2025-12-19

## Overview

This index provides direct links to all evidence files analyzed in the 2025-12-19 comprehensive refinement. Each evidence file includes burden of proof assessments for both civil (50%) and criminal (95%) standards.

---

## SF Evidence Files (ad-res-j7/ANNEXURES)

### SF1 - Ketoni R18.75M Payout Documentation Documentation (R18.75M (Ketoni debt to FFT))

**File**: `ANNEXURES/SF1_Ketoni_Debt_FFT_Documentation.md`  
**Subject**: Ketoni's R18.75M debt to FFT to Faucitt Family Trust  
**Burden of Proof**: Civil (HIGH), Criminal (MEDIUM)

**Key Points**:
- Documents R18.75M (Ketoni debt to FFT) debt creating massive conflict of interest
- Bantjies simultaneously: trustee + debtor + accountant
- Provides motive to dismiss audit requests and prevent fraud discovery
- Explains obstruction pattern (June 10, 2025 audit dismissal)

**Related Entities**: PERSON_007 (Danie Bantjies), TRUST_001 (Faucitt Family Trust)  
**Related Events**: EVENT_089  
**Related Relations**: REL_023

**Evidence Strength**: Documentary, financial records  
**Legal Significance**: CRITICAL - Establishes motive and conflict of interest

---

### SF2: Sage Screenshots - Rynette Control

**File**: `ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md`  
**Subject**: Rynette's control of Sage accounting system and Pete@regima.com email  
**Burden of Proof**: Civil (HIGH), Criminal (HIGH)

**Key Points**:
- Screenshot dated 2025-06-20 shows Rynette with system control
- User accounts: Pete@regima.com, rynette@regima.zone
- Direct proof of email access and financial system control
- Technical capability to manipulate financial records

**Related Entities**: PERSON_002 (Rynette Farrar), ORG_001 (RegimA)  
**Related Events**: EVENT_090  
**Related Relations**: REL_024

**Evidence Strength**: Visual evidence (screenshots), system-generated  
**Legal Significance**: CRITICAL - Proves technical capability for fraud

---

### SF3: Strategic Logistics Stock Adjustment

**File**: `ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md`  
**Subject**: R5.4M stock adjustment manipulation  
**Burden of Proof**: Civil (MEDIUM), Criminal (LOW)

**Key Points**:
- R5,400,000 stock adjustment
- Potential accounting manipulation
- Strategic Logistics entity involvement

**Related Entities**: ORG_003 (Strategic Logistics)  
**Evidence Strength**: Company records, accounting entries

---

### SF4: SARS Audit Email

**File**: `ANNEXURES/SF4_SARS_Audit_Email.md`  
**Subject**: SARS tax audit notification  
**Burden of Proof**: Civil (HIGH), Criminal (N/A)

**Key Points**:
- Official SARS audit notification (2021-03-15)
- Independent regulatory verification of irregularities
- Third-party corroboration of financial misconduct
- Tax fraud carries criminal penalties

**Related Entities**: ORG_015 (SARS), ORG_001 (RegimA)  
**Related Events**: EVENT_088  
**Related Relations**: REL_025

**Evidence Strength**: Official correspondence  
**Legal Significance**: HIGH - Independent regulatory verification

---

### SF5: Adderory Company Registration & Stock Supply

**File**: `ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md`  
**Subject**: Adderory company registration and stock supply arrangement  
**Burden of Proof**: Civil (MEDIUM), Criminal (LOW)

**Key Points**:
- Company registration (2019-11-20)
- Stock supply arrangement with RegimA
- Potential fictitious or controlled supplier
- Revenue recognition manipulation

**Related Entities**: ORG_014 (Adderory), ORG_001 (RegimA)  
**Related Events**: EVENT_091  
**Related Relations**: REL_026

**Evidence Strength**: Company records, CIPC documentation

---

### SF6: Kayla Pretorius Estate Documentation

**File**: `ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md`  
**Subject**: Estate documentation for Kayla Pretorius  
**Burden of Proof**: Civil (MEDIUM), Criminal (N/A)

**Key Points**:
- Estate executor documentation (2021-09-10)
- Email account holder
- Context for court-ordered seizure (SF7)

**Related Entities**: PERSON_013 (Kayla Pretorius)  
**Related Events**: EVENT_086

**Evidence Strength**: Legal documentation

---

### SF7: Court Order - Kayla Email Seizure

**File**: `ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md`  
**Subject**: Court order for seizure of Kayla Pretorius email account  
**Burden of Proof**: Civil (HIGH), Criminal (MEDIUM)

**Key Points**:
- Court order dated 2021-10-05
- Email account seizure for evidence
- Judicial recognition of potential incriminating communications
- Legal action indicating serious concerns

**Related Entities**: PERSON_013 (Kayla Pretorius)  
**Related Events**: EVENT_087

**Evidence Strength**: Court order (official judicial document)  
**Legal Significance**: HIGH - Judicial recognition

---

### SF8: Linda Employment Records

**File**: `ANNEXURES/SF8_Linda_Employment_Records.md`  
**Subject**: Employment records for Linda (bookkeeper)  
**Burden of Proof**: Civil (MEDIUM), Criminal (LOW)

**Key Points**:
- Employment documentation
- Sister of Rynette Farrar
- Operational structure evidence
- Employed while Rynette controlled accounting system

**Related Entities**: PERSON_006 (Linda)

**Evidence Strength**: Employment records, company documentation

---

## New Entities (2025-12-19)

### PERSON_013: Kayla Pretorius
- **Role**: Estate executor, email account holder
- **Evidence**: SF6, SF7
- **Legal Significance**: Email account subject to court-ordered seizure
- **Burden of Proof**: Civil (HIGH), Criminal (MEDIUM)

### ORG_015: SARS (South African Revenue Service)
- **Role**: Tax authority conducting audit
- **Evidence**: SF4
- **Legal Significance**: Independent regulatory verification
- **Burden of Proof**: Civil (HIGH), Criminal (N/A)

---

## New Relations (2025-12-19)

### REL_023: Bantjies → Faucitt Family Trust (DEBT)
- **Amount**: R18.75M (Ketoni debt to FFT).00
- **Evidence**: SF1
- **Type**: Documentary
- **Burden of Proof**: Civil (HIGH), Criminal (MEDIUM)
- **Significance**: CRITICAL - Motive and conflict of interest

### REL_024: Rynette → RegimA (SYSTEM_CONTROL)
- **Evidence**: SF2
- **Type**: Visual (screenshots)
- **Burden of Proof**: Civil (HIGH), Criminal (HIGH)
- **Significance**: CRITICAL - Technical capability proof

### REL_025: SARS → RegimA (TAX_AUDIT)
- **Evidence**: SF4
- **Type**: Official correspondence
- **Burden of Proof**: Civil (HIGH), Criminal (N/A)
- **Significance**: HIGH - Independent verification

### REL_026: Adderory → RegimA (STOCK_SUPPLY)
- **Evidence**: SF5
- **Type**: Company records
- **Burden of Proof**: Civil (MEDIUM), Criminal (LOW)
- **Significance**: MEDIUM - Potential fictitious supplier

---

## New Timeline Events (2025-12-19)

### EVENT_086: Kayla Pretorius Estate Documentation (2021-09-10)
- **Category**: Legal documentation
- **Burden of Proof**: Civil (MEDIUM), Criminal (N/A)

### EVENT_087: Court Order for Kayla Email Seizure (2021-10-05)
- **Category**: Legal action
- **Burden of Proof**: Civil (HIGH), Criminal (MEDIUM)
- **Significance**: HIGH - Judicial recognition

### EVENT_088: SARS Tax Audit Notification (2021-03-15)
- **Category**: Regulatory action
- **Burden of Proof**: Civil (HIGH), Criminal (N/A)
- **Significance**: HIGH - Independent verification

### EVENT_089: Bantjies R18.75M (Ketoni debt to FFT) Debt (2020-02-28)
- **Category**: Accounting fraud / Conflict of interest
- **Financial Impact**: R18.75M (Ketoni debt to FFT).00
- **Burden of Proof**: Civil (HIGH), Criminal (MEDIUM)
- **Significance**: CRITICAL - Motive established

### EVENT_090: Rynette Sage System Control (2020-08-15)
- **Category**: System control
- **Burden of Proof**: Civil (HIGH), Criminal (HIGH)
- **Significance**: CRITICAL - Capability proof

### EVENT_091: Adderory Registration (2019-11-20)
- **Category**: Business structure
- **Burden of Proof**: Civil (MEDIUM), Criminal (LOW)

---

## Burden of Proof Summary

### Civil Standard (50% - Balance of Probabilities)

**Evidence Meeting Standard**: 7 items
- SF1 - Ketoni R18.75M Payout Documentation (HIGH)
- SF2: Rynette system control (HIGH)
- SF4: SARS audit (HIGH)
- SF7: Court order (HIGH)
- REL_023, REL_024, REL_025 (all HIGH)

### Criminal Standard (95% - Beyond Reasonable Doubt)

**Strong Indicators**: 4 items
- SF2: Rynette system control (HIGH)
- EVENT_089: Bantjies debt with motive (MEDIUM)
- EVENT_090: System control proof (HIGH)
- EVENT_087: Court order (MEDIUM)

---

## Application Integration

### Application 1 (Civil Action)
**Strengthened by**: SF1, SF2, SF4, SF5, SF7  
**Key Evidence**: Bantjies debt (motive), Rynette control (capability)

### Application 2 (Criminal Complaint)
**Strengthened by**: SF1, SF2, SF7  
**Key Evidence**: System control, conflict of interest, judicial recognition

### Application 3 (Regulatory Complaints)
**Strengthened by**: SF4, SF1, SF5  
**Key Evidence**: SARS audit, professional misconduct, CIPC implications

---

## Repository Links

- **Main Repository**: [cogpy/revstream1](https://github.com/cogpy/revstream1)
- **Evidence Repository**: [cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
- **Evidence Files**: [ad-res-j7/ANNEXURES](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES)

---

**Last Updated**: 2025-12-19  
**Version**: 12.0_REFINED_2025_12_19  
**Prepared by**: Manus AI
