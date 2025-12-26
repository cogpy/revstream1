#!/usr/bin/env python3
"""
Comprehensive Data Model Analysis for revstream1
Date: 2025-11-25
Purpose: Analyze entities, relations, events, and timelines for refinement opportunities
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class DataModelAnalyzer:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.data_models_path = self.base_path / "data_models"
        self.analysis_results = {
            "timestamp": datetime.now().isoformat(),
            "entities_analysis": {},
            "events_analysis": {},
            "relations_analysis": {},
            "timeline_analysis": {},
            "issues_found": [],
            "recommendations": []
        }
    
    def load_latest_models(self):
        """Load the latest version of each data model"""
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
        
        # Load timeline
        timeline_file = self.data_models_path / "timelines" / "timeline_refined_2025_11_23_v9.json"
        with open(timeline_file, 'r') as f:
            self.timeline = json.load(f)
    
    def analyze_entities(self):
        """Analyze entity structure and completeness"""
        print("Analyzing entities...")
        
        entities_data = self.entities.get("entities", {})
        total_entities = 0
        entities_by_type = defaultdict(int)
        missing_evidence = []
        missing_github_refs = []
        missing_ad_res_refs = []
        
        for entity_type, entity_list in entities_data.items():
            if isinstance(entity_list, list):
                total_entities += len(entity_list)
                entities_by_type[entity_type] = len(entity_list)
                
                for entity in entity_list:
                    entity_id = entity.get("entity_id", "UNKNOWN")
                    
                    # Check for missing evidence files
                    if not entity.get("evidence_files") or len(entity.get("evidence_files", [])) == 0:
                        missing_evidence.append(entity_id)
                    
                    # Check for missing GitHub Pages references
                    if not entity.get("github_pages_reference"):
                        missing_github_refs.append(entity_id)
                    
                    # Check for missing ad-res-j7 references
                    if not entity.get("ad_res_j7_references"):
                        missing_ad_res_refs.append(entity_id)
        
        self.analysis_results["entities_analysis"] = {
            "total_entities": total_entities,
            "entities_by_type": dict(entities_by_type),
            "missing_evidence_files": missing_evidence,
            "missing_github_pages_refs": missing_github_refs,
            "missing_ad_res_j7_refs": missing_ad_res_refs,
            "metadata": self.entities.get("metadata", {})
        }
        
        if missing_evidence:
            self.analysis_results["issues_found"].append({
                "category": "entities",
                "severity": "medium",
                "issue": f"{len(missing_evidence)} entities missing evidence files",
                "entities": missing_evidence
            })
        
        if missing_github_refs:
            self.analysis_results["issues_found"].append({
                "category": "entities",
                "severity": "high",
                "issue": f"{len(missing_github_refs)} entities missing GitHub Pages references",
                "entities": missing_github_refs
            })
    
    def analyze_events(self):
        """Analyze event structure and timeline coverage"""
        print("Analyzing events...")
        
        events_list = self.events.get("events", [])
        total_events = len(events_list)
        events_by_category = defaultdict(int)
        events_by_phase = defaultdict(int)
        events_with_financial_impact = 0
        missing_evidence = []
        missing_github_refs = []
        events_without_dates = []
        
        for event in events_list:
            event_id = event.get("event_id", "UNKNOWN")
            
            # Count by category
            category = event.get("category", "uncategorized")
            events_by_category[category] += 1
            
            # Count by phase
            phase = event.get("timeline_phase", "unassigned")
            events_by_phase[phase] += 1
            
            # Check financial impact
            if event.get("financial_impact"):
                events_with_financial_impact += 1
            
            # Check for missing dates
            if not event.get("date"):
                events_without_dates.append(event_id)
            
            # Check for missing evidence
            if not event.get("evidence_files") or len(event.get("evidence_files", [])) == 0:
                missing_evidence.append(event_id)
            
            # Check for missing GitHub references
            if not event.get("github_pages_reference"):
                missing_github_refs.append(event_id)
        
        self.analysis_results["events_analysis"] = {
            "total_events": total_events,
            "events_by_category": dict(events_by_category),
            "events_by_phase": dict(events_by_phase),
            "events_with_financial_impact": events_with_financial_impact,
            "events_without_dates": events_without_dates,
            "missing_evidence_files": missing_evidence,
            "missing_github_pages_refs": missing_github_refs,
            "metadata": self.events.get("metadata", {})
        }
        
        if events_without_dates:
            self.analysis_results["issues_found"].append({
                "category": "events",
                "severity": "high",
                "issue": f"{len(events_without_dates)} events missing dates",
                "events": events_without_dates
            })
    
    def analyze_relations(self):
        """Analyze relation structure and completeness"""
        print("Analyzing relations...")
        
        relations_data = self.relations.get("relations", {})
        total_relations = 0
        relations_by_type = defaultdict(int)
        missing_evidence = []
        missing_github_refs = []
        
        for relation_type, relation_list in relations_data.items():
            if isinstance(relation_list, list):
                total_relations += len(relation_list)
                relations_by_type[relation_type] = len(relation_list)
                
                for relation in relation_list:
                    relation_id = relation.get("relation_id", "UNKNOWN")
                    
                    # Check for missing evidence
                    if not relation.get("evidence") or len(relation.get("evidence", [])) == 0:
                        missing_evidence.append(relation_id)
                    
                    # Check for missing GitHub references
                    if not relation.get("github_pages_reference"):
                        missing_github_refs.append(relation_id)
        
        self.analysis_results["relations_analysis"] = {
            "total_relations": total_relations,
            "relations_by_type": dict(relations_by_type),
            "missing_evidence": missing_evidence,
            "missing_github_pages_refs": missing_github_refs,
            "metadata": self.relations.get("metadata", {})
        }
    
    def analyze_timeline(self):
        """Analyze timeline structure and phase coverage"""
        print("Analyzing timeline...")
        
        timeline_phases = self.timeline.get("timeline_phases", {})
        total_phases = len(timeline_phases)
        events_per_phase = {}
        phases_without_evidence_refs = []
        
        for phase_key, phase_data in timeline_phases.items():
            phase_id = phase_data.get("phase_id", "UNKNOWN")
            events_count = len(phase_data.get("events", []))
            events_per_phase[phase_id] = events_count
            
            # Check for missing evidence repository references
            if not phase_data.get("evidence_repository"):
                phases_without_evidence_refs.append(phase_id)
        
        self.analysis_results["timeline_analysis"] = {
            "total_phases": total_phases,
            "events_per_phase": events_per_phase,
            "phases_without_evidence_refs": phases_without_evidence_refs,
            "metadata": self.timeline.get("metadata", {})
        }
    
    def generate_recommendations(self):
        """Generate recommendations based on analysis"""
        print("Generating recommendations...")
        
        recommendations = []
        
        # Recommendation 1: Complete missing GitHub Pages references
        missing_gh_entities = len(self.analysis_results["entities_analysis"].get("missing_github_pages_refs", []))
        missing_gh_events = len(self.analysis_results["events_analysis"].get("missing_github_pages_refs", []))
        missing_gh_relations = len(self.analysis_results["relations_analysis"].get("missing_github_pages_refs", []))
        
        if missing_gh_entities > 0 or missing_gh_events > 0 or missing_gh_relations > 0:
            recommendations.append({
                "priority": "HIGH",
                "category": "github_pages_integration",
                "title": "Complete GitHub Pages References",
                "description": f"Add GitHub Pages references to {missing_gh_entities} entities, {missing_gh_events} events, and {missing_gh_relations} relations",
                "impact": "Improves evidence navigation and cross-referencing"
            })
        
        # Recommendation 2: Enhance evidence file references
        missing_ev_entities = len(self.analysis_results["entities_analysis"].get("missing_evidence_files", []))
        missing_ev_events = len(self.analysis_results["events_analysis"].get("missing_evidence_files", []))
        
        if missing_ev_entities > 0 or missing_ev_events > 0:
            recommendations.append({
                "priority": "HIGH",
                "category": "evidence_completeness",
                "title": "Add Evidence File References",
                "description": f"Add evidence file references to {missing_ev_entities} entities and {missing_ev_events} events",
                "impact": "Ensures all data points are backed by verifiable evidence"
            })
        
        # Recommendation 3: Create application-specific evidence pages
        recommendations.append({
            "priority": "MEDIUM",
            "category": "github_pages_organization",
            "title": "Enhance Application-Specific Evidence Pages",
            "description": "Ensure each of the 3 applications has a dedicated evidence page with clear cross-references to ad-res-j7",
            "impact": "Improves evidence organization and accessibility for legal review"
        })
        
        # Recommendation 4: Add timeline visualization
        recommendations.append({
            "priority": "MEDIUM",
            "category": "visualization",
            "title": "Create Interactive Timeline Visualization",
            "description": "Generate visual timeline showing all 8 phases with events, financial impact, and evidence links",
            "impact": "Provides clear visual representation of case progression"
        })
        
        # Recommendation 5: Cross-reference validation
        recommendations.append({
            "priority": "HIGH",
            "category": "data_integrity",
            "title": "Validate Cross-References Between Models",
            "description": "Ensure all event IDs referenced in entities exist in events model, and all entity IDs in relations exist",
            "impact": "Prevents broken references and ensures data model integrity"
        })
        
        # Recommendation 6: Evidence index enhancement
        recommendations.append({
            "priority": "MEDIUM",
            "category": "evidence_index",
            "title": "Enhance Evidence Index with Direct File Links",
            "description": "Update evidence-index-enhanced.md with direct links to specific files in ad-res-j7 repository",
            "impact": "Enables one-click access to source evidence documents"
        })
        
        self.analysis_results["recommendations"] = recommendations
    
    def save_analysis(self):
        """Save analysis results to file"""
        output_file = self.base_path / "DATA_MODEL_ANALYSIS_2025_11_25.json"
        with open(output_file, 'w') as f:
            json.dump(self.analysis_results, f, indent=2)
        print(f"\nAnalysis saved to: {output_file}")
        
        # Also create a markdown summary
        self.create_markdown_summary()
    
    def create_markdown_summary(self):
        """Create a markdown summary of the analysis"""
        md_content = f"""# Data Model Analysis Summary
