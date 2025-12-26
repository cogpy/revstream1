#!/usr/bin/env python3

# --- CONFIG ---

# Input
AD_RES_J7_PATH = "/home/ubuntu/ad-res-j7"
COMPREHENSIVE_INDEX_PATH = f"{AD_RES_J7_PATH}/COMPREHENSIVE_EVIDENCE_INDEX.md"

# --- SCRIPT ---

def debug_parser():
    """Debug the markdown table parsing logic."""

    with open(COMPREHENSIVE_INDEX_PATH, "r") as f:
        lines = f.readlines()

    # Print candidate lines
    for i, line in enumerate(lines):
        if line.startswith("| `"):
            print(f"Line {i+1}: {line.strip()}")

if __name__ == "__main__":
    debug_parser()
