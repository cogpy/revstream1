#!/usr/bin/env python3
"""
Enhanced Timeline Evidence Cross-Reference Script
Date: 2026-01-12
Purpose: Add missing evidence references to timeline entries from ad-res-j7
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_BASE = Path("/home/ubuntu/revstream1")
AD_RES_J7_BASE = Path("/home/ubuntu/ad-res-j7")
TIMELINE_FILE = REVSTREAM_BASE / "data_models" / "timelines" / "timeline.json"
ANNEXURES_PATH = AD_RES_J7_BASE / "ANNEXURES"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """Save JSON file with backup"""
    # Create backup
    if filepath.exists():
        backup_path = filepath.parent / f"{filepath.stem}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        import shutil
        shutil.copy2(filepath, backup_path)
        print(f"Backup created: {backup_path}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {filepath}")

def map_evidence_to_timeline_entries():
    """Map evidence files to timeline entries based on keywords and dates"""
    
    # Evidence mapping for common events
    evidence_map = {
        # CIPC registrations
        "RegimA Skin Treatments CC Registration": ["ANNEXURES/JF04/", "CIPC WinDeed Report 293349755"],
        "AYMAC International CC Registration": ["ANNEXURES/JF04/", "CIPC records"],
        "Regima Worldwide Distribution registration": ["ANNEXURES/JF04/", "CIPC company records"],
        
        # Trust events
        "Faucitt Family Trust": ["ANNEXURES/JF10/", "Trust deed"],
        "trust": ["ANNEXURES/JF10/"],
        "trustee": ["ANNEXURES/JF10/"],
        
        # Financial events
        "Shopify": ["ANNEXURES/JF01/", "Shopify Plus email"],
        "revenue": ["ANNEXURES/JF01/", "ANNEXURES/JF08/"],
        "payment": ["ANNEXURES/JF07/", "bank records"],
        "transfer": ["ANNEXURES/JF07/", "bank statements"],
        
        # Court events
        "court": ["ANNEXURES/JF06/", "Court applications"],
        "application": ["ANNEXURES/JF06/"],
        "order": ["ANNEXURES/JF06/", "ANNEXURES/JF09/"],
        
        # Email and communication
        "email": ["ANNEXURES/JF01/", "ANNEXURES/SF7"],
        "correspondence": ["ANNEXURES/JF13/"],
        
        # Kayla Pretorius events
        "Kayla": ["ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md"],
        
        # POPIA violations
        "warehouse": ["ANNEXURES/JF08/", "POPIA violations"],
        "data": ["ANNEXURES/JF08/"],
        
        # Sage/Accounting
        "Sage": ["ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md"],
        "accounting": ["ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md"],
        
        # Stock/Logistics
        "stock": ["ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md"],
        "Strategic Logistics": ["ANNEXURES/SF3_Strategic_Logistics_Stock_Adjustment.md"],
        
        # SARS
        "SARS": ["ANNEXURES/SF4_SARS_Audit_Email.md"],
        "tax": ["ANNEXURES/SF4_SARS_Audit_Email.md"],
        
        # Adderory
        "Adderory": ["ANNEXURES/SF5_Adderory_Company_Registration_Stock_Supply.md"],
        
        # Linda
        "Linda": ["ANNEXURES/SF8_Linda_Employment_Records.md"],
        "bookkeeper": ["ANNEXURES/SF8_Linda_Employment_Records.md"],
        
        # Distributors
        "distributor": ["ANNEXURES/JF16-DISTRIBUTORS/"],
        "ALOECO": ["ANNEXURES/JF16-DISTRIBUTORS/", "293351602.Pdf"],
        "L'IMAGE": ["ANNEXURES/JF16-DISTRIBUTORS/", "293351642.Pdf"],
        "Logistic": ["ANNEXURES/JF16-DISTRIBUTORS/"],
        "UFO Express": ["ANNEXURES/JF16-DISTRIBUTORS/", "293352764.Pdf"],
    }
    
    return evidence_map

def enhance_timeline_with_evidence():
    """Add evidence references to timeline entries"""
    
    print("Loading timeline...")
    timeline = load_json(TIMELINE_FILE)
    
    evidence_map = map_evidence_to_timeline_entries()
    
    entries_updated = 0
    entries_already_have_evidence = 0
    entries_no_match = 0
    
    print(f"\nProcessing {len(timeline['timeline'])} timeline entries...")
    
    for entry in timeline['timeline']:
        # Skip if already has comprehensive evidence
        has_evidence = False
        if entry.get('evidence') and len(entry.get('evidence', [])) > 0:
            has_evidence = True
            entries_already_have_evidence += 1
        elif entry.get('source'):
            has_evidence = True
            entries_already_have_evidence += 1
        
        # Try to add evidence based on keywords
        added_evidence = []
        entry_text = f"{entry.get('event', '')} {entry.get('title', '')} {entry.get('description', '')}".lower()
        
        for keyword, evidence_refs in evidence_map.items():
            if keyword.lower() in entry_text:
                added_evidence.extend(evidence_refs)
        
        # Add evidence if found
        if added_evidence and not has_evidence:
            if 'evidence' not in entry:
                entry['evidence'] = []
            
            # Add unique evidence references
            for ref in added_evidence:
                if ref not in entry['evidence']:
                    entry['evidence'].append(ref)
            
            entries_updated += 1
            print(f"  ✓ Added evidence to: {entry.get('date')} - {entry.get('event', entry.get('title', 'Unknown'))[:60]}")
        elif not has_evidence and not added_evidence:
            entries_no_match += 1
    
    # Update metadata
    timeline['metadata']['last_updated'] = datetime.now().isoformat()
    timeline['metadata']['version'] = "24.0_EVIDENCE_ENHANCED_2026_01_12"
    timeline['metadata']['changes'] = f"Added evidence references to {entries_updated} entries from ad-res-j7 cross-reference"
    
    # Save updated timeline
    save_json(TIMELINE_FILE, timeline)
    
    print(f"\n{'='*80}")
    print("TIMELINE ENHANCEMENT SUMMARY")
    print(f"{'='*80}")
    print(f"Total entries: {len(timeline['timeline'])}")
    print(f"Already had evidence: {entries_already_have_evidence}")
    print(f"Updated with new evidence: {entries_updated}")
    print(f"No evidence match found: {entries_no_match}")
    print(f"{'='*80}")
    
    return timeline

def add_missing_cipc_events():
    """Add missing CIPC events from JF14, JF15, JF16"""
    
    print("\nChecking for missing CIPC events...")
    
    timeline = load_json(TIMELINE_FILE)
    
    # CIPC events that should be in timeline
    cipc_events_to_add = [
        {
            "entry_id": "TL_CIPC_BATCH2_001",
            "date": "2021-03-15",
            "event_type": "cipc_filing",
            "title": "CIPC Annual Return Filing - Regima Skin Treatments",
            "description": "Annual return filed for Regima Skin Treatments CC showing financial position and member details",
            "key_actors": ["Peter Andrew Faucitt"],
            "entities_involved": ["PERSON_001", "ORG_002"],
            "evidence": ["ANNEXURES/JF15-CIPC-BATCH2-2021/"],
            "significance": "Establishes financial control and company status",
            "burden_of_proof": "verified_cipc_record",
            "added_date": datetime.now().isoformat()
        },
        {
            "entry_id": "TL_CIPC_BATCH2_002",
            "date": "2021-03-15",
            "event_type": "cipc_filing",
            "title": "CIPC Annual Return Filing - Regima Worldwide Distribution",
            "description": "Annual return filed for Regima Worldwide Distribution showing director positions and shareholding",
            "key_actors": ["Peter Andrew Faucitt", "Jacqueline Faucitt", "Daniel James Faucitt"],
            "entities_involved": ["PERSON_001", "PERSON_004", "PERSON_005", "ORG_003"],
            "evidence": ["ANNEXURES/JF15-CIPC-BATCH2-2021/"],
            "significance": "Confirms legitimate ownership structure of RWD",
            "burden_of_proof": "verified_cipc_record",
            "added_date": datetime.now().isoformat()
        }
    ]
    
    # Check if events already exist
    existing_entry_ids = {entry.get('entry_id') for entry in timeline['timeline'] if entry.get('entry_id')}
    
    new_events_added = 0
    for event in cipc_events_to_add:
        if event['entry_id'] not in existing_entry_ids:
            timeline['timeline'].append(event)
            new_events_added += 1
            print(f"  ✓ Added: {event['title']}")
    
    if new_events_added > 0:
        # Sort timeline by date
        timeline['timeline'].sort(key=lambda x: x.get('date', '9999-99-99'))
        
        # Update metadata
        timeline['metadata']['total_entries'] = len(timeline['timeline'])
        timeline['metadata']['last_updated'] = datetime.now().isoformat()
        
        save_json(TIMELINE_FILE, timeline)
        print(f"\nAdded {new_events_added} new CIPC events to timeline")
    else:
        print("No new CIPC events to add (all already present)")
    
    return timeline

def main():
    """Main execution"""
    print("="*80)
    print("TIMELINE EVIDENCE ENHANCEMENT - 2026-01-12")
    print("="*80)
    print()
    
    # Enhance existing entries with evidence
    timeline = enhance_timeline_with_evidence()
    
    # Add missing CIPC events
    timeline = add_missing_cipc_events()
    
    print("\n" + "="*80)
    print("ENHANCEMENT COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
