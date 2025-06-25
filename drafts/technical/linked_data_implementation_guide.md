# BOOST Linked Data Implementation Guide

## Overview

This guide provides practical implementation patterns for integrating linked data capabilities into existing BOOST biomass supply chain systems. It covers the technical architecture, migration strategies, and operational considerations for adopting semantic web technologies while maintaining compatibility with existing relational database systems.

## Implementation Architecture

### Hybrid Approach: Relational + Semantic

The recommended architecture maintains existing relational databases as the primary operational store while adding a semantic layer for enhanced analytics and interoperability.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Application Layer                            │
├─────────────────────────┬───────────────────────────────────────┤
│   Traditional APIs      │         Semantic APIs                │
│   (REST/GraphQL)        │       (SPARQL/JSON-LD)               │
├─────────────────────────┼───────────────────────────────────────┤
│                         │                                       │
│  ┌─────────────────┐   │   ┌─────────────────┐                │
│  │ JSON Schema     │   │   │ JSON-LD Context │                │
│  │ Validation      │   │   │ Processing      │                │
│  └─────────────────┘   │   └─────────────────┘                │
│                         │                                       │
├─────────────────────────┼───────────────────────────────────────┤
│                         │                                       │
│  ┌─────────────────┐   │   ┌─────────────────┐                │
│  │  Relational DB  │◄──┼──►│   Triple Store  │                │
│  │ (PostgreSQL/    │   │   │ (Apache Jena/   │                │
│  │  MySQL)         │   │   │  Blazegraph)    │                │
│  └─────────────────┘   │   └─────────────────┘                │
│                         │                                       │
└─────────────────────────┴───────────────────────────────────────┘
           │                           │
           └───────────┬───────────────┘
                       │
           ┌─────────────────┐
           │  ETL Pipeline   │
           │  (Sync Layer)   │
           └─────────────────┘
```

### Data Flow Patterns

#### 1. Input Processing
```python
# Traditional JSON Input
{
  "organizationId": "ORG123",
  "name": "Biomass Corp",
  "role": "BP"
}

# Step 1: Add JSON-LD Context
{
  "@context": "https://boost.carbondirect.io/context.jsonld",
  "organizationId": "ORG123",
  "name": "Biomass Corp", 
  "role": "BP"
}

# Step 2: JSON-LD Expansion (automatic)
[
  {
    "@id": "boost:org/ORG123",
    "@type": ["https://boost.carbondirect.io/schema/Organization"],
    "https://schema.org/name": [{"@value": "Biomass Corp"}],
    "https://boost.carbondirect.io/schema/organizationRole": [{"@value": "BP"}]
  }
]

# Step 3: RDF Triples (for triple store)
<boost:org/ORG123> rdf:type boost:Organization .
<boost:org/ORG123> schema:name "Biomass Corp" .
<boost:org/ORG123> boost:organizationRole "BP" .
```

#### 2. Query Processing
```sql
-- Traditional SQL Query
SELECT o.name, c.certificateNumber 
FROM organizations o 
JOIN certificates c ON o.organizationId = c.organizationId
WHERE o.role = 'BP';
```

```sparql
-- Enhanced SPARQL Query
PREFIX boost: <https://boost.carbondirect.io/schema/>
PREFIX schema: <https://schema.org/>

SELECT ?name ?certNumber WHERE {
  ?org a boost:Organization ;
       schema:name ?name ;
       boost:organizationRole "BP" ;
       boost:has ?cert .
  ?cert boost:certificateNumber ?certNumber .
}
```

## Implementation Phases

### Phase 1: Foundation Setup (Weeks 1-4)

#### 1.1 Context Development
Create and deploy JSON-LD context files:

```bash
# Deploy context to web server
curl -X PUT https://boost.carbondirect.io/context.jsonld \
  -H "Content-Type: application/ld+json" \
  -d @boost_context.jsonld
```

#### 1.2 Validation Setup
```javascript
// JSON-LD validation middleware
const jsonld = require('jsonld');

async function validateJSONLD(data) {
  try {
    const expanded = await jsonld.expand(data);
    return { valid: true, expanded };
  } catch (error) {
    return { valid: false, error: error.message };
  }
}
```

#### 1.3 Triple Store Installation
```yaml
# docker-compose.yml for Apache Jena Fuseki
version: '3.8'
services:
  fuseki:
    image: secoresearch/fuseki
    ports:
      - "3030:3030"
    environment:
      - ADMIN_PASSWORD=boost_admin
    volumes:
      - fuseki_data:/fuseki
