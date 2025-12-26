#!/usr/bin/env python3
"""
Extract key sections from the urgent application transcript
Focus on: Notice of Motion, key allegations, relief sought
"""

import re

def extract_key_sections(filepath):
    """Extract key sections from the urgent application"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into sections
    sections = {
        "notice_of_motion": "",
        "relief_sought": "",
        "founding_affidavit_intro": "",
        "key_allegations": [],
        "document_structure": ""
    }
    
    # Extract Notice of Motion
    notice_match = re.search(r'\*\*NOTICE OF MOTION\*\*(.*?)(?=\*\*AND TAKE NOTICE\*\*|\*\*FOUNDING AFFIDAVIT\*\*)', content, re.DOTALL)
    if notice_match:
        sections["notice_of_motion"] = notice_match.group(1).strip()
    
    # Extract relief sought (paragraphs 1-4 of Notice of Motion)
    relief_match = re.search(r'NOTICE OF MOTION.*?1\.(.*?)(?=\*\*AND TAKE NOTICE\*\*)', content, re.DOTALL)
    if relief_match:
        sections["relief_sought"] = relief_match.group(1).strip()
    
    # Extract founding affidavit introduction
    affidavit_intro_match = re.search(r'\*\*FOUNDING AFFIDAVIT\*\*(.*?)(?=\n\n---|\Z)', content, re.DOTALL)
    if affidavit_intro_match:
        sections["founding_affidavit_intro"] = affidavit_intro_match.group(1).strip()[:2000]  # First 2000 chars
    
    # Extract page structure
    pages = re.findall(r'\*\*PAGE (\d+) / (\d+)\*\*', content)
    if pages:
        sections["document_structure"] = f"Total pages: {pages[-1][1] if pages else 'Unknown'}"
    
    # Look for key allegation patterns
    allegation_patterns = [
        r'(first respondent.*?(?:harass|interfere|contact|restrain))',
        r'(second respondent.*?(?:harass|interfere|contact|restrain))',
        r'(respondents.*?(?:harass|interfere|contact|restrain))',
    ]
    
    for pattern in allegation_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
        sections["key_allegations"].extend([m[:200] for m in matches[:5]])  # First 5 matches, truncated
    
    return sections

def main():
    """Main extraction function"""
    print("=" * 80)
    print("URGENT APPLICATION KEY SECTIONS EXTRACTION")
    print("=" * 80)
    
    filepath = "/home/ubuntu/upload/pasted_content_3.txt"
    
    print("\n1. Extracting key sections...")
    sections = extract_key_sections(filepath)
    
    print("\n2. Document Structure:")
    print(f"   {sections['document_structure']}")
    
    print("\n3. Notice of Motion (excerpt):")
    print(f"   {sections['notice_of_motion'][:500]}...")
    
    print("\n4. Relief Sought (excerpt):")
    print(f"   {sections['relief_sought'][:500]}...")
    
    print("\n5. Founding Affidavit Intro (excerpt):")
    print(f"   {sections['founding_affidavit_intro'][:500]}...")
    
    print("\n6. Key Allegations Found:")
    for i, allegation in enumerate(sections['key_allegations'][:3], 1):
        print(f"   {i}. {allegation[:150]}...")
    
    # Save full extraction
    output_file = "URGENT_APPLICATION_KEY_SECTIONS.txt"
    with open(output_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("URGENT APPLICATION KEY SECTIONS\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("DOCUMENT STRUCTURE:\n")
        f.write(sections['document_structure'] + "\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("NOTICE OF MOTION:\n")
        f.write("=" * 80 + "\n")
        f.write(sections['notice_of_motion'] + "\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("RELIEF SOUGHT:\n")
        f.write("=" * 80 + "\n")
        f.write(sections['relief_sought'] + "\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("FOUNDING AFFIDAVIT INTRODUCTION:\n")
        f.write("=" * 80 + "\n")
        f.write(sections['founding_affidavit_intro'] + "\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("KEY ALLEGATIONS:\n")
        f.write("=" * 80 + "\n")
        for i, allegation in enumerate(sections['key_allegations'], 1):
            f.write(f"{i}. {allegation}\n\n")
    
    print(f"\n{'=' * 80}")
    print(f"Extraction complete. Saved to: {output_file}")
    print(f"{'=' * 80}")

if __name__ == "__main__":
    main()
