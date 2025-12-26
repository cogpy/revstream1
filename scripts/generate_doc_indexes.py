#!/usr/bin/env python3.11
"""
Generates index files for the entity documentation.
"""
import json
from pathlib import Path

def generate_doc_indexes():
    # Load the refined comprehensive analysis
    with open("../COMPREHENSIVE_ANALYSIS_2025_12_26.json", "r") as f:
        data = json.load(f)

    entities_data = data["entities"]["data"]["entities"]
    persons = sorted(entities_data["persons"], key=lambda x: x.get("name", ""))
    orgs = sorted(entities_data["organizations"], key=lambda x: x.get("name", ""))

    # Main entities index
    main_index = "# Entities Index\n\n"
    main_index += "This section provides a comprehensive overview of all entities involved in the case.\n\n"
    main_index += "## Persons\n\n"
    main_index += "| ID | Name | Role |\n"
    main_index += "|---|---|---|\n"
    for p in persons:
        main_index += f"| `{p['entity_id']}` | [{p['name']}](./persons/{p['entity_id']}.md) | {p['role']} |\n"
    
    main_index += "\n## Organizations\n\n"
    main_index += "| ID | Name | Role |\n"
    main_index += "|---|---|---|\n"
    for o in orgs:
        main_index += f"| `{o['entity_id']}` | [{o['name']}](./organizations/{o['entity_id']}.md) | {o['role']} |\n"

    with open("../docs/entities/README.md", "w") as f:
        f.write(main_index)

    # Persons index
    persons_index = "# Persons Index\n\n"
    for p in persons:
        persons_index += f"- [{p['name']}](./{p['entity_id']}.md)\n"
    with open("../docs/entities/persons/README.md", "w") as f:
        f.write(persons_index)

    # Organizations index
    orgs_index = "# Organizations Index\n\n"
    for o in orgs:
        orgs_index += f"- [{o['name']}](./{o['entity_id']}.md)\n"
    with open("../docs/entities/organizations/README.md", "w") as f:
        f.write(orgs_index)

    print("Documentation index generation complete.")

if __name__ == "__main__":
    generate_doc_indexes()
