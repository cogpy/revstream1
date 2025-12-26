;;; ============================================================================
;;; ENTITY-RELATION FRAMEWORK V47 - RIGOROUSLY VERIFIED FROM PRIMARY SOURCES
;;; ============================================================================
;;; Version: 47.0
;;; Date: 2025-12-26
;;; Verification Level: PRIMARY SOURCE VERIFIED
;;; 
;;; METHODOLOGY:
;;; - All entity data extracted from official documents only
;;; - No assumptions or inferences without explicit source citation
;;; - Confidence levels based on source reliability
;;; - Unverified claims explicitly marked as UNVERIFIED
;;; ============================================================================

;;; ============================================================================
;;; SECTION 1: FAUCITT FAMILY TRUST - VERIFIED FROM TRUST DEED & J246
;;; ============================================================================

(define-entity faucitt-family-trust
  (type trust)
  (official-name "FAUCITT FAMILY TRUST")
  
  ;; VERIFIED from J246 Letter of Authority
  (trust-number "IT 003651/2013")
  (urn "9922013TRU003651")
  (registration-office "JOHANNESBURG")
  (j246-authorization-date "2024-10-18")
  (source-j246 "J246+-+Letter+of+Authority(3).pdf")
  (verification-confidence 1.00)
  
  ;; VERIFIED from Trust Deed (deed_of_trust_reconstructed.md)
  (execution-date "2013-11-27")  ;; Signed at Bedfordview on 27th November 2013
  (registration-date "2013-12-05")  ;; Master's stamp shows 2013-12-05
  (initial-donation "R100.00")
  (source-deed "deed_of_trust_reconstructed.md")
  
  ;; VERIFIED Founder from Trust Deed
  (founder
    (name "PETER ANDREW FAUCITT")
    (id-number "5204305708185")
    (address "20 River Road, Morning Hill, Bedfordview")
    (source "Trust Deed - Image 12 Deed Of Trust Title")
    (verification-confidence 1.00))
  
  ;; VERIFIED Original Trustees from Trust Deed (2013)
  (original-trustees
    ((name "PETER ANDREW FAUCITT")
     (id-number "5204305708185")
     (role "Trustee")
     (appointment-date "2013-11-27")
     (source "Trust Deed - Declaration by Trustees")
     (verification-confidence 1.00))
    ((name "JACQUELINE FAUCITT")
     (id-number "5706070898181")
     (role "Trustee")
     (appointment-date "2013-11-27")
     (source "Trust Deed - Declaration by Trustees")
     (verification-confidence 1.00)))
  
  ;; VERIFIED Current Trustees from J246 (2024)
  (current-trustees-as-of-2024-10-18
    ((name "PETER ANDREW FAUCITT")
     (id-number "5204305708185")
     (source "J246 Letter of Authority")
     (verification-confidence 1.00))
    ((name "JACQUELINE FAUCITT")
     (id-number "5706070898181")
     (source "J246 Letter of Authority")
     (verification-confidence 1.00))
    ((name "DANIEL JACOBUS BANTJES")
     (id-number "5810045103089")
     (source "J246 Letter of Authority")
     (verification-confidence 1.00)
     (notes "Third trustee - appointment date NOT in J246")))
  
  ;; VERIFIED Beneficiaries from Trust Deed
  (beneficiaries
    ((name "PETER ANDREW FAUCITT")
     (id-number "5204305708185")
     (address "20 River Road, Morning Hill, Bedfordview")
     (source "Trust Deed - Clause 1.3 and Image 12")
     (signature-date "2013-11-27")
     (verification-confidence 1.00))
    ((name "JACQUELINE FAUCITT")
     (id-number "5706070898181")
     (address "20 River Road, Morning Hill, Bedfordview")
     (source "Trust Deed - Clause 1.3 and Image 25")
     (signature-date "2013-11-27")
     (verification-confidence 1.00))
    ((name "DANIEL JAMES FAUCITT")
     (id-number "8207155300182")
     (address "16 Villa Palmar, 20A Protea Road, Bedfordview")
     (source "Trust Deed - Image 29 Deed Preamble Daniel")
     (signature-date "2013-11-27")
     (verification-confidence 1.00)))
  
  ;; VERIFIED Trust Accountant from Declaration by Trustees
  (accountant
    (name "D J BANTJES")
    (designation "CA (SA)")
    (address "19 Fisheagle Lane, Country Lane Estate, Rietvalleirand, 0081")
    (practice-number "944130")
    (source "Trust Deed - Declaration by Trustees, clause 6.b")
    (verification-confidence 1.00)
    (notes "Same person as later trustee Daniel Jacobus Bantjes"))
  
  ;; VERIFIED Bank Details from Declaration by Trustees
  (bank-account
    (bank "First National Bank")
    (branch "Private Clients, Johannesburg")
    (branch-code "256605")
    (source "Trust Deed - Declaration by Trustees, clause 6.a")
    (verification-confidence 1.00))
  
  ;; VERIFIED Main Asset Location from Declaration by Trustees
  (main-asset-location "20 River Road, Morninghill, Bedfordview"
    (source "Trust Deed - Declaration by Trustees, clause 5")
    (verification-confidence 1.00))
  
  ;; Key Trust Deed Provisions (VERIFIED)
  (trustee-appointment-power
    (during-founder-life "Founder has sole power to appoint trustees")
    (after-founder-death "Surviving trustees may appoint new trustees")
    (source "Trust Deed - Clause 3.2 and 3.3")
    (verification-confidence 1.00))
  
  (minimum-trustees 2)
  (maximum-trustees 5)
  (source-trustee-limits "Trust Deed - Clause 3.4")
  
  (termination-provision
    (description "Trust terminates at time determined by trustees in sole discretion")
    (vesting "Trust assets vest in beneficiaries on termination date")
    (source "Trust Deed - Clause 15")
    (verification-confidence 1.00)))

