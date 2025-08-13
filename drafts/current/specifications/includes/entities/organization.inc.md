The Organization entity manages companies and institutions with geographic data references and certification management capabilities as part of the BOOST traceability system enhancements. This entity serves as the foundational record for all organizational entities participating in the biomass supply chain, including harvesters, processors, certifiers, and other stakeholders.

## Required Fields

All Organization implementations MUST include the following required fields:

- **`organizationId`** (string) - Unique identifier for the organization (primary key)  
    Examples: `ORG-001`, `ORG-FORESTCO-PACIFIC`

- **`organizationName`** (string) - Legal name of the organization  
    Examples: `Pacific Forest Products LLC`, `Klamath Sustainable Forestry`

- **`organizationType`** (string enum) - Type of organization  
    Valid values: `harvester`, `processor`, `certifier`, `transporter`

## Optional Fields

Organization entities MAY include additional fields for enhanced functionality:

- **`primaryGeographicDataId`** (string, foreign key) - Primary operational location reference  
    Examples: `GEO-MILL-PACIFIC-001`, `GEO-OFFICE-KLAMATH`

- **`operationalAreas`** (array<string>) - Geographic areas where organization operates  
    Example: `["GEO-FOREST-AREA-01", "GEO-MILL-SITE-02"]`

- **`contactEmail`** (string, email format) - Primary contact email address  
    Example: `operations@pacificforest.com`

- **`contactPhone`** (string) - Primary contact phone number  
    Examples: `+1-555-123-4567`, `+1-800-FOREST-1`

- **`certifications`** (array<string>) - Certification IDs held by organization  
    Example: `["CERT-FSC-001", "CERT-SFI-002"]`

- **`establishedDate`** (string, date format) - Date organization was established  
    Examples: `1995-03-15`, `2010-07-01`

- **`taxId`** (string) - Tax identification number  
    Examples: `12-3456789`, `98-7654321`

- **`website`** (string, URI format) - Organization website URL  
    Example: `https://www.pacificforest.com`

## Key Capabilities

### Geographic Operations Management
Organizations can specify operational areas and primary locations for:
- Harvest operation boundaries
- Processing facility locations
- Distribution center management
- Certification compliance tracking

### Certification Integration
The certifications array enables tracking of:
- FSC (Forest Stewardship Council) certifications
- SFI (Sustainable Forestry Initiative) compliance
- PEFC (Programme for the Endorsement of Forest Certification) status
- Regional certification scheme memberships

### Supply Chain Role Classification
Organization types enable proper role-based data validation and workflow management across the entire biomass supply chain ecosystem.