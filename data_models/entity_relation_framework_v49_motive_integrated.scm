;;; =============================================================================
;;; ENTITY-RELATION FRAMEWORK V49 - R18.75M KETONI PAYOUT MOTIVE INTEGRATED
;;; =============================================================================
;;; Version: 49.0
;;; Date: 2025-12-26
;;; Purpose: Complete entity-relation model with R18.75M central motive
;;; Methodology: All events recontextualized through R18.75M payout lens
;;; =============================================================================

;;; -----------------------------------------------------------------------------
;;; SECTION 1: CENTRAL MOTIVE DEFINITION
;;; -----------------------------------------------------------------------------

(define-motive ketoni-payout-capture
  (description "Scheme to capture 100% of R18.75M Ketoni payout through curatorship fraud")
  (amount 18750000)
  (currency "ZAR")
  (due-date "2026-05")
  (debtor "Ketoni Investment Holdings (Pty) Ltd")
  (creditor "Faucitt Family Trust")
  (beneficiary-split
    (peter-share 0.50 9375000)
    (jax-share 0.50 9375000))
  (scheme-goal "Peter captures Jax's R9.375M share via curatorship")
  (confidence 0.98)
  (source "User revelation 2025-12-26"))

;;; -----------------------------------------------------------------------------
;;; SECTION 2: ENTITY DEFINITIONS (RECONTEXTUALIZED)
;;; -----------------------------------------------------------------------------

;;; --- 2.1 NATURAL PERSONS ---

(define-entity peter-andrew-faucitt
  (type natural-person)
  (id-number "5103215039082")
  (role-previous "Aggrieved father protecting family business")
  (role-recontextualized "Primary beneficiary seeking 100% of R18.75M payout")
  (trust-role "Founder, Trustee, 50% Beneficiary")
  (motive-connection
    (direct-benefit 9375000)
    (target-benefit 9375000)
    (total-if-scheme-succeeds 18750000))
  (actions
    (interdict-filing "Restrict Jax before payout")
    (medical-testing-demand "Prerequisite for curatorship")
    (family-court-selection "Enable curatorship proceedings")
    (settlement-breach "Ensure control before payout"))
  (confidence 0.98)
  (source "Trust Deed, J246, Court filings"))

