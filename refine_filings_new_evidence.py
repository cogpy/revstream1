'''
Refines legal filings based on the new evidence analyzed on 2026-02-05.

This script will update the following filings:
- CIPC Companies Act Complaint
- POPIA Criminal Complaint
- NPA Tax Fraud Report
- Commercial Crime Case Submission
'''

import json
import os
from datetime import datetime

# Paths
FILINGS_DIR = "/home/ubuntu/revstream1/docs/filings/"
ANALYSIS_NOTES = "/home/ubuntu/revstream1/evidence/2026-02-05_new_evidence/analysis_notes.md"

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
    print(f"Wrote refined filing: {path}")

def generate_cipc_complaint():
    '''Generates the refined CIPC complaint for director disqualification.'''
    content = """
# CIPC Complaint: Application for Director Disqualification of Peter Andrew Faucitt

**Date:** {date}
**Case Number:** 2025-137857
**Complainant:** Daniel James Faucitt (Director, RegimA SA (Pty) Ltd)
**Respondent:** Peter Andrew Faucitt (Director, RegimA SA (Pty) Ltd)
**Company:** RegimA SA (Pty) Ltd (2017/087935/07)

## 1. Introduction

This is an application to the Companies and Intellectual Property Commission (CIPC) for a declaration of delinquency against Director Peter Andrew Faucitt under **Section 162(5) of the Companies Act, 71 of 2008**. The application is based on overwhelming evidence of gross abuse of position, breach of fiduciary duties, and willful misconduct that has directly led to the financial ruin of RegimA SA (Pty) Ltd.

## 2. Grounds for Delinquency: Breach of Fiduciary Duty (Section 76)

Director Peter Faucitt has fundamentally breached his fiduciary duties as outlined in Section 76 of the Companies Act. The evidence demonstrates a coordinated and intentional effort to destroy the company to inflict harm on his co-director, Daniel Faucitt.

### 2.1. Intentional Financial Sabotage

**Evidence:**
- **Bank Statements (Oct 2024 vs. Mar 2025):** In October 2024, RegimA SA held a healthy balance of **R2,554,860.93**. By March 2025, just before the main revenue stream was diverted, the account had been systematically stripped to a mere **R5,284.08**—a 99.8% decline. This demonstrates a clear pattern of asset stripping.
- **Shopify Revenue Diversion (May 2025):** The company's primary revenue stream, generating **R8.5 million annually** via Shopify, was completely diverted starting around May 22, 2025. Sales reports show a drop from over R948,000 in May 2025 to **R0.00 in June 2025**.
- **Shopify Payment Failures (Sep-Oct 2025):** As a direct result of the revenue diversion, the company defaulted on its Shopify platform fees, with **9 consecutive payment failures** recorded.

### 2.2. Gross Abuse of Position

**Evidence:**
- **CIPC Records:** Official records confirm Peter Faucitt and Daniel Faucitt are the sole active directors of RegimA SA. Jacqui Faucitt is not a director or shareholder, yet Peter Faucitt acted in concert with non-directors (e.g., Rynette Farrar) to undermine the company.
- **Formal Notice (8 Jul 2025):** Daniel Faucitt issued a formal notice demanding Peter cease his criminal instructions to bypass Shopify. Peter Faucitt ignored this notice and instead retaliated with vexatious litigation 36 days later.
- **Premeditation (11 Apr 2025):** An organogram created by Rynette Farrar for Peter Faucitt 40 days before the sabotage proves he had full knowledge of Shopify's critical role in the business, establishing clear premeditation.

## 3. Conclusion

Peter Faucitt has intentionally and maliciously destroyed a profitable company in breach of his fiduciary duties. He has:
1.  Systematically stripped its assets.
2.  Diverted its entire revenue stream.
3.  Caused it to default on its critical operational platforms.
4.  Ignored formal notices to cease his unlawful conduct.

His actions constitute a textbook case for a declaration of delinquency. We request the CIPC to investigate and disqualify Peter Andrew Faucitt from serving as a director of any company.

**[1]** *62707308252 2024-10-07.pdf*
**[2]** *62707308252 2025-03-06.pdf*
**[3]** *RegimA SA Shopify Plus - Total sales over time.pdf*
**[4]** *RegimA_SA_423808676.pdf*
**[5]** *347975701_REGIMA_SA_K201708793507.Pdf*
**[6]** *FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.pdf*
**[7]** *Power point - how sales work.pdf*

""".format(date=datetime.now().strftime("%Y-%m-%d"))
    return content

