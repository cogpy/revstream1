#!/usr/bin/env python3
"""
Final cleanup of remaining Bantjies debt references to Ketoni.
"""

import os
import re
from pathlib import Path

REPO_DIR = Path("/home/ubuntu/revstream1")

# More comprehensive replacement patterns
REPLACEMENTS = [
    # Direct debt statements
    (r"Bantjies is unknown trustee of trust he owes R18[,.]?685[,.]?000 to", 
     "Bantjies is trustee of FFT with conflict of interest (CFO of George Group whose CEO owns Ketoni which owes R18.75M to FFT)"),
    
    (r"Bantjies R18[,.]?685[,.]?000 debt to trust while serving as trustee",
     "Bantjies conflict of interest: CFO of George Group (whose CEO owns Ketoni which owes R18.75M to FFT) while serving as FFT trustee"),
    
    (r"Bantjies.*owes R18[,.]?685[,.]?000 to",
     "Ketoni owes R18.75M to FFT (Bantjies has conflict as George Group CFO where"),
    
    (r"R18[,.]?685[,.]?000.*Bantjies.*debt",
     "R18.75M Ketoni debt to FFT (Bantjies conflict as George Group CFO)"),
    
    (r"Bantjies.*debt.*R18[,.]?685",
     "Ketoni R18.75M debt to FFT (Bantjies conflict as George Group CFO)"),
    
    # SF1 file references - already partially updated but clean up remaining
    (r"SF1_Bantjies_Debt",
     "SF1_Ketoni_Debt_FFT"),
    
    (r"SF1 - Bantjies Debt",
     "SF1 - Ketoni R18.75M Payout to FFT"),
    
    # Conflict statements that mention debt incorrectly
    (r"Bantjies.*debt.*conflict of interest",
     "Bantjies conflict of interest as CFO of George Group (whose CEO owns Ketoni which owes R18.75M to FFT)"),
    
    # Specific amount variations
    (r"R18,685,000",
     "R18.75M (Ketoni debt to FFT)"),
    
    (r"R18\.685M",
     "R18.75M (Ketoni debt to FFT)"),
    
    (r"ZAR 18,685,000",
     "ZAR 18.75M (Ketoni debt to FFT)"),
]

def process_file(filepath):
    """Process a single file and apply replacements."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original = content
        for pattern, replacement in REPLACEMENTS:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    print("="*70)
    print("FINAL KETONI REFERENCE CLEANUP")
    print("="*70)
    
    updated_count = 0
    
    # Process all markdown files in docs
    docs_dir = REPO_DIR / "docs"
    for md_file in docs_dir.rglob("*.md"):
        if process_file(md_file):
            updated_count += 1
    
    # Process archive directory
    archive_dir = REPO_DIR / "archive"
    if archive_dir.exists():
        for json_file in archive_dir.rglob("*.json"):
            if process_file(json_file):
                updated_count += 1
    
    print(f"\nUpdated {updated_count} files")
    print("="*70)

if __name__ == "__main__":
    main()
