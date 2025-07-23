# Data Dictionary

## Operator

### Overview
The `Operator` entity represents personnel within the BOOST biomass chain of custody system, tracking individual workers who perform critical operations throughout the supply chain. This entity manages certification requirements, equipment authorizations, and operational responsibilities to ensure accountability, safety, and regulatory compliance across all biomass tracking and processing activities.

### Fields

| Field                      | Type             | Required | Description                                                                 | Examples                                    |
|----------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `operatorId`               | string           | Yes      | Unique identifier for the operator (primary key)                          | `OP-ANDERSON-HARVEST-001`, `OP-PACIFIC-MILL-QA-042` |
| `organizationId`           | string (FK)      | Yes      | Foreign key reference to employing organization                            | `ORG-KLAMATH-HARVEST-OPERATIONS-001`      |
| `operatorName`             | string           | Yes      | Full name of the operator                                                  | `John Anderson`, `Maria Rodriguez-Chen`    |
| `employeeId`               | string           | No       | Internal employee identification number                                    | `EMP-001234`, `H-5678`                     |
| `operatorType`             | string           | Yes      | Type/role of operator within the supply chain (enum)                      | `harvester_operator`, `quality_inspector`  |
| `certifications`           | array<string>    | No       | Array of certifications held by the operator                              | `["CDL_Class_A", "Chainsaw_Safety"]`      |
| `equipmentAuthorizations`  | array<string>    | No       | Equipment the operator is authorized to operate                            | `["HARVESTER-001", "MILL-SCALE-A"]`       |
| `contactInfo`              | string           | No       | Phone/email contact information                                            | `555-0123, john.anderson@klamathops.com`  |
| `isActive`                 | boolean          | Yes      | Current employment status - true if actively employed                     | `true`, `false`                           |
| `hireDate`                 | string (date)    | Yes      | Date when operator started employment                                      | `2018-04-15`                              |
| `skillsQualifications`     | array<string>    | No       | Relevant skills and qualifications                                         | `["10+ years experience", "Bilingual"]`   |
| `supervisorOperatorId`     | string (FK)      | No       | Foreign key reference to direct supervisor operator (optional)             | `OP-SUPERVISOR-HARVEST-001`               |
| `@id`                      | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                         | `https://github.com/carbondirect/BOOST/schemas/operator/OP-ANDERSON-HARVEST-001` |
| `lastUpdated`              | string (date-time)| Yes     | Timestamp of last record modification                                      | `2025-07-22T09:15:00Z`                    |

### Operator Types

1. **harvester_operator**
   - Operates harvesting equipment and machinery
   - Responsible for tree felling and initial processing
   - Creates initial TRU records and biometric captures
   - Manages harvest site operations and safety
   - Examples: Feller buncher operators, chainsaw operators

2. **transport_driver**
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

5. **processing_technician**
   - Operates specialized processing equipment
   - Manages technical processing operations
   - Documents processing steps and quality metrics
   - Maintains equipment calibration and performance
   - Examples: Delimbing technicians, sorting specialists

6. **equipment_maintenance**
   - Maintains and repairs operational equipment
   - Ensures equipment calibration and accuracy
   - Manages preventive maintenance schedules
   - Troubleshoots equipment malfunctions
   - Examples: Mechanic technicians, calibration specialists

7. **loading_operator**
   - Operates loading and material handling equipment
   - Manages TRU loading and unloading operations
   - Documents material transfer activities
   - Ensures safe and efficient material handling
   - Examples: Crane operators, loader operators

8. **scaling_specialist**
   - Operates weighing and measurement systems
   - Manages tracking point measurement activities
   - Documents volume and weight measurements
   - Maintains scale calibration and accuracy
   - Examples: Truck scale operators, volume measurement technicians

9. **environmental_monitor**
   - Monitors environmental compliance and conditions
   - Documents environmental impact assessments
   - Ensures regulatory compliance adherence
   - Manages environmental data collection
   - Examples: Air quality monitors, soil impact assessors

10. **safety_coordinator**
    - Oversees workplace safety and compliance
    - Manages safety training and certification programs
    - Conducts safety inspections and audits
    - Coordinates emergency response procedures
    - Examples: Safety officers, training coordinators

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