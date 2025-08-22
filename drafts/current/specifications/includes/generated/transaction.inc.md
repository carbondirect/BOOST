<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: transaction/validation_schema.json and transaction_dictionary.md
     To modify this content, edit the source file and regenerate -->

Transaction entity in BOOST data model

**[View Transaction in ERD Navigator](erd-navigator/index.html?focus=Transaction)**

### Relationships ### {{.unnumbered}}

- **OrganizationId** → [[#organization|Organization]] - Primary organization involved in transaction (seller/supplier)
- **CustomerId** → [[#customer|Customer]] - Customer organization (buyer) - uses EntityNameId convention referencing Customer entity
- **SalesDeliveryDocumentId** → [[#sales-delivery-document|Sales Delivery Document]] - Foreign key to sales/delivery documentation - uses EntityNameId convention referencing SalesDeliveryDocument
- **GeographicDataId** → [[#geographic-data|Geographic Data]] - Primary transaction location - uses EntityNameId convention referencing GeographicData
- **LcfsPathwayId** → [[#lcfs-pathway|Lcfs Pathway]] - CARB-certified pathway identifier for LCFS compliance - uses EntityNameId convention referencing LcfsPathway

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
<td>JSON-LD context defining semantic vocabulary mappings
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>Globally unique IRI identifying this specific entity instance
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>enum(Transaction)
<td>Entity type identifier for JSON-LD processing
<td>✓
</tr>
<tr>
<td><code>CustomerId</code>
<td>string (pattern)
<td>Customer organization (buyer) - uses EntityNameId convention referencing Customer entity
<td>✓
</tr>
<tr>
<td><code>OrganizationId</code>
<td>string (pattern)
<td>Primary organization involved in transaction (seller/supplier)
<td>✓
</tr>
<tr>
<td><code>contractCurrency</code>
<td>enum(9 values)
<td>Currency code for contract value
<td>✓
</tr>
<tr>
<td><code>contractValue</code>
<td>number (≥0, ≤999999999.99)
<td>Total monetary value of the transaction
<td>✓
</tr>
<tr>
<td><code>transactionDate</code>
<td>string (date)
<td>Date of business agreement
<td>✓
</tr>
<tr>
<td><code>transactionId</code>
<td>string (pattern)
<td>Unique identifier for the business transaction
<td>✓
</tr>
<tr>
<td><code>transactionStatus</code>
<td>enum(6 values)
<td>Current status of business transaction
<td>✓
</tr>
<tr>
<td><code>BioramPathwayId</code>
<td>string (pattern)
<td>BioRAM pathway identifier for biomass power generation - uses EntityNameId convention referencing BioramPathway
<td>
</tr>
<tr>
<td><code>BrokerOrganizationId</code>
<td>string | null
<td>Optional intermediary broker organization - uses EntityNameId convention referencing Organization
<td>
</tr>
<tr>
<td><code>GeographicDataId</code>
<td>string (pattern)
<td>Primary transaction location - uses EntityNameId convention referencing GeographicData
<td>
</tr>
<tr>
<td><code>LcfsPathwayId</code>
<td>string (pattern)
<td>CARB-certified pathway identifier for LCFS compliance - uses EntityNameId convention referencing LcfsPathway
<td>
</tr>
<tr>
<td><code>SalesDeliveryDocumentId</code>
<td>string (pattern)
<td>Foreign key to sales/delivery documentation - uses EntityNameId convention referencing SalesDeliveryDocument
<td>
</tr>
<tr>
<td><code>attestationDate</code>
<td>string (date)
<td>Date of BioRAM compliance attestation
<td>
</tr>
<tr>
<td><code>attestationSignatory</code>
<td>string
<td>Name and title of person attesting to BioRAM compliance
<td>
</tr>
<tr>
<td><code>biomassVolume</code>
<td>number (≥0)
<td>Volume of biomass fuel in transaction for BioRAM reporting
<td>
</tr>
<tr>
<td><code>biomassVolumeUnit</code>
<td>enum(bone_dry_tonnes, green_tonnes, cubic_yards)
<td>Unit of measurement for biomass volume
<td>
</tr>
<tr>
<td><code>bioramCertificationId</code>
<td>string
<td>BioRAM compliance certification identifier for transaction
<td>
</tr>
<tr>
<td><code>bioramEligible</code>
<td>boolean
<td>Whether transaction meets BioRAM program eligibility requirements
<td>
</tr>
<tr>
<td><code>calFirePermitNumber</code>
<td>string
<td>CAL FIRE permit number for harvest or treatment activities
<td>
</tr>
<tr>
<td><code>complianceRequirements</code>
<td>array&amp;lt;string&amp;gt;
<td>Regulatory compliance requirements for transaction
<td>
</tr>
<tr>
<td><code>contractSignedDate</code>
<td>string | null
<td>Date when contract was executed
<td>
</tr>
<tr>
<td><code>contractTerms</code>
<td>enum(8 values)
<td>Incoterms delivery conditions
<td>
</tr>
<tr>
<td><code>expectedDeliveryDate</code>
<td>string | null
<td>Expected completion/delivery date
<td>
</tr>
<tr>
<td><code>fhszVerificationSource</code>
<td>string
<td>Source of fire hazard zone verification (e.g., CAL_FIRE_2024_MAPS)
<td>
</tr>
<tr>
<td><code>financialTerms</code>
<td>object (structured)
<td>Detailed financial terms and conditions
<td>
</tr>
<tr>
<td><code>fireHazardSeverityZone</code>
<td>enum(4 values)
<td>CAL FIRE fire hazard severity zone designation
<td>
</tr>
<tr>
<td><code>fuelCategory</code>
<td>enum(10 values)
<td>Category of fuel for LCFS classification
<td>
</tr>
<tr>
<td><code>fuelOriginCoordinates</code>
<td>object (structured)
<td>Geographic coordinates of biomass fuel origin
<td>
</tr>
<tr>
<td><code>fuelOriginFacilityId</code>
<td>string
<td>Identifier for source facility or harvest site
<td>
</tr>
<tr>
<td><code>fuelType</code>
<td>enum(6 values)
<td>BioRAM eligible fuel type classification
<td>
</tr>
<tr>
<td><code>fuelVolume</code>
<td>number (≥0)
<td>Volume of fuel in transaction for LCFS reporting
<td>
</tr>
<tr>
<td><code>fuelVolumeUnit</code>
<td>enum(gallons, liters, GGE)
<td>Unit of measurement for fuel volume
<td>
</tr>
<tr>
<td><code>haulDistance</code>
<td>number (≥0)
<td>Transportation distance from source to facility in miles
<td>
</tr>
<tr>
<td><code>haulUnit</code>
<td>enum(miles, kilometers)
<td>Unit of measurement for haul distance
<td>
</tr>
<tr>
<td><code>landowner</code>
<td>string
<td>Legal landowner of biomass source location
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of last modification
<td>
</tr>
<tr>
<td><code>manipulationTimestamps</code>
<td>array&amp;lt;string&amp;gt;
<td>Processing step timestamps
<td>
</tr>
<tr>
<td><code>materialEligibilityConfirmed</code>
<td>boolean
<td>Confirmation that material meets BioRAM eligibility criteria
<td>
</tr>
<tr>
<td><code>mediaBreaksDetected</code>
<td>array&amp;lt;boolean&amp;gt;
<td>Continuity flags per TRU
<td>
</tr>
<tr>
<td><code>parcelId</code>
<td>string
<td>Assessor parcel number or legal land description
<td>
</tr>
<tr>
<td><code>paymentTerms</code>
<td>string
<td>Payment conditions and timeline
<td>
</tr>
<tr>
<td><code>permitStatus</code>
<td>enum(4 values)
<td>Status of required permits for biomass harvesting
<td>
</tr>
<tr>
<td><code>reconciliationStatus</code>
<td>enum(pending, resolved, disputed)
<td>Transaction reconciliation status
<td>
</tr>
<tr>
<td><code>regulatedPartyRole</code>
<td>enum(5 values)
<td>Role of regulated party in LCFS transaction
<td>
</tr>
<tr>
<td><code>reportingAccuracyConfirmed</code>
<td>boolean
<td>Confirmation of reporting data accuracy for BioRAM compliance
<td>
</tr>
<tr>
<td><code>reportingPeriod</code>
<td>string (pattern)
<td>LCFS reporting quarter in YYYY-QN format
<td>
</tr>
<tr>
<td><code>riskManagement</code>
<td>object (structured)
<td>Risk management and mitigation terms
<td>
</tr>
<tr>
<td><code>speciesCompositionAtTransaction</code>
<td>array&amp;lt;object&amp;gt;
<td>Species breakdown at transaction time
<td>
</tr>
<tr>
<td><code>timberHarvestPlan</code>
<td>string
<td>Timber harvest plan identifier if applicable
<td>
</tr>
<tr>
<td><code>traceableUnitIds</code>
<td>array&amp;lt;string&amp;gt;
<td>TRUs included in this transaction
<td>
</tr>
<tr>
<td><code>trackingPointIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Location trail references
<td>
</tr>
<tr>
<td><code>withinSRA</code>
<td>boolean
<td>Whether fuel source is within California State Responsibility Area
<td>
</tr>
</tbody>
</table>

## Transaction
### Overview
The `Transaction` entity manages comprehensive business transactions within the BOOST traceability system. Transactions represent formal business agreements for the transfer of biomass materials, wood products, or energy feedstocks between organizations. This entity integrates financial management, regulatory compliance, supply chain traceability, risk management, and contract administration to support complete transaction lifecycle management across complex supply chain operations.
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
<td>`transactionId`
<td>string
<td>Yes
<td>Unique identifier for the business transaction (primary key)
<td>`TXN-001`, `TXN-PACIFIC-2024-001`
</tr>
<tr>
<td>`OrganizationId`
<td>string (FK)
<td>Yes
<td>Primary organization involved in transaction (seller/supplier)
<td>`ORG-PACIFIC-FOREST-001`, `ORG-KLAMATH-HARVEST`
</tr>
<tr>
<td>`CustomerId`
<td>string (FK)
<td>Yes
<td>Customer organization (buyer)
<td>`CUST-GREEN-ENERGY-CORP`, `CUST-PACIFIC-PAPER-MILLS`
</tr>
<tr>
<td>`transactionDate`
<td>string (date)
<td>Yes
<td>Date of business agreement
<td>`2024-03-15`, `2024-07-22`
</tr>
<tr>
<td>`SalesDeliveryDocumentId`
<td>string (FK)
<td>No
<td>Foreign key to sales/delivery documentation
<td>`SDD-PACIFIC-DELIVERY-2024-001`, `SDD-BIOMASS-SHIPMENT-789`
</tr>
<tr>
<td>`contractValue`
<td>number
<td>Yes
<td>Total monetary value of the transaction
<td>`125000.00`, `2500000.50`, `850000.00`
</tr>
<tr>
<td>`contractCurrency`
<td>string
<td>Yes
<td>Currency code for contract value (enum)
<td>`USD`, `EUR`, `CAD`, `GBP`
</tr>
<tr>
<td>`contractTerms`
<td>string
<td>No
<td>Incoterms delivery conditions (enum)
<td>`FOB`, `CIF`, `DDP`, `EXW`, `FCA`
</tr>
<tr>
<td>`paymentTerms`
<td>string
<td>No
<td>Payment conditions and timeline
<td>`Net 30 days`, `50% down, balance on delivery`, `Letter of credit`
</tr>
<tr>
<td>`transactionStatus`
<td>string
<td>Yes
<td>Current status of business transaction (enum)
<td>`pending`, `confirmed`, `delivered`, `completed`, `cancelled`
</tr>
<tr>
<td>`GeographicDataId`
<td>string (FK)
<td>No
<td>Primary transaction location
<td>`GEO-MILL-ENTRANCE-001`, `GEO-PORT-EXPORT-TERMINAL`
</tr>
<tr>
<td>`BrokerOrganizationId`
<td>string (FK)
<td>No
<td>Optional intermediary broker organization
<td>`ORG-TIMBER-BROKER-PACIFIC`, `ORG-BIOMASS-TRADING-001`
</tr>
<tr>
<td>`contractSignedDate`
<td>string (date)
<td>No
<td>Date when contract was executed
<td>`2024-03-10`, `2024-07-18`
</tr>
<tr>
<td>`expectedDeliveryDate`
<td>string (date)
<td>No
<td>Expected completion/delivery date
<td>`2024-04-15`, `2024-08-30`
</tr>
<tr>
<td>`complianceRequirements`
<td>array&lt;string&gt;
<td>No
<td>Regulatory compliance requirements for transaction
<td>`["FSC_Chain_of_Custody", "LCFS_Reporting", "SBP_DTS_Registration"]`
</tr>
<tr>
<td>`LcfsPathwayId`
<td>string (FK)
<td>No
<td>CARB-certified pathway identifier for LCFS compliance
<td>`CA-RD-001-Tier1-Bio`, `CA-ET-002-LookupTable`
</tr>
<tr>
<td>`fuelVolume`
<td>number
<td>No
<td>Volume of fuel in transaction for LCFS reporting
<td>`50000.0`, `125000.5`, `2500000.0`
</tr>
<tr>
<td>`fuelVolumeUnit`
<td>string
<td>No
<td>Unit of measurement for fuel volume (enum)
<td>`gallons`, `liters`, `GGE`
</tr>
<tr>
<td>`fuelCategory`
<td>string
<td>No
<td>Category of fuel for LCFS classification (enum)
<td>`renewable_diesel`, `ethanol`, `sustainable_aviation_fuel`, `biodiesel`
</tr>
<tr>
<td>`reportingPeriod`
<td>string
<td>No
<td>LCFS reporting quarter in YYYY-QN format
<td>`2024-Q1`, `2024-Q3`, `2025-Q2`
</tr>
<tr>
<td>`regulatedPartyRole`
<td>string
<td>No
<td>Role of regulated party in LCFS transaction (enum)
<td>`producer`, `importer`, `blender`, `distributor`
</tr>
<tr>
<td>`traceableUnitIds`
<td>array&lt;string&gt;
<td>No
<td>TRUs included in this transaction
<td>`["TRU-LOG-001", "TRU-PILE-002", "TRU-BATCH-003"]`
</tr>
<tr>
<td>`reconciliationStatus`
<td>string
<td>No
<td>Transaction reconciliation status (enum)
<td>`pending`, `resolved`, `disputed`
</tr>
<tr>
<td>`trackingPointIds`
<td>array&lt;string&gt;
<td>No
<td>Location trail references
<td>`["TP-HARVEST-001", "TP-FOREST-ROAD-002", "TP-MILL-ENTRANCE-003"]`
</tr>
<tr>
<td>`speciesCompositionAtTransaction`
<td>array&lt;object&gt;
<td>No
<td>Species breakdown at transaction time
<td>`[{"species": "Douglas Fir", "percentage": 65.0}, {"species": "Hemlock", "percentage": 35.0}]`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/transaction/TXN-001`
</tr>
</tbody>
</table>
### Transaction Status Workflow
1. **pending**
    - Initial transaction creation and negotiation phase
    - Contract terms under discussion
    - Awaiting final approvals and signatures
    - No material transfer or payment processing
2. **confirmed**
    - Contract signed and terms finalized
    - Transaction authorized for execution
    - Material preparation and logistics coordination
    - Payment processing initiated according to terms
3. **delivered**
    - Materials physically delivered to customer
    - Delivery documentation completed and verified
    - Quality inspection and acceptance procedures
    - Awaiting final payment and transaction closure
4. **completed**
    - All contract obligations fulfilled
    - Payment processed and received
    - Documentation finalized and archived
    - Transaction closed with full compliance
5. **cancelled**
    - Transaction terminated before completion
    - Cancellation terms and penalties applied
    - Partial deliveries and payments reconciled
    - Documentation updated for audit trail
6. **disputed**
    - Transaction issues under dispute resolution
    - Quality, quantity, or delivery discrepancies
    - Legal or arbitration proceedings active
    - Resolution pending with partial execution
### Financial Terms Management
1. **Contract Value Structure**
    - Base price per unit or total contract value
    - Currency specification and exchange rate handling
    - Price adjustments for quality variations
    - Volume-based pricing tiers and discounts
2. **Payment Terms**
    - Payment schedule and milestone requirements
    - Down payment and progress payment structures
    - Payment methods and processing procedures
    - Late payment penalties and interest charges
3. **Risk Management**
    - Force majeure clauses and conditions
    - Quality guarantees and performance bonds
    - Insurance requirements and coverage
    - Dispute resolution mechanisms and procedures
4. **Financial Controls**
    - Credit limits and approval authorities
    - Payment security and collateral requirements
    - Multi-currency transaction management
    - Financial reporting and audit trail requirements
### LCFS Compliance Integration
1. **Pathway Management**
    - CARB-certified pathway identification and validation
    - Carbon intensity value assignment and tracking
    - Energy economy ratio calculations
    - Regulatory benchmark comparison and compliance
2. **Fuel Classification**
    - Renewable fuel category determination
    - Advanced biofuel qualification assessment
    - Low carbon fuel standard compliance verification
    - California Air Resources Board reporting requirements
3. **Credit Calculations**
    - LCFS credit generation calculations
    - Fuel volume and energy content verification
    - Lifecycle emission reductions quantification
    - Quarterly reporting aggregation and submission
4. **Regulated Party Compliance**
    - Producer, importer, blender role identification
    - Compliance obligation calculation and tracking
    - Credit trading and banking system integration
    - Annual compliance demonstration requirements
### Supply Chain Integration
1. **TRU Traceability**
    - Complete traceable unit inclusion and tracking
    - Species composition documentation and verification
    - Processing history and transformation tracking
    - Quality specifications and grade compliance
2. **Tracking Point Coordination**
    - Multi-point location tracking and verification
    - Chain of custody maintenance across locations
    - Continuous tracking validation
    - Geographic verification and compliance
3. **Processing Integration**
    - Material processing coordination and scheduling
    - Quality control and specification compliance
    - Volume reconciliation and measurement validation
    - Processing facility integration and coordination
4. **Documentation Management**
    - Sales and delivery document coordination
    - Certificate and compliance documentation
    - Audit trail maintenance and verification
    - Regulatory reporting and submission coordination
### Example Use Cases
1. **Renewable Diesel Feedstock Transaction**
    - Transaction: Large-scale used cooking oil supply contract
    - LCFS Compliance: Tier 1 pathway with verified carbon intensity
    - Financial Terms: $2.5M contract with quarterly deliveries
    - Traceability: Complete supply chain documentation from collection to processing
    - Compliance: CARB LCFS reporting with verified sustainability claims
2. **Export Lumber Transaction**
    - Transaction: Container shipment of certified lumber to international customer
    - Certification: FSC Chain of Custody with species-specific claims
    - Financial Terms: Letter of credit with FOB shipping terms
    - Traceability: Individual log tracking from forest to port
    - Compliance: Phytosanitary certification and export documentation
3. **Biomass Energy Supply Agreement**
    - Transaction: Long-term biomass fuel supply contract
    - SBP Compliance: Sustainable biomass partnership verification
    - Financial Terms: Multi-year agreement with price escalation clauses
    - Traceability: Supply base reporting and mass balance tracking
    - Compliance: Regional risk assessment and mitigation measures
### Validation Rules
1. **Transaction Requirements**
    - transactionId must be unique across system
    - OrganizationId and CustomerId must reference valid entities
    - contractValue must be positive number
    - transactionStatus must follow valid workflow progression
2. **Financial Consistency**
    - contractCurrency must be supported currency code
    - Payment terms must be realistic and enforceable
    - Contract value must align with material quantities and market rates
    - Financial terms must comply with applicable regulations
3. **LCFS Integration**
    - LcfsPathwayId must reference valid CARB-certified pathway
    - Fuel category must align with pathway feedstock specifications
    - Fuel volume must be consistent with TRU quantities
    - Reporting period must be current or future quarter
4. **Supply Chain Consistency**
    - traceableUnitIds must reference valid TRUs available for transaction
    - trackingPointIds must represent logical supply chain progression
    - Species composition must align with TRU species data
    - Geographic locations must be consistent with operational areas
### Relationships
- Transaction between one Organization (seller) and one Customer (buyer)
- Transaction may involve one Broker Organization for intermediary services
- Transaction documented by one SalesDeliveryDocument
- Transaction conducted at one primary GeographicData location
- Transaction includes multiple TraceableUnits for material transfer
- Transaction tracked through multiple TrackingPoints for chain of custody
- Transaction may reference one LCFSPathway for regulatory compliance
- Transaction enables reconciliation through DataReconciliation processes
