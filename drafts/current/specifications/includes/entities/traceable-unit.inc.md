The TraceableUnit represents the fundamental unit of traceability in the BOOST timber supply chain tracking system. A TRU can be an individual log, pile, volume aggregation, or processed batch that maintains continuous data linkage throughout its lifecycle. This entity replaces MaterialBatch as the primary traceable unit and supports flexible identification methods, species composition tracking, and complete audit trails.

## Required Fields

All TraceableUnit implementations MUST include the following required fields:

- **`traceableUnitId`** (string) - Unique identifier for the TRU (primary key)  
    Examples: `TRU-LOG-001`, `TRU-PILE-CA-Klamath-042`

- **`unitType`** (string enum) - Type of traceable unit  
    Valid values: `individual_log`, `pile`, `volume_aggregation`, `processed_batch`

- **`uniqueIdentifier`** (string) - Trip ticket ID, RFID tag, QR code, or biometric signature  
    Examples: `TRIP-2025-001234`, `RFID-TAG-67890`, `QR-CODE-ABC123`, `BIO-OAK-12345`

- **`totalVolumeM3`** (number) - Total volume in cubic meters  
    Examples: `12.5`, `250.75`, `1000.0`

- **`createdTimestamp`** (string, ISO 8601) - When the TRU was created  
    Example: `2025-07-21T08:30:00Z`

- **`harvesterId`** (string, foreign key) - Reference to harvesting organization  
    Example: `ORG-HARVESTER-001`

- **`materialTypeId`** (string, foreign key) - Reference to Material entity  
    Examples: `MAT-TYPE-PINE`, `MAT-TYPE-FIR`

- **`isMultiSpecies`** (boolean) - Flag indicating multiple species composition  
    Values: `true`, `false`

## Optional Fields

TraceableUnit entities MAY include additional fields for enhanced tracking:

- **Geographic Information**: `currentGeographicDataId`, `harvestGeographicDataId`
- **Processing Information**: `processingHistory`, `attachedInformation`
- **Quality Classification**: `assortmentType`, `qualityGrade`
- **Hierarchical Relationships**: `parentTraceableUnitId`, `childTraceableUnitIds`
- **Status Tracking**: `currentStatus`, `sustainabilityCertification`

## Key Capabilities

### Flexible Identification Methods
TRUs support multiple identification approaches to accommodate current industry practices and future technologies:
- **Trip Tickets**: Current industry standard with unique delivery numbers
- **RFID Tags**: Automated tracking systems for equipment and load identification  
- **QR Codes**: Human-readable codes linking to digital records
- **Manual Documentation**: Paper-based tracking with reference numbers
- **Biometric Signatures**: Emerging optical pattern recognition technology

### Current Industry Integration
BOOST TraceableUnits integrate seamlessly with existing forest industry workflows:

**Trip Ticket Integration**: Existing trip ticket systems can populate the `uniqueIdentifier` field with delivery numbers, enabling immediate BOOST adoption without changing current documentation practices. Additional TRU fields capture enhanced tracking data while maintaining compatibility with established transportation and delivery workflows.

**Legacy System Compatibility**: TRUs accommodate existing identification schemes through flexible field mapping, allowing gradual system integration without disrupting ongoing operations.

### Multi-Species Support
When `isMultiSpecies` is true, TRUs can reference multiple SpeciesComponent entities to track:
- Individual species percentages within mixed materials
- Species-specific sustainability claims
- Regulatory compliance for species-specific requirements

### Processing Chain Integration
TRUs maintain complete audit trails through:
- Processing history references linking all transformation operations
- Parent-child relationships for split and merge operations
- Status tracking throughout the supply chain lifecycle