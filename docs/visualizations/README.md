# Timeline Visualizations

This directory contains Mermaid diagram files (.mmd) and their rendered PNG images for visualizing various aspects of the Revenue Stream Hijacking case.

## Available Visualizations

### Timeline Diagrams

#### Card Cancellation Timeline
- **Files:** `card_cancellation_timeline.mmd`, `card_cancellation_timeline.png`
- **Description:** Timeline showing the card cancellation events and their impact

#### Comprehensive Timeline
- **Files:** `comprehensive_timeline_2026_01_02.mmd`, `comprehensive_timeline_fixed.mmd`
- **Description:** Complete timeline of all case events

#### Criminal Events Timeline
- **Files:** `criminal_events_timeline_2026_01_02.mmd`, `criminal_events_timeline_fixed.mmd`, `criminal_events_timeline_fixed.png`
- **Description:** Timeline focused on events meeting criminal threshold

#### Criminal Threshold Events Timeline
- **Files:** `criminal_threshold_events_timeline.mmd`, `criminal_threshold_events_timeline.png`
- **Description:** Timeline highlighting events with criminal significance

#### Corrected Expenditure Timeline
- **Files:** `corrected_expenditure_timeline.mmd`, `corrected_expenditure_timeline.png`
- **Description:** Timeline showing corrected expenditure tracking

#### Phase Timeline
- **Files:** `phase_timeline_2026_01_02.mmd`, `phase_timeline_fixed.mmd`
- **Description:** Timeline organized by case phases (setup, fraud, aftermath)

#### Revenue Stream Fraud Timeline
- **Files:** `revenue_stream_fraud_timeline.mmd`, `revenue_stream_fraud_timeline.png`
- **Description:** Timeline focused on revenue stream hijacking events

### Fraud Diagrams

#### CIPC Fraud Timeline
- **Files:** `cipc_fraud_timeline.mmd`, `cipc_fraud_timeline.png`
- **Description:** Timeline of CIPC-related fraud activities

#### Fabricated Accounts Fraud Proof
- **Files:** `fabricated_accounts_fraud_proof.mmd`, `fabricated_accounts_fraud_proof.png`
- **Description:** Diagram proving fabricated accounting fraud

### Network Diagrams

#### Causal Chain Torture
- **Files:** `causal_chain_torture.mmd`, `causal_chain_torture.png`
- **Description:** Complex causal chain showing torture through financial abuse

#### Conspiracy Network Graph
- **Files:** `conspiracy_network_graph.png`
- **Description:** Network graph showing conspiracy relationships between entities

#### Curatorship Conspiracy
- **Files:** `curatorship_conspiracy_flowchart.mmd`, `curatorship_conspiracy_flowchart.png`, `curatorship_conspiracy_timeline.mmd`
- **Description:** Flowchart and timeline of curatorship conspiracy elements

## Rendering Mermaid Diagrams

To render Mermaid diagrams:

### Online
1. Visit [Mermaid Live Editor](https://mermaid.live/)
2. Paste the .mmd file contents
3. Export as PNG/SVG

### Command Line
```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Render diagram
mmdc -i timeline.mmd -o timeline.png
```

### VS Code
- Install "Markdown Preview Mermaid Support" extension
- Open .mmd file and preview

## Updating Diagrams

When updating timelines or diagrams:
1. Edit the .mmd source file
2. Re-render to PNG
3. Update both files in this directory
4. Reference in relevant legal documents

## Usage in Documents

These visualizations are referenced in:
- Legal filings (CIPC complaints, NPA reports)
- Analysis reports
- GitHub Pages documentation
- Evidence presentations

## Notes

- PNG files are generated from .mmd sources
- Keep .mmd and .png files synchronized
- Large diagrams may need size adjustments for documents
- Use high-resolution exports for legal submissions
