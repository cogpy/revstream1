#!/usr/bin/env python3
"""
Generate the Master Record for Exchanges (Exchanges.md).
System Dynamics Stocks & Flows - Financial movements and obligations.
"""

import json
from pathlib import Path
from datetime import datetime

REPO_DIR = Path("/home/ubuntu/revstream1")

def load_json(filepath):
    """Load a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def main():
    """Main function to generate the Exchanges.md file."""
    relations_path = REPO_DIR / "data_models/relations/relations.json"
    entities_path = REPO_DIR / "data_models/entities/entities.json"
    events_path = REPO_DIR / "data_models/events/events.json"
    
    relations_data = load_json(relations_path)
    entities_data = load_json(entities_path)
    events_data = load_json(events_path)
    
    output_path = REPO_DIR / "MR/Exchanges.md"
    
    md_content = []
    md_content.append("# Master Record: Exchanges")
    md_content.append("## System Dynamics Stocks & Flows")
    md_content.append("--- ")
    md_content.append(f"*Version: {relations_data['metadata']['version']}* ")
    md_content.append(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}* ")
    md_content.append("")
    
    # Section 1: Key Financial Stocks
    md_content.append("## 1. Key Financial Stocks (Accumulated Values)")
    md_content.append("")
    md_content.append("| Stock | Value | Holder | Status |")
    md_content.append("|---|---|---|---|")
    md_content.append("| **Ketoni Payout Obligation** | R18.75M | FFT (owed by Ketoni) | Pending (May 2026) |")
    md_content.append("| **Revenue Stream Hijacked** | R10,269,727.90 | Diverted from Daniel/Jacqui | Stolen |")
    md_content.append("| **Stock Adjustment Loss** | R5,400,000 | SLG (Strategic Logistics) | Disappeared |")
    md_content.append("| **ReZonance Misallocated** | R1,035,000 | RST (misallocated) | Disputed |")
    md_content.append("| **Ian Levitt Demand** | R63,000,000 | Ignored by Peter | Unresolved |")
    md_content.append("")
    
    # Section 2: Key Financial Flows
    md_content.append("## 2. Key Financial Flows (Transactions)")
    md_content.append("")
    
    # Extract events with financial impact
    financial_events = []
    for event in events_data['events']:
        impact = event.get('financial_impact', 0)
        if impact and impact != 0 and impact != "N/A":
            financial_events.append(event)
    
    md_content.append("| Date | Flow Description | Amount | From | To | Evidence |")
    md_content.append("|---|---|---|---|---|---|")
    
    for event in sorted(financial_events, key=lambda x: x.get('date', '9999'))[:30]:
        date = event.get('date', 'N/A')
        desc = event.get('title', event.get('description', 'N/A'))[:50]
        amount = event.get('financial_impact', 'N/A')
        entities = event.get('entities_involved', [])
        from_entity = entities[0] if len(entities) > 0 else 'N/A'
        to_entity = entities[1] if len(entities) > 1 else 'N/A'
        evidence = event.get('burden_of_proof', 'N/A')
        md_content.append(f"| {date} | {desc} | {amount} | {from_entity} | {to_entity} | {evidence} |")
    
    md_content.append("")
    
    # Section 3: Control Flows
    md_content.append("## 3. Control Flows (Power & Access)")
    md_content.append("")
    md_content.append("| Controller | Controls | Type | Status |")
    md_content.append("|---|---|---|---|")
    md_content.append("| **Rynette Farrar** | Sage Accounting System | Financial Control | Active |")
    md_content.append("| **Rynette Farrar** | Pete@regima.com email | Email Access | Active |")
    md_content.append("| **Rynette Farrar** | Bank Accounts | Account Control | Active |")
    md_content.append("| **Peter Faucitt** | FFT (as Trustee) | Fiduciary Control | Violated |")
    md_content.append("| **Bantjies** | FFT (as unlawful Trustee) | Fiduciary Control | Conflict |")
    md_content.append("| **Kevin Derrick** | Ketoni Investment Holdings | Ownership | Active |")
    md_content.append("| **Kevin Derrick** | The George Group (CEO) | Executive | Active |")
    md_content.append("| **Bantjies** | The George Group (CFO) | Executive | Active |")
    md_content.append("")
    
    # Section 4: Obligation Flows
    md_content.append("## 4. Obligation Flows (Debts & Duties)")
    md_content.append("")
    md_content.append("| Obligor | Obligee | Obligation | Amount | Due Date | Status |")
    md_content.append("|---|---|---|---|---|---|")
    md_content.append("| **Ketoni** | FFT | Investment Payout | R18.75M | May 2026 | Pending |")
    md_content.append("| **Peter** | Daniel | Revenue Share | R10.27M | Ongoing | Violated |")
    md_content.append("| **Peter** | Jacqui | Revenue Share | R10.27M | Ongoing | Violated |")
    md_content.append("| **Bantjies** | FFT Beneficiaries | Fiduciary Duty | N/A | Ongoing | Conflicted |")
    md_content.append("")
    
    # Section 5: Conflict of Interest Map
    md_content.append("## 5. Conflict of Interest Map")
    md_content.append("")
    md_content.append("```")
    md_content.append("THE GEORGE GROUP")
    md_content.append("├── CEO: Kevin Derrick ──────────┐")
    md_content.append("│                                │")
    md_content.append("└── CFO: Danie Bantjies          │")
    md_content.append("         │                       │")
    md_content.append("         │ Professional          │ Owns/Directs")
    md_content.append("         │ Loyalty               │")
    md_content.append("         ▼                       ▼")
    md_content.append("    ┌─────────┐           ┌─────────────────┐")
    md_content.append("    │ Bantjies│           │ KETONI          │")
    md_content.append("    │ Trustee │           │ Investment      │")
    md_content.append("    │ of FFT  │           │ Holdings        │")
    md_content.append("    └────┬────┘           └────────┬────────┘")
    md_content.append("         │                         │")
    md_content.append("         │ Fiduciary               │ Owes R18.75M")
    md_content.append("         │ Duty                    │")
    md_content.append("         ▼                         ▼")
    md_content.append("    ┌─────────────────────────────────────┐")
    md_content.append("    │     FAUCITT FAMILY TRUST (FFT)      │")
    md_content.append("    │  Beneficiaries: Daniel, Jacqui      │")
    md_content.append("    │  Payout Due: R18.75M (May 2026)     │")
    md_content.append("    └─────────────────────────────────────┘")
    md_content.append("```")
    md_content.append("")
    md_content.append("**CONFLICT:** Bantjies owes professional loyalty to Kevin Derrick (his CEO)")
    md_content.append("while simultaneously owing fiduciary duty to FFT beneficiaries.")
    md_content.append("Kevin Derrick owns Ketoni which owes R18.75M to FFT.")
    md_content.append("")

    with open(output_path, 'w') as f:
        f.write("\n".join(md_content))
    
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
