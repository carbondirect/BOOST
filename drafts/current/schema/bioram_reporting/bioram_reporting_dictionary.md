# BioramReporting

## BioramReporting

### Overview
The `BioramReporting` entity represents quarterly compliance reports submitted by biomass power generation facilities participating in California's Bioenergy Renewable Auction Mechanism (BioRAM) program. Each report aggregates fuel sourcing data, tracks efficiency performance against contract targets, and demonstrates compliance with fire hazard reduction and renewable energy objectives.

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
<td>`reportingId`
<td>string
<td>Yes
<td>Unique identifier for quarterly BioRAM report (primary key)
<td>`BIORAM-RPT-2025-Q3-SHWD001`
</tr>
<tr>
<td>`facilityEntityId`
<td>string (FK)
<td>Yes
<td>Reference to biomass facility Organization entity
<td>`ORG-SHERWOOD-POWER-001`
</tr>
<tr>
<td>`bioramContractId`
<td>string
<td>No
<td>BioRAM contract identifier from competitive procurement
<td>`BR-RFO-2024-01-A`
</tr>
<tr>
<td>`reportingPeriod`
<td>string
<td>Yes
<td>Reporting quarter in YYYY-QN format
<td>`2025-Q3`, `2025-Q4`, `2026-Q1`
</tr>
<tr>
<td>`totalBiomassVolume`
<td>number
<td>Yes
<td>Total biomass fuel consumed in bone dry tonnes
<td>`3500.0`, `2800.5`, `4200.3`
</tr>
<tr>
<td>`totalEnergyGenerated`
<td>number
<td>Yes
<td>Total electrical energy generated in MWh
<td>`2800.0`, `2240.4`, `3360.2`
</tr>
<tr>
<td>`overallEfficiency`
<td>number
<td>Yes
<td>Overall facility efficiency (fraction)
<td>`0.36`, `0.38`, `0.34`
</tr>
<tr>
<td>`efficiencyTarget`
<td>number
<td>No
<td>Contract efficiency target for BioRAM compliance
<td>`0.35`, `0.37`, `0.32`
</tr>
<tr>
<td>`complianceStatus`
<td>string (enum)
<td>Yes
<td>Overall BioRAM compliance status for reporting period
<td>`compliant`, `efficiency_shortfall`, `sourcing_violation`
</tr>
<tr>
<td>`submissionDate`
<td>string (date-time)
<td>No
<td>Date and time report was submitted to CEC
<td>`2025-10-15T14:30:00Z`
</tr>
<tr>
<td>`verificationDate`
<td>string (date-time)
<td>No
<td>Date of independent verification completion
<td>`2025-10-10T16:45:00Z`
</tr>
<tr>
<td>`verificationRequired`
<td>boolean
<td>No
<td>Whether third-party verification is required
<td>`true`, `false`
</tr>
<tr>
<td>`VerificationStatementId`
<td>string (FK)
<td>No
<td>Reference to VerificationStatement for independent verification
<td>`VS-BIORAM-2025-Q3-001`
</tr>
<tr>
<td>`reportingDeadline`
<td>string (date)
<td>No
<td>CEC deadline for BioRAM report submission
<td>`2025-10-31`, `2026-01-31`
</tr>
<tr>
<td>`transactionIds`
<td>array&lt;string&gt;
<td>No
<td>Transaction entity IDs for fuel procurement included in report
<td>`["TXN-BIORAM-2025-001", "TXN-BIORAM-2025-002"]`
</tr>
<tr>
<td>`fuelSourcingSummary`
<td>object
<td>No
<td>Summary of fuel sourcing compliance metrics
<td>Comprehensive fuel sourcing breakdown and compliance analysis
</tr>
<tr>
<td>`performanceMetrics`
<td>object
<td>No
<td>Facility performance and grid contribution metrics
<td>Capacity factor, availability, grid reliability contributions
</tr>
<tr>
<td>`environmentalImpact`
<td>object
<td>No
<td>Environmental and fire hazard reduction benefits
<td>CO2 reduction, fire risk mitigation, waste reduction metrics
</tr>
<tr>
<td>`financialSummary`
<td>object
<td>No
<td>Financial performance and cost metrics
<td>Contract values, fuel costs, pricing per MWh and BDT
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/bioram-reporting/BIORAM-RPT-2025-Q3-SHWD001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of most recent report update
<td>`2025-10-15T16:22:00Z`
</tr>
</tbody>
</table>

