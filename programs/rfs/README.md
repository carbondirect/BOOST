# RFS - Renewable Fuel Standard

BOOST implementation for US EPA's Renewable Fuel Standard program.

## Overview

The **Renewable Fuel Standard (RFS)** is the US EPA's biofuel program that requires renewable fuel to be blended into transportation fuel. This BOOST extension provides entity framework and workflow support for RFS compliance.

### Key Features

🚧 **RIN Tracking** - Renewable Identification Number management  
🚧 **Pathway Verification** - EPA-approved pathway tracking  
🚧 **Quarterly Reporting** - EPA EMTS system integration  
🚧 **D-Code Management** - Fuel category classification  
🚧 **Generation/Separation** - RIN lifecycle tracking  

## Quick Start

### RFS Program Background

**Administrator**: US Environmental Protection Agency (EPA)  
**Program Type**: Renewable fuel volume mandates with RIN trading  
**Reporting**: Quarterly and annual submissions to EPA  
**System**: EPA Moderated Transaction System (EMTS)  

### Key Components

- **RINs**: Renewable Identification Numbers for fuel tracking
- **D-Codes**: Fuel category classifications (D3, D4, D5, D6, D7)
- **Pathways**: EPA-approved production pathways
- **EMTS**: EPA's electronic tracking and reporting system

## Documentation

### Available Documentation
- **Examples**: Sample RFS transaction payloads
  - `RFS_woodchip_tx_example.json` - Wood chip transaction example
  - `RFS_woodchip_tx_example.yaml` - YAML format example

### Documentation Needed
- [ ] RFS Implementation Guide
- [ ] RFS Workflow Specification  
- [ ] RFS Entity Mapping
- [ ] RFS Validation Checklist

## RFS Entities (Planned)

### Enhanced Core Entities
- `Organization` + EPA registration and company type
- `Transaction` + RIN assignment and D-code tracking
- `Material` + feedstock qualification and pathway mapping

### New RFS Entities
- `RFSPathway` - EPA-approved production pathways
- `RIN` - Renewable Identification Number tracking
- `RFSReporting` - Quarterly and annual EPA reports

## Implementation Status

**Current Status**: 📋 **Planning Phase**
- Sample transaction data available
- Entity design in progress
- Documentation development needed

**Next Steps**:
1. Develop RFS entity specifications
2. Create implementation documentation
3. Build RFS workflow processes
4. EPA EMTS integration planning

## EPA Resources

- **RFS Program**: [https://www.epa.gov/renewable-fuel-standard-program](https://www.epa.gov/renewable-fuel-standard-program)
- **EMTS System**: [https://www.epa.gov/fuels-registration-reporting-and-compliance-help/emts-users](https://www.epa.gov/fuels-registration-reporting-and-compliance-help/emts-users)
- **Pathway Database**: [https://www.epa.gov/renewable-fuel-standard-program/approved-pathways-renewable-fuel](https://www.epa.gov/renewable-fuel-standard-program/approved-pathways-renewable-fuel)

## Contributing

RFS implementation is in early planning phase. Contributions welcome for:
- Entity design and specifications
- Workflow documentation
- EPA EMTS integration research
- Sample data and examples