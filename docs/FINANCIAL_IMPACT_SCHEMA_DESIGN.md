# Financial Impact Schema Design
## Structured Financial Data Model for Event Analysis

**Version**: 1.0  
**Date**: 2025-11-14  
**Status**: PROPOSED

---

## Executive Summary

This document defines a comprehensive, structured financial impact schema to replace the current free-text `financial_impact` field across all 53 events in the revstream1 data model. The schema enables precise financial analysis, automated aggregation, evidence strength tracking, and court-ready financial reporting.

---

## Current State Analysis

### Problems with Current Approach

**Inconsistent Formats:**
```json
"financial_impact": "R22,800,000"
"financial_impact": "R1,642,000"
"financial_impact": "R414,334.09"
"financial_impact": "unknown_amount"
"financial_impact": "R89.1M+"
```

**Issues:**
- Mixed precision (whole numbers vs. decimals)
- Inconsistent formatting (commas, decimals, abbreviations)
- No evidence strength indication
- No transaction type classification
- No multi-currency support
- Cannot distinguish between documented vs. estimated amounts
- Difficult to aggregate programmatically
- No breakdown for complex transactions

---

## Proposed Schema Structure

### Core Financial Impact Object

```json
{
  "financial_impact": {
    "total_amount": {
      "value": 22800000.00,
      "currency": "ZAR",
      "formatted": "R22,800,000.00",
      "precision": "exact"
    },
    "evidence_strength": "documented",
    "transaction_type": "capital_extraction",
    "impact_category": "profit_extraction",
    "breakdown": [
      {
        "description": "Members loan account balance",
        "amount": {
          "value": 22800000.00,
          "currency": "ZAR",
          "formatted": "R22,800,000.00"
        },
        "source_entity": "ORG_005",
        "target_entity": "members",
        "transaction_date": "2020-04-30",
        "evidence_reference": "villa_via_trial_balance_apr_2020"
      }
    ],
    "aggregation_notes": "Single transaction, members loan account",
    "court_presentation": "R22.8 million capital extraction via members loan"
  }
}
```

### Schema Field Definitions

#### 1. `total_amount` (Object, Required)

**Purpose**: Standardized representation of the total financial impact

**Fields:**
- `value` (Number, Required): Numeric value for computation (no formatting)
- `currency` (String, Required): ISO 4217 currency code (default: "ZAR")
- `formatted` (String, Required): Human-readable formatted string
- `precision` (Enum, Required): Level of precision
  - `"exact"`: Documented to the cent (e.g., R414,334.09)
  - `"rounded"`: Documented but rounded (e.g., R1,642,000)
  - `"estimated"`: Calculated estimate with basis (e.g., R100,000+)
  - `"minimum"`: Minimum known amount, actual higher (e.g., R89.1M+)
  - `"unknown"`: Amount exists but not quantified

**Examples:**
```json
// Exact precision
{
  "value": 414334.09,
  "currency": "ZAR",
  "formatted": "R414,334.09",
  "precision": "exact"
}

// Estimated precision
{
  "value": 100000.00,
  "currency": "ZAR",
  "formatted": "R100,000+",
  "precision": "estimated"
}

// Unknown amount
{
  "value": null,
  "currency": "ZAR",
  "formatted": "Unknown amount",
  "precision": "unknown"
}
```

#### 2. `evidence_strength` (Enum, Required)

**Purpose**: Indicates the quality and reliability of financial evidence

**Values:**
- `"documented"`: Direct evidence in financial records (trial balance, bank statement, invoice)
- `"inferred"`: Calculated from documented evidence (e.g., monthly rent × months)
- `"estimated"`: Reasonable estimate based on patterns (e.g., "R100,000+" from service expansion)
- `"alleged"`: Claimed but not yet verified
- `"unknown"`: Amount exists but no evidence available

**Court Implications:**
- `documented`: Admissible as direct evidence
- `inferred`: Admissible with supporting calculation
- `estimated`: Indicative only, requires qualification
- `alleged`: Requires corroboration
- `unknown`: Placeholder only

#### 3. `transaction_type` (Enum, Required)

**Purpose**: Classifies the nature of the financial transaction

