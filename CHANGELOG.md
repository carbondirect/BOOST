# Changelog

All notable changes to the BOOST data standard are documented in this file.

## [3.0.8] - 2025-08-12 - Shell Compatibility Fix for Release Packaging

### Fixed
- **Release Package Creation Error** - Fixed "Bad substitution" error in release workflow
  - **release.yml**: Added `shell: bash` to release package creation step
  - **Parameter Expansion**: `${GITHUB_SHA::8}` requires bash, not default sh shell
  - **Shell Compatibility**: Ensure bash-specific syntax works in release package creation
- **Workflow Progression** - PDF generation now works, but packaging step was failing
  - LaTeX PDF generation: ✅ Working (66 pages)
  - HTML documentation: ✅ Working  
  - Release packaging: ✅ Fixed shell compatibility

### Technical Improvements
- **Consistent Shell Usage** - All workflow steps requiring bash features now explicitly use bash
- **Parameter Expansion** - Proper handling of Git SHA truncation in release notes
- **Error Isolation** - Each step now uses appropriate shell for its requirements

*This fix ensures the complete release workflow from PDF generation through package creation.*

## [3.0.7] - 2025-08-12 - LaTeX Workflow Error Handling Fix

### Fixed
- **Release Workflow Exit Code Issue** - Fixed workflow failing despite successful PDF generation
  - **release.yml**: Added proper error handling for LaTeX warnings using `set +e` and `|| true`
  - **LaTeX Warnings**: LaTeX warnings no longer cause workflow failure when PDF is successfully generated
  - **Shell Configuration**: Explicitly use bash shell with proper exit code handling
  - **Verification**: Added PDF file verification and listing after successful generation
- **PDF Build Process** - LaTeX now consistently generates 66-page PDF without workflow failure
  - LaTeX builds successfully with warnings (normal behavior) 
  - PDF generation confirmed with file size verification
  - Proper cleanup and renaming of output files

### Technical Improvements
- **Robust Error Handling** - Distinguish between critical errors and expected LaTeX warnings
- **Workflow Reliability** - Release process now completes successfully when PDF is generated
- **Better Diagnostics** - Added file listing and verification steps for debugging

*This fix ensures the release workflow completes successfully when LaTeX generates PDFs with normal warnings.*

## [3.0.6] - 2025-08-12 - Complete LaTeX Build Fixes

### Fixed
- **LaTeX Compilation Errors** - Resolved all remaining LaTeX build issues in CI environment
  - **release.yml**: Added `-shell-escape` flag to pdflatex commands for minted package compatibility
  - **tex files**: Removed problematic Unicode emoji characters (🗂️) that caused LaTeX errors
  - **tex files**: Replaced Unicode mathematical symbols (≤, ≥) with proper LaTeX commands (\leq, \geq)
  - **Minted package**: Fixed "You must invoke LaTeX with the -shell-escape flag" error
  - **Unicode support**: Fixed "Unicode character not set up for use with LaTeX" errors
- **PDF Generation Reliability** - LaTeX now builds successfully generating 68-page PDF
  - Verified locally with pdflatex -shell-escape -interaction=nonstopmode boost-spec.tex
  - All Unicode characters properly converted to LaTeX-compatible format
  - Mathematical symbols now render correctly in PDF output

### Technical Improvements
- **CI/CD Compatibility** - LaTeX build process now fully compatible with containerized environment
- **Character Encoding** - Systematic removal of problematic Unicode characters from all .tex files
- **Mathematical Notation** - Proper LaTeX mathematical symbol usage throughout documentation

*These fixes ensure reliable PDF generation in both local and CI environments without Unicode or package errors.*

## [3.0.5] - 2025-08-12 - LaTeX Build Fixes and Name Standardization

### Fixed
- **LaTeX Build Issues** - Fixed font expansion errors and syntax issues in PDF generation
  - **boost-spec.tex**: Removed problematic `microtype` package causing font expansion errors
  - **boost-spec.tex**: Switched from `cmbright` to `lmodern` font for better CI compatibility
  - **boost-spec-minimal.sty**: Updated `\boosttitle` command with proper syntax and correct standard name
  - **boost-spec-minimal.sty**: Commented out `cmbright` font that caused CI build failures
- **LaTeX Title Updates** - All LaTeX titles now use correct "Biomass Open Origin Standard for Tracking (BOOST)" name
  - **boost-spec.tex**: Updated document title, PDF metadata, and headers with correct standard name
  - **boost-spec-minimal.sty**: Updated title page generation with correct name and version info

### Technical Improvements
- **PDF Generation Reliability** - LaTeX now builds successfully without font expansion errors
- **CI/CD Compatibility** - Removed font packages that caused issues in containerized builds
- **Version Updates** - Updated LaTeX version references to v3.0.5 and current date

*These fixes ensure reliable PDF generation in both local and CI environments while maintaining correct standard naming.*

## [3.0.4] - 2025-08-12 - Standard Name Standardization

