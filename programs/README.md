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
- [Entity Specification](./lcfs/lcfs_entity_specification.md) - LCFS data model and entity definitions
- [Pacific Renewable Fuels Example](./lcfs/pacific_renewable_fuels_example/) - Complete worked example

## Directory Structure

The LCFS program follows this structure:

```
lcfs/
├── README.md                           # Program overview and quick start
├── lcfs_entity_specification.md        # LCFS data model and entity definitions
└── pacific_renewable_fuels_example/    # Complete worked example
    ├── README.md
    ├── calculated_results.json
    ├── organization.json
    └── transactions_q1_2025.json
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

For technical implementation questions, see the main BOOST documentation.