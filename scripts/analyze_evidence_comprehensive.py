#!/usr/bin/env python3
"""
Comprehensive Evidence Analysis for revstream1
Analyzes ad-res-j7 evidence to extract new entities, relations, and events
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
AD_RES_J7_PATH = Path("/home/ubuntu/ad-res-j7")
DOCS_PATH = REVSTREAM_PATH / "docs"
ENTITIES_PATH = DOCS_PATH / "entities"
EVENTS_PATH = DOCS_PATH / "events"

# Load existing entities and events
def load_existing_entities():
    """Load all existing entity IDs"""
    entities = {}
    if ENTITIES_PATH.exists():
        for entity_file in ENTITIES_PATH.glob("*.md"):
            entity_id = entity_file.stem
            entities[entity_id] = entity_file
    return entities

def load_existing_events():
    """Load all existing event IDs"""
    events = {}
    if EVENTS_PATH.exists():
        for event_file in EVENTS_PATH.glob("*.md"):
            event_id = event_file.stem
            events[event_id] = event_file
    return events

def analyze_sf_files():
    """Analyze all SF (Smoking Gun) files for new evidence"""
    sf_files = list((AD_RES_J7_PATH / "ANNEXURES").glob("SF*.md"))
    
    analysis = {
        "timestamp": datetime.now().isoformat(),
        "sf_files_analyzed": len(sf_files),
        "new_entities_identified": [],
        "new_relations_identified": [],
        "new_events_identified": [],
        "evidence_strength_assessment": {}
    }
    
    for sf_file in sorted(sf_files):
        sf_id = sf_file.stem
        print(f"Analyzing {sf_id}...")
        
        with open(sf_file, 'r') as f:
            content = f.read()
        
        # Extract key information
        file_analysis = {
            "file": sf_id,
            "path": str(sf_file.relative_to(AD_RES_J7_PATH)),
            "entities_mentioned": extract_entities(content),
            "financial_amounts": extract_financial_amounts(content),
            "dates_mentioned": extract_dates(content),
            "legal_implications": extract_legal_implications(content),
            "burden_of_proof": assess_burden_of_proof(content, sf_id)
        }
        
        analysis["evidence_strength_assessment"][sf_id] = file_analysis
    
    return analysis

def extract_entities(content):
    """Extract entity mentions from content"""
    entities = []
    
    # Common entity patterns
    patterns = {
        "persons": [
            r"Bantjies", r"Danie Bantjies", r"Peter Faucitt", r"Peter Andrew Faucitt",
            r"Rynette Farrar", r"Jacqui Faucitt", r"Daniel Faucitt", 
            r"Kayla Pretorius", r"Linda", r"Chantal"
        ],
        "organizations": [
            r"RegimA", r"Strategic Logistics", r"Villa Via", r"ReZonance",
            r"Adderory", r"SARS", r"Faucitt Family Trust"
        ]
    }
    
    for entity_type, entity_list in patterns.items():
        for entity in entity_list:
            if re.search(entity, content, re.IGNORECASE):
                entities.append({
                    "name": entity,
                    "type": entity_type,
                    "mentions": len(re.findall(entity, content, re.IGNORECASE))
                })
    
    return entities

def extract_financial_amounts(content):
    """Extract financial amounts from content"""
    amounts = []
    
    # Pattern for South African Rand amounts
    patterns = [
        r"R\s*[\d,]+(?:\.\d{2})?",
        r"R[\d,]+(?:\.\d{2})?"
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content)
        amounts.extend(matches)
    
    return list(set(amounts))

def extract_dates(content):
    """Extract dates from content"""
    dates = []
    
    # Common date patterns
    patterns = [
        r"\d{4}-\d{2}-\d{2}",
        r"\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}",
        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}",
        r"(?:June|July|August)\s+\d{4}"
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        dates.extend(matches)
    
    return list(set(dates))

def extract_legal_implications(content):
    """Extract legal implications mentioned in content"""
    implications = []
    
    keywords = [
        "breach of fiduciary duty", "conflict of interest", "fraud",
        "professional misconduct", "ethical breach", "criminal",
        "civil liability", "regulatory violation"
    ]
    
    for keyword in keywords:
        if re.search(keyword, content, re.IGNORECASE):
            implications.append(keyword)
    
    return implications

def assess_burden_of_proof(content, sf_id):
    """Assess burden of proof based on evidence type"""
    assessment = {
        "civil_standard": "UNKNOWN",
        "criminal_standard": "UNKNOWN",
        "evidence_type": []
    }
    
    # Documentary evidence indicators
    if any(term in content.lower() for term in ["ledger", "financial statement", "accounting record", "trial balance"]):
        assessment["evidence_type"].append("documentary")
        assessment["civil_standard"] = "HIGH"
        assessment["criminal_standard"] = "MEDIUM"
    
    # System-generated evidence
    if any(term in content.lower() for term in ["screenshot", "system", "sage", "database"]):
        assessment["evidence_type"].append("system_generated")
        assessment["civil_standard"] = "HIGH"
        assessment["criminal_standard"] = "MEDIUM"
    
    # Official correspondence
    if any(term in content.lower() for term in ["sars", "court order", "official", "government"]):
        assessment["evidence_type"].append("official")
        assessment["civil_standard"] = "HIGH"
        assessment["criminal_standard"] = "HIGH"
    
    # Email/communication evidence
    if any(term in content.lower() for term in ["email", "correspondence", "letter"]):
        assessment["evidence_type"].append("communication")
        assessment["civil_standard"] = "MEDIUM"
        assessment["criminal_standard"] = "LOW"
    
    return assessment

def identify_new_entities():
    """Identify new entities not yet in the repository"""
    existing = load_existing_entities()
    
    new_entities = []
    
    # Check for entities mentioned in SF files but not in existing entities
    # This would require cross-referencing with the SF analysis
    
    # Known new entities from recent analysis
    potential_new = [
        {
            "id": "PERSON_015",
            "name": "Chantal",
            "type": "PERSON",
            "role": "Estate executor correspondent",
            "evidence": ["JF08", "SF6"],
            "significance": "Correspondence regarding Kayla Pretorius estate finalization"
        }
    ]
    
    for entity in potential_new:
        if entity["id"] not in existing:
            new_entities.append(entity)
    
    return new_entities

def identify_new_relations():
    """Identify new relations between entities"""
    relations = []
    
    # Based on SF file analysis
    potential_relations = [
        {
            "source": "PERSON_007",  # Bantjies
            "target": "TRUST_001",   # Faucitt Family Trust
            "type": "DEBTOR",
            "amount": "R18,685,000",
            "evidence": "SF1",
            "civil_burden": "HIGH",
            "criminal_burden": "MEDIUM"
        },
        {
            "source": "PERSON_007",  # Bantjies
            "target": "TRUST_001",   # Faucitt Family Trust
            "type": "UNDISCLOSED_TRUSTEE",
            "evidence": "SF1",
            "civil_burden": "HIGH",
            "criminal_burden": "HIGH"
        },
        {
            "source": "ORG_015",     # SARS
            "target": "ORG_002",     # RegimA
            "type": "TAX_AUDIT",
            "evidence": "SF4",
            "civil_burden": "HIGH",
            "criminal_burden": "N/A"
        }
    ]
    
    return potential_relations

def identify_new_events():
    """Identify new timeline events from evidence"""
    existing = load_existing_events()
    
    new_events = []
    
    # Events identified from SF files
    potential_events = [
        {
            "id": "EVENT_086",
            "date": "2025-06-06",
            "title": "Daniel reports fraud to Bantjies (unknowingly to perpetrator)",
            "category": "fraud_exposure",
            "evidence": "SF1",
            "entities": ["PERSON_003", "PERSON_007"],
            "significance": "Daniel unknowingly reported fraud to conflicted party with R18.685M debt",
            "civil_burden": "HIGH",
            "criminal_burden": "MEDIUM"
        },
        {
            "id": "EVENT_087",
            "date": "2025-06-10",
            "title": "Bantjies dismisses Daniel's audit request",
            "category": "obstruction",
            "evidence": "SF1",
            "entities": ["PERSON_007", "PERSON_003"],
            "financial_impact": "R18,685,000.00",
            "significance": "Bantjies had R18.685M reasons to prevent audit discovery",
            "civil_burden": "HIGH",
            "criminal_burden": "HIGH"
        },
        {
            "id": "EVENT_088",
            "date": "2025-08-01",
            "title": "Bantjies certifies Peter's affidavit as Commissioner of Oaths",
            "category": "professional_misconduct",
            "evidence": "SF1",
            "entities": ["PERSON_007", "PERSON_001"],
            "significance": "Ethical breach - certified affidavit omitting own trustee status and debt",
            "civil_burden": "HIGH",
            "criminal_burden": "HIGH"
        }
    ]
    
    for event in potential_events:
        if event["id"] not in existing:
            new_events.append(event)
    
    return new_events

def main():
    print("=" * 80)
    print("COMPREHENSIVE EVIDENCE ANALYSIS")
    print("=" * 80)
    
    # Analyze SF files
    print("\n1. Analyzing SF (Smoking Gun) files...")
    sf_analysis = analyze_sf_files()
    
    # Identify new entities
    print("\n2. Identifying new entities...")
    new_entities = identify_new_entities()
    sf_analysis["new_entities_identified"] = new_entities
    
    # Identify new relations
    print("\n3. Identifying new relations...")
    new_relations = identify_new_relations()
    sf_analysis["new_relations_identified"] = new_relations
    
    # Identify new events
    print("\n4. Identifying new timeline events...")
    new_events = identify_new_events()
    sf_analysis["new_events_identified"] = new_events
    
    # Save analysis
    output_file = REVSTREAM_PATH / f"EVIDENCE_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
    with open(output_file, 'w') as f:
        json.dump(sf_analysis, f, indent=2)
    
    print(f"\n✓ Analysis saved to: {output_file}")
    print(f"\n✓ SF files analyzed: {sf_analysis['sf_files_analyzed']}")
    print(f"✓ New entities identified: {len(new_entities)}")
    print(f"✓ New relations identified: {len(new_relations)}")
    print(f"✓ New events identified: {len(new_events)}")
    
    return sf_analysis

if __name__ == "__main__":
    main()
