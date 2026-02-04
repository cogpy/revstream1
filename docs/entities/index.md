# Entities Index

**Last Updated:** 2026-02-04  
**Total Entities:** 90+

This index catalogs all entities involved in Case 2025-137857: Revenue Stream Hijacking.

---

## Persons

### Primary Perpetrators

| Entity ID | Name | Role | Evidence Strength |
|-----------|------|------|-------------------|
| [PERSON_001](./PERSON_001.md) | Peter Andrew Faucitt | Primary Perpetrator | Conclusive (95%+) |
| [PERSON_002](./PERSON_002.md) | Rynette Farrar | Co-Conspirator | Conclusive (95%+) |

### Accomplices

| Entity ID | Name | Role | Evidence Strength |
|-----------|------|------|-------------------|
| [PERSON_003](./PERSON_003.md) | Adderory (Rynette's Son) | Co-Conspirator (Family) | Strong |
| [PERSON_007](./PERSON_007.md) | Daniel Jacobus Bantjies | Strategic Appointee/Accountant | Strong |

### Victims/Respondents

| Entity ID | Name | Role | Status |
|-----------|------|------|--------|
| [PERSON_004](./PERSON_004.md) | Jacqueline Faucitt | First Respondent | Victim |
| [PERSON_005](./PERSON_005.md) | Daniel James Faucitt | Second Respondent | Victim |

### Other Persons

| Entity ID | Name | Role | Relevance |
|-----------|------|------|-----------|
| [PERSON_006](./PERSON_006.md) | Linda | Employee (Bookkeeper) | Witness |
| [PERSON_008](./PERSON_008.md) | Kayla | ReZonance Director | Deceased (2023-07-13) |
| [PERSON_009](./PERSON_009.md) | Gee | Employee | Witness (Domain Switch) |
| [PERSON_010](./PERSON_010.md) | Bernadine Wright | Financial Advisor | Key Decision-Maker |
| [PERSON_011](./PERSON_011.md) | Chantal | Kayla Estate Representative | Estate Matters |
| [PERSON_012](./PERSON_012.md) | Jacqueline "Jax" Faucitt | FFT Trustee | Neutralized via Interdict |
| [PERSON_013](./PERSON_013.md) | Kayla Pretorius | ReZonance Co-Director | Deceased (SF6) |
| [PERSON_014](./PERSON_014.md) | Kevin Michael Derrick | Ketoni Director | Bantjies Connection |

---

## Organizations

### RegimA Group Companies

| Entity ID | Name | Registration | Status |
|-----------|------|--------------|--------|
| [ORG_001](./ORG_001.md) | Regima Worldwide Distribution (Pty) Ltd | 2011/005722/07 | Active |
| [ORG_002](./ORG_002.md) | Regima Skin Treatments CC | 1992 | Active |
| [ORG_004](./ORG_004.md) | Strategic Logistics Group (Pty) Ltd | 2008 | Active |
| [ORG_005](./ORG_005.md) | Villa Via | - | Property Holding |
| [ORG_006](./ORG_006.md) | RegimA SA | - | Active |
| [ORG_012](./ORG_012.md) | RegimaSA (Pty) Ltd | - | Active |
| [ORG_014](./ORG_014.md) | RegimA SA (Pty) Ltd | - | Active |

### UK Entity

| Entity ID | Name | Jurisdiction | Owner |
|-----------|------|--------------|-------|
| [ORG_003](./ORG_003.md) | RegimA Zone Ltd | UK | Daniel James Faucitt |

### Shell/Competing Companies

| Entity ID | Name | Owner | Purpose |
|-----------|------|-------|---------|
| [ORG_008](./ORG_008.md) | ReZonance (Pty) Ltd | Daniel/Kayla | IT Services |
| [ORG_009](./ORG_009.md) | Adderory (Pty) Ltd | Adderory (PERSON_003) | Shell Company |
| [ORG_010](./ORG_010.md) | Adderory Skin (Pty) Ltd | Adderory (PERSON_003) | Competing Business |
| [ORG_013](./ORG_013.md) | Unicorn Dynamics (Pty) Ltd | Daniel James Faucitt | Technology |

### External Organizations

| Entity ID | Name | Role | Relevance |
|-----------|------|------|-----------|
| [ORG_007](./ORG_007.md) | Ian Levitt Attorneys | Legal | R63M Demand (SF9) |
| [ORG_015](./ORG_015.md) | SARS | Revenue Service | Tax Audit |
| [ORG_016](./ORG_016.md) | Ketoni Investment Holdings | Investment | ZAR 18.75M Payout |

---

## Trusts

| Entity ID | Name | Trustees | Significance |
|-----------|------|----------|--------------|
| [TRUST_001](./TRUST_001.md) | Faucitt Family Trust (FFT) | Peter, Jax, Bantjies | Central to ZAR 18.75M motive |

---

## Platforms

| Entity ID | Name | Owner | Status |
|-----------|------|-------|--------|
| [PLATFORM_001](./PLATFORM_001.md) | Shopify Platform | RegimA Zone Ltd | Hijacked (2025-05-22) |

---

## Domains

| Entity ID | Domain | Owner | Status |
|-----------|--------|-------|--------|
| [DOMAIN_001](./DOMAIN_001.md) | regimaskin.co.za | Adderory (Pty) Ltd | Fraudulent Registration |
| [DOMAIN_002](./DOMAIN_002.md) | regima.zone | RegimA Zone Ltd | Legitimate |

---

## Bank Accounts

| Entity ID | Description | Status |
|-----------|-------------|--------|
| [BANK_001](./BANK_001.md) | ABSA Accounts (8 suspected fraudulent) | Under Investigation |
| [BANK_002](./BANK_002.md) | FNB Account 62323196362 (RWD) | Fraud Acknowledged (FNB Letter) |

---

## Key Entity Relationships

### Ketoni Connection (Central Motive)

```
Ketoni Investment Holdings (ORG_016)
    ├── Director: Kevin Michael Derrick (PERSON_014)
    │       └── Colleague of: Daniel Jacobus Bantjies (PERSON_007)
    │
    └── Shareholder: Faucitt Family Trust (TRUST_001)
            ├── Trustee: Peter Andrew Faucitt (PERSON_001)
            ├── Trustee: Jacqueline Faucitt (PERSON_012) - Neutralized
            └── Trustee: Daniel Jacobus Bantjies (PERSON_007) - Appointed by Rynette
            
    ZAR 18.75M Payout Due: May 2026
```

### Control Structure

```
Peter Andrew Faucitt (PERSON_001)
    ├── Director: RWD, RST, SLG, RegimA SA
    ├── Main Trustee: FFT (backdated 2025-08-11)
    └── Controls: Bank accounts, Trust decisions

Rynette Farrar (PERSON_002)
    ├── Financial Controller: All RegimA entities
    ├── Sage System Control: pete@regima.com + rynette@regima.zone
    └── Appointed: Bantjies as Trustee (July 2024)
```

---

## Evidence Cross-References

- **[Evidence Index](../evidence-index-enhanced.md)** - Comprehensive evidence catalog
- **[Timeline](../timeline.md)** - Chronological event sequence
- **[Relations](../relations/index.md)** - Entity relationship mapping
- **[ad-res-j7 Repository](https://github.com/cogpy/ad-res-j7)** - Extended evidence

---

*Last updated by LEX Investigation System: 2026-02-04*
