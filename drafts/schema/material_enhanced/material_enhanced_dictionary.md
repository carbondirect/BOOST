# Data Dictionary

## Material (Enhanced)

### Overview
The enhanced `Material` entity serves as a reference table for material types with geographic data references and processing specifications to support species-specific sustainability claims in the Kaulen framework. This entity has been refactored from a traceable entity to a reference table, with TraceableUnit now serving as the primary traceable entity for individual wood pieces.

### Fields

| Field                        | Type             | Required | Description                                                                 | Examples                                    |
|-----------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `materialTypeId`            | string           | Yes      | Unique identifier for the material type (primary key)                    | `MAT-TYPE-001`, `MAT-DOUGLAS-FIR-SAWTIMBER` |
| `materialName`              | string           | Yes      | Descriptive name of the material type                                     | `Douglas Fir Sawtimber`, `Mixed Hardwood Chips` |
| `materialCategory`          | string           | Yes      | Category classification (enum)                                            | `softwood`, `hardwood`, `mixed`            |
| `defaultAssortmentTypes`    | string           | No       | Default assortment classifications for this material                      | `sawtimber, pulpwood`, `veneer, lumber`    |
| `standardQualityGrades`     | string           | No       | Standard quality grades available for this material                       | `Grade A, Grade B, Utility`, `Select, Common` |
| `carbonStorageRate`         | string           | No       | Carbon storage characteristics                                            | `0.47 tCO2/m3`, `0.52 tCO2/m3`           |
| `density`                   | string           | No       | Material density specifications                                           | `450 kg/m3`, `380-420 kg/m3`             |
| `applicableProcessingTypes` | array<string>    | No       | Processing types applicable to this material                              | `["felling", "delimbing", "crosscutting"]` |
| `typicalSpecies`            | array<string>    | No       | Species typically included in this material type                          | `["douglas_fir", "ponderosa_pine"]`       |
| `standardMoistureContent`   | string           | No       | Standard moisture content ranges                                          | `8-12%`, `15-20%`                        |
| `energyContent`             | string           | No       | Energy content specifications for biomass applications                    | `18.5 MJ/kg`, `16.2-19.8 MJ/kg`          |
| `@id`                       | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/material-enhanced/MAT-TYPE-001` |
| `lastUpdated`               | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Material Categories

1. **softwood**
   - Coniferous species material types
   - Typically used for construction lumber
   - Examples: Douglas Fir, Ponderosa Pine, Western Hemlock
   - Higher structural strength characteristics
   - Common processing: sawtimber, dimension lumber

2. **hardwood**
   - Deciduous species material types  
   - Varied applications from furniture to pulp
   - Examples: Oak, Maple, Cherry, Poplar
   - Higher density and varied grain patterns
   - Common processing: furniture stock, flooring, pulpwood

3. **mixed**
   - Multi-species material combinations
   - Biomass and chip applications
   - Variable composition by harvest location
   - Averaged characteristics across species
   - Common processing: chipping, pelletizing

### Key Features

1. **Reference Table Design**
   - No longer a traceable entity
   - Provides specifications for TRU material typing
   - Standardized material classifications
   - Processing guidance and specifications
   - Carbon accounting reference data

2. **Species Integration**
   - Links to typical species compositions
   - Species-specific processing guidelines
   - Biodiversity impact assessments
   - Sustainability claim foundations
   - Multi-species material support

3. **Processing Specifications**
   - Applicable processing type definitions
   - Quality grade standardizations
   - Assortment classification guidelines
   - Equipment compatibility specifications
   - Processing efficiency expectations

4. **Carbon and Energy Data**
   - Carbon storage rate specifications
   - Energy content for biomass applications
   - Density and moisture content standards
   - Sustainability metric foundations
   - Environmental impact references

### Processing Type Applications

1. **felling**
   - Tree cutting and initial processing
   - Species identification during harvest
   - Initial volume and quality assessment
   - Primary processing operation

2. **delimbing**
   - Branch removal preparation
   - Clean stem material preparation
   - Volume refinement specifications
   - Quality improvement processing

3. **crosscutting**
   - Length optimization specifications
   - Market requirement alignment
   - Quality grade maximization
   - Assortment classification support

4. **chipping**
   - Biomass preparation specifications
   - Size and quality requirements
   - Mixed species chip production
   - Energy content optimization

5. **debarking**
   - Clean wood preparation
   - Processing facility requirements
   - Volume loss expectations
   - Quality improvement specifications

### Quality Grade Standards

1. **Structural Grades**
   - Load-bearing capacity classifications
   - Strength and stiffness requirements
   - Defect limitations and allowances
   - Construction application suitability

2. **Appearance Grades**
   - Visual quality classifications
   - Grain pattern and color consistency
   - Surface quality requirements
   - Furniture and millwork applications

3. **Industrial Grades**
   - Functional performance requirements
   - Processing suitability specifications
   - Chemical composition consistency
   - Industrial application compatibility

### Validation Rules

1. **Classification Consistency**
   - materialCategory must align with typicalSpecies
   - applicableProcessingTypes must be appropriate for category
   - Quality grades must match industry standards
   - Species list must be ecologically consistent

2. **Processing Logic**
   - Processing types must be technically feasible
   - Quality grades must be achievable through specified processing
   - Assortment types must align with material characteristics
   - Equipment requirements must be reasonable

3. **Carbon and Energy Data**
   - Carbon storage rates must be scientifically valid
   - Energy content must align with species characteristics
   - Density specifications must be within reasonable ranges
   - Moisture content ranges must be practical

### Example Use Cases

1. **Douglas Fir Sawtimber Specifications**
   - Material type for high-grade construction lumber
   - Processing through felling, delimbing, crosscutting
   - Quality grades from Select to Utility
   - Carbon storage rate: 0.47 tCO2/m3
   - Typical density: 450 kg/m3

2. **Mixed Hardwood Chip Material**
   - Multi-species biomass material type
   - Processing through chipping and pelletizing
   - Industrial grade specifications
   - Variable species composition
   - Energy content: 17-19 MJ/kg

3. **Softwood Dimension Lumber**
   - Standard construction material type
   - Structural grade classifications
   - Standardized processing specifications
   - Moisture content: 19% or less
   - Multiple species applicability

### Relationships
- Material referenced by TraceableUnit for material type classification
- Material supports SpeciesComponent material categorization
- Material provides processing specifications for MaterialProcessing
- Material enables standardized Claim applications
- Material supports carbon accounting in sustainability assessments
- Material guides quality grading in MeasurementRecord operations