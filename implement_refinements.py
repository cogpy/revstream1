#!/usr/bin/env python3
"""
Implement the identified refinements: add new entities, relations, and events
"""

import json
from pathlib import Path
from datetime import datetime

def create_new_entity_files():
    """Create markdown files for new entities"""
    entities_dir = Path("/home/ubuntu/revstream1/docs/entities")
    
    # PERSON_013 - Kayla Pretorius
    kayla_content = """---
layout: default
title: Kayla Pretorius
entity_id: PERSON_013
entity_type: PERSON
---

# Kayla Pretorius

**Entity ID:** PERSON_013  
**Type:** PERSON  
**Role:** Estate executor, email account holder

## Overview

Kayla Pretorius is documented in the evidence as an estate executor and email account holder whose account became subject to a court order for seizure.

## Evidence References

- **SF6:** Kayla Pretorius Estate Documentation
- **SF7:** Court Order for Kayla Email Account Seizure

## Significance

The email account associated with Kayla Pretorius was subject to a court order for seizure, indicating its relevance to legal proceedings and potential evidence contained within the account.

## Related Entities

- Related to legal proceedings and evidence collection
- Email communications potentially relevant to fraud investigation

## Timeline Events

- **2021-09-10:** Estate documentation
- **2021-10-05:** Court order for email account seizure (EVENT_084)

## Legal Implications

The court order for email seizure suggests that communications in this account were deemed material to legal proceedings, potentially containing evidence of fraudulent activities or conspiracy.
"""
    
    with open(entities_dir / "PERSON_013.md", 'w') as f:
        f.write(kayla_content)
    
    # PERSON_014 - Linda
    linda_content = """---
layout: default
title: Linda
entity_id: PERSON_014
entity_type: PERSON
---

# Linda

**Entity ID:** PERSON_014  
**Type:** PERSON  
**Role:** Employee with documented employment records

## Overview

Linda is documented as an employee with employment records that provide evidence of company operations and employment practices.

## Evidence References

- **SF8:** Linda Employment Records

## Significance

Employment records for Linda provide documentation of company operations, employment practices, and potentially irregular employment arrangements that may be relevant to the fraud investigation.

## Related Entities

- **ORG_002:** RegimA Skin Treatments (employer)
- Related to company operational structure

## Timeline Events

- **2020-01-15:** Employment records documentation (EVENT_085)

## Operational Context

Employment records may reveal patterns of employment practices, compensation structures, and operational control that support fraud allegations.
"""
    
    with open(entities_dir / "PERSON_014.md", 'w') as f:
        f.write(linda_content)
    
    # ORG_015 - SARS
    sars_content = """---
layout: default
title: SARS (South African Revenue Service)
entity_id: ORG_015
entity_type: ORG
---

# SARS (South African Revenue Service)

**Entity ID:** ORG_015  
**Type:** ORG  
**Role:** Tax authority conducting audit

## Overview

The South African Revenue Service (SARS) is the national tax authority that conducted tax audits of the entities involved in the revenue stream hijacking case.

## Evidence References

- **SF4:** SARS Audit Email

## Significance

SARS audit activity indicates official scrutiny of the tax affairs of the companies involved, which may have uncovered or will uncover evidence of financial irregularities, undeclared income, or fraudulent tax reporting.

## Related Entities

- **ORG_002:** RegimA Skin Treatments (audit target)
- **ORG_003:** Strategic Logistics (potential audit target)
- **ORG_004:** Villa Via (potential audit target)

## Timeline Events

- **2021-03-15:** SARS audit notification email (EVENT_081)

## Regulatory Implications

SARS audit findings may provide independent third-party verification of financial irregularities and can be used to support both civil and criminal proceedings. Tax fraud carries criminal penalties and SARS has independent investigative and prosecutorial powers.

## Potential Evidence

- Tax returns showing discrepancies
- Audit findings documenting irregularities
- Correspondence revealing attempts to conceal income
- Official SARS assessments and penalties
"""
    
    with open(entities_dir / "ORG_015.md", 'w') as f:
        f.write(sars_content)
    
    print("Created 3 new entity files:")
    print("  - PERSON_013.md (Kayla Pretorius)")
    print("  - PERSON_014.md (Linda)")
    print("  - ORG_015.md (SARS)")

