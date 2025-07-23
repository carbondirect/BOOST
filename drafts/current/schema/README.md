# BOOST Schema Directory

This directory contains JSON schema definitions for all BOOST entities. These schema files serve as the single source of truth for entity structure and are automatically consumed by the BOOST ERD visualization.

## Overview

Each entity in the BOOST data model has its own subdirectory containing:
- `validation_schema.json` - JSON schema definition with field types, constraints, and validation rules
- `*_example.json` - Example data instances 
- `*_dictionary.md` - Human-readable field descriptions

## Directory Structure

```
schema/
├── traceable_unit/           # Core entity for biomass tracking
│   ├── validation_schema.json
│   ├── traceable_unit_example.json
│   └── traceable_unit_dictionary.md
├── material/                 # Material types and specifications  
│   ├── validation_schema.json
│   ├── material_example.json
│   └── material_dictionary.md
├── organization/             # Business entities
├── transaction/              # Business transactions
├── [22+ other entities]/
└── README.md                 # This file
```

## Schema Integration with ERD

The BOOST ERD Navigator (`../../erd-navigator/index.html`) **dynamically loads these schema files** instead of using hardcoded definitions. This means:

✅ **Schema changes automatically appear in the ERD**  
✅ **Field additions/removals are immediately reflected**  
✅ **Type changes update ERD display**  
✅ **Single source of truth maintained**

### For Schema Maintainers

When you modify a `validation_schema.json` file:
1. **Add/remove fields**: They automatically appear/disappear in the ERD
2. **Change field types**: ERD display updates to reflect new types  
3. **Modify required fields**: ERD styling updates accordingly
4. **Update descriptions**: Available for future tooltip integration

## Quick Start

To see your schema changes in the ERD:

1. **Edit any `validation_schema.json` file** in this directory
2. **Refresh the ERD Navigator** (`../../erd-navigator/index.html`)
3. **Changes appear automatically** - no manual updates needed

### Example: Adding a Field

```json
{
  "schema": {
    "properties": {
      "existingField": {"type": "string"},
      "newField": {                    # ← Add this
        "type": "string",
        "description": "My new field"
      }
    },
    "required": ["existingField", "newField"]  # ← Add to required if needed
  }
}
```

The ERD will automatically show `newField` in the entity with appropriate styling.

## Architecture

### Components

1. **Schema Loading (`loadSchemaFile`)**
   - Fetches JSON schema files from the file system
   - Handles missing files gracefully
   - Uses proper path conversion for entity names

2. **Schema Conversion (`convertSchemaToEntity`)**
   - Converts JSON schema properties to ERD field format
   - Automatically detects primary and foreign keys
   - Maps schema types to display types

3. **Entity Metadata (`entityMetadata`)**
   - Maintains visual positioning and styling information
   - Preserves entity area assignments and descriptions

4. **Async Initialization (`loadEntitiesFromSchema`)**
   - Orchestrates the loading and conversion process
   - Provides fallback to static definitions

## File Structure

```
/drafts/current/
├── images/current/
├── erd-navigator/
│   └── index.html                      # Main ERD Navigator with dynamic loading
│   └── DYNAMIC_SCHEMA_LOADING.md       # This documentation
└── schema/
    ├── traceable_unit/
    │   └── validation_schema.json       # TraceableUnit schema
    ├── material/
    │   └── validation_schema.json       # Material schema
    └── [other entities]/
        └── validation_schema.json
```

## Schema File Path Convention

Entity names are converted to file paths using the following pattern:
- `TraceableUnit` → `traceable_unit/validation_schema.json`
- `MaterialProcessing` → `material_processing/validation_schema.json`
- `EnergyCarbonData` → `energy_carbon_data/validation_schema.json`

**Conversion Rule**: CamelCase → snake_case with underscores

## Schema to ERD Mapping

### Field Type Mapping

| Schema Type | ERD Display Type | Notes |
|-------------|------------------|-------|
| `string` | `string` | Default string type |
| `number` | `decimal` | Numeric values |
| `integer` | `integer` | Whole numbers |
| `boolean` | `boolean` | True/false values |
| `array` | `array` | List of items |
| `object` | `object` | Complex nested data |
| `string` with `enum` | `enum` | Enumerated values |
| `string` with `format: "date-time"` | `datetime` | Timestamps |

### Key Detection Rules

#### Primary Keys (PK)
A field is considered a Primary Key if:
- Field name contains "id" (case-insensitive)
- AND field name contains the entity name (case-insensitive)
- OR field name is exactly "id"

**Examples**: 
- `traceableUnitId` in TraceableUnit entity ✅
- `materialId` in Material entity ✅
- `id` in any entity ✅

#### Foreign Keys (FK)
A field is considered a Foreign Key if:
- Field name ends with "Id"
- AND it's not a Primary Key

**Examples**:
- `organizationId` ✅
- `materialTypeId` ✅
- `currentGeographicDataId` ✅

### Required Fields
Fields are marked as required based on the `required` array in the JSON schema.

