# BOOST ERD Navigator Configuration Guide

This document provides comprehensive guidance for configuring and maintaining the BOOST Interactive ERD Navigator system.

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Entity Positioning System](#entity-positioning-system)
3. [Relationship Configuration](#relationship-configuration)
4. [Schema Integration](#schema-integration)
5. [Visual Design System](#visual-design-system)
6. [Configuration Files](#configuration-files)
7. [Adding New Entities](#adding-new-entities)
8. [Maintenance Guide](#maintenance-guide)

## System Architecture

The BOOST ERD Navigator uses a **metadata-driven architecture** that automatically generates entity relationships and visualizations from JSON schema files. The system consists of:

- **Dynamic Schema Loading**: Entities loaded from `/drafts/current/schema/*/validation_schema.json`
- **Metadata-Driven Relationships**: Relationships defined in `boost_metadata` sections of schemas
- **Configuration-Based Positioning**: Entity positions defined in `erd-config.json`
- **Interactive Visualization**: D3.js-based SVG rendering with zoom/pan controls

## Entity Positioning System

### Hub-and-Spoke Layout Design

The ERD uses a **hub-and-spoke layout** with TraceableUnit as the central hub and 7 thematic areas arranged around it:

```
    Geographic & Tracking (🟣)
            |
Organizational ─── Core Traceability ─── Measurement & Verification
Foundation (🔵)    (🟢 CENTER)         (🟡)
            |           |                   |
Transaction ─────── TraceableUnit ──── Compliance & Reporting
Management (🟠)    (📦 HUB)           (🔴)
            |
    Material & Supply Chain (🟤)
```

### Coordinate System

**Center Hub**: TraceableUnit at `(1600, 1200)`

**Thematic Area Positions**:
- **Top (y=100)**: Geographic & Tracking
- **Top-Left (x=100, y=400)**: Organizational Foundation  
- **Left (x=100, y=2000)**: Material & Supply Chain
- **Right (x=2700+)**: Transaction Management, Measurement & Verification, Compliance & Reporting
- **Core Center (x=1300-1900, y=1000-1400)**: Core Traceability entities

### Spacing Requirements

- **Minimum Entity Spacing**: 300px between entity centers
- **Thematic Group Spacing**: 250px between entities within same group
- **Inter-Group Spacing**: 600px+ between different thematic areas
- **Hub Distance**: Core traceability entities within 400px of TraceableUnit

### Emoji Selection

Each entity has a carefully chosen emoji for visual identification:

```json
{
  "TraceableUnit": "📦",    // Central package/container
  "Organization": "🏢",     // Business building
  "Material": "🪵",         // Wood/forestry
  "Transaction": "💰",      // Financial exchange
  "GeographicData": "🗺️",   // Map/location
  "MeasurementRecord": "📏", // Measurement tool
  "MaterialProcessing": "🔄" // Process/transformation
}
```

## Relationship Configuration

### Metadata-Driven Relationships

Relationships are primarily defined in schema files using the `boost_metadata.relationships` structure:

```json
{
  "boost_metadata": {
    "relationships": [
      {
        "field": "traceableUnitId",
        "targetEntity": "TraceableUnit",
        "relationshipType": "many-to-one",
        "required": true,
        "label": "measuring",
        "example": "Record-456 measures volume/moisture of TRU-123"
      }
    ]
  }
}
```

### Relationship Properties

- **field**: The JSON schema field containing the foreign key
- **targetEntity**: The target entity name (must match schema entity name)
- **relationshipType**: `"many-to-one"`, `"one-to-many"`, or `"many-to-many"`
- **required**: Boolean indicating if relationship is mandatory
- **label**: Human-readable relationship description
- **example**: Concrete example showing the relationship in action

### Manual Relationship Overrides

Some relationships are defined in `erd-config.json` under `manual_relationships` for cases where:
- The relationship spans multiple fields
- Custom labeling is needed
- Legacy compatibility is required

### Field Mapping System

The `field_mappings` section automatically detects foreign key relationships:

```json
{
  "field_mappings": {
    "Organization": ["OrganizationId", "organizationId", "harvesterId"],
    "TraceableUnit": ["TraceableUnitId", "traceableUnitId", "inputTraceableUnitId"],
    "GeographicData": ["GeographicDataId", "currentGeographicDataId", "harvestGeographicDataId"]
  }
}
```

### Relationship Examples System

Examples appear in relationship popups when users click on relationship lines. Examples should:
- Use realistic entity IDs (e.g., "TRU-123", "ORG-001")
- Include organization names in quotes (e.g., "'Olympic Forest Products'")
- Be concise (under 100 characters)
- Show concrete business scenarios

## Schema Integration

### Dynamic Schema Loading

The ERD automatically discovers entities using:

1. **Schema Directory Manifest**: `/drafts/current/schema/directories.json`
2. **Validation Schema Files**: `/drafts/current/schema/*/validation_schema.json`
3. **Metadata Schema Definition**: `/drafts/current/schema/boost_metadata_schema.json`

### Boost Metadata Schema Structure

```json
{
  "boost_metadata": {
    "entity": {
      "name": "EntityName",
      "primaryKey": "entityId", 
      "area": "thematic_category",
      "description": "Entity description with emoji"
    },
    "relationships": [/* relationship definitions */]
  }
}
```

### Required Metadata Fields

Every entity must include:
- **name**: Exact entity name matching schema title
- **primaryKey**: Field name of the primary key
- **area**: One of 7 thematic categories
- **description**: Brief description (emoji optional but recommended)

### Thematic Categories

Entities must use one of these 7 standard categories:

1. `"core_traceability"` - 🟢 Green
2. `"organizational_foundation"` - 🔵 Blue  
3. `"material_supply_chain"` - 🟤 Brown
4. `"transaction_management"` - 🟠 Orange
5. `"measurement_verification"` - 🟡 Yellow
6. `"geographic_tracking"` - 🟣 Purple
7. `"compliance_reporting"` - 🔴 Red

## Visual Design System

### Color Coding

Each thematic area has semantic color meanings:

- **🟢 Core Traceability (Green)**: Growth, sustainability, life cycle
- **🔵 Organizational Foundation (Blue)**: Trust, authority, certification
- **🟤 Material & Supply Chain (Brown)**: Earth, wood, raw materials
- **🟠 Transaction Management (Orange)**: Commerce, energy, exchange
- **🟡 Measurement & Verification (Yellow)**: Quality, precision, validation
- **🟣 Geographic & Tracking (Purple)**: Space, location, mapping
- **🔴 Compliance & Reporting (Red)**: Regulation, alerts, compliance

### Interactive Features

The ERD includes these interactive capabilities:

- **Zoom & Pan**: Mouse wheel zoom, click-and-drag panning
- **Entity Filtering**: Filter by thematic areas using buttons
- **TraceableUnit Focus**: 🎯 button highlights only essential relationships
- **Relationship Labels**: Toggle relationship labels on/off
- **GitHub Integration**: 💬 icons link to entity discussions
- **Relationship Examples**: Click relationships to see example popups

### UI Controls

Standard UI controls include:
- Zoom controls (+ / - buttons)
- Reset zoom button (🔄)
- Filter buttons for each thematic area
- TraceableUnit focus button (🎯)
- Toggle labels button (🏷️)

## Configuration Files

### Primary Configuration: `erd-config.json`

```json
{
  "areas": {/* thematic area definitions */},
  "entity_display": {/* entity positions and emojis */},
  "manual_relationships": [/* override relationships */],
  "field_mappings": {/* FK detection patterns */},
  "primary_key_mappings": {/* entity PK mappings */}
}
```

### Schema Manifest: `directories.json`

```json
{
  "schema_directories": ["entity1", "entity2"],
  "total_entities": 31,
  "description": "Schema directory listing for auto-discovery"
}
```

### Metadata Schema: `boost_metadata_schema.json`

Defines the structure and validation rules for entity metadata sections.

## Adding New Entities

### Step 1: Create Schema Directory

1. Create directory: `/drafts/current/schema/new_entity/`
2. Add `validation_schema.json` with complete JSON schema
3. Include dictionary and example files as needed

### Step 2: Add Boost Metadata

Include metadata section in validation schema:

```json
{
  "boost_metadata": {
    "entity": {
      "name": "NewEntity",
      "primaryKey": "newEntityId",
      "area": "appropriate_category",
      "description": "🆕 New entity description"
    },
    "relationships": [
      /* Define all relationships */
    ]
  }
}
```

### Step 3: Update Configuration

1. **Add to directories.json**: Include entity in schema_directories array
2. **Add position to erd-config.json**: Define x,y coordinates and emoji
3. **Update field mappings**: Add FK patterns if needed

### Step 4: Position on ERD

Choose coordinates based on thematic area:
- Maintain 300px+ spacing from existing entities
- Position within appropriate thematic zone
- Consider relationship density for optimal placement

### Step 5: Add Relationship Examples

Include concrete examples in relationship definitions to help users understand connections.

## Maintenance Guide

### Regular Maintenance Tasks

1. **Update Entity Counts**: Sync total_entities in directories.json
2. **Review Positioning**: Check for overlaps after adding entities
3. **Validate Relationships**: Ensure all FK references are valid
4. **Update Examples**: Keep relationship examples current and realistic

### Troubleshooting Common Issues

**Entity Not Appearing**:
- Check directories.json includes entity directory
- Verify validation_schema.json has valid boost_metadata
- Confirm entity name matches exactly between files

**Relationship Not Showing**:
- Verify targetEntity name matches exactly
- Check field name exists in schema properties
- Ensure field_mappings includes FK patterns

**Positioning Issues**:
- Check for coordinate conflicts (< 300px spacing)
- Verify coordinates are within reasonable bounds
- Test zoom/pan behavior after changes

**Color/Theme Issues**:
- Confirm area category is one of 7 standard values
- Check color definitions in erd-config.json areas section
- Verify emoji renders correctly across platforms

### Performance Considerations

- **Schema File Size**: Keep validation schemas under 100KB for fast loading
- **Relationship Count**: More than 100 relationships may impact performance
- **Entity Count**: Monitor performance with >40 entities
- **Image Assets**: Optimize emoji rendering for slower connections

### Best Practices

1. **Consistent Naming**: Use PascalCase for entity names, camelCase for fields
2. **Clear Examples**: Make relationship examples specific and realistic
3. **Logical Grouping**: Position related entities near each other
4. **Progressive Enhancement**: Add complexity gradually, test frequently
5. **Documentation**: Update this guide when making structural changes

---

For additional support, refer to:
- **ERD Navigator README**: Basic usage and features
- **Schema README**: Schema development guidelines  
- **GitHub Discussions**: Community feedback and entity-specific discussions