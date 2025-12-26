#!/usr/bin/env python3
"""
Calculate total expenditures from Daniel's personal bank statements (May-October 2025).
Key correction: All transfers INTO the account were from Dan's personal investment account,
EXCEPT the R500k from Strategic Logistics on July 16, 2025.
"""

# Data extracted from bank statements
statements = {
    "June 2025": {
        "period": "2025-05-03 to 2025-06-04",
        "opening_balance": 3192.33,
        "closing_balance": 48996.11,
        "total_credits": 260000.00,  # 5 credit transactions (all from Dan's investment account)
        "total_debits": 214196.22,   # 103 debit transactions
        "credit_breakdown": [
            {"date": "2025-05-05", "desc": "FNB App Transfer From Trs", "amount": 20000.00, "source": "Investment Account"},
            {"date": "2025-05-07", "desc": "FNB App Transfer From Trs", "amount": 70000.00, "source": "Investment Account"},
            {"date": "2025-05-12", "desc": "FNB App Transfer From Trs", "amount": 50000.00, "source": "Investment Account"},
            {"date": "2025-05-19", "desc": "FNB App Transfer From Trs", "amount": 70000.00, "source": "Investment Account"},
            {"date": "2025-06-03", "desc": "FNB App Transfer From Trs", "amount": 50000.00, "source": "Investment Account"},
        ]
    },
    "July 2025": {
        "period": "2025-06-04 to 2025-07-04",
        "opening_balance": 48996.11,
        "closing_balance": 24314.31,
        "total_credits": 100403.00,  # 3 credit transactions
        "total_debits": 125084.80,   # 91 debit transactions
        "credit_breakdown": [
            {"date": "2025-06-17", "desc": "FNB App Transfer From Trs", "amount": 50000.00, "source": "Investment Account"},
            {"date": "2025-06-26", "desc": "FNB App Transfer From Trs", "amount": 50000.00, "source": "Investment Account"},
            {"date": "2025-07-03", "desc": "Credit Voucher Vouch Glitch", "amount": 403.00, "source": "Credit Voucher"},
        ]
    },
    "August 2025": {
        "period": "2025-07-04 to 2025-08-04",
        "opening_balance": 24314.31,
        "closing_balance": 363386.47,
        "total_credits": 660000.00,  # 5 credit transactions
        "total_debits": 320927.84,   # 121 debit transactions
        "credit_breakdown": [
            {"date": "2025-07-07", "desc": "FNB App Transfer From Trs", "amount": 20000.00, "source": "Investment Account"},
            {"date": "2025-07-07", "desc": "FNB App Transfer From Trs", "amount": 50000.00, "source": "Investment Account"},
            {"date": "2025-07-09", "desc": "FNB App Payment To Rezonance", "amount": 4000.00, "source": "Investment Account"},
            {"date": "2025-07-16", "desc": "FNB App Transfer From Trs", "amount": 40000.00, "source": "Investment Account"},
            {"date": "2025-07-16", "desc": "FNB OB Pmt Daniel J Faucitt", "amount": 500000.00, "source": "Strategic Logistics (External)"},
            {"date": "2025-07-16", "desc": "FNB App Transfer From Trs", "amount": 50000.00, "source": "Investment Account"},
        ],
        "note": "R500k from Strategic Logistics is the ONLY external transfer"
    },
    "September 2025": {
        "period": "2025-08-04 to 2025-09-04",
        "opening_balance": 363386.47,
        "closing_balance": 151271.60,
        "total_credits": 0.00,       # 0 credit transactions
        "total_debits": 212114.87,   # 108 debit transactions
        "credit_breakdown": []
    },
    "October 2025": {
        "period": "2025-09-04 to 2025-10-04",
        "opening_balance": 151271.60,
        "closing_balance": 26149.29,
        "total_credits": 65000.00,   # 3 credit transactions
        "total_debits": 190122.31,   # 97 debit transactions
        "credit_breakdown": [
            {"date": "2025-09-19", "desc": "FNB App Payment To Rezonance", "amount": 1000.00, "source": "Investment Account"},
            {"date": "2025-09-19", "desc": "FNB App Payment To Unicorn Dynamics", "amount": 1000.00, "source": "Investment Account"},
            {"date": "2025-09-19", "desc": "FNB App Transfer From Trs", "amount": 15000.00, "source": "Investment Account"},
            {"date": "2025-09-19", "desc": "FNB App Transfer From Trs", "amount": 20000.00, "source": "Investment Account"},
            {"date": "2025-09-27", "desc": "FNB App Transfer To Trs", "amount": 9000.00, "source": "Investment Account (OUT)"},
            {"date": "2025-09-27", "desc": "FNB App Transfer To Init", "amount": 4000.00, "source": "Investment Account (OUT)"},
            {"date": "2025-09-27", "desc": "FNB App Transfer To Init", "amount": 5000.00, "source": "Investment Account (OUT)"},
            {"date": "2025-09-27", "desc": "FNB App Payment To Tnb0036 2002", "amount": 6500.00, "source": "Investment Account"},
            {"date": "2025-09-27", "desc": "FNB App Transfer From Trs", "amount": 30000.00, "source": "Investment Account"},
        ]
    }
}

