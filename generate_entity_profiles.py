#!/usr/bin/env python3
"""
Entity Profile Page Generator
Creates comprehensive profile pages for each entity in the case
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Paths
BASE_DIR = Path("/home/ubuntu/revstream1")
DATA_MODELS_DIR = BASE_DIR / "data_models"
DOCS_DIR = BASE_DIR / "docs"
ENTITY_PROFILES_DIR = DOCS_DIR / "entity-profiles"

# Create entity profiles directory
ENTITY_PROFILES_DIR.mkdir(exist_ok=True)

# Load data models
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

entities_data = load_json(DATA_MODELS_DIR / "entities/entities_refined_2025_11_25_v19.json")
events_data = load_json(DATA_MODELS_DIR / "events/events_refined_2025_11_25_v20.json")
relations_data = load_json(DATA_MODELS_DIR / "relations/relations_refined_2025_11_25_v16.json")

print("="*80)
print("GENERATING ENTITY PROFILE PAGES")
print("="*80)
print()

# Extract all entities
all_entities = []

# Persons
for person in entities_data["entities"].get("persons", []):
    all_entities.append({
        "entity_id": person["entity_id"],
        "name": person["name"],
        "type": "Natural Person",
        "category": "persons",
        "data": person
    })

# Organizations
for org in entities_data["entities"].get("organizations", []):
    all_entities.append({
        "entity_id": org["entity_id"],
        "name": org["name"],
        "type": "Juristic Person (Organization)",
        "category": "organizations",
        "data": org
    })

# Trust entities
for trust in entities_data["entities"].get("trust_entities", []):
    all_entities.append({
        "entity_id": trust["entity_id"],
        "name": trust["name"],
        "type": "Juristic Person (Trust)",
        "category": "trust_entities",
        "data": trust
    })

# Bank accounts
for account in entities_data["entities"].get("bank_accounts", []):
    all_entities.append({
        "entity_id": account["entity_id"],
        "name": account.get("entity_name", account.get("name", "Unknown Account")),
        "type": "Bank Account",
        "category": "bank_accounts",
        "data": account
    })

print(f"Found {len(all_entities)} entities to process")
print()

# Helper function to get events involving entity
def get_entity_events(entity_id):
    entity_events = []
    for event in events_data["events"]:
        if entity_id in event.get("entities_involved", []):
            entity_events.append(event)
    return sorted(entity_events, key=lambda x: x.get("event_date", ""))

# Helper function to get relations involving entity
def get_entity_relations(entity_id):
    outgoing = []
    incoming = []
    
    # Check all relation categories
    for category, relations_list in relations_data["relations"].items():
        if isinstance(relations_list, list):
            for relation in relations_list:
                if relation.get("from_entity") == entity_id:
                    outgoing.append(relation)
                if relation.get("to_entity") == entity_id:
                    incoming.append(relation)
    
    return outgoing, incoming

# Generate profile page for each entity
for entity in all_entities:
    entity_id = entity["entity_id"]
    entity_name = entity["name"]
    entity_type = entity["type"]
    entity_data = entity["data"]
    
    print(f"Generating profile for {entity_id}: {entity_name}")
    
    # Get entity-specific data
    entity_events = get_entity_events(entity_id)
    outgoing_relations, incoming_relations = get_entity_relations(entity_id)
    
    # Calculate financial impact
    total_financial_impact = 0.0
    for event in entity_events:
        impact_str = event.get("financial_impact", "R0")
        if impact_str and impact_str != "Unknown":
            # Extract numeric value
            impact_str = impact_str.replace("R", "").replace(",", "").replace("+", "").strip()
            try:
                if "M" in impact_str:
                    total_financial_impact += float(impact_str.replace("M", "")) * 1000000
                else:
                    total_financial_impact += float(impact_str)
            except:
                pass
    
    # Generate markdown content
    content = f"""# Entity Profile: {entity_name}

---

## Entity Information

