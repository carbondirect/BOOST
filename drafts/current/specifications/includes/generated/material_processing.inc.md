<!-- Auto-generated from material_processing/validation_schema.json -->

Processing operations that transform TRUs with plant part tracking

**[View Material Processing in ERD Navigator](erd-navigator/index.html?focus=MaterialProcessing)**

### Relationships ### {{.unnumbered}}

- **operatorId** → [[#operator|Operator]]

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
<td>enum(MaterialProcessing)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>inputTraceableUnitId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>inputVolume</code>
<td>number (≥0)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>outputTraceableUnitId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>outputVolume</code>
<td>number (≥0)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>processTimestamp</code>
<td>string (date-time)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>processType</code>
<td>enum(6 values)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>processingId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>equipmentUsed</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>inputComposition</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>inputPlantParts</code>
<td>object (structured)
<td>Plant parts in input TRU before processing
<td>
</tr>
<tr>
<td><code>operatorId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
<tr>
<td><code>outputComposition</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>outputPlantParts</code>
<td>object (structured)
<td>Plant parts in output TRU after processing
<td>
</tr>
<tr>
<td><code>plantPartLosses</code>
<td>object (structured)
<td>Volume losses by plant part during processing
<td>
</tr>
<tr>
<td><code>plantPartTransformations</code>
<td>array&amp;lt;object&amp;gt;
<td>Specific plant part transformations during processing
<td>
</tr>
<tr>
<td><code>processingGeographicDataId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
<tr>
<td><code>qualityMetrics</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>volumeLoss</code>
<td>number (≥0)
<td>No description provided
<td>
</tr>
</tbody>
</table>

## MaterialProcessing
### Overview
The `MaterialProcessing` entity tracks all technical manipulations with input/output TRU references and species composition changes to support complete audit trails in the BOOST traceability system. This entity captures every processing operation that transforms, moves, or modifies TRUs throughout the supply chain, maintaining complete traceability and volume conservation validation.
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
<td>`processingId`
<td>string
<td>Yes
<td>Unique identifier for the processing operation (primary key)
<td>`PROC-001`, `PROC-FELL-KLA-042`
</tr>
<tr>
<td>`inputTraceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to input TRU being processed
<td>`TRU-TREE-001`, `TRU-LOG-CA-042`
</tr>
<tr>
<td>`outputTraceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to output TRU created (may be same as input)
<td>`TRU-LOG-001`, `TRU-PILE-CA-042`
</tr>
<tr>
<td>`processType`
<td>string
<td>Yes
<td>Type of processing operation (enum)
<td>`felling`, `delimbing`, `crosscutting`, `chipping`, `debarking`, `assortment`
</tr>
<tr>
<td>`processTimestamp`
<td>string (date-time)
<td>Yes
<td>When the processing operation occurred
<td>`2025-07-15T07:15:00Z`
</tr>
<tr>
<td>`processingGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where processing occurred
<td>`GEO-HARVEST-SITE-001`, `GEO-MILL-001`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Foreign key to operator who performed processing
<td>`OP-HARVESTER-001`, `OP-MILL-TECH-02`
</tr>
<tr>
<td>`inputComposition`
<td>string
<td>No
<td>Species composition before processing
<td>`Douglas Fir: 100%`, `Mixed: DF 60%, PP 40%`
</tr>
<tr>
<td>`outputComposition`
<td>string
<td>No
<td>Species composition after processing
<td>`Douglas Fir: 100%`, `Separated by species`
</tr>
<tr>
<td>`inputVolume`
<td>number
<td>Yes
<td>Input volume before processing (cubic meters)
<td>`25.5`, `85.25`, `150.0`
</tr>
<tr>
<td>`outputVolume`
<td>number
<td>Yes
<td>Output volume after processing (cubic meters)
<td>`24.2`, `80.75`, `140.5`
</tr>
<tr>
<td>`volumeLoss`
<td>number
<td>No
<td>Volume lost during processing (cubic meters)
<td>`1.3`, `4.5`, `9.5`
</tr>
<tr>
<td>`qualityMetrics`
<td>string
<td>No
<td>Quality measurements and assessments
<td>`Grade A: 80%, Grade B: 20%`, `Moisture: 12%`
</tr>
<tr>
<td>`equipmentUsed`
<td>string
<td>No
<td>Equipment used for processing
<td>`harvester_head`, `chainsaw`, `chipper`, `debarker`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/material-processing/PROC-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-21T15:45:00Z`
</tr>
</tbody>
</table>
### Processing Types
1. **felling**
     Tree cutting and initial processing
     Standing tree to log conversion
     Initial volume measurement
     Species identification and verification
     Primary processing operation
2. **delimbing**
     Branch removal from felled trees
     Clean stem preparation
     Volume refinement and measurement
     Quality assessment after delimbing
     Preparation for transport or further processing
3. **crosscutting**
     Log cutting to specified lengths
     Length optimization for market requirements
     Multiple output logs from single input
     Volume distribution and measurement
     Quality grade assignment
4. **chipping**
     Conversion to wood chips
     Volume reduction and format change
     Species mixing or separation
     Moisture content adjustment
     Final product preparation
5. **debarking**
     Bark removal from logs
     Clean wood preparation for processing
     Volume loss measurement
     Bark disposal or utilization tracking
     Quality improvement operation
6. **assortment**
     Sorting and classification by quality/species
     Grade assignment and segregation
     Market specification preparation
     Quality-based value optimization
     Inventory organization
### Key Features
1. **Complete Processing Chain Tracking**
     Input/output TRU relationship mapping
     Chronological processing sequence
     Volume conservation validation
     Quality transformation tracking
     Operator accountability
2. **Species Composition Management**
     Before/after species composition tracking
     Multi-species processing support
     Species separation and mixing operations
     Composition validation and verification
     Biodiversity impact assessment
3. **Volume Conservation Validation**
     Input volume measurement
     Output volume calculation
     Volume loss quantification and justification
     Processing efficiency metrics
     Mass balance verification
4. **Quality Transformation Tracking**
     Quality metrics before and after processing
     Grade assignment and modification
     Defect identification and impact
     Processing quality assurance
     Value optimization tracking
### Processing Efficiency Metrics
1. **Volume Recovery Rates**
     Standard recovery rates by processing type
     Equipment-specific efficiency tracking
     Operator performance metrics
     Quality impact on recovery rates
2. **Quality Transformation**
     Grade improvement through processing
     Defect removal effectiveness
     Value-added processing metrics
     Market specification achievement
3. **Species-Specific Processing**
     Species-appropriate processing methods
     Species-specific recovery rates
     Quality outcomes by species
     Processing optimization by species
### Validation Rules
1. **TRU Relationship Validation**
     inputTraceableUnitId must reference existing TRU
     outputTraceableUnitId must be created or reference existing TRU
     processTimestamp must be ≥ input TRU creation timestamp
     Output TRU creation must be ≥ processTimestamp
2. **Volume Conservation**
     outputVolume + volumeLoss should approximately equal inputVolume
     Volume loss must be reasonable for processing type
     Volume calculations must account for species composition changes
3. **Processing Logic**
     Processing type must be appropriate for input TRU type
     Equipment must be suitable for processing type
     Operator must be qualified for processing operation
     Location must support specified processing type
### Example Use Cases
1. **Tree Felling Operation**
     Input: Standing tree (estimated volume)
     Process: Felling with chainsaw
     Output: Felled tree/log with measured volume
     Volume loss: Sawdust and cutting waste
     Quality assessment: Initial grade assignment
2. **Log Crosscutting**
     Input: Long log (25.5 m³)
     Process: Crosscutting to market lengths
     Output: Multiple shorter logs (24.2 m³ total)
     Volume loss: Saw kerf and end trim (1.3 m³)
     Quality: Length optimization for grade recovery
3. **Multi-Species Pile Processing**
     Input: Mixed species pile
     Process: Species sorting and assortment
     Output: Separate species piles
     Composition change: Mixed to segregated
     Quality improvement through sorting
### Relationships
- MaterialProcessing consumes one input TraceableUnit
- MaterialProcessing produces one output TraceableUnit
- MaterialProcessing located at one GeographicData location
- MaterialProcessing performed by one Operator
- MaterialProcessing generates MeasurementRecord entries
- MaterialProcessing triggers LocationHistory events
- MaterialProcessing supports TRU split/merge operations
- MaterialProcessing enables processing chain audit trails
