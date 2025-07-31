# LCFS - Low Carbon Fuel Standard

BOOST entity framework extension for California's Low Carbon Fuel Standard regulatory compliance.

## Overview

This directory contains the **BOOST entity specifications** for California's Low Carbon Fuel Standard (LCFS) regulatory program, administered by the California Air Resources Board (CARB). 

**Purpose**: Demonstrates how BOOST entities can be extended to support LCFS compliance requirements while maintaining complete biomass supply chain traceability.

### What's Included

✅ **Entity Specifications** - LCFS-enhanced BOOST entity definitions  
✅ **Regulatory Mapping** - How BOOST entities map to LCFS requirements  
✅ **Calculation Framework** - LCFS credit calculation using BOOST data  
✅ **Working Example** - Real-world renewable diesel producer scenario  
✅ **Compliance Workflow** - End-to-end CARB reporting process  

## Entity Extensions

### LCFS-Enhanced Entities

BOOST's core entities are extended with LCFS-specific attributes to support carbon intensity tracking and credit calculations:

#### Organization
```json
{
  "lcfsRegistrationId": "LCFS-REG-2025-003",
  "regulatedEntityType": "producer|importer|blender|distributor"
}
```

#### Transaction  
```json
{
  "fuelVolume": 875000.0,
  "fuelVolumeUnit": "gallons",
  "fuelCategory": "renewable_diesel",
  "reportingPeriod": "2025-Q1",
  "lcfsPathwayId": "CA-RD-2025-LMR-001"
}
```

#### EnergyCarbonData
```json
{
  "measurementMethod": "CA-GREET3.0",
  "lcfsPathwayType": "Tier_1", 
  "energyEconomyRatio": 1.0,
  "regulatoryBenchmark": 98.47
}
```

### New LCFS-Specific Entities

#### LCFSPathway
```json
{
  "pathwayId": "CA-RD-2025-LMR-001",
  "feedstockCategory": "logging_and_mill_residue",
  "carbonIntensity": 19.85,
  "verificationStatus": "active"
}
```

#### LCFSReporting
```json
{
  "reportingPeriod": "2025-Q1",
  "totalCreditsGenerated": 54580477.10,
  "complianceStatus": "compliant"
}
```

## LCFS Credit Calculation

The LCFS program generates credits when fuel carbon intensity is below regulatory benchmarks:

```
Credits = (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER
```

**Example Calculation:**
- Fuel: 875,000 gallons renewable diesel
- Pathway CI: 19.85 gCO2e/MJ (logging residue)  
- Benchmark: 98.47 gCO2e/MJ (2025 diesel standard)
- Volume: 121.36M MJ (875,000 × 138.7 MJ/gallon)
- **Result**: 9.54M LCFS credits

## Documentation Structure

```
lcfs/
├── README.md                           # This overview
├── lcfs_entity_specification.md        # Complete entity definitions
└── pacific_renewable_fuels_example/    # Comprehensive working example
    ├── README.md                       # Example overview with metrics
    ├── documentation/                  # Rich visualization and analysis
    │   ├── pacific_renewable_fuels_boost_entity_flow.md  # Main Mermaid diagrams
    │   ├── boost_entity_attribute_flow.md               # Detailed attribute mapping
    │   └── pacific_renewable_fuels_lcfs_example.org     # Literate programming (66K lines)
    └── data/                           # Complete JSON entities and calculations
        ├── organization.json           # Pacific Renewable Fuels Corp entity
        ├── transactions_q1_2025.json  # Q1 2025 fuel transactions
        ├── calculated_results.json    # LCFS credit calculations
        ├── energy_carbon_data.json    # Carbon intensity profiles
        ├── lcfs_pathways.json         # CARB pathway definitions
        └── materials_feedstocks.json  # Feedstock classifications
```

## Pacific Renewable Fuels Example

**Scenario**: Renewable diesel producer using lignocellulosic biomass feedstocks

**Q1 2025 Results**:
- **Fuel Volume**: 5.075 million gallons renewable diesel
- **Credits Generated**: 54.58 million LCFS credits  
- **Estimated Value**: $109.16 million
- **CO2 Reduction**: 55,249 metric tons
- **Feedstock Types**: 4 different CARB-certified pathways

**Demonstrates**:
- Multi-pathway operations with diverse feedstock sources
- Complete BOOST entity relationships for regulatory compliance
- Quarterly aggregation and CARB reporting workflows
- Real-world transaction volumes and carbon intensity data

## Regulatory Context

### LCFS Program
- **Administrator**: California Air Resources Board (CARB)
- **Objective**: Reduce carbon intensity of transportation fuels
- **Mechanism**: Credit trading system based on carbon intensity benchmarks
- **Reporting**: Quarterly submissions to CARB's LRT-CBTS system

### Regulated Parties
- **Producers**: Refineries and renewable fuel facilities
- **Importers**: Entities importing fuels into California  
- **Blenders**: Entities blending biofuels with conventional fuels
- **Distributors**: Large fuel distribution companies

### Compliance Requirements
- Register with CARB as regulated entity
- Use CARB-certified fuel pathways
- Submit quarterly transaction reports
- Obtain third-party verification (large entities)
- Meet annual compliance obligations

## BOOST Integration Benefits

### Supply Chain Traceability
- Complete biomass feedstock tracking from harvest to fuel production
- Species composition and geographic origin documentation  
- Processing step documentation with TRU continuity
- Sustainability certification tracking throughout supply chain

### Regulatory Compliance
- LCFS credit calculation using verified BOOST transaction data
- Automated quarterly report generation from BOOST entities
- Complete audit trail for verification and compliance
- Integration with existing biomass certification schemes

### Data Quality
- Validated entity relationships ensure data consistency
- Standardized measurement units and conversion factors
- Built-in validation rules for regulatory requirements
- Error detection and reconciliation workflows

## Related Standards

This LCFS specification demonstrates BOOST's ability to integrate with multiple regulatory frameworks:

- **FSC**: Forest Stewardship Council certification tracking
- **SBP**: Sustainable Biomass Program compliance  
- **RFS**: EPA Renewable Fuel Standard (federal program)
- **ISO 38200**: Chain of custody standard for bioenergy

## Resources

### Regulatory References
- **CARB LCFS Program**: https://ww2.arb.ca.gov/our-work/programs/low-carbon-fuel-standard
- **LRT-CBTS System**: https://www.arb.ca.gov/fuels/lcfs/lrt-cbts/lrt-cbts.htm  
- **CA-GREET Model**: https://ww2.arb.ca.gov/resources/documents/ca-greet-3-0

### BOOST Framework
- **Core Entities**: See main repository documentation
- **Entity Relationships**: Refer to BOOST ERD diagrams
- **Validation Rules**: Review BOOST validation specifications

---

**Note**: This specification demonstrates BOOST's regulatory compliance capabilities. The entity extensions shown here maintain full compatibility with core BOOST entities while adding the specific attributes needed for LCFS compliance.