def generate_popia_complaint():
    '''Generates the refined POPIA complaint.'''
    content = """
# POPIA Criminal Complaint

**Date:** {date}
**Case Number:** 2025-137857
**Complainant:** Daniel James Faucitt (Director, RegimA SA (Pty) Ltd)
**Respondent:** Peter Andrew Faucitt (Director, RegimA SA (Pty) Ltd)

## 1. Summary of Complaint

This complaint details a series of criminal offenses under the **Protection of Personal Information Act (POPIA), 4 of 2013**, orchestrated by Peter Andrew Faucitt. The evidence shows a willful and intentional breach of data protection principles for the purpose of concealing fraudulent activities and retaliating against a fellow director who attempted to enforce compliance.

## 2. Offenses Under POPIA

### 2.1. Unlawful Processing of Personal Information (Section 11)

Peter Faucitt instructed employees to bypass the company's secure and audited Shopify system and process customer data using unauthorized domains and systems. This constitutes a direct violation of the lawfulness of processing principle.

**Evidence:**
- **Formal Notice (8 Jul 2025):** Daniel Faucitt issued a formal notice to Peter Faucitt explicitly stating that his "instructions to employees to bypass Shopify and use unauthorized domains for processing customer data" were illegal.
- **POPIA Violation Notice (8 Jul 2025):** A separate notice was sent detailing the customer data breach related to the May 22nd Shopify revenue stream diversion.

### 2.2. Failure to Secure Personal Information (Section 19)

By diverting customer order processing away from the secure Shopify platform to unknown, unaudited systems, Peter Faucitt willfully compromised the integrity and confidentiality of customer personal information, including names, addresses, and purchase histories.

### 2.3. Obstruction of the Regulator (Section 105) and Retaliation

The entire scheme was designed to create an unauditable revenue stream, thereby obstructing any potential investigation by the Information Regulator or SARS. Furthermore, Peter Faucitt's actions were a direct retaliation against Daniel Faucitt for attempting to enforce POPIA compliance.

**Evidence:**
- **Retaliation Timeline:**
    - **6 Jun 2025:** Daniel reports fraud concerns to the accountant.
    - **7 Jun 2025:** Peter cancels all of Daniel's bank cards (less than 24 hours later).
    - **8 Jul 2025:** Daniel sends the POPIA Violation Notice.
    - **13 Aug 2025:** Peter files a retaliatory ex parte court application, falsely framing the compliance demands as "harassment".

## 3. Conclusion

Peter Faucitt's actions were not accidental; they were a deliberate criminal strategy to facilitate fraud and silence a whistleblower. He knowingly compromised customer data and then weaponized the legal system when his actions were challenged. We urge the Information Regulator to pursue criminal charges against Peter Andrew Faucitt for these flagrant violations of POPIA, which carry a maximum penalty of **R10 million fine and/or 10 years imprisonment**.

**[1]** *FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.pdf*
**[2]** *POPIA_VIOLATION_NOTICE_&_RETALIATION_TIMELINE.pdf*

""".format(date=datetime.now().strftime("%Y-%m-%d"))
    return content

def generate_npa_tax_fraud_report():
    '''Generates the refined NPA Tax Fraud Report.'''
    content = """
# Report to the National Prosecuting Authority (NPA): Tax Fraud

**Date:** {date}
**Case Number:** 2025-137857
**Reporting Party:** Daniel James Faucitt
**Subjects:** Peter Andrew Faucitt, Rynette Farrar, De Novo Business Services (Pty) Ltd, Marisca Meyer

## 1. Executive Summary

This report details a sophisticated tax fraud scheme involving the fabrication of financial statements, fraudulent allocation of expenses, and the creation of false inter-company loan accounts. The evidence points to a coordinated effort to under-report income and create fictitious expenses for RegimA SA (Pty) Ltd (Tax No. 9746755165).

## 2. Evidence of Financial Statement Fabrication

The most damning piece of evidence is a set of **Annual Financial Statements for RegimA SA for the period ending 28 February 2019**, which were **created and issued on 25 June 2025**.

**Evidence:**
- **Document:** *Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf*
- **Key Fraud Indicators:**
    1.  **Impossible Issue Date:** The statements for the 2019 financial year were fabricated over six years later.
    2.  **Complicit Accountant:** The preparer, Marisca Meyer of De Novo Business Services, is the same accountant who received instructions to create fraudulent records.
    3.  **Timing:** The statements were created just seven days after Rynette Farrar instructed De Novo to create fraudulent loan accounts to hide expenses.
    4.  **Lack of Oversight:** The statements were not audited or independently reviewed, and were created without the knowledge of co-director Daniel Faucitt.

## 3. Evidence of Fraudulent Expense Allocation

Email correspondence proves that Rynette Farrar, an accountant manager at RegimA, instructed the company's external accountants, De Novo Business Services, to commit accounting fraud.

**Evidence:**
- **Document:** *2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf*
- **Rynette Farrar's Instructions (17-18 Jun 2025):**
    > "No, I think the best will be to create a loan account within RegimA SA, for the other company. Then these invoice (not belonging to RegimA SA) can be allocated to this loan account."
    > "The expenses for the Coral draw and Quickbooks do not belong to this company, so I suggest you open a loan account for one of Danny's other company's called Rezonance and post these expenses then to Rezonance's loan account."

This is a direct instruction to misrepresent expenses and create false inter-company loans to defraud SARS.

## 4. Conclusion

This evidence demonstrates a clear and deliberate conspiracy to commit tax fraud in violation of the **Tax Administration Act, 28 of 2011**. The back-dated financial statements and the explicit instructions to create fraudulent records constitute a prima facie case. We request the NPA to launch a full criminal investigation into the actions of Peter Faucitt, Rynette Farrar, and the complicit accounting firm De Novo Business Services and its employee Marisca Meyer.

""".format(date=datetime.now().strftime("%Y-%m-%d"))
    return content

