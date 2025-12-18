#!/usr/bin/env python3
"""
Comprehensive analysis of current entities, relations, events, and timelines
in revstream1 repository with cross-reference to ad-res-j7 evidence.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def analyze_entities():
    """Analyze entity files in docs/entities/"""
    entities_dir = Path("/home/ubuntu/revstream1/docs/entities")
    entities = {}
    
    for entity_file in entities_dir.glob("*.md"):
        entity_id = entity_file.stem
        with open(entity_file, 'r') as f:
            content = f.read()
            entities[entity_id] = {
                'file': str(entity_file),
                'size': len(content),
                'lines': len(content.split('\n'))
            }
    
    return entities

def analyze_events():
    """Analyze event files in docs/events/"""
    events_dir = Path("/home/ubuntu/revstream1/docs/events")
    events = {}
    
    for event_file in events_dir.glob("*.md"):
        event_id = event_file.stem
        with open(event_file, 'r') as f:
            content = f.read()
            events[event_id] = {
                'file': str(event_file),
                'size': len(content),
                'lines': len(content.split('\n')),
                'has_evidence': 'Evidence:' in content or 'evidence' in content.lower()
            }
    
    return events

def analyze_timeline():
    """Analyze timeline structure"""
    timeline_file = Path("/home/ubuntu/revstream1/docs/timeline.md")
    
    with open(timeline_file, 'r') as f:
        content = f.read()
    
    # Count phases
    phases = content.count('## ')
    # Count events
    events = content.count('#### ')
    # Count evidence links
    evidence_links = content.count('github.com/cogpy/ad-res-j7')
    
    return {
        'phases': phases,
        'events': events,
        'evidence_links': evidence_links,
        'size': len(content)
    }

def analyze_filings():
    """Analyze legal filings structure"""
    filings_dir = Path("/home/ubuntu/revstream1/docs/filings")
    filings = {}
    
    for filing_dir in filings_dir.iterdir():
        if filing_dir.is_dir():
            filing_files = list(filing_dir.glob("*.md"))
            filings[filing_dir.name] = {
                'count': len(filing_files),
                'files': [f.name for f in filing_files]
            }
    
    return filings

def analyze_evidence_cross_refs():
    """Analyze evidence cross-references from JSON files"""
    json_files = [
        "AD_RES_J7_EXTENDED_ANALYSIS_2025_12_17.json",
        "AD_RES_J7_EVIDENCE_INVENTORY_2025_12_16.json",
        "COMPREHENSIVE_ANALYSIS_REFINEMENT_2025_12_17.json"
    ]
    
    evidence_catalog = {}
    
    for json_file in json_files:
        filepath = Path(f"/home/ubuntu/revstream1/{json_file}")
        if filepath.exists():
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                    if 'evidence_catalog' in data:
                        evidence_catalog.update(data['evidence_catalog'])
                except json.JSONDecodeError:
                    pass
    
    return evidence_catalog

def main():
    print("=" * 80)
    print("REVSTREAM1 CURRENT STATE ANALYSIS")
    print("=" * 80)
    print()
    
    # Analyze entities
    print("ENTITIES ANALYSIS")
    print("-" * 80)
    entities = analyze_entities()
    print(f"Total entities: {len(entities)}")
    
    entity_types = defaultdict(int)
    for entity_id in entities.keys():
        entity_type = entity_id.split('_')[0]
        entity_types[entity_type] += 1
    
    print("\nEntity breakdown by type:")
    for entity_type, count in sorted(entity_types.items()):
        print(f"  {entity_type}: {count}")
    print()
    
    # Analyze events
    print("EVENTS ANALYSIS")
    print("-" * 80)
    events = analyze_events()
    print(f"Total events: {len(events)}")
    events_with_evidence = sum(1 for e in events.values() if e['has_evidence'])
    print(f"Events with evidence references: {events_with_evidence}")
    print(f"Events without evidence: {len(events) - events_with_evidence}")
    print()
    
    # Analyze timeline
    print("TIMELINE ANALYSIS")
    print("-" * 80)
    timeline = analyze_timeline()
    print(f"Phases: {timeline['phases']}")
    print(f"Events in timeline: {timeline['events']}")
    print(f"Evidence links to ad-res-j7: {timeline['evidence_links']}")
    print(f"Timeline size: {timeline['size']:,} bytes")
    print()
    
    # Analyze filings
    print("LEGAL FILINGS ANALYSIS")
    print("-" * 80)
    filings = analyze_filings()
    print(f"Total filing categories: {len(filings)}")
    for filing_type, info in sorted(filings.items()):
        print(f"  {filing_type}: {info['count']} files")
    print()
    
    # Analyze evidence catalog
    print("EVIDENCE CATALOG ANALYSIS")
    print("-" * 80)
    evidence_catalog = analyze_evidence_cross_refs()
    print(f"Total evidence items cataloged: {len(evidence_catalog)}")
    
    # Analyze burden of proof
    civil_ready = 0
    criminal_ready = 0
    for item_id, item_data in evidence_catalog.items():
        if isinstance(item_data, dict) and 'burden_of_proof' in item_data:
            bop = item_data['burden_of_proof']
            if isinstance(bop, dict):
                if bop.get('civil_50_percent'):
                    civil_ready += 1
                if bop.get('criminal_95_percent'):
                    criminal_ready += 1
    
    print(f"Evidence meeting civil burden (50%): {civil_ready}")
    print(f"Evidence meeting criminal burden (95%): {criminal_ready}")
    print()
    
    # Save analysis report
    report = {
        'timestamp': datetime.now().isoformat(),
        'entities': {
            'total': len(entities),
            'by_type': dict(entity_types)
        },
        'events': {
            'total': len(events),
            'with_evidence': events_with_evidence,
            'without_evidence': len(events) - events_with_evidence
        },
        'timeline': timeline,
        'filings': filings,
        'evidence_catalog': {
            'total': len(evidence_catalog),
            'civil_ready': civil_ready,
            'criminal_ready': criminal_ready
        }
    }
    
    output_file = Path("/home/ubuntu/revstream1/CURRENT_STATE_ANALYSIS_2025_12_18.json")
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Analysis report saved to: {output_file}")
    print()
    
    # Identify gaps and improvements needed
    print("GAPS AND IMPROVEMENTS NEEDED")
    print("-" * 80)
    
    gaps = []
    
    if len(events) - events_with_evidence > 0:
        gaps.append(f"- {len(events) - events_with_evidence} events lack evidence references")
    
    if evidence_catalog:
        insufficient = len(evidence_catalog) - civil_ready
        if insufficient > 0:
            gaps.append(f"- {insufficient} evidence items don't meet civil burden of proof")
    
    if gaps:
        for gap in gaps:
            print(gap)
    else:
        print("No major gaps identified")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    main()
