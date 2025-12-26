#!/usr/bin/env python3
"""
Comprehensive GitHub Pages update with evidence references
Creates organized structure for Civil, Criminal, and Regulatory applications
Date: 2025-12-21
"""

import json
from pathlib import Path
from datetime import datetime

REVSTREAM_PATH = Path("/home/ubuntu/revstream1")
DOCS_PATH = REVSTREAM_PATH / "docs"
DATA_MODELS_PATH = REVSTREAM_PATH / "data_models"

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def create_index_html():
    """Create main index.html for GitHub Pages"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Case 2025-137857: Revenue Stream Hijacking Evidence Repository</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
        .header p { font-size: 1.1rem; opacity: 0.9; }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #667eea;
            margin-bottom: 1rem;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        .card h3 {
            color: #764ba2;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }
        .applications {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .app-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .app-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .app-card.civil { border-top: 4px solid #3b82f6; }
        .app-card.criminal { border-top: 4px solid #ef4444; }
        .app-card.regulatory { border-top: 4px solid #f59e0b; }
        .app-card h3 { margin-top: 0; }
        .app-card .status {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .status.active { background: #dcfce7; color: #166534; }
        .status.pending { background: #fef3c7; color: #92400e; }
        .evidence-link {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 0.5rem 0.5rem 0.5rem 0;
            transition: background 0.2s;
        }
        .evidence-link:hover { background: #764ba2; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
        }
        .stat-box .number { font-size: 2.5rem; font-weight: bold; }
        .stat-box .label { font-size: 0.875rem; opacity: 0.9; }
        .timeline-link {
            display: block;
            padding: 1rem;
            background: #f3f4f6;
            border-left: 4px solid #667eea;
            margin: 1rem 0;
            text-decoration: none;
            color: #333;
            transition: background 0.2s;
        }
        .timeline-link:hover { background: #e5e7eb; }
        footer {
            text-align: center;
            padding: 2rem;
            color: #666;
            font-size: 0.875rem;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Case 2025-137857</h1>
        <p>Revenue Stream Hijacking: Comprehensive Evidence Repository</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Jacqueline Faucitt & Daniel James Faucitt (Respondents)</p>
    </div>

    <div class="container">
        <div class="card">
            <h2>📊 Case Overview</h2>
            <div class="stats">
                <div class="stat-box">
                    <div class="number">R63M</div>
                    <div class="label">Total Quantum Claimed</div>
                </div>
                <div class="stat-box">
                    <div class="number">12</div>
                    <div class="label">Annexures (JF01-JF12)</div>
                </div>
                <div class="stat-box">
                    <div class="number">9</div>
                    <div class="label">Supplementary Files (SF1-SF9)</div>
                </div>
                <div class="stat-box">
                    <div class="number">95%+</div>
                    <div class="label">Criminal Burden Met</div>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>⚖️ Legal Applications</h2>
            <div class="applications">
                <div class="app-card civil">
                    <h3>Civil Response</h3>
                    <span class="status active">Active</span>
                    <p>Answering affidavit and rescission application responding to Case 2025-137857.</p>
                    <h4 style="margin-top: 1rem; font-size: 0.9rem;">Key Evidence:</h4>
                    <a href="civil-evidence.html" class="evidence-link">View Civil Evidence</a>
                    <a href="https://github.com/cogpy/ad-res-j7/tree/main/1-CIVIL-RESPONSE" class="evidence-link">GitHub Source</a>
                </div>

                <div class="app-card criminal">
                    <h3>Criminal Case</h3>
                    <span class="status pending">Pending Filing</span>
                    <p>Criminal complaints for fraud, identity theft, POPIA violations, and financial crimes.</p>
                    <h4 style="margin-top: 1rem; font-size: 0.9rem;">Complaints:</h4>
                    <a href="criminal-evidence.html" class="evidence-link">View Criminal Evidence</a>
                    <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">GitHub Source</a>
                </div>

                <div class="app-card regulatory">
                    <h3>Regulatory Complaints</h3>
                    <span class="status pending">Pending Filing</span>
                    <p>CIPC Companies Act complaints, POPIA criminal complaints, and NPA tax fraud reports.</p>
                    <h4 style="margin-top: 1rem; font-size: 0.9rem;">Agencies:</h4>
                    <a href="regulatory-evidence.html" class="evidence-link">View Regulatory Evidence</a>
                    <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">GitHub Source</a>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>📅 Timeline & Events</h2>
            <a href="timeline.html" class="timeline-link">
                <strong>Interactive Timeline</strong><br>
                <span style="font-size: 0.875rem; color: #666;">View chronological sequence of events with evidence references</span>
            </a>
            <a href="https://github.com/cogpy/revstream1/blob/main/data_models/timelines/timeline.json" class="timeline-link">
                <strong>Timeline Data (JSON)</strong><br>
                <span style="font-size: 0.875rem; color: #666;">Raw timeline data with complete event details</span>
            </a>
        </div>

        <div class="card">
            <h2>📁 Evidence Repository</h2>
            <h3>Primary Annexures (JF01-JF12)</h3>
            <div style="margin-left: 1rem;">
                <p><strong>JF01:</strong> Shopify Plus Email (26 July 2017) - "Forensic Time Capsule"</p>
                <p><strong>JF02:</strong> Shopify Sales Reports</p>
                <p><strong>JF03:</strong> Financial Records and Analysis</p>
                <p><strong>JF04:</strong> Daniel Faucitt Personal Bank Records</p>
                <p><strong>JF05:</strong> Correspondence Evidence (JF8 Series)</p>
                <p><strong>JF06:</strong> Court Documents and Filings</p>
                <p><strong>JF07:</strong> Screenshots and Visual Evidence</p>
                <p><strong>JF08:</strong> Evidence Packages (May-October 2025)</p>
                <p><strong>JF09:</strong> Timeline Analysis</p>
                <p><strong>JF10:</strong> Additional Supporting Documentation</p>
                <p><strong>JF11:</strong> Communication Records</p>
                <p><strong>JF12:</strong> Business Operations Evidence</p>
            </div>

            <h3 style="margin-top: 1.5rem;">Supplementary Files (SF1-SF9)</h3>
            <div style="margin-left: 1rem;">
                <p><strong>SF1:</strong> Bantjies Debt Documentation</p>
                <p><strong>SF2:</strong> Sage Screenshots - Rynette Control Evidence</p>
                <p><strong>SF3:</strong> Strategic Logistics Stock Adjustment</p>
                <p><strong>SF4:</strong> SARS Audit Email</p>
                <p><strong>SF5:</strong> Adderory Company Registration</p>
                <p><strong>SF6:</strong> Kayla Pretorius Estate Documentation</p>
                <p><strong>SF7:</strong> Court Order - Kayla Email Seizure</p>
                <p><strong>SF8:</strong> Linda Employment Records</p>
                <p><strong>SF9:</strong> Ian Levitt R63M Demand Letter (23 Oct 2025)</p>
            </div>

            <a href="https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES" class="evidence-link" style="margin-top: 1rem;">View All Evidence on GitHub</a>
        </div>

        <div class="card">
            <h2>🔗 Data Models</h2>
            <p>Structured data models for entities, relations, events, and timelines:</p>
            <a href="https://github.com/cogpy/revstream1/tree/main/data_models/entities" class="evidence-link">Entities</a>
            <a href="https://github.com/cogpy/revstream1/tree/main/data_models/relations" class="evidence-link">Relations</a>
            <a href="https://github.com/cogpy/revstream1/tree/main/data_models/events" class="evidence-link">Events</a>
            <a href="https://github.com/cogpy/revstream1/tree/main/data_models/timelines" class="evidence-link">Timelines</a>
        </div>
    </div>

    <footer>
        <p>Case 2025-137857 | Last Updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """ UTC</p>
        <p>Repository: <a href="https://github.com/cogpy/revstream1" style="color: #667eea;">cogpy/revstream1</a> | Evidence: <a href="https://github.com/cogpy/ad-res-j7" style="color: #667eea;">cogpy/ad-res-j7</a></p>
    </footer>
