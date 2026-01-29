#!/usr/bin/env python3
"""
Comprehensive Model Refinement Script
Integrates FNB Fraud Letter evidence and refines all data models.
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_DOCS = Path("/home/ubuntu/revstream1/docs")
DATA_MODELS = REVSTREAM_DOCS / "data_models"
EVENTS_PATH = DATA_MODELS / "events.json"
TIMELINE_PATH = DATA_MODELS / "timeline.json"
ENTITIES_PATH = DATA_MODELS / "entities" / "entities.json"
RELATIONS_PATH = DATA_MODELS / "relations.json"

def load_json(path):
    """Load JSON file."""
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    """Save JSON file."""
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}")

def analyze_june_2025_timeline():
    """Analyze and document the June 2025 timeline with FNB letter context."""
    
    june_2025_timeline = {
        "title": "June 2025 Critical Timeline - Fraud Exposure and Response",
        "description": "Timeline showing the sequence of events from fraud exposure to FNB letter",
        "events": [
            {
                "date": "2025-06-06",
                "event": "Daniel Finalizes Fraud Reports",
                "event_id": "EVENT_011",
                "description": "Daniel finalizes comprehensive fraud reports after using time from March 30 deadline extension",
                "significance": "Fraud formally documented"
            },
            {
                "date": "2025-06-06",
                "event": "Daniel Sends Reports to Bantjies",
                "event_id": "EVENT_057",
                "description": "Daniel sends comprehensive documentation to Bantjies (accountant) including listing of all companies, Shopify store operations, and preliminary reports",
                "significance": "Full transparency demonstrated"
            },
            {
                "date": "2025-06-07",
                "event": "Secret Card Cancellations",
                "event_id": "EVENT_012",
                "description": "Secret cancellation of cards to sabotage Daniel's ability to pay creditors - less than 24 hours after fraud exposure",
                "significance": "Immediate retaliation for fraud exposure",
                "days_after_exposure": 1
            },
            {
                "date": "2025-06-17",
                "event": "Peter Writes FNB Fraud Letter",
                "event_id": "EVENT_FNB_001",
                "description": "Peter Faucitt writes formal letter to FNB acknowledging suspected fraud on RWD account 62323196362",
                "significance": "Director's written admission of suspected fraud",
                "days_after_exposure": 11,
                "key_admissions": [
                    "Suspected fraud on RWD account",
                    "Prior request to cancel 3 debit cards",
                    "FNB could be accessory after the fact",
                    "Potential Exchange Control violations"
                ]
            }
        ],
        "analysis": {
            "pattern": "fraud_exposure_retaliation_acknowledgment",
            "timeline_significance": "Peter's FNB letter written 11 days after Daniel exposed fraud to Bantjies confirms Peter was aware of suspected fraud, yet his court filings blame Daniel and Jax",
            "contradiction": "Peter's court position claims Daniel and Jax are perpetrators, but his FNB letter shows he was aware of fraud on the RWD account and was taking action to stop it",
            "legal_implications": [
                "Director's admission of suspected fraud strengthens criminal case",
                "Exchange Control acknowledgment adds SARB regulatory dimension",
                "FNB accessory warning standard applies equally to Peter"
            ]
        }
    }
    
    # Save analysis
    analysis_path = DATA_MODELS / "JUNE_2025_TIMELINE_ANALYSIS.json"
    save_json(analysis_path, june_2025_timeline)
    
    return june_2025_timeline

def create_evidence_chain_document():
    """Create evidence chain document linking FNB letter to other evidence."""
    
    evidence_chain = {
        "title": "FNB Fraud Letter Evidence Chain",
        "evidence_id": "PAF_FNB_FRAUD_LETTER_2025_06_17",
        "date": "2025-06-17",
        "author": "Peter Andrew Faucitt",
        "recipient": "Nondu Motlhala (FNB)",
        "account": "62323196362",
        "company": "RegimA Worldwide Distribution (Pty) Ltd",
        "chain_links": [
            {
                "link_type": "precursor_event",
                "event_id": "EVENT_011",
                "date": "2025-06-06",
                "description": "Daniel finalizes fraud reports",
                "days_before": 11
            },
            {
                "link_type": "precursor_event",
                "event_id": "EVENT_057",
                "date": "2025-06-06",
                "description": "Daniel sends reports to Bantjies",
                "days_before": 11
            },
            {
                "link_type": "immediate_response",
                "event_id": "EVENT_012",
                "date": "2025-06-07",
                "description": "Secret card cancellations",
                "days_before": 10
            },
            {
                "link_type": "corroborating_evidence",
                "evidence_id": "SF2",
                "description": "Sage Screenshots showing Rynette's system control",
                "relevance": "Confirms Rynette controlled accounting systems"
            },
            {
                "link_type": "corroborating_evidence",
                "evidence_id": "JF08",
                "description": "Comprehensive fraud evidence package",
                "relevance": "Documents the fraud Peter acknowledges"
            },
            {
                "link_type": "contradicting_document",
                "document": "Peter's Court Affidavit",
                "contradiction": "Claims Daniel and Jax are perpetrators, but FNB letter shows Peter was aware of fraud on RWD account"
            }
        ],
        "legal_weight": {
            "civil_burden_50": "EXCEEDED - Director's own admission",
            "criminal_burden_95": "STRENGTHENED - Written acknowledgment of suspected fraud",
            "exchange_control": "NEW DIMENSION - Potential SARB violations acknowledged"
        },
        "filing_relevance": {
            "CIPC_Complaint": "HIGH - Director's knowledge of fraud",
            "POPIA_Complaint": "MEDIUM - Data processing under fraudulent circumstances",
            "Commercial_Crime": "HIGH - Director's admission of suspected fraud",
            "NPA_Tax_Fraud": "HIGH - Exchange Control violations acknowledged"
        }
    }
    
    # Save evidence chain
    chain_path = DATA_MODELS / "FNB_FRAUD_LETTER_EVIDENCE_CHAIN.json"
    save_json(chain_path, evidence_chain)
    
    return evidence_chain

def update_event_cross_references():
    """Update cross-references between events."""
    
    events_data = load_json(EVENTS_PATH)
    
    # Find and update related events
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        
        # Add FNB letter reference to June 2025 events
        if event_id in ['EVENT_011', 'EVENT_057', 'EVENT_012']:
            if 'related_events' not in event:
                event['related_events'] = []
            if 'EVENT_FNB_001' not in event['related_events']:
                event['related_events'].append('EVENT_FNB_001')
                event['fnb_letter_context'] = "Peter's FNB letter (2025-06-17) written after this event confirms awareness of suspected fraud"
    
    events_data['metadata']['last_updated'] = datetime.now().isoformat()
    events_data['metadata']['changes'] = "Added FNB letter cross-references to June 2025 events"
    
    save_json(EVENTS_PATH, events_data)

def generate_refinement_summary():
    """Generate summary of all refinements."""
    
    summary = {
        "refinement_date": datetime.now().isoformat(),
        "new_evidence": {
            "id": "PAF_FNB_FRAUD_LETTER_2025_06_17",
            "type": "Director's Letter to FNB",
            "date": "2025-06-17",
            "significance": "CRITICAL - Director's written acknowledgment of suspected fraud"
        },
        "models_updated": [
            "events.json - Added EVENT_FNB_001",
            "timeline.json - Added 2025-06-17 entry",
            "entities.json - Updated PERSON_001 with FNB letter evidence",
            "relations.json - Added REL_FNB_001"
        ],
        "new_analysis_files": [
            "JUNE_2025_TIMELINE_ANALYSIS.json",
            "FNB_FRAUD_LETTER_EVIDENCE_CHAIN.json"
        ],
        "key_findings": [
            "Peter Faucitt acknowledged suspected fraud on RWD account in writing",
            "Letter written 11 days after Daniel exposed fraud to Bantjies",
            "Peter warned FNB about being 'accessory after the fact'",
            "Peter acknowledged potential Exchange Control violations",
            "This contradicts Peter's court position blaming Daniel and Jax"
        ],
        "legal_implications": {
            "civil_case": "Burden of proof strengthened by director's admission",
            "criminal_case": "Written acknowledgment supports fraud charges",
            "regulatory": "Exchange Control violations add SARB dimension",
            "CIPC": "Director misconduct evidence strengthened"
        },
        "burden_of_proof_assessment": {
            "civil_50_percent": "EXCEEDED",
            "criminal_95_percent": "STRENGTHENED",
            "exchange_control": "NEW EVIDENCE"
        }
    }
    
    # Save summary
    summary_path = DATA_MODELS / "REFINEMENT_SUMMARY_2026_01_29.json"
    save_json(summary_path, summary)
    
    # Also save as markdown
    md_content = f"""# Model Refinement Summary - 2026-01-29

