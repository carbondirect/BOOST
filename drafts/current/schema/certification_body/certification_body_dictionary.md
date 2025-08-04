# CertificationBody

## Overview
The `CertificationBody` object represents an independent organization authorized to issue certificates under specific certification schemes. The primary key is `cbId`.

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
<td>`cbId`
<td>string
<td>Yes
<td>Unique identifier for the certification body (primary key)
<td>`SFI`, `FSC-US`, `PEFC-001`
</tr>
<tr>
<td>`cbName`
<td>string
<td>Yes
<td>Official name of the certification body
<td>`Sustainable Forestry Initiative`
</tr>
<tr>
<td>`cbType`
<td>string
<td>Yes
<td>Type or category of certification body
<td>`scheme-owner`, `third-party`, `accredited-body`
</tr>
<tr>
<td>`accreditationStatus`
<td>string
<td>Yes
<td>Current accreditation status
<td>`active`, `suspended`, `expired`
</tr>
<tr>
<td>`authorizedSchemes`
<td>array
<td>Yes
<td>List of schemes the CB can certify under
<td>`["SFI-CoC", "SFI-FM"]`
</tr>
<tr>
<td>`contactInformation`
<td>object
<td>Yes
<td>Contact details
<td>`{"email": "certs@sfiprogram.org", "phone": "+1-202-555-0100"}`
</tr>
<tr>
<td>`operationalRegions`
<td>array
<td>Yes
<td>Geographic regions where CB operates
<td>`["US", "CA", "MX"]`
</tr>
<tr>
<td>`accreditationBody`
<td>string
<td>No
<td>Organization that accredited this CB
<td>`ANSI-ASQ National Accreditation Board`
</tr>
<tr>
<td>`validityPeriod`
<td>object
<td>Yes
<td>Period of CB authorization
<td>`{"start": "2020-01-01", "end": "2025-12-31"}`
</tr>
</tbody>
</table>
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