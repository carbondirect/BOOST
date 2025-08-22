The TraceableUnit represents the fundamental unit of traceability in the BOOST continuous traceability timber supply chain tracking system. A TRU can be an individual log, pile, volume aggregation, or processed batch that maintains continuous data linkage throughout its lifecycle. This entity replaces MaterialBatch as the primary traceable unit and supports biometric identification, species composition tracking, and complete audit trails.

## Required Fields

All TraceableUnit implementations MUST include the following required fields:

- **`traceableUnitId`** (string) - Unique identifier for the TRU (primary key)  
    Examples: `TRU-LOG-001`, `TRU-PILE-CA-Klamath-042`

- **`unitType`** (string enum) - Type of traceable unit  
    Valid values: `individual_log`, `pile`, `volume_aggregation`, `processed_batch`

- **`uniqueIdentifier`** (string) - Biometric signature, RFID tag, or QR code  
    Examples: `BIO-OAK-12345`, `RFID-TAG-67890`, `QR-CODE-ABC123`

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

### Biometric Identification
TRUs support multiple identification methods without requiring physical attachments:
- Optical pattern recognition of grain, bark, or cut surfaces
- RFID tags for conventional tracking
- QR codes for human-readable identification
- Biometric signatures for tamper-proof identification

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