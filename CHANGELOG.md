# Changelog

All notable changes to the BOOST data standard are documented in this file.

## [2.2.0] - 2025-07-23 - Interactive ERD Navigator

### Added
- **Interactive ERD Navigator** - Complete replacement of static Mermaid diagram with dynamic D3.js-based interactive visualization
- **29 Entity Coverage** - Full visualization of all entities across 7 thematic areas with real-time schema loading
- **GitHub Discussion Integration** - Purple 💬 chat icons in each entity header providing direct access to entity-specific discussions
- **Dynamic Thematic Filtering** - 9 filter buttons for focusing on specific domains (Core Traceability, Organizational, Material & Supply, etc.)
- **TraceableUnit Focus Mode** - 🎯 button to reduce visual complexity by highlighting only essential TraceableUnit relationships
- **Advanced Zoom & Pan Controls** - Mouse wheel zoom, click-and-drag panning for detailed exploration
- **Smart Relationship Routing** - Intelligent path routing to minimize visual clutter with 300px avoidance zones around TraceableUnit
- **Schema-Driven Architecture** - Dynamic entity definition loading from JSON validation schema files
- **Professional Styling** - GitHub-style design with SF Pro Display fonts and responsive layout

### Enhanced
- **Stakeholder Experience** - Comprehensive instructions and tooltips for non-technical users
- **Discussion Accessibility** - All 29 entities now have direct discussion access (#90-107, #166-179)
- **Visual Decluttering** - Advanced label positioning and collision detection for improved readability
- **Mobile Responsiveness** - Touch-friendly controls and responsive design for all device sizes
- **Documentation Integration** - Real-time integration with schema files eliminates manual diagram maintenance

### Changed
- **ERD Navigator Migration** - Replaced static SVG-based navigator with fully interactive implementation
- **Entity Link Organization** - Removed redundant entity link sections in favor of direct ERD access
- **Documentation Updates** - Updated README.md and navigator documentation to reflect interactive capabilities
- **Repository Cleanup** - Removed outdated GitHub discussion management scripts and temporary files

### Technical Improvements
- **D3.js v7 Integration** - Modern interactive SVG manipulation with advanced zoom and pan functionality  
- **Dynamic Path Adjustment** - Real-time schema path resolution for different deployment contexts
- **Performance Optimization** - Efficient rendering of complex relationship networks with selective hiding
- **Cross-browser Compatibility** - Tested functionality across modern web browsers with fallback support

## [2.1.2] - 2025-07-22 - Comprehensive Moisture Content Integration

### Added
- **Comprehensive moisture content tracking** - End-to-end moisture monitoring from harvest through delivery
- **MeasurementRecord moisture fields** - moistureContent, moistureMeasurementMethod, moistureEquipmentUsed
- **TraceableUnit moisture status** - currentMoistureContent, moistureContentTimestamp, moistureContentSource
- **ProcessingHistory moisture tracking** - Input/output moisture content with change ratios and reasons
- **EnergyCarbonData moisture enhancement** - Environmental conditions, quality assurance, measurement context
- **Moisture validation schema** - Comprehensive business rules and regulatory compliance validation
- **Quality grade moisture requirements** - Grade-specific moisture thresholds (Grade A: ≤18%, Grade B: ≤22%, etc.)
- **Regulatory compliance integration** - LCFS, FSC, SBP moisture tracking requirements
- **Processing event type expansion** - Added "drying" as explicit moisture reduction operation
- **Moisture content documentation** - Complete specification with measurement methods and standards

### Enhanced
- **ERD relationship modeling** - Added MeasurementRecord and ProcessingHistory moisture data relationships
- **Validation algorithms** - Moisture consistency checks, quality grade validation, volume adjustment formulas
- **Data quality assurance** - Equipment calibration tracking, measurement accuracy standards, environmental monitoring
- **Business rule enforcement** - Automated validation of moisture content against quality grades and regulatory limits

## [2.1.1] - 2025-07-21 - Drafts Folder Reorganization

### Changed
- **Drafts folder restructure** - Major reorganization for improved navigation and maintainability
- **Active content separation** - Current working files moved to `drafts/current/` structure
- **Legacy content archival** - Historical files organized in `drafts/archive/` with clear categorization
- **Communications organization** - California agency materials grouped by agency type
- **Examples reorganization** - Sample payloads restructured by transaction/validation type
- **Images cleanup** - Current ERD files separated from historical versions
- **Tools consolidation** - Development utilities moved from scripts/ to tools/ structure

### Removed
- **Temporary files cleanup** - Removed .~undo-tree~, #files#, and auto-generated LaTeX files
- **Duplicate content** - Consolidated multiple ERD versions with clear current vs. archive separation

### Updated  
- **README.md paths** - Updated all file references to reflect new directory structure
- **Documentation links** - Getting started guides now point to correct current/ locations

## [2.1.0] - 2025-07-21 - Plant Part Categorization Integration

### Added
- **Plant part categorization system** - Comprehensive semantic categorization of plant components
- **Material entity plant part specs** - applicablePlantParts, excludedPlantParts, plantPartProcessingSpecs
- **SpeciesComponent plant tracking** - plantPartComposition with volume/percentage by plant part
- **MaterialProcessing plant transformations** - inputPlantParts, outputPlantParts, plantPartTransformations
- **Standardized plant part taxonomy** - 17 plant parts across woody, foliage, reproductive, agricultural categories
- **Processing method compatibility** - Plant part-specific processing methods and quality grades
- **Plant part transformation tracking** - Recovery rates, quality changes, and waste stream documentation

### Enhanced
- **Value chain optimization** - Route materials based on plant part composition for optimal processing
- **Circular economy support** - Track byproduct utilization (bark→mulch, sawdust→pellets)
- **Premium product tracking** - Heartwood vs sapwood quality differentiation
- **Waste stream management** - Detailed tracking of plant part losses and disposal methods

## [2.0.0] - 2025-07-21 - Kaulen Framework Implementation

### Added
- **TraceableUnit (TRU)** - New primary traceable entity with multi-species support and biometric identification
- **Three critical tracking points** - harvest_site, skid_road, forest_road, mill_entrance infrastructure
- **Biometric identification system** - Attachment-free wood identification using optical patterns
- **Complete processing chain tracking** - MaterialProcessing, MeasurementRecord, LocationHistory entities
- **Enhanced geographic integration** - Spatial data support with GeoJSON compliance
- **Species-specific sustainability claims** - Claim inheritance through TRU processing chains
- **Organization and Operator management** - Enhanced entity management with certification tracking
- **Comprehensive migration tools** - MaterialBatch to TRU migration scripts and validation
- **Integration testing scenarios** - End-to-end traceability testing documentation

### Changed
- **MaterialBatch deprecated** - Replaced by TraceableUnit as primary traceable entity
- **Material refactored** - Now reference table only, no longer traceable
- **ERD completely rebuilt** - 452-line mermaid diagram with all new relationships
- **Documentation structure** - All entities now follow product_group pattern with validation schemas

### Updated
- **ERD visualizations** - Regenerated SVG files with current entity relationships
- **Entity schemas** - Comprehensive JSON schemas with validation rules and examples

## [1.2.0] - 2025-06-25 - Schema Standardization

### Added
- **Product group schema** - Standardized validation schema and data dictionary
- **Certification objects** - Certificate, CertificationBody, CertificationScheme entities
- **SFI examples** - Concrete examples using Sustainable Forestry Initiative standards

### Changed
- **MaterialFeedstock renamed** - Now called Material for consistency
- **Schema organization** - Migrated to `drafts/schema/` directory structure

### Updated
- **ERD consolidation** - Unified into single `boost_erd.mermaid` file
- **Entity nomenclature** - Cleaned up naming conventions across all entities

## [1.1.0] - 2025-06-11 - Interactive Features

### Added
- **Interactive ERD navigator** - Stakeholder feedback system with zoom/pan controls
- **Transaction objects** - YAML and JSON transaction examples with validation
- **Transportation units** - Added to object schema specifications
- **JSON-LD support** - Linked data specifications for interoperability

### Updated
- **Meeting documentation** - Comprehensive notes and presentation materials
- **GitHub Pages site** - Enhanced with presentations section and navigation

## [1.0.0] - 2025-05-22 - Initial Release

### Added
- **Core ERD models** - Initial entity relationship diagrams for SBP, ISO, FSC, RSB standards
- **Basic schema structure** - Foundation entities for biomass chain of custody
- **W3C community integration** - Baseline W3C.json, contributing guidelines, code of conduct
- **Presentation materials** - Kickoff slides and meeting documentation
- **Project governance** - Charter, LICENSE, README, and contribution guidelines

### Infrastructure
- **Repository setup** - GitHub repository with proper documentation structure
- **Build system** - LaTeX presentation compilation with custom styling
- **Version control** - Git workflow with branch management and pull requests

---

## Project Timeline

- **April 2025** - Project inception and initial documentation
- **May 2025** - Core ERD development and W3C community setup  
- **June 2025** - Interactive features and schema standardization
- **July 2025** - Kaulen Framework implementation with comprehensive entity system

For detailed technical documentation, see entity schemas in `drafts/schema/` and implementation guides.