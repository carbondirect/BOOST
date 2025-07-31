# BOOST Python Reference Implementation - Schema Change Propagation Guide

## Overview

The BOOST Python reference implementation uses a **dynamic, schema-driven architecture** that automatically adapts to changes in the BOOST JSON schemas. This document explains how schema changes propagate through the system and identifies any manual updates that may be required.

## Architecture Overview

The reference implementation consists of three main components:

1. **Schema Loader** (`schema_loader.py`) - Dynamically loads schemas and generates models
2. **Dynamic Validator** (`dynamic_validation.py`) - Validates entities using current schema rules
3. **BOOST Client** (`boost_client.py`) - Main API that uses dynamic models

## Automatic Schema Change Propagation

### ✅ Changes That Require NO Manual Updates

The following schema changes are handled automatically without any code modifications:

#### 1. Adding New Fields to Existing Entities
- **What happens**: New fields are automatically added to dynamic Pydantic models
- **Validation**: New required fields will cause validation errors until data includes them
- **Example**: Adding `carbonFootprint` field to `TraceableUnit`

```json
// Schema change - no code changes needed
{
  "properties": {
    "carbonFootprint": {
      "type": "number",
      "minimum": 0,
      "description": "Carbon footprint in kg CO2 equivalent"
    }
  },
  "required": ["carbonFootprint"]  // Will be enforced automatically
}
```

#### 2. Adding New Enum Values
- **What happens**: Dynamic enums are regenerated with new values
- **Validation**: New enum values become immediately available
- **Example**: Adding new organization types

```json
// Schema change - no code changes needed
{
  "organizationType": {
    "enum": ["harvester", "processor", "certifier", "new_type"]
  }
}
```

#### 3. Adding New Entity Types
- **What happens**: New entity schemas are automatically discovered and loaded
- **Models**: Dynamic models are generated for new entities
- **Example**: Adding `CarbonCredit` entity

```json
// New file: schema/carbon_credit/validation_schema.json
// Automatically discovered and loaded
```

#### 4. Modifying Field Constraints
- **What happens**: New validation rules are applied automatically
- **Validation**: Updated min/max lengths, patterns, ranges are enforced
- **Example**: Changing phone number pattern

```json
// Schema change - validation updates automatically
{
  "contactPhone": {
    "pattern": "^\\+[1-9]\\d{1,14}$"  // New pattern enforced immediately
  }
}
```

#### 5. Adding New Business Logic Rules
- **What happens**: New rules in `business_logic_validation.json` are automatically loaded
- **Validation**: New business rules are enforced immediately
- **Example**: Adding price validation rules

```json
// Schema change - no code changes needed
{
  "economicLogicRules": {
    "pricingReasonableness": {
      "newPriceType": {
        "rule": {"const": "price_within_range"},
        "validation": {"min": 10, "max": 1000}
      }
    }
  }
}
```

#### 6. Updating Relationship Definitions
- **What happens**: Foreign key relationships are rediscovered automatically
- **Validation**: New relationship constraints are enforced
- **Example**: Adding new foreign key relationships

## Manual Updates Required

### ⚠️ Changes That May Require Manual Updates

#### 1. Renaming Entity Types

**Impact**: High - requires code changes in multiple places

**Schema Change**:
```json
// Old: traceable_unit -> New: traceable_item
```

**Required Manual Updates**:
```python
# boost_client.py - Update method names and storage keys
def create_traceable_item(self, ...):  # Renamed from create_traceable_unit
    # ...
    self.traceable_items[item_id] = item  # Update storage dict name

# examples/*.py - Update method calls
item = client.create_traceable_item(...)  # Update all example calls
```

**Search Commands**:
```bash
# Find all references to old entity name
grep -r "traceable_unit" python/
grep -r "TraceableUnit" python/
```

#### 2. Renaming Core Fields (Primary Keys, Foreign Keys)

**Impact**: High - affects relationships and lookups

**Schema Change**:
```json
// Old: organizationId -> New: orgId
```

**Required Manual Updates**:
```python
# boost_client.py - Update field access
org_data = org.model_dump(by_alias=True)
org_id = org_data['orgId']  # Update field name

# dynamic_validation.py - Update primary key mappings if hardcoded
```

#### 3. Major Structural Changes

**Impact**: High - may require architectural updates

**Examples**:
- Changing from flat structure to nested objects
- Moving fields between entities
- Changing relationship cardinality (one-to-many → many-to-many)

**Required Manual Updates**:
- Update client methods that assume specific structures
- Modify example code that depends on field locations
- Update business logic validators that reference moved fields

