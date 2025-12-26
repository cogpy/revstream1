#!/usr/bin/env python3
"""
Update GitHub Pages - December 19, 2025
Updates timeline, index, and application pages with new evidence
"""

from pathlib import Path
from datetime import datetime

DOCS_PATH = Path("/home/ubuntu/revstream1/docs")

def update_timeline():
    """Add new events to timeline.md"""
    timeline_path = DOCS_PATH / "timeline.md"
    
    # Read existing timeline
    with open(timeline_path, 'r') as f:
        content = f.read()
    
    # New section to add
    new_section = """

## Newly Identified Events (2025-12-19 Refinement)

These events were identified through comprehensive analysis of SF (Smoking Gun) evidence files, particularly SF1 (Bantjies Debt Documentation). They reveal the critical conflict of interest that drove the obstruction pattern.

### 2025-06-06 - Daniel reports fraud to Bantjies (unknowingly to perpetrator)

**Event ID:** EVENT_086  
**Category:** fraud_exposure  

**Description:** Daniel Faucitt reported the Villa Via fraud discovery to Danie Bantjies, unaware that Bantjies was an undisclosed trustee of the Faucitt Family Trust owing R18,685,000 to the trust. This was a critical turning point where Daniel unknowingly reported fraud to a conflicted party who had massive financial motive to suppress the investigation.

**Evidence:**  
- [SF1: Bantjies Debt Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)

**Entities:** PERSON_003 (Daniel Faucitt), PERSON_007 (Danie Bantjies), TRUST_001 (Faucitt Family Trust)

**Financial Context:** R18,685,000 - Bantjies's debt to the trust

**Burden of Proof:** Civil HIGH, Criminal MEDIUM

---

### 2025-06-10 - Bantjies dismisses Daniel's audit request

**Event ID:** EVENT_087  
**Category:** obstruction  

**Description:** Four days after Daniel reported the fraud, Bantjies dismissed Daniel's request for an independent audit. This dismissal occurred despite clear evidence of R22.8M in unexplained Villa Via transactions and Bantjies's fiduciary duty as trustee to investigate fraud. Bantjies had R18,685,000 reasons to prevent an audit that would likely discover his undisclosed trustee status and massive debt to the trust.

**Evidence:**  
- [SF1: Bantjies Debt Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)

**Entities:** PERSON_007 (Danie Bantjies), PERSON_003 (Daniel Faucitt), TRUST_001 (Faucitt Family Trust)

**Financial Impact:** R18,685,000.00

**Burden of Proof:** Civil HIGH, Criminal HIGH

**Significance:** Demonstrates breach of fiduciary duty, conflict of interest, and systematic obstruction

---

### 2025-08-01 - Bantjies certifies Peter's affidavit as Commissioner of Oaths

**Event ID:** EVENT_088  
**Category:** professional_misconduct  

**Description:** Danie Bantjies, acting as Commissioner of Oaths, certified Peter Faucitt's founding affidavit for the interdict application against Jacqui and Daniel. This certification constituted professional misconduct because the affidavit omitted Bantjies's undisclosed trustee status and his R18,685,000 debt to the trust. The certification gave false legitimacy to a deceptive application that directly benefited Bantjies's conflicted position.

**Evidence:**  
- [SF1: Bantjies Debt Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)
- Court records: Peter's founding affidavit with Bantjies's certification

**Entities:** PERSON_007 (Danie Bantjies), PERSON_001 (Peter Faucitt), TRUST_001 (Faucitt Family Trust)

**Financial Context:** R18,685,000 - Bantjies's debt creating motive to support Peter's application

**Burden of Proof:** Civil HIGH, Criminal HIGH

**Significance:** Abuse of Commissioner authority, breach of fiduciary duty, facilitation of fraud concealment

---

"""
    
    # Insert before the last section or at the end
    if "## Newly Identified Events" not in content:
        content = content.rstrip() + "\n" + new_section
    
    with open(timeline_path, 'w') as f:
        f.write(content)
    
    print(f"✓ Updated: {timeline_path}")

def update_index():
    """Update index.md with new evidence and relations"""
    index_path = DOCS_PATH / "index.md"
    
    with open(index_path, 'r') as f:
        lines = f.readlines()
    
    # Find the section to update (after Evidence & Analysis)
    insert_index = None
    for i, line in enumerate(lines):
        if "### Evidence & Analysis" in line:
            insert_index = i + 1
            break
    
    if insert_index:
        # Add new evidence links
        new_lines = [
            "- [Entity Relations Update (2025-12-19)](RELATIONS_UPDATE_2025_12_19.html)\n",
        ]
        
        # Insert after existing evidence links
        for i, line in enumerate(lines[insert_index:], start=insert_index):
            if line.startswith("###") or line.strip() == "":
                lines.insert(i, "\n")
                for new_line in reversed(new_lines):
                    lines.insert(i, new_line)
                break
    
    with open(index_path, 'w') as f:
        f.writelines(lines)
    
    print(f"✓ Updated: {index_path}")

