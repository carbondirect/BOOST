# Data Dictionary

## ProcessingHistory

### Overview
The `ProcessingHistory` entity provides chronological tracking of all processing operations that affect a TracableUnit throughout its lifecycle. This entity creates a complete audit trail of transformations, movements, and quality changes, enabling comprehensive genealogy tracking and supporting media-interruption-free traceability requirements of the Kaulen framework.

ProcessingHistory serves as the TRU-centric complement to the operation-centric MaterialProcessing entity, providing a unified timeline view of how materials evolve through the supply chain.

### Purpose
- **Chronological Processing Timeline**: Complete ordered sequence of processing events for each TRU
- **Genealogy Tracking**: Parent/child relationships through split and merge operations  
- **Volume Conservation Validation**: Track volume changes and losses across processing chain
- **Claim Inheritance Management**: Sustainability claim propagation through processing steps
- **Audit Trail Completeness**: Support regulatory compliance and third-party verification
- **Processing Analytics**: Enable business intelligence on processing efficiency and quality

### Fields

| Field                        | Type             | Required | Description                                                                 | Examples                                    |
|-----------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `processingHistoryId`       | string           | Yes      | Unique identifier for the processing history record (primary key)        | `PROC-HIST-TRU-LOG-CA-042-001`, `PROC-HIST-SPLIT-KLA-015` |
| `traceableUnitId`           | string (FK)      | Yes      | Foreign key to TRU this history record belongs to                        | `TRU-LOG-CA-042`, `TRU-PILE-SORTED-001`   |
| `materialProcessingId`      | string (FK)      | Yes      | Foreign key to MaterialProcessing operation that created this history    | `PROC-FELL-KLA-042`, `PROC-CROSSCUT-001`  |
| `timestamp`                 | string (date-time)| Yes     | When this processing step occurred                                        | `2025-07-15T08:30:00Z`                    |
| `processSequenceNumber`     | integer          | Yes      | Sequential order of this processing step for the TRU (starts at 1)      | `1`, `2`, `3`                              |
| `processingEventType`       | string           | Yes      | Type of processing event (enum)                                          | `transformation`, `split`, `merge`, `quality_change`, `loading` |
| `inputTRUIds`               | string[]         | Yes      | Array of input TRU IDs (multiple for merge operations)                  | `["TRU-TREE-CA-042"]`, `["TRU-LOG-001", "TRU-LOG-002"]` |
| `outputTRUIds`              | string[]         | Yes      | Array of output TRU IDs (multiple for split operations)                 | `["TRU-LOG-CA-042"]`, `["TRU-PILE-A", "TRU-PILE-B"]` |
| `processingDuration`        | string (ISO8601) | No       | ISO 8601 duration format for processing time                            | `PT45M`, `PT2H30M`, `PT1D`                |
| `qualityChangeDescription` | string           | No       | Description of quality changes during processing                          | `Grade assessment: A-grade sawlog`, `Moisture reduced from 25% to 15%` |
| `operatorId`                | string (FK)      | No       | Foreign key to operator who performed processing                         | `OP-HARVESTER-KLA-001`, `OP-MILL-TECH-02` |
| `equipmentUsed`             | string           | No       | Equipment used for this processing step                                  | `harvester_head_001`, `crosscut_saw`, `loader_CAT_320` |
| `volumeChangeRatio`         | number           | No       | Ratio of output volume to input volume (1.0 = no change)               | `0.94`, `1.0`, `0.85`                     |
| `speciesCompositionChange`  | string           | No       | How species composition changed during processing (enum)                 | `unchanged`, `separated`, `mixed`          |
| `plantPartTransformation`   | string           | No       | Summary of plant part changes during processing                          | `trunk→trunk (sized)`, `branches→chips`   |
| `isCurrentProcessingState`  | boolean          | No       | True if this represents the current processing state                     | `true`, `false`                            |
| `processingGeographicDataId`| string (FK)      | No       | Foreign key to location where processing occurred                        | `GEO-HARVEST-KLAMATH-04`, `GEO-MILL-001`  |
| `previousProcessingHistoryId`| string (FK)     | No       | Foreign key to previous processing history record (forms chain)         | `PROC-HIST-TRU-LOG-CA-042-001`, `null`    |
| `nextProcessingHistoryIds`  | string[]         | No       | Array of next processing history record IDs (for split operations)     | `["PROC-HIST-TRU-042-002"]`, `["PROC-HIST-A", "PROC-HIST-B"]` |
| `volumeConservationData`    | object           | No       | Volume conservation validation data                                      | See Volume Conservation section            |
| `mediaBreakData`            | object           | No       | Media break detection and recovery information                           | See Media Break section                   |
| `claimInheritanceData`      | object           | No       | Sustainability claim inheritance tracking                                | See Claim Inheritance section             |
| `@id`                       | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                       | `https://github.com/carbondirect/BOOST/schemas/processing-history/PROC-HIST-001` |

### Processing Event Types

1. **transformation**
   - Standard processing operations that change material characteristics
   - Includes felling, delimbing, crosscutting, chipping, debarking
   - Single input TRU → Single output TRU with changed properties
   - Volume, quality, or plant part composition changes

2. **split**
   - One input TRU divided into multiple output TRUs
   - Examples: Log crosscutting, pile sorting by grade, load division
   - Single input TRU → Multiple output TRUs
   - Volume conservation across all outputs required

