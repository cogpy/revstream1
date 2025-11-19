#!/usr/bin/env python3
"""
Cross-reference analysis between revstream1 data models and ad-res-j7 evidence
"""

import json
import os
import re
from collections import defaultdict
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_dates_from_timeline_md(filepath):
    """Extract dates and events from markdown timeline"""
    events = []
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Pattern to match dates in format: ### Month Day, Year
    date_pattern = r'###\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})'
    # Pattern to match **Event**: description
    event_pattern = r'\*\*Event\*\*:\s+(.+?)(?:\n|$)'
    # Pattern to match **Significance**: description
    significance_pattern = r'\*\*Significance\*\*:\s+(.+?)(?:\n|$)'
    # Pattern to match **Entities Involved**: entities
    entities_pattern = r'\*\*Entities Involved\*\*:\s+(.+?)(?:\n|$)'
    
    lines = content.split('\n')
    current_date = None
    current_event = {}
    
    for i, line in enumerate(lines):
        date_match = re.search(date_pattern, line)
        if date_match:
            if current_event and current_date:
                events.append(current_event)
            current_date = date_match.group(1)
            current_event = {'date_text': current_date, 'line_num': i}
        
        if current_date:
            event_match = re.search(event_pattern, line)
            if event_match:
                current_event['event'] = event_match.group(1).strip()
            
            sig_match = re.search(significance_pattern, line)
            if sig_match:
                current_event['significance'] = sig_match.group(1).strip()
            
            ent_match = re.search(entities_pattern, line)
            if ent_match:
                current_event['entities'] = ent_match.group(1).strip()
    
    if current_event and current_date:
        events.append(current_event)
    
    return events

def parse_date_text(date_text):
    """Parse date text to YYYY-MM-DD format"""
    try:
        # Try parsing "Month Day, Year" format
        dt = datetime.strptime(date_text, '%B %d, %Y')
        return dt.strftime('%Y-%m-%d')
    except:
        try:
            # Try parsing "Month Year" format
            dt = datetime.strptime(date_text, '%B %Y')
            return dt.strftime('%Y-%m-01')
        except:
            return None

def cross_reference_events(revstream_events, evidence_timeline_events):
    """Cross-reference events between revstream1 and ad-res-j7"""
    matches = []
    missing_in_revstream = []
    date_mismatches = []
    
    # Create lookup by date for revstream events
    revstream_by_date = defaultdict(list)
    for event in revstream_events:
        if 'date' in event:
            revstream_by_date[event['date']].append(event)
    
    # Check each evidence timeline event
    for ev_event in evidence_timeline_events:
        parsed_date = parse_date_text(ev_event.get('date_text', ''))
        if not parsed_date:
            continue
        
        # Look for matching events in revstream
        matching = revstream_by_date.get(parsed_date, [])
        
        if matching:
            matches.append({
                'date': parsed_date,
                'evidence_event': ev_event.get('event', ''),
                'revstream_events': [e.get('title', e.get('event_id', '')) for e in matching],
                'match_count': len(matching)
            })
        else:
            # Check nearby dates (within 7 days)
            nearby_found = False
            for days_offset in range(-7, 8):
                try:
                    from datetime import timedelta
                    check_date = datetime.strptime(parsed_date, '%Y-%m-%d') + timedelta(days=days_offset)
                    check_date_str = check_date.strftime('%Y-%m-%d')
                    if revstream_by_date.get(check_date_str):
                        date_mismatches.append({
                            'evidence_date': parsed_date,
                            'revstream_date': check_date_str,
                            'evidence_event': ev_event.get('event', ''),
                            'revstream_events': [e.get('title', '') for e in revstream_by_date[check_date_str]]
                        })
                        nearby_found = True
                        break
                except:
                    pass
            
            if not nearby_found:
                missing_in_revstream.append({
                    'date': parsed_date,
                    'event': ev_event.get('event', ''),
                    'significance': ev_event.get('significance', ''),
                    'entities': ev_event.get('entities', '')
                })
    
    return {
        'matches': matches,
        'missing_in_revstream': missing_in_revstream,
        'date_mismatches': date_mismatches
    }

def identify_new_entities(evidence_timeline_events, revstream_entities):
    """Identify entities mentioned in evidence but not in revstream data"""
    # Extract entity names from revstream
    revstream_entity_names = set()
    if 'entities' in revstream_entities:
        for entity_type, entities in revstream_entities['entities'].items():
            if isinstance(entities, list):
                for entity in entities:
                    if 'name' in entity:
                        revstream_entity_names.add(entity['name'].lower())
    
    # Common entities mentioned in evidence
    evidence_entities = set()
    for ev_event in evidence_timeline_events:
        entities_text = ev_event.get('entities', '')
        if entities_text:
            # Split by comma and clean
            parts = [e.strip() for e in entities_text.split(',')]
            evidence_entities.update([p.lower() for p in parts if p])
    
    # Find missing entities
    missing_entities = []
    for ent in evidence_entities:
        # Check if entity name appears in revstream
        found = False
        for rev_ent in revstream_entity_names:
            if ent in rev_ent or rev_ent in ent:
                found = True
                break
        if not found:
            missing_entities.append(ent)
    
    return missing_entities

