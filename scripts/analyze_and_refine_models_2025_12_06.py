#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script for Revenue Stream Case Data Models
Date: 2025-12-06
Purpose: Analyze entities, relations, events, and timelines for gaps, inconsistencies, and improvements
"""

import json
import os
from datetime import datetime
from collections import defaultdict

# File paths
ENTITIES_FILE = "data_models/entities/entities_refined_2025_12_05_v25.json"
EVENTS_FILE = "data_models/events/events_refined_2025_12_05_v27.json"
RELATIONS_FILE = "data_models/relations/relations_refined_2025_12_05_v21.json"
TIMELINE_FILE = "data_models/timelines/timeline_refined_2025_12_05_v18.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entity data for gaps and improvements"""
    print("\n" + "="*80)
    print("ENTITY ANALYSIS")
    print("="*80)
    
    entities = entities_data.get('entities', {})
    issues = []
    suggestions = []
    
    # Analyze persons
    persons = entities.get('persons', [])
    print(f"\n✓ Total Persons: {len(persons)}")
    
    for person in persons:
        entity_id = person.get('entity_id')
        name = person.get('name')
        
        # Check for missing evidence
        if not person.get('evidence_files') or len(person.get('evidence_files', [])) == 0:
            issues.append(f"{entity_id} ({name}): Missing evidence files")
        
        # Check for missing timeline events
        if not person.get('timeline_events') or len(person.get('timeline_events', [])) == 0:
            issues.append(f"{entity_id} ({name}): No timeline events linked")
        
        # Check for missing financial impact
        if person.get('role') in ['primary_perpetrator', 'co_conspirator'] and not person.get('financial_impact'):
            suggestions.append(f"{entity_id} ({name}): Consider adding financial_impact details")
    
    # Analyze organizations
    orgs = entities.get('organizations', [])
    print(f"✓ Total Organizations: {len(orgs)}")
    
    for org in orgs:
        entity_id = org.get('entity_id')
        name = org.get('name')
        
        # Check for missing evidence
        if not org.get('evidence_files') or len(org.get('evidence_files', [])) == 0:
            issues.append(f"{entity_id} ({name}): Missing evidence files")
    
    # Analyze bank accounts
    bank_accounts = entities.get('bank_accounts', [])
    print(f"✓ Total Bank Accounts: {len(bank_accounts)}")
    
    for account in bank_accounts:
        entity_id = account.get('entity_id')
        account_number = account.get('account_number')
        
        # Check for missing control information
        if not account.get('controlled_by'):
            issues.append(f"{entity_id} ({account_number}): Missing controlled_by information")
        
        # Check for missing transaction data
        if not account.get('timeline_events') or len(account.get('timeline_events', [])) == 0:
            suggestions.append(f"{entity_id} ({account_number}): No timeline events linked")
    
    # Print issues
    if issues:
        print(f"\n⚠ Issues Found ({len(issues)}):")
        for issue in issues[:10]:
            print(f"  - {issue}")
        if len(issues) > 10:
            print(f"  ... and {len(issues) - 10} more")
    
    # Print suggestions
    if suggestions:
        print(f"\n💡 Suggestions ({len(suggestions)}):")
        for suggestion in suggestions[:10]:
            print(f"  - {suggestion}")
        if len(suggestions) > 10:
            print(f"  ... and {len(suggestions) - 10} more")
    
    return {
        'total_entities': len(persons) + len(orgs) + len(bank_accounts),
        'issues': issues,
        'suggestions': suggestions
    }

def analyze_events(events_data):
    """Analyze event data for gaps and improvements"""
    print("\n" + "="*80)
    print("EVENT ANALYSIS")
    print("="*80)
    
    events = events_data.get('events', [])
    print(f"\n✓ Total Events: {len(events)}")
    
    issues = []
    suggestions = []
    
    # Analyze phase distribution
    phase_counts = defaultdict(int)
    events_without_phase = []
    events_without_evidence = []
    events_without_entities = []
    events_without_financial_impact = []
    
    for event in events:
        event_id = event.get('event_id')
        
        # Check phase assignment
        phase = event.get('timeline_phase') or event.get('phase')
        if phase:
            phase_counts[phase] += 1
        else:
            events_without_phase.append(event_id)
        
        # Check evidence
        evidence = event.get('evidence') or event.get('evidence_files')
        if not evidence or len(evidence) == 0:
            events_without_evidence.append(event_id)
        
        # Check entity involvement
        entities = event.get('entities_involved') or event.get('perpetrators', [])
        if not entities or len(entities) == 0:
            events_without_entities.append(event_id)
        
        # Check financial impact
        if not event.get('financial_impact'):
            events_without_financial_impact.append(event_id)
    
    print(f"\n✓ Phase Distribution:")
    for phase, count in sorted(phase_counts.items()):
        print(f"  - {phase}: {count} events")
    
    if events_without_phase:
        issues.append(f"{len(events_without_phase)} events without phase assignment: {', '.join(events_without_phase[:5])}")
    
    if events_without_evidence:
        issues.append(f"{len(events_without_evidence)} events without evidence files")
    
    if events_without_entities:
        issues.append(f"{len(events_without_entities)} events without entity involvement")
    
    if events_without_financial_impact:
        suggestions.append(f"{len(events_without_financial_impact)} events without financial_impact (may be intentional)")
    
    # Print issues
    if issues:
        print(f"\n⚠ Issues Found ({len(issues)}):")
        for issue in issues:
            print(f"  - {issue}")
    
    # Print suggestions
    if suggestions:
        print(f"\n💡 Suggestions ({len(suggestions)}):")
        for suggestion in suggestions:
            print(f"  - {suggestion}")
    
    return {
        'total_events': len(events),
        'phase_distribution': dict(phase_counts),
        'issues': issues,
        'suggestions': suggestions
    }

