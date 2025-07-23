# Data Dictionary

## CertificationScheme

### Overview
The `CertificationScheme` entity defines certification standards and requirements with geographic applicability as part of Phase 2 BOOST traceability system enhancements. This entity provides the foundational definitions for sustainability certifications, their requirements, and applicable contexts for use throughout the timber supply chain.

### Fields

| Field                          | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `certificationSchemeId`       | string           | Yes      | Unique identifier for the certification scheme (primary key)              | `CERT-SCHEME-FSC-001`, `CERT-SCHEME-SFI-COC` |
| `schemeName`                  | string           | Yes      | Official name of the certification scheme                                 | `FSC Chain of Custody`, `SFI Chain of Custody` |
| `schemeType`                  | string           | Yes      | Type of certification scheme (enum)                                       | `forest_management`, `chain_of_custody`, `biomass_sustainability` |
| `schemeStandard`              | string           | No       | Standard or version identifier                                            | `FSC-STD-40-004 V3-1`, `SFI-2015-2019 COC` |
| `issuingOrganizationId`       | string (FK)      | Yes      | Foreign key to organization that issues this scheme                       | `ORG-FSC-INTERNATIONAL`, `ORG-SFI-INC`    |
| `schemeDescription`           | string           | No       | Detailed description of the certification scheme                          | `Ensures responsible forest management`     |
| `applicableGeographicAreas`   | array<string>    | No       | Geographic areas where this scheme is applicable                          | `["GEO-REGION-NORTH-AMERICA"]`            |
| `eligibleMaterialTypes`       | array<string>    | No       | Material types eligible for this certification scheme                     | `["softwood", "hardwood", "mixed"]`       |
| `claimTypes`                  | array<string>    | No       | Types of claims supported by this scheme                                  | `["FSC Mix", "FSC 100%", "FSC Recycled"]` |
| `auditRequirements`           | string           | No       | Audit and verification requirements                                       | `Annual surveillance audits`               |
| `chainOfCustodyRequirements`  | string           | No       | Chain of custody tracking requirements                                    | `Physical or percentage-based system`      |
| `documentationRequirements`   | array<string>    | No       | Required documentation and record-keeping                                 | `["purchase_records", "sales_invoices"]`  |
| `validityPeriod`              | string           | No       | Typical validity period for certifications                               | `3 years`, `5 years`                      |
| `website`                     | string (uri)     | No       | Official website for the certification scheme                             | `https://fsc.org/`                        |
| `@id`                         | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/certification-scheme/CERT-SCHEME-FSC-001` |
| `lastUpdated`                 | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Scheme Types

1. **forest_management**
   - Certifies responsible forest management practices
   - Covers forest planning, biodiversity conservation, and social impacts
   - Examples: FSC Forest Management, SFI Forest Management
   - Applies to forest owners and managers
   - Long-term forest stewardship focus

2. **chain_of_custody**
   - Tracks certified material through supply chain
   - Ensures segregation and proper mixing calculations
   - Examples: FSC Chain of Custody, SFI Chain of Custody
   - Applies to processors, manufacturers, and traders
   - Material flow and claim verification

3. **controlled_wood**
   - Ensures wood avoids controversial sources
   - Risk assessment and mitigation requirements
   - Examples: FSC Controlled Wood, SFI Fiber Sourcing
   - Due diligence and supply chain verification
   - Minimum acceptable standards

4. **biomass_sustainability**
   - Verifies sustainable biomass production and sourcing
   - Greenhouse gas emission reductions and land use criteria
   - Examples: SBP (Sustainable Biomass Partnership)
   - Regional risk assessments and supply base evaluations
   - Energy and environmental benefits focus

5. **carbon_offset**
   - Quantifies and verifies carbon sequestration and emission reductions
   - Additionality, permanence, and measurement requirements
   - Examples: Verified Carbon Standard (VCS), Climate Action Reserve
   - Forest carbon projects and methodologies
   - Third-party verification and monitoring

6. **environmental_management**
   - Comprehensive environmental management systems
   - ISO 14001 and other environmental standards
   - Continuous improvement and compliance frameworks
   - Environmental impact assessment and mitigation
   - Stakeholder engagement and reporting

### Key Features

1. **Geographic Applicability**
   - Regional and national scheme variations
   - Jurisdiction-specific requirements and adaptations
   - Local stakeholder consultation requirements
   - National forest legislation compliance
   - Cultural and social context integration

2. **Material Type Specificity**
   - Scheme requirements vary by material type
   - Species-specific requirements and considerations
   - Product category eligibility and restrictions
   - Processing method compatibility
   - End-use application suitability

3. **Claim Management**
   - Supported claim types and calculation methods
   - Percentage thresholds and mixing allowances
   - Label use requirements and restrictions
   - Marketing claim validation requirements
   - Consumer communication standards

4. **Verification Requirements**
   - Audit frequency and scope requirements
   - Certification body accreditation standards
   - Competency requirements for auditors
   - Stakeholder consultation processes
   - Complaint and dispute resolution procedures

### Chain of Custody Systems

1. **Physical Separation**
   - Complete segregation of certified and non-certified materials
   - Separate storage, processing, and handling systems
   - No mixing of certified and non-certified materials
   - Highest integrity but most restrictive system
   - Premium pricing and marketing advantages

2. **Percentage System**
   - Allows mixing of certified and non-certified materials
   - Volume-based or mass-based percentage calculations
   - Rolling average calculations over defined periods
   - Balance monitoring and claim reconciliation
   - Flexibility for complex supply chains

3. **Credit System**
   - Credits earned from certified purchases
   - Credits applied to sales of eligible products
   - Time-based credit accumulation and application
   - Complex accounting and verification requirements
   - Maximum supply chain flexibility

### Documentation Requirements

1. **Purchase Records**
   - Supplier information and certification status
   - Volume and material type documentation
   - Certificate numbers and validity verification
   - Purchase order and invoice records
   - Chain of custody claim verification

2. **Production Records**
   - Input material tracking and inventory management
   - Processing records and yield calculations
   - Quality control and specification compliance
   - Waste and by-product tracking
   - Production planning and scheduling

3. **Sales Documentation**
   - Customer information and requirements
   - Product specifications and claims
   - Delivery documentation and tracking
   - Invoice and shipping records
   - Certificate and label application

4. **Training and Competency**
   - Staff training records and competency assessment
   - Chain of custody system understanding
   - Procedure compliance and verification
   - Continuous improvement and corrective actions
   - Management system documentation

### Validation Rules

1. **Scheme Identification**
   - certificationSchemeId must be unique across system
   - schemeName must match official scheme designation
   - schemeStandard must reference current valid version
   - issuingOrganizationId must reference valid organization

2. **Geographic and Material Consistency**
   - applicableGeographicAreas must reference valid geographic boundaries
   - eligibleMaterialTypes must align with scheme scope
   - claimTypes must be officially recognized by issuing organization
   - Geographic coverage must not exceed scheme authority

3. **Requirement Specifications**
   - auditRequirements must specify minimum frequency and scope
   - chainOfCustodyRequirements must be technically feasible
   - documentationRequirements must support verification needs
   - validityPeriod must align with scheme standards

### Example Use Cases

1. **FSC Chain of Custody Implementation**
   - Multi-site certification for integrated forest products company
   - Percentage-based system for mixed material processing
   - Species-specific claims for biodiversity conservation
   - Third-party audits with annual surveillance
   - International supply chain verification

2. **SFI Fiber Sourcing Program**
   - Regional fiber sourcing with controlled wood requirements
   - Training programs for logger and landowner education
   - Biodiversity conservation and water quality protection
   - Community involvement and stakeholder engagement
   - Research and development support

3. **Biomass Sustainability Partnership (SBP)**
   - Regional risk assessment and mitigation implementation
   - Supply base evaluation and verification
   - Greenhouse gas emission analysis and reporting
   - Energy efficiency and carbon footprint reduction
   - Independent third-party evaluation

### Relationships
- CertificationScheme issued by one Organization
- CertificationScheme applies to multiple GeographicData areas
- CertificationScheme supports multiple material types
- CertificationScheme defines requirements for Claim validation
- CertificationScheme referenced by Certificate issuance
- CertificationScheme guides Organization certification processes
- CertificationScheme enables species-specific sustainability tracking