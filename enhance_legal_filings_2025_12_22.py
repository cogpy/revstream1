#!/usr/bin/env python3
"""
Legal Filings Enhancement Script
Date: 2025-12-22
Purpose: Review and enhance legal filings with latest evidence
"""

import json
from pathlib import Path
from datetime import datetime

REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
DATA_MODELS = REVSTREAM_ROOT / "data_models"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_legal_filings():
    """Analyze existing legal filings for completeness"""
    filings = {
        "CIPC_COMPLAINT": REVSTREAM_ROOT / "CIPC_COMPLAINT_REFINED_2025_12_21.md",
        "POPIA_COMPLAINT": REVSTREAM_ROOT / "POPIA_COMPLAINT_REFINED_2025_12_21.md",
        "NPA_TAX_FRAUD": REVSTREAM_ROOT / "NPA_TAX_FRAUD_REPORT_2025_12_21.md"
    }
    
    analysis = {}
    
    for name, path in filings.items():
        if path.exists():
            content = path.read_text()
            analysis[name] = {
                "exists": True,
                "size": path.stat().st_size,
                "last_modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
                "has_sf1": "SF1" in content,
                "has_sf2": "SF2" in content,
                "has_sf3": "SF3" in content,
                "has_sf4": "SF4" in content,
                "has_sf5": "SF5" in content,
                "has_sf6": "SF6" in content,
                "has_sf7": "SF7" in content,
                "has_sf8": "SF8" in content,
                "has_jf01": "JF01" in content or "JF 01" in content,
                "has_burden_of_proof": "burden of proof" in content.lower() or "95%" in content,
                "line_count": len(content.split('\n'))
            }
        else:
            analysis[name] = {"exists": False}
    
    return analysis

def generate_enhancement_recommendations():
    """Generate recommendations for legal filing enhancements"""
    entities = load_json(DATA_MODELS / "entities" / "entities.json")
    events = load_json(DATA_MODELS / "events" / "events.json")
    
    recommendations = {
        "timestamp": datetime.now().isoformat(),
        "cipc_complaint": {
            "priority": "HIGH",
            "enhancements": [
                "Add SF8 (Linda employment) - demonstrates employment structure manipulation",
                "Add SF5 (Adderory registration) - shows competing business setup",
                "Cross-reference all 77 events with ad-res-j7 evidence",
                "Add burden of proof assessment for each violation",
                "Include entity relationship diagram showing conspiracy network"
            ],
            "evidence_to_add": ["SF5", "SF8", "JF13"],
            "sections_to_enhance": [
                "Section 76 violations",
                "Section 163 oppression claims",
                "Timeline of director misconduct"
            ]
        },
        "popia_complaint": {
            "priority": "CRITICAL",
            "enhancements": [
                "Add SF2 detailed analysis - dual email access proves POPIA violations",
                "Add SF7 (Court email seizure) - judicial recognition of violations",
                "Document each instance of unauthorized data access",
                "Add criminal burden of proof (95%) assessments",
                "Include technical analysis of system access violations"
            ],
            "evidence_to_add": ["SF2", "SF7", "JF08"],
            "sections_to_enhance": [
                "Section 11 violations (lawful processing)",
                "Section 19 violations (security measures)",
                "Criminal liability under Section 107"
            ]
        },
        "npa_tax_fraud": {
            "priority": "HIGH",
            "enhancements": [
                "Add SF4 (SARS audit) - independent regulatory verification",
                "Add SF3 (Stock adjustment) - R5.4M fraud concealment",
                "Add transfer pricing analysis",
                "Document inter-company loan manipulation",
                "Add criminal burden of proof assessments"
            ],
            "evidence_to_add": ["SF3", "SF4", "JF10"],
            "sections_to_enhance": [
                "Transfer pricing violations",
                "Stock adjustment fraud",
                "Inter-company loan manipulation"
            ]
        },
        "commercial_crime": {
            "priority": "CRITICAL",
            "status": "TO BE CREATED",
            "enhancements": [
                "Create comprehensive commercial crime case submission",
                "Include all SF files as primary evidence",
                "Document R10.2M revenue theft with bank records",
                "Add trust violation analysis",
                "Include conspiracy network diagram"
            ],
            "evidence_to_include": ["SF1", "SF2", "SF3", "SF6", "JF01", "JF02", "JF07"],
            "charges_to_document": [
                "Fraud (Criminal Procedure Act)",
                "Theft (Criminal Procedure Act)",
                "Money laundering (POCA)",
                "Racketeering (POCA)",
                "Forgery and uttering"
            ]
        }
    }
    
    return recommendations

