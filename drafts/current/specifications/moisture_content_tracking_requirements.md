# Moisture Content Tracking Requirements
## BOOST Data Standard Enhancement - Comprehensive Moisture Integration

### Executive Summary

This specification defines comprehensive moisture content tracking requirements for the BOOST data standard, integrating moisture measurement and monitoring throughout the biomass supply chain from harvest to delivery. Moisture content, defined as the percentage of weight contributed by water, is critical for quality assessment, regulatory compliance, and processing optimization.

### 1. Moisture Content Definition and Standards

#### 1.1 Definition
- **Moisture Content**: Percentage of total weight contributed by water content (0-100%)
- **Measurement Basis**: Weight basis moisture content calculation: `((wet_weight - dry_weight) / wet_weight) × 100`
- **Standard Conditions**: Measurements referenced to oven-dry basis per ASTM D4442 or equivalent

#### 1.2 Measurement Methods
- **Oven Dry Method**: ASTM D4442 standard (primary reference method)
- **Electrical Resistance**: Pin-type moisture meters for field measurements
- **Microwave**: Non-destructive measurement for large volumes
- **Near-Infrared**: Rapid analysis for batch processing
- **Gravimetric**: Laboratory precision method
- **Capacitive**: Non-invasive measurement through contactless sensors

### 2. Entity Integration Requirements

#### 2.1 TraceableUnit (TRU) Integration
**Required Fields:**
- `currentMoistureContent`: Current moisture percentage (0-100)
- `moistureContentTimestamp`: When moisture was last measured/updated
- `moistureContentSource`: Source of moisture data (measurement, calculation, estimate)

**Business Rules:**
- Moisture content must be updated during processing operations that affect moisture
- TRU moisture content serves as authoritative current value for quality assessments
- Moisture content source must be documented for regulatory compliance

#### 2.2 MeasurementRecord Enhancement
**Required Fields:**
- `moistureContent`: Measured moisture percentage
- `moistureMeasurementMethod`: Method used for measurement
- `moistureEquipmentUsed`: Specific equipment/model used

**Integration Rules:**
- All measurement records should include moisture content when feasible
- Moisture measurements update associated TRU current moisture content
- Cross-validation required for moisture changes >10% from previous measurements

#### 2.3 ProcessingHistory Moisture Tracking
**Required Fields:**
- `inputMoistureContent`: Moisture content before processing
- `outputMoistureContent`: Moisture content after processing
- `moistureChangeRatio`: Ratio of output to input moisture
- `moistureChangeReason`: Reason for moisture change (drying, wetting, natural_loss, processing)

**Processing Event Types Supporting Moisture:**
- **Drying**: Explicit moisture reduction operations
- **Transformation**: Physical processing that may affect moisture
- **Storage**: Natural moisture changes over time
- **Transport**: Moisture changes during transportation
- **Quality_Change**: Moisture-related quality modifications

#### 2.4 EnergyCarbonData Enhancement
**Moisture Data Type Support:**
- Enhanced `dataType` field supports "moisture" with comprehensive measurement context
- Related measurement record linkage for traceability
- Environmental conditions tracking (temperature, humidity)
- Quality assurance documentation

### 3. Quality Grade Integration

#### 3.1 Moisture Requirements by Grade
- **Grade A**: ≤18% moisture content (premium lumber)
- **Grade B**: ≤22% moisture content (standard lumber)
- **Grade C**: ≤30% moisture content (utility lumber)
- **Structural**: ≤19% moisture content (structural applications)
- **Fuel**: ≤50% moisture content (biomass fuel)
- **Pulpwood**: ≤60% moisture content (pulp production)

#### 3.2 Quality Grade Validation
- Automated validation of moisture content against quality grade requirements
- Quality downgrading triggers when moisture exceeds grade thresholds
- Documentation of quality grade changes due to moisture content

### 4. Regulatory Compliance Integration

#### 4.1 LCFS (Low Carbon Fuel Standard) Requirements
- **Mandatory Measurement**: At point of delivery to fuel production facility
- **Maximum Moisture**: 65% for biomass feedstock eligibility
- **Measurement Standards**: ASTM D4442 or near-infrared calibrated to ASTM standard
- **Documentation**: Complete chain of custody with moisture tracking

