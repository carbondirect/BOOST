<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: sales_delivery_document/validation_schema.json and sales_delivery_document_dictionary.md
     To modify this content, edit the source file and regenerate -->

SalesDeliveryDocument entity in BOOST data model

**[View Sales Delivery Document in ERD Navigator](erd-navigator/index.html?focus=SalesDeliveryDocument)**

### Relationships ### {{.unnumbered}}

- **transactionId** → [[#transaction|Transaction]]

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
<td>enum(SalesDeliveryDocument)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>buyerName</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>dateIssued</code>
<td>string (date)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>documentId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>productDescription</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>quantity</code>
<td>number
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>sellerName</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>buyerAddress</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>certificateCode</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>sellerAddress</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>transactionId</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>transportReference</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## SalesDeliveryDocument
### Overview
The `SalesDeliveryDocument` entity manages sales and delivery documentation for business transactions within the BOOST traceability system. These documents serve as formal records of material transfers, providing essential transaction details, party information, and product specifications. This entity supports transaction documentation, delivery verification, and compliance record-keeping for supply chain operations.
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
<td>`documentId`
<td>string
<td>Yes
<td>Unique identifier for the sales delivery document (primary key)
<td>`SDD-001`, `SDD-PACIFIC-DELIVERY-2024-001`
</tr>
<tr>
<td>`dateIssued`
<td>string (date)
<td>Yes
<td>Date when the document was issued
<td>`2024-03-15`, `2024-07-22`
</tr>
<tr>
<td>`buyerName`
<td>string
<td>Yes
<td>Name of the purchasing organization
<td>`Pacific Paper Mills LLC`, `Green Energy Corporation`
</tr>
<tr>
<td>`buyerAddress`
<td>string
<td>No
<td>Address of the purchasing organization
<td>`123 Industrial Way, Portland, OR 97201`, `456 Mill Road, Sacramento, CA 95814`
</tr>
<tr>
<td>`sellerName`
<td>string
<td>Yes
<td>Name of the selling organization
<td>`Klamath Forest Products`, `Pacific Timber Harvesters LLC`
</tr>
<tr>
<td>`sellerAddress`
<td>string
<td>No
<td>Address of the selling organization
<td>`789 Forest Road, Klamath Falls, OR 97601`, `321 Logging Way, Eureka, CA 95501`
</tr>
<tr>
<td>`productDescription`
<td>string
<td>Yes
<td>Detailed description of the products being delivered
<td>`Douglas Fir sawlogs, Grade A, 24-foot lengths`, `Mixed hardwood chips, moisture content 15%`
</tr>
<tr>
<td>`quantity`
<td>number
<td>Yes
<td>Quantity of product being delivered
<td>`125.5`, `2500.0`, `1850.75`
</tr>
<tr>
<td>`transactionId`
<td>string (FK)
<td>No
<td>Foreign key reference to associated transaction
<td>`TXN-PACIFIC-2024-001`, `TXN-BIOMASS-DELIVERY-789`
</tr>
<tr>
<td>`certificateCode`
<td>string
<td>No
<td>Certification code applicable to the delivered products
<td>`FSC-C123456`, `SFI-SFIS-COC-123456`, `SBP-DTS-001`
</tr>
<tr>
<td>`transportReference`
<td>string
<td>No
<td>Transportation reference or tracking number
<td>`TRUCK-001-20240315`, `RAIL-CAR-ABC123`, `CONTAINER-HLXU1234567`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/sales-delivery-document/SDD-001`
</tr>
</tbody>
</table>
### Document Types
1. **Sales Invoice**
    - Primary commercial document for completed transactions
    - Includes pricing, payment terms, and financial details
    - Legal document for accounting and tax purposes
    - Links to purchase orders and delivery confirmations
2. **Delivery Receipt**
    - Proof of material delivery and acceptance
    - Includes quantity verification and quality confirmation
    - Signed acknowledgment by receiving party
    - Critical for chain of custody documentation
3. **Bill of Lading**
    - Transportation document for shipped materials
    - Includes carrier information and transportation details
    - Legal document for cargo responsibility transfer
    - Required for interstate and international shipments
4. **Packing List**
    - Detailed inventory of shipped materials
    - Includes individual TRU references and specifications
    - Quality grades, species composition, and certifications
    - Support document for delivery verification
### Key Features
1. **Transaction Documentation**
    - Complete transaction record keeping
    - Buyer and seller information management
    - Product specification and quantity tracking
    - Payment and delivery term documentation
2. **Certification Integration**
    - Certificate code tracking and validation
    - Chain of custody documentation support
    - Sustainability claim transfer documentation
    - Third-party certification compliance
3. **Transportation Coordination**
    - Transport reference and tracking integration
    - Delivery scheduling and coordination support
    - Multi-modal transportation documentation
    - Logistics and routing optimization
4. **Compliance Support**
    - Regulatory documentation requirements
    - Audit trail and record keeping
    - Tax and customs documentation support
    - Legal document archival and retrieval
### Product Description Guidelines
1. **Species Information**
    - Common and scientific species names
    - Species composition percentages for mixed materials
    - Grade classifications and quality specifications
    - Processing stage and product form
2. **Quantity Specifications**
    - Volume measurements in cubic meters
    - Weight measurements in metric tons
    - Piece counts for individual logs or products
    - Unit conversion factors and calculations
3. **Quality Parameters**
    - Moisture content percentages
    - Grade classifications (A, B, C, etc.)
    - Defect descriptions and tolerances
    - Processing specifications and requirements
4. **Certification Status**
    - Applicable certification schemes
    - Percentage-based claims (FSC Mix 70%)
    - Certificate numbers and validity periods
    - Chain of custody claim statements
### Example Use Cases
1. **Sawlog Delivery Documentation**
    - Document Type: Bill of Lading + Delivery Receipt
    - Product: Douglas Fir and Hemlock sawlogs
    - Quantity: 125.5 cubic meters
    - Certification: FSC Mix 75% with certificate FSC-C123456
    - Transportation: Logging truck with GPS tracking
2. **Biomass Fuel Delivery**
    - Document Type: Sales Invoice + Packing List
    - Product: Wood chips for biomass power plant
    - Quantity: 2,500 metric tons (dry weight basis)
    - Certification: SBP-compliant biomass
    - Transportation: Rail car shipment with moisture monitoring
3. **Export Documentation**
    - Document Type: Commercial Invoice + Export Certificate
    - Product: Lumber products for international export
    - Quantity: Container load with detailed inventory
    - Certification: PEFC certified with phytosanitary certificate
    - Transportation: Container shipping with customs documentation
### Validation Rules
1. **Document Requirements**
    - documentId must be unique across system
    - dateIssued must be valid date format
    - buyerName and sellerName must be non-empty
    - productDescription must provide adequate detail
    - quantity must be positive number
2. **Transaction Integration**
    - transactionId must reference valid Transaction if provided
    - Document details must be consistent with transaction terms
    - Delivery dates must align with transaction timeline
    - Parties must match transaction buyer and seller
3. **Certification Consistency**
    - certificateCode must be valid format if provided
    - Certificate must be active and applicable to products
    - Chain of custody claims must be supported by documentation
    - Certification scope must cover described products
### Relationships
- SalesDeliveryDocument documents one Transaction
- SalesDeliveryDocument references Certificate through certificateCode
- SalesDeliveryDocument includes TraceableUnits through transaction linkage
- SalesDeliveryDocument supports transportation coordination
- SalesDeliveryDocument enables compliance documentation and audit trails
