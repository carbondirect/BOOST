<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: customer/validation_schema.json and customer_dictionary.md
     To modify this content, edit the source file and regenerate -->

Customer entity in BOOST data model

**[View Customer in ERD Navigator](erd-navigator/index.html?focus=Customer)**

### Relationships ### {{.unnumbered}}

- **GeographicDataId** → [[#geographic-data|Geographic Data]] - Customer location - uses EntityNameId convention referencing GeographicData

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
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>enum(Customer)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>customerId</code>
<td>string (pattern)
<td>Unique identifier for the customer
<td>✓
</tr>
<tr>
<td><code>customerName</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>GeographicDataId</code>
<td>string (pattern)
<td>Customer location - uses EntityNameId convention referencing GeographicData
<td>
</tr>
<tr>
<td><code>address</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## Customer
### Overview
The `Customer` entity represents buyer organizations in the BOOST traceability system. Customers are organizations that purchase biomass materials, wood products, or other materials tracked through the supply chain. This entity supports transaction management, delivery coordination, and supply chain relationship tracking by providing essential customer information and geographic location data.
### Fields
<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Required
<th>Description
<th>Examples
</tr>
</thead>
<tbody>
<tr>
<td>`customerId`
<td>string
<td>Yes
<td>Unique identifier for the customer (primary key)
<td>`CUST-001`, `CUST-PACIFIC-MILLS`
</tr>
<tr>
<td>`customerName`
<td>string
<td>Yes
<td>Legal name of the customer organization
<td>`Pacific Paper Mills LLC`, `Green Energy Corporation`
</tr>
<tr>
<td>`address`
<td>string
<td>No
<td>Physical address of the customer
<td>`123 Industrial Way, Portland, OR 97201`, `456 Mill Road, Sacramento, CA 95814`
</tr>
<tr>
<td>`GeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to customer's geographic location
<td>`GEO-CUSTOMER-PACIFIC-001`, `GEO-MILL-DELIVERY-SITE`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/customer/CUST-001`
</tr>
</tbody>
</table>
### Key Features
1. **Transaction Integration**
    - Direct integration with Transaction entities as buyers
    - Support for multiple concurrent transactions
    - Purchase order and contract management
    - Payment terms and financial relationship tracking
2. **Delivery Coordination**
    - Geographic location management for deliveries
    - Multiple delivery site support through GeographicData
    - Logistics and transportation coordination
    - Delivery documentation and tracking
3. **Supply Chain Relationships**
    - Multi-vendor relationship management
    - Supplier performance and quality tracking
    - Contract negotiation and management
    - Long-term partnership establishment
4. **Geographic Integration**
    - Precise location data for delivery planning
    - Multi-site customer management
    - Regional market analysis support
    - Transportation cost optimization
### Customer Categories
1. **Manufacturing Customers**
    - Paper mills and pulp facilities
    - Sawmills and lumber processors
    - Engineered wood product manufacturers
    - Furniture and construction companies
2. **Energy Customers**
    - Biomass power plants
    - Biorefinery facilities
    - Pellet manufacturing plants
    - Renewable energy producers
3. **Trading Organizations**
    - Commodity trading companies
    - Biomass brokers and distributors
    - Export/import organizations
    - Market intermediaries
4. **End-Use Industries**
    - Construction companies
    - Packaging manufacturers
    - Chemical industry consumers
    - Agricultural operations
### Example Use Cases
1. **Paper Mill Customer**
    - Customer: Large integrated paper manufacturing facility
    - Multiple delivery locations across processing facilities
    - Regular bulk purchases with long-term contracts
    - Quality specifications for fiber content and species
2. **Biomass Energy Customer**
    - Customer: Renewable energy power plant
    - Consistent fuel supply requirements
    - LCFS compliance and carbon intensity tracking
    - Seasonal demand variations and storage coordination
3. **Export Customer**
    - Customer: International trading organization
    - Port delivery locations with container coordination
    - Species-specific export requirements
    - Certification compliance for international markets
### Validation Rules
1. **Identity Requirements**
    - customerId must be unique across system
    - customerName must be non-empty string
    - customerId must follow pattern `^CUST-[A-Z0-9-_]+$`
2. **Geographic Consistency**
    - GeographicDataId must reference valid GeographicData entity
    - Address should be consistent with geographic location
    - Multiple delivery sites supported through GeographicData
3. **Transaction Integration**
    - Customer must be referenceable by Transaction entities
    - Customer information must be current for active transactions
    - Contact information must be maintained for business operations
### Relationships
- Customer purchases materials through Transaction entities
- Customer located at GeographicData delivery sites
- Customer receives TraceableUnits through supply chain operations
- Customer may have multiple delivery locations via GeographicData
- Customer integrated with SalesDeliveryDocument for delivery coordination
