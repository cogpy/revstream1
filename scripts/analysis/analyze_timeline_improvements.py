#!/usr/bin/env python3
"""
Analyze timeline events and suggest improvements based on evidence
"""
import json
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def analyze_timeline(timeline_file, entities_file):
    """Analyze timeline and suggest improvements"""
    
    timeline_data = load_json(timeline_file)
    entities_data = load_json(entities_file)
    
    analysis = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'timeline_version': timeline_data['metadata']['version'],
            'entities_version': entities_data['metadata']['version']
        },
        'statistics': {
            'total_events': len(timeline_data.get('timeline', [])),
            'events_by_type': defaultdict(int),
            'events_by_phase': defaultdict(int),
            'events_with_evidence': 0,
            'events_without_evidence': 0,
            'criminal_threshold_events': 0,
            'civil_threshold_events': 0
        },
        'gaps': [],
        'improvements': [],
        'critical_events': []
    }
    
    # Analyze timeline entries
    events_without_evidence = []
    critical_events = []
    
    for entry in timeline_data.get('timeline', []):
        event_type = entry.get('event_type', 'unknown')
        phase = entry.get('phase', 'UNKNOWN')
        
        analysis['statistics']['events_by_type'][event_type] += 1
        analysis['statistics']['events_by_phase'][phase] += 1
        
        # Check for evidence
        has_evidence = (
            'ad_res_j7_evidence_enhanced' in entry or
            'ad_res_j7_references' in entry or
            'evidence' in entry
        )
        
        if has_evidence:
            analysis['statistics']['events_with_evidence'] += 1
        else:
            analysis['statistics']['events_without_evidence'] += 1
            events_without_evidence.append({
                'entry_id': entry.get('entry_id', entry.get('event_id', 'unknown')),
                'date': entry.get('date', 'unknown'),
                'title': entry.get('title', entry.get('event', 'unknown'))
            })
        
        # Check burden of proof
        burden = entry.get('burden_of_proof', entry.get('burden_of_proof_verified', ''))
        if 'criminal' in burden or '95%' in burden:
            analysis['statistics']['criminal_threshold_events'] += 1
        elif 'civil' in burden or '50%' in burden:
            analysis['statistics']['civil_threshold_events'] += 1
        
        # Identify critical events (high financial impact or criminal threshold)
        financial_impact = entry.get('financial_impact', 0)
        if isinstance(financial_impact, str):
            # Try to extract numeric value
            import re
            match = re.search(r'R?(\d+(?:,\d+)*(?:\.\d+)?)', str(financial_impact))
            if match:
                financial_impact = float(match.group(1).replace(',', ''))
            else:
                financial_impact = 0
        
        if financial_impact > 100000 or 'criminal' in burden:
            critical_events.append({
                'entry_id': entry.get('entry_id', entry.get('event_id', 'unknown')),
                'date': entry.get('date', 'unknown'),
                'title': entry.get('title', entry.get('event', 'unknown')),
                'financial_impact': financial_impact,
                'burden_of_proof': burden,
                'perpetrators': entry.get('perpetrators', [])
            })
    
    # Convert defaultdict to regular dict
    analysis['statistics']['events_by_type'] = dict(analysis['statistics']['events_by_type'])
    analysis['statistics']['events_by_phase'] = dict(analysis['statistics']['events_by_phase'])
    
    # Identify gaps
    if events_without_evidence:
        analysis['gaps'].append({
            'gap_type': 'missing_evidence_references',
            'count': len(events_without_evidence),
            'events': events_without_evidence[:10]  # First 10 examples
        })
    
    # Suggest improvements
    analysis['improvements'] = [
        {
            'improvement_type': 'evidence_enhancement',
            'priority': 'high',
            'description': f'Add evidence references to {len(events_without_evidence)} events without evidence',
            'action': 'Cross-reference with ad-res-j7 ANNEXURES and add specific evidence paths'
        },
        {
            'improvement_type': 'burden_of_proof_classification',
            'priority': 'high',
            'description': 'Classify all events by burden of proof standard (civil 50% vs criminal 95%)',
            'action': 'Review each event and assign appropriate burden_of_proof field'
        },
        {
            'improvement_type': 'phase_classification',
            'priority': 'medium',
            'description': 'Ensure all events are properly classified into phases (PHASE_1, PHASE_2, PHASE_3)',
            'action': 'Review timeline and assign phase based on chronology and fraud pattern'
        },
        {
            'improvement_type': 'perpetrator_linking',
            'priority': 'high',
            'description': 'Link all events to specific perpetrators from entities model',
            'action': 'Add perpetrators field with entity IDs (PERSON_001, PERSON_002, etc.)'
        },
        {
            'improvement_type': 'financial_impact_quantification',
            'priority': 'high',
            'description': 'Quantify financial impact for all fraud events',
            'action': 'Add or update financial_impact field with specific amounts from evidence'
        }
    ]
    
    # Store critical events
    analysis['critical_events'] = sorted(critical_events, key=lambda x: x.get('financial_impact', 0), reverse=True)[:20]
    
    return analysis