### Ignored Fields
The following JSON-LD context fields are automatically excluded:
- `@context`
- `@type` 
- `@id`

## Entity Metadata Configuration

Each entity requires metadata for visual display:

```javascript
const entityMetadata = {
    'EntityName': {
        area: 'functional_area',           // Color/grouping area
        description: 'Entity description', // Tooltip description
        position: { x: 100, y: 200 }      // ERD coordinates
    }
};
```

### Functional Areas

| Area | Color | Description |
|------|-------|-------------|
| `core_traceability` | 🟢 Green | Central tracking entities |
| `organizational_foundation` | 🔵 Blue | Business entities |
| `material_supply_chain` | 🟤 Brown | Material and supply entities |
| `transaction_management` | 🟠 Orange | Transaction entities |
| `sustainability_claims` | 🟡 Yellow | Sustainability entities |
| `geographic_location` | 🟣 Purple | Location entities |
| `reporting_compliance` | 🔴 Red | Reporting entities |
| `analytics_data` | ⚫ Black | Analytics entities |
| `personnel` | 👥 Gray | Personnel entities |

## Usage

### Loading Process

1. **Initialization**: When the ERD loads, it calls `initializeVisualization()`
2. **Schema Loading**: `loadEntitiesFromSchema()` fetches all schema files
3. **Conversion**: Each schema is converted to ERD entity format
4. **Rendering**: Entities are drawn with their schema-defined fields
5. **Fallback**: If loading fails, static entities are used as backup

### Console Output

The loading process provides detailed console logging:

```
Loaded 25 entities from schema files
```

Or in case of issues:
```
Could not load schema for EntityName: 404
No entities loaded from schemas, falling back to static entities
```

## Error Handling

### Missing Schema Files
- Individual missing files are logged as warnings
- ERD continues loading other entities
- Falls back to static definition if available

### Network Issues
- Fetch errors are caught and logged
- ERD falls back to static entities completely
- User sees visual feedback in console

### Invalid Schema Format
- Malformed JSON is handled gracefully
- Entity is skipped with warning message
- ERD continues with remaining entities

## Benefits

### For Developers
- ✅ Single source of truth for entity definitions
- ✅ Automatic synchronization between schema and ERD
- ✅ No manual maintenance of duplicate entity lists
- ✅ Type safety and consistency validation

### For Schema Maintenance
- ✅ Changes to JSON schemas immediately reflect in ERD
- ✅ Field additions/removals are automatically detected
- ✅ Type changes are reflected in visual display
- ✅ Required field changes update styling

## Future Enhancements

This foundation enables several future features:

### Live Editing
- Real-time schema editing interface
- Immediate ERD updates on schema changes
- Schema validation and error reporting

### Advanced Features
- Schema diff visualization
- Version control integration
- Collaborative editing capabilities
- Export functionality to various formats

## Troubleshooting

### ERD Shows Static Entities Instead of Schema
**Problem**: ERD falls back to hardcoded entities
**Solutions**:
1. Check browser console for error messages
2. Verify schema file paths are correct
3. Ensure schema files have valid JSON format
4. Check file permissions and accessibility

### Missing Entities in ERD
**Problem**: Some entities don't appear in the visualization
**Solutions**:
1. Verify entity name exists in `entityMetadata`
2. Check schema file exists at expected path
3. Ensure schema has valid `properties` section
4. Look for console warning messages

### Incorrect Field Types or Keys
**Problem**: Fields show wrong types or PK/FK detection is incorrect
**Solutions**:
1. Review field naming conventions for key detection
2. Check schema type definitions match expected mappings
3. Verify `required` array includes intended fields
4. Update type mapping logic if needed

### Performance Issues
**Problem**: ERD loads slowly
**Solutions**:
1. Check network performance for schema file loading
2. Consider adding loading indicators
3. Implement schema caching for repeated loads
4. Optimize schema file sizes

## Technical Implementation Details

### Schema Loading Function
```javascript
async function loadSchemaFile(entityName) {
    const schemaPath = `../../schema/${entityName.toLowerCase().replace(/([A-Z])/g, '_$1').substring(1)}/validation_schema.json`;
    const response = await fetch(schemaPath);
    return await response.json();
}
```

### Type Detection Logic
```javascript
// Primary Key Detection
if (fieldName.toLowerCase().includes('id') && 
    (fieldName.toLowerCase().includes(entityName.toLowerCase()) || fieldName === 'id')) {
    isPK = true;
}

// Foreign Key Detection  
if (fieldName.endsWith('Id') && !isPK && fieldName !== 'id') {
    isFK = true;
}
```

### Entity Structure Output
```javascript
{
    id: 'EntityName',
    name: 'EntityName', 
    area: 'functional_area',
    description: 'Entity description',
    fields: [
        {
            name: 'fieldName',
            type: 'fieldType',
            isPK: boolean,
            isFK: boolean,
            required: boolean
        }
    ],
    x: number,
    y: number
}
```

---

*This documentation reflects the implementation as of the dynamic schema loading integration. For questions or issues, check the browser console output and verify schema file accessibility.*