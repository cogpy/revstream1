# Application 3: External Validation

**Last Updated:** 2026-01-05

## Overview

This application provides a comprehensive package for independent verification and external expert review.

**Purpose:** Enable external validators to independently verify the analysis, methodology, and conclusions.

## Data Models

### Current Versions

| Model | Version | Last Updated | Entities/Items |
| :--- | :--- | :--- | :--- |
| Entities | 22.1_REFINED_2026_01_05 | 2026-01-05 | 33 |
| Relations | 18.1_REFINED_2026_01_05 | 2026-01-05 | 75 |
| Events | 21.1_REFINED_2026_01_05 | 2026-01-05 | 77 |
| Timeline | 18.1_ENHANCED_2026_01_05 | 2026-01-05 | 56 entries |

### Modeling Approach

- **Entity Modeling:** Agentic entity modeling (each entity modeled as an agent)
- **Relations:** Hypergraph-compatible relations
- **Evidence:** Rigorously verified against primary source documents
- **Methodology:** Continuous refinement based on new evidence

## Verification Checklist

### Data Integrity
- ✓ All entities have evidence references
- ✓ All events have burden of proof classifications
- ✓ All timeline entries have evidence references
- ✓ All relations have evidence backing

### Evidence Completeness
- ✓ 46 events meet criminal threshold (95%)
- ✓ 31 events meet civil threshold (50%)
- ✓ All SF evidence (SF1-SF9) cataloged and referenced
- ✓ All JF annexures (JF01-JF09) indexed

### Cross-Reference Accuracy
- ✓ Entities linked to events
- ✓ Events linked to timeline
- ✓ Timeline linked to evidence
- ✓ Evidence linked to applications

## Validation Methodology

### 1. Entity Verification
Review each entity in [entities.json](../data_models/entities/entities.json) against:
- Primary source documents in ad-res-j7/ANNEXURES
- CIPC company records
- Court filings
- Financial records

### 2. Event Verification
Review each event in [events.json](../data_models/events/events.json) against:
- Timeline entries
- Evidence references
- Burden of proof standards
- Legal significance classifications

### 3. Timeline Verification
Review timeline in [timeline.json](../data_models/timelines/timeline.json) against:
- Source documents
- Date accuracy
- Event clustering
- Phase transitions

### 4. Evidence Verification
Review evidence catalog against:
- Actual files in ad-res-j7 repository
- Cross-references in data models
- Application requirements
- Legal standards

## Visualizations for Verification

Use these visualizations to verify timeline accuracy and relationship mapping:

- [Comprehensive Timeline](comprehensive_timeline.png)
- [Criminal Events Timeline](criminal_events_timeline_fixed.png)
- [Conspiracy Network Graph](conspiracy_network_graph.png)
- [Curatorship Conspiracy Flowchart](curatorship_conspiracy_flowchart.png)

## Application Documents

Located in [ad-res-j7/3-EXTERNAL-VALIDATION](https://github.com/cogpy/ad-res-j7/tree/main/3-EXTERNAL-VALIDATION):

- External Validation Package
- Methodology Documentation
- Agent Mapping
- Arena Mapping

## Contact for Validation

For external validation inquiries or to report discrepancies, please open an issue in the [revstream1 repository](https://github.com/cogpy/revstream1/issues).

[← Back to Main Index](index.md)