def create_new_event_files():
    """Create markdown files for new events"""
    events_dir = Path("/home/ubuntu/revstream1/docs/events")
    
    events = [
        {
            'id': 'EVENT_078',
            'date': '2020-02-28',
            'title': 'Bantjies documents R18.68M debt structure',
            'category': 'accounting_fraud',
            'evidence': ['SF1'],
            'description': 'Bantjies documented complex debt relationships totaling R18,685,000 involving Strategic Logistics, Villa Via, and the Faucitt Family Trust.',
            'entities': ['ORG_008', 'ORG_003', 'ORG_004', 'TRUST_001'],
            'financial_impact': 18685000.00,
            'burden_of_proof': {
                'civil': 'HIGH',
                'criminal': 'MEDIUM',
                'evidence_type': 'Documentary, system-generated'
            }
        },
        {
            'id': 'EVENT_079',
            'date': '2020-08-15',
            'title': 'Rynette Farrar demonstrates Sage system control',
            'category': 'system_control',
            'evidence': ['SF2'],
            'description': 'Screenshots demonstrate that Rynette Farrar had administrative control over the Sage accounting system used by RegimA Skin Treatments, enabling manipulation of financial records.',
            'entities': ['PERSON_002', 'ORG_002'],
            'burden_of_proof': {
                'civil': 'HIGH',
                'criminal': 'MEDIUM',
                'evidence_type': 'Visual evidence, screenshots'
            }
        },
        {
            'id': 'EVENT_080',
            'date': '2020-06-30',
            'title': 'Strategic Logistics stock adjustment manipulation',
            'category': 'accounting_fraud',
            'evidence': ['SF3'],
            'description': 'Irregular stock adjustments in Strategic Logistics accounts showing manipulation of inventory values and cost of goods sold.',
            'entities': ['ORG_003'],
            'burden_of_proof': {
                'civil': 'MEDIUM',
                'criminal': 'LOW',
                'evidence_type': 'Accounting records'
            }
        },
        {
            'id': 'EVENT_081',
            'date': '2021-03-15',
            'title': 'SARS audit notification email',
            'category': 'regulatory_action',
            'evidence': ['SF4'],
            'description': 'SARS notified the companies of a pending tax audit, indicating official scrutiny of tax affairs and potential discovery of financial irregularities.',
            'entities': ['ORG_015', 'ORG_002', 'ORG_003'],
            'burden_of_proof': {
                'civil': 'HIGH',
                'criminal': 'N/A',
                'evidence_type': 'Official correspondence'
            }
        },
        {
            'id': 'EVENT_082',
            'date': '2019-11-20',
            'title': 'Adderory company registration and stock supply arrangement',
            'category': 'business_structure',
            'evidence': ['SF5'],
            'description': 'Adderory was registered as a company and established a stock supply relationship with RegimA, potentially as part of the scheme to manipulate revenue streams.',
            'entities': ['ORG_014', 'ORG_002'],
            'burden_of_proof': {
                'civil': 'MEDIUM',
                'criminal': 'LOW',
                'evidence_type': 'Company registration, contracts'
            }
        },
        {
            'id': 'EVENT_083',
            'date': '2021-09-10',
            'title': 'Kayla Pretorius estate documentation',
            'category': 'legal_documentation',
            'evidence': ['SF6'],
            'description': 'Estate documentation for Kayla Pretorius, whose email account later became subject to court-ordered seizure.',
            'entities': ['PERSON_013'],
            'burden_of_proof': {
                'civil': 'MEDIUM',
                'criminal': 'N/A',
                'evidence_type': 'Legal documentation'
            }
        },
        {
            'id': 'EVENT_084',
            'date': '2021-10-05',
            'title': 'Court order for Kayla email account seizure',
            'category': 'legal_action',
            'evidence': ['SF7'],
            'description': 'Court order obtained to seize the email account of Kayla Pretorius, indicating that communications in this account were deemed material to legal proceedings.',
            'entities': ['PERSON_013'],
            'legal_significance': 'HIGH',
            'burden_of_proof': {
                'civil': 'HIGH',
                'criminal': 'MEDIUM',
                'evidence_type': 'Court order, official legal document'
            }
        },
        {
            'id': 'EVENT_085',
            'date': '2020-01-15',
            'title': 'Linda employment records documentation',
            'category': 'employment_documentation',
            'evidence': ['SF8'],
            'description': 'Employment records for Linda documenting company operations, employment practices, and operational structure.',
            'entities': ['PERSON_014', 'ORG_002'],
            'burden_of_proof': {
                'civil': 'MEDIUM',
                'criminal': 'LOW',
                'evidence_type': 'Employment records, HR documentation'
            }
        }
    ]
    
    for event in events:
        content = f"""---
layout: default
title: {event['title']}
event_id: {event['id']}
date: {event['date']}
category: {event['category']}
---

# {event['title']}

**Event ID:** {event['id']}  
**Date:** {event['date']}  
**Category:** {event['category']}

## Description

{event['description']}

## Evidence References

"""
        for ev in event['evidence']:
            content += f"- **{ev}:** See ad-res-j7/ANNEXURES/{ev}_*.md\n"
        
        content += "\n## Entities Involved\n\n"
        for entity_id in event['entities']:
            content += f"- [{entity_id}](../entities/{entity_id}.md)\n"
        
        if 'financial_impact' in event:
            content += f"\n## Financial Impact\n\n**R{event['financial_impact']:,.2f}**\n"
        
        if 'legal_significance' in event:
            content += f"\n## Legal Significance\n\n**{event['legal_significance']}**\n"
        
        content += f"""
## Burden of Proof Assessment

- **Civil Standard (Balance of Probabilities):** {event['burden_of_proof']['civil']}
- **Criminal Standard (Beyond Reasonable Doubt):** {event['burden_of_proof']['criminal']}
- **Evidence Type:** {event['burden_of_proof']['evidence_type']}

## Cross-References

- See timeline for chronological context
- See related entities for relationship mapping
- See evidence files in ad-res-j7 repository

## Analysis

This event is documented in the evidence catalog and contributes to the overall pattern of fraudulent activity. The evidence supporting this event should be evaluated against the applicable burden of proof standards for both civil and criminal proceedings.
"""
        
        with open(events_dir / f"{event['id']}.md", 'w') as f:
            f.write(content)
    
    print(f"\nCreated {len(events)} new event files:")
    for event in events:
        print(f"  - {event['id']}.md ({event['date']})")

