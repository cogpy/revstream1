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

    # Extract file list from markdown tables
    file_list = []
    current_category = None

    for line in lines:
        # Check for category headers
        category_match = re.match(r"### (.*?) \((\d+) files\)", line)
        if category_match:
            current_category = category_match.group(1)
            continue

        # Check for file entries in tables
        if line.startswith("| `"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) > 3 and parts[1].startswith("`"):
                file_path = parts[1].strip("`")
                size = parts[2]
                evidence_codes = parts[3]
                link = f"https://github.com/cogpy/ad-res-j7/blob/main/{file_path}"
                file_list.append((current_category, file_path, size, evidence_codes, link))

    # Group files by category
    categories = {}
    for category, file_path, size, evidence_codes, link in file_list:
        if category not in categories:
            categories[category] = []
        categories[category].append((file_path, size, evidence_codes, link))

    # Generate new index
    with open(OUTPUT_PATH, "w") as f:
        f.write("---\n")
        f.write("layout: default\n")
        f.write("title: Generated Evidence Index\n")
        f.write("---\n\n")
        f.write("# Generated Evidence Index\n\n")
        f.write(f"This index provides a complete, generated catalog of all **{len(file_list)}** evidence files from the `cogpy/ad-res-j7` repository, organized by category.\n\n")

        for category, files in sorted(categories.items()):
            f.write(f"<details>\n")
            f.write(f'<summary><h3>{category.replace("_", " ").title()} ({len(files)} files)</h3></summary>\n\n')
            f.write("| File Path | Size | Evidence Codes | Direct Link |\n")
            f.write("|---|---|---|---|\n")
            for file_path, size, evidence_codes, link in files:
                f.write(f"| `{file_path}` | {size} | {evidence_codes} | [View File]({link}) |\n")
            f.write("\n</details>\n\n")

    print(f"Generated evidence index with {len(file_list)} files at: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_evidence_index()
