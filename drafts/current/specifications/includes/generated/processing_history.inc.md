<!-- Auto-generated from processing_history/validation_schema.json -->

Complete timeline of processing events with moisture tracking

**🗂️ [View Processing History in ERD Navigator](erd-navigator/index.html?focus=ProcessingHistory)**

### Relationships ### {{.unnumbered}}

- **processingHistoryId** → [[#processing-history|Processing History]] - Unique identifier for the processing history record
- **traceableUnitId** → [[#traceable-unit|Traceable Unit]] - Foreign key to TRU this history record belongs to
- **materialProcessingId** → [[#material-processing|Material Processing]] - Foreign key to MaterialProcessing operation
- **operatorId** → [[#operator|Operator]] - Foreign key to operator who performed processing

### Properties ### {{.unnumbered}}

<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Description
<th>Required
</tr>
</thead>
<tbody>
<tr>
<td><code>@context</code>
<td>object (structured)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>enum(ProcessingHistory)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>inputTRUIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of input TRU IDs (multiple for merge operations)
<td>✓
</tr>
<tr>
<td><code>materialProcessingId</code>
<td>string (pattern)
<td>Foreign key to MaterialProcessing operation
<td>✓
</tr>
<tr>
<td><code>outputTRUIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of output TRU IDs (multiple for split operations)
<td>✓
</tr>
<tr>
<td><code>processSequenceNumber</code>
<td>integer
<td>Sequential order of this processing step for the TRU
<td>✓
</tr>
<tr>
<td><code>processingEventType</code>
<td>enum(7 values)
<td>Type of processing event
<td>✓
</tr>
<tr>
<td><code>processingHistoryId</code>
<td>string (pattern)
<td>Unique identifier for the processing history record
<td>✓
</tr>
<tr>
<td><code>timestamp</code>
<td>string (date-time)
<td>When this processing step occurred
<td>✓
</tr>
<tr>
<td><code>traceableUnitId</code>
<td>string (pattern)
<td>Foreign key to TRU this history record belongs to
<td>✓
</tr>
<tr>
<td><code>claimInheritanceData</code>
<td>object (structured)
<td>Sustainability claim inheritance tracking
<td>
</tr>
<tr>
<td><code>equipmentUsed</code>
<td>string
<td>Equipment used for this processing step
<td>
</tr>
<tr>
<td><code>isCurrentProcessingState</code>
<td>boolean
<td>True if this represents the current processing state
<td>
</tr>
<tr>
<td><code>mediaBreakData</code>
<td>object (structured)
<td>Media break detection and recovery information
<td>
</tr>
<tr>
<td><code>nextProcessingHistoryIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of next processing history record IDs (for split operations)
<td>
</tr>
<tr>
<td><code>operatorId</code>
<td>string (pattern)
<td>Foreign key to operator who performed processing
<td>
</tr>
<tr>
<td><code>plantPartTransformation</code>
<td>string
<td>Summary of plant part changes during processing
<td>
</tr>
<tr>
<td><code>previousProcessingHistoryId</code>
<td>string | null
<td>Foreign key to previous processing history record (forms chain)
<td>
</tr>
<tr>
<td><code>processingDuration</code>
<td>string (pattern)
<td>ISO 8601 duration format for processing time
<td>
</tr>
<tr>
<td><code>processingGeographicDataId</code>
<td>string (pattern)
<td>Foreign key to location where processing occurred
<td>
</tr>
<tr>
<td><code>qualityChangeDescription</code>
<td>string
<td>Description of quality changes during processing
<td>
</tr>
<tr>
<td><code>speciesCompositionChange</code>
<td>enum(5 values)
<td>How species composition changed during processing
<td>
</tr>
<tr>
<td><code>volumeChangeRatio</code>
<td>number (≥0, ≤2.0)
<td>Ratio of output volume to input volume (1.0 = no change)
<td>
</tr>
<tr>
<td><code>volumeConservationData</code>
<td>object (structured)
<td>Volume conservation validation data
<td>
</tr>
</tbody>
</table>

## ProcessingHistory
### Overview
The `ProcessingHistory` entity provides chronological tracking of all processing operations that affect a TracableUnit throughout its lifecycle. This entity creates a complete audit trail of transformations, movements, and quality changes, enabling comprehensive genealogy tracking and supporting media-interruption-free traceability requirements of the BOOST traceability system.
ProcessingHistory serves as the TRU-centric complement to the operation-centric MaterialProcessing entity, providing a unified timeline view of how materials evolve through the supply chain.
### Purpose
- **Chronological Processing Timeline**: Complete ordered sequence of processing events for each TRU
- **Genealogy Tracking**: Parent/child relationships through split and merge operations  
- **Volume Conservation Validation**: Track volume changes and losses across processing chain
- **Claim Inheritance Management**: Sustainability claim propagation through processing steps
- **Audit Trail Completeness**: Support regulatory compliance and third-party verification
- **Processing Analytics**: Enable business intelligence on processing efficiency and quality
### Fields
<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Required
<th>Description
<th>Examples
</tr>
</thead>
<tbody>
<tr>
<td>`processingHistoryId`
<td>string
<td>Yes
<td>Unique identifier for the processing history record (primary key)
<td>`PROC-HIST-TRU-LOG-CA-042-001`, `PROC-HIST-SPLIT-KLA-015`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU this history record belongs to
<td>`TRU-LOG-CA-042`, `TRU-PILE-SORTED-001`
</tr>
<tr>
<td>`materialProcessingId`
<td>string (FK)
<td>Yes
<td>Foreign key to MaterialProcessing operation that created this history
<td>`PROC-FELL-KLA-042`, `PROC-CROSSCUT-001`
</tr>
<tr>
<td>`timestamp`
<td>string (date-time)
<td>Yes
<td>When this processing step occurred
<td>`2025-07-15T08:30:00Z`
</tr>
<tr>
<td>`processSequenceNumber`
<td>integer
<td>Yes
<td>Sequential order of this processing step for the TRU (starts at 1)
<td>`1`, `2`, `3`
</tr>
<tr>
<td>`processingEventType`
<td>string
<td>Yes
<td>Type of processing event (enum)
<td>`transformation`, `split`, `merge`, `quality_change`, `loading`
</tr>
<tr>
<td>`inputTRUIds`
<td>string[]
<td>Yes
<td>Array of input TRU IDs (multiple for merge operations)
<td>`["TRU-TREE-CA-042"]`, `["TRU-LOG-001", "TRU-LOG-002"]`
</tr>
<tr>
<td>`outputTRUIds`
<td>string[]
<td>Yes
<td>Array of output TRU IDs (multiple for split operations)
<td>`["TRU-LOG-CA-042"]`, `["TRU-PILE-A", "TRU-PILE-B"]`
</tr>
<tr>
<td>`processingDuration`
<td>string (ISO8601)
<td>No
<td>ISO 8601 duration format for processing time
<td>`PT45M`, `PT2H30M`, `PT1D`
</tr>
<tr>
<td>`qualityChangeDescription`
<td>string
<td>No
<td>Description of quality changes during processing
<td>`Grade assessment: A-grade sawlog`, `Moisture reduced from 25% to 15%`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Foreign key to operator who performed processing
<td>`OP-HARVESTER-KLA-001`, `OP-MILL-TECH-02`
</tr>
<tr>
<td>`equipmentUsed`
<td>string
<td>No
<td>Equipment used for this processing step
<td>`harvester_head_001`, `crosscut_saw`, `loader_CAT_320`
</tr>
<tr>
<td>`volumeChangeRatio`
<td>number
<td>No
<td>Ratio of output volume to input volume (1.0 = no change)
<td>`0.94`, `1.0`, `0.85`
</tr>
<tr>
<td>`speciesCompositionChange`
<td>string
<td>No
<td>How species composition changed during processing (enum)
<td>`unchanged`, `separated`, `mixed`
</tr>
<tr>
<td>`plantPartTransformation`
<td>string
<td>No
<td>Summary of plant part changes during processing
<td>`trunk→trunk (sized)`, `branches→chips`
</tr>
<tr>
<td>`isCurrentProcessingState`
<td>boolean
<td>No
<td>True if this represents the current processing state
<td>`true`, `false`
</tr>
<tr>
<td>`processingGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where processing occurred
<td>`GEO-HARVEST-KLAMATH-04`, `GEO-MILL-001`
</tr>
<tr>
<td>`previousProcessingHistoryId`
<td>string (FK)
<td>No
<td>Foreign key to previous processing history record (forms chain)
<td>`PROC-HIST-TRU-LOG-CA-042-001`, `null`
</tr>
<tr>
<td>`nextProcessingHistoryIds`
<td>string[]
<td>No
<td>Array of next processing history record IDs (for split operations)
<td>`["PROC-HIST-TRU-042-002"]`, `["PROC-HIST-A", "PROC-HIST-B"]`
</tr>
<tr>
<td>`volumeConservationData`
<td>object
<td>No
<td>Volume conservation validation data
<td>See Volume Conservation section
</tr>
<tr>
<td>`mediaBreakData`
<td>object
<td>No
<td>Media break detection and recovery information
<td>See Media Break section
</tr>
<tr>
<td>`claimInheritanceData`
<td>object
<td>No
<td>Sustainability claim inheritance tracking
<td>See Claim Inheritance section
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/processing-history/PROC-HIST-001`
</tr>
</tbody>
</table>
### Processing Event Types
1. **transformation**
     Standard processing operations that change material characteristics
     Includes felling, delimbing, crosscutting, chipping, debarking
     Single input TRU → Single output TRU with changed properties
     Volume, quality, or plant part composition changes
2. **split**
     One input TRU divided into multiple output TRUs
     Examples: Log crosscutting, pile sorting by grade, load division
     Single input TRU → Multiple output TRUs
     Volume conservation across all outputs required
3. **merge**
     Multiple input TRUs combined into single output TRU
     Examples: Pile consolidation, load combining, batch aggregation
     Multiple input TRUs → Single output TRU
     Species and plant part composition tracking required
4. **quality_change**
     Processing that primarily affects quality without volume change
     Examples: Grading, moisture testing, defect assessment
     Quality characteristics updated without physical transformation
     May trigger claim validation requirements
5. **loading** 
     Transportation-related processing with material transformation
     Examples: Pile to truck conversion with volume settling
     Configuration or accessibility changes during transport preparation
     Bridges pure movement (LocationHistory) with processing
6. **transport_processing**
     Processing operations that occur during transportation
     Examples: In-transit sorting, consolidation stops, quality monitoring
     Combines spatial movement with material transformation
     Requires both ProcessingHistory and LocationHistory records
7. **measurement**
     Processing events focused on data collection and validation
     Examples: Volume reconciliation, biometric scanning, quality testing
     May not change material but updates TRU characteristics
     Critical for media-break prevention and data validation
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
### Integration with BOOST Traceability System
ProcessingHistory directly supports BOOST traceability system requirements:
- **Media-Interruption-Free Traceability**: Complete chronological processing chain
- **Volume Conservation**: Detailed tracking of volume changes and losses  
- **Biometric Integration**: Links to biometric identification at each processing step
- **Three Critical Tracking Points**: Processing events at harvest, transport, and mill locations
- **Equipment Integration**: Direct connection to harvesting and processing equipment data
