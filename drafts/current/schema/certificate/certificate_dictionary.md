# Certificate

## Overview
The `Certificate` object represents a formal record of certification issued by a certification body (cbId) to an organization under a specific certification scheme. The primary key is `certificateNumber`.

## Fields
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
<td>`certificateId`
<td>string
<td>No
<td>Optional internal identifier
<td>`SFI-CERT-001`
</tr>
<tr>
<td>`certificateNumber`
<td>string
<td>Yes
<td>Official certificate number (primary key)
<td>`SFI-2025-12345`
</tr>
<tr>
<td>`certificationSchemeId`
<td>string
<td>Yes
<td>FK to Certification Scheme
<td>`SFI-CoC`
</tr>
<tr>
<td>`cbId`
<td>string
<td>Yes
<td>FK to Certification Body
<td>`SFI`
</tr>
<tr>
<td>`organizationId`
<td>string
<td>Yes
<td>FK to Organization receiving the certificate
<td>`ORG-FORESTCO-001`
</tr>
<tr>
<td>`dateOfIssue`
<td>string (date)
<td>Yes
<td>Date of issuance
<td>`2025-01-01`
</tr>
<tr>
<td>`dateOfExpiry`
<td>string (date)
<td>Yes
<td>Expiry date
<td>`2030-01-01`
</tr>
<tr>
<td>`status`
<td>string
<td>Yes
<td>Current certificate status
<td>`active`, `expired`, `revoked`, etc.
</tr>
<tr>
<td>`scopeOfCertification`
<td>string
<td>Yes
<td>Summary of certification coverage
<td>`Chain of Custody for lumber and pulp`
</tr>
<tr>
<td>`versionNumber`
<td>string
<td>Yes
<td>Version of standard applied
<td>`2022`
</tr>
<tr>
<td>`conditionalRequirements`
<td>array
<td>No
<td>Special conditions or requirements
<td>`[{"type": "surveillance", "frequency": "annual"}]`
</tr>
<tr>
<td>`suspensionHistory`
<td>array
<td>No
<td>History of suspensions
<td>`[{"date": "2023-06-01", "reason": "non-compliance"}]`
</tr>
<tr>
<td>`auditSchedule`
<td>object
<td>No
<td>Scheduled audit information
<td>`{"nextAudit": "2025-12-01", "type": "surveillance"}`
</tr>
<tr>
<td>`certificateDocument`
<td>string
<td>No
<td>Link or reference to certificate document
<td>`https://sfiprogram.org/certificates/2025-12345.pdf`
</tr>
</tbody>
</table>
## Relationships

### Parent Entities
- **CertificationScheme** (`certificationSchemeId`) - The standard or program under which certification was issued
- **CertificationBody** (`cbId`) - The independent organization that issued the certificate
- **Organization** (`organizationId`) - The entity that received the certificate

### Child Entities
- **Claim** - Claims can reference certificates as validation
- **VerificationStatement** - May reference certificates for third-party validation

## Business Rules

1. **Certificate Number Uniqueness**: `certificateNumber` must be unique across all certificates
2. **Date Validation**: `dateOfExpiry` must be after `dateOfIssue`
3. **Status Consistency**: Status must reflect current validity based on dates and conditions
4. **Scheme Alignment**: Certificate scope must align with the capabilities of the certification scheme
5. **Organization Eligibility**: Only organizations meeting scheme requirements can receive certificates

## Common Queries

- Find all active certificates for an organization
- List certificates expiring within a date range
- Validate certificate status for claim verification
- Generate certificate renewal notifications
- Track certification body performance metrics

## Integration Points

- **Supply Chain Validation**: Certificates validate sustainability claims in transactions
- **Compliance Reporting**: Required for regulatory compliance in various jurisdictions
- **Third-party Verification**: Referenced in verification statements and audit reports
- **Mass Balance Accounting**: Certificates enable certified material tracking