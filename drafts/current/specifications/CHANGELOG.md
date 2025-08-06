# CHANGELOG

All notable changes to the BOOST Specification documentation system will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v2.9.0] - 2025-08-06

### Added
- **Comprehensive PDF Build System**: Complete 67-page PDF with all 33 entities across 7 thematic areas
- **Minted Syntax Highlighting**: Professional JSON code highlighting in LaTeX examples
- **Single Source of Truth Architecture**: All entity documentation generated from JSON schemas
- **Build System Consolidation**: Organized scripts, outputs, and documentation structure
- **Technical Documentation**: Added comprehensive `docs/BUILD.md` architecture guide
- **Professional Directory Structure**: Clean separation of source files, scripts, and generated content

### Changed  
- **Build Output Management**: All generated files now consolidated in `build/` directory
- **Script Organization**: Moved Python generators to dedicated `scripts/` directory
- **Documentation Structure**: Complete rewrite of README.md with current workflow
- **Git Management**: Updated .gitignore to properly handle build artifacts and intermediate files
- **PDF Generation**: Enhanced 3-pass LaTeX compilation with comprehensive error reporting

### Fixed
- **Unicode Issues**: Resolved emoji and mathematical symbol rendering in LaTeX
- **Entity Coverage**: Fixed missing 29 entities - now includes all 33 entities in PDF
- **Build Consistency**: Standardized all build scripts to use `build/` directory consistently
- **LaTeX Symbol Handling**: Proper escaping of ≥, ≤, and underscore characters in entity tables

### Technical Implementation
- Created `scripts/` directory with organized Python content generators
- Implemented unified `build-all.sh` pipeline with content generation → PDF compilation → validation
- Enhanced `build-pdf.sh` with minted support and comprehensive logging
- Added `docs/BUILD.md` with complete technical architecture documentation
- Updated `.gitignore` with comprehensive build system patterns
- Cleaned up root directory intermediate files and temporary artifacts

### Build System Features
- **Complete Entity Coverage**: All 33 entities documented across 7 thematic areas
- **Schema-to-LaTeX Pipeline**: Automated conversion from JSON schemas to professional LaTeX tables
- **Multi-Pass Compilation**: 3-pass LaTeX build for complete cross-reference resolution
- **Error Handling**: Comprehensive validation, logging, and troubleshooting support
- **CI/CD Ready**: All scripts designed for automated build environments

## [v2.8.0] - 2025-08-06

### Added
- **Integrated Documentation System**: Consolidated ERD Navigator with Bikeshed specification system
- **ERD Navigator Integration**: Interactive entity relationship diagram with 33 entities across 7 thematic areas
- **Resources & Community Section**: Complete integration of presentations, meeting notes, and community resources
- **Entity Cross-References**: Comprehensive navigation links between related entities throughout specification
- **Interactive ERD Links**: Direct navigation from specification sections to ERD Navigator entity views
- **Enhanced Introduction**: Added community development process and participation information
- **Build System**: Automated Bikeshed specification generation with schema integration

### Changed
- **Documentation Architecture**: Migrated from ReSpec to consolidated Bikeshed + ERD Navigator system
- **Navigation Experience**: Enhanced bidirectional navigation between ERD and specification sections
- **Content Organization**: Structured all community resources, presentations, and technical content in unified system
- **Entity Documentation**: Added schema-driven entity definitions with interactive ERD integration

### Technical Implementation
- Created `/includes/resources-community.inc.md` for presentations and community content
- Created `/includes/erd-integration.inc.md` for ERD Navigator integration
- Enhanced `/includes/introduction.inc.md` with community development information
- Added comprehensive entity cross-references with ERD Navigator links
- Implemented automated build system with `build-spec.sh`
- Restored and configured ERD Navigator with all 33 BOOST entities

### Integration Features
- **33 Interactive Entities**: Complete entity relationship visualization
- **7 Thematic Areas**: Organized entity categorization and filtering
- **Schema-Driven Content**: Direct loading from JSON schema validation files
- **Dynamic Navigation**: Real-time relationship highlighting and entity exploration
- **Responsive Design**: Mobile-friendly specification and ERD Navigator

## Previous Versions

See Git history for detailed changes in previous development iterations.