# EnergyCarbonData

## EnergyCarbonData

### Overview
The `EnergyCarbonData` entity manages energy and carbon intensity data for lifecycle assessments and regulatory compliance within the BOOST traceability system. This entity captures comprehensive carbon accounting information, energy content measurements, and environmental impact data required for Low Carbon Fuel Standard (LCFS) compliance, renewable fuel certification, and sustainability reporting. It integrates field measurements, laboratory analysis, and lifecycle modeling to provide complete energy and carbon profiles for materials throughout the supply chain.

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
<td>`energyCarbonDataId`
<td>string
<td>Yes
<td>Unique identifier for the energy/carbon data record (primary key)
<td>`ECD-001`, `ECD-MOISTURE-ANALYSIS-2024-001`
</tr>
<tr>
<td>`dataType`
<td>string
<td>Yes
<td>Type of energy/carbon data being recorded (enum)
<td>`moisture`, `carbon_intensity`, `energy_content`, `emissions`, `lifecycle_assessment`
</tr>
<tr>
<td>`value`
<td>number
<td>Yes
<td>Numeric value of the measurement or calculation
<td>`12.5`, `45.2`, `18.7`, `102.3`
</tr>
<tr>
<td>`unit`
<td>string
<td>Yes
<td>Unit of measurement for the value (enum)
<td>`percentage`, `kg_CO2e`, `MJ`, `gCO2e/MJ`, `MJ/kg`
</tr>
<tr>
<td>`source`
<td>string
<td>Yes
<td>Source or method of data acquisition (enum)
<td>`field_measurement`, `laboratory_analysis`, `default_values`, `calculated`
</tr>
<tr>
<td>`measurementMethod`
<td>string
<td>No
<td>Specific measurement or calculation method (enum)
<td>`oven_dry`, `CA-GREET3.0`, `GREET2023`, `near_infrared`, `LCA_Modeling`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>No
<td>Foreign key to associated traceable unit
<td>`TRU-LOG-001`, `TRU-BIOMASS-BATCH-456`
</tr>
<tr>
<td>`measurementRecordId`
<td>string (FK)
<td>No
<td>Foreign key to detailed measurement record
<td>`MR-MOISTURE-ANALYSIS-001`, `MR-CARBON-LAB-789`
</tr>
<tr>
<td>`measurementTimestamp`
<td>string (datetime)
<td>No
<td>Date and time when measurement was taken
<td>`2024-03-15T10:30:00Z`, `2024-07-22T14:45:00Z`
</tr>
<tr>
<td>`measurementGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where measurement was taken
<td>`GEO-LAB-FACILITY-001`, `GEO-FIELD-SITE-HARVEST`
</tr>
<tr>
<td>`temperatureConditions`
<td>number
<td>No
<td>Temperature during measurement (Celsius)
<td>`20.5`, `-2.3`, `35.8`
</tr>
<tr>
<td>`humidityConditions`
<td>number
<td>No
<td>Relative humidity during measurement (percentage)
<td>`45.2`, `78.5`, `23.1`
</tr>
<tr>
<td>`lcfsPathwayType`
<td>string
<td>No
<td>LCFS pathway tier classification (enum)
<td>`Lookup_Table`, `Tier_1`, `Tier_2`, `Not_LCFS`
</tr>
<tr>
<td>`energyEconomyRatio`
<td>number
<td>No
<td>Energy economy ratio for LCFS credit calculation (0.5-3.0)
<td>`1.0`, `2.5`, `0.8`, `1.75`
</tr>
<tr>
<td>`lifeCycleStage`
<td>string
<td>No
<td>Lifecycle stage for carbon intensity data (enum)
<td>`feedstock`, `production`, `transport`, `distribution`, `combustion`
</tr>
<tr>
<td>`regulatoryBenchmark`
<td>number
<td>No
<td>CARB regulatory benchmark for comparison (gCO2e/MJ)
<td>`90.27`, `88.45`, `82.15`, `95.12`
</tr>
<tr>
<td>`caGreetVersion`
<td>string
<td>No
<td>CA-GREET model version used for calculation
<td>`3.0`, `4.0`, `4.1`, `5.0`
</tr>
<tr>
<td>`qualityAssurance`
<td>string
<td>No
<td>Quality assurance and validation notes
<td>`Third-party laboratory verified`, `ISO 17025 certified`, `CARB approved methodology`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/energy-carbon-data/ECD-001`
</tr>
</tbody>
</table>

