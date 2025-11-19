#!/usr/bin/env python3
"""
Refinement script for data models - fixes issues and enhances evidence references
Date: 2025-11-19
"""

import json
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def fix_person_012_events(entities_data):
    """Fix PERSON_012 (Jax) timeline events - remove non-existent events"""
    if 'entities' in entities_data and 'persons' in entities_data['entities']:
        for person in entities_data['entities']['persons']:
            if person.get('entity_id') == 'PERSON_012':
                # Remove non-existent events and replace with correct ones
                person['timeline_events'] = ['EVENT_027', 'EVENT_007']
                person['additional_notes'] = "Received email from Gee in August 2025 about domain switch instruction sent June 20, 2025; confronted Rynette on May 15, 2025 about R1,035,000 owed to ReZonance (EVENT_007 confrontation triggered escalation)"
                print("Fixed PERSON_012 timeline events")
    return entities_data

def enhance_evidence_references(events_data):
    """Enhance evidence references in events with ad-res-j7 cross-references"""
    
    # Add comprehensive evidence references to key events
    evidence_enhancements = {
        'EVENT_001': {
            'evidence': [
                'trust_deed_2025_03_15',
                'trustee_appointment_documents',
                'ad_res_j7/ANNEXURES/trust_documentation'
            ]
        },
        'EVENT_007': {
            'evidence': [
                'confrontation_email_2025_05_15',
                'rezonance_debt_documentation',
                'ad_res_j7/ANNEXURES/rezonance_invoices',
                'ad_res_j7/1-CIVIL-RESPONSE/rezonance_payment_analysis'
            ]
        },
        'EVENT_027': {
            'evidence': [
                'gee_email_august_2025',
                'domain_switch_instruction_june_20_2025',
                'customer_diversion_scheme_documentation',
                'ad_res_j7/ANNEXURES/email_evidence'
            ]
        }
    }
    
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        if event_id in evidence_enhancements:
            # Merge existing evidence with enhancements
            existing_evidence = event.get('evidence', [])
            new_evidence = evidence_enhancements[event_id]['evidence']
            event['evidence'] = list(set(existing_evidence + new_evidence))
            print(f"Enhanced evidence for {event_id}")
    
    return events_data

def add_github_pages_references(events_data):
    """Add GitHub Pages evidence references to events"""
    
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        
        # Add github_pages_reference field for key events
        if event.get('category') in ['revenue_theft', 'trust_violations', 'financial_manipulation']:
            event['github_pages_reference'] = f"https://cogpy.github.io/revstream1/evidence-index.html#{event_id.lower()}"
    
    return events_data

def enhance_timeline_with_evidence_links(timeline_data):
    """Enhance timeline phases with evidence links"""
    
    for phase_key, phase in timeline_data.get('timeline_phases', {}).items():
        # Add evidence_summary field
        phase['evidence_summary'] = {
            'primary_documents': f"See evidence-index.html for phase {phase.get('phase_id')}",
            'github_pages_link': f"https://cogpy.github.io/revstream1/evidence-index.html"
        }
    
    return timeline_data

def add_cross_references_to_relations(relations_data):
    """Add cross-references to ad-res-j7 in relations"""
    
    for rel_type, relations in relations_data.get('relations', {}).items():
        for relation in relations:
            # Add ad_res_j7_reference field
            if not relation.get('ad_res_j7_reference'):
                relation['ad_res_j7_reference'] = "See ad-res-j7/COMPREHENSIVE_EVIDENCE_INDEX.json for detailed evidence"
    
    return relations_data

def update_metadata(data, model_type):
    """Update metadata with refinement information"""
    if 'metadata' in data:
        data['metadata']['last_updated'] = '2025-11-19'
        data['metadata']['version'] = '10.0'
        data['metadata']['changes'] = f"Refinement 2025-11-19: Fixed PERSON_012 events, enhanced evidence references, added GitHub Pages links, improved ad-res-j7 cross-references"
    return data

def main():
    print("Loading data models...")
    
    # Load all data models
    entities_data = load_json('data_models/entities/entities_refined_2025_11_18.json')
    events_data = load_json('data_models/events/events_refined_2025_11_18.json')
    relations_data = load_json('data_models/relations/relations_refined_2025_11_18.json')
    timeline_data = load_json('data_models/timelines/timeline_refined_2025_11_18.json')
    
    print("\nApplying refinements...")
    
    # Fix issues
    print("- Fixing PERSON_012 timeline events...")
    entities_data = fix_person_012_events(entities_data)
    
    # Enhance evidence references
    print("- Enhancing evidence references...")
    events_data = enhance_evidence_references(events_data)
    
    # Add GitHub Pages references
    print("- Adding GitHub Pages references...")
    events_data = add_github_pages_references(events_data)
    
    # Enhance timeline
    print("- Enhancing timeline with evidence links...")
    timeline_data = enhance_timeline_with_evidence_links(timeline_data)
    
    # Add cross-references to relations
    print("- Adding cross-references to relations...")
    relations_data = add_cross_references_to_relations(relations_data)
    
    # Update metadata
    print("- Updating metadata...")
    entities_data = update_metadata(entities_data, 'entities')
    events_data = update_metadata(events_data, 'events')
    relations_data = update_metadata(relations_data, 'relations')
    timeline_data = update_metadata(timeline_data, 'timeline')
    
    # Save refined models
    print("\nSaving refined models...")
    save_json(entities_data, 'data_models/entities/entities_refined_2025_11_19.json')
    save_json(events_data, 'data_models/events/events_refined_2025_11_19.json')
    save_json(relations_data, 'data_models/relations/relations_refined_2025_11_19.json')
    save_json(timeline_data, 'data_models/timelines/timeline_refined_2025_11_19.json')
    
    print("\n" + "="*80)
    print("REFINEMENT COMPLETE")
    print("="*80)
    print("\nRefined models saved:")
    print("  - data_models/entities/entities_refined_2025_11_19.json")
    print("  - data_models/events/events_refined_2025_11_19.json")
    print("  - data_models/relations/relations_refined_2025_11_19.json")
    print("  - data_models/timelines/timeline_refined_2025_11_19.json")
    
    return True

if __name__ == '__main__':
    main()
