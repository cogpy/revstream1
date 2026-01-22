#!/usr/bin/env python3
"""
Comprehensive audit and fix for Kayla Pretorius death date timeline errors.
CRITICAL: Kayla was murdered on 13 July 2023, NOT in 2021.
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DOCS_ROOT = REVSTREAM_ROOT / "docs"
DATA_MODELS_ROOT = DOCS_ROOT / "data_models"

# Data model files
ENTITIES_FILE = DATA_MODELS_ROOT / "entities" / "entities.json"
RELATIONS_FILE = DATA_MODELS_ROOT / "relations.json"
EVENTS_FILE = DATA_MODELS_ROOT / "events.json"
TIMELINE_FILE = DATA_MODELS_ROOT / "timeline.json"

# Critical date
KAYLA_DEATH_DATE = "2023-07-13"
KAYLA_DEATH_DATE_DISPLAY = "13 July 2023"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file with formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def audit_events():
    """Audit events.json for timeline errors"""
    print("=" * 80)
    print("AUDITING EVENTS.JSON")
    print("=" * 80)
    
    events = load_json(EVENTS_FILE)
    errors = []
    fixes = []
    
    for event in events["events"]:
        event_id = event.get("event_id")
        date = event.get("date", "")
        title = event.get("title", "")
        description = event.get("description", "")
        
        # Check for Kayla murder event
        if event_id == "EVENT_H010":
            print(f"\n✓ Found Kayla murder event: {event_id}")
            print(f"  Current date: {date}")
            if date != KAYLA_DEATH_DATE:
                errors.append(f"EVENT_H010 has WRONG date: {date} (should be {KAYLA_DEATH_DATE})")
                event["date"] = KAYLA_DEATH_DATE
                fixes.append(f"Fixed EVENT_H010 date: {date} → {KAYLA_DEATH_DATE}")
                print(f"  ❌ INCORRECT - should be {KAYLA_DEATH_DATE}")
            else:
                print(f"  ✓ CORRECT")
        
        # Check for events dated 2021 that mention Kayla death/murder
        if date.startswith("2021"):
            if any(term in description.lower() for term in ["kayla", "death", "murder", "deceased", "estate"]):
                if "resigned" not in description.lower():  # Kayla did resign in 2021, that's valid
                    errors.append(f"{event_id} dated {date} mentions Kayla death/estate (should be post-2023)")
                    print(f"\n⚠️  {event_id} ({date}): mentions Kayla death/estate")
                    print(f"    Description: {description[:100]}...")
        
        # Check for events dated 2021-2022 that are described as "post-Kayla death"
        if date.startswith("2021") or date.startswith("2022"):
            if any(term in title.lower() + description.lower() for term in ["post-kayla", "after kayla", "following kayla"]):
                errors.append(f"{event_id} dated {date} described as post-Kayla death (should be post-2023)")
                print(f"\n⚠️  {event_id} ({date}): described as post-Kayla death")
                print(f"    Title: {title}")
    
    # Save fixed events
    if fixes:
        save_json(EVENTS_FILE, events)
        print(f"\n✓ Applied {len(fixes)} fixes to events.json")
    
    return errors, fixes

def audit_timeline():
    """Audit timeline.json for timeline errors"""
    print("\n" + "=" * 80)
    print("AUDITING TIMELINE.JSON")
    print("=" * 80)
    
    timeline = load_json(TIMELINE_FILE)
    errors = []
    fixes = []
    
    for entry in timeline["timeline"]:
        date = entry.get("date", "")
        title = entry.get("title", "")
        description = entry.get("description", "")
        
        # Check for Kayla murder entry
        if "kayla" in title.lower() and "murder" in title.lower():
            print(f"\n✓ Found Kayla murder timeline entry")
            print(f"  Current date: {date}")
            if date != KAYLA_DEATH_DATE:
                errors.append(f"Kayla murder timeline entry has WRONG date: {date} (should be {KAYLA_DEATH_DATE})")
                entry["date"] = KAYLA_DEATH_DATE
                fixes.append(f"Fixed Kayla murder timeline date: {date} → {KAYLA_DEATH_DATE}")
                print(f"  ❌ INCORRECT - should be {KAYLA_DEATH_DATE}")
            else:
                print(f"  ✓ CORRECT")
        
        # Check for entries dated 2021-2022 that mention Kayla death/estate
        if date.startswith("2021") or date.startswith("2022"):
            if any(term in (title + description).lower() for term in ["kayla.*death", "kayla.*murder", "kayla.*estate", "post.*kayla", "after.*kayla"]):
                if "resigned" not in (title + description).lower():
                    errors.append(f"Timeline entry {date} mentions Kayla death/estate (should be post-2023)")
                    print(f"\n⚠️  Timeline entry ({date}): mentions Kayla death/estate")
                    print(f"    Title: {title}")
    
    # Save fixed timeline
    if fixes:
        save_json(TIMELINE_FILE, timeline)
        print(f"\n✓ Applied {len(fixes)} fixes to timeline.json")
    
    return errors, fixes

def audit_entities():
    """Audit entities.json for timeline errors"""
    print("\n" + "=" * 80)
    print("AUDITING ENTITIES.JSON")
    print("=" * 80)
    
    entities = load_json(ENTITIES_FILE)
    errors = []
    
    # Check Kayla Pretorius entity
    for person in entities["entities"]["persons"]:
        if person.get("entity_id") == "PERSON_013":
            print(f"\n✓ Found Kayla Pretorius entity (PERSON_013)")
            notes = person.get("notes", "")
            if "2021" in notes and "death" in notes.lower():
                errors.append("PERSON_013 notes mention 2021 and death (should be 2023)")
                print(f"  ⚠️  Notes mention 2021 and death")
            print(f"  Role: {person.get('role', 'N/A')}")
    
    return errors

def audit_markdown_files():
    """Audit markdown files for timeline errors"""
    print("\n" + "=" * 80)
    print("AUDITING MARKDOWN FILES")
    print("=" * 80)
    
    errors = []
    fixes = []
    
    # Check FINAL_REFINEMENT_REPORT
    report_file = REVSTREAM_ROOT / "FINAL_REFINEMENT_REPORT_2026_01_10.md"
    if report_file.exists():
        with open(report_file, 'r') as f:
            content = f.read()
        
        # Find the problematic line
        if "2021-03-15 to 2021-10-05:** Post-Kayla death asset appropriation period" in content:
            errors.append("FINAL_REFINEMENT_REPORT contains '2021 Post-Kayla death' (should be 2023)")
            print(f"\n⚠️  Found error in FINAL_REFINEMENT_REPORT_2026_01_10.md")
            print(f"    Line: '2021-03-15 to 2021-10-05:** Post-Kayla death asset appropriation period'")
            
            # Fix it - this should be about company structure changes, NOT post-Kayla death
            content = content.replace(
                "- **2021-03-15 to 2021-10-05:** Post-Kayla death asset appropriation period",
                "- **2021-03-15 to 2021-10-05:** Company structure manipulation period (RegimA SA name change, director changes)"
            )
            
            with open(report_file, 'w') as f:
                f.write(content)
            
            fixes.append("Fixed FINAL_REFINEMENT_REPORT: Changed '2021 Post-Kayla death' to 'Company structure manipulation'")
            print(f"  ✓ FIXED")
    
    # Check evidence catalog
    evidence_catalog = REVSTREAM_ROOT / "evidence" / "EVIDENCE_CATALOG.md"
    if evidence_catalog.exists():
        with open(evidence_catalog, 'r') as f:
            content = f.read()
        
        # The 2021 Kayla resignation is CORRECT - she did resign in 2021, murdered in 2023
        if "Kayla resigned (2021-03-08)" in content:
            print(f"\n✓ EVIDENCE_CATALOG.md correctly shows Kayla resigned 2021-03-08 (before her murder in 2023)")
    
    return errors, fixes

def generate_audit_report(all_errors, all_fixes):
    """Generate comprehensive audit report"""
    print("\n" + "=" * 80)
    print("AUDIT REPORT SUMMARY")
    print("=" * 80)
    
    report = f"""# Timeline Audit Report: Kayla Pretorius Death Date

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Critical Fact:** Kayla Pretorius was murdered on **{KAYLA_DEATH_DATE_DISPLAY}**

