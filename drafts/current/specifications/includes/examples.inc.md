This section provides practical examples of BOOST data structures and common implementation patterns to help developers understand how to work with the standard.

All examples use the JSON-LD format with the BOOST context definition to ensure semantic interoperability.

## Python Implementation Examples

### Basic Client Usage

```python
from boost_client import create_client

# Initialize BOOST client with dynamic schema loading
client = create_client()

# Check what entities and enums are available from current schemas
schema_info = client.get_schema_info()
print(f"Available entities: {schema_info['available_entities']}")

# Get valid enum values dynamically from schemas
org_types = client.get_available_enum_values('organization', 'organizationType')
print(f"Valid organization types: {org_types}")
```

### Creating Organizations

```python
# Create an organization using schema-validated enum values
harvester = client.create_organization(
    organization_id="ORG-FOREST-001",
    name="Pacific Forest Products",
    org_type="harvester",  # Validated against current schema
    contact_email="ops@pacificforest.com",
    contact_phone="+15415550123"  # Must match schema pattern
)
```

### Creating TraceableUnits

```python
# Get available unit types from schema
unit_types = client.get_available_enum_values('traceable_unit', 'unitType')
print(f"Valid unit types: {unit_types}")

# Create a traceable unit with all required fields
harvester_data = harvester.model_dump(by_alias=True)
log_pile = client.create_traceable_unit(
    traceable_unit_id="TRU-LOGS-001",
    unit_type="pile",  # Validated against current schema
    harvester_id=harvester_data['organizationId'],
    total_volume_m3=125.5,
    sustainability_certification="FSC Mix Credit 70%",
    unique_identifier="RFID-001-A",  # Required by schema
    is_multi_species=False  # Required by schema
)
```

### Comprehensive Validation

```python
# Comprehensive validation using dynamic business rules
validation = client.validate_all()
if validation['valid']:
    print("✓ All entities are valid!")
else:
    print("✗ Schema and business logic validation errors:")
    for error in validation['errors']:
        print(f"  - {error}")

# Export to JSON-LD
jsonld_output = client.export_to_jsonld()
print(jsonld_output)
```

## Supply Chain Workflow Example

### Complete Harvest-to-Processing Chain

```python
# 1. Create harvest operation
harvest_site = client.create_geographic_data(
    geographic_data_id="GEO-HARVEST-SITE-001",
    coordinates={"type": "Point", "coordinates": [-123.1234, 45.6789]},
    location_type="harvest_site"
)

# 2. Create individual log TRUs
individual_logs = []
for i in range(1, 6):  # 5 logs
    log = client.create_traceable_unit(
        traceable_unit_id=f"TRU-LOG-{i:03d}",
        unit_type="individual_log",
        harvester_id="ORG-FOREST-001",
        total_volume_m3=2.5,
        unique_identifier=f"BIO-DOUGLAS-FIR-{i:03d}",
        harvest_geographic_data_id=harvest_site.geographicDataId,
        is_multi_species=False
    )
    individual_logs.append(log)

# 3. Create pile aggregation
log_pile = client.create_traceable_unit(
    traceable_unit_id="TRU-PILE-001",
    unit_type="pile",
    harvester_id="ORG-FOREST-001",
    total_volume_m3=12.5,  # Sum of individual logs
    unique_identifier="PILE-ROADSIDE-001",
    parent_traceable_unit_ids=[log.traceableUnitId for log in individual_logs],
    is_multi_species=False
)

# 4. Document processing operation
processing_op = client.create_material_processing(
    processing_id="PROC-SAWMILL-001",
    process_type="primary_breakdown",
    input_traceable_unit_ids=[log_pile.traceableUnitId],
    process_timestamp="2025-08-01T10:30:00Z",
    facility_id="FAC-SAWMILL-PORTLAND"
)
```