#!/usr/bin/env python3
"""
Implement Refinements for revstream1 - December 19, 2025
Creates new entity, relation, and event files based on evidence analysis
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
DOCS_PATH = REVSTREAM_PATH / "docs"
ENTITIES_PATH = DOCS_PATH / "entities"
EVENTS_PATH = DOCS_PATH / "events"

def create_entity_person_015():
    """Create PERSON_015: Chantal"""
    content = """# Chantal

**Entity ID:** `PERSON_015`

- **Entity Type:** person
- **Role:** Estate executor correspondent
- **Involvement Events:** 1
- **Primary Actions:** 
  - estate_correspondence
  - legal_documentation
- **Relationships:** 
  - correspondent_kayla_estate
  - communication_with_jacqui
- **Timeline Events:** 
  - kayla_estate_finalization_2025_01_15
- **Additional Notes:** Correspondent regarding Kayla Pretorius estate finalization, mentioned in JF08 evidence packages
- **Evidence References:** JF08, SF6

## Related Events

- **2025-01-15**: [Chantal Letter - Kayla Estate Finalization](../events/EVENT_023.md)

## Evidence Cross-References

- **JF08**: Evidence package correspondence
- **SF6**: Kayla Pretorius Estate Documentation
"""
    
    file_path = ENTITIES_PATH / "PERSON_015.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Created: {file_path}")

def create_event_086():
    """Create EVENT_086: Daniel reports fraud to Bantjies"""
    content = """---
layout: default
title: Daniel reports fraud to Bantjies (unknowingly to perpetrator)
event_id: EVENT_086
date: 2025-06-06
category: fraud_exposure
---

# Daniel reports fraud to Bantjies (unknowingly to perpetrator)

**Event ID:** EVENT_086  
**Date:** 2025-06-06  
**Category:** fraud_exposure

## Description

Daniel Faucitt reported the Villa Via fraud discovery to Danie Bantjies, unaware that Bantjies was:
1. An undisclosed trustee of the Faucitt Family Trust
2. A debtor owing R18,685,000 to the trust
3. The accountant with control over all financial systems
4. A party with significant motive to prevent fraud discovery

This was a critical turning point where Daniel unknowingly reported fraud to a conflicted party who had R18.685M reasons to suppress the investigation.

## Evidence References

- **SF1:** Bantjies Debt Documentation - See ad-res-j7/ANNEXURES/SF1_Bantjies_Debt_Documentation.md

## Entities Involved

- [PERSON_003 - Daniel Faucitt](../entities/PERSON_003.md)
- [PERSON_007 - Danie Bantjies](../entities/PERSON_007.md)
- [TRUST_001 - Faucitt Family Trust](../entities/TRUST_001.md)

## Financial Context

**R18,685,000** - Bantjies's debt to the trust, creating massive conflict of interest

## Burden of Proof Assessment

- **Civil Standard (Balance of Probabilities):** HIGH
- **Criminal Standard (Beyond Reasonable Doubt):** MEDIUM
- **Evidence Type:** Documentary, correspondence, financial records

## Significance

This event demonstrates:
1. Daniel's good faith attempt to address fraud through proper channels
2. Bantjies's position as a conflicted party from the outset
3. The structural impediment to legitimate fraud investigation
4. The beginning of the obstruction pattern

## Timeline Context

**4 days later:** Bantjies dismisses Daniel's audit request (EVENT_087)

## Cross-References

- See SF1 for complete conflict of interest analysis
- See EVENT_087 for Bantjies's response
- See timeline for chronological context
"""
    
    file_path = EVENTS_PATH / "EVENT_086.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Created: {file_path}")

def create_event_087():
    """Create EVENT_087: Bantjies dismisses audit request"""
    content = """---
layout: default
title: Bantjies dismisses Daniel's audit request
event_id: EVENT_087
date: 2025-06-10
category: obstruction
---

# Bantjies dismisses Daniel's audit request

**Event ID:** EVENT_087  
**Date:** 2025-06-10  
**Category:** obstruction

## Description

