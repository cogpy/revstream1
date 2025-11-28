#!/usr/bin/env python3
"""
Cross-reference revstream1 data models with ad-res-j7 evidence repository
Identifies missing evidence links and suggests improvements
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import re

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_J7_ROOT = Path("/home/ubuntu/ad-res-j7")

# Data model paths
ENTITIES_FILE = REVSTREAM_ROOT / "data_models/entities/entities_refined_2025_11_27_v22.json"
EVENTS_FILE = REVSTREAM_ROOT / "data_models/events/events_refined_2025_11_27_v23.json"
RELATIONS_FILE = REVSTREAM_ROOT / "data_models/relations/relations_refined_2025_11_27_v19.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty printing"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def scan_evidence_repository():
    """Scan ad-res-j7 for evidence files and categorize them"""
    evidence_map = {
        'ANNEXURES': defaultdict(list),
        'case_2025_137857': defaultdict(list),
        'FINAL_AFFIDAVIT_PACKAGE': defaultdict(list),
        'evidence': defaultdict(list),
        'docs': defaultdict(list),
        'other': defaultdict(list)
    }
    
    # Key directories to scan
    key_dirs = ['ANNEXURES', 'case_2025_137857', 'FINAL_AFFIDAVIT_PACKAGE', 'evidence', 'docs']
    
    for key_dir in key_dirs:
        dir_path = AD_RES_J7_ROOT / key_dir
        if dir_path.exists():
            for file_path in dir_path.rglob('*'):
                if file_path.is_file():
                    rel_path = str(file_path.relative_to(AD_RES_J7_ROOT))
                    ext = file_path.suffix.lower()
                    
                    # Categorize by evidence type
                    if 'JF' in rel_path:
                        evidence_map[key_dir]['JF_evidence'].append(rel_path)
                    elif ext in ['.pdf', '.PDF']:
                        evidence_map[key_dir]['pdfs'].append(rel_path)
                    elif ext in ['.eml', '.msg']:
                        evidence_map[key_dir]['emails'].append(rel_path)
                    elif ext in ['.jpg', '.png', '.jpeg']:
                        evidence_map[key_dir]['images'].append(rel_path)
                    elif ext == '.md':
                        evidence_map[key_dir]['markdown'].append(rel_path)
                    elif ext == '.json':
                        evidence_map[key_dir]['json'].append(rel_path)
                    else:
                        evidence_map[key_dir]['other'].append(rel_path)
    
    return evidence_map

def find_missing_event_dates():
    """Find events with missing dates and suggest dates based on context"""
    events_data = load_json(EVENTS_FILE)
    events = events_data.get('events', [])
    
    missing_dates = []
    for event in events:
        if not event.get('date'):
            missing_dates.append({
                'event_id': event.get('event_id'),
                'title': event.get('title'),
                'category': event.get('category'),
                'timeline_phase': event.get('timeline_phase'),
                'related_events': event.get('related_events', [])
            })
    
    return missing_dates

def find_missing_entities():
    """Find events and relations with missing entity references"""
    events_data = load_json(EVENTS_FILE)
    relations_data = load_json(RELATIONS_FILE)
    
    events = events_data.get('events', [])
    relations = relations_data.get('relations', {})
    
    missing_entity_events = []
    for event in events:
        if not event.get('entities_involved') or len(event.get('entities_involved', [])) == 0:
            missing_entity_events.append({
                'event_id': event.get('event_id'),
                'title': event.get('title'),
                'perpetrators': event.get('perpetrators', []),
                'victims': event.get('victims', [])
            })
    
    missing_entity_relations = []
    for rel_type, rel_list in relations.items():
        for rel in rel_list:
            if not rel.get('source_entity') or not rel.get('target_entity'):
                missing_entity_relations.append({
                    'relation_id': rel.get('relation_id'),
                    'relation_type': rel.get('relation_type'),
                    'source_entity': rel.get('source_entity'),
                    'target_entity': rel.get('target_entity')
                })
    
    return missing_entity_events, missing_entity_relations

def generate_evidence_suggestions():
    """Generate suggestions for evidence links based on event/entity context"""
    events_data = load_json(EVENTS_FILE)
    entities_data = load_json(ENTITIES_FILE)
    
    events = events_data.get('events', [])
    entities = entities_data.get('entities', {})
    
    suggestions = []
    
    # Scan for events that might benefit from additional evidence
    for event in events:
        event_id = event.get('event_id')
        title = event.get('title', '')
        category = event.get('category', '')
        
        # Suggest evidence based on keywords
        if 'shopify' in title.lower():
            suggestions.append({
                'event_id': event_id,
                'suggestion': 'Consider adding Shopify invoice evidence from ANNEXURES/JF02/',
                'evidence_dir': 'ANNEXURES/JF02/'
            })
        
        if 'email' in title.lower() or 'correspondence' in category.lower():
            suggestions.append({
                'event_id': event_id,
                'suggestion': 'Consider adding email evidence from ANNEXURES/JF05/',
                'evidence_dir': 'ANNEXURES/JF05/'
            })
        
        if 'bank' in title.lower() or 'transfer' in title.lower():
            suggestions.append({
                'event_id': event_id,
                'suggestion': 'Consider adding bank statement evidence from ANNEXURES/JF04/',
                'evidence_dir': 'ANNEXURES/JF04/'
            })
    
    return suggestions

def main():
    print("Cross-referencing revstream1 with ad-res-j7 evidence repository...")
    
    print("\n1. Scanning evidence repository...")
    evidence_map = scan_evidence_repository()
    
    print("2. Finding events with missing dates...")
    missing_dates = find_missing_event_dates()
    
    print("3. Finding missing entity references...")
    missing_entity_events, missing_entity_relations = find_missing_entities()
    
    print("4. Generating evidence suggestions...")
    evidence_suggestions = generate_evidence_suggestions()
    
    # Compile report
    report = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'ad_res_j7_path': str(AD_RES_J7_ROOT),
            'revstream_path': str(REVSTREAM_ROOT)
        },
        'evidence_repository_summary': {
            'ANNEXURES': {
                'total_files': sum(len(files) for files in evidence_map['ANNEXURES'].values()),
                'categories': {k: len(v) for k, v in evidence_map['ANNEXURES'].items()}
            },
            'case_2025_137857': {
                'total_files': sum(len(files) for files in evidence_map['case_2025_137857'].values()),
                'categories': {k: len(v) for k, v in evidence_map['case_2025_137857'].items()}
            },
            'FINAL_AFFIDAVIT_PACKAGE': {
                'total_files': sum(len(files) for files in evidence_map['FINAL_AFFIDAVIT_PACKAGE'].values()),
                'categories': {k: len(v) for k, v in evidence_map['FINAL_AFFIDAVIT_PACKAGE'].items()}
            },
            'evidence': {
                'total_files': sum(len(files) for files in evidence_map['evidence'].values()),
                'categories': {k: len(v) for k, v in evidence_map['evidence'].items()}
            }
        },
        'missing_dates': {
            'count': len(missing_dates),
            'events': missing_dates
        },
        'missing_entities': {
            'events_count': len(missing_entity_events),
            'relations_count': len(missing_entity_relations),
            'events': missing_entity_events,
            'relations': missing_entity_relations
        },
        'evidence_suggestions': {
            'count': len(evidence_suggestions),
            'suggestions': evidence_suggestions[:20]  # Top 20
        }
    }
    
    # Save report
    report_file = REVSTREAM_ROOT / f"CROSS_REFERENCE_REPORT_{datetime.now().strftime('%Y_%m_%d')}.json"
    save_json(report, report_file)
    
    print(f"\n✓ Cross-reference report saved to: {report_file}")
    print(f"\nSummary:")
    print(f"  Evidence files in ANNEXURES: {report['evidence_repository_summary']['ANNEXURES']['total_files']}")
    print(f"  Evidence files in case_2025_137857: {report['evidence_repository_summary']['case_2025_137857']['total_files']}")
    print(f"  Events with missing dates: {len(missing_dates)}")
    print(f"  Events with missing entities: {len(missing_entity_events)}")
    print(f"  Relations with missing entities: {len(missing_entity_relations)}")
    print(f"  Evidence suggestions generated: {len(evidence_suggestions)}")
    
    return report

if __name__ == '__main__':
    report = main()
