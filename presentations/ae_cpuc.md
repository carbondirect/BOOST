# BOOST Agency Engagement: CPUC

---


## Outline

- BOOST Overview (10-15 minutes)
- Review BOOST Entity-Relationship Diagram (20-30 minutes)
    - *DISCUSSION:* Are we missing entities?
    - Specific entities *DISCUSSION*:
        - Do we have the right attributes? 
        - What are we missing?
- CPUC Topics:
    - Utility Biomass Program Integration
    - Renewable Energy Certificate (REC) Support
    - Example Implementation


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

## Utility Biomass Integration Overview

BOOST supports comprehensive tracking for utility biomass programs with:

**Key Features:**
- Forest management activity documentation  
- Renewable Energy Certificate (REC) tracking
- Power generation sourcing and verification
- Biomass fuel quality and energy content tracking

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
- Essential for utility compliance as it tracks the biomass feedstock used for power generation
- Volume tracking supports accurate energy content calculations for REC generation

--

## Core Entity: <span style="color: #1B4F72;">`Transaction`</span>

- <span style="color: #1B4F72;">`transactionId`</span>: Unique business transaction ID
- <span style="color: #1B4F72;">`supplyingOrganizationId`</span>: Seller organization
- <span style="color: #1B4F72;">`customerOrganizationId`</span>: Buyer organization
- <span style="color: #1B4F72;">`contractValue`</span>: Transaction financial value
- <span style="color: #1B4F72;">`deliveryLocation`</span>: Biomass delivery point
- <span style="color: #1B4F72;">`transactionStatus`</span>: Current status

**Links biomass materials to power generation**

Note:
- Transaction entity tracks commercial exchange of biomass materials between organizations
- Original attributes: transactionId, organizations, transactionDate, contractValue, terms
- Critical for utility programs to track biomass from forest to power plant
- contractValue and contractCurrency for financial tracking and cost recovery
- transactionStatus for workflow management (pending, confirmed, delivered, completed)
- Links to SalesDeliveryDocument for complete transaction documentation
- Supports both traditional biomass transactions and utility fuel purchases

--

## Core Entity: <span style="color: #1B4F72;">`EnergyCarbonData`</span>

- <span style="color: #1B4F72;">`energyCarbonDataId`</span>: Unique measurement ID
- <span style="color: #1B4F72;">`dataType`</span>: `energy_content`, `moisture`, `emissions`
- <span style="color: #1B4F72;">`value`</span>: Numeric measurement value
- <span style="color: #1B4F72;">`unit`</span>: `MJ/kg`, `percentage`, `kg_CO2e`
- <span style="color: #1B4F72;">`measurementDate`</span>: When measured
- <span style="color: #1B4F72;">`methodologyUsed`</span>: Testing standard

**Supports energy generation and emissions calculations**

Note:
- EnergyCarbonData stores all energy and carbon measurements throughout the supply chain
- dataType includes: moisture, energy_content, emissions, fuel_consumption, carbon_intensity
- unit supports various measurement types: percentage, MJ/kg, kg_CO2e, BTU/lb
- measurementDate and methodologyUsed for traceability and verification
- Links to TraceableUnit for biomass-specific measurements
- Critical for REC generation and utility compliance reporting
- Supports power generation efficiency calculations and emissions tracking

---

## Utility Program Entity: <span style="color: #1B4F72;">`ForestManagementActivity`</span>

- <span style="color: #1B4F72;">`activityId`</span>: Unique activity identifier
- <span style="color: #1B4F72;">`activityType`</span>: `fuel_reduction`, `forest_thinning`, `fire_prevention`
- <span style="color: #1B4F72;">`landOwnership`</span>: `federal`, `state`, `private`, `tribal`
- <span style="color: #1B4F72;">`treatmentObjective`</span>: Primary management goal
- <span style="color: #1B4F72;">`acresTreated`</span>: Area covered in acres
- <span style="color: #1B4F72;">`permitNumber`</span>: Regulatory permit reference