#### 4.2 FSC (Forest Stewardship Council) Integration
- **Chain of Custody**: Moisture content tracking throughout supply chain
- **Quality Assurance**: Documented measurement procedures and equipment calibration
- **Claim Inheritance**: Moisture-related quality claims passed through processing

#### 4.3 SBP (Sustainable Biomass Program) Requirements
- **Per-Batch Measurement**: Moisture content measured and documented per transaction batch
- **Validation Requirements**: Independent verification of moisture measurements
- **Risk Assessment**: Moisture content included in risk management protocols

### 5. Processing Operation Requirements

#### 5.1 Moisture Change Tracking
**Drying Operations:**
- Minimum moisture reduction: 2% to qualify as drying event
- Equipment documentation: Kiln specifications, drying conditions
- Duration tracking: Complete drying cycle documentation

**Storage Operations:**
- Natural moisture changes: ±5% acceptable over 30-day periods
- Environmental monitoring: Temperature and humidity conditions
- Storage method documentation: Covered, outdoor, ventilated

**Transportation:**
- Minimal moisture change expected: ±2% acceptable
- Route duration correlation with moisture change
- Container/covering specifications affecting moisture

#### 5.2 Split/Merge Operation Moisture Handling
- **Split Operations**: Output TRUs inherit input TRU moisture content unless processing changes moisture
- **Merge Operations**: Volume-weighted average moisture content calculation
- **Conservation Rules**: Total moisture mass conservation validation

### 6. Measurement Quality Assurance

#### 6.1 Equipment Calibration
- **Calibration Schedule**: Equipment calibrated per manufacturer specifications
- **Reference Standards**: Calibration against known moisture standards
- **Documentation**: Calibration certificates linked to measurement records

#### 6.2 Measurement Accuracy
- **Field Methods**: ±2% accuracy acceptable for operational decisions
- **Laboratory Methods**: ±0.5% accuracy required for regulatory compliance
- **Cross-Validation**: Secondary measurement required for >10% moisture changes

#### 6.3 Environmental Conditions
- **Temperature Recording**: Ambient temperature during measurement
- **Humidity Recording**: Relative humidity conditions
- **Correction Factors**: Environmental corrections applied when necessary

### 7. Data Validation and Business Rules

#### 7.1 Consistency Validation
- **Temporal Consistency**: Moisture changes validated against time elapsed and conditions
- **Processing Consistency**: Moisture changes consistent with processing operations
- **Volume Correlation**: Volume changes correlated with moisture changes for shrinkage

#### 7.2 Outlier Detection
- **Daily Change Limits**: Flag changes >10% per day for investigation
- **Investigation Threshold**: Investigate changes >15% per day
- **Manual Override**: Documented override process for validated outliers

#### 7.3 Data Completeness
- **Minimum Frequency**: Moisture measured every 7 days for active TRUs
- **Processing Points**: Moisture measured at all critical tracking points
- **Delivery Requirement**: Moisture content required for all delivery transactions

### 8. Integration with Existing Systems

#### 8.1 TransactionBatch Integration
- Existing `qualityMetrics.moistureContent` field maintained for compatibility
- Enhanced with measurement method and timestamp documentation
- Cross-reference to detailed measurement records

#### 8.2 Measurement Equipment Integration
- **Equipment Registry**: Catalog of approved moisture measurement equipment
- **Calibration Tracking**: Equipment calibration status and history
- **Method Validation**: Approved methods for different TRU types and conditions

### 9. Implementation Timeline

#### 9.1 Phase 1: Core Integration (Immediate)
- ✅ Enhanced MeasurementRecord entity with moisture fields
- ✅ Updated EnergyCarbonData for comprehensive moisture data
- ✅ ProcessingHistory moisture change tracking
- ✅ TraceableUnit current moisture status

#### 9.2 Phase 2: Validation and Business Rules (Next)
- ✅ Comprehensive validation schema with business rules
- Quality grade integration with automated validation
- Regulatory compliance validation algorithms

#### 9.3 Phase 3: Advanced Features (Future)
- Predictive moisture modeling based on environmental conditions
- Automated moisture content updates from IoT sensors
- Machine learning algorithms for moisture change prediction

### 10. Conclusion

The comprehensive moisture content integration provides end-to-end tracking from harvest through delivery, supporting quality assessment, processing optimization, and regulatory compliance. This enhancement maintains backward compatibility while significantly expanding moisture content capabilities throughout the BOOST data standard.