volumes:
  fuseki_data:
```

### Phase 2: Data Synchronization (Weeks 5-8)

#### 2.1 ETL Pipeline Development
```python
import json
import requests
from pyld import jsonld
from SPARQLWrapper import SPARQLWrapper, POST, JSON

class BOOSTETLPipeline:
    def __init__(self, db_conn, sparql_endpoint):
        self.db = db_conn
        self.sparql = SPARQLWrapper(sparql_endpoint)
        
    def sync_organization(self, org_id):
        # Fetch from relational DB
        org_data = self.fetch_organization(org_id)
        
        # Add JSON-LD context
        jsonld_data = {
            "@context": "https://boost.carbondirect.io/context.jsonld",
            **org_data
        }
        
        # Expand to RDF
        expanded = jsonld.expand(jsonld_data)
        
        # Convert to N-Triples
        ntriples = jsonld.to_rdf(jsonld_data, {'format': 'application/n-quads'})
        
        # Insert into triple store
        self.insert_triples(ntriples)
        
    def fetch_organization(self, org_id):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT organizationId, name, address, role, 
                   scopeOfOperations, legalEntityStatus
            FROM organizations 
            WHERE organizationId = %s
        """, (org_id,))
        
        columns = [desc[0] for desc in cursor.description]
        row = cursor.fetchone()
        return dict(zip(columns, row)) if row else None
        
    def insert_triples(self, ntriples):
        query = f"""
        INSERT DATA {{
            {ntriples}
        }}
        """
        self.sparql.setQuery(query)
        self.sparql.setMethod(POST)
        self.sparql.query()
```

#### 2.2 Incremental Sync Strategy
```python
# Database trigger for real-time sync
def create_sync_trigger():
    return """
    CREATE OR REPLACE FUNCTION sync_to_rdf()
    RETURNS trigger AS $$
    BEGIN
        -- Queue record for RDF sync
        INSERT INTO rdf_sync_queue (table_name, record_id, operation, timestamp)
        VALUES (TG_TABLE_NAME, NEW.id, TG_OP, NOW());
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    CREATE TRIGGER org_sync_trigger
        AFTER INSERT OR UPDATE OR DELETE ON organizations
        FOR EACH ROW EXECUTE FUNCTION sync_to_rdf();
    """
```

### Phase 3: API Enhancement (Weeks 9-12)

#### 3.1 JSON-LD Response Format
```javascript
// Express.js middleware for JSON-LD responses
app.use('/api/v2', (req, res, next) => {
  const originalSend = res.send;
  
  res.send = function(data) {
    if (req.headers.accept === 'application/ld+json') {
      // Add @context to response
      const jsonldData = {
        "@context": "https://boost.carbondirect.io/context.jsonld",
        ...JSON.parse(data)
      };
      return originalSend.call(this, JSON.stringify(jsonldData));
    }
    return originalSend.call(this, data);
  };
  
  next();
});
```

#### 3.2 SPARQL Endpoint
```javascript
// SPARQL query endpoint
app.post('/sparql', async (req, res) => {
  const { query } = req.body;
  
  try {
    const results = await executeSPARQLQuery(query);
    res.json(results);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

async function executeSPARQLQuery(query) {
  const response = await fetch('http://localhost:3030/boost/sparql', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/sparql-query',
      'Accept': 'application/sparql-results+json'
    },
    body: query
  });
  
  return response.json();
}
```

### Phase 4: Advanced Features (Weeks 13-16)

#### 4.1 Reasoning and Inference
```turtle
# BOOST inference rules (SHACL or SWRL)
@prefix boost: <https://boost.carbondirect.io/schema/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

boost:MaterialShape a sh:NodeShape ;
    sh:targetClass boost:Material ;
    sh:rule [
        a sh:SPARQLRule ;
        sh:construct """
            CONSTRUCT {
                ?this boost:requiresCertification true .
            }
            WHERE {
                ?this boost:materialType "Pellets" ;
                      boost:countryOfOrigin ?country .
                FILTER(?country IN ("US", "CA", "EU"))
            }
        """
    ] .
```

#### 4.2 Complex Analytics Queries
```sparql
# Supply chain carbon footprint analysis
PREFIX boost: <https://boost.carbondirect.io/schema/>
PREFIX schema: <https://schema.org/>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?materialType (AVG(?carbonValue) as ?avgCarbon) WHERE {
  ?material a boost:Material ;
            boost:materialType ?materialType ;
            boost:characterizedBy ?carbonData .
  
  ?carbonData boost:dataType "carbon_footprint" ;
              schema:value ?carbonValue .
              
  # Only include recent data
  ?carbonData prov:generatedAtTime ?time .
  FILTER(?time > "2024-01-01T00:00:00Z"^^xsd:dateTime)
} 
GROUP BY ?materialType
ORDER BY ?avgCarbon
```

## Integration Patterns

### Pattern 1: Gradual Migration
```javascript
// Version-aware API responses
app.get('/api/organizations/:id', async (req, res) => {
  const orgData = await getOrganization(req.params.id);
  
  switch(req.headers['api-version']) {
    case 'v1':
      res.json(orgData);
      break;
    case 'v2':
    default:
      res.json({
        "@context": "https://boost.carbondirect.io/context.jsonld",
        "@type": "Organization",
        ...orgData
      });
  }
});
```

### Pattern 2: Semantic Validation
```python
from pyshacl import validate

def validate_boost_data(data):
    # Load BOOST SHACL shapes
    shapes_graph = Graph().parse("boost_shapes.ttl")
    
    # Convert JSON-LD to RDF
    data_graph = Graph().parse(data=json.dumps(data), format='json-ld')
    
    # Validate
    conforms, results_graph, results_text = validate(
        data_graph, 
        shacl_graph=shapes_graph,
        inference='rdfs'
    )
    
    return {
        'valid': conforms,
        'violations': results_text if not conforms else None
    }
```

### Pattern 3: Cross-Reference Resolution
```sparql
# Resolve entity references across datasets
PREFIX boost: <https://boost.carbondirect.io/schema/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

CONSTRUCT {
  ?org boost:sameAs ?externalOrg .
}
WHERE {
  ?org a boost:Organization ;
       boost:globalLocationNumber ?gln .
       
  SERVICE <http://external-registry.example.org/sparql> {
    ?externalOrg gs1:globalLocationNumber ?gln .
  }
}
```

## Performance Optimization

### 1. Indexing Strategy
```sql
-- Triple store indexes for common query patterns
CREATE INDEX idx_subject_type ON triples (subject, predicate) 
WHERE predicate = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type';

CREATE INDEX idx_organization_role ON triples (subject, object)
WHERE predicate = 'https://boost.carbondirect.io/schema/organizationRole';
```

### 2. Caching Layer
```javascript
// Redis caching for frequent SPARQL queries
const redis = require('redis');
const client = redis.createClient();

async function cachedSPARQLQuery(query) {
  const cacheKey = `sparql:${crypto.createHash('md5').update(query).digest('hex')}`;
  
  // Check cache first
  const cached = await client.get(cacheKey);
  if (cached) return JSON.parse(cached);
  
  // Execute query
  const results = await executeSPARQLQuery(query);
  
  // Cache for 5 minutes
  await client.setex(cacheKey, 300, JSON.stringify(results));
  
  return results;
}
```

### 3. Query Optimization
```sparql
# Optimized query with LIMIT and OFFSET
PREFIX boost: <https://boost.carbondirect.io/schema/>

SELECT ?org ?name ?cert WHERE {
  ?org a boost:Organization ;
       schema:name ?name .
  
  OPTIONAL {
    ?org boost:has ?cert .
    ?cert boost:certificateStatus "Valid" .
  }
}
ORDER BY ?name
LIMIT 50 OFFSET 0
```

## Error Handling and Monitoring

### 1. Sync Error Recovery
```python
class SyncErrorHandler:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
        
    def handle_sync_error(self, record_id, error):
        retry_count = self.get_retry_count(record_id)
        
        if retry_count < self.max_retries:
            # Schedule retry with exponential backoff
            delay = 2 ** retry_count
            self.schedule_retry(record_id, delay)
        else:
            # Send to dead letter queue for manual review
            self.send_to_dlq(record_id, error)
            
    def schedule_retry(self, record_id, delay):
        # Use task queue (Celery, RQ, etc.)
        sync_task.apply_async(args=[record_id], countdown=delay)
```

### 2. Health Monitoring
```python
# Health check endpoints
@app.route('/health/semantic')
def semantic_health_check():
    checks = {
        'triple_store': check_triple_store_connection(),
        'context_availability': check_context_availability(),
        'sync_lag': check_sync_lag()
    }
    
    all_healthy = all(checks.values())
    status_code = 200 if all_healthy else 503
    
    return jsonify(checks), status_code

def check_sync_lag():
    # Check if sync is behind
    lag = get_sync_lag_minutes()
    return lag < 5  # Alert if more than 5 minutes behind
```

## Security Considerations

### 1. Access Control
```javascript
// SPARQL endpoint access control
app.use('/sparql', requireAuth, (req, res, next) => {
  const { query } = req.body;
  
  // Parse and validate SPARQL query
  if (containsUnsafeOperations(query)) {
    return res.status(403).json({ error: 'Query not allowed' });
  }
  
  // Add organization-specific filters
  const filteredQuery = addAccessFilters(query, req.user.organization);
  
  req.body.query = filteredQuery;
  next();
});
```

### 2. Data Privacy
```sparql
# Privacy-aware query filtering
PREFIX boost: <https://boost.carbondirect.io/schema/>

SELECT ?org ?publicInfo WHERE {
  ?org a boost:Organization ;
       boost:publiclyAvailable ?publicInfo .
  
  # Filter based on user permissions
  FILTER NOT EXISTS {
    ?org boost:restricted true .
    FILTER(?userOrg != ?org)  # Only show restricted data to owning org
  }
}
```

## Testing Strategy

### 1. Unit Tests
```python
import unittest
from boost_semantic import BOOSTSemanticProcessor

class TestSemanticProcessing(unittest.TestCase):
    def test_jsonld_expansion(self):
        input_data = {
            "@context": "https://boost.carbondirect.io/context.jsonld",
            "organizationId": "ORG123",
            "name": "Test Corp"
        }
        
        processor = BOOSTSemanticProcessor()
        result = processor.expand(input_data)
        
        self.assertIn("https://schema.org/name", str(result))
        self.assertEqual(result[0]["@id"], "boost:org/ORG123")
```

### 2. Integration Tests
```python
def test_end_to_end_sync():
    # Insert into relational DB
    org_id = insert_test_organization()
    
    # Wait for sync
    time.sleep(2)
    
    # Verify in triple store
    query = f"""
    ASK WHERE {{
        boost:org/{org_id} a boost:Organization .
    }}
    """
    
    result = execute_sparql_query(query)
    assert result['boolean'] == True
```

## Migration Checklist

### Pre-Migration
- [ ] Context files deployed and accessible
- [ ] Triple store configured and running
- [ ] ETL pipeline tested with sample data
- [ ] Backup procedures verified

### During Migration
- [ ] Enable sync for one entity type at a time
- [ ] Monitor sync lag and error rates
- [ ] Validate data consistency between stores
- [ ] Performance testing under load

### Post-Migration
- [ ] All entity types synchronized
- [ ] SPARQL endpoint accessible
- [ ] JSON-LD APIs responding correctly
- [ ] Monitoring and alerting configured

## Troubleshooting Guide

### Common Issues

#### 1. Context Loading Failures
```javascript
// Fallback context loading
async function loadContext(url) {
  try {
    return await fetch(url).then(r => r.json());
  } catch (error) {
    console.warn(`Failed to load context from ${url}, using local fallback`);
    return require('./fallback-context.json');
  }
}
```

#### 2. Sync Performance Issues
- Check triple store memory allocation
- Verify index coverage for common queries
- Monitor ETL pipeline queue depth
- Consider batch processing for large updates

#### 3. Query Timeout Issues
```sparql
# Add query hints for performance
PREFIX boost: <https://boost.carbondirect.io/schema/>

SELECT ?org ?name WHERE {
  ?org a boost:Organization .
  ?org schema:name ?name .
} 
# HINT: Consider adding LIMIT clause
LIMIT 1000
```

This implementation guide provides the technical foundation for successfully integrating linked data capabilities into BOOST systems while maintaining operational stability and performance.