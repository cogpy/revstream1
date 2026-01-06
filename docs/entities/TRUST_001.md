---
layout: default
title: Faucitt Family Trust
---
# Faucitt Family Trust (TRUST_001)

**Role:** family_trust_structure_manipulated

## Details

| Field | Value |
|---|---|
| Entity Id | TRUST_001 |
| Name | Faucitt Family Trust |
| Entity Type | family_trust |
| Agent Type | victim_entity |
| Role | family_trust_structure_manipulated |
| Founder | PERSON_001 |
| Legal Significance | trust_structure_manipulation_and_beneficiary_attack |
| Additional Notes | Bantjies is unknown trustee with R18.685M debt to trust, creating massive conflict of interest |
| Evidence Enhanced | 2025-12-28T05:36:36.077524 |
| Evidence Strength | strong |

## Raw Data

```json
{
  "entity_id": "TRUST_001",
  "name": "Faucitt Family Trust",
  "entity_type": "family_trust",
  "agent_type": "victim_entity",
  "role": "family_trust_structure_manipulated",
  "trustees": [
    "PERSON_001",
    "PERSON_007"
  ],
  "beneficiaries": [
    "PERSON_004",
    "PERSON_005"
  ],
  "founder": "PERSON_001",
  "owned_entities": [
    "ORG_001",
    "ORG_004"
  ],
  "key_characteristics": [
    "unusual_trustee_powers",
    "absence_of_beneficiary_powers",
    "founder_additional_powers",
    "used_for_attacking_beneficiaries"
  ],
  "financial_impact": {
    "debt_owed_by_trustee": "R18,685,000",
    "debtor": "PERSON_007"
  },
  "legal_significance": "trust_structure_manipulation_and_beneficiary_attack",
  "additional_notes": "Bantjies is unknown trustee with R18.685M debt to trust, creating massive conflict of interest",
  "relationships": [
    "trustee_PERSON_001",
    "beneficiary_PERSON_004",
    "beneficiary_PERSON_005",
    "asset_holder_for_regima_group"
  ],
  "evidence": [
    "JF10 - Trust documents",
    "Trust deed and amendments",
    "SF1 - Bantjies trustee appointment"
  ],
  "ad_res_j7_references": [
    "ANNEXURES/JF10 - Trust documents",
    "ANNEXURES/SF1_Bantjies_Debt_Documentation.md",
    "ANNEXURES/JF06 - Court documents and filings"
  ],
  "evidence_enhanced": "2025-12-28T05:36:36.077524",
  "evidence_strength": "strong"
}
```
