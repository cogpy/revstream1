#!/usr/bin/env python3
"""
Enhance entities with additional evidence from ad-res-j7 repository
"""

import json
from datetime import datetime
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def enhance_entities():
    """Enhance entities with additional evidence references"""
    entities_path = Path('/home/ubuntu/revstream1/data_models/entities/entities.json')
    entities = load_json(entities_path)
    
    # Enhancement mappings based on ad-res-j7 evidence
    enhancements = {
        'PERSON_006': {  # Linda
            'evidence_strength': 'strong',
            'ad_res_j7_references': [
                'ANNEXURES/SF8_Linda_Employment_Records.md - Employment documentation',
                'ANNEXURES/JF08/evidence_package_20251012 - Comprehensive fraud timeline',
                '1-CIVIL-RESPONSE/RESCISSION_AFFIDAVIT_JACQUELINE_FAUCITT.md - Witness testimony'
            ]
        },
        'PERSON_009': {  # Gee
            'evidence_strength': 'strong',
            'ad_res_j7_references': [
                'ANNEXURES/JF08/evidence_package_20251012 - Business relationship documentation',
                'ANNEXURES/JF03 - Financial records showing interactions',
                '1-CIVIL-RESPONSE - Civil case documentation'
            ]
        },
        'PERSON_010': {  # Bernadine Wright
            'evidence_strength': 'strong',
            'ad_res_j7_references': [
                'ANNEXURES/JF08/evidence_package_20251012 - Professional relationship evidence',
                'ANNEXURES/JF06 - Court documents and filings',
                '1-CIVIL-RESPONSE - Civil case documentation'
            ]
        },
        'PERSON_011': {  # Chantal
            'evidence_strength': 'strong',
            'ad_res_j7_references': [
                'ANNEXURES/JF08/evidence_package_20251012 - Business operations evidence',
                'ANNEXURES/JF03 - Financial records',
                '1-CIVIL-RESPONSE - Civil case documentation'
            ]
        },
        'PERSON_012': {  # Jax / Marisca Meyer
            'evidence_strength': 'strong',
            'ad_res_j7_references': [
                'ANNEXURES/JF08/evidence_package_20251012 - Comprehensive fraud timeline',
                'ANNEXURES/JF06 - Court documents and filings',
                '1-CIVIL-RESPONSE/RESCISSION_AFFIDAVIT_JACQUELINE_FAUCITT.md - Witness testimony'
            ]
        },
        'PERSON_013': {  # Kayla Pretorius
            'evidence_strength': 'conclusive',
            'ad_res_j7_references': [
                'ANNEXURES/JF01 - Shopify Plus email (26 July 2017) - CRITICAL EVIDENCE',
                'ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md - Estate documentation',
                'ANNEXURES/SF7_Court_Order_Kayla_Email_Seizure.md - Court order evidence',
                'ANNEXURES/JF08/evidence_package_20251012 - Comprehensive fraud timeline',
                '1-CIVIL-RESPONSE - Civil case documentation'
            ]
        }
    }
    
    # Apply enhancements
    updated_count = 0
    for person in entities.get('entities', {}).get('persons', []):
        entity_id = person.get('entity_id')
        if entity_id in enhancements:
            enhancement = enhancements[entity_id]
            person['evidence_strength'] = enhancement['evidence_strength']
            person['ad_res_j7_references'] = enhancement['ad_res_j7_references']
            person['evidence_enhanced'] = datetime.now().isoformat()
            updated_count += 1
            print(f"Enhanced {entity_id}: {person.get('name')} -> {enhancement['evidence_strength']}")
    
    # Update metadata
    entities['metadata']['last_updated'] = datetime.now().isoformat()
    entities['metadata']['version'] = '24.0_ENHANCED_2026_01_09'
    entities['metadata']['changes'] = 'Enhanced evidence strength and ad-res-j7 references for 7 entities'
    
    # Save enhanced entities
    save_json(entities_path, entities)
    
    print(f"\nTotal entities enhanced: {updated_count}")
    print(f"Saved to: {entities_path}")

if __name__ == '__main__':
    enhance_entities()
