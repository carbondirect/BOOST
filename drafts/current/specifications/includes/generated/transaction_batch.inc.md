<!-- Auto-generated from transaction_batch/validation_schema.json -->

TransactionBatch entity in BOOST data model

**🗂️ [View Transaction Batch in ERD Navigator](erd-navigator/index.html?focus=TransactionBatch)**

### Relationships ### {{.unnumbered}}

- **transactionBatchId** → [[#transaction-batch|Transaction Batch]] - Unique identifier for the physical material batch
- **transactionId** → [[#transaction|Transaction]] - Foreign key to parent business transaction
- **claimId** → [[#claim|Claim]] - Foreign key to primary sustainability claim

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
<td>enum(TransactionBatch)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>batchStatus</code>
<td>enum(6 values)
<td>Current status of the physical batch
<td>✓
</tr>
<tr>
<td><code>quantity</code>
<td>number (≥0)
<td>Physical quantity of material in this batch
<td>✓
</tr>
<tr>
<td><code>quantityUnit</code>
<td>enum(7 values)
<td>Unit of measurement for quantity
<td>✓
</tr>
<tr>
<td><code>traceableUnitIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of TRU IDs included in this batch
<td>✓
</tr>
<tr>
<td><code>transactionBatchId</code>
<td>string (pattern)
<td>Unique identifier for the physical material batch
<td>✓
</tr>
<tr>
<td><code>transactionId</code>
<td>string (pattern)
<td>Foreign key to parent business transaction
<td>✓
</tr>
<tr>
<td><code>additionalClaimIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of secondary claim IDs
<td>
</tr>
<tr>
<td><code>batchCreatedDate</code>
<td>string (date-time)
<td>When the batch was prepared/created
<td>
</tr>
<tr>
<td><code>certificationValidation</code>
<td>object (structured)
<td>Certification and compliance validation data
<td>
</tr>
<tr>
<td><code>claimId</code>
<td>string | null
<td>Foreign key to primary sustainability claim
<td>
</tr>
<tr>
<td><code>deliveryDate</code>
<td>string | null
<td>Actual delivery timestamp
<td>
</tr>
<tr>
<td><code>deliveryGeographicDataId</code>
<td>string | null
<td>Foreign key to delivery location
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of last modification
<td>
</tr>
<tr>
<td><code>measurementRecordIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of measurement record IDs
<td>
</tr>
<tr>
<td><code>mediaBreakDetected</code>
<td>boolean
<td>Flag indicating if traceability continuity was broken
<td>
</tr>
<tr>
<td><code>plantPartComposition</code>
<td>object (structured)
<td>Plant part composition breakdown
<td>
</tr>
<tr>
<td><code>processingHistoryIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of processing history record IDs
<td>
</tr>
<tr>
<td><code>productionBatchId</code>
<td>string | null
<td>Foreign key to source production batch
<td>
</tr>
<tr>
<td><code>qualityGrade</code>
<td>enum(9 values)
<td>Overall quality grade for the batch
<td>
</tr>
<tr>
<td><code>qualityMetrics</code>
<td>object (structured)
<td>Detailed quality assessment metrics
<td>
</tr>
<tr>
<td><code>reconciliationStatus</code>
<td>enum(5 values)
<td>Status of volume/quality reconciliation
<td>
</tr>
<tr>
<td><code>speciesComposition</code>
<td>array&amp;lt;object&amp;gt;
<td>Species breakdown with percentages
<td>
</tr>
<tr>
<td><code>trackingHistory</code>
<td>string
<td>Complete location trail summary
<td>
</tr>
<tr>
<td><code>transportationData</code>
<td>object (structured)
<td>Transportation and logistics information
<td>
</tr>
</tbody>
</table>

## TransactionBatch
### Overview
The `TransactionBatch` entity manages physical material batches within business transactions in the BOOST traceability system. Transaction batches represent specific, physically aggregated quantities of materials that are prepared, transported, and delivered as cohesive units within larger commercial transactions. This entity provides detailed tracking of material composition, quality characteristics, transportation logistics, certification validation, and complete traceability across the physical supply chain from preparation through final delivery.
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
<td>`transactionBatchId`
<td>string
<td>Yes
<td>Unique identifier for the physical material batch (primary key)
<td>`TB-001`, `TB-PACIFIC-2024-SHIPMENT-001`
</tr>
<tr>
<td>`transactionId`
<td>string (FK)
<td>Yes
<td>Foreign key to parent business transaction
<td>`TXN-PACIFIC-2024-001`, `TXN-BIOMASS-EXPORT-789`
</tr>
<tr>
<td>`productionBatchId`
<td>string (FK)
<td>No
<td>Foreign key to source production batch
<td>`PB-MILL-2024-Q1-001`, `PB-HARVEST-SPRING-123`
</tr>
<tr>
<td>`quantity`
<td>number
<td>Yes
<td>Physical quantity of material in this batch
<td>`1250.5`, `25000.0`, `500.75`
</tr>
<tr>
<td>`quantityUnit`
<td>string
<td>Yes
<td>Unit of measurement for quantity (enum)
<td>`cubic_meters`, `metric_tons`, `board_feet`, `cord`, `green_tons`
</tr>
<tr>
<td>`traceableUnitIds`
<td>array&lt;string&gt;
<td>Yes
<td>Array of TRU IDs included in this batch
<td>`["TRU-LOG-001", "TRU-PILE-002", "TRU-BATCH-003"]`
</tr>
<tr>
<td>`claimId`
<td>string (FK)
<td>No
<td>Foreign key to primary sustainability claim
<td>`CLAIM-FSC-MIX-75`, `CLAIM-SBP-COMPLIANT`
</tr>
<tr>
<td>`additionalClaimIds`
<td>array&lt;string&gt;
<td>No
<td>Array of secondary claim IDs
<td>`["CLAIM-PEFC-CERTIFIED", "CLAIM-SFI-SOURCING"]`
</tr>
<tr>
<td>`speciesComposition`
<td>array&lt;object&gt;
<td>No
<td>Species breakdown with percentages and volumes
<td>`[{"species": "Douglas Fir", "percentage": 65.0, "volume": 812.8}, {"species": "Hemlock", "percentage": 35.0, "volume": 437.7}]`
</tr>
<tr>
<td>`qualityGrade`
<td>string
<td>No
<td>Overall quality grade for the batch (enum)
<td>`Grade_A`, `Structural`, `Sawlog`, `Fuel`, `Mixed`
</tr>
<tr>
<td>`processingHistoryIds`
<td>array&lt;string&gt;
<td>No
<td>Array of processing history record IDs
<td>`["PH-SAWMILL-001", "PH-PLANER-002", "PH-KILN-003"]`
</tr>
<tr>
<td>`reconciliationStatus`
<td>string
<td>No
<td>Status of volume/quality reconciliation (enum)
<td>`pending`, `in_progress`, `resolved`, `disputed`, `escalated`
</tr>
<tr>
<td>`trackingHistory`
<td>string
<td>No
<td>Complete location trail summary
<td>`Harvest Site A → Skid Road 101 → Forest Road Main → Mill Yard → Loading Dock`
</tr>
<tr>
<td>`measurementRecordIds`
<td>array&lt;string&gt;
<td>No
<td>Array of measurement record IDs
<td>`["MR-SCALE-001", "MR-MOISTURE-002", "MR-GRADE-003"]`
</tr>
<tr>
<td>`mediaBreakDetected`
<td>boolean
<td>No
<td>Flag indicating if traceability continuity was broken
<td>`false`, `true`
</tr>
<tr>
<td>`batchStatus`
<td>string
<td>Yes
<td>Current status of the physical batch (enum)
<td>`prepared`, `in_transit`, `delivered`, `accepted`, `rejected`
</tr>
<tr>
<td>`batchCreatedDate`
<td>string (datetime)
<td>No
<td>When the batch was prepared/created
<td>`2024-03-15T08:30:00Z`, `2024-07-22T14:45:00Z`
</tr>
<tr>
<td>`deliveryDate`
<td>string (datetime)
<td>No
<td>Actual delivery timestamp
<td>`2024-03-18T11:15:00Z`, `2024-07-25T09:30:00Z`
</tr>
<tr>
<td>`deliveryGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to delivery location
<td>`GEO-MILL-ENTRANCE-001`, `GEO-PORT-TERMINAL-EAST`
</tr>
<tr>
<td>`qualityMetrics`
<td>object
<td>No
<td>Detailed quality assessment metrics
<td>`{"moistureContent": 12.5, "density": 450.0, "defectRate": 2.1, "contaminationLevel": "minimal"}`
</tr>
<tr>
<td>`plantPartComposition`
<td>object
<td>No
<td>Plant part composition breakdown
<td>`{"trunk": {"volume": 1000.0, "percentage": 85.0}, "branches": {"volume": 150.0, "percentage": 12.0}}`
</tr>
<tr>
<td>`transportationData`
<td>object
<td>No
<td>Transportation and logistics information
<td>`{"carrierOrganizationId": "CARRIER-001", "transportMethod": "truck", "vehicleId": "TRUCK-789"}`
</tr>
<tr>
<td>`certificationValidation`
<td>object
<td>No
<td>Certification and compliance validation data
<td>`{"certificateIds": ["CERT-FSC-001"], "validationRequired": true, "validationCompleted": true}`
</tr>
<tr>
<td>`lastUpdated`
<td>string (datetime)
<td>No
<td>Timestamp of last modification
<td>`2024-03-20T16:45:00Z`, `2024-07-28T10:30:00Z`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/transaction-batch/TB-001`
</tr>
</tbody>
</table>
### Batch Status Workflow
1. **prepared**
    - Batch assembled and ready for shipment
    - Quality assessment completed and documented
    - All TRUs allocated and consolidated
    - Transportation arrangements finalized
2. **in_transit**
    - Batch loaded and en route to destination
    - Transportation tracking active
    - Chain of custody maintained during transport
    - Estimated arrival time being monitored
3. **delivered**
    - Physical arrival at destination location
    - Delivery documentation completed
    - Initial receipt confirmation obtained
    - Awaiting quality inspection and acceptance
4. **accepted**
    - Quality inspection completed successfully
    - Batch accepted by receiving party
    - Final documentation and certificates validated
    - Batch integration into recipient's inventory
5. **rejected**
    - Quality inspection failed or non-conforming
    - Batch refused by receiving party
    - Return logistics or rework arrangements required
    - Documentation updated with rejection reasons
6. **partially_delivered**
    - Partial delivery due to transportation constraints
    - Remaining materials scheduled for follow-up delivery
    - Partial acceptance and payment processing
    - Split batch tracking and reconciliation
### Quality Metrics Components
1. **Physical Properties**
    - **moistureContent**: Moisture percentage (0-100%)
    - **density**: Material density in kg/m³
    - **defectRate**: Percentage of defective material (0-100%)
    - **contaminationLevel**: Contamination assessment (none, minimal, moderate, significant, unacceptable)
2. **Assessment Methods**
    - **gradingMethod**: Grading technique (visual, mechanical, optical, combination)
    - **qualityAssessmentDate**: When assessment was performed
    - **assessorId**: Qualified assessor identification
    - **gradingStandards**: Applicable quality standards and specifications
3. **Performance Indicators**
    - Conformance to customer specifications
    - Market grade equivalency and value
    - Processing suitability and efficiency
    - End-use application compatibility
### Plant Part Composition Structure
1. **Wood Components**
    - **trunk**: Main stem portion with volume and percentage
    - **branches**: Branch material inclusion
    - **bark**: Bark content and separation
    - **heartwood/sapwood**: Wood type differentiation
2. **Biomass Components**
    - **leaves/needles**: Foliage content for energy applications
    - **twigs**: Small branch and twig material
    - **seeds/nuts/cones**: Reproductive material content
    - **stalks/straw**: Agricultural residue components
3. **Processing Residues**
    - **husks/hulls**: Processing by-product inclusion
    - **chaff**: Fine material and particle content
    - **stubble**: Field residue components
    - **sawdust**: Mill residue integration
### Transportation Data Management
1. **Carrier Information**
    - **carrierOrganizationId**: Transportation company identification
    - **vehicleId**: Specific vehicle or container identification
    - **driverOperatorId**: Personnel responsible for transport
    - **transportMethod**: Mode of transportation (truck, rail, ship, barge)
2. **Logistics Coordination**
    - **pickupDate**: Scheduled and actual pickup times
    - **estimatedArrival**: Projected delivery schedule
    - **routeOptimization**: Route selection criteria and efficiency
    - **transitTime**: Duration and schedule performance
3. **Transportation Compliance**
    - Weight and dimension regulations
    - Hazardous materials handling requirements
    - International shipping documentation
    - Insurance and liability coverage
### Certification Validation Process
1. **Certificate Verification**
    - **certificateIds**: Applicable certification references
    - **validationRequired**: Compliance verification necessity
    - **validationCompleted**: Verification completion status
    - **validationDate**: When verification was performed
2. **Compliance Assessment**
    - **validatorId**: Qualified validator identification
    - **validationNotes**: Detailed verification findings
    - Chain of custody validation
    - Sustainability claim verification
3. **Documentation Management**
    - Certificate authenticity verification
    - Expiration date and renewal tracking
    - Audit trail maintenance
    - Third-party verification coordination
### Reconciliation Status Management
1. **pending**
    - Initial batch creation with preliminary measurements
    - Awaiting final quality assessment and validation
    - Documentation compilation in progress
    - Quantity and quality verification pending
2. **in_progress**
    - Active reconciliation process underway
    - Measurements being verified and cross-checked
    - Quality assessments being completed
    - Documentation review and validation ongoing
3. **resolved**
    - All measurements and quality assessments completed
    - Documentation validated and approved
    - Quantity and quality reconciliation successful
    - Batch ready for final delivery and acceptance
4. **disputed**
    - Measurement or quality discrepancies identified
    - Customer or supplier disagreement on specifications
    - Resolution process initiated with stakeholders
    - Additional verification or rework may be required
5. **escalated**
    - Dispute resolution unsuccessful at operational level
    - Management or legal intervention required
    - Third-party arbitration or mediation initiated
    - Contract terms and penalties under review
### Traceability Integration
1. **TRU Aggregation**
    - Complete tracking of all constituent TRUs
    - Maintenance of individual TRU identity within batch
    - Species composition aggregation and validation
    - Processing history consolidation across TRUs
2. **Chain of Custody Maintenance**
    - Unbroken traceability from source to delivery
    - Documentation of all custody transfers
    - Geographic tracking and location verification
    - Media break detection and remediation
3. **Processing History Integration**
    - Consolidation of processing records across TRUs
    - Value-added processing documentation
    - Quality transformation tracking
    - Certification maintenance through processing
### Example Use Cases
1. **Lumber Export Shipment**
    - Transaction Batch: Container load of FSC-certified Douglas Fir lumber
    - Quantity: 45 cubic meters of Grade A structural lumber
    - Composition: 100% Douglas Fir from certified forest management unit
    - Quality: Kiln-dried to 12% moisture, mechanically graded
    - Transportation: Truck transport to port, container loading
    - Certification: FSC Chain of Custody validation completed
2. **Biomass Fuel Delivery**
    - Transaction Batch: Truck load of SBP-compliant wood chips
    - Quantity: 25 metric tons green weight biomass fuel
    - Composition: Mixed species (60% hardwood, 40% softwood)
    - Quality: <50% moisture content, minimal contamination
    - Transportation: Direct delivery from processing facility
    - Certification: SBP sustainability verification completed
3. **Multi-Species Log Load**
    - Transaction Batch: Logging truck load from selective harvest
    - Quantity: 40 cubic meters mixed species sawlogs
    - Composition: Douglas Fir (50%), Hemlock (30%), Cedar (20%)
    - Quality: Grade B sawlogs with visual grading assessment
    - Transportation: Forest road to mill yard delivery
    - Certification: Multiple certificate validation for species mix
### Validation Rules
1. **Batch Requirements**
    - transactionBatchId must be unique across system
    - transactionId must reference valid Transaction entity
    - quantity must be positive number greater than zero
    - quantityUnit must be appropriate for material type
2. **TRU Integration**
    - traceableUnitIds must reference valid existing TRUs
    - All TRUs must be available for batch allocation
    - TRU species composition must align with batch species data
    - TRU processing history must be consistent with batch claims
3. **Quality Consistency**
    - qualityGrade must align with quality metrics assessment
    - Species composition percentages must sum to 100%
    - Plant part composition percentages must sum to 100%
    - Quality assessment date must be within reasonable timeframe
4. **Transportation Validation**
    - carrierOrganizationId must reference valid Organization
    - Transport method must be appropriate for material type
    - Pickup and delivery dates must be logically sequenced
    - Route optimization must align with transportation method
5. **Certification Compliance**
    - Certificate IDs must reference valid active certificates
    - Validation requirements must be met before delivery
    - Certification scope must cover all materials in batch
    - Validator must be qualified for certification scheme
### Relationships
- TransactionBatch part of one Transaction for commercial context
- TransactionBatch contains multiple TraceableUnits for material composition
- TransactionBatch delivered to one GeographicData location for logistics
- TransactionBatch validated through multiple Certificate references for compliance
- TransactionBatch measured through multiple MeasurementRecord entries for quality assurance
- TransactionBatch processed through ProcessingHistory records for transformation tracking
- TransactionBatch reconciled through DataReconciliation processes for accuracy verification
