# BOOST ERD Navigator Quick Reference

Quick reference guide for common ERD maintenance tasks. For comprehensive documentation, see [ERD_CONFIGURATION.md](ERD_CONFIGURATION.md).

## 🚀 Quick Actions

### Adding a New Entity

1. **Create schema directory**: `mkdir drafts/current/schema/new_entity/`
2. **Create validation_schema.json** with boost_metadata:
   ```json
   {
     "boost_metadata": {
       "entity": {
         "name": "NewEntity",
         "primaryKey": "newEntityId", 
         "area": "core_traceability",
         "description": "🆕 New entity description"
       },
       "relationships": []
     }
   }
   ```
3. **Add to directories.json**: Include in `schema_directories` array
4. **Add position to erd-config.json**:
   ```json
   "NewEntity": {
     "emoji": "🆕",
     "position": {"x": 1600, "y": 800}
   }
   ```

### Adding a Relationship

Add to `boost_metadata.relationships` in source entity schema:
```json
{
  "field": "targetEntityId",
  "targetEntity": "TargetEntity", 
  "relationshipType": "many-to-one",
  "required": true,
  "label": "relationship description",
  "example": "Entity-123 relates to 'Target Company Name'"
}
```

### Positioning an Entity

Update coordinates in `erd-config.json`:
```json
"EntityName": {
  "emoji": "📦",
  "position": {"x": 1600, "y": 1200}
}
```

**Coordinate Guidelines**:
- **Center Hub**: TraceableUnit at (1600, 1200)
- **Top (y=100)**: Geographic & Tracking
- **Left (x=100)**: Organizational Foundation & Material Supply Chain
- **Right (x=2700+)**: Transaction Management & Reporting
- **Minimum Spacing**: 300px between entities

### Adding Relationship Examples

Include realistic examples in relationship definitions:
```json
{
  "example": "TRU-456 is harvested by 'Olympic Forest Products'"
}
```

**Example Guidelines**:
- Use realistic IDs (TRU-123, ORG-001, etc.)
- Put organization names in quotes
- Keep under 100 characters
- Show concrete business scenarios

## 📍 Positioning Zones

### Hub-and-Spoke Layout
```
           Geographic & Tracking (🟣)
                   y=100
                     |
Organizational  ── Core ── Measurement &
Foundation         Hub      Verification  
(🔵) x=100      (🟢 Center)   (🟡) x=2700+
                     |
           Material & Supply Chain
               (🟤) y=2000
```

### Thematic Area Coordinates

| Area | X Range | Y Range | Color |
|------|---------|---------|-------|
| Core Traceability | 1300-1900 | 1000-1400 | 🟢 Green |
| Organizational Foundation | 100-700 | 400-700 | 🔵 Blue |
| Material & Supply Chain | 100-1600 | 2000+ | 🟤 Brown |
| Transaction Management | 2700+ | 400+ | 🟠 Orange |
| Measurement & Verification | 2700+ | 100+ | 🟡 Yellow |
| Geographic & Tracking | 100-400 | 100+ | 🟣 Purple |
| Compliance & Reporting | 2700+ | 2000+ | 🔴 Red |

## 🎨 Visual Design System

### Thematic Categories
Choose from these 7 standard categories for consistent coloring:

- `"core_traceability"` - 🟢 Green
- `"organizational_foundation"` - 🔵 Blue
- `"material_supply_chain"` - 🟤 Brown  
- `"transaction_management"` - 🟠 Orange
- `"measurement_verification"` - 🟡 Yellow
- `"geographic_tracking"` - 🟣 Purple
- `"compliance_reporting"` - 🔴 Red

### Common Emojis by Category

