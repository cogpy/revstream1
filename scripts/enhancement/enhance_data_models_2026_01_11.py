#!/usr/bin/env python3.11
"""
Enhancement script for revstream1 data models.

This script programmatically enhances the data models by:
- Adding ad_res_j7_references to entities and relations.
- Adding evidence to timeline entries.
- Strengthening evidence where possible.

Date: 2026-01-11
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

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


def get_evidence_map():
    """Create a map of keywords to evidence files."""
    evidence_map = defaultdict(list)
    annexures_path = AD_RES_J7_ROOT / "ANNEXURES"
    if annexures_path.exists():
        for jf_dir in annexures_path.iterdir():
            if jf_dir.is_dir() and jf_dir.name.startswith('JF'):
                for file in jf_dir.rglob('*'):
                    if file.is_file():
                        evidence_path = str(file.relative_to(AD_RES_J7_ROOT))
                        # Keywords from filename
                        keywords = re.findall(r'\w+', file.name.lower())
                        for keyword in keywords:
                            if len(keyword) > 3:
                                evidence_map[keyword].append(evidence_path)
                        # Keywords from directory name
                        keywords_dir = re.findall(r'\w+', jf_dir.name.lower())
                        for keyword in keywords_dir:
                            if len(keyword) > 3:
                                evidence_map[keyword].append(evidence_path)

    return evidence_map

def enhance_entities(evidence_map):
    """Enhance entities with ad_res_j7_references."""
    entities = load_json(ENTITIES_FILE)
    updated = False

    for person in entities.get('entities', {}).get('persons', []):
        if not person.get('ad_res_j7_references'):
            name_keywords = re.findall(r'\w+', person.get('name', '').lower())
            found_evidence = []
            for keyword in name_keywords:
                if keyword in evidence_map:
                    found_evidence.extend(evidence_map[keyword])
            if found_evidence:
                person['ad_res_j7_references'] = sorted(list(set(found_evidence)))
                person['evidence_enhanced'] = datetime.now().isoformat()
                updated = True

    for org in entities.get('entities', {}).get('organizations', []):
        if not org.get('ad_res_j7_references'):
            name_keywords = re.findall(r'\w+', org.get('name', '').lower())
            found_evidence = []
            for keyword in name_keywords:
                if keyword in evidence_map:
                    found_evidence.extend(evidence_map[keyword])
            if found_evidence:
                org['ad_res_j7_references'] = sorted(list(set(found_evidence)))
                org['evidence_enhanced'] = datetime.now().isoformat()
                updated = True

    if updated:
        entities['metadata']['last_updated'] = datetime.now().isoformat()
        entities['metadata']['version'] = f"{entities['metadata'].get('version', '1.0').split('_')[0]}_ENHANCED_{datetime.now().strftime('%Y%m%d')}"
        save_json(ENTITIES_FILE, entities)
        print("Entities file updated.")

def enhance_relations(evidence_map):
    """Enhance relations with ad_res_j7_references."""
    relations = load_json(RELATIONS_FILE)
    updated = False

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
        if not rel.get('ad_res_j7_references'):
            rel_type_keywords = re.findall(r'\w+', rel.get('relation_type', '').lower())
            found_evidence = []
            for keyword in rel_type_keywords:
                if keyword in evidence_map:
                    found_evidence.extend(evidence_map[keyword])
            if found_evidence:
                rel['ad_res_j7_references'] = sorted(list(set(found_evidence)))
                rel['evidence_verified'] = datetime.now().isoformat()
                updated = True

    if updated:
        relations['metadata']['last_updated'] = datetime.now().isoformat()
        relations['metadata']['version'] = f"{relations['metadata'].get('version', '1.0').split('_')[0]}_ENHANCED_{datetime.now().strftime('%Y%m%d')}"
        save_json(RELATIONS_FILE, relations)
        print("Relations file updated.")

def enhance_timeline(evidence_map):
    """Enhance timeline with evidence."""
    timeline = load_json(TIMELINE_FILE)
    updated = False

    for entry in timeline.get('timeline', []):
        if not entry.get('evidence') and not entry.get('source'):
            event_keywords = re.findall(r'\w+', entry.get('event', '').lower())
            found_evidence = []
            for keyword in event_keywords:
                if keyword in evidence_map:
                    found_evidence.extend(evidence_map[keyword])
            if found_evidence:
                entry['evidence'] = sorted(list(set(found_evidence)))
                entry['last_updated'] = datetime.now().isoformat()
                updated = True

    if updated:
        timeline['metadata']['last_updated'] = datetime.now().isoformat()
        timeline['metadata']['version'] = f"{timeline['metadata'].get('version', '1.0').split('_')[0]}_ENHANCED_{datetime.now().strftime('%Y%m%d')}"
        save_json(TIMELINE_FILE, timeline)
        print("Timeline file updated.")

def main():
    print("Starting data model enhancement...")
    evidence_map = get_evidence_map()
    enhance_entities(evidence_map)
    enhance_relations(evidence_map)
    enhance_timeline(evidence_map)
    print("Enhancement process complete.")

if __name__ == "__main__":
    main()
