#!/usr/bin/env python3
"""
Timeline Analysis and Improvements - November 21, 2025
Analyze timeline events and suggest improvements based on patterns and gaps
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def analyze_timeline_gaps(timeline_data, events_data):
    """Analyze gaps in timeline coverage"""
    gaps = []
    
    # Create event lookup
    event_lookup = {}
    for event in events_data.get('events', []):
        event_lookup[event.get('event_id')] = event
    
    # Analyze each phase
    for phase_key, phase_data in sorted(timeline_data.get('timeline_phases', {}).items()):
        phase_id = phase_data.get('phase_id')
        phase_name = phase_data.get('phase_name')
        phase_events = phase_data.get('events', [])
        
        # Check for missing financial impact
        if phase_data.get('financial_impact') == 'unknown_amount':
            gaps.append({
                'type': 'missing_financial_impact',
                'phase': phase_id,
                'phase_name': phase_name,
                'recommendation': 'Calculate or estimate financial impact based on events in this phase'
            })
        
        # Check for phases with very few events
        if len(phase_events) < 3 and phase_id not in ['PHASE_007']:
            gaps.append({
                'type': 'sparse_phase',
                'phase': phase_id,
                'phase_name': phase_name,
                'event_count': len(phase_events),
                'recommendation': 'Review if additional events should be mapped to this phase'
            })
    
    return gaps

def analyze_event_patterns(events_data):
    """Analyze patterns in events"""
    patterns = {
        'by_category': defaultdict(list),
        'by_phase': defaultdict(list),
        'by_application': defaultdict(list),
        'financial_events': [],
        'non_financial_events': [],
        'evidence_rich_events': [],
        'evidence_sparse_events': []
    }
    
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        category = event.get('category', 'uncategorized')
        phase = event.get('timeline_phase', 'UNKNOWN')
        
        patterns['by_category'][category].append(event_id)
        patterns['by_phase'][phase].append(event_id)
        
        # Application mapping
        for app in event.get('related_applications', []):
            patterns['by_application'][app].append(event_id)
        
        # Financial impact
        if event.get('financial_impact'):
            patterns['financial_events'].append(event_id)
        else:
            patterns['non_financial_events'].append(event_id)
        
        # Evidence richness
        evidence_count = len(event.get('evidence_files', []))
        if evidence_count >= 10:
            patterns['evidence_rich_events'].append(event_id)
        elif evidence_count < 3:
            patterns['evidence_sparse_events'].append(event_id)
    
    return patterns

def generate_timeline_improvements(timeline_data, events_data, patterns, gaps):
    """Generate specific improvement recommendations"""
    improvements = {
        'critical': [],
        'important': [],
        'suggested': [],
        'statistics': {}
    }
    
    # Critical: Timeline gaps
    for gap in gaps:
        if gap['type'] == 'missing_financial_impact':
            improvements['critical'].append({
                'area': 'Timeline Phases',
                'issue': f"Phase {gap['phase']} ({gap['phase_name']}) has unknown financial impact",
                'recommendation': gap['recommendation'],
                'priority': 'high'
            })
    
    # Important: Event distribution
    if len(patterns['by_phase'].get('UNKNOWN', [])) > 0:
        improvements['important'].append({
            'area': 'Event Mapping',
            'issue': f"{len(patterns['by_phase']['UNKNOWN'])} events not mapped to timeline phases",
            'recommendation': 'Map all events to appropriate timeline phases',
            'affected_events': patterns['by_phase']['UNKNOWN'][:10],
            'priority': 'high'
        })
    
    # Important: Application coverage
    for app in ['APPLICATION_1', 'APPLICATION_2', 'APPLICATION_3']:
        app_events = patterns['by_application'].get(app, [])
        if len(app_events) < 15:
            improvements['important'].append({
                'area': 'Application Mapping',
                'issue': f"{app} has only {len(app_events)} events mapped",
                'recommendation': f'Review and map additional relevant events to {app}',
                'priority': 'medium'
            })
    
    # Suggested: Evidence enhancement
    if len(patterns['evidence_sparse_events']) > 0:
        improvements['suggested'].append({
            'area': 'Evidence Documentation',
            'issue': f"{len(patterns['evidence_sparse_events'])} events have sparse evidence files (<3)",
            'recommendation': 'Enhance evidence_files arrays with references from ad-res-j7 repository',
            'sample_events': patterns['evidence_sparse_events'][:5],
            'priority': 'low'
        })
    
    # Statistics
    improvements['statistics'] = {
        'total_events': len(events_data.get('events', [])),
        'events_by_category': {k: len(v) for k, v in patterns['by_category'].items()},
        'events_by_phase': {k: len(v) for k, v in patterns['by_phase'].items()},
        'events_by_application': {k: len(v) for k, v in patterns['by_application'].items()},
        'financial_events': len(patterns['financial_events']),
        'non_financial_events': len(patterns['non_financial_events']),
        'evidence_rich_events': len(patterns['evidence_rich_events']),
        'evidence_sparse_events': len(patterns['evidence_sparse_events'])
    }
    
    return improvements

def generate_timeline_enhancements(timeline_data, events_data):
    """Generate enhanced timeline with additional metadata"""
    enhanced_timeline = timeline_data.copy()
    
    # Create event lookup
    event_lookup = {}
    for event in events_data.get('events', []):
        event_lookup[event.get('event_id')] = event
    
    # Enhance each phase
    for phase_key, phase_data in enhanced_timeline.get('timeline_phases', {}).items():
        phase_events = phase_data.get('events', [])
        
        # Calculate category distribution
        category_dist = defaultdict(int)
        application_dist = defaultdict(int)
        total_evidence_files = 0
        
        for event_id in phase_events:
            event = event_lookup.get(event_id)
            if event:
                category = event.get('category', 'uncategorized')
                category_dist[category] += 1
                
                for app in event.get('related_applications', []):
                    application_dist[app] += 1
                
                total_evidence_files += len(event.get('evidence_files', []))
        
        # Add enhanced metadata
        phase_data['category_distribution'] = dict(category_dist)
        phase_data['application_distribution'] = dict(application_dist)
        phase_data['total_evidence_files'] = total_evidence_files
        phase_data['average_evidence_per_event'] = round(total_evidence_files / len(phase_events), 2) if phase_events else 0
    
    return enhanced_timeline

def main():
    """Main analysis function"""
    base_dir = '/home/ubuntu/revstream1/data_models'
    
    # Load latest refined data models
    events_file = os.path.join(base_dir, 'events/events_refined_2025_11_21_v9.json')
    timeline_file = os.path.join(base_dir, 'timelines/timeline_refined_2025_11_21_v7.json')
    
    print("Loading data models...")
    events_data = load_json(events_file)
    timeline_data = load_json(timeline_file)
    
    print("Analyzing timeline gaps...")
    gaps = analyze_timeline_gaps(timeline_data, events_data)
    
    print("Analyzing event patterns...")
    patterns = analyze_event_patterns(events_data)
    
    print("Generating improvement recommendations...")
    improvements = generate_timeline_improvements(timeline_data, events_data, patterns, gaps)
    
    print("Generating enhanced timeline...")
    enhanced_timeline = generate_timeline_enhancements(timeline_data, events_data)
    
    # Save outputs
    print("\nSaving analysis outputs...")
    
    improvements_file = '/home/ubuntu/revstream1/TIMELINE_IMPROVEMENTS_2025_11_21.json'
    save_json(improvements, improvements_file)
    
    enhanced_timeline_file = os.path.join(base_dir, 'timelines/timeline_enhanced_2025_11_21.json')
    save_json(enhanced_timeline, enhanced_timeline_file)
    
    patterns_file = '/home/ubuntu/revstream1/EVENT_PATTERNS_2025_11_21.json'
    # Convert defaultdict to dict for JSON serialization
    patterns_serializable = {
        'by_category': dict(patterns['by_category']),
        'by_phase': dict(patterns['by_phase']),
        'by_application': dict(patterns['by_application']),
        'financial_events': patterns['financial_events'],
        'non_financial_events': patterns['non_financial_events'],
        'evidence_rich_events': patterns['evidence_rich_events'],
        'evidence_sparse_events': patterns['evidence_sparse_events']
    }
    save_json(patterns_serializable, patterns_file)
    
    print("\n✓ Timeline analysis complete!")
    print(f"\nFiles created:")
    print(f"  - TIMELINE_IMPROVEMENTS_2025_11_21.json")
    print(f"  - EVENT_PATTERNS_2025_11_21.json")
    print(f"  - timelines/timeline_enhanced_2025_11_21.json")
    
    print(f"\nSummary:")
    print(f"  Critical Issues: {len(improvements['critical'])}")
    print(f"  Important Issues: {len(improvements['important'])}")
    print(f"  Suggested Improvements: {len(improvements['suggested'])}")
    print(f"  Total Events: {improvements['statistics']['total_events']}")
    print(f"  Events with Financial Impact: {improvements['statistics']['financial_events']}")
    print(f"  Evidence-Rich Events: {improvements['statistics']['evidence_rich_events']}")

if __name__ == '__main__':
    main()
