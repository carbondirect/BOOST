# BOOST Schema Changelog

All notable changes to the BOOST (Biomass Origin and Supply Tracking) schema and reference implementations will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.6.0] - 2025-01-31

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

---

## Previous Versions

### [2.5.1] - Earlier 2025 releases  
- Schema robustness improvements and validation enhancements
- ERD auto-discovery and comprehensive documentation
- LCFS pathway integration and compliance features
- Mass balance account and energy carbon data entities

### [2.0.0 - 2.5.0] - Major releases
- Comprehensive entity relationship documentation
- Advanced validation framework implementation
- Cross-entity validation and business logic rules
- JSON-LD context and semantic web compatibility

### [1.0.0 - 1.2.0] - Foundation releases
- Initial BOOST schema implementation
- Core entity definitions and relationships
- Basic validation framework
- Python reference implementation foundation