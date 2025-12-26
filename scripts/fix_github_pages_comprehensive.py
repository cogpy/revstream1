#!/usr/bin/env python3.11
"""
Fix GitHub Pages Links and Enhance Organization
Date: 2025-11-19
Purpose: Fix broken links, enhance evidence references, improve navigation
"""

import os
import re

def fix_html_links_to_md(content):
    """Convert .html links to .md for GitHub Pages"""
    # Replace .html with .md for internal links
    content = re.sub(r'\]\(([^)]+)\.html\)', r'](\1.md)', content)
    # Fix anchor links (keep .html for anchor references)
    content = re.sub(r'\]\(([^)]+)\.md(#[^)]+)\)', r'](\1.html\2)', content)
    return content

def enhance_evidence_references(content, page_name):
    """Enhance evidence references with ad-res-j7 links"""
    
    # Add ad-res-j7 reference section if not present
    if "ad-res-j7" not in content.lower() and page_name != "index.md":
        evidence_section = """
---

## Extended Evidence Repository

For comprehensive supporting documentation, see the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7) which contains:

- **2,866 evidence files** (226.78 MB total)
- Complete email archives and correspondence
- Financial documents and analysis
- Legal filings and court documents
- CIPC records and corporate documentation
- Comprehensive evidence index and catalog

**[View Complete Evidence Catalog →](https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md)**

"""
        # Insert before the last --- or at the end
        if content.rfind("---") > 100:
            insert_pos = content.rfind("---")
            content = content[:insert_pos] + evidence_section + content[insert_pos:]
        else:
            content = content + evidence_section
    
    return content

def add_navigation_breadcrumbs(content, page_name):
    """Add navigation breadcrumbs to pages"""
    
    breadcrumb_map = {
        "application-1.md": "**Navigation:** [Home](index.md) → Application 1",
        "application-2.md": "**Navigation:** [Home](index.md) → [Application 1](application-1.md) → Application 2",
        "application-3.md": "**Navigation:** [Home](index.md) → [Application 1](application-1.md) → [Application 2](application-2.md) → Application 3",
        "applications.md": "**Navigation:** [Home](index.md) → All Applications",
        "evidence-index.md": "**Navigation:** [Home](index.md) → Evidence Index",
        "data-model-analysis.md": "**Navigation:** [Home](index.md) → Data Model Analysis"
    }
    
    if page_name in breadcrumb_map:
        breadcrumb = breadcrumb_map[page_name] + "\n\n---\n\n"
        
        # Check if breadcrumb already exists
        if "**Navigation:**" not in content:
            # Insert after front matter if present
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = "---" + parts[1] + "---\n\n" + breadcrumb + parts[2]
                else:
                    content = breadcrumb + content
            else:
                content = breadcrumb + content
    
    return content

def enhance_evidence_index(content):
    """Enhance the evidence index with better organization"""
    
    # Add summary statistics at the top
    summary = """
## Evidence Summary

This repository contains organized evidence across **11 categories** supporting Case 2025-137857. All evidence files are stored in the `evidence/` directory with clear categorization.

For **extended evidence** (2,866 additional files), see the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).

### Quick Statistics

| Category | Files | Description |
|----------|-------|-------------|
| Accounting | 4 | Financial records and trial balances |
| CIPC | 2 | Corporate registration documents |
| Critical Analysis | 13 | Legal analysis and mediation notes |
| Emails | 8 | Email correspondence evidence |
| Fabricated Accounts | 6 | Evidence of fraudulent accounting |
| Financial | 1 | Financial impact documentation |
| Mediation | 2 | Mediation session records |
| POPIA | 4 | Privacy violation evidence |
| ReZonance | 4 | Service provider documentation |
| Sage | 2 | Accounting system evidence |
| Trademark | 2 | Intellectual property documentation |

---

"""
    
    # Insert after front matter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            # Check if summary already exists
            if "Evidence Summary" not in content:
                content = "---" + parts[1] + "---\n\n" + summary + parts[2]
    else:
        if "Evidence Summary" not in content:
            content = summary + content
    
    return content

def main():
    """Main function to fix GitHub Pages"""
    base_path = "/home/ubuntu/revstream1"
    
    pages_files = [
        "index.md",
        "application-1.md",
        "application-2.md",
        "application-3.md",
        "applications.md",
        "evidence-index.md",
        "data-model-analysis.md"
    ]
    
    print("=" * 80)
    print("FIXING GITHUB PAGES LINKS AND ORGANIZATION")
    print("=" * 80)
    
    for page_file in pages_files:
        filepath = os.path.join(base_path, page_file)
        
        if not os.path.exists(filepath):
            print(f"\n⚠ SKIPPING: {page_file} (not found)")
            continue
        
        print(f"\n### Processing {page_file} ###")
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        original_content = content
        
        # Fix HTML links to MD
        content = fix_html_links_to_md(content)
        print("  ✓ Fixed .html links to .md")
        
        # Add navigation breadcrumbs
        content = add_navigation_breadcrumbs(content, page_file)
        print("  ✓ Added navigation breadcrumbs")
        
        # Enhance evidence references
        content = enhance_evidence_references(content, page_file)
        print("  ✓ Enhanced evidence references")
        
        # Special handling for evidence-index.md
        if page_file == "evidence-index.md":
            content = enhance_evidence_index(content)
            print("  ✓ Enhanced evidence index organization")
        
        # Save if changed
        if content != original_content:
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"  ✓ Saved changes to {page_file}")
        else:
            print(f"  ℹ No changes needed for {page_file}")
    
    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATES COMPLETE")
    print("=" * 80)
    print("\nAll pages have been updated with:")
    print("  - Fixed internal links (.html → .md)")
    print("  - Navigation breadcrumbs")
    print("  - Enhanced evidence references")
    print("  - Cross-references to ad-res-j7 repository")

if __name__ == "__main__":
    main()
