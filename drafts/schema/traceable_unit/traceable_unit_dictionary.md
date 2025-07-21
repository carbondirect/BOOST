# Data Dictionary

## TraceableUnit

### Overview
The `TraceableUnit` object represents the fundamental unit of traceability in the Kaulen framework for media-interruption-free timber supply chain tracking. A TRU can be an individual log, pile, volume aggregation, or processed batch that maintains continuous data linkage throughout its lifecycle. This entity replaces MaterialBatch as the primary traceable unit and supports biometric identification, species composition tracking, and complete audit trails.

### Fields

| Field                         | Type             | Required | Description                                                                 | Examples                                    |
|------------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `traceableUnitId`            | string           | Yes      | Unique identifier for the TRU (primary key)                               | `TRU-LOG-001`, `TRU-PILE-CA-Klamath-042`   |
| `unitType`                   | string           | Yes      | Type of traceable unit (enum)                                             | `individual_log`, `pile`, `volume_aggregation`, `processed_batch` |
| `uniqueIdentifier`           | string           | Yes      | Biometric signature, RFID tag, or QR code                                | `BIO-OAK-12345`, `RFID-TAG-67890`, `QR-CODE-ABC123` |
| `totalVolumeM3`              | number           | Yes      | Total volume of the traceable unit in cubic meters                        | `12.5`, `250.75`, `1000.0`                |
| `currentGeographicDataId`    | string (FK)      | No       | Foreign key to current location (GeographicData entity)                   | `GEO-MILL-ENTRANCE-001`, `GEO-FOREST-ROAD-23` |
| `harvestGeographicDataId`    | string (FK)      | No       | Foreign key to harvest location (GeographicData entity)                   | `GEO-HARVEST-SITE-CA-001`                 |
| `createdTimestamp`           | string (date-time)| Yes     | When the TRU was created                                                  | `2025-07-21T08:30:00Z`                    |
| `harvesterId`                | string (FK)      | Yes      | Foreign key to harvesting organization                                    | `ORG-HARVESTER-001`                       |
| `operatorId`                 | string (FK)      | No       | Foreign key to operator                                                   | `OP-JOHN-DOE-001`                         |
| `materialTypeId`             | string (FK)      | Yes      | Foreign key to Material entity (reference table)                         | `MAT-TYPE-PINE`, `MAT-TYPE-FIR`           |
| `assortmentType`             | string           | No       | Type of wood assortment (enum)                                           | `sawlog`, `pulpwood`, `biomass`, `chips`   |
| `qualityGrade`               | string           | No       | Quality grade classification (enum)                                       | `A`, `B`, `C`, `structural`, `fuel`        |
| `isMultiSpecies`             | boolean          | Yes      | True if contains multiple species                                         | `true`, `false`                           |
| `attachedInformation`        | array<string>    | No       | All data linked to this TRU                                             | `["moisture_content: 12%", "bark_removed: true"]` |
| `processingHistory`          | array<string>    | No       | Complete processing chain references (Phase 2)                           | `["PROC-FELL-001", "PROC-LIMB-002"]`     |
| `parentTraceableUnitId`      | string (FK)      | No       | For split/merge operations (Phase 2)                                     | `TRU-PARENT-001`                          |
| `childTraceableUnitIds`      | array<string>    | No       | For split/merge operations (Phase 2)                                     | `["TRU-CHILD-001", "TRU-CHILD-002"]`     |
| `currentStatus`              | string           | No       | Current status of the TRU (Phase 2, enum)                               | `active`, `processed`, `delivered`, `consumed` |
| `sustainabilityCertification`| string           | No       | FSC, PEFC, etc. claims (Phase 2)                                        | `FSC-Mix Credit`, `SBP-compliant`         |
| `mediaBreakFlags`            | array<string>    | No       | Points where data continuity was lost (Phase 2)                         | `["RFID_tag_lost_at_forest_road", "GPS_signal_interrupted"]` |
| `@id`                        | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/traceable-unit/TRU-001` |
| `lastUpdated`                | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                   |

---

### Key Features

1. **Media-Interruption-Free Traceability**
   - Continuous data linkage from harvest to mill entrance
   - Multiple identification methods (biometric, RFID, QR codes)
   - Media break detection and flagging

2. **Species Composition Support**
   - Multi-species flag for complex piles and batches
   - Integration with SpeciesComponent entity for detailed tracking
   - Species-specific sustainability claims

3. **Complete Audit Trails**
   - Processing history with complete transformation records
   - Location history through LocationHistory entity
   - Measurement reconciliation through DataReconciliation entity

4. **Split/Merge Operations**
   - Parent/child relationships for TRU genealogy
   - Volume conservation validation
   - Claim inheritance tracking

### Example Use Cases

1. **Individual Log Tracking**
   - Type: individual_log
   - Unique biometric signature from optical scanner
   - Single species with specific quality grade
   - Complete harvest-to-mill tracking

2. **Multi-Species Pile**
   - Type: pile
   - RFID tag identification
   - Multiple species tracked via SpeciesComponent entities
   - Volume aggregation with species percentages

3. **Processed Batch**
   - Type: processed_batch
   - Parent TRU references for split operations
   - Processing history with transformation details
   - Sustainability claim inheritance

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