def update_application_pages():
    """Update application pages with new evidence"""
    
    # Application 1: Civil Response
    app1_path = DOCS_PATH / "application-1.md"
    if app1_path.exists():
        with open(app1_path, 'r') as f:
            content = f.read()
        
        new_evidence_section = """

## New Evidence - Bantjies Conflict of Interest (2025-12-19)

### SF1: Bantjies Debt Documentation (R18.685M)

**Evidence Type:** Documentary, financial records  
**Burden of Proof:** Civil HIGH, Criminal MEDIUM

**Key Findings:**

1. **R18,685,000 Debt:** Bantjies owes R18,685,000 to the Faucitt Family Trust
2. **Undisclosed Trustee:** Bantjies was appointed trustee in July 2024 but never disclosed this status
3. **Triple Conflict:** Bantjies simultaneously held three incompatible positions:
   - Trustee (fiduciary duty to trust)
   - Debtor (personal interest in avoiding collection)
   - Accountant (control over financial systems)

**Timeline of Obstruction:**

- **June 6, 2025:** Daniel reports fraud to Bantjies (EVENT_086)
- **June 10, 2025:** Bantjies dismisses audit request (EVENT_087)
- **August 1, 2025:** Bantjies certifies Peter's affidavit (EVENT_088)
- **August 13, 2025:** Interdict granted against Jacqui and Daniel

**Legal Implications:**

- Breach of fiduciary duty
- Conflict of interest
- Professional misconduct (Commissioner of Oaths)
- Material non-disclosure in court proceedings
- Obstruction of fraud investigation

**Impact on Civil Application:**

This evidence demonstrates clear motive for the entire obstruction pattern. Bantjies had R18,685,000 reasons to:
- Dismiss Daniel's legitimate audit request
- Support Peter's interdict application
- Certify affidavit with material omissions
- Prevent discovery of fraud

The interdict application may be voidable due to material non-disclosure of Bantjies's trustee status and debt.

**Cross-References:**
- [SF1 Full Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)
- [EVENT_086: Daniel reports to Bantjies](events/EVENT_086.html)
- [EVENT_087: Bantjies dismisses audit](events/EVENT_087.html)
- [EVENT_088: Bantjies certifies affidavit](events/EVENT_088.html)
- [Relations Update 2025-12-19](RELATIONS_UPDATE_2025_12_19.html)

"""
        
        if "New Evidence - Bantjies Conflict of Interest" not in content:
            content = content.rstrip() + "\n" + new_evidence_section
        
        with open(app1_path, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated: {app1_path}")
    
    # Application 2: CIPC Complaint
    app2_path = DOCS_PATH / "application-2.md"
    if app2_path.exists():
        with open(app2_path, 'r') as f:
            content = f.read()
        
        new_evidence_section = """

## New Evidence - Bantjies Undisclosed Trustee Status (2025-12-19)

### SF1: Bantjies Debt Documentation

**Regulatory Violation:** Undisclosed trustee status in court proceedings

**Key Findings:**

1. **Trustee Appointment:** Bantjies appointed as trustee in July 2024
2. **Non-Disclosure:** Status not disclosed in Peter's founding affidavit
3. **Commissioner Misconduct:** Bantjies certified affidavit omitting own status
4. **Debt Concealment:** R18,685,000 debt to trust not disclosed

**CIPC Implications:**

- Director/trustee duties violation
- Breach of fiduciary duty to trust
- Conflict of interest in multiple roles
- Material non-disclosure affecting trust governance

**Supporting Evidence:**
- Trust deed amendments
- Master's Office records
- Court affidavit with Bantjies's certification
- Financial records showing R18.685M debt

**Cross-References:**
- [SF1 Full Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)
- [Relations Update 2025-12-19](RELATIONS_UPDATE_2025_12_19.html)

"""
        
        if "New Evidence - Bantjies Undisclosed Trustee Status" not in content:
            content = content.rstrip() + "\n" + new_evidence_section
        
        with open(app2_path, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated: {app2_path}")
    
    # Application 3: POPIA Complaint
    app3_path = DOCS_PATH / "application-3.md"
    if app3_path.exists():
        with open(app3_path, 'r') as f:
            content = f.read()
        
        new_evidence_section = """

## New Evidence - System Control and Access (2025-12-19)

### SF1 & SF4: Bantjies Control Structure

**POPIA Violation:** Unauthorized system access and control

**Key Findings:**

1. **Undisclosed Trustee:** Bantjies had trustee-level access without disclosure
2. **Accountant Access:** Bantjies controlled financial systems as "accountant"
3. **Conflict of Interest:** R18,685,000 debt creating motive for data manipulation
4. **SARS Audit:** Independent verification of irregularities (SF4)

**Data Protection Implications:**

- Unauthorized access to personal and financial data
- System control by conflicted party
- Potential data manipulation to conceal debt
- Obstruction of legitimate data access requests

**Supporting Evidence:**
- SF1: Bantjies Debt Documentation
- SF2: Sage Screenshots (Rynette Control)
- SF4: SARS Audit Email

**Cross-References:**
- [SF1 Full Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)
- [SF4 SARS Audit](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF4_SARS_Audit_Email.md)
- [Relations Update 2025-12-19](RELATIONS_UPDATE_2025_12_19.html)

"""
        
        if "New Evidence - System Control and Access" not in content:
            content = content.rstrip() + "\n" + new_evidence_section
        
        with open(app3_path, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated: {app3_path}")

def main():
    print("=" * 80)
    print("UPDATING GITHUB PAGES - December 19, 2025")
    print("=" * 80)
    
    print("\n1. Updating timeline.md...")
    update_timeline()
    
    print("\n2. Updating index.md...")
    update_index()
    
    print("\n3. Updating application pages...")
    update_application_pages()
    
    print("\n" + "=" * 80)
    print("✓ GITHUB PAGES UPDATED SUCCESSFULLY")
    print("=" * 80)
    print("\nUpdated files:")
    print("  - docs/timeline.md")
    print("  - docs/index.md")
    print("  - docs/application-1.md")
    print("  - docs/application-2.md")
    print("  - docs/application-3.md")

if __name__ == "__main__":
    main()
