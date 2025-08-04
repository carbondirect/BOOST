# Supplier

## Supplier

### Overview
The `Supplier` entity represents organizations that provide biomass materials, wood products, and related materials in the BOOST traceability system. Suppliers are critical supply chain participants who harvest, process, or distribute materials to other organizations. This entity supports certification management, claim tracking, and supply chain relationship coordination with comprehensive supplier information and capability tracking.

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
<td>`supplierId`
<td>string
<td>Yes
<td>Unique identifier for the supplier (primary key)
<td>`SUPP-001`, `SUPP-KLAMATH-FOREST-CO`
</tr>
<tr>
<td>`supplierName`
<td>string
<td>Yes
<td>Legal name of the supplier organization
<td>`Klamath Forest Products`, `Pacific Timber Harvesters LLC`
</tr>
<tr>
<td>`address`
<td>string
<td>No
<td>Physical address of the supplier
<td>`789 Forest Road, Klamath Falls, OR 97601`, `321 Logging Way, Eureka, CA 95501`
</tr>
<tr>
<td>`certificateCode`
<td>string
<td>No
<td>Primary certification code for the supplier
<td>`FSC-C123456`, `SFI-SFIS-COC-123456`, `PEFC/05-33-123`
</tr>
<tr>
<td>`claim`
<td>string
<td>No
<td>Primary sustainability claim offered by supplier
<td>`FSC Mix 70%`, `SBP-compliant biomass`, `PEFC Certified`
</tr>
<tr>
<td>`supplierType`
<td>string
<td>No
<td>Classification of supplier operations
<td>`harvester`, `processor`, `trader`, `integrated`, `contractor`
</tr>
<tr>
<td>`GeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to supplier's geographic location
<td>`GEO-SUPPLIER-KLAMATH-001`, `GEO-HARVEST-BASE-PACIFIC`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/supplier/SUPP-001`
</tr>
</tbody>
</table>

### Supplier Types

1. **harvester**
    - Forest harvesting and timber extraction operations
    - Primary material production from standing forests
    - Logging contractors and forest management companies
    - Initial TRU creation and biometric identification

2. **processor**
    - Manufacturing and material transformation operations
    - Sawmills, pulp mills, and processing facilities
    - Value-added processing and product manufacturing
    - TRU transformation and split/merge operations

3. **trader**
    - Material trading and distribution organizations
    - Commodity brokers and market intermediaries
    - Import/export operations and logistics coordination
    - Supply chain optimization and market access

4. **integrated**
    - Vertically integrated operations across multiple stages
    - Combined harvesting, processing, and distribution
    - End-to-end supply chain management
    - Complex organizational structures with multiple facilities

5. **contractor**
    - Service providers and specialized contractors
    - Equipment operation and maintenance services
    - Specialized processing or transportation services
    - Support services for primary operations

### Key Features

1. **Certification Management**
    - Primary certification tracking and validation
    - Multiple certification scheme support
    - Certificate expiry monitoring and renewal tracking
    - Audit and compliance history management

2. **Claim Verification**
    - Sustainability claim documentation and validation
    - Species-specific claim management
    - Chain of custody claim inheritance
    - Third-party verification support

3. **Supply Chain Integration**
    - Multi-customer relationship management
    - Transaction history and performance tracking
    - Quality specifications and delivery capabilities
    - Long-term contract and partnership management

4. **Geographic Operations**
    - Primary operation location management
    - Multi-site operational capability tracking
    - Regional market coverage and access
    - Transportation and logistics coordination

### Certification Examples

1. **Forest Stewardship Council (FSC)**
    - Certificate Code: `FSC-C123456`
    - Claims: `FSC 100%`, `FSC Mix 70%`, `FSC Recycled`
    - Chain of custody and forest management certifications
    - Species-specific and percentage-based claims

2. **Sustainable Forestry Initiative (SFI)**
    - Certificate Code: `SFI-SFIS-COC-123456`
    - Claims: `SFI Certified Sourcing`, `SFI Chain of Custody`
    - Fiber sourcing and chain of custody standards
    - Regional sustainable forestry practices

3. **Programme for the Endorsement of Forest Certification (PEFC)**
    - Certificate Code: `PEFC/05-33-123`
    - Claims: `PEFC Certified`, `PEFC Controlled Sources`
    - International mutual recognition system
    - National scheme integration and compliance

### Example Use Cases

1. **Integrated Forest Products Supplier**
    - Supplier Type: integrated
    - Operations: Combined harvesting and processing
    - Certifications: FSC Forest Management + Chain of Custody
    - Claims: FSC Mix 85% for both harvested and processed materials
    - Geographic coverage: Multiple forest areas and processing facilities

2. **Specialized Biomass Harvester**
    - Supplier Type: harvester
    - Operations: Forest residue collection and preparation
    - Certifications: SBP Data Transfer System registration
    - Claims: SBP-compliant biomass from sustainably managed forests
    - Focus: Biomass fuel supply for renewable energy markets

3. **Regional Timber Trader**
    - Supplier Type: trader
    - Operations: Regional timber marketing and distribution
    - Certifications: FSC Chain of Custody for trading
    - Claims: Variable based on source suppliers
    - Services: Market access and logistics coordination for small suppliers

### Validation Rules

1. **Identity Requirements**
    - supplierId must be unique across system
    - supplierName must be non-empty string
    - supplierId must follow established pattern conventions

2. **Certification Consistency**
    - certificateCode must be valid format for certification scheme
    - claim must be consistent with certificate authority and scope
    - Certification expiry dates must be monitored and maintained

3. **Operational Validity**
    - supplierType must align with actual operational capabilities
    - Geographic location must be consistent with service areas
    - Claims must be supported by valid certification documentation

### Relationships
- Supplier provides materials to Customer entities through Transactions
- Supplier operates from GeographicData locations
- Supplier creates and manages TraceableUnits in supply chain
- Supplier holds Certificates supporting sustainability claims
- Supplier may operate multiple SupplyBase areas for material sourcing