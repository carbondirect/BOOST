## Tolerance Standards and Precision Guidelines ## {#tolerance-standards}

BOOST recognizes that real-world biomass supply chains cannot achieve perfect accuracy in volume/mass conservation, species composition, or measurement precision. This section establishes acceptable tolerance standards and precision requirements for BOOST implementations.

### **Volume and Mass Conservation Tolerances**

**California CARB Standards**:
- **Volume Tolerance**: ±0.5% for LCFS reporting calculations (as specified in CARB LCFS Regulation Section 95488.8)
- **Application**: Applies to total volume reconciliation between harvest and processing stages
- **Documentation Requirement**: Variances exceeding ±0.5% require documented justification and corrective action plans

**Processing-Specific Tolerances**:
- **Pelletizing Operations**: ±2.0% volume variance acceptable due to densification and moisture content changes during pellet formation
- **Chipping Operations**: ±1.5% volume variance acceptable due to material loss during mechanical processing
- **Drying Operations**: Mass variance up to 15% acceptable due to moisture content reduction (tracked separately through `MoistureContent` entity)

**Transportation Tolerances**:
- **Handling Loss**: Up to 0.5% volume loss acceptable during loading, transportation, and unloading operations
- **Scale Accuracy**: ±0.25% for truck scale measurements, ±0.5% for portable scale measurements
- **Documentation**: Losses exceeding acceptable tolerances must be documented with cause analysis

### **De Minimis Thresholds**

**Material Loss Categories**:
- **Sawdust and Debris**: Material fragments <2cm not requiring individual tracking
- **Incidental Loss**: Spillage, dust, and minor material loss during handling <1% of total volume
- **Quality Degradation**: Material downgraded due to moisture, contamination, or damage <5% of total volume per processing stage

**Tracking Exemptions**:
- Material losses below de minimis thresholds may be recorded as aggregate loss rather than requiring individual TRU tracking
- Total aggregate losses must not exceed 2% of initial harvest volume across entire supply chain
- Systematic losses exceeding de minimis thresholds indicate process control issues requiring corrective action

### **Numeric Precision Requirements**

**Carbon Intensity Values**:
- **Standard Precision**: 2 decimal places (e.g., 94.17 gCO2e/MJ)
- **Rationale**: Matches CARB LCFS reporting precision requirements
- **Application**: All `benchmarkCI`, `pathwayCI`, and calculated CI values

**Volume Measurements**:
- **Cubic Meter Values**: 3 decimal places (e.g., 125.847 m³)
- **Rationale**: Maintains precision for volume conservation calculations across aggregation operations
- **Application**: `TraceableUnit.totalVolumeM3`, `Transaction.quantityM3`, `MaterialProcessing.outputQuantity`

**Percentage Compositions**:
- **Species Composition**: 1 decimal place (e.g., 78.5%)
- **Moisture Content**: 1 decimal place (e.g., 15.2%)
- **Quality Grade Distribution**: Whole percentages (e.g., 85%)
- **Rationale**: Balances practical measurement accuracy with data precision needs

**Geographic Coordinates**:
- **Latitude/Longitude**: 6 decimal places (~0.1 meter precision)
- **Application**: All `GeographicData` location fields
- **Rationale**: Provides sub-meter accuracy for harvest site and critical tracking point location

### **Measurement Accuracy Standards**

**Field Measurement Equipment**:
- **Diameter Measurements**: ±0.5 cm accuracy for individual log measurements
- **Length Measurements**: ±5 cm accuracy for log length measurements
- **Volume Calculations**: Combine diameter and length measurements using standard forestry volume equations

**Scale and Weighing Systems**:
- **Truck Scales**: Class III scales with ±0.25% accuracy certification
- **Portable Scales**: Class II scales with ±0.5% accuracy certification  
- **Calibration**: Annual calibration required, quarterly verification recommended

**Moisture Content Measurement**:
- **Oven-Dry Method**: ±1.0% accuracy (reference standard)
- **Electronic Meters**: ±2.0% accuracy with species-specific calibration
- **Sampling Requirements**: Minimum 3 samples per TRU, average used for reporting

### **Error Rate Acceptability Criteria**

**Volume Conservation Validation**:
- **Acceptable Range**: 98.0% - 102.0% volume conservation across supply chain stages
- **Warning Threshold**: 97.0% - 103.0% requires investigation and documentation
- **Failure Threshold**: <97.0% or >103.0% requires corrective action and potential TRU revalidation

**Species Composition Accuracy**:
- **Primary Species**: ±5% accuracy for species comprising >20% of TRU composition
- **Minor Species**: ±10% accuracy for species comprising 5-20% of TRU composition
- **Trace Species**: ±15% accuracy for species comprising <5% of TRU composition

**Temporal Reporting Tolerances**:
- **Timestamp Accuracy**: ±15 minutes for operational activities (harvest, processing, transport)
- **Date Accuracy**: Same calendar day for all supply chain stage transitions
- **Reporting Periods**: Monthly aggregation acceptable for regulatory compliance reporting

### **Quality Assurance Requirements**

**Data Validation Rules**:
- Volume conservation validation must pass for all TRU transformations
- Species composition percentages must sum to 100.0% ±0.1%
- Moisture content values must be within realistic ranges (5.0% - 60.0% for wood biomass)
- Geographic coordinates must validate against known harvest and processing locations

**Audit Trail Requirements**:
- All tolerance-exceeding variances must include documented cause analysis
- Measurement equipment calibration records must be maintained and available for audit
- Operator training records must demonstrate competency in measurement procedures
- Corrective actions taken for tolerance violations must be documented with effectiveness verification

This tolerance framework ensures that BOOST implementations maintain practical operability while preserving the data integrity required for regulatory compliance and sustainability verification across diverse biomass supply chain operations.