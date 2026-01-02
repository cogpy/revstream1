#!/usr/bin/env python3.11
"""
Generate comprehensive timeline with proper escaping for mermaid
"""
import json
import re
from datetime import datetime
from pathlib import Path

def sanitize_text(text):
    """Sanitize text for mermaid timeline"""
    if not text:
        return ""
    
    # Remove special characters that break mermaid
    text = text.replace('"', "'")
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace(':', ' -')
    text = text.replace(';', ',')
    
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Truncate if too long
    if len(text) > 70:
        text = text[:67] + "..."
    
    return text.strip()

def load_events():
    """Load events from JSON"""
    events_path = Path('/home/ubuntu/revstream1/data_models/events/events.json')
    with open(events_path, 'r') as f:
        data = json.load(f)
    return data.get('events', [])

def generate_comprehensive_timeline():
    """Generate comprehensive timeline with all events"""
    events = load_events()
    
    # Sort events by date
    sorted_events = sorted([e for e in events if e.get('date')], key=lambda x: x['date'])
    
    # Generate mermaid timeline
    mmd = ["timeline"]
    mmd.append("    title Revenue Stream Hijacking Timeline 2017-2025")
    
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
        desc = sanitize_text(desc)
        
        burden = event.get('burden_of_proof', '')
        
        # Add burden of proof indicator
        if 'criminal' in burden.lower() or '95%' in burden:
            indicator = "[CRIMINAL]"
        elif 'exceeded' in burden.lower():
            indicator = "[CIVIL+]"
        else:
            indicator = ""
        
        # Add date and description
        if indicator:
            mmd.append(f"    {date} - {indicator} {desc}")
        else:
            mmd.append(f"    {date} - {desc}")
    
    return "\n".join(mmd)

def generate_criminal_events_timeline():
    """Generate timeline focusing on criminal threshold events"""
    events = load_events()
    
    # Filter criminal threshold events
    criminal_events = [e for e in events if 'criminal' in e.get('burden_of_proof', '').lower() or '95%' in e.get('burden_of_proof', '')]
    criminal_events = sorted([e for e in criminal_events if e.get('date')], key=lambda x: x['date'])
    
    mmd = ["timeline"]
    mmd.append("    title Criminal Threshold Events - 95 Percent Burden of Proof")
    
    current_year = None
    for event in criminal_events:
        date = event.get('date', '')
        year = date[:4]
        
        if year != current_year:
            mmd.append(f"    section {year}")
            current_year = year
        
        desc = event.get('description', event.get('title', 'Unknown event'))
        desc = sanitize_text(desc)
        
        mmd.append(f"    {date} - [CRIMINAL] {desc}")
    
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
        phase_name = phase.replace('_', ' ')
        mmd.append(f"    section {phase_name}")
        
        phase_events = sorted([e for e in phases[phase] if e.get('date')], key=lambda x: x['date'])
        
        for event in phase_events[:20]:  # Limit to 20 per phase to avoid overcrowding
            date = event.get('date', '')
            desc = event.get('description', event.get('title', 'Unknown event'))
            desc = sanitize_text(desc)
            
            burden = event.get('burden_of_proof', '')
            if 'criminal' in burden.lower() or '95%' in burden:
                indicator = "[CRIM]"
            elif 'exceeded' in burden.lower():
                indicator = "[CIV+]"
            else:
                indicator = ""
            
            if indicator:
                mmd.append(f"    {date} - {indicator} {desc}")
            else:
                mmd.append(f"    {date} - {desc}")
    
    return "\n".join(mmd)

def main():
    base_path = Path('/home/ubuntu/revstream1')
    
    # Generate comprehensive timeline
    print("Generating comprehensive timeline...")
    comprehensive = generate_comprehensive_timeline()
    with open(base_path / 'comprehensive_timeline_fixed.mmd', 'w') as f:
        f.write(comprehensive)
    print(f"  Saved: comprehensive_timeline_fixed.mmd")
    
    # Generate criminal events timeline
    print("Generating criminal events timeline...")
    criminal = generate_criminal_events_timeline()
    with open(base_path / 'criminal_events_timeline_fixed.mmd', 'w') as f:
        f.write(criminal)
    print(f"  Saved: criminal_events_timeline_fixed.mmd")
    
    # Generate phase timeline
    print("Generating phase timeline...")
    phase = generate_phase_timeline()
    with open(base_path / 'phase_timeline_fixed.mmd', 'w') as f:
        f.write(phase)
    print(f"  Saved: phase_timeline_fixed.mmd")
    
    print("\nTimeline generation complete!")

if __name__ == '__main__':
    main()
