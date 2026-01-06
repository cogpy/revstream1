#!/usr/bin/env python3.11
"""
Enhanced Timeline Generator
Adds key_actors, cumulative financial impact, and improved application context
"""

import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def load_data():
    """Load all necessary data"""
    base_path = Path('/home/ubuntu/revstream1/data_models')
    
    with open(base_path / 'entities/entities.json') as f:
        entities = json.load(f)
    with open(base_path / 'events/events.json') as f:
        events = json.load(f)
    with open(base_path / 'timelines/timeline.json') as f:
        timeline = json.load(f)
    
    return entities, events, timeline

def get_entity_name(entity_id, entities):
    """Get entity name from entity_id"""
    for entity_type, entity_list in entities['entities'].items():
        for entity in entity_list:
            if entity.get('entity_id') == entity_id:
                return entity.get('name', entity_id)
    return entity_id

def extract_financial_amount(financial_str):
    """Extract numeric amount from financial string"""
    if not financial_str:
        return 0
    
    if isinstance(financial_str, (int, float)):
        return float(financial_str)
    
    if isinstance(financial_str, str):
        # Remove R, commas, spaces, and + signs
        cleaned = financial_str.replace('R', '').replace(',', '').replace(' ', '').replace('+', '')
        
        # Handle ranges (take the higher value)
        if '-' in cleaned:
            parts = cleaned.split('-')
            try:
                return float(parts[-1])
            except:
                return 0
        
        try:
            return float(cleaned)
        except:
            return 0
    
    return 0

def enhance_timeline(entities, events, timeline):
    """Enhance timeline with additional information"""
    
    # Create event lookup
    event_lookup = {e['event_id']: e for e in events['events']}
    
    # Track cumulative financial impact
    cumulative_financial = 0
    
    enhanced_timeline = []
    
    for entry in timeline['timeline']:
        enhanced_entry = entry.copy()
        
        # Extract key actors from events
        key_actors = set()
        total_financial = 0
        burden_levels = set()
        
        for event_id in entry.get('events', []):
            if event_id in event_lookup:
                event = event_lookup[event_id]
                
                # Add perpetrators and victims as key actors
                for perpetrator in event.get('perpetrators', []):
                    actor_name = get_entity_name(perpetrator, entities)
                    key_actors.add(actor_name)
                
                for victim in event.get('victims', []):
                    actor_name = get_entity_name(victim, entities)
                    key_actors.add(actor_name)
                
                # Calculate financial impact
                financial = extract_financial_amount(event.get('financial_impact', 0))
                total_financial += financial
                
                # Track burden of proof levels
                burden = event.get('burden_of_proof', '')
                if burden:
                    burden_levels.add(burden)
        
        # Add key_actors if not already present
        if key_actors:
            enhanced_entry['key_actors'] = sorted(list(key_actors))
        
        # Add financial impact tracking
        if total_financial > 0:
            cumulative_financial += total_financial
            enhanced_entry['financial_impact'] = f"R{total_financial:,.2f}"
            enhanced_entry['cumulative_financial_impact'] = f"R{cumulative_financial:,.2f}"
        
        # Enhance application context based on burden of proof
        if not enhanced_entry.get('application_context'):
            app_context = []
            if 'criminal_95' in burden_levels:
                app_context.append('2-CRIMINAL-CASE')
            if any(b in burden_levels for b in ['civil_50%', 'civil_50%_exceeded']):
                app_context.append('1-CIVIL-RESPONSE')
            app_context.append('3-EXTERNAL-VALIDATION')
            enhanced_entry['application_context'] = app_context
        
        # Add burden of proof summary
        if burden_levels:
            enhanced_entry['burden_of_proof_levels'] = sorted(list(burden_levels))
        
        enhanced_timeline.append(enhanced_entry)
    
    return enhanced_timeline

def main():
    print("Loading data models...")
    entities, events, timeline = load_data()
    
    print("Enhancing timeline...")
    enhanced_timeline = enhance_timeline(entities, events, timeline)
    
    # Update metadata
    timeline['metadata']['version'] = '19.0_ENHANCED_2026_01_06'
    timeline['metadata']['last_updated'] = datetime.now().isoformat()
    timeline['metadata']['changes'] = 'Added key_actors, financial tracking, and enhanced application context'
    timeline['timeline'] = enhanced_timeline
    
    # Save enhanced timeline
    output_path = Path('/home/ubuntu/revstream1/data_models/timelines/timeline.json')
    
    # Backup current version
    backup_path = output_path.with_suffix('.json.backup_' + datetime.now().strftime('%Y%m%d_%H%M%S'))
    if output_path.exists():
        import shutil
        shutil.copy(output_path, backup_path)
        print(f"Backup created: {backup_path}")
    
    # Save enhanced version
    with open(output_path, 'w') as f:
        json.dump(timeline, f, indent=2)
    
    print(f"Enhanced timeline saved to: {output_path}")
    print(f"\nEnhancements:")
    print(f"  - Added key_actors to {len([e for e in enhanced_timeline if 'key_actors' in e])} entries")
    print(f"  - Added financial tracking to {len([e for e in enhanced_timeline if 'financial_impact' in e])} entries")
    print(f"  - Enhanced application context for {len([e for e in enhanced_timeline if 'application_context' in e])} entries")

if __name__ == '__main__':
    main()