**Documents forest management and fire prevention activities**

Note:
- Purpose: Tracks forest management activities that generate biomass for utility programs
- activityType covers various management activities including fuel reduction treatments, forest thinning, and wildfire prevention projects
- landOwnership classification is critical for utility programs that prioritize certain land types
- treatmentObjective documents the primary forest management goal (fuel reduction, habitat improvement, forest health)
- acresTreated provides scale information for program impact assessment
- permitNumber links to regulatory permits (Cal Fire THP, NEPA, etc.)
- Relationships: Links to TraceableUnit for biomass generated and to Location for treatment areas

--

## Utility Program Entity: <span style="color: #1B4F72;">`Certificate`</span>

- <span style="color: #1B4F72;">`certificateId`</span>: Unique certificate ID
- <span style="color: #1B4F72;">`certificateType`</span>: `REC`, `sustainability_certification`
- <span style="color: #1B4F72;">`issuingOrganization`</span>: Certifying body
- <span style="color: #1B4F72;">`energyGenerated`</span>: MWh for REC certificates
- <span style="color: #1B4F72;">`generationDate`</span>: Power generation date
- <span style="color: #1B4F72;">`certificateStatus`</span>: `active`, `retired`, `transferred`

**Tracks Renewable Energy Certificates and sustainability certifications**

Note:
- Purpose: Manages REC certificates and sustainability certifications for utility biomass programs
- certificateType covers RECs, FSC certification, SFI certification, and other sustainability standards
- issuingOrganization identifies the certifying body (WREGIS, NAR, FSC, SFI, etc.)
- energyGenerated tracks MWh for REC calculation and compliance reporting
- generationDate links to specific power generation events
- certificateStatus tracks lifecycle from issuance through retirement
- Relationships: Links to Transaction for REC sales and to Organization for certificate ownership

---

## California Utility Example

**Biomass power generation scenario**

### Organization Profile
```json
{
  "organizationId": "sierra-biomass-power-001",
  "name": "Sierra Biomass Power LLC",
  "organizationType": "utility_generator",
  "facilityCapacity": {
    "ratedCapacity": 18,
    "unit": "MW",
    "fuelType": "forest_biomass"
  },
  "utilityPrograms": ["BioRAM", "RPS_compliance"]
}
```

Note:
- This demonstrates a real biomass power plant scenario using BOOST entities
- Organization shows utility generator with biomass-specific attributes
- Located in Northern California with 18 MW capacity using forest biomass
- Participates in CPUC BioRAM program and RPS compliance
- Contact information and operational status included in full organization profile

--

### Sample Fuel Supply Transactions

**Transaction 1**: 2,500 bone dry tons forest residue
- Source: Fuel reduction project, Plumas National Forest
- Treatment Type: `fuel_reduction`
- Energy Content: 18.5 GJ/BDT
- Power Generation: 1,250 MWh

**Transaction 2**: 1,800 bone dry tons mill residue  
- Source: Local sawmill processing operations
- Energy Content: 19.2 GJ/BDT
- Power Generation: 950 MWh

**Monthly Total**: 4,300 BDT, 2,200 MWh, 2,200 RECs

Note:
- Transaction 1 details: 2,500 bone dry tons from forest fuel reduction project
- Delivered from Plumas National Forest management activity on forest service land
- Transaction 2 details: 1,800 bone dry tons from mill residue
- Sourced from local sawmill processing operations
- Monthly totals demonstrate scale of biomass power generation
- REC generation: 1 REC per MWh of renewable electricity generated
- Energy content varies by biomass type and moisture content

--

### Utility Compliance Workflow

1. **Forest Activity Documentation**: Track management activities
2. **Biomass Sourcing**: Link fuel to forest treatments  
3. **Power Generation**: Monitor energy output and efficiency
4. **REC Generation**: Create and track renewable certificates
5. **Compliance Reporting**: Aggregate for CPUC and CARB submission

