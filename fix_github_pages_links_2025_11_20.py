#!/usr/bin/env python3
"""
Fix broken links in GitHub Pages
Converts .html#anchor links to .md#anchor format
"""

import re
from pathlib import Path

def fix_links_in_file(filepath):
    """Fix broken links in a markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix evidence-index.html links to evidence-index-enhanced.md
    content = re.sub(
        r'\(evidence-index\.html(#[^)]+)?\)',
        r'(evidence-index-enhanced.md\1)',
        content
    )
    
    # Fix any remaining .html links to .md
    content = re.sub(
        r'\(([^)]+)\.html(#[^)]+)?\)',
        r'(\1.md\2)',
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Main function"""
    docs_dir = Path("/home/ubuntu/revstream1/docs")
    
    files_to_fix = [
        "index.md",
        "application-1.md",
        "application-2.md",
        "application-3.md",
        "applications.md"
    ]
    
    print("=" * 80)
    print("FIXING GITHUB PAGES LINKS")
    print("=" * 80)
    print()
    
    fixed_count = 0
    
    for filename in files_to_fix:
        filepath = docs_dir / filename
        if filepath.exists():
            if fix_links_in_file(filepath):
                print(f"✓ Fixed links in {filename}")
                fixed_count += 1
            else:
                print(f"  No changes needed in {filename}")
        else:
            print(f"✗ File not found: {filename}")
    
    print()
    print("=" * 80)
    print(f"SUMMARY: Fixed {fixed_count} files")
    print("=" * 80)

if __name__ == "__main__":
    main()