### Data Types and Applications

1. **moisture**
    - Moisture content percentage for biomass materials
    - Critical for energy content and carbon intensity calculations
    - Required for LCFS pathway qualification
    - Impacts processing efficiency and fuel quality

2. **carbon_intensity**
    - Lifecycle carbon intensity in gCO2e/MJ
    - Primary metric for LCFS compliance assessment
    - Used for regulatory credit calculations
    - Compared against CARB regulatory benchmarks

3. **energy_content**
    - Energy content in MJ/kg or MJ/gallon
    - Higher heating value (HHV) or lower heating value (LHV)
    - Essential for fuel quality specifications
    - Required for energy economy ratio calculations

4. **transport**
    - Transportation-related energy consumption and emissions
    - Fuel consumption for logistics operations
    - Distance-based emission factors
    - Modal transport efficiency analysis

5. **fuel_consumption**
    - Equipment and process fuel consumption data
    - Harvesting, processing, and handling energy use
    - Direct measurement or calculated consumption
    - Basis for lifecycle emission calculations

6. **emissions**
    - Direct greenhouse gas emissions measurements
    - Process-specific emission factors
    - Scope 1, 2, and 3 emission categories
    - Supporting data for carbon intensity calculations

7. **lifecycle_assessment**
    - Comprehensive LCA results and analysis
    - Cradle-to-grave or cradle-to-gate assessments
    - Multiple impact categories beyond carbon
    - Full system boundary analysis

### Measurement Methods and Standards

1. **Physical Measurement Methods**
    - **oven_dry**: Standard oven-drying method for moisture content
    - **electrical_resistance**: Electrical moisture meters
    - **microwave**: Microwave moisture analysis
    - **near_infrared**: NIR spectroscopy for rapid analysis
    - **gravimetric**: Weight-based measurement techniques

2. **Carbon Intensity Modeling**
    - **CA-GREET3.0**: California-modified GREET model version 3.0
    - **GREET2023**: Latest Argonne National Lab GREET model
    - **Direct_Measurement**: Field or facility-based measurements
    - **LCA_Modeling**: Comprehensive lifecycle assessment modeling

3. **Quality Assurance Standards**
    - ISO 17025 laboratory accreditation
    - ASTM standard test methods
    - CARB-approved methodologies
    - Third-party verification protocols

### LCFS Pathway Integration

1. **Lookup Table Pathways**
    - Pre-approved carbon intensity values
    - Simplified pathway requirements
    - Standard feedstock and production processes
    - Limited documentation requirements

2. **Tier 1 Pathways**
    - Site-specific carbon intensity calculations
    - Enhanced data requirements
    - Facility-specific operational data
    - Moderate verification requirements

3. **Tier 2 Pathways**
    - Comprehensive lifecycle assessment
    - Detailed process modeling
    - Extensive data collection and verification
    - Highest accuracy and regulatory scrutiny

4. **Non-LCFS Applications**
    - Carbon accounting for non-regulated markets
    - Voluntary sustainability reporting
    - Corporate carbon footprint analysis
    - Research and development applications

### Lifecycle Stage Analysis

1. **feedstock**
    - Raw material production and harvesting
    - Land use change considerations
    - Agricultural or forestry practices
    - Feedstock transportation to processing

2. **production**
    - Processing facility operations
    - Energy consumption for conversion
    - Process emissions and efficiency
    - Co-product allocation and credits

3. **transport**
    - Finished fuel transportation
    - Distribution network efficiency
    - Modal transport optimization
    - Regional distribution considerations

4. **distribution**
    - Retail distribution and storage
    - Terminal and station operations
    - Final delivery to end users
    - Infrastructure energy requirements

