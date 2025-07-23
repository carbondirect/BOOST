# BOOST Data Standard - Comprehensive ERD Documentation

## Overview

This document describes the comprehensive Entity Relationship Diagram (ERD) for the BOOST (Biomass Object-Oriented Standard for Traceability) data model. The ERD represents a complete biomass chain of custody system with **20 core entities** organized into **7 thematic areas**.

## Version Information

- **Version**: 2.0.0 
- **Date**: January 22, 2025
- **Framework**: Kaulen Framework Integration
- **Entities**: 20 core entities, 31 relationships
- **Schema Files**: Full JSON schema validation available

## System Architecture

### Core Principles

1. **Media-Interruption-Free Tracking**: Implementation of the Kaulen framework ensuring continuous data traceability
2. **Moisture Content Integration**: Comprehensive moisture tracking throughout the supply chain
3. **Multi-Species Support**: Full support for complex species compositions
4. **Certification Integration**: Complete sustainability certification tracking (FSC, PEFC, SBP, etc.)
5. **Commercial Transaction Support**: Full business transaction and batch management

### Thematic Organization

The ERD is organized into 7 functional areas for improved readability and understanding:

#### 🟢 Core Traceability
**Entities**: TraceableUnit, MaterialProcessing, ProcessingHistory, TrackingPoint, LocationHistory
- Central biomass tracking and processing operations
- Kaulen framework implementation for media-interruption-free tracking
- Complete processing history with moisture content tracking

#### 🟠 Commercial Transactions  
**Entities**: Transaction, TransactionBatch, DataReconciliation
- Business transactions between organizations
- Batch-level commercial tracking with full traceability
- Automated reconciliation for transaction discrepancies

#### 🔵 Organizational
**Entities**: Organization, Operator
- Business entities and personnel in supply chain
- Enhanced certification and equipment authorization tracking
- Multi-role organization support

#### 🟣 Certification & Claims
**Entities**: Claim, Certificate, CertificationBody, CertificationScheme
- Sustainability certification tracking
- Multi-scheme support (FSC, PEFC, SBP, RSB, ISCC, RED II)
- Claims validation and evidence tracking

#### 🟤 Material Specification
**Entities**: Material, SpeciesComponent, ProductGroup, MoistureContent
- Material types and specifications
- Species composition tracking
- Product classification and moisture management

#### 🟪 Geographic & Spatial
**Entities**: GeographicData
- GeoJSON-based spatial data
- Multi-geometry support (points, polygons, linestrings)
- GPS accuracy and elevation tracking

#### 🔴 Measurement & Quality
**Entities**: MeasurementRecord, BiometricIdentifier
- Quality metrics and dimensional data
- Biometric identification for media-interruption-free tracking
- Multi-instrument measurement support

## Key Entity Descriptions

### TraceableUnit (TRU)
**Central Hub Entity** - The core of the BOOST system representing any discrete biomass unit that can be tracked.

**Key Features**:
- Unique biometric/RFID/QR identification
- Multiple unit types: individual_log, pile, volume_aggregation, processed_batch
- Self-referential relationships for splits/merges
- Moisture content tracking integration
- Multi-species composition support

**Relationships**: Connected to 15+ other entities, serving as the primary hub

### MaterialProcessing
**Process Management** - Represents any operation that transforms a TRU.

**Key Features**:
- Input/output volume tracking
- Moisture content changes
- Processing efficiency calculations
- Equipment and operator tracking

### TransactionBatch
**Commercial Integration** - Batch-level commercial transactions with full traceability.

**Key Features**:
- Many-to-many relationship with TRUs
- Quality grade and reconciliation status
- Media break detection
- Multi-unit quantity management

### Claim
**Sustainability Integration** - Certification claims with validation tracking.

**Key Features**:
- Multi-scheme support (FSC, PEFC, SBP, etc.)
- Percentage-based claims (0-100%)
- Scope tracking (harvest, processing, transport, full_chain)
- Evidence and validation tracking

## Relationship Types

### Identifying Relationships (Solid Lines)
- Child entity cannot exist without parent
- Foreign key is part of primary key
- Examples: TRU → ProcessingHistory, Transaction → TransactionBatch

