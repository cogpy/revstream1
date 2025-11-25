#!/usr/bin/env python3
"""
Comprehensive Data Model Refinement and Improvement
Date: 2025-11-25
Purpose: Refine entities, relations, events, and timelines based on analysis findings
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class DataModelRefiner:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.data_models_path = self.base_path / "data_models"
        self.timestamp = datetime.now().isoformat()
        
        self.refinement_log = {
            "timestamp": self.timestamp,
            "refinements_applied": [],
            "improvements_made": [],
            "version_updates": {}
        }
    
    def load_models(self):
        """Load current data models"""
        print("Loading current data models...")
        
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
    
    def enhance_github_pages_references(self):
        """Enhance GitHub Pages references across all models"""
        print("Enhancing GitHub Pages references...")
        
        base_url = "https://cogpy.github.io/revstream1"
        
        # Update entities
        entities_data = self.entities.get("entities", {})
        for entity_type, entity_list in entities_data.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    entity_id = entity.get("entity_id", "")
                    if entity_id and not entity.get("github_pages_reference"):
                        entity["github_pages_reference"] = f"{base_url}/evidence-index-enhanced.md#{entity_id.lower()}"
        
        # Update events
        events_list = self.events.get("events", [])
        for event in events_list:
            event_id = event.get("event_id", "")
            if event_id and not event.get("github_pages_reference"):
                event["github_pages_reference"] = f"{base_url}/index.md#timeline-progression"
        
        # Update relations
        relations_data = self.relations.get("relations", {})
        for relation_type, relation_list in relations_data.items():
            if isinstance(relation_list, list):
                for relation in relation_list:
                    relation_id = relation.get("relation_id", "")
                    if relation_id and not relation.get("github_pages_reference"):
                        relation["github_pages_reference"] = f"{base_url}/NETWORK_ANALYSIS.md#{relation_id.lower()}"
        
        self.refinement_log["refinements_applied"].append({
            "refinement": "enhanced_github_pages_references",
            "description": "Added GitHub Pages references to all entities, events, and relations",
            "timestamp": self.timestamp
        })
    
    def add_evidence_urls(self):
        """Add direct evidence URLs to ad-res-j7 repository"""
        print("Adding direct evidence URLs...")
        
        base_evidence_url = "https://github.com/cogpy/ad-res-j7/blob/main"
        
        # Update entities with evidence URLs
        entities_data = self.entities.get("entities", {})
        for entity_type, entity_list in entities_data.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    evidence_files = entity.get("evidence_files", [])
                    if evidence_files and not entity.get("evidence_urls"):
                        entity["evidence_urls"] = [
                            f"{base_evidence_url}/{ef.lstrip('./')}" 
                            for ef in evidence_files[:5]  # Limit to first 5
                        ]
        
        # Update events with evidence URLs
        events_list = self.events.get("events", [])
        for event in events_list:
            evidence_files = event.get("evidence_files", [])
            if evidence_files and not event.get("evidence_urls"):
                event["evidence_urls"] = [
                    f"{base_evidence_url}/{ef.lstrip('./')}" 
                    for ef in evidence_files[:5]  # Limit to first 5
                ]
        
        self.refinement_log["refinements_applied"].append({
            "refinement": "added_evidence_urls",
            "description": "Added direct evidence URLs linking to ad-res-j7 repository",
            "timestamp": self.timestamp
        })
    
    def enhance_timeline_with_evidence_links(self):
        """Enhance timeline phases with evidence links"""
        print("Enhancing timeline with evidence links...")
        
        timeline_phases = self.timeline.get("timeline_phases", {})
        for phase_key, phase_data in timeline_phases.items():
            # Add evidence repository link if missing
            if not phase_data.get("evidence_repository"):
                phase_data["evidence_repository"] = "https://github.com/cogpy/ad-res-j7"
            
            # Add comprehensive evidence index link if missing
            if not phase_data.get("comprehensive_evidence_index"):
                phase_data["comprehensive_evidence_index"] = "https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md"
            
            # Add GitHub Pages reference if missing
            if not phase_data.get("github_pages_reference"):
                phase_data["github_pages_reference"] = "https://cogpy.github.io/revstream1/index.md#timeline-progression"
        
        self.refinement_log["refinements_applied"].append({
            "refinement": "enhanced_timeline_evidence_links",
            "description": "Added evidence repository and index links to all timeline phases",
            "timestamp": self.timestamp
        })
    
    def validate_cross_references(self):
        """Validate cross-references between models"""
        print("Validating cross-references between models...")
        
        # Build event ID index
        event_ids = set()
        for event in self.events.get("events", []):
            event_ids.add(event.get("event_id", ""))
        
        # Build entity ID index
        entity_ids = set()
        entities_data = self.entities.get("entities", {})
        for entity_type, entity_list in entities_data.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    entity_ids.add(entity.get("entity_id", ""))
        
        # Validate entity timeline_events references
        invalid_event_refs = []
        for entity_type, entity_list in entities_data.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    entity_id = entity.get("entity_id", "")
                    timeline_events = entity.get("timeline_events", [])
                    for event_id in timeline_events:
                        if event_id not in event_ids:
                            invalid_event_refs.append({
                                "entity_id": entity_id,
                                "invalid_event_id": event_id
                            })
        
        # Validate relation entity references
        invalid_entity_refs = []
        relations_data = self.relations.get("relations", {})
        for relation_type, relation_list in relations_data.items():
            if isinstance(relation_list, list):
                for relation in relation_list:
                    relation_id = relation.get("relation_id", "")
                    source = relation.get("source_entity", "")
                    target = relation.get("target_entity", "")
                    
                    if source and source not in entity_ids:
                        invalid_entity_refs.append({
                            "relation_id": relation_id,
                            "invalid_entity_id": source,
                            "type": "source"
                        })
                    if target and target not in entity_ids:
                        invalid_entity_refs.append({
                            "relation_id": relation_id,
                            "invalid_entity_id": target,
                            "type": "target"
                        })
        
        self.refinement_log["improvements_made"].append({
            "improvement": "cross_reference_validation",
            "invalid_event_references": len(invalid_event_refs),
            "invalid_entity_references": len(invalid_entity_refs),
            "details": {
                "invalid_event_refs": invalid_event_refs[:10],
                "invalid_entity_refs": invalid_entity_refs[:10]
            }
        })
    
    def update_metadata(self):
        """Update metadata in all models"""
        print("Updating metadata...")
        
        # Update entities metadata
        self.entities["metadata"]["last_updated"] = self.timestamp
        self.entities["metadata"]["version"] = "18.0"
        self.entities["metadata"]["changes"] = "Refinement 2025-11-25: Enhanced GitHub Pages references, added direct evidence URLs, validated cross-references"
        
        # Update events metadata
        self.events["metadata"]["last_updated"] = self.timestamp
        self.events["metadata"]["version"] = "19.0"
        self.events["metadata"]["changes"] = "Refinement 2025-11-25: Enhanced GitHub Pages references, added direct evidence URLs, validated cross-references"
        
        # Update relations metadata
        self.relations["metadata"]["last_updated"] = self.timestamp
        self.relations["metadata"]["version"] = "15.0"
        self.relations["metadata"]["changes"] = "Refinement 2025-11-25: Enhanced GitHub Pages references, validated entity references"
        
        # Update timeline metadata
        self.timeline["metadata"]["last_updated"] = self.timestamp
        self.timeline["metadata"]["version"] = "16.0"
        self.timeline["metadata"]["changes"] = "Refinement 2025-11-25: Enhanced evidence links, added comprehensive evidence index references"
        
        self.refinement_log["version_updates"] = {
            "entities": "18.0",
            "events": "19.0",
            "relations": "15.0",
            "timeline": "16.0"
        }
    
    def save_refined_models(self):
        """Save refined models to new version files"""
        print("Saving refined models...")
        
        # Save entities
        entities_file = self.data_models_path / "entities" / "entities_refined_2025_11_25_v11.json"
        with open(entities_file, 'w') as f:
            json.dump(self.entities, f, indent=2)
        print(f"Saved: {entities_file}")
        
        # Save events
        events_file = self.data_models_path / "events" / "events_refined_2025_11_25_v12.json"
        with open(events_file, 'w') as f:
            json.dump(self.events, f, indent=2)
        print(f"Saved: {events_file}")
        
        # Save relations
        relations_file = self.data_models_path / "relations" / "relations_refined_2025_11_25_v9.json"
        with open(relations_file, 'w') as f:
            json.dump(self.relations, f, indent=2)
        print(f"Saved: {relations_file}")
        
        # Save timeline
        timeline_file = self.data_models_path / "timelines" / "timeline_refined_2025_11_25_v10.json"
        with open(timeline_file, 'w') as f:
            json.dump(self.timeline, f, indent=2)
        print(f"Saved: {timeline_file}")
    
    def save_refinement_log(self):
        """Save refinement log"""
        log_file = self.base_path / "REFINEMENT_LOG_2025_11_25.json"
        with open(log_file, 'w') as f:
            json.dump(self.refinement_log, f, indent=2)
        print(f"\nRefinement log saved to: {log_file}")
        
        # Create markdown summary
        self.create_markdown_summary()
    
    def create_markdown_summary(self):
        """Create markdown summary of refinements"""
        md_content = f"""# Data Model Refinement Summary