3. **merge**
   - Multiple input TRUs combined into single output TRU
   - Examples: Pile consolidation, load combining, batch aggregation
   - Multiple input TRUs → Single output TRU
   - Species and plant part composition tracking required

4. **quality_change**
   - Processing that primarily affects quality without volume change
   - Examples: Grading, moisture testing, defect assessment
   - Quality characteristics updated without physical transformation
   - May trigger claim validation requirements

5. **loading** 
   - Transportation-related processing with material transformation
   - Examples: Pile to truck conversion with volume settling
   - Configuration or accessibility changes during transport preparation
   - Bridges pure movement (LocationHistory) with processing

6. **transport_processing**
   - Processing operations that occur during transportation
   - Examples: In-transit sorting, consolidation stops, quality monitoring
   - Combines spatial movement with material transformation
   - Requires both ProcessingHistory and LocationHistory records

7. **measurement**
   - Processing events focused on data collection and validation
   - Examples: Volume reconciliation, biometric scanning, quality testing
   - May not change material but updates TRU characteristics
   - Critical for media-break prevention and data validation

### Volume Conservation Data

Complex object tracking volume conservation across processing operations:

```json
{
  "totalInputVolume": 25.5,
  "totalOutputVolume": 24.2, 
  "volumeLoss": 1.3,
  "lossReason": "sawdust",
  "conservationValidated": true
}
```

**Volume Loss Reasons:**
- `sawdust`: Material lost as sawdust during cutting operations
- `trimming`: Volume lost during quality improvement trimming
- `moisture_loss`: Volume reduction due to drying/seasoning
- `handling_damage`: Volume lost due to handling damage
- `sorting_loss`: Volume lost during sorting/grading operations  
- `measurement_variance`: Apparent loss due to measurement differences

### Media Break Data

Information about media breaks and recovery procedures:

```json
{
  "mediaBreakOccurred": false,
  "breakDuration": null,
  "breakReason": null, 
  "recoveryMethod": null,
  "dataIntegrityValidated": true
}
```

**Media Break Recovery Methods:**
- `biometric_verification`: Recovery using optical biometric patterns
- `rfid_backup`: Recovery using backup RFID identification
- `operator_verification`: Manual verification by qualified operator
- `measurement_reconciliation`: Recovery through volume/dimension matching

### Claim Inheritance Data

Tracking sustainability claim inheritance through processing:

```json
{
  "inheritedClaims": ["CLAIM-FSC-MIX-KLA-042"],
  "newClaims": ["CLAIM-GRADE-A-SAWLOG"],
  "claimValidationRequired": true,
  "claimValidationCompleted": true
}
```

### Relationships

- **ProcessingHistory** belongs to **TraceableUnit** (many-to-one)
- **ProcessingHistory** references **MaterialProcessing** (many-to-one)  
- **ProcessingHistory** references **GeographicData** (many-to-one)
- **ProcessingHistory** references **Operator** (many-to-one)
- **ProcessingHistory** forms processing chains with other **ProcessingHistory** records (linked list)
- **ProcessingHistory** supports split/merge through multiple input/output TRU references

### Usage Examples

#### Simple Transformation Chain
```sql
-- Get complete processing timeline for TRU
SELECT * FROM ProcessingHistory 
WHERE traceableUnitId = 'TRU-LOG-CA-042'
ORDER BY processSequenceNumber;
```

#### Split Operation Tracking  
```sql
-- Find all TRUs created from split operation
SELECT outputTRUIds FROM ProcessingHistory
WHERE processingEventType = 'split' 
AND 'TRU-PILE-ORIGINAL' = ANY(inputTRUIds);
```

#### Volume Conservation Analysis
```sql
-- Analyze volume losses by processing type
SELECT 
  mph.processType,
  AVG(ph.volumeChangeRatio) as avg_recovery_rate,
  SUM((ph.volumeConservationData->>'volumeLoss')::numeric) as total_loss
FROM ProcessingHistory ph
JOIN MaterialProcessing mph ON ph.materialProcessingId = mph.processingId
GROUP BY mph.processType;
```

### Transportation Classification Framework

This entity supports the transportation classification framework where:

1. **Pure Transportation** → LocationHistory only (spatial movement)
2. **Transformative Transportation** → ProcessingHistory + MaterialProcessing (material changes)  
3. **Complex Transportation** → Both ProcessingHistory and LocationHistory (movement + transformation)

See transportation classification documentation for detailed decision framework.

### Business Rules

1. **Sequence Integrity**: ProcessSequenceNumber must be sequential and unique per TRU
2. **Volume Conservation**: Total input volume should equal total output volume plus documented losses
3. **Claim Inheritance**: Claims must be properly inherited based on volume percentages and processing type
4. **Media Break Prevention**: Each processing step must maintain traceability chain integrity
5. **Geographic Consistency**: Processing location should be consistent with LocationHistory records
6. **Temporal Ordering**: Timestamp sequence should align with processSequenceNumber ordering

### Integration with Kaulen Framework

ProcessingHistory directly supports Kaulen framework requirements:

- **Media-Interruption-Free Traceability**: Complete chronological processing chain
- **Volume Conservation**: Detailed tracking of volume changes and losses  
- **Biometric Integration**: Links to biometric identification at each processing step
- **Three Critical Tracking Points**: Processing events at harvest, transport, and mill locations
- **Equipment Integration**: Direct connection to harvesting and processing equipment data