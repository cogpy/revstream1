#!/usr/bin/env python3
"""
Evidence Cross-Reference Script
Date: 2025-12-06
Purpose: Cross-reference ad-res-j7 evidence with revstream1 data models
"""

import json
import os
from pathlib import Path
from collections import defaultdict

# Paths
AD_RES_J7_PATH = "/home/ubuntu/ad-res-j7"
ENTITIES_FILE = "data_models/entities/entities_refined_2025_12_06_v26.json"
EVENTS_FILE = "data_models/events/events_refined_2025_12_06_v28.json"

def scan_evidence_repository():
    """Scan ad-res-j7 for key evidence files"""
    print("\n" + "="*80)
    print("SCANNING AD-RES-J7 EVIDENCE REPOSITORY")
    print("="*80)
    
    evidence_categories = defaultdict(list)
    
    # Key directories to scan
    key_dirs = [
        "ANNEXURES/JF01",  # Trust documents
        "ANNEXURES/JF02",  # Shopify operations
        "ANNEXURES/JF03",  # POPIA violations
        "ANNEXURES/JF04",  # Bank records
        "ANNEXURES/JF05",  # Correspondence
        "ANNEXURES/JF06",  # Legal documents
        "ANNEXURES/JF07",  # Financial statements
        "ANNEXURES/JF08",  # Evidence packages
        "case_2025_137857/02_evidence",
        "evidence"
    ]
    
    for dir_name in key_dirs:
        dir_path = Path(AD_RES_J7_PATH) / dir_name
        if dir_path.exists():
            files = list(dir_path.rglob("*"))
            file_count = len([f for f in files if f.is_file()])
            evidence_categories[dir_name] = file_count
            print(f"✓ {dir_name}: {file_count} files")
    
    return evidence_categories

def analyze_entity_evidence_coverage(entities_data, evidence_categories):
    """Analyze entity evidence coverage"""
    print("\n" + "="*80)
    print("ENTITY EVIDENCE COVERAGE ANALYSIS")
    print("="*80)
    
    entities = entities_data.get('entities', {})
    coverage_report = {
        'well_documented': [],
        'needs_improvement': [],
        'missing_evidence': []
    }
    
    # Analyze persons
    persons = entities.get('persons', [])
    for person in persons:
        entity_id = person.get('entity_id')
        name = person.get('name')
        evidence_files = person.get('evidence_files', [])
        
        if len(evidence_files) >= 3:
            coverage_report['well_documented'].append(f"{entity_id} ({name}): {len(evidence_files)} files")
        elif len(evidence_files) > 0:
            coverage_report['needs_improvement'].append(f"{entity_id} ({name}): {len(evidence_files)} files")
        else:
            coverage_report['missing_evidence'].append(f"{entity_id} ({name}): No evidence")
    
    print(f"\n✓ Well Documented Entities: {len(coverage_report['well_documented'])}")
    print(f"⚠ Needs Improvement: {len(coverage_report['needs_improvement'])}")
    print(f"❌ Missing Evidence: {len(coverage_report['missing_evidence'])}")
    
    if coverage_report['missing_evidence']:
        print("\n❌ Entities Missing Evidence:")
        for item in coverage_report['missing_evidence']:
            print(f"  - {item}")
    
    return coverage_report