**Values:**
- `"theft"`: Direct unauthorized taking (payment redirection, bank account changes)
- `"fraud"`: Deceptive misrepresentation for gain (false invoices, accounting fraud)
- `"misappropriation"`: Unauthorized use of funds (unauthorized transfers, fund diversions)
- `"capital_extraction"`: Profit extraction mechanisms (members loans, dividends)
- `"revenue_diversion"`: Redirecting income streams (domain hijacking, customer redirection)
- `"cost_manipulation"`: Artificial cost inflation/reallocation (inter-company charges)
- `"loan"`: Inter-company or external lending
- `"interest_payment"`: Loan interest charges
- `"service_fee"`: Legitimate or inflated service charges
- `"stock_adjustment"`: Inventory write-offs or disappearances
- `"asset_transfer"`: Movement of assets between entities
- `"expense_dumping"`: Allocation of expenses to victim entities
- `"other"`: Does not fit standard categories

#### 4. `impact_category` (Enum, Required)

**Purpose**: High-level categorization for pattern analysis

**Values:**
- `"profit_extraction"`: Mechanisms to extract profits from entities
- `"revenue_theft"`: Direct theft or diversion of revenue
- `"financial_manipulation"`: Accounting or cost manipulation
- `"trust_violation"`: Breach of fiduciary duties
- `"transfer_pricing_fraud"`: Inter-company pricing manipulation
- `"accounting_fraud"`: False financial reporting
- `"evidence_destruction"`: Destruction of financial records
- `"business_relationship"`: Legitimate business transactions
- `"infrastructure"`: Financial system setup (not inherently fraudulent)

#### 5. `breakdown` (Array of Objects, Optional)

**Purpose**: Detailed breakdown for complex or multi-part transactions

**When to Use:**
- Multiple transactions in single event
- Complex calculations requiring explanation
- Multiple entities involved
- Need to show component parts

**Object Structure:**
```json
{
  "description": "Human-readable description of this component",
  "amount": {
    "value": 1642000.00,
    "currency": "ZAR",
    "formatted": "R1,642,000.00"
  },
  "source_entity": "ORG_001",
  "target_entity": "ORG_002",
  "transaction_date": "2020-02-20",
  "evidence_reference": "trial_balance_2020_02",
  "calculation_basis": "Optional: how this was calculated"
}
```

**Example - Multi-component Transaction:**
```json
{
  "breakdown": [
    {
      "description": "RWW stock provision write-back",
      "amount": {"value": 500000.00, "currency": "ZAR", "formatted": "R500,000.00"},
      "source_entity": "ORG_001",
      "transaction_date": "2020-02-20"
    },
    {
      "description": "RWW admin fee reallocation to production",
      "amount": {"value": 810000.00, "currency": "ZAR", "formatted": "R810,000.00"},
      "source_entity": "ORG_001",
      "transaction_date": "2020-02-20"
    },
    {
      "description": "SLG admin fee reallocation to production",
      "amount": {"value": 252000.00, "currency": "ZAR", "formatted": "R252,000.00"},
      "source_entity": "ORG_004",
      "transaction_date": "2020-02-20"
    },
    {
      "description": "SLG production cost transfer to RST",
      "amount": {"value": 80000.00, "currency": "ZAR", "formatted": "R80,000.00"},
      "source_entity": "ORG_004",
      "target_entity": "ORG_002",
      "transaction_date": "2020-02-20"
    }
  ]
}
```

#### 6. `aggregation_notes` (String, Optional)

**Purpose**: Notes for financial analysts on how to aggregate this amount

**Examples:**
- `"Single transaction, full amount"`
- `"Part of larger R89M+ total, avoid double-counting with EVENT_042"`
- `"Monthly recurring, multiply by period for total impact"`
- `"Offset by REL_LOAN_002, net impact R164K"`

#### 7. `court_presentation` (String, Required)

**Purpose**: Pre-formatted, court-ready summary for legal documents

**Guidelines:**
- Concise, neutral language
- Include amount and nature
- Suitable for affidavits and court submissions
- No hyperbole or speculation

**Examples:**
- `"R22.8 million capital extraction via members loan"`
- `"R1.642 million inter-company cost reallocations"`
- `"R414,334.09 interest payment on inter-company loan"`
- `"Estimated R100,000+ service expansion establishing operational dependency"`

---

## Implementation Examples

### Example 1: Exact Documented Amount (Simple)

**Event**: EVENT_H012 - SLG Interest Payment to RST

```json
{
  "event_id": "EVENT_H012",
  "financial_impact": {
    "total_amount": {
      "value": 414334.09,
      "currency": "ZAR",
      "formatted": "R414,334.09",
      "precision": "exact"
    },
    "evidence_strength": "documented",
    "transaction_type": "interest_payment",
    "impact_category": "infrastructure",
    "breakdown": [
      {
        "description": "Interest payment per loan agreement",
        "amount": {
          "value": 414334.09,
          "currency": "ZAR",
          "formatted": "R414,334.09"
        },
        "source_entity": "ORG_004",
        "target_entity": "ORG_002",
        "transaction_date": "2020-02-28",
        "evidence_reference": "trial_balance_2020_02_28"
      }
    ],
    "aggregation_notes": "Single transaction, documents inter-company loan structure",
    "court_presentation": "R414,334.09 interest payment on inter-company loan from SLG to RST"
  }
}
```

