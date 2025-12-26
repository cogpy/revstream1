import json
from datetime import datetime

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def parse_amount(amount_str):
    """Parse various amount formats to numeric value"""
    if not amount_str or amount_str == "unknown_amount":
        return None
    
    # Remove currency symbol, commas, and + signs
    cleaned = amount_str.replace('R', '').replace(',', '').replace('+', '').strip()
    
    # Handle M/K abbreviations
    if 'M' in cleaned:
        return float(cleaned.replace('M', '')) * 1000000
    elif 'K' in cleaned:
        return float(cleaned.replace('K', '')) * 1000
    
    try:
        return float(cleaned)
    except:
        return None

def create_financial_impact(event):
    """Convert old financial_impact string to new structured format"""
    old_impact = event.get('financial_impact', 'unknown_amount')
    event_id = event['event_id']
    
    # Parse amount
    value = parse_amount(old_impact)
    
    # Determine precision
    if old_impact == "unknown_amount":
        precision = "unknown"
        formatted = "No direct financial impact"
    elif '+' in old_impact:
        precision = "minimum" if value and value > 1000000 else "estimated"
        formatted = old_impact
    elif value and '.' in old_impact:
        precision = "exact"
        formatted = f"R{value:,.2f}"
    elif value:
        precision = "rounded"
        formatted = f"R{int(value):,}.00"
    else:
        precision = "unknown"
        formatted = "Amount not quantified"
    
    # Determine evidence strength based on event category and existing evidence
    evidence = event.get('evidence', [])
    if 'trial_balance' in str(evidence).lower() or 'financial' in str(evidence).lower():
        evidence_strength = "documented"
    elif value and value < 1000:
        evidence_strength = "documented"
    elif '+' in old_impact or 'estimate' in event.get('description', '').lower():
        evidence_strength = "estimated"
    elif value is None:
        evidence_strength = "unknown"
    else:
        evidence_strength = "documented"
    
    # Map event categories to transaction types and impact categories
    category = event.get('category', 'other')
    event_type = event.get('event_type', 'other')
    
    # Transaction type mapping
    transaction_type_map = {
        'revenue_theft': 'theft',
        'payment_redirection': 'theft',
        'unauthorized_transfer': 'misappropriation',
        'fund_diversion': 'misappropriation',
        'accounting_fraud': 'fraud',
        'false_invoice': 'fraud',
        'cost_manipulation': 'cost_manipulation',
        'inter_company_loan': 'loan',
        'interest_payment': 'interest_payment',
        'capital_extraction': 'capital_extraction',
        'profit_extraction': 'capital_extraction',
        'stock_adjustment': 'stock_adjustment',
        'domain_hijacking': 'revenue_diversion',
        'business_relationship': 'service_fee',
        'relationship_establishment': 'service_fee',
        'service_expansion': 'service_fee'
    }
    
    transaction_type = transaction_type_map.get(event_type, 'other')
    
    # Impact category mapping
    impact_category_map = {
        'revenue_theft': 'revenue_theft',
        'financial_manipulation': 'financial_manipulation',
        'trust_violation': 'trust_violation',
        'transfer_pricing_fraud': 'transfer_pricing_fraud',
        'accounting_fraud': 'accounting_fraud',
        'evidence_destruction': 'evidence_destruction',
        'business_relationship': 'business_relationship',
        'inter_company_loan': 'infrastructure',
        'profit_extraction': 'profit_extraction',
        'cost_manipulation': 'financial_manipulation'
    }
    
    impact_category = impact_category_map.get(category, 'financial_manipulation')
    
    # Generate court presentation
    title = event.get('title', 'Financial transaction')
    if value and value > 0:
        court_presentation = f"{formatted} - {title}"
    else:
        court_presentation = f"{title} - financial impact not quantified"
    
    # Build structured financial impact
    financial_impact = {
        "total_amount": {
            "value": value,
            "currency": "ZAR",
            "formatted": formatted,
            "precision": precision
        },
        "evidence_strength": evidence_strength,
        "transaction_type": transaction_type,
        "impact_category": impact_category,
        "breakdown": [],
        "aggregation_notes": "Converted from legacy format",
        "court_presentation": court_presentation
    }
    
    return financial_impact

# Load events
print("=== FINANCIAL SCHEMA CONVERSION ===\n")
events_data = load_json('/home/ubuntu/revstream1/data_models/events/events_refined.json')

converted_count = 0
total_documented = 0
total_estimated = 0
unknown_count = 0

for event in events_data['events']:
    old_impact = event.get('financial_impact', 'unknown_amount')
    new_impact = create_financial_impact(event)
    
    # Replace old format with new
    event['financial_impact'] = new_impact
    
    # Track statistics
    converted_count += 1
    if new_impact['total_amount']['value']:
        if new_impact['evidence_strength'] == 'documented':
            total_documented += new_impact['total_amount']['value']
        elif new_impact['evidence_strength'] == 'estimated':
            total_estimated += new_impact['total_amount']['value']
    else:
        unknown_count += 1
    
    print(f"✅ {event['event_id']}: {old_impact} → {new_impact['total_amount']['formatted']}")

# Update metadata
events_data['metadata']['version'] = "6.0"
events_data['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
events_data['metadata']['changes'] = "Converted all financial_impact fields to structured schema v1.0"

# Save updated events
save_json('/home/ubuntu/revstream1/data_models/events/events_refined.json', events_data)

print(f"\n=== CONVERSION COMPLETE ===")
print(f"Events converted: {converted_count}")
print(f"Total documented: R{total_documented:,.2f}")
print(f"Total estimated: R{total_estimated:,.2f}")
print(f"Unknown amounts: {unknown_count}")
print(f"Events model updated to v6.0")
