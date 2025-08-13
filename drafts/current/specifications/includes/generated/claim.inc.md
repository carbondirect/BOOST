<!-- Auto-generated from claim/validation_schema.json -->

Claim entity in BOOST data model

**🗂️ [View Claim in ERD Navigator](erd-navigator/index.html?focus=Claim)**

### Relationships ### {{.unnumbered}}

- **TraceableUnitId** → [[#traceable-unit|Traceable Unit]] - Referenced traceable unit - uses EntityNameId convention referencing TraceableUnit
- **CertificationSchemeId** → [[#certification-scheme|Certification Scheme]] - Certification scheme - uses EntityNameId convention referencing CertificationScheme

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
<td>enum(Claim)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>TraceableUnitId</code>
<td>string (pattern)
<td>Referenced traceable unit - uses EntityNameId convention referencing TraceableUnit
<td>✓
</tr>
<tr>
<td><code>claimId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>claimType</code>
<td>enum(9 values)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>statement</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>validated</code>
<td>boolean
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>CertificationSchemeId</code>
<td>string (pattern)
<td>Certification scheme - uses EntityNameId convention referencing CertificationScheme
<td>
</tr>
<tr>
<td><code>applicableSpecies</code>
<td>array&amp;lt;string&amp;gt;
<td>No description provided
<td>
</tr>
<tr>
<td><code>claimExpiry</code>
<td>string (date-time)
<td>No description provided
<td>
</tr>
<tr>
<td><code>claimPercentage</code>
<td>number (≥0, ≤100)
<td>No description provided
<td>
</tr>
<tr>
<td><code>claimScope</code>
<td>enum(4 values)
<td>No description provided
<td>
</tr>
<tr>
<td><code>evidenceDocumentId</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>inheritedFromTRU</code>
<td>array&amp;lt;string&amp;gt;
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
<td><code>validatedBy</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>validationDate</code>
<td>string (date-time)
<td>No description provided
<td>
</tr>
</tbody>
</table>

## Claim
### Overview
The `Claim` entity enables species-specific sustainability claims with TRU references and inheritance tracking for comprehensive certification chain-of-custody in the BOOST traceability system. This entity supports multiple certification schemes and enables granular tracking of sustainability claims through the processing chain, including parent-child TRU inheritance.
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
<td>`claimId`
<td>string
<td>Yes
<td>Unique identifier for the claim (primary key)
<td>`CLAIM-001`, `CLAIM-FSC-KLA-042`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU this claim applies to
<td>`TRU-LOG-001`, `TRU-PILE-CA-042`
</tr>
<tr>
<td>`claimType`
<td>string
<td>Yes
<td>Type of sustainability claim (enum)
<td>`FSC Mix`, `SBP-compliant`, `PEFC`, `organic`
</tr>
<tr>
<td>`certificationSchemeId`
<td>string (FK)
<td>No
<td>Foreign key to certification scheme details
<td>`CERT-FSC-001`, `CERT-SBP-GLOBAL`
</tr>
<tr>
<td>`statement`
<td>string
<td>Yes
<td>Formal claim statement
<td>`FSC Mix 70%`, `SBP-compliant biomass`
</tr>
<tr>
<td>`validated`
<td>boolean
<td>Yes
<td>Whether the claim has been validated
<td>`true`, `false`
</tr>
<tr>
<td>`validatedBy`
<td>string (FK)
<td>No
<td>Foreign key to validator (Organization/Person)
<td>`ORG-FSC-CERTIFIER-001`, `OP-AUDITOR-02`
</tr>
<tr>
<td>`validationDate`
<td>string (date-time)
<td>No
<td>When the claim was validated
<td>`2025-07-15T09:00:00Z`
</tr>
<tr>
<td>`applicableSpecies`
<td>array&lt;string&gt;
<td>No
<td>Specific species this claim applies to
<td>`["douglas_fir", "ponderosa_pine"]`
</tr>
<tr>
<td>`claimPercentage`
<td>number
<td>No
<td>Percentage of material covered by claim (0-100)
<td>`70.5`, `100.0`, `45.2`
</tr>
<tr>
<td>`claimScope`
<td>string
<td>No
<td>Scope of the claim through supply chain
<td>`harvest`, `processing`, `transport`, `full_chain`
</tr>
<tr>
<td>`evidenceDocumentId`
<td>string (FK)
<td>No
<td>Foreign key to supporting evidence document
<td>`DOC-CERT-FSC-001`, `DOC-AUDIT-RPT-042`
</tr>
<tr>
<td>`claimExpiry`
<td>string (date-time)
<td>No
<td>When the claim expires
<td>`2026-07-15T23:59:59Z`
</tr>
<tr>
<td>`inheritedFromTRU`
<td>array&lt;string&gt;
<td>No
<td>TRU IDs from which this claim was inherited
<td>`["TRU-PARENT-001", "TRU-PARENT-002"]`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/claim/CLAIM-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-21T15:45:00Z`
</tr>
</tbody>
</table>
### Claim Types
1. **FSC Mix**
     Forest Stewardship Council mixed content claims
     Percentage-based certification claims
     Chain of custody requirements
     Species-specific applicability
     Controlled wood component tracking
2. **FSC 100%**
     Full FSC certified content
     Complete chain of custody verification
     No non-certified material mixing
     Premium certification status
     Strict processing segregation
3. **FSC Recycled**
     Post-consumer recycled content claims
     Recycled content percentage tracking
     Source material verification
     Environmental impact claims
     Circular economy support
4. **PEFC**
     Programme for the Endorsement of Forest Certification
     Regional forest management standards
     Sustainable forest management claims
     International mutual recognition
     National scheme integration
5. **SBP-compliant**
     Sustainable Biomass Partnership compliance
     Biomass sustainability verification
     Regional risk assessment integration
     Supply base evaluation compliance
     Biomass-specific claim requirements
6. **ISCC EU**
     International Sustainability and Carbon Certification
     European Union renewable energy directive compliance
     Greenhouse gas emission reduction verification
     Sustainability criteria compliance
     Mass balance chain of custody
7. **RED II**
     Renewable Energy Directive II compliance
     EU renewable energy sustainability requirements
     Greenhouse gas emission thresholds
     Land use change restrictions
     Sustainability governance requirements
### Claim Scopes
1. **harvest**
     Claims applicable to harvesting operations
     Forest management practice compliance
     Sustainable harvesting method verification
     Species-specific harvest practices
     Ecosystem impact assessments
2. **processing**
     Manufacturing and processing compliance
     Processing facility certification
     Chemical treatment restrictions
     Processing efficiency requirements
     Quality management systems
3. **transport**
     Supply chain transportation compliance
     Segregation maintenance during transport
     Chain of custody documentation
     Transport emission considerations
     Logistics sustainability practices
4. **full_chain**
     Complete supply chain claim coverage
     End-to-end certification maintenance
     Comprehensive audit trail requirements
     Multi-stakeholder verification
     Complete chain of custody
### Key Features
1. **Species-Specific Claims**
     Individual species claim applications
     Multi-species claim distribution
     Species composition validation
     Biodiversity compliance verification
     Conservation impact tracking
2. **TRU Inheritance Tracking**
     Parent TRU claim inheritance
     Split/merge claim distribution
     Processing chain claim continuity
     Chain of custody maintenance
     Audit trail preservation
3. **Percentage-Based Claims**
     Partial certification content tracking
     Mixed source material claims
     Controlled wood component identification
     Claim percentage validation
     Mass balance calculations
4. **Validation and Verification**
     Third-party validation support
     Evidence document linking
     Expiry date management
     Validation timestamp tracking
     Auditor accountability
### Claim Inheritance Rules
1. **Split Operations**
     Claims inherited by all child TRUs
     Percentage adjustments for volume changes
     Species-specific claim distribution
     Volume-weighted claim allocation
     Conservation of total certified volume
2. **Merge Operations**
     Claims combined from parent TRUs
     Percentage recalculation for combined volume
     Species composition impact on claims
     Claim compatibility verification
     Mixed claim scenario handling
3. **Processing Operations**
     Claim continuity through processing
     Processing-specific claim restrictions
     Equipment contamination considerations
     Segregation requirement compliance
     Processing facility certification requirements
### Validation Rules
1. **TRU Integration**
     traceableUnitId must reference existing TRU
     Claim must be compatible with TRU species composition
     Claim percentage must not exceed 100%
     Inheritance tracking must reference valid parent TRUs
2. **Certification Logic**
     Claim type must be compatible with certification scheme
     Validation must be performed by authorized validator
     Evidence documents must support claim statement
     Expiry dates must be reasonable and future-dated
3. **Species Consistency**
     applicableSpecies must be subset of TRU species composition
     Species-specific claims must sum to valid totals
     Multi-species claims must account for all species
     Species claim percentages must align with composition
### Example Use Cases
1. **FSC Mix Inheritance**
     Parent TRU with 70% FSC Mix claim
     Crosscutting operation creates 3 child TRUs
     Each child inherits 70% FSC Mix claim
     Volume distribution tracked for mass balance
     Chain of custody documentation maintained
2. **Multi-Species Claim Application**
     Mixed species TRU with Douglas Fir and Pine
     FSC claim applies only to Douglas Fir component
     Species-specific claim percentage calculation
     Pine component tracked as controlled wood
     Overall claim percentage reflects species mix
3. **Processing Chain Claim Continuity**
     Harvest site TRU with SBP-compliant claim
     Processing through felling, delimbing, crosscutting
     Claim maintained through each processing step
     Processing facility certification verified
     Final product maintains SBP compliance
### Relationships
- Claim belongs to one TraceableUnit
- Claim references CertificationScheme for detailed requirements
- Claim validated by Organization or Operator
- Claim supported by evidence documents
- Claim inherited from parent TraceableUnits through processing chain
- Claim enables species-specific sustainability tracking
- Claim supports mass balance chain of custody calculations
