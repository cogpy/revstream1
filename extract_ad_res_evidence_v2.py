import os
import json
import re
from pathlib import Path

def extract_timeline_events(ad_res_path):
    """Extract timeline events from ad-res-j7 comprehensive timeline"""
    timeline_file = f"{ad_res_path}/ANNEXURES/JF09/COMPREHENSIVE_TIMELINE_2017_2025.md"
    
    events = []
    if os.path.exists(timeline_file):
        with open(timeline_file, 'r') as f:
            content = f.read()
            
            # Extract date-based events
            date_pattern = r'### ([A-Za-z]+ \d+, \d{4})\n\*\*Event\*\*: (.+?)\n\*\*Significance\*\*: (.+?)(?:\n|$)'
            matches = re.findall(date_pattern, content, re.MULTILINE)
            
            for match in matches:
                events.append({
                    "date": match[0],
                    "event": match[1],
                    "significance": match[2]
                })
    
    return events

def extract_entity_updates(ad_res_path):
    """Extract entity updates from ad-res-j7"""
    entity_file = f"{ad_res_path}/ANNEXURES/JF09/ENTITY_RELATION_UPDATES_20250811_COMPLETE.md"
    
    entities = []
    if os.path.exists(entity_file):
        with open(entity_file, 'r') as f:
            content = f.read()
            
            # Extract entity sections
            entity_pattern = r'## (.+?Entity.+?)\n\n(.+?)(?=\n##|\Z)'
            matches = re.findall(entity_pattern, content, re.DOTALL)
            
            for match in matches:
                entities.append({
                    "title": match[0],
                    "content": match[1][:500]  # First 500 chars
                })
    
    return entities

def scan_key_documents(ad_res_path):
    """Scan for key documents with evidence"""
    key_files = [
        "KEY_EVENTS_TIMELINE_MARCH_AUGUST_2025.md",
        "COMPREHENSIVE_EVIDENCE_INDEX.json",
        "MASTER_CONSPIRACY_TIMELINE_2021_2025.md",
        "FINANCIAL_HYPERGRAPH_TIMELINE_LINKS.md"
    ]
    
    found_files = []
    for root, dirs, files in os.walk(ad_res_path):
        for file in files:
            if file in key_files:
                found_files.append(os.path.join(root, file))
    
    return found_files

def extract_key_events_timeline(ad_res_path):
    """Extract from KEY_EVENTS_TIMELINE_MARCH_AUGUST_2025.md"""
    timeline_file = f"{ad_res_path}/KEY_EVENTS_TIMELINE_MARCH_AUGUST_2025.md"
    
    events = []
    if os.path.exists(timeline_file):
        with open(timeline_file, 'r') as f:
            content = f.read()
            
            # Extract events with dates
            event_pattern = r'(?:###|##) (.+?)\n(?:.+?\n)*?\*\*Date\*\*: (.+?)\n'
            matches = re.findall(event_pattern, content, re.MULTILINE)
            
            for match in matches:
                events.append({
                    "title": match[0],
                    "date": match[1]
                })
    
    return events

def main():
    ad_res_path = "/home/ubuntu/ad-res-j7"
    
    # Extract various evidence types
    timeline_events = extract_timeline_events(ad_res_path)
    entity_updates = extract_entity_updates(ad_res_path)
    key_files = scan_key_documents(ad_res_path)
    key_events = extract_key_events_timeline(ad_res_path)
    
    # Compile cross-reference report
    cross_ref = {
        "metadata": {
            "extraction_date": "2025-11-17",
            "source_repository": "ad-res-j7",
            "target_repository": "revstream1"
        },
        "timeline_events_extracted": len(timeline_events),
        "timeline_events": timeline_events[:20],  # First 20
        "entity_updates_extracted": len(entity_updates),
        "entity_updates": entity_updates,
        "key_events_extracted": len(key_events),
        "key_events": key_events[:20],  # First 20
        "key_files_found": key_files,
        "recommendations": {
            "new_events_to_add": [],
            "entities_to_update": [],
            "relations_to_add": []
        }
    }
    
    # Save cross-reference report
    output_path = "/home/ubuntu/revstream1/AD_RES_J7_CROSS_REFERENCE.json"
    with open(output_path, 'w') as f:
        json.dump(cross_ref, f, indent=2)
    
    print(json.dumps(cross_ref, indent=2))

if __name__ == "__main__":
    main()
