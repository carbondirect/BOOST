# BOOST JSON-LD Examples

This document provides practical examples of how BOOST entities can be represented using JSON-LD with the BOOST context. These examples demonstrate the semantic enhancement of existing BOOST JSON structures.

## Context Usage

All examples use the BOOST JSON-LD context:
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld"
}
```

## Core Entity Examples

### Organization Entity

**Traditional JSON:**
```json
{
  "organizationId": "ORG_ABC123",
  "name": "Sustainable Biomass Corp",
  "address": "123 Green Street, Portland, OR 97205, USA",
  "role": "BP",
  "scopeOfOperations": "North America",
  "legalEntityStatus": "Corporation",
  "certificateCode": "FSC-C123456",
  "contactInfo": "contact@sustainablebiomass.com"
}
```

**Enhanced JSON-LD:**
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "Organization",
  "@id": "boost:org/ABC123",
  "name": "Sustainable Biomass Corp",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Green Street",
    "addressLocality": "Portland",
    "addressRegion": "OR",
    "postalCode": "97205",
    "addressCountry": "US"
  },
  "role": "BP",
  "scopeOfOperations": "North America",
  "legalEntityStatus": "Corporation",
  "certificateCode": "boost:cert/FSC-C123456",
  "contactInfo": {
    "@type": "ContactPoint",
    "email": "contact@sustainablebiomass.com",
    "contactType": "customer service"
  },
  "globalLocationNumber": "1234567890123",
  "isActive": true,
  "lastUpdated": "2025-06-25T14:30:00Z"
}
```

### Material Entity

**Traditional JSON:**
```json
{
  "materialId": "MAT_789",
  "quantity": 10.5,
  "unit": "ton",
  "materialType": "Pellets",
  "category": "SBP-compliant",
  "species": "Pinus sylvestris",
  "countryOfOrigin": "FI",
  "source": "Managed forest",
  "rawMaterialEligibility": "Primary",
  "gmoStatus": false
}
```

**Enhanced JSON-LD:**
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "Material",
  "@id": "boost:material/MAT789",
  "quantity": {
    "@type": "QuantitativeValue",
    "value": 10.5,
    "unit": "TNE",
    "unitText": "metric tons"
  },
  "materialType": "Pellets",
  "category": "SBP-compliant",
  "species": "Pinus sylvestris",
  "countryOfOrigin": "boost:country/FI",
  "source": "Managed forest",
  "rawMaterialEligibility": "Primary",
  "gmoStatus": false,
  "location": {
    "@type": "Place",
    "name": "Finnish Forest Region",
    "latitude": 64.9841,
    "longitude": 25.7482
  },
  "wasGeneratedBy": "boost:activity/HARVEST_001",
  "productClass": "gs1:ProductClass/Wood_Pellets"
}
```

### DTSTransaction Entity

**Traditional JSON:**
```json
{
  "dtsTransactionId": "TX_456",
  "supplyingOrganizationId": "ORG_ABC123",
  "customerOrganizationId": "ORG_DEF789",
  "transactionDate": "2025-06-25T10:30:00Z",
  "salesDocumentId": "SDD_123"
}
```

**Enhanced JSON-LD:**
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "DTSTransaction",
  "@id": "boost:transaction/TX456",
  "supplyingOrganizationId": "boost:org/ABC123",
  "customerOrganizationId": "boost:org/DEF789", 
  "transactionDate": "2025-06-25T10:30:00Z",
  "salesDocumentId": "boost:doc/SDD123",
  "startedAtTime": "2025-06-25T10:30:00Z",
  "wasAssociatedWith": [
    {
      "@id": "boost:org/ABC123",
      "role": "supplier"
    },
    {
      "@id": "boost:org/DEF789", 
      "role": "customer"
    }
  ],
  "contains": [
    "boost:batch/BATCH001",
    "boost:batch/BATCH002"
  ]
}
```

### Certificate Entity

**Traditional JSON:**
```json
{
  "certificateNumber": "FSC-C123456",
  "dateOfIssue": "2024-01-15",
  "dateOfExpiry": "2029-01-15",
  "scopeOfCertification": "Chain of Custody",
  "versionNumber": "v5.0",
  "cbId": "CB_FSC01",
  "organizationId": "ORG_ABC123"
}
```

**Enhanced JSON-LD:**
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "Certificate",
  "@id": "boost:cert/FSC-C123456",
  "certificateNumber": "FSC-C123456",
  "dateOfIssue": "2024-01-15",
  "dateOfExpiry": "2029-01-15",
  "scopeOfCertification": "Chain of Custody",
  "status": "Valid",
  "versionNumber": "v5.0",
  "cbId": "boost:cb/FSC01",
  "organizationId": "boost:org/ABC123",
  "certificationSchemeId": "boost:scheme/FSC",
  "issuedBy": "boost:cb/FSC01",
  "certifiesAgainst": "boost:scheme/FSC",
  "lastUpdated": "2024-01-15T09:00:00Z"
}
```

### TransactionBatch Entity with Complex Relationships

**Enhanced JSON-LD:**
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "TransactionBatch",
  "@id": "boost:batch/BATCH001",
  "transactionBatchId": "BATCH001",
  "dtsTransactionId": "boost:transaction/TX456",
  "productionBatchId": "boost:production/PROD789",
  "quantity": {
    "@type": "QuantitativeValue",
    "value": 5.2,
    "unit": "TNE"
  },
  "claimId": "boost:claim/CLAIM001",
  "contains": "boost:material/MAT789",
  "associatedWith": [
    "boost:energyCarbon/EC001",
    "boost:energyCarbon/EC002"
  ],
  "verifiedBy": "boost:verification/VS001",
  "wasDerivedFrom": "boost:material/RAW456",
  "wasGeneratedBy": "boost:activity/PROCESSING_001"
}
```

