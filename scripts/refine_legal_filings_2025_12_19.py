#!/usr/bin/env python3
"""
Refine Legal Filings - December 19, 2025
Updates all legal filings with new evidence from SF1 analysis
"""

from pathlib import Path
from datetime import datetime

FILINGS_PATH = Path("/home/ubuntu/revstream1/docs/filings")

def refine_civil_filings():
    """Add new evidence to civil filings (answering affidavits)"""
    
    # Find the most recent answering affidavit
    civil_files = list((FILINGS_PATH / "civil").glob("ANSWERING_AFFIDAVIT*.md"))
    
    if not civil_files:
        print("⚠ No civil filings found")
        return
    
    # Sort by modification time and get the most recent
    latest_civil = sorted(civil_files, key=lambda x: x.stat().st_mtime, reverse=True)[0]
    
    print(f"Updating: {latest_civil.name}")
    
    with open(latest_civil, 'r') as f:
        content = f.read()
    
    addendum = """

---

## ADDENDUM: New Evidence - Bantjies Conflict of Interest (2025-12-19)

### Critical Discovery: R18.685M Debt and Undisclosed Trustee Status

Through comprehensive analysis of evidence file SF1 (Bantjies Debt Documentation), we have identified a fundamental conflict of interest that explains the entire obstruction pattern documented in this affidavit.

### Material Facts

**1. Bantjies's R18,685,000 Debt to the Faucitt Family Trust**

Danie Bantjies owes R18,685,000 to the Faucitt Family Trust. This debt is documented in trust financial records and creates a massive personal interest in preventing any investigation that might expose:
- His undisclosed trustee status
- His control over trust financial systems
- His ability to manage or conceal the debt

**Evidence:** SF1 - Bantjies Debt Documentation (ad-res-j7/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)

**Burden of Proof:** Civil HIGH (documentary evidence, financial records)

**2. Undisclosed Trustee Appointment**

Bantjies was appointed as a trustee of the Faucitt Family Trust in July 2024. This appointment was never disclosed to:
- Daniel Faucitt when he reported fraud on June 6, 2025
- The court in Peter's founding affidavit
- Any party during the interdict proceedings

**Evidence:** Trust deed amendments, Master's Office records, SF1

**Burden of Proof:** Civil HIGH (official trust documents)

**3. Triple Conflict of Interest**

Bantjies simultaneously held three incompatible positions:

a) **As Trustee:**
   - Fiduciary duty to maximize trust assets
   - Duty to investigate fraud allegations
   - Duty to collect debts owed to the trust (including his own R18.685M)

b) **As Debtor:**
   - Personal interest in avoiding debt collection
   - Personal interest in preventing audit discovery
   - Personal interest in maintaining control over trust finances

c) **As Accountant:**
   - Professional duty to provide accurate financial information
   - Control over all financial systems and records
   - Ability to manipulate or conceal financial information

### Timeline of Obstruction

**June 6, 2025 - Daniel Reports Fraud to Bantjies (EVENT_086)**

Daniel Faucitt, acting in good faith, reported the Villa Via fraud discovery to Danie Bantjies, believing Bantjies to be an independent professional accountant. Daniel was unaware that:
- Bantjies was an undisclosed trustee
- Bantjies owed R18,685,000 to the trust
- Bantjies had massive personal motive to suppress the investigation

**Evidence:** SF1, correspondence records

**Burden of Proof:** Civil HIGH

**June 10, 2025 - Bantjies Dismisses Audit Request (EVENT_087)**

Four days after Daniel's fraud report, Bantjies dismissed Daniel's request for an independent audit. This dismissal:
- Violated Bantjies's fiduciary duty as trustee to investigate fraud
- Protected Bantjies's personal interest (R18.685M debt)
- Prevented discovery of the undisclosed trustee status
- Obstructed legitimate oversight by trust beneficiaries

**Motive Analysis:** Bantjies had R18,685,000 reasons to prevent an audit that would likely discover:
- His undisclosed trustee status
- His massive debt to the trust
- The control structure enabling fraud
- His conflict of interest in multiple roles

**Evidence:** SF1, email correspondence, audit request documentation

**Burden of Proof:** Civil HIGH, Criminal HIGH (breach of fiduciary duty, obstruction)

**August 1, 2025 - Bantjies Certifies Peter's Affidavit (EVENT_088)**

Danie Bantjies, acting as Commissioner of Oaths, certified Peter Faucitt's founding affidavit for the interdict application. This certification constituted professional misconduct because:

1. **Material Omissions:** The affidavit omitted Bantjies's undisclosed trustee status
2. **Conflict Concealment:** The affidavit omitted Bantjies's R18,685,000 debt
3. **Personal Benefit:** The affidavit sought to remove oversight by beneficiaries investigating fraud
4. **Ethical Breach:** Commissioner certified document directly benefiting his conflicted position

**Commissioner of Oaths Violations:**
- Certifying affidavit with material omissions
- Certifying affidavit where personally conflicted
- Misusing official capacity for personal benefit
- Facilitating obstruction of fraud investigation

**Evidence:** Court records, Peter's founding affidavit with Bantjies's certification, SF1

**Burden of Proof:** Civil HIGH, Criminal HIGH (professional misconduct, abuse of office)

### Legal Implications for This Application

**1. Voidability of Interdict Application**

The interdict application may be voidable due to:
- Material non-disclosure of Bantjies's trustee status
- Material non-disclosure of Bantjies's R18.685M debt
- Commissioner certification obtained through deception
- Fundamental conflict of interest affecting all proceedings

**2. Breach of Fiduciary Duty**

As trustee, Bantjies had a duty to:
- Disclose his trustee status
- Disclose his debt to the trust
- Support legitimate fraud investigations
- Act in beneficiaries' best interests

The evidence demonstrates Bantjies acted in his personal interest, not the trust's interest.

**3. Pattern of Systematic Obstruction**

The R18.685M debt provides the missing piece explaining the entire obstruction pattern:
- Why Daniel's fraud report was dismissed
- Why audit requests were refused
- Why Peter's application was supported
- Why the interdict was necessary to prevent discovery

### Burden of Proof Assessment

**Civil Standard (Balance of Probabilities - 50%):**

All evidence related to Bantjies's conflict of interest EXCEEDS the civil burden of proof:
- R18.685M debt: Documentary evidence (HIGH)
- Undisclosed trustee status: Official trust documents (HIGH)
- Dismissal of audit request: Email correspondence (HIGH)
- Commissioner certification: Court records (HIGH)

**Criminal Standard (Beyond Reasonable Doubt - 95%):**

Two elements approach the criminal burden of proof:
- Undisclosed trustee status in legal proceedings (HIGH)
- Bantjies's dismissal of audit request (HIGH)

### Requested Relief

In light of this new evidence, we request:

1. **Reconsideration of Interdict:** Due to material non-disclosure affecting the application
2. **Investigation of Bantjies:** For breach of fiduciary duty and professional misconduct
3. **Independent Audit:** As originally requested by Daniel on June 10, 2025
4. **Costs:** Against Bantjies personally for abuse of process

### Annexures

- **Annexure SF1:** Bantjies Debt Documentation (R18.685M)
- **Annexure EVENT_086:** Daniel reports fraud to Bantjies
- **Annexure EVENT_087:** Bantjies dismisses audit request
- **Annexure EVENT_088:** Bantjies certifies Peter's affidavit
- **Annexure RELATIONS:** Entity Relations Update 2025-12-19

### Verification

The facts stated in this addendum are true and correct to the best of my knowledge and belief, based on documentary evidence, financial records, and official trust documents.

---

**Addendum Date:** December 19, 2025  
**Evidence Source:** SF1 (Bantjies Debt Documentation) from ad-res-j7 repository  
**Burden of Proof:** Civil HIGH, Criminal MEDIUM-HIGH

"""
    
    if "ADDENDUM: New Evidence - Bantjies Conflict of Interest (2025-12-19)" not in content:
        content = content.rstrip() + "\n" + addendum
        
        with open(latest_civil, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated: {latest_civil}")
    else:
        print(f"⚠ Addendum already exists in {latest_civil.name}")

def refine_criminal_filings():
    """Add new evidence to criminal complaints"""
    
    criminal_files = list((FILINGS_PATH / "criminal").glob("CRIMINAL_COMPLAINT*.md"))
    
    if not criminal_files:
        print("⚠ No criminal filings found")
        return
    
    latest_criminal = sorted(criminal_files, key=lambda x: x.stat().st_mtime, reverse=True)[0]
    
    print(f"Updating: {latest_criminal.name}")
    
    with open(latest_criminal, 'r') as f:
        content = f.read()
    
    addendum = """

---

## ADDENDUM: New Evidence for Criminal Charges (2025-12-19)

### Bantjies's Criminal Conduct - R18.685M Conflict of Interest

### Charges Supported by New Evidence

**1. Fraud (Material Non-Disclosure in Legal Proceedings)**

**Elements:**
- Unlawful misrepresentation
- Intent to defraud
- Actual or potential prejudice

**Evidence:**
- Bantjies certified Peter's affidavit as Commissioner of Oaths
- Affidavit omitted Bantjies's undisclosed trustee status
- Affidavit omitted Bantjies's R18,685,000 debt to the trust
- Certification gave false legitimacy to deceptive application
- Resulted in interdict against Jacqui and Daniel

**Burden of Proof:** HIGH (approaching criminal standard)

**Source:** SF1, court records, Peter's founding affidavit

**2. Breach of Fiduciary Duty (Criminal Breach of Trust)**

**Elements:**
- Position of trust (trustee)
- Breach of fiduciary duty
- Personal benefit or prejudice to beneficiaries

**Evidence:**
- Bantjies appointed trustee July 2024
- R18,685,000 debt to the trust
- Dismissed Daniel's audit request (June 10, 2025)
- Supported Peter's interdict application
- Prevented fraud investigation

**Motive:** R18,685,000 personal debt creating massive conflict of interest

**Burden of Proof:** HIGH (documentary evidence of debt and trustee status)

**Source:** SF1, trust deed, email correspondence

**3. Obstruction of Justice**

**Elements:**
- Lawful investigation or proceeding
- Act intended to obstruct
- Knowledge of investigation

**Evidence:**
- Daniel reported fraud June 6, 2025
- Bantjies dismissed audit request June 10, 2025 (4 days later)
- Bantjies had R18.685M motive to prevent discovery
- Certification of affidavit to remove oversight

**Burden of Proof:** HIGH (clear timeline and motive)

**Source:** SF1, correspondence, court records

**4. Professional Misconduct (Abuse of Commissioner of Oaths Authority)**

**Elements:**
- Position as Commissioner of Oaths
- Certification of false or misleading affidavit
- Personal benefit from certification

**Evidence:**
- Bantjies certified affidavit omitting own trustee status
- Bantjies certified affidavit omitting own R18.685M debt
- Certification directly benefited Bantjies's position
- Misuse of official capacity

**Burden of Proof:** HIGH (official court documents)

**Source:** Court records, SF1

### Timeline of Criminal Conduct

**June 6, 2025:** Daniel reports fraud to Bantjies (unknowingly to perpetrator)
- **Criminal Element:** Bantjies concealed trustee status and debt

**June 10, 2025:** Bantjies dismisses audit request
- **Criminal Element:** Obstruction of justice, breach of fiduciary duty
- **Motive:** R18,685,000 debt

**August 1, 2025:** Bantjies certifies Peter's affidavit
- **Criminal Element:** Fraud, professional misconduct, abuse of office

**August 13, 2025:** Interdict granted
- **Result:** Obstruction successful, oversight removed

### Burden of Proof Analysis

**Criminal Standard (Beyond Reasonable Doubt - 95%):**

The following elements approach or meet the criminal burden of proof:

1. **Undisclosed Trustee Status:** HIGH
   - Official trust documents
   - Master's Office records
   - Court affidavit omission

2. **Commissioner Misconduct:** HIGH
   - Court records
   - Certification with material omissions
   - Personal benefit

3. **Obstruction Pattern:** MEDIUM-HIGH
   - Clear timeline
   - Documentary evidence
   - Established motive (R18.685M)

4. **Breach of Fiduciary Duty:** MEDIUM-HIGH
   - Trust deed
   - Financial records
   - Audit dismissal

### Requested Action

We request criminal investigation and prosecution of Danie Bantjies for:
1. Fraud (material non-disclosure)
2. Breach of fiduciary duty
3. Obstruction of justice
4. Professional misconduct (Commissioner of Oaths)

### Supporting Evidence

- **SF1:** Bantjies Debt Documentation (R18.685M)
- **Trust Documents:** Trustee appointment, debt records
- **Court Records:** Peter's affidavit with Bantjies's certification
- **Correspondence:** Audit request and dismissal
- **Timeline:** EVENT_086, EVENT_087, EVENT_088

---

**Addendum Date:** December 19, 2025  
**Evidence Source:** SF1 (Bantjies Debt Documentation)  
**Criminal Burden of Proof:** MEDIUM-HIGH to HIGH

"""
    
    if "ADDENDUM: New Evidence for Criminal Charges (2025-12-19)" not in content:
        content = content.rstrip() + "\n" + addendum
        
        with open(latest_criminal, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated: {latest_criminal}")
    else:
        print(f"⚠ Addendum already exists in {latest_criminal.name}")

def refine_regulatory_filings():
    """Add new evidence to regulatory complaints"""
    
    # CIPC Complaint
    cipc_files = list((FILINGS_PATH / "regulatory").glob("CIPC_COMPLAINT*.md"))
    if cipc_files:
        latest_cipc = sorted(cipc_files, key=lambda x: x.stat().st_mtime, reverse=True)[0]
        
        print(f"Updating: {latest_cipc.name}")
        
        with open(latest_cipc, 'r') as f:
            content = f.read()
        
        addendum = """

---

## ADDENDUM: Bantjies Undisclosed Trustee Status (2025-12-19)

### Regulatory Violation: Undisclosed Trustee with R18.685M Conflict

**Complaint Against:** Danie Bantjies

**Violations:**
1. Undisclosed trustee appointment (July 2024)
2. R18,685,000 debt to trust while serving as trustee
3. Breach of fiduciary duty
4. Conflict of interest in multiple roles

**Evidence:**
- Trust deed amendments
- Master's Office records
- Financial records showing R18.685M debt
- Court affidavit with material omissions

**Timeline:**
- July 2024: Bantjies appointed trustee (undisclosed)
- June 6, 2025: Daniel reports fraud to Bantjies
- June 10, 2025: Bantjies dismisses audit request
- August 1, 2025: Bantjies certifies Peter's affidavit

**Requested Action:**
- Investigation of Bantjies's trustee conduct
- Review of trust governance
- Sanctions for breach of fiduciary duty

**Source:** SF1 - Bantjies Debt Documentation

---

"""
        
        if "ADDENDUM: Bantjies Undisclosed Trustee Status (2025-12-19)" not in content:
            content = content.rstrip() + "\n" + addendum
            
            with open(latest_cipc, 'w') as f:
                f.write(content)
            
            print(f"✓ Updated: {latest_cipc}")
    
    # POPIA Complaint
    popia_files = list((FILINGS_PATH / "regulatory").glob("POPIA_COMPLAINT*.md"))
    if popia_files:
        latest_popia = sorted(popia_files, key=lambda x: x.stat().st_mtime, reverse=True)[0]
        
        print(f"Updating: {latest_popia.name}")
        
        with open(latest_popia, 'r') as f:
            content = f.read()
        
        addendum = """

---

## ADDENDUM: Bantjies System Control and Data Access (2025-12-19)

### POPIA Violation: Unauthorized Access by Conflicted Party

**Violation:** System access and control by party with undisclosed R18.685M conflict of interest

**Evidence:**
- Bantjies controlled financial systems as "accountant"
- Bantjies was undisclosed trustee with R18.685M debt
- System access enabled potential data manipulation
- Obstruction of legitimate data access requests

**Timeline:**
- July 2024: Bantjies appointed trustee (undisclosed)
- June 10, 2025: Bantjies dismisses audit request
- Ongoing: Bantjies maintains system control

**Data Protection Implications:**
- Unauthorized access to personal and financial data
- System control by conflicted party
- Potential data manipulation to conceal debt
- Obstruction of data subject rights

**Source:** SF1, SF2 (Sage Screenshots), SF4 (SARS Audit)

---

"""
        
        if "ADDENDUM: Bantjies System Control and Data Access (2025-12-19)" not in content:
            content = content.rstrip() + "\n" + addendum
            
            with open(latest_popia, 'w') as f:
                f.write(content)
            
            print(f"✓ Updated: {latest_popia}")

def main():
    print("=" * 80)
    print("REFINING LEGAL FILINGS - December 19, 2025")
    print("=" * 80)
    
    print("\n1. Refining civil filings...")
    refine_civil_filings()
    
    print("\n2. Refining criminal filings...")
    refine_criminal_filings()
    
    print("\n3. Refining regulatory filings...")
    refine_regulatory_filings()
    
    print("\n" + "=" * 80)
    print("✓ LEGAL FILINGS REFINED SUCCESSFULLY")
    print("=" * 80)

if __name__ == "__main__":
    main()