(define-entity jacqueline-faucitt
  (type natural-person)
  (id-number "5706070898181")
  (role-previous "First Respondent, alleged co-conspirator")
  (role-recontextualized "Target of curatorship fraud for R9.375M capture")
  (trust-role "Trustee, 50% Beneficiary")
  (motive-connection
    (beneficiary-share 9375000)
    (target-of-scheme #t)
    (loss-if-scheme-succeeds 9375000))
  (vulnerability
    (interdicted #t)
    (medical-testing-demanded #t)
    (curatorship-risk #t))
  (confidence 0.98)
  (source "Trust Deed, J246, Court filings"))

(define-entity daniel-jacobus-bantjes
  (type natural-person)
  (id-number "5810045103089")
  (role-previous "Neutral accountant/trustee")
  (role-recontextualized "Compliant trustee ensuring Peter's majority control")
  (trust-role "Trustee (appointed Jul 2024)")
  (professional-roles
    (accountant-since 2013)
    (cfo-george-group "May 2023"))
  (motive-connection
    (creates-majority-for-peter #t)
    (professional-relationship-kih #t)
    (appointment-hidden-from-daniel #t))
  (conflict-of-interest
    (colleague-of-kih-director #t)
    (kevin-derrick-connection "George Group"))
  (confidence 0.95)
  (source "Trust Deed, J246, B2Bhint"))

(define-entity rynette-farrar
  (type natural-person)
  (role-previous "Employee managing finances")
  (role-recontextualized "Operational executor of payout capture scheme")
  (trust-role "NOT a Trustee - Financial Controller only")
  (motive-connection
    (appointed-bantjes #t)
    (controls-accounts #t)
    (executes-financial-operations #t))
  (actions
    (bantjes-appointment "Jul 2024 - created compliant majority")
    (rezonance-debt-disappearance "Misallocated payments")
    (sage-account-seizure "Post-murder control")
    (account-emptying "Sep 2025"))
  (confidence 0.95)
  (source "Sage screenshots, Email correspondence"))

(define-entity kevin-michael-derrick
  (type natural-person)
  (role-previous "Unrelated director")
  (role-recontextualized "Connection between KIH debt and Bantjies")
  (positions
    (director-kih #t)
    (director-george-group #t))
  (motive-connection
    (kih-owes-fft 18750000)
    (colleague-of-bantjes #t)
    (bantjes-joined-george-group-after-kih-shares #t))
  (confidence 0.90)
  (source "B2Bhint, CIPC records"))

(define-entity kayla-pretorius
  (type natural-person)
  (status "Deceased")
  (date-of-death "2023-07-13")
  (role-previous "Daniel's partner, murder victim")
  (role-recontextualized "Eliminated witness to ReZonance creditor claim")
  (positions
    (co-director-rezonance #t)
    (50-percent-owner-rezonance #t))
  (motive-connection
    (rezonance-owed 1035000)
    (death-eliminates-witness #t)
    (estate-claim-unpaid #t))
  (confidence 0.98)
  (source "Police records, Financial records"))

;;; --- 2.2 JURISTIC PERSONS ---

(define-entity faucitt-family-trust
  (type trust)
  (registration "IT 003651/2013")
  (role-recontextualized "Vehicle for R18.75M payout distribution")
  (trustees
    (peter-andrew-faucitt "Original 2013")
    (jacqueline-faucitt "Original 2013")
    (daniel-jacobus-bantjes "Appointed Jul 2024"))
  (beneficiaries
    (peter-andrew-faucitt 0.50)
    (jacqueline-faucitt 0.50))
  (assets
    (ketoni-shares 5000 "A-Ordinary")
    (ketoni-payout-receivable 18750000))
  (control-structure
    (before-jul-2024 "Peter vs Jax = potential deadlock")
    (after-jul-2024 "Peter + Bantjies vs Jax = Peter majority")
    (after-aug-2025 "Peter + Bantjies vs Jax(interdicted) = total control"))
  (confidence 0.98)
  (source "Trust Deed, J246, Share Certificate"))

(define-entity ketoni-investment-holdings
  (type company)
  (registration "2023/562189/07")
  (incorporation-date "2023-02-20")
  (role-recontextualized "Debtor of R18.75M to FFT")
  (directors
    (kevin-michael-derrick #t))
  (debt-to-fft
    (amount 18750000)
    (due-date "2026-05")
    (type "option"))
  (connection-to-scheme
    (bantjes-colleague-is-director #t)
    (incorporated-before-rezonance-debt-statement #t))
  (confidence 0.90)
  (source "CIPC, Share Certificate, User revelation"))

(define-entity rezonance
  (type company)
  (registration "K2017081396")
  (role-recontextualized "Creditor targeted for elimination before payout")
  (directors
    (daniel-faucitt #t)
    (kayla-pretorius "Deceased 2023-07-13"))
  (debt-owed-by-rst 1035000)
  (scheme-connection
    (dissolution-pressure "Feb 14, 2024")
    (debt-disappearance "2024 misallocation")
    (kayla-murder-eliminates-witness #t))
  (confidence 0.95)
  (source "Financial records, Meeting records"))

;;; -----------------------------------------------------------------------------
;;; SECTION 3: RELATIONS (RECONTEXTUALIZED)
;;; -----------------------------------------------------------------------------

(define-relation ketoni-debt-to-fft
  (type financial-obligation)
  (from ketoni-investment-holdings)
  (to faucitt-family-trust)
  (amount 18750000)
  (due-date "2026-05")
  (significance "CENTRAL MOTIVE - explains all events")
  (confidence 0.98))

(define-relation bantjes-appointment
  (type trust-appointment)
  (appointee daniel-jacobus-bantjes)
  (appointed-by rynette-farrar)
  (date "2024-07")
  (significance-previous "Administrative")
  (significance-recontextualized "Create compliant trustee majority before payout")
  (hidden-from daniel-faucitt)
  (confidence 0.95))

(define-relation peter-jax-interdict
  (type legal-action)
  (applicant peter-andrew-faucitt)
  (respondent jacqueline-faucitt)
  (date "2025-08-13")
  (forum "Family Court")
  (significance-previous "Family dispute")
  (significance-recontextualized "First step in curatorship fraud for R9.375M capture")
  (forum-selection-reason "Family Court enables curatorship; Commercial Court does not")
  (confidence 0.98))

(define-relation medical-testing-demand
  (type legal-demand)
  (demander peter-andrew-faucitt)
  (target jacqueline-faucitt)
  (significance-previous "Bizarre, unexplained")
  (significance-recontextualized "Prerequisite for curatorship declaration")
  (legal-pathway "Testing → Incompetence → Curatorship → Financial control → Payout capture")
  (confidence 0.98))

(define-relation rezonance-dissolution-pressure
  (type coordinated-action)
  (actors (peter-andrew-faucitt daniel-jacobus-bantjes rynette-farrar))
  (target rezonance)
  (date "2024-02-14")
  (significance-previous "Debt avoidance")
  (significance-recontextualized "Eliminate creditor before R18.75M payout")
  (confidence 0.95))

;;; -----------------------------------------------------------------------------
;;; SECTION 4: EVENTS (RECONTEXTUALIZED)
;;; -----------------------------------------------------------------------------

(define-event ketoni-incorporation
  (date "2023-02-20")
  (actors (kevin-michael-derrick))
  (significance-previous "Random investment vehicle")
  (significance-recontextualized "Vehicle for R18.75M debt to FFT")
  (days-before-rezonance-statement 8)
  (confidence 0.95))

(define-event fft-ketoni-investment
  (date "2023-04-24")
  (actors (faucitt-family-trust ketoni-investment-holdings))
  (amount 5000)
  (share-type "A-Ordinary")
  (significance-previous "Trust investment")
  (significance-recontextualized "R18.75M claim established")
  (confidence 0.98))

(define-event kayla-murder
  (date "2023-07-13")
  (victim kayla-pretorius)
  (significance-previous "Tragedy")
  (significance-recontextualized "Eliminates ReZonance creditor claim witness")
  (days-after-kih-shares 80)
  (confidence 0.98))

(define-event card-expiry-except-rwd
  (date "2023-07-31")
  (significance-previous "Administrative")
  (significance-recontextualized "Forces expenses to RWD, obscures trust finances")
  (days-after-kayla-murder 18)
  (confidence 0.90))

(define-event sage-admin-seizure
  (date "2023-post-july")
  (actors (peter-andrew-faucitt rynette-farrar))
  (target "Kayla's RWD Sage Admin account")
  (significance-previous "Administrative")
  (significance-recontextualized "Seize financial control, obstruct murder investigation")
  (confidence 0.90))

(define-event rezonance-dissolution-meeting
  (date "2024-02-14")
  (actors (peter-andrew-faucitt daniel-jacobus-bantjes rynette-farrar))
  (target daniel-faucitt)
  (demand "Wind up ReZonance")
  (significance-previous "Debt avoidance")
  (significance-recontextualized "Eliminate R1.035M creditor before R18.75M payout")
  (confidence 0.95))

(define-event bantjes-trustee-appointment
  (date "2024-07")
  (appointee daniel-jacobus-bantjes)
  (appointed-by rynette-farrar)
  (significance-previous "Administrative")
  (significance-recontextualized "Create compliant trustee majority (Peter + Bantjies vs Jax)")
  (hidden-from daniel-faucitt)
  (months-before-payout 22)
  (confidence 0.95))

(define-event settlement-agreement
  (date "2025-08-11")
  (parties (peter-andrew-faucitt jacqueline-faucitt daniel-faucitt))
  (significance-previous "Resolution")
  (significance-recontextualized "Temporary measure before payout control scheme")
  (confidence 0.98))

(define-event interdict-filing
  (date "2025-08-13")
  (applicant peter-andrew-faucitt)
  (respondents (jacqueline-faucitt daniel-faucitt))
  (forum "Family Court")
  (days-after-settlement 2)
  (months-before-payout 9)
  (significance-previous "Broken settlement")
  (significance-recontextualized "Begin curatorship fraud for R9.375M capture")
  (forum-selection-reason "Family Court enables curatorship; Commercial Court does not")
  (confidence 0.98))

;;; -----------------------------------------------------------------------------
;;; SECTION 5: SCHEME STRUCTURE
;;; -----------------------------------------------------------------------------

(define-scheme curatorship-fraud-for-payout-capture
  (goal "Peter captures 100% of R18.75M Ketoni payout")
  (target-beneficiary jacqueline-faucitt)
  (target-amount 9375000)
  (steps
    (step-1
      (action "Interdict Jax")
      (date "2025-08-13")
      (purpose "Restrict her actions")
      (status "Completed"))
    (step-2
      (action "Demand medical testing")
      (date "2025-08")
      (purpose "Establish incompetence")
      (status "In progress"))
    (step-3
      (action "Apply for curatorship")
      (date "TBD")
      (purpose "Gain legal control")
      (status "Pending"))
    (step-4
      (action "Control trust distributions")
      (date "TBD")
      (purpose "Receive Jax's R9.375M")
      (status "Pending"))
    (step-5
      (action "May 2026 payout")
      (date "2026-05")
      (purpose "Full R18.75M to Peter")
      (status "Future")))
  (actors
    (primary peter-andrew-faucitt)
    (compliant-trustee daniel-jacobus-bantjes)
    (operational-executor rynette-farrar))
  (confidence 0.98))

;;; -----------------------------------------------------------------------------
;;; SECTION 6: LEGAL IMPLICATIONS
;;; -----------------------------------------------------------------------------

(define-legal-aspect fraud
  (type criminal)
  (elements
    (misrepresentation "False mental health claims to court")
    (intent "Capture R9.375M beneficiary share")
    (reliance "Court relies on medical testing demand")
    (damages "Jax loses R9.375M"))
  (confidence 0.95))

(define-legal-aspect curatorship-fraud
  (type criminal)
  (elements
    (false-incompetency-claim "No medical basis for testing demand")
    (financial-motive "R9.375M beneficiary share")
    (timing "9 months before R18.75M payout"))
  (confidence 0.95))

(define-legal-aspect conspiracy
  (type criminal)
  (actors (peter-andrew-faucitt daniel-jacobus-bantjes rynette-farrar))
  (elements
    (agreement "Coordinated scheme")
    (overt-acts "Interdict, medical testing, trustee appointment")
    (goal "Capture R18.75M payout"))
  (confidence 0.95))

(define-legal-aspect abuse-of-process
  (type civil)
  (elements
    (improper-purpose "Curatorship for financial gain")
    (forum-shopping "Family Court instead of Commercial Court"))
  (confidence 0.95))

(define-legal-aspect breach-of-fiduciary-duty
  (type civil)
  (actors (peter-andrew-faucitt daniel-jacobus-bantjes))
  (elements
    (duty "Trustees must act in beneficiary interests")
    (breach "Acting to capture beneficiary share")
    (self-dealing "Peter benefits as both trustee and beneficiary"))
  (confidence 0.95))

;;; -----------------------------------------------------------------------------
;;; SECTION 7: KEY INSIGHT
;;; -----------------------------------------------------------------------------

(define-insight central-revelation
  (statement "The R18.75M Ketoni payout is THE motive that explains everything")
  (implications
    (interdict "Control Jax before payout")
    (family-court "Enable curatorship")
    (medical-testing "Prerequisite for curatorship")
    (bantjes-appointment "Create compliant majority")
    (timing "All actions timed for May 2026 payout"))
  (quote "This is not a free-floating motive. This is THE motive.")
  (confidence 0.98))

;;; =============================================================================
;;; END OF ENTITY-RELATION FRAMEWORK V49
;;; =============================================================================
