import json
import os
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_entities(entities_data):
    """Analyze entities structure and completeness"""
    analysis = {
        "total_entities": 0,
        "by_type": defaultdict(int),
        "missing_timeline_events": [],
        "missing_financial_impact": [],
        "entities_with_events": 0,
        "entities_without_events": 0
    }
    
    for entity_type, entities in entities_data.get('entities', {}).items():
        if isinstance(entities, list):
            analysis["by_type"][entity_type] = len(entities)
            analysis["total_entities"] += len(entities)
            
            for entity in entities:
                entity_id = entity.get('entity_id', 'UNKNOWN')
                
                # Check timeline events
                timeline_events = entity.get('timeline_events', [])
                if timeline_events:
                    analysis["entities_with_events"] += 1
                else:
                    if entity.get('involvement_events', 0) > 0:
                        analysis["missing_timeline_events"].append(entity_id)
                        analysis["entities_without_events"] += 1
                
                # Check financial impact
                if entity.get('agent_type') in ['antagonist', 'accomplice']:
                    if not entity.get('financial_impact'):
                        analysis["missing_financial_impact"].append(entity_id)
    
    return analysis

def analyze_events(events_data):
    """Analyze events structure and completeness"""
    analysis = {
        "total_events": len(events_data.get('events', [])),
        "by_category": defaultdict(int),
        "by_phase": defaultdict(int),
        "events_with_financial_impact": 0,
        "events_without_financial_impact": 0,
        "missing_perpetrators": [],
        "missing_evidence": [],
        "date_coverage": {"earliest": None, "latest": None}
    }
    
    dates = []
    for event in events_data.get('events', []):
        event_id = event.get('event_id', 'UNKNOWN')
        category = event.get('category', 'uncategorized')
        phase = event.get('timeline_phase', 'PHASE_UNKNOWN')
        
        analysis["by_category"][category] += 1
        analysis["by_phase"][phase] += 1
        
        # Check financial impact
        if event.get('financial_impact') and event['financial_impact'] not in ['unknown', 'N/A', 'unknown_amount']:
            analysis["events_with_financial_impact"] += 1
        else:
            analysis["events_without_financial_impact"] += 1
        
        # Check perpetrators
        if not event.get('perpetrators'):
            analysis["missing_perpetrators"].append(event_id)
        
        # Check evidence
        if not event.get('evidence') and not event.get('evidence_sources'):
            analysis["missing_evidence"].append(event_id)
        
        # Date tracking
        if event.get('date'):
            dates.append(event['date'])
    
    if dates:
        analysis["date_coverage"]["earliest"] = min(dates)
        analysis["date_coverage"]["latest"] = max(dates)
    
    return analysis

def analyze_relations(relations_data):
    """Analyze relations structure and completeness"""
    analysis = {
        "total_relations": 0,
        "by_type": defaultdict(int),
        "missing_evidence": [],
        "relations_with_timeline": 0,
        "relations_without_timeline": 0
    }
    
    for relation_type, relations in relations_data.get('relations', {}).items():
        if isinstance(relations, list):
            analysis["by_type"][relation_type] = len(relations)
            analysis["total_relations"] += len(relations)
            
            for relation in relations:
                relation_id = relation.get('relation_id', 'UNKNOWN')
                
                # Check evidence
                if not relation.get('evidence'):
                    analysis["missing_evidence"].append(relation_id)
                
                # Check timeline events
                if relation.get('timeline_events'):
                    analysis["relations_with_timeline"] += 1
                else:
                    analysis["relations_without_timeline"] += 1
    
    return analysis

def analyze_timeline(timeline_data):
    """Analyze timeline structure and completeness"""
    analysis = {
        "total_phases": 0,
        "phases": {},
        "total_events_in_phases": 0,
        "orphaned_events": [],
        "phase_coverage": {}
    }
    
    for phase_key, phase_data in timeline_data.get('timeline_phases', {}).items():
        phase_id = phase_data.get('phase_id', 'UNKNOWN')
        phase_events = phase_data.get('events', [])
        
        analysis["total_phases"] += 1
        analysis["total_events_in_phases"] += len(phase_events)
        analysis["phases"][phase_id] = {
            "name": phase_data.get('phase_name'),
            "event_count": len(phase_events),
            "duration_days": phase_data.get('duration_days'),
            "financial_impact": phase_data.get('financial_impact')
        }
    
    return analysis

def main():
    base_path = "/home/ubuntu/revstream1/data_models"
    
    # Load all data models
    entities = load_json(f"{base_path}/entities/entities.json")
    events = load_json(f"{base_path}/events/events.json")
    relations = load_json(f"{base_path}/relations/relations.json")
    timeline = load_json(f"{base_path}/timelines/timeline_enhanced.json")
    
    # Perform analysis
    entities_analysis = analyze_entities(entities)
    events_analysis = analyze_events(events)
    relations_analysis = analyze_relations(relations)
    timeline_analysis = analyze_timeline(timeline)
    
    # Compile comprehensive report
    report = {
        "metadata": {
            "analysis_date": "2025-11-17",
            "entities_version": entities.get('metadata', {}).get('version'),
            "events_version": events.get('metadata', {}).get('version'),
            "relations_version": relations.get('metadata', {}).get('version'),
            "timeline_version": timeline.get('metadata', {}).get('version')
        },
        "entities_analysis": entities_analysis,
        "events_analysis": events_analysis,
        "relations_analysis": relations_analysis,
        "timeline_analysis": timeline_analysis,
        "data_quality_issues": {
            "entities_missing_timeline_events": entities_analysis["missing_timeline_events"],
            "entities_missing_financial_impact": entities_analysis["missing_financial_impact"],
            "events_missing_perpetrators": events_analysis["missing_perpetrators"],
            "events_missing_evidence": events_analysis["missing_evidence"],
            "relations_missing_evidence": relations_analysis["missing_evidence"]
        }
    }
    
    # Save report
    with open(f"{base_path}/COMPREHENSIVE_MODEL_ANALYSIS.json", 'w') as f:
        json.dump(report, f, indent=2)
    
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
