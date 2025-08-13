<!-- Auto-generated from geographic_data/validation_schema.json -->

GeographicData entity in BOOST data model

**🗂️ [View Geographic Data in ERD Navigator](erd-navigator/index.html?focus=GeographicData)**

### Relationships ### {{.unnumbered}}

- **geographicDataId** → [[#geographic-data|Geographic Data]] - Unique identifier for the geographic data

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
<td>enum(GeographicData)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>dataType</code>
<td>enum(7 values)
<td>Type of geographic data
<td>✓
</tr>
<tr>
<td><code>description</code>
<td>string
<td>Human-readable description of the geographic area
<td>✓
</tr>
<tr>
<td><code>geoJsonData</code>
<td>object (structured)
<td>Valid GeoJSON object (Point, Polygon, LineString, etc.)
<td>✓
</tr>
<tr>
<td><code>geographicDataId</code>
<td>string (pattern)
<td>Unique identifier for the geographic data
<td>✓
</tr>
<tr>
<td><code>accessRestrictions</code>
<td>string
<td>Any access restrictions or special conditions
<td>
</tr>
<tr>
<td><code>accuracy</code>
<td>number (≥0)
<td>GPS accuracy in meters
<td>
</tr>
<tr>
<td><code>administrativeRegion</code>
<td>string
<td>Administrative region or jurisdiction
<td>
</tr>
<tr>
<td><code>coordinateSystem</code>
<td>string
<td>Coordinate reference system (e.g., WGS84, UTM Zone 10N)
<td>
</tr>
<tr>
<td><code>elevationM</code>
<td>number
<td>Elevation in meters above sea level
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of the most recent data update
<td>
</tr>
</tbody>
</table>

## GeographicData
### Overview
The `GeographicData` entity provides comprehensive spatial data support for the BOOST framework using GeoJSON standards. This entity enables precise location tracking, geographic boundaries definition, and spatial relationship management throughout the biomass supply chain. It supports the BOOST traceability system's requirement for complete location-based traceability and addresses California agency engagement commitments for spatial data integration.
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
<td>`geographicDataId`
<td>string
<td>Yes
<td>Unique identifier for the geographic data (primary key)
<td>`GEO-HARVEST-001`, `GEO-MILL-PACIFIC-01`
</tr>
<tr>
<td>`geoJsonData`
<td>object
<td>Yes
<td>Valid GeoJSON object (Point, Polygon, LineString, etc.)
<td>See GeoJSON examples below
</tr>
<tr>
<td>`dataType`
<td>string
<td>Yes
<td>Type of geographic data (enum)
<td>`harvest_site`, `processing_location`, `administrative_boundary`, `supply_base_area`
</tr>
<tr>
<td>`description`
<td>string
<td>Yes
<td>Human-readable description of the geographic area
<td>`Klamath Ridge Harvest Site Unit 4`, `Pacific Lumber Mill Entrance`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-21T15:00:00Z`
</tr>
<tr>
<td>`coordinateSystem`
<td>string
<td>No
<td>Coordinate reference system (default: WGS84)
<td>`WGS84`, `UTM Zone 10N`, `NAD83`
</tr>
<tr>
<td>`accuracy`
<td>number
<td>No
<td>GPS accuracy in meters
<td>`3.5`, `10.0`, `1.2`
</tr>
<tr>
<td>`elevationM`
<td>number
<td>No
<td>Elevation in meters above sea level
<td>`1250.5`, `450.0`, `2100.8`
</tr>
<tr>
<td>`administrativeRegion`
<td>string
<td>No
<td>Administrative region or jurisdiction
<td>`California`, `Humboldt County`, `Klamath National Forest`
</tr>
<tr>
<td>`accessRestrictions`
<td>string
<td>No
<td>Any access restrictions or special conditions
<td>`Seasonal road closure Nov-Apr`, `Permit required for access`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/geographic-data/GEO-001`
</tr>
</tbody>
</table>
---
### GeoJSON Data Types
#### Point (Single Location)
```json
{
  "type": "Point",
  "coordinates": [-124.2345, 41.7891]
}
```
#### Polygon (Area/Boundary)
```json
{
  "type": "Polygon",
  "coordinates": [[
    [-124.2345, 41.7891],
    [-124.2300, 41.7891],
    [-124.2300, 41.7850],
    [-124.2345, 41.7850],
    [-124.2345, 41.7891]
  ]]
}
```
#### LineString (Road/Path)
```json
{
  "type": "LineString",
  "coordinates": [
    [-124.2345, 41.7891],
    [-124.2320, 41.7885],
    [-124.2300, 41.7870]
  ]
}
```
---
### Data Type Classifications
1. **harvest_site**
     Specific locations where timber harvesting occurs
     Typically Point or small Polygon geometries
     Links to TraceableUnit harvest locations
2. **processing_location**
     Locations where MaterialProcessing occurs
     Mills, sorting yards, chipping facilities
     Point geometries with facility boundaries
3. **administrative_boundary**
     Regulatory or administrative boundaries
     County lines, forest service boundaries, permit areas
     Polygon geometries
4. **supply_base_area**
     Overall supply base geographic boundaries
     Large Polygon geometries encompassing multiple harvest sites
     Links to SupplyBase entities
5. **skid_road / forest_road**
     Transportation infrastructure
     LineString geometries showing road networks
     Critical for tracking point infrastructure
6. **mill_entrance**
     Specific points where TRUs enter processing facilities
     Point geometries at facility gates
     Final tracking points in BOOST traceability system
### Key Features
1. **GeoJSON Compliance**
     Full GeoJSON specification support
     Multiple geometry types (Point, Polygon, LineString, etc.)
     Properties object for additional spatial metadata
2. **Coordinate System Support**
     Default WGS84 for global interoperability
     Support for regional coordinate systems (UTM, NAD83, etc.)
     Accuracy metadata for GPS precision tracking
3. **Hierarchical Relationships**
     Support for nested geographic relationships
     Harvest sites within supply base areas
     Administrative boundaries containing operational areas
4. **Agency Integration**
     Designed for California agency mapping requirements
     Support for regulatory boundary definitions
     Integration with GIS systems and spatial databases
### Example Use Cases
1. **Harvest Site Tracking**
     Precise GPS coordinates of harvest operations
     Links to TraceableUnit harvest locations
     Support for environmental compliance reporting
2. **Supply Base Boundaries**
     Large polygon areas defining operational scope
     Integration with forest management plans
     Regulatory compliance boundary definitions
3. **Transportation Networks**
     Skid road and forest road mapping
     Route optimization and planning
     Infrastructure maintenance tracking
4. **Processing Facility Locations**
     Mill entrance points for final tracking
     Processing location definitions
     Facility boundary and access point mapping
### Relationships
- GeographicData provides harvest locations for TraceableUnit
- GeographicData defines current locations for TraceableUnit
- GeographicData defines operational areas for Organization
- GeographicData locates Transaction processing
- GeographicData defines boundaries for SupplyBase
- GeographicData locates Supplier and Customer facilities
- GeographicData defines scope for Certificate coverage
- GeographicData covers areas for SupplyBaseReport
- GeographicData locates Audit activities
- GeographicData defines origins for SpeciesComponent
- GeographicData locates MaterialProcessing operations
- GeographicData locates MeasurementRecord activities
- GeographicData locates BiometricIdentifier capture points
