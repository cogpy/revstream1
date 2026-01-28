#!/usr/bin/env python3
"""
Generate the Master Record for Events (Events.md).
"""

import json
from pathlib import Path
from datetime import datetime

REPO_DIR = Path("/home/ubuntu/revstream1")

def load_json(filepath):
    """Load a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def format_event(event):
    """Format a single event into Markdown."""
    md = []
    title = event.get('title', event.get('description', 'N/A'))
    md.append(f"### {title} (`{event.get('event_id', 'N/A')}`)")
    md.append("")
    
    md.append("| Attribute | Details |")
    md.append("|---|---|")
    md.append(f"| **Date** | {event.get('date', 'N/A')} |")
    md.append(f"| **Category** | {event.get('category', 'N/A').replace('_', ' ').title()} |")
    md.append(f"| **Type** | {event.get('event_type', 'N/A').replace('_', ' ').title()} |")
    md.append(f"| **Burden of Proof** | {event.get('burden_of_proof', 'N/A')} |")
    
    if event.get('financial_impact', 0) != 0:
        md.append(f"| **Financial Impact** | {event.get('financial_impact', 'N/A')} |")

    md.append("")
    md.append("**Description:**")
    md.append(f"> {event.get('description', 'No description provided.')}")
    md.append("")
    
    md.append("**Entities Involved:**")
    md.append(", ".join(event.get('entities_involved', [])))
    md.append("")

    return "\n".join(md)

def main():
    """Main function to generate the Events.md file."""
    events_path = REPO_DIR / "data_models/events/events.json"
    events_data = load_json(events_path)
    
    output_path = REPO_DIR / "MR/Events.md"
    
    md_content = []
    md_content.append("# Master Record: Events")
    md_content.append("## Discrete Timelines & State Changes")
    md_content.append("--- ")
    md_content.append(f"*Version: {events_data['metadata']['version']}* ")
    md_content.append(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}* ")
    md_content.append("")

    # Sort events by date
    sorted_events = sorted(events_data['events'], key=lambda x: x.get('date', '9999-99-99'))

    for event in sorted_events:
        md_content.append(format_event(event))
        md_content.append("---")

    with open(output_path, 'w') as f:
        f.write("\n".join(md_content))
    
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