Four days after Daniel reported the fraud to Bantjies, Bantjies dismissed Daniel's request for an independent audit. This dismissal occurred despite:
1. Clear evidence of R22.8M in unexplained Villa Via transactions
2. Bantjies's fiduciary duty as trustee to investigate fraud
3. Bantjies's professional duty as accountant to ensure accurate records
4. Daniel's status as a trust beneficiary with legitimate concerns

## Evidence References

- **SF1:** Bantjies Debt Documentation - See ad-res-j7/ANNEXURES/SF1_Bantjies_Debt_Documentation.md

## Entities Involved

- [PERSON_007 - Danie Bantjies](../entities/PERSON_007.md)
- [PERSON_003 - Daniel Faucitt](../entities/PERSON_003.md)
- [TRUST_001 - Faucitt Family Trust](../entities/TRUST_001.md)

## Financial Impact

**R18,685,000** - Bantjies's personal debt providing motive to prevent audit

## Burden of Proof Assessment

- **Civil Standard (Balance of Probabilities):** HIGH
- **Criminal Standard (Beyond Reasonable Doubt):** HIGH
- **Evidence Type:** Documentary, correspondence, conflict of interest analysis

## Significance

This dismissal demonstrates:
1. **Breach of fiduciary duty** - Trustee refusing to investigate fraud
2. **Conflict of interest** - R18.685M debt creating motive to suppress investigation
3. **Obstruction** - Preventing legitimate oversight by beneficiaries
4. **Pattern establishment** - Beginning of systematic obstruction

## Motive Analysis

Bantjies had R18,685,000 reasons to prevent an audit:
- Audit would likely discover his undisclosed trustee status
- Audit would reveal his massive debt to the trust
- Audit would expose the control structure
- Audit would threaten his position and ability to manage the debt

## Timeline Context

**4 days earlier:** Daniel reported fraud to Bantjies (EVENT_086)  
**2 months later:** Bantjies certifies Peter's affidavit (EVENT_088)

## Cross-References

- See SF1 for complete conflict of interest analysis
- See EVENT_086 for initial fraud report
- See EVENT_088 for subsequent professional misconduct
- See timeline for full obstruction pattern
"""
    
    file_path = EVENTS_PATH / "EVENT_087.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Created: {file_path}")

def create_event_088():
    """Create EVENT_088: Bantjies certifies affidavit"""
    content = """---
layout: default
title: Bantjies certifies Peter's affidavit as Commissioner of Oaths
event_id: EVENT_088
date: 2025-08-01
category: professional_misconduct
---

# Bantjies certifies Peter's affidavit as Commissioner of Oaths

**Event ID:** EVENT_088  
**Date:** 2025-08-01 (estimated)  
**Category:** professional_misconduct

## Description

Danie Bantjies, acting as Commissioner of Oaths, certified Peter Faucitt's founding affidavit for the interdict application against Jacqui and Daniel. This certification constituted professional misconduct because:

1. **Material Omissions:** The affidavit omitted Bantjies's undisclosed trustee status
2. **Conflict Concealment:** The affidavit omitted Bantjies's R18,685,000 debt to the trust
3. **Personal Benefit:** The affidavit sought to remove oversight by beneficiaries investigating fraud
4. **Ethical Breach:** Commissioner certified document that directly benefited his conflicted position

## Evidence References

- **SF1:** Bantjies Debt Documentation - See ad-res-j7/ANNEXURES/SF1_Bantjies_Debt_Documentation.md
- **Court Records:** Peter's founding affidavit with Bantjies's certification

## Entities Involved

- [PERSON_007 - Danie Bantjies](../entities/PERSON_007.md)
- [PERSON_001 - Peter Faucitt](../entities/PERSON_001.md)
- [TRUST_001 - Faucitt Family Trust](../entities/TRUST_001.md)

## Financial Context

**R18,685,000** - Bantjies's debt creating motive to support Peter's application

## Burden of Proof Assessment

- **Civil Standard (Balance of Probabilities):** HIGH
- **Criminal Standard (Beyond Reasonable Doubt):** HIGH
- **Evidence Type:** Official court documents, certification records, conflict analysis

## Professional Misconduct Analysis

### Commissioner of Oaths Duties

