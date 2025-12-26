#!/usr/bin/env python3
"""
Refines data models (entities, events, relations, timeline) and generates updated, 
consistent documentation, including a master timeline and entity profiles.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class ModelRefiner:
    def __init__(self, revstream_path: str, ad_res_path: str):
        self.revstream_path = revstream_path
        self.ad_res_path = ad_res_path
        self.docs_path = os.path.join(self.revstream_path, "docs")
        self.data_models_path = os.path.join(self.revstream_path, "data_models")
        self.entities = {}
        self.events = []
        self.relations = {}
        self.timeline = {}

        os.makedirs(os.path.join(self.docs_path, "entities"), exist_ok=True)
        os.makedirs(os.path.join(self.docs_path, "events"), exist_ok=True)

    def load_data(self):
        """Load the latest data models from the repository."""
        print("Loading latest data models...")
        # Entities
        entities_file = os.path.join(self.data_models_path, 'entities/entities.json')
        entities_data = self._load_json(entities_file)
        if entities_data:
            persons = entities_data.get("entities", {}).get("persons", [])
            organizations = entities_data.get("entities", {}).get("organizations", [])
            self.entities = {p["entity_id"]: p for p in persons if "entity_id" in p} 
            self.entities.update({o["entity_id"]: o for o in organizations if "entity_id" in o})

        # Events
        events_file = os.path.join(self.data_models_path, 'events/events_refined_2025_11_28_v25.json')
        events_data = self._load_json(events_file)
        if events_data:
            self.events = sorted(events_data.get("events", []), key=lambda x: x.get("date", ""))

        # Timeline Phases
        timeline_file = os.path.join(self.data_models_path, 'timelines/timeline_enhanced.json')
        timeline_data = self._load_json(timeline_file)
        if timeline_data:
            self.timeline = {phase["phase_id"]: phase for phase in timeline_data.get("phases", []) if "phase_id" in phase}
        print("✓ Data loading complete.")

    def _load_json(self, filepath: str) -> Dict[str, Any]:
        """Helper to load a single JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Could not load {filepath}: {e}")
            return {}

    def generate_entity_profiles(self):
        """Generate individual Markdown files for each entity."""
        print("Generating entity profiles...")
        if not self.entities:
            print("No entities to process.")
            return

        for entity_id, entity_data in self.entities.items():
            name = entity_data.get("name", "Unknown Entity")
            profile_path = os.path.join(self.docs_path, f"entities/{entity_id}.md")
            with open(profile_path, 'w', encoding='utf-8') as f:
                f.write(f"# {name}\n\n")
                f.write(f"**Entity ID:** `{entity_id}`\n\n")
                
                for key, value in entity_data.items():
                    if key not in ["name", "entity_id"]:
                        f.write(f"- **{key.replace('_', ' ').title()}:** {self._format_value(value)}\n")
                
                f.write("\n## Related Events\n\n")
                related_events = [e for e in self.events if entity_id in e.get("entities_involved", [])]
                if related_events:
                    for event in related_events:
                        event_title = event.get('title', 'Untitled Event')
                        event_id_str = event.get('event_id', 'no-id')
                        event_date = event.get('date', 'N/A')
                        f.write(f"- **{event_date}**: [{event_title}](../events/{event_id_str}.md)\n")
                else:
                    f.write("No direct events found for this entity.\n")
        print(f"✓ {len(self.entities)} entity profiles generated.")

    def generate_event_pages(self):
        """Generate individual Markdown files for each event."""
        print("Generating event pages...")
        if not self.events:
            print("No events to process.")
            return

        for event in self.events:
            event_id = event.get("event_id", "no-id")
            title = event.get("title", "Unknown Event")
            page_path = os.path.join(self.docs_path, f"events/{event_id}.md")
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**Event ID:** `{event_id}`\n")
                f.write(f"**Date:** {event.get('date', 'N/A')}\n\n")

                for key, value in event.items():
                    if key not in ["title", "event_id", "date"]:
                         f.write(f"- **{key.replace('_', ' ').title()}:** {self._format_value(value)}\n")
        print(f"✓ {len(self.events)} event pages generated.")

    def generate_master_timeline(self):
        """Generate a single, comprehensive timeline.md file from the events data."""
        print("Generating master timeline...")
        timeline_path = os.path.join(self.docs_path, "timeline.md")
        events_by_phase = {}
        for event in self.events:
            phase_id = event.get("timeline_phase", "UNKNOWN")
            if phase_id not in events_by_phase:
                events_by_phase[phase_id] = []
            events_by_phase[phase_id].append(event)

        with open(timeline_path, 'w', encoding='utf-8') as f:
            f.write("# Master Timeline of Events\n\n")
            f.write("This timeline is automatically generated from the refined data models.\n\n")

            sorted_phases = sorted(events_by_phase.keys(), key=lambda p: self.timeline.get(p, {}).get("start_date", ""))

            for phase_id in sorted_phases:
                phase_info = self.timeline.get(phase_id, {"name": f"Phase {phase_id}"})
                f.write(f"## {phase_info.get('name', f'Phase {phase_id}')}\n\n")
                if phase_info.get("description"):
                    f.write(f"{phase_info['description']}\n\n")
                
                for event in sorted(events_by_phase[phase_id], key=lambda x: x.get("date", "")):
                    event_title = event.get('title', 'Untitled Event')
                    event_id_str = event.get('event_id', 'no-id')
                    event_date = event.get('date', 'N/A')
                    f.write(f"### {event_date} - {event_title}\n\n")
                    f.write(f"- **Event ID:** `__{event_id_str}__`\n")
                    f.write(f"- **Category:** {event.get('category', 'N/A')}\n")
                    f.write(f"- **Description:** {event.get('description', 'N/A')}\n")
                    evidence_files = event.get("evidence_files", [])
                    if evidence_files:
                        f.write("- **Evidence:**\n")
                        for ev in evidence_files[:3]: # Limit to 3 for brevity
                            f.write(f"  - `{ev}`\n")
                    f.write(f"- **[View Full Event Details](events/{event_id_str}.md)**\n\n")
        print("✓ Master timeline generated.")

    def _format_value(self, value):
        if isinstance(value, list):
            return "\n  - " + "\n  - ".join(map(str, value))
        return value

    def run_refinement(self):
        self.load_data()
        self.generate_entity_profiles()
        self.generate_event_pages()
        self.generate_master_timeline()
        print("\nRefinement and documentation generation complete.")

if __name__ == "__main__":
    refiner = ModelRefiner(
        revstream_path="/home/ubuntu/revstream1",
        ad_res_path="/home/ubuntu/ad-res-j7"
    )
    refiner.run_refinement()
