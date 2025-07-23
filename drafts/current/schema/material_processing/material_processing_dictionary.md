# Data Dictionary

## MaterialProcessing

### Overview
The `MaterialProcessing` entity tracks all technical manipulations with input/output TRU references and species composition changes to support complete audit trails in the BOOST traceability system. This entity captures every processing operation that transforms, moves, or modifies TRUs throughout the supply chain, maintaining complete traceability and volume conservation validation.

### Fields

| Field                        | Type             | Required | Description                                                                 | Examples                                    |
|-----------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `processingId`              | string           | Yes      | Unique identifier for the processing operation (primary key)              | `PROC-001`, `PROC-FELL-KLA-042`           |
| `inputTraceableUnitId`      | string (FK)      | Yes      | Foreign key to input TRU being processed                                 | `TRU-TREE-001`, `TRU-LOG-CA-042`          |
| `outputTraceableUnitId`     | string (FK)      | Yes      | Foreign key to output TRU created (may be same as input)                 | `TRU-LOG-001`, `TRU-PILE-CA-042`          |
| `processType`               | string           | Yes      | Type of processing operation (enum)                                       | `felling`, `delimbing`, `crosscutting`, `chipping`, `debarking`, `assortment` |
| `processTimestamp`          | string (date-time)| Yes     | When the processing operation occurred                                    | `2025-07-15T07:15:00Z`                    |
| `processingGeographicDataId`| string (FK)      | No       | Foreign key to location where processing occurred                         | `GEO-HARVEST-SITE-001`, `GEO-MILL-001`    |
| `operatorId`                | string (FK)      | No       | Foreign key to operator who performed processing                          | `OP-HARVESTER-001`, `OP-MILL-TECH-02`     |
| `inputComposition`          | string           | No       | Species composition before processing                                     | `Douglas Fir: 100%`, `Mixed: DF 60%, PP 40%` |
| `outputComposition`         | string           | No       | Species composition after processing                                      | `Douglas Fir: 100%`, `Separated by species` |
| `inputVolume`               | number           | Yes      | Input volume before processing (cubic meters)                            | `25.5`, `85.25`, `150.0`                  |
| `outputVolume`              | number           | Yes      | Output volume after processing (cubic meters)                            | `24.2`, `80.75`, `140.5`                  |
| `volumeLoss`                | number           | No       | Volume lost during processing (cubic meters)                             | `1.3`, `4.5`, `9.5`                       |
| `qualityMetrics`            | string           | No       | Quality measurements and assessments                                      | `Grade A: 80%, Grade B: 20%`, `Moisture: 12%` |
| `equipmentUsed`             | string           | No       | Equipment used for processing                                             | `harvester_head`, `chainsaw`, `chipper`, `debarker` |
| `@id`                       | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/material-processing/PROC-001` |
| `lastUpdated`               | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Processing Types

1. **felling**
   - Tree cutting and initial processing
   - Standing tree to log conversion
   - Initial volume measurement
   - Species identification and verification
   - Primary processing operation

2. **delimbing**
   - Branch removal from felled trees
   - Clean stem preparation
   - Volume refinement and measurement
   - Quality assessment after delimbing
   - Preparation for transport or further processing

3. **crosscutting**
   - Log cutting to specified lengths
   - Length optimization for market requirements
   - Multiple output logs from single input
   - Volume distribution and measurement
   - Quality grade assignment

4. **chipping**
   - Conversion to wood chips
   - Volume reduction and format change
   - Species mixing or separation
   - Moisture content adjustment
   - Final product preparation

5. **debarking**
   - Bark removal from logs
   - Clean wood preparation for processing
   - Volume loss measurement
   - Bark disposal or utilization tracking
   - Quality improvement operation

6. **assortment**
   - Sorting and classification by quality/species
   - Grade assignment and segregation
   - Market specification preparation
   - Quality-based value optimization
   - Inventory organization

### Key Features

1. **Complete Processing Chain Tracking**
   - Input/output TRU relationship mapping
   - Chronological processing sequence
   - Volume conservation validation
   - Quality transformation tracking
   - Operator accountability

2. **Species Composition Management**
   - Before/after species composition tracking
   - Multi-species processing support
   - Species separation and mixing operations
   - Composition validation and verification
   - Biodiversity impact assessment

3. **Volume Conservation Validation**
   - Input volume measurement
   - Output volume calculation
   - Volume loss quantification and justification
   - Processing efficiency metrics
   - Mass balance verification

4. **Quality Transformation Tracking**
   - Quality metrics before and after processing
   - Grade assignment and modification
   - Defect identification and impact
   - Processing quality assurance
   - Value optimization tracking

### Processing Efficiency Metrics

1. **Volume Recovery Rates**
   - Standard recovery rates by processing type
   - Equipment-specific efficiency tracking
   - Operator performance metrics
   - Quality impact on recovery rates

2. **Quality Transformation**
   - Grade improvement through processing
   - Defect removal effectiveness
   - Value-added processing metrics
   - Market specification achievement

3. **Species-Specific Processing**
   - Species-appropriate processing methods
   - Species-specific recovery rates
   - Quality outcomes by species
   - Processing optimization by species

### Validation Rules

1. **TRU Relationship Validation**
   - inputTraceableUnitId must reference existing TRU
   - outputTraceableUnitId must be created or reference existing TRU
   - processTimestamp must be ≥ input TRU creation timestamp
   - Output TRU creation must be ≥ processTimestamp

2. **Volume Conservation**
   - outputVolume + volumeLoss should approximately equal inputVolume
   - Volume loss must be reasonable for processing type
   - Volume calculations must account for species composition changes

3. **Processing Logic**
   - Processing type must be appropriate for input TRU type
   - Equipment must be suitable for processing type
   - Operator must be qualified for processing operation
   - Location must support specified processing type

### Example Use Cases

1. **Tree Felling Operation**
   - Input: Standing tree (estimated volume)
   - Process: Felling with chainsaw
   - Output: Felled tree/log with measured volume
   - Volume loss: Sawdust and cutting waste
   - Quality assessment: Initial grade assignment

2. **Log Crosscutting**
   - Input: Long log (25.5 m³)
   - Process: Crosscutting to market lengths
   - Output: Multiple shorter logs (24.2 m³ total)
   - Volume loss: Saw kerf and end trim (1.3 m³)
   - Quality: Length optimization for grade recovery

3. **Multi-Species Pile Processing**
   - Input: Mixed species pile
   - Process: Species sorting and assortment
   - Output: Separate species piles
   - Composition change: Mixed to segregated
   - Quality improvement through sorting

### Relationships
- MaterialProcessing consumes one input TraceableUnit
- MaterialProcessing produces one output TraceableUnit
- MaterialProcessing located at one GeographicData location
- MaterialProcessing performed by one Operator
- MaterialProcessing generates MeasurementRecord entries
- MaterialProcessing triggers LocationHistory events
- MaterialProcessing supports TRU split/merge operations
- MaterialProcessing enables processing chain audit trails