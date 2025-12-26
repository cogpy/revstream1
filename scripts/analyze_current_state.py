#!/usr/bin/env python3.11
import json
from datetime import datetime
from collections import defaultdict

# Load the comprehensive analysis
with open('COMPREHENSIVE_ANALYSIS_2025_12_25.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("CURRENT STATE ANALYSIS - REVSTREAM1")
print("=" * 80)
print(f"\nTimestamp: {data['timestamp']}")

# Entities Analysis
entities = data['entities']
print(f"\n{'ENTITIES':-^80}")
print(f"Version: {entities['version']}")
print(f"Total Count: {entities['total_count']}")
print(f"  - Persons: {entities['persons']}")
print(f"  - Organizations: {entities['organizations']}")

# List all persons
persons = entities['data']['entities']['persons']
print(f"\nPersons ({len(persons)}):")
for p in persons:
    print(f"  {p['entity_id']}: {p['name']} - {p['role']}")
    print(f"    Events: {p.get('involvement_events', 0)}, Evidence Strength: {p.get('evidence_strength', 'N/A')}")

# List all organizations
orgs = entities['data']['entities']['organizations']
print(f"\nOrganizations ({len(orgs)}):")
for o in orgs:
    print(f"  {o['entity_id']}: {o['name']} - {o['role']}")
    print(f"    Events: {o.get('involvement_events', 0)}, Evidence Strength: {o.get('evidence_strength', 'N/A')}")

# Relations Analysis
relations = data['relations']
print(f"\n{'RELATIONS':-^80}")
print(f"Version: {relations['version']}")
print(f"Total Count: {relations['total_count']}")
print(f"By Type: {relations['by_type']}")

rels_data = relations['data']['relations']
print(f"\nRelationships ({len(rels_data)}):")
for r in rels_data[:10]:  # Show first 10
    print(f"  {r['relation_id']}: {r['source']} -> {r['target']}")
    print(f"    Type: {r['type']}, Strength: {r.get('strength', 'N/A')}")

# Events Analysis
events = data['events']
print(f"\n{'EVENTS':-^80}")
print(f"Version: {events['version']}")
print(f"Total Count: {events['total_count']}")

events_data = events['data']['events']
print(f"\nEvent Categories:")
categories = defaultdict(int)
for e in events_data:
    categories[e.get('category', 'unknown')] += 1
for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
    print(f"  {cat}: {count}")

print(f"\nCritical Events (first 10):")
for e in events_data[:10]:
    print(f"  {e['event_id']}: {e['date']} - {e['title']}")
    print(f"    Category: {e.get('category', 'N/A')}, Impact: {e.get('impact_level', 'N/A')}")

# Timeline Analysis
timelines = data['timelines']
print(f"\n{'TIMELINES':-^80}")
print(f"Version: {timelines['version']}")
print(f"Total Phases: {timelines['total_phases']}")
print(f"Phases: {timelines['phases']}")

tl_data = timelines['data']
print(f"\nTimeline Components:")
for key in tl_data.keys():
    if key != 'metadata':
        print(f"  - {key}")

# Evidence Mapping
evidence = data.get('evidence_mapping', {})
print(f"\n{'EVIDENCE MAPPING':-^80}")
print(f"Total Evidence Items: {evidence.get('total_evidence_items', 0)}")
print(f"Evidence Categories: {list(evidence.get('evidence_categories', {}).keys())}")

# Burden of Proof
burden = data.get('burden_of_proof_analysis', {})
print(f"\n{'BURDEN OF PROOF':-^80}")
if burden:
    print(f"Civil Threshold (50%): {burden.get('civil_threshold_met', 'N/A')}")
    print(f"Criminal Threshold (95%): {burden.get('criminal_threshold_met', 'N/A')}")

# Filing Recommendations
filings = data.get('filing_recommendations', {})
print(f"\n{'FILING RECOMMENDATIONS':-^80}")
if filings:
    for filing_type, details in filings.items():
        if isinstance(details, dict):
            print(f"  {filing_type}: {details.get('status', 'N/A')}")

print("\n" + "=" * 80)
