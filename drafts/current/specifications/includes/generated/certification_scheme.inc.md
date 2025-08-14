<!-- Auto-generated from certification_scheme/validation_schema.json -->

CertificationScheme entity defining certification standards and requirements with geographic applicability for Phase 2 BOOST traceability system enhancements

**[View CertificationScheme in ERD Navigator](erd-navigator/index.html?focus=CertificationScheme)**

### Relationships ### {{.unnumbered}}

- **certificationSchemeId** → [[#certification-scheme|Certification Scheme]] - Unique identifier for the certification scheme

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
<td>Unique URI identifier for the certification scheme
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>string
<td>JSON-LD type identifier
<td>✓
</tr>
<tr>
<td><code>certificationSchemeId</code>
<td>string (pattern)
<td>Unique identifier for the certification scheme
<td>✓
</tr>
<tr>
<td><code>issuingOrganizationId</code>
<td>string (pattern)
<td>Foreign key to organization that issues this scheme
<td>✓
</tr>
<tr>
<td><code>schemeName</code>
<td>string
<td>Official name of the certification scheme
<td>✓
</tr>
<tr>
<td><code>schemeType</code>
<td>enum(6 values)
<td>Type of certification scheme
<td>✓
</tr>
<tr>
<td><code>applicableGeographicAreas</code>
<td>array&amp;lt;string&amp;gt;
<td>Geographic areas where this scheme is applicable
<td>
</tr>
<tr>
<td><code>auditRequirements</code>
<td>string
<td>Audit and verification requirements
<td>
</tr>
<tr>
<td><code>chainOfCustodyRequirements</code>
<td>string
<td>Chain of custody tracking and documentation requirements
<td>
</tr>
<tr>
<td><code>claimTypes</code>
<td>array&amp;lt;string&amp;gt;
<td>Types of claims supported by this scheme
<td>
</tr>
<tr>
<td><code>documentationRequirements</code>
<td>array&amp;lt;string&amp;gt;
<td>Required documentation and record-keeping
<td>
</tr>
<tr>
<td><code>eligibleMaterialTypes</code>
<td>array&amp;lt;string&amp;gt;
<td>Material types eligible for this certification scheme
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of the most recent data update
<td>
</tr>
<tr>
<td><code>schemeDescription</code>
<td>string
<td>Detailed description of the certification scheme
<td>
</tr>
<tr>
<td><code>schemeStandard</code>
<td>string
<td>Standard or version identifier
<td>
</tr>
<tr>
<td><code>validityPeriod</code>
<td>string
<td>Typical validity period for certifications under this scheme
<td>
</tr>
<tr>
<td><code>website</code>
<td>string (uri)
<td>Official website for the certification scheme
<td>
</tr>
</tbody>
</table>

## CertificationScheme
### Overview
The `CertificationScheme` entity defines certification standards and requirements with geographic applicability as part of Phase 2 BOOST traceability system enhancements. This entity provides the foundational definitions for sustainability certifications, their requirements, and applicable contexts for use throughout the timber supply chain.
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
<td>`certificationSchemeId`
<td>string
<td>Yes
<td>Unique identifier for the certification scheme (primary key)
<td>`CERT-SCHEME-FSC-001`, `CERT-SCHEME-SFI-COC`
</tr>
<tr>
<td>`schemeName`
<td>string
<td>Yes
<td>Official name of the certification scheme
<td>`FSC Chain of Custody`, `SFI Chain of Custody`
</tr>
<tr>
<td>`schemeType`
<td>string
<td>Yes
<td>Type of certification scheme (enum)
<td>`forest_management`, `chain_of_custody`, `biomass_sustainability`
</tr>
<tr>
<td>`schemeStandard`
<td>string
<td>No
<td>Standard or version identifier
<td>`FSC-STD-40-004 V3-1`, `SFI-2015-2019 COC`
</tr>
<tr>
<td>`issuingOrganizationId`
<td>string (FK)
<td>Yes
<td>Foreign key to organization that issues this scheme
<td>`ORG-FSC-INTERNATIONAL`, `ORG-SFI-INC`
</tr>
<tr>
<td>`schemeDescription`
<td>string
<td>No
<td>Detailed description of the certification scheme
<td>`Ensures responsible forest management`
</tr>
<tr>
<td>`applicableGeographicAreas`
<td>array&lt;string&gt;
<td>No
<td>Geographic areas where this scheme is applicable
<td>`["GEO-REGION-NORTH-AMERICA"]`
</tr>
<tr>
<td>`eligibleMaterialTypes`
<td>array&lt;string&gt;
<td>No
<td>Material types eligible for this certification scheme
<td>`["softwood", "hardwood", "mixed"]`
</tr>
<tr>
<td>`claimTypes`
<td>array&lt;string&gt;
<td>No
<td>Types of claims supported by this scheme
<td>`["FSC Mix", "FSC 100%", "FSC Recycled"]`
</tr>
<tr>
<td>`auditRequirements`
<td>string
<td>No
<td>Audit and verification requirements
<td>`Annual surveillance audits`
</tr>
<tr>
<td>`chainOfCustodyRequirements`
<td>string
<td>No
<td>Chain of custody tracking requirements
<td>`Physical or percentage-based system`
</tr>
<tr>
<td>`documentationRequirements`
<td>array&lt;string&gt;
<td>No
<td>Required documentation and record-keeping
<td>`["purchase_records", "sales_invoices"]`
</tr>
<tr>
<td>`validityPeriod`
<td>string
<td>No
<td>Typical validity period for certifications
<td>`3 years`, `5 years`
</tr>
<tr>
<td>`website`
<td>string (uri)
<td>No
<td>Official website for the certification scheme
<td>`https://fsc.org/`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/certification-scheme/CERT-SCHEME-FSC-001`
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
### Scheme Types
1. **forest_management**
     Certifies responsible forest management practices
     Covers forest planning, biodiversity conservation, and social impacts
     Examples: FSC Forest Management, SFI Forest Management
     Applies to forest owners and managers
     Long-term forest stewardship focus
2. **chain_of_custody**
     Tracks certified material through supply chain
     Ensures segregation and proper mixing calculations
     Examples: FSC Chain of Custody, SFI Chain of Custody
     Applies to processors, manufacturers, and traders
     Material flow and claim verification
3. **controlled_wood**
     Ensures wood avoids controversial sources
     Risk assessment and mitigation requirements
     Examples: FSC Controlled Wood, SFI Fiber Sourcing
     Due diligence and supply chain verification
     Minimum acceptable standards
4. **biomass_sustainability**
     Verifies sustainable biomass production and sourcing
     Greenhouse gas emission reductions and land use criteria
     Examples: SBP (Sustainable Biomass Partnership)
     Regional risk assessments and supply base evaluations
     Energy and environmental benefits focus
5. **carbon_offset**
     Quantifies and verifies carbon sequestration and emission reductions
     Additionality, permanence, and measurement requirements
     Examples: Verified Carbon Standard (VCS), Climate Action Reserve
     Forest carbon projects and methodologies
     Third-party verification and monitoring
6. **environmental_management**
     Comprehensive environmental management systems
     ISO 14001 and other environmental standards
     Continuous improvement and compliance frameworks
     Environmental impact assessment and mitigation
     Stakeholder engagement and reporting
### Key Features
1. **Geographic Applicability**
     Regional and national scheme variations
     Jurisdiction-specific requirements and adaptations
     Local stakeholder consultation requirements
     National forest legislation compliance
     Cultural and social context integration
2. **Material Type Specificity**
     Scheme requirements vary by material type
     Species-specific requirements and considerations
     Product category eligibility and restrictions
     Processing method compatibility
     End-use application suitability
3. **Claim Management**
     Supported claim types and calculation methods
     Percentage thresholds and mixing allowances
     Label use requirements and restrictions
     Marketing claim validation requirements
     Consumer communication standards
4. **Verification Requirements**
     Audit frequency and scope requirements
     Certification body accreditation standards
     Competency requirements for auditors
     Stakeholder consultation processes
     Complaint and dispute resolution procedures
### Chain of Custody Systems
1. **Physical Separation**
     Complete segregation of certified and non-certified materials
     Separate storage, processing, and handling systems
     No mixing of certified and non-certified materials
     Highest integrity but most restrictive system
     Premium pricing and marketing advantages
2. **Percentage System**
     Allows mixing of certified and non-certified materials
     Volume-based or mass-based percentage calculations
     Rolling average calculations over defined periods
     Balance monitoring and claim reconciliation
     Flexibility for complex supply chains
3. **Credit System**
     Credits earned from certified purchases
     Credits applied to sales of eligible products
     Time-based credit accumulation and application
     Complex accounting and verification requirements
     Maximum supply chain flexibility
### Documentation Requirements
1. **Purchase Records**
     Supplier information and certification status
     Volume and material type documentation
     Certificate numbers and validity verification
     Purchase order and invoice records
     Chain of custody claim verification
2. **Production Records**
     Input material tracking and inventory management
     Processing records and yield calculations
     Quality control and specification compliance
     Waste and by-product tracking
     Production planning and scheduling
3. **Sales Documentation**
     Customer information and requirements
     Product specifications and claims
     Delivery documentation and tracking
     Invoice and shipping records
     Certificate and label application
4. **Training and Competency**
     Staff training records and competency assessment
     Chain of custody system understanding
     Procedure compliance and verification
     Continuous improvement and corrective actions
     Management system documentation
### Validation Rules
1. **Scheme Identification**
     certificationSchemeId must be unique across system
     schemeName must match official scheme designation
     schemeStandard must reference current valid version
     issuingOrganizationId must reference valid organization
2. **Geographic and Material Consistency**
     applicableGeographicAreas must reference valid geographic boundaries
     eligibleMaterialTypes must align with scheme scope
     claimTypes must be officially recognized by issuing organization
     Geographic coverage must not exceed scheme authority
3. **Requirement Specifications**
     auditRequirements must specify minimum frequency and scope
     chainOfCustodyRequirements must be technically feasible
     documentationRequirements must support verification needs
     validityPeriod must align with scheme standards
### Example Use Cases
1. **FSC Chain of Custody Implementation**
     Multi-site certification for integrated forest products company
     Percentage-based system for mixed material processing
     Species-specific claims for biodiversity conservation
     Third-party audits with annual surveillance
     International supply chain verification
2. **SFI Fiber Sourcing Program**
     Regional fiber sourcing with controlled wood requirements
     Training programs for logger and landowner education
     Biodiversity conservation and water quality protection
     Community involvement and stakeholder engagement
     Research and development support
3. **Biomass Sustainability Partnership (SBP)**
     Regional risk assessment and mitigation implementation
     Supply base evaluation and verification
     Greenhouse gas emission analysis and reporting
     Energy efficiency and carbon footprint reduction
     Independent third-party evaluation
### Relationships
- CertificationScheme issued by one Organization
- CertificationScheme applies to multiple GeographicData areas
- CertificationScheme supports multiple material types
- CertificationScheme defines requirements for Claim validation
- CertificationScheme referenced by Certificate issuance
- CertificationScheme guides Organization certification processes
- CertificationScheme enables species-specific sustainability tracking
