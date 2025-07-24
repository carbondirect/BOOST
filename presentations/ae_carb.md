# BOOST Agency Engagement: CARB

---


## Outline

- BOOST Overview (10-15 minutes)
- Review BOOST Entity-Relationship Diagram (20-30 minutes)
    - *DISCUSSION:* Are we missing entities?
    - Specific entities *DISCUSSION*:
        - Do we have the right attributes? 
        - What are we missing?
- CARB Topics:
    - LCFS Integration Overview, Entities Deep Dive, Example
    - Biomass pathways update ?


Note: 
- We are hosting targeted meetings with CA agencies to ensure we understand need 
- Version 0.1 will be released in Q2 of 2025.

---

<img src="img/boost_logo.png" alt="logo" style="height: 400px;">

--

## What BOOST is


- A specification defining data formats, field definitions, and validation rules
- A common vocabulary enabling consistent interpretation of biomass chain-of-custody information
- A framework establishing relationships between different types of information
- A validation mechanism ensuring data quality and consistency

--

## What BOOST Is Not

- **Not Software**: BOOST does not prescribe specific applications, databases, or user interfaces. 
- **Not a Database**: BOOST does not create centralized storage or control where data resides. 
- **Not Dashboards or Analytics**: BOOST does not define how data should be visualized or analyzed. 
- **Not a Certification Scheme**: BOOST does not establish sustainability criteria or certification requirements. 

Note: 
- **Not Software** Organizations remain free to choose their preferred software platforms while adhering to BOOST data exchange requirements. 
- **Not Database** Each organization maintains control over their data while following standard formats for sharing.
- **Not Dashboards or Analytics**: It provides the foundation that enables various analytical tools to work with standardized data.
- **Not a Certification Scheme**: It provides the structure for documenting compliance with existing schemes.

--

## What is the objective?

*To develop and maintain a robust interoperable data standard for solid biomass comprised of schemas, protocols, and documenation for tracking biomass materials from source to end-use*

--

## WHAT are the goals

*To improve transparency, verification and trust in biomass supply chains*

*Reduce operational costs and increase access to markets for biomass producers and consumers*

--

## Who is involved?

- Anyone!
- stakeholders:
  - NGOs, independent certification bodies 
  - fed/state agencies, 
  - small and large businesses
  - independent technical experts
  - software developers

---
## Data Standards ??

<img src="img/dm-metadata-standards.jpg" alt="logo" style="height: 200px;">

--
## What are Data Standards?

*Data standards are agreed-upon approaches that allow for consistent measurement, qualification, or exchange of information*

--

## Why develop a Data Standard

Provides a structured framework and a common language for:

- organizing, 
- documenting, 
- formatting **data**
  
Facilitating **aggregation**, **sharing**, and **reuse** across different systems and organizations

--

## What is Chain of Custody (CoC)?

Documentation and recording of:
- movement, 
- handling, 
- transformation 

of material through a supply chain


--

## How do Data Standards Support CoC?

For CoC software, data standards:
  - provide a data framework (entities, attributes, and relationships)
  - provide logic for tracking across complex processes and organizational boundaries
  - enable interoperability between systems
  - provide validation rules

---

## OPEN Standards

<img src="img/open-data-institute.jpg" alt="logo" style="height: 400px;">
<br>
<em>Source: The Open Data Institute</em>

--

## Benefits of Openness

- encourages **interoperability** and digital integration across the supply chain
- transparency and trust among stakeholders in complex supply chains
- democratizes chain of custody data
- software differentiates on performance not on customer coersion

Note:
+ proprietary data formats
+ complex integration
+ data migration obstacles
+ lack of portability


---

## Core Components of the CoC Data Standard

