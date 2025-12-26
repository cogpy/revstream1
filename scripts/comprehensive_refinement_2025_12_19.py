#!/usr/bin/env python3.11
"""
Comprehensive Refinement Script - 2025-12-19
Analyzes ad-res-j7 evidence and refines revstream1 data models
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

# Paths
REVSTREAM_ROOT = Path("/home/ubuntu/revstream1")
AD_RES_ROOT = Path("/home/ubuntu/ad-res-j7")
DATA_MODELS = REVSTREAM_ROOT / "data_models"
ANNEXURES = AD_RES_ROOT / "ANNEXURES"

# Load current data models
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def analyze_evidence_files():
    """Analyze all SF evidence files for entities, relations, and events"""
    
    sf_files = sorted(ANNEXURES.glob("SF*.md"))
    print(f"Found {len(sf_files)} SF evidence files")
    
    analysis = {
        "entities_found": [],
        "relations_found": [],
        "events_found": [],
        "financial_amounts": [],
        "dates_found": [],
        "evidence_summary": {}
    }
    
    for sf_file in sf_files:
        print(f"\nAnalyzing: {sf_file.name}")
        content = sf_file.read_text()
        
        # Extract entities mentioned
        entities = extract_entities(content, sf_file.name)
        analysis["entities_found"].extend(entities)
        
        # Extract financial amounts
        amounts = extract_financial_amounts(content, sf_file.name)
        analysis["financial_amounts"].extend(amounts)
        
        # Extract dates
        dates = extract_dates(content, sf_file.name)
        analysis["dates_found"].extend(dates)
        
        # Extract relations
        relations = extract_relations(content, sf_file.name)
        analysis["relations_found"].extend(relations)
        
        # Extract events
        events = extract_events(content, sf_file.name)
        analysis["events_found"].extend(events)
        
        # Summary
        analysis["evidence_summary"][sf_file.name] = {
            "entities": len(entities),
            "amounts": len(amounts),
            "dates": len(dates),
            "relations": len(relations),
            "events": len(events),
            "content_length": len(content)
        }
    
    return analysis

def extract_entities(content, source):
    """Extract entity mentions from evidence"""
    entities = []
    
    # Common entity patterns
    patterns = {
        "PERSON": [
            r"Peter\s+(?:Andrew\s+)?Faucitt",
            r"Rynette\s+Farrar",
            r"Jacqueline\s+Faucitt",
            r"Daniel\s+(?:James\s+)?Faucitt",
            r"Danie\s+Bantjies",
            r"Kayla\s+Pretorius",
            r"Linda",
            r"Bernadine\s+Wright",
            r"Adv\.\s+\w+\s+\w+",
        ],
        "ORG": [
            r"RegimA\s+(?:Worldwide\s+Distribution)?(?:\s+\(Pty\)\s+Ltd)?",
            r"Strategic\s+Logistics",
            r"Villa\s+Via",
            r"Bantjies\s+(?:Inc)?",
            r"Adderory",
            r"SARS",
            r"South\s+African\s+Revenue\s+Service",
            r"ENS\s+Africa",
            r"Shopify",
            r"CIPC",
        ],
        "BANK": [
            r"(?:Standard\s+Bank|FNB|ABSA|Nedbank|Capitec)",
        ]
    }
    
    for entity_type, pattern_list in patterns.items():
        for pattern in pattern_list:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                entities.append({
                    "type": entity_type,
                    "name": match.group(0),
                    "source": source,
                    "context": content[max(0, match.start()-50):min(len(content), match.end()+50)]
                })
    
    return entities

def extract_financial_amounts(content, source):
    """Extract financial amounts from evidence"""
    amounts = []
    
    # Pattern for South African Rand amounts
    patterns = [
        r"R\s*[\d,]+(?:\.\d{2})?",
        r"ZAR\s*[\d,]+(?:\.\d{2})?",
        r"[\d,]+(?:\.\d{2})?\s*(?:Rand|rand)",
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            amount_str = match.group(0)
            # Clean and convert
            clean_amount = re.sub(r'[^\d.]', '', amount_str)
            try:
                amount_value = float(clean_amount)
                amounts.append({
                    "amount": amount_value,
                    "formatted": amount_str,
                    "source": source,
                    "context": content[max(0, match.start()-100):min(len(content), match.end()+100)]
                })
            except ValueError:
                pass
    
    return amounts

def extract_dates(content, source):
    """Extract dates from evidence"""
    dates = []
    
    # Date patterns
    patterns = [
        r"\d{4}-\d{2}-\d{2}",
        r"\d{2}/\d{2}/\d{4}",
        r"\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}",
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            dates.append({
                "date": match.group(0),
                "source": source,
                "context": content[max(0, match.start()-50):min(len(content), match.end()+50)]
            })
    
    return dates

def extract_relations(content, source):
    """Extract entity relations from evidence"""
    relations = []
    
    # Relation patterns
    relation_patterns = [
        (r"(\w+(?:\s+\w+)*)\s+(?:owes|owed|debt to|indebted to)\s+(\w+(?:\s+\w+)*)", "DEBT"),
        (r"(\w+(?:\s+\w+)*)\s+(?:controls|controlled|manages|managed)\s+(\w+(?:\s+\w+)*)", "CONTROL"),
        (r"(\w+(?:\s+\w+)*)\s+(?:director of|trustee of|member of)\s+(\w+(?:\s+\w+)*)", "FIDUCIARY"),
        (r"(\w+(?:\s+\w+)*)\s+(?:employed by|works for|employee of)\s+(\w+(?:\s+\w+)*)", "EMPLOYMENT"),
        (r"(\w+(?:\s+\w+)*)\s+(?:transferred|paid|sent)\s+.*\s+to\s+(\w+(?:\s+\w+)*)", "TRANSFER"),
    ]
    
    for pattern, relation_type in relation_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            relations.append({
                "from_entity": match.group(1),
                "to_entity": match.group(2),
                "relation_type": relation_type,
                "source": source,
                "context": match.group(0)
            })
    
    return relations

def extract_events(content, source):
    """Extract timeline events from evidence"""
    events = []
    
    # Event patterns (date + action)
    event_patterns = [
        r"(?:On|on)\s+(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{1,2}\s+\w+\s+\d{4})[,:]?\s+([^.]+\.)",
        r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}):\s+([^.]+\.)",
    ]
    
    for pattern in event_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            events.append({
                "date": match.group(1),
                "description": match.group(2),
                "source": source,
                "context": match.group(0)
            })
    
    return events

def main():
    print("=" * 80)
    print("COMPREHENSIVE REFINEMENT ANALYSIS - 2025-12-19")
    print("=" * 80)
    
    # Analyze evidence
    print("\n[1/5] Analyzing evidence files from ad-res-j7...")
    analysis = analyze_evidence_files()
    
    # Save analysis results
    output_file = REVSTREAM_ROOT / "COMPREHENSIVE_ANALYSIS_2025_12_19.json"
    save_json(output_file, analysis)
    print(f"\n✓ Analysis saved to: {output_file}")
    
    # Print summary
    print("\n" + "=" * 80)
    print("ANALYSIS SUMMARY")
    print("=" * 80)
    print(f"Total entities found: {len(analysis['entities_found'])}")
    print(f"Total financial amounts: {len(analysis['financial_amounts'])}")
    print(f"Total dates found: {len(analysis['dates_found'])}")
    print(f"Total relations found: {len(analysis['relations_found'])}")
    print(f"Total events found: {len(analysis['events_found'])}")
    
    print("\n" + "=" * 80)
    print("EVIDENCE FILE SUMMARY")
    print("=" * 80)
    for filename, summary in analysis["evidence_summary"].items():
        print(f"\n{filename}:")
        for key, value in summary.items():
            print(f"  {key}: {value}")
    
    # Top financial amounts
    if analysis['financial_amounts']:
        print("\n" + "=" * 80)
        print("TOP 10 FINANCIAL AMOUNTS")
        print("=" * 80)
        sorted_amounts = sorted(analysis['financial_amounts'], key=lambda x: x['amount'], reverse=True)
        for i, amount in enumerate(sorted_amounts[:10], 1):
            print(f"{i}. {amount['formatted']} (R {amount['amount']:,.2f}) - {amount['source']}")
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
