# BOOST Validation Rules and Constraints
## Comprehensive Data Integrity Framework

This document defines the complete validation framework for the BOOST (Biomass Open Origin Standard for Tracking) data model, ensuring data integrity, consistency, and regulatory compliance across all entities and relationships.

---

## Overview

The BOOST validation framework operates at four levels:
1. **Schema-Level Validation**: JSON Schema constraints for individual entities
2. **Cross-Entity Validation**: Relationship integrity and foreign key constraints
3. **Business Logic Validation**: Domain-specific rules and calculations
4. **Regulatory Compliance Validation**: Certification and reporting requirements

---

## Schema-Level Validation Rules

### Universal Requirements

All BOOST entities must include:
- **JSON-LD Context**: `@context`, `@type`, `@id` fields for semantic web compatibility
- **Primary Identifier**: Entity-specific ID with standardized pattern
- **Timestamp Fields**: ISO 8601 date-time format for all temporal data
- **Foreign Key Format**: EntityNameId convention for all references
- **Additional Properties**: Disabled (`additionalProperties: false`) for strict validation

### Entity-Specific Validation

#### Organization Entity
```json
{
  "organizationId": {
    "required": true,
    "pattern": "^ORG-[A-Z0-9-_]+$",
    "minLength": 5,
    "maxLength": 50
  },
  "organizationName": {
    "required": true,
    "minLength": 1,
    "maxLength": 200
  },
  "organizationType": {
    "required": true,
    "enum": ["harvester", "processor", "certifier", "transporter", "supplier", "manufacturer", "producer", "importer", "blender", "distributor"]
  }
}
```

#### Transaction Entity
```json
{
  "transactionId": {
    "required": true,
    "pattern": "^TXN-[A-Z0-9-_]+$"
  },
  "contractValue": {
    "type": "number",
    "minimum": 0,
    "maximum": 999999999.99
  },
  "transactionDate": {
    "required": true,
    "format": "date"
  },
  "OrganizationId": {
    "required": true,
    "pattern": "^ORG-[A-Z0-9-_]+$"
  },
  "CustomerId": {
    "required": true,
    "pattern": "^CUST-[A-Z0-9-_]+$"
  }
}
```

#### TraceableUnit Entity
```json
{
  "traceableUnitId": {
    "required": true,
    "pattern": "^TRU-[A-Z0-9-_]+$"
  },
  "volume": {
    "type": "number",
    "minimum": 0,
    "maximum": 999999
  },
  "mass": {
    "type": "number",
    "minimum": 0,
    "maximum": 999999
  },
  "OrganizationId": {
    "required": true,
    "pattern": "^ORG-[A-Z0-9-_]+$"
  }
}
```

#### MaterialProcessing Entity
```json
{
  "processingId": {
    "required": true,
    "pattern": "^PROC-[A-Z0-9-_]+$"
  },
  "processType": {
    "required": true,
    "enum": ["felling", "delimbing", "crosscutting", "chipping", "debarking", "assortment"]
  },
  "inputVolume": {
    "type": "number",
    "minimum": 0
  },
  "outputVolume": {
    "type": "number",
    "minimum": 0
  },
  "volumeLoss": {
    "type": "number",
    "minimum": 0
  }
}
```

#### Certificate Entity
```json
{
  "certificateId": {
    "required": true,
    "pattern": "^CERT-[A-Z0-9-_]+$"
  },
  "certificateStatus": {
    "required": true,
    "enum": ["valid", "expired", "suspended", "revoked"]
  },
  "issueDate": {
    "required": true,
    "format": "date"
  },
  "expiryDate": {
    "required": true,
    "format": "date"
  }
}
```

---

## Cross-Entity Validation Rules

### Foreign Key Integrity

All entity references must resolve to valid, existing entities:

#### Organization References
- `OrganizationId` in Transaction → Must exist in Organization entity
- `OrganizationId` in TraceableUnit → Must exist in Organization entity
- `organizationId` in Operator → Must exist in Organization entity

#### Geographic Data References
- `primaryGeographicDataId` in Organization → Must exist in GeographicData entity
- `harvestGeographicDataId` in TraceableUnit → Must exist in GeographicData entity
- `processingGeographicDataId` in MaterialProcessing → Must exist in GeographicData entity

#### Supply Chain References
- `inputTraceableUnitId` in MaterialProcessing → Must exist in TraceableUnit entity
- `outputTraceableUnitId` in MaterialProcessing → Must exist in TraceableUnit entity
- `TraceableUnitId` in Transaction → Must exist in TraceableUnit entity

### Relationship Cardinality Rules

