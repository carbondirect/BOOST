# Data Dictionary

## DataReconciliation

### Overview
The `DataReconciliation` entity reconciles measurements between forest and mill with TRU references and species-specific discrepancies to ensure data accuracy and prevent media breaks. This entity enables automated comparison of harvest measurements with mill scale measurements, identifies discrepancies, and tracks resolution status as required by the BOOST traceability system for measurement validation.

### Fields

| Field                    | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `reconciliationId`      | string           | Yes      | Unique identifier for the reconciliation record (primary key)             | `DR-001`, `DR-KLA-042-RECON-001`          |
| `traceableUnitId`       | string (FK)      | Yes      | Foreign key to TRU being reconciled                                       | `TRU-PILE-CA-Klamath-042`                 |
| `transactionId`         | string (FK)      | No       | Foreign key to associated transaction                                     | `TXN-PACIFIC-MILL-001`                    |
| `forestMeasurement`     | number           | Yes      | Measurement taken in forest (cubic meters)                               | `85.25`, `120.50`, `45.75`                |
| `millMeasurement`       | number           | Yes      | Measurement taken at mill (cubic meters)                                 | `84.75`, `119.25`, `46.10`                |
| `discrepancy`           | number           | Yes      | Difference between measurements (forest - mill)                          | `0.50`, `-1.25`, `0.35`                   |
| `reconciliationStatus` | string           | Yes      | Current status of reconciliation (enum)                                  | `pending`, `resolved`, `disputed`          |
| `discrepancyReason`     | string           | No       | Reason for discrepancy                                                    | `Natural moisture loss`, `Scale calibration error`, `Bark loss` |
| `reconciliationDate`    | string (date-time)| Yes     | When reconciliation was performed                                         | `2025-07-21T15:00:00Z`                    |
| `reconciliationOperator`| string           | No       | Operator who performed reconciliation                                     | `OP-QUALITY-TECH-001`, `OP-SCALE-MANAGER-02` |
| `speciesDiscrepancies`  | array<string>    | No       | Per-species discrepancies for multi-species TRUs                        | `["Douglas Fir: +0.25m3", "Pine: -0.15m3"]` |
| `tolerancePercentage`   | number           | No       | Acceptable tolerance percentage (0-100)                                   | `2.5`, `5.0`, `1.0`                       |
| `resolutionNotes`       | string           | No       | Notes on how discrepancy was resolved                                     | `Accepted within tolerance`, `Remeasurement confirmed mill scale` |
| `@id`                   | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/data-reconciliation/DR-001` |
| `lastUpdated`           | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:30:00Z`                    |

### Reconciliation Status Values

1. **pending**
   - Reconciliation process initiated but not completed
   - Measurements compared, discrepancy calculated
   - Awaiting review or resolution action
   - Default status for new reconciliation records

2. **resolved**
   - Discrepancy has been addressed and accepted
   - Resolution notes document how discrepancy was handled
   - TRU can proceed in transaction processing
   - Final status for acceptable discrepancies

3. **disputed**
   - Discrepancy exceeds acceptable tolerance
   - Requires investigation or remeasurement
   - TRU processing may be held pending resolution
   - Escalation to quality assurance team

### Key Features

1. **Automated Comparison**
   - Systematic comparison of forest vs mill measurements
   - Automatic discrepancy calculation
   - Tolerance-based status assignment
   - Species-level discrepancy tracking

2. **Quality Assurance**
   - Tolerance percentage enforcement
   - Discrepancy reason categorization
   - Resolution process documentation
   - Audit trail for measurement validation

3. **Species-Specific Tracking**
   - Individual species discrepancy tracking
   - Multi-species TRU reconciliation support
   - Species composition validation
   - Detailed discrepancy analysis

4. **Process Integration**
   - Transaction processing integration
   - TRU status workflow integration
   - Operator accountability tracking
   - Measurement record validation

### Discrepancy Analysis

1. **Common Discrepancy Reasons**
   - **Natural moisture loss**: Drying during transport
   - **Bark loss**: Natural bark shedding during handling
   - **Scale calibration**: Equipment calibration differences
   - **Measurement method**: Different measurement techniques
   - **Species misidentification**: Incorrect species classification

2. **Tolerance Guidelines**
   - **High-value timber**: 1-2% tolerance
   - **Pulp wood**: 3-5% tolerance
   - **Biomass fuel**: 5-10% tolerance
   - **Multi-species piles**: Higher tolerance for complexity

3. **Resolution Strategies**
   - **Within tolerance**: Accept discrepancy, document reason
   - **Exceeds tolerance**: Investigate and remeasure
   - **Systematic error**: Calibrate equipment, adjust process
   - **Species composition**: Verify species identification

### Validation Rules

1. **Measurement Consistency**
   - forestMeasurement and millMeasurement must be ≥ 0
   - discrepancy = forestMeasurement - millMeasurement
   - tolerancePercentage must be between 0 and 100

2. **Status Workflow**
   - Initial status must be "pending"
   - Status changes must be documented with reconciliationDate
   - Resolved status requires resolutionNotes

3. **TRU Integration**
   - traceableUnitId must reference existing TRU
   - reconciliationDate must be ≥ TRU measurement timestamps
   - Species discrepancies must match TRU species composition

### Example Use Cases

1. **Standard Reconciliation**
   - Forest measurement: 85.25 m³
   - Mill measurement: 84.75 m³
   - Discrepancy: 0.50 m³ (0.6%)
   - Status: Resolved (within 2% tolerance)
   - Reason: Natural moisture loss during transport

2. **Disputed Reconciliation**
   - Forest measurement: 120.50 m³
   - Mill measurement: 115.25 m³
   - Discrepancy: 5.25 m³ (4.4%)
   - Status: Disputed (exceeds 3% tolerance)
   - Action: Remeasurement and investigation required

3. **Species-Specific Reconciliation**
   - Multi-species pile with individual species discrepancies
   - Overall discrepancy within tolerance
   - Individual species discrepancies documented
   - Species composition validation completed

### Relationships
- DataReconciliation belongs to one TraceableUnit
- DataReconciliation may belong to one Transaction
- DataReconciliation performed by one reconciliationOperator
- DataReconciliation validates MeasurementRecord accuracy
- DataReconciliation supports Transaction processing validation
- DataReconciliation enables TRU quality assurance workflows