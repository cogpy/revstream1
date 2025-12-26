#!/usr/bin/env python3
"""
Entity Profile Index Page Generator
Creates an index page for all generated entity profiles.
"""

import os
from pathlib import Path

# Paths
DOCS_DIR = Path("/home/ubuntu/revstream1/docs")
ENTITY_PROFILES_DIR = DOCS_DIR / "entity-profiles"

# Get all generated profile pages
profile_pages = sorted(ENTITY_PROFILES_DIR.glob("*.md"))

# Generate index page content
content = "# Entity Profiles\n\n---\n\n"
content += "This section provides comprehensive profile pages for each natural and juristic person involved in the case. Each profile breaks down the entity's specific involvement, including factors, impacts, actions, events, timelines, and relationships.\n\n"

# Group by category
profiles_by_category = {
    "Natural Persons": [],
    "Juristic Persons (Organizations)": [],
    "Juristic Persons (Trusts)": [],
    "Bank Accounts": []
}

for page in profile_pages:
    filename = page.name
    entity_id = filename.split("-")[0]
    entity_name = " ".join(filename.split("-")[1:]).replace(".md", "").title()

    if entity_id.startswith("person"):
        profiles_by_category["Natural Persons"].append((entity_name, f"./{filename}"))
    elif entity_id.startswith("org"):
        profiles_by_category["Juristic Persons (Organizations)"].append((entity_name, f"./{filename}"))
    elif entity_id.startswith("trust"):
        profiles_by_category["Juristic Persons (Trusts)"].append((entity_name, f"./{filename}"))
    elif entity_id.startswith("bank"):
        profiles_by_category["Bank Accounts"].append((entity_name, f"./{filename}"))

for category, profiles in profiles_by_category.items():
    if profiles:
        content += f"## {category}\n\n"
        content += "| Entity Name | Profile Link |\n"
        content += "|-------------|--------------|\n"
        for name, link in sorted(profiles):
            content += f"| {name} | [View Profile]({link}) |\n"
        content += "\n"

# Save index page
index_filepath = ENTITY_PROFILES_DIR / "index.md"
with open(index_filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Entity profile index page created at: {index_filepath}")
