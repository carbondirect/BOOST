# Certification Scheme Data Dictionary

## Overview
The `CertificationScheme` entity defines the standards, requirements, and geographic applicability for sustainability certifications within the BOOST system. It serves as the foundational definition for how certifications are managed and validated throughout the timber supply chain, with full support for JSON-LD.

## Fields

| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `@context` | object | No | JSON-LD context for semantic web compatibility. | `{"@vocab": "https://schema.org/"}` |
| `@type` | string | No | JSON-LD type identifier, constant: `CertificationScheme`. | `CertificationScheme` |
| `@id` | string (uri)| Yes | Unique URI identifier for the certification scheme. | `https://example.com/schemes/FSC-CoC` |
| `certificationSchemeId`| string | Yes | Unique identifier for the certification scheme (primary key). | `CERT-SCHEME-FSC-001` |
| `schemeName` | string | Yes | Official name of the certification scheme. | `FSC Chain of Custody` |
| `recognitionStatus` | string | Yes | The recognition status of the scheme. Enum: `internationally-recognized`, `nationally-approved`, `pending-approval`, `not-recognized`. | `internationally-recognized` |
| `schemeType` | string | Yes | The type of certification scheme. | `forest_management`, `chain_of_custody` |
| `schemeStandard` | string | No | The specific standard or version identifier. | `FSC-STD-40-004 V3-1` |
| `issuingOrganizationId`| string | Yes | Foreign key to the `Organization` that issues this scheme. | `ORG-FSC-INTERNATIONAL` |
| `description` | string | No | A short, generic description of the scheme. | `A certification for responsible forestry.` |
| `schemeDescription` | string | No | A more detailed description of the certification scheme. | `Ensures responsible forest management...` |
| `applicableGeographicAreas`| array | No | Geographic areas where this scheme is applicable. | `["GEO-REGION-NORTH-AMERICA"]` |
| `materialCategories` | array | No | A list of material categories covered by the scheme. | `["Roundwood", "Chips"]` |
| `controlSystems` | array | No | A list of control systems required by the scheme. | `["Physical Separation", "Credit"]` |
| `labelUseRequirements` | string | No | Requirements for using the scheme's label on products. | `Must display logo with license number.` |
| `volumeTrackingRequirements`| string | No | Requirements for tracking the volume of certified material. | `Mass balance calculations required quarterly.` |
| `dueDiligenceRequirements`| string | No | Due diligence requirements for verifying material sources. | `Risk assessment required for all new suppliers.` |
| `sustainabilityCriteria`| array | No | A list of sustainability criteria the scheme addresses. | `["Biodiversity", "Water Quality"]` |
| `applicableRegions`| array | No | A list of regions where the scheme is applicable. | `["North America", "Europe"]` |
| `dateEstablished` | string (date)| No | The date the certification scheme was established. | `1993-01-01` |
| `eligibleMaterialTypes`| array | No | A list of material types eligible for this certification. | `["softwood", "hardwood"]` |
| `claimTypes` | array | No | The types of claims supported by this scheme. | `["FSC Mix", "FSC 100%"]` |
| `auditRequirements`| string | No | Requirements for audits and verification. | `Annual surveillance audits required.` |
| `chainOfCustodyRequirements`| string | No | Requirements for chain of custody tracking. | `Physical or percentage-based system.` |
| `documentationRequirements`| array | No | A list of required documentation for compliance. | `["purchase_records", "sales_invoices"]` |
| `validityPeriod` | string | No | The typical validity period for certifications under this scheme. | `3 years`, `5 years` |
| `website` | string (uri)| No | The official website for the certification scheme. | `https://fsc.org/` |
| `lastUpdated` | string (date-time)| No | Timestamp of the most recent data update. | `2025-07-21T15:45:00Z` |
| `versionNumber` | string | Yes | The version number of the certification scheme. | `v3-1` |

---

### Scheme Types

1.  **forest_management**: Certifies responsible forest management practices, covering planning, biodiversity, and social impacts.
2.  **chain_of_custody**: Tracks certified material through the supply chain, ensuring proper segregation and mixing calculations.
3.  **controlled_wood**: Ensures wood avoids controversial sources through risk assessment and mitigation.
4.  **biomass_sustainability**: Verifies sustainable biomass production, focusing on GHG reductions and land use.
5.  **carbon_offset**: Quantifies and verifies carbon sequestration and emission reductions.
6.  **environmental_management**: Focuses on comprehensive environmental management systems, like ISO 14001.

---

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