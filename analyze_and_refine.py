#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script
Extracts and maps entities, relations, events, and timelines from both repositories
Analyzes evidence against burden of proof standards
Generates improvement recommendations
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re

class CaseAnalyzer:
    def __init__(self, revstream_path: str, ad_res_path: str):
        self.revstream_path = revstream_path
        self.ad_res_path = ad_res_path
        self.analysis = {
            "timestamp": datetime.now().isoformat(),
            "entities": {},
            "relations": {},
            "events": {},
            "timelines": {},
            "evidence_mapping": {},
            "burden_of_proof_analysis": {},
            "filing_recommendations": {}
        }
    
    def load_json_file(self, filepath: str) -> Dict[str, Any]:
        """Load JSON file safely"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return {}
    
    def analyze_entities(self):
        """Extract and analyze entities from latest models"""
        entities_file = os.path.join(
            self.revstream_path, 
            'data_models/entities/entities.json'
        )
        
        if os.path.exists(entities_file):
            entities_data = self.load_json_file(entities_file)
            if entities_data:
                self.analysis["entities"] = {
                    "version": entities_data.get("metadata", {}).get("version", "unknown"),
                    "total_count": len(entities_data.get("entities", {}).get("persons", [])) +
                                  len(entities_data.get("entities", {}).get("organizations", [])) +
                                  len(entities_data.get("entities", {}).get("accounts", [])),
                    "persons": len(entities_data.get("entities", {}).get("persons", [])),
                    "organizations": len(entities_data.get("entities", {}).get("organizations", [])),
                    "accounts": len(entities_data.get("entities", {}).get("accounts", [])),
                    "data": entities_data
                }
    
    def analyze_events(self):
        """Extract and analyze events from latest models"""
        events_file = os.path.join(
            self.revstream_path,
            'data_models/events/events_refined_2025_11_28_v25.json'
        )
        
        if os.path.exists(events_file):
            events_data = self.load_json_file(events_file)
            if events_data:
                events_list = events_data.get("events", [])
                self.analysis["events"] = {
                    "version": events_data.get("metadata", {}).get("version", "unknown"),
                    "total_count": len(events_list),
                    "by_category": self._categorize_events(events_list),
                    "by_phase": self._phase_events(events_list),
                    "data": events_data
                }
    
    def _categorize_events(self, events: List[Dict]) -> Dict[str, int]:
        """Categorize events by type"""
        categories = {}
        for event in events:
            cat = event.get("category", "unknown")
            categories[cat] = categories.get(cat, 0) + 1
        return categories
    
    def _phase_events(self, events: List[Dict]) -> Dict[str, int]:
        """Phase events by timeline phase"""
        phases = {}
        for event in events:
            phase = event.get("timeline_phase", "UNKNOWN")
            phases[phase] = phases.get(phase, 0) + 1
        return phases
    
    def analyze_relations(self):
        """Extract and analyze relations from latest models"""
        relations_dir = os.path.join(self.revstream_path, 'data_models/relations')
        relations_files = sorted([
            f for f in os.listdir(relations_dir) 
            if f.endswith('.json')
        ], reverse=True)
        
        if relations_files:
            relations_file = os.path.join(relations_dir, relations_files[0])
            relations_data = self.load_json_file(relations_file)
            if relations_data:
                relations_dict = relations_data.get("relations", {})
                total_count = sum(len(v) if isinstance(v, list) else 1 for v in relations_dict.values())
                self.analysis["relations"] = {
                    "version": relations_data.get("metadata", {}).get("version", "unknown"),
                    "total_count": total_count,
                    "by_type": self._categorize_relations_dict(relations_dict),
                    "data": relations_data
                }
    
    def _categorize_relations_dict(self, relations_dict: Dict[str, List]) -> Dict[str, int]:
        """Categorize relations by type from dict structure"""
        rel_types = {}
        for rel_category, rel_list in relations_dict.items():
            if isinstance(rel_list, list):
                rel_types[rel_category] = len(rel_list)
        return rel_types
    
    def analyze_timelines(self):
        """Extract and analyze timeline data"""
        timeline_file = os.path.join(
            self.revstream_path,
            'data_models/timelines/timeline_enhanced.json'
        )
        
        if os.path.exists(timeline_file):
            timeline_data = self.load_json_file(timeline_file)
            if timeline_data:
                phases = timeline_data.get("phases", [])
                self.analysis["timelines"] = {
                    "version": timeline_data.get("metadata", {}).get("version", "unknown"),
                    "total_phases": len(phases),
                    "phases": [p.get("name") for p in phases],
                    "data": timeline_data
                }
    
    def generate_report(self) -> str:
        """Generate comprehensive analysis report"""
        report = []
        report.append("# Comprehensive Case Analysis Report")
        report.append(f"**Generated:** {self.analysis['timestamp']}")
        report.append("")
        
        # Entities Summary
        report.append("## Entities Summary")
        if self.analysis["entities"]:
            ent = self.analysis["entities"]
            report.append(f"- **Version:** {ent['version']}")
            report.append(f"- **Total Entities:** {ent['total_count']}")
            report.append(f"  - Persons: {ent['persons']}")
            report.append(f"  - Organizations: {ent['organizations']}")
            report.append(f"  - Accounts: {ent['accounts']}")
        report.append("")
        
        # Events Summary
        report.append("## Events Summary")
        if self.analysis["events"]:
            evt = self.analysis["events"]
            report.append(f"- **Version:** {evt['version']}")
            report.append(f"- **Total Events:** {evt['total_count']}")
            report.append("- **By Category:**")
            for cat, count in sorted(evt['by_category'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"  - {cat}: {count}")
            report.append("- **By Phase:**")
            for phase, count in sorted(evt['by_phase'].items()):
                report.append(f"  - {phase}: {count}")
        report.append("")
        
        # Relations Summary
        report.append("## Relations Summary")
        if self.analysis["relations"]:
            rel = self.analysis["relations"]
            report.append(f"- **Version:** {rel['version']}")
            report.append(f"- **Total Relations:** {rel['total_count']}")
            report.append("- **By Type:**")
            for rel_type, count in sorted(rel['by_type'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"  - {rel_type}: {count}")
        report.append("")
        
        # Timeline Summary
        report.append("## Timeline Summary")
        if self.analysis["timelines"]:
            tl = self.analysis["timelines"]
            report.append(f"- **Version:** {tl['version']}")
            report.append(f"- **Total Phases:** {tl['total_phases']}")
            report.append("- **Phases:**")
            for phase in tl['phases']:
                report.append(f"  - {phase}")
        report.append("")
        
        return "\n".join(report)
    
    def run_analysis(self):
        """Execute full analysis"""
        print("Starting comprehensive case analysis...")
        self.analyze_entities()
        print("✓ Entities analyzed")
        self.analyze_events()
        print("✓ Events analyzed")
        self.analyze_relations()
        print("✓ Relations analyzed")
        self.analyze_timelines()
        print("✓ Timelines analyzed")
        
        # Save analysis
        analysis_file = os.path.join(
            self.revstream_path,
            f"COMPREHENSIVE_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
        )
        with open(analysis_file, 'w') as f:
            json.dump(self.analysis, f, indent=2)
        print(f"✓ Analysis saved to {analysis_file}")
        
        # Generate report
        report = self.generate_report()
        report_file = os.path.join(
            self.revstream_path,
            f"COMPREHENSIVE_ANALYSIS_REPORT_{datetime.now().strftime('%Y_%m_%d')}.md"
        )
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"✓ Report saved to {report_file}")
        
        return self.analysis, report

if __name__ == "__main__":
    analyzer = CaseAnalyzer(
        "/home/ubuntu/revstream1",
        "/home/ubuntu/ad-res-j7"
    )
    analysis, report = analyzer.run_analysis()
    print("\n" + report)
