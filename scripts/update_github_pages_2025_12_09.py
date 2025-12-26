#!/usr/bin/env python3
"""
Update GitHub Pages Script for Revenue Stream Hijacking Case
Date: 2025-12-09
Purpose: Update GitHub Pages with new evidence, entity relationship diagrams, and an updated timeline.
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DOCS_DIR = BASE_DIR / "docs"
DATA_MODELS_DIR = BASE_DIR / "data_models"
RELATIONS_FILE = DATA_MODELS_DIR / "relations/relations_refined_2025_12_09_v23.json"
TIMELINE_FILE = DATA_MODELS_DIR / "timelines/timeline_refined_2025_12_09_v22.json"
INDEX_MD = DOCS_DIR / "index.md"
EVIDENCE_INDEX_MD = DOCS_DIR / "evidence-index-enhanced.md"
TIMELINE_HTML = DOCS_DIR / "timeline.html"

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_mermaid_diagram(relations_data):
    """Generate a Mermaid diagram for entity relationships"""
    print("Generating Mermaid diagram for entity relationships...")
    mermaid_string = "graph TD;\n"
    mermaid_string += "    subgraph \"Ownership Relations\"\n"
    for rel in relations_data["relations"]["ownership_relations"]:
        source = rel.get("source_entity", rel.get("from_entity", ""))
        target = rel.get("target_entity", rel.get("to_entity", ""))
        mermaid_string += f"        {source}[{source}] -->|{rel['relation_type']}| {target}[{target}];\n"
    mermaid_string += "    end\n"

    mermaid_string += "    subgraph \"Control Relations\"\n"
    for rel in relations_data["relations"]["control_relations"]:
        source = rel.get("source_entity", "")
        target = rel.get("target_entity", "")
        mermaid_string += f"        {source}[{source}] -->|{rel.get('control_type', rel.get('relation_type'))}| {target}[{target}];\n"
    mermaid_string += "    end\n"

    mermaid_string += "    subgraph \"Conspiracy Relations\"\n"
    for rel in relations_data["relations"]["conspiracy_relations"]:
        source = rel.get("source_entity", "")
        target = rel.get("target_entity", "")
        mermaid_string += f"        {source}[{source}] ---|co-conspirators| {target}[{target}];\n"
    mermaid_string += "    end\n"

    # Add a new subgraph for the access relations
    if "access_relations" in relations_data["relations"]:
        mermaid_string += "    subgraph \"Access & Impersonation Relations\"\n"
        for rel in relations_data["relations"]["access_relations"]:
            source = rel.get("source_entity", "")
            target = rel.get("target_entity", "")
            mermaid_string += f"        {source}[{source}] -->|{rel['relation_type']}| {target}[{target}];\n"
        mermaid_string += "    end\n"

    return mermaid_string

def update_evidence_index():
    """Update the evidence index with new annexures"""
    print("Updating evidence index...")
    with open(EVIDENCE_INDEX_MD, "r+") as f:
        content = f.read()
        if "SF9" not in content:
            print("  - Adding SF9, SF10, SF2A, SF2B, SF1A to evidence index...")
            new_annexures = """\n| **SF1A** | Bantjies Call Option Agreement Excerpt | MEDIUM | 181 KB |
