# SupplyBase

## SupplyBase

### Overview
The `SupplyBase` entity manages geographic and operational areas for biomass supply operations within the BOOST traceability system. Supply bases represent coordinated geographic regions where organizations conduct harvesting, processing, and material collection activities. This entity supports area-based management, equipment deployment coordination, species availability tracking, and comprehensive supply chain planning across defined operational boundaries.

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
<td>`supplyBaseId`
<td>string
<td>Yes
<td>Unique identifier for the supply base (primary key)
<td>`SB-001`, `SB-KLAMATH-FOREST-REGION`
</tr>
<tr>
<td>`OrganizationId`
<td>string (FK)
<td>Yes
<td>Foreign key to managing organization
<td>`ORG-PACIFIC-FOREST-001`, `ORG-KLAMATH-HARVEST`
</tr>
<tr>
<td>`supplyBaseName`
<td>string
<td>Yes
<td>Descriptive name of the supply base area
<td>`Klamath National Forest Region`, `Pacific Northwest Operations`
</tr>
<tr>
<td>`description`
<td>string
<td>Yes
<td>Detailed description of supply base operations and scope
<td>`Sustainable forest management operations across 50,000 acres of mixed conifer forests`
</tr>
<tr>
<td>`harvestSites`
<td>array&lt;string&gt;
<td>No
<td>Array of harvest site identifiers within supply base
<td>`["GEO-HARVEST-001", "GEO-HARVEST-002", "GEO-HARVEST-003"]`
</tr>
<tr>
<td>`skidRoads`
<td>array&lt;string&gt;
<td>No
<td>Array of skid road infrastructure identifiers
<td>`["GEO-SKID-ROAD-A", "GEO-SKID-ROAD-B", "GEO-SKID-ROAD-C"]`
</tr>
<tr>
<td>`forestRoads`
<td>array&lt;string&gt;
<td>No
<td>Array of forest road infrastructure identifiers
<td>`["GEO-FOREST-ROAD-101", "GEO-FOREST-ROAD-102"]`
</tr>
<tr>
<td>`equipmentDeployment`
<td>array&lt;string&gt;
<td>No
<td>Array of equipment deployed across supply base
<td>`["EQ-HARVESTER-001", "EQ-FORWARDER-002", "EQ-LOADER-003"]`
</tr>
<tr>
<td>`traceableUnitIds`
<td>array&lt;string&gt;
<td>No
<td>Array of TRUs originating from this supply base
<td>`["TRU-LOG-001", "TRU-PILE-002", "TRU-BATCH-003"]`
</tr>
<tr>
<td>`speciesAvailable`
<td>array&lt;string&gt;
<td>No
<td>Array of species available within supply base
<td>`["Douglas Fir", "Ponderosa Pine", "Western Hemlock", "Incense Cedar"]`
</tr>
<tr>
<td>`GeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to primary geographic boundary of supply base
<td>`GEO-SUPPLY-BASE-KLAMATH-001`, `GEO-REGION-PACIFIC-NW`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/supply-base/SB-001`
</tr>
</tbody>
</table>

### Supply Base Types

1. **Forest Management Area**
    - Comprehensive forest management operations
    - Multiple harvest sites with coordinated planning
    - Long-term sustainable forestry practices
    - Integration with forest management plans

2. **Biomass Collection Region**
    - Specialized biomass and residue collection
    - Coordination with timber harvesting operations
    - Focus on energy and biofuel feedstock supply
    - Integration with processing facility requirements

3. **Multi-Owner Cooperative Area**
    - Coordination across multiple land ownerships
    - Shared infrastructure and equipment utilization
    - Collaborative harvesting and transportation
    - Economies of scale for small landowners

4. **Processing Facility Supply Zone**
    - Geographic area supplying specific processing facilities
    - Optimized transportation and logistics coordination
    - Species and quality specifications alignment
    - Just-in-time inventory management

### Key Features

1. **Geographic Coordination**
    - Area-based planning and management
    - Infrastructure development and maintenance
    - Transportation route optimization
    - Environmental compliance coordination