def generate_commercial_crime_submission():
    '''Generates the refined Commercial Crime Submission.'''
    content = """
# Submission to the SAPS Commercial Crime Unit

**Date:** {date}
**Case Number:** 2025-137857
**Complainant:** Daniel James Faucitt
**Subjects:** Peter Andrew Faucitt, Rynette Farrar

## 1. Nature of Complaint: Revenue Stream Hijacking & Company Destruction

This submission outlines a multi-faceted commercial crime scheme resulting in the complete financial destruction of RegimA SA (Pty) Ltd (Reg. No. 2017/087935/07). The scheme, orchestrated by director Peter Faucitt and his associate Rynette Farrar, involved asset stripping, revenue diversion, and accounting fraud, culminating in losses exceeding R8.5 million annually.

## 2. Modus Operandi

The crime was executed in three phases:

**Phase 1: Asset Stripping (Oct 2024 - Mar 2025)**
- The company's bank account was systematically drained from a healthy **R2.5 million** to just **R5,284** through a series of large, unexplained outbound transfers.
- **Evidence:** FNB Bank Statements (*62707308252 2024-10-07.pdf* vs. *62707308252 2025-03-06.pdf*)

**Phase 2: Revenue Diversion (May 2025 onwards)**
- The company's entire Shopify revenue stream, worth R8.5M annually, was hijacked. Revenue dropped to zero from June 2025 onwards.
- This was a premeditated act, occurring 40 days after Rynette Farrar created an organogram for Peter Faucitt detailing Shopify's central importance.
- **Evidence:** Shopify Sales Report (*RegimA SA Shopify Plus - Total sales over time.pdf*), Organogram (*Power point - how sales work.pdf*)

**Phase 3: Fraudulent Cover-Up (June 2025)**
- To conceal the theft, the perpetrators engaged in accounting fraud, instructing their accountants (De Novo Business Services) to create false loan accounts and fabricating financial statements for 2019 six years after the fact.
- **Evidence:** Email Instructions (*2025-06-18 - Rynette & De Novo...pdf*), Fabricated Statements (*Regima SA (Pty) Ltd - 2019...pdf*)

## 3. Key Criminal Acts

1.  **Theft:** Diversion of the R8.5M annual revenue stream.
2.  **Fraud:** Creation of backdated financial statements and false loan accounts to deceive SARS and auditors.
3.  **Conspiracy:** Coordinated actions between Peter Faucitt, Rynette Farrar, and De Novo Business Services.
4.  **Uttering:** Presenting fraudulent financial documents as genuine.

## 4. Conclusion

This was not a business failure; it was the deliberate and criminal destruction of a company from within by one of its own directors. The evidence is documentary, comprehensive, and demonstrates a clear timeline of intent, execution, and cover-up. We request the Commercial Crime Unit to open a formal investigation into these serious economic crimes.

""".format(date=datetime.now().strftime("%Y-%m-%d"))
    return content

def main():
    print("Refining legal filings with new evidence...")
    
    # Generate and write CIPC Complaint
    cipc_content = generate_cipc_complaint()
    write_file(os.path.join(FILINGS_DIR, "CIPC_COMPLAINT_REFINED_2026_02_05.md"), cipc_content)
    
    # Generate and write POPIA Complaint
    popia_content = generate_popia_complaint()
    write_file(os.path.join(FILINGS_DIR, "POPIA_COMPLAINT_REFINED_2026_02_05.md"), popia_content)
    
    # Generate and write NPA Tax Fraud Report
    npa_content = generate_npa_tax_fraud_report()
    write_file(os.path.join(FILINGS_DIR, "NPA_TAX_FRAUD_REPORT_REFINED_2026_02_05.md"), npa_content)
    
    # Generate and write Commercial Crime Submission
    crime_content = generate_commercial_crime_submission()
    write_file(os.path.join(FILINGS_DIR, "COMMERCIAL_CRIME_SUBMISSION_REFINED_2026_02_05.md"), crime_content)
    
    print("All filings have been refined and saved.")

if __name__ == "__main__":
    main()
