---
layout: default
title: Data Model Analysis
---

# Data Model Analysis Report

**Date:** 2025-11-19

This report provides a detailed, automated analysis of the structural integrity and completeness of the JSON data models powering this investigation. The analysis was performed to ensure data quality, identify gaps, and provide a transparent overview of the case's data foundation.

---

## 1. Metadata Summary

| Data Model | Version | Last Updated |
|------------|---------|--------------|
| Entities   | 9.1     | 2025-11-18   |
| Events     | 9.1     | 2025-11-19   |
| Relations  | 7.1     | 2025-11-19   |
| Timeline   | 8.1     | 2025-11-18   |

- **Total Events Tracked:** 69

---

## 2. Entity Analysis

| Entity Type       | Count |
|-------------------|-------|
| Persons           | 12    |
| Organizations     | 9     |
| Trusts            | 1     |
| Platforms         | 1     |
| Domains           | 2     |
| Bank Accounts     | 1     |

### Persons by Role

| Role                             | Count |
|----------------------------------|-------|
| accountant_and_unknown_trustee   | 1     |
| bookkeeper                       | 1     |
| co_conspirator                   | 1     |
| co_conspirator_family_member     | 1     |
| email_sender_witness             | 1     |
| estate_creditor                  | 1     |
| estate_related_party             | 1     |
| financial_professional           | 1     |
| first_respondent                 | 1     |
| primary_perpetrator              | 1     |
| second_respondent                | 1     |
| witness_and_victim               | 1     |

---

## 3. Event Analysis

- **Total Events:** 69

### Events by Category

| Category                 | Count |
|--------------------------|-------|
| financial_manipulation   | 12    |
| revenue_theft            | 7     |
| trust_violations         | 6     |
| financial_structure      | 3     |
| accounting_fraud         | 3     |
| fraud_concealment        | 3     |
| financial_fraud          | 3     |
| ... *(other categories)* | ...   |

### Events by Timeline Phase

| Phase                       | Event Count |
|-----------------------------|-------------|
| PHASE_000: Historical       | 14          |
| PHASE_001: Foundation       | 5           |
| PHASE_002: Initial Theft    | 5           |
| PHASE_003: Escalation       | 6           |
| PHASE_004: Consolidation    | 11          |
| PHASE_005: Control Seizure  | 9           |
| PHASE_006: Cover-up         | 8           |
| *Unassigned*                | 11          |

---

## 4. Data Integrity Checks

- **Event ID Uniqueness:** ✓ **Passed**. All 69 event IDs are unique.
- **Evidence Linkage:** ✓ **Passed**. 100% of events have associated evidence links.
- **Cross-Reference Integrity:** ✓ **Passed**. All event IDs referenced in the timeline exist in the main events model.

---

## 5. Financial Impact Summary

- **Events with Financial Data:** 54 (78% of total)
- **Estimated Total Financial Impact:** **R115,015,600**

*This is a conservative estimate based on direct financial values present in the event data.*

---

## 6. Recommendations

The data models are in excellent condition. The following minor refinements are recommended:

1.  **Review Unassigned Events:** Assign the 11 events currently marked as `unknown` to their correct timeline phase to complete the narrative sequence.
2.  **Review Person Entity:** Review the 1 person entity flagged for having no direct event involvement to confirm their role is accurate or if links are missing.

---

*This report was generated automatically by a Python script (`analyze_data_models.py`) to ensure objective and repeatable analysis.*
