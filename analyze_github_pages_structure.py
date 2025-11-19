#!/usr/bin/env python3
"""
Analyze GitHub Pages structure and evidence linkage
Ensure all 3 applications have clear evidence references
"""

import os
import re
from pathlib import Path

def find_markdown_files(directory):
    """Find all markdown files in directory"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def analyze_evidence_links(content):
    """Extract and analyze evidence links from markdown content"""
    # Find all markdown links
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    links = re.findall(link_pattern, content)
    
    evidence_links = []
    broken_links = []
    
    for text, url in links:
        if 'evidence' in url.lower():
            evidence_links.append((text, url))
            # Check if it's a relative path
            if not url.startswith('http'):
                # Check if file exists
                if not os.path.exists(url) and not os.path.exists(url.replace('.html', '.md')):
                    broken_links.append((text, url))
    
    return evidence_links, broken_links

def analyze_application_file(filepath):
    """Analyze an application markdown file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    evidence_links, broken_links = analyze_evidence_links(content)
    
    # Count sections
    sections = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    
    # Check for evidence categories
    has_evidence_section = any('evidence' in s.lower() for s in sections)
    
    return {
        'filepath': filepath,
        'total_links': len(evidence_links),
        'broken_links': len(broken_links),
        'sections': len(sections),
        'has_evidence_section': has_evidence_section,
        'evidence_links': evidence_links,
        'broken_links_list': broken_links
    }

def check_evidence_directory():
    """Check evidence directory structure"""
    evidence_dir = 'evidence'
    if not os.path.exists(evidence_dir):
        return {'exists': False}
    
    categories = {}
    total_files = 0
    
    for root, dirs, files in os.walk(evidence_dir):
        category = os.path.basename(root)
        if category != 'evidence':
            file_count = len([f for f in files if not f.startswith('.')])
            categories[category] = file_count
            total_files += file_count
    
    return {
        'exists': True,
        'categories': categories,
        'total_files': total_files
    }

def analyze_index_page():
    """Analyze the main index page"""
    if not os.path.exists('index.md'):
        return {'exists': False}
    
    with open('index.md', 'r') as f:
        content = f.read()
    
    # Check for application links
    app1_link = 'application-1' in content
    app2_link = 'application-2' in content
    app3_link = 'application-3' in content
    evidence_index_link = 'evidence-index' in content
    
    evidence_links, broken_links = analyze_evidence_links(content)
    
    return {
        'exists': True,
        'has_app1_link': app1_link,
        'has_app2_link': app2_link,
        'has_app3_link': app3_link,
        'has_evidence_index': evidence_index_link,
        'evidence_links': len(evidence_links),
        'broken_links': len(broken_links)
    }

def main():
    print("=" * 80)
    print("GITHUB PAGES STRUCTURE ANALYSIS")
    print("=" * 80)
    print()
    
    # Analyze index page
    print("ANALYZING INDEX PAGE...")
    index_analysis = analyze_index_page()
    if index_analysis['exists']:
        print(f"  ✓ index.md exists")
        print(f"  Application 1 link: {'✓' if index_analysis['has_app1_link'] else '✗'}")
        print(f"  Application 2 link: {'✓' if index_analysis['has_app2_link'] else '✗'}")
        print(f"  Application 3 link: {'✓' if index_analysis['has_app3_link'] else '✗'}")
        print(f"  Evidence index link: {'✓' if index_analysis['has_evidence_index'] else '✗'}")
        print(f"  Evidence links: {index_analysis['evidence_links']}")
        print(f"  Broken links: {index_analysis['broken_links']}")
    else:
        print(f"  ✗ index.md NOT FOUND")
    print()
    
    # Analyze application files
    print("ANALYZING APPLICATION FILES...")
    application_files = ['application-1.md', 'application-2.md', 'application-3.md']
    app_analyses = {}
    
    for app_file in application_files:
        if os.path.exists(app_file):
            analysis = analyze_application_file(app_file)
            app_analyses[app_file] = analysis
            print(f"\n  {app_file}:")
            print(f"    Sections: {analysis['sections']}")
            print(f"    Evidence links: {analysis['total_links']}")
            print(f"    Broken links: {analysis['broken_links']}")
            print(f"    Has evidence section: {'✓' if analysis['has_evidence_section'] else '✗'}")
            
            if analysis['broken_links'] > 0:
                print(f"    Broken links:")
                for text, url in analysis['broken_links_list'][:5]:
                    print(f"      - {text}: {url}")
        else:
            print(f"\n  ✗ {app_file} NOT FOUND")
    print()
    
    # Analyze evidence directory
    print("ANALYZING EVIDENCE DIRECTORY...")
    evidence_analysis = check_evidence_directory()
    if evidence_analysis['exists']:
        print(f"  ✓ evidence/ directory exists")
        print(f"  Total files: {evidence_analysis['total_files']}")
        print(f"  Categories:")
        for category, count in sorted(evidence_analysis['categories'].items()):
            print(f"    - {category}: {count} files")
    else:
        print(f"  ✗ evidence/ directory NOT FOUND")
    print()
    
    # Check evidence-index.md
    print("ANALYZING EVIDENCE INDEX...")
    if os.path.exists('evidence-index.md'):
        with open('evidence-index.md', 'r') as f:
            content = f.read()
        evidence_links, broken_links = analyze_evidence_links(content)
        print(f"  ✓ evidence-index.md exists")
        print(f"  Evidence links: {len(evidence_links)}")
        print(f"  Broken links: {len(broken_links)}")
    else:
        print(f"  ✗ evidence-index.md NOT FOUND")
    print()
    
    # Generate recommendations
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    recommendations = []
    
    # Check for broken links
    total_broken = sum(a.get('broken_links', 0) for a in app_analyses.values())
    if total_broken > 0:
        recommendations.append({
            'priority': 'HIGH',
            'issue': f'{total_broken} broken evidence links across application pages',
            'action': 'Fix broken links to ensure all evidence is accessible'
        })
    
    # Check evidence section presence
    apps_without_evidence = [f for f, a in app_analyses.items() if not a.get('has_evidence_section', False)]
    if apps_without_evidence:
        recommendations.append({
            'priority': 'MEDIUM',
            'issue': f'{len(apps_without_evidence)} application(s) without dedicated evidence section',
            'action': 'Add evidence sections to: ' + ', '.join(apps_without_evidence)
        })
    
    # Check evidence directory coverage
    if evidence_analysis['exists']:
        if evidence_analysis['total_files'] < 20:
            recommendations.append({
                'priority': 'MEDIUM',
                'issue': f'Only {evidence_analysis["total_files"]} evidence files found',
                'action': 'Review ad-res-j7 repository and add missing evidence files'
            })
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. [{rec['priority']}] {rec['issue']}")
        print(f"   Action: {rec['action']}")
        print()
    
    if not recommendations:
        print("✓ No critical issues found. GitHub Pages structure is well-organized.")
        print()
    
    print("=" * 80)

if __name__ == '__main__':
    main()
