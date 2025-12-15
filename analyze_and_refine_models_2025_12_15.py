#!/usr/bin/env python3
"""
Comprehensive Data Model Analysis and Refinement
Based on evidence from both revstream1 and ad-res-j7 repositories
Date: 2025-12-15
"""

import json
import os
from datetime import datetime
from collections import defaultdict

# Paths
REVSTREAM_BASE = "/home/ubuntu/revstream1"
AD_RES_BASE = "/home/ubuntu/ad-res-j7"
DATA_MODELS_DIR = f"{REVSTREAM_BASE}/data_models"

# Load latest data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Load current models
print("Loading current data models...")
entities = load_json(f"{DATA_MODELS_DIR}/entities/entities_refined_2025_12_14_v35.json")
events = load_json(f"{DATA_MODELS_DIR}/events/events_refined_2025_12_14_v35.json")
relations = load_json(f"{DATA_MODELS_DIR}/relations/relations_refined_2025_12_14_v30.json")
timeline = load_json(f"{DATA_MODELS_DIR}/timelines/timeline_refined_2025_12_14_v22.json")

# Analysis Report
report = {
    "analysis_date": datetime.now().isoformat(),
    "version": "v36",
    "entities_analysis": {},
    "events_analysis": {},
    "relations_analysis": {},
    "timeline_analysis": {},
    "improvements": [],
    "evidence_gaps": [],
    "recommendations": []
}

# Analyze Entities
print("\nAnalyzing entities...")
entity_count = {
    "persons": len(entities["entities"]["persons"]),
    "organizations": len(entities["entities"]["organizations"]),
    "platforms": len(entities["entities"]["platforms"]),
    "bank_accounts": len(entities["entities"]["bank_accounts"])
}

report["entities_analysis"] = {
    "total_count": sum(entity_count.values()),
    "breakdown": entity_count,
    "version": entities["metadata"]["version"],
    "last_updated": entities["metadata"]["last_updated"]
}

# Analyze Events
print("Analyzing events...")
event_categories = defaultdict(int)
events_with_evidence = 0
events_without_evidence = 0

for event in events["events"]:
    event_categories[event.get("category", "unknown")] += 1
    if event.get("evidence") or event.get("evidence_support"):
        events_with_evidence += 1
    else:
        events_without_evidence += 1

report["events_analysis"] = {
    "total_events": events["metadata"]["total_events"],
    "categories": dict(event_categories),
    "with_evidence": events_with_evidence,
    "without_evidence": events_without_evidence,
    "evidence_coverage": f"{(events_with_evidence/len(events['events'])*100):.1f}%"
}

# Analyze Relations
print("Analyzing relations...")
relation_types = {
    "ownership": len(relations["relations"]["ownership_relations"]),
    "control": len(relations["relations"]["control_relations"]),
    "financial": len(relations["relations"]["financial_relations"]),
    "conspiracy": len(relations["relations"]["conspiracy_relations"])
}

report["relations_analysis"] = {
    "total_relations": sum(relation_types.values()),
    "breakdown": relation_types,
    "version": relations["metadata"]["version"]
}

# Analyze Timeline
print("Analyzing timeline...")
timeline_phases = defaultdict(int)
for entry in timeline["timeline_entries"]:
    phase = entry.get("phase", "unknown")
    timeline_phases[phase] += 1

report["timeline_analysis"] = {
    "total_entries": timeline["metadata"]["total_entries"],
    "date_range": timeline["metadata"]["date_range"],
    "phases": dict(timeline_phases)
}

# Check for evidence gaps
print("\nIdentifying evidence gaps...")

# Events without proper evidence references
for event in events["events"]:
    if not event.get("evidence") and not event.get("evidence_support"):
        report["evidence_gaps"].append({
            "event_id": event["event_id"],
            "title": event["title"],
            "date": event["date"],
            "issue": "Missing evidence references"
        })

# Check for ANNEXURES references
annexures_referenced = set()
for event in events["events"]:
    if event.get("evidence_support"):
        for ev in event["evidence_support"].get("evidence", []):
            if "JF" in ev or "SF" in ev:
                annexures_referenced.add(ev.split(" - ")[0] if " - " in ev else ev)

print(f"Found {len(annexures_referenced)} unique ANNEXURE references")

# Recommendations
report["recommendations"] = [
    {
        "priority": "HIGH",
        "category": "evidence_integration",
        "recommendation": "Enhance all events with specific ANNEXURE references from ad-res-j7",
        "affected_items": events_without_evidence
    },
    {
        "priority": "HIGH",
        "category": "timeline_refinement",
        "recommendation": "Add more granular timeline entries for critical fraud events in March-May 2025",
        "rationale": "Escalation phase needs more detailed tracking"
    },
    {
        "priority": "MEDIUM",
        "category": "entity_enhancement",
        "recommendation": "Add more detailed financial impact tracking per entity",
        "rationale": "Better burden of proof documentation"
    },
    {
        "priority": "MEDIUM",
        "category": "relations_expansion",
        "recommendation": "Map more conspiracy relations based on SF evidence files",
        "rationale": "SF1-SF8 contain additional relationship evidence"
    },
    {
        "priority": "HIGH",
        "category": "github_pages",
        "recommendation": "Create comprehensive evidence index linking all applications to ANNEXURES",
        "rationale": "Clear evidence trail for each legal claim"
    }
]

# Save report
report_path = f"{REVSTREAM_BASE}/DATA_MODEL_ANALYSIS_2025_12_15.json"
save_json(report, report_path)
print(f"\nAnalysis report saved to: {report_path}")

# Print summary
print("\n" + "="*60)
print("DATA MODEL ANALYSIS SUMMARY")
print("="*60)
print(f"\nEntities: {report['entities_analysis']['total_count']}")
for entity_type, count in entity_count.items():
    print(f"  - {entity_type}: {count}")

print(f"\nEvents: {report['events_analysis']['total_events']}")
print(f"  - With evidence: {events_with_evidence} ({report['events_analysis']['evidence_coverage']})")
print(f"  - Without evidence: {events_without_evidence}")

print(f"\nRelations: {report['relations_analysis']['total_relations']}")
for rel_type, count in relation_types.items():
    print(f"  - {rel_type}: {count}")

print(f"\nTimeline: {report['timeline_analysis']['total_entries']} entries")
print(f"  Date range: {timeline['metadata']['date_range']['start']} to {timeline['metadata']['date_range']['end']}")

print(f"\nEvidence Gaps: {len(report['evidence_gaps'])} events need evidence")
print(f"ANNEXURES Referenced: {len(annexures_referenced)}")

print(f"\nRecommendations: {len(report['recommendations'])}")
for rec in report["recommendations"]:
    print(f"  [{rec['priority']}] {rec['recommendation']}")

print("\n" + "="*60)
