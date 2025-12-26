#!/usr/bin/env python3
"""
Extract key evidence from parsed emails
Create structured evidence database
Date: 2025-11-19
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def load_parsed_emails():
    """Load parsed email data"""
    with open('/home/ubuntu/revstream1/TODO-SEARCH/parsed_output/all_emails_parsed.json', 'r') as f:
        return json.load(f)

def extract_daniel_response_evidence(emails):
    """Extract Daniel's detailed response from Bantjes email thread"""
    evidence = []
    
    for email in emails:
        if 'Computer Expense analysis' in email['filename']:
            # This is Daniel's comprehensive response
            evidence_item = {
                'type': 'email_thread',
                'subject': 'The RegimA Group results and Computer Expense analysis',
                'date': '2025-06-10',
                'participants': ['Danie Bantjes', 'Daniel Faucitt', 'Peter Faucitt', 'Jacqui Faucitt'],
                'key_claims': [
                    {
                        'claim': 'Kayla murdered August 2023',
                        'context': 'Cards expired 2 weeks after Kayla\'s murder in Aug 2023',
                        'significance': 'Timeline of financial control shift'
                    },
                    {
                        'claim': 'Emergency measure - expenses on Worldwide cards',
                        'context': 'RegimA Skin Treatments and Strategic have no record of computer expenses',
                        'significance': 'Explains expense allocation irregularities'
                    },
                    {
                        'claim': 'ReZonance made first annual profit Feb 2023',
                        'context': 'Kayla and Daniel celebrated after decade of work',
                        'significance': 'Establishes ReZonance value before fraud'
                    },
                    {
                        'claim': 'ReZonance owes Daniel ZAR 1.8 million',
                        'context': 'Director loans from investments over the years',
                        'significance': 'Financial motive to preserve company'
                    },
                    {
                        'claim': 'Pete insisted Daniel close ReZonance',
                        'context': 'Daniel firmly rejected this demand',
                        'significance': 'Conflict over company control'
                    },
                    {
                        'claim': 'Murder investigation - freeze all activity',
                        'context': 'Authorities instructed freeze while investigating',
                        'significance': 'Legal justification for account freeze'
                    },
                    {
                        'claim': 'Worldwide absorbed 4 distribution partners overhead (2020-2023)',
                        'context': 'Daniel single-handedly rebuilt demand side',
                        'significance': 'Explains revenue/expense growth'
                    },
                    {
                        'claim': 'Rynette took all payments into account only she has access to',
                        'context': 'Denied Daniel visibility while leaving expenses with him',
                        'significance': 'Financial control and liability manipulation'
                    },
                    {
                        'claim': 'Rynette is neither director nor employee of Worldwide',
                        'context': 'Yet has complete control without liability',
                        'significance': 'Illegal control structure'
                    },
                    {
                        'claim': 'Turnover increase: 2M → 12M → 19M',
                        'context': 'Reflects additional distribution activity',
                        'significance': 'Business growth under Daniel\'s management'
                    },
                    {
                        'claim': 'Drop to 18M after Pete became administrator',
                        'context': 'Pete signed affidavit, unhooked automations',
                        'significance': 'Revenue decline after Pete took control'
                    },
                    {
                        'claim': 'Pete and Rynette broke automations despite warning',
                        'context': 'Daniel warned not to touch or it would break',
                        'significance': 'Deliberate sabotage'
                    },
                    {
                        'claim': 'Bank contacted Daniel about Pete/Rynette mandate changes',
                        'context': 'Attempted to change ownership, close accounts, cancel cards',
                        'significance': 'Unauthorized control attempts'
                    },
                    {
                        'claim': 'Daniel informed bank these were errors',
                        'context': 'All without Daniel\'s knowledge or consent',
                        'significance': 'Fraudulent banking instructions'
                    },
                    {
                        'claim': 'ReZonance invoices with 10% mark-up',
                        'context': 'Itemized billing with R50 processing fee',
                        'significance': 'Legitimate service fee structure'
                    },
                    {
                        'claim': 'After Aug 2023 all allocated to FNB auto feed',
                        'context': 'No more itemized ReZonance invoices',
                        'significance': 'Loss of proper accounting after Kayla\'s death'
                    },
                    {
                        'claim': 'RegimA SA and Zone use trust accounts',
                        'context': 'Structured to prevent Pete taking revenue',
                        'significance': 'Protection against theft (like with Kachan)'
                    },
                    {
                        'claim': 'Pete did to Kachan what he\'s doing to Daniel',
                        'context': 'Simply taking revenue by instructing payments to another account',
                        'significance': 'Pattern of theft behavior'
                    },
                    {
                        'claim': 'Moving assets between companies is theft',
                        'context': 'Different ownership structures, not subsidiaries',
                        'significance': 'Legal definition of fraud'
                    },
                    {
                        'claim': 'Outstanding R1M+ owed to ReZonance (Feb 2023)',
                        'context': 'RegimA Skin Treatments debt to ReZonance',
                        'significance': 'Unpaid legitimate debt'
                    },
                    {
                        'claim': 'Rynette made debt disappear in 2024',
                        'context': 'Misallocated GoDaddy payments as ReZonance payments',
                        'significance': 'Fraudulent accounting'
                    },
                    {
                        'claim': 'ReZonance never received the payments',
                        'context': 'Amounts still outstanding despite allocation',
                        'significance': 'Provable fraud - money trail mismatch'
                    },
                    {
                        'claim': 'Will flag as fraudulent with SARS',
                        'context': 'Mismatch between companies\' records',
                        'significance': 'Tax fraud implications'
                    },
                    {
                        'claim': 'Pete never seen actual accounts',
                        'context': 'Nor has Jacqui, nor has Daniel',
                        'significance': 'Rynette has exclusive access'
                    },
                    {
                        'claim': 'Accounts exist solely on Rynette\'s computer',
                        'context': 'Nobody else able to see them',
                        'significance': 'Complete financial control by non-director'
                    },
                    {
                        'claim': 'Amounts going through Strategic and RST seem off the charts',
                        'context': 'Need internal audit with extreme urgency',
                        'significance': 'Suspected massive fraud'
                    }
                ],
                'bantjes_response': {
                    'date': '2025-06-10',
                    'tone': 'Dismissive',
                    'action': 'Away for 2 weeks, little/no access to communications',
                    'significance': 'Avoids addressing Daniel\'s detailed evidence'
                },
                'smoking_gun_evidence': [
                    'Rynette controls all accounts despite not being director/employee',
                    'Rynette made R1M+ debt disappear through fraudulent allocation',
                    'Pete attempted unauthorized banking changes',
                    'Pattern of theft (Kachan precedent)',
                    'Accounts exist only on Rynette\'s computer',
                    'ReZonance never received payments allocated to it'
                ]
            }
            evidence.append(evidence_item)
    
    return evidence