</body>
</html>"""
    
    index_file = DOCS_PATH / "index.html"
    with open(index_file, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created index.html at {index_file}")

def create_civil_evidence_page():
    """Create civil evidence page"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Civil Response Evidence | Case 2025-137857</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #3b82f6;
            margin-bottom: 1rem;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 0.5rem;
        }
        .evidence-item {
            background: #f9fafb;
            border-left: 4px solid #3b82f6;
            padding: 1rem;
            margin: 1rem 0;
        }
        .evidence-item h3 { color: #2563eb; margin-bottom: 0.5rem; }
        .evidence-link {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: #3b82f6;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 0.5rem 0.5rem 0.5rem 0;
            transition: background 0.2s;
        }
        .evidence-link:hover { background: #2563eb; }
        .back-link {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: #6b7280;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        .back-link:hover { background: #4b5563; }
        .burden-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: #dcfce7;
            color: #166534;
            border-radius: 12px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-left: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Civil Response Evidence</h1>
        <p>Case 2025-137857: Answering Affidavit & Rescission Application</p>
    </div>

    <div class="container">
        <a href="index.html" class="back-link">← Back to Main Index</a>

        <div class="card">
            <h2>Overview</h2>
            <p>This page consolidates all evidence supporting the civil response to Case 2025-137857. The civil burden of proof (balance of probabilities - 50%+) has been exceeded for all key claims.</p>
            <p style="margin-top: 1rem;"><strong>Status:</strong> <span class="burden-badge">50%+ Burden Exceeded</span></p>
        </div>

        <div class="card">
            <h2>Key Evidence Items</h2>

            <div class="evidence-item">
                <h3>JF01: Shopify Plus Email (26 July 2017)</h3>
                <p><strong>Significance:</strong> "Forensic Time Capsule" - Irrefutable proof of independent business operations</p>
                <p><strong>Proves:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>Kayla Pretorius personally managed Shopify Plus onboarding</li>
                    <li>Daniel was directly involved (CC'd on communications)</li>
                    <li>Independent business operations (no "head office" involvement)</li>
                    <li>Direct client relationship management</li>
                </ul>
                <p><strong>Refutes:</strong> Applicant's claims of centralized control and Daniel's alleged "delusion"</p>
                <a href="https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES/JF01" class="evidence-link">View JF01</a>
            </div>

            <div class="evidence-item">
                <h3>SF2: Sage Screenshots - Rynette Control Evidence</h3>
                <p><strong>Significance:</strong> Demonstrates identity fraud and unauthorized system access</p>
                <p><strong>Events:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li><strong>SF2A (2025-06-20):</strong> Discovery of Rynette's dual account access (Pete@regima.com AND rynette@regima.zone)</li>
                    <li><strong>SF2B (2025-07-23):</strong> Sage subscription expired, access obstruction for over 1 month</li>
                </ul>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md" class="evidence-link">View SF2</a>
            </div>

            <div class="evidence-item">
                <h3>SF6: Kayla Pretorius Estate Documentation</h3>
                <p><strong>Significance:</strong> Trigger event for revenue stream appropriation</p>
                <p><strong>Context:</strong> Following Kayla's passing, systematic appropriation of business assets and revenue streams commenced</p>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF6_Kayla_Pretorius_Estate_Documentation.md" class="evidence-link">View SF6</a>
            </div>

            <div class="evidence-item">
                <h3>SF9: Ian Levitt R63M Demand Letter (23 Oct 2025)</h3>
                <p><strong>Significance:</strong> Establishes quantum and demonstrates ignored formal demand</p>
                <p><strong>Details:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>R60.25M revenue theft</li>
                    <li>$150K platform fees</li>
                    <li>Total: ~R63M</li>
                    <li>48-hour deadline (ignored)</li>
                </ul>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF9_Ian_Levitt_Demand_Letter.md" class="evidence-link">View SF9</a>
            </div>
        </div>

        <div class="card">
            <h2>Complete Evidence Index</h2>
            <p>All annexures and supplementary files are available in the ad-res-j7 repository:</p>
            <a href="https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES" class="evidence-link">View All Annexures (JF01-JF12)</a>
            <a href="https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES" class="evidence-link">View All Supplementary Files (SF1-SF9)</a>
            <a href="https://github.com/cogpy/ad-res-j7/tree/main/1-CIVIL-RESPONSE" class="evidence-link">View Civil Response Documents</a>
        </div>
    </div>
</body>
</html>"""
    
    civil_file = DOCS_PATH / "civil-evidence.html"
    with open(civil_file, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created civil-evidence.html at {civil_file}")

def create_criminal_evidence_page():
    """Create criminal evidence page"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Criminal Case Evidence | Case 2025-137857</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #ef4444;
            margin-bottom: 1rem;
            border-bottom: 2px solid #ef4444;
            padding-bottom: 0.5rem;
        }
        .crime-category {
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 1rem;
            margin: 1rem 0;
        }
        .crime-category h3 { color: #dc2626; margin-bottom: 0.5rem; }
        .evidence-link {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: #ef4444;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 0.5rem 0.5rem 0.5rem 0;
            transition: background 0.2s;
        }
        .evidence-link:hover { background: #dc2626; }
        .back-link {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: #6b7280;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        .back-link:hover { background: #4b5563; }
        .burden-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: #dcfce7;
            color: #166534;
            border-radius: 12px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-left: 0.5rem;
        }
        .burden-badge.approaching {
            background: #fef3c7;
            color: #92400e;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Criminal Case Evidence</h1>
        <p>Case 2025-137857: Criminal Complaints & POPIA Violations</p>
    </div>

    <div class="container">
        <a href="index.html" class="back-link">← Back to Main Index</a>

        <div class="card">
            <h2>Overview</h2>
            <p>This page consolidates all evidence supporting criminal complaints. The criminal burden of proof (beyond reasonable doubt - 95%+) has been exceeded for identity fraud and is approaching for financial crimes.</p>
            <p style="margin-top: 1rem;">
                <strong>Identity Fraud:</strong> <span class="burden-badge">95%+ Burden Exceeded</span><br>
                <strong>Financial Crimes:</strong> <span class="burden-badge approaching">Approaching 95%</span>
            </p>
        </div>

        <div class="card">
            <h2>Criminal Offenses</h2>

            <div class="crime-category">
                <h3>1. Identity Fraud & Impersonation</h3>
                <p><strong>Evidence:</strong> SF2A - Rynette's dual account access (Pete@regima.com AND rynette@regima.zone)</p>
                <p><strong>Date:</strong> Discovered 2025-06-20</p>
                <p><strong>Legal Basis:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>Identity fraud (Criminal Procedure Act)</li>
                    <li>Unauthorized system access</li>
                    <li>Email impersonation</li>
                </ul>
                <p><strong>Burden of Proof:</strong> <span class="burden-badge">95%+ Exceeded</span></p>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md" class="evidence-link">View Evidence</a>
            </div>

            <div class="crime-category">
                <h3>2. POPIA Violations (Criminal)</h3>
                <p><strong>Evidence:</strong> SF2, SF7 - Unauthorized access to personal information and email accounts</p>
                <p><strong>Violations:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>Unlawful processing of personal information</li>
                    <li>Unauthorized access to email accounts</li>
                    <li>Failure to secure personal information</li>
                </ul>
                <p><strong>Burden of Proof:</strong> <span class="burden-badge">95%+ Exceeded</span></p>
                <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">View POPIA Complaint</a>
            </div>

            <div class="crime-category">
                <h3>3. Fraud & Financial Crimes</h3>
                <p><strong>Evidence:</strong> SF9, JF01-JF08 - R63M revenue theft scheme</p>
                <p><strong>Components:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>R60.25M revenue theft</li>
                    <li>$150K platform fees misappropriation</li>
                    <li>Coordinated fraud scheme</li>
                    <li>Trust asset misappropriation</li>
                </ul>
                <p><strong>Burden of Proof:</strong> <span class="burden-badge approaching">Approaching 95%</span></p>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF9_Ian_Levitt_Demand_Letter.md" class="evidence-link">View SF9</a>
            </div>

            <div class="crime-category">
                <h3>4. Obstruction & Section 163 Oppression</h3>
                <p><strong>Evidence:</strong> SF2B - Sage subscription expiry and access obstruction</p>
                <p><strong>Date:</strong> 2025-07-23 (over 1 month denial of access)</p>
                <p><strong>Legal Basis:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>Section 163 Companies Act - oppression</li>
                    <li>Denial of access to company records</li>
                    <li>Obstruction of business operations</li>
                </ul>
                <p><strong>Burden of Proof:</strong> <span class="burden-badge">95%+ Exceeded</span></p>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/ANNEXURES/SF2_Sage_Screenshots_Rynette_Control.md" class="evidence-link">View Evidence</a>
            </div>
        </div>

        <div class="card">
            <h2>Criminal Complaints</h2>
            <p>Formal criminal complaints have been prepared for filing:</p>
            <a href="https://github.com/cogpy/ad-res-j7/blob/main/2-CRIMINAL-CASE/POPIA_Criminal_Complaint.md" class="evidence-link">POPIA Criminal Complaint</a>
            <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">View All Criminal Case Documents</a>
        </div>
    </div>
</body>
</html>"""
    
    criminal_file = DOCS_PATH / "criminal-evidence.html"
    with open(criminal_file, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created criminal-evidence.html at {criminal_file}")

def create_regulatory_evidence_page():
    """Create regulatory evidence page"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Regulatory Complaints Evidence | Case 2025-137857</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card h2 {
            color: #f59e0b;
            margin-bottom: 1rem;
            border-bottom: 2px solid #f59e0b;
            padding-bottom: 0.5rem;
        }
        .regulatory-item {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 1rem;
            margin: 1rem 0;
        }
        .regulatory-item h3 { color: #d97706; margin-bottom: 0.5rem; }
        .evidence-link {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: #f59e0b;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 0.5rem 0.5rem 0.5rem 0;
            transition: background 0.2s;
        }
        .evidence-link:hover { background: #d97706; }
        .back-link {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            background: #6b7280;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        .back-link:hover { background: #4b5563; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Regulatory Complaints Evidence</h1>
        <p>Case 2025-137857: CIPC, POPIA, NPA & Other Regulatory Actions</p>
    </div>

    <div class="container">
        <a href="index.html" class="back-link">← Back to Main Index</a>

        <div class="card">
            <h2>Overview</h2>
            <p>This page consolidates all evidence supporting regulatory complaints to various authorities including CIPC, Information Regulator, NPA, and SARS.</p>
        </div>

        <div class="card">
            <h2>Regulatory Complaints</h2>

            <div class="regulatory-item">
                <h3>1. CIPC Companies Act Complaint</h3>
                <p><strong>Authority:</strong> Companies and Intellectual Property Commission</p>
                <p><strong>Basis:</strong> Section 163 - Oppression and unfair prejudice</p>
                <p><strong>Key Evidence:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>SF2B - Denial of access to company records (Sage accounting)</li>
                    <li>JF04 - CIPC company registration documents</li>
                    <li>JF06 - Court documents showing pattern of oppression</li>
                </ul>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/2-CRIMINAL-CASE/CIPC_Companies_Act_Complaint.md" class="evidence-link">View CIPC Complaint</a>
            </div>

            <div class="regulatory-item">
                <h3>2. POPIA Criminal Complaint (Information Regulator)</h3>
                <p><strong>Authority:</strong> Information Regulator of South Africa</p>
                <p><strong>Violations:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>Unlawful processing of personal information</li>
                    <li>Unauthorized access to email accounts (SF7)</li>
                    <li>Identity fraud (SF2A)</li>
                    <li>Failure to secure personal information</li>
                </ul>
                <a href="https://github.com/cogpy/ad-res-j7/blob/main/2-CRIMINAL-CASE/POPIA_Criminal_Complaint.md" class="evidence-link">View POPIA Complaint</a>
            </div>

            <div class="regulatory-item">
                <h3>3. NPA Tax Fraud Report</h3>
                <p><strong>Authority:</strong> National Prosecuting Authority - Priority Crimes Litigation Unit</p>
                <p><strong>Allegations:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>R63M revenue theft with tax implications</li>
                    <li>Unreported income from misappropriated revenue</li>
                    <li>Trust asset misappropriation</li>
                    <li>SARS audit implications (SF4)</li>
                </ul>
                <p><strong>Key Evidence:</strong> SF9, JF03, SF4</p>
                <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">View Tax Fraud Evidence</a>
            </div>

            <div class="regulatory-item">
                <h3>4. Commercial Crime Case Submission</h3>
                <p><strong>Authority:</strong> SAPS Commercial Crime Unit</p>
                <p><strong>Offenses:</strong></p>
                <ul style="margin-left: 2rem; margin-top: 0.5rem;">
                    <li>Fraud (R63M)</li>
                    <li>Identity theft and impersonation</li>
                    <li>Unauthorized access to computer systems</li>
                    <li>Theft of business assets</li>
                </ul>
                <p><strong>Quantum:</strong> R63,000,000 (established by SF9)</p>
                <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">View Commercial Crime Evidence</a>
            </div>
        </div>

        <div class="card">
            <h2>Supporting Evidence Index</h2>
            <p>All evidence supporting regulatory complaints:</p>
            <a href="https://github.com/cogpy/ad-res-j7/tree/main/ANNEXURES" class="evidence-link">View All Annexures</a>
            <a href="https://github.com/cogpy/ad-res-j7/tree/main/2-CRIMINAL-CASE" class="evidence-link">View Regulatory Documents</a>
        </div>
    </div>
</body>
</html>"""
    
    regulatory_file = DOCS_PATH / "regulatory-evidence.html"
    with open(regulatory_file, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Created regulatory-evidence.html at {regulatory_file}")

def update_timeline_html():
    """Update timeline.html with new events"""
    
    # Load timeline data
    timeline_file = DATA_MODELS_PATH / "timelines" / "timeline.json"
    timeline_data = load_json(timeline_file)
    
    # Generate timeline HTML
    timeline_html = """<!DOCTYPE html>
<html>
<head>
<title>Case Timeline - Revenue Stream Hijacking</title>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; background: #f5f5f5; padding: 2rem; }
.header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; text-align: center; border-radius: 8px; margin-bottom: 2rem; }
.timeline { position: relative; max-width: 1200px; margin: 0 auto; }
.timeline::after { content: ''; position: absolute; width: 6px; background-color: #667eea; top: 0; bottom: 0; left: 50%; margin-left: -3px; }
.container { padding: 10px 40px; position: relative; background-color: inherit; width: 50%; }
.left { left: 0; }
.right { left: 50%; }
.left::before, .right::before { content: " "; height: 0; position: absolute; top: 22px; width: 0; z-index: 1; border: medium solid white; border-width: 10px 0 10px 10px; border-color: transparent transparent transparent white; }
.right::before { border-width: 10px 10px 10px 0; border-color: transparent white transparent transparent; left: 60px; }
.left::before { right: 60px; }
.right::after, .left::after { content: ''; position: absolute; width: 25px; height: 25px; right: -17px; background-color: white; border: 4px solid #667eea; top: 15px; border-radius: 50%; z-index: 1; }
.right::after { left: -16px; }
.content { padding: 20px 30px; background-color: white; position: relative; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.content h2 { color: #667eea; margin-top: 0; }
.content h3 { color: #764ba2; margin-top: 0; }
.badge { display: inline-block; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.875rem; font-weight: 600; margin: 0.25rem; }
.badge.criminal { background: #fee2e2; color: #991b1b; }
.badge.civil { background: #dbeafe; color: #1e40af; }
.badge.legal { background: #fef3c7; color: #92400e; }
.back-link { display: inline-block; padding: 0.75rem 1.5rem; background: #6b7280; color: white; text-decoration: none; border-radius: 4px; margin-bottom: 1rem; }
.back-link:hover { background: #4b5563; }
</style>
</head>
<body>
<div class="header">
<h1>Case Timeline: Revenue Stream Hijacking</h1>
<p>Case 2025-137857: Chronological Sequence of Events</p>
</div>
<a href="index.html" class="back-link">← Back to Main Index</a>
<div class="timeline">"""
    
    # Add events from timeline
    events = timeline_data.get("timeline", [])
    for i, event in enumerate(events):
        side = "left" if i % 2 == 0 else "right"
        
        # Determine badge based on category
        category = event.get("category", "")
        if "criminal" in category or "fraud" in category:
            badge_class = "criminal"
        elif "legal" in category:
            badge_class = "legal"
        else:
            badge_class = "civil"
        
        timeline_html += f"""
<div class="container {side}">
    <div class="content">
        <h2>{event.get('date', 'Unknown Date')}</h2>
        <h3>{event.get('title', 'Untitled Event')}</h3>
        <p>{event.get('description', '')}</p>
        <p><b>Category:</b> <span class="badge {badge_class}">{event.get('category', 'N/A')}</span><br>
        <b>Significance:</b> {event.get('significance', 'N/A')}<br>
        <b>Evidence:</b> {', '.join(event.get('evidence', [])) if event.get('evidence') else 'N/A'}</p>
    </div>
</div>"""
    
    timeline_html += """
</div>
</body>
</html>"""
    
    timeline_html_file = DOCS_PATH / "timeline.html"
    with open(timeline_html_file, 'w') as f:
        f.write(timeline_html)
    
    print(f"✓ Updated timeline.html at {timeline_html_file}")

def main():
    print("=" * 80)
    print("GITHUB PAGES COMPREHENSIVE UPDATE")
    print("Date: 2025-12-21")
    print("=" * 80)
    print()
    
    print("Creating main index page...")
    create_index_html()
    print()
    
    print("Creating civil evidence page...")
    create_civil_evidence_page()
    print()
    
    print("Creating criminal evidence page...")
    create_criminal_evidence_page()
    print()
    
    print("Creating regulatory evidence page...")
    create_regulatory_evidence_page()
    print()
    
    print("Updating timeline page...")
    update_timeline_html()
    print()
    
    print("=" * 80)
    print("GITHUB PAGES UPDATE COMPLETE")
    print("=" * 80)
    print()
    print("Pages created:")
    print("  • index.html - Main landing page")
    print("  • civil-evidence.html - Civil response evidence")
    print("  • criminal-evidence.html - Criminal case evidence")
    print("  • regulatory-evidence.html - Regulatory complaints evidence")
    print("  • timeline.html - Interactive timeline")
    print()

if __name__ == "__main__":
    main()