#### One-to-Many Relationships
- Organization → Multiple TraceableUnits (1:N)
- Organization → Multiple Transactions (1:N)
- TraceableUnit → Multiple MaterialProcessing (as input) (1:N)
- Certificate → Multiple Organizations (1:N)

#### Many-to-One Relationships
- Multiple TraceableUnits → One Organization (N:1)
- Multiple Transactions → One Organization (N:1)
- Multiple MaterialProcessing → One TraceableUnit (as output) (N:1)

### Circular Reference Detection

Prevent circular dependencies in processing chains:
- MaterialProcessing input/output chains must be acyclic
- TraceableUnit parent/child relationships must be acyclic
- Geographic data hierarchies must be acyclic

---

## Business Logic Validation Rules

### Volume and Mass Balance

#### Processing Conservation Rules
```javascript
// Volume conservation in MaterialProcessing
inputVolume >= (outputVolume + volumeLoss)
volumeLoss >= 0
outputVolume > 0 (for valid processing)

// Mass balance validation
if (inputMass && outputMass) {
  inputMass >= outputMass
  massLoss = inputMass - outputMass
  massLoss >= 0
}
```

#### Transaction Quantity Validation
```javascript
// Transaction quantities must not exceed available TRU volumes
transaction.quantity <= traceableUnit.volume
transaction.quantity > 0

// Cumulative transactions cannot exceed TRU capacity
sum(transactions.quantity) <= traceableUnit.volume
```

### Temporal Validation

#### Date Sequence Rules
```javascript
// Processing dates must be chronological
materialProcessing.processTimestamp >= inputTRU.harvestDate

// Transaction dates must be after production
transaction.transactionDate >= traceableUnit.harvestDate

// Certificate validity
certificate.issueDate <= certificate.expiryDate
current_date <= certificate.expiryDate (for active certificates)
```

#### Harvesting Season Validation
```javascript
// Validate harvest dates against species growing seasons
if (species.requiresSeasonalHarvest) {
  harvest.date.month in species.validHarvestMonths
}
```

### Geographic Consistency

#### Proximity Validation
```javascript
// Processing locations must be within reasonable distance of harvest
distance(harvest.location, processing.location) <= maxTransportDistance

// Organization operational areas must contain referenced locations
organization.operationalAreas.contains(processing.location)
```

#### Jurisdiction Compliance
```javascript
// Certifications must be valid in harvest jurisdiction
certificate.validJurisdictions.contains(harvest.jurisdiction)

// Regulatory compliance by location
if (location.country === "USA" && location.state === "CA") {
  // California-specific validation rules
  validateLCFSCompliance(transaction)
}
```

### Species and Material Validation

#### Species Composition Rules
```javascript
// Species percentages must sum to 100%
sum(speciesComponent.percentage) === 100.0

// Individual species percentages must be valid
speciesComponent.percentage >= 0.0
speciesComponent.percentage <= 100.0
```

#### Plant Part Consistency
```javascript
// Plant parts must be appropriate for species
if (species.type === "coniferous") {
  allowedParts = ["trunk", "branches", "twigs", "bark", "needles", "cones"]
} else if (species.type === "deciduous") {
  allowedParts = ["trunk", "branches", "twigs", "bark", "leaves", "seeds"]
}
plantPart.type in allowedParts
```

---

## Regulatory Compliance Validation

### Certification Requirements

#### Certificate Chain Validation
```javascript
// Chain of custody certificates must be continuous
for each transaction in supply_chain {
  transaction.seller_certificate.validAt(transaction.date)
  transaction.buyer_certificate.validAt(transaction.date)
  transaction.seller_certificate.scope.covers(transaction.material)
}
```

#### Certification Body Authorization
```javascript
// Certification bodies must be authorized for scheme and region
certificationBody.authorizedSchemes.contains(certificate.scheme)
certificationBody.authorizedRegions.contains(certificate.region)
certificationBody.status === "active"
```

### LCFS-Specific Validation

#### Pathway Certification
```javascript
// LCFS pathways must be CARB-certified and current
lcfsPathway.certificationStatus === "active"
lcfsPathway.expirationDate >= transaction.date
lcfsPathway.feedstockCategory.matches(traceableUnit.materialType)
```

#### Credit Calculation Validation
```javascript
// LCFS credit calculations must use approved formulas
credits = (benchmarkCI - pathwayCI) * fuelVolumeMJ * energyEconomyRatio
credits >= 0 // No negative credits allowed
benchmarkCI >= pathwayCI // Must provide carbon benefit
```

### SBP Compliance Validation

#### Supply Base Assessment
```javascript
// Supply base must have valid SBP assessment
supplyBase.sbpAssessment.status === "approved"
supplyBase.sbpAssessment.expiryDate >= harvest.date
harvest.location within supplyBase.assessedArea
```

