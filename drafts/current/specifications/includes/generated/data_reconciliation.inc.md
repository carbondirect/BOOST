<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: data_reconciliation/validation_schema.json and data_reconciliation_dictionary.md
     To modify this content, edit the source file and regenerate -->

DataReconciliation entity in BOOST data model

**[View Data Reconciliation in ERD Navigator](erd-navigator/index.html?focus=DataReconciliation)**

### Relationships ### {{.unnumbered}}

- **traceableUnitId** → [[#traceable-unit|Traceable Unit]]
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
<td>enum(DataReconciliation)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>discrepancy</code>
<td>number
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>forestMeasurement</code>
<td>number (≥0)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>millMeasurement</code>
<td>number (≥0)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>reconciliationDate</code>
<td>string (date-time)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>reconciliationId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>reconciliationStatus</code>
<td>enum(pending, resolved, disputed)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>traceableUnitId</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>discrepancyReason</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>No description provided
<td>
</tr>
<tr>
<td><code>reconciliationOperator</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>resolutionNotes</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>speciesDiscrepancies</code>
<td>array&amp;lt;string&amp;gt;
<td>No description provided
<td>
</tr>
<tr>
<td><code>tolerancePercentage</code>
<td>number (≥0, ≤100)
<td>No description provided
<td>
</tr>
<tr>
<td><code>transactionId</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## DataReconciliation
### Overview
The `DataReconciliation` entity reconciles measurements between forest and mill with TRU references and species-specific discrepancies to ensure data accuracy and prevent media breaks. This entity enables automated comparison of harvest measurements with mill scale measurements, identifies discrepancies, and tracks resolution status as required by the BOOST traceability system for measurement validation.
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
<td>`reconciliationId`
<td>string
<td>Yes
<td>Unique identifier for the reconciliation record (primary key)
<td>`DR-001`, `DR-KLA-042-RECON-001`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU being reconciled
<td>`TRU-PILE-CA-Klamath-042`
</tr>
<tr>
<td>`transactionId`
<td>string (FK)
<td>No
<td>Foreign key to associated transaction
<td>`TXN-PACIFIC-MILL-001`
</tr>
<tr>
<td>`forestMeasurement`
<td>number
<td>Yes
<td>Measurement taken in forest (cubic meters)
<td>`85.25`, `120.50`, `45.75`
</tr>
<tr>
<td>`millMeasurement`
<td>number
<td>Yes
<td>Measurement taken at mill (cubic meters)
<td>`84.75`, `119.25`, `46.10`
</tr>
<tr>
<td>`discrepancy`
<td>number
<td>Yes
<td>Difference between measurements (forest - mill)
<td>`0.50`, `-1.25`, `0.35`
</tr>
<tr>
<td>`reconciliationStatus`
<td>string
<td>Yes
<td>Current status of reconciliation (enum)
<td>`pending`, `resolved`, `disputed`
</tr>
<tr>
<td>`discrepancyReason`
<td>string
<td>No
<td>Reason for discrepancy
<td>`Natural moisture loss`, `Scale calibration error`, `Bark loss`
</tr>
<tr>
<td>`reconciliationDate`
<td>string (date-time)
<td>Yes
<td>When reconciliation was performed
<td>`2025-07-21T15:00:00Z`
</tr>
<tr>
<td>`reconciliationOperator`
<td>string
<td>No
<td>Operator who performed reconciliation
<td>`OP-QUALITY-TECH-001`, `OP-SCALE-MANAGER-02`
</tr>
<tr>
<td>`speciesDiscrepancies`
<td>array&lt;string&gt;
<td>No
<td>Per-species discrepancies for multi-species TRUs
<td>`["Douglas Fir: +0.25m3", "Pine: -0.15m3"]`
</tr>
<tr>
<td>`tolerancePercentage`
<td>number
<td>No
<td>Acceptable tolerance percentage (0-100)
<td>`2.5`, `5.0`, `1.0`
</tr>
<tr>
<td>`resolutionNotes`
<td>string
<td>No
<td>Notes on how discrepancy was resolved
<td>`Accepted within tolerance`, `Remeasurement confirmed mill scale`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/data-reconciliation/DR-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-21T15:30:00Z`
</tr>
</tbody>
</table>
### Reconciliation Status Values
1. **pending**
     Reconciliation process initiated but not completed
     Measurements compared, discrepancy calculated
     Awaiting review or resolution action
     Default status for new reconciliation records
2. **resolved**
     Discrepancy has been addressed and accepted
     Resolution notes document how discrepancy was handled
     TRU can proceed in transaction processing
     Final status for acceptable discrepancies
3. **disputed**
     Discrepancy exceeds acceptable tolerance
     Requires investigation or remeasurement
     TRU processing may be held pending resolution
     Escalation to quality assurance team
### Key Features
1. **Automated Comparison**
     Systematic comparison of forest vs mill measurements
     Automatic discrepancy calculation
     Tolerance-based status assignment
     Species-level discrepancy tracking
2. **Quality Assurance**
     Tolerance percentage enforcement
     Discrepancy reason categorization
     Resolution process documentation
     Audit trail for measurement validation
3. **Species-Specific Tracking**
     Individual species discrepancy tracking
     Multi-species TRU reconciliation support
     Species composition validation
     Detailed discrepancy analysis
4. **Process Integration**
     Transaction processing integration
     TRU status workflow integration
     Operator accountability tracking
     Measurement record validation
### Discrepancy Analysis
1. **Common Discrepancy Reasons**
     **Natural moisture loss**: Drying during transport
     **Bark loss**: Natural bark shedding during handling
     **Scale calibration**: Equipment calibration differences
     **Measurement method**: Different measurement techniques
     **Species misidentification**: Incorrect species classification
2. **Tolerance Guidelines**
     **High-value timber**: 1-2% tolerance
     **Pulp wood**: 3-5% tolerance
     **Biomass fuel**: 5-10% tolerance
     **Multi-species piles**: Higher tolerance for complexity
3. **Resolution Strategies**
     **Within tolerance**: Accept discrepancy, document reason
     **Exceeds tolerance**: Investigate and remeasure
     **Systematic error**: Calibrate equipment, adjust process
     **Species composition**: Verify species identification
### Validation Rules
1. **Measurement Consistency**
     forestMeasurement and millMeasurement must be ≥ 0
     discrepancy = forestMeasurement - millMeasurement
     tolerancePercentage must be between 0 and 100
2. **Status Workflow**
     Initial status must be "pending"
     Status changes must be documented with reconciliationDate
     Resolved status requires resolutionNotes
3. **TRU Integration**
     traceableUnitId must reference existing TRU
     reconciliationDate must be ≥ TRU measurement timestamps
     Species discrepancies must match TRU species composition
### Example Use Cases
1. **Standard Reconciliation**
     Forest measurement: 85.25 m³
     Mill measurement: 84.75 m³
     Discrepancy: 0.50 m³ (0.6%)
     Status: Resolved (within 2% tolerance)
     Reason: Natural moisture loss during transport
2. **Disputed Reconciliation**
     Forest measurement: 120.50 m³
     Mill measurement: 115.25 m³
     Discrepancy: 5.25 m³ (4.4%)
     Status: Disputed (exceeds 3% tolerance)
     Action: Remeasurement and investigation required
3. **Species-Specific Reconciliation**
     Multi-species pile with individual species discrepancies
     Overall discrepancy within tolerance
     Individual species discrepancies documented
     Species composition validation completed
### Relationships
- DataReconciliation belongs to one TraceableUnit
- DataReconciliation may belong to one Transaction
- DataReconciliation performed by one reconciliationOperator
- DataReconciliation validates MeasurementRecord accuracy
- DataReconciliation supports Transaction processing validation
- DataReconciliation enables TRU quality assurance workflows
