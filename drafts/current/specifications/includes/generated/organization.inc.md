<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: organization/validation_schema.json and organization_dictionary.md
     To modify this content, edit the source file and regenerate -->

Organization entity with geographic data references and certification management capabilities for Phase 2 BOOST traceability system enhancements

**[View Organization in ERD Navigator](erd-navigator/index.html?focus=Organization)**

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
<td>JSON-LD context for semantic web compatibility
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>Unique URI identifier for the organization
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>string
<td>JSON-LD type identifier
<td>✓
</tr>
<tr>
<td><code>organizationId</code>
<td>string (pattern)
<td>Unique identifier for the organization
<td>✓
</tr>
<tr>
<td><code>organizationName</code>
<td>string
<td>Legal name of the organization
<td>✓
</tr>
<tr>
<td><code>organizationType</code>
<td>enum(10 values)
<td>Type of organization
<td>✓
</tr>
<tr>
<td><code>airDistrictPermit</code>
<td>string
<td>Air quality management district permit identifier
<td>
</tr>
<tr>
<td><code>bioramContractId</code>
<td>string (pattern)
<td>BioRAM competitive procurement contract identifier
<td>
</tr>
<tr>
<td><code>bioramEligibilityStatus</code>
<td>enum(4 values)
<td>Current BioRAM program eligibility status
<td>
</tr>
<tr>
<td><code>bioramFacilityId</code>
<td>string (pattern)
<td>BioRAM facility identifier for program tracking
<td>
</tr>
<tr>
<td><code>bioramRegistrationId</code>
<td>string (pattern)
<td>CEC BioRAM registration identifier for biomass power facilities
<td>
</tr>
<tr>
<td><code>calFireJurisdiction</code>
<td>string
<td>CAL FIRE unit or jurisdiction for facility area
<td>
</tr>
<tr>
<td><code>californiaSRA</code>
<td>boolean
<td>Whether facility operates within California State Responsibility Area
<td>
</tr>
<tr>
<td><code>certifications</code>
<td>array&amp;lt;string&amp;gt;
<td>List of certification IDs held by organization
<td>
</tr>
<tr>
<td><code>contactEmail</code>
<td>string (email)
<td>Primary contact email address
<td>
</tr>
<tr>
<td><code>contactPhone</code>
<td>string (pattern)
<td>Primary contact phone number
<td>
</tr>
<tr>
<td><code>equipmentIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Harvester/machine tracking references
<td>
</tr>
<tr>
<td><code>establishedDate</code>
<td>string (date)
<td>Date organization was established
<td>
</tr>
<tr>
<td><code>facilityCapacity</code>
<td>object (structured)
<td>Facility production or handling capacity for LCFS reporting
<td>
</tr>
<tr>
<td><code>fireHazardZoneDesignation</code>
<td>enum(4 values)
<td>CAL FIRE fire hazard severity zone designation for facility location
<td>
</tr>
<tr>
<td><code>gridInterconnectionPoint</code>
<td>string
<td>Grid interconnection substation or transmission point
<td>
</tr>
<tr>
<td><code>harvestSites</code>
<td>array&amp;lt;string&amp;gt;
<td>Operational harvest locations managed
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of the most recent data update
<td>
</tr>
<tr>
<td><code>lcfsRegistrationId</code>
<td>string (pattern)
<td>CARB LCFS registration identifier for regulated entities
<td>
</tr>
<tr>
<td><code>operationalAreas</code>
<td>array&amp;lt;string&amp;gt;
<td>List of geographic areas where organization operates
<td>
</tr>
<tr>
<td><code>operationalStatus</code>
<td>enum(4 values)
<td>Current operational status of the organization
<td>
</tr>
<tr>
<td><code>operatorIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Personnel tracking references
<td>
</tr>
<tr>
<td><code>powerPurchaseAgreementId</code>
<td>string
<td>Power purchase agreement identifier with utility offtaker
<td>
</tr>
<tr>
<td><code>primaryGeographicDataId</code>
<td>string (pattern)
<td>Foreign key to primary operational location
<td>
</tr>
<tr>
<td><code>regulatedEntityType</code>
<td>enum(5 values)
<td>LCFS regulated entity classification
<td>
</tr>
<tr>
<td><code>taxId</code>
<td>string
<td>Tax identification number
<td>
</tr>
<tr>
<td><code>traceableUnitIds</code>
<td>array&amp;lt;string&amp;gt;
<td>TRUs managed by this organization
<td>
</tr>
<tr>
<td><code>utilityOfftaker</code>
<td>string
<td>Utility company purchasing power under BioRAM contract
<td>
</tr>
<tr>
<td><code>website</code>
<td>string (uri)
<td>Organization website URL
<td>
</tr>
</tbody>
</table>

