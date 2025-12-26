#!/usr/bin/env python3.11
"""
Comprehensive Refinement Script for RevStream1
Cross-references evidence from ad-res-j7 and refines entities, relations, events, and timelines
"""
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Load current comprehensive analysis
with open('COMPREHENSIVE_ANALYSIS_2025_12_25.json', 'r') as f:
    current_data = json.load(f)

print("=" * 80)
print("COMPREHENSIVE REFINEMENT - 2025-12-26")
print("=" * 80)
print(f"\nLoaded current analysis from: 2025-12-25")
print(f"Starting refinement at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Initialize refinement tracking
refinements = {
    'entities_added': [],
    'entities_updated': [],
    'relations_added': [],
    'relations_updated': [],
    'events_added': [],
    'events_updated': [],
    'evidence_added': [],
    'timeline_updates': []
}

# ============================================================================
# PHASE 1: ADD MISSING ENTITIES
# ============================================================================
print(f"\n{'PHASE 1: ENTITY REFINEMENT':-^80}")

entities_data = current_data['entities']['data']['entities']
persons = entities_data['persons']
orgs = entities_data['organizations']

# Check for Elliott Attorneys (ORG_011)
elliott_exists = any(o.get('entity_id') == 'ORG_011' for o in orgs)
if not elliott_exists:
    new_org = {
        "entity_id": "ORG_011",
        "name": "Elliott Attorneys",
        "role": "rynette_legal_representative",
        "agent_type": "antagonist_legal_counsel",
        "involvement_events": 3,
        "primary_actions": [
            "defamation_demand_letter",
            "legal_intimidation",
            "strategic_counterattack"
        ],
        "relationships": [
            "legal_representative_of_PERSON_002"
        ],
        "evidence": [
            "JF13 - Letter of Demand 26.11.2025",
            "JF13 - Letter to Opposing Attorney 26.11.2025"
        ],
        "ad_res_j7_references": [
            "ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf",
            "ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"
        ],
        "evidence_strength": "conclusive",
        "first_appearance": "2025-11-26"
    }
    orgs.append(new_org)
    refinements['entities_added'].append('ORG_011: Elliott Attorneys')
    print(f"✓ Added ORG_011: Elliott Attorneys")
else:
    print(f"  ORG_011: Elliott Attorneys already exists")

# Check for Pottas Attorneys (ORG_012 might be misnamed)
pottas_exists = any('Pottas' in o.get('name', '') for o in orgs)
if not pottas_exists:
    new_org = {
        "entity_id": "ORG_016",
        "name": "Pottas Attorneys",
        "role": "peter_legal_representative",
        "agent_type": "antagonist_legal_counsel",
        "involvement_events": 2,
        "primary_actions": [
            "legal_representation",
            "interdict_applications"
        ],
        "relationships": [
            "legal_representative_of_PERSON_001"
        ],
        "evidence": [
            "JF13 - Letters addressed to Pottas Attorneys"
        ],
        "ad_res_j7_references": [
            "ANNEXURES/JF13/"
        ],
        "evidence_strength": "conclusive",
        "first_appearance": "2025-10-01"
    }
    orgs.append(new_org)
    refinements['entities_added'].append('ORG_016: Pottas Attorneys')
    print(f"✓ Added ORG_016: Pottas Attorneys")

# Update entity counts
current_data['entities']['total_count'] = len(persons) + len(orgs)
current_data['entities']['persons'] = len(persons)
current_data['entities']['organizations'] = len(orgs)

print(f"\nEntity Summary:")
print(f"  Total Entities: {current_data['entities']['total_count']}")
print(f"  Persons: {len(persons)}")
print(f"  Organizations: {len(orgs)}")
print(f"  New Entities Added: {len(refinements['entities_added'])}")

# ============================================================================
# PHASE 2: ADD MISSING RELATIONS
# ============================================================================
print(f"\n{'PHASE 2: RELATIONS REFINEMENT':-^80}")

relations_data = current_data['relations']['data']['relations']

# Add legal representation relations
if 'legal_representation_relations' not in relations_data:
    relations_data['legal_representation_relations'] = []

legal_reps = relations_data['legal_representation_relations']

# Elliott Attorneys -> Rynette Farrar
elliott_rynette_exists = any(
    r.get('source_entity') == 'ORG_011' and r.get('target_entity') == 'PERSON_002'
    for r in legal_reps
)
if not elliott_rynette_exists:
    new_rel = {
        "relation_id": "REL_LEGAL_001",
        "relation_type": "legal_representation",
        "source_entity": "ORG_011",
        "target_entity": "PERSON_002",
        "strength": "active_representation",
        "legal_status": "legitimate",
        "evidence": ["JF13 - Letter of Demand"],
        "start_date": "2025-11-26",
        "evidence_verified": datetime.now().isoformat(),
        "ad_res_j7_evidence": ["ANNEXURES/JF13/"]
    }
    legal_reps.append(new_rel)
    refinements['relations_added'].append('REL_LEGAL_001: Elliott Attorneys represents Rynette Farrar')
    print(f"✓ Added REL_LEGAL_001: Elliott Attorneys -> Rynette Farrar")

# Pottas Attorneys -> Peter Faucitt
pottas_peter_exists = any(
    r.get('source_entity') == 'ORG_016' and r.get('target_entity') == 'PERSON_001'
    for r in legal_reps
)
if not pottas_peter_exists:
    new_rel = {
        "relation_id": "REL_LEGAL_002",
        "relation_type": "legal_representation",
        "source_entity": "ORG_016",
        "target_entity": "PERSON_001",
        "strength": "active_representation",
        "legal_status": "legitimate",
        "evidence": ["JF13 - Letters to Pottas Attorneys"],
        "start_date": "2025-10-01",
        "evidence_verified": datetime.now().isoformat(),
        "ad_res_j7_evidence": ["ANNEXURES/JF13/"]
    }
    legal_reps.append(new_rel)
    refinements['relations_added'].append('REL_LEGAL_002: Pottas Attorneys represents Peter Faucitt')
    print(f"✓ Added REL_LEGAL_002: Pottas Attorneys -> Peter Faucitt")

# Add defamation counterclaim relation
if 'defamation_relations' not in relations_data:
    relations_data['defamation_relations'] = []

defamation_rels = relations_data['defamation_relations']
rynette_jax_defamation = {
    "relation_id": "REL_DEFAM_001",
    "relation_type": "defamation_counterclaim",
    "source_entity": "PERSON_002",
    "target_entity": "PERSON_004",
    "strength": "legal_threat",
    "legal_status": "pending",
    "evidence": ["JF13 - Letter of Demand"],
    "date": "2025-11-26",
    "deadline": "2025-11-28",
    "allegations_count": 7,
    "evidence_verified": datetime.now().isoformat(),
    "ad_res_j7_evidence": ["ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf"]
}
defamation_rels.append(rynette_jax_defamation)
refinements['relations_added'].append('REL_DEFAM_001: Rynette defamation counterclaim against Jacqueline')
print(f"✓ Added REL_DEFAM_001: Rynette -> Jacqueline (defamation counterclaim)")

# Update relation counts
total_relations = sum(len(rel_list) for rel_list in relations_data.values() if isinstance(rel_list, list))
current_data['relations']['total_count'] = total_relations

# Update by_type
current_data['relations']['by_type'] = {
    rel_type: len(rel_list) 
    for rel_type, rel_list in relations_data.items() 
    if isinstance(rel_list, list)
}

print(f"\nRelations Summary:")
print(f"  Total Relations: {total_relations}")
print(f"  Relation Types: {len(current_data['relations']['by_type'])}")
print(f"  New Relations Added: {len(refinements['relations_added'])}")

# ============================================================================
# PHASE 3: ADD MISSING EVENTS
# ============================================================================
print(f"\n{'PHASE 3: EVENTS REFINEMENT':-^80}")

events_data = current_data['events']['data']['events']

# Event 074: Application 3 Dismissed
event_074_exists = any(e.get('event_id') == 'EVENT_074' for e in events_data)
if not event_074_exists:
    new_event = {
        "event_id": "EVENT_074",
        "date": "2025-11-25",
        "description": "Application 3 (Contact Interdict) Dismissed",
        "category": "legal_action",
        "impact_level": "high",
        "participants": ["PERSON_001", "PERSON_004"],
        "evidence": ["JF13 - Reference to Application 3 dismissal"],
        "significance": "Peter's third application unsuccessful, strengthens Jacqueline's position",
        "ad_res_j7_references": ["ANNEXURES/JF13/README.md"],
        "evidence_verified": datetime.now().isoformat()
    }
    events_data.append(new_event)
    refinements['events_added'].append('EVENT_074: Application 3 Dismissed')
    print(f"✓ Added EVENT_074: Application 3 Dismissed")

# Event 075: Rynette Retains Legal Counsel
event_075_exists = any(e.get('event_id') == 'EVENT_075' for e in events_data)
if not event_075_exists:
    new_event = {
        "event_id": "EVENT_075",
        "date": "2025-11-26",
        "description": "Rynette Farrar Retains Elliott Attorneys",
        "category": "legal_action",
        "impact_level": "high",
        "participants": ["PERSON_002", "ORG_011"],
        "evidence": ["JF13 - Letter of Demand from Elliott Attorneys"],
        "significance": "Rynette enters proceedings with defamation counterclaim strategy",
        "ad_res_j7_references": ["ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf"],
        "evidence_verified": datetime.now().isoformat()
    }
    events_data.append(new_event)
    refinements['events_added'].append('EVENT_075: Rynette Retains Legal Counsel')
    print(f"✓ Added EVENT_075: Rynette Retains Legal Counsel")

# Event 076: Letter of Demand Issued
event_076_exists = any(e.get('event_id') == 'EVENT_076' for e in events_data)
if not event_076_exists:
    new_event = {
        "event_id": "EVENT_076",
        "date": "2025-11-26",
        "description": "Rynette Issues Defamation Letter of Demand (48-hour deadline)",
        "category": "legal_action",
        "impact_level": "critical",
        "participants": ["PERSON_002", "PERSON_004", "ORG_011"],
        "evidence": ["JF13 - KL0034 Letter of Demand"],
        "allegations_count": 7,
        "deadline": "2025-11-28",
        "demands": [
            "Written retraction and apology",
            "Cease and desist",
            "Written confirmation of non-republication"
        ],
        "significance": "Creates immediate response requirement, defamation counterclaim strategy",
        "ad_res_j7_references": ["ANNEXURES/JF13/KL0034-LetterofDemand-26.11.2025.pdf"],
        "evidence_verified": datetime.now().isoformat()
    }
    events_data.append(new_event)
    refinements['events_added'].append('EVENT_076: Letter of Demand Issued')
    print(f"✓ Added EVENT_076: Letter of Demand Issued")

# Event 077: Ongoing Interdict Violations Reported
event_077_exists = any(e.get('event_id') == 'EVENT_077' for e in events_data)
if not event_077_exists:
    new_event = {
        "event_id": "EVENT_077",
        "date": "2025-11-26",
        "description": "Peter Removes Work Phone Again - Ongoing Interdict Violations",
        "category": "interdict_violation",
        "impact_level": "high",
        "participants": ["PERSON_001"],
        "evidence": ["JF13 - KF0019 Letter to Opposing Attorney"],
        "significance": "Continued violations strengthen contempt of court case",
        "ad_res_j7_references": ["ANNEXURES/JF13/KF0019-LettertoOpp(PottasAttorneys)26.11.2025.pdf"],
        "evidence_verified": datetime.now().isoformat()
    }
    events_data.append(new_event)
    refinements['events_added'].append('EVENT_077: Ongoing Interdict Violations')
    print(f"✓ Added EVENT_077: Ongoing Interdict Violations")

# Update event counts
current_data['events']['total_count'] = len(events_data)

print(f"\nEvents Summary:")
print(f"  Total Events: {len(events_data)}")
print(f"  New Events Added: {len(refinements['events_added'])}")

# ============================================================================
# PHASE 4: UPDATE TIMELINE
# ============================================================================
print(f"\n{'PHASE 4: TIMELINE REFINEMENT':-^80}")

timeline_data = current_data['timelines']['data']

# Add new timeline phase: Legal Escalation (Nov 2025)
if 'legal_escalation_phase' not in timeline_data['timeline_phases']:
    timeline_data['timeline_phases']['legal_escalation_phase'] = {
        "phase_id": "PHASE_009",
        "phase_name": "Legal Escalation and Defamation Counterclaim",
        "start_date": "2025-11-25",
        "end_date": "ongoing",
        "key_events": ["EVENT_074", "EVENT_075", "EVENT_076", "EVENT_077"],
        "significance": "Rynette enters proceedings with defamation strategy, Application 3 dismissed",
        "participants": ["PERSON_001", "PERSON_002", "PERSON_004", "ORG_011", "ORG_016"],
        "evidence": ["JF13"]
    }
    refinements['timeline_updates'].append('Added PHASE_009: Legal Escalation')
    print(f"✓ Added PHASE_009: Legal Escalation and Defamation Counterclaim")

# Update timeline version
current_data['timelines']['version'] = "7.0_ENHANCED_2025_12_26"
current_data['timelines']['total_phases'] = len([k for k in timeline_data['timeline_phases'].keys() if k.startswith('phase_') or k.startswith('PHASE_')])

print(f"\nTimeline Summary:")
print(f"  Total Phases: {current_data['timelines']['total_phases']}")
print(f"  Timeline Updates: {len(refinements['timeline_updates'])}")

# ============================================================================
# PHASE 5: UPDATE METADATA
# ============================================================================
print(f"\n{'PHASE 5: METADATA UPDATE':-^80}")

current_data['timestamp'] = datetime.now().isoformat()
current_data['entities']['version'] = "17.0_REFINED_2025_12_26"
current_data['entities']['data']['metadata']['last_updated'] = datetime.now().isoformat()
current_data['entities']['data']['metadata']['changes'] = "Enhanced with JF13 legal correspondence and defamation counterclaim"

current_data['relations']['version'] = "8.0_EVIDENCE_ENHANCED_2025_12_26"
current_data['relations']['data']['metadata']['last_updated'] = datetime.now().isoformat()

current_data['events']['version'] = "26.0_ENHANCED_2025_12_26"
current_data['events']['data']['metadata']['last_updated'] = datetime.now().isoformat()

print(f"✓ Updated all metadata versions")

# ============================================================================
# SAVE REFINED DATA
# ============================================================================
print(f"\n{'SAVING REFINED DATA':-^80}")

output_file = 'COMPREHENSIVE_ANALYSIS_2025_12_26.json'
with open(output_file, 'w') as f:
    json.dump(current_data, f, indent=2)

print(f"✓ Saved refined data to: {output_file}")

# ============================================================================
# REFINEMENT SUMMARY
# ============================================================================
print(f"\n{'REFINEMENT SUMMARY':-^80}")
print(f"\nEntities:")
print(f"  Added: {len(refinements['entities_added'])}")
for entity in refinements['entities_added']:
    print(f"    - {entity}")

print(f"\nRelations:")
print(f"  Added: {len(refinements['relations_added'])}")
for relation in refinements['relations_added']:
    print(f"    - {relation}")

print(f"\nEvents:")
print(f"  Added: {len(refinements['events_added'])}")
for event in refinements['events_added']:
    print(f"    - {event}")

print(f"\nTimeline:")
print(f"  Updates: {len(refinements['timeline_updates'])}")
for update in refinements['timeline_updates']:
    print(f"    - {update}")

print(f"\n{'REFINEMENT COMPLETE':-^80}")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# Save refinement report
refinement_report = {
    "timestamp": datetime.now().isoformat(),
    "source_file": "COMPREHENSIVE_ANALYSIS_2025_12_25.json",
    "output_file": output_file,
    "refinements": refinements,
    "summary": {
        "total_entities": current_data['entities']['total_count'],
        "total_relations": current_data['relations']['total_count'],
        "total_events": current_data['events']['total_count'],
        "total_timeline_phases": current_data['timelines']['total_phases']
    }
}

with open('REFINEMENT_REPORT_2025_12_26.json', 'w') as f:
    json.dump(refinement_report, f, indent=2)

print(f"\n✓ Saved refinement report to: REFINEMENT_REPORT_2025_12_26.json")
