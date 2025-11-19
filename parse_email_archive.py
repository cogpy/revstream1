#!/usr/bin/env python3
"""
Parse 426 email text files from TODO-SEARCH folder
Extract entities, events, financial data, and relations
Date: 2025-11-19
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

class EmailParser:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.emails = []
        self.entities = defaultdict(set)
        self.events = []
        self.financial_data = []
        self.relations = []
        
        # Known entities for matching
        self.known_persons = {
            'Peter Faucitt', 'Pete Faucitt', 'Peter Andrew Faucitt', 'P.A. Faucitt',
            'Rynette Farrar', 'Rynette', 
            'Daniel Faucitt', 'Danny Faucitt', 'D.J. Faucitt',
            'Jacqui Faucitt', 'Jacqueline Faucitt',
            'Danie Bantjes', 'Danie',
            'Marisca Meyer',
            'Linda Kruger',
            'Eldridge Davids',
            'Tracey Clark',
            'Kayla'
        }
        
        self.known_orgs = {
            'RegimA Worldwide Distribution', 'RegimA WWD',
            'RegimA SA', 'RegimaSA',
            'RegimA Africa', 'RegimA Zone',
            'RegimA Skin Treatments',
            'ReZonance', 'Rezonance',
            'Unicorn Dynamics',
            'Villa Via',
            'Strategic Logistics'
        }
        
        # Financial patterns
        self.amount_pattern = re.compile(r'R\s*[\d,]+(?:\.\d{2})?')
        self.date_pattern = re.compile(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}')
        
    def parse_email_file(self, filepath):
        """Parse a single email text file"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            email_data = {
                'filepath': str(filepath.relative_to(self.base_path)),
                'filename': filepath.name,
                'account': self.extract_account_from_path(filepath),
                'metadata': self.extract_metadata(content),
                'content': content,
                'entities_found': self.find_entities(content),
                'amounts_found': self.find_amounts(content),
                'dates_found': self.find_dates(content),
                'keywords': self.extract_keywords(content),
                'priority': self.assess_priority(filepath.name, content)
            }
            
            return email_data
            
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            return None
    
    def extract_account_from_path(self, filepath):
        """Extract email account from file path"""
        parts = filepath.parts
        if len(parts) >= 4:
            return f"{parts[-3]}/{parts[-2]}" if parts[-2] != parts[-3] else parts[-2]
        return "unknown"
    
    def extract_metadata(self, content):
        """Extract email metadata (From, To, Date, Subject)"""
        metadata = {}
        
        # Try to find From
        from_match = re.search(r'^From:\s*(.+?)$', content, re.MULTILINE | re.IGNORECASE)
        if from_match:
            metadata['from'] = from_match.group(1).strip()
        
        # Try to find To
        to_match = re.search(r'^To:\s*(.+?)$', content, re.MULTILINE | re.IGNORECASE)
        if to_match:
            metadata['to'] = to_match.group(1).strip()
        
        # Try to find Date
        date_match = re.search(r'^Date:\s*(.+?)$', content, re.MULTILINE | re.IGNORECASE)
        if date_match:
            metadata['date'] = date_match.group(1).strip()
        
        # Try to find Subject
        subject_match = re.search(r'^Subject:\s*(.+?)$', content, re.MULTILINE | re.IGNORECASE)
        if subject_match:
            metadata['subject'] = subject_match.group(1).strip()
        
        return metadata
    
    def find_entities(self, content):
        """Find known entities in content"""
        found = {'persons': [], 'organizations': []}
        
        for person in self.known_persons:
            if person.lower() in content.lower():
                found['persons'].append(person)
        
        for org in self.known_orgs:
            if org.lower() in content.lower():
                found['organizations'].append(org)
        
        return found
    
    def find_amounts(self, content):
        """Find financial amounts in content"""
        amounts = self.amount_pattern.findall(content)
        return [amt.strip() for amt in amounts]
    
    def find_dates(self, content):
        """Find dates in content"""
        dates = self.date_pattern.findall(content)
        return dates
    
    def extract_keywords(self, content):
        """Extract important keywords"""
        keywords = []
        
        important_terms = [
            'fraud', 'theft', 'unauthorized', 'illegal',
            'payment', 'transfer', 'invoice', 'statement',
            'sage', 'accounting', 'financial',
            'CIPC', 'registration', 'company',
            'trust', 'beneficiary', 'director',
            'email', 'access', 'password', 'account',
            'POPIA', 'violation', 'privacy',
            'overdrawn', 'debt', 'loan',
            'employment', 'salary', 'contract'
        ]
        
        content_lower = content.lower()
        for term in important_terms:
            if term in content_lower:
                keywords.append(term)
        
        return keywords
    
    def assess_priority(self, filename, content):
        """Assess priority level of email"""
        priority = 0
        
        # High priority filenames
        high_priority_terms = [
            'sage', 'rynette', 'pete@regima.com',
            'fnb statement', 'regima sa',
            'bantjes', 'computer expense',
            'popia', 'employment',
            'cipc', 'rezonance', 'unicorn'
        ]
        
        filename_lower = filename.lower()
        for term in high_priority_terms:
            if term in filename_lower:
                priority += 2
        
        # High priority content
        content_lower = content.lower()
        if 'r10m' in content_lower or 'r 10m' in content_lower:
            priority += 5
        if 'fraud' in content_lower or 'theft' in content_lower:
            priority += 3
        if 'unauthorized' in content_lower:
            priority += 2
        if 'pete@regima.com' in content_lower and 'rynette' in content_lower:
            priority += 5
        
        return priority
    
    def parse_all_emails(self):
        """Parse all email files in TODO-SEARCH folder"""
        txt_path = self.base_path / 'txt'
        
        if not txt_path.exists():
            print(f"Error: {txt_path} does not exist")
            return
        
        # Find all .txt files
        txt_files = list(txt_path.rglob('*.txt'))
        total = len(txt_files)
        
        print(f"Found {total} email text files")
        print("Parsing emails...")
        
        for i, filepath in enumerate(txt_files, 1):
            if i % 50 == 0:
                print(f"  Processed {i}/{total} files...")
            
            email_data = self.parse_email_file(filepath)
            if email_data:
                self.emails.append(email_data)
        
        print(f"Successfully parsed {len(self.emails)} emails")
    
    def categorize_emails(self):
        """Categorize emails by type and priority"""
        categories = {
            'high_priority': [],
            'financial': [],
            'legal': [],
            'sage_accounting': [],
            'company_registration': [],
            'employment': [],
            'banking': [],
            'rezonance_unicorn': [],
            'other': []
        }
        
        for email in self.emails:
            filename = email['filename'].lower()
            keywords = email['keywords']
            priority = email['priority']
            
            if priority >= 5:
                categories['high_priority'].append(email)
            
            if 'sage' in filename or 'sage' in keywords:
                categories['sage_accounting'].append(email)
            
            if 'fnb' in filename or 'statement' in filename or 'payment' in keywords:
                categories['financial'].append(email)
            
            if 'popia' in filename or 'legal' in filename or 'case' in filename:
                categories['legal'].append(email)
            
            if 'cipc' in filename or 'registration' in filename:
                categories['company_registration'].append(email)
            
            if 'employment' in filename or 'offer' in filename:
                categories['employment'].append(email)
            
            if 'bank' in filename or 'account' in filename or 'mandate' in filename:
                categories['banking'].append(email)
            
            if 'rezonance' in filename or 'unicorn' in filename:
                categories['rezonance_unicorn'].append(email)
            
            if not any(email in cat for cat in categories.values()):
                categories['other'].append(email)
        
        return categories
    
    def generate_summary(self):
        """Generate summary statistics"""
        summary = {
            'total_emails': len(self.emails),
            'emails_by_account': defaultdict(int),
            'high_priority_count': 0,
            'emails_with_amounts': 0,
            'total_amounts_found': 0,
            'emails_with_dates': 0,
            'top_keywords': defaultdict(int)
        }
        
        for email in self.emails:
            account = email['account']
            summary['emails_by_account'][account] += 1
            
            if email['priority'] >= 5:
                summary['high_priority_count'] += 1
            
            if email['amounts_found']:
                summary['emails_with_amounts'] += 1
                summary['total_amounts_found'] += len(email['amounts_found'])
            
            if email['dates_found']:
                summary['emails_with_dates'] += 1
            
            for keyword in email['keywords']:
                summary['top_keywords'][keyword] += 1
        
        # Convert defaultdicts to regular dicts for JSON serialization
        summary['emails_by_account'] = dict(summary['emails_by_account'])
        summary['top_keywords'] = dict(sorted(
            summary['top_keywords'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:20])
        
        return summary
    
    def save_results(self, output_dir):
        """Save parsing results to JSON files"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Save all emails
        with open(output_path / 'all_emails_parsed.json', 'w') as f:
            json.dump(self.emails, f, indent=2)
        
        # Save categorized emails
        categories = self.categorize_emails()
        with open(output_path / 'emails_categorized.json', 'w') as f:
            json.dump(categories, f, indent=2)
        
        # Save summary
        summary = self.generate_summary()
        with open(output_path / 'parsing_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Save high priority emails separately
        high_priority = [e for e in self.emails if e['priority'] >= 5]
        high_priority_sorted = sorted(high_priority, key=lambda x: x['priority'], reverse=True)
        with open(output_path / 'high_priority_emails.json', 'w') as f:
            json.dump(high_priority_sorted, f, indent=2)
        
        return summary, categories, high_priority_sorted

def main():
    print("=" * 80)
    print("EMAIL ARCHIVE PARSER")
    print("Date: 2025-11-19")
    print("=" * 80)
    print()
    
    base_path = Path('/home/ubuntu/revstream1/TODO-SEARCH')
    output_dir = Path('/home/ubuntu/revstream1/TODO-SEARCH/parsed_output')
    
    parser = EmailParser(base_path)
    
    # Parse all emails
    parser.parse_all_emails()
    
    # Save results
    print("\nSaving results...")
    summary, categories, high_priority = parser.save_results(output_dir)
    
    # Print summary
    print("\n" + "=" * 80)
    print("PARSING SUMMARY")
    print("=" * 80)
    print(f"\nTotal emails parsed: {summary['total_emails']}")
    print(f"High priority emails: {summary['high_priority_count']}")
    print(f"Emails with financial amounts: {summary['emails_with_amounts']}")
    print(f"Total amounts found: {summary['total_amounts_found']}")
    print(f"Emails with dates: {summary['emails_with_dates']}")
    
    print(f"\nEmails by account:")
    for account, count in sorted(summary['emails_by_account'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {account}: {count}")
    
    print(f"\nTop keywords:")
    for keyword, count in list(summary['top_keywords'].items())[:10]:
        print(f"  {keyword}: {count}")
    
    print(f"\nCategories:")
    for category, emails in categories.items():
        print(f"  {category}: {len(emails)}")
    
    print(f"\nTop 10 high priority emails:")
    for i, email in enumerate(high_priority[:10], 1):
        print(f"  {i}. [{email['priority']}] {email['filename']}")
    
    print("\n" + "=" * 80)
    print("PARSING COMPLETE")
    print("=" * 80)
    print(f"\nOutput saved to: {output_dir}")
    print(f"  - all_emails_parsed.json")
    print(f"  - emails_categorized.json")
    print(f"  - parsing_summary.json")
    print(f"  - high_priority_emails.json")

if __name__ == '__main__':
    main()