;;; ============================================================================
;;; SECTION 2: INDIVIDUALS - VERIFIED FROM MULTIPLE SOURCES
;;; ============================================================================

(define-entity peter-andrew-faucitt
  (type individual)
  (full-name "PETER ANDREW FAUCITT")
  (id-number "5204305708185")
  (birth-date-derived "1952-04-30")  ;; Derived from ID number
  (gender "Male")
  (citizenship "South African")
  
  ;; VERIFIED Address from Trust Deed
  (address-2013 "20 River Road, Morning Hill, Bedfordview"
    (source "Trust Deed 2013")
    (verification-confidence 1.00))
  
  ;; VERIFIED Roles in Trust
  (trust-roles
    ((role "Founder")
     (trust "Faucitt Family Trust")
     (date "2013-11-27")
     (source "Trust Deed")
     (verification-confidence 1.00))
    ((role "Trustee")
     (trust "Faucitt Family Trust")
     (appointment-date "2013-11-27")
     (source "Trust Deed")
     (verification-confidence 1.00))
    ((role "Beneficiary")
     (trust "Faucitt Family Trust")
     (date "2013-11-27")
     (source "Trust Deed - Clause 1.3")
     (verification-confidence 1.00)))
  
  ;; VERIFIED Company Roles from B2Bhint CIPC Records
  (company-roles
    ((company "REGIMA WORLDWIDE DISTRIBUTION")
     (registration "2011/005722/07")
     (role "Director")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "VILLA VIA ARCADIA NO 2")
     (registration "1996/004451")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SKIN TREATMENTS")
     (registration "1992/005371")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "CORPCLO 2304")
     (registration "2005/014378")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SA")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA INTERNATIONAL SKIN TREATMENTS")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "CORPCLO 2065")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "STRATEGIC LOGISTICS")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SPAZONE")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA MEDIC")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "AYMAC INTERNATIONAL")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))))

