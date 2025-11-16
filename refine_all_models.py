import json
import os
from datetime import datetime

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def refine_entities():
    """Refine entities with ad-res-j7 evidence"""
    entities_path = '/home/ubuntu/revstream1/data_models/entities/entities.json'
    extraction_path = '/home/ubuntu/revstream1/ad_res_j7_extraction_report.json'
    
    entities_data = load_json(entities_path)
    extraction_data = load_json(extraction_path)
    
    # Update metadata
    entities_data['metadata']['version'] = "7.0"
    entities_data['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
    entities_data['metadata']['changes'] = "Integrated ad-res-j7 evidence: added new events to entities, enhanced entity descriptions with timeline evidence"
    
    # Apply entity updates from extraction
    entity_updates = extraction_data['entity_updates']
    
    for person in entities_data['entities']['persons']:
        entity_id = person['entity_id']
        if entity_id in entity_updates:
            updates = entity_updates[entity_id]
            
            # Add additional events
            if 'additional_events' in updates:
                if 'timeline_events' not in person:
                    person['timeline_events'] = []
                person['timeline_events'].extend(updates['additional_events'])
                person['timeline_events'] = list(set(person['timeline_events']))  # Remove duplicates
            
            # Update additional notes
            if 'additional_notes' in updates:
                if 'additional_notes' in person:
                    person['additional_notes'] += "; " + updates['additional_notes']
                else:
                    person['additional_notes'] = updates['additional_notes']
            
            # Add role clarification
            if 'role_clarification' in updates:
                person['role_clarification'] = updates['role_clarification']
            
            # Update involvement events count
            if 'timeline_events' in person:
                person['involvement_events'] = len(person['timeline_events'])
    
    # Save refined entities
    save_json(entities_path, entities_data)
    print("✓ Entities refined successfully")
    return entities_data

def refine_events():
    """Refine events with ad-res-j7 evidence"""
    events_path = '/home/ubuntu/revstream1/data_models/events/events.json'
    extraction_path = '/home/ubuntu/revstream1/ad_res_j7_extraction_report.json'
    
    events_data = load_json(events_path)
    extraction_data = load_json(extraction_path)
    
    # Update metadata
    events_data['metadata']['version'] = "7.0"
    events_data['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
    events_data['metadata']['total_events'] = len(events_data['events']) + len(extraction_data['new_events'])
    events_data['metadata']['changes'] = "Integrated ad-res-j7 evidence: added 9 new critical events including Bantjies knowledge acquisition, settlement timing, and perjury events"
    
    # Add new events
    events_data['events'].extend(extraction_data['new_events'])
    
    # Sort events by date
    events_data['events'].sort(key=lambda x: x['date'])
    
    # Save refined events
    save_json(events_path, events_data)
    print(f"✓ Events refined successfully - added {len(extraction_data['new_events'])} new events")
    return events_data

def refine_relations():
    """Refine relations with ad-res-j7 evidence"""
    relations_path = '/home/ubuntu/revstream1/data_models/relations/relations.json'
    extraction_path = '/home/ubuntu/revstream1/ad_res_j7_extraction_report.json'
    
    relations_data = load_json(relations_path)
    extraction_data = load_json(extraction_path)
    
    # Update metadata
    relations_data['metadata']['version'] = "5.0"
    relations_data['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
    relations_data['metadata']['changes'] = "Integrated ad-res-j7 evidence: added professional_correspondence_relations, knowledge_acquisition_relations, strategic_coordination_relations"
    
    # Add new relation categories if they don't exist
    new_relations = extraction_data['new_relations']
    
    # Group new relations by type
    for relation in new_relations:
        rel_type = relation['relation_type']
        
        if rel_type == 'professional_correspondence':
            if 'professional_correspondence_relations' not in relations_data['relations']:
                relations_data['relations']['professional_correspondence_relations'] = []
            relations_data['relations']['professional_correspondence_relations'].append(relation)
        
        elif rel_type == 'knowledge_acquisition':
            if 'knowledge_acquisition_relations' not in relations_data['relations']:
                relations_data['relations']['knowledge_acquisition_relations'] = []
            relations_data['relations']['knowledge_acquisition_relations'].append(relation)
        
        elif rel_type == 'strategic_coordination':
            if 'strategic_coordination_relations' not in relations_data['relations']:
                relations_data['relations']['strategic_coordination_relations'] = []
            relations_data['relations']['strategic_coordination_relations'].append(relation)
    
    # Save refined relations
    save_json(relations_path, relations_data)
    print(f"✓ Relations refined successfully - added {len(new_relations)} new relations")
    return relations_data

def refine_timeline():
    """Refine timeline with ad-res-j7 evidence"""
    timeline_path = '/home/ubuntu/revstream1/data_models/timelines/timeline_enhanced.json'
    extraction_path = '/home/ubuntu/revstream1/ad_res_j7_extraction_report.json'
    
    timeline_data = load_json(timeline_path)
    extraction_data = load_json(extraction_path)
    
    # Update metadata
    timeline_data['metadata']['version'] = "6.0"
    timeline_data['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
    timeline_data['metadata']['total_events'] = 53 + len(extraction_data['new_events'])
    timeline_data['metadata']['changes'] = "Integrated ad-res-j7 evidence: added 9 new events, enhanced phase analysis with strategic timing patterns"
    
    # Add new events to appropriate phases
    new_events = extraction_data['new_events']
    
    for event in new_events:
        event_id = event['event_id']
        pattern = event.get('pattern', '')
        
        # Add to historical foundation phase
        if pattern == 'historical_foundation':
            if event_id not in timeline_data['timeline_phases']['phase_0_historical_foundation']['events']:
                timeline_data['timeline_phases']['phase_0_historical_foundation']['events'].append(event_id)
        
        # Add to debt accumulation phase
        elif pattern == 'debt_accumulation':
            if event_id not in timeline_data['timeline_phases']['phase_0_5_debt_accumulation']['events']:
                timeline_data['timeline_phases']['phase_0_5_debt_accumulation']['events'].append(event_id)
        
        # Add to escalation phase
        elif pattern == 'escalation_phase':
            if event_id not in timeline_data['timeline_phases']['phase_3_escalation']['events']:
                timeline_data['timeline_phases']['phase_3_escalation']['events'].append(event_id)
        
        # Add to consolidation phase
        elif pattern == 'consolidation_phase':
            if event_id not in timeline_data['timeline_phases']['phase_4_consolidation']['events']:
                timeline_data['timeline_phases']['phase_4_consolidation']['events'].append(event_id)
        
        # Add to cover-up phase
        elif pattern == 'cover_up_phase':
            if event_id not in timeline_data['timeline_phases']['phase_6_cover_up']['events']:
                timeline_data['timeline_phases']['phase_6_cover_up']['events'].append(event_id)
    
    # Update phase characteristics
    timeline_data['timeline_phases']['phase_4_consolidation']['key_characteristics'].extend([
        "daniel_provides_comprehensive_reports_to_bantjies",
        "bantjies_learns_of_criminal_matters_june_10_2025"
    ])
    
    timeline_data['timeline_phases']['phase_6_cover_up']['key_characteristics'].extend([
        "settlement_agreement_signed_2_days_before_interdict",
        "peter_files_founding_affidavit_with_material_non_disclosures",
        "ens_africa_acknowledges_then_suppresses_criminal_matters"
    ])
    
    # Add new temporal pattern for strategic timing
    if 'strategic_timing_patterns' not in timeline_data:
        timeline_data['strategic_timing_patterns'] = []
    
    timeline_data['strategic_timing_patterns'].append({
        "pattern_id": "STRATEGIC_001",
        "pattern_name": "Settlement-Interdict Coordination",
        "event_sequence": ["EVENT_059", "EVENT_060"],
        "timing_gap_days": 2,
        "significance": "Settlement signed 2 days before interdict filing demonstrates premeditation and strategic litigation tactic",
        "legal_implication": "Not genuine business protection but control and financial positioning"
    })
    
    timeline_data['strategic_timing_patterns'].append({
        "pattern_id": "STRATEGIC_002",
        "pattern_name": "Knowledge-Perjury Timeline",
        "event_sequence": ["EVENT_058", "EVENT_061"],
        "timing_gap_days": 80,
        "significance": "Bantjies learned of criminal matters June 10, then ENS Africa suppressed this information August 29",
        "legal_implication": "Professional misconduct and evidence suppression"
    })
    
    # Save refined timeline
    save_json(timeline_path, timeline_data)
    print(f"✓ Timeline refined successfully - added {len(new_events)} new events and 2 strategic timing patterns")
    return timeline_data

def generate_refinement_summary():
    """Generate comprehensive refinement summary"""
    extraction_data = load_json('/home/ubuntu/revstream1/ad_res_j7_extraction_report.json')
    
    summary = {
        "refinement_date": datetime.now().isoformat(),
        "source_repositories": ["revstream1", "ad-res-j7"],
        "refinements_applied": {
            "entities": {
                "entities_updated": len(extraction_data['entity_updates']),
                "updates_applied": list(extraction_data['entity_updates'].keys())
            },
            "events": {
                "new_events_added": len(extraction_data['new_events']),
                "event_ids": [e['event_id'] for e in extraction_data['new_events']]
            },
            "relations": {
                "new_relations_added": len(extraction_data['new_relations']),
                "relation_types": list(set([r['relation_type'] for r in extraction_data['new_relations']]))
            },
            "timeline": {
                "new_events_integrated": len(extraction_data['new_events']),
                "strategic_patterns_added": 2
            }
        },
        "critical_improvements": extraction_data['critical_findings'],
        "key_insights": [
            "Bantjies knowledge acquisition timeline (June 10, 2025) establishes perjury foundation",
            "Settlement-interdict timing (2 days gap) demonstrates strategic litigation coordination",
            "Peter's founding affidavit contains material non-disclosures and perjury",
            "ENS Africa professional misconduct through evidence suppression documented",
            "Cloud IT systems removal and server disappearance establish evidence tampering pattern",
            "Chantal letter indicates ongoing estate exploitation of deceased victim"
        ],
        "next_steps": [
            "Update Supabase/Neon database schemas with new events and relations",
            "Generate updated hypergraph visualizations",
            "Create timeline visualization with strategic timing patterns",
            "Prepare evidence cross-reference documentation"
        ]
    }
    
    save_json('/home/ubuntu/revstream1/REFINEMENT_SUMMARY_2025-11-16.json', summary)
    
    # Create markdown summary
    md_summary = f"""# Data Model Refinement Summary
## Date: {datetime.now().strftime("%Y-%m-%d")}

### Source Integration
- **Primary Repository**: revstream1
- **Evidence Repository**: ad-res-j7
- **Integration Method**: Cross-repository timeline and evidence analysis

### Refinements Applied

#### Entities
- **Entities Updated**: {len(extraction_data['entity_updates'])}
- **Updated IDs**: {', '.join(extraction_data['entity_updates'].keys())}

#### Events
- **New Events Added**: {len(extraction_data['new_events'])}
- **Event IDs**: {', '.join([e['event_id'] for e in extraction_data['new_events']])}

#### Relations
- **New Relations Added**: {len(extraction_data['new_relations'])}
- **Relation Types**: {', '.join(set([r['relation_type'] for r in extraction_data['new_relations']]))}

#### Timeline
- **New Events Integrated**: {len(extraction_data['new_events'])}
- **Strategic Patterns Added**: 2

### Critical Improvements

"""
    for finding in extraction_data['critical_findings']:
        md_summary += f"- {finding}\n"
    
    md_summary += """
### Key Insights

1. **Bantjies Knowledge Acquisition Timeline**: June 10, 2025 establishes perjury foundation
2. **Settlement-Interdict Timing**: 2 days gap demonstrates strategic litigation coordination
3. **Material Non-Disclosures**: Peter's founding affidavit contains perjury
4. **Professional Misconduct**: ENS Africa evidence suppression documented
5. **Evidence Tampering Pattern**: Cloud IT systems removal and server disappearance
6. **Estate Exploitation**: Chantal letter indicates ongoing exploitation of deceased victim

### Next Steps

1. Update Supabase/Neon database schemas with new events and relations
2. Generate updated hypergraph visualizations
3. Create timeline visualization with strategic timing patterns
4. Prepare evidence cross-reference documentation

### Version Updates

- **Entities**: v6.0 → v7.0
- **Events**: v6.0 → v7.0
- **Relations**: v4.0 → v5.0
- **Timeline**: v5.0 → v6.0

---

**Total Events**: 62 (53 original + 9 new)
**Total Relations**: 54 (51 original + 3 new)
**Total Entities Updated**: 3
"""
    
    with open('/home/ubuntu/revstream1/REFINEMENT_SUMMARY_2025-11-16.md', 'w') as f:
        f.write(md_summary)
    
    print("\n✓ Refinement summary generated")
    return summary

def main():
    print("=" * 60)
    print("DATA MODEL REFINEMENT - INTEGRATING AD-RES-J7 EVIDENCE")
    print("=" * 60)
    print()
    
    # Refine all models
    print("Refining entities...")
    refine_entities()
    
    print("Refining events...")
    refine_events()
    
    print("Refining relations...")
    refine_relations()
    
    print("Refining timeline...")
    refine_timeline()
    
    print("\nGenerating refinement summary...")
    summary = generate_refinement_summary()
    
    print("\n" + "=" * 60)
    print("REFINEMENT COMPLETE")
    print("=" * 60)
    print(f"\nTotal refinements:")
    print(f"  - Entities updated: {summary['refinements_applied']['entities']['entities_updated']}")
    print(f"  - Events added: {summary['refinements_applied']['events']['new_events_added']}")
    print(f"  - Relations added: {summary['refinements_applied']['relations']['new_relations_added']}")
    print(f"  - Strategic patterns added: {summary['refinements_applied']['timeline']['strategic_patterns_added']}")
    print(f"\nSummary files created:")
    print(f"  - REFINEMENT_SUMMARY_2025-11-16.json")
    print(f"  - REFINEMENT_SUMMARY_2025-11-16.md")

if __name__ == '__main__':
    main()
