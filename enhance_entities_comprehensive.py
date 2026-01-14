#!/usr/bin/env python3
"""
Comprehensive entity enhancement with ad-res-j7 evidence references
"""
import json
import os
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def scan_ad_res_j7_evidence(ad_res_j7_path):
    """Scan ad-res-j7 repository for evidence files"""
    evidence_map = {}
    
    # Key evidence directories
    annexures_path = Path(ad_res_j7_path) / "ANNEXURES"
    civil_path = Path(ad_res_j7_path) / "1-CIVIL-RESPONSE"
    criminal_path = Path(ad_res_j7_path) / "2-CRIMINAL-CASE"
    
    # Scan ANNEXURES
    if annexures_path.exists():
        for annexure_dir in annexures_path.iterdir():
            if annexure_dir.is_dir():
                annexure_name = annexure_dir.name
                evidence_map[annexure_name] = {
                    'path': str(annexure_dir.relative_to(ad_res_j7_path)),
                    'files': []
                }
                
                # Scan for key files
                for ext in ['*.md', '*.pdf', '*.txt', '*.json']:
                    for file in annexure_dir.rglob(ext):
                        evidence_map[annexure_name]['files'].append(
                            str(file.relative_to(ad_res_j7_path))
                        )
    
    return evidence_map

def enhance_entities_with_evidence(entities_file, ad_res_j7_path, output_file):
    """Enhance entities with comprehensive evidence references"""
    
    # Load entities
    entities_data = load_json(entities_file)
    
    # Scan ad-res-j7 evidence
    evidence_map = scan_ad_res_j7_evidence(ad_res_j7_path)
    
    # Entity-specific evidence mapping
    entity_evidence_mapping = {
        'PERSON_001': {  # Peter Andrew Faucitt
            'annexures': ['JF01', 'JF04', 'JF06', 'JF08'],
            'key_evidence': [
                'ANNEXURES/JF01 - Shopify Plus email evidence',
                'ANNEXURES/JF04 - CIPC company records',
                'ANNEXURES/JF08/evidence_package_20251012',
                '1-CIVIL-RESPONSE/ANSWERING_AFFIDAVIT_JACQUI.md',
                'SF9_Ian_Levitt_Demand_Letter.md'
            ],
            'evidence_strength': 'conclusive',
            'criminal_threshold': '95%_exceeded'
        },
        'PERSON_002': {  # Rynette Farrar
            'annexures': ['JF05', 'JF07', 'JF08'],
            'key_evidence': [
                'ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md',
                'ANNEXURES/JF07 - Sage system screenshots',
                'ANNEXURES/JF08/evidence_package_20251012',
                'SF9_Ian_Levitt_Demand_Letter.md'
            ],
            'evidence_strength': 'conclusive',
            'criminal_threshold': '95%_likely'
        },
        'PERSON_004': {  # Jacqueline Faucitt
            'annexures': ['JF01', 'JF02', 'JF05', 'JF06', 'JF08'],
            'key_evidence': [
                '1-CIVIL-RESPONSE/ANSWERING_AFFIDAVIT_JACQUI.md',
                'ANNEXURES/JF01 - Shopify platform operator evidence',
                'ANNEXURES/JF06 - Court documents'
            ],
            'evidence_strength': 'strong'
        },
        'PERSON_005': {  # Daniel James Faucitt
            'annexures': ['JF01', 'JF02', 'JF06'],
            'key_evidence': [
                'ANNEXURES/JF01 - Shopify Plus email',
                'ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md',
                'ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md'
            ],
            'evidence_strength': 'strong'
        },
        'PERSON_007': {  # Danie Bantjies
            'annexures': ['JF03', 'JF08'],
            'key_evidence': [
                'ANNEXURES/SF1_Bantjies_Debt_Documentation.md',
                'ANNEXURES/JF03 - Financial records',
                'ANNEXURES/JF08/evidence_package_20251012'
            ],
            'evidence_strength': 'strong',
            'criminal_threshold': '95%_likely'
        },
        'ORG_001': {  # RWD ZA
            'annexures': ['JF04', 'JF08'],
            'key_evidence': [
                'ANNEXURES/JF04 - CIPC registration documents',
                'ANNEXURES/JF08/evidence_package_20251012'
            ],
            'evidence_strength': 'conclusive'
        },
        'ORG_008': {  # ReZonance
            'annexures': ['JF03', 'JF08'],
            'key_evidence': [
                'ANNEXURES/JF03 - Financial transaction records',
                'ANNEXURES/JF08/evidence_package_20251012'
            ],
            'evidence_strength': 'strong'
        }
    }
    
    # Track enhancements
    enhanced_count = 0
    
    # Enhance persons
    if 'persons' in entities_data.get('entities', {}):
        for person in entities_data['entities']['persons']:
            entity_id = person.get('entity_id')
            if entity_id in entity_evidence_mapping:
                mapping = entity_evidence_mapping[entity_id]
                
                # Add evidence references if not already present
                if 'ad_res_j7_evidence_enhanced' not in person:
                    person['ad_res_j7_evidence_enhanced'] = mapping['key_evidence']
                    person['evidence_strength'] = mapping['evidence_strength']
                    if 'criminal_threshold' in mapping:
                        person['criminal_threshold'] = mapping['criminal_threshold']
                    person['evidence_enhanced_timestamp'] = datetime.now().isoformat()
                    enhanced_count += 1
    
    # Enhance organizations
    if 'organizations' in entities_data.get('entities', {}):
        for org in entities_data['entities']['organizations']:
            entity_id = org.get('entity_id')
            if entity_id in entity_evidence_mapping:
                mapping = entity_evidence_mapping[entity_id]
                
                if 'ad_res_j7_evidence_enhanced' not in org:
                    org['ad_res_j7_evidence_enhanced'] = mapping['key_evidence']
                    org['evidence_strength'] = mapping['evidence_strength']
                    if 'criminal_threshold' in mapping:
                        org['criminal_threshold'] = mapping['criminal_threshold']
                    org['evidence_enhanced_timestamp'] = datetime.now().isoformat()
                    enhanced_count += 1
    
    # Update metadata
    entities_data['metadata']['last_updated'] = datetime.now().isoformat()
    entities_data['metadata']['changes'] = f'Enhanced {enhanced_count} entities with comprehensive ad-res-j7 evidence'
    
    # Save enhanced entities
    save_json(output_file, entities_data)
    
    return enhanced_count, evidence_map

if __name__ == '__main__':
    entities_file = '/home/ubuntu/revstream1/data_models/entities/entities.json'
    ad_res_j7_path = '/home/ubuntu/ad-res-j7'
    output_file = '/home/ubuntu/revstream1/data_models/entities/entities.json'
    
    enhanced_count, evidence_map = enhance_entities_with_evidence(
        entities_file, ad_res_j7_path, output_file
    )
    
    print(f"Enhanced {enhanced_count} entities")
    print(f"Scanned {len(evidence_map)} annexure directories")
    
    # Save evidence map for reference
    with open('/home/ubuntu/revstream1/AD_RES_J7_EVIDENCE_MAP.json', 'w') as f:
        json.dump(evidence_map, f, indent=2)
    print("Evidence map saved to AD_RES_J7_EVIDENCE_MAP.json")
