#!/usr/bin/env python3.11
"""
Generate comprehensive timeline mermaid diagram from events data
"""
import json
from datetime import datetime
from pathlib import Path

def load_events():
    """Load events from JSON"""
    events_path = Path('/home/ubuntu/revstream1/data_models/events/events.json')
    with open(events_path, 'r') as f:
        data = json.load(f)
    return data.get('events', [])

def load_entities():
    """Load entities for name resolution"""
    entities_path = Path('/home/ubuntu/revstream1/data_models/entities/entities.json')
    with open(entities_path, 'r') as f:
        data = json.load(f)
    
    # Create entity lookup
    entity_map = {}
    for category, items in data.get('entities', {}).items():
        if isinstance(items, list):
            for entity in items:
                entity_id = entity.get('entity_id')
                name = entity.get('name', entity_id)
                if entity_id:
                    entity_map[entity_id] = name
    
    return entity_map

def generate_comprehensive_timeline():
    """Generate comprehensive timeline with all events"""
    events = load_events()
    entity_map = load_entities()
    
    # Sort events by date
    sorted_events = sorted([e for e in events if e.get('date')], key=lambda x: x['date'])
    
    # Generate mermaid timeline
    mmd = ["timeline"]
    mmd.append("    title Comprehensive Revenue Stream Hijacking Timeline (2017-2025)")
    
    current_year = None
    for event in sorted_events:
        date = event.get('date', '')
        if not date:
            continue
        
        year = date[:4]
        
        # Add year section if new year
        if year != current_year:
            mmd.append(f"    section {year}")
            current_year = year
        
        # Format event description
        desc = event.get('description', event.get('title', 'Unknown event'))
        event_id = event.get('event_id', '')
        burden = event.get('burden_of_proof', '')
        
        # Truncate description if too long
        if len(desc) > 80:
            desc = desc[:77] + "..."
        
        # Add burden of proof indicator
        if 'criminal' in burden.lower() or '95%' in burden:
            desc = f"🔴 {desc}"
        elif 'exceeded' in burden.lower():
            desc = f"🟡 {desc}"
        
        # Add date and description
        mmd.append(f"    {date} : {desc}")
    
    return "\n".join(mmd)

def generate_criminal_events_timeline():
    """Generate timeline focusing on criminal threshold events"""
    events = load_events()
    
    # Filter criminal threshold events
    criminal_events = [e for e in events if 'criminal' in e.get('burden_of_proof', '').lower() or '95%' in e.get('burden_of_proof', '')]
    criminal_events = sorted([e for e in criminal_events if e.get('date')], key=lambda x: x['date'])
    
    mmd = ["timeline"]
    mmd.append("    title Criminal Threshold Events (95% Burden of Proof)")
    
    current_year = None
    for event in criminal_events:
        date = event.get('date', '')
        year = date[:4]
        
        if year != current_year:
            mmd.append(f"    section {year}")
            current_year = year
        
        desc = event.get('description', event.get('title', 'Unknown event'))
        if len(desc) > 80:
            desc = desc[:77] + "..."
        
        mmd.append(f"    {date} : 🔴 {desc}")
    
    return "\n".join(mmd)

def generate_phase_timeline():
    """Generate timeline organized by phases"""
    events = load_events()
    
    # Group by phase
    phases = {}
    for event in events:
        phase = event.get('phase', 'UNKNOWN')
        if phase not in phases:
            phases[phase] = []
        phases[phase].append(event)
    
    mmd = ["timeline"]
    mmd.append("    title Timeline by Investigation Phases")
    
    for phase in sorted(phases.keys()):
        mmd.append(f"    section {phase}")
        
        phase_events = sorted([e for e in phases[phase] if e.get('date')], key=lambda x: x['date'])
        
        for event in phase_events:
            date = event.get('date', '')
            desc = event.get('description', event.get('title', 'Unknown event'))
            
            if len(desc) > 80:
                desc = desc[:77] + "..."
            
            burden = event.get('burden_of_proof', '')
            if 'criminal' in burden.lower() or '95%' in burden:
                desc = f"🔴 {desc}"
            elif 'exceeded' in burden.lower():
                desc = f"🟡 {desc}"
            
            mmd.append(f"    {date} : {desc}")
    
    return "\n".join(mmd)

def main():
    base_path = Path('/home/ubuntu/revstream1')
    
    # Generate comprehensive timeline
    print("Generating comprehensive timeline...")
    comprehensive = generate_comprehensive_timeline()
    with open(base_path / 'comprehensive_timeline_2026_01_02.mmd', 'w') as f:
        f.write(comprehensive)
    print(f"  Saved: comprehensive_timeline_2026_01_02.mmd")
    
    # Generate criminal events timeline
    print("Generating criminal events timeline...")
    criminal = generate_criminal_events_timeline()
    with open(base_path / 'criminal_events_timeline_2026_01_02.mmd', 'w') as f:
        f.write(criminal)
    print(f"  Saved: criminal_events_timeline_2026_01_02.mmd")
    
    # Generate phase timeline
    print("Generating phase timeline...")
    phase = generate_phase_timeline()
    with open(base_path / 'phase_timeline_2026_01_02.mmd', 'w') as f:
        f.write(phase)
    print(f"  Saved: phase_timeline_2026_01_02.mmd")
    
    print("\nTimeline generation complete!")

if __name__ == '__main__':
    main()
