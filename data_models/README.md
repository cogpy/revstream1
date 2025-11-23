# Data Models Directory

This directory contains the refined data models for Case 2025-137857.

## Latest Versions (2025-11-23)

- **[entities_refined_2025_11_23_v10.json](entities/entities_refined_2025_11_23_v10.json)** - v17.0
  - 27 entities across 7 types
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

- **[events_refined_2025_11_23_v11.json](events/events_refined_2025_11_23_v11.json)** - v18.0
  - 69 events across 8 phases
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

- **[relations_refined_2025_11_23_v8.json](relations/relations_refined_2025_11_23_v8.json)** - v14.0
  - 60 relations across multiple types
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

- **[timeline_refined_2025_11_23_v9.json](timelines/timeline_refined_2025_11_23_v9.json)** - v15.0
  - 8 phases spanning 2017-2025
  - Enhanced evidence cross-references
  - Direct links to GitHub Pages and ad-res-j7

## Structure

Each data model file contains:

1. **Metadata** - Version, creation date, description, case number, last updated
2. **Data** - Entities, events, relations, or timeline phases
3. **Cross-References** - Links to evidence files, GitHub Pages, and ad-res-j7 repository

## Evidence Integration

All data models now include:

- `evidence_files` - Direct paths to evidence files
- `evidence_repository` - Link to ad-res-j7 repository
- `comprehensive_evidence_index` - Link to comprehensive evidence catalog
- `github_pages_reference` - Link to relevant GitHub Pages documentation
- `ad_res_j7_references` - Specific references to evidence in ad-res-j7

## Extended Evidence Repository

For complete evidence files and documentation, see:
- **Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
- **Evidence Index:** [COMPREHENSIVE_EVIDENCE_INDEX.md](https://github.com/cogpy/ad-res-j7/blob/main/COMPREHENSIVE_EVIDENCE_INDEX.md)

## Version History

- **v17.0 (2025-11-23)** - Entities: Enhanced evidence cross-references, improved GitHub Pages links
- **v18.0 (2025-11-23)** - Events: Enhanced evidence cross-references, improved GitHub Pages links
- **v14.0 (2025-11-23)** - Relations: Enhanced evidence cross-references, improved GitHub Pages links
- **v15.0 (2025-11-23)** - Timeline: Enhanced evidence cross-references, improved GitHub Pages links

## Usage

These JSON files can be:
- Loaded into analysis tools
- Used for hypergraph visualization
- Imported into databases (Supabase, Neon)
- Referenced in legal documentation
- Used for timeline visualization

## Maintenance

Data models are regularly refined and updated. Check the `last_updated` field in the metadata for the most recent modification date.
