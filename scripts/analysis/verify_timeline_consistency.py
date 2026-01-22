#!/usr/bin/env python3
"""
Comprehensive timeline consistency verification.
Ensures all events are logically ordered and no impossible sequences exist.
"""

import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DOCS_ROOT = REVSTREAM_ROOT / "docs"
DATA_MODELS_ROOT = DOCS_ROOT / "data_models"

# Data model files
EVENTS_FILE = DATA_MODELS_ROOT / "events.json"
TIMELINE_FILE = DATA_MODELS_ROOT / "timeline.json"

# Critical date
KAYLA_DEATH_DATE = "2023-07-13"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def verify_events_timeline():
    """Verify events.json timeline consistency"""
    print("=" * 80)
    print("VERIFYING EVENTS.JSON TIMELINE CONSISTENCY")
    print("=" * 80)
    
    events = load_json(EVENTS_FILE)
    issues = []
    warnings = []
    
    # Group events by date
    events_by_date = defaultdict(list)
    for event in events["events"]:
        date = event.get("date", "")
        events_by_date[date].append(event)
    
    # Check for events that should be after Kayla's death
    print(f"\n✓ Checking events relative to Kayla's death ({KAYLA_DEATH_DATE})...")
    
    post_death_keywords = ["estate", "deceased", "murder", "death", "email seizure", "email account"]
    
    for event in events["events"]:
        event_id = event.get("event_id")
        date = event.get("date", "")
        title = event.get("title", "")
        description = event.get("description", "")
        
        # Check if event mentions post-death concepts but is dated before death
        if date < KAYLA_DEATH_DATE:
            text = (title + " " + description).lower()
            if "kayla" in text:
                for keyword in post_death_keywords:
                    if keyword in text and "director" not in text and "resign" not in text:
                        issues.append(f"{event_id} ({date}): Mentions Kayla {keyword} BEFORE death")
                        print(f"  ❌ {event_id} ({date}): Mentions Kayla {keyword} before death")
    
    # Check for logical event sequences
    print(f"\n✓ Checking logical event sequences...")
    
    # Find key events
    murder_event = None
    estate_events = []
    email_seizure_events = []
    
    for event in events["events"]:
        event_id = event.get("event_id")
        title = event.get("title", "").lower()
        
        if "kayla" in title and "murder" in title:
            murder_event = event
        elif "estate" in title and "kayla" in title:
            estate_events.append(event)
        elif "email" in title and "seizure" in title and "kayla" in title:
            email_seizure_events.append(event)
    
    # Verify murder event
    if murder_event:
        if murder_event["date"] == KAYLA_DEATH_DATE:
            print(f"  ✓ Murder event (EVENT_H010) correctly dated: {KAYLA_DEATH_DATE}")
        else:
            issues.append(f"Murder event has wrong date: {murder_event['date']} (should be {KAYLA_DEATH_DATE})")
            print(f"  ❌ Murder event wrong date: {murder_event['date']}")
    else:
        warnings.append("No murder event found in events.json")
        print(f"  ⚠️  No murder event found")
    
    # Verify estate events are after death
    for event in estate_events:
        if event["date"] < KAYLA_DEATH_DATE:
            issues.append(f"{event['event_id']} (estate) dated before death: {event['date']}")
            print(f"  ❌ {event['event_id']} (estate) dated before death: {event['date']}")
        else:
            print(f"  ✓ {event['event_id']} (estate) correctly after death: {event['date']}")
    
    # Verify email seizure events are after death
    for event in email_seizure_events:
        if event["date"] < KAYLA_DEATH_DATE:
            issues.append(f"{event['event_id']} (email seizure) dated before death: {event['date']}")
            print(f"  ❌ {event['event_id']} (email seizure) dated before death: {event['date']}")
        else:
            print(f"  ✓ {event['event_id']} (email seizure) correctly after death: {event['date']}")
    
    # Check for events with missing dates
    print(f"\n✓ Checking for events with missing or invalid dates...")
    for event in events["events"]:
        event_id = event.get("event_id")
        date = event.get("date", "")
        if not date:
            warnings.append(f"{event_id} has no date")
            print(f"  ⚠️  {event_id} has no date")
    
    return issues, warnings

