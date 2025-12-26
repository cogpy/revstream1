import os
import re
from pathlib import Path

def analyze_markdown_file(filepath):
    """Analyze a markdown file for evidence references and structure"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find evidence links
    evidence_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    
    # Find broken links (pointing to non-existent files)
    broken_links = []
    for text, link in evidence_links:
        if link.startswith('http'):
            continue
        # Resolve relative path
        file_dir = os.path.dirname(filepath)
        target_path = os.path.join(file_dir, link)
        target_path = os.path.normpath(target_path)
        if not os.path.exists(target_path):
            broken_links.append((text, link))
    
    # Count headers
    headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    
    return {
        "filepath": filepath,
        "total_links": len(evidence_links),
        "broken_links": broken_links,
        "headers": headers,
        "word_count": len(content.split())
    }

def main():
    """Main analysis function"""
    base_path = "/home/ubuntu/revstream1"
    
    # Key GitHub Pages files
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
    print("GITHUB PAGES ORGANIZATION ANALYSIS")
    print("=" * 80)
    
    all_broken_links = []
    
    for page_file in pages_files:
        filepath = os.path.join(base_path, page_file)
        if not os.path.exists(filepath):
            print(f"\n❌ MISSING: {page_file}")
            continue
        
        analysis = analyze_markdown_file(filepath)
        
        print(f"\n### {page_file} ###")
        print(f"Word Count: {analysis['word_count']}")
        print(f"Total Links: {analysis['total_links']}")
        print(f"Broken Links: {len(analysis['broken_links'])}")
        
        if analysis['broken_links']:
            print("  Broken links:")
            for text, link in analysis['broken_links'][:5]:
                print(f"    - [{text}]({link})")
                all_broken_links.append({
                    "file": page_file,
                    "text": text,
                    "link": link
                })
        
        print(f"Headers: {len(analysis['headers'])}")
    
    # Check evidence directory structure
    print("\n" + "=" * 80)
    print("EVIDENCE DIRECTORY STRUCTURE")
    print("=" * 80)
    
    evidence_path = os.path.join(base_path, "evidence")
    if os.path.exists(evidence_path):
        evidence_dirs = [d for d in os.listdir(evidence_path) if os.path.isdir(os.path.join(evidence_path, d))]
        print(f"\nEvidence subdirectories: {len(evidence_dirs)}")
        for d in evidence_dirs:
            subdir_path = os.path.join(evidence_path, d)
            file_count = len([f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))])
            print(f"  - {d}: {file_count} files")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total broken links across all pages: {len(all_broken_links)}")
    
    if all_broken_links:
        print("\nTop broken links:")
        for item in all_broken_links[:10]:
            print(f"  - {item['file']}: [{item['text']}]({item['link']})")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
