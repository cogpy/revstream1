#!/usr/bin/env python3
"""
Comprehensive Data Model Analysis Script
Analyzes entities, relations, events, and timelines for completeness and consistency
"""

import json
from datetime import datetime
from collections import defaultdict, Counter
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities for completeness and issues"""
    analysis = {
        "total_entities": 0,
        "by_category": {},
        "missing_timeline_events": [],
        "zero_involvement_events": [],
        "missing_relationships": [],
        "entity_summary": []
    }
    
    all_entities = entities_data.get("entities", {})
    
    for category, entity_list in all_entities.items():
        analysis["by_category"][category] = len(entity_list)
        analysis["total_entities"] += len(entity_list)
        
        for entity in entity_list:
            entity_id = entity.get("entity_id", "UNKNOWN")
            name = entity.get("name", "UNKNOWN")
            
            # Check for missing timeline events
            timeline_events = entity.get("timeline_events", [])
            involvement_events = entity.get("involvement_events", 0)
            
            if involvement_events > 0 and len(timeline_events) == 0:
                analysis["missing_timeline_events"].append({
                    "entity_id": entity_id,
                    "name": name,
                    "involvement_events": involvement_events
                })
            
            if involvement_events == 0 and entity.get("agent_type") in ["antagonist", "accomplice"]:
                analysis["zero_involvement_events"].append({
                    "entity_id": entity_id,
                    "name": name,
                    "agent_type": entity.get("agent_type")
                })
            
            # Check for missing relationships
            relationships = entity.get("relationships", [])
            if len(relationships) == 0:
                analysis["missing_relationships"].append({
                    "entity_id": entity_id,
                    "name": name
                })
            
            # Create summary
            analysis["entity_summary"].append({
                "entity_id": entity_id,
                "name": name,
                "category": category,
                "agent_type": entity.get("agent_type", "N/A"),
                "involvement_events": involvement_events,
                "timeline_events_count": len(timeline_events),
                "relationships_count": len(relationships)
            })
    
    return analysis

def analyze_events(events_data):
    """Analyze events for completeness and issues"""
    analysis = {
        "total_events": 0,
        "by_category": Counter(),
        "by_phase": Counter(),
        "missing_perpetrators": [],
        "missing_victims": [],
        "missing_financial_impact": [],
        "event_summary": []
    }
    
    events = events_data.get("events", [])
    analysis["total_events"] = len(events)
    
    for event in events:
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "unknown")
        phase = event.get("timeline_phase", "UNASSIGNED")
        
        analysis["by_category"][category] += 1
        analysis["by_phase"][phase] += 1
        
        # Check for missing perpetrators
        perpetrators = event.get("perpetrators", [])
        if len(perpetrators) == 0 and category not in ["business_relationship", "financial_structure", "evidence_documentation"]:
            analysis["missing_perpetrators"].append({
                "event_id": event_id,
                "title": event.get("title", "N/A"),
                "category": category
            })
        
        # Check for missing victims
        victims = event.get("victims", [])
        if category in ["theft", "fraud", "unauthorized_transfer"] and len(victims) == 0:
            analysis["missing_victims"].append({
                "event_id": event_id,
                "title": event.get("title", "N/A"),
                "category": category
            })
        
        # Check for missing financial impact
        financial_impact = event.get("financial_impact", "unknown")
        if financial_impact in ["unknown", "N/A", None] and category in ["theft", "fraud", "payment_redirection", "unauthorized_transfer"]:
            analysis["missing_financial_impact"].append({
                "event_id": event_id,
                "title": event.get("title", "N/A"),
                "category": category
            })
        
        # Create summary
        analysis["event_summary"].append({
            "event_id": event_id,
            "date": event.get("date", "N/A"),
            "title": event.get("title", "N/A"),
            "category": category,
            "phase": phase,
            "perpetrators_count": len(perpetrators),
            "victims_count": len(victims),
            "financial_impact": financial_impact
        })
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations for completeness and issues"""
    analysis = {
        "total_relations": 0,
        "by_type": {},
        "missing_evidence": [],
        "weak_evidence": [],
        "relation_summary": []
    }
    
    all_relations = relations_data.get("relations", {})
    
    for rel_type, relation_list in all_relations.items():
        analysis["by_type"][rel_type] = len(relation_list)
        analysis["total_relations"] += len(relation_list)
        
        for relation in relation_list:
            relation_id = relation.get("relation_id", "UNKNOWN")
            
            # Check for missing evidence
            evidence = relation.get("evidence", [])
            if len(evidence) == 0:
                analysis["missing_evidence"].append({
                    "relation_id": relation_id,
                    "type": rel_type,
                    "source": relation.get("source_entity", "N/A"),
                    "target": relation.get("target_entity", "N/A")
                })
            
            # Check for weak evidence
            evidence_strength = relation.get("evidence_strength", "unknown")
            if evidence_strength in ["weak", "moderate"]:
                analysis["weak_evidence"].append({
                    "relation_id": relation_id,
                    "type": rel_type,
                    "strength": evidence_strength,
                    "source": relation.get("source_entity", "N/A"),
                    "target": relation.get("target_entity", "N/A")
                })
            
            # Create summary
            analysis["relation_summary"].append({
                "relation_id": relation_id,
                "type": rel_type,
                "source": relation.get("source_entity", "N/A"),
                "target": relation.get("target_entity", "N/A"),
                "evidence_count": len(evidence),
                "evidence_strength": evidence_strength
            })
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline for completeness and issues"""
    analysis = {
        "total_phases": 0,
        "phase_summary": [],
        "event_distribution": {},
        "gaps_and_overlaps": []
    }
    
    phases = timeline_data.get("timeline_phases", {})
    analysis["total_phases"] = len(phases)
    
    phase_list = []
    for phase_key, phase_data in phases.items():
        phase_id = phase_data.get("phase_id", "UNKNOWN")
        phase_name = phase_data.get("phase_name", "N/A")
        start_date = phase_data.get("start_date", "N/A")
        end_date = phase_data.get("end_date", "N/A")
        events = phase_data.get("events", [])
        event_count = phase_data.get("event_count", len(events))
        
        phase_list.append({
            "phase_id": phase_id,
            "phase_name": phase_name,
            "start_date": start_date,
            "end_date": end_date,
            "event_count": event_count,
            "events": events
        })
        
        analysis["event_distribution"][phase_id] = event_count
    
    # Sort phases by start date
    phase_list.sort(key=lambda x: x["start_date"])
    analysis["phase_summary"] = phase_list
    
    # Check for gaps and overlaps
    for i in range(len(phase_list) - 1):
        current_end = phase_list[i]["end_date"]
        next_start = phase_list[i + 1]["start_date"]
        
        if current_end != next_start:
            analysis["gaps_and_overlaps"].append({
                "between": f"{phase_list[i]['phase_name']} and {phase_list[i+1]['phase_name']}",
                "current_end": current_end,
                "next_start": next_start
            })
    
    return analysis

def cross_reference_analysis(entities_data, events_data, relations_data, timeline_data):
    """Cross-reference analysis between all data models"""
    analysis = {
        "entity_event_consistency": [],
        "event_phase_consistency": [],
        "relation_entity_consistency": []
    }
    
    # Extract all entity IDs
    all_entity_ids = set()
    for category, entity_list in entities_data.get("entities", {}).items():
        for entity in entity_list:
            all_entity_ids.add(entity.get("entity_id"))
    
    # Extract all event IDs
    all_event_ids = set()
    for event in events_data.get("events", []):
        all_event_ids.add(event.get("event_id"))
    
    # Check entity-event consistency
    for category, entity_list in entities_data.get("entities", {}).items():
        for entity in entity_list:
            entity_id = entity.get("entity_id")
            timeline_events = entity.get("timeline_events", [])
            
            for event_id in timeline_events:
                if event_id not in all_event_ids:
                    analysis["entity_event_consistency"].append({
                        "issue": "entity_references_nonexistent_event",
                        "entity_id": entity_id,
                        "event_id": event_id
                    })
    
    # Check event-phase consistency
    phase_ids = set()
    for phase_key, phase_data in timeline_data.get("timeline_phases", {}).items():
        phase_ids.add(phase_data.get("phase_id"))
    
    for event in events_data.get("events", []):
        event_id = event.get("event_id")
        phase = event.get("timeline_phase", "UNASSIGNED")
        
        if phase != "UNASSIGNED" and phase not in phase_ids:
            analysis["event_phase_consistency"].append({
                "issue": "event_references_nonexistent_phase",
                "event_id": event_id,
                "phase": phase
            })
    
    # Check relation-entity consistency
    for rel_type, relation_list in relations_data.get("relations", {}).items():
        for relation in relation_list:
            relation_id = relation.get("relation_id")
            source = relation.get("source_entity")
            target = relation.get("target_entity")
            
            if source and source not in all_entity_ids and not source in ["director", "associates", "accounts", "bank_accounts", "financial_systems"]:
                analysis["relation_entity_consistency"].append({
                    "issue": "relation_references_nonexistent_source_entity",
                    "relation_id": relation_id,
                    "source_entity": source
                })
            
            if target and target not in all_entity_ids and not target in ["director", "associates", "accounts", "bank_accounts", "financial_systems"]:
                analysis["relation_entity_consistency"].append({
                    "issue": "relation_references_nonexistent_target_entity",
                    "relation_id": relation_id,
                    "target_entity": target
                })
    
    return analysis

def main():
    """Main analysis function"""
    print("=" * 80)
    print("COMPREHENSIVE DATA MODEL ANALYSIS")
    print("=" * 80)
    
    # Load all data models
    entities_data = load_json("data_models/entities/entities.json")
    events_data = load_json("data_models/events/events.json")
    relations_data = load_json("data_models/relations/relations.json")
    timeline_data = load_json("data_models/timelines/timeline_enhanced.json")
    
    # Perform analyses
    print("\n1. ENTITY ANALYSIS")
    print("-" * 80)
    entity_analysis = analyze_entities(entities_data)
    print(f"Total Entities: {entity_analysis['total_entities']}")
    print(f"By Category: {json.dumps(entity_analysis['by_category'], indent=2)}")
    print(f"Missing Timeline Events: {len(entity_analysis['missing_timeline_events'])}")
    print(f"Zero Involvement Events: {len(entity_analysis['zero_involvement_events'])}")
    print(f"Missing Relationships: {len(entity_analysis['missing_relationships'])}")
    
    print("\n2. EVENT ANALYSIS")
    print("-" * 80)
    event_analysis = analyze_events(events_data)
    print(f"Total Events: {event_analysis['total_events']}")
    print(f"By Category: {json.dumps(dict(event_analysis['by_category']), indent=2)}")
    print(f"By Phase: {json.dumps(dict(event_analysis['by_phase']), indent=2)}")
    print(f"Missing Perpetrators: {len(event_analysis['missing_perpetrators'])}")
    print(f"Missing Victims: {len(event_analysis['missing_victims'])}")
    print(f"Missing Financial Impact: {len(event_analysis['missing_financial_impact'])}")
    
    print("\n3. RELATION ANALYSIS")
    print("-" * 80)
    relation_analysis = analyze_relations(relations_data)
    print(f"Total Relations: {relation_analysis['total_relations']}")
    print(f"By Type: {json.dumps(relation_analysis['by_type'], indent=2)}")
    print(f"Missing Evidence: {len(relation_analysis['missing_evidence'])}")
    print(f"Weak Evidence: {len(relation_analysis['weak_evidence'])}")
    
    print("\n4. TIMELINE ANALYSIS")
    print("-" * 80)
    timeline_analysis = analyze_timeline(timeline_data)
    print(f"Total Phases: {timeline_analysis['total_phases']}")
    print(f"Event Distribution: {json.dumps(timeline_analysis['event_distribution'], indent=2)}")
    print(f"Gaps and Overlaps: {len(timeline_analysis['gaps_and_overlaps'])}")
    
    print("\n5. CROSS-REFERENCE ANALYSIS")
    print("-" * 80)
    cross_ref_analysis = cross_reference_analysis(entities_data, events_data, relations_data, timeline_data)
    print(f"Entity-Event Inconsistencies: {len(cross_ref_analysis['entity_event_consistency'])}")
    print(f"Event-Phase Inconsistencies: {len(cross_ref_analysis['event_phase_consistency'])}")
    print(f"Relation-Entity Inconsistencies: {len(cross_ref_analysis['relation_entity_consistency'])}")
    
    # Save comprehensive analysis
    comprehensive_analysis = {
        "metadata": {
            "analysis_date": datetime.now().isoformat(),
            "version": "1.0"
        },
        "entity_analysis": entity_analysis,
        "event_analysis": event_analysis,
        "relation_analysis": relation_analysis,
        "timeline_analysis": timeline_analysis,
        "cross_reference_analysis": cross_ref_analysis
    }
    
    output_file = "COMPREHENSIVE_DATA_ANALYSIS_2025-11-18.json"
    with open(output_file, 'w') as f:
        json.dump(comprehensive_analysis, f, indent=2)
    
    print(f"\n{'=' * 80}")
    print(f"Analysis complete. Results saved to: {output_file}")
    print(f"{'=' * 80}")

if __name__ == "__main__":
    main()
