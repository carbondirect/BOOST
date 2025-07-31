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
- [Pacific Renewable Fuels Example](./lcfs/pacific_renewable_fuels_example/) - Comprehensive real-world example with:
  - **Professional Mermaid Visualizations** - 3 specialized diagrams (ER, data flow, production workflow)
  - **Interactive Documentation** - 66K+ line literate programming document 
  - **Complete Data Suite** - 6 JSON files with real Q1 2025 business data ($109M+ credit value)
  - **Separate Diagram Files** - Both .mermaid source and .svg rendered versions

## Directory Structure

The LCFS program follows this structure:

```
lcfs/
├── README.md                           # Program overview and quick start
├── lcfs_entity_specification.md        # LCFS data model and entity definitions
└── pacific_renewable_fuels_example/    # Comprehensive worked example
    ├── README.md                       # Example overview with business metrics
    ├── documentation/                  # Rich visualization and analysis
    │   ├── pacific_renewable_fuels_boost_entity_flow.md  # Main workflow documentation
    │   ├── boost_entity_attribute_flow.md               # Detailed attribute mapping
    │   └── pacific_renewable_fuels_lcfs_example.org     # Literate programming (66K lines)
    ├── diagrams/                       # Professional Mermaid visualizations
    │   ├── feedstock_flow.mermaid/.svg      # Data flow through BOOST entities
    │   ├── boost_entity_relationships.mermaid/.svg # Complete ERD with attributes
    │   └── production_workflow.mermaid/.svg        # Transaction aggregation workflow
    └── data/                           # Complete JSON entities and calculations
        ├── organization.json           # Pacific Renewable Fuels Corp entity
        ├── transactions_q1_2025.json  # Q1 2025 fuel transactions
        ├── calculated_results.json    # LCFS credit calculations
        ├── energy_carbon_data.json    # Carbon intensity profiles
        ├── lcfs_pathways.json         # CARB pathway definitions
        └── materials_feedstocks.json  # Feedstock classifications
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