Note:
- Step 1: ForestManagementActivity entities track fuel reduction and forest thinning projects
- Step 2: Transaction entities link biomass fuel purchases to specific forest activities
- Step 3: EnergyCarbonData tracks power generation efficiency and emissions
- Step 4: Certificate entities create and manage REC generation and transfers
- Step 5: Compliance reporting aggregates data for CPUC BioRAM and CARB Cap-and-Trade
- This workflow demonstrates end-to-end utility compliance using BOOST data entities

---

## Utility Program Benefits: Generators

- Streamlined fuel sourcing documentation
- Automated REC tracking and transfer
- Forest treatment activity verification
- Compliance status monitoring

--

## Utility Program Benefits: CPUC

- Standardized biomass program data submission
- Enhanced verification of forest benefits  
- Improved data quality and consistency
- Reduced administrative processing overhead

--

## Utility Program Benefits: Supply Chain

- End-to-end traceability from forest to power generation
- Integration with forest management planning
- Supports multiple regulatory programs simultaneously

---

## Future Enhancement: Grid Integration

**Smart grid and renewable energy optimization**

### Real-Time Tracking
- <span style="color: #1B4F72;">`EnergyCarbonData`</span>: Live generation monitoring
- <span style="color: #1B4F72;">`Transaction`</span>: Dynamic fuel pricing  
- <span style="color: #D35400;">`GridIntegration`</span>: Grid stability support *(future)*

**Supporting California's renewable energy goals**

Note:
- BOOST's granular tracking enables real-time monitoring of biomass power generation
- Live generation monitoring through EnergyCarbonData enables grid operators to track renewable output
- Dynamic fuel pricing based on real-time availability and transportation costs
- GridIntegration entity (future enhancement) could track grid stability services provided by biomass plants
- Biomass provides dispatchable renewable energy that complements solar and wind
- Real-time fuel availability tracking helps grid operators plan renewable energy dispatch
- Integration with CAISO markets for renewable energy trading and grid services
- This supports California's SB 100 goals for 100% clean electricity by 2045

--

## Future Enhancement: Forest Management Optimization

**Data-driven forest treatment planning**

### Optimization Areas
- **Fuel Load Mapping**: Biomass availability forecasting
- **Treatment Prioritization**: Fire risk reduction impact
- **Transport Efficiency**: Optimal facility siting

**Enabling coordinated forest and energy planning**

Note:
- Fuel load mapping uses BOOST data to forecast biomass availability from planned treatments
- Treatment prioritization based on fire risk reduction and biomass energy potential
- Transport efficiency analysis for optimal siting of biomass facilities relative to treatment areas
- Coordination between Cal Fire treatment planning and utility fuel sourcing
- Integration with forest carbon offset projects and cap-and-trade programs
- Real-time monitoring of treatment effectiveness through before/after forest measurements
- Supply chain optimization reduces costs and increases program effectiveness
- Data-driven approach enables adaptive management based on actual outcomes

--

## Future Enhancement: Cross-Agency Integration

**Integrated regulatory reporting**

### Program Integration
- **Cal Fire THP**: Treatment permit integration
- **CARB Cap-and-Trade**: Emissions offset tracking
- **CPUC BioRAM**: Program compliance monitoring

**Streamlined multi-agency compliance**

Note:
- Cross-agency integration addresses current pain point where operators must manually reconcile data across multiple agency portals
- Cal Fire THP integration links treatment permits to biomass generation and utilization
- CARB Cap-and-Trade integration tracks forest carbon offsets and biomass emissions
- CPUC BioRAM program compliance monitoring with automated reporting
- Eliminates duplicate data entry across agency systems
- Reduces administrative burden on utilities and forest managers
- Enables coordinated policy implementation across agencies
- Supports California's integrated approach to climate and fire policy

--

## Thank You!