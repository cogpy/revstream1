#!/usr/bin/env python3.11
"""
Refine legal filings based on the latest evidence and analysis.
"""
import json
from datetime import datetime
from pathlib import Path

def load_data():
    """Load entities, relations, and events data."""
    base_path = Path("/home/ubuntu/revstream1/data_models")
    with open(base_path / "events/events.json", "r") as f:
        events = json.load(f)["events"]
    return events

def generate_cipc_complaint(events):
    """Generate the refined CIPC complaint."""
    criminal_events = [e for e in events if "criminal" in e.get("burden_of_proof", "").lower() or "95%" in e.get("burden_of_proof", "")]
    civil_events = [e for e in events if "exceeded" in e.get("burden_of_proof", "").lower()]

    content = f"""# CIPC Complaint: Delinquent Director Application (Section 162)

**Date:** {datetime.now().strftime("%Y-%m-%d")}
**Case:** 2025-137857
**Subject:** Application for a declaration of delinquency against Peter Andrew Faucitt and Rynette Farrar.

---

## 1. Introduction

This complaint is filed to request that the Companies and Intellectual Property Commission (CIPC) investigate the conduct of Peter Andrew Faucitt and Rynette Farrar and declare them delinquent directors under Section 162 of the Companies Act, 71 of 2008.

The evidence demonstrates a consistent pattern of gross abuse of position, misappropriation of assets, and fraudulent conduct that has caused significant harm to RegimA Zone Ltd and its stakeholders.

## 2. Summary of Offenses

The following is a summary of the key offenses, supported by extensive evidence:

*   **Financial Fraud:** Manipulation of accounting records to conceal the theft of revenue.
*   **Unauthorized Transfers:** Diversion of over R10 million in revenue to accounts controlled by the perpetrators.
*   **Trust Violations:** Abuse of fiduciary duties as trustees of the Faucitt Family Trust.
*   **POPIA Violations:** Unlawful access to and use of personal information.
*   **Tax Evasion:** Failure to declare and pay taxes on the diverted revenue.
*   **Director Misconduct:** Gross abuse of the position of director for personal gain.
*   **Conspiracy:** Coordinated actions to defraud the company and its stakeholders.

## 3. Burden of Proof Analysis

### Criminal Threshold (95%)

**{len(criminal_events)} events** meet the criminal threshold, with conclusive evidence:

"""
    for event in criminal_events[:5]:
        content += f"*   **{event['date']}**: {event['description']}\n"

    content += f"""\n### Civil Threshold (50%+)

**{len(civil_events)} events** exceed the civil threshold, demonstrating a clear pattern of misconduct:

"""
    for event in civil_events[:5]:
       content += f"*   **{event['date']}**: {event['description']}\n"
    content += """\n---\n
## 4. Conclusion

The evidence is overwhelming and demonstrates a clear case for the delinquency of Peter Faucitt and Rynette Farrar. We urge the CIPC to act swiftly to protect the public and the integrity of the South African business environment.

*This document is supported by the evidence cataloged in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).*
"""

    return content

def generate_popia_complaint(events):
    """Generate the refined POPIA complaint."""
    popia_events = [e for e in events if "popia" in e.get("description", "").lower()]

    content = f"""# POPIA Complaint: Unlawful Processing of Personal Information

**Date:** {datetime.now().strftime("%Y-%m-%d")}
**Case:** 2025-137857
**Subject:** Complaint against Peter Andrew Faucitt and Rynette Farrar for violations of the Protection of Personal Information Act (POPIA).

---

## 1. Introduction

This complaint details the unlawful processing of personal information by Peter Andrew Faucitt and Rynette Farrar, in contravention of the Protection of Personal Information Act (POPIA).

## 2. Summary of Violations

The perpetrators have engaged in the following violations:

*   **Unlawful Access:** Gaining unauthorized access to personal information, including email accounts and financial records.
*   **Identity Fraud:** Using personal information to register fraudulent domain names and impersonate individuals.
*   **Failure to Secure:** Negligently failing to protect personal information from unauthorized access and use.

## 3. Key Events

"""
    for event in popia_events[:5]:
        content += f"*   **{event['date']}**: {event['description']}\n"

    content += """\n---\n
## 4. Conclusion

The evidence clearly shows a disregard for the protection of personal information. We request that the Information Regulator investigate these violations and take appropriate action.

*This document is supported by the evidence cataloged in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).*
"""

    return content

def generate_npa_report(events):
    """Generate the refined NPA Tax Fraud report."""
    tax_events = [e for e in events if "tax" in e.get("description", "").lower() or "sars" in e.get("description", "").lower()]

    content = f"""# NPA Tax Fraud Report

**Date:** {datetime.now().strftime("%Y-%m-%d")}
**Case:** 2025-137857
**Subject:** Report of tax fraud and related financial crimes by Peter Andrew Faucitt and Rynette Farrar.

---

## 1. Introduction

This report outlines a systematic scheme of tax evasion and financial fraud perpetrated by Peter Andrew Faucitt and Rynette Farrar.

## 2. Summary of Crimes

*   **Tax Evasion:** Failure to declare and pay taxes on over R10 million in diverted revenue.
*   **Fraud:** Intentional misrepresentation and concealment of financial information to deceive SARS.
*   **Money Laundering:** Disguising the proceeds of crime through a complex web of inter-company transactions.

## 3. Key Events

"""
    for event in tax_events[:5]:
        content += f"*   **{event['date']}**: {event['description']}\n"

    content += """\n---\n
## 4. Conclusion

The evidence points to a deliberate and sophisticated tax fraud scheme. We urge the National Prosecuting Authority (NPA) to investigate and prosecute these crimes to the fullest extent of the law.

*This document is supported by the evidence cataloged in the [ad-res-j7 repository](https://github.com/cogpy/ad-res-j7).*
"""

    return content

def main():
    """Main execution function."""
    events = load_data()
    docs_path = Path("/home/ubuntu/revstream1/docs/filings")
    docs_path.mkdir(exist_ok=True, parents=True)

    # Generate CIPC complaint
    print("Generating refined CIPC complaint...")
    cipc_complaint = generate_cipc_complaint(events)
    with open(docs_path / "CIPC_COMPLAINT_REFINED_2026_01_02.md", "w") as f:
        f.write(cipc_complaint)
    print("  Saved: CIPC_COMPLAINT_REFINED_2026_01_02.md")

    # Generate POPIA complaint
    print("Generating refined POPIA complaint...")
    popia_complaint = generate_popia_complaint(events)
    with open(docs_path / "POPIA_COMPLAINT_REFINED_2026_01_02.md", "w") as f:
        f.write(popia_complaint)
    print("  Saved: POPIA_COMPLAINT_REFINED_2026_01_02.md")

    # Generate NPA report
    print("Generating refined NPA Tax Fraud report...")
    npa_report = generate_npa_report(events)
    with open(docs_path / "NPA_TAX_FRAUD_REPORT_REFINED_2026_01_02.md", "w") as f:
        f.write(npa_report)
    print("  Saved: NPA_TAX_FRAUD_REPORT_REFINED_2026_01_02.md")

    print("\nLegal filings refinement complete!")

if __name__ == "__main__":
    main()