(define-entity jacqueline-faucitt
  (type individual)
  (full-name "JACQUELINE FAUCITT")
  (id-number "5706070898181")
  (birth-date-derived "1957-06-07")  ;; Derived from ID number
  (gender "Female")
  (citizenship "South African")
  
  ;; VERIFIED Address from Trust Deed
  (address-2013 "20 River Road, Morning Hill, Bedfordview"
    (source "Trust Deed 2013")
    (verification-confidence 1.00))
  
  ;; VERIFIED Roles in Trust
  (trust-roles
    ((role "Trustee")
     (trust "Faucitt Family Trust")
     (appointment-date "2013-11-27")
     (source "Trust Deed")
     (verification-confidence 1.00))
    ((role "Beneficiary")
     (trust "Faucitt Family Trust")
     (date "2013-11-27")
     (source "Trust Deed - Clause 1.3")
     (verification-confidence 1.00)))
  
  ;; VERIFIED Company Roles from B2Bhint CIPC Records
  (company-roles
    ((company "REGIMA WORLDWIDE DISTRIBUTION")
     (registration "2011/005722/07")
     (role "Director")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "VILLA VIA ARCADIA NO 2")
     (registration "1996/004451")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SKIN TREATMENTS")
     (registration "1992/005371")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "CORPCLO 2304")
     (registration "2005/014378")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA INTERNATIONAL SKIN TREATMENTS")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "CORPCLO 2065")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "STRATEGIC LOGISTICS")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SPAZONE")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA MEDIC")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "AYMAC INTERNATIONAL")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))))

(define-entity daniel-james-faucitt
  (type individual)
  (full-name "DANIEL JAMES FAUCITT")
  (known-as "Jax" "Dan")
  (id-number "8207155300182")
  (birth-date-derived "1982-07-15")  ;; Derived from ID number
  (gender "Male")
  (citizenship "South African")
  
  ;; VERIFIED Address from Trust Deed (2013)
  (address-2013 "16 Villa Palmar, 20A Protea Road, Bedfordview"
    (source "Trust Deed - Image 29")
    (verification-confidence 1.00))
  
  ;; VERIFIED Role in Trust
  (trust-roles
    ((role "Beneficiary")
     (trust "Faucitt Family Trust")
     (date "2013-11-27")
     (source "Trust Deed - Clause 1.3 and Image 29")
     (verification-confidence 1.00)))
  
  ;; VERIFIED: Daniel is NOT a trustee (as of Trust Deed 2013)
  (trustee-status "NOT A TRUSTEE"
    (source "Trust Deed - only Peter and Jacqueline listed as trustees")
    (verification-confidence 1.00))
  
  ;; VERIFIED Company Roles from B2Bhint CIPC Records
  (company-roles
    ((company "REZONANCE")
     (registration "2017/081396")
     (role "Director")
     (status "Deregistration due to annual return non compliance")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "STRATEGIC LOGISTICS")
     (registration "2008/136496")
     (role "Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "JOZI WAY TRADING")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA ZONE ACADEMY")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SA")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "PANDAMANIA")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA ZONE IMPACT")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SPAZONE")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA MEDIC")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA WORLDWIDE DISTRIBUTION")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "AYMAC INTERNATIONAL")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "UNICORN DYNAMICS")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA ZONE")
     (role "Director/Member")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95)))
  
  ;; KEY OBSERVATION: Daniel NOT in older CCs
  (not-member-of
    ((company "VILLA VIA ARCADIA NO 2")
     (note "Peter and Jacqueline are members, Daniel is NOT")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))
    ((company "REGIMA SKIN TREATMENTS")
     (note "Peter and Jacqueline are members, Daniel is NOT")
     (source "B2Bhint CIPC")
     (verification-confidence 0.95))))

(define-entity daniel-jacobus-bantjes
  (type individual)
  (full-name "DANIEL JACOBUS BANTJES")
  (known-as "Danie Bantjes")
  (id-number "5810045103089")
  (birth-date-derived "1958-10-04")  ;; Derived from ID number
  (gender "Male")
  (citizenship "South African")
  
  ;; VERIFIED Address from Trust Deed Declaration (2013)
  (address-2013 "19 Fisheagle Lane, Country Lane Estate, Rietvalleirand, 0081"
    (source "Trust Deed - Declaration by Trustees, clause 6.b")
    (verification-confidence 1.00))
  
  ;; VERIFIED Role as Trust Accountant (2013)
  (trust-accountant-role
    (trust "Faucitt Family Trust")
    (designation "CA (SA)")
    (practice-number "944130")
    (appointment-date "2013-11-27")  ;; Date of Trust Deed
    (source "Trust Deed - Declaration by Trustees")
    (verification-confidence 1.00))
  
  ;; VERIFIED Role as Trustee (2024)
  (trustee-role
    (trust "Faucitt Family Trust")
    (verified-as-of "2024-10-18")
    (source "J246 Letter of Authority")
    (verification-confidence 1.00)
    (appointment-date "UNKNOWN - NOT IN J246")))

