# LCFS - Low Carbon Fuel Standard

BOOST implementation for California's Low Carbon Fuel Standard compliance program.

## Overview

The **Low Carbon Fuel Standard (LCFS)** is California's carbon reduction program for transportation fuels, administered by the California Air Resources Board (CARB). This BOOST extension provides complete entity framework and workflow support for LCFS compliance.

### Key Features

✅ **Fuel Pathway Tracking** - CARB-certified pathway management  
✅ **Carbon Intensity Calculations** - CA-GREET methodology support  
✅ **Credit/Deficit Accounting** - Automated LCFS credit calculations  
✅ **Quarterly Reporting** - CARB LRT-CBTS system integration  
✅ **Verification Support** - Third-party verification documentation  
✅ **Audit Trail** - Complete compliance documentation  

## Quick Start

### 1. Core LCFS Entities

The LCFS extension adds two new entities and enhances three existing ones:

**New Entities:**
- `LCFSPathway` - CARB-certified fuel pathways
- `LCFSReporting` - Quarterly compliance reports

**Enhanced Entities:**
- `Organization` + LCFS registration and entity type
- `Transaction` + fuel volume and pathway tracking  
- `EnergyCarbonData` + CA-GREET and carbon intensity data

### 2. Credit Calculation

LCFS credits are calculated using the formula:
```
Credits = (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER
```

Where:
- **Benchmark_CI**: Annual regulatory benchmark (gCO2e/MJ)
- **Pathway_CI**: Certified pathway carbon intensity 
- **Fuel_Volume_MJ**: Fuel volume in megajoules
- **EER**: Energy Economy Ratio

### 3. Implementation Process

1. **Set Up Entities** - Implement LCFS-enhanced BOOST entities
2. **Load Pathways** - Import CARB-certified pathway data
3. **Track Transactions** - Capture fuel transfers with pathway attribution
4. **Calculate Credits** - Apply LCFS formulas for credit/deficit generation
5. **Generate Reports** - Create quarterly compliance reports
6. **Submit to CARB** - Automated submission to LRT-CBTS system

## Documentation

### Primary Documentation
- **[Implementation Guide](./docs/lcfs_implementation_guide.md)** - Developer quick-start and architecture overview
- **[Workflow Specification](./docs/lcfs_workflow_specification.md)** - Complete 5-phase compliance process  
- **[Entity Mapping](./docs/lcfs_entity_mapping.md)** - Detailed entity relationships and attributes
- **[Validation Checklist](./docs/lcfs_validation_checklist.md)** - Comprehensive validation procedures

### Supporting Resources
- **Entity Relationship Diagram**: `../../drafts/images/boost_erd.mermaid`
- **Sample Payloads**: `./examples/` (coming soon)
- **JSON Schemas**: `./schemas/` (coming soon)

## LCFS Program Background

### Regulatory Framework
- **Administrator**: California Air Resources Board (CARB)
- **Program Type**: Cap-and-trade with credit banking
- **Reporting**: Quarterly submissions due 45 days after quarter end
- **Verification**: Third-party verification required for large entities

### Key Requirements
- **Registration**: All regulated entities must register with CARB
- **Pathway Certification**: Fuel pathways must be CARB-certified  
- **Carbon Intensity**: Use CA-GREET methodology for CI calculations
- **Credit Generation**: Based on CI difference from regulatory benchmark
- **Compliance**: Annual compliance obligation based on fuel volumes

### Regulated Parties
- **Producers**: Refineries and fuel production facilities
- **Importers**: Entities importing fuel into California
- **Blenders**: Entities blending biofuels with conventional fuels
- **Distributors**: Large fuel distribution companies

## Implementation Timeline

### Phase 1: Foundation 
- Set up enhanced BOOST entities
- Load CARB pathway database
- Implement validation rules

### Phase 2: Processing 
- Build credit calculation engine
- Create transaction processing system
- Implement pathway attribution logic

### Phase 3: Reporting 
- Develop quarterly report generator
- Create CARB submission workflows
- Add compliance status tracking

### Phase 4: Integration 
- CARB LRT-CBTS API integration
- Third-party verification support
- Production deployment

### Phase 5: Production 
- User training and documentation
- Go-live support and monitoring

## Technical Requirements

### System Requirements
- **Database**: Entity storage with relationship support
- **API Integration**: CARB LRT-CBTS connectivity
- **Calculation Engine**: LCFS credit/deficit calculations
- **Report Generation**: CARB-compliant output formats

### Data Requirements
- **CARB Pathways**: Current certified pathway database
- **Regulatory Benchmarks**: Annual benchmark CI values
- **CA-GREET Data**: Carbon intensity calculation inputs
- **Organization Registration**: LCFS entity registration data

## Support and Resources

### Technical Support
- **BOOST Framework**: See main repository documentation
- **Implementation Questions**: Review implementation guide and workflow specification
- **Entity Design**: See entity mapping documentation

### Regulatory Support
- **CARB LCFS Program**: [https://ww2.arb.ca.gov/our-work/programs/low-carbon-fuel-standard](https://ww2.arb.ca.gov/our-work/programs/low-carbon-fuel-standard)
- **LRT-CBTS System**: [https://www.arb.ca.gov/fuels/lcfs/lrt-cbts/lrt-cbts.htm](https://www.arb.ca.gov/fuels/lcfs/lrt-cbts/lrt-cbts.htm)
- **CA-GREET Model**: [https://ww2.arb.ca.gov/resources/documents/ca-greet-3-0](https://ww2.arb.ca.gov/resources/documents/ca-greet-3-0)

### Verification Support
- **Approved Verifiers**: Contact CARB for current list of approved verification bodies
- **Verification Guidance**: See LCFS regulation Section 95132

## Getting Started Checklist

- [ ] Review LCFS Implementation Guide
- [ ] Understand entity relationship model  
- [ ] Set up development environment
- [ ] Implement core LCFS entities
- [ ] Load CARB pathway database
- [ ] Build credit calculation engine
- [ ] Create test transaction data
- [ ] Generate sample quarterly report
- [ ] Test CARB API integration (sandbox)
- [ ] Complete validation checklist
- [ ] Deploy to production

## Status

**Current Status**: ✅ **Documentation Complete**
- Comprehensive implementation guide
- Complete workflow specification  
- Detailed entity mapping
- Validation checklist ready

**Next Steps**: 🚧 **Implementation Phase**
- Code implementation of entities
- Credit calculation engine development
- CARB API integration testing
