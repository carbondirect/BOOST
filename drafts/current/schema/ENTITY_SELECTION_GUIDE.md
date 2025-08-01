# BOOST Entity Selection Guide

## Customer vs Organization Usage Guidelines

### Overview

The BOOST data standard includes separate entities for **Customer** and **Organization** to support different business scenarios and data modeling needs. This guide clarifies when to use each entity type and how they interact within the biomass supply chain.

### Entity Purposes

#### Organization 🏢
**Primary Purpose**: Represents business entities that actively participate in the biomass supply chain with operational capabilities.

**Key Characteristics**:
- Has operational roles (harvester, processor, certifier, transporter, supplier, manufacturer, producer, importer, blender, distributor)
- Can hold certifications and manage supply chain operations
- Maintains operational status and geographic presence
- References primary and operational geographic locations
- Can employ operators and manage traceable units
- Central to chain of custody tracking

#### Customer 🏭
**Primary Purpose**: Represents buyers/purchasers in commercial transactions, regardless of their operational capabilities.

**Key Characteristics**:
- Focused on purchasing and receiving materials
- Simplified entity optimized for transaction processing
- May or may not have operational capabilities within BOOST scope
- Geographic data limited to delivery/billing location
- Referenced primarily in Transaction entities

### Usage Decision Matrix

| Scenario | Use Entity | Rationale |
|----------|------------|-----------|
| **Forest harvesting company** | Organization | Active supply chain participant with operational role |
| **Wood processing mill** | Organization | Operational participant that processes Traceable Units |
| **Energy producer buying biomass** | Customer | Primary role is purchasing, not operational within biomass chain |
| **Biomass trader/broker** | Organization | Active intermediary managing supply chain operations |
| **Paper mill buying wood chips** | Customer | End consumer, focus on purchasing transaction |
| **Certification body** | Organization | Service provider with operational role in certification |
| **Transportation company** | Organization | Operational participant managing TRU movement |
| **Retail energy company** | Customer | Purchasing entity, minimal operational involvement |

### Dual Entity Scenarios

Some business entities may be represented as **both** Customer and Organization:

#### When to Use Both:
- **Large integrated companies** that both produce and consume biomass
- **Energy producers** that also operate harvesting/processing facilities  
- **Multi-role organizations** with distinct purchasing and operational functions

#### Implementation Approach:
```json
{
  "organization": {
    "@id": "https://boost.example/org/pacific-energy-001",
    "organizationId": "ORG-PACIFIC-ENERGY-001",
    "organizationName": "Pacific Energy Solutions LLC",
    "organizationType": "manufacturer"
  },
  "customer": {
    "@id": "https://boost.example/customer/pacific-energy-001", 
    "customerId": "CUST-PACIFIC-ENERGY-001",
    "customerName": "Pacific Energy Solutions LLC - Purchasing Dept"
  }
}
```

### Relationship Patterns

#### Organization-Centric Relationships:
- **Organization** → **TraceableUnit** (via harvesterId)
- **Organization** → **Certificate** (certificate holder)
- **Organization** → **TrackingPoint** (site management)
- **Organization** → **Operator** (employment)
- **Organization** → **Transaction** (seller role)

#### Customer-Centric Relationships:
- **Customer** → **Transaction** (buyer role)
- **Customer** → **GeographicData** (delivery location)

### Business Rules

#### Organization Requirements:
1. Must have an `organizationType` from the defined enum
2. Required for entities that participate in chain of custody
3. Can reference multiple geographic locations (HQ + operational areas)
4. Must maintain operational status for related entity validation

#### Customer Requirements:
1. Must have valid `customerId` with pattern `^CUST-[A-Z0-9-_]+$`
2. Required for commercial transaction recording
3. Single geographic reference for delivery/billing
4. No operational status requirements

### Data Quality Considerations

#### Avoid These Anti-Patterns:
❌ **Using Organization for simple end customers** - Creates unnecessary complexity
❌ **Using Customer for operational entities** - Loses supply chain traceability  
❌ **Duplicate data across both entities** - Maintenance burden and consistency issues
❌ **Mixing roles within single entity type** - Confuses business semantics

#### Follow These Best Practices:
✅ **Start with business role analysis** - What does this entity actually do?
✅ **Consider data consumer needs** - Who will query this information?
✅ **Plan for entity relationships** - What other entities need to reference this?
✅ **Document entity selection rationale** - Why was this choice made?

### Migration Guidelines

#### When Converting Customer → Organization:
1. Verify operational role justification
2. Add required `organizationType`
3. Update referencing Transaction entities
4. Add geographic operational areas if applicable
5. Consider certification and operator relationships

#### When Converting Organization → Customer:
1. Verify limited operational involvement
2. Simplify to core customer attributes
3. Ensure Transaction references remain valid
4. Archive operational data appropriately

### Integration with External Systems

#### ERP/Accounting Systems:
- **Organizations** typically map to vendors/suppliers
- **Customers** typically map to customer master records
- Consider separate integration endpoints for each entity type

#### Regulatory Reporting:
- **Organizations** required for supply chain compliance reporting
- **Customers** sufficient for sales/delivery documentation
- Certification chains require Organization entities

This entity selection guide ensures consistent, appropriate usage of Customer and Organization entities while supporting the full range of biomass supply chain business scenarios.