#!/usr/bin/env python3.11
"""
Generates Markdown documentation for entities from the comprehensive analysis file.
"""
import json
from pathlib import Path

def generate_entity_documentation():
    # Load the refined comprehensive analysis
    with open("../COMPREHENSIVE_ANALYSIS_2025_12_26.json", "r") as f:
        data = json.load(f)

    entities_data = data["entities"]["data"]["entities"]
    persons = entities_data["persons"]
    orgs = entities_data["organizations"]

    # Create output directories
    Path("../docs/entities/persons").mkdir(parents=True, exist_ok=True)
    Path("../docs/entities/organizations").mkdir(parents=True, exist_ok=True)

    # Generate documentation for persons
    for person in persons:
        entity_id = person.get("entity_id", "UNKNOWN_ID")
        name = person.get("name", "Unknown Name")
        role = person.get("role", "N/A")
        evidence_strength = person.get("evidence_strength", "N/A")
        financial_impact = person.get("financial_impact", {}).get("direct_involvement", "N/A")

        md_content = f"# {name}\n\n"
        md_content += f"**Entity ID:** {entity_id}\n"
        md_content += f"**Role:** {role}\n"
        md_content += f"**Evidence Strength:** {evidence_strength}\n"
        md_content += f"**Financial Impact:** {financial_impact}\n\n"

        md_content += "## Primary Actions\n"
        if "primary_actions" in person and person["primary_actions"]:
            for action in person["primary_actions"]:
                md_content += f"- {action}\n"
        else:
            md_content += "No primary actions listed.\n"

        md_content += "\n## Relationships\n"
        if "relationships" in person and person["relationships"]:
            for rel in person["relationships"]:
                md_content += f"- {rel}\n"
        else:
            md_content += "No relationships listed.\n"

        md_content += "\n## Evidence\n"
        if "evidence" in person and person["evidence"]:
            for ev in person["evidence"]:
                md_content += f"- {ev}\n"
        else:
            md_content += "No evidence listed.\n"

        md_content += "\n## Ad-Res-J7 References\n"
        if "ad_res_j7_references" in person and person["ad_res_j7_references"]:
            for ref in person["ad_res_j7_references"]:
                md_content += f"- `{ref}`\n"
        else:
            md_content += "No ad-res-j7 references listed.\n"

        with open(f"../docs/entities/persons/{entity_id}.md", "w") as f:
            f.write(md_content)

    # Generate documentation for organizations
    for org in orgs:
        entity_id = org.get("entity_id", "UNKNOWN_ID")
        name = org.get("name", "Unknown Name")
        role = org.get("role", "N/A")

        md_content = f"# {name}\n\n"
        md_content += f"**Entity ID:** {entity_id}\n"
        md_content += f"**Role:** {role}\n\n"

        md_content += "## Primary Actions\n"
        if "primary_actions" in org and org["primary_actions"]:
            for action in org["primary_actions"]:
                md_content += f"- {action}\n"
        else:
            md_content += "No primary actions listed.\n"

        md_content += "\n## Relationships\n"
        if "relationships" in org and org["relationships"]:
            for rel in org["relationships"]:
                md_content += f"- {rel}\n"
        else:
            md_content += "No relationships listed.\n"

        md_content += "\n## Evidence\n"
        if "evidence" in org and org["evidence"]:
            for ev in org["evidence"]:
                md_content += f"- {ev}\n"
        else:
            md_content += "No evidence listed.\n"

        md_content += "\n## Ad-Res-J7 References\n"
        if "ad_res_j7_references" in org and org["ad_res_j7_references"]:
            for ref in org["ad_res_j7_references"]:
                md_content += f"- `{ref}`\n"
        else:
            md_content += "No ad-res-j7 references listed.\n"

        with open(f"../docs/entities/organizations/{entity_id}.md", "w") as f:
            f.write(md_content)

    print("Documentation generation complete.")

if __name__ == "__main__":
    generate_entity_documentation()
