# JSON-LD Context and Semantic Web Integration # {#jsonld-context}

BOOST implements JSON-LD (JSON for Linking Data) as its primary serialization format, enabling semantic web compatibility, data linking, and machine-readable context definitions. This section explains the JSON-LD context structure, semantic annotations, and integration with existing ontologies.

## JSON-LD Overview ## {#jsonld-overview}

JSON-LD extends standard JSON with semantic web capabilities through:

- **@context**: Defines mappings between JSON properties and RDF vocabularies
- **@id**: Provides unique identifiers for entities (IRIs)
- **@type**: Specifies the semantic type of an entity
- **@vocab**: Sets a default vocabulary for properties
- **Linked Data**: Enables connections between distributed datasets

## BOOST Context Definition ## {#boost-context}

The BOOST JSON-LD context maps entity properties to established vocabularies:

<pre class="json">
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "gs1": "https://gs1.org/voc/",
    "biomass": "http://example.org/biomass#",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    
    "TraceableUnit": "biomass:TraceableUnit",
    "Organization": "schema:Organization",
    "Transaction": "schema:Order",
    "MaterialProcessing": "prov:Activity",
    
    "traceableUnitId": {
      "@id": "schema:identifier",
      "@type": "schema:Text"
    },
    "organizationId": {
      "@id": "schema:identifier",
      "@type": "schema:Text"
    },
    "createdAt": {
      "@id": "schema:dateCreated",
      "@type": "xsd:dateTime"
    },
    "modifiedAt": {
      "@id": "schema:dateModified",
      "@type": "xsd:dateTime"
    }
  }
}
</pre>

## Vocabulary Mappings ## {#vocabulary-mappings}

### Schema.org Integration ### {#schema-org-integration}

BOOST entities map to Schema.org types for web compatibility:

- **Organization** → `schema:Organization`
- **Transaction** → `schema:Order`
- **GeographicData** → `schema:Place`
- **Certificate** → `schema:Certification`
- **Claim** → `schema:Claim`

### W3C PROV Ontology ### {#prov-ontology}

Provenance tracking using PROV vocabulary:

- **MaterialProcessing** → `prov:Activity`
- **ProcessingHistory** → `prov:Entity`
- **Operator** → `prov:Agent`
- **wasGeneratedBy** → `prov:wasGeneratedBy`
- **wasAttributedTo** → `prov:wasAttributedTo`

### GS1 Vocabulary ### {#gs1-vocabulary}

Supply chain standards alignment:

- **productCode** → `gs1:gtin`
- **locationCode** → `gs1:gln`
- **shipmentId** → `gs1:sscc`
- **batchNumber** → `gs1:batchNumber`

## Entity Context Examples ## {#entity-context-examples}

### TraceableUnit with Context ### {#tru-with-context}

Complete JSON-LD representation of a TraceableUnit:

<pre class="json">
{
  "@context": "https://boost.org/context.jsonld",
  "@type": "biomass:TraceableUnit",
  "@id": "https://example.org/tru/TRU-2025-001",
  
  "traceableUnitId": "TRU-2025-001",
  "unitType": "pile",
  "totalVolume": {
    "@type": "qudt:QuantityValue",
    "qudt:value": 500.0,
    "qudt:unit": "unit:M3"
  },
  "speciesComposition": [{
    "@type": "biomass:SpeciesComponent",
    "species": "Pseudotsuga menziesii",
    "percentage": 75.0
  }],
  "harvestLocation": {
    "@type": "geo:Point",
    "geo:lat": 45.5231,
    "geo:long": -122.6765
  },
  "prov:wasGeneratedBy": {
    "@id": "https://example.org/harvest/HARV-2025-001"
  },
  "prov:wasAttributedTo": {
    "@id": "https://example.org/org/ORG-FOREST-001"
  }
}
</pre>

### Transaction with Linked Data ### {#linked-transaction}

Transaction linking multiple entities:

<pre class="json">
{
  "@context": "https://boost.org/context.jsonld",
  "@type": "schema:Order",
  "@id": "https://example.org/txn/TXN-2025-001",
  
  "transactionId": "TXN-2025-001",
  "schema:seller": {
    "@id": "https://example.org/org/ORG-SUPPLIER-001"
  },
  "schema:buyer": {
    "@id": "https://example.org/org/ORG-BUYER-001"
  },
  "schema:orderedItem": [{
    "@id": "https://example.org/tru/TRU-2025-001"
  }],
  "schema:price": {
    "@type": "schema:PriceSpecification",
    "schema:price": 85.50,
    "schema:priceCurrency": "USD"
  },
  "prov:startedAtTime": "2025-01-15T09:00:00Z",
  "prov:endedAtTime": "2025-01-15T14:30:00Z"
}
</pre>

