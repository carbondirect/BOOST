The Certificate entity represents a formal record of certification issued by a certification body to an organization under a specific certification scheme. This entity provides the foundation for tracking all sustainability certifications throughout the BOOST supply chain, including FSC, SFI, PEFC, and other certification systems.

## Required Fields

All Certificate implementations MUST include the following required fields:

- **`certificateNumber`** (string) - Official certificate number (primary key)  
    Examples: `SFI-2025-12345`, `FSC-COC-12345`, `PEFC-2024-67890`

- **`certificationSchemeId`** (string, foreign key) - Reference to CertificationScheme entity  
    Examples: `SFI-CoC`, `FSC-Chain-of-Custody`, `PEFC-CoC`

- **`cbId`** (string, foreign key) - Reference to issuing Certification Body  
    Examples: `SFI`, `FSC-US`, `PEFC-COUNCIL`

- **`organizationId`** (string, foreign key) - Reference to Organization receiving certificate  
    Examples: `ORG-FORESTCO-001`, `ORG-MILL-PACIFIC`

- **`dateOfIssue`** (string, date format) - Certificate issuance date  
    Examples: `2025-01-01`, `2024-06-15`

- **`dateOfExpiry`** (string, date format) - Certificate expiration date  
    Examples: `2030-01-01`, `2029-06-15`

- **`status`** (string enum) - Current certificate status  
    Valid values: `active`, `expired`, `suspended`, `revoked`

- **`scopeOfCertification`** (string) - Description of certification coverage  
    Examples: `Chain of Custody for lumber and pulp`, `Forest Management for 10,000 hectares`

- **`versionNumber`** (string) - Version of certification standard applied  
    Examples: `2022`, `FSC-STD-40-004 v3.1`, `SFI 2022-2026`

## Optional Fields

Certificate entities MAY include additional fields for enhanced tracking:

- **`certificateId`** (string) - Optional internal identifier  
    Examples: `SFI-CERT-001`, `INTERNAL-FSC-12345`

- **`conditionalRequirements`** (array) - Special conditions or requirements  
    Example: `[{"type": "surveillance", "frequency": "annual"}]`

- **`suspensionHistory`** (array) - Record of any suspensions  
    Example: `[{"date": "2023-06-01", "reason": "non-compliance", "resolved": "2023-08-15"}]`

- **`auditHistory`** (array) - Record of certification audits  
    Example: `[{"date": "2024-01-15", "type": "surveillance", "auditor": "CERT-AUDITOR-001"}]`

## Key Capabilities

### Multi-Standard Support
Certificate entities support all major forest certification systems:
- **FSC (Forest Stewardship Council)** - Chain of custody and forest management
- **SFI (Sustainable Forestry Initiative)** - Fiber sourcing and chain of custody  
- **PEFC (Programme for Endorsement of Forest Certification)** - International framework
- **Regional Standards** - Country-specific certification schemes

### Status Tracking
Real-time certificate status management enables:
- Automatic expiry notifications
- Suspension and revocation tracking
- Audit schedule management
- Compliance verification workflows

### Chain of Custody Integration
Certificates link directly to supply chain operations through:
- Organization certification requirements
- Material certification claims
- Transaction certification transfers
- Audit trail maintenance for regulatory compliance