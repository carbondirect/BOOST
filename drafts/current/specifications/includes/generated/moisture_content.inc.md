<!-- Auto-generated from moisture_content/validation_schema.json -->

Comprehensive validation rules and business logic for moisture content tracking across the BOOST data standard

**[View BOOST Moisture Content Validation Rules in ERD Navigator](erd-navigator/index.html?focus=MoistureContent)**

### Relationships ### {{.unnumbered}}

- **moistureContentId** → [[#moisture-content|Moisture Content]] - Unique identifier for moisture content record

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
<td><code>measurementMethod</code>
<td>any
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>moistureContent</code>
<td>any
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>moistureContentId</code>
<td>string (pattern)
<td>Unique identifier for moisture content record
<td>✓
</tr>
<tr>
<td><code>qualityAssurance</code>
<td>any
<td>No description provided
<td>
</tr>
</tbody>
</table>

## MoistureContent
### Overview
The `MoistureContent` entity tracks moisture measurements for biomass materials throughout the BOOST traceability system. Moisture content is a critical quality parameter affecting material processing, energy content, pricing, and regulatory compliance. This entity provides comprehensive moisture tracking with measurement validation, quality assurance protocols, and integration with processing operations and regulatory requirements.
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
<td>`moistureContentId`
<td>string
<td>Yes
<td>Unique identifier for the moisture content record (primary key)
<td>`MC-001`, `MC-TRU-LOG-CA-042-20240315`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU being measured for moisture
<td>`TRU-LOG-001`, `TRU-PILE-CA-042`
</tr>
<tr>
<td>`moisturePercentage`
<td>number
<td>Yes
<td>Moisture content as percentage of weight (0-100%)
<td>`12.5`, `18.2`, `45.7`
</tr>
<tr>
<td>`measurementMethod`
<td>string
<td>Yes
<td>Method used to determine moisture content (enum)
<td>`oven_dry`, `electrical_resistance`, `near_infrared`, `microwave`
</tr>
<tr>
<td>`measurementDate`
<td>string (date-time)
<td>Yes
<td>When the moisture measurement was taken
<td>`2024-03-15T10:30:00Z`, `2024-07-22T14:15:00Z`
</tr>
<tr>
<td>`measurementGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where measurement was taken
<td>`GEO-MILL-ENTRANCE-001`, `GEO-HARVEST-SITE-KLA-04`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Foreign key to operator who performed measurement
<td>`OP-MILL-TECH-001`, `OP-QUALITY-INSPECTOR-02`
</tr>
<tr>
<td>`standardReference`
<td>string
<td>No
<td>Standard procedure followed for measurement (enum)
<td>`ASTM_D4442`, `ISO_13061`, `CEN_EN_14774`, `local_standard`
</tr>
<tr>
<td>`sampleSize`
<td>integer
<td>No
<td>Number of measurement points taken
<td>`3`, `5`, `10`
</tr>
<tr>
<td>`measurementAccuracy`
<td>number
<td>No
<td>Estimated accuracy of measurement (± percentage points)
<td>`1.0`, `0.5`, `2.0`
</tr>
<tr>
<td>`temperatureDuringMeasurement`
<td>number
<td>No
<td>Temperature during measurement (Celsius)
<td>`20.5`, `15.2`, `28.0`
</tr>
<tr>
<td>`humidityDuringMeasurement`
<td>number
<td>No
<td>Relative humidity during measurement (%)
<td>`45.0`, `62.5`, `38.0`
</tr>
<tr>
<td>`calibrationDate`
<td>string (date-time)
<td>No
<td>Last calibration date of measurement equipment
<td>`2024-01-15T09:00:00Z`, `2024-06-01T08:30:00Z`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/moisture-content/MC-001`
</tr>
</tbody>
</table>
### Measurement Methods
1. **oven_dry**
    - Laboratory standard method using controlled heating
    - High accuracy (±0.5-1.0%) but time-intensive
    - Requires sample removal and laboratory facilities
    - ASTM D4442 and ISO 13061 standard compliance
2. **electrical_resistance**
    - Portable probe method using electrical conductivity
    - Moderate accuracy (±1-2%) with immediate results
    - Species-specific calibration required
    - Field-suitable for routine measurements
3. **near_infrared**
    - Non-destructive spectroscopic analysis
    - High accuracy (±0.5-1.5%) with rapid results
    - Expensive equipment but minimal sample preparation
    - Suitable for continuous monitoring applications
4. **microwave**
    - Rapid moisture determination using microwave energy
    - Moderate accuracy (±1-2%) with fast results
    - Requires sample preparation and specific equipment
    - Good for bulk material assessment
5. **gravimetric**
    - Weight-based calculation using before/after drying
    - High accuracy reference method
    - Time-intensive but reliable
    - Used for calibrating other methods
6. **capacitive**
    - Dielectric measurement of moisture content
    - Fast results with moderate accuracy
    - Portable equipment for field use
    - Species and density dependent
### Quality Grade Requirements
1. **Grade A (Premium)**
    - Maximum moisture: 18%
    - Structural and appearance applications
    - High-value products requiring stability
    - Enhanced durability and workability
2. **Grade B (Standard)**
    - Maximum moisture: 22%
    - General construction and manufacturing
    - Good balance of quality and cost
    - Suitable for most commercial applications
3. **Grade C (Utility)**
    - Maximum moisture: 30%
    - Lower-grade applications and processing
    - Cost-effective for specific uses
    - May require additional drying for some applications
4. **Structural**
    - Maximum moisture: 19%
    - Load-bearing construction applications
    - Engineered wood products
    - Building code compliance requirements
5. **Fuel Grade**
    - Maximum moisture: 50%
    - Biomass fuel applications
    - Energy content directly affected by moisture
    - Economic optimization for fuel efficiency
### Key Features
1. **Quality Assurance**
    - Standardized measurement protocols
    - Equipment calibration tracking
    - Environmental condition monitoring
    - Sample size and accuracy documentation
2. **Processing Integration**
    - Pre- and post-processing moisture tracking
    - Drying operation effectiveness monitoring
    - Volume adjustment calculations
    - Quality grade validation support
3. **Regulatory Compliance**
    - LCFS biomass moisture requirements
    - FSC chain of custody moisture tracking
    - SBP per-batch moisture validation
    - Export/import documentation support
4. **Business Intelligence**
    - Processing efficiency analysis
    - Quality control trend monitoring
    - Economic optimization through moisture management
    - Customer specification compliance verification
### Validation Rules
1. **Measurement Consistency**
    - moisturePercentage must be between 0 and 100%
    - measurementDate must be ≥ TRU creation timestamp
    - Measurement location must be valid if specified
    - Operator must be qualified for measurement method
2. **Processing Logic**
    - Drying operations must reduce moisture content
    - Storage may increase moisture within limits
    - Transportation should not significantly change moisture
    - Quality grade must be compatible with moisture level
3. **Quality Assurance Requirements**
    - Equipment calibration must be current
    - Standard procedures must be followed
    - Environmental conditions must be recorded
    - Sample size must be adequate for accuracy
### Example Use Cases
1. **Sawlog Processing Moisture Control**
    - Initial measurement at harvest: 35% moisture
    - Measurement method: electrical_resistance probe
    - Processing: Air drying to 18% for Grade A lumber
    - Final verification: oven_dry method for accuracy
    - Quality assurance: Multi-point sampling with ASTM D4442
2. **Biomass Fuel Delivery Verification**
    - Delivery requirement: Maximum 45% moisture content
    - Measurement method: near_infrared for rapid assessment
    - LCFS compliance: Documentation for carbon intensity calculation
    - Quality control: Continuous monitoring during unloading
    - Contract validation: Meeting customer specifications
3. **Export Lumber Certification**
    - Export requirement: 19% moisture maximum
    - Measurement method: oven_dry for regulatory compliance
    - Phytosanitary documentation: Moisture levels for pest control
    - Customer specifications: Meeting international standards
    - Quality certification: Third-party verification support
### Relationships
- MoistureContent measured on one TraceableUnit
- MoistureContent taken at one GeographicData location
- MoistureContent performed by one Operator
- MoistureContent supports quality grade determination in Material entities
- MoistureContent enables volume adjustments in MeasurementRecord entities
- MoistureContent required for LCFS compliance in EnergyCarbonData calculations