;;; ============================================================================
;;; SECTION 3: COMPANIES - VERIFIED FROM B2BHINT CIPC RECORDS
;;; ============================================================================

(define-entity regima-worldwide-distribution
  (type company)
  (official-name "REGIMA WORLDWIDE DISTRIBUTION")
  (registration-number "2011/005722/07")
  (enterprise-number "M2011005722")
  (legal-form "Private company")
  (incorporation-date "2011-03-11")
  (status "In Business")
  (subtype "R10 million but less than R25 million")
  (vat-number "9876222150")
  (legal-address "20 RIVER ROAD, MORNINGHILL, BEDFORDVIEW, GAUTENG, 2007")
  (mailing-address "50 VAN BUUREN ROAD, BEDFORDVIEW, BEDFORDVIEW, GAUTENG, 2008")
  (directors
    ((name "Jacqueline Faucitt") (role "Director"))
    ((name "Peter Andrew Faucitt") (role "Director")))
  (officer-count 6)
  (last-updated "2025-01-04")
  (source "B2Bhint CIPC")
  (source-url "https://b2bhint.com/en/company/za/regima-worldwide-distribution--M2011005722")
  (verification-confidence 0.95)
  
  ;; UNVERIFIED: Trust ownership claim
  (trust-ownership-claim
    (status "UNVERIFIED")
    (claim "Trust Deed Declaration states main assets at 20 River Road")
    (note "CIPC shows Peter and Jacqueline as directors, not FFT")
    (requires-verification "Share register or CIPC CM29 forms")))

(define-entity villa-via-arcadia-no-2
  (type company)
  (official-name "VILLA VIA ARCADIA NO 2")
  (registration-number "1996/004451")
  (enterprise-number "B1996004451")
  (legal-form "Close corporation")
  (incorporation-date "1996-02-02")
  (status "In Business")
  (subtype "Less than R1 million")
  (vat-number "9636866841")
  (legal-address "20 RIVER ROAD, MORNINGHILL, BEDFORDVIEW, GAUTENG, 2007")
  (mailing-address "50 VAN BUUREN ROAD, BEDFORDVIEW, BEDFORDVIEW, GAUTENG, 2008")
  (members
    ((name "Jacqueline Faucitt") (role "Member"))
    ((name "Peter Andrew Faucitt") (role "Member")))
  (officer-count 4)
  (last-updated "2024-07-12")
  (source "B2Bhint CIPC")
  (source-url "https://b2bhint.com/en/company/za/villa-via-arcadia-no-2--B1996004451")
  (verification-confidence 0.95)
  
  ;; KEY: Daniel is NOT a member
  (daniel-membership "NOT A MEMBER"
    (source "B2Bhint CIPC")
    (verification-confidence 0.95)))

(define-entity strategic-logistics
  (type company)
  (official-name "STRATEGIC LOGISTICS")
  (registration-number "2008/136496")
  (enterprise-number "B2008136496")
  (legal-form "Close corporation")
  (incorporation-date "2008-06-27")
  (status "In Business")
  (subtype "Less than R1 million")
  (vat-number "9952347152")
  (legal-address "20 RIVER ROAD, MORNINGHILL, BEDFORDVIEW, GAUTENG, 2007")
  (mailing-address "50 VAN BUUREN ROAD, BEDFORDVIEW, BEDFORDVIEW, GAUTENG, 2008")
  (members
    ((name "Daniel James Faucitt") (role "Member"))
    ((name "Jacqueline Faucitt") (role "Member")))
  (officer-count 6)
  (last-updated "2024-07-05")
  (source "B2Bhint CIPC")
  (source-url "https://b2bhint.com/en/company/za/strategic-logistics--B2008136496")
  (verification-confidence 0.95)
  
  ;; KEY: Daniel IS a member here (unlike Villa Via)
  (daniel-membership "MEMBER"
    (source "B2Bhint CIPC")
    (verification-confidence 0.95)))

