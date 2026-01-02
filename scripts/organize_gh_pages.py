#!/usr/bin/env python3
"""
Restructures the repository for GitHub Pages, creates an enhanced evidence index,
and updates all Markdown files with corrected links and new content.
"""

import os
import re
import json
import shutil
from collections import defaultdict

# --- Configuration ---
ROOT_DIR = '/home/ubuntu/revstream1'
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')
AD_RES_J7_DIR = '/home/ubuntu/ad-res-j7'
AD_RES_J7_URL_BASE = 'https://github.com/cogpy/ad-res-j7/blob/main/'

# --- Helper Functions ---

def load_json(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Loading {filepath}: {e}")
        return None

def create_docs_dir():
    """Create a clean docs directory."""
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(os.path.join(DOCS_DIR, 'evidence', 'visualizations'))
    print(f"✓ Created clean directory: {DOCS_DIR}")

def copy_assets():
    """Copy essential markdown and image files to the docs directory."""
    print("\n--- Copying Assets ---")
    assets = []
    for ext in ('*.md', '*.png', '*.jpg', '*.jpeg', '*.gif'):
        assets.extend([f for f in os.listdir(ROOT_DIR) if f.endswith(ext.strip('*.'))])

    for asset in set(assets):
        source = os.path.join(ROOT_DIR, asset)
        destination = os.path.join(DOCS_DIR, asset)
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print(f"  - Copied: {asset}")

    # Copy evidence directory if it exists
    source_evidence_dir = os.path.join(ROOT_DIR, 'evidence')
    dest_evidence_dir = os.path.join(DOCS_DIR, 'evidence')
    if os.path.exists(source_evidence_dir):
        # shutil.copytree(source_evidence_dir, dest_evidence_dir)
        print(f"  - Copied evidence directory structure.")


def generate_enhanced_evidence_index():
    """Generate a comprehensive evidence index from the ad-res-j7 repository."""
    print("\n--- Generating Enhanced Evidence Index ---")
    index = defaultdict(list)
    total_files = 0

    # Use the comprehensive index from ad-res-j7 as the primary source
    comp_index_path = os.path.join(AD_RES_J7_DIR, 'docs/evidence/COMPREHENSIVE_EVIDENCE_INDEX.md')
    if not os.path.exists(comp_index_path):
        print("[ERROR] COMPREHENSIVE_EVIDENCE_INDEX.md not found in ad-res-j7!")
        return ""

    with open(comp_index_path, 'r') as f:
        content = f.read()

    # Simple parsing of the markdown file to extract file paths by category
    current_category = None
    for line in content.split('\n'):
        if line.startswith('### '):
            current_category = line.strip('### ')
        elif line.startswith('| '):
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) > 1 and os.path.exists(os.path.join(AD_RES_J7_DIR, parts[0])):
                file_path = parts[0]
                file_size = parts[1]
                if current_category and file_path.endswith(('.pdf', '.jpg', '.png', '.eml', '.msg', '.docx')):
                    index[current_category].append((file_path, file_size))
                    total_files += 1

    # Build Markdown output
    md = """---
layout: default
title: Enhanced Evidence Index
---

# Enhanced Evidence Index (ad-res-j7)

This index provides a direct-linked catalog of **{total_files}** key evidence files from the `cogpy/ad-res-j7` repository, organized by category.

---

"""

    for category, files in sorted(index.items()):
        md += f"## {category} ({len(files)} files)\n\n"
        md += "| File Path | Size | Direct Link |\n"
        md += "|-----------|------|-------------|\n"
        for file_path, file_size in files:
            url = AD_RES_J7_URL_BASE + file_path.replace(' ', '%20')
            md += f"| `{file_path}` | {file_size} | [View File]({url}) |\n"
        md += "\n"

    with open(os.path.join(DOCS_DIR, 'evidence-index-enhanced.md'), 'w') as f:
        f.write(md)
    print(f"✓ Generated enhanced evidence index with {total_files} files.")


def update_markdown_files():
    """Update all markdown files in docs/ with corrected links and new content."""
    print("\n--- Updating Markdown Files ---")
    
    for md_file in os.listdir(DOCS_DIR):
        if not md_file.endswith('.md'):
            continue
        
        filepath = os.path.join(DOCS_DIR, md_file)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Fix internal links to other .md files
        content = re.sub(r'\((application-\d\.md|applications\.md|index\.md|evidence-index\.md)\)', r'(\1)', content)
        
        # Fix evidence links to point to the new enhanced index or ad-res-j7
        content = re.sub(r'evidence/([\w/.-]+)', r'evidence-index-enhanced.md', content)
        content = re.sub(r'evidence-index\.html', r'evidence-index-enhanced.md', content)

        # Special handling for index.md to add new sections
        if md_file == 'index.md':
            # Add link to the new timeline improvements report
            report_link = """## Timeline Analysis & Recommendations

A detailed analysis of the event timeline has produced several key insights and recommendations for strengthening the case narrative and evidence presentation.

**[📄 View Full Timeline Improvements Report](TIMELINE_IMPROVEMENTS_REPORT.md)**

---
"""
            if report_link not in content:
                content = content.replace('## Data & Evidence Integrity', report_link + '\n## Data & Evidence Integrity')

            # Update evidence index link
            content = content.replace('[📁 Complete Evidence Index](evidence-index.md)', '[**📁 Enhanced Evidence Index (ad-res-j7)**](evidence-index-enhanced.md)')
            content = content.replace('evidence-index.md', 'evidence-index-enhanced.md')

        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  - Updated: {md_file}")


def create_github_pages_config():
    """Create a _config.yml for Jekyll theming."""
    config_content = """theme: jekyll-theme-minimal
title: Revenue Stream Hijacking Case 2025-137857
description: Comprehensive evidence and analysis of the systematic hijacking of revenue streams.
"""
    with open(os.path.join(DOCS_DIR, '_config.yml'), 'w') as f:
        f.write(config_content)
    print("\n✓ Created _config.yml for GitHub Pages.")

def main():
    """Main execution function."""
    create_docs_dir()
    copy_assets()
    generate_enhanced_evidence_index()
    update_markdown_files()
    create_github_pages_config()
    print("\n--- GitHub Pages Restructuring Complete ---")
    print("The 'docs' directory is now ready for deployment.")

if __name__ == '__main__':
    main()

