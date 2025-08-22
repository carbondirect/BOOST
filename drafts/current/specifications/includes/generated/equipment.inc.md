<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: equipment/validation_schema.json and equipment_dictionary.md
     To modify this content, edit the source file and regenerate -->

Equipment entity representing forestry machinery and equipment used in biomass harvesting and processing operations

**[View Equipment in ERD Navigator](erd-navigator/index.html?focus=Equipment)**

### Relationships ### {{.unnumbered}}

- **organizationId** → [[#organization|Organization]] - Foreign key to owning organization

### Properties ### {{.unnumbered}}

<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Description
<th>Required
</tr>
</thead>
<tbody>
<tr>
<td><code>@context</code>
<td>object (structured)
<td>JSON-LD context for semantic web compatibility
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>Unique URI identifier for the equipment
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>string
<td>JSON-LD type identifier
<td>✓
</tr>
<tr>
<td><code>equipmentId</code>
<td>string (pattern)
<td>Unique identifier for the equipment
<td>✓
</tr>
<tr>
<td><code>equipmentName</code>
<td>string
<td>Descriptive name of the equipment
<td>✓
</tr>
<tr>
<td><code>equipmentType</code>
<td>enum(12 values)
<td>Type of forestry equipment
<td>✓
</tr>
<tr>
<td><code>operationalStatus</code>
<td>enum(5 values)
<td>Current operational status of the equipment
<td>✓
</tr>
<tr>
<td><code>organizationId</code>
<td>string (pattern)
<td>Foreign key to owning organization
<td>✓
</tr>
<tr>
<td><code>acquisitionCost</code>
<td>number (≥0)
<td>Equipment acquisition cost in USD
<td>
</tr>
<tr>
<td><code>acquisitionDate</code>
<td>string (date)
<td>Date equipment was acquired by organization
<td>
</tr>
<tr>
<td><code>assignedTrackingPointId</code>
<td>string (pattern)
<td>Foreign key to current location/assignment
<td>
</tr>
<tr>
<td><code>certifications</code>
<td>array&amp;lt;string&amp;gt;
<td>Equipment certifications (safety, emissions, etc.)
<td>
</tr>
<tr>
<td><code>currentOperatorId</code>
<td>string (pattern)
<td>Foreign key to current operator (if assigned)
<td>
</tr>
<tr>
<td><code>insuranceInfo</code>
<td>object (structured)
<td>Equipment insurance information
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of the most recent data update
<td>
</tr>
<tr>
<td><code>maintenanceSchedule</code>
<td>object (structured)
<td>Maintenance schedule information
<td>
</tr>
<tr>
<td><code>manufacturer</code>
<td>string
<td>Equipment manufacturer
<td>
</tr>
<tr>
<td><code>model</code>
<td>string
<td>Equipment model designation
<td>
</tr>
<tr>
<td><code>notes</code>
<td>string
<td>Additional notes or comments about the equipment
<td>
</tr>
<tr>
<td><code>serialNumber</code>
<td>string
<td>Manufacturer serial number
<td>
</tr>
<tr>
<td><code>specifications</code>
<td>object (structured)
<td>Technical specifications for the equipment
<td>
</tr>
<tr>
<td><code>yearManufactured</code>
<td>integer
<td>Year the equipment was manufactured
<td>
</tr>
</tbody>
</table>

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
