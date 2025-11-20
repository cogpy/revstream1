#!/usr/bin/env python3
"""
Comprehensive Analysis of revstream1 Data Models - FIXED
Version: 2025-11-20
"""

import json
from pathlib import Path
from collections import defaultdict

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_relations(relations_data):
    """Analyze relations structure - handle nested structure"""
    analysis = {
        "total_relations": 0,
        "relation_types": defaultdict(int),
        "relations_with_evidence": 0
    }
    
    # Relations are nested by type
    relations_dict = relations_data.get("relations", {})
    
    for rel_category, rel_list in relations_dict.items():
        if isinstance(rel_list, list):
            for relation in rel_list:
                analysis["total_relations"] += 1
                rel_type = relation.get("relation_type", "unknown")
                analysis["relation_types"][rel_type] += 1
                
                if relation.get("evidence") and len(relation["evidence"]) > 0:
                    analysis["relations_with_evidence"] += 1
    
    return analysis

def main():
    base_path = Path("/home/ubuntu/revstream1/data_models")
    
    print("="*80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS - FIXED")
    print("="*80)
    
    # Load relations
    relations = load_json(base_path / "relations/relations_refined_2025_11_19_v4.json")
    
    if relations:
        print("\n### RELATIONS ANALYSIS ###")
        relation_analysis = analyze_relations(relations)
        print(f"Total Relations: {relation_analysis['total_relations']}")
        print(f"Relations with Evidence: {relation_analysis['relations_with_evidence']}")
        
        print("\nRelation Types:")
        for rel_type, count in sorted(relation_analysis['relation_types'].items()):
            print(f"  {rel_type}: {count}")

if __name__ == "__main__":
    main()
