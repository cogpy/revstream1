#!/usr/bin/env python3.11
"""
Comprehensive analysis and enhancement script for revstream1 data models
Cross-references with ad-res-j7 evidence repository
Date: 2026-01-11
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")

# Data model paths
ENTITIES_FILE = REVSTREAM_ROOT / "data_models/entities/entities_enhanced_2025_12_12.json"
RELATIONS_FILE = REVSTREAM_ROOT / "data_models/relations/relations_refined_2025_12_27_v31.json"
TIMELINE_FILE = REVSTREAM_ROOT / "data_models/timelines/timeline.json"

# Load data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def scan_evidence_files():
    """Scan ad-res-j7 for evidence files and categorize them"""
    evidence_map = defaultdict(list)
    
    annexures_path = AD_RES_J7_ROOT / "ANNEXURES"
    if annexures_path.exists():
        for jf_dir in annexures_path.iterdir():
            if jf_dir.is_dir() and jf_dir.name.startswith('JF'):
                for file in jf_dir.rglob('*'):
                    if file.is_file():
                        evidence_map[jf_dir.name].append(str(file.relative_to(AD_RES_J7_ROOT)))
    
    # Scan application directories
    for app_dir in ['1-CIVIL-RESPONSE', '2-CRIMINAL-CASE', '3-EXTERNAL-VALIDATION']:
        app_path = AD_RES_J7_ROOT / app_dir
        if app_path.exists():
            for file in app_path.rglob('*'):
                if file.is_file():
                    evidence_map[app_dir].append(str(file.relative_to(AD_RES_J7_ROOT)))
    
    return evidence_map

def analyze_entities():
    """Analyze entities for missing evidence references"""
    entities = load_json(ENTITIES_FILE)
    
    issues = {
        'persons_without_refs': [],
        'orgs_without_refs': [],
        'weak_evidence': [],
        'missing_financial_impact': []
    }
    
    for person in entities.get('entities', {}).get('persons', []):
        name = person.get('name', person.get('entity_id'))
        
        if not person.get('ad_res_j7_references'):
            issues['persons_without_refs'].append(name)
        
        if person.get('evidence_strength') in ['weak', 'moderate']:
            issues['weak_evidence'].append({
                'name': name,
                'strength': person.get('evidence_strength'),
                'type': 'person'
            })
        
        if person.get('agent_type') == 'antagonist' and not person.get('financial_impact'):
            issues['missing_financial_impact'].append(name)
    
    for org in entities.get('entities', {}).get('organizations', []):
        name = org.get('name', org.get('entity_id'))
        
        if not org.get('ad_res_j7_references'):
            issues['orgs_without_refs'].append(name)
        
        if org.get('evidence_strength') in ['weak', 'moderate']:
            issues['weak_evidence'].append({
                'name': name,
                'strength': org.get('evidence_strength'),
                'type': 'organization'
            })
    
    return issues

def analyze_timeline():
    """Analyze timeline for gaps and improvements"""
    timeline = load_json(TIMELINE_FILE)
    
    issues = {
        'missing_evidence': [],
        'missing_key_actors': [],
        'missing_burden_of_proof': [],
        'timeline_gaps': []
    }
    
    entries = timeline.get('timeline', [])
    
    for i, entry in enumerate(entries):
        entry_id = entry.get('entry_id', f"Entry {i}")
        
        if not entry.get('evidence') and not entry.get('source'):
            issues['missing_evidence'].append(entry_id)
        
        if entry.get('event_type') and not entry.get('key_actors'):
            issues['missing_key_actors'].append(entry_id)
        
        if entry.get('event_type') and not entry.get('burden_of_proof'):
            issues['missing_burden_of_proof'].append(entry_id)
    
    # Check for timeline gaps
    dates = [entry.get('date') for entry in entries if entry.get('date')]
    dates.sort()
    
    for i in range(len(dates) - 1):
        # Check for gaps > 1 year
        from datetime import datetime
        try:
            d1 = datetime.strptime(dates[i], '%Y-%m-%d')
            d2 = datetime.strptime(dates[i+1], '%Y-%m-%d')
            gap_days = (d2 - d1).days
            if gap_days > 365:
                issues['timeline_gaps'].append({
                    'from': dates[i],
                    'to': dates[i+1],
                    'gap_days': gap_days
                })
        except:
            pass
    
    return issues

def analyze_relations():
    """Analyze relations for missing evidence"""
    relations = load_json(RELATIONS_FILE)
    
    issues = {
        'missing_evidence': [],
        'weak_evidence': [],
        'missing_ad_res_j7': []
    }
    
    # Handle nested relations structure
    all_relations = []
    relations_data = relations.get('relations', {})
    if isinstance(relations_data, dict):
        for category, rels in relations_data.items():
            if isinstance(rels, list):
                all_relations.extend(rels)
    elif isinstance(relations_data, list):
        all_relations = relations_data
    
    for rel in all_relations:
        if not isinstance(rel, dict):
            continue
        rel_id = rel.get('relation_id', 'unknown')
        
        evidence_items = rel.get('evidence', [])
        if not evidence_items or len(evidence_items) < 2:
            issues['missing_evidence'].append({
                'relation_id': rel_id,
                'type': rel.get('relation_type'),
                'evidence_count': len(evidence_items)
            })
        
        if rel.get('evidence_strength') in ['weak', 'moderate']:
            issues['weak_evidence'].append({
                'relation_id': rel_id,
                'strength': rel.get('evidence_strength')
            })
        
        if not rel.get('ad_res_j7_references'):
            issues['missing_ad_res_j7'].append(rel_id)
    
    return issues

def generate_report():
    """Generate comprehensive analysis report"""
    print("=" * 80)
    print("REVSTREAM1 DATA MODEL ANALYSIS - 2026-01-11")
    print("=" * 80)
    print()
    
    # Scan evidence
    print("Scanning ad-res-j7 evidence repository...")
    evidence_map = scan_evidence_files()
    
    total_files = sum(len(files) for files in evidence_map.values())
    print(f"Total evidence files found: {total_files}")
    print()
    
    for category, files in sorted(evidence_map.items()):
        print(f"  {category}: {len(files)} files")
    print()
    
    # Analyze entities
    print("-" * 80)
    print("ENTITIES ANALYSIS")
    print("-" * 80)
    entity_issues = analyze_entities()
    
    print(f"Persons without ad_res_j7_references: {len(entity_issues['persons_without_refs'])}")
    for name in entity_issues['persons_without_refs']:
        print(f"  - {name}")
    print()
    
    print(f"Organizations without ad_res_j7_references: {len(entity_issues['orgs_without_refs'])}")
    for name in entity_issues['orgs_without_refs']:
        print(f"  - {name}")
    print()
    
    print(f"Entities with weak/moderate evidence: {len(entity_issues['weak_evidence'])}")
    for item in entity_issues['weak_evidence']:
        print(f"  - {item['name']} ({item['type']}, {item['strength']})")
    print()
    
    print(f"Antagonists missing financial impact: {len(entity_issues['missing_financial_impact'])}")
    for name in entity_issues['missing_financial_impact']:
        print(f"  - {name}")
    print()
    
    # Analyze timeline
    print("-" * 80)
    print("TIMELINE ANALYSIS")
    print("-" * 80)
    timeline_issues = analyze_timeline()
    
    print(f"Entries missing evidence: {len(timeline_issues['missing_evidence'])}")
    print(f"Entries missing key actors: {len(timeline_issues['missing_key_actors'])}")
    print(f"Entries missing burden of proof: {len(timeline_issues['missing_burden_of_proof'])}")
    print(f"Timeline gaps > 1 year: {len(timeline_issues['timeline_gaps'])}")
    
    if timeline_issues['timeline_gaps']:
        print("\nSignificant timeline gaps:")
        for gap in timeline_issues['timeline_gaps'][:5]:
            print(f"  {gap['from']} -> {gap['to']} ({gap['gap_days']} days)")
    print()
    
    # Analyze relations
    print("-" * 80)
    print("RELATIONS ANALYSIS")
    print("-" * 80)
    relation_issues = analyze_relations()
    
    print(f"Relations with insufficient evidence: {len(relation_issues['missing_evidence'])}")
    print(f"Relations with weak evidence: {len(relation_issues['weak_evidence'])}")
    print(f"Relations missing ad_res_j7 references: {len(relation_issues['missing_ad_res_j7'])}")
    print()
    
    # Generate recommendations
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()
    
    recommendations = []
    
    if entity_issues['persons_without_refs']:
        recommendations.append(f"1. Add ad_res_j7_references to {len(entity_issues['persons_without_refs'])} persons")
    
    if entity_issues['orgs_without_refs']:
        recommendations.append(f"2. Add ad_res_j7_references to {len(entity_issues['orgs_without_refs'])} organizations")
    
    if entity_issues['weak_evidence']:
        recommendations.append(f"3. Strengthen evidence for {len(entity_issues['weak_evidence'])} entities")
    
    if timeline_issues['missing_evidence']:
        recommendations.append(f"4. Add evidence to {len(timeline_issues['missing_evidence'])} timeline entries")
    
    if timeline_issues['missing_key_actors']:
        recommendations.append(f"5. Add key actors to {len(timeline_issues['missing_key_actors'])} timeline entries")
    
    if relation_issues['missing_ad_res_j7']:
        recommendations.append(f"6. Add ad_res_j7_references to {len(relation_issues['missing_ad_res_j7'])} relations")
    
    for rec in recommendations:
        print(rec)
    
    print()
    print("=" * 80)
    
    # Save detailed report
    report = {
        'timestamp': datetime.now().isoformat(),
        'evidence_summary': {
            'total_files': total_files,
            'categories': {k: len(v) for k, v in evidence_map.items()}
        },
        'entity_issues': entity_issues,
        'timeline_issues': timeline_issues,
        'relation_issues': relation_issues,
        'recommendations': recommendations
    }
    
    report_file = REVSTREAM_ROOT / "ANALYSIS_REPORT_2026_01_11.json"
    save_json(report_file, report)
    print(f"\nDetailed report saved to: {report_file}")

if __name__ == "__main__":
    generate_report()
