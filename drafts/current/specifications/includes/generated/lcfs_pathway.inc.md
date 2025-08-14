<!-- Auto-generated from lcfs_pathway/validation_schema.json -->

CARB-certified fuel pathway for LCFS compliance with carbon intensity and regulatory attributes

**[View LCFS Pathway in ERD Navigator](erd-navigator/index.html?focus=LcfsPathway)**

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
<td>Unique URI identifier for JSON-LD
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>caGreetVersion</code>
<td>string (pattern)
<td>CA-GREET model version used for pathway certification
<td>✓
</tr>
<tr>
<td><code>carbonIntensity</code>
<td>number (≥0, ≤200)
<td>Certified carbon intensity in gCO2e/MJ
<td>✓
</tr>
<tr>
<td><code>certificationDate</code>
<td>string (date)
<td>CARB pathway certification date
<td>✓
</tr>
<tr>
<td><code>energyEconomyRatio</code>
<td>number (≥0.5, ≤3.0)
<td>Energy economy ratio multiplier for credit calculation
<td>✓
</tr>
<tr>
<td><code>facilityLocation</code>
<td>string
<td>Production facility location (city, state or geographic region)
<td>✓
</tr>
<tr>
<td><code>feedstockCategory</code>
<td>enum(13 values)
<td>Primary feedstock type for pathway
<td>✓
</tr>
<tr>
<td><code>fuelProduct</code>
<td>enum(8 values)
<td>Final fuel product produced
<td>✓
</tr>
<tr>
<td><code>pathwayId</code>
<td>string (pattern)
<td>CARB-assigned pathway identifier
<td>✓
</tr>
<tr>
<td><code>pathwayType</code>
<td>enum(Lookup_Table, Tier_1, Tier_2)
<td>CARB pathway certification tier
<td>✓
</tr>
<tr>
<td><code>verificationStatus</code>
<td>enum(4 values)
<td>Current CARB verification status
<td>✓
</tr>
<tr>
<td><code>expirationDate</code>
<td>string (date)
<td>Pathway certification expiration date
<td>
</tr>
<tr>
<td><code>facilityCapacity</code>
<td>number (≥0)
<td>Annual production capacity in gallons
<td>
</tr>
<tr>
<td><code>geographicScope</code>
<td>enum(4 values)
<td>Geographic applicability of pathway
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of most recent pathway data update
<td>
</tr>
<tr>
<td><code>processDescription</code>
<td>string
<td>Brief description of production process
<td>
</tr>
</tbody>
</table>