def extract_sage_control_evidence(emails):
    """Extract Sage system control evidence"""
    evidence = []
    
    for email in emails:
        if 'Sage' in email['filename'] and 'Pete@regima.com' in email['filename']:
            evidence_item = {
                'type': 'system_control',
                'subject': 'Sage - Rynette using Pete@regima.com',
                'date': '2025-08-29',
                'from': 'Daniel Faucitt',
                'to': ['smunga@ensafrica.com', 'jfaucitt@proton.me'],
                'attachments': [
                    'Screenshot-2025-06-20-Sage-Account-RegimA-Worldwide-Distribution.jpg',
                    'Screenshot-2025-08-25-Sage-Account-RegimA-Worldwide-Distribution.jpg'
                ],
                'evidence_type': 'Email control proof',
                'significance': 'Direct evidence Rynette has access to Pete@regima.com',
                'legal_impact': 'Proves unauthorized email access and impersonation'
            }
            evidence.append(evidence_item)
    
    return evidence

def extract_popia_violation_evidence(emails):
    """Extract POPIA violation evidence"""
    evidence = []
    
    for email in emails:
        if 'POPIA' in email['filename']:
            evidence_item = {
                'type': 'legal_notice',
                'subject': 'POPIA Violation Notice',
                'date_sent': '2025-07-08',
                'date_forwarded': '2025-08-29',
                'from': 'Daniel Faucitt',
                'to_original': 'Pete Faucitt',
                'to_forwarded': ['smunga@ensafrica.com', 'jfaucitt@proton.me'],
                'attachment': 'FORMAL NOTICE - CESSATION OF CRIMINAL INSTRUCTIONS.docx',
                'context': 'Pete instructed staff to use new system only accessible to him and Rynette; redirected revenue streams; audit trail disappeared',
                'significance': 'Formal legal notice of privacy violation and criminal instructions',
                'legal_impact': 'POPIA violation, evidence of revenue diversion'
            }
            evidence.append(evidence_item)
    
    return evidence

def extract_employment_evidence(emails):
    """Extract Rynette employment evidence"""
    evidence = []
    
    for email in emails:
        if 'OFFER OF EMPLOYMENT' in email['filename'] and 'RYNETTE' in email['filename']:
            evidence_item = {
                'type': 'employment_contract',
                'subject': 'Rynette Farrar Employment Offer',
                'date': '2020-03-19',
                'participants': ['Danie Bantjes', 'Pete Faucitt', 'Jacqui Faucitt', 'Bernadine Wright'],
                'start_date': '2020-04-14',
                'start_time': '7:30 AM',
                'notice_periods': {
                    'under_4_weeks': '1 week',
                    '4_weeks_to_1_year': '2 weeks',
                    'over_1_year': '4 weeks'
                },
                'context': 'Employment offer during COVID-19 pandemic; concerns about virus disruption',
                'bantjes_role': 'Drafted employment contract and advised on notice periods',
                'significance': 'Establishes Rynette as employee, not director; Bantjes involved in employment',
                'legal_impact': 'Rynette has no legal authority to control company finances as employee'
            }
            evidence.append(evidence_item)
    
    return evidence

