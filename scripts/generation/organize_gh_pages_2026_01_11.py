#!/usr/bin/env python3.11
"""
GitHub Pages Organization Script

This script reorganizes the GitHub Pages documentation for clarity and improved navigation.

Date: 2026-01-11
"""

import json
import os
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DOCS_ROOT = REVSTREAM_ROOT / "docs"

# Data model paths
ENTITIES_FILE = REVSTREAM_ROOT / "data_models/entities/entities_enhanced_2025_12_12.json"
RELATIONS_FILE = REVSTREAM_ROOT / "data_models/relations/relations_refined_2025_12_27_v31.json"
TIMELINE_FILE = REVSTREAM_ROOT / "data_models/timelines/timeline.json"

# Load data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def create_entity_pages():
    """Create individual pages for each entity."""
    entities = load_json(ENTITIES_FILE)
    entities_dir = DOCS_ROOT / "entities"
    entities_dir.mkdir(exist_ok=True)

    all_entities = entities.get('entities', {}).get('persons', []) + entities.get('entities', {}).get('organizations', [])

    # Create index page
    with open(entities_dir / "index.md", "w") as f:
        f.write("# Entities\n\n")
        for entity in sorted(all_entities, key=lambda x: x.get('name', '')):
            entity_id = entity.get('entity_id')
            name = entity.get('name')
            f.write(f"- [{name}]({entity_id}.md)\n")

    # Create individual pages
    for entity in all_entities:
        entity_id = entity.get('entity_id')
        name = entity.get('name')
        with open(entities_dir / f"{entity_id}.md", "w") as f:
            f.write(f"# {name}\n\n")
            f.write("```json\n")
            f.write(json.dumps(entity, indent=2))
            f.write("\n```")

    print("Entity pages created.")

def create_relation_pages():
    """Create a page for relations."""
    relations = load_json(RELATIONS_FILE)
    relations_dir = DOCS_ROOT / "relations"
    relations_dir.mkdir(exist_ok=True)

    with open(relations_dir / "index.md", "w") as f:
        f.write("# Relations\n\n")
        f.write("```json\n")
        f.write(json.dumps(relations, indent=2))
        f.write("\n```")
    print("Relation page created.")

def create_timeline_page():
    """Create a page for the timeline."""
    timeline = load_json(TIMELINE_FILE)
    timeline_dir = DOCS_ROOT

    with open(timeline_dir / "timeline.md", "w") as f:
        f.write("# Timeline\n\n")
        for entry in timeline.get('timeline', [])[:50]: # Truncate for summary page
            f.write(f"## {entry.get('date')} - {entry.get('event')}\n\n")
            f.write("```json\n")
            f.write(json.dumps(entry, indent=2))
            f.write("\n```\n\n")
    print("Timeline page created.")

def main():
    print("Organizing GitHub Pages documentation...")
    create_entity_pages()
    create_relation_pages()
    create_timeline_page()
    print("GitHub Pages organization complete.")

if __name__ == "__main__":
    main()
