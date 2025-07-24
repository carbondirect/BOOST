# Data Dictionary

## LCFSPathway

### Overview
The `LCFSPathway` entity represents CARB-certified fuel pathways for California's Low Carbon Fuel Standard (LCFS) compliance. Each pathway defines the carbon intensity, feedstock type, production process, and regulatory status for specific fuel production routes. This entity enables LCFS credit calculations and regulatory reporting by linking transactions to certified carbon intensities.

### Fields

| Field                | Type                | Required | Description                                                                 | Examples                                    |
|---------------------|---------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `pathwayId`         | string              | Yes      | CARB-assigned pathway identifier (primary key)                            | `CA-RD-2025-LMR-001`, `CA-ET-2025-CRN-042` |
| `pathwayType`       | string (enum)       | Yes      | CARB pathway certification tier                                            | `Lookup_Table`, `Tier_1`, `Tier_2`         |
| `feedstockCategory` | string (enum)       | Yes      | Primary feedstock type for pathway                                         | `logging_and_mill_residue`, `corn`, `algae` |
| `fuelProduct`       | string (enum)       | Yes      | Final fuel product produced                                                | `renewable_diesel`, `ethanol`, `biodiesel`  |
| `facilityLocation`  | string              | Yes      | Production facility location                                               | `Stockton, CA`, `Iowa`, `Western_US`        |
| `carbonIntensity`   | number              | Yes      | Certified carbon intensity in gCO2e/MJ                                    | `19.85`, `74.32`, `12.41`                  |
| `energyEconomyRatio`| number              | Yes      | Energy economy ratio multiplier for credit calculation                     | `1.0`, `1.5`, `2.0`                        |
| `certificationDate` | string (date)       | Yes      | CARB pathway certification date                                            | `2025-01-15`                               |
| `expirationDate`    | string (date)       | No       | Pathway certification expiration date                                      | `2028-01-15`                               |
| `verificationStatus`| string (enum)       | Yes      | Current CARB verification status                                           | `active`, `suspended`, `expired`            |
| `caGreetVersion`    | string              | Yes      | CA-GREET model version used for certification                              | `3.0`, `2.1`                              |
| `facilityCapacity`  | number              | No       | Annual production capacity in gallons                                      | `50000000`, `125000000`                    |
| `processDescription`| string              | No       | Brief description of production process                                    | `Hydrotreated renewable diesel production`  |
| `geographicScope`   | string (enum)       | No       | Geographic applicability of pathway                                        | `California`, `Western_US`, `National`      |
| `@id`               | string (uri)        | Yes      | Unique URI identifier for JSON-LD                                         | `https://github.com/carbondirect/BOOST/schemas/lcfs-pathway/CA-RD-2025-LMR-001` |
| `lastUpdated`       | string (date-time)  | No       | Timestamp of most recent pathway data update                               | `2025-07-21T14:30:00Z`                     |

---

### Key Features

1. **CARB Pathway Integration**
   - Direct mapping to official CARB pathway database
   - Standardized pathway ID format validation
   - Certification tier tracking (Lookup Table, Tier 1, Tier 2)

2. **Carbon Intensity Tracking**
   - Certified CI values from CA-GREET modeling
   - Energy Economy Ratio for electric vehicle pathways
   - Regulatory benchmark comparison support

3. **Feedstock Classification**
   - Comprehensive feedstock categories for all LCFS fuel types
   - Forest biomass subcategories for waste vs. purpose-grown materials
   - Integration with BOOST material tracking entities

4. **Regulatory Compliance**
   - Active/suspended/expired status tracking
   - Certification and expiration date management
   - CA-GREET version compatibility

### Example Use Cases

1. **Renewable Diesel from Forest Residue**
   - Pathway Type: Tier_1
   - Feedstock: logging_and_mill_residue
   - Carbon Intensity: 19.85 gCO2e/MJ
   - Energy Economy Ratio: 1.0

2. **Ethanol from Corn**
   - Pathway Type: Lookup_Table
   - Feedstock: corn
   - Carbon Intensity: 74.32 gCO2e/MJ
   - Energy Economy Ratio: 1.0

3. **Sustainable Aviation Fuel**
   - Pathway Type: Tier_2
   - Feedstock: used_cooking_oil
   - Carbon Intensity: 12.41 gCO2e/MJ
   - Energy Economy Ratio: 1.0

### Relationships
- LCFSPathway referenced by Transaction entities for LCFS reporting
- LCFSPathway linked to EnergyCarbonData for detailed carbon accounting
- LCFSPathway used in LCFSReporting for quarterly submissions
- LCFSPathway connected to Organization entities for pathway ownership
- LCFSPathway integrated with TraceableUnit for feedstock traceability

### Credit Calculation Formula

LCFS credits are calculated using pathway data:

```
Credits = (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER
```

Where:
- **Benchmark_CI**: Annual regulatory benchmark (95.61 for gasoline, 98.47 for diesel)
- **Pathway_CI**: `carbonIntensity` field value
- **Fuel_Volume_MJ**: Fuel volume converted to megajoules
- **EER**: `energyEconomyRatio` field value

### Validation Rules
- Pathway IDs must follow CARB format: `CA-{FUEL}-{YEAR}-{FEEDSTOCK}-{NUMBER}`
- Carbon intensity must be positive and typically under 200 gCO2e/MJ
- Energy Economy Ratio typically ranges from 0.5 to 3.0
- Certification dates must precede expiration dates
- Active pathways must have future expiration dates