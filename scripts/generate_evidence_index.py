#!/usr/bin/env python3

import re

# --- CONFIG ---

# Input
AD_RES_J7_PATH = "/home/ubuntu/ad-res-j7"
COMPREHENSIVE_INDEX_PATH = f"{AD_RES_J7_PATH}/COMPREHENSIVE_EVIDENCE_INDEX.md"

# Output
OUTPUT_PATH = "/home/ubuntu/revstream1/docs/evidence-index-generated.md"

# --- SCRIPT ---

def generate_evidence_index():
    """Generate a new evidence index from the ad-res-j7 repository."""

    with open(COMPREHENSIVE_INDEX_PATH, "r") as f:
        lines = f.readlines()

    # Extract file list from markdown table
    file_list = []
    for line in lines:
        if line.startswith("| `"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) > 2:
                file_path = parts[1].strip("`")
                size = parts[2]
                link = f"https://github.com/cogpy/ad-res-j7/blob/main/{file_path}"
                file_list.append((file_path, size, link))


    # Group files by top-level directory
    categories = {}
    for file_path, size, link in file_list:
        category = file_path.split("/")[0] if "/" in file_path else "root"
        if category not in categories:
            categories[category] = []
        categories[category].append((file_path, size, link))

    # Generate new index
    with open(OUTPUT_PATH, "w") as f:
        f.write("---\n")
        f.write("layout: default\n")
        f.write("title: Generated Evidence Index\n")
        f.write("---\n\n")
        f.write("# Generated Evidence Index\n\n")
        f.write("This index provides a complete, generated catalog of all evidence files from the `cogpy/ad-res-j7` repository, organized by category.\n\n")

        for category, files in sorted(categories.items()):
            f.write(f"<details>\n")
            f.write(f'<summary><h3>{category.replace("_", " ").title()} ({len(files)} files)</h3></summary>\n\n')
            f.write("| File Path | Size | Direct Link |\n")
            f.write("|---|---|---|\n")
            for file_path, size, link in files:
                f.write(f"| `{file_path}` | {size} | [View File]({link}) |\n")
            f.write("\n</details>\n\n")

    print(f"Generated evidence index with {len(file_list)} files at: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_evidence_index()