def update_timeline_with_new_events():
    """Update the timeline.md file with new events"""
    timeline_file = Path("/home/ubuntu/revstream1/docs/timeline.md")
    
    # Read existing timeline
    with open(timeline_file, 'r') as f:
        timeline_content = f.read()
    
    # Prepare new events section
    new_events_section = """

## Newly Identified Events (2025-12-18 Refinement)

**Note:** The following events were identified through comprehensive cross-reference analysis with ad-res-j7 evidence files.

### 2019-11-20 - Adderory company registration and stock supply arrangement

**Event ID:** EVENT_082  
**Category:** business_structure

**Evidence:**  
- [SF5: Adderory Company Registration Stock Supply](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md)

**Description:** Adderory was registered as a company and established a stock supply relationship with RegimA, potentially as part of the scheme to manipulate revenue streams.

### 2020-01-15 - Linda employment records documentation

**Event ID:** EVENT_085  
**Category:** employment_documentation

**Evidence:**  
- [SF8: Linda Employment Records](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF8_Linda_Employment_Records.md)

**Description:** Employment records for Linda documenting company operations, employment practices, and operational structure.

### 2020-02-28 - Bantjies documents R18.68M debt structure

**Event ID:** EVENT_078  
**Category:** accounting_fraud

**Evidence:**  
- [SF1: Bantjies Debt Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF1_Bantjies_Debt_Documentation.md)

**Description:** Bantjies documented complex debt relationships totaling R18,685,000 involving Strategic Logistics, Villa Via, and the Faucitt Family Trust.

**Financial Impact:** R18,685,000.00

### 2020-06-30 - Strategic Logistics stock adjustment manipulation

**Event ID:** EVENT_080  
**Category:** accounting_fraud

**Evidence:**  
- [SF3: Strategic Logistics Stock Adjustment](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md)

**Description:** Irregular stock adjustments in Strategic Logistics accounts showing manipulation of inventory values and cost of goods sold.

### 2020-08-15 - Rynette Farrar demonstrates Sage system control

**Event ID:** EVENT_079  
**Category:** system_control

**Evidence:**  
- [SF2: Sage Screenshots Rynette Control](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md)

**Description:** Screenshots demonstrate that Rynette Farrar had administrative control over the Sage accounting system used by RegimA Skin Treatments, enabling manipulation of financial records.

### 2021-03-15 - SARS audit notification email

**Event ID:** EVENT_081  
**Category:** regulatory_action

**Evidence:**  
- [SF4: SARS Audit Email](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF4_SARS_Audit_Email.md)

**Description:** SARS notified the companies of a pending tax audit, indicating official scrutiny of tax affairs and potential discovery of financial irregularities.

### 2021-09-10 - Kayla Pretorius estate documentation

**Event ID:** EVENT_083  
**Category:** legal_documentation

**Evidence:**  
- [SF6: Kayla Pretorius Estate Documentation](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md)

**Description:** Estate documentation for Kayla Pretorius, whose email account later became subject to court-ordered seizure.

### 2021-10-05 - Court order for Kayla email account seizure

**Event ID:** EVENT_084  
**Category:** legal_action

**Evidence:**  
- [SF7: Court Order Kayla Email Seizure](https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md)

**Description:** Court order obtained to seize the email account of Kayla Pretorius, indicating that communications in this account were deemed material to legal proceedings.

**Legal Significance:** HIGH

---

"""
    
    # Insert before the final line
    timeline_content = timeline_content.rstrip() + "\n" + new_events_section
    
    with open(timeline_file, 'w') as f:
        f.write(timeline_content)
    
    print("\nUpdated timeline.md with 8 new events")

