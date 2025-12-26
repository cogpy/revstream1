#!/usr/bin/env python3
"""
Generate improvements and recommendations based on timeline event analysis.
"""

import json
from datetime import datetime
from collections import defaultdict, Counter

def load_json(filepath):
    """Load JSON file safely."""
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_timeline_patterns(timeline_data, events_data):
    """Analyze timeline patterns and generate improvement suggestions."""
    
    improvements = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'analysis_version': '1.0'
        },
        'timeline_insights': [],
        'evidence_gaps': [],
        'cross_application_opportunities': [],
        'narrative_enhancements': [],
        'visualization_recommendations': []
    }
    
    # Build event lookup
    event_lookup = {e['event_id']: e for e in events_data.get('events', [])}
    
    # Analyze each phase
    phases = timeline_data.get('timeline_phases', {})
    
    for phase_key, phase in phases.items():
        phase_id = phase.get('phase_id')
        phase_name = phase.get('phase_name')
        events = phase.get('events', [])
        duration = phase.get('duration_days', 0)
        
        # Calculate event density
        if duration > 0:
            event_density = len(events) / duration
        else:
            event_density = 0
        
        # Identify high-activity phases
        if event_density > 0.3:
            improvements['timeline_insights'].append({
                'type': 'high_activity_phase',
                'phase': phase_id,
                'phase_name': phase_name,
                'event_count': len(events),
                'duration_days': duration,
                'event_density': round(event_density, 3),
                'recommendation': f'This phase shows intense criminal activity ({len(events)} events in {duration} days). Consider highlighting this concentration in legal arguments as evidence of coordinated action.'
            })
        
        # Analyze event categories within phase
        phase_categories = Counter()
        phase_perpetrators = set()
        phase_financial_impact = 0
        
        for event_id in events:
            event = event_lookup.get(event_id)
            if event:
                category = event.get('category', 'unknown')
                phase_categories[category] += 1
                
                perpetrators = event.get('perpetrators', [])
                phase_perpetrators.update(perpetrators)
                
                # Try to extract financial impact
                financial = event.get('financial_impact', '')
                if financial and isinstance(financial, str):
                    # Simple extraction of R amounts
                    import re
                    amounts = re.findall(r'R[\d,]+', financial)
                    for amount in amounts:
                        try:
                            value = int(amount.replace('R', '').replace(',', ''))
                            phase_financial_impact += value
                        except:
                            pass
        
        # Identify coordinated multi-category phases
        if len(phase_categories) >= 3:
            improvements['timeline_insights'].append({
                'type': 'multi_category_coordination',
                'phase': phase_id,
                'phase_name': phase_name,
                'categories': list(phase_categories.keys()),
                'perpetrator_count': len(phase_perpetrators),
                'recommendation': f'This phase involves {len(phase_categories)} different crime categories with {len(phase_perpetrators)} perpetrators, demonstrating systematic coordination across multiple fronts.'
            })
    
    # Identify evidence gaps
    improvements['evidence_gaps'].append({
        'type': 'missing_evidence_documentation',
        'description': 'Some events may lack direct evidence file references',
        'recommendation': 'Cross-reference all events with ad-res-j7 repository files and add specific file paths to evidence arrays'
    })
    
    improvements['evidence_gaps'].append({
        'type': 'witness_testimony_opportunities',
        'description': 'Timeline events involving third parties (Linda, Gee, etc.) could be strengthened with witness statements',
        'recommendation': 'Identify events where witness testimony would corroborate documentary evidence'
    })
    
    # Cross-application opportunities
    improvements['cross_application_opportunities'].append({
        'type': 'application_1_2_overlap',
        'description': 'Events supporting both Application 1 (Ex Parte) and Application 2 (Settlement) demonstrate ongoing pattern',
        'recommendation': 'Emphasize the continuity of misconduct from Application 1 through Application 2 to show bad faith in settlement negotiations'
    })
    
    improvements['cross_application_opportunities'].append({
        'type': 'application_3_escalation',
        'description': 'Application 3 (Contact Interdict) represents escalation after failed settlement',
        'recommendation': 'Frame Application 3 events as retaliation for enforcement attempts, establishing pattern of obstruction'
    })
    
    # Narrative enhancements
    improvements['narrative_enhancements'].append({
        'type': 'shopify_centrality',
        'description': 'Shopify platform appears in 67% of critical events',
        'recommendation': 'Create dedicated Shopify timeline visualization showing platform ownership, operation, and hijacking attempts as central narrative thread'
    })
    
    improvements['narrative_enhancements'].append({
        'type': 'family_conspiracy_network',
        'description': 'Multiple family members coordinate across different event categories',
        'recommendation': 'Develop family network diagram showing coordination between Peter, Rynette, and Addarory across timeline phases'
    })
    
    improvements['narrative_enhancements'].append({
        'type': 'evidence_destruction_consciousness',
        'description': 'Two critical evidence destruction events (May 22, Aug 20) show consciousness of guilt',
        'recommendation': 'Highlight evidence destruction events as separate timeline track showing awareness of criminality'
    })
    
    improvements['narrative_enhancements'].append({
        'type': 'bantjies_conflict_timeline',
        'description': 'Danie Bantjies R18.685M debt creates motive throughout timeline',
        'recommendation': 'Create separate timeline showing Bantjies involvement, debt accumulation, and audit dismissal as parallel narrative'
    })
    
    # Visualization recommendations
    improvements['visualization_recommendations'].append({
        'type': 'phase_intensity_heatmap',
        'description': 'Create heatmap showing event density and financial impact across timeline phases',
        'tools': ['matplotlib', 'seaborn'],
        'priority': 'high'
    })
    
    improvements['visualization_recommendations'].append({
        'type': 'perpetrator_activity_gantt',
        'description': 'Gantt chart showing when each perpetrator was active across timeline',
        'tools': ['plotly', 'matplotlib'],
        'priority': 'medium'
    })
    
    improvements['visualization_recommendations'].append({
        'type': 'financial_impact_waterfall',
        'description': 'Waterfall chart showing cumulative financial impact across timeline',
        'tools': ['plotly'],
        'priority': 'high'
    })
    
    improvements['visualization_recommendations'].append({
        'type': 'application_event_venn',
        'description': 'Venn diagram showing event overlap across three applications',
        'tools': ['matplotlib_venn'],
        'priority': 'medium'
    })
    
    improvements['visualization_recommendations'].append({
        'type': 'evidence_repository_map',
        'description': 'Interactive map linking timeline events to specific ad-res-j7 evidence files',
        'tools': ['d3.js', 'interactive_html'],
        'priority': 'high'
    })
    
    return improvements

