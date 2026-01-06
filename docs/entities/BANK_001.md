---
layout: default
title: ABSA Accounts (8 suspected fraudulent accounts)
---
# ABSA Accounts (8 suspected fraudulent accounts) (BANK_001)

**Role:** allegedly_fraudulently_opened

## Details

| Field | Value |
|---|---|
| Entity Id | BANK_001 |
| Account Type | business_account |
| Bank Name | ABSA |
| Entity Type | bank_account |
| Agent Type | instrument_of_fraud |
| Role | allegedly_fraudulently_opened |
| Controlled By | PERSON_002 |
| Additional Notes | One of 8 ABSA accounts allegedly opened by Rynette using Daniel's stolen card |
| Account Description | Multiple fraudulently opened accounts |
| Name | ABSA Accounts (8 suspected fraudulent accounts) |
| Evidence Enhanced | 2025-12-31T05:34:39.187421 |
| Evidence Strength | moderate |

## Raw Data

```json
{
  "entity_id": "BANK_001",
  "account_type": "business_account",
  "bank_name": "ABSA",
  "entity_type": "bank_account",
  "agent_type": "instrument_of_fraud",
  "role": "allegedly_fraudulently_opened",
  "controlled_by": "PERSON_002",
  "additional_notes": "One of 8 ABSA accounts allegedly opened by Rynette using Daniel's stolen card",
  "account_description": "Multiple fraudulently opened accounts",
  "relationships": [
    "controlled_by_PERSON_002",
    "used_for_payment_redirection",
    "linked_to_fraud_scheme"
  ],
  "name": "ABSA Accounts (8 suspected fraudulent accounts)",
  "evidence": [
    "JF07 - Financial transaction records",
    "JF08 - Evidence of unauthorized account openings"
  ],
  "ad_res_j7_references": [
    "ANNEXURES/JF07 - Bank account transaction records",
    "ANNEXURES/JF08/evidence_package_20251012 - Unauthorized banking activity"
  ],
  "evidence_enhanced": "2025-12-31T05:34:39.187421",
  "evidence_strength": "moderate"
}
```