## Advanced Examples

### Supply Chain Traceability Chain

```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@graph": [
    {
      "@type": "Material",
      "@id": "boost:material/LOGS001",
      "materialType": "Roundwood",
      "species": "Pinus sylvestris",
      "quantity": {
        "value": 50.0,
        "unit": "TNE"
      },
      "location": {
        "@type": "Place",
        "name": "Managed Forest Block A7",
        "latitude": 65.0124,
        "longitude": 25.4681
      }
    },
    {
      "@type": "Material", 
      "@id": "boost:material/CHIPS001",
      "materialType": "Chips",
      "quantity": {
        "value": 25.0,
        "unit": "TNE"
      },
      "wasDerivedFrom": "boost:material/LOGS001",
      "wasGeneratedBy": "boost:activity/CHIPPING_001"
    },
    {
      "@type": "Material",
      "@id": "boost:material/PELLETS001", 
      "materialType": "Pellets",
      "quantity": {
        "value": 20.0,
        "unit": "TNE"
      },
      "wasDerivedFrom": "boost:material/CHIPS001",
      "wasGeneratedBy": "boost:activity/PELLETIZING_001"
    }
  ]
}
```

### Mass Balance Account with Semantic Relationships

```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "MassBalanceAccount",
  "@id": "boost:account/MBA001",
  "organizationId": "boost:org/ABC123",
  "productGroupId": "boost:productGroup/PG001",
  "periodInputs": 1000.0,
  "periodOutputs": 950.0,
  "currentBalance": 50.0,
  "balancingPeriod": "2025-Q2",
  "conversionFactors": 0.95,
  "manages": [
    "boost:material/PELLETS001",
    "boost:material/PELLETS002"
  ],
  "tracks": "boost:productGroup/PG001"
}
```

### Energy and Carbon Data with Measurements

```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "EnergyCarbonData",
  "@id": "boost:energyCarbon/EC001",
  "dataType": "carbon_footprint",
  "value": 15.2,
  "unit": "KGM",
  "unitText": "kg CO2e per metric ton",
  "source": "LCA analysis",
  "measurementMethod": "ISO 14067",
  "characterizedBy": "boost:material/PELLETS001",
  "wasGeneratedBy": "boost:activity/LCA_ANALYSIS_001"
}
```

### Verification Statement with Provenance

```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "VerificationStatement", 
  "@id": "boost:verification/VS001",
  "verificationDate": "2025-06-20",
  "issuingBody": "Third Party Verifier Inc",
  "scope": "Supply chain sustainability claims",
  "transactionBatchId": "boost:batch/BATCH001",
  "verifiedBy": "boost:cb/TPV01",
  "wasInformedBy": "boost:audit/AUDIT001",
  "wasAttributedTo": "boost:auditor/JOHN_DOE"
}
```

## Query Examples

### SPARQL Queries for Enhanced Data

#### Find Complete Supply Chain for a Material
```sparql
PREFIX boost: <https://boost.carbondirect.io/schema/>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?material ?predecessor ?activity WHERE {
  boost:material/PELLETS001 prov:wasDerivedFrom* ?material .
  ?material prov:wasDerivedFrom ?predecessor .
  ?material prov:wasGeneratedBy ?activity .
}
```

#### Calculate Total Carbon Footprint for Transaction
```sparql
PREFIX boost: <https://boost.carbondirect.io/schema/>
PREFIX schema: <https://schema.org/>

SELECT ?transaction (SUM(?carbonValue) as ?totalCarbon) WHERE {
  ?transaction boost:contains ?batch .
  ?batch boost:associatedWith ?carbonData .
  ?carbonData boost:dataType "carbon_footprint" .
  ?carbonData schema:value ?carbonValue .
  FILTER(?transaction = boost:transaction/TX456)
}
```

#### Find All Certificates for an Organization
```sparql
PREFIX boost: <https://boost.carbondirect.io/schema/>

SELECT ?certificate ?scheme ?status ?expiry WHERE {
  boost:org/ABC123 boost:has ?certificate .
  ?certificate boost:certifiesAgainst ?scheme .
  ?certificate boost:certificateStatus ?status .
  ?certificate boost:dateOfExpiry ?expiry .
}
```

## Migration Strategy

### Step 1: Add Context to Existing JSON
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  // ... existing JSON properties remain unchanged
}
```

### Step 2: Add @type and @id
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "Organization",
  "@id": "boost:org/ABC123",
  // ... existing properties
}
```

### Step 3: Enhance with Semantic Relationships
```json
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "@type": "Organization", 
  "@id": "boost:org/ABC123",
  // ... existing properties
  "has": ["boost:cert/FSC-C123456"],
  "manages": ["boost:account/MBA001"]
}
```

This gradual approach ensures backward compatibility while enabling semantic capabilities.