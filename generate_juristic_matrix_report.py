#!/usr/bin/env python3
"""
Generate Juristic Timeline Matrix Report in Markdown format
"""

import json

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def generate_juristic_matrix_md(matrix_data):
    """Generate markdown table for the juristic timeline matrix"""
    
    md_content = "# Juristic Timeline Matrix\n\n"
    md_content += "**Date:** 2025-11-18  \n"
    md_content += "**Case:** 2025-137857 (Revenue Stream Hijacking)  \n"
    md_content += "**Author:** Manus AI\n\n"
    md_content += "---\n\n"
    md_content += "This matrix maps each legally significant event to the legal theories it supports, providing a chronological view of how the narrative builds a multi-faceted legal argument.\n\n"
    
    md_content += "| Date       | Event ID | Event Description | Financial Impact | Legal Theories Supported |\n"
    md_content += "| :---       | :---     | :---              | :---             | :---                     |\n"
    
    for item in matrix_data:
        date = item.get("date", "N/A")
        event_id = item.get("event_id", "N/A")
        description = item.get("description", "N/A").replace('\n', ' ')
        financial_impact = item.get("financial_impact", "N/A") or "N/A"
        
        theories_supported = "<br>".join([
            f"- **{t['theory_name']}**" for t in item.get("legal_theories_supported", [])
        ])
        
        md_content += f"| {date} | `{event_id}` | {description} | {financial_impact} | {theories_supported} |\n"
        
    return md_content

def main():
    """Main generation function"""
    print("=" * 80)
    print("GENERATING JURISTIC TIMELINE MATRIX REPORT")
    print("=" * 80)
    
    # Load the integration data
    print("\n1. Loading legal framework integration data...")
    integration_data = load_json("LEGAL_FRAMEWORK_INTEGRATION.json")
    juristic_matrix_data = integration_data.get("juristic_timeline_matrix", [])
    
    # Generate markdown report
    print("2. Generating Markdown report...")
    md_report = generate_juristic_matrix_md(juristic_matrix_data)
    
    # Save the report
    output_file = "JURISTIC_TIMELINE_MATRIX.md"
    with open(output_file, 'w') as f:
        f.write(md_report)
        
    print(f"\n{'=' * 80}")
    print(f"Report generation complete. Saved to: {output_file}")
    print(f"{'=' * 80}")

if __name__ == "__main__":
    main()
