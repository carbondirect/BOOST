# Data Dictionary

## Operator

### Overview
The `Operator` entity manages individual workers with certification tracking and geographic assignment capabilities as part of Phase 2 Kaulen framework enhancements. This entity represents the individual people responsible for operating equipment, taking measurements, and performing activities throughout the timber supply chain with accountability and traceability.

### Fields

| Field                       | Type             | Required | Description                                                                 | Examples                                    |
|----------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `operatorId`               | string           | Yes      | Unique identifier for the operator (primary key)                          | `OP-001`, `OP-JOHN-SMITH-HARVESTER`       |
| `operatorName`             | string           | Yes      | Full name of the operator                                                  | `John Smith`, `Maria Rodriguez`            |
| `employeeId`               | string           | No       | Employee identification number                                             | `EMP-12345`, `PACIFIC-FOREST-001`         |
| `organizationId`           | string (FK)      | Yes      | Foreign key to employing organization                                      | `ORG-PACIFIC-FOREST-001`                  |
| `operatorRole`             | string           | Yes      | Primary role or job function (enum)                                       | `harvester`, `mill_operator`, `truck_driver` |
| `certifications`           | array<string>    | No       | List of operator certifications and licenses                               | `["CDL-A", "CERTIFIED-LOGGER"]`           |
| `equipmentQualifications`  | array<string>    | No       | Equipment the operator is qualified to use                                 | `["harvester_head", "log_loader"]`        |
| `primaryWorkLocationId`    | string (FK)      | No       | Foreign key to primary work location                                       | `GEO-MILL-PACIFIC-001`                    |
| `assignedTrackingPoints`   | array<string>    | No       | List of tracking points assigned to operator                               | `["TP-MILL-ENTRANCE-001"]`                |
| `contactPhone`             | string           | No       | Operator contact phone number                                              | `+1-555-123-4567`                         |
| `contactEmail`             | string (email)   | No       | Operator contact email address                                             | `j.smith@pacificforest.com`               |
| `hireDate`                 | string (date)    | No       | Date operator was hired                                                    | `2020-03-15`                              |
| `trainingRecords`          | array<string>    | No       | List of completed training programs                                        | `["SAFETY-TRAINING-2025"]`                |
| `activeStatus`             | boolean          | No       | Whether operator is currently active                                       | `true`, `false`                           |
| `@id`                      | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                         | `https://github.com/carbondirect/BOOST/schemas/operator/OP-001` |
| `lastUpdated`              | string (date-time)| No      | Timestamp of the most recent data update                                  | `2025-07-21T15:45:00Z`                    |

### Operator Roles

1. **harvester**
   - Operates harvesting equipment and machinery
   - Responsible for tree felling and initial processing
   - Creates initial TRU records and biometric captures
   - Manages harvest site operations and safety
   - Examples: Feller buncher operators, chainsaw operators

2. **truck_driver**
   - Responsible for timber transportation
   - Manages chain of custody during transport
   - Operates tracking point check-ins and check-outs
   - Maintains load documentation and manifests
   - Examples: Log truck drivers, chip truck operators

3. **mill_operator**
   - Operates processing equipment and machinery
   - Manages TRU processing and transformation
   - Responsible for quality control and grading
   - Operates measurement and verification equipment
   - Examples: Saw operators, debarker operators

4. **quality_inspector**
   - Conducts quality assessments and grading
   - Validates measurements and specifications
   - Performs audit and compliance inspections
   - Documents quality metrics and defects
   - Examples: Lumber graders, quality control technicians

5. **scale_operator**
   - Operates weighing and measurement systems
   - Manages tracking point measurement activities
   - Documents volume and weight measurements
   - Maintains scale calibration and accuracy
   - Examples: Truck scale operators, volume measurement technicians

6. **equipment_operator**
   - Operates specialized equipment and machinery
   - Maintains equipment performance and calibration
   - Manages equipment-based data collection
   - Ensures proper equipment operation and safety
   - Examples: Crane operators, loader operators

7. **supervisor**
   - Manages teams and operations
   - Oversees quality control and compliance
   - Responsible for training and certification management
   - Coordinates multi-operator activities
   - Examples: Harvest supervisors, mill shift supervisors

8. **technician**
   - Maintains and calibrates technical equipment
   - Supports technology-based identification and measurement
   - Troubleshoots system issues and malfunctions
   - Provides technical training and support
   - Examples: Biometric system technicians, GPS technicians