### Fixed
- **Standard Name Consistency** - Corrected all references to use proper "Biomass Open Origin Standard for Tracking (BOOST)" name
  - **README.md**: Updated title from "Biomass Chain of Custody (CoC) Data Standard" to correct name
  - **Release Workflow**: Fixed release names for major, minor, and patch versions
  - **GitHub Actions Workflows**: Updated all workflow documentation with correct standard name
  - **Version Management**: Corrected release notes generation text
- **Release Strategy Enhancement** - Updated release workflow to build and release all semantic versions (major, minor, patch)
  - Previously only major versions (v1.0.0, v2.0.0) triggered releases
  - Now all versions (v1.0.0, v1.2.3, v2.1.0) trigger automatic releases with appropriate naming
- **Workflow Documentation** - Updated comprehensive workflow documentation with correct standard name references

### Technical Improvements  
- **Name Standardization** - Eliminated inconsistent references like "BOOST Data Standard" and "Biomass Chain of Custody"
- **Release Automation** - Enhanced release workflow to properly handle all semantic version types
- **Documentation Accuracy** - All references now consistently use "Biomass Open Origin Standard for Tracking (BOOST)"

*These fixes ensure consistent and correct standard naming across all documentation, workflows, and release processes.*

## [3.0.2] - 2025-08-12 - Documentation Consistency Fixes

### Fixed
- **Entity Count Consistency** - Standardized all references to show correct count of 33 entities
  - **boost-spec.bs**: Updated abstract and full conformance sections (29→33)
  - **core-entities.inc.md**: Updated data model description (29→33)
  - **BOOST_FORMAL_DOCUMENTATION_OUTLINE.md**: Updated all references (29→33)
  - **includes/data-model.inc.md**: Updated framework description (29→33)
  - **erd-navigator/README.md**: Updated explorer documentation (29→33)
  - **erd-navigator/index.html**: Updated discussion coverage text (29→33)
  - **relationship_definition_system_consolidation_proposal.md**: Updated scope (32→33)
- **BOOST Acronym Consistency** - Corrected all expansions to proper "Biomass Open Origin Standard for Tracking"
  - **boost-spec.bs**: Fixed abstract and specification definition
  - **BOOST_FORMAL_DOCUMENTATION_OUTLINE.md**: Fixed abstract
  - **includes/introduction.inc.md**: Fixed opening paragraph
  - **tex/introduction.tex**: Fixed LaTeX introduction
  - **reference-implementations/python/README.md**: Fixed library description

### Technical Improvements
- **Documentation Accuracy** - All current documentation now consistently reflects actual schema structure
- **Acronym Standardization** - Eliminated inconsistent "Biomass Open-Source Traceability" references
- **Historical Preservation** - CHANGELOG entries maintained as accurate for their time periods

*These fixes ensure professional consistency across all documentation formats and eliminate confusion about entity counts and proper BOOST terminology.*

## [3.0.0] - 2025-08-12 - Complete CI/CD Documentation Build System

### Major Enhancements
- **Complete CI/CD Pipeline** - Comprehensive GitHub Actions workflow system for automated documentation build and deployment
  - **6 Workflows**: build-deploy, build-dev-docs, release, schema-validation, status-badges, validate-pr, version-check
  - **Multi-Environment Support**: Production (main), development (feature branches), and release builds
  - **GitHub Pages Integration**: Automated deployment to carbondirect.github.io/BOOST with proper versioning
  - **Quality Gates**: Schema validation, integrity checks, and comprehensive testing before deployment
- **Automated Version Management** - Git tag-based version extraction replacing hardcoded version references
  - **Dynamic Version Injection**: {{VERSION}} placeholders automatically replaced during build
  - **Release Policy**: Major versions only (v1.0.0, v2.0.0, v3.0.0) trigger production releases
  - **Development Versioning**: Branch-specific versions for development builds (e.g., v2.9.0-dev-abc123)
- **Multi-Format Documentation Generation** - Complete HTML and PDF generation with LaTeX support
  - **HTML**: ReSpec-based interactive documentation with enhanced CSS styling and navigation
  - **PDF**: Multi-pass LaTeX compilation ensuring complete table of contents, list of figures, and list of tables
  - **Schema Integration**: Automatic entity table generation and cross-references

### Infrastructure Improvements
- **Schema Integrity Validation** - Comprehensive validation system ensuring data model consistency
  - **Foreign Key Integrity**: Automated checking for orphaned references and missing entities
  - **Cross-Entity Validation**: Ensures all relationships are properly defined and accessible
  - **Pattern Consistency**: Validates ID patterns and field naming conventions across all entities
- **Enhanced Build System** - Robust build process with error handling and quality assurance
  - **Multi-Pass LaTeX**: 3-pass compilation for complete PDF navigation and cross-references
  - **HTML Cleaning**: Automated HTML cleanup for PDF conversion using external Python scripts
  - **Artifact Management**: Systematic artifact retention and organization for different build types