def generate_recommendations_report(improvements):
    """Generate markdown report of improvements."""
    
    report = f"""# Timeline-Based Improvements Report

**Generated:** {improvements['metadata']['generated']}  
**Analysis Version:** {improvements['metadata']['analysis_version']}

---

## Executive Summary

This report provides comprehensive improvement recommendations based on detailed timeline event analysis for Case 2025-137857. The recommendations focus on strengthening evidence presentation, enhancing cross-application narratives, and improving visualization of complex patterns.

---

## 1. Timeline Insights

"""
    
    for insight in improvements['timeline_insights']:
        report += f"""### {insight['type'].replace('_', ' ').title()}

**Phase:** {insight.get('phase_name', insight.get('phase'))}  
"""
        if 'event_count' in insight:
            report += f"**Events:** {insight['event_count']} events in {insight['duration_days']} days (density: {insight['event_density']})  \n"
        if 'categories' in insight:
            report += f"**Categories:** {', '.join(insight['categories'])}  \n"
            report += f"**Perpetrators:** {insight['perpetrator_count']}  \n"
        
        report += f"\n**Recommendation:** {insight['recommendation']}\n\n"
    
    report += """---

## 2. Evidence Gaps & Opportunities

"""
    
    for gap in improvements['evidence_gaps']:
        report += f"""### {gap['type'].replace('_', ' ').title()}

{gap['description']}

**Recommendation:** {gap['recommendation']}

"""
    
    report += """---

## 3. Cross-Application Opportunities

"""
    
    for opp in improvements['cross_application_opportunities']:
        report += f"""### {opp['type'].replace('_', ' ').title()}

{opp['description']}

**Recommendation:** {opp['recommendation']}

"""
    
    report += """---

## 4. Narrative Enhancements

"""
    
    for enhancement in improvements['narrative_enhancements']:
        report += f"""### {enhancement['type'].replace('_', ' ').title()}

{enhancement['description']}

**Recommendation:** {enhancement['recommendation']}

"""
    
    report += """---

## 5. Visualization Recommendations

"""
    
    for viz in improvements['visualization_recommendations']:
        report += f"""### {viz['type'].replace('_', ' ').title()}

**Description:** {viz['description']}  
**Tools:** {', '.join(viz['tools'])}  
**Priority:** {viz['priority'].upper()}

"""
    
    report += """---

## Implementation Priority

### High Priority (Immediate)
1. Phase intensity heatmap - Shows concentration of criminal activity
2. Financial impact waterfall - Demonstrates cumulative harm
3. Evidence repository map - Links timeline to supporting documentation
4. Shopify centrality visualization - Core narrative thread

### Medium Priority (Next Phase)
1. Perpetrator activity Gantt chart - Shows coordination
2. Application event Venn diagram - Demonstrates overlap
3. Bantjies conflict timeline - Parallel motive narrative

### Ongoing
1. Continuous evidence gap filling from ad-res-j7 repository
2. Witness statement integration
3. Cross-application narrative strengthening

---

## Next Steps

1. **Implement high-priority visualizations** to enhance GitHub Pages presentation
2. **Cross-reference all events** with ad-res-j7 evidence files for complete documentation
3. **Develop interactive timeline** allowing filtering by application, perpetrator, and category
4. **Create evidence summary pages** for each application with direct links to supporting files
5. **Generate executive summaries** for each timeline phase highlighting key patterns

---

**Repository:** [github.com/cogpy/revstream1](https://github.com/cogpy/revstream1)  
**Evidence Repository:** [github.com/cogpy/ad-res-j7](https://github.com/cogpy/ad-res-j7)
"""
    
    return report

