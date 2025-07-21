# Data Dictionary

## GeographicData

### Overview
The `GeographicData` entity provides comprehensive spatial data support for the BOOST framework using GeoJSON standards. This entity enables precise location tracking, geographic boundaries definition, and spatial relationship management throughout the biomass supply chain. It supports the Kaulen framework's requirement for complete location-based traceability and addresses California agency engagement commitments for spatial data integration.

### Fields

| Field                    | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `geographicDataId`      | string           | Yes      | Unique identifier for the geographic data (primary key)                   | `GEO-HARVEST-001`, `GEO-MILL-PACIFIC-01`   |
| `geoJsonData`           | object           | Yes      | Valid GeoJSON object (Point, Polygon, LineString, etc.)                  | See GeoJSON examples below                  |
| `dataType`              | string           | Yes      | Type of geographic data (enum)                                           | `harvest_site`, `processing_location`, `administrative_boundary`, `supply_base_area` |
| `description`           | string           | Yes      | Human-readable description of the geographic area                        | `Klamath Ridge Harvest Site Unit 4`, `Pacific Lumber Mill Entrance` |
| `lastUpdated`           | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:00:00Z`                    |
| `coordinateSystem`      | string           | No       | Coordinate reference system (default: WGS84)                            | `WGS84`, `UTM Zone 10N`, `NAD83`           |
| `accuracy`              | number           | No       | GPS accuracy in meters                                                   | `3.5`, `10.0`, `1.2`                      |
| `elevationM`            | number           | No       | Elevation in meters above sea level                                      | `1250.5`, `450.0`, `2100.8`               |
| `administrativeRegion`  | string           | No       | Administrative region or jurisdiction                                    | `California`, `Humboldt County`, `Klamath National Forest` |
| `accessRestrictions`    | string           | No       | Any access restrictions or special conditions                            | `Seasonal road closure Nov-Apr`, `Permit required for access` |
| `@id`                   | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                       | `https://github.com/carbondirect/BOOST/schemas/geographic-data/GEO-001` |

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
   - Specific locations where timber harvesting occurs
   - Typically Point or small Polygon geometries
   - Links to TraceableUnit harvest locations

2. **processing_location**
   - Locations where MaterialProcessing occurs
   - Mills, sorting yards, chipping facilities
   - Point geometries with facility boundaries

3. **administrative_boundary**
   - Regulatory or administrative boundaries
   - County lines, forest service boundaries, permit areas
   - Polygon geometries

4. **supply_base_area**
   - Overall supply base geographic boundaries
   - Large Polygon geometries encompassing multiple harvest sites
   - Links to SupplyBase entities

5. **skid_road / forest_road**
   - Transportation infrastructure
   - LineString geometries showing road networks
   - Critical for tracking point infrastructure

6. **mill_entrance**
   - Specific points where TRUs enter processing facilities
   - Point geometries at facility gates
   - Final tracking points in Kaulen framework

### Key Features

1. **GeoJSON Compliance**
   - Full GeoJSON specification support
   - Multiple geometry types (Point, Polygon, LineString, etc.)
   - Properties object for additional spatial metadata

2. **Coordinate System Support**
   - Default WGS84 for global interoperability
   - Support for regional coordinate systems (UTM, NAD83, etc.)
   - Accuracy metadata for GPS precision tracking

3. **Hierarchical Relationships**
   - Support for nested geographic relationships
   - Harvest sites within supply base areas
   - Administrative boundaries containing operational areas

4. **Agency Integration**
   - Designed for California agency mapping requirements
   - Support for regulatory boundary definitions
   - Integration with GIS systems and spatial databases

### Example Use Cases

1. **Harvest Site Tracking**
   - Precise GPS coordinates of harvest operations
   - Links to TraceableUnit harvest locations
   - Support for environmental compliance reporting

2. **Supply Base Boundaries**
   - Large polygon areas defining operational scope
   - Integration with forest management plans
   - Regulatory compliance boundary definitions

3. **Transportation Networks**
   - Skid road and forest road mapping
   - Route optimization and planning
   - Infrastructure maintenance tracking

4. **Processing Facility Locations**
   - Mill entrance points for final tracking
   - Processing location definitions
   - Facility boundary and access point mapping

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