- **Development Tools Enhancement** - Comprehensive tooling for local development and testing
  - **Local Testing**: Complete local testing environment with Docker support and quick-test scripts
  - **Script Automation**: Python scripts for HTML cleaning, schema validation, and LaTeX generation
  - **Documentation**: Extensive CI/CD documentation and troubleshooting guides

### Technical Architecture
- **Build Environment Standardization** - Consistent build environments across all workflows
  - **Python 3.11**: Standardized Python environment with comprehensive dependency management
  - **LaTeX Distribution**: Full texlive installation with minted package for syntax highlighting
  - **System Dependencies**: Automated installation of required packages (pygments, pandoc)
- **Workflow Orchestration** - Sophisticated workflow management with proper dependencies and concurrency
  - **Parallel Execution**: Multiple validation and build steps run concurrently for performance
  - **Conditional Logic**: Smart deployment logic ensuring only main branch deployments reach production
  - **Error Handling**: Comprehensive error handling with detailed logging and failure reporting
- **Artifact Management** - Professional artifact handling with proper retention policies
  - **Development Builds**: 7-day retention for feature branch artifacts
  - **Production Builds**: 30-day retention for main branch artifacts
  - **Release Packages**: 90-day retention for tagged releases with complete documentation packages

### Enhanced Documentation
- **PDF Navigation Completeness** - Fully functional PDF with complete navigation elements
  - **Table of Contents**: Multi-level TOC with proper page references and hyperlinks
  - **List of Figures**: Comprehensive figure list with captions and page references
  - **List of Tables**: Complete table inventory with descriptive captions
  - **Cross-References**: Working internal links and references throughout the document
- **LaTeX Integration** - Professional LaTeX styling and formatting
  - **Entity Tables**: Automated LaTeX table generation from JSON schemas
  - **Figure Management**: Placeholder figures with proper captions for List of Figures functionality
  - **Styling**: Custom BOOST styling with thematic colors and professional typography
- **Interactive ERD Navigator** - Enhanced entity relationship diagram with improved functionality
  - **Schema Integration**: Real-time loading from JSON schema files
  - **Relationship Examples**: Interactive examples for all major entity relationships
  - **Navigation Enhancement**: Improved filtering and search capabilities

### Quality Assurance
- **Comprehensive Testing** - Multi-layer testing ensuring documentation quality and consistency
  - **Schema Validation**: All 33+ entity schemas validated for structure and integrity
  - **Build Validation**: HTML size, content presence, and styling verification
  - **Cross-Reference Validation**: Ensures all internal links and references are functional
- **Error Prevention** - Proactive error detection and prevention systems
  - **Pre-commit Validation**: Schema integrity checks before any commit
  - **PR Validation**: Comprehensive pull request validation with quality gates
  - **Release Validation**: Additional validation layers for production releases
- **Performance Optimization** - Build system optimized for speed and reliability
  - **Caching**: Intelligent caching of dependencies and build artifacts
  - **Parallel Processing**: Concurrent execution of independent build steps
  - **Incremental Updates**: Smart detection of changes requiring rebuild

### Migration and Deployment
- **GitHub Pages Deployment** - Complete deployment pipeline to GitHub Pages
  - **URL Structure**: Clean URLs with proper redirects and canonical references
  - **Content Organization**: Systematic organization of HTML, PDF, schemas, and ERD Navigator
  - **Version Tracking**: Build timestamps and version information embedded in deployed content
- **Backward Compatibility** - Maintains compatibility with existing documentation consumers
  - **URL Preservation**: Existing documentation URLs continue to function
  - **Format Support**: Both HTML and PDF formats available with consistent content
  - **API Stability**: Schema file locations and formats remain stable

### Developer Experience
- **Comprehensive Documentation** - Detailed documentation for all CI/CD components
  - **Setup Guides**: Step-by-step setup instructions for local development
  - **Troubleshooting**: Common issues and solutions documented
  - **Best Practices**: Guidelines for contributing to the documentation system
- **Local Development Support** - Complete local development environment
  - **Quick Testing**: Rapid local testing with ./quick-test.sh script
  - **Development Server**: Local HTTP server for testing HTML documentation
  - **Build Scripts**: Standalone build scripts for individual components

### Business Impact
- **Automated Documentation Delivery** - Eliminates manual documentation build and deployment processes
- **Quality Assurance** - Ensures consistent, high-quality documentation with automated validation
- **Developer Productivity** - Streamlined contribution process with immediate feedback on changes
- **Stakeholder Access** - Reliable, always-current documentation accessible via GitHub Pages
- **Professional Presentation** - Publication-quality documentation suitable for standards organizations

*This major release establishes BOOST as having enterprise-grade documentation infrastructure with automated quality assurance, multi-format output, and professional deployment capabilities.*

## [2.7.0] - 2025-08-04 - Core Traceability Entity Restructuring

