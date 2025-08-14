<!-- Auto-generated from traceable_unit/validation_schema.json -->

Unique biomass tracking unit with BOOST traceability system integration

**[View Traceable Unit in ERD Navigator](erd-navigator/index.html?focus=TraceableUnit)**

### Relationships ### {{.unnumbered}}

- **traceableUnitId** → [[#traceable-unit|Traceable Unit]] - Unique ID for each TRU
- **operatorId** → [[#operator|Operator]] - Foreign key to operator

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
<td>JSON-LD context defining semantic vocabulary mappings
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>Globally unique IRI identifying this specific entity instance
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>enum(TraceableUnit)
<td>Entity type identifier for JSON-LD processing
<td>✓
</tr>
<tr>
<td><code>createdTimestamp</code>
<td>string (date-time)
<td>When the TRU was created
<td>✓
</tr>
<tr>
<td><code>harvestGeographicDataId</code>
<td>string (pattern)
<td>Harvest location - uses EntityNameId convention referencing GeographicData
<td>✓
</tr>
<tr>
<td><code>harvesterId</code>
<td>string (pattern)
<td>Foreign key to harvesting organization
<td>✓
</tr>
<tr>
<td><code>isMultiSpecies</code>
<td>boolean
<td>True if contains multiple species
<td>✓
</tr>
<tr>
<td><code>materialTypeId</code>
<td>string (pattern)
<td>Foreign key to Material entity (reference table)
<td>✓
</tr>
<tr>
<td><code>totalVolumeM3</code>
<td>number (≥0)
<td>Total volume of the traceable unit in cubic meters
<td>✓
</tr>
<tr>
<td><code>traceableUnitId</code>
<td>string (pattern)
<td>Unique ID for each TRU
<td>✓
</tr>
<tr>
<td><code>uniqueIdentifier</code>
<td>string
<td>Biometric signature, RFID tag, or QR code
<td>✓
</tr>
<tr>
<td><code>unitType</code>
<td>enum(4 values)
<td>Type of traceable unit
<td>✓
</tr>
<tr>
<td><code>assortmentType</code>
<td>enum(4 values)
<td>Type of wood assortment
<td>
</tr>
<tr>
<td><code>attachedInformation</code>
<td>array&amp;lt;string&amp;gt;
<td>All data linked to this TRU
<td>
</tr>
<tr>
<td><code>childTraceableUnitIds</code>
<td>array&amp;lt;string&amp;gt;
<td>For split/merge operations (Phase 2)
<td>
</tr>
<tr>
<td><code>currentGeographicDataId</code>
<td>string (pattern)
<td>Current location - uses EntityNameId convention referencing GeographicData
<td>
</tr>
<tr>
<td><code>currentStatus</code>
<td>enum(4 values)
<td>Current status of the TRU (Phase 2)
<td>
</tr>
<tr>
<td><code>lastUpdated</code>
<td>string (date-time)
<td>Timestamp of the most recent data update
<td>
</tr>
<tr>
<td><code>mediaBreakFlags</code>
<td>array&amp;lt;string&amp;gt;
<td>Points where data continuity was lost (Phase 2)
<td>
</tr>
<tr>
<td><code>operatorId</code>
<td>string (pattern)
<td>Foreign key to operator
<td>
</tr>
<tr>
<td><code>parentTraceableUnitId</code>
<td>string
<td>For split/merge operations (Phase 2)
<td>
</tr>
<tr>
<td><code>processingHistory</code>
<td>array&amp;lt;string&amp;gt;
<td>Complete processing chain references (Phase 2)
<td>
</tr>
<tr>
<td><code>qualityGrade</code>
<td>enum(5 values)
<td>Quality grade classification
<td>
</tr>
<tr>
<td><code>sustainabilityCertification</code>
<td>string
<td>FSC, PEFC, etc. claims (Phase 2)
<td>
</tr>
</tbody>
</table>

## TraceableUnit
### Overview
The `TraceableUnit` object represents the fundamental unit of traceability in the BOOST media-interruption-free timber supply chain tracking system. A TRU can be an individual log, pile, volume aggregation, or processed batch that maintains continuous data linkage throughout its lifecycle. This entity replaces MaterialBatch as the primary traceable unit and supports biometric identification, species composition tracking, and complete audit trails.
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
<td>`traceableUnitId`
<td>string
<td>Yes
<td>Unique identifier for the TRU (primary key)
<td>`TRU-LOG-001`, `TRU-PILE-CA-Klamath-042`
</tr>
<tr>
<td>`unitType`
<td>string
<td>Yes
<td>Type of traceable unit (enum)
<td>`individual_log`, `pile`, `volume_aggregation`, `processed_batch`
</tr>
<tr>
<td>`uniqueIdentifier`
<td>string
<td>Yes
<td>Biometric signature, RFID tag, or QR code
<td>`BIO-OAK-12345`, `RFID-TAG-67890`, `QR-CODE-ABC123`
</tr>
<tr>
<td>`totalVolumeM3`
<td>number
<td>Yes
<td>Total volume of the traceable unit in cubic meters
<td>`12.5`, `250.75`, `1000.0`
</tr>
<tr>
<td>`currentGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to current location (GeographicData entity)
<td>`GEO-MILL-ENTRANCE-001`, `GEO-FOREST-ROAD-23`
</tr>
<tr>
<td>`harvestGeographicDataId`
<td>string (FK)
<td>Yes
<td>Foreign key to harvest location (GeographicData entity)
<td>`GEO-HARVEST-SITE-CA-001`
</tr>
<tr>
<td>`createdTimestamp`
<td>string (date-time)
<td>Yes
<td>When the TRU was created
<td>`2025-07-21T08:30:00Z`
</tr>
<tr>
<td>`harvesterId`
<td>string (FK)
<td>Yes
<td>Foreign key to harvesting organization
<td>`ORG-HARVESTER-001`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Foreign key to operator
<td>`OP-JOHN-DOE-001`
</tr>
<tr>
<td>`materialTypeId`
<td>string (FK)
<td>Yes
<td>Foreign key to Material entity (reference table)
<td>`MAT-TYPE-PINE`, `MAT-TYPE-FIR`
</tr>
<tr>
<td>`assortmentType`
<td>string
<td>No
<td>Type of wood assortment (enum)
<td>`sawlog`, `pulpwood`, `biomass`, `chips`
</tr>
<tr>
<td>`qualityGrade`
<td>string
<td>No
<td>Quality grade classification (enum)
<td>`A`, `B`, `C`, `structural`, `fuel`
</tr>
<tr>
<td>`isMultiSpecies`
<td>boolean
<td>Yes
<td>True if contains multiple species
<td>`true`, `false`
</tr>
<tr>
<td>`attachedInformation`
<td>array&lt;string&gt;
<td>No
<td>All data linked to this TRU
<td>`["moisture_content: 12%", "bark_removed: true"]`
</tr>
<tr>
<td>`processingHistory`
<td>array&lt;string&gt;
<td>No
<td>Complete processing chain references (Phase 2)
<td>`["PROC-FELL-001", "PROC-LIMB-002"]`
</tr>
<tr>
<td>`parentTraceableUnitId`
<td>string (FK)
<td>No
<td>For split/merge operations (Phase 2)
<td>`TRU-PARENT-001`
</tr>
<tr>
<td>`childTraceableUnitIds`
<td>array&lt;string&gt;
<td>No
<td>For split/merge operations (Phase 2)
<td>`["TRU-CHILD-001", "TRU-CHILD-002"]`
</tr>
<tr>
<td>`currentStatus`
<td>string
<td>No
<td>Current status of the TRU (Phase 2, enum)
<td>`active`, `processed`, `delivered`, `consumed`
</tr>
<tr>
<td>`sustainabilityCertification`
<td>string
<td>No
<td>FSC, PEFC, etc. claims (Phase 2)
<td>`FSC-Mix Credit`, `SBP-compliant`
</tr>
<tr>
<td>`mediaBreakFlags`
<td>array&lt;string&gt;
<td>No
<td>Points where data continuity was lost (Phase 2)
<td>`["RFID_tag_lost_at_forest_road", "GPS_signal_interrupted"]`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/traceable-unit/TRU-001`
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
---
### Key Features
1. **Media-Interruption-Free Traceability**
     Continuous data linkage from harvest to mill entrance
     Multiple identification methods (biometric, RFID, QR codes)
     Media break detection and flagging
2. **Species Composition Support**
     Multi-species flag for complex piles and batches
     Integration with SpeciesComponent entity for detailed tracking
     Species-specific sustainability claims
3. **Complete Audit Trails**
     Processing history with complete transformation records
     Location history through LocationHistory entity
     Measurement reconciliation through DataReconciliation entity
4. **Split/Merge Operations**
     Parent/child relationships for TRU genealogy
     Volume conservation validation
     Claim inheritance tracking
### Example Use Cases
1. **Individual Log Tracking**
     Type: individual_log
     Unique biometric signature from optical scanner
     Single species with specific quality grade
     Complete harvest-to-mill tracking
2. **Multi-Species Pile**
     Type: pile
     RFID tag identification
     Multiple species tracked via SpeciesComponent entities
     Volume aggregation with species percentages
3. **Processed Batch**
     Type: processed_batch
     Parent TRU references for split operations
     Processing history with transformation details
     Sustainability claim inheritance
### Relationships
- TraceableUnit contains multiple SpeciesComponents (multi-species support)
- TraceableUnit undergoes MaterialProcessing operations
- TraceableUnit has LocationHistory for movement tracking
- TraceableUnit has BiometricIdentifier for optical identification
- TraceableUnit has MeasurementRecord entries at tracking points
- TraceableUnit has sustainability Claims
- TraceableUnit references Material entity for material type
- TraceableUnit managed by Organization
- TraceableUnit originates from SupplyBase
- TraceableUnit included in Transactions and TransactionBatches
- TraceableUnit has parent/child relationships for split/merge operations
