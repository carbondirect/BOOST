# Biomass Chain of Custody (CoC) Data Standard Community Group

## Overview
This repository contains the working draft and artifacts of the Biomass Chain of Custody (CoC) Data Standard, which defines a robust and interoperable data model for tracking biomass through complex supply chains. The standard supports transparent, verifiable, and consistent data exchange to enable sustainability, regulatory compliance, and supply chain integrity.

**Current Version: v2.2.1** - Repository cleanup and ERD consolidation with single source of truth ERD Navigator, eliminated redundant code, and consistent terminology.

- **Charter:** [BOOST_Charter.org](BOOST_Charter.org)
- **Charter Effective Date:** 
- **Last Modified:** 

Feedback and contributions are welcomed via GitHub Issues and Pull Requests at [BOOST](https://github.com/carbondirect/BOOST).

W3C Community Group page: [BOOST-01](https://www.w3.org/community/boost-01/)

## 🌟 Key Features

### BOOST Traceability System Implementation
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
- **29 Interconnected Entities** - Complete data model covering all aspects of biomass supply chains across 7 thematic areas
- **JSON-LD Validation** - Structured schemas with business rules and examples
- **Interactive ERD Navigator** - Dynamic exploration with GitHub discussion integration
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
├── erd-navigator/           # Interactive ERD Navigator for stakeholder feedback
│   ├── index.html                   # Main interactive ERD interface
│   └── README.md                    # Navigator documentation
├── drafts/                  # Organized draft content
│   ├── current/             # Active working content
│   │   ├── specifications/        # Current spec documents
│   │   ├── schema/               # Entity schemas and validation (29 entities)
│   │   │   ├── traceable_unit/        # Core TRU entity with examples
│   │   │   ├── species_component/     # Multi-species tracking
│   │   │   ├── material_processing/   # Processing operations
│   │   │   └── [26 additional entities] # Complete BOOST Traceability System
│   │   ├── images/
│   │   │   ├── current/              # Interactive ERD and current visuals
│   │   │   └── archive/              # Historical ERD iterations and deprecated files
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
│   └── BOOST_INTEGRATION_TESTING_SCENARIOS.md
└── drafts/current/specifications/  # Technical specifications and migration guides
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
- `tests/`: Integration testing scenarios for BOOST Traceability System validation
- `drafts/current/specifications/`: Technical specifications and migration guides

## 🚀 Getting Started

### For Developers
1. **Explore the Interactive ERD**: Use the [Interactive ERD Navigator](erd-navigator/index.html) to explore all 29 entities with dynamic filtering and GitHub discussion integration
2. **Review Entity Schemas**: Check `drafts/current/schema/` for JSON validation schemas and examples
3. **Review Schema Organization**: Check entity schemas in `drafts/current/schema/` for implementation details
4. **Migration Guide**: See `drafts/current/specifications/MATERIALBATCH_TO_TRU_MIGRATION_GUIDE.md` for conceptual changes

### For Standards Organizations
- **California Agencies**: GeoJSON spatial data ready for regulatory integration
- **Certification Bodies**: Multi-scheme support with claim inheritance
- **Supply Chain Partners**: TRU-centric design for seamless data exchange

### For Implementation Testing
- **Integration Scenarios**: See `tests/BOOST_INTEGRATION_TESTING_SCENARIOS.md`
- **Plant Part Examples**: Review processing transformations in `drafts/current/schema/material_processing/`
- **Multi-Species Cases**: Check species component tracking in `drafts/current/schema/species_component/`
- **Transaction Examples**: See `drafts/current/examples/transactions/`

## 🎯 Interactive ERD Navigator

The [Interactive ERD Navigator](erd-navigator/index.html) provides a comprehensive, stakeholder-friendly way to explore the BOOST data model:

### 🔍 Key Features
- **29 Entity Coverage**: Complete visualization of all entities across 7 thematic areas
- **Dynamic Filtering**: Focus on specific domains (Core Traceability, Organizational, Material & Supply, etc.)
- **Direct Discussion Access**: Purple 💬 icons in each entity header link directly to GitHub discussions
- **TraceableUnit Focus Mode**: 🎯 button to reduce visual complexity and highlight essential relationships
- **Schema Integration**: Real-time loading of entity definitions from JSON schema files

### 🎨 Thematic Organization
- 🟢 **Core Traceability** (9 entities): TraceableUnit, MaterialProcessing, DataReconciliation, etc.
- 🔵 **Organizational** (4 entities): Organization, Certificate, CertificationScheme, CertificationBody
- 🟤 **Material & Supply** (4 entities): Material, SupplyBase, Supplier, Customer
- 🟠 **Transactions** (3 entities): Transaction, TransactionBatch, SalesDeliveryDocument
- 🟡 **Sustainability** (1 entity): Claim
- 🟣 **Geographic** (1 entity): GeographicData
- 🔴 **Reporting** (3 entities): SupplyBaseReport, VerificationStatement, Audit
- ⚫ **Analytics** (2 entities): EnergyCarbonData, MoistureContent
- 👥 **Personnel** (2 entities): Operator, ProductGroup

### 💬 Community Feedback
Each entity has a dedicated GitHub discussion thread accessible via the ERD. This enables:
- **Structured feedback** on schema definitions and relationships
- **Real-world validation** from supply chain stakeholders
- **Iterative improvement** based on implementation experience

**Access**: Visit the [Live Interactive ERD Navigator](https://carbondirect.github.io/BOOST/erd-navigator/) or use the local version at `erd-navigator/index.html`

## 📊 Current Status

- **✅ Complete**: BOOST Traceability System Phases 1-3 implementation
- **✅ Complete**: Plant part categorization system 
- **✅ Complete**: 29 entity schemas with validation and examples
- **✅ Complete**: Interactive ERD Navigator with GitHub discussion integration
- **✅ Complete**: Integration testing scenarios and migration documentation
- **🔄 Active**: Community feedback integration and use case expansion

## 🚀 Contributing

Please review `CONTRIBUTING.md` and our `CODE_OF_CONDUCT.md` before submitting PRs or issues.

For technical discussions about the BOOST Traceability System implementation or plant part categorization, please use GitHub Issues with appropriate labels.