(define-entity rezonance
  (type company)
  (official-name "REZONANCE")
  (registration-number "2017/081396")
  (enterprise-number "K2017081396")
  (legal-form "Private company")
  (incorporation-date "2017-02-22")
  (status "Deregistration due to annual return non compliance")
  (subtype "R1 million but less than R10 million")
  (vat-number "9251480225")
  (legal-address "20 RIVER ROAD, MORNINGHILL, BEDFORDVIEW, GAUTENG, 2007")
  (mailing-address "50 VAN BUUREN ROAD, BEDFORDVIEW, BEDFORDVIEW, GAUTENG, 2008")
  (directors
    ((name "Daniel James Faucitt") (role "Director"))
    ((name "Kayla Pretorius") (role "Director")))
  (officer-count 2)
  (last-updated "2025-12-14")
  (source "B2Bhint CIPC")
  (source-url "https://b2bhint.com/en/company/za/rezonance--K2017081396")
  (verification-confidence 0.95)
  (liquidation-status "In process of liquidation as of Dec 14, 2025"))

;;; ============================================================================
;;; SECTION 4: KETONI INVESTMENT HOLDINGS - PARTIALLY VERIFIED
;;; ============================================================================

(define-entity ketoni-investment-holdings
  (type company)
  (official-name "KETONI INVESTMENT HOLDINGS (PTY) LTD")
  (registration-number "2023/126217/07")
  (incorporation-date "2023-02-20")
  (status "UNKNOWN - requires CIPC verification")
  
  ;; VERIFIED from Share Certificate Analysis
  (share-certificate
    (certificate-number 3)
    (issue-date "2023-04-24")
    (shareholder "FAUCITT FAMILY TRUST")
    (share-class "A-Ordinary")
    (share-quantity 5000)
    (source "KETONI_INVESTMENT_HOLDINGS_SHARE_CERTIFICATE_ANALYSIS.md")
    (verification-confidence 0.90))
  
  ;; VERIFIED Director from Kevin Derrick B2Bhint
  (directors
    ((name "Kevin Michael Derrick")
     (source "KevinMichaelDerrick_B2BHint.md")
     (verification-confidence 0.90)))
  
  ;; UNVERIFIED: May 2026 Payout
  (may-2026-payout
    (status "UNVERIFIED")
    (claimed-amount "R28.7M")
    (note "Source of this figure requires verification")
    (requires-verification "Investment agreement, payout schedule, or other documentation")))

;;; ============================================================================
;;; SECTION 5: VERIFIED TIMELINE EVENTS
;;; ============================================================================

