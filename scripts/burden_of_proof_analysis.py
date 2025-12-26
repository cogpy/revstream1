#!/usr/bin/env python3
"""
Analyzes evidence against burden of proof standards for each filing type:
- Civil Actions (50% - balance of probabilities)
- Criminal Actions (95%+ - beyond reasonable doubt)
- CIPC Complaints (Administrative - reasonable grounds)
- POPIA Criminal Complaints (95%+ - beyond reasonable doubt)
- Commercial Crime (95%+ - beyond reasonable doubt)
- NPA Tax Fraud (95%+ - beyond reasonable doubt)
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class BurdenOfProofAnalyzer:
    def __init__(self, revstream_path: str):
        self.revstream_path = revstream_path
        self.events = []
        self.entities = {}
        self.analysis = {
            "timestamp": datetime.now().isoformat(),
            "civil_actions": {
                "burden_of_proof": "50% - Balance of Probabilities",
                "events_meeting_standard": [],
                "events_approaching_standard": [],
                "events_insufficient": [],
                "strength_assessment": {}
            },
            "criminal_actions": {
                "burden_of_proof": "95%+ - Beyond Reasonable Doubt",
                "events_meeting_standard": [],
                "events_approaching_standard": [],
                "events_insufficient": [],
                "strength_assessment": {}
            },
            "cipc_complaints": {
                "burden_of_proof": "Reasonable Grounds",
                "events_meeting_standard": [],
                "events_approaching_standard": [],
                "events_insufficient": [],
                "strength_assessment": {}
            },
            "popia_complaints": {
                "burden_of_proof": "95%+ - Beyond Reasonable Doubt",
                "events_meeting_standard": [],
                "events_approaching_standard": [],
                "events_insufficient": [],
                "strength_assessment": {}
            },
            "commercial_crime": {
                "burden_of_proof": "95%+ - Beyond Reasonable Doubt",
                "events_meeting_standard": [],
                "events_approaching_standard": [],
                "events_insufficient": [],
                "strength_assessment": {}
            },
            "npa_tax_fraud": {
                "burden_of_proof": "95%+ - Beyond Reasonable Doubt",
                "events_meeting_standard": [],
                "events_approaching_standard": [],
                "events_insufficient": [],
                "strength_assessment": {}
            }
        }

    def load_data(self):
        """Load events and entities data"""
        events_file = os.path.join(
            self.revstream_path,
            'data_models/events/events_refined_2025_11_28_v25.json'
        )
        entities_file = os.path.join(
            self.revstream_path,
            'data_models/entities/entities.json'
        )
        
        try:
            with open(events_file, 'r') as f:
                events_data = json.load(f)
                self.events = events_data.get("events", [])
            with open(entities_file, 'r') as f:
                entities_data = json.load(f)
                persons = entities_data.get("entities", {}).get("persons", [])
                orgs = entities_data.get("entities", {}).get("organizations", [])
                self.entities = {e["entity_id"]: e for e in persons + orgs if "entity_id" in e}
        except Exception as e:
            print(f"Error loading data: {e}")

    def assess_evidence_strength(self, event: Dict[str, Any]) -> float:
        """
        Assess evidence strength on a scale of 0-1.0
        Factors: has evidence files, has financial impact, has documentation, has witness involvement
        """
        strength = 0.0
        
        # Evidence files present
        if event.get("evidence_files") and len(event.get("evidence_files", [])) > 0:
            strength += 0.25
        
        # Financial impact documented
        if event.get("financial_impact") and event.get("financial_impact") != "0":
            strength += 0.25
        
        # Description/documentation present
        if event.get("description") and len(event.get("description", "")) > 50:
            strength += 0.25
        
        # Multiple entities involved (corroboration)
        if len(event.get("entities_involved", [])) > 1:
            strength += 0.25
        
        return min(strength, 1.0)

    def categorize_event(self, event: Dict[str, Any]) -> List[str]:
        """Categorize event by filing type relevance"""
        categories = []
        category = event.get("category", "").lower()
        
        if "financial" in category or "fraud" in category or "theft" in category:
            categories.append("civil_actions")
            categories.append("criminal_actions")
            categories.append("commercial_crime")
        
        if "popia" in category or "privacy" in category or "data" in category:
            categories.append("popia_complaints")
        
        if "trust" in category or "misconduct" in category:
            categories.append("cipc_complaints")
        
        if "tax" in category or "financial" in category:
            categories.append("npa_tax_fraud")
        
        return categories if categories else ["civil_actions"]

    def analyze_events(self):
        """Analyze all events against burden of proof standards"""
        print(f"Analyzing {len(self.events)} events against burden of proof standards...")
        
        for event in self.events:
            event_id = event.get("event_id", "unknown")
            strength = self.assess_evidence_strength(event)
            categories = self.categorize_event(event)
            
            event_summary = {
                "event_id": event_id,
                "title": event.get("title", "Unknown"),
                "date": event.get("date", "N/A"),
                "strength": strength,
                "evidence_count": len(event.get("evidence_files", [])),
                "financial_impact": event.get("financial_impact", "0")
            }
            
            for category in categories:
                if strength >= 0.75:  # 75%+ strength = meets high standard
                    self.analysis[category]["events_meeting_standard"].append(event_summary)
                elif strength >= 0.50:  # 50-75% = approaching standard
                    self.analysis[category]["events_approaching_standard"].append(event_summary)
                else:  # Below 50% = insufficient
                    self.analysis[category]["events_insufficient"].append(event_summary)

    def generate_report(self) -> str:
        """Generate comprehensive burden of proof analysis report"""
        report = []
        report.append("# Burden of Proof Analysis Report")
        report.append(f"**Generated:** {self.analysis['timestamp']}\n")
        report.append("This report analyzes all timeline events against the burden of proof standards for different filing types.\n")
        
        filing_types = [
            ("civil_actions", "Civil Actions (50% - Balance of Probabilities)"),
            ("criminal_actions", "Criminal Actions (95%+ - Beyond Reasonable Doubt)"),
            ("cipc_complaints", "CIPC Complaints (Reasonable Grounds)"),
            ("popia_complaints", "POPIA Criminal Complaints (95%+ - Beyond Reasonable Doubt)"),
            ("commercial_crime", "Commercial Crime (95%+ - Beyond Reasonable Doubt)"),
            ("npa_tax_fraud", "NPA Tax Fraud (95%+ - Beyond Reasonable Doubt)")
        ]
        
        for filing_key, filing_name in filing_types:
            filing_data = self.analysis[filing_key]
            report.append(f"\n## {filing_name}\n")
            report.append(f"**Burden of Proof:** {filing_data['burden_of_proof']}\n")
            
            meeting = filing_data["events_meeting_standard"]
            approaching = filing_data["events_approaching_standard"]
            insufficient = filing_data["events_insufficient"]
            
            report.append(f"- **Events Meeting Standard:** {len(meeting)}")
            report.append(f"- **Events Approaching Standard:** {len(approaching)}")
            report.append(f"- **Events Insufficient:** {len(insufficient)}\n")
            
            if meeting:
                report.append(f"### Events Meeting Burden of Proof ({len(meeting)})\n")
                for event in meeting[:5]:  # Show top 5
                    report.append(f"- **{event['date']}:** {event['title']} (Strength: {event['strength']:.0%})")
                if len(meeting) > 5:
                    report.append(f"- ... and {len(meeting) - 5} more events\n")
                report.append("")
        
        return "\n".join(report)

    def run_analysis(self):
        """Execute full analysis"""
        print("Starting burden of proof analysis...")
        self.load_data()
        print(f"✓ Loaded {len(self.events)} events")
        self.analyze_events()
        print("✓ Events analyzed")
        
        # Save analysis
        analysis_file = os.path.join(
            self.revstream_path,
            f"BURDEN_OF_PROOF_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
        )
        with open(analysis_file, 'w') as f:
            json.dump(self.analysis, f, indent=2)
        print(f"✓ Analysis saved to {analysis_file}")
        
        # Generate report
        report = self.generate_report()
        report_file = os.path.join(
            self.revstream_path,
            f"BURDEN_OF_PROOF_REPORT_{datetime.now().strftime('%Y_%m_%d')}.md"
        )
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"✓ Report saved to {report_file}")
        
        return self.analysis, report

if __name__ == "__main__":
    analyzer = BurdenOfProofAnalyzer("/home/ubuntu/revstream1")
    analysis, report = analyzer.run_analysis()
    print("\n" + report)
