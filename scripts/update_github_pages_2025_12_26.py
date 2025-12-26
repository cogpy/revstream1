#!/usr/bin/env python3.11
"""
Updates GitHub Pages with the latest entity documentation, filings, and evidence references.
"""
import json
from pathlib import Path
from datetime import datetime

def update_github_pages():
    # Load the refined comprehensive analysis
    with open("../COMPREHENSIVE_ANALYSIS_2025_12_26.json", "r") as f:
        data = json.load(f)

    print("=" * 80)
    print("UPDATING GITHUB PAGES")
    print("=" * 80)

    # Create main index page
    index_content = "# Revenue Stream Hijacking Case - Evidence Repository\n\n"
    index_content += f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
    index_content += "## Overview\n\n"
    index_content += "This repository contains comprehensive documentation, evidence, and analysis for Case 2025-137857.\n\n"
    index_content += "## Navigation\n\n"
    index_content += "- [Entities](./entities/README.md) - All persons and organizations involved\n"
    index_content += "- [Events](./events/README.md) - Timeline of key events\n"
    index_content += "- [Evidence](./evidence/README.md) - Evidence mapping and cross-references\n"
    index_content += "- [Filings](./filings/index.md) - Legal filings and complaints\n"
    index_content += "- [Analysis](./analysis/README.md) - Burden of proof and data analysis\n\n"
    
    index_content += "## Key Statistics\n\n"
    index_content += f"- **Total Entities:** {data['entities']['total_count']}\n"
    index_content += f"- **Total Relations:** {data['relations']['total_count']}\n"
    index_content += f"- **Total Events:** {data['events']['total_count']}\n"
    index_content += f"- **Timeline Phases:** {data['timelines']['total_phases']}\n\n"
    
    index_content += "## Applications\n\n"
    index_content += "### Civil Actions\n"
    index_content += "- [Answering Affidavit](./filings/civil/ANSWERING_AFFIDAVIT_EVIDENCE_ENHANCED_20251217_UPDATED_20251226.md)\n\n"
    index_content += "### Criminal Actions\n"
    index_content += "- [POPIA Criminal Complaint](./filings/POPIA_COMPLAINT_REFINED_2025_12_24_UPDATED_20251226.md)\n\n"
    index_content += "### Regulatory Actions\n"
    index_content += "- [CIPC Companies Act Complaint](./filings/CIPC_COMPLAINT_REFINED_2025_12_24_UPDATED_20251226.md)\n"
    index_content += "- [NPA Tax Fraud Report](./filings/NPA_TAX_FRAUD_REPORT_REFINED_2025_12_24_UPDATED_20251226.md)\n\n"
    
    index_content += "## Evidence Cross-Reference\n\n"
    index_content += "All evidence is cross-referenced with the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).\n\n"
    
    with open("../docs/index.md", "w") as f:
        f.write(index_content)
    print("✓ Updated main index page")

    # Create events index
    events = data['events']['data']['events']
    events_index = "# Events Timeline\n\n"
    events_index += f"**Total Events:** {len(events)}\n\n"
    events_index += "## Event Categories\n\n"
    
    # Count events by category
    from collections import defaultdict
    categories = defaultdict(int)
    for e in events:
        categories[e.get('category', 'unknown')] += 1
    
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        events_index += f"- **{cat}:** {count} events\n"
    
    events_index += "\n## Chronological Event List\n\n"
    for e in sorted(events, key=lambda x: x.get('date', '9999-99-99')):
        events_index += f"- **{e.get('date', 'N/A')}** - {e.get('description', 'N/A')} (`{e.get('event_id', 'N/A')}`)\n"
    
    Path("../docs/events").mkdir(parents=True, exist_ok=True)
    with open("../docs/events/README.md", "w") as f:
        f.write(events_index)
    print("✓ Updated events index")

    # Create evidence index
    evidence_index = "# Evidence Index\n\n"
    evidence_index += "This section provides a comprehensive mapping of all evidence to entities, events, and filings.\n\n"
    evidence_index += "## Evidence Categories\n\n"
    evidence_index += "### Primary Evidence (JF Series)\n"
    evidence_index += "- **JF01:** Shopify Plus Email (Forensic Time Capsule)\n"
    evidence_index += "- **JF02:** Shopify Sales Reports\n"
    evidence_index += "- **JF03:** Financial Records and Analysis\n"
    evidence_index += "- **JF04:** Daniel Faucitt Personal Bank Records\n"
    evidence_index += "- **JF05-JF08:** Correspondence and Evidence Packages\n"
    evidence_index += "- **JF09:** Timeline Analysis\n"
    evidence_index += "- **JF10:** Legal Analysis\n"
    evidence_index += "- **JF11-JF13:** Supporting Documentation\n\n"
    evidence_index += "### Supplementary Evidence (SF Series)\n"
    evidence_index += "- **SF1:** Bantjies Debt Documentation\n"
    evidence_index += "- **SF2:** Sage Screenshots - Rynette Control\n"
    evidence_index += "- **SF3:** Strategic Logistics Stock Adjustment\n"
    evidence_index += "- **SF4:** SARS Audit Email\n"
    evidence_index += "- **SF5:** Adderory Company Registration\n"
    evidence_index += "- **SF6:** Kayla Pretorius Estate Documentation\n"
    evidence_index += "- **SF7:** Court Order - Kayla Email Seizure\n"
    evidence_index += "- **SF8:** Linda Employment Records\n\n"
    evidence_index += "## Cross-Reference to ad-res-j7\n\n"
    evidence_index += "All evidence files are stored in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES).\n\n"
    
    Path("../docs/evidence").mkdir(parents=True, exist_ok=True)
    with open("../docs/evidence/README.md", "w") as f:
        f.write(evidence_index)
    print("✓ Updated evidence index")

    # Create analysis index
    analysis_index = "# Analysis\n\n"
    analysis_index += "This section contains comprehensive data analysis and burden of proof assessments.\n\n"
    analysis_index += "## Documents\n\n"
    analysis_index += "- [Comprehensive Analysis](../COMPREHENSIVE_ANALYSIS_2025_12_26.json) - Full data model\n"
    analysis_index += "- [Refinement Report](../REFINEMENT_REPORT_2025_12_26.json) - Latest changes\n\n"
    
    Path("../docs/analysis").mkdir(parents=True, exist_ok=True)
    with open("../docs/analysis/README.md", "w") as f:
        f.write(analysis_index)
    print("✓ Updated analysis index")

    # Update filings index
    filings_index = "# Legal Filings Index\n\n"
    filings_index += f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
    filings_index += "## Civil Actions\n\n"
    filings_index += "- [Answering Affidavit (Latest)](./civil/ANSWERING_AFFIDAVIT_EVIDENCE_ENHANCED_20251217_UPDATED_20251226.md)\n\n"
    filings_index += "## Criminal Actions\n\n"
    filings_index += "- [POPIA Criminal Complaint (Latest)](./POPIA_COMPLAINT_REFINED_2025_12_24_UPDATED_20251226.md)\n\n"
    filings_index += "## Regulatory Actions\n\n"
    filings_index += "- [CIPC Companies Act Complaint (Latest)](./CIPC_COMPLAINT_REFINED_2025_12_24_UPDATED_20251226.md)\n"
    filings_index += "- [NPA Tax Fraud Report (Latest)](./NPA_TAX_FRAUD_REPORT_REFINED_2025_12_24_UPDATED_20251226.md)\n\n"
    
    with open("../docs/filings/index.md", "w") as f:
        f.write(filings_index)
    print("✓ Updated filings index")

    print("\n" + "=" * 80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    update_github_pages()