| Field | Value |
|-------|-------|
| **Entity ID** | {entity_id} |
| **Entity Name** | {entity_name} |
| **Entity Type** | {entity_type} |
| **Category** | {entity["category"]} |
"""
    
    # Add entity-specific fields
    if entity_type == "Natural Person":
        content += f"""| **ID Number** | {entity_data.get("id_number", "N/A")} |
| **Role** | {entity_data.get("role", "N/A")} |
| **Agent Type** | {entity_data.get("agent_type", "N/A")} |
| **Legal Status** | {entity_data.get("legal_status", "N/A")} |
"""
    elif entity_type.startswith("Juristic Person"):
        content += f"""| **Registration Number** | {entity_data.get("registration_number", entity_data.get("reg_number", "N/A"))} |
| **Entity Type** | {entity_data.get("entity_type", "N/A")} |
| **Status** | {entity_data.get("status", "N/A")} |
"""
    elif entity_type == "Bank Account":
        content += f"""| **Account Number** | {entity_data.get("account_number", "N/A")} |
| **Account Type** | {entity_data.get("account_type", "N/A")} |
"""
    
    content += f"""
---

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Events Involved** | {len(entity_events)} |
| **Outgoing Relations** | {len(outgoing_relations)} |
| **Incoming Relations** | {len(incoming_relations)} |
| **Total Financial Impact** | R{total_financial_impact:,.2f} |

---

## Primary Actions

"""
    
    if "primary_actions" in entity_data:
        for action in entity_data["primary_actions"]:
            content += f"- {action.replace('_', ' ').title()}\n"
    else:
        content += "*No primary actions documented*\n"
    
    content += """
---

## Events Timeline

"""
    
    if entity_events:
        content += f"This entity is involved in **{len(entity_events)} events** across the case timeline.\n\n"
        
        # Group events by timeline phase
        events_by_phase = defaultdict(list)
        for event in entity_events:
            phase = event.get("timeline_phase", "Unknown Phase")
            events_by_phase[phase].append(event)
        
        for phase in sorted(events_by_phase.keys()):
            phase_events = events_by_phase[phase]
            content += f"### {phase}\n\n"
            
            for event in phase_events:
                event_date = event.get("event_date", "Unknown")
                event_title = event.get("event_title", "Untitled Event")
                event_id = event.get("event_id", "")
                event_desc = event.get("event_description", "")
                financial_impact = event.get("financial_impact", "Unknown")
                
                content += f"#### {event_id}: {event_title}\n\n"
                content += f"**Date:** {event_date}  \n"
                content += f"**Financial Impact:** {financial_impact}  \n\n"
                content += f"{event_desc}\n\n"
                
                # Evidence
                evidence_files = event.get("evidence_files", [])
                if evidence_files:
                    content += "**Evidence:**\n"
                    for evidence in evidence_files[:3]:  # Show first 3
                        content += f"- `{evidence}`\n"
                    if len(evidence_files) > 3:
                        content += f"- *...and {len(evidence_files) - 3} more*\n"
                    content += "\n"
    else:
        content += "*This entity is not directly involved in any documented events.*\n\n"
    
    content += """---

## Relationships

"""
    
    # Outgoing relations
    if outgoing_relations:
        content += f"### Outgoing Relations ({len(outgoing_relations)})\n\n"
        content += "Relations where this entity is the **source**:\n\n"
        
        # Group by relation type
        relations_by_type = defaultdict(list)
        for rel in outgoing_relations:
            rel_type = rel.get("relation_type", "UNKNOWN")
            relations_by_type[rel_type].append(rel)
        
        for rel_type in sorted(relations_by_type.keys()):
            content += f"#### {rel_type}\n\n"
            for rel in relations_by_type[rel_type]:
                to_entity = rel.get("to_entity", "Unknown")
                rel_desc = rel.get("relation_description", "")
                content += f"- **→ {to_entity}**: {rel_desc}\n"
            content += "\n"
    else:
        content += "### Outgoing Relations\n\n*No outgoing relations documented.*\n\n"
    
    # Incoming relations
    if incoming_relations:
        content += f"### Incoming Relations ({len(incoming_relations)})\n\n"
        content += "Relations where this entity is the **target**:\n\n"
        
        # Group by relation type
        relations_by_type = defaultdict(list)
        for rel in incoming_relations:
            rel_type = rel.get("relation_type", "UNKNOWN")
            relations_by_type[rel_type].append(rel)
        
        for rel_type in sorted(relations_by_type.keys()):
            content += f"#### {rel_type}\n\n"
            for rel in relations_by_type[rel_type]:
                from_entity = rel.get("from_entity", "Unknown")
                rel_desc = rel.get("relation_description", "")
                content += f"- **{from_entity} →**: {rel_desc}\n"
            content += "\n"
    else:
        content += "### Incoming Relations\n\n*No incoming relations documented.*\n\n"
    
    content += """---

