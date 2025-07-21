# Changelog

All notable changes to the BOOST data standard are documented in this file.

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