# BOOST Python Reference Implementation

A comprehensive Python library for working with the BOOST (Biomass Open Origin Standard for Tracking) standard, providing **dynamic, schema-driven** data models, validation, and supply chain tracking capabilities for biomass chain of custody operations.

## Overview

This reference implementation demonstrates how to use the BOOST standard in Python applications, providing:

- **🔄 Dynamic Schema-Driven Architecture**: Automatically adapts to schema changes without code modifications
- **✅ Comprehensive Validation**: Schema, business logic, and cross-entity validation
- **🏗️ Dynamic Model Generation**: Pydantic models generated directly from JSON schemas
- **📋 Configuration-Driven Business Rules**: 8 categories of business logic validation from schema configuration
- **🔗 Supply Chain Tracking**: Complete traceability with automatic relationship discovery
- **🏷️ Multi-Certification Support**: FSC, SBP, PEFC, ISCC, RED II compliance
- **⚖️ Mass Balance Accounting**: Volume and mass conservation with tolerance checking
- **🌐 JSON-LD Export/Import**: Full semantic web compatibility
- **🛡️ Schema Version Compatibility**: Graceful handling of schema evolution

## Recent Updates: Full Dynamic Architecture

**🎉 The Python implementation now fully delivers on its promise of "Dynamic Schema-Driven Architecture"!**

- **✅ All models generated dynamically** from JSON schemas at runtime
- **✅ No more static model files** to maintain or synchronize  
- **✅ Always current** - models automatically reflect schema changes
- **✅ Complete entity coverage** - all 36 BOOST entities available dynamically

See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for details on migrating from the old static models approach.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Core Dependencies

- `pydantic>=2.0.0` - Data validation and settings management
- `jsonschema>=4.0.0` - JSON Schema validation
- `requests>=2.28.0` - HTTP library for API calls
- `pyld>=2.0.0` - JSON-LD processor

## Quick Start

### Basic Usage

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

# Create an organization using schema-validated enum values
harvester = client.create_organization(
    organization_id="ORG-FOREST-001",
    name="Pacific Forest Products",
    org_type="harvester",  # Validated against current schema
    contact_email="ops@pacificforest.com",
    contact_phone="+15415550123"  # Must match schema pattern
)

# Get available unit types from schema
unit_types = client.get_available_enum_values('traceable_unit', 'unitType')
print(f"Valid unit types: {unit_types}")

# Create a traceable unit with all required fields (discovered from schema)
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

## Core Components

### 1. Schema Loader (`schema_loader.py`)

**Dynamic schema loading and model generation engine:**

```python
from schema_loader import SchemaLoader

# Automatically discovers and loads all BOOST schemas
loader = SchemaLoader()

# Get dynamically generated Pydantic models
OrganizationModel = loader.get_model('organization')
TraceableUnitModel = loader.get_model('traceable_unit')

# Get enum values directly from schemas
org_types = loader.get_field_enum_values('organization', 'organizationType')
print(f"Valid organization types: {org_types}")

# Get relationship information discovered from schemas
relationships = loader.get_relationships('traceable_unit')
primary_key = loader.get_primary_key('organization')
```

**Key Features:**
- **Automatic Schema Discovery**: Finds and loads all validation_schema.json files
- **Dynamic Model Generation**: Creates Pydantic models from JSON schemas at runtime
- **Enum Generation**: Dynamically creates enums from schema definitions
- **Relationship Discovery**: Automatically discovers foreign key relationships
- **Schema Refresh**: Reloads schemas without restarting application

### 2. Dynamic Validation (`dynamic_validation.py`)

**Schema-driven validation that adapts to schema changes:**

```python
from dynamic_validation import DynamicBOOSTValidator

validator = DynamicBOOSTValidator()

# Individual entity validation against current schema
is_valid, errors = validator.validate_entity("organization", org_data)

# Configuration-driven business logic validation
is_valid, errors = validator.validate_business_logic("material_processing", processing_data)

# Cross-entity validation with dynamic relationship discovery
entities = {
    'organization': [org1, org2],
    'traceable_unit': [tru1, tru2],
    'transaction': [txn1]
}
results = validator.comprehensive_validation(entities)
```

