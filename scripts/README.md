# Scripts Directory

This directory contains Python scripts used for analyzing, enhancing, and refining the data models and legal documents for the Revenue Stream Hijacking case.

## Directory Structure

### `/analysis/`
Scripts for analyzing data models, timeline, evidence, and relationships:
- Timeline analysis and validation
- Cross-reference analysis  
- Evidence scanning
- Data integrity checks
- Audit scripts

### `/enhancement/`
Scripts for enhancing data models with additional information:
- Entity enhancements
- Event enhancements
- Relation enhancements
- Timeline enhancements
- Data model enhancements

### `/refinement/`
Scripts for refining data models and legal documents:
- Data model refinements
- Legal filing refinements
- Comprehensive refinement scripts

### `/generation/`
Scripts for generating reports, updates, and legal documents:
- Legal filing generation
- Report generation
- GitHub Pages updates
- Documentation organization
- Integration scripts

### `/archive/`
Older versions of scripts kept for reference

## Usage

Most scripts can be run directly from the command line:

```bash
# Analysis scripts
python3 scripts/analysis/analyze_timeline_improvements.py
python3 scripts/analysis/audit_and_fix_timeline.py

# Enhancement scripts
python3 scripts/enhancement/enhance_entities.py
python3 scripts/enhancement/enhance_timeline.py

# Refinement scripts
python3 scripts/refinement/refine_legal_filings_2026_01_22.py
python3 scripts/refinement/refine_data_models_2026_01_22.py

# Generation scripts
python3 scripts/generation/generate_all_filings_2026_01_22.py
```

## Script Naming Convention

Scripts follow a naming pattern that indicates their purpose and date:
- `[action]_[target]_[date].py` - Dated scripts (e.g., `refine_legal_filings_2026_01_22.py`)
- `[action]_[target].py` - Generic scripts (e.g., `enhance_entities.py`)

## Dependencies

Most scripts depend on:
- Python 3.x
- JSON file handling
- Data models in `/data_models/`
- Evidence in `/evidence/`
- Legal documents in `/docs/`

## Notes

- Scripts with dates are typically iteration-specific
- Generic scripts are more general-purpose
- Always backup data before running modification scripts
- Check script comments for specific usage instructions
