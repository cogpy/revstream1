#!/usr/bin/env python3
"""
Analyze ad-res-j7 evidence and create comprehensive cross-reference mapping
"""
import json
import os
from datetime import datetime
from pathlib import Path

BASE_DIR = "/home/ubuntu/revstream1"
AD_RES_J7_DIR = "/home/ubuntu/ad-res-j7"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def analyze_annexures():
    """Analyze ANNEXURES directory structure"""
    print("Analyzing ANNEXURES...")
    
    annexures_dir = f"{AD_RES_J7_DIR}/ANNEXURES"
    annexures = {}
    
    for annexure_folder in sorted(os.listdir(annexures_dir)):
        folder_path = os.path.join(annexures_dir, annexure_folder)
        if os.path.isdir(folder_path):
            files = []
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(file_path, AD_RES_J7_DIR)
                    files.append(rel_path)
            
            annexures[annexure_folder] = {
                'folder': annexure_folder,
                'file_count': len(files),
                'files': files[:10]  # Sample first 10 files
            }
            print(f"  {annexure_folder}: {len(files)} files")
    
    return annexures

def analyze_case_evidence():
    """Analyze case_2025_137857 evidence structure"""
    print("\nAnalyzing case_2025_137857 evidence...")
    
    case_dir = f"{AD_RES_J7_DIR}/case_2025_137857"
    evidence_structure = {}
    
    if os.path.exists(case_dir):
        for subdir in sorted(os.listdir(case_dir)):
            subdir_path = os.path.join(case_dir, subdir)
            if os.path.isdir(subdir_path):
                files = []
                for root, dirs, filenames in os.walk(subdir_path):
                    for filename in filenames:
                        file_path = os.path.join(root, filename)
                        rel_path = os.path.relpath(file_path, AD_RES_J7_DIR)
                        files.append(rel_path)
                
                evidence_structure[subdir] = {
                    'directory': subdir,
                    'file_count': len(files),
                    'sample_files': files[:5]
                }
                print(f"  {subdir}: {len(files)} files")
    
    return evidence_structure

def create_evidence_mapping():
    """Create comprehensive evidence mapping for events"""
    print("\nCreating evidence mapping...")
    
    # Load events
    events_file = f"{BASE_DIR}/data_models/events/events_refined_2025_12_07_v29.json"
    events_data = load_json(events_file)
    
    # Create mapping structure
    evidence_mapping = {
        'metadata': {
            'created': datetime.now().isoformat(),
            'case_number': '2025-137857',
            'description': 'Evidence mapping between revstream1 events and ad-res-j7 repository'
        },
        'evidence_categories': {
            'financial': {
                'location': 'case_2025_137857/02_evidence/financial',
                'annexures': ['JF02', 'JF04'],
                'description': 'Bank statements, financial records, Shopify reports'
            },
            'cipc': {
                'location': 'evidence/cipc',
                'annexures': ['JF01'],
                'description': 'CIPC company registrations and filings'
            },
            'emails': {
                'location': 'evidence/emails',
                'annexures': ['JF05', 'JF08'],
                'description': 'Email correspondence and communication records'
            },
            'legal_documents': {
                'location': 'case_2025_137857/01_court_documents',
                'annexures': ['JF06', 'JF07'],
                'description': 'Court filings, affidavits, legal correspondence'
            },
            'popia': {
                'location': 'evidence/popia',
                'annexures': ['JF09'],
                'description': 'POPIA violations and data protection evidence'
            },
            'accounting': {
                'location': 'evidence/accounting',
                'annexures': ['JF03'],
                'description': 'Sage accounting records and financial statements'
            },
            'mediation': {
                'location': 'evidence/mediation',
                'annexures': ['JF10'],
                'description': 'Mediation records and correspondence'
            }
        },
        'event_evidence_links': {}
    }
    
    # Map events to evidence categories
    for event in events_data.get('events', []):
        event_id = event.get('event_id')
        categories = event.get('categories', [])
        
        evidence_links = []
        
        # Map categories to evidence locations
        if 'revenue_theft' in categories or 'financial_manipulation' in categories:
            evidence_links.extend([
                'case_2025_137857/02_evidence/financial/',
                'ANNEXURES/JF02/',
                'ANNEXURES/JF04/'
            ])
        
        if 'trust_violation' in categories:
            evidence_links.extend([
                'case_2025_137857/02_evidence/',
                'ANNEXURES/JF01/'
            ])
        
        if 'email_fraud' in categories or 'identity_fraud' in categories:
            evidence_links.extend([
                'evidence/emails/',
                'ANNEXURES/JF05/',
                'ANNEXURES/JF08/'
            ])
        
        if 'popia_violation' in categories:
            evidence_links.extend([
                'evidence/popia/',
                'ANNEXURES/JF09/'
            ])
        
        if 'accounting_fraud' in categories:
            evidence_links.extend([
                'evidence/accounting/',
                'ANNEXURES/JF03/'
            ])
        
        evidence_mapping['event_evidence_links'][event_id] = {
            'event_title': event.get('title'),
            'evidence_locations': list(set(evidence_links)),
            'ad_res_j7_references': [
                f"See {loc} in ad-res-j7 repository" for loc in evidence_links
            ]
        }
    
    return evidence_mapping

def main():
    print("=" * 80)
    print("AD-RES-J7 EVIDENCE ANALYSIS")
    print("=" * 80)
    print()
    
    # Analyze evidence structure
    annexures = analyze_annexures()
    case_evidence = analyze_case_evidence()
    
    # Create evidence mapping
    evidence_mapping = create_evidence_mapping()
    
    # Save evidence mapping
    mapping_file = f"{BASE_DIR}/AD_RES_J7_EVIDENCE_MAPPING_2025_12_07.json"
    save_json(evidence_mapping, mapping_file)
    print(f"\nEvidence mapping saved to: {mapping_file}")
    
    # Create summary report
    summary = {
        'timestamp': datetime.now().isoformat(),
        'ad_res_j7_analysis': {
            'total_annexures': len(annexures),
            'annexure_folders': list(annexures.keys()),
            'case_evidence_directories': list(case_evidence.keys())
        },
        'evidence_mapping': {
            'total_events_mapped': len(evidence_mapping['event_evidence_links']),
            'evidence_categories': len(evidence_mapping['evidence_categories'])
        }
    }
    
    summary_file = f"{BASE_DIR}/AD_RES_J7_ANALYSIS_SUMMARY_2025_12_07.json"
    save_json(summary, summary_file)
    print(f"Analysis summary saved to: {summary_file}")
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print(f"\nTotal Annexures: {len(annexures)}")
    print(f"Evidence Categories: {len(evidence_mapping['evidence_categories'])}")
    print(f"Events Mapped: {len(evidence_mapping['event_evidence_links'])}")

if __name__ == "__main__":
    main()