| **SF2A** | Sage User Access - Rynette Dual Accounts (June 2025) | **CRITICAL** | 53 KB |
| **SF2B** | Sage Subscription Expiry - Rynette Owner (August 2025) | **CRITICAL** | 51 KB |
| **SF9** | Attorney Letter to KEIRO re Payment (October 2025) | MEDIUM | 1.4 MB |
| **SF10** | Sales Workflow Presentation | MEDIUM | - |\n"""
            # Find the table and add the new rows
            table_end = content.find("| SF8 | Linda Employment Records | MEDIUM | - |")
            if table_end != -1:
                insert_position = content.find("\n", table_end) + 1
                content = content[:insert_position] + new_annexures + content[insert_position:]
                f.seek(0)
                f.write(content)
                f.truncate()
                print("  ✓ Evidence index updated successfully.")
        else:
            print("  ✓ Evidence index already contains new annexures.")

def update_main_index(mermaid_diagram):
    """Update the main index.md with new evidence and the diagram"""
    print("Updating main index page...")
    with open(INDEX_MD, "r+") as f:
        content = f.read()
        # Update timestamp
        content = content.replace(content.split("**Last Updated:**")[1].split("\n")[0], f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Add mermaid diagram
        if "## Entity Relationship Diagram" not in content:
            print("  - Adding entity relationship diagram...")
            diagram_section = f"""\n---\n\n##  Entity Relationship Diagram\n\n```mermaid\n{mermaid_diagram}```\n"""
            content += diagram_section

        f.seek(0)
        f.write(content)
        f.truncate()
        print("  ✓ Main index page updated successfully.")

def generate_timeline_html(timeline_data):
    """Generate an HTML timeline from the timeline data"""
    print("Generating HTML timeline...")
    html = """<!DOCTYPE html>
<html>
<head>
<title>Case Timeline</title>
<style>
body { font-family: sans-serif; }
.timeline { position: relative; max-width: 1200px; margin: 0 auto; }
.timeline::after { content: ''; position: absolute; width: 6px; background-color: #939393; top: 0; bottom: 0; left: 50%; margin-left: -3px; }
.container { padding: 10px 40px; position: relative; background-color: inherit; width: 50%; }
.left { left: 0; }
.right { left: 50%; }
.left::before, .right::before { content: \" \"; height: 0; position: absolute; top: 22px; width: 0; z-index: 1; border: medium solid white; border-width: 10px 0 10px 10px; border-color: transparent transparent transparent white; }
.right::before { border-width: 10px 10px 10px 0; border-color: transparent white transparent transparent; left: 60px; }
.left::before { right: 60px; }
.right::after, .left::after { content: ''; position: absolute; width: 25px; height: 25px; right: -17px; background-color: white; border: 4px solid #FF9F55; top: 15px; border-radius: 50%; z-index: 1; }
.right::after { left: -16px; }
.content { padding: 20px 30px; background-color: #f2f2f2; position: relative; border-radius: 6px; }
</style>
</head>
<body>
<div class=\"timeline\">"""

    for i, entry in enumerate(timeline_data["timeline"]):
        side = "left" if i % 2 == 0 else "right"
        html += f"""<div class=\"container {side}\">
    <div class=\"content\">
        <h2>{entry['date']}</h2>
        <h3>{entry['title']}</h3>
        <p>{entry['description']}</p>
        <p><b>Category:</b> {entry['category']}<br>
        <b>Significance:</b> {entry['significance']}<br>
        <b>Evidence:</b> {', '.join(entry['evidence'])}</p>
    </div>
</div>"""

    html += """</div>
</body>
</html>"""

    with open(TIMELINE_HTML, "w") as f:
        f.write(html)
    print("  ✓ HTML timeline generated successfully.")

def main():
    """Main execution function"""
    print("="*80)
    print("UPDATING GITHUB PAGES - Revenue Stream Hijacking Case 2025-137857")
    print("="*80)

    # Load data
    print("\nLoading data models...")
    relations = load_json(RELATIONS_FILE)
    timeline = load_json(TIMELINE_FILE)

    # Generate Mermaid diagram
    mermaid_diagram = generate_mermaid_diagram(relations)

    # Update evidence index
    update_evidence_index()

    # Update main index page
    update_main_index(mermaid_diagram)

    # Generate HTML timeline
    generate_timeline_html(timeline)

    print("\n" + "="*80)
    print("GITHUB PAGES UPDATED SUCCESSFULLY")
    print("="*80)

if __name__ == "__main__":
    main()