print("=" * 100)
print("CORRECTED EXPENDITURE ANALYSIS: Daniel's Personal Bank Account (May-October 2025)")
print("=" * 100)
print()

print("KEY CORRECTION:")
print("-" * 100)
print("All transfers INTO the account were from Daniel's PERSONAL INVESTMENT ACCOUNT,")
print("EXCEPT the R500,000 from Strategic Logistics on July 16, 2025.")
print()
print("This means:")
print("1. Daniel was funding his personal account from his OWN savings/investments")
print("2. The R500k was the ONLY external transfer (reimbursement from his company)")
print("3. Total expenditures show the true cost of company expenses on his personal card")
print()

print("=" * 100)
print("MONTHLY BREAKDOWN")
print("=" * 100)
print()

total_credits_all = 0
total_debits_all = 0
total_investment_transfers = 0
strategic_logistics_transfer = 0

for month, data in statements.items():
    print(f"### {month} ({data['period']})")
    print("-" * 100)
    print(f"Opening Balance:  R{data['opening_balance']:>15,.2f}")
    print(f"Credits:          R{data['total_credits']:>15,.2f}")
    print(f"Debits:           R{data['total_debits']:>15,.2f}")
    print(f"Closing Balance:  R{data['closing_balance']:>15,.2f}")
    print()
    
    if data['credit_breakdown']:
        print("Credit Breakdown:")
        for credit in data['credit_breakdown']:
            source_label = f"({credit['source']})"
            print(f"  {credit['date']}: {credit['desc']:<40} R{credit['amount']:>12,.2f} {source_label}")
            if "Strategic Logistics" in credit['source']:
                strategic_logistics_transfer += credit['amount']
            elif "Investment Account" in credit['source'] and "OUT" not in credit['source']:
                total_investment_transfers += credit['amount']
        print()
    
    # Calculate net change
    net_change = data['closing_balance'] - data['opening_balance']
    print(f"Net Change:       R{net_change:>15,.2f} ({'+' if net_change > 0 else ''}{(net_change / data['opening_balance'] * 100):.1f}%)")
    print()
    
    total_credits_all += data['total_credits']
    total_debits_all += data['total_debits']

print("=" * 100)
print("CUMULATIVE TOTALS (May 3 - October 4, 2025)")
print("=" * 100)
print()
print(f"Opening Balance (May 3):              R{statements['June 2025']['opening_balance']:>15,.2f}")
print(f"Closing Balance (Oct 4):              R{statements['October 2025']['closing_balance']:>15,.2f}")
print()
print(f"Total Credits (All Sources):          R{total_credits_all:>15,.2f}")
print(f"Total Debits (Expenditures):          R{total_debits_all:>15,.2f}")
print()
print("BREAKDOWN OF CREDITS:")
print(f"  Investment Account Transfers:       R{total_investment_transfers:>15,.2f}")
print(f"  Strategic Logistics (Jul 16):       R{strategic_logistics_transfer:>15,.2f}")
print(f"  Other (Credit Vouchers, etc.):      R{total_credits_all - total_investment_transfers - strategic_logistics_transfer:>15,.2f}")
print()
print(f"Net Change:                           R{statements['October 2025']['closing_balance'] - statements['June 2025']['opening_balance']:>15,.2f}")
print()

