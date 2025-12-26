#!/usr/bin/env python3
"""
Update GitHub Pages with SF9 Attorney Letter Evidence (R63M Quantum)
Date: 2025-12-08
Purpose: Update GitHub Pages with the R63M quantum of damages from SF9.
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
DOCS_PATH = REVSTREAM_PATH / "docs"
ENTITY_PROFILES_PATH = DOCS_PATH / "entity-profiles"

def read_file(filepath):
    """Read a file and return its content"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def write_file(filepath, content):
    """Write content to a file"""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing {filepath}: {e}")
        return False

def update_index_page_with_sf9():
    """Update main index page with SF9 evidence"""
    index_path = DOCS_PATH / "index.md"
    
    existing_content = read_file(index_path)
    if not existing_content:
        print("Warning: Could not read index.md")
        return
    
    # Add new section for SF9
    sf9_section = """
---

## 🔴 NEW CRITICAL EVIDENCE (2025-12-08) - SF9 Attorney Letter

### R63M Revenue Hijacking Quantum Established

**Annexure:** SF9  
**Date:** 23 October 2025  
**Source:** Ian Levitt Attorneys (representing Jacqui Faucitt)  
**To:** Elliot Attorneys Inc (representing Peter Faucitt)

**What it proves:**
- ✅ **R60,251,961.60** revenue outstanding from RegimA Worldwide Distribution
- ✅ **$150,000** in platform fees outstanding
- ✅ **Total: ~R63M**
- ✅ **Source:** Emma Wallis (RegimA Zone UK)
- ✅ **Period:** July 2023 - October 2025 (27 months)
- ✅ **Formal demand** with 48-hour deadline (ignored)

**What it refutes:**
- ❌ Claims that Peter is owed money (he owes R63M)
- ❌ Claims that Daniel doesn't have independent business operations
- ❌ Claims that RWW owns the Shopify stores

**Legal Significance:**
- **Attorney-documented quantum** for all claims
- **Corroborates JF1** "Forensic Time Capsule" (Shopify ownership)
- **Establishes pattern** of financial misconduct
- **Formal demand** creates legal obligation

"""
    
    # Insert new section after the existing SF2B section
    updated_content = existing_content.replace(
        "---\n\n## 📊 Burden of Proof Analysis",
        f"{sf9_section}\n---\n\n## 📊 Burden of Proof Analysis"
    )
    
    # Update burden of proof analysis
    updated_content = re.sub(r"(Revenue Hijacking.*Exceeded)", "\g<1> | **SF9** | **STRONGLY EXCEEDED** ⬆️", updated_content)
    updated_content = re.sub(r"(Theft.*Achievable)", "\g<1> | **SF9** | **STRENGTHENED** ⬆️", updated_content)
    
    write_file(index_path, updated_content)
    print(f"✓ Updated: {index_path}")

def update_peter_profile_with_sf9():
    """Update Peter Faucitt entity profile with SF9 evidence"""
    peter_path = ENTITY_PROFILES_PATH / "person_001-peter-andrew-faucitt.md"
    
    existing_content = read_file(peter_path)
    if not existing_content:
        print("Warning: Could not read Peter Faucitt profile")
        return
    
    # Add new section for SF9
    sf9_section = """
---

## 🔴 NEW CRITICAL EVIDENCE (2025-12-08) - SF9 Attorney Letter

### R63M Liability to RegimA Zone UK

**Annexure:** SF9  
**Date:** 23 October 2025

**What it proves:**
- **R60,251,961.60** revenue outstanding from RegimA Worldwide Distribution
- **$150,000** in platform fees outstanding
- **Total: ~R63M**
- **Period:** July 2023 - October 2025 (27 months)
- **Formal demand** with 48-hour deadline (ignored)

**Legal Significance:**
- **Attorney-documented quantum** for theft and damages
- **Establishes Peter as debtor** (owes R63M), not creditor
- **Corroborates JF1** (Shopify ownership)
- **Pattern of financial misconduct**

"""
    
    # Insert new section after the header
    updated_content = existing_content.replace(
        "**Legal Scenario Mapping:** Director AB",
        f"**Legal Scenario Mapping:** Director AB\n{sf9_section}"
    )
    
    write_file(peter_path, updated_content)
    print(f"✓ Updated: {peter_path}")

def main():
    """Main execution function"""
    print("=" * 80)
    print("UPDATE GITHUB PAGES WITH SF9 EVIDENCE SCRIPT - 2025-12-08")
    print("=" * 80)
    print()

    print("Updating GitHub Pages with SF9 evidence...")
    update_index_page_with_sf9()
    update_peter_profile_with_sf9()

    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATE WITH SF9 EVIDENCE COMPLETE")
    print("=" * 80)
    print("\nUpdated pages:")
    print("✓ docs/index.md - Added SF9 highlight and updated burden of proof")
    print("✓ docs/entity-profiles/person_001-peter-andrew-faucitt.md - Added R63M liability")
    print("\nNext step: Commit and push changes to repository")

if __name__ == "__main__":
    main()
