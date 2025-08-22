# BOOST Python Migration Guide: Static to Dynamic Models

This guide documents the migration from static Pydantic models to the dynamic, schema-driven architecture as promised in the README.

## What Changed

### Before: Static Models (Removed)
```python
from models import Organization, TraceableUnit, OrganizationType, UnitType
```

### After: Dynamic Models  
```python
from dynamic_models import get_models, OrganizationType, UnitType

# Get models dynamically from schemas
models = get_models()
Organization = models.get_model('organization')
TraceableUnit = models.get_model('traceable_unit')
```

## Migration Steps

### 1. Update Imports

**Old approach:**
```python
from models import Organization, TraceableUnit, Transaction
from models import OrganizationType, UnitType, ProcessType, ClaimType
```

**New approach:**
```python
from dynamic_models import get_models, OrganizationType, UnitType, ProcessType
# For backward compatibility, enums are still available as classes
```

### 2. Get Model Classes Dynamically

**Old approach:**
```python
org = Organization(
    organizationId="ORG-001",
    organizationName="Forest Co",
    organizationType=OrganizationType.HARVESTER
)
```

**New approach:**
```python
models = get_models()
Organization = models.get_model('organization')

org = Organization(
    organizationId="ORG-001", 
    organizationName="Forest Co",
    organizationType=OrganizationType.HARVESTER  # Still works!
)
```

### 3. Use String Values Directly (Recommended)

**Even better approach:**
```python
models = get_models()
Organization = models.get_model('organization')

# Use strings directly - always valid with current schema
org = Organization(
    organizationId="ORG-001",
    organizationName="Forest Co", 
    organizationType="harvester"  # String values from schema
)
```

### 4. Validate Enum Values

```python
models = get_models()

# Get valid enum values for validation
org_types = models.get_enum_values('organization', 'organizationType')
print(f"Valid org types: {org_types}")  # ['harvester', 'processor', ...]

# Validate before creating
if org_type in org_types:
    org = models.get_model('organization')(organizationType=org_type, ...)
```

## Benefits of Dynamic Models

### 1. Always Current
Models are generated from JSON schemas at runtime, so they always reflect the latest schema definitions.

### 2. No Synchronization Issues  
No more mismatches between static Python models and JSON schemas.

### 3. Complete Coverage
All 36 BOOST entities are available dynamically, not just the 8 that were hand-coded.

### 4. Easier Maintenance
Schema changes automatically propagate to Python models without code updates.

## Backward Compatibility

The new `dynamic_models.py` provides backward compatibility:

```python
# These still work for existing code:
from dynamic_models import OrganizationType, UnitType, ProcessType

org_type = OrganizationType.HARVESTER  # Returns "harvester" 
unit_type = UnitType.INDIVIDUAL_LOG    # Returns "individual_log"
```

## Available Entities

The dynamic system provides access to all 36 BOOST entities:

```python
models = get_models()

# Core entities
Organization = models.get_model('organization')
TraceableUnit = models.get_model('traceable_unit') 
Transaction = models.get_model('transaction')
MaterialProcessing = models.get_model('material_processing')

# All other entities are now available too:
Certificate = models.get_model('certificate')
Equipment = models.get_model('equipment')
GeographicData = models.get_model('geographic_data')
# ... and 29 more
```

## Best Practices

### 1. Use String Values
Prefer string enum values over enum classes for better schema alignment:

```python
# Good
org = Organization(organizationType="harvester")

# Still works, but string is better
org = Organization(organizationType=OrganizationType.HARVESTER)
```

### 2. Validate Dynamically  
Use schema-based validation instead of static type checking:

```python
models = get_models()

# Validate enum values dynamically
valid_types = models.get_enum_values('organization', 'organizationType')
if org_type not in valid_types:
    raise ValueError(f"Invalid org type. Valid types: {valid_types}")
```

### 3. Cache Model Classes
If creating many instances, cache the model class:

```python
models = get_models()
Organization = models.get_model('organization')  # Cache this

# Create many instances
orgs = [Organization(...) for _ in range(100)]
```

## Testing Updates

Test files now import from `dynamic_models` instead of `models`:

```python
# test_bioram_validation.py
from dynamic_models import get_models

def test_validation():
    models = get_models()
    BioramPathway = models.get_model('bioram_pathway')
    pathway = BioramPathway(...)
```

## Schema Path Configuration

By default, dynamic models load schemas from `../../schema` relative to the Python files. You can specify a different path:

```python
from dynamic_models import get_models

# Use custom schema path
models = get_models(schema_path="/path/to/boost/schemas")
```

## Troubleshooting

### Entity Not Found
```python
# If you get "Entity 'foo' not found"
models = get_models()
available = models.list_entities()
print(f"Available entities: {available}")
```

### Enum Not Found  
```python
# If you get "Enum 'entity.field' not found"
models = get_models()
available_enums = models.list_enums()
print(f"Available enums: {available_enums}")
```

### Schema Loading Errors
Make sure the schema path is correct and contains valid JSON schema files:

```python
from pathlib import Path

schema_path = Path("../../schema").resolve()
print(f"Schema path exists: {schema_path.exists()}")
print(f"Schema contents: {list(schema_path.iterdir())}")
```

This migration ensures the BOOST Python implementation truly delivers on its promise of being a "Dynamic Schema-Driven Architecture."