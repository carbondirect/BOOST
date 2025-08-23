# TrackingPoint

## TrackingPoint

### Overview
The `TrackingPoint` entity implements critical tracking points as specific geographic locations where custody changes, aggregation, or measurement occurs in biomass supply chains. BOOST supports flexible tracking configurations based on operational complexity, from minimum 2-point systems to extended 5+ point configurations addressing real-world operational variations including edge cases like silo storage and mobile processing.

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
<td>`trackingPointId`
<td>string
<td>Yes
<td>Unique identifier for the tracking point (primary key)
<td>`TP-001`, `TP-HARVEST-KLAMATH-04`
</tr>
<tr>
<td>`pointType`
<td>string
<td>Yes
<td>Type of tracking point (enum) - flexible based on operational needs
<td>`harvest_site`, `consolidation_point`, `mill_entrance`, `transfer_station`, `storage_facility`
</tr>
<tr>
<td>`coordinatePrecision`
<td>number
<td>No
<td>Required coordinate precision in meters (±accuracy)
<td>`5`, `10`, `25` (for ±5m, ±10m, ±25m accuracy)
</tr>
<tr>
<td>`configurationRole`
<td>string
<td>No
<td>Role in tracking configuration (enum)
<td>`required`, `optional`, `seasonal`, `conditional`
</tr>
<tr>
<td>`geographicDataId`
<td>string (FK)
<td>Yes
<td>Foreign key to location of tracking point
<td>`GEO-HARVEST-SITE-001`, `GEO-MILL-ENTRANCE-01`
</tr>
<tr>
<td>`equipmentUsed`
<td>string
<td>Yes
<td>Equipment deployed at this tracking point
<td>`RFID_reader, QR_scanner, biometric_system, GPS`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Foreign key to operator responsible for tracking point
<td>`OP-HARVEST-TECH-001`, `OP-MILL-GATE-02`
</tr>
<tr>
<td>`establishedTimestamp`
<td>string (date-time)
<td>Yes
<td>When the tracking point was established
<td>`2025-07-15T06:00:00Z`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/tracking-point/TP-001`
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
### Tracking Point Types

#### **Standard Configuration**

1. **harvest_site**
     - Specific coordinate where biomass is initially harvested (±10m precision typical)
     - Initial TRU creation with biometric identification
     - Species identification and volume measurements
     - GPS coordinate capture for regulatory compliance

2. **consolidation_point** 
     - Designated loading area with specific GPS coordinates (±25m precision typical)
     - TRU aggregation from multiple harvest sites before transport
     - Quality grading and load preparation
     - Replaces ambiguous "skid_road/forest_road" concept

3. **mill_entrance**
     - Final delivery point with precise coordinates (±5m precision typical)
     - Scale-based measurement and verification
     - TRU handoff from transport to processing operations

#### **Extended Configuration Options**

4. **transfer_station**
     - Intermediate custody transfer points between harvest and processing
     - Common in operations with multiple transport stages

5. **storage_facility**
     - Temporary biomass storage locations (silos, covered storage)
     - Addresses Colin's edge case question about aggregation

6. **quality_control_point**
     - Dedicated measurement and quality assessment locations
     - Optional for operations requiring detailed quality verification

7. **mobile_processing_unit**
     - Tracking points that move with mobile equipment
     - Coordinates updated as equipment relocates

### Implementation Guidance

#### **Configuration Selection**
- **2-Point Minimum**: harvest_site → mill_entrance (direct transport operations)
- **3-Point Standard**: harvest_site → consolidation_point → mill_entrance
- **4-5 Point Extended**: Including transfer stations, storage facilities based on operational complexity

#### **Coordinate Precision Requirements**
- **harvest_site**: ±10m (sufficient for regulatory compliance)
- **consolidation_point**: ±25m (loading area boundaries)
- **mill_entrance**: ±5m (precise scale location)
- **Other points**: ±10-50m based on operational requirements

#### **Seasonal and Mobile Considerations**
- **Seasonal access**: Use `configurationRole: "seasonal"` for roads/sites with limited access
- **Mobile equipment**: Update coordinates as equipment moves, maintain tracking continuity
- **Alternative routes**: Multiple consolidation_points for different seasonal/weather conditions

### Edge Cases and Alternative Configurations

#### **Colin's Edge Case Analysis - System Universality**

**Question**: "Do they exist in all biomass harvest / transport / processing systems? Are there any edge cases to address?"

**Answer**: BOOST's flexible tracking point system addresses operational variations through configurable point types:

#### **Silo and Aggregation Systems**
- **Scenario**: Biomass aggregated at silos before mill transport
- **Solution**: Use `storage_facility` tracking points for silo locations
- **Configuration**: harvest_site → storage_facility → mill_entrance
- **Data Capture**: Volume measurements at silo intake and outfeed
- **GPS Requirements**: ±10m precision for silo facility boundaries

#### **Multi-Stage Transport Operations**  
- **Scenario**: Transfer points between forest and mill (truck-to-rail, truck-to-truck)
- **Solution**: Use `transfer_station` tracking points for custody handoffs
- **Configuration**: harvest_site → consolidation_point → transfer_station → mill_entrance  
- **Data Validation**: Volume conservation across all transfer points
- **Operator Accountability**: Different operators at each transfer stage

#### **Mobile Processing Units**
- **Scenario**: Portable chippers, mobile sawmills moving between sites
- **Solution**: `mobile_processing_unit` points with dynamic coordinate updates
- **GPS Integration**: Continuous location tracking as equipment relocates
- **Processing Continuity**: TRU identity maintained through equipment moves
- **Seasonal Operations**: Equipment stored/moved based on access conditions

#### **Direct Mill Delivery Systems** 
- **Scenario**: Operations bypassing consolidation (small-scale, local mills)
- **Solution**: 2-point minimum configuration
- **Configuration**: harvest_site → mill_entrance (skip consolidation_point)
- **Regulatory Compliance**: Meets minimum traceability requirements
- **Scalability**: Can upgrade to 3+ points as operations expand

#### **Alternative Workflow Handling**
- **Non-standard systems**: Custom point types through extensible `pointType` enum
- **Legacy integration**: Map existing tracking points to BOOST point types
- **Regulatory adaptation**: Configure points to match specific compliance requirements (LCFS, RFS, EU RED-II)
- **Operational flexibility**: Mix-and-match point types based on business needs

#### **Universal Applicability Validation**
✅ **Small Operations**: 2-point minimum (harvest → mill)
✅ **Standard Operations**: 3-point configuration (harvest → consolidation → mill)  
✅ **Complex Operations**: 4-5+ points with storage, transfer stations
✅ **Mobile Operations**: Dynamic tracking points with coordinate updates
✅ **Seasonal Operations**: Conditional points based on access/weather
✅ **Multi-Modal Transport**: Transfer stations for transport method changes

**Conclusion**: BOOST's flexible tracking point system accommodates all biomass operational models through configurable point types, precision requirements, and seasonal/mobile considerations.
     Scale-based measurement and reconciliation
     Quality assessment and acceptance
     Processing facility intake documentation

### Equipment Categories

- **RFID_reader**: Radio frequency identification scanning equipment
- **QR_scanner**: Optical QR code reading systems
- **biometric_system**: Optical wood fingerprinting equipment
- **GPS**: Global positioning systems for location verification
- **scale_system**: Weighing and volume measurement equipment
- **optical_scanner**: Advanced optical measurement systems

### Key Features

1. **Critical Point Infrastructure**
     Implements BOOST traceability system's three critical points
     Equipment redundancy for media break prevention
     Location-based verification capabilities
     Operator accountability and management

2. **Multi-Technology Support**
     RFID tag reading capabilities
     QR code scanning systems
     Biometric pattern recognition
     GPS location verification
     Integration with multiple identification methods

3. **Process Integration**
     MeasurementRecord capture at tracking points
     BiometricIdentifier scanning locations
     LocationHistory event triggers
     Processing workflow integration

4. **Quality Assurance**
     Equipment calibration and maintenance tracking
     Operator training and certification requirements
     Performance monitoring and validation
     Backup identification methods

### Equipment Specifications

1. **RFID Systems**
     UHF RFID readers for tag detection
     Range: 1-10 meters depending on tag type
     Integration with handheld and fixed readers
     Weather-resistant installation options

2. **Optical Biometric Systems**
     High-resolution cameras for wood pattern capture
     Machine learning algorithms for pattern recognition
     No physical attachment requirements
     Multi-species pattern database support

3. **GPS Systems**
     Sub-meter accuracy for location verification
     WAAS/EGNOS correction support
     Integration with geographic data systems
     Offline capability for remote locations

### Validation Rules

1. **Location Consistency**
     geographicDataId must reference valid GeographicData
     pointType must be appropriate for geographic location
     Equipment must be suitable for environmental conditions

2. **Equipment Requirements**
     At least one identification method must be specified
     Equipment must be appropriate for pointType
     Operator must be certified for equipment operation

3. **Establishment Timeline**
     establishedTimestamp must be valid date-time
     Equipment installation must precede TRU processing
     Operator assignment must be current and valid

### Example Use Cases

1. **Harvest Site Setup**
     Establish biometric scanning equipment at harvest location
     GPS coordinate verification for precise location
     Operator training for equipment operation
     Integration with harvester computer systems

2. **Mill Entrance Configuration**
     Scale system integration with RFID readers
     Quality assessment station setup
     Final measurement and reconciliation equipment
     Processing facility intake procedures

3. **Mobile Tracking Points**
     Portable equipment for temporary harvest sites
     Quick setup and calibration procedures
     Weather-resistant equipment configurations
     Remote location connectivity solutions

### Relationships
- TrackingPoint located at one GeographicData location
- TrackingPoint operated by one or more Operators
- TrackingPoint captures MeasurementRecord entries
- TrackingPoint enables BiometricIdentifier scanning
- TrackingPoint managed by Organization
- TrackingPoint supports LocationHistory event recording