**Validation Categories (All Configuration-Driven):**
- **Volume/Mass Conservation**: Physical conservation laws with tolerance checking
- **Temporal Logic**: Date consistency, harvest seasons, processing windows
- **Geographic Logic**: Transport distances, jurisdictional compliance
- **Species Composition**: Percentage validation, ecosystem compatibility
- **Certification Logic**: Chain of custody, certificate validity
- **Regulatory Compliance**: LCFS, EU RED, sustainability criteria
- **Economic Logic**: Price reasonableness, payment terms
- **Quality Assurance**: Moisture content, contamination limits

### 3. BOOST Client (`boost_client.py`)

**High-level interface using dynamic models:**

```python
from boost_client import create_client

client = create_client()

# Schema introspection
schema_info = client.get_schema_info()
print(f"Loaded {len(schema_info['available_entities'])} entity types")

# Dynamic enum discovery
org_types = client.get_available_enum_values('organization', 'organizationType')

# Entity creation with schema validation
org = client.create_organization(
    organization_id=client.generate_id("organization", "FOREST"),
    name="Forest Products Inc",
    org_type="harvester"  # Validated against current schema
)

# Supply chain analysis with dynamic models
supply_chain = client.get_supply_chain("TRU-001")
print(f"Processing history: {len(supply_chain['processing_history'])}")

# Comprehensive validation using all dynamic rules
results = client.validate_all()
```

**Dynamic Features:**
- **Schema-Driven Entity Creation**: Uses current schema for validation
- **Automatic Enum Validation**: Validates against current enum values
- **Dynamic Model Usage**: All entities use dynamically generated models
- **Schema Refresh**: `client.refresh_schemas()` reloads without restart

## Schema Robustness and Change Management

### 🛡️ Automatic Schema Change Adaptation

The BOOST Python reference implementation is designed to be **robust to schema changes**. Most schema modifications require **no code changes**:

#### ✅ Automatically Handled Changes

**Adding New Fields:**
```json
// Schema change - no code changes needed
{
  "properties": {
    "carbonFootprint": {
      "type": "number",
      "description": "CO2 equivalent in kg"
    }
  }
}
```

**Adding New Enum Values:**
```json
// Schema change - immediately available
{
  "organizationType": {
    "enum": ["harvester", "processor", "new_type"]
  }
}
```

**Adding New Entity Types:**
```json
// New schema file automatically discovered
// schema/carbon_credit/validation_schema.json
```

**Modifying Validation Rules:**
```json
// Business logic changes applied automatically
{
  "volumeMassConservation": {
    "materialProcessing": {
      "volumeConservation": {
        "validation": {
          "tolerance": 0.005  // Updated tolerance
        }
      }
    }
  }
}
```

#### ⚠️ Changes Requiring Manual Updates

**Entity Renaming:**
```python
# Manual update needed in client methods
def create_new_entity_name(self, ...):  # Update method name
```

**Core Field Renaming:**
```python
# Manual update needed for field access
primary_key = entity_data['newFieldName']  # Update field references
```

### 📋 Schema Change Detection

The system provides built-in tools to detect and handle schema changes:

```python
# Check current schema status
client = create_client()
schema_info = client.get_schema_info()
print(f"Available entities: {schema_info['available_entities']}")

# Validate against current schema
validation = client.validate_all()
if not validation['valid']:
    print("Schema changes detected - validation errors:")
    for error in validation['errors']:
        print(f"  - {error}")

# Refresh schemas after changes
client.refresh_schemas()
```

### 📖 Complete Schema Change Documentation

For detailed information on schema change propagation, see:
**[📄 SCHEMA_CHANGE_GUIDE.md](SCHEMA_CHANGE_GUIDE.md)**

This guide covers:
- **Automatic Change Propagation**: What changes require no code updates
- **Manual Update Requirements**: When code changes are needed
- **Migration Procedures**: Step-by-step change management
- **Testing Strategies**: How to validate schema changes
- **Troubleshooting**: Common issues and solutions

## Examples

### Running Examples

All examples are in the `examples/` directory and can be run directly:

```bash
# Basic workflow demonstration
python examples/basic_workflow.py

# Certification claim management
python examples/certification_demo.py

# Mass balance accounting
python examples/mass_balance_example.py

# Complete supply chain tracking
python examples/supply_chain_demo.py
```

### Example 1: Basic Workflow

Demonstrates the fundamental BOOST workflow:

1. Create organizations
2. Create traceable units
3. Process materials
4. Execute transactions
5. Validate everything