#### 4. Adding New Client Methods for New Entities

**Impact**: Medium - enhances functionality

**When**: Adding entirely new entity types that need creation methods

**Required Manual Updates**:
```python
# boost_client.py - Add new creation method
def create_carbon_credit(self, credit_id: str, **kwargs) -> Any:
    # Validate against new schema
    # Create using dynamic model
    # Store in new storage dict
    pass
```

#### 5. Updating Example Code for New Required Fields

**Impact**: Medium - examples may fail validation

**When**: New required fields are added to existing entities

**Required Manual Updates**:
```python
# examples/*.py - Add new required fields
harvester = client.create_organization(
    # ... existing fields ...
    new_required_field="value"  # Add new required field
)
```

## Schema Change Detection and Testing

### Automated Detection

The system provides built-in schema change detection:

```python
from boost_client import create_client

client = create_client()

# Check current schema info
schema_info = client.get_schema_info()
print(f"Available entities: {schema_info['available_entities']}")

# Check available enum values
org_types = client.get_available_enum_values('organization', 'organizationType')
print(f"Organization types: {org_types}")

# Test validation with new schema
is_valid, errors = client.validator.validate_entity('organization', test_data)
```

### Validation Testing

After schema changes, test validation:

```python
# Test that new fields are properly validated
try:
    org = client.create_organization("TEST-001", "Test Org", "harvester")
    print("✅ Schema changes working correctly")
except ValueError as e:
    print(f"⚠️ Manual update needed: {e}")
```

### Compatibility Testing

```python
# Test backward compatibility
validation_results = client.validate_all()
if not validation_results['valid']:
    print("⚠️ Schema changes broke existing data:")
    for error in validation_results['errors']:
        print(f"  - {error}")
```

## Best Practices for Schema Changes

### 1. Incremental Changes
- Make small, incremental schema changes rather than large restructuring
- Test each change individually before combining

### 2. Backward Compatibility
- When possible, make new fields optional initially
- Use deprecation warnings before removing fields
- Provide migration paths for breaking changes

### 3. Testing Workflow
1. **Update schemas** in the schema directory
2. **Run schema refresh**: `client.refresh_schemas()`
3. **Test examples**: Run all example scripts to check for errors
4. **Check validation**: Run comprehensive validation on existing data
5. **Update code**: Make any necessary manual updates identified above

### 4. Documentation
- Document all breaking changes in schema changelog
- Update example code to demonstrate new features
- Provide migration guides for complex changes

## Migration Checklist

When schema changes are made, use this checklist:

### Automatic Propagation (No Action Needed)
- [ ] New optional fields added
- [ ] New enum values added  
- [ ] Field constraints modified (min/max, patterns)
- [ ] New business logic rules added
- [ ] New entity types added

### Manual Updates Required
- [ ] Entity types renamed → Update client methods and examples
- [ ] Core fields renamed → Update field access code
- [ ] Required fields added → Update example code
- [ ] Structural changes → Review and update affected code
- [ ] New entities need client methods → Add creation methods

### Testing Required
- [ ] Run all example scripts
- [ ] Test validation with existing data
- [ ] Test creation of all entity types
- [ ] Verify enum values are correctly loaded
- [ ] Check foreign key validation still works

## Troubleshooting Common Issues

### Schema Loading Errors
```python
# Check if schemas are loading correctly
client = create_client()
entities = client.schema_loader.get_all_entity_types()
if not entities:
    print("❌ Schemas not loading - check file paths")
```

### Validation Errors After Changes
```python
# Check what validation errors occur
try:
    entity = client.create_organization("TEST", "Test", "harvester")
except Exception as e:
    print(f"Validation error: {e}")
    # Check if new required fields need to be added
```

### Enum Value Errors
```python
# Check available enum values
available = client.get_available_enum_values('organization', 'organizationType')
print(f"Valid values: {available}")
```

## Performance Considerations

### Schema Refresh Frequency
- Schemas are loaded once at client initialization
- Call `client.refresh_schemas()` to reload after changes
- Consider caching strategy for production environments

### Memory Usage
- Dynamic models are generated once and cached
- Large schemas may increase memory usage
- Monitor memory usage in production deployments

## Conclusion

The BOOST Python reference implementation's schema-driven architecture provides excellent resilience to schema changes. Most changes require no manual updates, and the system provides clear feedback when manual updates are needed. Following the guidelines in this document will ensure smooth schema evolution while maintaining system reliability.
