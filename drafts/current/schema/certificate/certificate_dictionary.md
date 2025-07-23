# Certificate Data Dictionary

## Overview
The `Certificate` object represents a formal record of certification issued by a certification body (cbId) to an organization under a specific certification scheme. The primary key is `certificateNumber`.

## Fields
| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `certificateId` | string | No | Optional internal identifier | `SFI-CERT-001` |
| `certificateNumber` | string | Yes | Official certificate number (primary key) | `SFI-2025-12345` |
| `certificationSchemeId` | string | Yes | FK to Certification Scheme | `SFI-CoC` |
| `cbId` | string | Yes | FK to Certification Body | `SFI` |
| `organizationId` | string | Yes | FK to Organization receiving the certificate | `ORG-FORESTCO-001` |
| `dateOfIssue` | string (date) | Yes | Date of issuance | `2025-01-01` |
| `dateOfExpiry` | string (date) | Yes | Expiry date | `2030-01-01` |
| `status` | string | Yes | Current certificate status | `active`, `expired`, `revoked`, etc. |
| `scopeOfCertification` | string | Yes | Summary of certification coverage | `Chain of Custody for lumber and pulp` |
| `versionNumber` | string | Yes | Version of standard applied | `2022` |
| `conditionalRequirements` | array | No | Special conditions or requirements | `[{"type": "surveillance", "frequency": "annual"}]` |
| `suspensionHistory` | array | No | History of suspensions | `[{"date": "2023-06-01", "reason": "non-compliance"}]` |
| `auditSchedule` | object | No | Scheduled audit information | `{"nextAudit": "2025-12-01", "type": "surveillance"}` |
| `certificateDocument` | string | No | Link or reference to certificate document | `https://sfiprogram.org/certificates/2025-12345.pdf` |

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