def analyze_relations(relations_data):
    """Analyze relation data for gaps and improvements"""
    print("\n" + "="*80)
    print("RELATION ANALYSIS")
    print("="*80)
    
    relations = relations_data.get('relations', {})
    issues = []
    suggestions = []
    
    total_relations = 0
    relation_type_counts = defaultdict(int)
    
    for relation_type, relation_list in relations.items():
        count = len(relation_list)
        total_relations += count
        relation_type_counts[relation_type] = count
        
        # Check for missing evidence
        for relation in relation_list:
            if not relation.get('evidence') or len(relation.get('evidence', [])) == 0:
                rel_id = relation.get('relation_id', 'unknown')
                suggestions.append(f"{rel_id}: Missing evidence")
    
    print(f"\n✓ Total Relations: {total_relations}")
    print(f"✓ Relation Types: {len(relation_type_counts)}")
    
    print(f"\n✓ Relation Type Distribution:")
    for rel_type, count in sorted(relation_type_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {rel_type}: {count}")
    
    # Print suggestions
    if suggestions:
        print(f"\n💡 Suggestions ({len(suggestions)}):")
        for suggestion in suggestions[:10]:
            print(f"  - {suggestion}")
        if len(suggestions) > 10:
            print(f"  ... and {len(suggestions) - 10} more")
    
    return {
        'total_relations': total_relations,
        'relation_types': len(relation_type_counts),
        'issues': issues,
        'suggestions': suggestions
    }

def analyze_timeline(timeline_data):
    """Analyze timeline data for gaps and improvements"""
    print("\n" + "="*80)
    print("TIMELINE ANALYSIS")
    print("="*80)
    
    timeline = timeline_data.get('timeline', [])
    print(f"\n✓ Total Timeline Entries: {len(timeline)}")
    
    issues = []
    suggestions = []
    
    # Check for date gaps
    dates = []
    for entry in timeline:
        date_str = entry.get('date')
        if date_str:
            dates.append(date_str)
    
    dates.sort()
    if dates:
        print(f"✓ Timeline Span: {dates[0]} to {dates[-1]}")
    
    # Check for missing evidence in timeline entries
    entries_without_evidence = []
    for entry in timeline:
        event_id = entry.get('event_id')
        evidence = entry.get('evidence_files')
        if not evidence or len(evidence) == 0:
            entries_without_evidence.append(event_id)
    
    if entries_without_evidence:
        suggestions.append(f"{len(entries_without_evidence)} timeline entries without evidence files")
    
    # Print suggestions
    if suggestions:
        print(f"\n💡 Suggestions ({len(suggestions)}):")
        for suggestion in suggestions:
            print(f"  - {suggestion}")
    
    return {
        'total_entries': len(timeline),
        'date_span': f"{dates[0]} to {dates[-1]}" if dates else "N/A",
        'issues': issues,
        'suggestions': suggestions
    }

def generate_refinement_report(entity_analysis, event_analysis, relation_analysis, timeline_analysis):
    """Generate comprehensive refinement report"""
    report = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'version': '26.0',
            'purpose': 'Comprehensive data model analysis and refinement recommendations'
        },
        'summary': {
            'total_entities': entity_analysis['total_entities'],
            'total_events': event_analysis['total_events'],
            'total_relations': relation_analysis['total_relations'],
            'total_timeline_entries': timeline_analysis['total_entries']
        },
        'entity_analysis': entity_analysis,
        'event_analysis': event_analysis,
        'relation_analysis': relation_analysis,
        'timeline_analysis': timeline_analysis,
        'priority_improvements': []
    }
    
    # Identify priority improvements
    all_issues = (
        entity_analysis['issues'] + 
        event_analysis['issues'] + 
        relation_analysis['issues'] + 
        timeline_analysis['issues']
    )
    
    if all_issues:
        report['priority_improvements'] = all_issues[:20]
    
    return report

def main():
    """Main analysis function"""
    print("\n" + "="*80)
    print("REVENUE STREAM CASE - DATA MODEL ANALYSIS")
    print("Date: 2025-12-06")
    print("="*80)
    
    # Load data
    print("\nLoading data models...")
    entities_data = load_json(ENTITIES_FILE)
    events_data = load_json(EVENTS_FILE)
    relations_data = load_json(RELATIONS_FILE)
    timeline_data = load_json(TIMELINE_FILE)
    
    # Analyze each component
    entity_analysis = analyze_entities(entities_data)
    event_analysis = analyze_events(events_data)
    relation_analysis = analyze_relations(relations_data)
    timeline_analysis = analyze_timeline(timeline_data)
    
    # Generate report
    report = generate_refinement_report(
        entity_analysis, 
        event_analysis, 
        relation_analysis, 
        timeline_analysis
    )
    
    # Save report
    output_file = "ANALYSIS_REPORT_2025_12_06.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"\n✓ Report saved to: {output_file}")
    print(f"✓ Total Issues: {len(entity_analysis['issues']) + len(event_analysis['issues']) + len(relation_analysis['issues']) + len(timeline_analysis['issues'])}")
    print(f"✓ Total Suggestions: {len(entity_analysis['suggestions']) + len(event_analysis['suggestions']) + len(relation_analysis['suggestions']) + len(timeline_analysis['suggestions'])}")

if __name__ == "__main__":
    main()
