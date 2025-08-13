<!-- Auto-generated from material/validation_schema.json -->

Material types and specifications

**🗂️ [View Material in ERD Navigator](erd-navigator/index.html?focus=Material)**

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
<td>enum(Material)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>materialCategory</code>
<td>enum(softwood, hardwood, mixed)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>materialName</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>materialTypeId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>applicablePlantParts</code>
<td>array&amp;lt;string&amp;gt;
<td>Plant parts included in this material type
<td>
</tr>
<tr>
<td><code>applicableProcessingTypes</code>
<td>array&amp;lt;string&amp;gt;
<td>No description provided
<td>
</tr>
<tr>
<td><code>carbonStorageRate</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>defaultAssortmentTypes</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>density</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>energyContent</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>excludedPlantParts</code>
<td>array&amp;lt;string&amp;gt;
<td>Plant parts excluded from this material type
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>No description provided
<td>
</tr>
<tr>
<td><code>plantPartProcessingSpecs</code>
<td>object (structured)
<td>Processing specifications by plant part
<td>
</tr>
<tr>
<td><code>standardMoistureContent</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>standardQualityGrades</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>typicalSpecies</code>
<td>array&amp;lt;string&amp;gt;
<td>No description provided
<td>
</tr>
</tbody>
</table>

## Material
### Overview
The `Material` entity serves as a reference table for material types with geographic data references and processing specifications to support species-specific sustainability claims in the BOOST traceability system. This entity has been refactored from a traceable entity to a reference table, with TraceableUnit now serving as the primary traceable entity for individual wood pieces.
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
<td>`materialTypeId`
<td>string
<td>Yes
<td>Unique identifier for the material type (primary key)
<td>`MAT-TYPE-001`, `MAT-DOUGLAS-FIR-SAWTIMBER`
</tr>
<tr>
<td>`materialName`
<td>string
<td>Yes
<td>Descriptive name of the material type
<td>`Douglas Fir Sawtimber`, `Mixed Hardwood Chips`
</tr>
<tr>
<td>`materialCategory`
<td>string
<td>Yes
<td>Category classification (enum)
<td>`softwood`, `hardwood`, `mixed`
</tr>
<tr>
<td>`defaultAssortmentTypes`
<td>string
<td>No
<td>Default assortment classifications for this material
<td>`sawtimber, pulpwood`, `veneer, lumber`
</tr>
<tr>
<td>`standardQualityGrades`
<td>string
<td>No
<td>Standard quality grades available for this material
<td>`Grade A, Grade B, Utility`, `Select, Common`
</tr>
<tr>
<td>`carbonStorageRate`
<td>string
<td>No
<td>Carbon storage characteristics
<td>`0.47 tCO2/m3`, `0.52 tCO2/m3`
</tr>
<tr>
<td>`density`
<td>string
<td>No
<td>Material density specifications
<td>`450 kg/m3`, `380-420 kg/m3`
</tr>
<tr>
<td>`applicableProcessingTypes`
<td>array&lt;string&gt;
<td>No
<td>Processing types applicable to this material
<td>`["felling", "delimbing", "crosscutting"]`
</tr>
<tr>
<td>`typicalSpecies`
<td>array&lt;string&gt;
<td>No
<td>Species typically included in this material type
<td>`["douglas_fir", "ponderosa_pine"]`
</tr>
<tr>
<td>`standardMoistureContent`
<td>string
<td>No
<td>Standard moisture content ranges
<td>`8-12%`, `15-20%`
</tr>
<tr>
<td>`energyContent`
<td>string
<td>No
<td>Energy content specifications for biomass applications
<td>`18.5 MJ/kg`, `16.2-19.8 MJ/kg`
</tr>
<tr>
<td>`applicablePlantParts`
<td>array&lt;string&gt;
<td>No
<td>Plant parts included in this material type
<td>`["trunk", "heartwood", "sapwood"]`
</tr>
<tr>
<td>`excludedPlantParts`
<td>array&lt;string&gt;
<td>No
<td>Plant parts excluded from this material type
<td>`["bark", "branches", "needles"]`
</tr>
<tr>
<td>`plantPartProcessingSpecs`
<td>object
<td>No
<td>Processing specifications by plant part
<td>`{"trunk": {"processingMethods": ["sawing"]}}`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/material/MAT-TYPE-001`
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
### Material Categories
1. **softwood**
     Coniferous species material types
     Typically used for construction lumber
     Examples: Douglas Fir, Ponderosa Pine, Western Hemlock
     Higher structural strength characteristics
     Common processing: sawtimber, dimension lumber
2. **hardwood**
     Deciduous species material types  
     Varied applications from furniture to pulp
     Examples: Oak, Maple, Cherry, Poplar
     Higher density and varied grain patterns
     Common processing: furniture stock, flooring, pulpwood
3. **mixed**
     Multi-species material combinations
     Biomass and chip applications
     Variable composition by harvest location
     Averaged characteristics across species
     Common processing: chipping, pelletizing
### Plant Part Categories
#### **Woody Components**
- **trunk** - Main structural wood, highest value for lumber
- **heartwood** - Inner non-living wood, premium lumber applications
- **sapwood** - Outer living wood, structural lumber with treatment
- **branches** - Secondary woody growth, suitable for chips and fuel
- **twigs** - Small terminal branches, primarily fuel applications
- **bark** - Outer protective layer, mulch and fuel applications
#### **Foliage Components**  
- **leaves** - Deciduous photosynthetic organs, composting applications
- **needles** - Coniferous leaves, mulch and soil amendment
#### **Reproductive Components**
- **seeds** - Propagation material, food and oil applications
- **nuts** - Hard-shelled seeds, food and specialty products
- **cones** - Coniferous reproductive structures, decorative and fuel
#### **Agricultural Components**
- **stalks** - Main stems of crops, biomass and building materials
- **straw** - Dried stalks after harvest, animal bedding and fuel
- **husks** - Outer seed coverings, fuel and industrial applications
- **hulls** - Hard outer shells, fuel and abrasive applications
- **chaff** - Seed casings, animal feed and fuel
- **stubble** - Remaining stalks, soil amendment and fuel
### Key Features
1. **Reference Table Design**
     No longer a traceable entity
     Provides specifications for TRU material typing
     Standardized material classifications
     Processing guidance and specifications
     Carbon accounting reference data
2. **Species Integration**
     Links to typical species compositions
     Species-specific processing guidelines
     Biodiversity impact assessments
     Sustainability claim foundations
     Multi-species material support
3. **Processing Specifications**
     Applicable processing type definitions
     Quality grade standardizations
     Assortment classification guidelines
     Equipment compatibility specifications
     Processing efficiency expectations
4. **Carbon and Energy Data**
     Carbon storage rate specifications
     Energy content for biomass applications
     Density and moisture content standards
     Sustainability metric foundations
     Environmental impact references
### Processing Type Applications
1. **felling**
     Tree cutting and initial processing
     Species identification during harvest
     Initial volume and quality assessment
     Primary processing operation
2. **delimbing**
     Branch removal preparation
     Clean stem material preparation
     Volume refinement specifications
     Quality improvement processing
3. **crosscutting**
     Length optimization specifications
     Market requirement alignment
     Quality grade maximization
     Assortment classification support
4. **chipping**
     Biomass preparation specifications
     Size and quality requirements
     Mixed species chip production
     Energy content optimization
5. **debarking**
     Clean wood preparation
     Processing facility requirements
     Volume loss expectations
     Quality improvement specifications
### Quality Grade Standards
1. **Structural Grades**
     Load-bearing capacity classifications
     Strength and stiffness requirements
     Defect limitations and allowances
     Construction application suitability
2. **Appearance Grades**
     Visual quality classifications
     Grain pattern and color consistency
     Surface quality requirements
     Furniture and millwork applications
3. **Industrial Grades**
     Functional performance requirements
     Processing suitability specifications
     Chemical composition consistency
     Industrial application compatibility
### Validation Rules
1. **Classification Consistency**
     materialCategory must align with typicalSpecies
     applicableProcessingTypes must be appropriate for category
     Quality grades must match industry standards
     Species list must be ecologically consistent
2. **Processing Logic**
     Processing types must be technically feasible
     Quality grades must be achievable through specified processing
     Assortment types must align with material characteristics
     Equipment requirements must be reasonable
3. **Carbon and Energy Data**
     Carbon storage rates must be scientifically valid
     Energy content must align with species characteristics
     Density specifications must be within reasonable ranges
     Moisture content ranges must be practical
### Example Use Cases
1. **Douglas Fir Sawtimber Specifications**
     Material type for high-grade construction lumber
     Processing through felling, delimbing, crosscutting
     Quality grades from Select to Utility
     Carbon storage rate: 0.47 tCO2/m3
     Typical density: 450 kg/m3
2. **Mixed Hardwood Chip Material**
     Multi-species biomass material type
     Processing through chipping and pelletizing
     Industrial grade specifications
     Variable species composition
     Energy content: 17-19 MJ/kg
3. **Softwood Dimension Lumber**
     Standard construction material type
     Structural grade classifications
     Standardized processing specifications
     Moisture content: 19% or less
     Multiple species applicability
### Relationships
- Material referenced by TraceableUnit for material type classification
- Material supports SpeciesComponent material categorization
- Material provides processing specifications for MaterialProcessing
- Material enables standardized Claim applications
- Material supports carbon accounting in sustainability assessments
- Material guides quality grading in MeasurementRecord operations
