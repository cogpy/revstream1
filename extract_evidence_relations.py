#!/usr/bin/env python3
"""
Extract and analyze the 17 relations that had evidence added
Focus on financially significant relations
"""

import json
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_relations_with_evidence(relations_data):
    """Extract all relations and categorize by evidence status"""
    
    relations_by_type = {}
    relations_with_added_evidence = []
    
    for rel_type, relation_list in relations_data.get("relations", {}).items():
        relations_by_type[rel_type] = []
        
        for relation in relation_list:
            relation_id = relation.get("relation_id", "UNKNOWN")
            source = relation.get("source_entity", "N/A")
            target = relation.get("target_entity", "N/A")
            evidence = relation.get("evidence", [])
            
            # Identify relations that likely had evidence added
            # (generic evidence patterns indicate automated addition)
            generic_evidence_patterns = [
                "timeline_analysis",
                "event_sequence_documentation",
                "coordinated_actions",
                "pattern_analysis",
                "timeline_correlation",
                "operational_records",
                "decision_documentation",
                "documented_evidence",
                "case_file_records"
            ]
            
            has_generic_evidence = any(e in evidence for e in generic_evidence_patterns)
            
            relation_info = {
                "relation_id": relation_id,
                "relation_type": rel_type,
                "source_entity": source,
                "target_entity": target,
                "evidence": evidence,
                "evidence_count": len(evidence),
                "has_generic_evidence": has_generic_evidence,
                "full_relation": relation
            }
            
            relations_by_type[rel_type].append(relation_info)
            
            if has_generic_evidence:
                relations_with_added_evidence.append(relation_info)
    
    return relations_by_type, relations_with_added_evidence

def analyze_financial_significance(relation_info):
    """Determine financial significance of a relation"""
    
    relation = relation_info["full_relation"]
    financial_indicators = []
    
    # Check for financial amount
    amount = relation.get("amount", "")
    if amount:
        financial_indicators.append(("amount", amount))
    
    # Check for financial type
    financial_type = relation.get("financial_type", "")
    if financial_type:
        financial_indicators.append(("financial_type", financial_type))
    
    # Check for financial impact
    financial_impact = relation.get("financial_impact", "")
    if financial_impact:
        financial_indicators.append(("financial_impact", financial_impact))
    
    # Check for debt amount
    debt_amount = relation.get("debt_amount", "")
    if debt_amount:
        financial_indicators.append(("debt_amount", debt_amount))
    
    # Extract numeric value for sorting
    numeric_value = 0
    for indicator_type, value in financial_indicators:
        if isinstance(value, str) and "R" in value:
            # Extract numeric value from string like "R4,276,832.85"
            try:
                numeric_str = value.replace("R", "").replace(",", "").replace("+", "").split()[0]
                numeric_value = max(numeric_value, float(numeric_str))
            except:
                pass
    
    return {
        "financial_indicators": financial_indicators,
        "numeric_value": numeric_value,
        "is_financial": len(financial_indicators) > 0
    }

def create_detailed_report(relations_with_added_evidence, entities_data, events_data):
    """Create detailed report of relations with added evidence"""
    
    # Load entity and event data for context
    entity_lookup = {}
    for category, entity_list in entities_data.get("entities", {}).items():
        for entity in entity_list:
            entity_lookup[entity.get("entity_id")] = entity
    
    event_lookup = {}
    for event in events_data.get("events", []):
        event_lookup[event.get("event_id")] = event
    
    # Analyze financial significance
    for relation_info in relations_with_added_evidence:
        financial_analysis = analyze_financial_significance(relation_info)
        relation_info["financial_analysis"] = financial_analysis
    
    # Sort by financial significance
    relations_with_added_evidence.sort(
        key=lambda x: x["financial_analysis"]["numeric_value"],
        reverse=True
    )
    
    # Create detailed report
    report = {
        "summary": {
            "total_relations_with_added_evidence": len(relations_with_added_evidence),
            "financially_significant_count": sum(1 for r in relations_with_added_evidence if r["financial_analysis"]["is_financial"])
        },
        "relations_by_financial_significance": []
    }
    
    for relation_info in relations_with_added_evidence:
        relation = relation_info["full_relation"]
        financial_analysis = relation_info["financial_analysis"]
        
        # Get entity details
        source_entity = entity_lookup.get(relation_info["source_entity"], {})
        target_entity = entity_lookup.get(relation_info["target_entity"], {})
        
        detailed_entry = {
            "relation_id": relation_info["relation_id"],
            "relation_type": relation_info["relation_type"],
            "source_entity": {
                "id": relation_info["source_entity"],
                "name": source_entity.get("name", relation_info["source_entity"]),
                "type": source_entity.get("agent_type", "N/A")
            },
            "target_entity": {
                "id": relation_info["target_entity"],
                "name": target_entity.get("name", relation_info["target_entity"]),
                "type": target_entity.get("agent_type", "N/A")
            },
            "evidence_added": relation_info["evidence"],
            "financial_significance": {
                "is_financial": financial_analysis["is_financial"],
                "indicators": financial_analysis["financial_indicators"],
                "numeric_value": financial_analysis["numeric_value"]
            },
            "additional_context": {
                "legal_status": relation.get("legal_status", "N/A"),
                "evidence_strength": relation.get("evidence_strength", "N/A"),
                "timeline_events": relation.get("timeline_events", []),
                "shared_events": relation.get("shared_events", [])
            }
        }
        
        report["relations_by_financial_significance"].append(detailed_entry)
    
    return report

def main():
    """Main extraction function"""
    print("=" * 80)
    print("EVIDENCE DOCUMENTATION ANALYSIS - 17 RELATIONS")
    print("=" * 80)
    
    # Load data models
    print("\n1. Loading data models...")
    relations_data = load_json("data_models/relations/relations.json")
    entities_data = load_json("data_models/entities/entities.json")
    events_data = load_json("data_models/events/events.json")
    
    # Extract relations with evidence
    print("2. Extracting relations with added evidence...")
    relations_by_type, relations_with_added_evidence = extract_relations_with_evidence(relations_data)
    
    print(f"   Found {len(relations_with_added_evidence)} relations with added evidence")
    
    # Create detailed report
    print("3. Creating detailed report...")
    detailed_report = create_detailed_report(relations_with_added_evidence, entities_data, events_data)
    
    # Save report
    output_file = "EVIDENCE_RELATIONS_DETAILED_REPORT.json"
    with open(output_file, 'w') as f:
        json.dump(detailed_report, f, indent=2)
    
    print(f"\n{'=' * 80}")
    print(f"Analysis complete. Report saved to: {output_file}")
    print(f"{'=' * 80}")
    
    # Print summary
    print(f"\nSummary:")
    print(f"  Total relations with added evidence: {detailed_report['summary']['total_relations_with_added_evidence']}")
    print(f"  Financially significant: {detailed_report['summary']['financially_significant_count']}")
    
    print(f"\nTop 5 Financially Significant Relations:")
    for i, relation in enumerate(detailed_report["relations_by_financial_significance"][:5], 1):
        if relation["financial_significance"]["is_financial"]:
            print(f"\n  {i}. {relation['relation_id']} ({relation['relation_type']})")
            print(f"     {relation['source_entity']['name']} → {relation['target_entity']['name']}")
            for indicator_type, value in relation["financial_significance"]["indicators"]:
                print(f"     {indicator_type}: {value}")

if __name__ == "__main__":
    main()
