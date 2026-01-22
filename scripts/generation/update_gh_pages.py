#!/usr/bin/env python3
"""
Update GitHub Pages documentation based on refined data models.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DOCS_ROOT = REVSTREAM_ROOT / "docs"
DATA_MODELS_ROOT = DOCS_ROOT / "data_models"
ENTITIES_DOCS_PATH = DOCS_ROOT / "entities"
EVENTS_DOCS_PATH = DOCS_ROOT / "events"
FILINGS_DOCS_PATH = DOCS_ROOT / "filings"

# Data model files
ENTITIES_FILE = DATA_MODELS_ROOT / "entities" / "entities.json"
RELATIONS_FILE = DATA_MODELS_ROOT / "relations.json"
EVENTS_FILE = DATA_MODELS_ROOT / "events.json"
TIMELINE_FILE = DATA_MODELS_ROOT / "timeline.json"
INDEX_FILE = DOCS_ROOT / "index.md"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_model_versions():
    """Get the latest versions of the data models"""
    versions = {}
    versions["entities"] = load_json(ENTITIES_FILE)["metadata"]["version"].split('_')[0]
    versions["relations"] = load_json(RELATIONS_FILE)["metadata"]["version"].split('_')[0]
    versions["events"] = load_json(EVENTS_FILE)["metadata"]["version"].split('_')[0]
    versions["timeline"] = load_json(TIMELINE_FILE)["metadata"]["version"].split('_')[0]
    return versions

def update_index_md():
    """Update the main index.md file"""
    print("Updating index.md...")
    with open(INDEX_FILE, 'r') as f:
        content = f.read()

    versions = get_model_versions()
    
    # Update data model versions
    content = content.replace(
        "Entities v27.0, Relations v22.0, Events v25.0, Timeline v23.0",
        f"Entities v{versions['entities']}, Relations v{versions['relations']}, Events v{versions['events']}, Timeline v{versions['timeline']}"
    )

    # Add new update log
    update_log = f"""**{datetime.now().strftime('%Y-%m-%d')}:**
- Refined all data models with comprehensive evidence from ad-res-j7.
- Enhanced 14 entities, 25 relations, 27 events, and 56 timeline entries.
- Upgraded Kayla Pretorius to conclusive evidence status.
- Updated data models to v{versions['entities']} (entities), v{versions['relations']} (relations), v{versions['events']} (events), v{versions['timeline']} (timeline)
"""
    content = content.replace("## Recent Updates", f"## Recent Updates\n\n{update_log}")
    
    # Update legal filing links
    today_str = datetime.now().strftime("%Y_%m_%d")
    content = content.replace("CIPC_COMPLAINT_REFINED_2026_01_09.md", f"CIPC_COMPLAINT_REFINED_{today_str}.md")
    content = content.replace("POPIA_COMPLAINT_REFINED_2026_01_09.md", f"POPIA_COMPLAINT_REFINED_{today_str}.md")
    content = content.replace("NPA_TAX_FRAUD_REPORT_REFINED_2026_01_09.md", f"NPA_TAX_FRAUD_REPORT_REFINED_{today_str}.md")

    with open(INDEX_FILE, 'w') as f:
        f.write(content)
    print("✓ index.md updated.")

def generate_entity_docs():
    """Generate markdown files for each entity"""
    print("Generating entity documentation...")
    ENTITIES_DOCS_PATH.mkdir(exist_ok=True)
    entities = load_json(ENTITIES_FILE)
    
    for person in entities["entities"]["persons"]:
        entity_id = person["entity_id"]
        with open(ENTITIES_DOCS_PATH / f"{entity_id}.md", 'w') as f:
            f.write(f"# {person['name']}\n\n")
            f.write(f"**ID:** {entity_id}\n")
            f.write(f"**Role:** {person.get('role', 'N/A')}\n")
            f.write(f"**Evidence Strength:** {person.get('evidence_strength', 'N/A')}\n\n")
            f.write("## Evidence\n")
            for ev in person.get('evidence', []):
                f.write(f"- {ev}\n")
            f.write("\n## Ad-Res-J7 References\n")
            for ref in person.get('ad_res_j7_references', []):
                f.write(f"- {ref}\n")

    for org in entities["entities"]["organizations"]:
        entity_id = org["entity_id"]
        with open(ENTITIES_DOCS_PATH / f"{entity_id}.md", 'w') as f:
            f.write(f"# {org['name']}\n\n")
            f.write(f"**ID:** {entity_id}\n")
            f.write(f"**Role:** {org.get('role', 'N/A')}\n")
            f.write(f"**Evidence Strength:** {org.get('evidence_strength', 'N/A')}\n\n")
            f.write("## Evidence\n")
            for ev in org.get('evidence', []):
                f.write(f"- {ev}\n")
            f.write("\n## Ad-Res-J7 References\n")
            for ref in org.get('ad_res_j7_references', []):
                f.write(f"- {ref}\n")
    print(f"✓ {len(entities['entities']['persons']) + len(entities['entities']['organizations'])} entity documents generated.")


def generate_event_docs():
    """Generate markdown files for each event"""
    print("Generating event documentation...")
    EVENTS_DOCS_PATH.mkdir(exist_ok=True)
    events = load_json(EVENTS_FILE)
    
    for event in events["events"]:
        event_id = event["event_id"]
        with open(EVENTS_DOCS_PATH / f"{event_id}.md", 'w') as f:
            f.write(f"# {event.get('title', event_id)}\n\n")
            f.write(f"**ID:** {event_id}\n")
            f.write(f"**Date:** {event.get('date', 'N/A')}\n")
            f.write(f"**Burden of Proof:** {event.get('burden_of_proof', 'N/A')}\n\n")
            f.write("## Description\n")
            f.write(f"{event.get('description', 'No description available.')}\n\n")
            f.write("## Evidence\n")
            for ev in event.get('evidence', []):
                f.write(f"- {ev}\n")
    print(f"✓ {len(events['events'])} event documents generated.")


def main():
    """Main function to update all GitHub Pages documentation"""
    update_index_md()
    generate_entity_docs()
    generate_event_docs()
    print("\nGitHub Pages documentation updated successfully.")

if __name__ == "__main__":
    main()
