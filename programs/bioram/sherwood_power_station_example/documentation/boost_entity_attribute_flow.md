# BOOST Entity Attribute Flow: BioRAM Implementation  

## Detailed Entity Attribute Mapping for Sherwood Power Station

This section provides detailed analysis of how specific BOOST entity attributes flow through the Sherwood Power Station BioRAM compliance workflow. The diagrams complement the main entity flow visualizations by showing granular field-level data relationships and transformations specific to biomass power generation.

## Primary Diagrams Reference

The three primary diagrams showing the complete BioRAM workflow are located in:
- [Sherwood Station BOOST Entity Flow](sherwood_station_boost_entity_flow.md)

These primary diagrams include:
1. **Data Flow Through BOOST Entities** ([feedstock_flow.svg](../diagrams/feedstock_flow.svg))
2. **BOOST Entity Relationships ERD** ([boost_entity_relationships.svg](../diagrams/boost_entity_relationships.svg))  
3. **Production Workflow** ([production_workflow.svg](../diagrams/production_workflow.svg))

## Attribute-Level Analysis

### Key Entity Attribute Flows

The BioRAM compliance workflow demonstrates sophisticated attribute mapping between BOOST entities for biomass power generation:

#### Material → BioRAMPathway → Transaction Chain
- **Feedstock Classification**: Material.materialType → BioRAMPathway.feedstockCategory
- **Carbon Intensity**: Material.biomassCI → BioRAMPathway.carbonIntensity → EnergyCarbonData.value
- **Moisture Content**: Material.moistureContent → affects energy conversion efficiency calculations
- **Certification**: Material.sustainabilityCertification → BioRAMPathway.verificationStatus

#### Organization → Regulatory Mapping
- **BioRAM Registration**: Organization.bioramRegistrationId → Transaction.organizationId → BioRAMReporting.organizationId
- **Facility Type**: Organization.facilityType → determines power generation pathway eligibility
- **Generation Capacity**: Organization.powerGenerationCapacity → validates efficiency calculations against rated capacity
- **Storage Capacity**: Organization.biomassStorageCapacity → ensures adequate feedstock handling capability

#### Transaction → Efficiency Calculation
- **Biomass Volume**: Transaction.biomassVolume → BioRAMReporting.totalBiomassVolume (bone dry tonnes)
- **Energy Output**: Transaction.energyGenerated → BioRAMReporting.totalEnergyGenerated (MWh)
- **Efficiency Calculation**: Energy_MWh ÷ Biomass_BDT = efficiency ratio (target: ≥35%)
- **Pathway Attribution**: Transaction.pathwayId → BioRAMPathway.carbonIntensity → weighted CI calculation

#### Location → Fire Hazard Zone Validation
- **Haul Distance**: Transaction.haulDistance → validates transportation efficiency and costs
- **Fire Hazard Zone**: Transaction.fireHazardZoneStatus → provides BioRAM program preference scoring
- **Geographic Data**: Links biomass source locations to CAL FIRE high-risk zone designations

### Business Logic Validation

The attribute flows demonstrate BOOST's built-in validation capabilities for biomass power:

1. **Efficiency Validation**: Power output validated against biomass input and facility capacity
2. **Feedstock Tracking**: Sustainability certifications maintained from forest/mill through final reporting
3. **Carbon Intensity Verification**: CI values tracked from feedstock through final compliance calculations
4. **Volume Limits**: Transaction volumes validated against BioRAMPathway.annualBiomassLimit
5. **Fire Zone Compliance**: Geographic validation ensures feedstock sourcing from priority areas

### Data Integrity Features

Key data integrity mechanisms demonstrated:

- **Unique Identifiers**: All entities use structured ID patterns (ORG-*, TXN-*, PWR-*) for traceability
- **Cross-Reference Validation**: Foreign key relationships ensure consistency across biomass supply chain
- **Audit Trail**: Complete attribute lineage from forest/mill source to CEC compliance reporting
- **Business Rule Enforcement**: Automatic validation of BioRAM regulatory constraints
- **Energy Balance**: Mass and energy conservation validated across the entire process

## Implementation Benefits

This attribute-level mapping demonstrates:

1. **Regulatory Readiness**: Direct mapping from BOOST attributes to BioRAM requirements
2. **Data Quality**: Built-in validation ensures compliance and audit integrity for power generation
3. **Scalability**: Entity structure supports multi-pathway, multi-supplier biomass operations
4. **Interoperability**: Standardized attributes enable integration with utility dispatch systems
5. **Environmental Tracking**: Complete carbon footprint and sustainability certification management

## Technical Specifications

### Entity Attribute Coverage
- **Material Entities**: 8 biomass-specific attributes with moisture content and sustainability tracking
- **Organization Entities**: 6 power generation facility attributes for BioRAM compliance
- **BioRAMPathway Entities**: 9 pathway attributes with carbon intensity and efficiency verification
- **Transaction Entities**: 10 biomass transaction attributes with volume, haul distance, and fire zone status
- **EnergyCarbonData Entities**: 7 carbon intensity attributes with biomass-specific methodology
- **BioRAMReporting Entities**: 12 compliance attributes for quarterly CEC submission

### Validation Rules
- Efficiency limits enforced at facility and pathway level (minimum 35%)
- Carbon intensity ranges validated against BioRAM targets (≤25.0 gCO2e/MJ)
- Feedstock eligibility verified for biomass categories (mill residues, forest residues)
- Energy conversion factors applied consistently (0.8 MWh/BDT target efficiency)
- Fire hazard zone status validated against CAL FIRE high-risk designations
- Haul distance limits enforced for economic and environmental optimization

### Power Generation Specific Attributes
- **Boiler Efficiency**: Tracked for overall plant performance monitoring
- **Turbine Efficiency**: Steam-to-electricity conversion efficiency
- **Grid Interconnection**: PG&E delivery point and REC generation tracking
- **Capacity Factor**: Actual vs. rated power generation performance
- **Availability**: Plant uptime and scheduled maintenance coordination

## Environmental Impact Tracking

The BioRAM implementation tracks key environmental benefits through BOOST attributes:

1. **Fire Risk Reduction**: Geographic tracking of biomass removal from high-hazard zones
2. **Carbon Sequestration**: Lifecycle carbon analysis from forest growth through power generation
3. **Waste Stream Utilization**: Conversion of mill residues from waste to valuable energy
4. **Rural Economic Impact**: Economic value creation in forestry and lumber communities
5. **Grid Decarbonization**: Renewable electricity contribution to California's clean energy goals

The Sherwood Power Station example demonstrates how BOOST's attribute-level design supports complex biomass power generation regulatory compliance while maintaining data integrity and environmental benefit tracking essential for BioRAM operations.
