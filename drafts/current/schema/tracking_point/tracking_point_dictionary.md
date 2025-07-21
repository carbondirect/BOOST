# Data Dictionary

## TrackingPoint

### Overview
The `TrackingPoint` entity implements the three critical tracking points (harvest site, skid road, forest road, mill entrance) as defined in the Kaulen framework for media-interruption-free traceability. These tracking points serve as infrastructure nodes where TRUs are identified, measured, and verified throughout the supply chain using various equipment and identification technologies.

### Fields

| Field                    | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `trackingPointId`       | string           | Yes      | Unique identifier for the tracking point (primary key)                   | `TP-001`, `TP-HARVEST-KLAMATH-04`         |
| `pointType`             | string           | Yes      | Type of tracking point (enum)                                            | `harvest_site`, `skid_road`, `forest_road`, `mill_entrance` |
| `geographicDataId`      | string (FK)      | Yes      | Foreign key to location of tracking point                                | `GEO-HARVEST-SITE-001`, `GEO-MILL-ENTRANCE-01` |
| `equipmentUsed`         | string           | Yes      | Equipment deployed at this tracking point                                | `RFID_reader, QR_scanner, biometric_system, GPS` |
| `operatorId`            | string (FK)      | No       | Foreign key to operator responsible for tracking point                   | `OP-HARVEST-TECH-001`, `OP-MILL-GATE-02`  |
| `establishedTimestamp`  | string (date-time)| Yes     | When the tracking point was established                                  | `2025-07-15T06:00:00Z`                    |
| `@id`                   | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                       | `https://github.com/carbondirect/BOOST/schemas/tracking-point/TP-001` |
| `lastUpdated`           | string (date-time)| No      | Timestamp of the most recent data update                                | `2025-07-21T15:45:00Z`                    |

### Tracking Point Types

1. **harvest_site**
   - Initial capture point where TRUs are created
   - Biometric identification at felling/delimbing
   - Species identification and initial measurements
   - GPS coordinate capture for harvest location

2. **skid_road** 
   - Secondary aggregation and sorting point
   - TRU consolidation from multiple harvest sites
   - Quality grading and assortment classification
   - Load preparation for transport

3. **forest_road**
   - Transport verification and load documentation
   - Final forest-based measurement and verification
   - Transport method and vehicle assignment
   - Departure timestamp and route planning

4. **mill_entrance**
   - Final verification point before processing
   - Scale-based measurement and reconciliation
   - Quality assessment and acceptance
   - Processing facility intake documentation

### Equipment Categories

- **RFID_reader**: Radio frequency identification scanning equipment
- **QR_scanner**: Optical QR code reading systems
- **biometric_system**: Optical wood fingerprinting equipment
- **GPS**: Global positioning systems for location verification
- **scale_system**: Weighing and volume measurement equipment
- **optical_scanner**: Advanced optical measurement systems

### Key Features

1. **Critical Point Infrastructure**
   - Implements Kaulen framework's three critical points
   - Equipment redundancy for media break prevention
   - Location-based verification capabilities
   - Operator accountability and management

2. **Multi-Technology Support**
   - RFID tag reading capabilities
   - QR code scanning systems
   - Biometric pattern recognition
   - GPS location verification
   - Integration with multiple identification methods

3. **Process Integration**
   - MeasurementRecord capture at tracking points
   - BiometricIdentifier scanning locations
   - LocationHistory event triggers
   - Processing workflow integration

4. **Quality Assurance**
   - Equipment calibration and maintenance tracking
   - Operator training and certification requirements
   - Performance monitoring and validation
   - Backup identification methods

### Equipment Specifications

1. **RFID Systems**
   - UHF RFID readers for tag detection
   - Range: 1-10 meters depending on tag type
   - Integration with handheld and fixed readers
   - Weather-resistant installation options

2. **Optical Biometric Systems**
   - High-resolution cameras for wood pattern capture
   - Machine learning algorithms for pattern recognition
   - No physical attachment requirements
   - Multi-species pattern database support

3. **GPS Systems**
   - Sub-meter accuracy for location verification
   - WAAS/EGNOS correction support
   - Integration with geographic data systems
   - Offline capability for remote locations

### Validation Rules

1. **Location Consistency**
   - geographicDataId must reference valid GeographicData
   - pointType must be appropriate for geographic location
   - Equipment must be suitable for environmental conditions

2. **Equipment Requirements**
   - At least one identification method must be specified
   - Equipment must be appropriate for pointType
   - Operator must be certified for equipment operation

3. **Establishment Timeline**
   - establishedTimestamp must be valid date-time
   - Equipment installation must precede TRU processing
   - Operator assignment must be current and valid

### Example Use Cases

1. **Harvest Site Setup**
   - Establish biometric scanning equipment at harvest location
   - GPS coordinate verification for precise location
   - Operator training for equipment operation
   - Integration with harvester computer systems

2. **Mill Entrance Configuration**
   - Scale system integration with RFID readers
   - Quality assessment station setup
   - Final measurement and reconciliation equipment
   - Processing facility intake procedures

3. **Mobile Tracking Points**
   - Portable equipment for temporary harvest sites
   - Quick setup and calibration procedures
   - Weather-resistant equipment configurations
   - Remote location connectivity solutions

### Relationships
- TrackingPoint located at one GeographicData location
- TrackingPoint operated by one or more Operators
- TrackingPoint captures MeasurementRecord entries
- TrackingPoint enables BiometricIdentifier scanning
- TrackingPoint managed by Organization
- TrackingPoint supports LocationHistory event recording