| Category | Common Emojis |
|----------|---------------|
| Core Traceability | 📦 🔄 ⚙️ 📍 🔬 |
| Organizational | 🏢 📜 🏛️ 🔍 👤 |
| Material & Supply | 🪵 🌲 🚚 🏭 🌍 |
| Transaction | 💰 📋 📄 |
| Measurement | 📏 ✅ 🔐 |
| Geographic | 🗺️ 📌 |
| Reporting | 📊 📈 ⚡ |

## 🔧 Configuration Files

### Key Files
- **`erd-config.json`**: Entity positions, emojis, manual relationships
- **`directories.json`**: Schema directory manifest
- **`boost_metadata_schema.json`**: Metadata structure definition
- **Individual schema files**: Entity definitions and relationships

### Critical Fields in boost_metadata
```json
{
  "entity": {
    "name": "EntityName",        // Must match exactly
    "primaryKey": "entityId",    // Field name of primary key
    "area": "thematic_category", // One of 7 standard categories
    "description": "Description" // Brief description (emoji optional)
  },
  "relationships": [             // All relationships from this entity
    {
      "field": "foreignKeyField",
      "targetEntity": "TargetEntity",
      "relationshipType": "many-to-one",
      "required": true,
      "label": "human readable label",
      "example": "Concrete example"
    }
  ]
}
```

## 🐛 Troubleshooting

### Entity Not Appearing
- ✅ Check directories.json includes entity directory
- ✅ Verify boost_metadata.entity.name matches exactly
- ✅ Ensure validation_schema.json has valid JSON
- ✅ Check browser console for errors

### Relationship Not Showing
- ✅ Verify targetEntity name matches exactly (case-sensitive)
- ✅ Ensure both source and target entities exist
- ✅ Check field name exists in schema properties
- ✅ Confirm no typos in relationship definition

### Positioning Issues
- ✅ Check for coordinate conflicts (< 300px spacing)
- ✅ Verify coordinates are within bounds (0-3600, 0-2400)
- ✅ Ensure entity has position in erd-config.json
- ✅ Test zoom/pan behavior after changes

### Color/Theme Issues
- ✅ Confirm area is one of 7 standard values
- ✅ Check color definitions in erd-config.json
- ✅ Verify emoji renders correctly
- ✅ Ensure consistent thematic grouping

## ⚡ Performance Tips

- Keep schema files under 100KB
- Limit to ~40 entities for optimal performance  
- Use descriptive but concise relationship examples
- Minimize complex nested objects in schemas
- Test frequently during development

## 🔄 Common Workflows

### Moving an Entity
1. Update position in `erd-config.json`
2. Ensure 300px+ spacing from other entities
3. Test zoom and pan behavior
4. Verify relationships still draw correctly

### Changing Entity Category
1. Update `area` in boost_metadata
2. Consider moving position to new thematic zone
3. Update colors if needed in erd-config.json
4. Test filtering functionality

### Adding Multiple Relationships
1. Add all relationships to source entity's boost_metadata
2. Ensure target entities exist and have boost_metadata
3. Test relationship examples by clicking lines
4. Verify no relationship line overlaps

### Updating Field Names
1. Update schema properties section
2. Update any referencing foreign key fields
3. Update boost_metadata relationships if affected
4. Test ERD field display updates correctly

## 📚 Documentation Links

- **[ERD_CONFIGURATION.md](ERD_CONFIGURATION.md)**: Comprehensive configuration guide
- **[README.md](README.md)**: ERD Navigator features and usage
- **[../drafts/current/schema/README.md](../drafts/current/schema/README.md)**: Schema development guide
- **[boost_metadata_schema.json](../drafts/current/schema/boost_metadata_schema.json)**: Metadata structure definition

## 🆘 Getting Help

1. **Check browser console** for error messages
2. **Validate JSON** syntax in schema files
3. **Compare working entities** for reference patterns
4. **Test incrementally** - add one change at a time
5. **Reference existing entities** for naming conventions

---

*For detailed explanations and advanced configuration, see the full [ERD Configuration Guide](ERD_CONFIGURATION.md).*