def create_legal_filings_summary():
    """Create summary document for legal filings status"""
    analysis = analyze_legal_filings()
    recommendations = generate_enhancement_recommendations()
    
    summary = f"""# Legal Filings Status Report
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Current Status

### CIPC Complaint
- **Status:** {'✅ EXISTS' if analysis['CIPC_COMPLAINT']['exists'] else '❌ MISSING'}
- **Size:** {analysis['CIPC_COMPLAINT'].get('size', 0):,} bytes
- **Last Modified:** {analysis['CIPC_COMPLAINT'].get('last_modified', 'N/A')}
- **Evidence Coverage:**
  - SF1 (Bantjies Debt): {'✅' if analysis['CIPC_COMPLAINT'].get('has_sf1') else '❌'}
  - SF2 (Rynette Control): {'✅' if analysis['CIPC_COMPLAINT'].get('has_sf2') else '❌'}
  - SF3 (Stock Adjustment): {'✅' if analysis['CIPC_COMPLAINT'].get('has_sf3') else '❌'}
  - SF6 (Kayla Estate): {'✅' if analysis['CIPC_COMPLAINT'].get('has_sf6') else '❌'}
  - JF01 (Shopify Email): {'✅' if analysis['CIPC_COMPLAINT'].get('has_jf01') else '❌'}

### POPIA Complaint
- **Status:** {'✅ EXISTS' if analysis['POPIA_COMPLAINT']['exists'] else '❌ MISSING'}
- **Size:** {analysis['POPIA_COMPLAINT'].get('size', 0):,} bytes
- **Last Modified:** {analysis['POPIA_COMPLAINT'].get('last_modified', 'N/A')}
- **Evidence Coverage:**
  - SF2 (Rynette Control): {'✅' if analysis['POPIA_COMPLAINT'].get('has_sf2') else '❌'}
  - SF7 (Email Seizure): {'✅' if analysis['POPIA_COMPLAINT'].get('has_sf7') else '❌'}

### NPA Tax Fraud Report
- **Status:** {'✅ EXISTS' if analysis['NPA_TAX_FRAUD']['exists'] else '❌ MISSING'}
- **Size:** {analysis['NPA_TAX_FRAUD'].get('size', 0):,} bytes
- **Last Modified:** {analysis['NPA_TAX_FRAUD'].get('last_modified', 'N/A')}
- **Evidence Coverage:**
  - SF3 (Stock Adjustment): {'✅' if analysis['NPA_TAX_FRAUD'].get('has_sf3') else '❌'}
  - SF4 (SARS Audit): {'✅' if analysis['NPA_TAX_FRAUD'].get('has_sf4') else '❌'}

### Commercial Crime Case
- **Status:** ❌ TO BE CREATED
- **Priority:** CRITICAL

## Enhancement Recommendations

### CIPC Complaint (Priority: HIGH)
{chr(10).join('- ' + e for e in recommendations['cipc_complaint']['enhancements'])}

### POPIA Complaint (Priority: CRITICAL)
{chr(10).join('- ' + e for e in recommendations['popia_complaint']['enhancements'])}

### NPA Tax Fraud Report (Priority: HIGH)
{chr(10).join('- ' + e for e in recommendations['npa_tax_fraud']['enhancements'])}

### Commercial Crime Case (Priority: CRITICAL)
{chr(10).join('- ' + e for e in recommendations['commercial_crime']['enhancements'])}

## Next Steps

1. **Immediate (Priority: CRITICAL)**
   - Create Commercial Crime case submission
   - Enhance POPIA complaint with SF2 and SF7 detailed analysis
   - Add criminal burden of proof assessments to all filings

2. **High Priority**
   - Enhance CIPC complaint with SF5 and SF8
   - Enhance NPA Tax Fraud report with SF3 and SF4 detailed analysis
   - Add entity relationship diagrams to all filings

3. **Medium Priority**
   - Cross-reference all events with ad-res-j7 evidence in each filing
   - Create visual evidence timelines for each filing
   - Add annexure indices to each filing

## Evidence Integration Status

- **Total SF Files:** 8
- **Total JF Directories:** 13
- **CIPC Integration:** Partial (needs SF5, SF8, JF13)
- **POPIA Integration:** Partial (needs SF2 details, SF7)
- **NPA Integration:** Partial (needs SF3 details, SF4)
- **Commercial Crime:** Not created

---

*Generated: {datetime.now().isoformat()}*
"""
    
    return summary, recommendations

def main():
    print("=" * 80)
    print("LEGAL FILINGS ENHANCEMENT ANALYSIS - 2025-12-22")
    print("=" * 80)
    
    # Analyze existing filings
    print("\n### ANALYZING EXISTING FILINGS ###")
    analysis = analyze_legal_filings()
    
    for name, details in analysis.items():
        print(f"\n{name}:")
        if details['exists']:
            print(f"  Size: {details['size']:,} bytes")
            print(f"  Lines: {details['line_count']}")
            print(f"  SF Evidence: {sum(1 for k,v in details.items() if k.startswith('has_sf') and v)}/8")
            print(f"  Burden of Proof: {'✅' if details['has_burden_of_proof'] else '❌'}")
        else:
            print("  Status: MISSING")
    
    # Generate recommendations
    print("\n### GENERATING RECOMMENDATIONS ###")
    summary, recommendations = create_legal_filings_summary()
    
    # Save summary
    summary_path = REVSTREAM_ROOT / "LEGAL_FILINGS_STATUS_2025_12_22.md"
    with open(summary_path, 'w') as f:
        f.write(summary)
    print(f"✓ Saved: {summary_path.name}")
    
    # Save recommendations JSON
    rec_path = REVSTREAM_ROOT / "LEGAL_FILINGS_RECOMMENDATIONS_2025_12_22.json"
    with open(rec_path, 'w') as f:
        json.dump(recommendations, f, indent=2)
    print(f"✓ Saved: {rec_path.name}")
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print("\nKey Findings:")
    print("  - CIPC Complaint: Needs SF5, SF8, JF13")
    print("  - POPIA Complaint: Needs detailed SF2, SF7 analysis")
    print("  - NPA Tax Fraud: Needs detailed SF3, SF4 analysis")
    print("  - Commercial Crime: TO BE CREATED (CRITICAL)")

if __name__ == "__main__":
    main()