**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Analysis Version:** 2025-11-25

## Overview

This analysis reviews the current state of entities, events, relations, and timelines in the revstream1 repository.

## Entities Analysis

- **Total Entities:** {self.analysis_results['entities_analysis']['total_entities']}
- **Entities by Type:** {json.dumps(self.analysis_results['entities_analysis']['entities_by_type'], indent=2)}
- **Missing Evidence Files:** {len(self.analysis_results['entities_analysis']['missing_evidence_files'])} entities
- **Missing GitHub Pages References:** {len(self.analysis_results['entities_analysis']['missing_github_pages_refs'])} entities
- **Missing ad-res-j7 References:** {len(self.analysis_results['entities_analysis']['missing_ad_res_j7_refs'])} entities

## Events Analysis

- **Total Events:** {self.analysis_results['events_analysis']['total_events']}
- **Events with Financial Impact:** {self.analysis_results['events_analysis']['events_with_financial_impact']}
- **Events by Category:** {json.dumps(self.analysis_results['events_analysis']['events_by_category'], indent=2)}
- **Events by Phase:** {json.dumps(self.analysis_results['events_analysis']['events_by_phase'], indent=2)}
- **Events Without Dates:** {len(self.analysis_results['events_analysis']['events_without_dates'])}
- **Missing Evidence Files:** {len(self.analysis_results['events_analysis']['missing_evidence_files'])} events