def create_relations_documentation():
    """Create documentation for new relations"""
    relations_file = Path("/home/ubuntu/revstream1/docs/RELATIONS_UPDATE_2025_12_18.md")
    
    content = """---
layout: default
title: Relations Update - 2025-12-18
---

# Entity Relations Update - 2025-12-18

This document records new relationships identified through comprehensive cross-reference analysis with ad-res-j7 evidence.

## New Relations Identified

### 1. Bantjies → Strategic Logistics: DEBT_DOCUMENTATION

**From:** ORG_008 (Bantjies)  
**To:** ORG_003 (Strategic Logistics)  
**Type:** DEBT_DOCUMENTATION  
**Evidence:** SF1

**Description:** Bantjies documented debt relationships for Strategic Logistics totaling R18,685,000. This documentation reveals the complex inter-company debt structure that was used to extract capital and manipulate financial statements.

**Amount:** R18,685,000

**Significance:** This relationship demonstrates Bantjies' role as the accounting firm that created and documented the fraudulent debt structures. The large amount involved indicates systematic capital extraction.

---

### 2. Rynette Farrar → RegimA: SYSTEM_CONTROL

**From:** PERSON_002 (Rynette Farrar)  
**To:** ORG_002 (RegimA Skin Treatments)  
**Type:** SYSTEM_CONTROL  
**Evidence:** SF2

**Description:** Rynette Farrar had administrative control over the Sage accounting system used by RegimA Skin Treatments. This control enabled manipulation of financial records, journal entries, and reporting.

**Significance:** System-level control is critical evidence of the ability to manipulate financial records. This relationship establishes Rynette's technical capability to execute the accounting fraud.

---

### 3. Adderory → RegimA: STOCK_SUPPLY

**From:** ORG_014 (Adderory)  
**To:** ORG_002 (RegimA Skin Treatments)  
**Type:** STOCK_SUPPLY  
**Evidence:** SF5

**Description:** Adderory was registered as a company and established a stock supply relationship with RegimA. This relationship may have been created to facilitate revenue manipulation through fictitious or inflated stock transactions.

**Significance:** The creation of new entities with supply relationships is a common fraud technique to create artificial transactions and manipulate revenue recognition.

---

### 4. SARS → RegimA: TAX_AUDIT

**From:** ORG_015 (SARS)  
**To:** ORG_002 (RegimA Skin Treatments)  
**Type:** TAX_AUDIT  
**Evidence:** SF4

**Description:** SARS (South African Revenue Service) initiated a tax audit of RegimA Skin Treatments. This official regulatory action indicates scrutiny of tax affairs and potential discovery of financial irregularities.

**Significance:** SARS audit findings provide independent third-party verification of financial irregularities. Tax fraud carries criminal penalties and SARS has independent investigative powers.

---

## Relationship Network Implications

These new relations enhance our understanding of the fraud network:

1. **Accounting Firm Complicity:** Bantjies' role in documenting fraudulent debt structures
2. **Technical Control:** Rynette's system access enabling record manipulation
3. **Entity Creation:** Adderory as a potentially fictitious or controlled supplier
4. **Regulatory Scrutiny:** SARS audit as independent verification of irregularities

## Burden of Proof Assessment

| Relation | Civil (50%) | Criminal (95%) | Evidence Strength |
|----------|-------------|----------------|-------------------|
| Bantjies → SLG Debt | ✓ HIGH | ○ MEDIUM | Documentary, system-generated |
| Rynette → RegimA Control | ✓ HIGH | ○ MEDIUM | Visual evidence, screenshots |
| Adderory → RegimA Supply | ○ MEDIUM | ✗ LOW | Company records, contracts |
| SARS → RegimA Audit | ✓ HIGH | N/A | Official correspondence |

**Legend:**
- ✓ = Meets burden of proof
- ○ = Partially meets burden of proof
- ✗ = Does not meet burden of proof

## Next Steps

1. Integrate these relations into the entity relationship diagrams
2. Update GitHub Pages visualization of the fraud network
3. Cross-reference with existing events and timeline
4. Incorporate into legal filings where applicable

---

*Generated: 2025-12-18*  
*Source: Comprehensive cross-reference analysis with ad-res-j7 evidence*
"""
    
    with open(relations_file, 'w') as f:
        f.write(content)
    
    print("\nCreated RELATIONS_UPDATE_2025_12_18.md")

def main():
    print("=" * 80)
    print("IMPLEMENTING REFINEMENTS")
    print("=" * 80)
    print()
    
    create_new_entity_files()
    create_new_event_files()
    update_timeline_with_new_events()
    create_relations_documentation()
    
    print()
    print("=" * 80)
    print("REFINEMENTS IMPLEMENTED SUCCESSFULLY")
    print("=" * 80)
    print()
    print("Summary:")
    print("  - 3 new entities created")
    print("  - 8 new events created")
    print("  - Timeline updated with new events")
    print("  - Relations documentation created")
    print()

if __name__ == "__main__":
    main()
