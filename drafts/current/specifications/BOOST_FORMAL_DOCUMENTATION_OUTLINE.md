# BOOST Data Standard - W3C Community Group Final Specification

**Version:** 1.0  
**Date:** 2025-08-01  
**Status:** W3C Community Group Final Specification  
**Editors:** [To be specified]  
**Contributors:** [To be specified from community participation]

---

## Abstract

The Biomass Open-Source Traceability (BOOST) data standard defines a comprehensive, interoperable framework for tracking biomass materials through complex supply chains. BOOST enables transparent, verifiable, and consistent data exchange to support sustainability verification, regulatory compliance, and supply chain integrity across the biomass economy. The standard implements a TraceableUnit (TRU)-centric model supporting media-interruption-free tracking, multi-species composition management, and comprehensive plant part categorization across 33 interconnected entities organized into 7 thematic areas.

## Status of This Document

This specification was published by the Biomass Open Origin Standard for Tracking (BOOST) W3C Community Group. It is not a W3C Standard nor is it on the W3C Standards Track. Please note that under the W3C Community Final Specification Agreement (FSA) other conditions apply. Learn more about W3C Community and Business Groups.

This document is governed by the W3C Community License Agreement (CLA). A human-readable summary is available.

Publication as a Community Group Report does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

## How to Give Feedback

This specification is primarily developed on GitHub. The best way to contribute to this specification is to:

1. File issues and suggestions in the [BOOST GitHub repository](https://github.com/carbondirect/BOOST/issues)
2. Submit pull requests for specific changes
3. Participate in community discussions via GitHub Discussions
4. Join the W3C Community Group mailing list for broader discussions

## Table of Contents

*[Table of contents will be auto-generated]*

---

## 1. Introduction *(Normative)*

### 1.1 Purpose and Scope
This specification defines the BOOST (Biomass Open-Source Traceability) data standard for biomass supply chain tracking and verification. The standard provides:

- A unified data model for biomass custody transfers
- Format constraints for serializing chain of custody data
- Integration specifications for certification systems
- Regulatory compliance frameworks for multiple jurisdictions

### 1.2 Background and Motivation
The development of comprehensive biomass traceability systems addresses critical needs for sustainability verification, regulatory compliance, and supply chain transparency in the growing biomass economy. This standard enables interoperability between reporting systems, registries, and certification bodies.

### 1.3 Relationship to Existing Standards
BOOST builds upon and integrates with established standards including:
- ISO 38200:2018 Chain of custody of wood and wood-based products
- Sustainable Biomass Partnership (SBP) Standards 4, 5, and 6
- Forest Stewardship Council (FSC) certification standards
- Programme for Endorsement of Forest Certification (PEFC) standards

### 1.4 Community Group Process
This specification was developed through the W3C Community Group process with balanced stakeholder participation including civil society organizations, government agencies, small and large businesses, and independent technical experts.

## 2. Conformance *(Normative)*

This section describes the conformance requirements for BOOST implementations. The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

### 2.1 Conformance Classes

#### 2.1.1 BOOST Core Conformance
Implementations claiming BOOST Core conformance MUST support:
- TraceableUnit entity with required fields
- Basic material tracking and identification
- JSON-LD serialization format
- Schema validation according to Section 4

#### 2.1.2 BOOST Extended Conformance  
Implementations claiming BOOST Extended conformance MUST support Core conformance plus:
- Multi-species composition tracking
- Geographic data integration (GeoJSON)
- Material processing operations
- Basic sustainability claims management

#### 2.1.3 BOOST Full Conformance
Implementations claiming BOOST Full conformance MUST support Extended conformance plus:
- All 33 BOOST entities
- Complete business logic validation
- Multi-certification scheme support
- LCFS regulatory integration

### 2.2 Implementation Requirements
Conforming implementations MUST:
- Validate data against BOOST JSON schemas
- Preserve entity relationships and referential integrity
- Support JSON-LD context and semantic annotations
- Implement required business logic validation rules

## 3. BOOST Traceability System *(Normative)*

### 3.1 TraceableUnit (TRU) Central Concept
The TraceableUnit entity serves as the central hub for all biomass tracking operations. Every TRU MUST have:
- Unique identifier with biometric signature capability
- Material type classification
- Volume and mass measurements
- Geographic location data
- Processing history linkage

### 3.2 Media-Interruption-Free Tracking
BOOST implementations MUST support continuous traceability through:
- Biometric identification without physical attachments
- Optical pattern recognition for TRU identification
- Data continuity validation across processing steps
- Media break detection and flagging mechanisms

### 3.3 Three Critical Tracking Points
Implementations MUST support measurement and verification at:
- **harvest_site** - Initial TRU creation and measurement
- **skid_road/forest_road** - Transportation consolidation points  
- **mill_entrance** - Processing facility entry points

### 3.4 Processing Chain Methodology
All material transformations MUST be documented through:
- MaterialProcessing entities linking input and output TRUs
- Volume and mass conservation validation
- Plant part transformation tracking
- Quality assessment throughout processing

## 4. Data Model Architecture *(Normative)*

### 4.1 Entity-Relationship Overview
The BOOST data model consists of 33 interconnected entities organized into 7 thematic areas:

1. **Core Traceability** (9 entities) - Central tracking infrastructure
2. **Organizational Foundation** (4 entities) - Business entities and certifications  
3. **Material & Supply Chain** (4 entities) - Material definitions and supply management
4. **Transaction Management** (3 entities) - Business transaction processing
5. **Sustainability Claims** (1 entity) - Certification and sustainability assertions
6. **Geographic Integration** (1 entity) - Spatial data and location services
7. **Reporting & Compliance** (7 entities) - Analytics, reporting, and regulatory compliance

### 4.2 Hub-and-Spoke Design
The data model implements a hub-and-spoke architecture with TraceableUnit as the central hub. All other entities MUST maintain direct or indirect relationships to TRUs to ensure complete traceability.

### 4.3 Foreign Key Conventions
All foreign key relationships MUST follow the EntityNameId pattern:
- Field names MUST end with "Id" 
- Field names MUST reference the target entity name in PascalCase
- Examples: `OrganizationId`, `TraceableUnitId`, `GeographicDataId`

### 4.4 Hierarchical Relationships
The data model supports hierarchical relationships through:
- Parent-child TRU relationships for split/merge operations
- Processing history chains through MaterialProcessing entities
- Organizational hierarchies through Organization entities
- Geographic containment through GeographicData entities

## 5. Plant Part Categorization System *(Normative)*

### 5.1 Standardized Plant Parts Taxonomy
Implementations MUST support the following 17 standardized plant parts:
- **trunk** - Main stem/bole of tree
- **heartwood** - Inner, non-living wood
- **sapwood** - Outer, living wood
- **bark** - Protective outer layer
- **branches** - Secondary stems
- **leaves** - Photosynthetic organs
- **seeds** - Reproductive structures
- **roots** - Below-ground structures
- **twigs** - Small branches
- **cones** - Seed-bearing structures
- **needles** - Coniferous leaves
- **foliage** - All leaf matter
- **crown** - Above-ground branching structure
- **stump** - Remaining base after felling
- **chips** - Mechanically processed fragments
- **sawdust** - Fine processing residue
- **pellets** - Densified processed material

### 5.2 Processing Transformation Rules
Material processing operations MUST document plant part transformations including:
- Input plant part composition percentages
- Output plant part composition percentages  
- Transformation methods and efficiency
- Byproduct and waste stream categorization

### 5.3 Value Optimization and Circular Economy
Implementations SHOULD support value optimization through:
- Plant part-specific routing and processing decisions
- Byproduct utilization tracking
- Waste stream minimization and circularity metrics
- Economic value attribution by plant part category

## 6. Core Data Entities *(Normative)*

### 6.1 Core Traceability Entities
Implementations claiming BOOST Core conformance MUST support these entities:

#### 6.1.1 TraceableUnit
Primary tracking entity with the following REQUIRED fields:
- `traceableUnitId` - Unique identifier
- `unitType` - Type classification (log, pile, batch, container)
- `uniqueIdentifier` - Biometric signature or physical identifier
- `totalVolumeM3` - Volume in cubic meters
- `materialTypeId` - Reference to Material entity
- `isMultiSpecies` - Boolean flag for species composition

#### 6.1.2 MaterialProcessing  
Processing operations with REQUIRED fields:
- `processingId` - Unique processing operation identifier
- `processType` - Type of processing operation
- `inputTraceableUnitIds` - Array of input TRU references
- `outputTraceableUnitIds` - Array of output TRU references
- `processTimestamp` - Date and time of processing

#### 6.1.3 GeographicData
Spatial location data with REQUIRED fields:
- `geographicDataId` - Unique location identifier  
- `coordinates` - GeoJSON compliant coordinate data
- `locationType` - Classification of location type
- `administrativeBoundary` - Jurisdictional information

### 6.2 Organizational Foundation Entities
Implementations MUST support these organizational entities:

#### 6.2.1 Organization
Supply chain participants with REQUIRED fields:
- `organizationId` - Unique organization identifier
- `name` - Legal entity name
- `organizationType` - Role classification (harvester, processor, transporter)
- `contactEmail` - Primary contact information

#### 6.2.2 Certificate  
Certification records with REQUIRED fields:
- `certificateId` - Unique certificate identifier
- `certificateNumber` - Official certificate number
- `certificationSchemeId` - Reference to CertificationScheme
- `validFrom` - Certificate validity start date
- `validTo` - Certificate expiration date

### 6.3 Additional Entity Requirements
Extended and Full conformance implementations MUST support additional entities as specified in Appendix A.

## 7. Schema Definitions *(Normative)*

### 7.1 JSON Schema Format
All BOOST entity definitions MUST be provided as JSON Schema Draft-07 compliant schemas with the following REQUIRED structure:

```json
{
  "schema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/carbondirect/BOOST/schemas/entity-name",
    "title": "Entity Name",
    "type": "object",
    "properties": { ... },
    "required": [ ... ]
  }
}
```

### 7.2 Required vs Optional Fields
- Fields listed in the `required` array MUST be present in all instances
- Optional fields MAY be omitted but MUST conform to schema when present
- Implementations MUST validate all fields against their schema definitions

### 7.3 Data Types and Constraints  
Implementations MUST support these data types:
- `string` - Text values with optional pattern constraints
- `number` - Numeric values with optional minimum/maximum
- `integer` - Whole number values  
- `boolean` - True/false values
- `array` - Lists of values
- `object` - Complex nested structures

### 7.4 Business Logic Validation
Implementations MUST validate entities against 8 categories of business rules:
1. **Volume/Mass Conservation** - Physical conservation laws
2. **Temporal Logic** - Date consistency validation  
3. **Geographic Logic** - Spatial relationship validation
4. **Species Composition** - Percentage validation (sum to 100%)
5. **Certification Logic** - Chain of custody validation
6. **Regulatory Compliance** - Jurisdiction-specific rules
7. **Economic Logic** - Price and payment validation
8. **Quality Assurance** - Material quality constraints

## 8. Serialization and Exchange *(Normative)*

### 8.1 JSON-LD as Primary Format
BOOST data MUST be serializable to JSON-LD 1.1 format with:
- Valid `@context` referencing BOOST context definition
- Entity `@type` declarations matching schema names
- Unique `@id` values for all entities

### 8.2 Context Definitions
The BOOST JSON-LD context MUST define:
- Semantic mappings for all entity types
- Property definitions with appropriate vocabularies
- Data type specifications for typed literals
- Language specifications for internationalization

### 8.3 Alternative Serialization Formats
Implementations MAY support additional formats:
- JSON (without semantic annotations)
- XML with BOOST schema definitions
- CSV for tabular data exchange
- Binary formats for efficient transmission

---

## 9. Use Cases and Requirements *(Informative)*

### 9.1 Primary Use Cases
BOOST addresses the following primary use cases:

#### 9.1.1 California Biomass Supply Chain Tracking
- Forest management organization harvests certified timber
- Processing facilities transform raw materials into biofuels
- Transportation companies maintain chain of custody
- Regulatory agencies verify compliance with LCFS requirements

#### 9.1.2 Multi-Certification Scheme Management
- Single TRU maintains multiple certification claims (FSC, SBP, PEFC)
- Processing operations preserve claim integrity
- Species-specific claims apply to mixed-species materials
- Third-party verification validates claim accuracy

#### 9.1.3 Regulatory Compliance Reporting
- Organizations generate quarterly LCFS compliance reports
- Supply base reports document sustainable sourcing
- Audit trails provide complete transaction history
- Data exchange enables cross-jurisdictional compliance

### 9.2 Stakeholder Requirements
Key stakeholder requirements include:
- **Forest Managers**: Harvest planning and certification tracking
- **Processing Facilities**: Material flow optimization and quality control
- **Transportation**: Chain of custody maintenance and efficiency
- **Regulatory Agencies**: Compliance monitoring and verification
- **Certification Bodies**: Audit trail access and claim validation

## 10. Examples *(Informative)*

### 10.1 Basic TraceableUnit Example
```json
{
  "@context": "https://boost-standard.org/context.jsonld",
  "@type": "TraceableUnit",
  "@id": "https://example.com/tru/TRU-001",
  "traceableUnitId": "TRU-FOREST-001",
  "unitType": "pile",
  "uniqueIdentifier": "BIOMETRIC-SIGNATURE-ABC123",
  "totalVolumeM3": 125.5,
  "materialTypeId": "MAT-DOUGLAS-FIR-SAWLOG",
  "isMultiSpecies": false,
  "harvesterId": "ORG-PACIFIC-FOREST",
  "currentGeographicDataId": "GEO-MILL-YARD-07"
}
```

### 10.2 Material Processing Chain Example
```json
{
  "@type": "MaterialProcessing",
  "processingId": "PROC-SAWMILL-001",
  "processType": "primary_breakdown",
  "inputTraceableUnitIds": ["TRU-FOREST-001"],
  "outputTraceableUnitIds": ["TRU-LUMBER-001", "TRU-CHIPS-001"],
  "processTimestamp": "2025-08-01T10:30:00Z",
  "facilityId": "FAC-SAWMILL-PORTLAND",
  "operatorId": "OPR-SMITH-JOHN"
}
```

## 11. Security Considerations *(Informative)*

### 11.1 Data Privacy
Implementations SHOULD consider privacy implications of biomass tracking data:
- Location data may reveal sensitive commercial information
- Biometric identifiers require secure storage and transmission
- Personal operator information needs appropriate access controls

### 11.2 Data Integrity
Critical security measures include:
- Digital signatures for high-value transactions
- Audit trails for all data modifications
- Backup and recovery procedures for critical supply chain data
- Validation of external data sources and certificates

### 11.3 Supply Chain Security
Implementations SHOULD address:
- Authentication of supply chain participants
- Authorization controls for data access and modification
- Secure communication channels for data exchange
- Fraud detection and prevention mechanisms

## Normative References

- **[RFC2119]** S. Bradner. "Key words for use in RFCs to Indicate Requirement Levels". RFC 2119, March 1997.
- **[RFC8174]** B. Leiba. "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words". RFC 8174, May 2017.
- **[JSON-LD11]** W3C JSON-LD Community Group. "JSON-LD 1.1". W3C Recommendation, 16 July 2020.
- **[JSON-SCHEMA]** JSON Schema specification. Draft-07, March 2019.
- **[GEOJSON]** H. Butler, M. Daly, A. Doyle, S. Gillies, S. Hagen, T. Schaub. "The GeoJSON Format". RFC 7946, August 2016.
- **[ISO38200]** ISO 38200:2018. "Chain of custody of wood and wood-based products".

## Informative References

- **[SBP-STANDARD-4]** Sustainable Biomass Partnership. "Chain of Custody Standard". Version 1.0, 2013.
- **[SBP-STANDARD-5]** Sustainable Biomass Partnership. "Collection and Communication of Data". Version 1.0, 2013.
- **[FSC-STD-40-004]** Forest Stewardship Council. "Chain of Custody Certification". Version 3.0, 2017.
- **[PEFC-ST-2002]** Programme for Endorsement of Forest Certification. "Chain of Custody of Forest Based Products". 2020.
- **[CA-LCFS]** California Air Resources Board. "Low Carbon Fuel Standard Regulation". 2024.
- **[EU-RED-II]** European Union. "Renewable Energy Directive II". Directive (EU) 2018/2001.

## Acknowledgments

This specification was developed through the collaborative efforts of the BOOST W3C Community Group with significant contributions from:

- **California Department of Conservation** - Funding and regulatory guidance
- **Forest industry stakeholders** - Requirements analysis and use case development  
- **Certification bodies** - Standards alignment and validation procedures
- **Technology providers** - Implementation guidance and tool development
- **Academic institutions** - Research and analysis support
- **Environmental organizations** - Sustainability criteria and verification methods

Special recognition to the contributors of the Interactive ERD Navigator, Python reference implementation, and comprehensive schema validation tools that support this specification.

---

## Appendix A: Complete Entity Schema Registry *(Informative)*

[Complete definitions of all 33 BOOST entities with required fields, optional fields, relationships, and examples]

## Appendix B: Implementation Examples *(Informative)*

[Detailed code samples, integration patterns, and common implementation scenarios]

## Appendix C: Regulatory Compliance Mapping *(Informative)*

[Mapping of BOOST entities to California LCFS, EU RED II, and other regulatory requirements]

## Appendix D: Migration and Integration Guide *(Informative)*

[Guidance for migrating from legacy systems and integrating with existing supply chain infrastructure]

## Appendix E: Interactive Tools Documentation *(Informative)*

[Usage guides for ERD Navigator, Schema integrity reviewer, and validation tools]

---

## Document Metadata

**Document Status:** W3C Community Group Final Specification  
**Publication Date:** 2025-08-01  
**Version:** 1.0  
**Previous Version:** N/A  
**Latest Version:** https://boost-standard.org/specifications/latest/  
**Repository:** https://github.com/carbondirect/BOOST  
**Test Suite:** https://github.com/carbondirect/BOOST/tree/main/tests  
**Implementation Reports:** https://boost-standard.org/implementation-reports/

**Copyright Notice:** Copyright © 2025 BOOST W3C Community Group. This work is licensed under the W3C Software and Document License.

**Patent Policy:** This specification is subject to the W3C Community Final Specification Agreement (FSA). Participants in the BOOST Community Group have made commitments under this agreement regarding any Essential Claims related to this specification.

---

## Summary of W3C Compliance

This specification now fully aligns with W3C Community Group requirements:

### ✅ **Required W3C Sections Included:**
- **Abstract** - Concise specification summary
- **Status of This Document** - W3C Community Group disclaimers and legal status
- **How to Give Feedback** - Clear contribution mechanisms via GitHub
- **Conformance** - RFC 2119 compliance with three conformance classes
- **Security Considerations** - Privacy, integrity, and supply chain security
- **Normative/Informative References** - Properly separated and formatted
- **Acknowledgments** - Community contributor recognition

### ✅ **Technical Specifications:**
- **Normative sections** (1-8) define required implementation behavior
- **Informative sections** (9-11, Appendices) provide guidance and examples
- **RFC 2119 keywords** properly used throughout normative sections
- **JSON-LD compliance** with semantic web integration
- **Conformance classes** enabling graduated implementation approaches

### ✅ **W3C Process Compliance:**
- **Community Group status** clearly stated with appropriate disclaimers
- **Patent commitments** referenced through FSA agreement
- **Copyright licensing** under W3C Software and Document License
- **Publication format** suitable for W3C Community Group publication

This W3C-compliant outline transforms BOOST from working draft to formal specification ready for Community Group publication and industry implementation.