**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Refinement Version:** 2025-11-25

## Version Updates

- **Entities:** v17.0 → v18.0
- **Events:** v18.0 → v19.0
- **Relations:** v14.0 → v15.0
- **Timeline:** v15.0 → v16.0

## Refinements Applied

"""
        for refinement in self.refinement_log["refinements_applied"]:
            md_content += f"\n### {refinement['refinement']}\n"
            md_content += f"{refinement['description']}\n\n"
        
        md_content += "\n## Improvements Made\n\n"
        for improvement in self.refinement_log["improvements_made"]:
            md_content += f"\n### {improvement['improvement']}\n"
            for key, value in improvement.items():
                if key != "improvement":
                    md_content += f"- **{key}:** {value}\n"
        
        md_content += f"""

## Files Updated

- `data_models/entities/entities_refined_2025_11_25_v11.json`
- `data_models/events/events_refined_2025_11_25_v12.json`
- `data_models/relations/relations_refined_2025_11_25_v9.json`
- `data_models/timelines/timeline_refined_2025_11_25_v10.json`

## Next Steps

1. Update GitHub Pages index.md to reference new model versions
2. Regenerate application-specific evidence pages
3. Create interactive timeline visualization
4. Validate all evidence file paths in ad-res-j7
5. Generate evidence summary pages for each application

---

**Refinement Complete:** {self.timestamp}
"""
        
        md_file = self.base_path / "REFINEMENT_SUMMARY_2025_11_25.md"
        with open(md_file, 'w') as f:
            f.write(md_content)
        print(f"Markdown summary saved to: {md_file}")
    
    def run_refinement(self):
        """Run complete refinement process"""
        print("Starting comprehensive data model refinement...")
        self.load_models()
        self.enhance_github_pages_references()
        self.add_evidence_urls()
        self.enhance_timeline_with_evidence_links()
        self.validate_cross_references()
        self.update_metadata()
        self.save_refined_models()
        self.save_refinement_log()
        print("\nRefinement complete!")

if __name__ == "__main__":
    refiner = DataModelRefiner("/home/ubuntu/revstream1")
    refiner.run_refinement()
