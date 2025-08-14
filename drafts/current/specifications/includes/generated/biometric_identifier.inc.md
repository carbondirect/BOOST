<!-- Auto-generated from biometric_identifier/validation_schema.json -->

BiometricIdentifier entity in BOOST data model

**[View Biometric Identifier in ERD Navigator](erd-navigator/index.html?focus=BiometricIdentifier)**

### Relationships ### {{.unnumbered}}

- **traceableUnitId** → [[#traceable-unit|Traceable Unit]]
- **trackingPointId** → [[#tracking-point|Tracking Point]]

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
<td>enum(BiometricIdentifier)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>biometricId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>biometricSignature</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>captureMethod</code>
<td>enum(optical_scanner, photo_analysis)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>captureTimestamp</code>
<td>string (date-time)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>traceableUnitId</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>captureGeographicDataId</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>speciesBiometrics</code>
<td>array&amp;lt;string&amp;gt;
<td>No description provided
<td>
</tr>
<tr>
<td><code>trackingPointId</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## BiometricIdentifier
### Overview
The `BiometricIdentifier` entity provides optical biometric identification for TRUs with multi-species support to enable attachment-free wood identification as required by the BOOST traceability system. This entity captures unique optical patterns from individual pieces of wood without requiring physical attachments, supporting media-interruption-free traceability through natural wood characteristics.
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
<td>`biometricId`
<td>string
<td>Yes
<td>Unique identifier for the biometric record (primary key)
<td>`BIO-001`, `BIO-DOUGLAS-FIR-KLA-042`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU being identified
<td>`TRU-LOG-001`, `TRU-PILE-CA-042`
</tr>
<tr>
<td>`biometricSignature`
<td>string
<td>Yes
<td>Optical pattern data (encoded string)
<td>Base64 encoded pattern data or hash
</tr>
<tr>
<td>`captureMethod`
<td>string
<td>Yes
<td>Method used for biometric capture (enum)
<td>`optical_scanner`, `photo_analysis`
</tr>
<tr>
<td>`captureGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to location where biometric was captured
<td>`GEO-HARVEST-SITE-001`, `GEO-MILL-001`
</tr>
<tr>
<td>`captureTimestamp`
<td>string (date-time)
<td>Yes
<td>When the biometric was captured
<td>`2025-07-15T06:45:00Z`
</tr>
<tr>
<td>`trackingPointId`
<td>string (FK)
<td>No
<td>Foreign key to tracking point where captured
<td>`TP-HARVEST-001`, `TP-MILL-ENTRANCE-01`
</tr>
<tr>
<td>`speciesBiometrics`
<td>array&lt;string&gt;
<td>No
<td>Individual species biometric data for multi-species TRUs
<td>`["Pine: pattern_hash_123", "Fir: pattern_hash_456"]`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/biometric-identifier/BIO-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-21T15:45:00Z`
</tr>
</tbody>
</table>
### Capture Methods
1. **optical_scanner**
     Dedicated optical scanning equipment
     High-resolution cameras with controlled lighting
     Automated pattern extraction algorithms
     Real-time processing and signature generation
     Integration with tracking point infrastructure
2. **photo_analysis**
     Mobile device camera capture
     Manual or semi-automated photo capture
     Post-processing pattern analysis
     Cloud-based or local analysis systems
     Field verification and backup identification
### Key Features
1. **Attachment-Free Identification**
     No physical tags or markers required
     Natural wood grain pattern recognition
     Unique optical signatures for individual logs
     Non-invasive identification process
     Environmentally friendly approach
2. **Multi-Species Support**
     Species-specific biometric algorithms
     Multiple pattern recognition within single TRU
     Complex pile and batch identification
     Species composition validation
     Mixed-species pile tracking
3. **Pattern Recognition Technology**
     Machine learning algorithms for pattern matching
     Unique signature generation from wood grain
     Bark pattern and texture analysis
     End-grain pattern recognition
     Cross-sectional analysis capabilities
4. **Quality Assurance**
     Pattern uniqueness validation
     False positive prevention
     Multiple angle capture support
     Lighting condition normalization
     Pattern degradation tracking over time
### Biometric Signature Formats
1. **Hash-Based Signatures**
     Cryptographic hash of pattern data
     Compact storage and fast comparison
     Privacy-preserving identification
     Tamper-evident signature format
2. **Vector-Based Signatures**
     Mathematical representation of patterns
     Machine learning feature vectors
     Scalable similarity matching
     Advanced pattern analysis support
3. **Image-Based Signatures**
     Processed image data storage
     Visual pattern verification
     Human-readable verification support
     Quality assessment capabilities
### Validation Rules
1. **TRU Integration**
     traceableUnitId must reference existing TRU
     captureTimestamp must be ≥ TRU creation timestamp
     Species biometrics must match TRU species composition
2. **Pattern Quality**
     biometricSignature must be non-empty and valid format
     Capture method must be appropriate for equipment type
     Pattern uniqueness must be verified within system
3. **Location Consistency**
     captureGeographicDataId must reference valid location
     trackingPointId must be consistent with location
     Capture equipment must be available at location
### Multi-Species Biometric Tracking
1. **Complex Pile Analysis**
     Individual log identification within piles
     Species-specific pattern databases
     Multiple biometric signatures per TRU
     Pattern correlation and validation
2. **Species Composition Validation**
     Biometric confirmation of species identification
     Cross-validation with visual species assessment
     Pattern-based species classification
     Biodiversity compliance verification
3. **Processing Chain Continuity**
     Pattern preservation through processing steps
     Split/merge operation pattern tracking
     Parent/child TRU pattern inheritance
     Continuous identification chain
### Example Use Cases
1. **Harvest Site Identification**
     Initial biometric capture during felling
     End-grain pattern analysis of fresh cuts
     Species verification through pattern analysis
     Unique identification without physical tags
2. **Mill Entrance Verification**
     Final biometric verification before processing
     Pattern matching with harvest site capture
     Quality assessment through pattern analysis
     Processing authorization through identification
3. **Multi-Species Pile Processing**
     Individual log identification within mixed piles
     Species-specific processing routing
     Pattern-based quality grading
     Biodiversity compliance documentation
### Relationships
- BiometricIdentifier belongs to one TraceableUnit
- BiometricIdentifier captured at one TrackingPoint
- BiometricIdentifier located at one GeographicData point
- BiometricIdentifier supports species-specific identification
- BiometricIdentifier enables attachment-free TRU tracking
- BiometricIdentifier validates TRU identity throughout processing chain