### Breaking Changes
- **TraceableUnit Schema** - `harvestGeographicDataId` is now REQUIRED for all new TraceableUnit instances
  - **Impact**: Core conformance implementations must provide harvest geographic data
  - **Migration**: Existing systems must update data creation workflows to include mandatory harvest location
  - **Validation**: Schema validation will reject TraceableUnit instances without `harvestGeographicDataId`

### Added
- **Location-Aware Core Conformance** - Enhanced Core traceability requirements for meaningful supply chain transparency
  - **Four Core Entities**: TraceableUnit, Organization, Material, GeographicData now form complete self-contained traceability system
  - **Geographic Origin Tracking**: Mandatory harvest location tracking for all traceable units
  - **Complete Dependency Graph**: Core entities form closed dependency loop with no external requirements
- **Extended Traceability Entities Section** - New conformance level for enhanced functionality
  - **MaterialProcessing**: Moved from Core to Extended conformance level
  - **Processing Operations**: Now classified as enhancement rather than core requirement
  - **Clear Separation**: Distinct Core vs Extended conformance requirements

### Enhanced
- **BOOST Conformance Classes** - Updated conformance requirements to match actual entity dependencies
  - **Core Conformance**: Now explicitly requires TraceableUnit, Organization, Material, GeographicData entities
  - **Extended Conformance**: Added MaterialProcessing operations and location history tracking
  - **Full Conformance**: Maintains all 29+ entities for complete functionality
- **Entity Organization** - Restructured specification sections for clarity
  - **Core Traceability Entities**: Contains only entities required for Core conformance
  - **Cross-References**: Added navigation links from original entity sections to Core locations
  - **Extended Entities**: Separate section for Extended conformance requirements

### Fixed
- **Schema Consistency Issues** - Resolved critical mismatches between documentation and validation schemas
  - **TraceableUnit JSON Schema**: Added `harvestGeographicDataId` to required fields array
  - **Cross-Entity Validation**: Updated validation rules to enforce mandatory harvest location
  - **Relationship Metadata**: Updated TraceableUnit relationships to reflect required geographic dependency
- **ERD Configuration Alignment** - Updated visualization to reflect new conformance structure
  - **MaterialProcessing Classification**: Moved from core_traceability to material_supply_chain area
  - **Visual Consistency**: ERD now correctly shows MaterialProcessing as Extended conformance entity

### Technical Improvements
- **Self-Contained Core Architecture** - Core entities now form complete dependency graph
  - **Foreign Key Resolution**: All Core entity FK references resolved within Core entity set
  - **Implementation Simplicity**: Core implementations need only 4 entities for basic traceability
  - **Validation Consistency**: Schema validation, cross-entity rules, and relationship metadata synchronized
- **Conformance Level Clarity** - Clear separation between conformance requirements
  - **Core**: Essential traceability with geographic origin tracking (4 entities)
  - **Extended**: Enhanced functionality with processing operations and history tracking
  - **Full**: Complete BOOST ecosystem with all regulatory and compliance features

### Migration Guide
- **Core Implementations**: Must update to include GeographicData entity and mandatory harvest locations
- **Data Creation**: All TraceableUnit creation workflows must provide `harvestGeographicDataId`
- **Extended Features**: MaterialProcessing operations now require Extended conformance level
- **Validation Updates**: Update validation frameworks to enforce new Core requirements

### Business Impact
- **Supply Chain Transparency**: Core conformance now guarantees geographic origin tracking
- **Implementation Clarity**: Clear separation between essential vs enhanced functionality  
- **Market Adoption**: Lower barrier for Core implementation while maintaining traceability value
- **Regulatory Alignment**: Core requirements align with EUDR and other geographic origin regulations

## [2.6.1] - 2025-08-01 - Schema Integrity Enhancements and Development Tools

### Added
- **Schema Integrity Reviewer Sub-Agent** - Comprehensive validation tool for BOOST schema system integrity
  - **Location**: `tools/agents/schema-integrity-reviewer.md` with detailed setup documentation
  - **7 Critical Validation Aspects**: Orphaned FK detection, data model validation, ERD alignment, pattern consistency, implementation integration, Python testing, and business logic validation
  - **Python Reference Implementation Testing**: Validates Pydantic models, field types, patterns, and validation logic alignment
  - **Comprehensive Reporting**: Provides specific file locations and actionable fix instructions
  - **Integration Testing**: Tests complete workflows using Python reference implementation
- **Equipment Entity** - New entity to resolve orphaned EQ- pattern references
  - **32 Comprehensive Fields**: Including equipmentId, organizationId, currentOperatorId, assignedTrackingPointId
  - **Pattern Validation**: `^EQ-[A-Z0-9-_]+$` format for equipment identification
  - **Foreign Key Relationships**: Proper references to Organization, Operator, and TrackingPoint entities
  - **ERD Integration**: Added to material_supply_chain area with proper positioning and relationships
