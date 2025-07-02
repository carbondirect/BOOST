# BOOST Program-Specific Extensions

This directory contains BOOST implementations and extensions for specific regulatory programs and certification schemes.

## Available Programs

### [LCFS - Low Carbon Fuel Standard](./lcfs/)
California's carbon reduction program for transportation fuels.

**Key Features:**
- Fuel pathway tracking and carbon intensity calculations
- Quarterly compliance reporting to CARB
- Credit/deficit accounting and verification
- Complete LCFS entity framework

**Documentation:**
- [Implementation Guide](./lcfs/docs/lcfs_implementation_guide.md) - Developer quick-start
- [Workflow Specification](./lcfs/docs/lcfs_workflow_specification.md) - Complete process
- [Entity Mapping](./lcfs/docs/lcfs_entity_mapping.md) - Detailed data model
- [Validation Checklist](./lcfs/docs/lcfs_validation_checklist.md) - Quality assurance

### [RFS - Renewable Fuel Standard](./rfs/)
US EPA biofuel program for renewable fuel identification and tracking.

**Key Features:**
- RIN (Renewable Identification Number) tracking
- Quarterly and annual reporting to EPA
- Feedstock qualification and pathway verification

### [FSC - Forest Stewardship Council](./fsc/)
International forest certification and chain of custody tracking.

**Key Features:**
- FSC-certified material tracking
- Chain of custody documentation
- Mixed percentage claims and verification

## Directory Structure

Each program follows a consistent structure:

```
program_name/
├── README.md              # Program overview and quick start
├── docs/                  # Detailed documentation
│   ├── implementation_guide.md
│   ├── workflow_specification.md
│   ├── entity_mapping.md
│   └── validation_checklist.md
├── examples/              # Sample data and payloads
│   ├── sample_transactions.json
│   └── report_templates.json
├── schemas/               # JSON schemas and validation rules
│   └── program_extensions.json
└── images/                # Diagrams and visualizations
    └── workflow_diagrams.mermaid
```

## Implementation Guidelines

### 1. Entity Extensions
Programs extend core BOOST entities with program-specific attributes:
- Enhanced `Organization` entity with program registration details
- Extended `Transaction` entity with program-specific tracking
- New program-specific entities (e.g., `LCFSPathway`, `RFSPathway`)

### 2. Validation Rules
Each program includes comprehensive validation:
- Data completeness verification
- Business logic validation
- Regulatory compliance checks
- Cross-entity relationship validation

### 3. Reporting Workflows
Standardized reporting processes:
- Data collection and aggregation
- Calculation engines for program metrics
- Report generation and formatting
- Regulatory submission workflows

## Getting Started

1. **Choose Your Program**: Navigate to the relevant program directory
2. **Read the Overview**: Start with the program's README.md
3. **Follow Implementation Guide**: Use the quick-start documentation
4. **Review Examples**: Examine sample data and payloads
5. **Implement Extensions**: Add program-specific entities and logic

## Contributing

When adding new programs:

1. Create program directory following the standard structure
2. Include comprehensive documentation using existing templates
3. Provide working examples and test data
4. Update this main README with program details
5. Add cross-references to relevant core BOOST documentation

## Support

For program-specific questions:
- **LCFS**: Contact CARB or approved LCFS verifiers
- **RFS**: Contact EPA RFS program staff
- **FSC**: Contact FSC International or local FSC offices

For technical implementation questions, see the main BOOST documentation.