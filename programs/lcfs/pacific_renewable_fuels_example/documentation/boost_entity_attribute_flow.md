# BOOST Entity Attribute Flow: LCFS Implementation  

## Detailed Entity Attribute Mapping for Pacific Renewable Fuels

This section provides detailed analysis of how specific BOOST entity attributes flow through the Pacific Renewable Fuels LCFS compliance workflow. The diagrams complement the main entity flow visualizations by showing granular field-level data relationships and transformations.

## Primary Diagrams Reference

The three primary diagrams showing the complete LCFS workflow are located in:
- [Pacific Renewable Fuels BOOST Entity Flow](pacific_renewable_fuels_boost_entity_flow.md)

These primary diagrams include:
1. **Data Flow Through BOOST Entities** ([feedstock_flow.svg](../diagrams/feedstock_flow.svg))
2. **BOOST Entity Relationships ERD** ([boost_entity_relationships.svg](../diagrams/boost_entity_relationships.svg))  
3. **Production Workflow** ([production_workflow.svg](../diagrams/production_workflow.svg))

## Attribute-Level Analysis

### Key Entity Attribute Flows

The LCFS compliance workflow demonstrates sophisticated attribute mapping between BOOST entities:

#### Material → LCFSPathway → Transaction Chain
- **Feedstock Classification**: Material.materialType → LCFSPathway.feedstockCategory
- **Carbon Intensity**: Material.totalFeedstockCI → LCFSPathway.carbonIntensity → EnergyCarbonData.value
- **Certification**: Material.sustainabilityCertification → LCFSPathway.verificationStatus

#### Organization → Regulatory Mapping
- **LCFS Registration**: Organization.lcfsRegistrationId → Transaction.organizationId → LCFSReporting.organizationId
- **Entity Type**: Organization.regulatedEntityType → determines reporting requirements and compliance obligations
- **Facility Capacity**: Organization.facilityCapacity → validates transaction volumes against operational limits

#### Transaction → Credit Calculation
- **Volume Conversion**: Transaction.fuelVolume → Transaction.energyMJ (using 138.7 MJ/gallon for renewable diesel)
- **Pathway Attribution**: Transaction.lcfsPathwayId → LCFSPathway.carbonIntensity → credit calculation
- **Credit Generation**: (Benchmark_CI - Pathway_CI) × Energy_MJ × EER = LCFS_Credits

### Business Logic Validation

The attribute flows demonstrate BOOST's built-in validation capabilities:

1. **Volume Validation**: Transaction volumes validated against LCFSPathway.annualVolumeLimit
2. **Certification Tracking**: Sustainability certifications maintained from Material through final reporting
3. **Carbon Intensity Verification**: CI values tracked from feedstock through final compliance calculations
4. **Regulatory Compliance**: All attributes mapped to CARB reporting requirements

### Data Integrity Features

Key data integrity mechanisms demonstrated:

- **Unique Identifiers**: All entities use structured ID patterns for traceability
- **Cross-Reference Validation**: Foreign key relationships ensure data consistency
- **Audit Trail**: Complete attribute lineage from source materials to compliance reporting
- **Business Rule Enforcement**: Automatic validation of regulatory constraints

## Implementation Benefits

This attribute-level mapping demonstrates:

1. **Regulatory Readiness**: Direct mapping from BOOST attributes to LCFS requirements
2. **Data Quality**: Built-in validation ensures compliance and audit integrity  
3. **Scalability**: Entity structure supports multi-pathway, multi-feedstock operations
4. **Interoperability**: Standardized attributes enable system integration

## Technical Specifications

### Entity Attribute Coverage
- **Material Entities**: 6 core attributes with sustainability certification tracking
- **Organization Entities**: 4 LCFS-specific attributes for regulatory compliance
- **LCFSPathway Entities**: 7 pathway attributes with carbon intensity verification
- **Transaction Entities**: 8 transaction attributes with volume and energy calculations
- **EnergyCarbonData Entities**: 5 carbon intensity attributes with CA-GREET methodology
- **LCFSReporting Entities**: 8 compliance attributes for quarterly CARB submission

### Validation Rules
- Volume limits enforced at pathway level
- Carbon intensity ranges validated against CARB benchmarks
- Certification requirements verified for feedstock categories
- Energy conversion factors applied consistently across all transactions

The Pacific Renewable Fuels example demonstrates how BOOST's attribute-level design supports complex regulatory compliance while maintaining data integrity and audit capabilities essential for LCFS operations.