## New Evidence Integrated

**Evidence ID:** PAF_FNB_FRAUD_LETTER_2025_06_17

**Type:** Director's Letter to FNB

**Date:** 17 June 2025

**Significance:** CRITICAL - Director's written acknowledgment of suspected fraud

## Models Updated

1. **events.json** - Added EVENT_FNB_001
2. **timeline.json** - Added 2025-06-17 entry
3. **entities.json** - Updated PERSON_001 with FNB letter evidence
4. **relations.json** - Added REL_FNB_001

## Key Findings

1. Peter Faucitt acknowledged suspected fraud on RWD account in writing
2. Letter written 11 days after Daniel exposed fraud to Bantjies (2025-06-06)
3. Peter warned FNB about being "accessory after the fact"
4. Peter acknowledged potential Exchange Control violations
5. This contradicts Peter's court position blaming Daniel and Jax

## Timeline Context

| Date | Event | Days After Exposure |
|------|-------|---------------------|
| 2025-06-06 | Daniel exposes fraud to Bantjies | T-0 |
| 2025-06-07 | Secret card cancellations | T+1 |
| **2025-06-17** | **Peter writes FNB letter** | **T+11** |

## Legal Implications

### Civil Case
- Burden of proof strengthened by director's admission

### Criminal Case
- Written acknowledgment supports fraud charges

### Regulatory
- Exchange Control violations add SARB dimension

### CIPC
- Director misconduct evidence strengthened

## Burden of Proof Assessment

| Standard | Status |
|----------|--------|
| Civil (50%) | ✅ EXCEEDED |
| Criminal (95%) | ✅ STRENGTHENED |
| Exchange Control | 🆕 NEW EVIDENCE |

---

*Refinement completed: {datetime.now().isoformat()}*
"""
    
    md_path = REVSTREAM_DOCS / "REFINEMENT_SUMMARY_2026_01_29.md"
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"Saved: {md_path}")
    
    return summary

def main():
    """Main refinement function."""
    print("=" * 60)
    print("Comprehensive Model Refinement - FNB Fraud Letter Integration")
    print("=" * 60)
    
    print("\n1. Analyzing June 2025 Timeline...")
    analyze_june_2025_timeline()
    
    print("\n2. Creating Evidence Chain Document...")
    create_evidence_chain_document()
    
    print("\n3. Updating Event Cross-References...")
    update_event_cross_references()
    
    print("\n4. Generating Refinement Summary...")
    generate_refinement_summary()
    
    print("\n" + "=" * 60)
    print("Model Refinement Complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
