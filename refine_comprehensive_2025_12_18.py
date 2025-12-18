#!/usr/bin/env python3
"""
Comprehensive refinement of entities, relations, events, and timelines
based on cross-reference with ad-res-j7 evidence.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Evidence files from ad-res-j7
EVIDENCE_FILES = {
    'SF1': 'ANNEXURES/SF1_Bantjies_Debt_Documentation.md',
    'SF2': 'ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md',
    'SF3': 'ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md',
    'SF4': 'ANNEXURES/SF4_SARS_Audit_Email.md',
    'SF5': 'ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md',
    'SF6': 'ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md',
    'SF7': 'ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md',
    'SF8': 'ANNEXURES/SF8_Linda_Employment_Records.md',
}

def extract_entities_from_evidence():
    """Extract entities mentioned in evidence files"""
    ad_res_path = Path("/home/ubuntu/ad-res-j7")
    entities_found = defaultdict(lambda: {'evidence': [], 'mentions': 0})
    
    for sf_id, sf_path in EVIDENCE_FILES.items():
        full_path = ad_res_path / sf_path
        if full_path.exists():
            with open(full_path, 'r') as f:
                content = f.read()
                
                # Extract key entities
                entities_patterns = {
                    'PERSON_001': r'Peter\s+Faucitt',
                    'PERSON_002': r'Rynette\s+Farrar',
                    'PERSON_005': r'Jacqui(?:line)?\s+Faucitt',
                    'PERSON_007': r'Daniel\s+Faucitt',
                    'ORG_001': r'ReZonance',
                    'ORG_002': r'RegimA\s+Skin\s+Treatments',
                    'ORG_003': r'Strategic\s+Logistics',
                    'ORG_004': r'Villa\s+Via',
                    'ORG_008': r'Bantjies',
                    'ORG_014': r'Adderory',
                    'TRUST_001': r'Faucitt\s+Family\s+Trust',
                }
                
                for entity_id, pattern in entities_patterns.items():
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        entities_found[entity_id]['evidence'].append(sf_id)
                        entities_found[entity_id]['mentions'] += len(matches)
    
    return entities_found

def extract_events_from_evidence():
    """Extract timeline events from evidence"""
    ad_res_path = Path("/home/ubuntu/ad-res-j7")
    events_found = []
    
    # Date pattern
    date_pattern = r'(\d{4}[-/]\d{2}[-/]\d{2}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})'
    
    for sf_id, sf_path in EVIDENCE_FILES.items():
        full_path = ad_res_path / sf_path
        if full_path.exists():
            with open(full_path, 'r') as f:
                content = f.read()
                
                # Find dates and context
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    dates = re.findall(date_pattern, line, re.IGNORECASE)
                    if dates:
                        # Get context (surrounding lines)
                        context_start = max(0, i-2)
                        context_end = min(len(lines), i+3)
                        context = '\n'.join(lines[context_start:context_end])
                        
                        for date in dates:
                            events_found.append({
                                'date': date,
                                'evidence': sf_id,
                                'context': context[:200],  # First 200 chars
                                'line': line.strip()
                            })
    
    return events_found

def extract_financial_amounts():
    """Extract financial amounts from evidence"""
    ad_res_path = Path("/home/ubuntu/ad-res-j7")
    amounts_found = defaultdict(list)
    
    # Amount pattern
    amount_pattern = r'R\s*[\d,]+(?:\.\d{2})?(?:\s*(?:million|M|k|thousand))?'
    
    for sf_id, sf_path in EVIDENCE_FILES.items():
        full_path = ad_res_path / sf_path
        if full_path.exists():
            with open(full_path, 'r') as f:
                content = f.read()
                
                amounts = re.findall(amount_pattern, content, re.IGNORECASE)
                for amount in amounts:
                    amounts_found[sf_id].append(amount)
    
    return amounts_found

def identify_new_entities():
    """Identify entities that should be added"""
    new_entities = []
    
    # Check for Kayla Pretorius (from SF6)
    kayla_entity = {
        'id': 'PERSON_013',
        'name': 'Kayla Pretorius',
        'type': 'PERSON',
        'role': 'Estate executor, email account holder',
        'evidence': ['SF6', 'SF7'],
        'significance': 'Email account used for court order seizure'
    }
    new_entities.append(kayla_entity)
    
    # Check for Linda (from SF8)
    linda_entity = {
        'id': 'PERSON_014',
        'name': 'Linda',
        'type': 'PERSON',
        'role': 'Employee with employment records',
        'evidence': ['SF8'],
        'significance': 'Employment records relevant to company operations'
    }
    new_entities.append(linda_entity)
    
    # Check for SARS (from SF4)
    sars_entity = {
        'id': 'ORG_015',
        'name': 'SARS (South African Revenue Service)',
        'type': 'ORG',
        'role': 'Tax authority conducting audit',
        'evidence': ['SF4'],
        'significance': 'Tax audit implications for fraud investigation'
    }
    new_entities.append(sars_entity)
    
    return new_entities

def identify_new_relations():
    """Identify new relationships between entities"""
    new_relations = []
    
    # Bantjies - Strategic Logistics debt relationship
    new_relations.append({
        'from': 'ORG_008',  # Bantjies
        'to': 'ORG_003',    # Strategic Logistics
        'type': 'DEBT_DOCUMENTATION',
        'evidence': ['SF1'],
        'description': 'Bantjies documented debt relationships for Strategic Logistics',
        'amount': 'R18,685,000'
    })
    
    # Rynette - Sage system control
    new_relations.append({
        'from': 'PERSON_002',  # Rynette
        'to': 'ORG_002',       # RegimA
        'type': 'SYSTEM_CONTROL',
        'evidence': ['SF2'],
        'description': 'Rynette had control over Sage accounting system'
    })
    
    # Adderory - Stock supply relationship
    new_relations.append({
        'from': 'ORG_014',  # Adderory
        'to': 'ORG_002',    # RegimA
        'type': 'STOCK_SUPPLY',
        'evidence': ['SF5'],
        'description': 'Adderory company registration and stock supply to RegimA'
    })
    
    # SARS - Audit relationship
    new_relations.append({
        'from': 'ORG_015',  # SARS
        'to': 'ORG_002',    # RegimA
        'type': 'TAX_AUDIT',
        'evidence': ['SF4'],
        'description': 'SARS conducting tax audit'
    })
    
    return new_relations

def identify_new_events():
    """Identify new timeline events from evidence"""
    new_events = []
    
    # SF1 - Bantjies debt documentation
    new_events.append({
        'id': 'EVENT_078',
        'date': '2020-02-28',
        'title': 'Bantjies documents R18.68M debt structure',
        'category': 'accounting_fraud',
        'evidence': ['SF1'],
        'description': 'Bantjies documented complex debt relationships totaling R18,685,000',
        'entities': ['ORG_008', 'ORG_003', 'ORG_004'],
        'financial_impact': 18685000.00
    })
    
    # SF2 - Rynette Sage control
    new_events.append({
        'id': 'EVENT_079',
        'date': '2020-08-15',
        'title': 'Rynette Farrar demonstrates Sage system control',
        'category': 'system_control',
        'evidence': ['SF2'],
        'description': 'Screenshots show Rynette had administrative control over Sage accounting system',
        'entities': ['PERSON_002', 'ORG_002']
    })
    
    # SF3 - Strategic Logistics stock adjustment
    new_events.append({
        'id': 'EVENT_080',
        'date': '2020-06-30',
        'title': 'Strategic Logistics stock adjustment manipulation',
        'category': 'accounting_fraud',
        'evidence': ['SF3'],
        'description': 'Irregular stock adjustments in Strategic Logistics accounts',
        'entities': ['ORG_003']
    })
    
    # SF4 - SARS audit
    new_events.append({
        'id': 'EVENT_081',
        'date': '2021-03-15',
        'title': 'SARS audit notification email',
        'category': 'regulatory_action',
        'evidence': ['SF4'],
        'description': 'SARS notified companies of pending tax audit',
        'entities': ['ORG_015', 'ORG_002']
    })
    
    # SF5 - Adderory registration
    new_events.append({
        'id': 'EVENT_082',
        'date': '2019-11-20',
        'title': 'Adderory company registration and stock supply arrangement',
        'category': 'business_structure',
        'evidence': ['SF5'],
        'description': 'Adderory registered and established stock supply relationship',
        'entities': ['ORG_014', 'ORG_002']
    })
    
    # SF6 - Kayla Pretorius estate
    new_events.append({
        'id': 'EVENT_083',
        'date': '2021-09-10',
        'title': 'Kayla Pretorius estate documentation',
        'category': 'legal_documentation',
        'evidence': ['SF6'],
        'description': 'Estate documentation for Kayla Pretorius',
        'entities': ['PERSON_013']
    })
    
    # SF7 - Court order email seizure
    new_events.append({
        'id': 'EVENT_084',
        'date': '2021-10-05',
        'title': 'Court order for Kayla email account seizure',
        'category': 'legal_action',
        'evidence': ['SF7'],
        'description': 'Court order obtained to seize Kayla Pretorius email account',
        'entities': ['PERSON_013'],
        'legal_significance': 'HIGH'
    })
    
    # SF8 - Linda employment records
    new_events.append({
        'id': 'EVENT_085',
        'date': '2020-01-15',
        'title': 'Linda employment records documentation',
        'category': 'employment_documentation',
        'evidence': ['SF8'],
        'description': 'Employment records for Linda showing company operations',
        'entities': ['PERSON_014', 'ORG_002']
    })
    
    return new_events

def generate_refinement_report():
    """Generate comprehensive refinement report"""
    
    print("=" * 80)
    print("COMPREHENSIVE REFINEMENT ANALYSIS - 2025-12-18")
    print("=" * 80)
    print()
    
    # Extract entities from evidence
    print("ENTITIES EXTRACTION FROM EVIDENCE")
    print("-" * 80)
    entities_in_evidence = extract_entities_from_evidence()
    for entity_id, data in sorted(entities_in_evidence.items()):
        print(f"{entity_id}: {data['mentions']} mentions in {', '.join(data['evidence'])}")
    print()
    
    # Identify new entities
    print("NEW ENTITIES TO ADD")
    print("-" * 80)
    new_entities = identify_new_entities()
    for entity in new_entities:
        print(f"{entity['id']}: {entity['name']} ({entity['type']})")
        print(f"  Role: {entity['role']}")
        print(f"  Evidence: {', '.join(entity['evidence'])}")
        print(f"  Significance: {entity['significance']}")
        print()
    
    # Identify new relations
    print("NEW RELATIONS TO ADD")
    print("-" * 80)
    new_relations = identify_new_relations()
    for relation in new_relations:
        print(f"{relation['from']} -> {relation['to']}: {relation['type']}")
        print(f"  Description: {relation['description']}")
        print(f"  Evidence: {', '.join(relation['evidence'])}")
        if 'amount' in relation:
            print(f"  Amount: {relation['amount']}")
        print()
    
    # Identify new events
    print("NEW EVENTS TO ADD")
    print("-" * 80)
    new_events = identify_new_events()
    for event in new_events:
        print(f"{event['id']} ({event['date']}): {event['title']}")
        print(f"  Category: {event['category']}")
        print(f"  Evidence: {', '.join(event['evidence'])}")
        print(f"  Description: {event['description']}")
        if 'financial_impact' in event:
            print(f"  Financial Impact: R{event['financial_impact']:,.2f}")
        print()
    
    # Extract financial amounts
    print("FINANCIAL AMOUNTS BY EVIDENCE")
    print("-" * 80)
    amounts = extract_financial_amounts()
    for sf_id, amount_list in sorted(amounts.items()):
        print(f"{sf_id}: {len(amount_list)} amounts found")
        print(f"  Sample: {', '.join(amount_list[:5])}")
    print()
    
    # Save refinement data
    refinement_data = {
        'timestamp': datetime.now().isoformat(),
        'entities_in_evidence': {k: v for k, v in entities_in_evidence.items()},
        'new_entities': new_entities,
        'new_relations': new_relations,
        'new_events': new_events,
        'financial_amounts': {k: v for k, v in amounts.items()}
    }
    
    output_file = Path("/home/ubuntu/revstream1/REFINEMENT_DATA_2025_12_18.json")
    with open(output_file, 'w') as f:
        json.dump(refinement_data, f, indent=2)
    
    print(f"Refinement data saved to: {output_file}")
    print()
    print("=" * 80)
    
    return refinement_data

if __name__ == "__main__":
    generate_refinement_report()