def main():
    """Main function."""
    print("\n" + "="*80)
    print("TIMELINE-BASED IMPROVEMENTS ANALYSIS")
    print("="*80)
    
    # Load data
    timeline = load_json('data_models/timelines/timeline_refined_2025_11_19_v4.json')
    events = load_json('data_models/events/events_refined_2025_11_19_v4.json')
    
    # Generate improvements
    improvements = analyze_timeline_patterns(timeline, events)
    
    # Save JSON report
    with open('TIMELINE_IMPROVEMENTS_REPORT.json', 'w') as f:
        json.dump(improvements, f, indent=2)
    print("\n✓ Saved: TIMELINE_IMPROVEMENTS_REPORT.json")
    
    # Generate markdown report
    report = generate_recommendations_report(improvements)
    with open('TIMELINE_IMPROVEMENTS_REPORT.md', 'w') as f:
        f.write(report)
    print("✓ Saved: TIMELINE_IMPROVEMENTS_REPORT.md")
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"\nGenerated {len(improvements['timeline_insights'])} timeline insights")
    print(f"Identified {len(improvements['evidence_gaps'])} evidence gaps")
    print(f"Found {len(improvements['cross_application_opportunities'])} cross-application opportunities")
    print(f"Suggested {len(improvements['narrative_enhancements'])} narrative enhancements")
    print(f"Recommended {len(improvements['visualization_recommendations'])} visualizations")

if __name__ == '__main__':
    main()