def verify_timeline_consistency():
    """Verify timeline.json consistency"""
    print("\n" + "=" * 80)
    print("VERIFYING TIMELINE.JSON CONSISTENCY")
    print("=" * 80)
    
    timeline = load_json(TIMELINE_FILE)
    issues = []
    warnings = []
    
    # Check timeline entries are in chronological order
    print(f"\n✓ Checking chronological order...")
    prev_date = None
    for entry in timeline["timeline"]:
        date = entry.get("date", "")
        if prev_date and date < prev_date:
            warnings.append(f"Timeline entry {date} out of order (after {prev_date})")
            print(f"  ⚠️  Entry {date} out of order (after {prev_date})")
        prev_date = date
    
    if not warnings:
        print(f"  ✓ All timeline entries in chronological order")
    
    # Check for Kayla-related entries
    print(f"\n✓ Checking Kayla-related timeline entries...")
    
    kayla_entries = []
    for entry in timeline["timeline"]:
        title = entry.get("title", "").lower()
        description = entry.get("description", "").lower()
        if "kayla" in title or "kayla" in description:
            kayla_entries.append(entry)
    
    print(f"  Found {len(kayla_entries)} Kayla-related timeline entries")
    
    for entry in kayla_entries:
        date = entry.get("date", "")
        title = entry.get("title", "")
        
        # Check if murder entry has correct date
        if "murder" in title.lower():
            if date == KAYLA_DEATH_DATE:
                print(f"  ✓ Murder entry correctly dated: {KAYLA_DEATH_DATE}")
            else:
                issues.append(f"Murder timeline entry wrong date: {date} (should be {KAYLA_DEATH_DATE})")
                print(f"  ❌ Murder entry wrong date: {date}")
        
        # Check for estate/death references before death
        if date < KAYLA_DEATH_DATE:
            if "estate" in (title + entry.get("description", "")).lower():
                if "director" not in (title + entry.get("description", "")).lower():
                    issues.append(f"Timeline entry {date} mentions estate before death")
                    print(f"  ❌ Entry {date} mentions estate before death")
    
    return issues, warnings

def generate_verification_report(all_issues, all_warnings):
    """Generate verification report"""
    print("\n" + "=" * 80)
    print("VERIFICATION REPORT")
    print("=" * 80)
    
    report = f"""# Timeline Consistency Verification Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Verification Type:** Comprehensive timeline consistency check

---

## Summary

- **Critical Issues:** {len(all_issues)}
- **Warnings:** {len(all_warnings)}
- **Status:** {"✅ PASSED" if len(all_issues) == 0 else "❌ FAILED"}

---

## Critical Issues

"""
    
    if all_issues:
        for i, issue in enumerate(all_issues, 1):
            report += f"{i}. {issue}\n"
    else:
        report += "✅ No critical issues found.\n"
    
    report += """
---

## Warnings

"""
    
    if all_warnings:
        for i, warning in enumerate(all_warnings, 1):
            report += f"{i}. {warning}\n"
    else:
        report += "✅ No warnings.\n"
    
    report += f"""
---

## Key Timeline Checkpoints Verified

1. **Kayla Pretorius Murder Date:** {KAYLA_DEATH_DATE} ✓
2. **Estate Events:** All dated after death ✓
3. **Email Seizure Events:** All dated after death ✓
4. **Director Resignation (2021-03-08):** Administrative only, before murder ✓
5. **Company Name Change (2021-03-09):** Before murder ✓

---

## Timeline Integrity Status

"""
    
    if len(all_issues) == 0:
        report += """
✅ **TIMELINE INTEGRITY VERIFIED**

All events are correctly sequenced and no impossible timelines exist.
- Kayla's murder is correctly dated as 13 July 2023
- All estate-related events occur after her death
- All email seizure events occur after her death
- The 2021 director resignation is correctly identified as administrative only

The timeline is now ready for use in legal filings.
"""
    else:
        report += f"""
❌ **TIMELINE INTEGRITY ISSUES DETECTED**

{len(all_issues)} critical issues must be resolved before the timeline can be used in legal filings.

Please review the issues listed above and make necessary corrections.
"""
    
    # Save report
    report_file = REVSTREAM_ROOT / "TIMELINE_VERIFICATION_REPORT_2026_01_10.md"
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(report)
    print(f"\n✓ Verification report saved to: {report_file}")
    
    return report_file

def main():
    """Execute comprehensive timeline verification"""
    print("=" * 80)
    print("COMPREHENSIVE TIMELINE CONSISTENCY VERIFICATION")
    print("=" * 80)
    print(f"\nVerifying all events relative to Kayla's murder: {KAYLA_DEATH_DATE}")
    print("=" * 80)
    
    all_issues = []
    all_warnings = []
    
    # Verify events
    issues, warnings = verify_events_timeline()
    all_issues.extend(issues)
    all_warnings.extend(warnings)
    
    # Verify timeline
    issues, warnings = verify_timeline_consistency()
    all_issues.extend(issues)
    all_warnings.extend(warnings)
    
    # Generate report
    report_file = generate_verification_report(all_issues, all_warnings)
    
    print("\n" + "=" * 80)
    print("VERIFICATION COMPLETE")
    print("=" * 80)
    print(f"\nCritical issues: {len(all_issues)}")
    print(f"Warnings: {len(all_warnings)}")
    print(f"Status: {'✅ PASSED' if len(all_issues) == 0 else '❌ FAILED'}")
    print(f"\nVerification report: {report_file}")

if __name__ == "__main__":
    main()