## Organization
### Overview
The `Organization` entity manages companies and institutions with geographic data references and certification management capabilities as part of the BOOST traceability system enhancements. This entity serves as the foundational record for all organizational entities participating in the timber supply chain, including harvesters, processors, certifiers, and other stakeholders.
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
<td>`organizationId`
<td>string
<td>Yes
<td>Unique identifier for the organization (primary key)
<td>`ORG-001`, `ORG-FORESTCO-PACIFIC`
</tr>
<tr>
<td>`organizationName`
<td>string
<td>Yes
<td>Legal name of the organization
<td>`Pacific Forest Products LLC`, `Klamath Sustainable Forestry`
</tr>
<tr>
<td>`organizationType`
<td>string
<td>Yes
<td>Type of organization (enum)
<td>`harvester`, `processor`, `certifier`, `transporter`, `supplier`, `manufacturer`, `producer`, `importer`, `blender`, `distributor`
</tr>
<tr>
<td>`primaryGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to primary operational location
<td>`GEO-MILL-PACIFIC-001`, `GEO-OFFICE-KLAMATH`
</tr>
<tr>
<td>`operationalAreas`
<td>array&lt;string&gt;
<td>No
<td>List of geographic areas where organization operates
<td>`["GEO-FOREST-AREA-01", "GEO-MILL-SITE-02"]`
</tr>
<tr>
<td>`contactEmail`
<td>string (email)
<td>No
<td>Primary contact email address
<td>`operations@pacificforest.com`
</tr>
<tr>
<td>`contactPhone`
<td>string
<td>No
<td>Primary contact phone number
<td>`+1-555-123-4567`, `+1-800-FOREST-1`
</tr>
<tr>
<td>`certifications`
<td>array&lt;string&gt;
<td>No
<td>List of certification IDs held by organization
<td>`["CERT-FSC-001", "CERT-SFI-002"]`
</tr>
<tr>
<td>`establishedDate`
<td>string (date)
<td>No
<td>Date organization was established
<td>`1995-03-15`, `2010-07-01`
</tr>
<tr>
<td>`taxId`
<td>string
<td>No
<td>Tax identification number
<td>`12-3456789`, `98-7654321`
</tr>
<tr>
<td>`website`
<td>string (uri)
<td>No
<td>Organization website URL
<td>`https://www.pacificforest.com`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/organization/ORG-001`
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
### Organization Types
1. **harvester**
     Forest harvesting and timber extraction operations
     Responsible for initial TRU creation and identification
     Manages harvest site operations and equipment
     Provides raw material to processing facilities
     Examples: Logging companies, forest management companies
2. **processor**
     Manufacturing and processing operations
     Transforms raw timber into finished products
     Operates sawmills, paper mills, and other processing facilities
     Manages quality control and product specifications
     Examples: Sawmills, paper manufacturers, engineered wood producers
3. **certifier**
     Third-party certification and validation services
     Conducts audits and issues certifications
     Validates sustainability claims and compliance
     Provides independent verification services
     Examples: FSC certifiers, SFI certification bodies
4. **transporter**
     Transportation and logistics services
     Manages supply chain movement and tracking
     Maintains chain of custody during transport
     Provides tracking point management
     Examples: Trucking companies, rail transport, shipping companies
5. **supplier**
     Supply chain intermediaries and distributors
     Manages inventory and product distribution
     Coordinates between producers and end users
     Provides market access and logistics coordination
     Examples: Timber brokers, wood product distributors
6. **manufacturer**
     End-product manufacturing and assembly
     Creates finished goods from processed timber
     Manages final product quality and specifications
     Provides consumer-ready products
     Examples: Furniture manufacturers, construction companies
7. **producer**
     Primary production and manufacturing of renewable fuels or products
     Operates refineries and production facilities for biofuels
     Manages feedstock conversion and processing operations
     Subject to LCFS regulatory requirements and reporting
     Examples: Renewable diesel producers, biodiesel refineries, ethanol plants
