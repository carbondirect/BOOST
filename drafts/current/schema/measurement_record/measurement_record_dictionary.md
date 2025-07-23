# Data Dictionary

## MeasurementRecord

### Overview
The `MeasurementRecord` entity captures measurements at different tracking points with TRU references and species-specific data to support automated reconciliation between forest and mill measurements. This entity enables complete volume tracking, quality assessment, and measurement validation throughout the supply chain as required by the BOOST traceability system.

### Fields

| Field                         | Type             | Required | Description                                                                 | Examples                                    |
|------------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `recordId`                   | string           | Yes      | Unique identifier for the measurement record (primary key)                | `MR-001`, `MR-KLAMATH-LOG-042`            |
| `traceableUnitId`            | string (FK)      | Yes      | Foreign key to TRU being measured                                        | `TRU-LOG-001`, `TRU-PILE-CA-042`          |
| `measuredVolume`             | number           | No       | Volume measurement in cubic meters                                        | `12.5`, `85.75`, `245.2`                  |
| `measuredLength`             | number           | No       | Length measurement in meters                                             | `8.2`, `12.5`, `16.0`                     |
| `measuredDiameter`           | number           | No       | Diameter measurement in centimeters                                      | `45.2`, `78.5`, `32.1`                    |
| `measurementMethod`          | string           | Yes      | Method used for measurement (enum)                                       | `harvester`, `mill`, `manual`, `optical`   |
| `measurementGeographicDataId`| string (FK)      | No       | Foreign key to location where measurement taken                          | `GEO-HARVEST-001`, `GEO-MILL-ENTRANCE-01` |
| `measurementTimestamp`       | string (date-time)| Yes     | When the measurement was taken                                           | `2025-07-21T08:30:00Z`                    |
| `operatorId`                 | string (FK)      | No       | Foreign key to operator who took measurement                             | `OP-JOHN-DOE-001`, `OP-SCALE-TECH-02`     |
| `trackingPointId`            | string (FK)      | No       | Foreign key to tracking point where measured                             | `TP-HARVEST-001`, `TP-MILL-ENTRANCE-01`   |
| `speciesMeasurements`        | array<string>    | No       | Individual species measurements for multi-species TRUs                   | `["Pine: 45.2m3", "Fir: 28.8m3"]`        |
| `@id`                        | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/measurement-record/MR-001` |
| `lastUpdated`                | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Measurement Methods

1. **harvester**
   - Automated measurements from harvesting equipment
   - High precision volume calculations
   - Real-time data collection during harvest operations
   - Integration with harvester computer systems

2. **mill**
   - Scale and measurement systems at processing facilities
   - Final volume and quality assessments
   - Integration with mill processing equipment
   - Quality grade determination

3. **manual** 
   - Hand measurements using calipers, measuring tapes
   - Field verification measurements
   - Quality control spot checks
   - Backup measurement method

4. **optical**
   - Optical scanning and measurement systems
   - Non-contact measurement techniques
   - 3D scanning for precise volume calculation
   - Integration with biometric identification

### Key Features

1. **Multi-Point Measurement**
   - Measurements at harvest, transport, and processing points
   - Tracking point integration for location-based measurements
   - Chronological measurement history

2. **Species-Specific Data**
   - Individual species measurements within multi-species TRUs
   - Species composition validation
   - Species-specific volume tracking

3. **Method Validation**
   - Multiple measurement methods for cross-validation
   - Automated vs manual measurement comparison
   - Quality assurance through redundant measurements

4. **Geographic Integration**
   - Location-based measurement tracking
   - Integration with tracking point infrastructure
   - Spatial validation of measurement locations

### Validation Rules

1. **Measurement Consistency**
   - All volume measurements must be ≥ 0
   - Length and diameter measurements must be ≥ 0
   - Measurement timestamp must be valid date-time

2. **TRU Integration**
   - traceableUnitId must reference existing TRU
   - Measurement timestamp must be ≥ TRU creation timestamp
   - Sum of species measurements must equal total measurement

3. **Location Validation**
   - measurementGeographicDataId must reference valid location
   - Tracking point integration for location consistency
   - Operator assignment validation

### Example Use Cases

1. **Harvest Measurements**
   - Harvester-based automated volume calculation
   - Real-time measurement during tree processing
   - Species-specific measurements for multi-species stands
   - GPS location integration

2. **Mill Entrance Verification**
   - Scale-based volume verification
   - Quality grade assessment measurements
   - Final reconciliation with harvest measurements
   - Processing facility integration

3. **Quality Control Measurements**
   - Manual verification measurements
   - Spot check validation of automated systems
   - Defect assessment and grading
   - Compliance verification measurements

### Relationships
- MeasurementRecord belongs to one TraceableUnit
- MeasurementRecord taken at one TrackingPoint
- MeasurementRecord located at one GeographicData point
- MeasurementRecord taken by one Operator
- MeasurementRecord supports DataReconciliation validation
- MeasurementRecord generated by MaterialProcessing operations