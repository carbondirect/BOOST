The ProcessingHistory entity provides chronological tracking of all processing operations that affect a TraceableUnit throughout its lifecycle. This entity creates a complete audit trail of transformations, movements, and quality changes, enabling comprehensive genealogy tracking and supporting media-interruption-free traceability requirements of the BOOST traceability system.

ProcessingHistory serves as the TRU-centric complement to the operation-centric MaterialProcessing entity, providing a unified timeline view of how materials evolve through the supply chain.

## Required Fields

All ProcessingHistory implementations MUST include the following required fields:

- **`processingHistoryId`** (string) - Unique identifier for processing history record (primary key)  
    Examples: `PROC-HIST-TRU-LOG-CA-042-001`, `PROC-HIST-SPLIT-KLA-015`

- **`traceableUnitId`** (string, foreign key) - Reference to TRU this history record belongs to  
    Examples: `TRU-LOG-CA-042`, `TRU-PILE-SORTED-001`

- **`materialProcessingId`** (string, foreign key) - Reference to MaterialProcessing operation  
    Examples: `PROC-FELL-KLA-042`, `PROC-CROSSCUT-001`

- **`processType`** (string enum) - Type of processing operation performed  
    Valid values: `harvest`, `transport`, `sort`, `crosscut`, `debarking`, `drying`, `sawmill`, `split`, `merge`

- **`processTimestamp`** (string, ISO 8601) - When processing operation occurred  
    Examples: `2025-07-21T14:30:00Z`, `2025-07-22T09:15:00Z`

- **`inputVolumeM3`** (number) - Volume before processing operation  
    Examples: `25.5`, `100.75`, `0.0` (for new TRU creation)

- **`outputVolumeM3`** (number) - Volume after processing operation  
    Examples: `22.8`, `95.25`, `150.0` (for TRU merge operations)

## Optional Fields

ProcessingHistory entities MAY include additional fields for enhanced tracking:

- **`qualityGradeBefore`** (string) - Quality grade before processing  
    Examples: `Grade-A`, `Grade-B`, `Sawlog`, `Pulpwood`

- **`qualityGradeAfter`** (string) - Quality grade after processing  
    Examples: `Grade-A`, `Grade-B`, `Sawlog`, `Pulpwood`

- **`volumeLossReason`** (string) - Explanation for volume changes  
    Examples: `moisture-loss`, `defect-removal`, `bark-removal`, `processing-waste`

- **`parentTraceableUnitIds`** (array<string>) - Source TRUs for merge operations  
    Example: `["TRU-LOG-001", "TRU-LOG-002"]`

- **`childTraceableUnitIds`** (array<string>) - Resulting TRUs from split operations  
    Example: `["TRU-LOG-003", "TRU-LOG-004", "TRU-CHIP-001"]`

- **`processingNotes`** (string) - Additional processing details  
    Examples: `"Removed bark defects"`, `"Split log at defect location"`

- **`moistureContentBefore`** (number) - Moisture content percentage before processing  
    Examples: `45.2`, `18.5`, `25.0`

- **`moistureContentAfter`** (number) - Moisture content percentage after processing  
    Examples: `42.1`, `15.2`, `12.0`

- **`operatorId`** (string, foreign key) - Reference to processing operator  
    Examples: `OP-SAWYER-001`, `OP-MACHINE-FORWARDER-03`

## Key Capabilities

### Chronological Processing Timeline
ProcessingHistory maintains complete ordered sequences of processing events:
- Time-stamped processing operations in chronological order
- Volume conservation tracking across all processing steps
- Quality grade evolution throughout TRU lifecycle
- Complete audit trail from harvest to end product

### Genealogy Tracking
Support for complex parent-child relationships:
- **Split Operations**: Single TRU becomes multiple child TRUs
- **Merge Operations**: Multiple parent TRUs combine into single TRU
- **Processing Chains**: Linked sequence of transformations
- **Volume Conservation**: Mathematical validation of input/output volumes

### Claim Inheritance Management
Sustainability claims propagation through processing:
- Certification claim tracking through processing chain
- Percentage-based claim allocation for split operations
- Claim validation against processing requirements
- Regulatory compliance documentation

### Business Intelligence Support
ProcessingHistory enables advanced analytics:
- Processing efficiency measurement and optimization
- Volume recovery rate analysis across operations
- Quality improvement tracking through processing steps
- Equipment performance monitoring and maintenance scheduling