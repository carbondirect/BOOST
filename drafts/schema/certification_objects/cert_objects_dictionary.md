# Data Dictionary

## Certificate

### Overview
The `Certificate` object represents a formal record of certification issued by a certification body (cbId) to an organization under a specific certification scheme. The primary key is `certificateNumber`.

### Fields
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
| `productGroups` | array<object> | No | List of covered products | See Product Group Object |
| `volumeTrackingRecord` | object | No | Input/output tracking by category | See Volume Tracking Object |
| `labelUseRecord` | array<object> | No | On/off-product label usage | See Label Use Object |
| `supplierInfo` | object | No | Name and address of primary supplier | — |
| `supplierRiskRatingDDS` | object | No | DDS rating and mitigation info | — |
| `attachments` | array<object> | No | Linked documents | See Attachment Object |
| `lastUpdated` | string (date-time) | No | Timestamp of last schema update | `2025-06-24T10:00:00Z` |

#### Product Group Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `productType` | string | Yes | Product category (e.g., lumber) |
| `materialCategories` | array<string> | No | SFI-recognized categories | `Certified Forest Content` |
| `controlSystems` | array<string> | No | Accounting methods | `mass balance` |

#### Volume Tracking Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `inputVolumeByCategory` | object | No | Input volume keyed by material category |
| `outputVolumeByCategory` | object | No | Output volume keyed by material category |

#### Label Use Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `product` | string | Yes | Product name using the label |
| `claimType` | string | Yes | Label claim classification |
| `approvalReference` | string | Yes | Link to approval metadata |

#### Attachment Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fileName` | string | Yes | Document name |
| `fileUrl` | string (uri) | Yes | Downloadable link |
| `fileType` | string | No | MIME type |

---

## Certification Body

### Overview
The `Certification Body` object captures the organization that governs and manages certification schemes (e.g., SFI Inc.).

### Fields
| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `cbId` | string | Yes | Unique identifier | `SFI` |
| `cbName` | string | Yes | Full legal name | `Sustainable Forestry Initiative` |
| `accreditationStatus` | string | No | Accreditation status | `accredited` |
| `accreditationScope` | string | No | Scope of accreditation | `Forestry and Chain of Custody` |
| `contactInformation` | object | Yes | Contact and website details | See Contact Info Object |
| `jurisdictions` | array<string> | No | Countries or regions covered | `USA`, `Canada` |
| `sectorsServed` | array<string> | No | Focus sectors | `Forestry`, `Pulp & Paper` |
| `isActive` | boolean | No | Status flag | `true` |
| `lastUpdated` | string (date-time) | No | Record update timestamp | `2025-06-24T09:00:00Z` |

#### Contact Info Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `address` | object | Yes | See Address Object |
| `email` | string | No | Email contact |
| `phone` | string | No | Phone number |
| `website` | string (uri) | No | Web link to certifier site |

##### Address Object
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `street` | string | No | Physical street address |
| `city` | string | Yes | City location |
| `state` | string | No | State or province |
| `postalCode` | string | No | Postal or zip code |
| `country` | string | Yes | Country |

---

## Certification Scheme

### Overview
The `Certification Scheme` object represents the standard or framework used to certify organizations, including rules and criteria (e.g., SFI Chain of Custody).

### Fields
| Field | Type | Required | Description | Examples |
|-------|------|----------|-------------|----------|
| `schemeId` | string | Yes | Unique scheme identifier | `SFI-CoC` |
| `schemeName` | string | Yes | Full name of the scheme | `SFI Chain of Custody` |
| `versionNumber` | string | Yes | Version of the standard | `2022` |
| `recognitionStatus` | string | Yes | Status or tier | `internationally-recognized` |
| `description` | string | No | Scheme summary | — |
| `website` | string (uri) | No | URL for scheme homepage | — |
| `materialCategories` | array<string> | No | Allowable categories | `Certified Forest Content` |
| `controlSystems` | array<string> | No | Accounting approaches | `transfer`, `credit` |
| `labelUseRequirements` | string | No | Narrative guidance on labels | — |
| `volumeTrackingRequirements` | string | No | Rules for material accounting | — |
| `dueDiligenceRequirements` | string | No | Risk-based procurement and controls | — |
| `sustainabilityCriteria` | array<string> | No | Principles defined by the scheme | — |
| `applicableRegions` | array<string> | No | Jurisdictional boundaries | — |
| `dateEstablished` | string (date) | No | Launch date of scheme | `1995-01-01` |
| `lastUpdated` | string (date-time) | No | Most recent update | `2025-06-24T09:00:00Z` |
