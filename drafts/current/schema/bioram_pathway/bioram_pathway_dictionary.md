# BioramPathway

## BioramPathway

### Overview
The `BioramPathway` entity represents California Energy Commission (CEC) certified pathways for the Bioenergy Renewable Auction Mechanism (BioRAM) program. Each pathway defines fuel type classifications, efficiency standards, and geographic eligibility criteria for biomass power generation facilities participating in the BioRAM competitive procurement process.

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
<td>BioRAM pathway identifier (primary key)
<td>`BIORAM-PWR-2025-LMR-001`, `BIORAM-PWR-2025-FHR-002`
</tr>
<tr>
<td>`fuelType`
<td>string (enum)
<td>Yes
<td>BioRAM eligible fuel type classification
<td>`lumber_mill_residual`, `forest_harvest_residual`, `agricultural_residue`
</tr>
<tr>
<td>`targetFacilityType`
<td>string (enum)
<td>Yes
<td>Type of facility this pathway applies to
<td>`biomass_power_plant`, `biogas_facility`, `combined_heat_power`
</tr>
<tr>
<td>`efficiencyStandard`
<td>number
<td>Yes
<td>Minimum efficiency requirement for BioRAM eligibility (fraction)
<td>`0.35`, `0.40`, `0.25`
</tr>
<tr>
<td>`carbonIntensity`
<td>number
<td>Yes
<td>Carbon intensity in gCO2e/MJ for biomass fuel
<td>`15.2`, `18.4`, `22.1`
</tr>
<tr>
<td>`geographicScope`
<td>string (enum)
<td>No
<td>Geographic applicability within State Responsibility Areas
<td>`California_SRA`, `California_Statewide`, `Western_States`
</tr>
<tr>
<td>`fireHazardZoneEligibility`
<td>array&lt;string&gt;
<td>No
<td>Eligible CAL FIRE hazard severity zones
<td>`["Very High", "High"]`, `["High", "Moderate"]`
</tr>
<tr>
<td>`certificationDate`
<td>string (date)
<td>Yes
<td>CEC BioRAM pathway certification date
<td>`2025-01-15`, `2024-11-30`
</tr>
<tr>
<td>`expirationDate`
<td>string (date)
<td>No
<td>Pathway certification expiration date
<td>`2030-01-15`, `2029-11-30`
</tr>
<tr>
<td>`eligibilityStatus`
<td>string (enum)
<td>Yes
<td>Current CEC eligibility status
<td>`active`, `suspended`, `expired`, `pending_approval`
</tr>
<tr>
<td>`cecVersion`
<td>string
<td>No
<td>CEC BioRAM program version used for certification
<td>`2.1`, `2.0`, `1.5`
</tr>
<tr>
<td>`haulDistanceLimit`
<td>number
<td>No
<td>Maximum economical haul distance in miles
<td>`75`, `100`, `50`
</tr>
<tr>
<td>`seasonalAvailability`
<td>object
<td>No
<td>Seasonal fuel availability characteristics
<td>`{"peakSeason": "fire_season", "availabilityFactor": 0.8}`
</tr>
<tr>
<td>`sourceRegion`
<td>string
<td>No
<td>Primary source region or forest management unit
<td>`Northern California`, `Sierra Nevada`, `Central Valley`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/bioram-pathway/BIORAM-PWR-2025-LMR-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of most recent pathway data update
<td>`2025-03-15T10:30:00Z`
</tr>
</tbody>
</table>

### Business Rules

#### Fuel Type Classifications
- **lumber_mill_residual**: Wood chips, sawdust, and bark from lumber processing
- **forest_harvest_residual**: Slash, tops, and limbs from timber harvesting operations  
- **agricultural_residue**: Orchard prunings, vineyard cuttings, and crop residues
- **urban_wood_waste**: Tree trimmings and construction/demolition wood
- **construction_demolition_wood**: Clean, untreated wood from C&amp;D activities

#### Efficiency Standards
- Minimum efficiency thresholds vary by fuel type and facility size
- Measured as net electrical output divided by fuel energy input
- Must be verified through independent performance testing

#### Geographic Eligibility
- Primary focus on State Responsibility Areas (SRA) for fire hazard reduction
- Extended eligibility for facilities serving grid reliability needs
- Transportation distances factored into economic viability assessments

#### Fire Hazard Zone Integration
- Preference for materials sourced from Very High and High fire hazard severity zones
- Supports CAL FIRE fuel reduction and forest management objectives
- Seasonal procurement timing aligned with fire prevention activities

### Relationships

This entity supports relationships with:
- **Transaction**: Via `bioramPathwayId` foreign key references
- **Organization**: Facilities certified under specific pathways
- **GeographicData**: Source regions and facility locations
- **BioramReporting**: Pathway performance aggregation

### Implementation Notes

BioRAM pathways are established through the California Energy Commission's renewable energy procurement processes and integrate with:
- CAL FIRE fire hazard severity zone mapping
- Forest management and fuel reduction planning
- Utility-scale renewable energy contracting
- Grid reliability and resource adequacy planning

The pathway certification process considers fuel availability, transportation logistics, facility efficiency, and environmental benefits in determining BioRAM program eligibility and competitive positioning.