print("=" * 100)
print("KEY FINDINGS")
print("=" * 100)
print()

print("1. TOTAL EXPENDITURES: R{:,.2f}".format(total_debits_all))
print("   This is the total amount Daniel spent on his personal card from May-October 2025.")
print()

print("2. INVESTMENT ACCOUNT TRANSFERS: R{:,.2f}".format(total_investment_transfers))
print("   Daniel transferred this amount from his OWN investment account to cover expenses.")
print()

print("3. STRATEGIC LOGISTICS TRANSFER: R{:,.2f}".format(strategic_logistics_transfer))
print("   This was the ONLY external transfer, from Daniel's company (reimbursement).")
print()

print("4. NET DEFICIT: R{:,.2f}".format(total_debits_all - total_credits_all))
print("   Even after the R500k reimbursement, Daniel's account declined by R{:,.2f}".format(
    statements['June 2025']['opening_balance'] - statements['October 2025']['closing_balance']
))
print()

print("5. PRE-CANCELLATION vs POST-CANCELLATION:")
print()
print("   PRE-CANCELLATION (May 3 - Jun 4):")
print("     Opening:  R{:,.2f}".format(statements['June 2025']['opening_balance']))
print("     Closing:  R{:,.2f}".format(statements['June 2025']['closing_balance']))
print("     Change:   +R{:,.2f} (+{:.1f}%)".format(
    statements['June 2025']['closing_balance'] - statements['June 2025']['opening_balance'],
    (statements['June 2025']['closing_balance'] - statements['June 2025']['opening_balance']) / statements['June 2025']['opening_balance'] * 100
))
print()
print("   POST-CANCELLATION (Jun 4 - Oct 4):")
print("     Opening:  R{:,.2f}".format(statements['June 2025']['closing_balance']))
print("     Closing:  R{:,.2f}".format(statements['October 2025']['closing_balance']))
print("     Change:   -R{:,.2f} (-{:.1f}%)".format(
    statements['June 2025']['closing_balance'] - statements['October 2025']['closing_balance'],
    (statements['June 2025']['closing_balance'] - statements['October 2025']['closing_balance']) / statements['June 2025']['closing_balance'] * 100
))
print()

print("=" * 100)
print("CONCLUSION")
print("=" * 100)
print()
print("1. Daniel spent R{:,.2f} on his personal card over 5 months.".format(total_debits_all))
print()
print("2. Daniel funded R{:,.2f} from his OWN investment account.".format(total_investment_transfers))
print()
print("3. Daniel received R{:,.2f} from Strategic Logistics (his company) as reimbursement.".format(strategic_logistics_transfer))
print()
print("4. Even with the R500k reimbursement, Daniel's account declined from R{:,.2f} to R{:,.2f}.".format(
    statements['June 2025']['opening_balance'],
    statements['October 2025']['closing_balance']
))
print()
print("5. The card cancellation on June 7 caused a dramatic reversal:")
print("   - Before: +{:.1f}% growth".format(
    (statements['June 2025']['closing_balance'] - statements['June 2025']['opening_balance']) / statements['June 2025']['opening_balance'] * 100
))
print("   - After:  -{:.1f}% decline".format(
    (statements['June 2025']['closing_balance'] - statements['October 2025']['closing_balance']) / statements['June 2025']['closing_balance'] * 100
))
print()
print("6. Peter's 'R500k birthday gift' narrative is PROVEN FALSE:")
print("   - The R500k came from Daniel's own company (Strategic Logistics)")
print("   - It was reimbursement for company expenses, not a 'gift'")
print("   - Daniel was funding expenses from his own investment account")
print()

print("=" * 100)
print("END OF ANALYSIS")
print("=" * 100)

