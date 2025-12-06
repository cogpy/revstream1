#!/usr/bin/env python3
"""
Entity Refinement Script - Fix Bank Account Control Information
Date: 2025-12-06
"""

import json
from datetime import datetime

# Load entities
with open('data_models/entities/entities_refined_2025_12_05_v25.json', 'r') as f:
    entities_data = json.load(f)

# Update metadata
entities_data['metadata']['version'] = '26.0'
entities_data['metadata']['last_updated'] = '2025-12-06'
entities_data['metadata']['changes'] = 'Added controlled_by information to bank accounts, standardized phase naming (2025-12-06)'

# Fix bank account control information
bank_accounts = entities_data['entities'].get('bank_accounts', [])

for account in bank_accounts:
    account_number = account.get('account_number')
    
    # BANK_ACCOUNT_001: 62134839127 - RegimA Zone Ltd (Daniel's UK company)
    if account_number == '62134839127':
        account['controlled_by'] = 'PERSON_005'  # Daniel Faucitt
        account['legitimate_owner'] = 'ORG_003'  # RegimA Zone Ltd
        account['control_status'] = 'legitimate'
        if 'relationships' not in account:
            account['relationships'] = []
        if 'legitimately_controlled_by_PERSON_005' not in account['relationships']:
            account['relationships'].append('legitimately_controlled_by_PERSON_005')
    
    # BANK_ACCOUNT_002: 62812835744 - ReZonance (Pty) Ltd
    elif account_number == '62812835744':
        account['controlled_by'] = 'PERSON_001'  # Peter Faucitt (as director)
        account['legitimate_owner'] = 'ORG_008'  # ReZonance (Pty) Ltd
        account['control_status'] = 'disputed'
        account['control_notes'] = 'Peter as director, but used for unauthorized diversions'
        if 'relationships' not in account:
            account['relationships'] = []
        if 'controlled_by_PERSON_001' not in account['relationships']:
            account['relationships'].append('controlled_by_PERSON_001')
    
    # BANK_ACCOUNT_003: 62593375829 - Faucitt Family Trust
    elif account_number == '62593375829':
        account['controlled_by'] = 'PERSON_001'  # Peter Faucitt (as trustee)
        account['legitimate_owner'] = 'ORG_001'  # Faucitt Family Trust
        account['control_status'] = 'disputed'
        account['control_notes'] = 'Peter as trustee, but evidence of trust violations'
        if 'relationships' not in account:
            account['relationships'] = []
        if 'controlled_by_PERSON_001_as_trustee' not in account['relationships']:
            account['relationships'].append('controlled_by_PERSON_001_as_trustee')

# Save updated entities
output_file = 'data_models/entities/entities_refined_2025_12_06_v26.json'
with open(output_file, 'w') as f:
    json.dump(entities_data, f, indent=2)

print(f"✓ Entities refined and saved to: {output_file}")
print(f"✓ Updated {len(bank_accounts)} bank accounts with control information")
print(f"✓ Version: 26.0")
print(f"✓ Date: 2025-12-06")