### Key Features

1. **Certification Management**
   - Professional certification tracking and validation
   - Equipment qualification documentation
   - Training record management and renewal tracking
   - Competency assessment and verification
   - Regulatory compliance monitoring

2. **Geographic Assignment**
   - Primary work location assignment
   - Mobile operator location tracking
   - Multi-site operator assignment capabilities
   - Tracking point responsibility assignment
   - Regional operational area access control

3. **Equipment Integration**
   - Equipment qualification and authorization
   - Equipment-specific training requirements
   - Operator-equipment pairing for accountability
   - Equipment access control and security
   - Performance tracking by equipment type

4. **Accountability and Traceability**
   - Individual operator identification in all operations
   - Activity logging and audit trail creation
   - Performance metrics and quality tracking
   - Incident and issue responsibility assignment
   - Chain of custody operator verification

### Certification Categories

1. **Professional Licenses**
   - Commercial Driver's License (CDL)
   - Certified Logger credentials
   - Professional engineer licenses
   - Safety training certifications
   - Equipment operator licenses

2. **Equipment Qualifications**
   - Harvester operation certification
   - Crane operator qualification
   - Scale system operation training
   - Biometric scanner certification
   - GPS system operation training

3. **Safety Certifications**
   - OSHA safety training
   - First aid and CPR certification
   - Hazmat handling certification
   - Confined space entry training
   - Fall protection certification

4. **Industry Certifications**
   - Lumber grading certification
   - Chain of custody training
   - Quality control certification
   - Environmental compliance training
   - Sustainable forestry practices

### Equipment Qualifications

1. **Harvesting Equipment**
   - harvester_head: Harvester head operation
   - feller_buncher: Feller buncher operation
   - delimber: Delimbing equipment operation
   - forwarder: Log forwarding equipment
   - skidder: Skidding equipment operation

2. **Transportation Equipment**
   - log_truck: Log truck operation
   - chip_truck: Chip truck operation
   - heavy_haul: Heavy haul equipment
   - crane: Crane operation certification
   - log_loader: Log loading equipment

3. **Processing Equipment**
   - sawmill: Sawmill equipment operation
   - debarker: Debarking equipment
   - chipper: Chipping equipment operation
   - planer: Planing equipment operation
   - sorter: Sorting equipment operation

4. **Measurement Equipment**
   - scale_system: Scale operation and calibration
   - optical_scanner: Optical measurement systems
   - biometric_scanner: Biometric identification equipment
   - GPS: GPS and location systems
   - moisture_meter: Moisture content measurement

### Validation Rules

1. **Identification Requirements**
   - operatorId must be unique across system
   - operatorName must be non-empty
   - employeeId must be unique within organization
   - organizationId must reference valid Organization

2. **Role and Qualification Consistency**
   - operatorRole must align with job responsibilities
   - certifications must be appropriate for operatorRole
   - equipmentQualifications must be relevant to work assignments
   - Training records must support certification claims

3. **Geographic and Assignment Logic**
   - primaryWorkLocationId must reference valid GeographicData
   - assignedTrackingPoints must be within operational area
   - Work location must be consistent with organization operations
   - Equipment access must align with location assignments

4. **Active Status and Compliance**
   - activeStatus must reflect current employment status
   - Certification expiry dates must be monitored
   - Training requirements must be current and valid
   - Contact information must be current and accessible

### Example Use Cases

1. **Mobile Harvesting Operator**
   - operatorRole: harvester
   - Multiple equipment qualifications for harvesting machinery
   - Mobile work assignments across forest locations
   - Safety and professional logging certifications
   - GPS and biometric scanner training

2. **Mill Scale Operator**
   - operatorRole: scale_operator
   - Fixed assignment to mill entrance tracking point
   - Scale system certification and calibration training
   - Quality inspector qualifications
   - Measurement accuracy and documentation responsibilities

3. **Multi-Role Supervisor**
   - operatorRole: supervisor
   - Oversight responsibilities for multiple operators
   - Broad equipment qualifications and certifications
   - Quality control and compliance authority
   - Training and certification management duties

### Relationships
- Operator employed by one Organization
- Operator assigned to primary GeographicData work location
- Operator responsible for multiple TrackingPoints
- Operator qualified to use specific equipment types
- Operator takes MeasurementRecord entries
- Operator performs MaterialProcessing operations
- Operator manages LocationHistory events
- Operator validates Claims and performs DataReconciliation