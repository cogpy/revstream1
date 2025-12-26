#!/usr/bin/env python3
"""
Cross-Reference ad-res-j7 Evidence with revstream1 Data Models
Date: 2025-11-25
Purpose: Validate and enhance evidence references from ad-res-j7 repository
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class EvidenceCrossReferencer:
    def __init__(self, revstream_path, ad_res_path):
        self.revstream_path = Path(revstream_path)
        self.ad_res_path = Path(ad_res_path)
        self.data_models_path = self.revstream_path / "data_models"
        
        self.cross_reference_results = {
            "timestamp": datetime.now().isoformat(),
            "ad_res_j7_stats": {},
            "evidence_mapping": {},
            "missing_references": [],
            "recommendations": []
        }
    
    def analyze_ad_res_j7_structure(self):
        """Analyze the ad-res-j7 repository structure"""
        print("Analyzing ad-res-j7 repository structure...")
        
        # Count files by category
        evidence_dirs = {
            "ANNEXURES": 0,
            "FINAL_AFFIDAVIT_PACKAGE": 0,
            "case_2025_137857": 0,
            "evidence": 0,
            "jax-response": 0,
            "docs": 0
        }
        
        for dir_name in evidence_dirs.keys():
            dir_path = self.ad_res_path / dir_name
            if dir_path.exists():
                # Count all files recursively
                files = list(dir_path.rglob("*"))
                evidence_dirs[dir_name] = len([f for f in files if f.is_file()])
        
        self.cross_reference_results["ad_res_j7_stats"] = {
            "repository_path": str(self.ad_res_path),
            "evidence_directories": evidence_dirs,
            "total_evidence_files": sum(evidence_dirs.values())
        }
        
        print(f"Found {sum(evidence_dirs.values())} evidence files across {len(evidence_dirs)} directories")
    
    def load_revstream_models(self):
        """Load revstream1 data models"""
        print("Loading revstream1 data models...")
        
        # Load entities
        entities_file = self.data_models_path / "entities" / "entities_refined_2025_11_23_v10.json"
        with open(entities_file, 'r') as f:
            self.entities = json.load(f)
        
        # Load events
        events_file = self.data_models_path / "events" / "events_refined_2025_11_23_v11.json"
        with open(events_file, 'r') as f:
            self.events = json.load(f)
        
        # Load relations
        relations_file = self.data_models_path / "relations" / "relations_refined_2025_11_23_v8.json"
        with open(relations_file, 'r') as f:
            self.relations = json.load(f)
    
    def validate_evidence_references(self):
        """Validate that evidence file references exist in ad-res-j7"""
        print("Validating evidence file references...")
        
        missing_files = []
        validated_files = []
        
        # Check entity evidence files
        entities_data = self.entities.get("entities", {})
        for entity_type, entity_list in entities_data.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    entity_id = entity.get("entity_id", "UNKNOWN")
                    evidence_files = entity.get("evidence_files", [])
                    
                    for evidence_file in evidence_files:
                        # Check if file exists in ad-res-j7
                        file_path = self.ad_res_path / evidence_file.lstrip("./")
                        if file_path.exists():
                            validated_files.append({
                                "entity_id": entity_id,
                                "file": evidence_file,
                                "status": "validated"
                            })
                        else:
                            # Try to find similar files
                            missing_files.append({
                                "entity_id": entity_id,
                                "file": evidence_file,
                                "status": "not_found"
                            })
        
        # Check event evidence files
        events_list = self.events.get("events", [])
        for event in events_list:
            event_id = event.get("event_id", "UNKNOWN")
            evidence_files = event.get("evidence_files", [])
            
            for evidence_file in evidence_files:
                file_path = self.ad_res_path / evidence_file.lstrip("./")
                if file_path.exists():
                    validated_files.append({
                        "event_id": event_id,
                        "file": evidence_file,
                        "status": "validated"
                    })
                else:
                    missing_files.append({
                        "event_id": event_id,
                        "file": evidence_file,
                        "status": "not_found"
                    })
        
        self.cross_reference_results["evidence_mapping"] = {
            "validated_files_count": len(validated_files),
            "missing_files_count": len(missing_files),
            "validated_files": validated_files[:50],  # Sample
            "missing_files": missing_files[:50]  # Sample
        }
        
        if missing_files:
            self.cross_reference_results["missing_references"] = missing_files
    
    def generate_evidence_enhancement_recommendations(self):
        """Generate recommendations for enhancing evidence references"""
        print("Generating evidence enhancement recommendations...")
        
        recommendations = []
        
        # Recommendation 1: Create direct evidence links
        recommendations.append({
            "priority": "HIGH",
            "category": "evidence_linking",
            "title": "Create Direct Evidence Links in GitHub Pages",
            "description": "Update all GitHub Pages evidence references to include direct links to specific files in ad-res-j7 repository",
            "implementation": "Add 'evidence_url' field to each evidence reference pointing to https://github.com/cogpy/ad-res-j7/blob/main/[file_path]",
            "impact": "Enables one-click access to source evidence documents from GitHub Pages"
        })
        
        # Recommendation 2: Create evidence summary pages
        recommendations.append({
            "priority": "HIGH",
            "category": "evidence_organization",
            "title": "Create Evidence Summary Pages for Each Application",
            "description": "Generate dedicated evidence summary pages for Application 1, 2, and 3 with categorized evidence links",
            "implementation": "Create application-1-evidence-detailed.md, application-2-evidence-detailed.md, application-3-evidence-detailed.md",
            "impact": "Provides clear, organized evidence presentation for legal review"
        })
        
        # Recommendation 3: Add evidence thumbnails
        recommendations.append({
            "priority": "MEDIUM",
            "category": "visualization",
            "title": "Add Evidence Thumbnails for Key Documents",
            "description": "Include thumbnail previews of key evidence documents in GitHub Pages",
            "implementation": "Generate thumbnails for PDFs and images, embed in evidence pages",
            "impact": "Provides visual preview of evidence documents"
        })
        
        # Recommendation 4: Create evidence timeline
        recommendations.append({
            "priority": "HIGH",
            "category": "timeline_integration",
            "title": "Create Interactive Evidence Timeline",
            "description": "Generate an interactive timeline showing events with linked evidence documents",
            "implementation": "Create timeline.html with event markers linking to evidence files",
            "impact": "Provides chronological view of evidence with direct access to supporting documents"
        })
        
        # Recommendation 5: Validate all evidence file paths
        recommendations.append({
            "priority": "HIGH",
            "category": "data_integrity",
            "title": "Validate and Update All Evidence File Paths",
            "description": "Ensure all evidence file paths in data models point to valid files in ad-res-j7",
            "implementation": "Run validation script and update broken references",
            "impact": "Ensures all evidence references are valid and accessible"
        })
        
        self.cross_reference_results["recommendations"] = recommendations
    
    def save_results(self):
        """Save cross-reference results"""
        output_file = self.revstream_path / "AD_RES_J7_CROSS_REFERENCE_2025_11_25.json"
        with open(output_file, 'w') as f:
            json.dump(self.cross_reference_results, f, indent=2)
        print(f"\nCross-reference results saved to: {output_file}")
        
        # Create markdown summary
        self.create_markdown_summary()
    
    def create_markdown_summary(self):
        """Create markdown summary of cross-reference analysis"""
        md_content = f"""# ad-res-j7 Cross-Reference Analysis