## Advanced Features ## {#jsonld-advanced}

### Named Graphs ### {#named-graphs}

Support for multi-source data using named graphs:

<pre class="json">
{
  "@context": "https://boost.org/context.jsonld",
  "@graph": [{
    "@id": "https://example.org/graph/supplier",
    "@graph": [
      {
        "@type": "Organization",
        "organizationId": "ORG-001",
        "name": "Forest Products Inc"
      }
    ]
  }, {
    "@id": "https://example.org/graph/certification",
    "@graph": [
      {
        "@type": "Certificate",
        "certificateId": "CERT-FSC-001",
        "issuedTo": {"@id": "ORG-001"}
      }
    ]
  }]
}
</pre>

### Framing ### {#jsonld-framing}

JSON-LD framing for specific data views:

<pre class="json">
{
  "@context": "https://boost.org/context.jsonld",
  "@type": "TraceableUnit",
  "harvestedBy": {
    "@type": "Organization",
    "certifications": {
      "@type": "Certificate",
      "certificationType": "FSC"
    }
  }
}
</pre>

### Compaction and Expansion ### {#compaction-expansion}

BOOST supports JSON-LD algorithms:

- **Compaction**: Shortens IRIs using context
- **Expansion**: Expands to full IRIs
- **Flattening**: Creates flat graph structure
- **Normalization**: Canonical RDF representation

## Context Negotiation ## {#context-negotiation}

### Content Type Headers ### {#content-type-headers}

HTTP content negotiation support:

- `application/ld+json` - JSON-LD format
- `application/json` - Plain JSON (context link in header)
- `text/turtle` - RDF Turtle format
- `application/n-quads` - N-Quads format

### Profile Parameters ### {#profile-parameters}

Profile-based context selection:

```
Accept: application/ld+json; 
        profile="https://boost.org/profiles/extended"
```

## Implementation Guidance ## {#jsonld-implementation}

### Python Implementation ### {#python-jsonld}

Using PyLD library for JSON-LD processing:

```python
from pyld import jsonld
import json

# Load BOOST context
with open('boost_context.jsonld') as f:
    context = json.load(f)

# Create entity with context
tru = {
    "@context": context,
    "@type": "TraceableUnit",
    "traceableUnitId": "TRU-001",
    "totalVolume": 100.0
}

# Expand to full IRIs
expanded = jsonld.expand(tru)

# Compact with custom context
compacted = jsonld.compact(expanded, context)

# Convert to RDF
rdf = jsonld.to_rdf(tru)

# Frame for specific view
frame = {"@type": "TraceableUnit"}
framed = jsonld.frame(tru, frame)
```

### JavaScript Implementation ### {#javascript-jsonld}

Browser and Node.js support:

```javascript
const jsonld = require('jsonld');

// Process BOOST data
async function processBoostData(data) {
  // Add context
  data['@context'] = 'https://boost.org/context.jsonld';
  
  // Validate structure
  const expanded = await jsonld.expand(data);
  
  // Generate RDF
  const nquads = await jsonld.toRDF(data, {format: 'N-Quads'});
  
  return nquads;
}
```

## Semantic Validation ## {#semantic-validation}

### SHACL Constraints ### {#shacl-constraints}

Shape validation for semantic correctness:

<pre class="json">
{
  "@context": {"sh": "http://www.w3.org/ns/shacl#"},
  "@type": "sh:NodeShape",
  "sh:targetClass": "biomass:TraceableUnit",
  "sh:property": [{
    "sh:path": "biomass:totalVolume",
    "sh:datatype": "xsd:decimal",
    "sh:minInclusive": 0,
    "sh:maxInclusive": 10000
  }]
}
</pre>

### Reasoning and Inference ### {#reasoning-inference}

Automatic inference capabilities:

- Type inheritance from parent classes
- Property domain/range validation
- Transitive relationship discovery
- Consistency checking

## Benefits and Use Cases ## {#jsonld-benefits}

### Interoperability Benefits ### {#interoperability-benefits}

- **Global Identifiers**: IRIs enable worldwide unique identification
- **Vocabulary Reuse**: Leverage existing ontologies
- **Tool Ecosystem**: Compatible with RDF/SPARQL tools
- **Web Integration**: SEO and knowledge graph inclusion

### Supply Chain Use Cases ### {#supply-chain-use-cases}

- **Cross-Organization Linking**: Connect data across partners
- **Provenance Tracking**: Complete chain of custody
- **Regulatory Reporting**: Machine-readable compliance data
- **Certification Verification**: Linked certificate validation

The JSON-LD context provides BOOST with semantic web capabilities essential for modern supply chain interoperability and regulatory compliance.