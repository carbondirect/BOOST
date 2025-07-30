# BOOST Python Reference Implementation - Architecture

## Overview

The BOOST Python reference implementation uses a **dynamic, schema-driven architecture** that automatically adapts to changes in the BOOST JSON schemas. This document provides a detailed view of the system architecture.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    BOOST JSON Schemas                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────┐  │
│  │organization/│ │traceable_   │ │transaction/ │ │   ...    │  │
│  │validation_  │ │unit/        │ │validation_  │ │          │  │
│  │schema.json  │ │validation_  │ │schema.json  │ │          │  │
│  │             │ │schema.json  │ │             │ │          │  │
│  └─────────────┘ └─────────────┘ └─────────────┘ └──────────┘  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │           business_logic_validation.json                │   │
│  │           cross_entity_validation.json                  │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Schema Loader (schema_loader.py)              │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌──────────────────┐  │
│  │   Automatic     │ │   Dynamic       │ │   Relationship   │  │
│  │   Schema        │ │   Model         │ │   Discovery      │  │
│  │   Discovery     │ │   Generation    │ │   & Enum         │  │
│  │                 │ │                 │ │   Creation       │  │
│  └─────────────────┘ └─────────────────┘ └──────────────────┘  │
│                                                                 │
│  Output: Dynamic Pydantic Models + Enums + Relationships       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            Dynamic Validation (dynamic_validation.py)          │
│                                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌─────────────────────────┐  │
│  │   Schema     │ │   Business   │ │   Cross-Entity &        │  │
│  │   Validation │ │   Logic      │ │   Temporal Validation   │  │
│  │              │ │   (8 Types)  │ │                         │  │
│  └──────────────┘ └──────────────┘ └─────────────────────────┘  │
│                                                                 │
│  • Volume/Mass Conservation  • Geographic Logic                 │
│  • Temporal Logic           • Species Composition              │
│  • Economic Logic           • Certification Logic              │
│  • Quality Assurance        • Regulatory Compliance            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  BOOST Client (boost_client.py)                │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌──────────────────┐  │
│  │   Entity        │ │   Schema        │ │   Supply Chain   │  │
│  │   Creation      │ │   Introspection │ │   Analysis       │  │
│  │   (Dynamic)     │ │                 │ │                  │  │
│  └─────────────────┘ └─────────────────┘ └──────────────────┘  │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌──────────────────┐  │
│  │   Validation    │ │   JSON-LD       │ │   ID Generation  │  │
│  │   (Dynamic)     │ │   Export/Import │ │                  │  │
│  └─────────────────┘ └─────────────────┘ └──────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Application Layer                             │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌──────────────────┐  │
│  │   Example       │ │   User          │ │   Integration    │  │
│  │   Scripts       │ │   Applications  │ │   Systems        │  │
│  └─────────────────┘ └─────────────────┘ └──────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Schema Loader (`schema_loader.py`)

**Responsibility**: Dynamic schema loading and model generation

**Key Features**:
- **Automatic Discovery**: Scans schema directory for `validation_schema.json` files
- **Dynamic Model Generation**: Creates Pydantic models from JSON schemas at runtime
- **Enum Generation**: Dynamically creates Python enums from schema enum definitions
- **Relationship Discovery**: Analyzes schemas to discover foreign key relationships
- **Metadata Extraction**: Extracts BOOST metadata for business logic integration

**Flow**:
1. Load all JSON schemas from disk
2. Parse schema properties and constraints
3. Generate Pydantic model classes dynamically
4. Create enum classes for schema enum fields
5. Discover relationships and primary keys
6. Cache generated models for performance

### 2. Dynamic Validation (`dynamic_validation.py`)

**Responsibility**: Schema-driven validation using configuration-based business rules

**Validation Categories**:
1. **Schema Validation**: JSON Schema compliance
2. **Volume/Mass Conservation**: Physical conservation laws
3. **Temporal Logic**: Date/time consistency rules
4. **Geographic Logic**: Location-based constraints
5. **Species Composition**: Biological consistency
6. **Certification Logic**: Chain of custody validation
7. **Regulatory Compliance**: LCFS, EU RED compliance
8. **Economic/Quality Logic**: Market and quality constraints

**Flow**:
1. Validate entity against JSON schema
2. Apply business logic rules from configuration
3. Check cross-entity relationships
4. Validate temporal consistency
5. Return comprehensive validation results

### 3. BOOST Client (`boost_client.py`)

**Responsibility**: High-level API using dynamic models

**Core Functions**:
- **Entity Creation**: Create entities using dynamically generated models
- **Schema Introspection**: Query available entities, enums, and constraints
- **Validation**: Comprehensive validation using dynamic rules
- **Supply Chain Analysis**: Trace relationships using dynamic models
- **JSON-LD Support**: Export/import with semantic annotations

**Flow**:
1. Initialize schema loader and validator
2. Provide high-level entity creation methods
3. Validate entities using dynamic validation
4. Support supply chain traceability queries
5. Handle JSON-LD serialization/deserialization

## Data Flow

### Entity Creation Flow
```
User Request → Client Method → Schema Validation → Dynamic Model Creation → Storage
```

### Validation Flow
```
Entity Data → Schema Validation → Business Logic Rules → Cross-Entity Checks → Results
```

### Schema Change Flow
```
Schema Update → Automatic Discovery → Model Regeneration → Validation Rule Update → Ready
```

## Key Design Principles

### 1. **Schema-First Design**
- All models and validation rules derived from schemas
- No hard-coded entity definitions
- Schema changes automatically propagate

### 2. **Configuration-Driven Business Logic**
- Business rules defined in JSON configuration
- Rules applied dynamically based on entity type
- New rules added without code changes

### 3. **Relationship Discovery**
- Foreign keys discovered from schema metadata
- Primary keys inferred from schema patterns
- Relationships validated dynamically

### 4. **Graceful Schema Evolution**
- Backward compatibility with schema versions
- Unknown fields treated as warnings, not errors
- Gradual migration support

## Performance Characteristics

### Initialization
- **Schema Loading**: O(n) where n = number of schema files
- **Model Generation**: O(m) where m = number of entity properties
- **Caching**: Models cached after first generation

### Runtime
- **Validation**: O(1) for schema validation, O(r) for relationship validation
- **Entity Creation**: O(1) with cached models
- **Memory Usage**: Moderate (dynamic models cached in memory)

## Extension Points

### Adding New Entity Types
1. Add schema file to appropriate directory
2. Restart application or call `refresh_schemas()`
3. Entity automatically available

### Adding New Business Rules
1. Update `business_logic_validation.json`
2. Rules automatically applied to relevant entities

### Custom Validation Logic
1. Extend `DynamicBOOSTValidator` class
2. Add custom validation methods
3. Integrate with existing validation flow

## Error Handling Strategy

### Schema Loading Errors
- Log warnings for missing schemas
- Continue with available schemas
- Provide diagnostic information

### Validation Errors
- Clear, actionable error messages
- Reference to specific schema constraints
- Suggestions for fixing common issues

### Runtime Errors
- Graceful degradation when possible
- Detailed error context
- Recovery mechanisms for transient issues

## Testing Strategy

### Unit Tests
- Schema loader functionality
- Dynamic model generation
- Individual validation rules

### Integration Tests
- End-to-end entity creation and validation
- Schema change scenarios
- Cross-entity validation

### Performance Tests
- Large dataset validation
- Schema loading performance
- Memory usage patterns

This architecture ensures that the BOOST Python reference implementation is robust, maintainable, and automatically adapts to the evolving BOOST standard while providing enterprise-grade validation and traceability capabilities.