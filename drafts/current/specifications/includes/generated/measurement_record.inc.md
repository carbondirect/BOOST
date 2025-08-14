<!-- Auto-generated from measurement_record/validation_schema.json -->

Quality measurements and dimensional data

**[View Measurement Record in ERD Navigator](erd-navigator/index.html?focus=MeasurementRecord)**

### Relationships ### {{.unnumbered}}

- **traceableUnitId** → [[#traceable-unit|Traceable Unit]]
- **operatorId** → [[#operator|Operator]]
- **trackingPointId** → [[#tracking-point|Tracking Point]]

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
<td>enum(MeasurementRecord)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>measurementMethod</code>
<td>enum(4 values)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>measurementTimestamp</code>
<td>string (date-time)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>recordId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>traceableUnitId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>No description provided
<td>
</tr>
<tr>
<td><code>measuredDiameter</code>
<td>number (≥0)
<td>No description provided
<td>
</tr>
<tr>
<td><code>measuredLength</code>
<td>number (≥0)
<td>No description provided
<td>
</tr>
<tr>
<td><code>measuredVolume</code>
<td>number (≥0)
<td>No description provided
<td>
</tr>
<tr>
<td><code>measurementGeographicDataId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
<tr>
<td><code>moistureAccuracy</code>
<td>number (≥0)
<td>Estimated accuracy of moisture measurement (± percentage points)
<td>
</tr>
<tr>
<td><code>moistureContent</code>
<td>number (≥0, ≤100)
<td>Moisture content as percentage of weight contributed by water (0-100%)
<td>
</tr>
<tr>
<td><code>moistureMethod</code>
<td>enum(8 values)
<td>Method used to determine moisture content
<td>
</tr>
<tr>
<td><code>moistureStandard</code>
<td>enum(5 values)
<td>Standard procedure followed for moisture measurement
<td>
</tr>
<tr>
<td><code>operatorId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
<tr>
<td><code>speciesMeasurements</code>
<td>array&amp;lt;string&amp;gt;
<td>No description provided
<td>
</tr>
<tr>
<td><code>trackingPointId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
</tbody>
</table>

## MeasurementRecord
### Overview
The `MeasurementRecord` entity captures measurements at different tracking points with TRU references and species-specific data to support automated reconciliation between forest and mill measurements. This entity enables complete volume tracking, quality assessment, and measurement validation throughout the supply chain as required by the BOOST traceability system.
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
<td>`recordId`
<td>string
<td>Yes
<td>Unique identifier for the measurement record (primary key)
<td>`MR-001`, `MR-KLAMATH-LOG-042`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU being measured
<td>`TRU-LOG-001`, `TRU-PILE-CA-042`
</tr>
<tr>
<td>`measuredVolume`
<td>number
<td>No
<td>Volume measurement in cubic meters
<td>`12.5`, `85.75`, `245.2`
</tr>
<tr>
<td>`measuredLength`
<td>number
<td>No
<td>Length measurement in meters
<td>`8.2`, `12.5`, `16.0`
</tr>
<tr>
<td>`measuredDiameter`
<td>number
<td>No
<td>Diameter measurement in centimeters
<td>`45.2`, `78.5`, `32.1`
</tr>
<tr>
<td>`measurementMethod`
<td>string
<td>Yes
<td>Method used for measurement (enum)
<td>`harvester`, `mill`, `manual`, `optical`
</tr>
<tr>
<td>`measurementGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where measurement taken
<td>`GEO-HARVEST-001`, `GEO-MILL-ENTRANCE-01`
</tr>
<tr>
<td>`measurementTimestamp`
<td>string (date-time)
<td>Yes
<td>When the measurement was taken
<td>`2025-07-21T08:30:00Z`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Foreign key to operator who took measurement
<td>`OP-JOHN-DOE-001`, `OP-SCALE-TECH-02`
</tr>
<tr>
<td>`trackingPointId`
<td>string (FK)
<td>No
<td>Foreign key to tracking point where measured
<td>`TP-HARVEST-001`, `TP-MILL-ENTRANCE-01`
</tr>
<tr>
<td>`speciesMeasurements`
<td>array&lt;string&gt;
<td>No
<td>Individual species measurements for multi-species TRUs
<td>`["Pine: 45.2m3", "Fir: 28.8m3"]`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/measurement-record/MR-001`
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
### Measurement Methods
1. **harvester**
     Automated measurements from harvesting equipment
     High precision volume calculations
     Real-time data collection during harvest operations
     Integration with harvester computer systems
2. **mill**
     Scale and measurement systems at processing facilities
     Final volume and quality assessments
     Integration with mill processing equipment
     Quality grade determination
3. **manual** 
     Hand measurements using calipers, measuring tapes
     Field verification measurements
     Quality control spot checks
     Backup measurement method
4. **optical**
     Optical scanning and measurement systems
     Non-contact measurement techniques
     3D scanning for precise volume calculation
     Integration with biometric identification
### Key Features
1. **Multi-Point Measurement**
     Measurements at harvest, transport, and processing points
     Tracking point integration for location-based measurements
     Chronological measurement history
2. **Species-Specific Data**
     Individual species measurements within multi-species TRUs
     Species composition validation
     Species-specific volume tracking
3. **Method Validation**
     Multiple measurement methods for cross-validation
     Automated vs manual measurement comparison
     Quality assurance through redundant measurements
4. **Geographic Integration**
     Location-based measurement tracking
     Integration with tracking point infrastructure
     Spatial validation of measurement locations
### Validation Rules
1. **Measurement Consistency**
     All volume measurements must be ≥ 0
     Length and diameter measurements must be ≥ 0
     Measurement timestamp must be valid date-time
2. **TRU Integration**
     traceableUnitId must reference existing TRU
     Measurement timestamp must be ≥ TRU creation timestamp
     Sum of species measurements must equal total measurement
3. **Location Validation**
     measurementGeographicDataId must reference valid location
     Tracking point integration for location consistency
     Operator assignment validation
### Example Use Cases
1. **Harvest Measurements**
     Harvester-based automated volume calculation
     Real-time measurement during tree processing
     Species-specific measurements for multi-species stands
     GPS location integration
2. **Mill Entrance Verification**
     Scale-based volume verification
     Quality grade assessment measurements
     Final reconciliation with harvest measurements
     Processing facility integration
3. **Quality Control Measurements**
     Manual verification measurements
     Spot check validation of automated systems
     Defect assessment and grading
     Compliance verification measurements
### Relationships
- MeasurementRecord belongs to one TraceableUnit
- MeasurementRecord taken at one TrackingPoint
- MeasurementRecord located at one GeographicData point
- MeasurementRecord taken by one Operator
- MeasurementRecord supports DataReconciliation validation
- MeasurementRecord generated by MaterialProcessing operations
