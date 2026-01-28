#!/usr/bin/env python3
"""
Refine the CIPC complaint with new evidence from the Rynette Organogram.
"""

import re

# Read the CIPC complaint
with open("docs/filings/CIPC_REFINED_2026_01_28.md", "r") as f:
    content = f.read()

# Add reference to the organogram in the executive summary
summary_section = re.search(r"(## Executive Summary\n\n.*?)(---)", content, re.DOTALL)
if summary_section:
    summary_text = summary_section.group(1)
    new_summary_text = summary_text.replace(
        "The evidence demonstrates a calculated scheme to defraud",
        "The evidence, including operational documentation like the Rynette Organogram (EVENT_ORG_001), demonstrates a calculated scheme to defraud"
    )
    content = content.replace(summary_text, new_summary_text)

# Add the organogram as a key piece of evidence
evidence_section = re.search(r"(### Primary Annexures\n\n.*?)(---)", content, re.DOTALL)
if evidence_section:
    evidence_text = evidence_section.group(1)
    new_evidence_text = evidence_text.replace(
        "| JF10 | Trust documents | Trust violations |",
        "| JF10 | Trust documents | Trust violations |\n| EVENT_ORG_001 | Rynette Organogram | Documented sales process |"
    )
    content = content.replace(evidence_text, new_evidence_text)

# Add a new section about operational evidence
violations_section = re.search(r"(## 4. Companies Act Violations\n\n.*?)(---)", content, re.DOTALL)
if violations_section:
    violations_text = violations_section.group(1)
    new_section = violations_text + """\n### 4.4 Operational Process vs. Fraudulent Actions

The Rynette Organogram (EVENT_ORG_001) documents a clear and legitimate sales process. This includes:

- **Dual-personnel order processing** by Kent (PERSON_037) and EL (PERSON_038).
- **Shopify-to-Sage automation** for tax invoice generation.
- **Third-party verification** via Courier Guy (PLATFORM_002).

This documented process stands in stark contrast to the fraudulent activities, demonstrating that the perpetrators knowingly and deliberately bypassed established procedures to commit fraud. The existence of this process documentation proves that the company had a defined, legitimate workflow, making the deviations even more egregious.

"""
    content = content.replace(violations_text, new_section)

# Write the updated content to a new file
with open("docs/filings/CIPC_REFINED_2026_01_28_ORGANOGRAM.md", "w") as f:
    f.write(content)

print("CIPC complaint refined with organogram evidence.")
