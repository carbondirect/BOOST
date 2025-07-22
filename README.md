# Biomass Chain of Custody (CoC) Data Standard Community Group

## Overview
This repository contains the working draft and artifacts of the Biomass Chain of Custody (CoC) Data Standard, which defines a robust and interoperable data model for tracking biomass through complex supply chains. The standard supports transparent, verifiable, and consistent data exchange to enable sustainability, regulatory compliance, and supply chain integrity.

**Current Version: v2.1.0** - Enhanced with the Kaulen Framework for media-interruption-free timber traceability and comprehensive plant part categorization system.

- **Charter:** [BOOST_Charter.org](BOOST_Charter.org)
- **Charter Effective Date:** 
- **Last Modified:** 

Feedback and contributions are welcomed via GitHub Issues and Pull Requests at [BOOST](https://github.com/carbondirect/BOOST).

W3C Community Group page: [BOOST-01](https://www.w3.org/community/boost-01/)

## 🌟 Key Features

### Kaulen Framework Implementation
- **Media-Interruption-Free Traceability** - TraceableUnit (TRU) entities with biometric identification
- **Three Critical Tracking Points** - harvest_site, skid_road, forest_road, mill_entrance infrastructure
- **Multi-Species Support** - Species-specific tracking within mixed material flows
- **Complete Processing Chain** - MaterialProcessing with input/output TRU relationships

### Plant Part Categorization System
- **17 Standardized Plant Parts** - trunk, heartwood, sapwood, bark, branches, leaves, seeds, etc.
- **Processing Transformations** - Detailed tracking of plant part changes during operations
- **Value Optimization** - Route materials based on plant part composition
- **Circular Economy** - Byproduct and waste stream management

### Enhanced Geographic Integration
- **GeoJSON Compliance** - Spatial data support for all location-aware entities
- **California Agency Ready** - Administrative boundary and jurisdiction tracking
- **Supply Base Management** - Infrastructure mapping with harvest sites and transportation routes

### Comprehensive Entity System
- **15+ Interconnected Entities** - Complete data model covering all aspects of biomass supply chains
- **JSON-LD Validation** - Structured schemas with business rules and examples
- **Sustainability Claims** - Species-specific claims with inheritance through processing

## 📁 Directory Structure

```
.
├── README.md                # This file
├── LICENSE.md               # License info (not auto-created)
├── CODE_OF_CONDUCT.md       # Community standards (not auto-created)
├── CONTRIBUTING.md          # Contribution guide (not auto-created)
├── CHARTER.md               # Group charter (not auto-created)
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── ci.yml           # Placeholder for GitHub Actions (not auto-created)
├── drafts/                  # Organized draft content
│   ├── current/             # Active working content
│   │   ├── specifications/        # Current spec documents
│   │   ├── schema/               # Entity schemas and validation
│   │   │   ├── traceable_unit/        # Core TRU entity with examples
│   │   │   ├── species_component/     # Multi-species tracking
│   │   │   ├── material_processing/   # Processing operations
│   │   │   └── [11 additional entities] # Complete Kaulen Framework
│   │   ├── images/
│   │   │   ├── current/              # Master ERD and current visuals
│   │   │   └── archive/              # Historical ERD versions
│   │   ├── examples/             # Sample payloads and validation
│   │   └── communications/       # Agency outreach materials
│   ├── archive/             # Historical content
│   │   ├── v1_drafts/            # Early specification drafts
│   │   ├── working_notes/        # Development notes (.org files)
│   │   └── deprecated_schemas/   # Old schema versions
│   └── tools/               # Development utilities
├── proposals/
├── meetings/
│   └── templates/
├── use-cases/
├── presentations/
├── tools/
├── data/                    # Optional: Sample or test data
├── tests/                   # Integration testing scenarios
│   └── KAULEN_INTEGRATION_TESTING_SCENARIOS.md
└── doc/                     # Implementation documentation
    ├── KAULEN_FRAMEWORK_IMPLEMENTATION_SUMMARY.md
    └── MATERIALBATCH_TO_TRU_MIGRATION_GUIDE.md
```

## 📂 Purpose of Each Directory

- `drafts/`: Organized draft content with clear current vs. archive separation
  - `current/`: Active working specifications, schemas, examples, and communications
  - `archive/`: Historical content preserved for reference
  - `tools/`: Development utilities for schema generation and validation
- `proposals/`: Early-stage ideas and design sketches
- `meetings/`: Agendas, minutes, and templates
- `use-cases/`: User scenarios guiding spec design
- `presentations/`: Slides and visual materials
- `tests/`: Integration testing scenarios for Kaulen Framework validation
- `doc/`: Implementation guides and migration documentation

## 🚀 Getting Started

### For Developers
1. **Explore the ERD**: Start with `drafts/current/images/current/boost_erd.mermaid` for the complete data model
2. **Review Entity Schemas**: Check `drafts/current/schema/` for JSON validation schemas and examples
3. **Understand Implementation**: Read `doc/KAULEN_FRAMEWORK_IMPLEMENTATION_SUMMARY.md`
4. **Migration Guide**: See `doc/MATERIALBATCH_TO_TRU_MIGRATION_GUIDE.md` for conceptual changes

### For Standards Organizations
- **California Agencies**: GeoJSON spatial data ready for regulatory integration
- **Certification Bodies**: Multi-scheme support with claim inheritance
- **Supply Chain Partners**: TRU-centric design for seamless data exchange

### For Implementation Testing
- **Integration Scenarios**: See `tests/KAULEN_INTEGRATION_TESTING_SCENARIOS.md`
- **Plant Part Examples**: Review processing transformations in `drafts/current/schema/material_processing/`
- **Multi-Species Cases**: Check species component tracking in `drafts/current/schema/species_component/`
- **Transaction Examples**: See `drafts/current/examples/transactions/`

## 📊 Current Status

- **✅ Complete**: Kaulen Framework Phases 1-3 implementation
- **✅ Complete**: Plant part categorization system 
- **✅ Complete**: 15+ entity schemas with validation and examples
- **✅ Complete**: Integration testing scenarios and migration documentation
- **🔄 Active**: Community feedback integration and use case expansion

## 🚀 Contributing

Please review `CONTRIBUTING.md` and our `CODE_OF_CONDUCT.md` before submitting PRs or issues.

For technical discussions about the Kaulen Framework implementation or plant part categorization, please use GitHub Issues with appropriate labels.