def extract_financial_statements_evidence(emails):
    """Extract FNB statement evidence"""
    evidence = []
    
    for email in emails:
        if 'FNB Statement' in email['filename'] and 'REGIMA SA' in email['filename']:
            evidence_item = {
                'type': 'bank_statement',
                'subject': 'FNB Statement for RegimA SA (Pty) Ltd',
                'account_holder': 'REGIMA SA (PTY) LTD',
                'statement_dates': [],
                'sent_to': 'Kay Pretorius <kayp@rzo.io>',
                'forwarded_to': 'Jacqui Faucitt',
                'significance': 'Bank statements for RegimA SA entity',
                'note': 'Statements sent to kayp@rzo.io (likely Daniel\'s team member)'
            }
            
            if '2025-03-06' in email['filename']:
                evidence_item['statement_dates'].append('2025-03-06')
            if '2025-07-27' in email['filename']:
                evidence_item['statement_dates'].append('2025-07-27')
            
            evidence.append(evidence_item)
    
    return evidence

def create_evidence_database():
    """Create comprehensive evidence database"""
    print("Loading parsed emails...")
    emails = load_parsed_emails()
    
    print("Extracting evidence...")
    
    evidence_db = {
        'metadata': {
            'extraction_date': datetime.now().strftime('%Y-%m-%d'),
            'total_emails_analyzed': len(emails),
            'evidence_categories': 6
        },
        'daniel_comprehensive_response': extract_daniel_response_evidence(emails),
        'sage_system_control': extract_sage_control_evidence(emails),
        'popia_violation': extract_popia_violation_evidence(emails),
        'employment_contracts': extract_employment_evidence(emails),
        'bank_statements': extract_financial_statements_evidence(emails),
        'summary': {
            'smoking_gun_count': 0,
            'high_priority_evidence': 0,
            'financial_fraud_evidence': 0,
            'system_control_evidence': 0,
            'legal_violations': 0
        }
    }
    
    # Count evidence
    evidence_db['summary']['smoking_gun_count'] = len(evidence_db['daniel_comprehensive_response'])
    evidence_db['summary']['system_control_evidence'] = len(evidence_db['sage_system_control'])
    evidence_db['summary']['legal_violations'] = len(evidence_db['popia_violation'])
    evidence_db['summary']['high_priority_evidence'] = (
        len(evidence_db['daniel_comprehensive_response']) +
        len(evidence_db['sage_system_control']) +
        len(evidence_db['popia_violation'])
    )
    
    return evidence_db

def main():
    print("=" * 80)
    print("KEY EVIDENCE EXTRACTION")
    print("Date: 2025-11-19")
    print("=" * 80)
    print()
    
    evidence_db = create_evidence_database()
    
    # Save evidence database
    output_path = Path('/home/ubuntu/revstream1/TODO-SEARCH/parsed_output')
    with open(output_path / 'evidence_database.json', 'w') as f:
        json.dump(evidence_db, f, indent=2)
    
    print("\n" + "=" * 80)
    print("EVIDENCE EXTRACTION SUMMARY")
    print("=" * 80)
    print(f"\nTotal emails analyzed: {evidence_db['metadata']['total_emails_analyzed']}")
    print(f"Evidence categories: {evidence_db['metadata']['evidence_categories']}")
    print(f"\nEvidence extracted:")
    print(f"  - Daniel's comprehensive response: {len(evidence_db['daniel_comprehensive_response'])} items")
    print(f"  - Sage system control: {len(evidence_db['sage_system_control'])} items")
    print(f"  - POPIA violations: {len(evidence_db['popia_violation'])} items")
    print(f"  - Employment contracts: {len(evidence_db['employment_contracts'])} items")
    print(f"  - Bank statements: {len(evidence_db['bank_statements'])} items")
    
    print(f"\nSummary:")
    print(f"  - Smoking gun evidence: {evidence_db['summary']['smoking_gun_count']}")
    print(f"  - High priority evidence: {evidence_db['summary']['high_priority_evidence']}")
    print(f"  - System control evidence: {evidence_db['summary']['system_control_evidence']}")
    print(f"  - Legal violations: {evidence_db['summary']['legal_violations']}")
    
    # Print key claims from Daniel's response
    if evidence_db['daniel_comprehensive_response']:
        print("\n" + "=" * 80)
        print("KEY CLAIMS FROM DANIEL'S COMPREHENSIVE RESPONSE")
        print("=" * 80)
        for item in evidence_db['daniel_comprehensive_response']:
            print(f"\nTotal claims: {len(item['key_claims'])}")
            print("\nTop 10 smoking gun claims:")
            for i, claim in enumerate(item['smoking_gun_evidence'][:10], 1):
                print(f"  {i}. {claim}")
    
    print("\n" + "=" * 80)
    print("EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"\nOutput saved to: {output_path / 'evidence_database.json'}")

if __name__ == '__main__':
    main()
