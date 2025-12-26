#!/usr/bin/env python3
"""
Comprehensive Data Model Analysis and Refinement Script
Date: 2025-12-16
Purpose: Analyze and refine entities, relations, events & timelines with ad-res-j7 evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_ROOT = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS = REVSTREAM_ROOT / "data_models"

# Load current data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved: {filepath}")

# Load all current models
print("📊 Loading current data models...")
entities = load_json(DATA_MODELS / "entities" / "entities.json")
relations = load_json(DATA_MODELS / "relations" / "relations.json")
events = load_json(DATA_MODELS / "events" / "events.json")

# Load latest timeline
timeline_files = list((DATA_MODELS / "timelines").glob("*.json"))
timeline_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
timeline = load_json(timeline_files[0]) if timeline_files else {"entries": []}

print(f"📌 Entities: {len(entities.get('entities', {}).get('persons', []))} persons")
print(f"📌 Relations: {len(relations.get('relations', {}).get('ownership_relations', []))} ownership relations")
print(f"📌 Events: {len(events.get('events', []))} events")
print(f"📌 Timeline: {timeline.get('metadata', {}).get('total_events', 0)} entries")

# Analysis Report
analysis = {
    "timestamp": datetime.now().isoformat(),
    "current_state": {
        "entities": {
            "persons": len(entities.get('entities', {}).get('persons', [])),
            "organizations": len(entities.get('entities', {}).get('organizations', [])),
            "platforms": len(entities.get('entities', {}).get('platforms', [])),
            "domains": len(entities.get('entities', {}).get('domains', []))
        },
        "relations": {
            "ownership": len(relations.get('relations', {}).get('ownership_relations', [])),
            "control": len(relations.get('relations', {}).get('control_relations', [])),
            "financial": len(relations.get('relations', {}).get('financial_relations', [])),
            "conspiracy": len(relations.get('relations', {}).get('conspiracy_relations', []))
        },
        "events": {
            "total": len(events.get('events', [])),
            "with_financial_impact": len([e for e in events.get('events', []) if e.get('financial_impact')])
        },
        "timeline": {
            "total_entries": timeline.get('metadata', {}).get('total_events', 0)
        }
    },
    "evidence_sources": {
        "JF01": "Shopify Plus Email (26 July 2017) - CRITICAL",
        "JF02": "Shopify Sales Reports - HIGH",
        "JF03": "Financial Records and Analysis - HIGH",
        "JF04": "Daniel Faucitt Personal Bank Records - HIGH",
        "JF05": "Correspondence Evidence - MEDIUM",
        "JF06": "Court Documents and Filings - HIGH",
        "JF07": "Screenshots and Visual Evidence - MEDIUM",
        "JF08": "Evidence Packages (May-October 2025) - HIGH",
        "JF09": "Timeline Analysis - HIGH",
        "JF10": "Additional Evidence",
        "JF11": "Additional Evidence",
        "JF12": "Additional Evidence",
        "SF1": "Bantjies Debt Documentation",
        "SF2": "Sage Screenshots - Rynette Control - CRITICAL",
        "SF3": "Strategic Logistics Stock Adjustment",
        "SF4": "SARS Audit Email",
        "SF5": "Adderory Company Registration Stock Supply",
        "SF6": "Kayla Pretorius Estate Documentation - CRITICAL",
        "SF7": "Court Order Kayla Email Seizure",
        "SF8": "Linda Employment Records"
    },
    "improvements_needed": []
}

# Check for missing evidence references
print("\n🔍 Analyzing evidence coverage...")

# Check entities for evidence references
for person in entities.get('entities', {}).get('persons', []):
    person_id = person.get('entity_id')
    evidence = person.get('evidence', [])
    ad_res_refs = person.get('ad_res_j7_references', [])
    
    if not ad_res_refs or len(ad_res_refs) < 2:
        analysis['improvements_needed'].append({
            "type": "entity_evidence",
            "entity_id": person_id,
            "name": person.get('name'),
            "issue": "Insufficient ad-res-j7 evidence references",
            "current_count": len(ad_res_refs),
            "recommended_action": "Add specific evidence file references from ad-res-j7"
        })

# Check events for evidence references
events_without_evidence = []
for event in events.get('events', []):
    event_id = event.get('event_id')
    evidence = event.get('evidence', [])
    
    if not evidence or len(evidence) == 0:
        events_without_evidence.append(event_id)
        analysis['improvements_needed'].append({
            "type": "event_evidence",
            "event_id": event_id,
            "title": event.get('title'),
            "date": event.get('date'),
            "issue": "No evidence references",
            "recommended_action": "Add evidence references from JF/SF series"
        })

print(f"⚠️  Events without evidence: {len(events_without_evidence)}")

# Check timeline for evidence integration
timeline_entries = timeline.get('entries', [])
timeline_without_evidence = []
for entry in timeline_entries:
    if 'evidence' not in entry or not entry.get('evidence'):
        timeline_without_evidence.append(entry.get('date'))

print(f"⚠️  Timeline entries without evidence: {len(timeline_without_evidence)}")

# Suggestions for improvement
analysis['suggestions'] = [
    {
        "priority": "CRITICAL",
        "category": "Evidence Integration",
        "action": "Ensure all entities have comprehensive ad-res-j7 references",
        "impact": "Strengthens burden of proof for both civil (50%) and criminal (95%) standards"
    },
    {
        "priority": "HIGH",
        "category": "Timeline Enhancement",
        "action": "Add critical evidence dates from SF6 (Kayla Pretorius death) and SF2 (Sage control)",
        "impact": "Establishes clear timeline of conspiracy and evidence destruction"
    },
    {
        "priority": "HIGH",
        "category": "Event Refinement",
        "action": "Link all financial impact events to specific evidence sources",
        "impact": "Quantifies damages with documentary support"
    },
    {
        "priority": "MEDIUM",
        "category": "Relation Enhancement",
        "action": "Add conspiracy relations based on SF2 (Rynette control) evidence",
        "impact": "Demonstrates coordinated action and joint liability"
    },
    {
        "priority": "MEDIUM",
        "category": "GitHub Pages",
        "action": "Update all application evidence pages with direct links to ad-res-j7 files",
        "impact": "Improves navigation and evidence accessibility"
    }
]

# Save analysis report
save_json(analysis, REVSTREAM_ROOT / f"DATA_MODEL_ANALYSIS_2025_12_16.json")

print("\n✅ Analysis complete!")
print(f"📊 Total improvements needed: {len(analysis['improvements_needed'])}")
print(f"💡 Total suggestions: {len(analysis['suggestions'])}")
print("\nNext steps:")
print("1. Review DATA_MODEL_ANALYSIS_2025_12_16.json")
print("2. Implement entity refinements")
print("3. Enhance timeline with critical evidence dates")
print("4. Update GitHub Pages with evidence links")
print("5. Refine legal filings based on evidence standards")
