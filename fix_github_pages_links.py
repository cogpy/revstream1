#!/usr/bin/env python3
"""
Fix broken evidence links in GitHub Pages
Update all application pages with correct evidence references
"""

import re
import os

def fix_evidence_links(content):
    """Fix broken evidence links by converting anchor links to proper file paths"""
    
    # Map of anchor links to actual file paths
    link_mappings = {
        'evidence-index.html#popia': 'evidence/popia/POPIAViolationNotice-SenttoPeteon8July2025-DanielFaucitt-Outlook.pdf',
        '#popia-evidence': 'evidence/popia/POPIAViolationNotice-SenttoPeteon8July2025-DanielFaucitt-Outlook.pdf',
        '#shopify-evidence': 'evidence-index.html#shopify',
        '#email-evidence': 'evidence/emails/TRUSTEEFw_CopyofyourID-DanielFaucitt-Outlook.pdf',
        '#sage-evidence': 'evidence/sage/SAGE_SCREENSHOTS_CONTROL_ANALYSIS.md.pdf',
        '#cipc-evidence': 'evidence/cipc/347975701_REGIMA_SA_K201708793507.Pdf',
        '#financial-evidence': 'evidence-index.html#financial',
        '#rezonance-evidence': 'evidence/rezonance/FW_RezonceREZONANCE23,24,25FEBS-DanielFaucitt-Outlook.pdf',
        '#accounting-evidence': 'evidence/accounting/Rez-WWDBooks2023-02.pdf',
        '#mediation-evidence': 'evidence/mediation/Re_MEDIATIONNOTES-DanielFaucitt-Outlook.pdf',
        '#trademark-evidence': 'evidence/trademark/FW_Trademarkregistrationnos.UK00914297063REGIMAZONEinclasses03,05and44inthenameofREGIMASKINTREATMENTSCC[Witzref_CS2511.UK.03+]-DanielFaucitt-Outlook.pdf'
    }
    
    # Replace broken links
    for old_link, new_link in link_mappings.items():
        # Match markdown links with the old link
        pattern = r'\[([^\]]+)\]\(' + re.escape(old_link) + r'\)'
        replacement = r'[\1](' + new_link + ')'
        content = re.sub(pattern, replacement, content)
    
    return content

def update_file_with_fixes(filepath):
    """Update a file with fixed evidence links"""
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    fixed_content = fix_evidence_links(content)
    
    if original_content != fixed_content:
        with open(filepath, 'w') as f:
            f.write(fixed_content)
        return True
    
    return False

def main():
    print("=" * 80)
    print("FIXING GITHUB PAGES EVIDENCE LINKS")
    print("=" * 80)
    print()
    
    files_to_fix = [
        'index.md',
        'application-1.md',
        'application-2.md',
        'application-3.md',
        'applications.md',
        'evidence-index.md'
    ]
    
    fixed_count = 0
    
    for filepath in files_to_fix:
        if update_file_with_fixes(filepath):
            print(f"  ✓ Fixed links in {filepath}")
            fixed_count += 1
        else:
            if os.path.exists(filepath):
                print(f"  - No changes needed in {filepath}")
            else:
                print(f"  ✗ File not found: {filepath}")
    
    print()
    print("=" * 80)
    print(f"Fixed {fixed_count} files")
    print("=" * 80)

if __name__ == '__main__':
    main()