(define-timeline verified-events
  
  ;; 1992 - Regima Skin Treatments incorporated
  ((date "1992-02-26")
   (event "Regima Skin Treatments CC incorporated")
   (source "B2Bhint CIPC")
   (verification-confidence 0.95))
  
  ;; 1996 - Villa Via incorporated
  ((date "1996-02-02")
   (event "Villa Via Arcadia No 2 CC incorporated")
   (source "B2Bhint CIPC")
   (verification-confidence 0.95))
  
  ;; 2005 - CorpClo 2304 incorporated
  ((date "2005-02-07")
   (event "CorpClo 2304 CC incorporated")
   (source "B2Bhint CIPC")
   (verification-confidence 0.95))
  
  ;; 2008 - Strategic Logistics incorporated
  ((date "2008-06-27")
   (event "Strategic Logistics CC incorporated")
   (members "Daniel James Faucitt, Jacqueline Faucitt")
   (source "B2Bhint CIPC")
   (verification-confidence 0.95))
  
  ;; 2011 - RegimA Worldwide Distribution incorporated
  ((date "2011-03-11")
   (event "RegimA Worldwide Distribution (Pty) Ltd incorporated")
   (source "B2Bhint CIPC")
   (verification-confidence 0.95))
  
  ;; 2013-11-11 - Trust Declaration signed
  ((date "2013-11-11")
   (event "Declaration by Trustees signed")
   (trustees "Peter Andrew Faucitt, Jacqueline Faucitt")
   (accountant "D J Bantjes CA(SA)")
   (source "Trust Deed - Image 20")
   (verification-confidence 1.00))
  
  ;; 2013-11-27 - Trust Deed executed
  ((date "2013-11-27")
   (event "Faucitt Family Trust Deed executed at Bedfordview")
   (founder "Peter Andrew Faucitt")
   (trustees "Peter Andrew Faucitt, Jacqueline Faucitt")
   (beneficiaries "Peter Andrew Faucitt, Jacqueline Faucitt, Daniel James Faucitt")
   (source "Trust Deed - Signature Pages")
   (verification-confidence 1.00))
  
  ;; 2013-12-05 - Trust registered with Master
  ((date "2013-12-05")
   (event "Trust registered with Master of South Gauteng High Court")
   (trust-number "IT 3651/2013")
   (source "Trust Deed - Master's Stamp")
   (verification-confidence 1.00))
  
  ;; 2017-02-22 - ReZonance incorporated
  ((date "2017-02-22")
   (event "ReZonance (Pty) Ltd incorporated")
   (directors "Daniel James Faucitt, Kayla Pretorius")
   (source "B2Bhint CIPC")
   (verification-confidence 0.95))
  
  ;; 2023-02-20 - Ketoni incorporated
  ((date "2023-02-20")
   (event "Ketoni Investment Holdings (Pty) Ltd incorporated")
   (source "KETONI_CIPC_SEARCH_RESULTS.md")
   (verification-confidence 0.90))
  
  ;; 2023-04-24 - FFT receives Ketoni shares
  ((date "2023-04-24")
   (event "FFT receives 5,000 A-Ordinary shares in Ketoni Investment Holdings")
   (certificate-number 3)
   (source "Share Certificate Analysis")
   (verification-confidence 0.90))
  
  ;; 2024-10-18 - J246 Letter of Authority issued
  ((date "2024-10-18")
   (event "J246 Letter of Authority issued by Master's Office")
   (trustees "Peter Andrew Faucitt, Jacqueline Faucitt, Daniel Jacobus Bantjes")
   (source "J246+-+Letter+of+Authority(3).pdf")
   (verification-confidence 1.00)))

;;; ============================================================================
;;; SECTION 6: UNVERIFIED CLAIMS REQUIRING DOCUMENTATION
;;; ============================================================================

(define-unverified-claims
  
  ;; Bantjes trustee appointment date
  ((claim "Bantjes appointed as trustee in July 2024")
   (status "UNVERIFIED")
   (j246-shows "Bantjes is trustee as of 2024-10-18")
   (requires "Trustee appointment letter or J246 showing appointment date"))
  
  ;; Trust ownership of companies
  ((claim "FFT owns RegimA Worldwide Distribution")
   (status "UNVERIFIED")
   (cipc-shows "Peter and Jacqueline as directors, not FFT")
   (requires "Share register, CM29 forms, or other ownership documentation"))
  
  ;; Trust ownership of Villa Via
  ((claim "FFT owns Villa Via Arcadia No 2")
   (status "UNVERIFIED")
   (cipc-shows "Peter and Jacqueline as members, not FFT")
   (requires "CK2 forms or member interest certificates"))
  
  ;; May 2026 payout amount
  ((claim "R28.7M payout expected May 2026 from Ketoni")
   (status "UNVERIFIED")
   (requires "Investment agreement, payout schedule, or financial projections"))
  
  ;; Beneficiary shares
  ((claim "Each beneficiary entitled to 50% or 33.33%")
   (status "UNVERIFIED")
   (trust-deed-says "Trustees have sole discretion on distribution")
   (requires "Trust amendment or distribution agreement")))

;;; ============================================================================
;;; END OF VERIFIED ENTITY-RELATION FRAMEWORK V47
;;; ============================================================================
