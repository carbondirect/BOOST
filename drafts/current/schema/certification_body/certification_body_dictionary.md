# Certification Body Data Dictionary

## Overview
The `CertificationBody` object represents an independent organization authorized to issue certificates under specific certification schemes. It includes details about their accreditation, operational scope, and contact information, and supports JSON-LD for linked data compatibility. The primary key is `cbId`.

## Fields
| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `@context` | object | No | JSON-LD context for semantic web compatibility. | `{"@vocab": "https://schema.org/"}` |
| `@type` | string | No | JSON-LD type identifier, constant: `CertificationBody`. | `CertificationBody` |
| `@id` | string (uri)| No | Unique URI identifier for the certification body. | `https://example.com/cbs/SFI` |
| `cbId` | string | Yes | Unique identifier for the certification body (primary key). | `SFI`, `FSC-US`, `PEFC-001` |
| `cbName` | string | Yes | Official name of the certification body. | `Sustainable Forestry Initiative` |
| `cbType` | string | Yes | Type or category of certification body. Enum: `scheme-owner`, `third-party`, `accredited-body`, `regulatory-body`. | `scheme-owner` |
| `accreditationStatus`| string | Yes | Current accreditation status. Enum: `active`, `suspended`, `expired`, `pending`, `revoked`. | `active` |
| `accreditationScope` | string | No | The scope of the certification body's accreditation. | `Forestry and Chain of Custody` |
| `authorizedSchemes`| array | Yes | A list of certification schemes the CB is authorized to certify under. | `["SFI-CoC", "SFI-FM"]` |
| `contactInformation` | object | Yes | Contact details for the certification body. | See details below. |
| `operationalRegions` | array | Yes | Geographic regions where the CB operates (ISO country codes). | `["US", "CA", "MX"]` |
| `jurisdictions` | array | No | A list of legal jurisdictions where the CB operates. | `["California", "Oregon"]` |
| `sectorsServed` | array | No | The industry sectors served by the CB. | `["Pulp & Paper", "Lumber"]` |
| `isActive` | boolean | No | A flag indicating if the certification body is currently active. | `true` |
| `lastUpdated` | string (date-time)| No | Timestamp of the last update to the record. | `2025-07-01T14:30:00Z` |
| `accreditationBody`| string | No | The organization that accredited this certification body. | `ANSI-ASQ National Accreditation Board` |
| `validityPeriod` | object | Yes | The period of the certification body's authorization. | See details below. |
| `specializations` | array | No | Areas of special expertise for the CB. | `["forestry", "chain-of-custody"]` |
| `performanceMetrics` | object | No | Key performance indicators for the CB. | See details below. |

---

## Detailed Field Descriptions

### `contactInformation`
An object containing contact details for the certification body.
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | string (email)| Yes | The primary email address. |
| `phone` | string | No | The primary phone number. |
| `address`| object | No | The physical address of the CB. |
| `website`| string (uri)| No | The official website of the CB. |

The `address` object has the following structure:
| Field | Type |
|-------|------|
| `street`| string |
| `city` | string |
| `state` | string |
| `postalCode`| string |
| `country`| string |

### `validityPeriod`
An object defining the period of authorization for the certification body.
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `start` | string (date)| Yes | The start date of the authorization. |
| `end` | string (date)| Yes | The end date of the authorization. |

### `performanceMetrics`
An object containing performance and quality indicators for the CB.
| Field | Type | Description |
|-------|------|-------------|
| `certificatesIssued` | integer | The number of certificates issued by the CB. |
| `averageAuditDuration`| number | The average duration of audits conducted by the CB. |
| `customerSatisfactionScore`| number | A score representing customer satisfaction (e.g., 1-5). |

---

## Relationships

### Parent Entities
- **AccreditationBody** (external) - Organization that provides accreditation oversight.

### Child Entities
- **Certificate** - Certificates issued by this certification body.
- **VerificationStatement** - Verification statements issued by this body.
- **Audit** - Audits conducted by this certification body.

## Business Rules

1. **Unique Identification**: `cbId` must be unique across all certification bodies.
2. **Scheme Authorization**: CB can only issue certificates for schemes in `authorizedSchemes`.
3. **Regional Compliance**: CB must operate within authorized `operationalRegions`.
4. **Accreditation Requirements**: Must maintain valid accreditation status.
5. **Validity Period**: Cannot issue certificates outside `validityPeriod`.

## Common Queries

- Find certification bodies authorized for specific schemes.
- List CBs operating in specific regions.
- Validate CB authorization for certificate issuance.
- Monitor accreditation status and renewal dates.
- Generate CB performance and compliance reports.