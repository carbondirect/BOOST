# Data Dictionary

## Organization

### Overview
The `Organization` entity manages companies and institutions with geographic data references and certification management capabilities as part of the BOOST traceability system enhancements. This entity serves as the foundational record for all organizational entities participating in the timber supply chain, including harvesters, processors, certifiers, and other stakeholders.

### Fields

| Field                       | Type             | Required | Description                                                                 | Examples                                    |
|----------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `organizationId`           | string           | Yes      | Unique identifier for the organization (primary key)                      | `ORG-001`, `ORG-FORESTCO-PACIFIC`         |
| `organizationName`         | string           | Yes      | Legal name of the organization                                            | `Pacific Forest Products LLC`, `Klamath Sustainable Forestry` |
| `organizationType`         | string           | Yes      | Type of organization (enum)                                               | `harvester`, `processor`, `certifier`, `transporter` |
| `primaryGeographicDataId`  | string (FK)      | No       | Foreign key to primary operational location                               | `GEO-MILL-PACIFIC-001`, `GEO-OFFICE-KLAMATH` |
| `operationalAreas`         | array<string>    | No       | List of geographic areas where organization operates                      | `["GEO-FOREST-AREA-01", "GEO-MILL-SITE-02"]` |
| `contactEmail`             | string (email)   | No       | Primary contact email address                                             | `operations@pacificforest.com`             |
| `contactPhone`             | string           | No       | Primary contact phone number                                              | `+1-555-123-4567`, `+1-800-FOREST-1`     |
| `certifications`           | array<string>    | No       | List of certification IDs held by organization                            | `["CERT-FSC-001", "CERT-SFI-002"]`       |
| `establishedDate`          | string (date)    | No       | Date organization was established                                         | `1995-03-15`, `2010-07-01`                |
| `taxId`                    | string           | No       | Tax identification number                                                 | `12-3456789`, `98-7654321`                |
| `website`                  | string (uri)     | No       | Organization website URL                                                  | `https://www.pacificforest.com`           |
| `@id`                      | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/organization/ORG-001` |
| `lastUpdated`              | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Organization Types

1. **harvester**
   - Forest harvesting and timber extraction operations
   - Responsible for initial TRU creation and identification
   - Manages harvest site operations and equipment
   - Provides raw material to processing facilities
   - Examples: Logging companies, forest management companies

2. **processor**
   - Manufacturing and processing operations
   - Transforms raw timber into finished products
   - Operates sawmills, paper mills, and other processing facilities
   - Manages quality control and product specifications
   - Examples: Sawmills, paper manufacturers, engineered wood producers

3. **certifier**
   - Third-party certification and validation services
   - Conducts audits and issues certifications
   - Validates sustainability claims and compliance
   - Provides independent verification services
   - Examples: FSC certifiers, SFI certification bodies

4. **transporter**
   - Transportation and logistics services
   - Manages supply chain movement and tracking
   - Maintains chain of custody during transport
   - Provides tracking point management
   - Examples: Trucking companies, rail transport, shipping companies

5. **supplier**
   - Supply chain intermediaries and distributors
   - Manages inventory and product distribution
   - Coordinates between producers and end users
   - Provides market access and logistics coordination
   - Examples: Timber brokers, wood product distributors

6. **manufacturer**
   - End-product manufacturing and assembly
   - Creates finished goods from processed timber
   - Manages final product quality and specifications
   - Provides consumer-ready products
   - Examples: Furniture manufacturers, construction companies

### Key Features

1. **Geographic Integration**
   - Primary location tracking with GeographicData references
   - Multiple operational area management
   - Location-based service area definition
   - Spatial analysis of organizational footprint
   - Regional operational compliance tracking

2. **Certification Management**
   - Multiple certification tracking and management
   - Certification expiry and renewal tracking
   - Audit trail for certification activities
   - Integration with claim validation processes
   - Certification scope and applicability management

3. **Multi-Location Operations**
   - Support for organizations with multiple facilities
   - Operational area geographic boundary definition
   - Location-specific capability and capacity tracking
   - Regional compliance and regulation management
   - Site-specific environmental impact assessment

4. **Supply Chain Integration**
   - Role-based organizational classification
   - Supply chain relationship management
   - Service capability and capacity tracking
   - Partner organization integration
   - Stakeholder communication and coordination

### Geographic Data Integration

1. **Primary Location**
   - Main operational headquarters or facility
   - Administrative and management location
   - Primary contact and communication center
   - Financial and legal registration address
   - Strategic planning and coordination hub

2. **Operational Areas**
   - Forest management areas for harvesters
   - Processing facility locations for manufacturers
   - Service territories for transporters
   - Market areas for suppliers
   - Geographic service boundaries

3. **Facility-Specific Data**
   - Processing capacity and capabilities by location
   - Equipment and infrastructure by facility
   - Environmental permits and compliance by site
   - Workforce and operational capacity by location
   - Location-specific certifications and approvals

### Certification Integration

1. **Certificate Management**
   - Current certification status tracking
   - Certification scope and applicability
   - Expiry date monitoring and renewal management
   - Multi-standard certification support
   - Certification body relationship management

2. **Compliance Tracking**
   - Regulatory compliance monitoring
   - Environmental permit management
   - Safety and quality standard compliance
   - Industry-specific requirement tracking
   - Audit and inspection history

3. **Claim Validation**
   - Authority to validate sustainability claims
   - Certification-based claim verification
   - Third-party validation services
   - Independent assessment capabilities
   - Conflict of interest management

### Validation Rules

1. **Identification Requirements**
   - organizationId must be unique across system
   - organizationName must be non-empty
   - organizationType must match business operations
   - Contact information must be valid and current

2. **Geographic Consistency**
   - primaryGeographicDataId must reference valid GeographicData
   - operationalAreas must reference valid geographic boundaries
   - Geographic areas must be logically consistent with organization type
   - Location data must align with legal and regulatory jurisdictions

3. **Certification Logic**
   - certifications must reference valid certification records
   - Certification types must be appropriate for organization type
   - Certification scope must align with operational areas
   - Certification expiry dates must be monitored and maintained

### Example Use Cases

1. **Integrated Forest Products Company**
   - organizationType: harvester, processor
   - Multiple operational areas including forest lands and mill sites
   - FSC and SFI certifications for both forest management and processing
   - Complex supply chain with internal transfer tracking
   - Multi-facility operations requiring coordination

2. **Independent Harvesting Contractor**
   - organizationType: harvester
   - Single primary location with mobile operations
   - Multiple operational areas across regional forest lands
   - SFI contractor certification
   - Service provider to multiple forest landowners

3. **Third-Party Certification Body**
   - organizationType: certifier
   - Office locations with regional service areas
   - Authority to issue and validate multiple certification types
   - Independent status and conflict of interest management
   - Audit and inspection service capabilities

### Relationships
- Organization operates at multiple GeographicData locations
- Organization holds multiple Certifications
- Organization employs multiple Operators
- Organization validates Claims through certification authority
- Organization manages TrackingPoints at operational locations
- Organization responsible for TraceableUnit creation and management
- Organization provides services throughout the supply chain