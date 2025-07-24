# Data Dictionary

## LCFSReporting

### Overview
The `LCFSReporting` entity represents quarterly compliance reports submitted by regulated entities to the California Air Resources Board (CARB) for the Low Carbon Fuel Standard (LCFS) program. Each report aggregates transaction data, calculates credit/deficit positions, and tracks submission status for regulatory compliance.

### Fields

| Field                    | Type                    | Required | Description                                                           | Examples                                    |
|--------------------------|-------------------------|----------|-----------------------------------------------------------------------|---------------------------------------------|
| `reportingId`            | string                  | Yes      | Unique identifier for quarterly report (primary key)                 | `LCFS-RPT-2025-Q1-PACIFIC001`             |
| `regulatedEntityId`      | string (FK)             | Yes      | Reference to regulated Organization entity                            | `pacific-renewable-fuels-001`              |
| `reportingPeriod`        | string                  | Yes      | Reporting quarter in YYYY-QN format                                  | `2025-Q1`, `2025-Q2`, `2025-Q3`           |
| `totalFuelVolume`        | number                  | Yes      | Total fuel volume reported in gallons                                | `5075000.0`, `8250000.0`                  |
| `totalCreditsGenerated`  | number                  | Yes      | Total LCFS credits generated in reporting period                      | `54580477.10`, `0.0`                      |
| `totalDeficitsIncurred`  | number                  | Yes      | Total LCFS deficits incurred in reporting period                      | `0.0`, `2500000.0`                        |
| `netPosition`            | number                  | Yes      | Net credit/deficit position (credits - deficits)                     | `54580477.10`, `-2500000.0`               |
| `complianceStatus`       | string (enum)           | Yes      | Overall compliance status for reporting period                        | `compliant`, `deficit`, `pending`          |
| `submissionDate`         | string (date-time)      | No       | Date and time report was submitted to CARB                           | `2025-04-15T10:30:00Z`                    |
| `verificationDate`       | string (date-time)      | No       | Date of third-party verification completion                           | `2025-04-10T14:00:00Z`                    |
| `verificationRequired`   | boolean                 | No       | Whether third-party verification is required                          | `true`, `false`                           |
| `reportingDeadline`      | string (date)           | No       | CARB deadline for report submission                                   | `2025-05-15`                              |
| `transactionIds`         | array<string>           | No       | Array of Transaction entity IDs included in report                    | `["TXN-2025-Q1-001", "TXN-2025-Q1-002"]` |
| `pathwaySummary`         | array<object>           | No       | Summary of activity by LCFS pathway                                   | See pathway summary structure below        |
| `calculationParameters`  | object                  | No       | Calculation parameters used for credit computation                     | See calculation parameters structure       |
| `complianceMetrics`      | object                  | No       | Additional compliance and environmental impact metrics                 | See compliance metrics structure           |
| `@id`                    | string (uri)            | Yes      | Unique URI identifier for JSON-LD                                     | `https://github.com/carbondirect/BOOST/schemas/lcfs-reporting/LCFS-RPT-2025-Q1-PACIFIC001` |
| `lastUpdated`            | string (date-time)      | No       | Timestamp of most recent report update                                | `2025-07-21T16:45:00Z`                    |

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
   - Standardized reporting period format (YYYY-QN)
   - Automatic deadline calculation and tracking
   - Submission status monitoring

2. **Credit/Deficit Calculation**
   - Aggregated credit generation from all transactions
   - Net position calculation (credits - deficits)
   - Compliance status determination

3. **Third-Party Verification**
   - Verification requirement tracking based on entity size
   - Verification completion date tracking
   - Compliance timeline management

4. **Pathway Activity Summary**
   - Breakdown of activity by CARB pathway
   - Transaction count and volume aggregation
   - Feedstock type categorization

### Example Use Cases

1. **Large Regulated Producer**
   - Multiple pathways and high transaction volume
   - Third-party verification required
   - Net credit generator with surplus for trading

2. **Small Regulated Importer** 
   - Single pathway, lower transaction volume
   - Self-certification allowed
   - Compliance through purchased credits

3. **Blender/Distributor**
   - Mix of conventional and renewable fuels
   - Deficit position requiring credit purchases
   - Complex pathway attribution

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