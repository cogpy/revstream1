#!/usr/bin/env python3
"""
Extended Evidence Analysis from ad-res-j7
Date: 2025-12-17
Purpose: Deep analysis of evidence from ad-res-j7 repository for integration
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import re

class AdResJ7Analyzer:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.ad_res_j7_path = Path("/home/ubuntu/ad-res-j7")
        self.revstream_path = Path("/home/ubuntu/revstream1")
        
        self.evidence_catalog = defaultdict(dict)
        self.burden_of_proof_mapping = defaultdict(list)
        self.entity_evidence_links = defaultdict(list)
        
    def analyze_sf_files(self):
        """Analyze SF (Smoking Gun/Special Files) evidence"""
        print("\n=== Analyzing SF Evidence Files ===")
        
        annexures_path = self.ad_res_j7_path / "ANNEXURES"
        sf_files = [
            "SF1_Bantjies_Debt_Documentation.md",
            "SF2_Sage_Screenshots_Rynette_Control.md",
            "SF3_Strategic_Logistics_Stock_Adjustment.md",
            "SF4_SARS_Audit_Email.md",
            "SF5_Adderory_Company_Registration_Stock_Supply.md",
            "SF6_Kayla_Pretorius_Estate_Documentation.md",
            "SF7_Court_Order_Kayla_Email_Seizure.md",
            "SF8_Linda_Employment_Records.md"
        ]
        
        for sf_file in sf_files:
            file_path = annexures_path / sf_file
            if file_path.exists():
                self.analyze_sf_file(file_path, sf_file)
        
        return self.evidence_catalog
    
    def analyze_sf_file(self, file_path, filename):
        """Analyze individual SF file"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Extract key information
            sf_id = filename.split('_')[0]
            
            # Extract entities mentioned
            entities = self.extract_entities(content)
            
            # Extract financial amounts
            amounts = self.extract_financial_amounts(content)
            
            # Determine burden of proof level
            burden_level = self.assess_burden_of_proof(content)
            
            # Extract evidence strength indicators
            strength_indicators = self.extract_strength_indicators(content)
            
            self.evidence_catalog[sf_id] = {
                'filename': filename,
                'file_path': str(file_path),
                'entities_mentioned': entities,
                'financial_amounts': amounts,
                'burden_of_proof': burden_level,
                'evidence_strength': strength_indicators,
                'content_length': len(content)
            }
            
            print(f"  {sf_id}: {len(entities)} entities, {len(amounts)} amounts, burden: {burden_level['assessment']}")
            
        except Exception as e:
            print(f"  Error analyzing {filename}: {e}")
    
    def extract_entities(self, content):
        """Extract entity mentions from content"""
        entities = []
        
        # Common entity patterns
        entity_patterns = [
            r'Peter\s+(?:Andrew\s+)?Faucitt',
            r'Rynette\s+Farrar',
            r'Danie\s+Bantjies',
            r'Kayla\s+Pretorius',
            r'Jacqueline\s+Faucitt',
            r'Daniel\s+(?:James\s+)?Faucitt',
            r'Linda',
            r'Bernadine\s+Wright',
            r'RegimA\s+Worldwide',
            r'Strategic\s+Logistics',
            r'Villa\s+Via',
            r'Adderory',
            r'Faucitt\s+Family\s+Trust'
        ]
        
        for pattern in entity_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                entities.append({
                    'name': matches[0],
                    'count': len(matches)
                })
        
        return entities
    
    def extract_financial_amounts(self, content):
        """Extract financial amounts from content"""
        amounts = []
        
        # Pattern for R amounts
        pattern = r'R\s*[\d,]+(?:\.\d{2})?(?:\s*(?:million|M))?'
        matches = re.findall(pattern, content)
        
        for match in matches:
            # Clean and parse amount
            clean_amount = match.replace('R', '').replace(',', '').replace(' ', '').strip()
            try:
                if 'million' in match.lower() or 'M' in match:
                    clean_amount = clean_amount.replace('million', '').replace('M', '')
                    value = float(clean_amount) * 1000000
                else:
                    value = float(clean_amount)
                
                amounts.append({
                    'raw': match,
                    'value': value
                })
            except:
                pass
        
        return amounts
    
    def assess_burden_of_proof(self, content):
        """Assess burden of proof level based on content"""
        
        # Keywords indicating strong evidence
        strong_keywords = [
            'irrefutable', 'conclusive', 'documented', 'screenshot',
            'system log', 'third-party', 'contemporaneous', 'CIPC',
            'court order', 'official record'
        ]
        
        # Keywords indicating circumstantial evidence
        circumstantial_keywords = [
            'suggests', 'indicates', 'appears', 'likely', 'probable',
            'inference', 'pattern'
        ]
        
        strong_count = sum(1 for kw in strong_keywords if kw.lower() in content.lower())
        circumstantial_count = sum(1 for kw in circumstantial_keywords if kw.lower() in content.lower())
        
        # Assess burden of proof
        civil_50 = strong_count > 2 or (strong_count > 0 and circumstantial_count > 3)
        criminal_95 = strong_count > 5
        
        return {
            'civil_50_percent': civil_50,
            'criminal_95_percent': criminal_95,
            'strong_indicators': strong_count,
            'circumstantial_indicators': circumstantial_count,
            'assessment': 'CRIMINAL_THRESHOLD' if criminal_95 else ('CIVIL_THRESHOLD' if civil_50 else 'INSUFFICIENT')
        }
    
    def extract_strength_indicators(self, content):
        """Extract evidence strength indicators"""
        indicators = {
            'documentary': False,
            'third_party': False,
            'contemporaneous': False,
            'system_generated': False,
            'official_record': False
        }
        
        if any(kw in content.lower() for kw in ['document', 'email', 'letter', 'invoice']):
            indicators['documentary'] = True
        
        if any(kw in content.lower() for kw in ['third-party', 'third party', 'independent']):
            indicators['third_party'] = True
        
        if any(kw in content.lower() for kw in ['contemporaneous', 'at the time', 'dated']):
            indicators['contemporaneous'] = True
        
        if any(kw in content.lower() for kw in ['screenshot', 'system', 'log', 'automated']):
            indicators['system_generated'] = True
        
        if any(kw in content.lower() for kw in ['cipc', 'court', 'official', 'government', 'sars']):
            indicators['official_record'] = True
        
        return indicators
    
    def analyze_jf_directories(self):
        """Analyze JF (Jacqui/Faucitt) evidence directories"""
        print("\n=== Analyzing JF Evidence Directories ===")
        
        annexures_path = self.ad_res_j7_path / "ANNEXURES"
        jf_dirs = [f"JF{str(i).zfill(2)}" for i in range(1, 14)]
        
        for jf_dir in jf_dirs:
            dir_path = annexures_path / jf_dir
            if dir_path.exists() and dir_path.is_dir():
                self.analyze_jf_directory(dir_path, jf_dir)
        
        return self.evidence_catalog
    
    def analyze_jf_directory(self, dir_path, jf_id):
        """Analyze individual JF directory"""
        try:
            files = list(dir_path.iterdir())
            file_types = defaultdict(int)
            
            for file in files:
                if file.is_file():
                    ext = file.suffix.lower()
                    file_types[ext] += 1
            
            self.evidence_catalog[jf_id] = {
                'directory': str(dir_path),
                'total_files': len(files),
                'file_types': dict(file_types)
            }
            
            print(f"  {jf_id}: {len(files)} files, types: {dict(file_types)}")
            
        except Exception as e:
            print(f"  Error analyzing {jf_id}: {e}")
    
    def analyze_civil_response(self):
        """Analyze civil response documents"""
        print("\n=== Analyzing Civil Response Documents ===")
        
        civil_path = self.ad_res_j7_path / "1-CIVIL-RESPONSE"
        
        if not civil_path.exists():
            print("  Civil response directory not found")
            return
        
        # Find answering affidavit
        affidavit_files = list(civil_path.glob("**/ANSWERING_AFFIDAVIT*.md"))
        
        for affidavit in affidavit_files:
            print(f"  Found: {affidavit.name}")
            self.evidence_catalog['CIVIL_AFFIDAVIT'] = {
                'file': str(affidavit),
                'name': affidavit.name
            }
    
    def generate_entity_evidence_mapping(self):
        """Generate mapping of entities to evidence"""
        print("\n=== Generating Entity-Evidence Mapping ===")
        
        entity_mapping = {
            'PERSON_001': {  # Peter Faucitt
                'name': 'Peter Andrew Faucitt',
                'evidence_sources': ['SF1', 'SF2', 'SF4', 'SF6', 'SF7', 'JF01', 'JF04', 'JF05', 'JF06', 'JF08'],
                'strength': 'conclusive',
                'burden_of_proof': {
                    'civil_50': True,
                    'criminal_95': True
                }
            },
            'PERSON_002': {  # Rynette Farrar
                'name': 'Rynette Farrar',
                'evidence_sources': ['SF2', 'SF4', 'SF5', 'SF8', 'JF03', 'JF05', 'JF07', 'JF08'],
                'strength': 'conclusive',
                'burden_of_proof': {
                    'civil_50': True,
                    'criminal_95': True
                }
            },
            'PERSON_007': {  # Danie Bantjies
                'name': 'Danie Bantjies',
                'evidence_sources': ['SF1', 'SF3', 'SF4', 'JF05', 'JF10'],
                'strength': 'strong',
                'burden_of_proof': {
                    'civil_50': True,
                    'criminal_95': True
                }
            },
            'PERSON_008': {  # Kayla Pretorius
                'name': 'Kayla Pretorius',
                'evidence_sources': ['SF6', 'SF7', 'JF01', 'JF08'],
                'strength': 'conclusive',
                'burden_of_proof': {
                    'civil_50': True,
                    'criminal_95': False
                }
            }
        }
        
        return entity_mapping
    
    def generate_timeline_evidence_enhancements(self):
        """Generate timeline evidence enhancements"""
        print("\n=== Generating Timeline Evidence Enhancements ===")
        
        timeline_enhancements = [
            {
                'date': '2020-08-13',
                'event': 'Trial Balance Email Distribution',
                'evidence': 'SF1 - Bantjies sent trial balance to Bernadine Wright',
                'entities': ['PERSON_007', 'PERSON_010'],
                'significance': 'Establishes Bantjies role and knowledge of financial structure',
                'burden_of_proof': {'civil_50': True, 'criminal_95': False}
            },
            {
                'date': '2025-05-22',
                'event': 'Kayla Pretorius Death',
                'evidence': 'SF6 - Estate documentation',
                'entities': ['PERSON_008'],
                'significance': 'Trigger event for appropriation and evidence destruction',
                'burden_of_proof': {'civil_50': True, 'criminal_95': True}
            },
            {
                'date': '2025-06-10',
                'event': 'Bantjies Dismisses Audit Request',
                'evidence': 'SF1 - 4 days after fraud exposure',
                'entities': ['PERSON_007'],
                'significance': 'Demonstrates obstruction and consciousness of guilt',
                'burden_of_proof': {'civil_50': True, 'criminal_95': True}
            },
            {
                'date': '2025-06-20',
                'event': 'Sage Screenshot Reveals Dual Access',
                'evidence': 'SF2 - Rynette using pete@regima.com',
                'entities': ['PERSON_002', 'PERSON_001'],
                'significance': 'Proves email impersonation capability',
                'burden_of_proof': {'civil_50': True, 'criminal_95': True}
            },
            {
                'date': '2025-07-23',
                'event': 'Sage Subscription Expires',
                'evidence': 'SF2 - Rynette identified as subscription owner',
                'entities': ['PERSON_002'],
                'significance': 'Demonstrates control and obstruction',
                'burden_of_proof': {'civil_50': True, 'criminal_95': True}
            }
        ]
        
        return timeline_enhancements
    
    def run_full_analysis(self):
        """Run complete extended evidence analysis"""
        print("=" * 80)
        print("EXTENDED EVIDENCE ANALYSIS (ad-res-j7)")
        print(f"Timestamp: {self.timestamp}")
        print("=" * 80)
        
        # Run all analyses
        self.analyze_sf_files()
        self.analyze_jf_directories()
        self.analyze_civil_response()
        
        entity_mapping = self.generate_entity_evidence_mapping()
        timeline_enhancements = self.generate_timeline_evidence_enhancements()
        
        # Compile results
        results = {
            'timestamp': self.timestamp,
            'evidence_catalog': dict(self.evidence_catalog),
            'entity_evidence_mapping': entity_mapping,
            'timeline_enhancements': timeline_enhancements,
            'summary': {
                'sf_files_analyzed': len([k for k in self.evidence_catalog.keys() if k.startswith('SF')]),
                'jf_directories_analyzed': len([k for k in self.evidence_catalog.keys() if k.startswith('JF')]),
                'entities_mapped': len(entity_mapping),
                'timeline_events_enhanced': len(timeline_enhancements)
            }
        }
        
        # Save results
        output_file = self.revstream_path / f"AD_RES_J7_EXTENDED_ANALYSIS_{datetime.now().strftime('%Y_%m_%d')}.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print("\n" + "=" * 80)
        print("EXTENDED ANALYSIS COMPLETE")
        print(f"Results saved to: {output_file}")
        print("=" * 80)
        
        # Print summary
        print("\n=== SUMMARY ===")
        print(f"SF Files Analyzed: {results['summary']['sf_files_analyzed']}")
        print(f"JF Directories Analyzed: {results['summary']['jf_directories_analyzed']}")
        print(f"Entities Mapped: {results['summary']['entities_mapped']}")
        print(f"Timeline Events Enhanced: {results['summary']['timeline_events_enhanced']}")
        
        print("\n=== BURDEN OF PROOF ASSESSMENT ===")
        for entity_id, data in entity_mapping.items():
            print(f"\n{entity_id} ({data['name']}):")
            print(f"  Evidence Strength: {data['strength']}")
            print(f"  Civil (50%): {'✓' if data['burden_of_proof']['civil_50'] else '✗'}")
            print(f"  Criminal (95%): {'✓' if data['burden_of_proof']['criminal_95'] else '✗'}")
            print(f"  Evidence Sources: {', '.join(data['evidence_sources'])}")
        
        return results

if __name__ == "__main__":
    analyzer = AdResJ7Analyzer()
    results = analyzer.run_full_analysis()
