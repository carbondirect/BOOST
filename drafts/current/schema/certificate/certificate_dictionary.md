# Certificate Data Dictionary

## Overview
The `Certificate` object represents a formal record of certification issued by a certification body (cbId) to an organization under a specific certification scheme. It includes details about the scope, validity, and status of the certification, and supports JSON-LD for linked data compatibility. The primary key is `certificateNumber`.

## Fields
| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `@context` | object | No | JSON-LD context for semantic web compatibility. | `{"@vocab": "https://schema.org/"}` |
| `@type` | string | No | JSON-LD type identifier, constant: `Certificate`. | `Certificate` |
| `@id` | string (uri)| No | Unique URI identifier for the certificate. | `https://example.com/certificates/SFI-2025-12345` |
| `certificateId` | string | No | Optional internal identifier for the certificate. | `SFI-CERT-001` |
| `certificateNumber` | string | Yes | Official certificate number, serving as the primary key. | `SFI-2025-12345`, `FSC-C123456` |
| `certificationSchemeId`| string | Yes | Foreign key to the `CertificationScheme` entity. | `SFI-CoC`, `FSC-CoC` |
| `cbId` | string | Yes | Foreign key to the `CertificationBody` entity. | `SFI`, `FSC-US` |
| `organizationId` | string | Yes | Foreign key to the `Organization` receiving the certificate. | `ORG-FORESTCO-001` |
| `dateOfIssue` | string (date)| Yes | Date when the certificate was issued. | `2025-01-01` |
| `dateOfExpiry` | string (date)| Yes | Date when the certificate expires. | `2030-01-01` |
| `status` | string | Yes | Current status of the certificate. Enum: `active`, `expired`, `revoked`, `suspended`, `pending`. | `active` |
| `scopeOfCertification`| string | Yes | A summary of what the certification covers. | `Chain of Custody for lumber and pulp` |
| `versionNumber` | string | Yes | The version of the standard under which the certificate was issued. | `2022`, `FSC-STD-40-004 v3-1` |
| `productGroups` | array | No | A list of product groups covered by the certificate. | See details below. |
| `volumeTrackingRecord`| object | No | Records of input and output volumes by category. | See details below. |
| `labelUseRecord` | array | No | A record of how and when certified labels are used. | See details below. |
| `supplierInfo` | object | No | Information about the supplier. | See details below. |
| `supplierRiskRatingDDS`| object | No | Due Diligence System risk rating for the supplier. | See details below. |
| `attachments` | array | No | A list of attached files related to the certificate. | See details below. |
| `lastUpdated` | string (date-time)| No | Timestamp of the last update to the record. | `2025-07-01T14:30:00Z` |
| `conditionalRequirements`| array | No | Any special conditions or requirements for the certificate. | See details below. |
| `suspensionHistory` | array | No | A history of any suspensions of the certificate. | See details below. |
| `auditSchedule` | object | No | Information about scheduled audits. | See details below. |
| `certificateDocument` | string (uri)| No | A link to the official certificate document. | `https://sfiprogram.org/certificates/2025-12345.pdf` |

---

## Detailed Field Descriptions

### `productGroups`
An array of objects, each defining a product group covered by the certification.
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `productType` | string | Yes | The type of product. |
| `materialCategories`| array | No | Categories of material associated with the product type. |
| `controlSystems` | array | No | Control systems applied to this product group. |

### `volumeTrackingRecord`
An object for tracking input and output volumes.
| Field | Type | Description |
|-------|------|-------------|
| `inputVolumeByCategory`| object | Key-value pairs of input categories and their volumes. |
| `outputVolumeByCategory`| object | Key-value pairs of output categories and their volumes. |

### `labelUseRecord`
An array of objects recording the use of certified labels.
| Field | Type | Description |
|-------|------|-------------|
| `product` | string | The product on which the label was used. |
| `claimType` | string | The type of claim made (e.g., FSC Mix, 100% Recycled). |
| `approvalReference`| string | Reference to the approval for using the label. |

### `supplierInfo`
An object containing supplier information.
| Field | Type | Description |
|-------|------|-------------|
| `name` | string | The name of the supplier. |
| `address`| string | The address of the supplier. |

### `supplierRiskRatingDDS`
An object for the supplier's Due Diligence System risk rating.
| Field | Type | Description |
|-------|------|-------------|
| `riskRating`| string | The assigned risk rating. |
| `mitigationMeasures` | string | Measures taken to mitigate the identified risk. |

### `attachments`
An array of objects representing attached files.
| Field | Type | Description |
|-------|------|-------------|
| `fileName`| string | The name of the attached file. |
| `fileUrl` | string (uri)| The URL where the file can be accessed. |
| `fileType`| string | The type of the file (e.g., 'pdf', 'jpg'). |

### `conditionalRequirements`
An array of objects, each specifying a condition for the certificate.
| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Type of requirement (e.g., `surveillance`, `corrective-action`). |
| `description`| string | A description of the requirement. |
| `dueDate` | string (date)| The due date for fulfilling the requirement. |

### `suspensionHistory`
An array of objects, each recording a suspension event.
| Field | Type | Description |
|-------|------|-------------|
| `date` | string (date)| The date the suspension occurred. |
| `reason` | string | The reason for the suspension. |
| `restoredDate`| string (date)| The date the certificate was restored, if applicable. |

### `auditSchedule`
An object describing the schedule for the next audit.
| Field | Type | Description |
|-------|------|-------------|
| `nextAudit` | string (date)| The date of the next scheduled audit. |
| `type` | string | The type of audit (e.g., `initial`, `surveillance`, `recertification`). |
| `auditorId` | string | The ID of the assigned auditor. |

---

## Relationships

### Parent Entities
- **CertificationScheme** (`certificationSchemeId`) - The standard or program under which certification was issued.
- **CertificationBody** (`cbId`) - The independent organization that issued the certificate.
- **Organization** (`organizationId`) - The entity that received the certificate.

### Child Entities
- **Claim** - Claims can reference certificates as validation.
- **VerificationStatement** - May reference certificates for third-party validation.

## Business Rules

1. **Certificate Number Uniqueness**: `certificateNumber` must be unique across all certificates.
2. **Date Validation**: `dateOfExpiry` must be after `dateOfIssue`.
3. **Status Consistency**: Status must reflect current validity based on dates and conditions.
4. **Scheme Alignment**: Certificate scope must align with the capabilities of the certification scheme.
5. **Organization Eligibility**: Only organizations meeting scheme requirements can receive certificates.

## Common Queries

- Find all active certificates for an organization.
- List certificates expiring within a date range.
- Validate certificate status for claim verification.
- Generate certificate renewal notifications.
- Track certification body performance metrics.

## Integration Points

- **Supply Chain Validation**: Certificates validate sustainability claims in transactions.
- **Compliance Reporting**: Required for regulatory compliance in various jurisdictions.
- **Third-party Verification**: Referenced in verification statements and audit reports.
- **Mass Balance Accounting**: Certificates enable certified material tracking.