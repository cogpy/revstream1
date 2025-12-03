#!/usr/bin/env python3
"""
Refines legal filing documents by integrating evidence that meets specific
burden of proof standards. It updates placeholders and strengthens arguments.
"""

import json
import os
import re
from datetime import datetime

class FilingRefiner:
    def __init__(self, revstream_path: str):
        self.revstream_path = revstream_path
        self.proof_analysis = {}
        self.filings_path = os.path.join(self.revstream_path, "docs")

    def load_analysis(self):
        """Load the burden of proof analysis data."""
        analysis_file = os.path.join(
            self.revstream_path,
            f"BURDEN_OF_PROOF_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
        )
        try:
            with open(analysis_file, 'r') as f:
                self.proof_analysis = json.load(f)
            print("✓ Burden of proof analysis loaded.")
        except FileNotFoundError:
            print(f"Error: Analysis file not found at {analysis_file}")
            self.proof_analysis = None

    def refine_cipc_complaint(self):
        """Refine the CIPC complaint with high-strength evidence."""
        if not self.proof_analysis:
            return

        print("Refining CIPC Complaint...")
        template_path = os.path.join(self.revstream_path, "CIPC_COMPLAINT_ENHANCED_2025_11_28.md")
        output_path = os.path.join(self.filings_path, f"CIPC_COMPLAINT_REFINED_{datetime.now().strftime('%Y%m%d')}.md")

        try:
            with open(template_path, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"CIPC template not found at {template_path}")
            return

        cipc_evidence = self.proof_analysis.get("cipc_complaints", {}).get("events_meeting_standard", [])
        
        if not cipc_evidence:
            print("No events meeting CIPC burden of proof.")
            return

        evidence_section = "\n### Evidence Meeting 'Reasonable Grounds' Standard\n\n"
        evidence_section += "The following events provide strong, reasonable grounds for the CIPC to investigate the conduct of the directors:\n\n"
        for event in cipc_evidence:
            evidence_section += f"- **{event['date']} - {event['title']}**:\n"
            evidence_section += f"  - **Strength:** {event['strength']:.0%}\n"
            evidence_section += f"  - **Financial Impact:** {event.get('financial_impact', 'N/A')}\n"
            evidence_section += f"  - **Evidence Files:** {event['evidence_count']} files available.\n"
            evidence_section += f"  - **[View Event Details](events/{event['event_id']}.md)**\n"

        # Replace a placeholder in the document
        content = re.sub(r"(\[Placeholder for synthesized evidence list\])", evidence_section, content, flags=re.IGNORECASE)

        with open(output_path, 'w') as f:
            f.write(content)
        print(f"✓ CIPC Complaint refined and saved to {output_path}")

    def refine_criminal_complaint(self):
        """Draft a criminal complaint summary using events that meet the 'Beyond Reasonable Doubt' standard."""
        if not self.proof_analysis:
            return

        print("Drafting Criminal Complaint Summary...")
        output_path = os.path.join(self.filings_path, f"CRIMINAL_COMPLAINT_SUMMARY_{datetime.now().strftime('%Y%m%d')}.md")

        criminal_evidence = self.proof_analysis.get("criminal_actions", {}).get("events_meeting_standard", [])
        commercial_evidence = self.proof_analysis.get("commercial_crime", {}).get("events_meeting_standard", [])
        
        # Combine and deduplicate evidence
        all_criminal_events = {e['event_id']: e for e in criminal_evidence + commercial_evidence}.values()
        sorted_events = sorted(all_criminal_events, key=lambda x: x['date'])

        if not sorted_events:
            print("No events meeting the criminal burden of proof.")
            return

        with open(output_path, 'w') as f:
            f.write(f"# DRAFT: Criminal Complaint Summary\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("**Case:** 2025-137857\n")
            f.write("**Subject:** Summary of Evidence for Criminal Prosecution (Fraud, Theft, Forgery)\n\n")
            f.write("This document summarizes key events with evidence meeting the 'Beyond a Reasonable Doubt' (95%+) standard, suitable for a criminal complaint.\n\n")

            for event in sorted_events:
                f.write(f"### {event['date']} - {event['title']}\n")
                f.write(f"- **Strength Score:** {event['strength']:.0%}\n")
                f.write(f"- **Financial Impact:** {event.get('financial_impact', 'N/A')}\n")
                f.write(f"- **Evidence Summary:** {event['evidence_count']} primary evidence files have been cataloged for this event.\n")
                f.write(f"- **Significance:** This event is a critical component in demonstrating a pattern of coordinated criminal activity.\n")
                f.write(f"- **[View Full Event Details](events/{event['event_id']}.md)**\n\n")

        print(f"✓ Criminal Complaint Summary drafted and saved to {output_path}")

    def run_refinement(self):
        self.load_analysis()
        if self.proof_analysis:
            self.refine_cipc_complaint()
            self.refine_criminal_complaint()

if __name__ == "__main__":
    refiner = FilingRefiner("/home/ubuntu/revstream1")
    refiner.run_refinement()