### Example 2: Complex Multi-Component Transaction

**Event**: EVENT_H011 - Inter-company Cost Reallocations

```json
{
  "event_id": "EVENT_H011",
  "financial_impact": {
    "total_amount": {
      "value": 1642000.00,
      "currency": "ZAR",
      "formatted": "R1,642,000.00",
      "precision": "rounded"
    },
    "evidence_strength": "documented",
    "transaction_type": "cost_manipulation",
    "impact_category": "financial_manipulation",
    "breakdown": [
      {
        "description": "RWW stock provision write-back",
        "amount": {"value": 500000.00, "currency": "ZAR", "formatted": "R500,000.00"},
        "source_entity": "ORG_001",
        "transaction_date": "2020-02-20",
        "evidence_reference": "adjusting_journal_entries_2020_02"
      },
      {
        "description": "RWW admin fee reallocation to production costs",
        "amount": {"value": 810000.00, "currency": "ZAR", "formatted": "R810,000.00"},
        "source_entity": "ORG_001",
        "transaction_date": "2020-02-20",
        "evidence_reference": "adjusting_journal_entries_2020_02"
      },
      {
        "description": "SLG admin fee reallocation to production costs",
        "amount": {"value": 252000.00, "currency": "ZAR", "formatted": "R252,000.00"},
        "source_entity": "ORG_004",
        "transaction_date": "2020-02-20",
        "evidence_reference": "adjusting_journal_entries_2020_02"
      },
      {
        "description": "SLG production cost transfer to RST",
        "amount": {"value": 80000.00, "currency": "ZAR", "formatted": "R80,000.00"},
        "source_entity": "ORG_004",
        "target_entity": "ORG_002",
        "transaction_date": "2020-02-20",
        "evidence_reference": "adjusting_journal_entries_2020_02"
      }
    ],
    "aggregation_notes": "Four separate adjusting entries, total R1.642M cost manipulation infrastructure",
    "court_presentation": "R1.642 million in inter-company cost reallocations establishing cost manipulation infrastructure"
  }
}
```

### Example 3: Estimated Amount

**Event**: EVENT_H017 - Major Service Expansion

```json
{
  "event_id": "EVENT_H017",
  "financial_impact": {
    "total_amount": {
      "value": 100000.00,
      "currency": "ZAR",
      "formatted": "R100,000+",
      "precision": "estimated"
    },
    "evidence_strength": "estimated",
    "transaction_type": "service_fee",
    "impact_category": "business_relationship",
    "breakdown": [
      {
        "description": "Enterprise service expansion (estimated based on service scope)",
        "amount": {"value": 100000.00, "currency": "ZAR", "formatted": "R100,000+"},
        "source_entity": "ORG_002",
        "target_entity": "ORG_007",
        "transaction_date": "2017-09-30",
        "calculation_basis": "Estimated from service scope and typical enterprise pricing"
      }
    ],
    "aggregation_notes": "Estimated minimum, actual amount likely higher, establishes trust phase",
    "court_presentation": "Estimated R100,000+ service expansion establishing trust and operational dependency"
  }
}
```

### Example 4: Unknown Amount

**Event**: EVENT_H015 - Bantjes Trial Balance Distribution

```json
{
  "event_id": "EVENT_H015",
  "financial_impact": {
    "total_amount": {
      "value": null,
      "currency": "ZAR",
      "formatted": "No direct financial impact",
      "precision": "unknown"
    },
    "evidence_strength": "unknown",
    "transaction_type": "other",
    "impact_category": "evidence_documentation",
    "breakdown": [],
    "aggregation_notes": "Evidence of control, no direct financial transaction",
    "court_presentation": "Evidence of financial system control, no direct monetary impact"
  }
}
```

### Example 5: Minimum Known Amount

**Event**: EVENT_042 - Total Financial Impact Summary

```json
{
  "event_id": "EVENT_042",
  "financial_impact": {
    "total_amount": {
      "value": 89124266.00,
      "currency": "ZAR",
      "formatted": "R89,124,266+",
      "precision": "minimum"
    },
    "evidence_strength": "documented",
    "transaction_type": "other",
    "impact_category": "financial_manipulation",
    "breakdown": [],
    "aggregation_notes": "Aggregate of multiple events, actual total higher due to unknown amounts",
    "court_presentation": "Minimum documented financial impact of R89.1 million across all fraud categories"
  }
}
```

