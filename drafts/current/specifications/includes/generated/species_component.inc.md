<!-- Auto-generated from species_component/validation_schema.json -->

Species composition within TRUs

**[View Species Component in ERD Navigator](erd-navigator/index.html?focus=SpeciesComponent)**

### Relationships ### {{.unnumbered}}

- **traceableUnitId** → [[#traceable-unit|Traceable Unit]] - Foreign key back reference to TraceableUnit

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
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>enum(SpeciesComponent)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>componentId</code>
<td>string (pattern)
<td>Unique identifier for the species component
<td>✓
</tr>
<tr>
<td><code>percentageByVolume</code>
<td>number (≥0, ≤100)
<td>Percentage of total TRU volume for this species
<td>✓
</tr>
<tr>
<td><code>species</code>
<td>string
<td>Species name (common or scientific)
<td>✓
</tr>
<tr>
<td><code>traceableUnitId</code>
<td>string (pattern)
<td>Foreign key back reference to TraceableUnit
<td>✓
</tr>
<tr>
<td><code>volumeM3</code>
<td>number (≥0)
<td>Volume of this species within the TRU in cubic meters
<td>✓
</tr>
<tr>
<td><code>ageYears</code>
<td>integer
<td>Estimated age in years
<td>
</tr>
<tr>
<td><code>carbonStorage</code>
<td>string
<td>CO2 data for this species component
<td>
</tr>
<tr>
<td><code>dbhCm</code>
<td>number (≥0)
<td>Diameter at breast height in centimeters
<td>
</tr>
<tr>
<td><code>defects</code>
<td>array&amp;lt;string&amp;gt;
<td>List of defects or quality issues
<td>
</tr>
<tr>
<td><code>harvestTimestamp</code>
<td>string (date-time)
<td>When this species was harvested
<td>
</tr>
<tr>
<td><code>harvestingMethod</code>
<td>enum(4 values)
<td>Method used to harvest this species
<td>
</tr>
<tr>
<td><code>heightM</code>
<td>number (≥0)
<td>Average tree height in meters
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of the most recent data update
<td>
</tr>
<tr>
<td><code>moistureContent</code>
<td>number (≥0, ≤100)
<td>Moisture content as percentage
<td>
</tr>
<tr>
<td><code>plantPartComposition</code>
<td>object (structured)
<td>Plant part breakdown within this species component
<td>
</tr>
<tr>
<td><code>primaryPlantPart</code>
<td>enum(17 values)
<td>Primary plant part represented by this species component
<td>
</tr>
<tr>
<td><code>qualityGrade</code>
<td>string
<td>Species-specific quality grade
<td>
</tr>
<tr>
<td><code>scientificName</code>
<td>string
<td>Scientific/Latin name of the species
<td>
</tr>
<tr>
<td><code>sourceGeographicDataId</code>
<td>string (pattern)
<td>Foreign key to geographic origin of this species
<td>
</tr>
<tr>
<td><code>structuralClassification</code>
<td>enum(5 values)
<td>Functional classification of the primary plant part
<td>
</tr>
</tbody>
</table>

## SpeciesComponent
### Overview
The `SpeciesComponent` entity enables detailed species-level tracking within multi-species TraceableUnits (TRUs). This entity supports biodiversity compliance, species-specific sustainability claims, and detailed forest composition analysis as required by the BOOST traceability system for comprehensive timber traceability. Each component represents a distinct species within a TRU with specific volume, quality, and origin data.
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
<td>`componentId`
<td>string
<td>Yes
<td>Unique identifier for the species component (primary key)
<td>`SC-PINE-001`, `SC-FIR-KLAMATH-042`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key back reference to TraceableUnit
<td>`TRU-PILE-CA-Klamath-042`
</tr>
<tr>
<td>`species`
<td>string
<td>Yes
<td>Species name (common or scientific)
<td>`Douglas Fir`, `Pinus ponderosa`, `Western Hemlock`
</tr>
<tr>
<td>`volumeM3`
<td>number
<td>Yes
<td>Volume of this species within the TRU in cubic meters
<td>`45.75`, `120.50`, `8.25`
</tr>
<tr>
<td>`percentageByVolume`
<td>number
<td>Yes
<td>Percentage of total TRU volume for this species (0-100)
<td>`53.7`, `25.0`, `12.8`
</tr>
<tr>
<td>`qualityGrade`
<td>string
<td>No
<td>Species-specific quality grade
<td>`Grade A Douglas Fir`, `Structural Pine`, `Pulp Grade Hemlock`
</tr>
<tr>
<td>`sourceGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to geographic origin of this species
<td>`GEO-HARVEST-RIDGE-01`, `GEO-STAND-NORTH-23`
</tr>
<tr>
<td>`harvestingMethod`
<td>string
<td>No
<td>Method used to harvest this species (enum)
<td>`chainsaw`, `harvester`, `manual`, `mechanical`
</tr>
<tr>
<td>`harvestTimestamp`
<td>string (date-time)
<td>No
<td>When this species was harvested
<td>`2025-07-15T07:30:00Z`
</tr>
<tr>
<td>`carbonStorage`
<td>string
<td>No
<td>CO2 data for this species component
<td>`12.5 tons CO2/m3`, `Carbon_class_A`
</tr>
<tr>
<td>`scientificName`
<td>string
<td>No
<td>Scientific/Latin name of the species
<td>`Pseudotsuga menziesii`, `Pinus ponderosa`, `Tsuga heterophylla`
</tr>
<tr>
<td>`dbhCm`
<td>number
<td>No
<td>Diameter at breast height in centimeters
<td>`45.2`, `78.5`, `32.1`
</tr>
<tr>
<td>`heightM`
<td>number
<td>No
<td>Average tree height in meters
<td>`28.5`, `35.2`, `22.8`
</tr>
<tr>
<td>`ageYears`
<td>integer
<td>No
<td>Estimated age in years
<td>`65`, `85`, `45`
</tr>
<tr>
<td>`moistureContent`
<td>number
<td>No
<td>Moisture content as percentage (0-100)
<td>`12.5`, `18.2`, `8.7`
</tr>
<tr>
<td>`defects`
<td>array&lt;string&gt;
<td>No
<td>List of defects or quality issues
<td>`["small_knots", "slight_bow"]`, `["bark_beetle_damage"]`
</tr>
<tr>
<td>`plantPartComposition`
<td>object
<td>No
<td>Plant part breakdown within this species component
<td>`{"trunk": {"volume": 18.5, "percentage": 75}}`
</tr>
<tr>
<td>`primaryPlantPart`
<td>string
<td>No
<td>Primary plant part represented by this species component
<td>`trunk`, `heartwood`, `bark`
</tr>
<tr>
<td>`structuralClassification`
<td>string
<td>No
<td>Functional classification of the primary plant part
<td>`structural`, `protective`, `metabolic`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/species-component/SC-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-21T15:45:00Z`
</tr>
</tbody>
</table>
---
### Key Features
1. **Species-Level Detail**
     Both common and scientific name support
     Detailed forestry metrics (DBH, height, age)
     Species-specific quality grading
     Individual harvesting method tracking
2. **Volume Integrity**
     Precise volume tracking in cubic meters
     Percentage composition within parent TRU
     Validation that components sum to 100% of TRU volume
     Support for volume conservation in processing
3. **Geographic Origin Tracking**
     Link to specific harvest locations
     Support for species migration tracking
     Integration with supply base area boundaries
     Environmental compliance reporting
4. **Quality and Condition Assessment**
     Species-specific quality grades
     Defect tracking and categorization
     Moisture content monitoring
     Structural integrity assessment
5. **Carbon and Environmental Data**
     Species-specific carbon storage calculations
     Integration with environmental impact assessments
     Support for carbon credit accounting
     Biodiversity compliance reporting
### Species Classification Examples
1. **Softwood Species**
     Douglas Fir (Pseudotsuga menziesii)
     Ponderosa Pine (Pinus ponderosa)
     Western Hemlock (Tsuga heterophylla)
     Incense Cedar (Calocedrus decurrens)
2. **Hardwood Species**
     California Black Oak (Quercus kelloggii)
     Pacific Madrone (Arbutus menziesii)
     Bigleaf Maple (Acer macrophyllum)
     Tanoak (Notholithocarpus densiflorus)
### Harvesting Method Classifications
- **chainsaw**: Manual chainsaw operation
- **harvester**: Mechanical harvester equipment
- **manual**: Hand tools and manual techniques
- **mechanical**: Other mechanical equipment
### Quality Grade Standards
Species-specific quality grades vary by:
- Structural integrity requirements
- Visual appearance standards
- Moisture content specifications
- Defect tolerance levels
- End-use applications
### Validation Rules
1. **Volume Conservation**
     Sum of all SpeciesComponent volumes must equal parent TRU volume
     Sum of all percentageByVolume must equal 100%
2. **Data Consistency**
     harvestTimestamp must be ≤ parent TRU createdTimestamp
     volumeM3 must be > 0
     percentageByVolume must be between 0 and 100
3. **Multi-Species Requirements**
     Only required when parent TRU has isMultiSpecies = true
     Single-species TRUs may optionally use SpeciesComponent for detailed tracking
### Example Use Cases
1. **Mixed Softwood Pile**
     Multiple SpeciesComponents for Douglas Fir, Pine, Hemlock
     Volume percentages sum to 100%
     Species-specific quality grades and harvesting methods
     Individual geographic origins within supply base
2. **Selective Harvest Tracking**
     Individual tree species from selective cutting operations
     Detailed forestry metrics (DBH, height, age)
     Species-specific carbon storage calculations
     Biodiversity impact assessment data
3. **Processing Operation Input**
     Species composition before and after processing
     Volume conservation validation
     Species-specific claim inheritance
     Quality grade preservation or transformation
### Relationships
- SpeciesComponent belongs to one TraceableUnit (many-to-one)
- SpeciesComponent references GeographicData for species origin
- SpeciesComponent supports species-specific Claims
- SpeciesComponent enables species-level MeasurementRecord tracking
- SpeciesComponent supports BiometricIdentifier species-specific data
- SpeciesComponent enables species-level carbon and environmental data