### Business Rules

#### Fuel Sourcing Requirements
- **Fire Hazard Zone Priority**: Preference for materials from Very High and High fire hazard severity zones
- **Geographic Scope**: Primary sourcing from State Responsibility Areas (SRA)
- **Haul Distance Limits**: Economic constraints on transportation distances
- **Supplier Diversity**: Encouragement of multiple fuel suppliers for supply security

#### Efficiency Standards
- Minimum efficiency thresholds established in competitive procurement contracts
- Measured as net electrical output divided by fuel energy input (HHV basis)
- Performance tracking against contracted efficiency targets
- Penalties for persistent efficiency shortfalls

#### Compliance Verification
- Quarterly reporting with annual independent verification for larger facilities
- Fuel sourcing documentation through BOOST supply chain tracking
- Energy generation verification through grid interconnection metering
- Fire hazard zone verification through CAL FIRE geographic data

#### Environmental Benefits Tracking
- CO2 emission reductions compared to fossil fuel baseline
- Fire risk mitigation through strategic fuel removal
- Waste biomass diversion from landfills and open burning
- Grid reliability contributions during peak demand periods

### Fuel Sourcing Summary Object

The `fuelSourcingSummary` object contains:

- **totalSuppliers**: Number of unique fuel suppliers
- **averageHaulDistance**: Average transportation distance in miles
- **fireHazardZoneBreakdown**: Volume breakdown by CAL FIRE hazard severity zones
- **fuelTypeBreakdown**: Array of fuel type consumption with volumes, percentages, and pathway references

### Performance Metrics Object

The `performanceMetrics` object includes:

- **capacityFactor**: Facility capacity utilization for the reporting period
- **availabilityFactor**: Facility uptime and availability metrics
- **fuelUtilizationRate**: Efficiency of fuel consumption
- **gridReliabilityContribution**: Peak hour generation and grid stabilization services

### Environmental Impact Object

The `environmentalImpact` object tracks:

- **co2Reduction**: CO2 emission reductions in metric tons
- **fireRiskMitigation**: Acres treated and firebreak contributions
- **wasteReduction**: Biomass waste diverted from disposal

### Financial Summary Object

The `financialSummary` object contains:

- **totalContractValue**: BioRAM contract payments for the period
- **fuelCosts**: Total fuel procurement expenses
- **averageFuelPrice**: Average cost per bone dry tonne
- **contractPricePerMWh**: BioRAM contract price per megawatt-hour

### Relationships

This entity supports relationships with:
- **Organization**: Via `facilityEntityId` foreign key to biomass power facilities
- **Transaction**: Via `transactionIds` array to fuel procurement transactions
- **VerificationStatement**: Via `VerificationStatementId` for independent verification
- **BioramPathway**: Through pathway references in fuel type breakdown

### Implementation Notes

BioRAM reporting integrates with California's renewable energy and fire prevention policies by:
- Supporting utility-scale renewable energy procurement
- Incentivizing strategic fuel reduction in high fire hazard areas
- Tracking grid reliability contributions during peak demand
- Documenting environmental benefits and CO2 emission reductions
- Ensuring fuel sourcing transparency through BOOST supply chain tracking

The reporting framework enables the California Energy Commission to monitor program effectiveness, verify compliance with procurement contracts, and assess environmental and fire prevention benefits achieved through the BioRAM competitive procurement process.
