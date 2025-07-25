# Certification Body Data Dictionary

## Overview
The `CertificationBody` object represents an independent organization authorized to issue certificates under specific certification schemes. The primary key is `cbId`.

## Fields
| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `cbId` | string | Yes | Unique identifier for the certification body (primary key) | `SFI`, `FSC-US`, `PEFC-001` |
| `cbName` | string | Yes | Official name of the certification body | `Sustainable Forestry Initiative` |
| `cbType` | string | Yes | Type or category of certification body | `scheme-owner`, `third-party`, `accredited-body` |
| `accreditationStatus` | string | Yes | Current accreditation status | `active`, `suspended`, `expired` |
| `authorizedSchemes` | array | Yes | List of schemes the CB can certify under | `["SFI-CoC", "SFI-FM"]` |
| `contactInformation` | object | Yes | Contact details | `{"email": "certs@sfiprogram.org", "phone": "+1-202-555-0100"}` |
| `operationalRegions` | array | Yes | Geographic regions where CB operates | `["US", "CA", "MX"]` |
| `accreditationBody` | string | No | Organization that accredited this CB | `ANSI-ASQ National Accreditation Board` |
| `validityPeriod` | object | Yes | Period of CB authorization | `{"start": "2020-01-01", "end": "2025-12-31"}` |

## Relationships

### Parent Entities
- **AccreditationBody** (external) - Organization that provides accreditation oversight

### Child Entities
- **Certificate** - Certificates issued by this certification body
- **VerificationStatement** - Verification statements issued by this body
- **Audit** - Audits conducted by this certification body

## Business Rules

1. **Unique Identification**: `cbId` must be unique across all certification bodies
2. **Scheme Authorization**: CB can only issue certificates for schemes in `authorizedSchemes`
3. **Regional Compliance**: CB must operate within authorized `operationalRegions`
4. **Accreditation Requirements**: Must maintain valid accreditation status
5. **Validity Period**: Cannot issue certificates outside `validityPeriod`

## Common Queries

- Find certification bodies authorized for specific schemes
- List CBs operating in specific regions
- Validate CB authorization for certificate issuance
- Monitor accreditation status and renewal dates
- Generate CB performance and compliance reports