A Commissioner of Oaths must:
- Ensure affidavits contain truthful statements
- Maintain independence and impartiality
- Disclose conflicts of interest
- Not certify documents where personally conflicted

### Violations

Bantjies violated these duties by:
1. Certifying affidavit omitting his own trustee status
2. Certifying affidavit omitting his own debt to the trust
3. Certifying affidavit that directly benefited his position
4. Using official capacity to facilitate obstruction of fraud investigation

## Legal Implications

### Abuse of Commissioner Authority

- Certification gave false legitimacy to deceptive application
- Misuse of official capacity for personal benefit
- Facilitation of fraud concealment

### Breach of Fiduciary Duty

- As trustee, should have disclosed conflicts
- As trustee, should have supported fraud investigation
- As trustee, should not have supported removal of oversight

## Timeline Context

**2 months earlier:** Bantjies dismissed Daniel's audit request (EVENT_087)  
**13 days later:** Interdict granted against Jacqui and Daniel (August 13, 2025)

## Significance

This certification demonstrates:
1. **Systematic abuse** of professional positions
2. **Coordination** with Peter to remove oversight
3. **Escalation** from dismissing audit to facilitating legal action
4. **Pattern** of using official capacities to conceal fraud

## Cross-References

- See SF1 for complete conflict of interest analysis
- See EVENT_087 for prior obstruction
- See timeline for full pattern of professional misconduct
- See court records for certified affidavit
"""
    
    file_path = EVENTS_PATH / "EVENT_088.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Created: {file_path}")

def create_relations_update():
    """Create relations update document"""
    content = """# Entity Relations Update - 2025-12-19

**Repository:** cogpy/revstream1  
**Evidence Source:** cogpy/ad-res-j7  
**Date:** December 19, 2025

---

## New Relations Identified

### Relation 1: Bantjies → Faucitt Family Trust (DEBTOR)

**Source Entity:** PERSON_007 (Danie Bantjies)  
**Target Entity:** TRUST_001 (Faucitt Family Trust)  
**Relation Type:** DEBTOR  
**Amount:** R18,685,000

**Evidence:** SF1 - Bantjies Debt Documentation

**Burden of Proof Assessment:**
- **Civil Standard:** HIGH
- **Criminal Standard:** MEDIUM
- **Evidence Type:** Documentary, financial records

**Significance:**

This debt creates a fundamental conflict of interest. Bantjies simultaneously held three incompatible positions:

1. **As Trustee:** Fiduciary duty to maximize trust assets and collect debts
2. **As Debtor:** Personal interest in avoiding debt collection
3. **As Accountant:** Control over financial systems and records

The R18,685,000 debt provides clear motive for Bantjies to:
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

**Evidence:** SF1 - Bantjies Debt Documentation, Trust deed amendments

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

1. **Bantjies Debt:** Documentary evidence of R18.685M debt
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

- **SF1:** Bantjies Debt Documentation → Relations 1 & 2
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
"""
    
    file_path = DOCS_PATH / "RELATIONS_UPDATE_2025_12_19.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Created: {file_path}")

def main():
    print("=" * 80)
    print("IMPLEMENTING REFINEMENTS - December 19, 2025")
    print("=" * 80)
    
    print("\n1. Creating new entity files...")
    create_entity_person_015()
    
    print("\n2. Creating new event files...")
    create_event_086()
    create_event_087()
    create_event_088()
    
    print("\n3. Creating relations update document...")
    create_relations_update()
    
    print("\n" + "=" * 80)
    print("✓ REFINEMENTS IMPLEMENTED SUCCESSFULLY")
    print("=" * 80)
    print("\nNew files created:")
    print("  - docs/entities/PERSON_015.md")
    print("  - docs/events/EVENT_086.md")
    print("  - docs/events/EVENT_087.md")
    print("  - docs/events/EVENT_088.md")
    print("  - docs/RELATIONS_UPDATE_2025_12_19.md")
    
    print("\nNext steps:")
    print("  - Update timeline.md with new events")
    print("  - Update legal filings with new evidence")
    print("  - Update GitHub Pages index")
    print("  - Commit and push changes")

if __name__ == "__main__":
    main()
