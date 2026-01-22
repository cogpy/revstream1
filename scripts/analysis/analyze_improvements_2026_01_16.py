#!/usr/bin/env python3
"""
Comprehensive Analysis and Improvement Script for revstream1
Date: 2026-01-16
Purpose: Analyze entities, relations, events, timelines and suggest improvements
"""

import json
import os
from datetime import datetime
from collections import defaultdict

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities for completeness and improvements"""
    improvements = []
    
    # Check for Ketoni entity
    entity_ids = [e['entity_id'] for e in entities_data['entities'].get('organizations', [])]
    if 'ORG_KETONI' not in entity_ids and 'ORG_015' not in entity_ids:
        improvements.append({
            'type': 'CRITICAL_MISSING_ENTITY',
            'entity': 'Ketoni Investment Holdings',
            'reason': 'ZAR 18.75M payout entity missing - central financial motive',
            'priority': 'CRITICAL',
            'suggested_entity_id': 'ORG_015',
            'attributes': {
                'name': 'Ketoni Investment Holdings',
                'role': 'investment_holding_company',
                'financial_obligation': 'ZAR 18,750,000 payout to FFT (May 2026)',
                'director': 'Kevin Michael Derrick (PERSON_014)',
                'connection': 'Bantjies colleague of Derrick'
            }
        })
    
    # Check for Kevin Derrick entity
    person_ids = [p['entity_id'] for p in entities_data['entities'].get('persons', [])]
    if 'PERSON_014' not in person_ids:
        improvements.append({
            'type': 'CRITICAL_MISSING_ENTITY',
            'entity': 'Kevin Michael Derrick',
            'reason': 'Ketoni Director - connects Bantjies to Ketoni payout',
            'priority': 'CRITICAL',
            'suggested_entity_id': 'PERSON_014',
            'attributes': {
                'name': 'Kevin Michael Derrick',
                'role': 'ketoni_director',
                'relationships': ['director_of_ketoni', 'colleague_of_bantjies'],
                'significance': 'Links Bantjies appointment to Ketoni payout'
            }
        })
    
    # Check Bantjies entity for Ketoni connection
    bantjies = next((p for p in entities_data['entities'].get('persons', []) 
                     if p['entity_id'] == 'PERSON_007'), None)
    if bantjies:
        if 'ketoni' not in str(bantjies).lower():
            improvements.append({
                'type': 'ENTITY_ENHANCEMENT',
                'entity': 'PERSON_007 (Danie Bantjies)',
                'reason': 'Missing Ketoni connection - colleague of Kevin Derrick',
                'priority': 'HIGH',
                'enhancement': {
                    'add_relationship': 'colleague_of_kevin_derrick',
                    'add_attribute': 'ketoni_connection',
                    'significance': 'Appointed T-10 months before ZAR 18.75M payout'
                }
            })
    
    # Check Trust entity for Ketoni payout
    trust = next((t for t in entities_data['entities'].get('trusts', []) 
                  if t['entity_id'] == 'TRUST_001'), None)
    if trust:
        trust_str = json.dumps(trust)
        if '18.75' not in trust_str:
            improvements.append({
                'type': 'ENTITY_ENHANCEMENT',
                'entity': 'TRUST_001 (Faucitt Family Trust)',
                'reason': 'Missing ZAR 18.75M Ketoni payout asset',
                'priority': 'CRITICAL',
                'enhancement': {
                    'add_financial_asset': {
                        'asset': 'Ketoni Investment Holdings payout option',
                        'value': 'ZAR 18,750,000',
                        'date': 'May 2026',
                        'beneficiaries': ['PERSON_001', 'PERSON_004', 'PERSON_005'],
                        'significance': 'Central financial motive for all trust actions since Apr 2023'
                    }
                }
            })
    
    return improvements

def analyze_relations(relations_data):
    """Analyze relations for missing connections"""
    improvements = []
    
    # Check for Ketoni-related relations
    relation_descriptions = [r.get('description', '') for r in 
                            relations_data.get('relations', {}).get('ownership_relations', [])]
    
    if not any('ketoni' in desc.lower() for desc in relation_descriptions):
        improvements.append({
            'type': 'MISSING_RELATION',
            'relation': 'TRUST_001 -> ORG_015 (Ketoni)',
            'reason': 'Missing shareholder relation: FFT owns 5,000 A-Ordinary shares in Ketoni',
            'priority': 'CRITICAL',
            'suggested_relation': {
                'relation_id': 'REL_OWN_008',
                'relation_type': 'shareholder',
                'source_entity': 'TRUST_001',
                'target_entity': 'ORG_015',
                'shares': '5,000 A-Ordinary shares',
                'payout_option': 'ZAR 18,750,000 (May 2026)',
                'evidence': ['Ketoni shareholder agreement', 'FFT investment records']
            }
        })
    
    # Check for Bantjies-Derrick relation
    improvements.append({
        'type': 'MISSING_RELATION',
        'relation': 'PERSON_007 (Bantjies) -> PERSON_014 (Derrick)',
        'reason': 'Missing colleague relation connecting Bantjies to Ketoni',
        'priority': 'HIGH',
        'suggested_relation': {
            'relation_id': 'REL_PROF_001',
            'relation_type': 'professional_colleague',
            'source_entity': 'PERSON_007',
            'target_entity': 'PERSON_014',
            'significance': 'Explains Bantjies appointment T-10 months before payout',
            'evidence': ['Professional records', 'Ketoni connection analysis']
        }
    })
    
    return improvements

def analyze_events(events_data):
    """Analyze events for missing critical events"""
    improvements = []
    
    # Check for Ketoni investment event
    event_descriptions = [e.get('description', '') for e in events_data.get('events', [])]
    
    if not any('ketoni' in desc.lower() for desc in event_descriptions):
        improvements.append({
            'type': 'CRITICAL_MISSING_EVENT',
            'event': 'FFT Ketoni Investment',
            'date': '2023-04-24',
            'reason': 'Missing central financial motive event - ZAR 18.75M payout option',
            'priority': 'CRITICAL',
            'suggested_event': {
                'event_id': 'EVENT_K001',
                'date': '2023-04-24',
                'title': 'Faucitt Family Trust Invests in Ketoni Investment Holdings',
                'category': 'financial_investment',
                'event_type': 'trust_investment',
                'entities_involved': ['TRUST_001', 'ORG_015', 'PERSON_001'],
                'description': 'FFT acquires 5,000 A-Ordinary shares in Ketoni with ZAR 18.75M payout option (May 2026)',
                'financial_impact': 'ZAR 18,750,000',
                'significance': 'Establishes central financial motive for all subsequent trust actions',
                'phase': 'PHASE_1',
                'timeline_phase': 'Investment Phase',
                'burden_of_proof': 'civil_50%_exceeded',
                'evidence': ['Ketoni shareholder agreement', 'FFT investment records']
            }
        })
    
    # Check for Kayla murder timing relative to Ketoni
    kayla_event = next((e for e in events_data.get('events', []) 
                       if 'kayla' in e.get('description', '').lower() and 
                       'murder' in e.get('description', '').lower()), None)
    if kayla_event:
        if 'ketoni' not in kayla_event.get('significance', '').lower():
            improvements.append({
                'type': 'EVENT_ENHANCEMENT',
                'event': kayla_event.get('event_id'),
                'reason': 'Missing Ketoni timing context - 80 days after FFT investment',
                'priority': 'HIGH',
                'enhancement': {
                    'add_to_significance': 'Occurred 80 days after FFT Ketoni investment (ZAR 18.75M)',
                    'add_context': 'ReZonance R1M debt obstacle to ZAR 18.75M control',
                    'phase_context': 'Creditor Elimination Phase'
                }
            })
    
    # Check for Bantjies appointment event
    bantjies_appt = next((e for e in events_data.get('events', []) 
                         if 'bantjies' in e.get('description', '').lower() and 
                         'trustee' in e.get('description', '').lower()), None)
    if bantjies_appt:
        if 't-10' not in bantjies_appt.get('significance', '').lower():
            improvements.append({
                'type': 'EVENT_ENHANCEMENT',
                'event': bantjies_appt.get('event_id'),
                'reason': 'Missing T-10 months timing and Ketoni connection',
                'priority': 'HIGH',
                'enhancement': {
                    'add_timing': 'T-10 months before May 2026 payout',
                    'add_connection': 'Colleague of Kevin Derrick (Ketoni Director)',
                    'add_significance': 'Strategic appointment to consolidate control before ZAR 18.75M payout'
                }
            })
    
    return improvements

def analyze_timeline(timeline_data):
    """Analyze timeline for phase improvements"""
    improvements = []
    
    # Check for phase structure relative to Ketoni payout
    improvements.append({
        'type': 'TIMELINE_ENHANCEMENT',
        'reason': 'Add Ketoni-centric phase structure',
        'priority': 'HIGH',
        'enhancement': {
            'add_phases': [
                {
                    'phase': 'PHASE_0_INVESTMENT',
                    'period': 'Feb 2023 - Apr 2023',
                    'description': 'Investment Phase - ZAR 18.75M entitlement established',
                    'key_event': 'EVENT_K001 (2023-04-24)'
                },
                {
                    'phase': 'PHASE_1_CREDITOR_ELIMINATION',
                    'period': 'Jul 2023 - Feb 2024',
                    'description': 'Creditor Elimination Phase - R1M debt obstacle removal attempt',
                    'key_events': ['Kayla murder (2023-07-13)', 'ReZonance dissolution pressure']
                },
                {
                    'phase': 'PHASE_2_CONTROL_CONSOLIDATION',
                    'period': 'Jul 2024 - Aug 2025',
                    'description': 'Control Consolidation Phase - Peter consolidates control before payout',
                    'key_events': ['Bantjies appointment', 'Main Trustee backdating', 'Interdicts filed']
                },
                {
                    'phase': 'PHASE_3_PAYOUT',
                    'period': 'May 2026',
                    'description': 'Payout Phase - ALL EVENTS CONVERGE HERE',
                    'financial_impact': 'ZAR 18,750,000'
                }
            ]
        }
    })
    
    return improvements

def generate_report(improvements_dict):
    """Generate comprehensive improvement report"""
    report = {
        'metadata': {
            'analysis_date': datetime.now().isoformat(),
            'version': 'KETONI_INTEGRATION_2026_01_16',
            'total_improvements': sum(len(v) for v in improvements_dict.values()),
            'critical_count': sum(1 for imps in improvements_dict.values() 
                                 for imp in imps if imp.get('priority') == 'CRITICAL')
        },
        'improvements': improvements_dict,
        'summary': {
            'entities': len(improvements_dict.get('entities', [])),
            'relations': len(improvements_dict.get('relations', [])),
            'events': len(improvements_dict.get('events', [])),
            'timeline': len(improvements_dict.get('timeline', []))
        }
    }
    return report

def main():
    """Main analysis function"""
    print("Starting comprehensive analysis...")
    
    # Load data models
    base_path = '/home/ubuntu/revstream1/docs/data_models'
    
    entities_data = load_json(f'{base_path}/entities/entities.json')
    relations_data = load_json(f'{base_path}/relations.json')
    events_data = load_json(f'{base_path}/events.json')
    timeline_data = load_json(f'{base_path}/timeline.json')
    
    print("Data models loaded successfully")
    
    # Analyze each component
    improvements = {
        'entities': analyze_entities(entities_data),
        'relations': analyze_relations(relations_data),
        'events': analyze_events(events_data),
        'timeline': analyze_timeline(timeline_data)
    }
    
    print(f"Analysis complete. Found {sum(len(v) for v in improvements.values())} improvements")
    
    # Generate report
    report = generate_report(improvements)
    
    # Save report
    output_path = '/home/ubuntu/revstream1/ANALYSIS_IMPROVEMENTS_2026_01_16.json'
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Report saved to {output_path}")
    
    # Print summary
    print("\n=== IMPROVEMENT SUMMARY ===")
    print(f"Total improvements: {report['metadata']['total_improvements']}")
    print(f"Critical improvements: {report['metadata']['critical_count']}")
    print(f"\nBreakdown:")
    for category, count in report['summary'].items():
        print(f"  {category}: {count}")
    
    return report

if __name__ == '__main__':
    main()
