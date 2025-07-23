# DEPRECATED ERD FILES

**Date**: July 23, 2025  
**Reason**: Superseded by Interactive ERD Navigator v2.2 with GitHub discussion integration

## What Happened

These ERD files have been deprecated in favor of the new Interactive ERD Navigator v2.2 system. The new system provides:

- **29 entities** (vs 8-20 in previous versions) across 7 thematic areas
- **Interactive exploration** with zoom, pan, and dynamic filtering
- **GitHub discussion integration** with direct access via purple chat icons
- **Schema-driven architecture** with real-time JSON validation loading
- **TraceableUnit focus mode** for visual decluttering
- **Professional stakeholder interface** with comprehensive documentation

## Deprecated Files

### HTML Implementations
- `boost_erd_final.html` - Previous "final" 8-entity version
- `boost_erd_curved.html` - Curved relationships prototype
- `boost_erd_smart_routing.html` - Smart routing implementation
- `boost_erd_no_overlap.html` - Force-directed layout version
- `boost_erd_fixed.html` - Fixed positioning version
- `boost_erd_clean.html` - Clean layout attempt
- `boost_erd_d3.html` - Early D3.js prototype  
- `boost_erd_enhanced.html` - Enhanced prototype
- `boost_erd_schema_driven.html` - Schema integration attempt
- `boost_erd_working.html` - Working prototype

### Mermaid Implementations
- `boost_erd.mermaid` - Original Mermaid ERD
- `boost_erd_colored.mermaid` - Colored version
- `boost_erd_organized.mermaid` - Organized layout
- `boost_erd_subtle_colors.mermaid` - Subtle color theme
- `boost_erd_subtle_with_legend.mermaid` - With legend
- `boost_erd_themed.mermaid` - Themed version
- `boost_erd_themed_styled.mermaid` - Styled theme
- `boost_erd_with_legend.mermaid` - Legend version

### SVG Exports
- `boost_erd.svg` - Original SVG export
- `boost_erd_colored.svg` - Colored SVG
- `boost_erd_comprehensive.svg` - Previous comprehensive version
- `boost_erd_organized.svg` - Organized SVG
- `boost_erd_subtle_colors.svg` - Subtle colors SVG
- `boost_erd_subtle_with_legend.svg` - With legend SVG  
- `boost_erd_themed_styled.svg` - Themed SVG

## Replacement Files

### Current Active Files
- **`/erd-navigator/index.html`** - Main ERD Navigator (current system)
- **`/erd-navigator/README.md`** - ERD Navigator documentation
- **Schema directory** - Entity definitions at `/drafts/current/schema/*/validation_schema.json`

### Features Evolution

| Feature | Old Versions | New v2.0 |
|---------|--------------|----------|
| Entities | 8 | 20 |
| Thematic Areas | 3 | 7 |
| Relationships | 9 | 31 |
| Schema Integration | Partial | Complete |
| Interactivity | Basic | Advanced |
| Documentation | Limited | Comprehensive |

## Migration Guide

### For Developers
1. Use the main ERD Navigator at `/erd-navigator/index.html`
2. Reference entity definitions from `/drafts/current/schema/*/validation_schema.json`
3. All legacy ERD files have been removed - use only the main ERD Navigator

### For Documentation
1. Replace ERD images with exports from v2.0
2. Update entity counts and relationship descriptions
3. Reference comprehensive documentation

### For Business Users
1. Use the new thematic filtering in v2.0
2. Refer to the enhanced tooltips and descriptions
3. Export updated diagrams for presentations

## Why These Files Were Deprecated

### Technical Limitations
- **Mermaid**: Limited styling and interactivity options
- **Early D3 versions**: Incomplete entity coverage
- **Static approaches**: No schema integration

### Incomplete Coverage
- **Missing entities**: Only 8 of 20 total entities
- **Limited relationships**: Core connections only
- **No certification integration**: Missing claims/certificates
- **No commercial integration**: Missing transactions

### Maintenance Burden
- **Multiple formats**: Hard to keep synchronized
- **Inconsistent styling**: Different visual approaches
- **No single source of truth**: Scattered definitions

## Historical Value

These files represent the evolution of the BOOST ERD system and demonstrate:
- Progressive enhancement approach
- Multiple visualization experiments
- Iterative design improvements
- Community feedback integration

## If You Need These Files

These deprecated files are preserved for:
- **Historical reference**
- **Migration assistance** 
- **Research purposes**
- **Backup/rollback scenarios**

**Recommendation**: Migrate to v2.0 system for all new work.

---

**Superseded by**: BOOST Data Standard v2.2 Interactive ERD Navigator  
**Current system**: `/erd-navigator/index.html` (Main ERD Navigator)  
**Stakeholder Interface**: `../../../../erd-navigator/index.html` (Navigator)  
**Documentation**: `../current/BOOST_ERD_COMPREHENSIVE_README.md`