def identify_new_evidence_opportunities():
    """Identify new evidence that could strengthen the case"""
    print("\n" + "="*80)
    print("NEW EVIDENCE OPPORTUNITIES")
    print("="*80)
    
    opportunities = []
    
    # Check for bank statement files
    bank_records_path = Path(AD_RES_J7_PATH) / "ANNEXURES" / "JF04"
    if bank_records_path.exists():
        bank_files = list(bank_records_path.glob("*.pdf"))
        if bank_files:
            opportunities.append({
                'category': 'bank_records',
                'description': f'Found {len(bank_files)} bank statement files in JF04',
                'files': [f.name for f in bank_files[:5]],
                'recommendation': 'Cross-reference with EVENT transactions'
            })
    
    # Check for correspondence
    correspondence_path = Path(AD_RES_J7_PATH) / "ANNEXURES" / "JF05"
    if correspondence_path.exists():
        email_files = list(correspondence_path.glob("*.eml")) + list(correspondence_path.glob("*.msg"))
        if email_files:
            opportunities.append({
                'category': 'correspondence',
                'description': f'Found {len(email_files)} email files in JF05',
                'files': [f.name for f in email_files[:5]],
                'recommendation': 'Extract key dates and parties for timeline events'
            })
    
    # Check for legal documents
    legal_path = Path(AD_RES_J7_PATH) / "ANNEXURES" / "JF06"
    if legal_path.exists():
        legal_files = list(legal_path.glob("*.pdf"))
        if legal_files:
            opportunities.append({
                'category': 'legal_documents',
                'description': f'Found {len(legal_files)} legal documents in JF06',
                'files': [f.name for f in legal_files[:5]],
                'recommendation': 'Link to APPLICATION events and timeline'
            })
    
    # Check for Shopify reports
    shopify_path = Path(AD_RES_J7_PATH) / "ANNEXURES" / "JF02"
    if shopify_path.exists():
        shopify_files = list(shopify_path.glob("*.pdf"))
        if shopify_files:
            opportunities.append({
                'category': 'shopify_evidence',
                'description': f'Found {len(shopify_files)} Shopify reports in JF02',
                'files': [f.name for f in shopify_files[:5]],
                'recommendation': 'Verify revenue figures and platform ownership timeline'
            })
    
    print(f"\n✓ Identified {len(opportunities)} evidence opportunity categories:")
    for opp in opportunities:
        print(f"\n  📁 {opp['category'].upper()}")
        print(f"     {opp['description']}")
        print(f"     💡 {opp['recommendation']}")
        if opp['files']:
            print(f"     Files: {', '.join(opp['files'][:3])}...")
    
    return opportunities

def generate_cross_reference_report(evidence_categories, coverage_report, opportunities):
    """Generate comprehensive cross-reference report"""
    report = {
        'metadata': {
            'analysis_date': '2025-12-06',
            'ad_res_j7_path': AD_RES_J7_PATH,
            'purpose': 'Cross-reference evidence repository with data models'
        },
        'evidence_repository_scan': {
            'total_categories': len(evidence_categories),
            'categories': dict(evidence_categories)
        },
        'entity_coverage': coverage_report,
        'new_opportunities': opportunities,
        'recommendations': [
            'Link bank statement files (JF04) to specific EVENT transactions',
            'Extract correspondence dates (JF05) for timeline verification',
            'Cross-reference legal documents (JF06) with APPLICATION events',
            'Verify Shopify reports (JF02) against revenue theft calculations',
            'Add evidence file references to entities missing documentation'
        ]
    }
    
    return report

def main():
    """Main cross-reference function"""
    print("\n" + "="*80)
    print("EVIDENCE CROSS-REFERENCE ANALYSIS")
    print("Date: 2025-12-06")
    print("="*80)
    
    # Scan evidence repository
    evidence_categories = scan_evidence_repository()
    
    # Load entities
    print("\nLoading entities data...")
    with open(ENTITIES_FILE, 'r') as f:
        entities_data = json.load(f)
    
    # Analyze coverage
    coverage_report = analyze_entity_evidence_coverage(entities_data, evidence_categories)
    
    # Identify opportunities
    opportunities = identify_new_evidence_opportunities()
    
    # Generate report
    report = generate_cross_reference_report(evidence_categories, coverage_report, opportunities)
    
    # Save report
    output_file = "AD_RES_J7_CROSS_REFERENCE_2025_12_06.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "="*80)
    print("CROSS-REFERENCE ANALYSIS COMPLETE")
    print("="*80)
    print(f"\n✓ Report saved to: {output_file}")
    print(f"✓ Evidence categories scanned: {len(evidence_categories)}")
    print(f"✓ New opportunities identified: {len(opportunities)}")

if __name__ == "__main__":
    main()