## Financial Impact Analysis

"""
    
    if entity_events:
        # Calculate impact by category
        impact_by_category = defaultdict(float)
        for event in entity_events:
            category = event.get("event_category", "Unknown")
            impact_str = event.get("financial_impact", "R0")
            if impact_str and impact_str != "Unknown":
                impact_str = impact_str.replace("R", "").replace(",", "").replace("+", "").strip()
                try:
                    if "M" in impact_str:
                        impact = float(impact_str.replace("M", "")) * 1000000
                    else:
                        impact = float(impact_str)
                    impact_by_category[category] += impact
                except:
                    pass
        
        if impact_by_category:
            content += "### Impact by Category\n\n"
            content += "| Category | Amount |\n"
            content += "|----------|--------|\n"
            for category in sorted(impact_by_category.keys(), key=lambda x: impact_by_category[x], reverse=True):
                content += f"| {category} | R{impact_by_category[category]:,.2f} |\n"
            content += f"| **TOTAL** | **R{total_financial_impact:,.2f}** |\n\n"
        else:
            content += "*No quantifiable financial impact documented.*\n\n"
    else:
        content += "*No financial impact data available.*\n\n"
    
    content += """---

## Evidence References

"""
    
    # Collect all evidence files
    all_evidence = set()
    for event in entity_events:
        all_evidence.update(event.get("evidence_files", []))
    for rel in outgoing_relations + incoming_relations:
        all_evidence.update(rel.get("evidence_files", []))
    
    if "evidence_files" in entity_data:
        all_evidence.update(entity_data["evidence_files"])
    
    if all_evidence:
        content += f"This entity is referenced in **{len(all_evidence)} evidence files**:\n\n"
        for evidence in sorted(all_evidence)[:10]:  # Show first 10
            content += f"- `{evidence}`\n"
        if len(all_evidence) > 10:
            content += f"- *...and {len(all_evidence) - 10} more*\n"
        content += "\n"
    else:
        content += "*No evidence files directly reference this entity.*\n\n"
    
    content += """---

## GitHub Pages References

"""
    
    if "github_pages_reference" in entity_data:
        content += f"- [Entity Reference]({entity_data['github_pages_reference']})\n"
    
    # Add event references
    event_pages = set()
    for event in entity_events:
        if "github_pages_reference" in event:
            event_pages.add(event["github_pages_reference"])
    
    if event_pages:
        content += "\n**Event References:**\n"
        for page in sorted(event_pages):
            content += f"- [{page.split('/')[-1]}]({page})\n"
    
    content += """
---

## Extended Evidence Repository

For additional evidence and supporting documentation, see the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).

"""
    
    if "ad_res_j7_reference" in entity_data:
        content += f"**Direct Reference:** `{entity_data['ad_res_j7_reference']}`\n\n"
    
    content += f"""---

*Entity profile generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*  
*Data models version: Entities v19.0, Events v20.0, Relations v16.0*
"""
    
    # Save profile page
    filename = f"{entity_id.lower()}-{entity_name.lower().replace(' ', '-').replace('(', '').replace(')', '')}.md"
    filepath = ENTITY_PROFILES_DIR / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Saved to {filename}")

print()
print("="*80)
print("ENTITY PROFILE PAGES GENERATED SUCCESSFULLY")
print("="*80)
print(f"\nTotal profiles created: {len(all_entities)}")
print(f"Output directory: {ENTITY_PROFILES_DIR}")
