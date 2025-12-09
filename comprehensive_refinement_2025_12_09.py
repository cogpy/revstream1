#!/usr/bin/env python3
"""
Comprehensive Refinement Script for Revenue Stream Hijacking Case
Date: 2025-12-09
Purpose: Analyze and refine entities, relations, events, and timelines with latest evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = BASE_DIR / "data_models"
ENTITIES_DIR = DATA_MODELS_DIR / "entities"
RELATIONS_DIR = DATA_MODELS_DIR / "relations"
EVENTS_DIR = DATA_MODELS_DIR / "events"
TIMELINES_DIR = DATA_MODELS_DIR / "timelines"

# Latest files
ENTITIES_FILE = ENTITIES_DIR / "entities_refined_2025_12_09_v28.json"
RELATIONS_FILE = RELATIONS_DIR / "relations_refined_2025_12_07_v22.json"
EVENTS_FILE = EVENTS_DIR / "events_refined_2025_12_09_v32.json"
TIMELINE_FILE = TIMELINES_DIR / "timeline_refined_2025_12_09_v21.json"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    """Save JSON file with pretty formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_entities(entities_data):
    """Analyze entities for completeness and evidence strength"""
    analysis = {
        "total_entities": 0,
        "by_type": {},
        "evidence_strength": {"strong": 0, "medium": 0, "weak": 0, "none": 0},
        "missing_evidence": [],
        "recommendations": []
    }
    
    for entity_type, entities in entities_data.get("entities", {}).items():
        if isinstance(entities, list):
            analysis["total_entities"] += len(entities)
            analysis["by_type"][entity_type] = len(entities)
            
            for entity in entities:
                entity_id = entity.get("entity_id", "UNKNOWN")
                strength = entity.get("evidence_strength", "none")
                analysis["evidence_strength"][strength] = analysis["evidence_strength"].get(strength, 0) + 1
                
                # Check for missing evidence support
                if "evidence_support" not in entity or not entity.get("evidence_support"):
                    analysis["missing_evidence"].append({
                        "entity_id": entity_id,
                        "name": entity.get("name", "UNKNOWN"),
                        "type": entity_type
                    })
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations for completeness"""
    analysis = {
        "total_relations": 0,
        "by_type": {},
        "missing_evidence": [],
        "recommendations": []
    }
    
    for relation_type, relations in relations_data.get("relations", {}).items():
        if isinstance(relations, list):
            analysis["total_relations"] += len(relations)
            analysis["by_type"][relation_type] = len(relations)
            
            for relation in relations:
                relation_id = relation.get("relation_id", "UNKNOWN")
                
                # Check for missing evidence
                if "evidence" not in relation or not relation.get("evidence"):
                    analysis["missing_evidence"].append({
                        "relation_id": relation_id,
                        "type": relation_type,
                        "source": relation.get("source_entity", relation.get("from_entity", "UNKNOWN")),
                        "target": relation.get("target_entity", relation.get("to_entity", "UNKNOWN"))
                    })
    
    return analysis

def analyze_events(events_data):
    """Analyze events for completeness and timeline coverage"""
    analysis = {
        "total_events": 0,
        "by_category": {},
        "by_year": {},
        "missing_financial_impact": [],
        "missing_evidence": [],
        "recommendations": []
    }
    
    events = events_data.get("events", [])
    analysis["total_events"] = len(events)
    
    for event in events:
        event_id = event.get("event_id", "UNKNOWN")
        category = event.get("category", "uncategorized")
        date = event.get("date", "unknown")
        
        # Count by category
        analysis["by_category"][category] = analysis["by_category"].get(category, 0) + 1
        
        # Count by year
        if date != "unknown":
            year = date.split("-")[0]
            analysis["by_year"][year] = analysis["by_year"].get(year, 0) + 1
        
        # Check for missing financial impact
        if "financial_impact" not in event or event.get("financial_impact") == "unknown_amount":
            analysis["missing_financial_impact"].append({
                "event_id": event_id,
                "title": event.get("title", "UNKNOWN"),
                "date": date
            })
        
        # Check for missing evidence
        if "evidence" not in event or not event.get("evidence"):
            analysis["missing_evidence"].append({
                "event_id": event_id,
                "title": event.get("title", "UNKNOWN"),
                "date": date
            })
    
    return analysis

def identify_improvements():
    """Identify specific improvements needed"""
    improvements = {
        "entities": [],
        "relations": [],
        "events": [],
        "timeline": [],
        "github_pages": []
    }
    
    # SF9 Attorney Letter improvements
    improvements["entities"].append({
        "priority": "HIGH",
        "item": "Add SF9 evidence to PERSON_001 (Peter) showing R63M debt",
        "evidence": "SF9 - Attorney Letter 23 October 2025",
        "action": "Update PERSON_001 financial_impact with R63M quantum"
    })
    
    improvements["entities"].append({
        "priority": "HIGH",
        "item": "Add SF9 evidence to PERSON_005 (Daniel) showing R63M victim amount",
        "evidence": "SF9 - Attorney Letter 23 October 2025",
        "action": "Update PERSON_005 financial_impact with R63M quantum"
    })
    
    # SF2A/SF2B improvements
    improvements["entities"].append({
        "priority": "CRITICAL",
        "item": "Add SF2A evidence to PERSON_002 (Rynette) for dual account access",
        "evidence": "SF2A - Sage User Access showing Pete@regima.com account",
        "action": "Update PERSON_002 criminal_liability with identity_impersonation evidence"
    })
    
    improvements["entities"].append({
        "priority": "CRITICAL",
        "item": "Add SF2B evidence to PERSON_002 (Rynette) for subscription control",
        "evidence": "SF2B - Sage Subscription Expiry showing Rynette as owner",
        "action": "Update PERSON_002 criminal_liability with obstruction_of_access evidence"
    })
    
    # SF1A improvements
    improvements["entities"].append({
        "priority": "HIGH",
        "item": "Add SF1A evidence to PERSON_007 (Bantjies) for call option schedule",
        "evidence": "SF1A - Bantjies Call Option Agreement excerpt",
        "action": "Update PERSON_007 financial_details with payment schedule"
    })
    
    # Relations improvements
    improvements["relations"].append({
        "priority": "HIGH",
        "item": "Create relation for Rynette's control of Sage subscription",
        "evidence": "SF2B",
        "action": "Add REL_CTRL_XXX: PERSON_002 controls SAGE_SUBSCRIPTION"
    })
    
    improvements["relations"].append({
        "priority": "HIGH",
        "item": "Create relation for Rynette's dual account access",
        "evidence": "SF2A",
        "action": "Add REL_ACCESS_XXX: PERSON_002 impersonates PERSON_001 via Pete@regima.com"
    })
    
    # Events improvements
    improvements["events"].append({
        "priority": "HIGH",
        "item": "Add event for SF9 attorney letter demand",
        "evidence": "SF9 - 23 October 2025",
        "action": "Create EVENT_XXX: R63M Formal Demand by Ian Levitt Attorneys"
    })
    
    improvements["events"].append({
        "priority": "CRITICAL",
        "item": "Add event for Sage subscription expiry",
        "evidence": "SF2B - 23 July 2025",
        "action": "Create EVENT_XXX: Sage Account Expiry - Access Obstruction"
    })
    
    improvements["events"].append({
        "priority": "HIGH",
        "item": "Add event for Rynette dual account discovery",
        "evidence": "SF2A - 20 June 2025",
        "action": "Create EVENT_XXX: Discovery of Rynette's Dual Account Access"
    })
    
    # Timeline improvements
    improvements["timeline"].append({
        "priority": "HIGH",
        "item": "Add timeline entry for SF9 attorney letter",
        "date": "2025-10-23",
        "action": "Add formal demand timeline entry"
    })
    
    improvements["timeline"].append({
        "priority": "CRITICAL",
        "item": "Add timeline entry for Sage expiry",
        "date": "2025-07-23",
        "action": "Add obstruction timeline entry"
    })
    
    # GitHub Pages improvements
    improvements["github_pages"].append({
        "priority": "HIGH",
        "item": "Update evidence index with SF9, SF10, SF2A, SF2B, SF1A",
        "action": "Add new annexures to evidence-index-enhanced.md"
    })
    
    improvements["github_pages"].append({
        "priority": "HIGH",
        "item": "Create entity relationship visualization",
        "action": "Generate mermaid diagram showing all entity relations with evidence links"
    })
    
    improvements["github_pages"].append({
        "priority": "MEDIUM",
        "item": "Update timeline.html with new events",
        "action": "Regenerate interactive timeline with SF9, SF2A, SF2B events"
    })
    
    return improvements

def generate_report():
    """Generate comprehensive analysis report"""
    print("Loading data models...")
    entities = load_json(ENTITIES_FILE)
    relations = load_json(RELATIONS_FILE)
    events = load_json(EVENTS_FILE)
    timeline = load_json(TIMELINE_FILE)
    
    print("\nAnalyzing entities...")
    entities_analysis = analyze_entities(entities)
    
    print("Analyzing relations...")
    relations_analysis = analyze_relations(relations)
    
    print("Analyzing events...")
    events_analysis = analyze_events(events)
    
    print("Identifying improvements...")
    improvements = identify_improvements()
    
    report = {
        "metadata": {
            "generated": datetime.now().isoformat(),
            "purpose": "Comprehensive analysis and refinement recommendations",
            "case_number": "2025-137857"
        },
        "current_state": {
            "entities": entities_analysis,
            "relations": relations_analysis,
            "events": events_analysis,
            "timeline": {
                "total_entries": len(timeline.get("timeline", [])),
                "date_range": f"{timeline.get('timeline', [{}])[0].get('date', 'unknown')} to {timeline.get('timeline', [{}])[-1].get('date', 'unknown')}"
            }
        },
        "improvements": improvements,
        "summary": {
            "total_improvements": sum(len(v) for v in improvements.values()),
            "critical_items": sum(1 for category in improvements.values() for item in category if item.get("priority") == "CRITICAL"),
            "high_priority_items": sum(1 for category in improvements.values() for item in category if item.get("priority") == "HIGH"),
            "medium_priority_items": sum(1 for category in improvements.values() for item in category if item.get("priority") == "MEDIUM")
        }
    }
    
    # Save report
    report_file = BASE_DIR / "COMPREHENSIVE_ANALYSIS_REPORT_2025_12_09.json"
    save_json(report, report_file)
    print(f"\nReport saved to: {report_file}")
    
    # Print summary
    print("\n" + "="*80)
    print("COMPREHENSIVE ANALYSIS SUMMARY")
    print("="*80)
    print(f"\nCurrent State:")
    print(f"  Entities: {entities_analysis['total_entities']}")
    print(f"  Relations: {relations_analysis['total_relations']}")
    print(f"  Events: {events_analysis['total_events']}")
    print(f"  Timeline Entries: {report['current_state']['timeline']['total_entries']}")
    
    print(f"\nEvidence Strength Distribution:")
    for strength, count in entities_analysis['evidence_strength'].items():
        print(f"  {strength.capitalize()}: {count}")
    
    print(f"\nImprovements Needed:")
    print(f"  Total: {report['summary']['total_improvements']}")
    print(f"  Critical: {report['summary']['critical_items']}")
    print(f"  High Priority: {report['summary']['high_priority_items']}")
    print(f"  Medium Priority: {report['summary']['medium_priority_items']}")
    
    print("\n" + "="*80)
    
    return report

if __name__ == "__main__":
    report = generate_report()