**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Analysis Version:** 2025-11-25

## Overview

This analysis validates evidence references between revstream1 data models and the ad-res-j7 evidence repository.

## ad-res-j7 Repository Statistics

**Repository Path:** {self.cross_reference_results['ad_res_j7_stats']['repository_path']}
**Total Evidence Files:** {self.cross_reference_results['ad_res_j7_stats']['total_evidence_files']}

### Evidence by Directory

"""
        for dir_name, count in self.cross_reference_results['ad_res_j7_stats']['evidence_directories'].items():
            md_content += f"- **{dir_name}:** {count} files\n"
        
        md_content += f"""

## Evidence Validation Results

- **Validated Files:** {self.cross_reference_results['evidence_mapping']['validated_files_count']}
- **Missing Files:** {self.cross_reference_results['evidence_mapping']['missing_files_count']}

## Recommendations

"""
        for i, rec in enumerate(self.cross_reference_results['recommendations'], 1):
            md_content += f"\n### {i}. [{rec['priority']}] {rec['title']}\n"
            md_content += f"**Category:** {rec['category']}\n"
            md_content += f"**Description:** {rec['description']}\n"
            md_content += f"**Implementation:** {rec['implementation']}\n"
            md_content += f"**Impact:** {rec['impact']}\n\n"
        
        md_file = self.revstream_path / "AD_RES_J7_CROSS_REFERENCE_2025_11_25.md"
        with open(md_file, 'w') as f:
            f.write(md_content)
        print(f"Markdown summary saved to: {md_file}")
    
    def run_analysis(self):
        """Run complete cross-reference analysis"""
        print("Starting ad-res-j7 cross-reference analysis...")
        self.analyze_ad_res_j7_structure()
        self.load_revstream_models()
        self.validate_evidence_references()
        self.generate_evidence_enhancement_recommendations()
        self.save_results()
        print("\nCross-reference analysis complete!")

if __name__ == "__main__":
    referencer = EvidenceCrossReferencer(
        "/home/ubuntu/revstream1",
        "/home/ubuntu/ad-res-j7"
    )
    referencer.run_analysis()