## LCFSPathway
### Overview
The `LCFSPathway` entity represents CARB-certified fuel pathways for California's Low Carbon Fuel Standard (LCFS) compliance. Each pathway defines the carbon intensity, feedstock type, production process, and regulatory status for specific fuel production routes. This entity enables LCFS credit calculations and regulatory reporting by linking transactions to certified carbon intensities.
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
<td>`pathwayId`
<td>string
<td>Yes
<td>CARB-assigned pathway identifier (primary key)
<td>`CA-RD-2025-LMR-001`, `CA-ET-2025-CRN-042`
</tr>
<tr>
<td>`pathwayType`
<td>string (enum)
<td>Yes
<td>CARB pathway certification tier
<td>`Lookup_Table`, `Tier_1`, `Tier_2`
</tr>
<tr>
<td>`feedstockCategory`
<td>string (enum)
<td>Yes
<td>Primary feedstock type for pathway
<td>`logging_and_mill_residue`, `corn`, `algae`
</tr>
<tr>
<td>`fuelProduct`
<td>string (enum)
<td>Yes
<td>Final fuel product produced
<td>`renewable_diesel`, `ethanol`, `biodiesel`
</tr>
<tr>
<td>`facilityLocation`
<td>string
<td>Yes
<td>Production facility location
<td>`Stockton, CA`, `Iowa`, `Western_US`
</tr>
<tr>
<td>`carbonIntensity`
<td>number
<td>Yes
<td>Certified carbon intensity in gCO2e/MJ
<td>`19.85`, `74.32`, `12.41`
</tr>
<tr>
<td>`energyEconomyRatio`
<td>number
<td>Yes
<td>Energy economy ratio multiplier for credit calculation
<td>`1.0`, `1.5`, `2.0`
</tr>
<tr>
<td>`certificationDate`
<td>string (date)
<td>Yes
<td>CARB pathway certification date
<td>`2025-01-15`
</tr>
<tr>
<td>`expirationDate`
<td>string (date)
<td>No
<td>Pathway certification expiration date
<td>`2028-01-15`
</tr>
<tr>
<td>`verificationStatus`
<td>string (enum)
<td>Yes
<td>Current CARB verification status
<td>`active`, `suspended`, `expired`
</tr>
<tr>
<td>`caGreetVersion`
<td>string
<td>Yes
<td>CA-GREET model version used for certification
<td>`3.0`, `2.1`
</tr>
<tr>
<td>`facilityCapacity`
<td>number
<td>No
<td>Annual production capacity in gallons
<td>`50000000`, `125000000`
</tr>
<tr>
<td>`processDescription`
<td>string
<td>No
<td>Brief description of production process
<td>`Hydrotreated renewable diesel production`
</tr>
<tr>
<td>`geographicScope`
<td>string (enum)
<td>No
<td>Geographic applicability of pathway
<td>`California`, `Western_US`, `National`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/lcfs-pathway/CA-RD-2025-LMR-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of most recent pathway data update
<td>`2025-07-21T14:30:00Z`
</tr>
</tbody>
</table>
---
### Key Features
1. **CARB Pathway Integration**
     Direct mapping to official CARB pathway database
     Standardized pathway ID format validation
     Certification tier tracking (Lookup Table, Tier 1, Tier 2)
2. **Carbon Intensity Tracking**
     Certified CI values from CA-GREET modeling
     Energy Economy Ratio for electric vehicle pathways
     Regulatory benchmark comparison support
3. **Feedstock Classification**
     Comprehensive feedstock categories for all LCFS fuel types
     Forest biomass subcategories for waste vs. purpose-grown materials
     Integration with BOOST material tracking entities
4. **Regulatory Compliance**
     Active/suspended/expired status tracking
     Certification and expiration date management
     CA-GREET version compatibility
### Example Use Cases
1. **Renewable Diesel from Forest Residue**
     Pathway Type: Tier_1
     Feedstock: logging_and_mill_residue
     Carbon Intensity: 19.85 gCO2e/MJ
     Energy Economy Ratio: 1.0
2. **Ethanol from Corn**
     Pathway Type: Lookup_Table
     Feedstock: corn
     Carbon Intensity: 74.32 gCO2e/MJ
     Energy Economy Ratio: 1.0
3. **Sustainable Aviation Fuel**
     Pathway Type: Tier_2
     Feedstock: used_cooking_oil
     Carbon Intensity: 12.41 gCO2e/MJ
     Energy Economy Ratio: 1.0
### Relationships
- LCFSPathway referenced by Transaction entities for LCFS reporting
- LCFSPathway linked to EnergyCarbonData for detailed carbon accounting
- LCFSPathway used in LCFSReporting for quarterly submissions
- LCFSPathway connected to Organization entities for pathway ownership
- LCFSPathway integrated with TraceableUnit for feedstock traceability
### Credit Calculation Formula
LCFS credits are calculated using pathway data:
```
Credits = (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER
```
Where:
- **Benchmark_CI**: Annual regulatory benchmark (95.61 for gasoline, 98.47 for diesel)
- **Pathway_CI**: `carbonIntensity` field value
- **Fuel_Volume_MJ**: Fuel volume converted to megajoules
- **EER**: `energyEconomyRatio` field value
### Validation Rules
- Pathway IDs must follow CARB format: `CA-{FUEL}-{YEAR}-{FEEDSTOCK}-{NUMBER}`
- Carbon intensity must be positive and typically under 200 gCO2e/MJ
- Energy Economy Ratio typically ranges from 0.5 to 3.0
- Certification dates must precede expiration dates
- Active pathways must have future expiration dates