```python
# See examples/basic_workflow.py for complete implementation
```

### Example 2: Certification Demo

Shows certification claim management:

1. FSC certified forest management
2. Claim inheritance through processing
3. Multi-scheme certification (FSC + SBP)
4. Certification validation

```python
# See examples/certification_demo.py for complete implementation
```

### Example 3: Mass Balance Accounting

Demonstrates conservation validation:

1. Multiple input materials
2. Processing with volume/mass tracking
3. Conservation law validation
4. Efficiency reporting

```python
# See examples/mass_balance_example.py for complete implementation
```

### Example 4: Complete Supply Chain

End-to-end supply chain demonstration:

1. Forest harvest
2. Primary processing (sawmill)
3. Secondary processing (pellets)
4. Multiple transactions
5. Complete traceability

```python
# See examples/supply_chain_demo.py for complete implementation
```

## Entity Types and Relationships

### Organizations
Supply chain participants with roles:
- `harvester` - Forest management, logging
- `processor` - Sawmills, pellet plants
- `transporter` - Logistics providers
- `certifier` - Certification bodies

### Traceable Units (TRUs)
Physical biomass units:
- `log` - Individual logs
- `pile` - Collections of logs
- `batch` - Processed materials
- `container` - Shipping units

### Processing Operations
Material transformations:
- `felling` - Tree cutting
- `crosscutting` - Log cutting
- `chipping` - Size reduction
- `debarking` - Bark removal

### Sustainability Claims
Certification claims:
- `FSC Mix` - Forest Stewardship Council
- `SBP-compliant` - Sustainable Biomass Partnership
- `PEFC` - Programme for Endorsement of Forest Certification

## Validation Rules

### Schema Validation
- Required fields present
- Correct data types
- Valid enumerations
- Pattern matching (IDs)

### Business Logic
- Volume conservation in processing
- Species composition sums to 100%
- Transaction quantities ≤ available volume
- Processing dates after harvest dates

### Cross-Entity Validation
- Foreign key integrity
- Circular reference detection
- Status consistency
- Relationship cardinality

## JSON-LD Integration

Full semantic web support:

```python
# Export with JSON-LD context
jsonld_data = client.export_to_jsonld(include_context=True)

# Import from JSON-LD
results = client.import_from_jsonld(jsonld_data)
print(f"Imported {results['imported']['organizations']} organizations")
```

**Context Support:**
- Schema.org vocabulary
- W3C PROV ontology
- GS1 Web vocabulary
- Custom BOOST terms

## Configuration

### Schema Path Configuration

By default, the implementation looks for schemas in `../schema/` relative to the Python files. You can specify a custom path:

```python
from boost_client import create_client
from validation import create_validator

# Custom schema path
client = create_client(schema_path="/path/to/boost/schemas")
validator = create_validator("/path/to/boost/schemas")
```

### Context URL Configuration

Customize the JSON-LD context URL:

```python
client = create_client(context_url="https://your-domain.com/boost-context.jsonld")
```

## API Reference

### BOOSTClient Class

#### Entity Creation Methods (Using Dynamic Models)
- `create_organization(organization_id, name, org_type, **kwargs)` → Dynamic Organization Model
- `create_traceable_unit(traceable_unit_id, unit_type, **kwargs)` → Dynamic TraceableUnit Model
- `create_transaction(transaction_id, organization_id, customer_id, transaction_date, **kwargs)` → Dynamic Transaction Model
- `create_material_processing(processing_id, input_tru_id, output_tru_id, process_type, **kwargs)` → Dynamic MaterialProcessing Model
- `create_claim(claim_id, traceable_unit_id, claim_type, statement, validated, **kwargs)` → Dynamic Claim Model

#### Schema Introspection Methods
- `get_schema_info()` → Dict[str, Any] - Get loaded schema information
- `get_available_enum_values(entity_type, field_name)` → List[str] - Get valid enum values from schema
- `refresh_schemas()` → None - Reload schemas from disk

#### Validation Methods
- `validate_entity(entity)` → Dict[str, Any] - Validate using dynamic schema and business rules
- `validate_all()` → Dict[str, Any] - Comprehensive validation of all entities

#### Supply Chain Methods
- `get_supply_chain(traceable_unit_id)` → Dict[str, Any] - Trace relationships using dynamic models

