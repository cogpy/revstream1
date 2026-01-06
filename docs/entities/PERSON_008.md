---
layout: default
title: Kayla
---
# Kayla (PERSON_008)

**Role:** estate_creditor

## Details

| Field | Value |
|---|---|
| Entity Id | PERSON_008 |
| Name | Kayla |
| Status | deceased |
| Role | estate_creditor |
| Agent Type | victim |
| Involvement Events | 2 |
| Additional Notes | Court order obtained to seize account from Kayla's email, interfering with law enforcement investigation that had instructed freeze |
| Evidence Enhanced | 2025-12-28T05:36:36.077463 |
| Evidence Strength | strong |

## Raw Data

```json
{
  "entity_id": "PERSON_008",
  "name": "Kayla",
  "status": "deceased",
  "role": "estate_creditor",
  "agent_type": "victim",
  "involvement_events": 2,
  "relationships": [
    "estate_creditor_of_ORG_002",
    "email_account_subject_to_court_order"
  ],
  "financial_impact": {
    "estate_debt_owed": "R1,035,000",
    "since": "Feb 2023",
    "primary_categories": [
      "unpaid_debt",
      "estate_fraud"
    ]
  },
  "additional_notes": "Court order obtained to seize account from Kayla's email, interfering with law enforcement investigation that had instructed freeze",
  "timeline_events": [
    "EVENT_023",
    "EVENT_054"
  ],
  "evidence": [
    "JF08 - Email evidence",
    "JF13 - Recent correspondence"
  ],
  "ad_res_j7_references": [
    "ANNEXURES/JF08 - Email correspondence evidence",
    "ANNEXURES/JF13 - Recent correspondence",
    "ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md - Death and estate documentation",
    "ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md - Email seizure court order"
  ],
  "evidence_enhanced": "2025-12-28T05:36:36.077463",
  "evidence_strength": "strong"
}
```