#### Risk Assessment Coverage
```javascript
// All risk categories must be assessed
requiredRiskCategories = ["biodiversity", "soil", "water", "air", "carbon", "local_economy", "social"]
supplyBase.riskAssessment.categories includes_all requiredRiskCategories
```

---

## Data Quality Validation

### Completeness Checks

#### Required Field Validation
- All required fields must be present and non-null
- Required arrays must contain at least one element
- Required objects must contain all mandatory properties

#### Referential Integrity
- All foreign key references must resolve to existing entities
- Deleted entities must not be referenced by active entities
- Entity status must be consistent across references

### Consistency Validation

#### Data Type Consistency
```javascript
// Numeric fields must be consistent across related entities
if (traceableUnit.volume && transaction.quantity) {
  typeof traceableUnit.volume === typeof transaction.quantity
  traceableUnit.volumeUnit === transaction.quantityUnit
}
```

#### Enumeration Consistency
```javascript
// Enum values must be consistent across related entities
if (organization.organizationType === "harvester") {
  traceableUnit.sourceType in ["harvest", "forest_residue"]
}
```

### Accuracy Validation

#### Range Validation
```javascript
// Values must be within realistic business ranges
volume >= 0 && volume <= 999999 // cubic meters
mass >= 0 && mass <= 999999 // metric tons
percentage >= 0.0 && percentage <= 100.0
carbonIntensity >= 0.0 && carbonIntensity <= 1000.0 // gCO2e/MJ
```

#### Precision Validation
```javascript
// Decimal places must be appropriate for measurement type
volume: max 3 decimal places
mass: max 3 decimal places
percentage: max 2 decimal places
monetary: max 2 decimal places
```

---

## Validation Implementation

### Schema Validation Order

1. **JSON Schema Validation**: Basic structure and data types
2. **Required Field Validation**: Presence of mandatory fields
3. **Format Validation**: Patterns, ranges, and enumerations
4. **Cross-Entity Validation**: Foreign key integrity
5. **Business Logic Validation**: Domain-specific rules
6. **Regulatory Compliance Validation**: Certification and reporting rules

### Error Handling

#### Validation Error Types
- **SCHEMA_ERROR**: JSON Schema validation failure
- **REQUIRED_FIELD_ERROR**: Missing required field
- **FORMAT_ERROR**: Invalid format or pattern
- **REFERENCE_ERROR**: Invalid foreign key reference
- **BUSINESS_LOGIC_ERROR**: Business rule violation
- **COMPLIANCE_ERROR**: Regulatory requirement violation

#### Error Response Format
```json
{
  "valid": false,
  "errors": [
    {
      "type": "REQUIRED_FIELD_ERROR",
      "field": "organizationId",
      "message": "Required field 'organizationId' is missing",
      "code": "E001"
    },
    {
      "type": "BUSINESS_LOGIC_ERROR",
      "field": "outputVolume",
      "message": "Output volume (1500) exceeds input volume (1200)",
      "code": "B005"
    }
  ],
  "warnings": [
    {
      "type": "DATA_QUALITY_WARNING",
      "field": "volume",
      "message": "Volume precision exceeds recommended 3 decimal places",
      "code": "W002"
    }
  ]
}
```

### Performance Optimization

#### Validation Caching
- Cache validation results for immutable entities
- Skip redundant cross-entity checks for unchanged references
- Batch validation for multiple entities

#### Selective Validation
- Skip business logic validation for draft entities
- Validate only modified fields in update operations
- Defer expensive compliance checks to background processes

---

## Testing and Quality Assurance

### Validation Test Categories

1. **Schema Compliance Tests**: Valid and invalid entity structures
2. **Cross-Entity Reference Tests**: Valid and broken foreign key relationships
3. **Business Logic Tests**: Valid and invalid business rule scenarios
4. **Regulatory Compliance Tests**: Certification and reporting edge cases
5. **Performance Tests**: Large-scale validation scenarios

### Test Data Requirements

- **Valid Examples**: Complete, compliant entity instances for each type
- **Invalid Examples**: Systematically broken entities for each validation rule
- **Edge Cases**: Boundary conditions and unusual but valid scenarios
- **Integration Tests**: Complete supply chain validation scenarios

---

## Maintenance and Updates

### Schema Evolution
- Maintain backward compatibility for existing validation rules
- Version validation schemas with semantic versioning
- Provide migration guides for validation rule changes
- Test validation changes against existing data sets

### Regulatory Updates
- Monitor regulatory changes affecting validation requirements
- Update compliance validation rules for new regulations
- Maintain audit trail of validation rule changes
- Coordinate validation updates with standards releases

This comprehensive validation framework ensures data integrity, regulatory compliance, and business rule adherence across the entire BOOST ecosystem.