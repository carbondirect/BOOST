The BOOST Traceability System implements a comprehensive approach to biomass supply chain tracking that addresses traditional weak points where traceability is lost during material transfers and processing operations.

## Key Implementation Features

### Progressive Identification Framework
TraceableUnit (TRU) entities maintain continuous identification through technology-appropriate methods including biometric signatures, RFID tags, QR codes, and manual identification. The multi-method approach provides data continuity while accommodating varying technology readiness levels and field conditions throughout handling and processing operations.

### Critical Tracking Points
The system establishes standardized measurement and verification infrastructure with flexible configurations. The standard three-point configuration includes:
- **harvest_site** - Initial TRU creation with appropriate identification method and volume measurement
- **consolidation_point** - Transportation consolidation points with reconciliation validation (formerly skid_road/forest_road)
- **mill_entrance** - Processing facility entry points with final verification before transformation

BOOST supports 7 tracking point types total (`harvest_site`, `consolidation_point`, `mill_entrance`, `transfer_station`, `storage_facility`, `quality_control_point`, `mobile_processing_unit`) enabling flexible configurations from 2-point minimum to 5+ point extended setups based on operational complexity.

### Multi-Species Support
Species-specific tracking capabilities enable:
- Individual species identification within mixed material flows
- Species-specific sustainability claim application and inheritance
- Detailed composition tracking with percentage validation
- Regulatory compliance for jurisdiction-specific species requirements

### Complete Processing Chain Documentation
MaterialProcessing entities provide comprehensive audit trails by:
- Linking input TRUs to output TRUs for every transformation
- Tracking plant part changes and transformations during processing
- Validating volume and mass conservation across processing steps
- Supporting split and merge operations with complete genealogy tracking