## Relations Analysis

- **Total Relations:** {self.analysis_results['relations_analysis']['total_relations']}
- **Relations by Type:** {json.dumps(self.analysis_results['relations_analysis']['relations_by_type'], indent=2)}
- **Missing Evidence:** {len(self.analysis_results['relations_analysis']['missing_evidence'])} relations
- **Missing GitHub Pages References:** {len(self.analysis_results['relations_analysis']['missing_github_pages_refs'])} relations

## Timeline Analysis

- **Total Phases:** {self.analysis_results['timeline_analysis']['total_phases']}
- **Events per Phase:** {json.dumps(self.analysis_results['timeline_analysis']['events_per_phase'], indent=2)}

## Issues Found

"""
        for issue in self.analysis_results['issues_found']:
            md_content += f"\n### {issue['severity'].upper()}: {issue['issue']}\n"
            md_content += f"**Category:** {issue['category']}\n\n"
        
        md_content += "\n## Recommendations\n\n"
        for i, rec in enumerate(self.analysis_results['recommendations'], 1):
            md_content += f"\n### {i}. [{rec['priority']}] {rec['title']}\n"
            md_content += f"**Category:** {rec['category']}\n"
            md_content += f"**Description:** {rec['description']}\n"
            md_content += f"**Impact:** {rec['impact']}\n\n"
        
        md_file = self.base_path / "DATA_MODEL_ANALYSIS_2025_11_25.md"
        with open(md_file, 'w') as f:
            f.write(md_content)
        print(f"Markdown summary saved to: {md_file}")
    
    def run_full_analysis(self):
        """Run complete analysis"""
        print("Starting comprehensive data model analysis...")
        self.load_latest_models()
        self.analyze_entities()
        self.analyze_events()
        self.analyze_relations()
        self.analyze_timeline()
        self.generate_recommendations()
        self.save_analysis()
        print("\nAnalysis complete!")

if __name__ == "__main__":
    analyzer = DataModelAnalyzer("/home/ubuntu/revstream1")
    analyzer.run_full_analysis()