- **Relationship Definition System Consolidation Proposal** - Future enhancement documentation
  - **Technical Specification**: Complete proposal at `drafts/current/specifications/relationship_definition_system_consolidation_proposal.md`
  - **GitHub Issue #190**: Critical priority enhancement for consolidating dual relationship systems
  - **Schema-First Architecture**: Proposed solution to eliminate dual maintenance burden

### Enhanced
- **Schema Validation Patterns** - Standardized pattern validation across entities
  - **TrackingPoint**: Added `^TP-[A-Z0-9-_]+$` pattern validation to trackingPointId
  - **Customer**: Added `^GEO-[A-Z0-9-_]+$` pattern validation to GeographicDataId
  - **Operator**: Updated pattern from `^OP-[A-Z0-9-]{6,50}$` to `^OP-[A-Z0-9-_]+$` for consistency
- **ERD Configuration** - Updated with Equipment entity integration
  - **Entity Count**: Updated from 31 to 32 entities in directories.json
  - **Equipment Positioning**: Added to material_supply_chain area at coordinates (1900, 2000)
  - **Relationship Definitions**: Added Organization→Equipment relationships with proper cardinality
  - **Field Mappings**: Updated to include Equipment foreign key fields
- **Cross-Entity Validation** - Enhanced validation rules and foreign key constraints
  - **Equipment Validation**: Added comprehensive validation rules for organizationId, currentOperatorId, assignedTrackingPointId
  - **SalesDeliveryDocument Fix**: Corrected foreign key reference from salesDeliveryDocumentId to documentId
  - **Pattern Consistency**: Ensured all FK patterns align with target entity primary key patterns
- **Development Documentation** - Added comprehensive setup and usage instructions
  - **Main README**: Added Development Tools section with sub-agent setup instructions
  - **Agent README**: Created `tools/agents/README.md` with detailed configuration options
  - **Three Setup Methods**: Automatic discovery, manual registration, and direct Task tool reference

### Fixed
- **Data Model Normalization Issues** - Resolved fundamental design problems
  - **Organization Entity**: Removed forestRoads and skidRoads arrays (data duplication with SupplyBase)
  - **Normalization Compliance**: Eliminated violation of database normalization principles
  - **Single Source of Truth**: Roads now properly managed by SupplyBase entity only
- **Orphaned Foreign Key References** - Resolved critical integrity issues
  - **Equipment References**: Created missing Equipment entity to handle all EQ- pattern references
  - **Pattern Validation**: Added missing pattern validation to prevent invalid references
  - **Cross-Entity Consistency**: Aligned validation rules with actual entity relationships
- **ERD Relationship Accuracy** - Corrected visualization inconsistencies
  - **Missing Equipment Relationships**: Added Organization→Equipment ownership relationships
  - **Field Mapping Coverage**: Ensured all FK fields are properly mapped for ERD visualization
  - **Relationship Completeness**: Added missing metadata relationships for proper ERD display

### Technical Improvements
- **Schema System Architecture** - Enhanced foundation for consistency and reliability
  - **Comprehensive Validation Framework**: 7-aspect validation covering all critical schema integrity areas
  - **Automated Testing Integration**: Sub-agent includes Python reference implementation testing
  - **Pattern Standardization**: Consistent ID patterns across all 32 entities
  - **Documentation Integration**: Clear setup instructions and troubleshooting guides
- **Development Workflow Enhancement** - Improved schema maintenance processes
  - **Sub-Agent Integration**: Professional validation tool integrated into repository structure
  - **Future Enhancement Planning**: Documented approach for addressing dual relationship system
  - **Critical Issue Tracking**: GitHub issue created for architectural improvements

### Migration Notes
- **Equipment Entity**: New entity is optional - existing systems remain fully compatible
- **Organization Entity**: Removed fields (forestRoads, skidRoads) were optional - no breaking changes
- **Pattern Updates**: Enhanced validation is additive and backward compatible
- **Sub-Agent Usage**: Optional development tool - does not affect production systems

### Business Impact
- **Data Integrity**: Eliminated orphaned foreign key references that could cause validation failures
- **Maintenance Efficiency**: Sub-agent reduces manual schema validation effort
- **System Reliability**: Resolved fundamental data model design issues
- **Developer Experience**: Clear documentation and automated validation tools

*Resolves: Multiple schema integrity issues, adds comprehensive validation tooling, establishes foundation for future architectural improvements*

## [2.6.0] - 2025-07-31 - Enhanced Transaction and Organization Entities for TRU Tracking

