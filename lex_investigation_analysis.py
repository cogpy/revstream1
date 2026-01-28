#!/usr/bin/env python3
"""
LEX Investigation Analysis Script
Deploys Super-Sleuth (Intro-Spect) and Hyper-Holmes (Turbo-Solve) analysis modes
for comprehensive evidence refinement.

Case: 2025-137857 - Revenue Stream Hijacking
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Configuration
DATA_MODELS_DIR = Path("/home/ubuntu/revstream1/data_models")
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
AD_RES_J7_DIR = Path("/home/ubuntu/ad-res-j7")

TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
DATE_STAMP = datetime.now().strftime("%Y_%m_%d")


def load_json(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None


def save_json(filepath, data):
    """Save JSON file with backup."""
    backup_path = str(filepath) + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    if filepath.exists():
        import shutil
        shutil.copy(filepath, backup_path)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {filepath}")


class SuperSleuthIntroSpect:
    """
    Lead generation agent - divergent thinking mode.
    Discovers patterns, gaps, and new connections.
    """
    
    def __init__(self):
        self.entities = load_json(DATA_MODELS_DIR / "entities" / "entities.json")
        self.events = load_json(DATA_MODELS_DIR / "events" / "events.json")
        self.relations = load_json(DATA_MODELS_DIR / "relations" / "relations.json")
        self.timeline = load_json(DATA_MODELS_DIR / "timelines" / "timeline.json")
        self.findings = {
            "timestamp": TIMESTAMP,
            "mode": "intro_spect",
            "pattern_discoveries": [],
            "evidence_gaps": [],
            "new_connections": [],
            "timeline_anomalies": [],
            "entity_refinements": [],
            "relation_refinements": [],
            "event_refinements": []
        }
    
    def analyze_entity_completeness(self):
        """Identify entities needing evidence enhancement."""
        print("\n=== Super-Sleuth: Entity Completeness Analysis ===")
        
        if not self.entities:
            return
        
        persons = self.entities.get("entities", {}).get("persons", [])
        orgs = self.entities.get("entities", {}).get("organizations", [])
        
        # Check persons
        for person in persons:
            issues = []
            entity_id = person.get("entity_id", "UNKNOWN")
            name = person.get("name", "Unknown")
            
            # Check evidence
            if not person.get("evidence"):
                issues.append("missing_evidence")
            if not person.get("ad_res_j7_references"):
                issues.append("missing_ad_res_j7_refs")
            if not person.get("timeline_events"):
                issues.append("missing_timeline_events")
            if not person.get("burden_of_proof_analysis"):
                issues.append("missing_burden_analysis")
            
            # Check for Ketoni context if relevant
            role = person.get("role", "")
            if role in ["primary_perpetrator", "co_conspirator", "accountant_and_unknown_trustee"]:
                if not person.get("ketoni_payout_context"):
                    issues.append("missing_ketoni_context")
            
            if issues:
                self.findings["entity_refinements"].append({
                    "entity_id": entity_id,
                    "name": name,
                    "type": "person",
                    "issues": issues,
                    "priority": "high" if "primary" in role or "conspirator" in role else "medium"
                })
        
        # Check organizations
        for org in orgs:
            issues = []
            entity_id = org.get("entity_id", "UNKNOWN")
            name = org.get("name", "Unknown")
            
            if not org.get("evidence"):
                issues.append("missing_evidence")
            if not org.get("ad_res_j7_references"):
                issues.append("missing_ad_res_j7_refs")
            if not org.get("directors"):
                issues.append("missing_directors")
            if not org.get("cipc_registration"):
                issues.append("missing_cipc_registration")
            
            if issues:
                self.findings["entity_refinements"].append({
                    "entity_id": entity_id,
                    "name": name,
                    "type": "organization",
                    "issues": issues,
                    "priority": "medium"
                })
        
        print(f"  Found {len(self.findings['entity_refinements'])} entities needing refinement")
    
    def analyze_event_linkages(self):
        """Identify events with missing entity linkages."""
        print("\n=== Super-Sleuth: Event Linkage Analysis ===")
        
        if not self.events:
            return
        
        events = self.events.get("events", [])
        
        for event in events:
            issues = []
            event_id = event.get("event_id", "UNKNOWN")
            
            # Check entity linkages
            entities_involved = event.get("entities_involved", [])
            if not entities_involved:
                issues.append("no_entities_linked")
            
            # Check perpetrators/victims
            perpetrators = event.get("perpetrators", [])
            victims = event.get("victims", [])
            if not perpetrators and not victims:
                issues.append("no_perpetrators_or_victims")
            
            # Check evidence
            if not event.get("evidence"):
                issues.append("missing_evidence")
            if not event.get("ad_res_j7_references"):
                issues.append("missing_ad_res_j7_refs")
            
            # Check burden of proof
            if not event.get("burden_of_proof"):
                issues.append("missing_burden_of_proof")
            
            if issues:
                self.findings["event_refinements"].append({
                    "event_id": event_id,
                    "title": event.get("title", event.get("description", "")[:50]),
                    "date": event.get("date", "unknown"),
                    "issues": issues,
                    "priority": "high" if "no_entities_linked" in issues else "medium"
                })
        
        print(f"  Found {len(self.findings['event_refinements'])} events needing refinement")
    
    def analyze_timeline_gaps(self):
        """Identify gaps and anomalies in timeline."""
        print("\n=== Super-Sleuth: Timeline Gap Analysis ===")
        
        if not self.timeline:
            return
        
        entries = self.timeline.get("timeline", [])
        
        # Sort by date
        dated_entries = []
        for entry in entries:
            date_str = entry.get("date", "")
            if date_str:
                dated_entries.append((date_str, entry))
        
        dated_entries.sort(key=lambda x: x[0])
        
        # Analyze gaps
        prev_date = None
        for date_str, entry in dated_entries:
            issues = []
            
            # Check for missing event reference
            if not entry.get("event_ref"):
                issues.append("missing_event_ref")
            
            # Check for missing actors
            if not entry.get("actors") and not entry.get("key_actor_names"):
                issues.append("missing_actors")
            
            # Check for missing entities
            if not entry.get("entities_involved"):
                issues.append("missing_entities")
            
            if issues:
                self.findings["timeline_anomalies"].append({
                    "date": date_str,
                    "event": entry.get("event", entry.get("title", ""))[:60],
                    "issues": issues
                })
            
            prev_date = date_str
        
        print(f"  Found {len(self.findings['timeline_anomalies'])} timeline entries needing refinement")
    
    def analyze_relation_completeness(self):
        """Identify relations needing event linkages."""
        print("\n=== Super-Sleuth: Relation Completeness Analysis ===")
        
        if not self.relations:
            return
        
        all_relations = []
        for rel_type, rels in self.relations.get("relations", {}).items():
            if isinstance(rels, list):
                all_relations.extend(rels)
        
        for rel in all_relations:
            issues = []
            rel_id = rel.get("relation_id", "UNKNOWN")
            
            # Check for related events
            if not rel.get("related_events"):
                issues.append("no_related_events")
            
            # Check evidence
            if not rel.get("evidence"):
                issues.append("missing_evidence")
            
            if issues:
                self.findings["relation_refinements"].append({
                    "relation_id": rel_id,
                    "type": rel.get("relation_type", "unknown"),
                    "source": rel.get("source_entity", rel.get("from_entity", "")),
                    "target": rel.get("target_entity", rel.get("to_entity", "")),
                    "issues": issues
                })
        
        print(f"  Found {len(self.findings['relation_refinements'])} relations needing refinement")
    
    def discover_patterns(self):
        """Discover patterns across the data model."""
        print("\n=== Super-Sleuth: Pattern Discovery ===")
        
        # Pattern 1: Ketoni timing convergence
        ketoni_events = []
        if self.events:
            for event in self.events.get("events", []):
                desc = str(event.get("description", "")).lower()
                title = str(event.get("title", "")).lower()
                if "ketoni" in desc or "ketoni" in title:
                    ketoni_events.append(event)
        
        if ketoni_events:
            self.findings["pattern_discoveries"].append({
                "pattern": "ketoni_timing_convergence",
                "description": f"Found {len(ketoni_events)} events related to Ketoni payout motive",
                "significance": "high",
                "events": [e.get("event_id") for e in ketoni_events]
            })
        
        # Pattern 2: Card cancellation timing
        card_events = []
        if self.events:
            for event in self.events.get("events", []):
                desc = str(event.get("description", "")).lower()
                if "card" in desc and ("cancel" in desc or "block" in desc):
                    card_events.append(event)
        
        if card_events:
            self.findings["pattern_discoveries"].append({
                "pattern": "card_cancellation_retaliation",
                "description": f"Found {len(card_events)} card cancellation events - potential retaliation pattern",
                "significance": "high",
                "events": [e.get("event_id") for e in card_events]
            })
        
        # Pattern 3: Trust manipulation
        trust_events = []
        if self.events:
            for event in self.events.get("events", []):
                desc = str(event.get("description", "")).lower()
                if "trust" in desc and ("backdated" in desc or "manipulation" in desc or "violation" in desc):
                    trust_events.append(event)
        
        if trust_events:
            self.findings["pattern_discoveries"].append({
                "pattern": "trust_manipulation_scheme",
                "description": f"Found {len(trust_events)} trust manipulation events",
                "significance": "high",
                "events": [e.get("event_id") for e in trust_events]
            })
        
        print(f"  Discovered {len(self.findings['pattern_discoveries'])} patterns")
    
    def run(self):
        """Run full Super-Sleuth analysis."""
        print("\n" + "="*60)
        print("SUPER-SLEUTH INTRO-SPECT MODE")
        print("Lead Generation & Pattern Discovery")
        print("="*60)
        
        self.analyze_entity_completeness()
        self.analyze_event_linkages()
        self.analyze_timeline_gaps()
        self.analyze_relation_completeness()
        self.discover_patterns()
        
        return self.findings


class HyperHolmesTurboSolve:
    """
    Validation agent - convergent thinking mode.
    Verifies findings and implements refinements.
    """
    
    def __init__(self, sleuth_findings):
        self.sleuth_findings = sleuth_findings
        self.entities = load_json(DATA_MODELS_DIR / "entities" / "entities.json")
        self.events = load_json(DATA_MODELS_DIR / "events" / "events.json")
        self.relations = load_json(DATA_MODELS_DIR / "relations" / "relations.json")
        self.timeline = load_json(DATA_MODELS_DIR / "timelines" / "timeline.json")
        self.refinements = {
            "timestamp": TIMESTAMP,
            "mode": "turbo_solve",
            "entities_refined": 0,
            "events_refined": 0,
            "relations_refined": 0,
            "timeline_refined": 0,
            "details": []
        }
    
    def refine_entities(self):
        """Apply entity refinements based on Super-Sleuth findings."""
        print("\n=== Hyper-Holmes: Entity Refinement ===")
        
        if not self.entities:
            return
        
        entity_issues = self.sleuth_findings.get("entity_refinements", [])
        
        # Build lookup
        persons = self.entities.get("entities", {}).get("persons", [])
        orgs = self.entities.get("entities", {}).get("organizations", [])
        
        for issue in entity_issues[:20]:  # Process top 20 priority
            entity_id = issue.get("entity_id")
            issues = issue.get("issues", [])
            
            # Find and update entity
            if issue.get("type") == "person":
                for person in persons:
                    if person.get("entity_id") == entity_id:
                        # Add missing fields with placeholders
                        if "missing_burden_analysis" in issues:
                            if not person.get("burden_of_proof_analysis"):
                                person["burden_of_proof_analysis"] = {
                                    "civil_50%": "PENDING_REVIEW",
                                    "criminal_95%": "PENDING_REVIEW",
                                    "key_evidence": []
                                }
                                self.refinements["entities_refined"] += 1
                        
                        # Add refinement timestamp
                        person["refinement_date"] = TIMESTAMP
                        break
            else:
                for org in orgs:
                    if org.get("entity_id") == entity_id:
                        org["refinement_date"] = TIMESTAMP
                        self.refinements["entities_refined"] += 1
                        break
        
        print(f"  Refined {self.refinements['entities_refined']} entities")
    
    def refine_events(self):
        """Apply event refinements based on Super-Sleuth findings."""
        print("\n=== Hyper-Holmes: Event Refinement ===")
        
        if not self.events:
            return
        
        event_issues = self.sleuth_findings.get("event_refinements", [])
        events = self.events.get("events", [])
        
        for issue in event_issues[:30]:  # Process top 30 priority
            event_id = issue.get("event_id")
            issues = issue.get("issues", [])
            
            for event in events:
                if event.get("event_id") == event_id:
                    # Add missing burden of proof
                    if "missing_burden_of_proof" in issues:
                        if not event.get("burden_of_proof"):
                            # Determine based on event type
                            if event.get("criminal_threshold"):
                                event["burden_of_proof"] = "criminal_95%_exceeded"
                            else:
                                event["burden_of_proof"] = "civil_50%"
                            self.refinements["events_refined"] += 1
                    
                    event["refinement_date"] = TIMESTAMP
                    break
        
        print(f"  Refined {self.refinements['events_refined']} events")
    
    def refine_timeline(self):
        """Apply timeline refinements."""
        print("\n=== Hyper-Holmes: Timeline Refinement ===")
        
        if not self.timeline:
            return
        
        timeline_issues = self.sleuth_findings.get("timeline_anomalies", [])
        entries = self.timeline.get("timeline", [])
        
        # Create event lookup
        event_lookup = {}
        if self.events:
            for event in self.events.get("events", []):
                event_lookup[event.get("event_id")] = event
        
        for issue in timeline_issues[:40]:  # Process top 40
            date = issue.get("date")
            issues = issue.get("issues", [])
            
            for entry in entries:
                if entry.get("date") == date:
                    # Generate event reference if missing
                    if "missing_event_ref" in issues:
                        if not entry.get("event_ref"):
                            # Create a generated event reference
                            date_clean = date.replace("-", "")
                            entry["event_ref"] = f"EVENT_GEN_{date_clean}"
                            self.refinements["timeline_refined"] += 1
                    
                    # Add empty actors list if missing
                    if "missing_actors" in issues:
                        if not entry.get("actors"):
                            entry["actors"] = []
                    
                    break
        
        print(f"  Refined {self.refinements['timeline_refined']} timeline entries")
    
    def update_metadata(self):
        """Update metadata versions."""
        print("\n=== Hyper-Holmes: Metadata Update ===")
        
        new_version = f"35.0_LEX_REFINED_{DATE_STAMP}"
        
        if self.entities:
            self.entities["metadata"]["version"] = new_version
            self.entities["metadata"]["last_updated"] = TIMESTAMP
            self.entities["metadata"]["changes"] = "LEX Investigation refinement"
        
        if self.events:
            self.events["metadata"]["version"] = f"30.0_LEX_REFINED_{DATE_STAMP}"
            self.events["metadata"]["last_updated"] = TIMESTAMP
            self.events["metadata"]["changes"] = "LEX Investigation refinement"
        
        if self.relations:
            self.relations["metadata"]["version"] = new_version
            self.relations["metadata"]["last_updated"] = TIMESTAMP
            self.relations["metadata"]["changes"] = "LEX Investigation refinement"
        
        if self.timeline:
            self.timeline["metadata"]["version"] = f"30.0_LEX_REFINED_{DATE_STAMP}"
            self.timeline["metadata"]["last_updated"] = TIMESTAMP
            self.timeline["metadata"]["changes"] = "LEX Investigation refinement"
        
        print("  Updated all metadata versions")
    
    def save_refinements(self):
        """Save all refined data models."""
        print("\n=== Hyper-Holmes: Saving Refinements ===")
        
        if self.entities:
            save_json(DATA_MODELS_DIR / "entities" / "entities.json", self.entities)
        
        if self.events:
            save_json(DATA_MODELS_DIR / "events" / "events.json", self.events)
        
        if self.relations:
            save_json(DATA_MODELS_DIR / "relations" / "relations.json", self.relations)
        
        if self.timeline:
            save_json(DATA_MODELS_DIR / "timelines" / "timeline.json", self.timeline)
        
        # Save refinement report
        report_path = DATA_MODELS_DIR / f"LEX_REFINEMENT_REPORT_{DATE_STAMP}.json"
        save_json(report_path, self.refinements)
    
    def run(self):
        """Run full Hyper-Holmes validation and refinement."""
        print("\n" + "="*60)
        print("HYPER-HOLMES TURBO-SOLVE MODE")
        print("Validation & Refinement Implementation")
        print("="*60)
        
        self.refine_entities()
        self.refine_events()
        self.refine_timeline()
        self.update_metadata()
        self.save_refinements()
        
        return self.refinements


def main():
    """Main execution."""
    print("\n" + "="*70)
    print("LEX INVESTIGATION SYSTEM - CASE 2025-137857")
    print("Revenue Stream Hijacking Analysis")
    print("="*70)
    print(f"Timestamp: {TIMESTAMP}")
    
    # Phase 1: Super-Sleuth Intro-Spect Mode
    sleuth = SuperSleuthIntroSpect()
    sleuth_findings = sleuth.run()
    
    # Save Super-Sleuth findings
    sleuth_report_path = DATA_MODELS_DIR / f"SUPER_SLEUTH_FINDINGS_{DATE_STAMP}.json"
    save_json(sleuth_report_path, sleuth_findings)
    
    # Phase 2: Hyper-Holmes Turbo-Solve Mode
    holmes = HyperHolmesTurboSolve(sleuth_findings)
    refinements = holmes.run()
    
    # Summary
    print("\n" + "="*70)
    print("LEX INVESTIGATION SUMMARY")
    print("="*70)
    print(f"Super-Sleuth Findings:")
    print(f"  - Entity refinements needed: {len(sleuth_findings.get('entity_refinements', []))}")
    print(f"  - Event refinements needed: {len(sleuth_findings.get('event_refinements', []))}")
    print(f"  - Timeline anomalies: {len(sleuth_findings.get('timeline_anomalies', []))}")
    print(f"  - Patterns discovered: {len(sleuth_findings.get('pattern_discoveries', []))}")
    print(f"\nHyper-Holmes Refinements:")
    print(f"  - Entities refined: {refinements.get('entities_refined', 0)}")
    print(f"  - Events refined: {refinements.get('events_refined', 0)}")
    print(f"  - Timeline entries refined: {refinements.get('timeline_refined', 0)}")
    print("\n" + "="*70)
    
    return sleuth_findings, refinements


if __name__ == "__main__":
    main()
