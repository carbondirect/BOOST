<!-- Auto-generated from audit/validation_schema.json -->

Audit entity in BOOST data model

**[View Audit in ERD Navigator](erd-navigator/index.html?focus=Audit)**

### Relationships ### {{.unnumbered}}

- **organizationId** → [[#organization|Organization]]

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
<td>enum(Audit)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>auditDate</code>
<td>string (date)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>auditId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>auditType</code>
<td>enum(Initial, Surveillance, Transfer)
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
<td><code>auditGeographicDataId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
<tr>
<td><code>cbId</code>
<td>string (pattern)
<td>No description provided
<td>
</tr>
<tr>
<td><code>findings</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>reportUrl</code>
<td>string (uri)
<td>No description provided
<td>
</tr>
</tbody>
</table>

## Audit
### Overview
The `Audit` entity tracks certification audits and compliance verification activities within the BOOST traceability system. Audits are conducted by certification bodies to verify that organizations meet sustainability standards, maintain proper chain of custody procedures, and comply with certification scheme requirements. This entity supports audit trail management, compliance verification, and certification maintenance tracking.
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
<td>`auditId`
<td>string
<td>Yes
<td>Unique identifier for the audit (primary key)
<td>`AUDIT-001`, `AUDIT-FSC-PACIFIC-2024-01`
</tr>
<tr>
<td>`auditType`
<td>string
<td>Yes
<td>Type of audit being conducted (enum)
<td>`Initial`, `Surveillance`, `Transfer`
</tr>
<tr>
<td>`auditDate`
<td>string (date)
<td>Yes
<td>Date when the audit was conducted
<td>`2024-03-15`, `2024-07-22`
</tr>
<tr>
<td>`organizationId`
<td>string (FK)
<td>Yes
<td>Foreign key to organization being audited
<td>`ORG-PACIFIC-FOREST-001`, `ORG-KLAMATH-HARVEST`
</tr>
<tr>
<td>`cbId`
<td>string (FK)
<td>No
<td>Foreign key to certification body conducting audit
<td>`SFI`, `FSC-US`, `PEFC-001`
</tr>
<tr>
<td>`findings`
<td>string
<td>No
<td>Summary of audit findings and recommendations
<td>`No major non-conformities found`, `Minor issues with record keeping resolved`
</tr>
<tr>
<td>`reportUrl`
<td>string (uri)
<td>No
<td>URL link to detailed audit report
<td>`https://audit-reports.example.com/AUDIT-FSC-001.pdf`
</tr>
<tr>
<td>`auditGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where audit was conducted
<td>`GEO-MILL-PACIFIC-001`, `GEO-OFFICE-KLAMATH`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/audit/AUDIT-001`
</tr>
</tbody>
</table>
### Audit Types
1. **Initial**
    - First-time certification audit for new certificate applicants
    - Comprehensive assessment of all certification requirements
    - Establishes baseline compliance and capability assessment
    - Results in initial certificate issuance or rejection
    - Typically requires 6-12 months preparation period
2. **Surveillance**
    - Ongoing monitoring audits for existing certificate holders
    - Annual or periodic verification of continued compliance
    - Focused review of key processes and risk areas
    - Maintains certificate validity and identifies improvements
    - Less comprehensive than initial audits
3. **Transfer**
    - Audit conducted when changing certification bodies
    - Verification of records and compliance history transfer
    - Ensures continuity of certification without gaps
    - Review of previous audit findings and corrective actions
    - Required for seamless certificate transfer
### Key Features
1. **Compliance Verification**
    - Systematic verification of certification scheme requirements
    - Documentation review and process assessment
    - Staff interviews and competency evaluation
    - Physical inspection of facilities and operations
2. **Audit Trail Management**
    - Complete audit history tracking for organizations
    - Corrective action follow-up and closure verification
    - Continuous improvement monitoring and progress tracking
    - Certificate maintenance and renewal timeline management
3. **Multi-Standard Support**
    - FSC (Forest Stewardship Council) audit management
    - SFI (Sustainable Forestry Initiative) compliance verification
    - PEFC (Programme for the Endorsement of Forest Certification) auditing
    - SBP (Sustainable Biomass Partnership) assessment support
4. **Geographic Integration**
    - Multi-site audit coordination and planning
    - Location-specific compliance assessment
    - Regional regulation and standard adaptation
    - Travel and logistics optimization for audit teams
### Audit Process Workflow
1. **Pre-Audit Phase**
    - Audit scheduling and scope definition
    - Document review and preparation
    - Stakeholder notification and coordination
    - Resource allocation and team assignment
2. **Audit Execution**
    - Opening meeting and scope confirmation
    - Document review and record examination
    - Process observation and staff interviews
    - Facility inspection and equipment verification
3. **Post-Audit Activities**
    - Finding documentation and classification
    - Corrective action plan development
    - Report preparation and review
    - Certificate decision and issuance
### Finding Classifications
1. **Conformity**
    - Full compliance with certification requirements
    - No corrective actions required
    - Positive findings supporting certificate maintenance
    - Best practice examples for improvement
2. **Minor Non-Conformity**
    - Small deviations from requirements
    - Corrective action required within defined timeframe
    - Certificate maintained with monitoring
    - Follow-up verification in next surveillance audit
3. **Major Non-Conformity**
    - Significant failure to meet requirements
    - Immediate corrective action required
    - Certificate suspension or withdrawal risk
    - Additional audit required to verify corrections
### Example Use Cases
1. **FSC Chain of Custody Initial Audit**
    - Audit Type: Initial
    - Organization: New sawmill seeking FSC certification
    - Scope: Complete chain of custody system assessment
    - Duration: 2-3 days including forest operations review
    - Outcome: Certificate issuance with minor corrective actions
2. **SFI Surveillance Audit**
    - Audit Type: Surveillance
    - Organization: Existing certified logging contractor
    - Scope: Annual compliance monitoring
    - Duration: 1 day focused on high-risk areas
    - Outcome: Continued certificate validity confirmed
3. **Multi-Site Transfer Audit**
    - Audit Type: Transfer
    - Organization: Integrated forest products company
    - Scope: Multiple facilities across different states
    - Duration: 5 days with coordinated audit team
    - Outcome: Successful certificate transfer to new certification body
### Validation Rules
1. **Audit Requirements**
    - auditId must be unique across system
    - auditType must be valid enumerated value
    - auditDate must be valid date format
    - organizationId must reference valid Organization
2. **Relationship Consistency**
    - cbId must reference valid CertificationBody if provided
    - auditGeographicDataId must reference valid GeographicData location
    - Organization must have active or pending certification status
3. **Audit Logic**
    - Initial audits must precede Surveillance audits for same organization
    - Transfer audits require existing certificate from different certification body
    - Audit findings must be consistent with audit type and scope
### Relationships
- Audit conducted on one Organization by audit team
- Audit performed by one CertificationBody (when specified)
- Audit conducted at one or more GeographicData locations
- Audit findings support Certificate issuance and maintenance decisions
- Audit history enables continuous improvement and compliance tracking
