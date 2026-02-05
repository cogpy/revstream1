#!/usr/bin/env python3
"""
Update data models with new evidence from February 2026 documents.

New Evidence Package:
1. Power Point - how sales work (11 Apr 2025) - Shopify centrality organogram
2. Fw: update - Some Initial Information (6 Jun 2025) - Company structure breakdown
3. CIPC Record - RegimA SA (347975701) - Dan & Pete as directors, NOT Jacqui
4. POPIA Violation Notice (8 Jul 2025) - Customer data breach complaint
5. Rynette & De Novo emails (17-18 Jun 2025) - Fraudulent record instructions
6. RegimA SA 2019 Financial Statements - Fabricated (issued 25 Jun 2025!)
7. Shopify Sales Report - Revenue diversion evidence
8. Formal Notice - Cessation of Criminal Instructions (8 Jul 2025)
9. Bank Statement Oct 2024 - Healthy R2.5M balance
10. Bank Statement Mar 2025 - Stripped to R5K
11. Shopify Invoice Sep 2025 - 9 payment failures
"""

import json
import os
from datetime import datetime

# Paths
ENTITIES_PATH = "/home/ubuntu/revstream1/data_models/entities/entities.json"
EVENTS_PATH = "/home/ubuntu/revstream1/data_models/events/events.json"
TIMELINE_PATH = "/home/ubuntu/revstream1/data_models/timelines/timeline.json"
RELATIONS_PATH = "/home/ubuntu/revstream1/data_models/relations/relations.json"

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    # Backup first
    backup_path = path.replace('.json', f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            backup_data = f.read()
        with open(backup_path, 'w') as f:
            f.write(backup_data)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")
    print(f"Backup: {backup_path}")

def update_entities(entities):
    """Add new entities from February 2026 evidence."""
    
    # New organization: De Novo Business Services
    de_novo = {
        "entity_id": "ORG_DE_NOVO",
        "name": "De Novo Business Services (Pty) Ltd",
        "type": "accounting_firm",
        "role": "complicit_accountant",
        "agent_type": "antagonist",
        "address": "43 Allouette Road, Impala Park, Boksburg, 1459",
        "phone": "(011) 452-0789 / 084 764 1045",
        "website": "www.denovobus.co.za",
        "involvement_events": 2,
        "primary_actions": [
            "fraudulent_record_creation",
            "backdated_financial_statements",
            "false_loan_account_creation"
        ],
        "relationships": [
            "instructed_by_PERSON_002",
            "prepared_fraudulent_statements_for_ORG_REGIMA_SA"
        ],
        "evidence": [
            "2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf",
            "Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf"
        ],
        "evidence_strength": "conclusive",
        "criminal_threshold": "95%_exceeded",
        "legal_implications": [
            "Professional misconduct",
            "Assisting in fraud",
            "Creating false financial records"
        ],
        "created_date": "2026-02-05",
        "source": "New evidence package Feb 2026"
    }
    
    # New person: Marisca Meyer
    marisca_meyer = {
        "entity_id": "PERSON_039",
        "name": "Marisca Meyer",
        "role": "complicit_accountant",
        "agent_type": "antagonist",
        "title": "Professional Accountant (SA)",
        "organization": "De Novo Business Services (Pty) Ltd",
        "email": "mmeyer@denovobus.co.za",
        "involvement_events": 2,
        "primary_actions": [
            "prepared_backdated_2019_financial_statements",
            "received_fraudulent_allocation_instructions",
            "created_false_loan_accounts"
        ],
        "relationships": [
            "employee_of_ORG_DE_NOVO",
            "instructed_by_PERSON_002",
            "prepared_statements_for_ORG_REGIMA_SA"
        ],
        "evidence": [
            "2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf - Email recipient",
            "Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf - Listed as Preparer"
        ],
        "evidence_strength": "conclusive",
        "criminal_threshold": "95%_likely",
        "key_evidence": {
            "financial_statements_issued": "2025-06-25",
            "period_covered": "15 months ended 28 February 2019",
            "backdating_gap": "6+ years",
            "fraud_indicator": "Created 2019 statements in June 2025"
        },
        "created_date": "2026-02-05",
        "source": "New evidence package Feb 2026"
    }
    
    # New person: Nadine Van Greunen
    nadine_van_greunen = {
        "entity_id": "PERSON_040",
        "name": "Nadine Van Greunen",
        "role": "complicit_accountant",
        "agent_type": "antagonist",
        "organization": "De Novo Business Services (Pty) Ltd",
        "email": "nvangreunen@denovobus.co.za",
        "phone": "(011) 452-0789",
        "involvement_events": 1,
        "primary_actions": [
            "received_fraudulent_allocation_instructions"
        ],
        "relationships": [
            "employee_of_ORG_DE_NOVO",
            "colleague_of_PERSON_039"
        ],
        "evidence": [
            "2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf - Email participant"
        ],
        "created_date": "2026-02-05",
        "source": "New evidence package Feb 2026"
    }
    
    # Add new entities
    entities["entities"]["organizations"].append(de_novo)
    entities["entities"]["persons"].append(marisca_meyer)
    entities["entities"]["persons"].append(nadine_van_greunen)
    
    # Update Rynette Farrar (PERSON_002) with new evidence
    for person in entities["entities"]["persons"]:
        if person["entity_id"] == "PERSON_002":
            person["primary_actions"].extend([
                "instructed_de_novo_fraudulent_records",
                "created_shopify_centrality_organogram",
                "coordinated_financial_statement_fabrication"
            ])
            person["relationships"].append("instructed_ORG_DE_NOVO")
            person["evidence"].extend([
                "2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf",
                "Power point - how sales work.pdf (11 Apr 2025)"
            ])
            person["de_novo_fraud_evidence"] = {
                "date": "2025-06-17 to 2025-06-18",
                "instruction": "Create loan account within RegimA SA for other company expenses",
                "purpose": "Hide expenses not belonging to RegimA SA",
                "recipient": "Marisca Meyer at De Novo Business Services",
                "dan_knowledge": "NOT copied - done without director knowledge"
            }
            person["organogram_evidence"] = {
                "date": "2025-04-11",
                "document": "Power point - how sales work.pdf",
                "purpose": "Created for Pete showing Shopify centrality",
                "significance": "40 days before May 22 sabotage - proves premeditation"
            }
            break
    
    # Update Peter Faucitt (PERSON_001) with fiduciary breach evidence
    for person in entities["entities"]["persons"]:
        if person["entity_id"] == "PERSON_001":
            person["primary_actions"].extend([
                "fiduciary_breach_regima_sa",
                "company_destruction_to_harm_co_director",
                "shopify_revenue_diversion"
            ])
            person["evidence"].extend([
                "347975701_REGIMA_SA_K201708793507.Pdf - CIPC record showing director status",
                "FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.pdf",
                "POPIA_VIOLATION_NOTICE_&_RETALIATION_TIMELINE.pdf",
                "62707308252 2024-10-07.pdf - Bank statement showing healthy business",
                "62707308252 2025-03-06.pdf - Bank statement showing asset stripping",
                "RegimA SA Shopify Plus - Total sales over time.pdf"
            ])
            person["fiduciary_breach_evidence"] = {
                "company": "RegimA SA (Pty) Ltd",
                "registration": "2017/087935/07",
                "director_since": "2021-03-08",
                "co_director": "Daniel Faucitt",
                "jacqui_status": "NOT a director or shareholder",
                "breach_actions": [
                    "Allowed company bank account to be stripped from R2.5M to R5K",
                    "Diverted Shopify revenue stream (R8.5M annual)",
                    "Failed to fulfill orders causing 9 consecutive payment failures",
                    "Instructed staff to bypass Shopify systems",
                    "Cancelled co-director's bank cards"
                ],
                "companies_act_violations": [
                    "Section 76 - Duty to act in good faith",
                    "Section 77 - Liability for breach of fiduciary duties",
                    "Section 69 - Grounds for director disqualification"
                ]
            }
            person["shopify_diversion_evidence"] = {
                "pre_diversion_revenue": "R800K-1.1M monthly",
                "post_diversion_revenue": "R0 (June 2025 onwards)",
                "diversion_date": "~22 May 2025",
                "organogram_date": "11 April 2025",
                "premeditation_gap": "40 days"
            }
            break
    
    # Update metadata
    entities["metadata"]["version"] = "39.0_NEW_EVIDENCE_2026_02_05"
    entities["metadata"]["last_updated"] = datetime.now().isoformat()
    entities["metadata"]["changes"] = "Added De Novo Business Services, Marisca Meyer, Nadine Van Greunen; Updated Rynette and Peter with fiduciary breach and fraudulent records evidence"
    entities["metadata"]["total_entities"] = len(entities["entities"]["persons"]) + len(entities["entities"]["organizations"])
    entities["metadata"]["total_persons"] = len(entities["entities"]["persons"])
    entities["metadata"]["total_organizations"] = len(entities["entities"]["organizations"])
    
    return entities

def update_events(events):
    """Add new events from February 2026 evidence."""
    
    new_events = [
        {
            "event_id": "EVENT_ORGANOGRAM_2025_04_11",
            "date": "2025-04-11",
            "title": "Rynette Creates Shopify Centrality Organogram",
            "description": "Rynette Farrar creates PowerPoint organogram for Peter showing Shopify as central hub for all sales operations. Document proves full understanding of Shopify's role 40 days before sabotage.",
            "category": "premeditation",
            "significance_level": "criminal_threshold",
            "actors": ["PERSON_002", "PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA", "PLATFORM_SHOPIFY"],
            "evidence": ["Power point - how sales work.pdf"],
            "evidence_strength": "conclusive",
            "legal_implications": [
                "Proves premeditation of Shopify sabotage",
                "Shows knowledge of business-critical systems",
                "Establishes conspiracy timeline"
            ]
        },
        {
            "event_id": "EVENT_SHOPIFY_SABOTAGE_2025_05_22",
            "date": "2025-05-22",
            "title": "Shopify Revenue Stream Sabotage/Diversion",
            "description": "Revenue stream diverted from RegimA SA Shopify stores. Monthly revenue dropped from R800K-1.1M to R0. 40 days after organogram creation.",
            "category": "revenue_theft",
            "significance_level": "criminal_threshold",
            "actors": ["PERSON_001", "PERSON_002"],
            "entities_involved": ["ORG_REGIMA_SA", "PLATFORM_SHOPIFY"],
            "evidence": ["RegimA SA Shopify Plus - Total sales over time.pdf"],
            "financial_impact": {
                "monthly_loss": "R800,000 - R1,100,000",
                "annual_loss": "R8,500,000+",
                "affected_stores": 9
            },
            "evidence_strength": "conclusive"
        },
        {
            "event_id": "EVENT_DAN_FRAUD_REPORT_2025_06_06",
            "date": "2025-06-06",
            "title": "Daniel Reports Fraud to Accountant Bantjies",
            "description": "Daniel Faucitt and Jacqui Faucitt report fraud concerns to accountant Danie Bantjies via email. Includes full breakdown of company shareholding, directorships, Shopify stores, QuickBooks accounts.",
            "category": "whistleblowing",
            "significance_level": "high",
            "actors": ["PERSON_003", "PERSON_004"],
            "entities_involved": ["ORG_REGIMA_SA", "ORG_REGIMA_ZONE"],
            "evidence": ["Fw_ update - Some Initial Information & Operating Entity Lists.pdf"],
            "key_disclosures": [
                "Over R1 million misallocated in RegimA Skin Treatments",
                "Accounts not reconciled since August 2023",
                "4 legally distinct company groups identified"
            ]
        },
        {
            "event_id": "EVENT_CARD_CANCELLATION_2025_06_07",
            "date": "2025-06-07",
            "title": "Peter Cancels All Bank Cards (Retaliation)",
            "description": "Within 24 hours of fraud report to accountant, Peter cancels ALL bank cards. R1,062,446.04 company expenses forced onto Daniel's personal account.",
            "category": "retaliation",
            "significance_level": "criminal_threshold",
            "actors": ["PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"],
            "evidence": ["POPIA_VIOLATION_NOTICE_&_RETALIATION_TIMELINE.pdf"],
            "financial_impact": {
                "forced_personal_expense": "R1,062,446.04"
            },
            "retaliation_timing": "Less than 24 hours after fraud report"
        },
        {
            "event_id": "EVENT_DE_NOVO_FRAUD_INSTRUCTION_2025_06_17",
            "date": "2025-06-17",
            "title": "Rynette Instructs De Novo to Create Fraudulent Records",
            "description": "Rynette Farrar emails De Novo Business Services instructing them to create loan accounts to hide expenses not belonging to RegimA SA. Daniel NOT copied on emails.",
            "category": "fraud",
            "significance_level": "criminal_threshold",
            "actors": ["PERSON_002", "PERSON_039", "PERSON_040"],
            "entities_involved": ["ORG_DE_NOVO", "ORG_REGIMA_SA", "ORG_REZONANCE"],
            "evidence": ["2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf"],
            "fraud_instructions": [
                "Create loan account within RegimA SA for other company",
                "Post Coral Draw and QuickBooks expenses to Rezonance loan account",
                "Hide expenses not belonging to RegimA SA"
            ],
            "evidence_strength": "conclusive"
        },
        {
            "event_id": "EVENT_FABRICATED_FINANCIALS_2025_06_25",
            "date": "2025-06-25",
            "title": "De Novo Creates Backdated 2019 Financial Statements",
            "description": "De Novo Business Services issues 'Annual Financial Statements for 15 months ended 28 February 2019' - created 6+ years after the period. Prepared by Marisca Meyer without Daniel's knowledge.",
            "category": "fraud",
            "significance_level": "criminal_threshold",
            "actors": ["PERSON_039", "ORG_DE_NOVO"],
            "entities_involved": ["ORG_REGIMA_SA"],
            "evidence": ["Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf"],
            "fraud_indicators": [
                "Issued 25 June 2025 for 2019 financial year",
                "Created 7 days after fraudulent instruction email",
                "Not audited or independently reviewed",
                "Director Daniel Faucitt not consulted"
            ],
            "legal_implications": [
                "Section 29 Companies Act - Accurate financial statements",
                "Section 214 Tax Administration Act - Fraudulent tax returns",
                "Section 77 Companies Act - Director liability"
            ]
        },
        {
            "event_id": "EVENT_FORMAL_NOTICE_2025_07_08",
            "date": "2025-07-08",
            "title": "Daniel Sends Formal Notice - Cessation of Criminal Instructions",
            "description": "Daniel Faucitt sends formal notice to Peter demanding cessation of criminal instructions to employees. Cites POPI Act violations, fiduciary breach, potential fraud. 48-hour deadline given.",
            "category": "compliance_demand",
            "significance_level": "high",
            "actors": ["PERSON_003", "PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"],
            "evidence": ["FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.pdf"],
            "demands": [
                "Rescind all instructions to bypass Shopify",
                "Confirm all orders must use approved systems",
                "Restore proper corporate governance",
                "Provide withheld bank cards for director oversight"
            ],
            "consequences_warned": [
                "Criminal charges",
                "Director delinquency proceedings",
                "Personal liability for all losses"
            ],
            "response": "Peter did NOT comply - filed ex parte application 36 days later"
        },
        {
            "event_id": "EVENT_POPIA_NOTICE_2025_07_08",
            "date": "2025-07-08",
            "title": "Daniel Sends POPIA Violation Notice to Peter",
            "description": "Daniel sends POPIA Violation Notice regarding customer data breach related to May 22nd Shopify revenue stream diversion.",
            "category": "compliance_demand",
            "significance_level": "high",
            "actors": ["PERSON_003", "PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"],
            "evidence": ["POPIA_VIOLATION_NOTICE_&_RETALIATION_TIMELINE.pdf"],
            "violations_cited": [
                "Unauthorized data access instructions",
                "Customer data breach",
                "Audit trail disappearance"
            ]
        },
        {
            "event_id": "EVENT_SHOPIFY_PAYMENT_FAILURES_2025_09",
            "date": "2025-09-27",
            "title": "RegimA SA Shopify Payment Failures Begin",
            "description": "RegimA SA unable to pay R60,960.11 monthly Shopify bill. 9 consecutive payment failures from Sep 27 to Oct 11, 2025. Company financially crippled by revenue diversion.",
            "category": "financial_collapse",
            "significance_level": "high",
            "actors": ["ORG_REGIMA_SA"],
            "entities_involved": ["ORG_REGIMA_SA", "PLATFORM_SHOPIFY"],
            "evidence": ["RegimA_SA_423808676.pdf"],
            "payment_failures": [
                "Sep 27 - Payment failed",
                "Sep 29 - Payment failed",
                "Oct 1 - Payment failed",
                "Oct 3 - Payment failed",
                "Oct 5 - Payment failed",
                "Oct 7 - Payment failed",
                "Oct 9 - Payment failed",
                "Oct 11 - Payment failed"
            ],
            "financial_impact": {
                "monthly_bill": "R60,960.11",
                "consequence": "Shopify store suspension risk",
                "affected_tenants": "1100+ B2B salons"
            }
        }
    ]
    
    # Add new events
    if "events" not in events:
        events["events"] = []
    events["events"].extend(new_events)
    
    # Update metadata
    events["metadata"]["version"] = "35.0_NEW_EVIDENCE_2026_02_05"
    events["metadata"]["last_updated"] = datetime.now().isoformat()
    events["metadata"]["changes"] = "Added 9 new events from February 2026 evidence package"
    events["metadata"]["total_events"] = len(events["events"])
    
    return events

def update_timeline(timeline):
    """Add new timeline entries from February 2026 evidence."""
    
    new_entries = [
        {
            "date": "2024-10-07",
            "event": "RegimA SA bank account healthy - R2,554,860.93 closing balance",
            "entity": "RegimA SA (Pty) Ltd",
            "source": "62707308252 2024-10-07.pdf",
            "significance_level": "high",
            "category": "financial_baseline",
            "event_ref": "EVENT_BANK_HEALTHY_2024_10",
            "actors": [],
            "entities_involved": ["ORG_REGIMA_SA"],
            "financial_data": {
                "opening_balance": "R1,925,869.31",
                "closing_balance": "R2,554,860.93",
                "status": "HEALTHY"
            }
        },
        {
            "date": "2025-03-06",
            "event": "RegimA SA bank account stripped - R5,284.08 closing balance (99.8% decline)",
            "entity": "RegimA SA (Pty) Ltd",
            "source": "62707308252 2025-03-06.pdf",
            "significance_level": "criminal_threshold",
            "category": "asset_stripping",
            "event_ref": "EVENT_BANK_STRIPPED_2025_03",
            "actors": ["PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"],
            "financial_data": {
                "opening_balance": "R997,597.94",
                "closing_balance": "R5,284.08",
                "decline_percentage": "99.8%",
                "status": "STRIPPED"
            }
        },
        {
            "date": "2025-04-11",
            "event": "Rynette creates Shopify centrality organogram for Peter - 40 days before sabotage",
            "entity": "Rynette Farrar",
            "source": "Power point - how sales work.pdf",
            "significance_level": "criminal_threshold",
            "category": "premeditation",
            "event_ref": "EVENT_ORGANOGRAM_2025_04_11",
            "actors": ["PERSON_002", "PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA", "PLATFORM_SHOPIFY"]
        },
        {
            "date": "2025-05-22",
            "event": "Shopify revenue stream sabotage - R800K-1.1M monthly revenue drops to R0",
            "entity": "RegimA SA (Pty) Ltd",
            "source": "RegimA SA Shopify Plus - Total sales over time.pdf",
            "significance_level": "criminal_threshold",
            "category": "revenue_theft",
            "event_ref": "EVENT_SHOPIFY_SABOTAGE_2025_05_22",
            "actors": ["PERSON_001", "PERSON_002"],
            "entities_involved": ["ORG_REGIMA_SA", "PLATFORM_SHOPIFY"]
        },
        {
            "date": "2025-06-06",
            "event": "Daniel reports fraud to accountant Bantjies with full company structure breakdown",
            "entity": "Daniel Faucitt",
            "source": "Fw_ update - Some Initial Information & Operating Entity Lists.pdf",
            "significance_level": "high",
            "category": "whistleblowing",
            "event_ref": "EVENT_DAN_FRAUD_REPORT_2025_06_06",
            "actors": ["PERSON_003", "PERSON_004"],
            "entities_involved": ["ORG_REGIMA_SA", "ORG_REGIMA_ZONE"]
        },
        {
            "date": "2025-06-07",
            "event": "Peter cancels ALL bank cards within 24 hours of fraud report - R1,062,446.04 forced onto Dan's personal account",
            "entity": "Peter Faucitt",
            "source": "POPIA_VIOLATION_NOTICE_&_RETALIATION_TIMELINE.pdf",
            "significance_level": "criminal_threshold",
            "category": "retaliation",
            "event_ref": "EVENT_CARD_CANCELLATION_2025_06_07",
            "actors": ["PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"]
        },
        {
            "date": "2025-06-17",
            "event": "Rynette instructs De Novo to create fraudulent loan accounts - Dan NOT copied",
            "entity": "Rynette Farrar",
            "source": "2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf",
            "significance_level": "criminal_threshold",
            "category": "fraud",
            "event_ref": "EVENT_DE_NOVO_FRAUD_INSTRUCTION_2025_06_17",
            "actors": ["PERSON_002", "PERSON_039", "PERSON_040"],
            "entities_involved": ["ORG_DE_NOVO", "ORG_REGIMA_SA"]
        },
        {
            "date": "2025-06-25",
            "event": "De Novo creates backdated 2019 financial statements - 6+ years after period",
            "entity": "De Novo Business Services",
            "source": "Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf",
            "significance_level": "criminal_threshold",
            "category": "fraud",
            "event_ref": "EVENT_FABRICATED_FINANCIALS_2025_06_25",
            "actors": ["PERSON_039", "ORG_DE_NOVO"],
            "entities_involved": ["ORG_REGIMA_SA"]
        },
        {
            "date": "2025-07-08",
            "event": "Daniel sends Formal Notice - Cessation of Criminal Instructions with 48-hour deadline",
            "entity": "Daniel Faucitt",
            "source": "FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.pdf",
            "significance_level": "high",
            "category": "compliance_demand",
            "event_ref": "EVENT_FORMAL_NOTICE_2025_07_08",
            "actors": ["PERSON_003", "PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"]
        },
        {
            "date": "2025-07-08",
            "event": "Daniel sends POPIA Violation Notice regarding customer data breach",
            "entity": "Daniel Faucitt",
            "source": "POPIA_VIOLATION_NOTICE_&_RETALIATION_TIMELINE.pdf",
            "significance_level": "high",
            "category": "compliance_demand",
            "event_ref": "EVENT_POPIA_NOTICE_2025_07_08",
            "actors": ["PERSON_003", "PERSON_001"],
            "entities_involved": ["ORG_REGIMA_SA"]
        },
        {
            "date": "2025-09-27",
            "event": "RegimA SA Shopify payment failures begin - 9 consecutive failures through Oct 11",
            "entity": "RegimA SA (Pty) Ltd",
            "source": "RegimA_SA_423808676.pdf",
            "significance_level": "high",
            "category": "financial_collapse",
            "event_ref": "EVENT_SHOPIFY_PAYMENT_FAILURES_2025_09",
            "actors": [],
            "entities_involved": ["ORG_REGIMA_SA", "PLATFORM_SHOPIFY"]
        }
    ]
    
    # Add new entries
    timeline["timeline"].extend(new_entries)
    
    # Sort by date
    timeline["timeline"].sort(key=lambda x: x["date"])
    
    # Update metadata
    timeline["metadata"]["version"] = "32.0_NEW_EVIDENCE_2026_02_05"
    timeline["metadata"]["last_updated"] = datetime.now().isoformat()
    timeline["metadata"]["changes"] = "Added 11 new timeline entries from February 2026 evidence package"
    timeline["metadata"]["total_entries"] = len(timeline["timeline"])
    
    # Update year counts
    year_counts = {}
    for entry in timeline["timeline"]:
        year = entry["date"][:4]
        year_counts[year] = year_counts.get(year, 0) + 1
    timeline["metadata"]["by_year"] = dict(sorted(year_counts.items()))
    
    return timeline

def update_relations(relations):
    """Add new relations from February 2026 evidence."""
    
    new_relations = [
        {
            "relation_id": "REL_RYNETTE_DE_NOVO",
            "type": "instructed",
            "source_entity": "PERSON_002",
            "target_entity": "ORG_DE_NOVO",
            "description": "Rynette instructed De Novo to create fraudulent loan accounts",
            "date": "2025-06-17",
            "evidence": ["2025-06-18 - Rynette & De Novo - RegimA SA Payments.pdf"],
            "significance": "criminal_threshold"
        },
        {
            "relation_id": "REL_DE_NOVO_REGIMA_SA",
            "type": "prepared_fraudulent_statements",
            "source_entity": "ORG_DE_NOVO",
            "target_entity": "ORG_REGIMA_SA",
            "description": "De Novo prepared backdated 2019 financial statements for RegimA SA",
            "date": "2025-06-25",
            "evidence": ["Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf"],
            "significance": "criminal_threshold"
        },
        {
            "relation_id": "REL_MARISCA_DE_NOVO",
            "type": "employed_by",
            "source_entity": "PERSON_039",
            "target_entity": "ORG_DE_NOVO",
            "description": "Marisca Meyer is Professional Accountant at De Novo Business Services",
            "evidence": ["Regima SA (Pty) Ltd - 2019 - Financial statements - SME.pdf"],
            "significance": "high"
        },
        {
            "relation_id": "REL_PETER_FIDUCIARY_BREACH",
            "type": "fiduciary_breach",
            "source_entity": "PERSON_001",
            "target_entity": "ORG_REGIMA_SA",
            "description": "Peter breached fiduciary duty as director by allowing company destruction",
            "date_range": "2025-03 to 2025-10",
            "evidence": [
                "347975701_REGIMA_SA_K201708793507.Pdf",
                "62707308252 2025-03-06.pdf",
                "RegimA SA Shopify Plus - Total sales over time.pdf",
                "RegimA_SA_423808676.pdf"
            ],
            "significance": "criminal_threshold",
            "legal_basis": [
                "Companies Act Section 76",
                "Companies Act Section 77",
                "Companies Act Section 69"
            ]
        },
        {
            "relation_id": "REL_RYNETTE_ORGANOGRAM",
            "type": "created_premeditation_evidence",
            "source_entity": "PERSON_002",
            "target_entity": "PERSON_001",
            "description": "Rynette created Shopify centrality organogram for Peter 40 days before sabotage",
            "date": "2025-04-11",
            "evidence": ["Power point - how sales work.pdf"],
            "significance": "criminal_threshold"
        }
    ]
    
    # Add new relations to fraud_relations category
    if "fraud_relations" not in relations["relations"]:
        relations["relations"]["fraud_relations"] = []
    relations["relations"]["fraud_relations"].extend(new_relations)
    
    # Count total relations across all categories
    total = 0
    for category in relations["relations"].values():
        if isinstance(category, list):
            total += len(category)
    
    # Update metadata
    relations["metadata"]["version"] = "17.0_NEW_EVIDENCE_2026_02_05"
    relations["metadata"]["last_updated"] = datetime.now().isoformat()
    relations["metadata"]["changes"] = "Added 5 new fraud relations from February 2026 evidence package"
    relations["metadata"]["total_relations"] = total
    
    return relations

def main():
    print("=" * 60)
    print("Updating data models with February 2026 evidence")
    print("=" * 60)
    
    # Load existing data
    print("\nLoading existing data models...")
    entities = load_json(ENTITIES_PATH)
    events = load_json(EVENTS_PATH)
    timeline = load_json(TIMELINE_PATH)
    relations = load_json(RELATIONS_PATH)
    
    # Update each model
    print("\nUpdating entities...")
    entities = update_entities(entities)
    
    print("\nUpdating events...")
    events = update_events(events)
    
    print("\nUpdating timeline...")
    timeline = update_timeline(timeline)
    
    print("\nUpdating relations...")
    relations = update_relations(relations)
    
    # Save updated data
    print("\nSaving updated data models...")
    save_json(ENTITIES_PATH, entities)
    save_json(EVENTS_PATH, events)
    save_json(TIMELINE_PATH, timeline)
    save_json(RELATIONS_PATH, relations)
    
    print("\n" + "=" * 60)
    print("Data model updates complete!")
    print("=" * 60)
    
    # Summary
    print("\nSummary of changes:")
    print(f"- Entities: {entities['metadata']['total_entities']} total ({entities['metadata']['total_persons']} persons, {entities['metadata']['total_organizations']} organizations)")
    print(f"- Events: {events['metadata']['total_events']} total")
    print(f"- Timeline: {timeline['metadata']['total_entries']} entries")
    print(f"- Relations: {relations['metadata']['total_relations']} total")
    
    print("\nNew entities added:")
    print("- ORG_DE_NOVO: De Novo Business Services (Pty) Ltd")
    print("- PERSON_039: Marisca Meyer (Professional Accountant)")
    print("- PERSON_040: Nadine Van Greunen (De Novo staff)")
    
    print("\nNew events added:")
    print("- EVENT_ORGANOGRAM_2025_04_11: Shopify centrality organogram")
    print("- EVENT_SHOPIFY_SABOTAGE_2025_05_22: Revenue stream diversion")
    print("- EVENT_DAN_FRAUD_REPORT_2025_06_06: Fraud report to accountant")
    print("- EVENT_CARD_CANCELLATION_2025_06_07: Retaliation card cancellation")
    print("- EVENT_DE_NOVO_FRAUD_INSTRUCTION_2025_06_17: Fraudulent records instruction")
    print("- EVENT_FABRICATED_FINANCIALS_2025_06_25: Backdated financial statements")
    print("- EVENT_FORMAL_NOTICE_2025_07_08: Cessation of criminal instructions")
    print("- EVENT_POPIA_NOTICE_2025_07_08: POPIA violation notice")
    print("- EVENT_SHOPIFY_PAYMENT_FAILURES_2025_09: Payment failures begin")

if __name__ == "__main__":
    main()