### Added
- **Enhanced Transaction Entity (#139)**: Added comprehensive TRU tracking and reconciliation workflow capabilities
  - `traceableUnitIds` array field for linking transactions to specific TRUs
  - `reconciliationStatus` enum field for tracking transaction reconciliation state (pending, resolved, disputed)
  - `manipulationTimestamps` array field for chronological processing step tracking
  - `trackingPointIds` array field for location trail references
  - `mediaBreaksDetected` boolean array field for continuity flags per TRU
  - `speciesCompositionAtTransaction` object array field for species breakdown at transaction time

- **Enhanced Organization Entity (#138)**: Added equipment and infrastructure management capabilities
  - `equipmentIds` array field for harvester/machine tracking references
  - `operatorIds` array field for personnel tracking references
  - `harvestSites` array field for operational harvest locations managed
  - `skidRoads` array field for infrastructure mapping references
  - `forestRoads` array field for transportation routes managed
  - `traceableUnitIds` array field for TRUs managed by organization

- **New Python API Methods**: Added array management methods to boost_client.py
  - `add_tru_to_transaction()` - Add TraceableUnit IDs to transaction TRU arrays
  - `add_tru_to_organization()` - Add TraceableUnit IDs to organization managed TRUs
  - `add_equipment_to_organization()` - Add equipment IDs to organization equipment arrays
  - `set_reconciliation_status()` - Update transaction reconciliation status with validation
  - `add_manipulation_timestamp()` - Add chronologically sorted processing timestamps

- **Enhanced Business Logic Validation**: Added new validation methods to dynamic_validation.py
  - `validate_tru_transaction_consistency()` - Cross-entity TRU-transaction validation
  - `validate_reconciliation_workflow()` - Transaction reconciliation status validation
  - `validate_timestamp_chronology()` - Manipulation timestamp ordering validation
  - `validate_organization_operational_consistency()` - Organization operational data validation

- **Comprehensive Test Suite**: Added test_enhanced_entities.py with full validation coverage
  - Enhanced Transaction entity testing with TRU tracking scenarios
  - Enhanced Organization entity testing with equipment management scenarios
  - Comprehensive cross-entity validation testing
  - Array management method testing

### Enhanced
- **Schema Relationships**: Updated boost_metadata sections with new foreign key relationships
  - Transaction → TraceableUnit (many-to-many via traceableUnitIds)
  - Transaction → TrackingPoint (many-to-many via trackingPointIds)  
  - Organization → TraceableUnit (many-to-many via traceableUnitIds)
  - Organization → TrackingPoint (many-to-many via harvestSites, skidRoads, forestRoads)

- **JSON Schema Validation**: Enhanced validation patterns and examples for all new fields
  - Proper ID pattern validation (TRU-, TP-, EQ-, OP- prefixes)
  - Array validation with uniqueItems constraints where appropriate
  - Comprehensive field descriptions and examples

### Fixed
- **Pydantic Validation**: Resolved None value handling in array management methods
- **Timestamp Serialization**: Fixed manipulation timestamp format and sorting issues
- **Model Recreation**: Implemented proper exclude_none=True patterns for dynamic model updates

### Technical Details
- All new fields follow BOOST EntityNameId foreign key conventions
- Enhanced entities maintain backward compatibility with existing schemas
- New validation methods integrate seamlessly with existing comprehensive_validation()
- Array management methods include proper None handling and validation
- Test coverage includes both positive and negative validation scenarios

### Migration Notes
- Existing Transaction and Organization entities remain fully compatible
- New fields are optional and do not require data migration
- Enhanced validation is additive and does not break existing workflows
- API methods are backward compatible with existing entity management

*Resolves: #139 (Enhanced Transaction Entity), #138 (Enhanced Organization Entity)*

## [2.5.1] - 2025-07-31 - LCFS Example Refactoring and Validation Fixes

### Added
- **📓 BOOST-Compliant LCFS Example** - Completely refactored Pacific Renewable Fuels LCFS example using BOOST Python reference implementation
- **🎯 Schema-Compliant Data Structures** - All entities now follow proper BOOST ID patterns (`ORG-*`, `TXN-*`, `CUST-*`)
- **🌐 JSON-LD Semantic Web Support** - Full `@context`, `@type`, `@id` compatibility for semantic web integration
- **✅ Dynamic Validation Demonstration** - Working example of schema-driven validation with real LCFS data
- **🚀 Production-Ready Example** - Enterprise-grade patterns for regulatory compliance applications

### Enhanced
- **📋 LCFS Example Documentation** - Streamlined to single high-quality BOOST-compliant Jupyter notebook
- **🔧 Validation Robustness** - Fixed enum serialization and None field handling in Python reference implementation
- **📖 User Experience** - Clear progression from basic concepts to advanced BOOST patterns

### Fixed
- **🐛 Validation Issues in Python Reference Implementation**:
  - Fixed enum serialization (`OrganizationOrganizationtypeEnum.PRODUCER` → `"producer"`)
  - Fixed None field validation (now properly excluded from validation)
  - Updated `validate_entity()` to use `model_dump(exclude_none=True, mode='json')`
  - Updated `validate_all()` for proper entity serialization
  - Updated `export_to_jsonld()` for clean JSON-LD output
- **📏 ID Pattern Compliance** - Fixed organization and transaction ID patterns in LCFS example
- **📞 Phone Number Format** - Corrected to E.164 format without dashes
- **🔗 Relative Path Issues** - Fixed Python import paths in Jupyter notebook

### Removed
- **🗑️ Redundant Documentation** - Removed org-mode version (66K+ lines) and original non-compliant Jupyter notebook
- **📂 Technical Debt** - Eliminated duplicate LCFS content and inconsistent data structures

### Migration Notes
- **LCFS Example Users**: The example now demonstrates proper BOOST usage - review the refactored notebook for best practices
- **Python Reference Implementation Users**: Validation now works correctly - update any custom validation code if needed

## [2.5.0] - 2025-07-30 - Schema-Driven Python Reference Implementation

### Added
- **🔄 Dynamic Schema-Driven Architecture** - Complete Python reference implementation that automatically adapts to schema changes without code modifications
- **📦 Dynamic Model Generation** - Pydantic models generated directly from JSON schemas at runtime using `SchemaLoader` class
- **🎯 Schema-Driven Enum Discovery** - Enum values dynamically loaded from current schemas, making new values instantly available
- **✅ Configuration-Driven Business Logic** - 8 categories of business validation rules loaded from `business_logic_validation.json`:
  - Volume/Mass Conservation with tolerance checking
  - Temporal Logic (dates, seasons, processing windows)
  - Geographic Logic (transport distances, jurisdictions)
  - Species Composition validation
  - Certification Logic (chain of custody, validity)
  - Regulatory Compliance (LCFS, EU RED, sustainability)
  - Economic Logic (pricing, payment terms)
  - Quality Assurance (moisture, contamination)
- **🔗 Automatic Relationship Discovery** - Foreign key relationships discovered from schema metadata automatically
- **📋 Comprehensive Validation Suite** - Schema validation, business logic validation, cross-entity validation, and temporal consistency
- **🌐 JSON-LD Export/Import** - Full semantic web compatibility with context support
- **📊 Interactive Jupyter Notebook** - `BOOST_Reference_Implementation_Demo.ipynb` demonstrating all features across 13 sections
- **📖 Complete Documentation Package**:
  - `SCHEMA_CHANGE_GUIDE.md` - Detailed schema change propagation guide
  - `ARCHITECTURE.md` - Technical architecture documentation
  - `SCHEMA_ROBUSTNESS_SUMMARY.md` - Executive summary of robustness improvements
  - Updated `README.md` with schema-driven features

### Enhanced
- **🛡️ Schema Robustness** - System now handles most schema changes automatically:
  - ✅ New fields → Automatically available with validation
  - ✅ New enum values → Instantly usable
  - ✅ New entity types → Auto-discovered and loaded
  - ✅ Updated constraints → Applied immediately
  - ✅ New business rules → Enforced automatically
- **🔄 Hot Reload Capability** - `refresh_schemas()` method reloads schemas without application restart
- **📈 Performance Optimization** - Schema loading with caching, efficient model generation, and reasonable memory usage
- **🎯 Developer Experience** - Schema introspection, clear validation error messages, and comprehensive API

### Fixed
- **Schema Brittleness** - Eliminated hard-coded models that broke with schema changes
- **Manual Updates** - Reduced need for code changes when schemas evolve
- **Validation Gaps** - Comprehensive business logic validation covering all 8 categories
- **Enum Validation** - Dynamic enum validation against current schema definitions

### Technical Improvements
- **Core Components**:
  - `schema_loader.py` - Dynamic schema discovery and Pydantic model generation
  - `dynamic_validation.py` - Configuration-driven validation with 8 business rule categories
  - `boost_client.py` - High-level API using dynamic models with schema introspection
- **Example Scripts** - Complete workflow demonstrations:
  - `basic_workflow.py` - End-to-end supply chain creation and validation
  - `certification_demo.py` - Multi-certification scheme management
  - `mass_balance_example.py` - Conservation validation and efficiency tracking
  - `supply_chain_demo.py` - Complete traceability demonstration
- **Enterprise Features** - Production-ready validation, audit trails, regulatory compliance support
- **Standards Compliance** - Full support for BOOST v2.2.1+ with automatic adaptation, JSON-LD 1.1, JSON Schema Draft-07

### Migration Benefits
- **Zero Code Changes** - Most schema updates require no manual modifications
- **Future-Proof Design** - Automatically adapts to BOOST standard evolution
- **Enhanced Data Quality** - Comprehensive validation ensures higher data integrity
- **Reduced Maintenance** - Schema-driven approach eliminates brittle hard-coded models

*Resolves: #36 (Python reference implementation), addresses validation framework requirements from #37*

## [2.4.0] - 2025-07-29 - ERD Configuration Documentation and Relationship Examples

### Added
- **Comprehensive ERD Configuration Documentation** - Created detailed `ERD_CONFIGURATION.md` covering hub-and-spoke layout, entity positioning, and relationship management
- **Quick Reference Guide** - Added `QUICK_REFERENCE.md` for common ERD maintenance tasks and troubleshooting
- **Relationship Examples System** - Implemented interactive relationship examples that appear when clicking relationship lines
- **Complete TraceableUnit Relationship Examples** - Added concrete examples to all 6 TraceableUnit relationships
- **Transaction Entity Examples** - Added examples for seller organization, buyer customer, and delivery document relationships
- **Organization Entity Relationships** - Added headquarters location and operational areas relationship examples
- **TransactionBatch Relationship Examples** - Added examples for transaction membership, unit contents, and delivery location

### Enhanced
- **ERD Navigator README** - Updated with comprehensive configuration references and metadata-driven architecture details  
- **Schema README Integration** - Added ERD configuration section with boost_metadata examples and positioning guidance
- **Visual Design Documentation** - Documented 7-color thematic system with semantic meanings and emoji selection rationale
- **Maintenance Procedures** - Comprehensive troubleshooting guides and best practices for ERD system maintenance

### Fixed
- **Missing Relationship Examples** - Completed relationship examples across key entities including MaterialProcessing, MeasurementRecord, and SupplyBaseReport
- **Documentation Cross-References** - Established proper linking between ERD configuration, schema development, and maintenance guides

### Technical Improvements
- **Hub-and-Spoke Layout Documentation** - Detailed coordinate system and spacing requirements (300px minimum spacing)
- **Metadata-Driven Relationship Documentation** - Complete guide for boost_metadata structure and automatic relationship detection
- **Schema Integration Guidance** - Step-by-step procedures for adding new entities and maintaining ERD consistency
- **GitHub Pages Compatibility Verification** - Confirmed full compatibility with static file serving and CORS requirements

## [2.3.0] - 2025-07-24 - ERD Auto-Discovery and Relationship Processing

### Added
- **Auto-Discovery System** - ERD Navigator now automatically discovers all 32 entities from schema directory structure
- **Schema-Based Relationship Processing** - Relationships defined in `boost_metadata` are automatically extracted and merged with static relationships
- **Comprehensive Entity Coverage** - All 32 BOOST entities now load with proper functional area classification and positioning
- **Cache-Busting** - Aggressive cache-busting ensures schema changes are immediately reflected in ERD
- **Entity Name Conversion** - Automatic snake_case to PascalCase conversion for entity discovery (e.g., `lcfs_pathway` → `LcfsPathway`)

### Enhanced
- **LCFS Entity Integration** - Fixed entity name mismatches that prevented LCFS relationship visualization
- **TrackingPoint Relationships** - Added missing relationships to GeographicData and Operator entities
- **Boost Metadata Processing** - Streamlined processing of entity metadata from schema files with strict validation
- **Schema File Structure** - All entities now consistently use `{"schema": {...}}` wrapper format for proper loading

### Fixed
- **Entity Classification** - Resolved issue where entities were defaulting to "Analytics" area instead of their proper functional areas
- **Relationship Name Matching** - Fixed case sensitivity issues preventing LCFS relationships from displaying
- **Duplicate Metadata** - Cleaned up duplicate boost_metadata sections that were preventing entity loading
- **Server Path Resolution** - Fixed schema directory access issues for proper auto-discovery functionality

### Technical Improvements
- **Single Source of Truth** - Schema files are now the authoritative source for entity structure and relationships
- **Automated Relationship Discovery** - No manual ERD code changes needed for new entity relationships
- **Comprehensive Documentation** - Added quick reference guide for entity/attribute/relationship management processes
- **Debug Logging** - Enhanced debugging capabilities for relationship processing and entity loading

## [2.2.1] - 2025-07-23 - Repository Cleanup and ERD Consolidation

### Removed
- **Legacy ERD Files** - Eliminated 10 redundant D3.js ERD implementations from deprecated directory
- **Interactive ERD Duplication** - Removed `boost_erd_interactive.html` to eliminate code duplication with main ERD Navigator
- **GitHub Scripts** - Removed obsolete GitHub issue creation scripts from project_planning directory
- **Outdated Documentation** - Removed `BOOST_ERD_COMPREHENSIVE_README.md` and `boost_erd_styling_guide.md`
- **Redundant JSON Definitions** - Removed `boost_erd_entities_complete.json` (superseded by schema directory)

### Changed
- **Framework References** - Replaced all "Kaulen framework" references with "BOOST traceability system" 
- **Blueprint Terminology** - Updated "blueprint" references to "schema-based" or "interactive" as appropriate
- **Single ERD System** - Consolidated to single ERD Navigator as authoritative visualization system
- **File Naming** - Renamed `boost_erd_blueprint_based.html` to `boost_erd_interactive.html` (then removed)
- **Documentation Updates** - Updated all ERD references to point to main ERD Navigator (`/erd-navigator/index.html`)

### Technical Improvements
- **Reduced Maintenance Burden** - Eliminated ~25,000+ lines of redundant D3.js ERD code
- **Clear Architecture** - Single source of truth for ERD visualization with schema-driven approach
- **Simplified References** - All documentation now consistently points to main ERD Navigator
- **Repository Organization** - Cleaner file structure with removal of outdated and redundant files

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