2. **Equipment Management**
    - Coordinated equipment deployment across area
    - Maintenance scheduling and resource sharing
    - Equipment utilization optimization
    - Multi-site operational efficiency

3. **Species Management**
    - Species availability tracking and planning
    - Biodiversity conservation coordination
    - Market demand alignment with species availability
    - Sustainable harvesting level management

4. **TRU Coordination**
    - Central tracking of all TRUs from supply base
    - Quality management across multiple sites
    - Processing coordination and scheduling
    - Supply chain optimization within area

### Infrastructure Components

1. **Harvest Sites**
    - Active timber harvesting locations
    - GPS coordinates and boundary definitions
    - Species composition and volume estimates
    - Access road and equipment requirements

2. **Skid Roads**
    - Primary extraction routes from harvest sites
    - Load capacity and equipment compatibility
    - Maintenance requirements and seasonal access
    - Integration with forest road network

3. **Forest Roads**
    - Main transportation arteries within supply base
    - Connection to public road systems
    - Multi-use coordination with other forest users
    - Long-term infrastructure maintenance planning

4. **Storage and Staging Areas**
    - Temporary material storage locations
    - Equipment parking and maintenance areas
    - Material sorting and quality assessment sites
    - Weather protection and security facilities

### Management Coordination

1. **Operational Planning**
    - Seasonal harvesting schedule coordination
    - Equipment deployment and utilization planning
    - Material flow optimization across sites
    - Workforce coordination and safety management

2. **Environmental Compliance**
    - Regulatory compliance across entire supply base
    - Environmental impact assessment coordination
    - Water quality protection and monitoring
    - Wildlife habitat conservation management

3. **Quality Management**
    - Consistent quality standards across all sites
    - Species identification and grading protocols
    - Processing specifications and requirements
    - Customer specification compliance

4. **Economic Optimization**
    - Cost minimization through coordinated operations
    - Transportation efficiency and logistics optimization
    - Shared infrastructure utilization
    - Market price optimization and timing

### Example Use Cases

1. **Integrated Forest Management Supply Base**
    - Supply Base: 75,000-acre managed forest region
    - Organization: Large integrated forest products company
    - Operations: Multiple harvest sites with coordinated planning
    - Infrastructure: Comprehensive road network and equipment fleet
    - Species: Mixed conifer forest with Douglas Fir, Pine, and Hemlock

2. **Biomass Collection Cooperative**
    - Supply Base: Regional biomass collection network
    - Organization: Biomass producer cooperative
    - Operations: Coordinated residue collection from multiple timber operations
    - Infrastructure: Shared equipment and transportation coordination
    - Species: Mixed species biomass for energy production

3. **Small Landowner Aggregation Area**
    - Supply Base: Multiple small private forest ownerships
    - Organization: Forest management service company
    - Operations: Coordinated harvesting across fragmented ownership
    - Infrastructure: Shared access roads and equipment services
    - Species: Variable species composition based on site conditions

### Validation Rules

1. **Identity Requirements**
    - supplyBaseId must be unique across system
    - OrganizationId must reference valid Organization
    - supplyBaseName and description must be non-empty
    - Geographic boundaries must be clearly defined

2. **Infrastructure Consistency**
    - harvestSites must reference valid GeographicData locations
    - Infrastructure elements must be within supply base boundaries
    - Equipment deployment must be appropriate for terrain and operations
    - Transportation networks must be logically connected

3. **Species and TRU Management**
    - speciesAvailable must reflect actual forest composition
    - traceableUnitIds must reference TRUs created within supply base
    - Species claims must be supported by forest inventory data
    - TRU origins must be traceable to specific harvest sites

### Relationships
- SupplyBase managed by one Organization
- SupplyBase encompasses multiple GeographicData locations (harvest sites, roads)
- SupplyBase coordinates Equipment deployment across operational area
- SupplyBase originates TraceableUnits from harvest operations
- SupplyBase supports SupplyBaseReport documentation for compliance and planning