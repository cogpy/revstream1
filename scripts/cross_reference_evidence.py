#!/usr/bin/env python3.11
"""
Cross-reference evidence from ad-res-j7 with entities and events in revstream1
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def scan_evidence_directory(base_path):
    """Scan ad-res-j7 for evidence files"""
    evidence_map = defaultdict(list)
    
    # Key directories to scan
    key_dirs = [
        'ANNEXURES',
        'evidence',
        'case_2025_137857',
        'FINAL_AFFIDAVIT_PACKAGE'
    ]
    
    for key_dir in key_dirs:
        dir_path = base_path / key_dir
        if dir_path.exists():
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(base_path)
                    
                    # Categorize by file type
                    ext = file_path.suffix.lower()
                    evidence_map[ext].append(str(rel_path))
    
    return evidence_map

def analyze_bank_accounts(entities_data, evidence_map):
    """Analyze bank account entities and suggest event links"""
    print("\n" + "="*80)
    print("BANK ACCOUNT ANALYSIS")
    print("="*80)
    
    bank_accounts = entities_data.get('entities', {}).get('bank_accounts', [])
    
    print(f"\nFound {len(bank_accounts)} bank account entities")
    
    # Look for bank statement evidence
    bank_evidence = [f for f in evidence_map.get('.pdf', []) if 'bank' in f.lower() or 'statement' in f.lower()]
    
    print(f"\nFound {len(bank_evidence)} potential bank-related evidence files:")
    for i, evidence in enumerate(bank_evidence[:10], 1):
        print(f"  {i}. {evidence}")
    
    improvements = []
    for account in bank_accounts:
        account_id = account.get('entity_id')
        account_name = account.get('name', 'Unknown')
        
        improvements.append({
            'entity_id': account_id,
            'entity_name': account_name,
            'issue': 'No linked events',
            'suggested_action': 'Link to payment redirection events, unauthorized transfers',
            'evidence_files': bank_evidence[:5]
        })
    
    return improvements

def analyze_entity_evidence_gaps(entities_data, ad_res_j7_path):
    """Find entities with missing or incomplete evidence links"""
    print("\n" + "="*80)
    print("ENTITY EVIDENCE GAP ANALYSIS")
    print("="*80)
    
    gaps = []
    entities = entities_data.get('entities', {})
    
    for category, entity_list in entities.items():
        for entity in entity_list:
            entity_id = entity.get('entity_id')
            name = entity.get('name', 'Unknown')
            evidence_files = entity.get('evidence_files', [])
            
            if not evidence_files:
                gaps.append({
                    'entity_id': entity_id,
                    'entity_name': name,
                    'category': category,
                    'issue': 'No evidence files linked',
                    'priority': 'HIGH'
                })
            elif len(evidence_files) < 3:
                gaps.append({
                    'entity_id': entity_id,
                    'entity_name': name,
                    'category': category,
                    'issue': f'Only {len(evidence_files)} evidence file(s) linked',
                    'priority': 'MEDIUM'
                })
    
    print(f"\nFound {len(gaps)} entities with evidence gaps")
    print("\n--- High Priority Gaps ---")
    for gap in [g for g in gaps if g['priority'] == 'HIGH'][:10]:
        print(f"  {gap['entity_id']} ({gap['entity_name']}): {gap['issue']}")
    
    return gaps

def analyze_event_evidence_quality(events_data, ad_res_j7_path):
    """Analyze quality and completeness of event evidence"""
    print("\n" + "="*80)
    print("EVENT EVIDENCE QUALITY ANALYSIS")
    print("="*80)
    
    events = events_data.get('events', [])
    
    # Categorize events by evidence quality
    no_evidence = []
    weak_evidence = []
    strong_evidence = []
    
    for event in events:
        event_id = event.get('event_id')
        title = event.get('title')
        evidence_files = event.get('evidence_files', [])
        
        if not evidence_files:
            no_evidence.append({'event_id': event_id, 'title': title})
        elif len(evidence_files) < 3:
            weak_evidence.append({'event_id': event_id, 'title': title, 'count': len(evidence_files)})
        else:
            strong_evidence.append({'event_id': event_id, 'title': title, 'count': len(evidence_files)})
    
    print(f"\nEvidence Quality Distribution:")
    print(f"  No Evidence: {len(no_evidence)} events")
    print(f"  Weak Evidence (1-2 files): {len(weak_evidence)} events")
    print(f"  Strong Evidence (3+ files): {len(strong_evidence)} events")
    
    if no_evidence:
        print(f"\n--- Events with No Evidence (showing first 10) ---")
        for event in no_evidence[:10]:
            print(f"  {event['event_id']}: {event['title']}")
    
    return {
        'no_evidence': no_evidence,
        'weak_evidence': weak_evidence,
        'strong_evidence': strong_evidence
    }

def suggest_timeline_improvements(events_data):
    """Suggest improvements to timeline organization"""
    print("\n" + "="*80)
    print("TIMELINE IMPROVEMENT SUGGESTIONS")
    print("="*80)
    
    events = events_data.get('events', [])
    
    # Check phase assignments
    unassigned_phases = []
    phase_distribution = defaultdict(list)
    
    for event in events:
        event_id = event.get('event_id')
        title = event.get('title')
        phase = event.get('timeline_phase', 'UNASSIGNED')
        date = event.get('date', 'NO_DATE')
        
        if phase == 'UNASSIGNED' or 'UNASSIGNED' in phase:
            unassigned_phases.append({'event_id': event_id, 'title': title, 'date': date})
        
        phase_distribution[phase].append(event_id)
    
    print(f"\nPhase Distribution:")
    for phase, events_list in sorted(phase_distribution.items()):
        print(f"  {phase}: {len(events_list)} events")
    
    if unassigned_phases:
        print(f"\n--- Unassigned Phase Events ({len(unassigned_phases)}) ---")
        for event in unassigned_phases[:10]:
            print(f"  {event['event_id']} ({event['date']}): {event['title']}")
    
    suggestions = []
    if unassigned_phases:
        suggestions.append({
            'issue': f'{len(unassigned_phases)} events have unassigned phases',
            'action': 'Review and assign appropriate timeline phases based on dates and context'
        })
    
    return suggestions

def generate_cross_reference_report(entities_data, events_data, relations_data, ad_res_j7_path):
    """Generate comprehensive cross-reference report"""
    print("\n" + "="*80)
    print("CROSS-REFERENCE ANALYSIS REPORT")
    print("Case 2025-137857: Revenue Stream Hijacking")
    print("="*80)
    
    # Scan evidence
    evidence_map = scan_evidence_directory(ad_res_j7_path)
    
    print(f"\n--- Evidence Repository Statistics ---")
    total_files = sum(len(files) for files in evidence_map.values())
    print(f"Total evidence files scanned: {total_files}")
    print(f"\nTop file types:")
    for ext, files in sorted(evidence_map.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
        print(f"  {ext}: {len(files)} files")
    
    # Run analyses
    bank_improvements = analyze_bank_accounts(entities_data, evidence_map)
    entity_gaps = analyze_entity_evidence_gaps(entities_data, ad_res_j7_path)
    event_quality = analyze_event_evidence_quality(events_data, ad_res_j7_path)
    timeline_suggestions = suggest_timeline_improvements(events_data)
    
    # Compile report
    report = {
        'analysis_date': '2025-12-05',
        'evidence_repository': str(ad_res_j7_path),
        'total_evidence_files': total_files,
        'bank_account_improvements': bank_improvements,
        'entity_evidence_gaps': entity_gaps,
        'event_evidence_quality': {
            'no_evidence_count': len(event_quality['no_evidence']),
            'weak_evidence_count': len(event_quality['weak_evidence']),
            'strong_evidence_count': len(event_quality['strong_evidence']),
            'no_evidence_events': event_quality['no_evidence'][:20]
        },
        'timeline_suggestions': timeline_suggestions,
        'recommendations': []
    }
    
    # Generate recommendations
    if bank_improvements:
        report['recommendations'].append({
            'priority': 'HIGH',
            'category': 'entities',
            'issue': f'{len(bank_improvements)} bank accounts have no linked events',
            'action': 'Link bank accounts to relevant payment redirection and transfer events'
        })
    
    if entity_gaps:
        high_priority_gaps = [g for g in entity_gaps if g['priority'] == 'HIGH']
        if high_priority_gaps:
            report['recommendations'].append({
                'priority': 'HIGH',
                'category': 'evidence',
                'issue': f'{len(high_priority_gaps)} entities have no evidence files',
                'action': 'Review ad-res-j7 repository and link relevant evidence files'
            })
    
    if event_quality['no_evidence']:
        report['recommendations'].append({
            'priority': 'MEDIUM',
            'category': 'evidence',
            'issue': f'{len(event_quality["no_evidence"])} events have no evidence files',
            'action': 'Link evidence files from ad-res-j7 repository to strengthen case'
        })
    
    return report

def main():
    """Main function"""
    revstream1_path = Path('/home/ubuntu/revstream1')
    ad_res_j7_path = Path('/home/ubuntu/ad-res-j7')
    
    # Load models
    entities_data = load_json(revstream1_path / 'data_models/entities/entities_refined_2025_12_04_v24.json')
    events_data = load_json(revstream1_path / 'data_models/events/events_refined_2025_12_04_v26.json')
    relations_data = load_json(revstream1_path / 'data_models/relations/relations_refined_2025_11_28_v20.json')
    
    # Generate report
    report = generate_cross_reference_report(entities_data, events_data, relations_data, ad_res_j7_path)
    
    # Save report
    output_path = revstream1_path / 'CROSS_REFERENCE_ANALYSIS_2025_12_05.json'
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"\nTotal Recommendations: {len(report['recommendations'])}")
    for rec in report['recommendations']:
        print(f"\n[{rec['priority']}] {rec['category'].upper()}")
        print(f"  Issue: {rec['issue']}")
        print(f"  Action: {rec['action']}")
    
    print(f"\n\nFull report saved to: {output_path}")

if __name__ == '__main__':
    main()
