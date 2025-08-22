<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: lcfs_reporting/validation_schema.json and lcfs_reporting_dictionary.md
     To modify this content, edit the source file and regenerate -->

Quarterly LCFS compliance report for regulated entities with credit calculations and submission tracking

**[View LCFS Reporting in ERD Navigator](erd-navigator/index.html?focus=LcfsReporting)**

### Relationships ### {{.unnumbered}}

- **VerificationStatementId** → [[#verification-statement|Verification Statement]] - Uses EntityNameId convention referencing VerificationStatement for third-party verification

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
<td>JSON-LD context for semantic web compatibility
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>Unique URI identifier for JSON-LD
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>complianceStatus</code>
<td>enum(4 values)
<td>Overall compliance status for the reporting period
<td>✓
</tr>
<tr>
<td><code>netPosition</code>
<td>number
<td>Net credit/deficit position (credits - deficits)
<td>✓
</tr>
<tr>
<td><code>regulatedEntityId</code>
<td>string (pattern)
<td>Reference to regulated Organization entity
<td>✓
</tr>
<tr>
<td><code>reportingId</code>
<td>string (pattern)
<td>Unique identifier for the quarterly report
<td>✓
</tr>
<tr>
<td><code>reportingPeriod</code>
<td>string (pattern)
<td>Reporting quarter in YYYY-QN format
<td>✓
</tr>
<tr>
<td><code>totalCreditsGenerated</code>
<td>number (≥0)
<td>Total LCFS credits generated in the reporting period
<td>✓
</tr>
<tr>
<td><code>totalDeficitsIncurred</code>
<td>number (≥0)
<td>Total LCFS deficits incurred in the reporting period
<td>✓
</tr>
<tr>
<td><code>totalFuelVolume</code>
<td>number (≥0)
<td>Total fuel volume reported in gallons
<td>✓
</tr>
<tr>
<td><code>VerificationStatementId</code>
<td>string (pattern)
<td>Uses EntityNameId convention referencing VerificationStatement for third-party verification
<td>
</tr>
<tr>
<td><code>calculationParameters</code>
<td>object (structured)
<td>Calculation parameters used for credit computation
<td>
</tr>
<tr>
<td><code>complianceMetrics</code>
<td>object (structured)
<td>Additional compliance and environmental impact metrics
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of most recent report update
<td>
</tr>
<tr>
<td><code>pathwaySummary</code>
<td>array&amp;lt;object&amp;gt;
<td>Summary of activity by LCFS pathway
<td>
</tr>
<tr>
<td><code>reportingDeadline</code>
<td>string (date)
<td>CARB deadline for report submission
<td>
</tr>
<tr>
<td><code>submissionDate</code>
<td>string (date-time)
<td>Date and time report was submitted to CARB
<td>
</tr>
<tr>
<td><code>transactionIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of Transaction entity IDs included in this report
<td>
</tr>
<tr>
<td><code>verificationDate</code>
<td>string (date-time)
<td>Date of third-party verification completion
<td>
</tr>
<tr>
<td><code>verificationRequired</code>
<td>boolean
<td>Whether third-party verification is required for this entity
<td>
</tr>
</tbody>
</table>

## LCFSReporting
### Overview
The `LCFSReporting` entity represents quarterly compliance reports submitted by regulated entities to the California Air Resources Board (CARB) for the Low Carbon Fuel Standard (LCFS) program. Each report aggregates transaction data, calculates credit/deficit positions, and tracks submission status for regulatory compliance.
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
<td>`reportingId`
<td>string
<td>Yes
<td>Unique identifier for quarterly report (primary key)
<td>`LCFS-RPT-2025-Q1-PACIFIC001`
</tr>
<tr>
<td>`regulatedEntityId`
<td>string (FK)
<td>Yes
<td>Reference to regulated Organization entity
<td>`pacific-renewable-fuels-001`
</tr>
<tr>
<td>`reportingPeriod`
<td>string
<td>Yes
<td>Reporting quarter in YYYY-QN format
<td>`2025-Q1`, `2025-Q2`, `2025-Q3`
</tr>
<tr>
<td>`totalFuelVolume`
<td>number
<td>Yes
<td>Total fuel volume reported in gallons
<td>`5075000.0`, `8250000.0`
</tr>
<tr>
<td>`totalCreditsGenerated`
<td>number
<td>Yes
<td>Total LCFS credits generated in reporting period
<td>`54580477.10`, `0.0`
</tr>
<tr>
<td>`totalDeficitsIncurred`
<td>number
<td>Yes
<td>Total LCFS deficits incurred in reporting period
<td>`0.0`, `2500000.0`
</tr>
<tr>
<td>`netPosition`
<td>number
<td>Yes
<td>Net credit/deficit position (credits - deficits)
<td>`54580477.10`, `-2500000.0`
</tr>
<tr>
<td>`complianceStatus`
<td>string (enum)
<td>Yes
<td>Overall compliance status for reporting period
<td>`compliant`, `deficit`, `pending`
</tr>
<tr>
<td>`submissionDate`
<td>string (date-time)
<td>No
<td>Date and time report was submitted to CARB
<td>`2025-04-15T10:30:00Z`
</tr>
<tr>
<td>`verificationDate`
<td>string (date-time)
<td>No
<td>Date of third-party verification completion
<td>`2025-04-10T14:00:00Z`
</tr>
<tr>
<td>`verificationRequired`
<td>boolean
<td>No
<td>Whether third-party verification is required
<td>`true`, `false`
</tr>
<tr>
<td>`reportingDeadline`
<td>string (date)
<td>No
<td>CARB deadline for report submission
<td>`2025-05-15`
</tr>
<tr>
<td>`transactionIds`
<td>array&lt;string&gt;
<td>No
<td>Array of Transaction entity IDs included in report
<td>`["TXN-2025-Q1-001", "TXN-2025-Q1-002"]`
</tr>
<tr>
<td>`pathwaySummary`
<td>array&lt;object&gt;
<td>No
<td>Summary of activity by LCFS pathway
<td>See pathway summary structure below
</tr>
<tr>
<td>`calculationParameters`
<td>object
<td>No
<td>Calculation parameters used for credit computation
<td>See calculation parameters structure
</tr>
<tr>
<td>`complianceMetrics`
<td>object
<td>No
<td>Additional compliance and environmental impact metrics
<td>See compliance metrics structure
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/lcfs-reporting/LCFS-RPT-2025-Q1-PACIFIC001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of most recent report update
<td>`2025-07-21T16:45:00Z`
</tr>
</tbody>
</table>
---
### Nested Structures
#### Pathway Summary
Each pathway summary object contains:
- `pathwayId` (string, required): CARB pathway identifier
- `feedstockType` (string, optional): Primary feedstock category 
- `transactionCount` (integer, required): Number of transactions for this pathway
- `totalVolume` (number, required): Total fuel volume for this pathway in gallons
- `creditsGenerated` (number, required): Credits generated from this pathway
#### Calculation Parameters
- `conversionFactor` (number): Energy conversion factor (MJ/gallon)
- `conversionFactorUnit` (string): Unit for energy conversion factor
- `regulatoryBenchmark` (number): Annual regulatory benchmark (gCO2e/MJ)
- `benchmarkUnit` (string): Unit for regulatory benchmark
- `defaultEER` (number): Default energy economy ratio
#### Compliance Metrics
- `creditValue` (object): Monetary valuation of credits
  - `estimatedValue` (number): Estimated monetary value of credits
  - `valueUnit` (string): Currency unit for credit value
  - `creditPrice` (number): Price per credit used in valuation
  - `priceUnit` (string): Unit for credit price
- `environmentalImpact` (object): Environmental impact metrics
  - `co2ReductionMT` (number): CO2 reduction in metric tons
  - `co2ReductionUnit` (string): Unit for CO2 reduction
  - `equivalentCarsRemoved` (integer): Equivalent number of cars removed from roads
---
### Key Features
1. **Quarterly Reporting Compliance**
     Standardized reporting period format (YYYY-QN)
     Automatic deadline calculation and tracking
     Submission status monitoring
2. **Credit/Deficit Calculation**
     Aggregated credit generation from all transactions
     Net position calculation (credits - deficits)
     Compliance status determination
3. **Third-Party Verification**
     Verification requirement tracking based on entity size
     Verification completion date tracking
     Compliance timeline management
4. **Pathway Activity Summary**
     Breakdown of activity by CARB pathway
     Transaction count and volume aggregation
     Feedstock type categorization
### Example Use Cases
1. **Large Regulated Producer**
     Multiple pathways and high transaction volume
     Third-party verification required
     Net credit generator with surplus for trading
2. **Small Regulated Importer** 
     Single pathway, lower transaction volume
     Self-certification allowed
     Compliance through purchased credits
3. **Blender/Distributor**
     Mix of conventional and renewable fuels
     Deficit position requiring credit purchases
     Complex pathway attribution
### Relationships
- LCFSReporting references Organization entity for regulated party
- LCFSReporting aggregates Transaction entities within reporting period
- LCFSReporting references LCFSPathway entities for pathway summaries
- LCFSReporting may reference VerificationStatement for third-party verification
- LCFSReporting connects to EnergyCarbonData for calculation validation
### Credit Calculation Logic
The report aggregates credits calculated at the transaction level:
```
Total Credits = Σ[(Benchmark_CI - Pathway_CI) × Transaction_Volume_MJ × EER]
```
For each transaction in the reporting period, using:
- Regulatory benchmarks: 95.61 gCO2e/MJ (gasoline), 98.47 gCO2e/MJ (diesel)
- Pathway carbon intensities from LCFSPathway entities
- Volume conversions: 138.7 MJ/gallon (diesel), 120.0 MJ/gallon (gasoline)
- Energy Economy Ratios from pathway specifications
### Validation Rules
- Reporting periods must follow YYYY-QN format
- Net position must equal credits generated minus deficits incurred
- Transaction IDs must reference valid Transaction entities
- Pathway IDs must reference active CARB pathways
- Submission dates must be before reporting deadlines
- All volumes and credits must be non-negative numbers
