#!/usr/bin/env python3
"""
Scan ad-res-j7 repository for evidence files and create comprehensive mapping
"""

import os
import json
from pathlib import Path
from datetime import datetime

def scan_evidence_directory(base_path):
    """Scan ad-res-j7 for evidence files"""
    evidence_map = {
        'ANNEXURES': {},
        'Supporting_Files': {},
        'Evidence': {},
        'Legal': {},
        'Other': {}
    }
    
    ad_res_j7_path = Path(base_path)
    
    # Scan ANNEXURES
    annexures_path = ad_res_j7_path / 'ANNEXURES'
    if annexures_path.exists():
        for item in annexures_path.iterdir():
            if item.is_dir():
                # Count files in subdirectory
                file_count = len(list(item.rglob('*')))
                evidence_map['ANNEXURES'][item.name] = {
                    'path': str(item.relative_to(ad_res_j7_path)),
                    'type': 'directory',
                    'file_count': file_count
                }
            elif item.is_file():
                evidence_map['ANNEXURES'][item.name] = {
                    'path': str(item.relative_to(ad_res_j7_path)),
                    'type': 'file',
                    'size': item.stat().st_size
                }
    
    # Scan for Supporting Files (SF series)
    for sf_file in ad_res_j7_path.rglob('SF*'):
        if sf_file.is_file() and sf_file.suffix in ['.md', '.pdf', '.txt']:
            evidence_map['Supporting_Files'][sf_file.name] = {
                'path': str(sf_file.relative_to(ad_res_j7_path)),
                'type': 'file',
                'size': sf_file.stat().st_size
            }
    
    # Scan evidence directory
    evidence_path = ad_res_j7_path / 'evidence'
    if evidence_path.exists():
        for item in evidence_path.iterdir():
            if item.is_file() and item.suffix in ['.md', '.pdf', '.txt', '.json']:
                evidence_map['Evidence'][item.name] = {
                    'path': str(item.relative_to(ad_res_j7_path)),
                    'type': 'file',
                    'size': item.stat().st_size
                }
    
    # Scan legal directories
    for legal_dir in ['1-CIVIL-RESPONSE', '2-CRIMINAL-CASE', '3-EXTERNAL-VALIDATION']:
        legal_path = ad_res_j7_path / legal_dir
        if legal_path.exists():
            for item in legal_path.rglob('*'):
                if item.is_file() and item.suffix in ['.md', '.pdf', '.txt']:
                    evidence_map['Legal'][f"{legal_dir}/{item.name}"] = {
                        'path': str(item.relative_to(ad_res_j7_path)),
                        'type': 'file',
                        'size': item.stat().st_size
                    }
    
    # Scan for Ketoni evidence
    for ketoni_file in ad_res_j7_path.rglob('*KETONI*'):
        if ketoni_file.is_file() and ketoni_file.suffix in ['.md', '.scm', '.txt']:
            evidence_map['Other'][ketoni_file.name] = {
                'path': str(ketoni_file.relative_to(ad_res_j7_path)),
                'type': 'ketoni_evidence',
                'size': ketoni_file.stat().st_size
            }
    
    return evidence_map

def create_evidence_index(evidence_map):
    """Create a searchable evidence index"""
    index = []
    
    for category, items in evidence_map.items():
        for name, details in items.items():
            index.append({
                'category': category,
                'name': name,
                'path': details['path'],
                'type': details.get('type', 'unknown'),
                'reference': f"{category}/{name}"
            })
    
    return index

def main():
    """Main function"""
    ad_res_j7_path = '/home/ubuntu/ad-res-j7'
    
    print("=" * 80)
    print("AD-RES-J7 EVIDENCE SCANNING")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    print("Scanning ad-res-j7 repository for evidence files...")
    evidence_map = scan_evidence_directory(ad_res_j7_path)
    
    print()
    print("EVIDENCE SUMMARY")
    print("-" * 80)
    for category, items in evidence_map.items():
        print(f"{category}: {len(items)} items")
    print()
    
    # Create searchable index
    evidence_index = create_evidence_index(evidence_map)
    
    # Save to JSON
    output_file = '/home/ubuntu/revstream1/AD_RES_J7_EVIDENCE_INDEX_2026_01_18.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'scan_date': datetime.now().isoformat(),
                'total_items': len(evidence_index),
                'categories': list(evidence_map.keys())
            },
            'evidence_map': evidence_map,
            'evidence_index': evidence_index
        }, f, indent=2, ensure_ascii=False)
    
    print(f"Evidence index saved to: {output_file}")
    print(f"Total evidence items indexed: {len(evidence_index)}")
    print()
    
    # Show some key evidence
    print("KEY EVIDENCE CATEGORIES:")
    print("-" * 80)
    
    # JF series
    jf_items = [item for item in evidence_index if 'JF' in item['name'] and item['category'] == 'ANNEXURES']
    print(f"JF Series (ANNEXURES): {len(jf_items)} items")
    for item in sorted(jf_items, key=lambda x: x['name'])[:10]:
        print(f"  - {item['name']}")
    if len(jf_items) > 10:
        print(f"  ... and {len(jf_items) - 10} more")
    print()
    
    # SF series
    sf_items = [item for item in evidence_index if item['category'] == 'Supporting_Files']
    print(f"SF Series (Supporting Files): {len(sf_items)} items")
    for item in sorted(sf_items, key=lambda x: x['name'])[:10]:
        print(f"  - {item['name']}")
    if len(sf_items) > 10:
        print(f"  ... and {len(sf_items) - 10} more")
    print()
    
    # Ketoni evidence
    ketoni_items = [item for item in evidence_index if 'ketoni' in item['name'].lower()]
    print(f"Ketoni Evidence: {len(ketoni_items)} items")
    for item in sorted(ketoni_items, key=lambda x: x['name'])[:10]:
        print(f"  - {item['name']}")
    print()
    
    print("=" * 80)
    print("Evidence scanning complete.")
    print("=" * 80)

if __name__ == '__main__':
    main()
