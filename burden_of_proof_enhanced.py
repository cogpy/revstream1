#!/usr/bin/env python3
"""
Enhanced Burden of Proof Analysis for Case 2025-137857
Maps events to legal standards for different filing types
"""

import json
from datetime import datetime
from collections import defaultdict

REVSTREAM_PATH = "/home/ubuntu/revstream1"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load updated events
events = load_json(f"{REVSTREAM_PATH}/data_models/events/events_refined_2025_12_04_v26.json")

print("=" * 80)
print("ENHANCED BURDEN OF PROOF ANALYSIS - CASE 2025-137857")
print("=" * 80)
print()

# Define legal standards
LEGAL_STANDARDS = {
    "civil_actions": {
        "name": "Civil Actions",
        "standard": "50% - Balance of Probabilities",
        "threshold": 0.50,
        "description": "More likely than not that the claim is true"
    },
    "criminal_actions": {
        "name": "Criminal Actions",
        "standard": "95%+ - Beyond Reasonable Doubt",
        "threshold": 0.95,
        "description": "No reasonable doubt in the mind of a reasonable person"
    },
    "cipc_complaints": {
        "name": "CIPC Companies Act Complaints",
        "standard": "Reasonable Grounds to Believe",
        "threshold": 0.65,
        "description": "Credible evidence suggesting a violation occurred"
    },
    "popia_complaints": {
        "name": "POPIA Criminal Complaints",
        "standard": "95%+ - Beyond Reasonable Doubt",
        "threshold": 0.95,
        "description": "Criminal standard for data protection violations"
    },
    "commercial_crime": {
        "name": "Commercial Crime Case Submissions",
        "standard": "95%+ - Beyond Reasonable Doubt",
        "threshold": 0.95,
        "description": "Criminal standard for commercial fraud"
    },
    "npa_tax_fraud": {
        "name": "NPA Tax Fraud Reports",
        "standard": "95%+ - Beyond Reasonable Doubt",
        "threshold": 0.95,
        "description": "Criminal standard for tax-related offenses"
    }
}

# Categorize events by legal filing type
def categorize_event_for_filing(event):
    """Determine which filing types an event is suitable for"""
    category = event.get('category', '')
    event_type = event.get('event_type', '')
    legal_sig = event.get('legal_significance', '')
    
    filings = []
    
    # All events with financial impact qualify for civil actions
    if event.get('financial_impact'):
        filings.append('civil_actions')
    
    # Criminal actions - fraud, theft, identity crimes
    criminal_categories = [
        'financial_fraud', 'revenue_theft', 'fraud', 'identity_fraud',
        'evidence_tampering', 'perjury', 'accounting_fraud', 'estate_fraud',
        'transfer_pricing_fraud', 'customer_hijacking', 'infrastructure_seizure'
    ]
    if category in criminal_categories:
        filings.append('criminal_actions')
        filings.append('commercial_crime')
    
    # CIPC complaints - company law violations
    cipc_categories = [
        'trust_violations', 'financial_manipulation', 'accounting_fraud',
        'director_misconduct', 'shareholder_oppression'
    ]
    if category in cipc_categories or 'director' in str(event.get('perpetrators', [])):
        filings.append('cipc_complaints')
    
    # POPIA complaints - data protection violations
    if 'popi' in str(event).lower() or 'data' in str(event).lower() or 'privacy' in str(event).lower():
        filings.append('popia_complaints')
    
    # Tax fraud - financial manipulation affecting tax
    if category in ['transfer_pricing_fraud', 'accounting_fraud', 'financial_manipulation']:
        if event.get('financial_impact') and 'R' in str(event.get('financial_impact')):
            filings.append('npa_tax_fraud')
    
    return filings

# Analyze all events
filing_categories = defaultdict(list)
for event in events.get('events', []):
    event_id = event.get('event_id')
    filings = categorize_event_for_filing(event)
    
    for filing in filings:
        filing_categories[filing].append({
            'event_id': event_id,
            'title': event.get('title', 'Unknown'),
            'date': event.get('date', 'Unknown'),
            'category': event.get('category', 'Unknown'),
            'financial_impact': event.get('financial_impact', 'N/A'),
            'evidence_files': len(event.get('evidence_files', [])),
            'legal_significance': event.get('legal_significance', 'N/A')
        })

# Generate report
print("FILING TYPE ANALYSIS")
print("-" * 80)
for filing_type, standard_info in LEGAL_STANDARDS.items():
    events_list = filing_categories.get(filing_type, [])
    print(f"\n{standard_info['name']}")
    print(f"Standard: {standard_info['standard']}")
    print(f"Description: {standard_info['description']}")
    print(f"Events Meeting Standard: {len(events_list)}")
    print(f"Status: {'✓ Strong' if len(events_list) > 30 else '✓ Sufficient' if len(events_list) > 5 else '⚠ Limited'}")

print("\n" + "=" * 80)
print("DETAILED BREAKDOWN BY FILING TYPE")
print("=" * 80)

# Generate detailed report
detailed_report = {
    "analysis_date": datetime.now().isoformat(),
    "case_number": "2025-137857",
    "legal_standards": LEGAL_STANDARDS,
    "filing_categories": {}
}

for filing_type, events_list in filing_categories.items():
    print(f"\n{LEGAL_STANDARDS[filing_type]['name']}: {len(events_list)} events")
    print("-" * 80)
    
    # Show sample events
    for event in events_list[:5]:
        print(f"  • {event['event_id']}: {event['title']} ({event['date']})")
        print(f"    Financial Impact: {event['financial_impact']}")
        print(f"    Evidence Files: {event['evidence_files']}")
    
    if len(events_list) > 5:
        print(f"  ... and {len(events_list) - 5} more events")
    
    detailed_report['filing_categories'][filing_type] = {
        "standard": LEGAL_STANDARDS[filing_type]['standard'],
        "events_count": len(events_list),
        "events": events_list
    }

# Save report
output_path = f"{REVSTREAM_PATH}/BURDEN_OF_PROOF_ENHANCED_2025_12_04.json"
save_json(detailed_report, output_path)
print(f"\n✓ Enhanced burden of proof analysis saved: {output_path}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