8. **importer**
     Import operations for renewable fuels and products
     Manages international supply chain and customs operations
     Handles regulatory compliance for imported fuels
     Subject to LCFS import reporting requirements
     Examples: Fuel importers, biofuel trading companies
9. **blender**
     Fuel blending and distribution operations
     Mixes renewable fuels with conventional petroleum products
     Manages fuel quality and specification compliance
     Subject to LCFS blending and distribution requirements
     Examples: Fuel blending terminals, distribution facilities
10. **distributor**
     Distribution and retail operations for renewable fuels
     Manages fuel delivery and retail sales operations
     Handles end-consumer fuel distribution
     Subject to LCFS distribution reporting requirements
     Examples: Fuel distributors, retail gas stations, fleet operators
### Key Features
1. **Geographic Integration**
     Primary location tracking with GeographicData references
     Multiple operational area management
     Location-based service area definition
     Spatial analysis of organizational footprint
     Regional operational compliance tracking
2. **Certification Management**
     Multiple certification tracking and management
     Certification expiry and renewal tracking
     Audit trail for certification activities
     Integration with claim validation processes
     Certification scope and applicability management
3. **Multi-Location Operations**
     Support for organizations with multiple facilities
     Operational area geographic boundary definition
     Location-specific capability and capacity tracking
     Regional compliance and regulation management
     Site-specific environmental impact assessment
4. **Supply Chain Integration**
     Role-based organizational classification
     Supply chain relationship management
     Service capability and capacity tracking
     Partner organization integration
     Stakeholder communication and coordination
### Geographic Data Integration
1. **Primary Location**
     Main operational headquarters or facility
     Administrative and management location
     Primary contact and communication center
     Financial and legal registration address
     Strategic planning and coordination hub
2. **Operational Areas**
     Forest management areas for harvesters
     Processing facility locations for manufacturers
     Service territories for transporters
     Market areas for suppliers
     Geographic service boundaries
3. **Facility-Specific Data**
     Processing capacity and capabilities by location
     Equipment and infrastructure by facility
     Environmental permits and compliance by site
     Workforce and operational capacity by location
     Location-specific certifications and approvals
### Certification Integration
1. **Certificate Management**
     Current certification status tracking
     Certification scope and applicability
     Expiry date monitoring and renewal management
     Multi-standard certification support
     Certification body relationship management
2. **Compliance Tracking**
     Regulatory compliance monitoring
     Environmental permit management
     Safety and quality standard compliance
     Industry-specific requirement tracking
     Audit and inspection history
3. **Claim Validation**
     Authority to validate sustainability claims
     Certification-based claim verification
     Third-party validation services
     Independent assessment capabilities
     Conflict of interest management
### Validation Rules
1. **Identification Requirements**
     organizationId must be unique across system
     organizationName must be non-empty
     organizationType must match business operations
     Contact information must be valid and current
2. **Geographic Consistency**
     primaryGeographicDataId must reference valid GeographicData
     operationalAreas must reference valid geographic boundaries
     Geographic areas must be logically consistent with organization type
     Location data must align with legal and regulatory jurisdictions
3. **Certification Logic**
     certifications must reference valid certification records
     Certification types must be appropriate for organization type
     Certification scope must align with operational areas
     Certification expiry dates must be monitored and maintained
### Example Use Cases
1. **Integrated Forest Products Company**
     organizationType: harvester, processor
     Multiple operational areas including forest lands and mill sites
     FSC and SFI certifications for both forest management and processing
     Complex supply chain with internal transfer tracking
     Multi-facility operations requiring coordination
2. **Independent Harvesting Contractor**
     organizationType: harvester
     Single primary location with mobile operations
     Multiple operational areas across regional forest lands
     SFI contractor certification
     Service provider to multiple forest landowners
3. **Third-Party Certification Body**
     organizationType: certifier
     Office locations with regional service areas
     Authority to issue and validate multiple certification types
     Independent status and conflict of interest management
     Audit and inspection service capabilities
### Relationships
- Organization operates at multiple GeographicData locations
- Organization holds multiple Certifications
- Organization employs multiple Operators
- Organization validates Claims through certification authority
- Organization manages TrackingPoints at operational locations
- Organization responsible for TraceableUnit creation and management
- Organization provides services throughout the supply chain
