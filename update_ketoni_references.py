#!/usr/bin/env python3
"""
Update Bantjies Debt References to Ketoni Debt/Payout

This script corrects the factual error where R18.75M was attributed to Bantjies
personally, when it is actually owed by Ketoni Investment Holdings to FFT.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

REPO_DIR = Path("/home/ubuntu/revstream1")

# Replacement patterns
REPLACEMENTS = [
    # Direct debt references
    (r"Bantjies.*owes.*R18[,.]?685[,.]?000", "Ketoni owes R18.75M to FFT (Bantjies has conflict as George Group CFO)"),
    (r"Bantjies'?s?\s+R18[,.]?685[,.]?000\s+debt", "Ketoni's R18.75M debt to FFT"),
    (r"R18[,.]?685[,.]?000\s+debt\s+to\s+(?:the\s+)?(?:Faucitt\s+Family\s+)?[Tt]rust", "R18.75M Ketoni payout owed to FFT"),
    (r"owes\s+R18[,.]?685[,.]?000\s+to\s+(?:the\s+)?(?:Faucitt\s+Family\s+)?[Tt]rust", "Ketoni owes R18.75M payout to FFT"),
    
    # Conflict of interest references - keep but reframe
    (r"Bantjies.*debt.*conflict\s+of\s+interest", "Bantjies has conflict of interest as CFO of George Group (whose CEO owns Ketoni which owes R18.75M to FFT)"),
    (r"debtor.*trustee.*conflict", "CFO-Trustee conflict (Bantjies serves Ketoni's owner while being FFT Trustee)"),
    
    # SF1 file references
    (r"SF1_Bantjies_Debt_Documentation", "SF1_Ketoni_Debt_FFT_Documentation"),
    (r"SF1 - Bantjies Debt Documentation", "SF1 - Ketoni R18.75M Payout to FFT Documentation"),
    (r"SF1.*Bantjies.*[Dd]ebt", "SF1 - Ketoni R18.75M Payout Documentation"),
    
    # Specific amount corrections
    (r'"debt_motive":\s*"R18,685,000"', '"debt_motive": "Ketoni R18.75M payout to FFT"'),
    (r'"debt_to_trust":\s*"R18,685,000"', '"ketoni_payout_to_fft": "R18.75M"'),
    (r'"debt_owed_by_trustee":\s*"R18,685,000"', '"ketoni_debt_to_fft": "R18.75M (Bantjies conflict as George Group CFO)"'),
]

def update_file_content(filepath, content):
    """Apply all replacements to content."""
    updated = content
    changes = []
    
    for pattern, replacement in REPLACEMENTS:
        matches = re.findall(pattern, updated, re.IGNORECASE)
        if matches:
            updated = re.sub(pattern, replacement, updated, flags=re.IGNORECASE)
            changes.append(f"  - Replaced '{pattern}' ({len(matches)} occurrences)")
    
    return updated, changes

def process_json_file(filepath):
    """Process a JSON file and update references."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        updated, changes = update_file_content(filepath, content)
        
        if changes:
            # Validate JSON
            try:
                json.loads(updated)
                with open(filepath, 'w') as f:
                    f.write(updated)
                return True, changes
            except json.JSONDecodeError as e:
                return False, [f"JSON validation failed: {e}"]
        
        return False, []
    except Exception as e:
        return False, [f"Error: {e}"]

def process_md_file(filepath):
    """Process a Markdown file and update references."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        updated, changes = update_file_content(filepath, content)
        
        if changes:
            with open(filepath, 'w') as f:
                f.write(updated)
            return True, changes
        
        return False, []
    except Exception as e:
        return False, [f"Error: {e}"]

def main():
    print("="*70)
    print("KETONI DEBT REFERENCE CORRECTION")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    results = {
        "json_updated": [],
        "md_updated": [],
        "errors": []
    }
    
    # Process entities.json
    print("\n[1/4] Processing entities.json...")
    entities_path = REPO_DIR / "data_models/entities/entities.json"
    if entities_path.exists():
        success, changes = process_json_file(entities_path)
        if success:
            results["json_updated"].append({"file": str(entities_path), "changes": changes})
            print(f"  Updated with {len(changes)} changes")
        elif changes:
            results["errors"].append({"file": str(entities_path), "errors": changes})
    
    # Process relations.json
    print("\n[2/4] Processing relations.json...")
    relations_path = REPO_DIR / "data_models/relations/relations.json"
    if relations_path.exists():
        success, changes = process_json_file(relations_path)
        if success:
            results["json_updated"].append({"file": str(relations_path), "changes": changes})
            print(f"  Updated with {len(changes)} changes")
    
    # Process events.json
    print("\n[3/4] Processing events.json...")
    events_path = REPO_DIR / "data_models/events/events.json"
    if events_path.exists():
        success, changes = process_json_file(events_path)
        if success:
            results["json_updated"].append({"file": str(events_path), "changes": changes})
            print(f"  Updated with {len(changes)} changes")
    
    # Process all markdown files in docs
    print("\n[4/4] Processing markdown files in docs/...")
    docs_dir = REPO_DIR / "docs"
    md_count = 0
    for md_file in docs_dir.rglob("*.md"):
        success, changes = process_md_file(md_file)
        if success:
            results["md_updated"].append({"file": str(md_file.relative_to(REPO_DIR)), "changes": changes})
            md_count += 1
    print(f"  Updated {md_count} markdown files")
    
    # Save results
    results_path = REPO_DIR / "KETONI_CORRECTION_RESULTS_2026_01_28.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "="*70)
    print("CORRECTION SUMMARY")
    print("="*70)
    print(f"JSON files updated: {len(results['json_updated'])}")
    print(f"Markdown files updated: {len(results['md_updated'])}")
    print(f"Errors: {len(results['errors'])}")
    print(f"\nResults saved to: {results_path}")
    
    return results

if __name__ == "__main__":
    main()