def analyze_event_coverage(revstream_events):
    """Analyze temporal coverage of events"""
    dates = []
    for event in revstream_events:
        if 'date' in event:
            try:
                dt = datetime.strptime(event['date'], '%Y-%m-%d')
                dates.append(dt)
            except:
                pass
    
    if not dates:
        return {}
    
    dates.sort()
    
    # Find gaps
    gaps = []
    for i in range(len(dates) - 1):
        gap_days = (dates[i+1] - dates[i]).days
        if gap_days > 90:  # Gaps larger than 90 days
            gaps.append({
                'start_date': dates[i].strftime('%Y-%m-%d'),
                'end_date': dates[i+1].strftime('%Y-%m-%d'),
                'gap_days': gap_days
            })
    
    return {
        'earliest_event': dates[0].strftime('%Y-%m-%d'),
        'latest_event': dates[-1].strftime('%Y-%m-%d'),
        'total_span_days': (dates[-1] - dates[0]).days,
        'total_events': len(dates),
        'significant_gaps': gaps
    }

def main():
    """Main cross-reference analysis"""
    print("=" * 80)
    print("CROSS-REFERENCE ANALYSIS: REVSTREAM1 vs AD-RES-J7")
    print("=" * 80)
    print()
    
    # Load revstream1 data
    revstream_base = '/home/ubuntu/revstream1/data_models'
    entities_data = load_json(f'{revstream_base}/entities/entities_refined_2025_11_18.json')
    events_data = load_json(f'{revstream_base}/events/events_refined_2025_11_18.json')
    relations_data = load_json(f'{revstream_base}/relations/relations_refined_2025_11_18.json')
    timeline_data = load_json(f'{revstream_base}/timelines/timeline_refined_2025_11_18.json')
    
    # Load ad-res-j7 evidence timeline
    evidence_timeline_path = '/home/ubuntu/ad-res-j7/ANNEXURES/JF09/COMPREHENSIVE_TIMELINE_2017_2025.md'
    evidence_events = extract_dates_from_timeline_md(evidence_timeline_path)
    
    print(f"Loaded {len(events_data.get('events', []))} events from revstream1")
    print(f"Extracted {len(evidence_events)} events from ad-res-j7 timeline")
    print()
    
    # Cross-reference events
    print("1. EVENT CROSS-REFERENCE ANALYSIS")
    print("-" * 80)
    cross_ref = cross_reference_events(events_data.get('events', []), evidence_events)
    
    print(f"Matched events: {len(cross_ref['matches'])}")
    print(f"Events in evidence but missing in revstream1: {len(cross_ref['missing_in_revstream'])}")
    print(f"Events with date mismatches: {len(cross_ref['date_mismatches'])}")
    print()
    
    if cross_ref['missing_in_revstream']:
        print("Missing Events (first 10):")
        for i, missing in enumerate(cross_ref['missing_in_revstream'][:10]):
            print(f"\n  {i+1}. Date: {missing['date']}")
            print(f"     Event: {missing['event'][:100]}")
            if missing.get('significance'):
                print(f"     Significance: {missing['significance'][:100]}")
    
    print("\n" + "=" * 80)
    print("2. ENTITY COVERAGE ANALYSIS")
    print("-" * 80)
    missing_entities = identify_new_entities(evidence_events, entities_data)
    print(f"Entities mentioned in evidence timeline: {len(missing_entities)}")
    if missing_entities:
        print("\nPotentially missing entities:")
        for ent in sorted(missing_entities)[:20]:
            print(f"  - {ent}")
    
    print("\n" + "=" * 80)
    print("3. TEMPORAL COVERAGE ANALYSIS")
    print("-" * 80)
    coverage = analyze_event_coverage(events_data.get('events', []))
    if coverage:
        print(f"Earliest event: {coverage['earliest_event']}")
        print(f"Latest event: {coverage['latest_event']}")
        print(f"Total span: {coverage['total_span_days']} days")
        print(f"Total events: {coverage['total_events']}")
        
        if coverage.get('significant_gaps'):
            print(f"\nSignificant temporal gaps (>90 days): {len(coverage['significant_gaps'])}")
            for gap in coverage['significant_gaps'][:5]:
                print(f"  - {gap['start_date']} to {gap['end_date']}: {gap['gap_days']} days")
    
    print("\n" + "=" * 80)
    print("CROSS-REFERENCE COMPLETE")
    print("=" * 80)
    
    # Save results
    results = {
        'cross_reference': cross_ref,
        'missing_entities': missing_entities,
        'temporal_coverage': coverage,
        'timestamp': datetime.now().isoformat()
    }
    
    output_file = '/home/ubuntu/revstream1/cross_reference_analysis.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nDetailed results saved to: {output_file}")

if __name__ == '__main__':
    main()