*DRAFT* [Entity Relationship Diagram](https://carbondirect.github.io/BOOST/erd-navigator/)

**Framing Questions**

+ *Did we get the right set of entities?*
+ *Did we get the right attributes for entities you care about?*
+ *Are the relationships between entities appropriate?*

---

## LCFS Integration Overview

BOOST now includes comprehensive support for California's Low Carbon Fuel Standard (LCFS) program compliance.

**Key Features:**
- Complete pathway certification tracking  
- Quarterly compliance reporting
- Credit/deficit calculation support
- Regulated entity management

---

## Core Entity: <span style="color: #1B4F72;">`TraceableUnit`</span>

- <span style="color: #1B4F72;">`traceableUnitId`</span>: Unique TRU identifier
- <span style="color: #1B4F72;">`unitType`</span>: `individual_log`, `pile`, `volume_aggregation`, `processed_batch`
- <span style="color: #1B4F72;">`uniqueIdentifier`</span>: Biometric signature, RFID, QR code
- <span style="color: #1B4F72;">`totalVolumeM3`</span>: Volume in cubic meters
- <span style="color: #1B4F72;">`species`</span>: Tree species information

**Foundation for all biomass traceability**

Note:
- TraceableUnit (TRU) is the core entity in BOOST for tracking biomass materials
- unitType covers different aggregation levels from individual logs to processed batches
- uniqueIdentifier supports various physical identification methods (biometric signatures, RFID tags, QR codes)
- Contains species information, harvest details, and geographic origin data
- Links to all other entities in the biomass supply chain
- Essential for LCFS compliance as it tracks the biomass feedstock that becomes renewable fuel
- Volume tracking supports accurate carbon intensity calculations

--

## Core Entity: <span style="color: #1B4F72;">`Transaction`</span>

- <span style="color: #1B4F72;">`transactionId`</span>: Unique business transaction ID
- <span style="color: #1B4F72;">`supplyingOrganizationId`</span>: Seller organization
- <span style="color: #1B4F72;">`customerOrganizationId`</span>: Buyer organization
- <span style="color: #1B4F72;">`fuelVolume`</span>: Fuel quantity *(LCFS enhancement)*
- <span style="color: #1B4F72;">`lcfsPathwayId`</span>: Linked CARB pathway *(LCFS)*
- <span style="color: #1B4F72;">`reportingPeriod`</span>: Quarterly period *(LCFS)*

**Links biomass materials to fuel transactions**

Note:
- Transaction entity has been enhanced with LCFS-specific fields for fuel compliance
- Original attributes: transactionId, organizations, transactionDate, contractValue, terms
- LCFS enhancements: fuelVolume, fuelCategory, lcfsPathwayId, reportingPeriod, regulatedPartyRole
- Supports both traditional biomass transactions and fuel sales
- Critical link between biomass supply chain and LCFS credit generation
- contractValue and contractCurrency for financial tracking
- transactionStatus for workflow management (pending, confirmed, delivered, completed)
- Links to SalesDeliveryDocument for complete transaction documentation

--

## Core Entity: <span style="color: #1B4F72;">`EnergyCarbonData`</span>

- <span style="color: #1B4F72;">`energyCarbonDataId`</span>: Unique measurement ID
- <span style="color: #1B4F72;">`dataType`</span>: `carbon_intensity`, `energy_content`, `emissions`
- <span style="color: #1B4F72;">`value`</span>: Numeric measurement value
- <span style="color: #1B4F72;">`unit`</span>: `gCO2e/MJ`, `MJ/kg`, `percentage`
- <span style="color: #1B4F72;">`lcfsPathwayType`</span>: CARB pathway classification 
- <span style="color: #1B4F72;">`energyEconomyRatio`</span>: Fuel efficiency ratio 

**Supports LCFS life-cycle carbon intensity calculations**

Note:
- EnergyCarbonData stores all energy and carbon measurements throughout the supply chain
- dataType includes: moisture, transport, fuel consumption, carbon_intensity, energy_content, emissions, lifecycle_assessment
- unit supports various measurement types: percentage, kg_CO2e, liters, MJ, gCO2e/MJ, MJ/kg, gCO2e/gallon, MJ/gallon
- LCFS enhancements: lcfsPathwayType, energyEconomyRatio, lifeCycleStage, regulatoryBenchmark
- measurementDate and methodologyUsed for traceability and verification
- Links to TraceableUnit for biomass-specific measurements
- Critical for LCFS pathway certification and credit calculations
- Supports lifecycle assessment from harvest through fuel production

---

## LCFS Entity: <span style="color: #1B4F72;">`LcfsPathway`</span>

- <span style="color: #1B4F72;">`pathwayId`</span>: CARB identifier 
- <span style="color: #1B4F72;">`carbonIntensity`</span>: `gCO2e/MJ` value
- <span style="color: #1B4F72;">`energyEconomyRatio`</span>: Fuel efficiency ratio
- <span style="color: #1B4F72;">`feedstockCategory`</span>: Biomass type
- <span style="color: #1B4F72;">`certificationDate`</span>: CARB cert date

**Connects to <span style="color: #1B4F72;">`Transaction`</span> and <span style="color: #1B4F72;">`EnergyCarbonData`</span> entities**

Note:
- Purpose: Represents CARB-certified fuel pathways with complete carbon intensity data for LCFS compliance
- pathwayId: Full CARB pathway identifier format (e.g., "CA-RD-2025-LMR-001" for California Renewable Diesel from Logging/Mill Residue)
- carbonIntensity: Complete gCO2e/MJ carbon intensity value used for credit calculations
- energyEconomyRatio: Fuel energy efficiency ratio compared to petroleum baseline
- feedstockCategory: Specific biomass feedstock type (forest residue, agricultural residue, etc.)
- certificationDate: Official CARB certification date for the pathway
- Relationships: Connected to Transaction entities for credit calculation and links to EnergyCarbonData for lifecycle assessments

--

## LCFS Entity: <span style="color: #1B4F72;">`LcfsReporting`</span>

- <span style="color: #1B4F72;">`reportingId`</span>: Quarterly report ID
- <span style="color: #1B4F72;">`reportingPeriod`</span>: Quarter (e.g., `"2025-Q1"`)
- <span style="color: #1B4F72;">`totalCreditsGenerated`</span>: LCFS credits earned
- <span style="color: #1B4F72;">`netPosition`</span>: Net credit/deficit position
- <span style="color: #1B4F72;">`complianceStatus`</span>: Compliance status

**Links to <span style="color: #1B4F72;">`Organization`</span>, <span style="color: #1B4F72;">`Transaction`</span>, and <span style="color: #1B4F72;">`LcfsPathway`</span>**

Note:
- Purpose: Quarterly compliance reports submitted to CARB for regulated entities
- reportingId: Unique quarterly report identifier for tracking submissions
- reportingPeriod: Specific quarter in YYYY-QN format (e.g., "2025-Q1")
- totalCreditsGenerated: Total LCFS credits earned during the reporting period
- totalDeficitsIncurred: Total deficits incurred (removed from slide for space)
- netPosition: Net credit/deficit position after accounting for all transactions
- complianceStatus: Current compliance status (compliant, deficit, etc.)
- Relationships: Links to Organization (regulated entity), summarizes Transaction data by pathway, references LcfsPathway entities

---

## Pacific Renewable Fuels Example

**Real-world LCFS compliance scenario**

### Organization Profile
```json
{
  "organizationId": "pacific-renewable-fuels-001",
  "name": "Pacific Renewable Fuels Corp",
  "lcfsRegistrationId": "LCFS-REG-2025-003",
  "regulatedEntityType": "producer",
  "facilityCapacity": {
    "annualCapacity": 50000000,
    "unit": "gallons_renewable_diesel"
  }
}
```

Note:
- This is a real-world LCFS compliance scenario using BOOST entities to demonstrate practical application
- Organization shows enhanced BOOST Organization entity with LCFS-specific fields
- Located in Stockton, CA with 50M gallon annual renewable diesel capacity
- Contact: compliance@pacificrenewable.com, +1-209-555-0150
- Website: https://www.pacificrenewable.com
- Full organization JSON includes address, contact info, and operational status details

--

### Sample Q1 2025 Transactions

**Transaction 1**: 875K gallons renewable diesel
- Pathway: `CA-RD-2025-LMR-001` 
- Carbon Intensity: 15.2 gCO2e/MJ
- Credits: 52,180 MT CO2e

**Transaction 2**: 1.25M gallons renewable diesel  
- Pathway: `CA-RD-2025-AGR-001`
- Carbon Intensity: 12.8 gCO2e/MJ
- Credits: 78,950 MT CO2e

**Q1 Total**: 3.375M gallons, 196,830 credits

Note:
- Transaction 1 full details: 875,000 gallons renewable diesel using Logging/Mill Residue pathway
- Customer: ca-fuel-distributor-001, delivered to Oakland, CA on 2025-01-15
- Transaction 2 full details: 1,250,000 gallons renewable diesel using Agricultural Residue pathway  
- Customer: ca-fuel-distributor-002, delivered on 2025-01-28
- Additional Q1 transactions bring total to 3.375M gallons across multiple pathways
- Credit calculation: (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER
- Q1 total: 196,830 credits generated across all transactions

--

### LCFS Compliance Workflow

1. **Pathway Certification**: Store CARB-certified data
2. **Transaction Tracking**: Link fuel sales to pathways  
3. **Credit Calculation**: Apply CARB formula
4. **Quarterly Reporting**: Aggregate for CARB submission
5. **Compliance Monitoring**: Track credit/deficit positions

Note:
- Step 1: LcfsPathway entities store CARB-certified pathway data with carbon intensity values
- Step 2: Enhanced Transaction entities link fuel sales to specific certified pathways
- Step 3: Credit calculation using full CARB formula: (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER
- Step 4: LcfsReporting entities aggregate transaction data for quarterly CARB submission
- Step 5: Compliance monitoring tracks credit/deficit positions and submission deadlines
- This workflow demonstrates end-to-end LCFS compliance using BOOST data entities

---

## LCFS Entities: Producers

- Streamlined quarterly reporting process
- Automated credit/deficit tracking
- Pathway management and optimization
- Compliance status monitoring

--

## LCFS Entities: CARB

- Standardized data submission format
- Enhanced verification capabilities  
- Improved data quality and consistency
- Reduced processing overhead

--

## LCFS Entities: For Supply Chain

- End-to-end traceability from feedstock to fuel
- Integration with biomass chain-of-custody data
- Supports multiple regulatory programs simultaneously

---

## Future Enhancement: Innovation Support

**LCFS carbon intensity reduction**

### Electrified Equipment Tracking
- <span style="color: #1B4F72;">`ProcessingHistory`</span>: Track electric equipment
- <span style="color: #1B4F72;">`EnergyCarbonData`</span>: Capture reduced emissions  
- <span style="color: #D35400;">`EnergySource`</span>: Document renewable power *(future)*

**Supporting CARB's innovation goals**

Note:
- BOOST's granular tracking enables documentation of innovative approaches to reducing LCFS fuel carbon intensity
- Electrified chipping example: ProcessingHistory entity can track when electric vs diesel equipment is used for chipping operations, providing documented evidence for carbon intensity reductions
- EnergyCarbonData captures the actual emissions reductions from using renewable electricity instead of diesel fuel
- EnergySource entity (future enhancement) could track the source of electricity (grid vs on-site solar)
- Moisture content optimization: Better moisture tracking leads to more efficient processing and lower CI
- Transport efficiency: Route optimization and electric transport vehicles can be tracked and credited
- Species selection: Different tree species have different carbon profiles that can be optimized for lowest CI pathways
- This supports CARB's goals of incentivizing innovation in the LCFS program through data-driven approaches
- Real-world example: Electric chippers powered by on-site solar could achieve significant CI reductions that are fully documented and verifiable through BOOST entities

--

## Future Enhancement: Biomass Optimization

**Data-driven carbon intensity reduction**

### Optimization Areas
- **Moisture Tracking**: Real-time optimization
- **Transport Efficiency**: Route optimization
- **Species Selection**: CI impact data

**Enabling measurable LCFS improvements**

Note:
- Moisture content optimization: Better moisture tracking leads to more efficient processing and lower CI through optimal drying schedules and reduced energy consumption
- Transport efficiency: Route optimization and electric transport vehicles can be tracked and credited, including electric delivery trucks and optimized logistics
- Species selection: Different tree species have different carbon profiles that can be optimized for lowest CI pathways - Douglas fir vs hardwoods have measurably different carbon intensities
- Route optimization: Electric delivery trucks and optimized logistics reduce transport emissions by 20-40% compared to conventional diesel transport
- Processing efficiency: Real-time equipment monitoring enables continuous process improvement and identifies optimal operating parameters
- Feedstock selection: Data-driven species selection based on carbon intensity profiles enables pathway optimization
- Supply chain innovation: Integration of electric transport, renewable energy, and optimized processing creates compound CI benefits
- This supports CARB's goals of incentivizing innovation through measurable, data-driven improvements that can be verified and credited

--

## Future Enhancement: Real-Time Monitoring

Continuous Monitoring: 

- **Live CI calculations** from supply chain data
- **Automated alerts** for pathway deviations
- **Real-time audit trails** for verification

Program Integration:

- **Cross-agency data sharing** 
- **API integration** with CARB database

**Continuous oversight instead of periodic reporting**

Note:
- Real-time monitoring represents a paradigm shift from current quarterly reporting to continuous oversight, enabling proactive management instead of reactive compliance
- Live CI calculations: As biomass moves through supply chain, carbon intensity is calculated in real-time based on actual operations rather than estimated values
- Automated alerts: System can flag when pathways are deviating from certified CI values, enabling immediate corrective action
- Real-time audit trails: Every transaction and measurement is immediately available for third-party verifiers, eliminating delays in verification processes
- Cross-agency integration addresses current pain point where operators must manually reconcile data across multiple agency portals (CARB LCFS, CalFire THP, CPUC BioRAM, CalRecycle RDRS)
- CARB LCFS database integration eliminates duplicate data entry and ensures consistency across regulatory systems
- Automated report generation reduces administrative burden on regulated entities by 60-80% while improving data quality
- This supports CARB's 2026 geographical data requirements and 2028 third-party certification mandates
- Enables CARB to shift from reactive oversight to proactive program management with early warning systems for compliance issues

--

## Thank You!
