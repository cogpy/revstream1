#!/usr/bin/env python3
"""
Timeline Completeness Script - 2026-01-22
Ensures the timeline is complete by cross-referencing all events and adding missing entries.
"""

import json
import os
from datetime import datetime
from copy import deepcopy

REVSTREAM_PATH = "/home/ubuntu/revstream1"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def get_event_details(events_data, event_id):
    """Get event details by ID"""
    for event in events_data.get('events', []):
        if event.get('event_id') == event_id:
            return event
    return None

def ensure_timeline_complete():
    """Ensure all events are in the timeline"""
    
    # Load data
    events_data = load_json(f"{REVSTREAM_PATH}/data_models/events/events.json")
    timeline_data = load_json(f"{REVSTREAM_PATH}/data_models/timelines/timeline.json")
    
    # Create backup
    backup_path = f"{REVSTREAM_PATH}/data_models/timelines/timeline.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    save_json(backup_path, timeline_data)
    print(f"Backup created: {backup_path}")
    
    # Get existing timeline event refs
    existing_refs = set()
    for entry in timeline_data.get('timeline', []):
        if entry.get('event_ref'):
            existing_refs.add(entry.get('event_ref'))
    
    print(f"\nExisting timeline entries: {len(timeline_data.get('timeline', []))}")
    print(f"Entries with event_ref: {len(existing_refs)}")
    
    # Find events not in timeline
    missing_events = []
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        if event_id and event_id not in existing_refs:
            missing_events.append(event)
    
    print(f"Events missing from timeline: {len(missing_events)}")
    
    # Add missing events to timeline
    new_entries = []
    for event in missing_events:
        # Determine category based on event content
        category = "general"
        desc = (event.get('description', '') + event.get('significance', '')).lower()
        
        if 'ketoni' in desc or 'payout' in desc:
            category = "ketoni_motive"
        elif 'fraud' in desc or 'theft' in desc or 'criminal' in desc:
            category = "criminal_activity"
        elif 'cipc' in desc or 'company' in desc or 'director' in desc:
            category = "cipc_corporate"
        elif 'trust' in desc or 'trustee' in desc or 'beneficiary' in desc:
            category = "trust_violations"
        elif 'revenue' in desc or 'payment' in desc or 'transfer' in desc:
            category = "revenue_hijacking"
        elif 'email' in desc or 'domain' in desc or 'shopify' in desc:
            category = "digital_fraud"
        elif 'stock' in desc or 'inventory' in desc or 'warehouse' in desc:
            category = "stock_manipulation"
        elif 'bantjies' in desc or 'accountant' in desc:
            category = "professional_misconduct"
        elif 'kayla' in desc or 'estate' in desc or 'death' in desc:
            category = "kayla_estate"
        
        # Determine significance level
        significance = event.get('significance', '')
        if 'CRITICAL' in significance:
            level = "critical"
        elif 'HIGH' in significance or 'MAJOR' in significance:
            level = "high"
        elif 'MEDIUM' in significance:
            level = "medium"
        else:
            level = "low"
        
        new_entry = {
            "date": event.get('date', ''),
            "event_ref": event.get('event_id'),
            "title": event.get('title', event.get('event_id')),
            "description": event.get('description', ''),
            "category": category,
            "significance_level": level,
            "evidence_refs": event.get('evidence', []),
            "actors": event.get('actors', []),
            "added_date": datetime.now().strftime('%Y-%m-%d')
        }
        new_entries.append(new_entry)
    
    # Add new entries to timeline
    timeline_data['timeline'].extend(new_entries)
    
    # Sort timeline by date
    timeline_data['timeline'] = sorted(
        timeline_data['timeline'],
        key=lambda x: x.get('date', '') or '9999-99-99'
    )
    
    # Update metadata
    timeline_data['metadata']['total_entries'] = len(timeline_data['timeline'])
    timeline_data['metadata']['version'] = "27.0"
    timeline_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    timeline_data['metadata']['completeness_audit'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Save updated timeline
    save_json(f"{REVSTREAM_PATH}/data_models/timelines/timeline.json", timeline_data)
    print(f"\nAdded {len(new_entries)} new timeline entries")
    print(f"Total timeline entries: {len(timeline_data['timeline'])}")
    
    return len(new_entries), timeline_data

def add_key_missing_events():
    """Add key events that may be missing from events.json"""
    
    events_data = load_json(f"{REVSTREAM_PATH}/data_models/events/events.json")
    
    # Key events that should exist based on knowledge base
    key_events_to_add = [
        {
            "event_id": "EVENT_REGIMA_SA_DIVERSION",
            "date": "2025-03-01",
            "title": "RegimA SA Revenue Diversion Begins",
            "description": "Diversion of revenue from RegimA SA begins, marking the start of systematic revenue stream hijacking.",
            "significance": "CRITICAL: First documented revenue diversion event in the sabotage timeline.",
            "actors": ["PERSON_001", "PERSON_002"],
            "evidence": ["JF03", "Bank statements"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_RYNETTE_BANK_LETTER",
            "date": "2025-04-14",
            "title": "Rynette Bank Letter for RegimA Worldwide Diversion",
            "description": "Rynette sends bank letter to divert RegimA Worldwide funds, escalating the revenue hijacking scheme.",
            "significance": "CRITICAL: Documentary evidence of intentional fund diversion.",
            "actors": ["PERSON_002"],
            "evidence": ["Bank letter", "JF03"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_SHOPIFY_ORDERS_REMOVED",
            "date": "2025-05-23",
            "title": "Orders Removed from Shopify Platform",
            "description": "Orders systematically removed from Shopify platform, disrupting business operations and revenue tracking.",
            "significance": "CRITICAL: Evidence of deliberate business sabotage.",
            "actors": ["PERSON_002"],
            "evidence": ["Shopify logs", "JF01"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_SECRET_CARD_CANCELLATION",
            "date": "2025-06-07",
            "title": "Secret Card Cancellations",
            "description": "Bank cards secretly cancelled less than 24 hours after Daniel exposed Villa Via fraud to Bantjies.",
            "significance": "CRITICAL: Demonstrates consciousness of guilt and retaliation for fraud exposure.",
            "actors": ["PERSON_001", "PERSON_002"],
            "evidence": ["Bank records", "JF07"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_JAX_CONFRONTS_RYNETTE",
            "date": "2025-05-15",
            "title": "Jacqui Confronts Rynette About R1,035,000 Debt",
            "description": "Jacqui confronts Rynette regarding ZAR 1,035,000 owed by RegimA Skin Treatments to Rezonance since Feb 2023. Jacqui stated these funds were part of Kayla's estate.",
            "significance": "CRITICAL: Trigger event for subsequent retaliation (Shopify removal, domain registration).",
            "actors": ["PERSON_003", "PERSON_002"],
            "evidence": ["Communication records"],
            "burden_of_proof": "verified_testimonial"
        },
        {
            "event_id": "EVENT_ADDERORY_DOMAIN_REG",
            "date": "2025-05-29",
            "title": "Adderory Registers regimaskin.co.za Domain",
            "description": "New domain regimaskin.co.za registered by Adderory (Rynette's son's company) following Shopify shutdown, enabling customer hijacking.",
            "significance": "CRITICAL: Evidence of premeditated customer diversion scheme.",
            "actors": ["PERSON_002", "ORG_ADDERORY"],
            "evidence": ["Domain registration records", "JF08"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_ACCOUNTS_EMPTIED",
            "date": "2025-09-11",
            "title": "Company Accounts Emptied",
            "description": "All company accounts emptied, potentially because Daniel was still managing to pay creditors despite 6 months of sabotage.",
            "significance": "CRITICAL: Final act of financial sabotage.",
            "actors": ["PERSON_001", "PERSON_002"],
            "evidence": ["Bank statements", "JF07"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_KETONI_INCORPORATION",
            "date": "2023-02-20",
            "title": "Ketoni Investment Holdings Incorporation",
            "description": "Ketoni Investment Holdings (Pty) Ltd incorporated, establishing the entity that would later owe ZAR 18.75M to FFT.",
            "significance": "CRITICAL: Establishes the corporate vehicle for the central financial motive.",
            "actors": ["Kevin Derrick"],
            "evidence": ["CIPC records"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_FFT_KETONI_INVESTMENT",
            "date": "2023-04-24",
            "title": "FFT Invests in Ketoni - ZAR 18.75M Entitlement Established",
            "description": "Faucitt Family Trust invests in Ketoni Investment Holdings, receiving Share Certificate #3 for 5,000 A-Ordinary shares. This establishes the ZAR 18.75M payout entitlement due May 2026.",
            "significance": "CRITICAL: Establishes the central financial motive for all subsequent events.",
            "actors": ["FFT", "Ketoni"],
            "evidence": ["Share Certificate J246", "Investment agreement"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_BANTJIES_TRUSTEE_APPOINTMENT",
            "date": "2024-07-01",
            "title": "Bantjies Appointed FFT Trustee by Rynette",
            "description": "Daniel Jacobus Bantjies appointed as Trustee of Faucitt Family Trust by Rynette, T-10 months before Ketoni payout. Strategic appointment to consolidate trust control.",
            "significance": "CRITICAL: Strategic trustee appointment aligned with Ketoni payout timeline.",
            "actors": ["PERSON_002", "PERSON_007"],
            "evidence": ["Trust documents"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_SETTLEMENT_SIGNED",
            "date": "2025-08-11",
            "title": "Settlement Agreement Signed - Main Trustee Power Backdated",
            "description": "Settlement agreement signed with Jacqui's cooperation. Main Trustee power backdated, occurring T-9 months before Ketoni payout.",
            "significance": "CRITICAL: Consolidation of trust control before payout.",
            "actors": ["PERSON_001", "PERSON_003"],
            "evidence": ["Settlement agreement"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_INTERDICT_FILED",
            "date": "2025-08-13",
            "title": "Peter Files Interdict - Jax & Dan Betrayal",
            "description": "Peter files interdict in family court (not commercial court), 48 hours after settlement signing. Forum shopping to control beneficiaries' shares of Ketoni payout.",
            "significance": "CRITICAL: Forum shopping to maximize control over trust assets.",
            "actors": ["PERSON_001"],
            "evidence": ["Court filings", "JF06"],
            "burden_of_proof": "verified_documentary"
        },
        {
            "event_id": "EVENT_R63M_DEMAND",
            "date": "2025-10-23",
            "title": "Ian Levitt R63M Formal Demand Letter",
            "description": "Ian Levitt Attorneys sends formal demand letter for R63M, which is subsequently ignored by Peter and legal team.",
            "significance": "HIGH: Evidence of substantial financial exposure being ignored.",
            "actors": ["Ian Levitt Attorneys", "PERSON_001"],
            "evidence": ["SF9", "Demand letter"],
            "burden_of_proof": "verified_documentary"
        }
    ]
    
    # Check which events already exist
    existing_ids = set(e.get('event_id') for e in events_data.get('events', []))
    
    added_count = 0
    for event in key_events_to_add:
        if event['event_id'] not in existing_ids:
            events_data['events'].append(event)
            added_count += 1
            print(f"Added event: {event['event_id']} - {event['title']}")
    
    if added_count > 0:
        # Update metadata
        events_data['metadata']['total_events'] = len(events_data['events'])
        events_data['metadata']['version'] = "28.0"
        events_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        
        # Save
        save_json(f"{REVSTREAM_PATH}/data_models/events/events.json", events_data)
        print(f"\nAdded {added_count} new events to events.json")
    else:
        print("\nNo new events needed to be added to events.json")
    
    return added_count

def generate_timeline_report(timeline_data):
    """Generate a timeline completeness report"""
    
    report = f"""# Timeline Completeness Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

| Metric | Value |
|--------|-------|
| Total Timeline Entries | {timeline_data['metadata']['total_entries']} |
| Version | {timeline_data['metadata']['version']} |
| Last Updated | {timeline_data['metadata']['last_updated']} |

## Timeline by Category

"""
    
    # Count by category
    categories = {}
    for entry in timeline_data.get('timeline', []):
        cat = entry.get('category', 'uncategorized')
        categories[cat] = categories.get(cat, 0) + 1
    
    report += "| Category | Count |\n|----------|-------|\n"
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        report += f"| {cat} | {count} |\n"
    
    report += "\n## Timeline by Year\n\n"
    
    # Count by year
    years = {}
    for entry in timeline_data.get('timeline', []):
        date = entry.get('date', '')
        if date:
            year = date[:4]
            years[year] = years.get(year, 0) + 1
    
    report += "| Year | Events |\n|------|--------|\n"
    for year, count in sorted(years.items()):
        report += f"| {year} | {count} |\n"
    
    report += "\n## Critical Events\n\n"
    
    critical_events = [e for e in timeline_data.get('timeline', []) 
                       if e.get('significance_level') == 'critical']
    
    for event in sorted(critical_events, key=lambda x: x.get('date', '')):
        report += f"- **{event.get('date')}**: {event.get('title')}\n"
    
    return report

def main():
    print("=" * 60)
    print("Timeline Completeness Audit - 2026-01-22")
    print("=" * 60)
    
    # Step 1: Add key missing events to events.json
    print("\n[1/3] Adding key missing events to events.json...")
    events_added = add_key_missing_events()
    
    # Step 2: Ensure all events are in timeline
    print("\n[2/3] Ensuring all events are in timeline...")
    entries_added, timeline_data = ensure_timeline_complete()
    
    # Step 3: Generate report
    print("\n[3/3] Generating timeline completeness report...")
    report = generate_timeline_report(timeline_data)
    
    report_path = f"{REVSTREAM_PATH}/docs/TIMELINE_COMPLETENESS_REPORT_2026_01_22.md"
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Report saved: {report_path}")
    
    print("\n" + "=" * 60)
    print("Timeline Completeness Audit Complete!")
    print(f"Events added: {events_added}")
    print(f"Timeline entries added: {entries_added}")
    print(f"Total timeline entries: {timeline_data['metadata']['total_entries']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
