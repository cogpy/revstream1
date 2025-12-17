#!/usr/bin/env python3
"""
Comprehensive Analysis and Refinement Script
Date: 2025-12-17
Purpose: Analyze and refine entities, relations, events, and timelines with ad-res-j7 evidence
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

class ComprehensiveAnalyzer:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.revstream_path = Path("/home/ubuntu/revstream1")
        self.ad_res_j7_path = Path("/home/ubuntu/ad-res-j7")
        
        # Load current data models
        self.entities = self.load_json(self.revstream_path / "data_models/entities/entities.json")
        self.relations = self.load_json(self.revstream_path / "data_models/relations/relations.json")
        self.events = self.load_json(self.revstream_path / "data_models/events/events.json")
        self.timeline = self.load_json(self.revstream_path / "data_models/timelines/timeline.json")
        
        # Analysis results
        self.gaps = defaultdict(list)
        self.improvements = defaultdict(list)
        self.evidence_mapping = defaultdict(list)
        
    def load_json(self, filepath):
        """Load JSON file"""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return {}
    
    def save_json(self, data, filepath):
        """Save JSON file"""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def analyze_entities(self):
        """Analyze entities for gaps and improvements"""
        print("\n=== Analyzing Entities ===")
        
        entities = self.entities.get('entities', {})
        persons = entities.get('persons', [])
        organizations = entities.get('organizations', [])
        
        # Check for missing evidence references
        for person in persons:
            entity_id = person.get('entity_id')
            name = person.get('name')
            evidence = person.get('evidence', [])
            ad_res_refs = person.get('ad_res_j7_references', [])
            
            if not ad_res_refs:
                self.gaps['entities'].append({
                    'entity_id': entity_id,
                    'name': name,
                    'issue': 'Missing ad_res_j7_references',
                    'severity': 'medium'
                })
            
            # Check evidence strength assessment
            if 'evidence_strength' not in person:
                self.gaps['entities'].append({
                    'entity_id': entity_id,
                    'name': name,
                    'issue': 'Missing evidence_strength assessment',
                    'severity': 'high'
                })
            
            # Check criminal threshold assessment
            if person.get('agent_type') == 'antagonist' and 'criminal_threshold' not in person:
                self.gaps['entities'].append({
                    'entity_id': entity_id,
                    'name': name,
                    'issue': 'Missing criminal_threshold for antagonist',
                    'severity': 'high'
                })
        
        # Check organizations
        for org in organizations:
            entity_id = org.get('entity_id')
            name = org.get('name')
            
            if 'ad_res_j7_references' not in org:
                self.gaps['entities'].append({
                    'entity_id': entity_id,
                    'name': name,
                    'issue': 'Missing ad_res_j7_references',
                    'severity': 'medium'
                })
        
        print(f"Found {len(self.gaps['entities'])} entity gaps")
        return self.gaps['entities']
    
    def analyze_relations(self):
        """Analyze relations for gaps and improvements"""
        print("\n=== Analyzing Relations ===")
        
        relations = self.relations.get('relations', {})
        
        for rel_type, rel_list in relations.items():
            for rel in rel_list:
                rel_id = rel.get('relation_id')
                
                # Check for evidence verification
                if 'evidence_verified' not in rel:
                    self.gaps['relations'].append({
                        'relation_id': rel_id,
                        'relation_type': rel_type,
                        'issue': 'Missing evidence_verified timestamp',
                        'severity': 'low'
                    })
                
                # Check for ad_res_j7 evidence
                if 'ad_res_j7_evidence' not in rel:
                    self.gaps['relations'].append({
                        'relation_id': rel_id,
                        'relation_type': rel_type,
                        'issue': 'Missing ad_res_j7_evidence',
                        'severity': 'medium'
                    })
        
        print(f"Found {len(self.gaps['relations'])} relation gaps")
        return self.gaps['relations']
    
    def analyze_timeline(self):
        """Analyze timeline for gaps and improvements"""
        print("\n=== Analyzing Timeline ===")
        
        entries = self.timeline.get('entries', [])
        critical_dates = self.timeline.get('critical_evidence_dates', {})
        
        # Check for missing burden of proof assessments
        for entry in entries:
            event_id = entry.get('event_id')
            date = entry.get('date')
            
            if 'burden_of_proof' not in entry:
                self.gaps['timeline'].append({
                    'event_id': event_id,
                    'date': date,
                    'issue': 'Missing burden_of_proof assessment',
                    'severity': 'high'
                })
            
            if 'evidence' not in entry or not entry.get('evidence'):
                self.gaps['timeline'].append({
                    'event_id': event_id,
                    'date': date,
                    'issue': 'Missing evidence references',
                    'severity': 'high'
                })
        
        # Suggest new critical dates from ad-res-j7
        self.improvements['timeline'].append({
            'type': 'critical_dates_expansion',
            'suggestion': 'Add critical dates from SF evidence files (SF1-SF8)',
            'priority': 'high'
        })
        
        print(f"Found {len(self.gaps['timeline'])} timeline gaps")
        return self.gaps['timeline']
    
    def analyze_events(self):
        """Analyze events for gaps and improvements"""
        print("\n=== Analyzing Events ===")
        
        events = self.events.get('events', [])
        
        for event in events:
            event_id = event.get('event_id')
            
            # Check for evidence strength
            if 'evidence_strength' not in event:
                self.gaps['events'].append({
                    'event_id': event_id,
                    'issue': 'Missing evidence_strength',
                    'severity': 'medium'
                })
            
            # Check for burden of proof
            if 'burden_of_proof' not in event:
                self.gaps['events'].append({
                    'event_id': event_id,
                    'issue': 'Missing burden_of_proof',
                    'severity': 'high'
                })
        
        print(f"Found {len(self.gaps['events'])} event gaps")
        return self.gaps['events']
    
    def scan_ad_res_j7_evidence(self):
        """Scan ad-res-j7 for new evidence"""
        print("\n=== Scanning ad-res-j7 Evidence ===")
        
        annexures_path = self.ad_res_j7_path / "ANNEXURES"
        
        if not annexures_path.exists():
            print(f"Warning: {annexures_path} does not exist")
            return
        
        # Scan for SF files
        sf_files = []
        for item in annexures_path.iterdir():
            if item.name.startswith('SF') and item.is_file():
                sf_files.append(item.name)
        
        print(f"Found {len(sf_files)} SF evidence files: {sf_files}")
        
        # Scan for JF directories
        jf_dirs = []
        for item in annexures_path.iterdir():
            if item.name.startswith('JF') and item.is_dir():
                jf_dirs.append(item.name)
        
        print(f"Found {len(jf_dirs)} JF evidence directories: {jf_dirs}")
        
        self.evidence_mapping['sf_files'] = sf_files
        self.evidence_mapping['jf_directories'] = jf_dirs
        
        return self.evidence_mapping
    
    def generate_improvement_recommendations(self):
        """Generate comprehensive improvement recommendations"""
        print("\n=== Generating Improvement Recommendations ===")
        
        recommendations = {
            'timestamp': self.timestamp,
            'summary': {
                'total_gaps': sum(len(v) for v in self.gaps.values()),
                'entities_gaps': len(self.gaps['entities']),
                'relations_gaps': len(self.gaps['relations']),
                'events_gaps': len(self.gaps['events']),
                'timeline_gaps': len(self.gaps['timeline'])
            },
            'gaps': dict(self.gaps),
            'improvements': dict(self.improvements),
            'evidence_mapping': dict(self.evidence_mapping),
            'priority_actions': []
        }
        
        # Priority 1: Add burden of proof assessments
        recommendations['priority_actions'].append({
            'priority': 1,
            'action': 'Add burden_of_proof assessments to all timeline events',
            'affected_items': len([g for g in self.gaps['timeline'] if 'burden_of_proof' in g.get('issue', '')]),
            'rationale': 'Critical for legal filing refinement (50% civil / 95% criminal thresholds)'
        })
        
        # Priority 2: Add evidence strength assessments
        recommendations['priority_actions'].append({
            'priority': 2,
            'action': 'Add evidence_strength assessments to all entities',
            'affected_items': len([g for g in self.gaps['entities'] if 'evidence_strength' in g.get('issue', '')]),
            'rationale': 'Essential for determining which claims meet evidentiary standards'
        })
        
        # Priority 3: Cross-reference with ad-res-j7
        recommendations['priority_actions'].append({
            'priority': 3,
            'action': 'Cross-reference all entities/events with ad-res-j7 evidence',
            'affected_items': len([g for g in self.gaps['entities'] if 'ad_res_j7' in g.get('issue', '')]),
            'rationale': 'Ensures comprehensive evidence trail for all claims'
        })
        
        # Priority 4: Update GitHub Pages
        recommendations['priority_actions'].append({
            'priority': 4,
            'action': 'Update GitHub Pages with clear evidence references',
            'rationale': 'Improves accessibility and organization of evidence for legal review'
        })
        
        return recommendations
    
    def run_full_analysis(self):
        """Run complete analysis"""
        print("=" * 80)
        print("COMPREHENSIVE ANALYSIS AND REFINEMENT")
        print(f"Timestamp: {self.timestamp}")
        print("=" * 80)
        
        # Run all analyses
        self.analyze_entities()
        self.analyze_relations()
        self.analyze_events()
        self.analyze_timeline()
        self.scan_ad_res_j7_evidence()
        
        # Generate recommendations
        recommendations = self.generate_improvement_recommendations()
        
        # Save results
        output_file = self.revstream_path / f"COMPREHENSIVE_ANALYSIS_REFINEMENT_{datetime.now().strftime('%Y_%m_%d')}.json"
        self.save_json(recommendations, output_file)
        
        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE")
        print(f"Results saved to: {output_file}")
        print("=" * 80)
        
        # Print summary
        print("\n=== SUMMARY ===")
        print(f"Total Gaps Found: {recommendations['summary']['total_gaps']}")
        print(f"  - Entities: {recommendations['summary']['entities_gaps']}")
        print(f"  - Relations: {recommendations['summary']['relations_gaps']}")
        print(f"  - Events: {recommendations['summary']['events_gaps']}")
        print(f"  - Timeline: {recommendations['summary']['timeline_gaps']}")
        
        print("\n=== PRIORITY ACTIONS ===")
        for action in recommendations['priority_actions']:
            print(f"\nPriority {action['priority']}: {action['action']}")
            if 'affected_items' in action:
                print(f"  Affected Items: {action['affected_items']}")
            print(f"  Rationale: {action['rationale']}")
        
        return recommendations

if __name__ == "__main__":
    analyzer = ComprehensiveAnalyzer()
    results = analyzer.run_full_analysis()