#### Import/Export Methods
- `export_to_jsonld(include_context=True)` → str - Export dynamic models to JSON-LD
- `import_from_jsonld(jsonld_data)` → Dict[str, Any] - Import using dynamic models

#### Utility Methods
- `generate_id(entity_type, prefix=None)` → str - Generate entity IDs

### SchemaLoader Class

#### Schema Management Methods
- `get_model(entity_name)` → Type[BaseModel] - Get dynamically generated Pydantic model
- `get_enum(entity_name, field_name)` → Type[Enum] - Get dynamically generated enum
- `get_all_entity_types()` → List[str] - Get all available entity types
- `get_field_enum_values(entity_name, field_name)` → List[str] - Get enum values for field
- `get_primary_key(entity_name)` → str - Get primary key field name
- `get_relationships(entity_name)` → List[Dict] - Get relationship definitions
- `refresh_schemas()` → None - Reload all schemas and regenerate models

#### Schema Validation Methods
- `validate_schema_compatibility(entity_name, data)` → Tuple[bool, List[str]] - Check compatibility

### DynamicBOOSTValidator Class

#### Schema Validation Methods
- `validate_entity(entity_type, entity_data)` → Tuple[bool, List[str]] - Validate against current schema
- `validate_required_fields(entity_type, entity_data)` → Tuple[bool, List[str]] - Check required fields
- `validate_field_constraints(entity_type, field_name, field_value)` → Tuple[bool, List[str]] - Validate field constraints

#### Business Logic Validation Methods (Configuration-Driven)
- `validate_business_logic(entity_type, entity_data)` → Tuple[bool, List[str]] - All business rules
- `validate_foreign_keys(entities)` → Tuple[bool, List[str]] - Dynamic relationship validation
- `validate_temporal_consistency(entities)` → Tuple[bool, List[str]] - Time-based validation

#### Comprehensive Validation
- `comprehensive_validation(entities)` → Dict[str, Any] - Complete validation with schema adaptation
- `refresh_schemas()` → None - Refresh validation rules from updated schemas

## Error Handling

The implementation provides detailed error messages for validation failures:

```python
validation = client.validate_all()
if not validation['valid']:
    for error in validation['errors']:
        print(f"Error: {error}")
    
    # Check individual entity results
    for entity_type, results in validation['entity_results'].items():
        if not results['valid']:
            print(f"{entity_type} errors: {results['errors']}")
```

## Performance Considerations

- **Validation Caching**: Schemas are loaded once and cached
- **Batch Operations**: Use `validate_all()` for multiple entities
- **Memory Usage**: Large supply chains may require streaming for very large datasets

## Contributing

This reference implementation is part of the BOOST standard development. To contribute:

1. Follow existing code patterns and style
2. Add comprehensive tests for new features
3. Update documentation for API changes
4. Ensure all examples continue to work

## Key Benefits of Schema-Driven Architecture

### 🚀 Automatic Adaptation
- **No Code Changes**: Most schema updates require zero code modifications
- **Immediate Availability**: New enum values and fields are instantly available
- **Dynamic Discovery**: Automatically finds and loads all schema changes

### 🛡️ Enhanced Robustness
- **Future-Proof**: Adapts to BOOST standard evolution automatically
- **Version Compatibility**: Gracefully handles schema version changes
- **Comprehensive Validation**: 8 categories of configurable business rules

### ⚡ Developer Experience
- **Schema Introspection**: Discover available entities and enums at runtime
- **Clear Error Messages**: Detailed validation feedback with schema context
- **Hot Reload**: Update schemas without application restart

### 📈 Enterprise Ready
- **Production Scalable**: Efficient schema caching and model generation
- **Audit Trail**: Track validation against specific schema versions
- **Compliance Support**: Built-in regulatory validation (LCFS, EU RED, etc.)

## Standards Compliance

This implementation fully supports:

- **BOOST Data Standard v2.2.1** (with automatic adaptation to newer versions)
- **JSON-LD 1.1 Specification**
- **JSON Schema Draft-07**
- **Schema.org Vocabulary**
- **W3C PROV Ontology**

## License

This reference implementation is part of the BOOST open standard project. See the main repository for licensing information.

## Support

For questions about this implementation:
- Review the example scripts
- Check the API documentation above
- Refer to the main BOOST standard documentation
- File issues in the main BOOST repository

---

This Python reference implementation provides a complete, production-ready foundation for building BOOST-compliant biomass traceability systems.