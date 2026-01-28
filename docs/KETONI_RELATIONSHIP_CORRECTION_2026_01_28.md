# Critical Correction: Ketoni R18.75M Debt Structure

**Date:** 2026-01-28
**Type:** Factual Correction
**Priority:** CRITICAL

## Summary of Correction

Previous documentation incorrectly attributed the R18.75M debt to Bantjies personally. The correct structure is:

### INCORRECT (Previous Understanding)
- Ketoni owes R18.75M to FFT (Bantjies has conflict as George Group CFO) to Faucitt Family Trust
- This created a conflict of interest for Bantjies as Trustee

### CORRECT (Updated Understanding)
- **Ketoni Investment Holdings (Pty) Ltd** owes R18.75M to Faucitt Family Trust
- The debt is a **payout obligation** from Ketoni to FFT for shares held
- Bantjies' conflict of interest arises from his **corporate position**, not personal debt

## Correct Relationship Structure

### 1. Ketoni Investment Holdings (Pty) Ltd
- **Debt to FFT:** R18.75M (payout due May 2026)
- **Owner/Shareholder/Director:** CEO of George Group
- **Connection to Bantjies:** Bantjies is CFO of George Group

### 2. George Group
- **CEO:** Owner/Shareholder/Director of Ketoni
- **CFO:** Danie Bantjies
- **Relationship:** Bantjies reports to Ketoni's owner through George Group

### 3. Faucitt Family Trust (IT 003651/2013)
- **Asset:** 5,000 A-Ordinary shares in Ketoni Investment Holdings
- **Entitlement:** R18.75M payout (May 2026 option)
- **Trustees:** Peter Faucitt (Founder), Bantjies (unlawfully appointed July 2024)

### 4. Bantjies' Conflict of Interest
- **Role 1:** CFO of George Group (reports to Ketoni's owner)
- **Role 2:** Trustee of FFT (owes fiduciary duty to beneficiaries)
- **Role 3:** Accountant for RegimA Group companies
- **Conflict:** As CFO of George Group, Bantjies has loyalty to Ketoni's owner who owes R18.75M to FFT where Bantjies is a Trustee

### 5. Unlawful Trustee Appointment
- **Appointed by:** Rynette Farrar (July 2024)
- **Issue:** Rynette had no authority to appoint trustees
- **Timing:** 10 months before May 2026 R18.75M payout
- **Motive:** Create compliant trustee majority to control payout

## Evidence Chain

| Fact | Evidence Reference |
|------|-------------------|
| FFT holds Ketoni shares | JF10 - Trust Documents |
| R18.75M payout due May 2026 | Ketoni Investment Agreement |
| Bantjies is CFO of George Group | Company records |
| Ketoni owner is CEO of George Group | Company records |
| Bantjies appointed Trustee July 2024 | Trust amendment documents |
| Rynette made the appointment | Trust amendment documents |

## Impact on Legal Filings

All references to "Ketoni R18.75M debt to FFT (Bantjies conflict as George Group CFO),000 owed by Bantjies" must be corrected to:

1. **Ketoni owes R18.75M to FFT** (not Bantjies personally)
2. **Bantjies has conflict of interest** due to his CFO role at George Group
3. **Bantjies' loyalty is to Ketoni's owner** who owes the debt
4. **Unlawful appointment** by Rynette created compliant trustee majority

## Files Requiring Update

- `data_models/entities/entities.json` - Bantjies entity, Ketoni entity, FFT entity
- `data_models/relations/relations.json` - Debt relationships
- `data_models/events/events.json` - Events referencing Bantjies debt
- `docs/filings/*.md` - All legal filings mentioning Bantjies debt
- `ANNEXURES/SF1_Ketoni_Debt_FFT_Documentation.md` - Rename/update to Ketoni documentation

## Corrected Narrative

> The Faucitt Family Trust holds 5,000 A-Ordinary shares in Ketoni Investment Holdings (Pty) Ltd, entitling the Trust to an R18.75M payout available as an option in May 2026. Danie Bantjies serves as CFO of George Group, whose CEO is the owner/shareholder/director of Ketoni. In July 2024, Rynette Farrar unlawfully appointed Bantjies as a Trustee of FFT, creating a compliant trustee majority 10 months before the R18.75M payout date. This appointment created a severe conflict of interest: Bantjies owes professional loyalty to Ketoni's owner (his ultimate superior at George Group) while simultaneously owing fiduciary duty to FFT beneficiaries who are entitled to the R18.75M payout from Ketoni.

---
*This correction supersedes all previous documentation regarding "Bantjies debt" to the Faucitt Family Trust.*
