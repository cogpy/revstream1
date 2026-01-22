#!/usr/bin/env python3
"""
Scan ad-res-j7 for evidence not yet fully integrated into revstream1
"""
import json
import os
from pathlib import Path
from datetime import datetime

def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        return None

def extract_evidence_refs(data_models_path):
    """Extract all evidence references from revstream1 data models"""
    refs = set()
    
    # Load entities
    entities_data = load_json(data_models_path / 'entities/entities.json')
    if entities_data and 'entities' in entities_data:
        for category, entities_list in entities_data['entities'].items():
            if isinstance(entities_list, list):
                for entity in entities_list:
                    refs.update(entity.get('ad_res_j7_references', []))
                    refs.update(entity.get('evidence', []))
    
    # Load events
    events_data = load_json(data_models_path / 'events.json')
    if events_data and 'events' in events_data:
        for event in events_data['events']:
            refs.update(event.get('ad_res_j7_references', []))
            refs.update(event.get('evidence', []))
    
    # Load relations
    relations_data = load_json(data_models_path / 'relations.json')
    if relations_data and 'relations' in relations_data:
        for rel_type, relations_list in relations_data['relations'].items():
            if isinstance(relations_list, list):
                for relation in relations_list:
                    refs.update(relation.get('ad_res_j7_evidence', []))
                    refs.update(relation.get('evidence', []))
    
    return refs

def scan_ad_res_j7_structure(ad_res_j7_path):
    """Scan ad-res-j7 for key evidence files"""
    evidence_files = {}
    
    # Key directories to scan
    key_dirs = [
        'ANNEXURES',
        'jax-response',
        '1-CIVIL-RESPONSE',
        '2-CRIMINAL-CASE',
        'revenue-stream-hijacking-rynette',
        'evidence'
    ]
    
    for dir_name in key_dirs:
        dir_path = ad_res_j7_path / dir_name
        if dir_path.exists():
            # Find markdown and PDF files
            md_files = list(dir_path.rglob('*.md'))
            pdf_files = list(dir_path.rglob('*.pdf'))
            json_files = list(dir_path.rglob('*.json'))
            
            evidence_files[dir_name] = {
                'md': [str(f.relative_to(ad_res_j7_path)) for f in md_files],
                'pdf': [str(f.relative_to(ad_res_j7_path)) for f in pdf_files],
                'json': [str(f.relative_to(ad_res_j7_path)) for f in json_files]
            }
    
    return evidence_files

def identify_gaps(existing_refs, ad_res_j7_files):
    """Identify evidence files not yet referenced"""
    gaps = []
    
    # Check for SF files
    sf_pattern = 'SF'
    for dir_name, file_types in ad_res_j7_files.items():
        for file_path in file_types.get('md', []):
            if 'SF' in file_path and not any(sf_ref in str(existing_refs) for sf_ref in [file_path, Path(file_path).name]):
                gaps.append({
                    'type': 'supporting_file',
                    'path': file_path,
                    'priority': 'high'
                })
    
    return gaps

def main():
    print("=" * 80)
    print("AD-RES-J7 EVIDENCE SCAN")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 80)
    
    revstream1_path = Path('/home/ubuntu/revstream1')
    ad_res_j7_path = Path('/home/ubuntu/ad-res-j7')
    
    # Extract existing references
    print("\n### Extracting existing evidence references from revstream1...")
    existing_refs = extract_evidence_refs(revstream1_path / 'docs/data_models')
    print(f"Found {len(existing_refs)} unique evidence references")
    
    # Scan ad-res-j7
    print("\n### Scanning ad-res-j7 repository structure...")
    ad_res_j7_files = scan_ad_res_j7_structure(ad_res_j7_path)
    
    total_files = sum(len(files['md']) + len(files['pdf']) + len(files['json']) 
                     for files in ad_res_j7_files.values())
    print(f"Found {total_files} evidence files in ad-res-j7")
    
    # Print summary by directory
    print("\n### Evidence file distribution:")
    for dir_name, file_types in ad_res_j7_files.items():
        md_count = len(file_types['md'])
        pdf_count = len(file_types['pdf'])
        json_count = len(file_types['json'])
        print(f"  {dir_name}: {md_count} MD, {pdf_count} PDF, {json_count} JSON")
    
    # Identify gaps
    print("\n### Identifying potential gaps...")
    gaps = identify_gaps(existing_refs, ad_res_j7_files)
    
    if gaps:
        print(f"\nFound {len(gaps)} potential evidence files to review:")
        for gap in gaps[:10]:
            print(f"  - {gap['path']} (Priority: {gap['priority']})")
    else:
        print("\nNo obvious gaps detected. Evidence coverage appears comprehensive.")
    
    # Check for SF files specifically
    print("\n### Supporting Files (SF) in ad-res-j7:")
    for dir_name, file_types in ad_res_j7_files.items():
        sf_files = [f for f in file_types['md'] if 'SF' in f and 'ANNEXURES' in f]
        if sf_files:
            for sf_file in sf_files:
                sf_name = Path(sf_file).name
                referenced = any(sf_name in str(ref) for ref in existing_refs)
                status = "✓ Referenced" if referenced else "✗ Not referenced"
                print(f"  {sf_name}: {status}")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
