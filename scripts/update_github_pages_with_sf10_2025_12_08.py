#!/usr/bin/env python3
"""
Update GitHub Pages with SF10 Sales Workflow Evidence
Date: 2025-12-08
Purpose: Update GitHub Pages with the SF10 sales workflow evidence.
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

def update_index_page_with_sf10():
    """Update main index page with SF10 evidence"""
    index_path = DOCS_PATH / "index.md"
    
    existing_content = read_file(index_path)
    if not existing_content:
        print("Warning: Could not read index.md")
        return
    
    # Add new section for SF10
    sf10_section = """
---

## 🔵 NEW OPERATIONAL EVIDENCE (2025-12-08) - SF10 Sales Workflow

### Professional, Automated E-Commerce Operations Proven

**Annexure:** SF10 (PowerPoint Presentation)  
**Source:** Internal documentation

**What it proves:**
- ✅ **Sophisticated three-system integration:** Shopify ↔ Sage ↔ Courier Guy
- ✅ **Automated accounting:** Tax invoices automatically generated in Sage when orders fulfilled in Shopify
- ✅ **Professional business operations:** Refutes claims of disorganized or improper business practices
- ✅ **Critical role of Sage:** Essential for tax invoice generation and accounting
- ✅ **Impact of Sage expiry (SF2B):** Halts tax invoice generation and disrupts operations

**Key Personnel Identified:**
- **Kent:** Customer order handler (Shopify access)
- **EL (Eldridge Davids):** Customer order handler (Shopify & Sage access, per SF2A)

**Legal Significance:**
- **Refutes claims of disorganization** in oppression application
- **Corroborates Shopify operations** for revenue hijacking claims
- **Demonstrates impact of Sage obstruction** (SF2B)

"""
    
    # Insert new section after the existing SF9 section
    updated_content = existing_content.replace(
        "## 🔴 NEW CRITICAL EVIDENCE (2025-12-08) - SF9 Attorney Letter",
        f"{sf10_section}\n---\n\n## 🔴 NEW CRITICAL EVIDENCE (2025-12-08) - SF9 Attorney Letter"
    )
    
    # Update burden of proof analysis
    updated_content = re.sub(r"(Obstruction.*Strong)", "\g<1> | **SF10** | **STRENGTHENED** ⬆️", updated_content)
    
    write_file(index_path, updated_content)
    print(f"✓ Updated: {index_path}")

def create_kent_profile():
    """Create entity profile for Kent"""
    kent_path = ENTITY_PROFILES_PATH / "person_004-kent.md"
    
    content = """
# PERSON_004: Kent

**Role:** Customer Order Handler

---

## Operational Role (per SF10)

**Annexure:** SF10 (Sales Workflow PowerPoint)

**Responsibilities:**
- Receive customer orders via phone/email
- Create proforma invoices in Shopify
- Verify proof of payment
- Trigger order fulfillment in Shopify

**System Access:**
- Shopify

**Significance:**
- Key operational staff member in e-commerce workflow
- Handles customer orders and payment verification
- Critical for order processing

"""
    
    write_file(kent_path, content)
    print(f"✓ Created: {kent_path}")

def create_el_profile():
    """Create entity profile for Eldridge Davids (EL)"""
    el_path = ENTITY_PROFILES_PATH / "person_005-eldridge-davids.md"
    
    content = """
# PERSON_005: Eldridge Davids (EL)

**Role:** Customer Order Handler

---

## Operational Role (per SF10 & SF2A)

**Annexures:**
- SF10 (Sales Workflow PowerPoint)
- SF2A (Sage User Access Screenshot)

**Responsibilities:**
- Receive customer orders via phone/email
- Create proforma invoices in Shopify
- Verify proof of payment
- Trigger order fulfillment in Shopify

**System Access:**
- Shopify (per SF10)
- Sage (per SF2A)

**Significance:**
- Key operational staff member in e-commerce workflow
- Handles customer orders and payment verification
- Has access to both Shopify and Sage systems
- Corroborates SF2A evidence

"""
    
    write_file(el_path, content)
    print(f"✓ Created: {el_path}")

def main():
    """Main execution function"""
    print("=" * 80)
    print("UPDATE GITHUB PAGES WITH SF10 EVIDENCE SCRIPT - 2025-12-08")
    print("=" * 80)
    print()

    print("Updating GitHub Pages with SF10 evidence...")
    update_index_page_with_sf10()
    create_kent_profile()
    create_el_profile()

    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATE WITH SF10 EVIDENCE COMPLETE")
    print("=" * 80)
    print("\nUpdated pages:")
    print("✓ docs/index.md - Added SF10 highlight and updated burden of proof")
    print("✓ docs/entity-profiles/person_004-kent.md - Created profile")
    print("✓ docs/entity-profiles/person_005-eldridge-davids.md - Created profile")
    print("\nNext step: Commit and push changes to repository")

if __name__ == "__main__":
    main()
