<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: tracking_point/validation_schema.json and tracking_point_dictionary.md
     To modify this content, edit the source file and regenerate -->

TrackingPoint entity in BOOST data model

**[View Tracking Point in ERD Navigator](erd-navigator/index.html?focus=TrackingPoint)**

### Relationships ### {{.unnumbered}}

- **trackingPointId** → [[#tracking-point|Tracking Point]] - Unique identifier for the tracking point
- **geographicDataId** → [[#geographic-data|Geographic Data]]
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
<td>enum(TrackingPoint)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>equipmentUsed</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>establishedTimestamp</code>
<td>string (date-time)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>geographicDataId</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>pointType</code>
<td>enum(4 values)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>trackingPointId</code>
<td>string (pattern)
<td>Unique identifier for the tracking point
<td>✓
</tr>
<tr>
<td><code>operatorId</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## TrackingPoint
### Overview
The `TrackingPoint` entity implements the critical tracking points (harvest site, skid road, forest road, mill entrance) as defined in the BOOST continuous traceability system. These tracking points serve as infrastructure nodes where TRUs are identified, measured, and verified throughout the supply chain using technology-appropriate equipment and identification methods.
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
<td>Type of tracking point (enum)
<td>`harvest_site`, `skid_road`, `forest_road`, `mill_entrance`
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
1. **harvest_site**
     Initial capture point where TRUs are created
     multi-method identification at felling/delimbing
     Species identification and initial measurements
     GPS coordinate capture for harvest location
2. **skid_road** 
     Secondary aggregation and sorting point
     TRU consolidation from multiple harvest sites
     Quality grading and assortment classification
     Load preparation for transport
3. **forest_road**
     Transport verification and load documentation
     Final forest-based measurement and verification
     Transport method and vehicle assignment
     Departure timestamp and route planning
4. **mill_entrance**
     Final verification point before processing
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