### Non-Identifying Relationships (Dashed Lines)
- Child can exist independently
- Foreign key is not part of primary key  
- Examples: Material → TRU, GeographicData → TRU

### Self-Referential Relationships
- TraceableUnit → TraceableUnit (parent/child for splits and merges)

### Many-to-Many Relationships
- TransactionBatch ↔ TraceableUnit (via junction table)
- TraceableUnit ↔ TrackingPoint (via LocationHistory)

## Data Flow Patterns

### 1. Harvest to Processing Flow
```
GeographicData → TraceableUnit → MaterialProcessing → ProcessingHistory
     ↓                ↓                    ↓               ↓
Organization → Operator → MeasurementRecord → MoistureContent
```

### 2. Commercial Transaction Flow
```
Organization → Transaction → TransactionBatch → DataReconciliation
     ↓              ↓             ↓                    ↓
  Certificate → Claim ←→ TraceableUnit ←→ SpeciesComponent
```

### 3. Quality and Certification Flow
```
BiometricIdentifier → TraceableUnit → Claim → CertificationScheme
        ↓                  ↓           ↓            ↓
MeasurementRecord → MoistureContent → Certificate → CertificationBody
```

## Schema Integration

All entities are backed by comprehensive JSON Schema validation files located in:
```
/schema/{entity_name}/validation_schema.json
```

Each schema includes:
- Complete field definitions with types and constraints
- Required field specifications
- Enumeration values
- Foreign key relationships
- Data validation rules

## File Structure

```
/images/current/
├── boost_erd_comprehensive.html          # Main interactive ERD
├── boost_erd_entities_complete.json      # Entity definitions
├── BOOST_ERD_COMPREHENSIVE_README.md     # This documentation
└── archive/                              # Deprecated versions
    ├── boost_erd_final.html              # Previous final version
    ├── boost_erd_curved.html             # Curved relationships version
    ├── boost_erd_smart_routing.html      # Smart routing version
    ├── boost_erd_no_overlap.html         # Force-directed version
    └── boost_erd_*.html                  # Other iterations
```

## Interactive Features

The comprehensive ERD includes:

### 🔍 Zoom & Pan
- Mouse wheel zoom (10%-500%)
- Click and drag panning
- Zoom controls and indicators
- Fit-to-screen functionality

### 🎨 Visual Styling
- Color-coded thematic areas
- Professional crow's foot notation
- SF Pro Display/SF Mono typography  
- Subtle transparency and shadows

### ⚡ Interactivity
- Entity highlighting on hover
- Relationship filtering by entity
- Thematic area filtering
- Curved relationship lines with multiple styles

### 📤 Export Options
- SVG export for documentation
- High-resolution rendering
- Preserves all visual styling

## Usage Guidelines

### For Developers
1. Reference `boost_erd_entities_complete.json` for complete entity definitions
2. Use schema validation files for data validation
3. Follow the thematic organization for UI design

### For Business Users
1. Start with the interactive ERD for visual understanding
2. Use thematic filtering to focus on relevant areas
3. Reference this documentation for detailed explanations

### For Data Architects
1. Entity definitions include all relationships and constraints
2. Self-referential relationships support complex hierarchies
3. Many-to-many relationships use junction tables

## Migration from Previous Versions

### Breaking Changes from v1.x
- Addition of 12 new entities
- Enhanced TraceableUnit with self-referential relationships
- New thematic organization structure
- Comprehensive certification and claims support

### Backward Compatibility
- Core entities (TRU, Processing, History) maintain field compatibility
- Existing relationships preserved with enhancements
- Schema files provide validation for migration

## Future Enhancements

### Planned Features
- IoT sensor integration entities
- Supply chain analytics entities  
- Carbon footprint calculation entities
- Blockchain integration entities

### Extension Points
- Custom measurement types
- Additional certification schemes
- Regional compliance entities
- Advanced quality metrics

## Support and Maintenance

### Version Control
- Entity definitions versioned in JSON schema
- ERD visualization updated automatically
- Documentation synchronized with schema changes

### Validation
- JSON Schema validation for all entities
- Relationship integrity checking
- Data consistency validation rules

---

**Last Updated**: January 22, 2025  
**Version**: 2.0.0  
**Schema Files**: 20 entities, 31 relationships  
**Interactive ERD**: `boost_erd_comprehensive.html`