def generate_timeline_improvements_report(analysis, output_file):
    """Generate a markdown report of timeline improvements"""
    
    report = f"""# Timeline Analysis and Improvement Report

**Analysis Date:** {analysis['metadata']['analysis_date']}
**Timeline Version:** {analysis['metadata']['timeline_version']}
**Entities Version:** {analysis['metadata']['entities_version']}

---

## Executive Summary

### Statistics

- **Total Events:** {analysis['statistics']['total_events']}
- **Events with Evidence:** {analysis['statistics']['events_with_evidence']}
- **Events without Evidence:** {analysis['statistics']['events_without_evidence']}
- **Criminal Threshold Events (95%):** {analysis['statistics']['criminal_threshold_events']}
- **Civil Threshold Events (50%):** {analysis['statistics']['civil_threshold_events']}

### Events by Phase

"""
    
    for phase, count in sorted(analysis['statistics']['events_by_phase'].items()):
        report += f"- **{phase}:** {count} events\n"
    
    report += "\n### Events by Type\n\n"
    
    for event_type, count in sorted(analysis['statistics']['events_by_type'].items(), key=lambda x: x[1], reverse=True)[:10]:
        report += f"- **{event_type}:** {count} events\n"
    
    report += "\n---\n\n## Critical Events (Top 20 by Financial Impact)\n\n"
    
    for i, event in enumerate(analysis['critical_events'], 1):
        report += f"### {i}. {event['title']}\n\n"
        report += f"- **Date:** {event['date']}\n"
        report += f"- **Entry ID:** {event['entry_id']}\n"
        report += f"- **Financial Impact:** R{event['financial_impact']:,.2f}\n"
        report += f"- **Burden of Proof:** {event['burden_of_proof']}\n"
        report += f"- **Perpetrators:** {', '.join(event['perpetrators'])}\n\n"
    
    report += "---\n\n## Identified Gaps\n\n"
    
    for gap in analysis['gaps']:
        report += f"### {gap['gap_type'].replace('_', ' ').title()}\n\n"
        report += f"**Count:** {gap['count']}\n\n"
        if 'events' in gap:
            report += "**Sample Events:**\n\n"
            for event in gap['events']:
                report += f"- {event['date']}: {event['title']} (ID: {event['entry_id']})\n"
        report += "\n"
    
    report += "---\n\n## Recommended Improvements\n\n"
    
    for i, improvement in enumerate(analysis['improvements'], 1):
        report += f"### {i}. {improvement['improvement_type'].replace('_', ' ').title()}\n\n"
        report += f"**Priority:** {improvement['priority'].upper()}\n\n"
        report += f"**Description:** {improvement['description']}\n\n"
        report += f"**Action:** {improvement['action']}\n\n"
    
    report += "---\n\n## Next Steps\n\n"
    report += "1. Address high-priority improvements first\n"
    report += "2. Cross-reference all events with ad-res-j7 evidence\n"
    report += "3. Ensure all criminal threshold events (95%) have conclusive evidence\n"
    report += "4. Update GitHub Pages documentation with enhanced timeline\n"
    report += "5. Refine legal filings based on improved timeline evidence\n"
    
    with open(output_file, 'w') as f:
        f.write(report)
    
    return report

if __name__ == '__main__':
    timeline_file = '/home/ubuntu/revstream1/data_models/timelines/timeline.json'
    entities_file = '/home/ubuntu/revstream1/data_models/entities/entities.json'
    
    analysis = analyze_timeline(timeline_file, entities_file)
    
    # Save analysis as JSON
    save_json('/home/ubuntu/revstream1/TIMELINE_ANALYSIS_2026_01_14.json', analysis)
    print("Timeline analysis saved to TIMELINE_ANALYSIS_2026_01_14.json")
    
    # Generate markdown report
    report = generate_timeline_improvements_report(
        analysis,
        '/home/ubuntu/revstream1/TIMELINE_IMPROVEMENTS_REPORT_2026_01_14.md'
    )
    print("Timeline improvements report saved to TIMELINE_IMPROVEMENTS_REPORT_2026_01_14.md")
    
    print(f"\nTotal Events: {analysis['statistics']['total_events']}")
    print(f"Events with Evidence: {analysis['statistics']['events_with_evidence']}")
    print(f"Events without Evidence: {analysis['statistics']['events_without_evidence']}")
    print(f"Criminal Threshold Events: {analysis['statistics']['criminal_threshold_events']}")
    print(f"Critical Events Identified: {len(analysis['critical_events'])}")