5. **combustion**
    - End-use combustion emissions
    - Vehicle or equipment efficiency
    - Criteria pollutant emissions
    - Direct carbon dioxide releases

6. **full_lifecycle**
    - Comprehensive cradle-to-grave analysis
    - All lifecycle stages included
    - System boundary completeness
    - Total environmental impact assessment

### Regulatory Compliance Integration

1. **CARB LCFS Compliance**
    - California Air Resources Board requirements
    - Quarterly reporting obligations
    - Credit generation calculations
    - Pathway certification maintenance

2. **EPA RFS Integration**
    - Renewable Fuel Standard compliance
    - D-code pathway qualification
    - RIN generation and tracking
    - Lifecycle threshold requirements

3. **International Standards**
    - ISO 14067 carbon footprint standards
    - RED II sustainability criteria
    - CORSIA aviation fuel requirements
    - National renewable fuel programs

### Energy Economy Ratio Applications

1. **LCFS Credit Calculations**
    - EER values between 0.5 and 3.0
    - Fuel type and application specific
    - Efficiency compared to petroleum baseline
    - Credit multiplier for advanced biofuels

2. **Technology Assessment**
    - Vehicle efficiency comparisons
    - Engine technology improvements
    - Fuel system optimization
    - Performance benchmarking

### Example Use Cases

1. **Biomass Moisture Content Analysis**
    - Data Type: moisture measurement for wood chips
    - Value: 35.2% moisture content (wet basis)
    - Method: Oven-dry analysis per ASTM D4442
    - Application: Energy content calculation for LCFS pathway
    - Quality Assurance: ISO 17025 certified laboratory

2. **Renewable Diesel Carbon Intensity**
    - Data Type: Tier 1 pathway carbon intensity
    - Value: 22.5 gCO2e/MJ lifecycle emissions
    - Method: CA-GREET 3.0 modeling with facility data
    - Application: LCFS credit generation calculation
    - Benchmark: 90.27 gCO2e/MJ regulatory standard

3. **Transportation Emission Factor**
    - Data Type: Transport stage emissions
    - Value: 5.8 gCO2e/MJ for 100-mile trucking
    - Method: Direct fuel consumption measurement
    - Application: Lifecycle assessment component
    - Integration: Combined with feedstock and production data

### Data Quality and Validation

1. **Measurement Accuracy**
    - Calibrated instrumentation requirements
    - Measurement uncertainty quantification
    - Traceability to national standards
    - Regular equipment maintenance and verification

2. **Data Verification**
    - Third-party validation protocols
    - Chain of custody for samples
    - Documentation requirements
    - Audit trail maintenance

3. **Regulatory Acceptance**
    - CARB methodology approval
    - EPA verification protocols
    - International standard compliance
    - Certification body recognition

### Validation Rules

1. **Data Requirements**
    - energyCarbonDataId must be unique across system
    - dataType must align with measurement method
    - value must be positive number appropriate for data type
    - unit must be compatible with data type and value

2. **Measurement Consistency**
    - measurementMethod must be appropriate for data type
    - measurementTimestamp must be within reasonable timeframe
    - Environmental conditions must be documented for sensitive measurements
    - Quality assurance must meet applicable standards

3. **LCFS Integration**
    - lcfsPathwayType must be valid for data application
    - energyEconomyRatio must be within allowable range (0.5-3.0)
    - regulatoryBenchmark must reference current CARB standards
    - caGreetVersion must be approved for regulatory use

4. **Traceability Integration**
    - traceableUnitId must reference valid TRU if provided
    - measurementRecordId must reference valid measurement record
    - Geographic location must be consistent with TRU origin
    - Lifecycle stage must align with TRU processing history

### Relationships
- EnergyCarbonData provides carbon profile for one TraceableUnit
- EnergyCarbonData based on one MeasurementRecord for detailed documentation
- EnergyCarbonData measured at one GeographicData location for spatial context
- EnergyCarbonData supports LCFSPathway calculations for regulatory compliance
- EnergyCarbonData enables Transaction carbon intensity reporting for commercial applications