---

## Aggregation and Analysis Capabilities

### Automated Financial Reporting

With the structured schema, the following reports can be generated automatically:

#### 1. Total Impact by Evidence Strength

```python
{
  "documented": "R92,106,584.89",
  "inferred": "R2,450,000.00",
  "estimated": "R350,000+",
  "unknown": "15 events"
}
```

#### 2. Total Impact by Transaction Type

```python
{
  "theft": "R7,420,000.00",
  "capital_extraction": "R22,800,000.00",
  "cost_manipulation": "R1,642,000.00",
  "revenue_diversion": "R15,000,000+",
  ...
}
```

#### 3. Total Impact by Category

```python
{
  "profit_extraction": "R25,000,000+",
  "revenue_theft": "R22,000,000+",
  "financial_manipulation": "R18,000,000+",
  ...
}
```

#### 4. Timeline Financial Flow

```python
{
  "2017-06-30": {"event": "EVENT_H016", "amount": 250.80},
  "2017-09-30": {"event": "EVENT_H017", "amount": 100000.00},
  "2020-02-20": {"event": "EVENT_H011", "amount": 1642000.00},
  ...
}
```

### Court-Ready Financial Summary

Automatically generate formatted summaries for affidavits:

```
The total documented financial impact across 53 events is R92,106,584.89, 
comprising:
- R25.1 million in profit extraction mechanisms
- R22.0 million in revenue theft
- R18.0 million in financial manipulation
- R15.0 million in transfer pricing fraud
- R12.0 million in other categories

An additional 15 events have financial impact that could not be quantified 
from available evidence, indicating the actual total is substantially higher.
```

---

## Migration Strategy

### Phase 1: Schema Implementation (Current)

1. Define schema structure ✅
2. Create documentation ✅
3. Develop conversion scripts
4. Validate against all 53 events

### Phase 2: Data Conversion

1. Convert all documented amounts (35 events)
2. Convert all estimated amounts (8 events)
3. Convert all unknown amounts (10 events)
4. Validate totals match previous calculations

### Phase 3: Validation and Testing

1. Run aggregation tests
2. Generate financial reports
3. Verify court presentation strings
4. Cross-check with ad-res-j7 evidence

### Phase 4: Documentation and Deployment

1. Update metadata versions
2. Generate migration report
3. Commit and push changes
4. Create Phase 3 completion summary

---

## Benefits Summary

### For Legal Team

✅ **Court-Ready Summaries**: Pre-formatted financial statements for affidavits  
✅ **Evidence Strength Tracking**: Clear indication of admissibility  
✅ **Automated Aggregation**: Instant total calculations by category  
✅ **Breakdown Visibility**: Complex transactions explained clearly  

### For Financial Analysts

✅ **Precise Calculations**: Numeric values for computation  
✅ **Consistent Formatting**: Standardized across all events  
✅ **Pattern Analysis**: Transaction type and category grouping  
✅ **Timeline Analysis**: Financial flow over time  

### For Investigators

✅ **Evidence Traceability**: Direct links to source documents  
✅ **Transaction Classification**: Clear categorization of fraud types  
✅ **Entity Tracking**: Source and target entities for each amount  
✅ **Gap Identification**: Unknown amounts flagged for investigation  

### For System Integration

✅ **JSON Schema Validation**: Structured, validatable format  
✅ **Database Ready**: Direct mapping to SQL/NoSQL schemas  
✅ **API Friendly**: Easy to query and filter  
✅ **Hypergraph Compatible**: Entity relationships preserved  

---

## Conclusion

The proposed financial impact schema transforms unstructured financial data into a comprehensive, analyzable, and court-ready format. It enables:

1. **Precision**: Exact, rounded, estimated, or unknown amounts clearly distinguished
2. **Evidence**: Strength tracking from documented to unknown
3. **Classification**: Transaction types and impact categories for pattern analysis
4. **Breakdown**: Complex transactions explained with component parts
5. **Automation**: Aggregation, reporting, and court summaries generated automatically
6. **Traceability**: Direct links to evidence and entities

This schema provides the foundation for Phase 3 implementation and establishes best practices for financial data modeling in legal case management systems.

---

**Next Steps**: Proceed with conversion script development and implementation across all 53 events.

**Document Status**: FINAL  
**Version**: 1.0  
**Date**: 2025-11-14
