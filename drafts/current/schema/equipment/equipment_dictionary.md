# Equipment Entity Dictionary

## Overview
The Equipment entity represents forestry machinery and equipment used in biomass harvesting, processing, and transportation operations. This entity enables tracking of equipment ownership, utilization, maintenance, and operational status within the BOOST supply chain.

## Business Purpose
- **Asset Management**: Track ownership and location of forestry equipment
- **Operational Planning**: Assign equipment to specific harvest sites and operations
- **Maintenance Tracking**: Monitor equipment condition and service schedules
- **Cost Allocation**: Associate equipment costs with specific operations and TRUs
- **Regulatory Compliance**: Track equipment certifications and emissions compliance
- **Insurance Management**: Maintain equipment insurance and coverage information

## Core Fields

### Identity Fields
- **equipmentId** (PK): Unique identifier using EQ- prefix pattern (e.g., EQ-HARVESTER-001)
- **equipmentName**: Descriptive name combining manufacturer and model (e.g., "John Deere 770G Harvester")
- **equipmentType**: Standardized equipment category for operational planning

### Organizational Relationships
- **organizationId** (FK): Links to owning Organization entity
- **currentOperatorId** (FK): Optional link to currently assigned Operator
- **assignedTrackingPointId** (FK): Current location or operational assignment

### Technical Specifications
- **manufacturer**: Equipment manufacturer (John Deere, Caterpillar, etc.)
- **model**: Specific model designation
- **serialNumber**: Manufacturer serial number for warranty and service
- **yearManufactured**: Manufacturing year for age and depreciation tracking
- **specifications**: Technical details including capacity, engine power, and weight

### Operational Management
- **operationalStatus**: Current status (active, maintenance, inactive, retired, repair)
- **maintenanceSchedule**: Service intervals, last service, and operating hours
- **certifications**: Safety, emissions, and regulatory certifications

### Financial Information
- **acquisitionDate**: When equipment was acquired by the organization
- **acquisitionCost**: Purchase or lease cost for depreciation calculations
- **insuranceInfo**: Policy details for risk management

## Equipment Types

### Primary Harvesting Equipment
- **harvester**: Felling and delimbing machines (e.g., John Deere 770G)
- **skidder**: Log transport from harvest site to landing (e.g., Caterpillar 535D)
- **forwarder**: Cut-to-length log transport (e.g., Ponsse Buffalo)

### Processing Equipment
- **chipper**: Wood chipping for biomass production
- **debarker**: Bark removal from logs
- **grinder**: Size reduction of wood waste
- **screener**: Material size classification

### Support Equipment
- **loader**: Material handling and loading (e.g., Liebherr L580)
- **conveyor**: Material transport systems
- **saw**: Cutting and bucking operations
- **kiln**: Drying operations for processed materials

## Usage Patterns

### Equipment Assignment Workflow
1. **Acquisition**: Equipment acquired by Organization, recorded with specifications
2. **Assignment**: Equipment assigned to TrackingPoint (harvest site, mill yard)
3. **Operation**: Current Operator assigned for daily operations
4. **Maintenance**: Status updated for scheduled or unscheduled maintenance
5. **Reassignment**: Equipment moved between locations as operations require

### Cost Allocation
- Equipment costs allocated to TRUs based on operational assignments
- Maintenance costs tracked against equipment for total cost of ownership
- Insurance and depreciation distributed across operations

### Compliance Tracking
- Emissions certifications ensure regulatory compliance
- Safety certifications validate operator training requirements
- Insurance tracking prevents operational gaps in coverage

## Relationships

### Organization → Equipment (One-to-Many)
- Organizations own and manage multiple pieces of equipment
- Equipment ownership determines operational responsibility
- Cost center allocation follows ownership structure

### Equipment → Operator (Many-to-One, Optional)
- Equipment can be operated by different operators over time
- Current operator assignment for accountability and training verification
- Operator certifications must match equipment requirements

### Equipment → TrackingPoint (Many-to-One, Optional)
- Equipment assigned to specific operational locations
- Enables spatial tracking of equipment utilization
- Supports operational planning and logistics

## Data Quality Considerations

### Required Information
- All equipment must have unique ID, name, type, and owning organization
- Operational status required for planning and allocation decisions
- Basic manufacturer and model information for service and parts management

### Optional but Important
- Operator assignments improve accountability and training compliance
- Location assignments enable better operational planning
- Maintenance schedules prevent unexpected downtime
- Financial information supports asset management decisions

### Validation Rules
- Equipment can only be assigned to one operator at a time
- Operational status must be consistent with assignments (inactive equipment shouldn't have operators)
- Maintenance schedules should align with manufacturer recommendations
- Certifications should be current for active equipment

## Integration Points

### TraceableUnit Integration
- Equipment usage tracked against TRUs for cost allocation
- Processing operations link equipment to material transformations
- Harvest operations connect equipment to TRU creation

### MaterialProcessing Integration
- Processing equipment linked to specific material transformations
- Equipment specifications influence processing capacity and output quality
- Maintenance schedules affect processing operation planning

### Compliance Integration
- Equipment certifications support regulatory reporting requirements
- Emissions data contributes to carbon footprint calculations
- Safety certifications ensure operational compliance

This Equipment entity provides comprehensive asset management capabilities while supporting the operational and regulatory requirements of biomass supply chain management.