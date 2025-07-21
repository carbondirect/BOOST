# Data Dictionary

## Claim (Enhanced)

### Overview
The enhanced `Claim` entity enables species-specific sustainability claims with TRU references and inheritance tracking for comprehensive certification chain-of-custody in the Kaulen framework. This entity supports multiple certification schemes and enables granular tracking of sustainability claims through the processing chain, including parent-child TRU inheritance.

### Fields

| Field                    | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `claimId`               | string           | Yes      | Unique identifier for the claim (primary key)                            | `CLAIM-001`, `CLAIM-FSC-KLA-042`          |
| `traceableUnitId`       | string (FK)      | Yes      | Foreign key to TRU this claim applies to                                 | `TRU-LOG-001`, `TRU-PILE-CA-042`          |
| `claimType`             | string           | Yes      | Type of sustainability claim (enum)                                       | `FSC Mix`, `SBP-compliant`, `PEFC`, `organic` |
| `certificationSchemeId` | string (FK)      | No       | Foreign key to certification scheme details                               | `CERT-FSC-001`, `CERT-SBP-GLOBAL`         |
| `statement`             | string           | Yes      | Formal claim statement                                                    | `FSC Mix 70%`, `SBP-compliant biomass`    |
| `validated`             | boolean          | Yes      | Whether the claim has been validated                                      | `true`, `false`                           |
| `validatedBy`           | string (FK)      | No       | Foreign key to validator (Organization/Person)                           | `ORG-FSC-CERTIFIER-001`, `OP-AUDITOR-02` |
| `validationDate`        | string (date-time)| No      | When the claim was validated                                             | `2025-07-15T09:00:00Z`                    |
| `applicableSpecies`     | array<string>    | No       | Specific species this claim applies to                                    | `["douglas_fir", "ponderosa_pine"]`       |
| `claimPercentage`       | number           | No       | Percentage of material covered by claim (0-100)                          | `70.5`, `100.0`, `45.2`                  |
| `claimScope`            | string           | No       | Scope of the claim through supply chain                                  | `harvest`, `processing`, `transport`, `full_chain` |
| `evidenceDocumentId`    | string (FK)      | No       | Foreign key to supporting evidence document                               | `DOC-CERT-FSC-001`, `DOC-AUDIT-RPT-042`  |
| `claimExpiry`           | string (date-time)| No      | When the claim expires                                                   | `2026-07-15T23:59:59Z`                   |
| `inheritedFromTRU`      | array<string>    | No       | TRU IDs from which this claim was inherited                              | `["TRU-PARENT-001", "TRU-PARENT-002"]`   |
| `@id`                   | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/claim-enhanced/CLAIM-001` |
| `lastUpdated`           | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Claim Types

1. **FSC Mix**
   - Forest Stewardship Council mixed content claims
   - Percentage-based certification claims
   - Chain of custody requirements
   - Species-specific applicability
   - Controlled wood component tracking

2. **FSC 100%**
   - Full FSC certified content
   - Complete chain of custody verification
   - No non-certified material mixing
   - Premium certification status
   - Strict processing segregation

3. **FSC Recycled**
   - Post-consumer recycled content claims
   - Recycled content percentage tracking
   - Source material verification
   - Environmental impact claims
   - Circular economy support

4. **PEFC**
   - Programme for the Endorsement of Forest Certification
   - Regional forest management standards
   - Sustainable forest management claims
   - International mutual recognition
   - National scheme integration

5. **SBP-compliant**
   - Sustainable Biomass Partnership compliance
   - Biomass sustainability verification
   - Regional risk assessment integration
   - Supply base evaluation compliance
   - Biomass-specific claim requirements

6. **ISCC EU**
   - International Sustainability and Carbon Certification
   - European Union renewable energy directive compliance
   - Greenhouse gas emission reduction verification
   - Sustainability criteria compliance
   - Mass balance chain of custody

7. **RED II**
   - Renewable Energy Directive II compliance
   - EU renewable energy sustainability requirements
   - Greenhouse gas emission thresholds
   - Land use change restrictions
   - Sustainability governance requirements

### Claim Scopes

1. **harvest**
   - Claims applicable to harvesting operations
   - Forest management practice compliance
   - Sustainable harvesting method verification
   - Species-specific harvest practices
   - Ecosystem impact assessments

2. **processing**
   - Manufacturing and processing compliance
   - Processing facility certification
   - Chemical treatment restrictions
   - Processing efficiency requirements
   - Quality management systems

3. **transport**
   - Supply chain transportation compliance
   - Segregation maintenance during transport
   - Chain of custody documentation
   - Transport emission considerations
   - Logistics sustainability practices

4. **full_chain**
   - Complete supply chain claim coverage
   - End-to-end certification maintenance
   - Comprehensive audit trail requirements
   - Multi-stakeholder verification
   - Complete chain of custody

### Key Features

1. **Species-Specific Claims**
   - Individual species claim applications
   - Multi-species claim distribution
   - Species composition validation
   - Biodiversity compliance verification
   - Conservation impact tracking

2. **TRU Inheritance Tracking**
   - Parent TRU claim inheritance
   - Split/merge claim distribution
   - Processing chain claim continuity
   - Chain of custody maintenance
   - Audit trail preservation

3. **Percentage-Based Claims**
   - Partial certification content tracking
   - Mixed source material claims
   - Controlled wood component identification
   - Claim percentage validation
   - Mass balance calculations

4. **Validation and Verification**
   - Third-party validation support
   - Evidence document linking
   - Expiry date management
   - Validation timestamp tracking
   - Auditor accountability

### Claim Inheritance Rules

1. **Split Operations**
   - Claims inherited by all child TRUs
   - Percentage adjustments for volume changes
   - Species-specific claim distribution
   - Volume-weighted claim allocation
   - Conservation of total certified volume

2. **Merge Operations**
   - Claims combined from parent TRUs
   - Percentage recalculation for combined volume
   - Species composition impact on claims
   - Claim compatibility verification
   - Mixed claim scenario handling

3. **Processing Operations**
   - Claim continuity through processing
   - Processing-specific claim restrictions
   - Equipment contamination considerations
   - Segregation requirement compliance
   - Processing facility certification requirements

### Validation Rules

1. **TRU Integration**
   - traceableUnitId must reference existing TRU
   - Claim must be compatible with TRU species composition
   - Claim percentage must not exceed 100%
   - Inheritance tracking must reference valid parent TRUs

2. **Certification Logic**
   - Claim type must be compatible with certification scheme
   - Validation must be performed by authorized validator
   - Evidence documents must support claim statement
   - Expiry dates must be reasonable and future-dated

3. **Species Consistency**
   - applicableSpecies must be subset of TRU species composition
   - Species-specific claims must sum to valid totals
   - Multi-species claims must account for all species
   - Species claim percentages must align with composition

### Example Use Cases

1. **FSC Mix Inheritance**
   - Parent TRU with 70% FSC Mix claim
   - Crosscutting operation creates 3 child TRUs
   - Each child inherits 70% FSC Mix claim
   - Volume distribution tracked for mass balance
   - Chain of custody documentation maintained

2. **Multi-Species Claim Application**
   - Mixed species TRU with Douglas Fir and Pine
   - FSC claim applies only to Douglas Fir component
   - Species-specific claim percentage calculation
   - Pine component tracked as controlled wood
   - Overall claim percentage reflects species mix

3. **Processing Chain Claim Continuity**
   - Harvest site TRU with SBP-compliant claim
   - Processing through felling, delimbing, crosscutting
   - Claim maintained through each processing step
   - Processing facility certification verified
   - Final product maintains SBP compliance

### Relationships
- Claim belongs to one TraceableUnit
- Claim references CertificationScheme for detailed requirements
- Claim validated by Organization or Operator
- Claim supported by evidence documents
- Claim inherited from parent TraceableUnits through processing chain
- Claim enables species-specific sustainability tracking
- Claim supports mass balance chain of custody calculations