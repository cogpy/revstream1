#!/usr/bin/env python3.11
"""
Entity Enhancement Script
Adds missing criminal thresholds, evidence strength, and cross-references
"""

import json
from datetime import datetime
from pathlib import Path

def load_entities():
    """Load entities data"""
    path = Path('/home/ubuntu/revstream1/data_models/entities/entities.json')
    with open(path) as f:
        return json.load(f)

def enhance_entities(entities_data):
    """Enhance entities with missing information"""
    
    enhanced_count = 0
    
    for entity_type, entity_list in entities_data['entities'].items():
        for entity in entity_list:
            entity_id = entity.get('entity_id', entity.get('name', 'UNKNOWN'))
            enhanced = False
            
            # Add criminal threshold to antagonists if missing
            if entity.get('agent_type') == 'antagonist' and not entity.get('criminal_threshold'):
                # Determine threshold based on evidence strength
                evidence_strength = entity.get('evidence_strength', 'moderate')
                
                if evidence_strength == 'conclusive':
                    entity['criminal_threshold'] = '95%_exceeded'
                elif evidence_strength == 'strong':
                    entity['criminal_threshold'] = '95%_likely'
                else:
                    entity['criminal_threshold'] = '95%_possible'
                
                enhanced = True
            
            # Add evidence strength if missing
            if not entity.get('evidence_strength'):
                # Determine based on evidence count and type
                evidence_count = len(entity.get('evidence', []))
                ad_res_count = len(entity.get('ad_res_j7_references', []))
                total_evidence = evidence_count + ad_res_count
                
                if total_evidence >= 5:
                    entity['evidence_strength'] = 'strong'
                elif total_evidence >= 3:
                    entity['evidence_strength'] = 'moderate'
                elif total_evidence >= 1:
                    entity['evidence_strength'] = 'weak'
                else:
                    entity['evidence_strength'] = 'insufficient'
                
                enhanced = True
            
            # Add evidence_enhanced timestamp if missing
            if not entity.get('evidence_enhanced'):
                entity['evidence_enhanced'] = datetime.now().isoformat()
                enhanced = True
            
            # Ensure all antagonists have financial_impact tracking
            if entity.get('agent_type') == 'antagonist' and not entity.get('financial_impact'):
                entity['financial_impact'] = {
                    'direct_involvement': 'To be calculated',
                    'primary_categories': []
                }
                enhanced = True
            
            if enhanced:
                enhanced_count += 1
    
    return enhanced_count

def main():
    print("Loading entities...")
    entities_data = load_entities()
    
    print("Enhancing entities...")
    enhanced_count = enhance_entities(entities_data)
    
    # Update metadata
    entities_data['metadata']['version'] = '23.0_ENHANCED_2026_01_06'
    entities_data['metadata']['last_updated'] = datetime.now().isoformat()
    entities_data['metadata']['changes'] = 'Added missing criminal thresholds, evidence strength, and timestamps'
    
    # Save enhanced entities
    output_path = Path('/home/ubuntu/revstream1/data_models/entities/entities.json')
    
    # Backup current version
    backup_path = output_path.with_suffix('.json.backup_' + datetime.now().strftime('%Y%m%d_%H%M%S'))
    if output_path.exists():
        import shutil
        shutil.copy(output_path, backup_path)
        print(f"Backup created: {backup_path}")
    
    # Save enhanced version
    with open(output_path, 'w') as f:
        json.dump(entities_data, f, indent=2)
    
    print(f"Enhanced entities saved to: {output_path}")
    print(f"Enhanced {enhanced_count} entities")

if __name__ == '__main__':
    main()
