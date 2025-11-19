# Data Model Updates - 2025-11-19

## Summary

The data models for Case 2025-137857 have been comprehensively refined and updated to version 11.0.

## Changes Made

### Entities (Version 11.0)
- ✓ Added evidence references to 9 key entities
- ✓ Enhanced ad-res-j7 cross-references
- ✓ Added evidence repository links
- ✓ New fields: `evidence_files`, `ad_res_j7_references`, `evidence_repository`

### Events (Version 11.0)
- ✓ Added perpetrators to 7 events (EVT-063 through EVT-069)
- ✓ Enhanced application mappings for all events
- ✓ New field: `related_applications`

### Timeline (Version 10.0)
- ✓ Resolved PHASE_005 duplication
- ✓ Renamed second PHASE_005 to PHASE_007 (Debt Accumulation Phase)
- ✓ Enhanced application mappings

### Relations (Version 9.0)
- ✓ Enhanced application mappings for all 24 relations
- ✓ Added evidence repository links
- ✓ New fields: `related_applications`, `evidence_repository`

## Files Updated

- `data_models/entities/entities_refined_2025_11_19_v3.json`
- `data_models/events/events_refined_2025_11_19_v3.json`
- `data_models/timelines/timeline_refined_2025_11_19_v3.json`
- `data_models/relations/relations_refined_2025_11_19_v3.json`

## GitHub Pages Updates

- ✓ Created enhanced evidence index with application-specific organization
- ✓ Updated main index with version information
- ✓ Improved evidence navigation and cross-referencing

## Evidence Integration

All entities now have direct references to evidence files in the ad-res-j7 repository:

- **Total evidence files:** 2,866 (226.78 MB)
- **Evidence codes:** JF (978), JAX (927), JF01-JF07 (266)
- **Repository:** https://github.com/cogpy/ad-res-j7

## Next Steps

1. Review the enhanced evidence index
2. Verify all cross-references are accurate
3. Sync changes to GitHub repository
4. Update GitHub Pages deployment

---

**Date:** 2025-11-19  
**Version:** 11.0  
**Status:** Complete
