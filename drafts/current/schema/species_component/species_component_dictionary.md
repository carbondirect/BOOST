# Data Dictionary

## SpeciesComponent

### Overview
The `SpeciesComponent` entity enables detailed species-level tracking within multi-species TraceableUnits (TRUs). This entity supports biodiversity compliance, species-specific sustainability claims, and detailed forest composition analysis as required by the Kaulen framework for comprehensive timber traceability. Each component represents a distinct species within a TRU with specific volume, quality, and origin data.

### Fields

| Field                    | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `componentId`           | string           | Yes      | Unique identifier for the species component (primary key)                | `SC-PINE-001`, `SC-FIR-KLAMATH-042`       |
| `traceableUnitId`       | string (FK)      | Yes      | Foreign key back reference to TraceableUnit                              | `TRU-PILE-CA-Klamath-042`                 |
| `species`               | string           | Yes      | Species name (common or scientific)                                      | `Douglas Fir`, `Pinus ponderosa`, `Western Hemlock` |
| `volumeM3`              | number           | Yes      | Volume of this species within the TRU in cubic meters                    | `45.75`, `120.50`, `8.25`                 |
| `percentageByVolume`    | number           | Yes      | Percentage of total TRU volume for this species (0-100)                 | `53.7`, `25.0`, `12.8`                    |
| `qualityGrade`          | string           | No       | Species-specific quality grade                                           | `Grade A Douglas Fir`, `Structural Pine`, `Pulp Grade Hemlock` |
| `sourceGeographicDataId`| string (FK)      | No       | Foreign key to geographic origin of this species                         | `GEO-HARVEST-RIDGE-01`, `GEO-STAND-NORTH-23` |
| `harvestingMethod`      | string           | No       | Method used to harvest this species (enum)                              | `chainsaw`, `harvester`, `manual`, `mechanical` |
| `harvestTimestamp`      | string (date-time)| No      | When this species was harvested                                          | `2025-07-15T07:30:00Z`                    |
| `carbonStorage`         | string           | No       | CO2 data for this species component                                      | `12.5 tons CO2/m3`, `Carbon_class_A`      |
| `scientificName`        | string           | No       | Scientific/Latin name of the species                                     | `Pseudotsuga menziesii`, `Pinus ponderosa`, `Tsuga heterophylla` |
| `dbhCm`                 | number           | No       | Diameter at breast height in centimeters                                | `45.2`, `78.5`, `32.1`                    |
| `heightM`               | number           | No       | Average tree height in meters                                           | `28.5`, `35.2`, `22.8`                    |
| `ageYears`              | integer          | No       | Estimated age in years                                                   | `65`, `85`, `45`                          |
| `moistureContent`       | number           | No       | Moisture content as percentage (0-100)                                   | `12.5`, `18.2`, `8.7`                     |
| `defects`               | array<string>    | No       | List of defects or quality issues                                        | `["small_knots", "slight_bow"]`, `["bark_beetle_damage"]` |
| `plantPartComposition`  | object           | No       | Plant part breakdown within this species component                       | `{"trunk": {"volume": 18.5, "percentage": 75}}` |
| `primaryPlantPart`      | string           | No       | Primary plant part represented by this species component                 | `trunk`, `heartwood`, `bark`              |
| `structuralClassification` | string        | No       | Functional classification of the primary plant part                      | `structural`, `protective`, `metabolic`   |
| `@id`                   | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                       | `https://github.com/carbondirect/BOOST/schemas/species-component/SC-001` |
| `lastUpdated`           | string (date-time)| No      | Timestamp of the most recent data update                                | `2025-07-21T15:45:00Z`                    |

---

### Key Features

1. **Species-Level Detail**
   - Both common and scientific name support
   - Detailed forestry metrics (DBH, height, age)
   - Species-specific quality grading
   - Individual harvesting method tracking

2. **Volume Integrity**
   - Precise volume tracking in cubic meters
   - Percentage composition within parent TRU
   - Validation that components sum to 100% of TRU volume
   - Support for volume conservation in processing

3. **Geographic Origin Tracking**
   - Link to specific harvest locations
   - Support for species migration tracking
   - Integration with supply base area boundaries
   - Environmental compliance reporting

4. **Quality and Condition Assessment**
   - Species-specific quality grades
   - Defect tracking and categorization
   - Moisture content monitoring
   - Structural integrity assessment

5. **Carbon and Environmental Data**
   - Species-specific carbon storage calculations
   - Integration with environmental impact assessments
   - Support for carbon credit accounting
   - Biodiversity compliance reporting

### Species Classification Examples

1. **Softwood Species**
   - Douglas Fir (Pseudotsuga menziesii)
   - Ponderosa Pine (Pinus ponderosa)
   - Western Hemlock (Tsuga heterophylla)
   - Incense Cedar (Calocedrus decurrens)

2. **Hardwood Species**
   - California Black Oak (Quercus kelloggii)
   - Pacific Madrone (Arbutus menziesii)
   - Bigleaf Maple (Acer macrophyllum)
   - Tanoak (Notholithocarpus densiflorus)

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
   - Sum of all SpeciesComponent volumes must equal parent TRU volume
   - Sum of all percentageByVolume must equal 100%

2. **Data Consistency**
   - harvestTimestamp must be ≤ parent TRU createdTimestamp
   - volumeM3 must be > 0
   - percentageByVolume must be between 0 and 100

3. **Multi-Species Requirements**
   - Only required when parent TRU has isMultiSpecies = true
   - Single-species TRUs may optionally use SpeciesComponent for detailed tracking

### Example Use Cases

1. **Mixed Softwood Pile**
   - Multiple SpeciesComponents for Douglas Fir, Pine, Hemlock
   - Volume percentages sum to 100%
   - Species-specific quality grades and harvesting methods
   - Individual geographic origins within supply base

2. **Selective Harvest Tracking**
   - Individual tree species from selective cutting operations
   - Detailed forestry metrics (DBH, height, age)
   - Species-specific carbon storage calculations
   - Biodiversity impact assessment data

3. **Processing Operation Input**
   - Species composition before and after processing
   - Volume conservation validation
   - Species-specific claim inheritance
   - Quality grade preservation or transformation

### Relationships
- SpeciesComponent belongs to one TraceableUnit (many-to-one)
- SpeciesComponent references GeographicData for species origin
- SpeciesComponent supports species-specific Claims
- SpeciesComponent enables species-level MeasurementRecord tracking
- SpeciesComponent supports BiometricIdentifier species-specific data
- SpeciesComponent enables species-level carbon and environmental data