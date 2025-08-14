<!-- Auto-generated from mass_balance_account/validation_schema.json -->

MassBalanceAccount entity in BOOST data model

**[View Mass Balance Account in ERD Navigator](erd-navigator/index.html?focus=MassBalanceAccount)**

### Relationships ### {{.unnumbered}}

- **organizationId** → [[#organization|Organization]]
- **productGroupId** → [[#product-group|Product Group]]

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
<td>enum(MassBalanceAccount)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>accountId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>currentBalance</code>
<td>number
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>organizationId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>productGroupId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>balancingPeriod</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>conversionFactors</code>
<td>number
<td>No description provided
<td>
</tr>
<tr>
<td><code>periodInputs</code>
<td>number
<td>No description provided
<td>
</tr>
<tr>
<td><code>periodOutputs</code>
<td>number
<td>No description provided
<td>
</tr>
</tbody>
</table>

## MassBalanceAccount
### Overview
The `MassBalanceAccount` entity manages mass balance accounting for material flow tracking and compliance reporting within the BOOST traceability system. Mass balance accounting is a fundamental requirement for certification schemes like FSC (Forest Stewardship Council), SBP (Sustainable Biomass Partnership), and PEFC (Programme for the Endorsement of Forest Certification) that allow mixing of certified and non-certified materials while maintaining accurate accounting of certified content percentages. This entity tracks material inputs, outputs, and balances across defined periods to ensure certification compliance and enable accurate sustainability claims.
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
<td>`accountId`
<td>string
<td>Yes
<td>Unique identifier for the mass balance account (primary key)
<td>`MBA-001`, `MBA-FSC-MILL-2024-Q1`
</tr>
<tr>
<td>`organizationId`
<td>string (FK)
<td>Yes
<td>Foreign key to organization maintaining the account
<td>`ORG-PACIFIC-MILL-001`, `ORG-BIOMASS-PROCESSOR`
</tr>
<tr>
<td>`productGroupId`
<td>string (FK)
<td>Yes
<td>Foreign key to product group being tracked
<td>`PG-LUMBER-PRODUCTS`, `PG-WOOD-CHIPS`, `PG-PULPWOOD`
</tr>
<tr>
<td>`periodInputs`
<td>number
<td>No
<td>Total certified material inputs during balancing period
<td>`15000.5`, `250000.0`, `75000.25`
</tr>
<tr>
<td>`periodOutputs`
<td>number
<td>No
<td>Total certified material outputs during balancing period
<td>`14750.0`, `245000.0`, `73500.0`
</tr>
<tr>
<td>`currentBalance`
<td>number
<td>Yes
<td>Current account balance of certified material credits
<td>`2500.0`, `-1500.0`, `8750.5`
</tr>
<tr>
<td>`balancingPeriod`
<td>string
<td>No
<td>Time period for mass balance accounting
<td>`2024-Q1`, `January 2024`, `2024-01-01 to 2024-03-31`
</tr>
<tr>
<td>`conversionFactors`
<td>number
<td>No
<td>Conversion factor for input/output calculations
<td>`0.85`, `1.0`, `0.92`, `1.15`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/mass-balance-account/MBA-001`
</tr>
</tbody>
</table>
### Mass Balance Principles
1. **Certification Scheme Compliance**
    - FSC Controlled Wood mass balance system
    - SBP biomass sustainability mass balance
    - PEFC Due Diligence System (DDS) tracking
    - Sustainable sourcing percentage calculations
2. **Material Flow Accounting**
    - Certified material inputs from suppliers
    - Non-certified material inputs identification
    - Processing efficiency and conversion rates
    - Output allocation to certified and non-certified products
3. **Balance Maintenance**
    - Credit accumulation from certified inputs
    - Debit allocation to certified output claims
    - Account balance monitoring and reconciliation
    - Compliance threshold management
4. **Periodic Reconciliation**
    - Regular accounting period closure
    - Physical inventory verification
    - Documentation and audit trail maintenance
    - Certification body reporting requirements
### Account Balance Management
1. **Positive Balance**
    - Surplus of certified material credits available
    - Ability to make certified content claims
    - Capacity for future certified product output
    - Compliance buffer for operational flexibility
2. **Negative Balance**
    - Deficit requiring corrective action
    - Temporary non-compliance status
    - Need for additional certified inputs
    - Potential suspension of certified claims
3. **Zero Balance**
    - Exact match between inputs and outputs
    - Optimal certification scheme compliance
    - Maximum utilization of certified materials
    - Efficient resource allocation
### Conversion Factors and Processing
1. **Volume-Based Conversions**
    - Green weight to dry weight conversions
    - Log volume to lumber volume yields
    - Bark inclusion and exclusion factors
    - Species-specific density adjustments
2. **Processing Efficiency**
    - Mill recovery rates and sawing efficiency
    - Biomass processing and densification
    - Energy conversion efficiency factors
    - Co-product allocation methodologies
3. **Quality Adjustments**
    - Grade recovery and quality sorting
    - Moisture content standardization
    - Size and dimensional standardization
    - Species composition accounting
### Balancing Period Management
1. **Quarterly Accounting**
    - Standard three-month accounting periods
    - Alignment with certification reporting cycles
    - Seasonal operation considerations
    - Cash flow and inventory optimization
2. **Monthly Reconciliation**
    - More frequent balance monitoring
    - Rapid identification of compliance issues
    - Improved inventory management
    - Enhanced operational control
3. **Annual Reporting**
    - Comprehensive yearly certification reporting
    - Long-term trend analysis and planning
    - Certification body annual assessments
    - Strategic sourcing planning
4. **Campaign-Based Accounting**
    - Project-specific mass balance tracking
    - Single-source material campaigns
    - Special product run accounting
    - Customer-specific certification requirements
### Certification Scheme Integration
1. **FSC (Forest Stewardship Council)**
    - FSC Mix products with percentage claims
    - Controlled Wood verification and accounting
    - Chain of custody maintenance requirements
    - Credit system and transfer mechanisms
2. **SBP (Sustainable Biomass Partnership)**
    - Supply base evaluation compliance
    - Regional risk assessment integration
    - Mass balance system requirements
    - Controlled feedstock accounting
3. **PEFC (Programme for the Endorsement of Forest Certification)**
    - Due Diligence System implementation
    - Controversial sources exclusion
    - Percentage-based claims support
    - Multi-site operation coordination
4. **Custom Certification Programs**
    - Company-specific sustainability programs
    - Regional certification scheme requirements
    - Customer-mandated tracking systems
    - Voluntary sustainability commitments
### Input and Output Tracking
1. **Certified Inputs**
    - FSC, PEFC, or SBP certified material receipts
    - Supplier certificate validation and verification
    - Volume and quality documentation
    - Species and origin verification
2. **Controlled Inputs**
    - Low-risk or controlled source materials
    - Due diligence verification completion
    - Risk assessment and mitigation documentation
    - Acceptable source verification
3. **Non-Certified Inputs**
    - Conventional material without certification
    - Unknown or unverified source materials
    - High-risk source identification
    - Segregation requirements
4. **Certified Outputs**
    - Products sold with certification claims
    - Certificate number and claim validation
    - Customer delivery documentation
    - Claim percentage calculation and verification
### Account Monitoring and Controls
1. **Real-Time Balance Tracking**
    - Continuous account balance monitoring
    - Automated alert systems for low balances
    - Proactive sourcing recommendations
    - Compliance risk management
2. **Audit Trail Documentation**
    - Complete transaction history maintenance
    - Supporting documentation archival
    - Certificate and claim verification records
    - Third-party audit preparation
3. **Exception Management**
    - Balance deficit identification and resolution
    - Sourcing adjustment and corrective actions
    - Certification body notification procedures
    - Customer communication protocols
### Example Use Cases
1. **FSC Mix Lumber Production**
    - Account: FSC Mix lumber mass balance
    - Inputs: 60% FSC certified logs, 40% controlled wood
    - Processing: 85% mill recovery rate conversion factor
    - Outputs: Lumber products with 60% FSC Mix claims
    - Balance: Positive balance allowing continued certified production
2. **SBP Biomass Processing**
    - Account: SBP compliant wood chip production
    - Inputs: 100% SBP-compliant feedstock from risk-assessed supply base
    - Processing: 1.0 conversion factor for chip production
    - Outputs: Wood chips with full SBP compliance claims
    - Balance: Maintained at optimal level for continuous operations
3. **Multi-Scheme Compliance**
    - Account: Combined FSC and PEFC mass balance system
    - Inputs: Mixed certified materials from multiple schemes
    - Processing: Product-specific conversion factors
    - Outputs: Segregated products with appropriate scheme claims
    - Balance: Separate accounting for each certification scheme
### Compliance Monitoring and Reporting
1. **Internal Controls**
    - Monthly balance reconciliation procedures
    - Quarterly compliance assessment reports
    - Annual management review processes
    - Continuous improvement identification
2. **External Reporting**
    - Certification body quarterly reports
    - Customer certification status updates
    - Regulatory compliance documentation
    - Third-party verification support
3. **Audit Preparation**
    - Complete documentation organization
    - Balance calculation verification
    - Supporting evidence compilation
    - Staff training and preparation
### Validation Rules
1. **Account Requirements**
    - accountId must be unique across system
    - organizationId must reference valid Organization
    - productGroupId must reference valid ProductGroup
    - currentBalance must be tracked continuously
2. **Balance Integrity**
    - periodInputs must be non-negative when provided
    - periodOutputs must be non-negative when provided
    - currentBalance calculation must be mathematically consistent
    - conversionFactors must be positive numbers when provided
3. **Period Management**
    - balancingPeriod must be clearly defined timeframe
    - Period inputs and outputs must align with specified timeframe
    - Account balance must be updated for each accounting period
    - Historical balances must be maintained for audit purposes
4. **Certification Compliance**
    - Account balance must not remain negative beyond certification limits
    - Input documentation must support balance calculations
    - Output claims must not exceed available certified content
    - Conversion factors must be verified and justified
### Relationships
- MassBalanceAccount managed by one Organization for operational control
- MassBalanceAccount tracks one ProductGroup for material categorization
- MassBalanceAccount enables Certificate compliance through accurate accounting
- MassBalanceAccount supports Transaction sustainability claims verification
- MassBalanceAccount integrates with SupplyBase risk assessment and material sourcing
