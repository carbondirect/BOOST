<!-- AUTO-GENERATED - DO NOT EDIT
     Generated from: verification_statement/validation_schema.json and verification_statement_dictionary.md
     To modify this content, edit the source file and regenerate -->

VerificationStatement entity in BOOST data model

**[View Verification Statement in ERD Navigator](erd-navigator/index.html?focus=VerificationStatement)**

### Relationships ### {{.unnumbered}}

- **transactionBatchId** → [[#transaction-batch|Transaction Batch]]

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
<td>enum(VerificationStatement)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>issuingBody</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>statementId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>verificationDate</code>
<td>string (date)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>scope</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>transactionBatchId</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## VerificationStatement
### Overview
The `VerificationStatement` entity manages third-party verification statements for certification compliance within the BOOST traceability system. Verification statements are formal declarations issued by authorized certification bodies confirming that materials, processes, or transactions meet specific sustainability standards. This entity supports audit trails, compliance verification, and certification maintenance across supply chain operations.
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
<td>`statementId`
<td>string
<td>Yes
<td>Unique identifier for the verification statement (primary key)
<td>`VS-001`, `VS-FSC-PACIFIC-2024-001`
</tr>
<tr>
<td>`verificationDate`
<td>string (date)
<td>Yes
<td>Date when the verification was completed
<td>`2024-03-15`, `2024-07-22`
</tr>
<tr>
<td>`issuingBody`
<td>string
<td>Yes
<td>Name of the certification body issuing the statement
<td>`FSC United States`, `SFI Inc.`, `PEFC Council`
</tr>
<tr>
<td>`scope`
<td>string
<td>No
<td>Scope and coverage of the verification statement
<td>`Chain of custody for Douglas Fir sawlogs`, `SBP biomass sustainability verification`
</tr>
<tr>
<td>`transactionBatchId`
<td>string (FK)
<td>No
<td>Foreign key to transaction batch being verified
<td>`TXN-BATCH-PACIFIC-2024-Q1`, `TXN-BATCH-BIOMASS-001`
</tr>
<tr>
<td>`verificationResult`
<td>string
<td>No
<td>Result of the verification process (enum)
<td>`compliant`, `non_compliant`, `conditional_compliance`
</tr>
<tr>
<td>`certificationSchemeId`
<td>string (FK)
<td>No
<td>Foreign key to certification scheme being verified
<td>`CERT-SCHEME-FSC-001`, `CERT-SCHEME-SBP`
</tr>
<tr>
<td>`validityPeriod`
<td>string
<td>No
<td>Period for which the verification statement is valid
<td>`12 months`, `2024-01-01 to 2024-12-31`, `Until next audit`
</tr>
<tr>
<td>`verificationDetails`
<td>string
<td>No
<td>Detailed findings and verification methodology
<td>`FSC Mix 70% verified through complete chain of custody review`, `All SBP requirements met`
</tr>
<tr>
<td>`documentUrl`
<td>string (uri)
<td>No
<td>URL link to complete verification statement document
<td>`https://certificates.fsc.org/statements/VS-FSC-001.pdf`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/verification-statement/VS-001`
</tr>
</tbody>
</table>
### Verification Types
1. **Chain of Custody Verification**
    - Verifies material flow and custody transfers
    - Confirms segregation and mixing calculations
    - Validates certificate claims and percentages
    - Ensures proper documentation and record keeping
2. **Sustainability Compliance Verification**
    - Confirms adherence to sustainability standards
    - Validates environmental and social criteria
    - Verifies supply base assessments and risk evaluations
    - Ensures compliance with regulatory requirements
3. **Product Specification Verification**
    - Confirms product meets specified requirements
    - Validates quality grades and technical specifications
    - Verifies species composition and processing methods
    - Ensures delivery compliance with contract terms
4. **Transaction Verification**
    - Verifies transaction completeness and accuracy
    - Confirms payment and delivery terms compliance
    - Validates regulatory reporting requirements
    - Ensures proper documentation and record keeping
### Verification Results
1. **compliant**
    - Full compliance with all verification criteria
    - No corrective actions required
    - Statement validates claims and certifications
    - Materials approved for use with specified claims
2. **non_compliant**
    - Failure to meet verification criteria
    - Corrective actions required before approval
    - Claims cannot be supported by evidence
    - Materials may require reclassification or rejection
3. **conditional_compliance**
    - Partial compliance with minor deficiencies
    - Specific conditions must be met for full compliance
    - Limited approval with restrictions
    - Follow-up verification required
### Key Features
1. **Third-Party Validation**
    - Independent verification by accredited bodies
    - Objective assessment of compliance claims
    - Professional auditor expertise and credentials
    - Impartial evaluation of evidence and documentation
2. **Multi-Standard Support**
    - FSC (Forest Stewardship Council) verification
    - SFI (Sustainable Forestry Initiative) validation
    - PEFC (Programme for the Endorsement of Forest Certification)
    - SBP (Sustainable Biomass Partnership) assessment
3. **Transaction Integration**
    - Batch-level verification for grouped transactions
    - Supply chain verification across multiple parties
    - Integration with transaction processing workflows
    - Support for complex multi-party transactions
4. **Documentation Management**
    - Complete verification statement archival
    - Document version control and access management
    - Integration with certificate management systems
    - Audit trail and compliance history tracking
### Certification Body Integration
1. **FSC United States**
    - Chain of custody verification services
    - Forest management standard compliance
    - Controlled wood verification programs
    - Multi-site and group certification support
2. **SFI Inc.**
    - Fiber sourcing verification programs
    - Chain of custody standard compliance
    - Procurement standard verification
    - Logger and landowner education validation
3. **PEFC Council**
    - International certification scheme recognition
    - National scheme compliance verification
    - Chain of custody program validation
    - Due diligence system verification
4. **SBP Approved Certification Bodies**
    - Biomass sustainability verification
    - Supply base evaluation compliance
    - Regional risk assessment validation
    - Mass balance system verification
### Example Use Cases
1. **FSC Chain of Custody Verification**
    - Verification Statement: FSC Mix 75% for lumber shipment
    - Issuing Body: FSC-accredited certification body
    - Scope: Complete supply chain from forest to mill
    - Result: Compliant with all FSC standards
    - Validity: 12 months from issuance date
2. **SBP Biomass Sustainability Verification**
    - Verification Statement: SBP-compliant biomass fuel
    - Issuing Body: SBP-approved certification body
    - Scope: Supply base evaluation and mass balance verification
    - Result: Conditional compliance pending risk mitigation
    - Validity: Until next surveillance audit
3. **Multi-Standard Transaction Verification**
    - Verification Statement: Combined FSC and PEFC materials
    - Issuing Body: Mutually recognized certification body
    - Scope: Complex transaction with multiple certification claims
    - Result: Compliant with segregation requirements
    - Validity: Transaction-specific validity period
### Validation Rules
1. **Statement Requirements**
    - statementId must be unique across system
    - verificationDate must be valid date format
    - issuingBody must be authorized certification body
    - Verification scope must be clearly defined
2. **Certification Body Authority**
    - issuingBody must be accredited for verification scope
    - Certification scheme must be within body's authority
    - Verification methods must follow approved procedures
    - Statement must be within body's geographic scope
3. **Transaction Integration**
    - transactionBatchId must reference valid TransactionBatch
    - Verification scope must cover transaction materials
    - Verification date must be appropriate for transaction timeline
    - Statement validity must cover transaction period
### Relationships
- VerificationStatement issued by one CertificationBody
- VerificationStatement verifies one TransactionBatch
- VerificationStatement validates compliance with CertificationScheme requirements
- VerificationStatement supports Certificate maintenance and renewal
- VerificationStatement enables third-party validation of sustainability claims