## Errors Found

Total errors: {len(all_errors)}

"""
    
    if all_errors:
        for i, error in enumerate(all_errors, 1):
            report += f"{i}. {error}\n"
    else:
        report += "✓ No errors found.\n"
    
    report += f"""
## Fixes Applied

Total fixes: {len(all_fixes)}

"""
    
    if all_fixes:
        for i, fix in enumerate(all_fixes, 1):
            report += f"{i}. {fix}\n"
    else:
        report += "No fixes needed.\n"
    
    report += """
## Key Timeline Facts

1. **Kayla Pretorius resigned as director of RegimA SA:** 2021-03-08 (CORRECT)
2. **RegimA SA name change (K OZ CREATIVE → REGIMA SA):** 2021-03-09 (CORRECT)
3. **Kayla Pretorius murdered:** 2023-07-13 (CRITICAL DATE)
4. **Post-murder asset appropriation:** 2023-07-13 onwards

## Recommendations

1. All events dated 2021-2022 that reference "post-Kayla death" or "Kayla estate" should be reviewed
2. The period 2021-03-15 to 2021-10-05 is about company structure manipulation, NOT post-Kayla death
3. All references to Kayla's death should use the date 2023-07-13
4. Kayla's resignation in 2021 is a separate event from her murder in 2023

## Next Steps

1. Review all timeline gaps identified in previous reports
2. Ensure no other events are misdated relative to Kayla's death
3. Cross-reference all ad-res-j7 evidence for date accuracy
4. Update legal filings if any contain timeline errors
"""
    
    # Save report
    report_file = REVSTREAM_ROOT / "TIMELINE_AUDIT_REPORT_2026_01_10.md"
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(report)
    print(f"\n✓ Audit report saved to: {report_file}")
    
    return report_file

def main():
    """Execute comprehensive timeline audit"""
    print("=" * 80)
    print("TIMELINE AUDIT: KAYLA PRETORIUS DEATH DATE")
    print("=" * 80)
    print(f"\nCRITICAL FACT: Kayla Pretorius was murdered on {KAYLA_DEATH_DATE_DISPLAY}")
    print("=" * 80)
    
    all_errors = []
    all_fixes = []
    
    # Audit all data sources
    errors, fixes = audit_events()
    all_errors.extend(errors)
    all_fixes.extend(fixes)
    
    errors, fixes = audit_timeline()
    all_errors.extend(errors)
    all_fixes.extend(fixes)
    
    errors = audit_entities()
    all_errors.extend(errors)
    
    errors, fixes = audit_markdown_files()
    all_errors.extend(errors)
    all_fixes.extend(fixes)
    
    # Generate report
    report_file = generate_audit_report(all_errors, all_fixes)
    
    print("\n" + "=" * 80)
    print("AUDIT COMPLETE")
    print("=" * 80)
    print(f"\nTotal errors found: {len(all_errors)}")
    print(f"Total fixes applied: {len(all_fixes)}")
    print(f"\nAudit report: {report_file}")

if __name__ == "__main__":
    main()
