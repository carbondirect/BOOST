# Data Dictionary

## LocationHistory

### Overview
The `LocationHistory` entity implements comprehensive location history tracking for TRUs with timestamps, processing links, and verification methods to support complete movement audit trails. This entity enables tracking every location change, transport method, and verification approach throughout the TRU lifecycle as required by the BOOST traceability system for media-interruption-free traceability.

### Fields

| Field                    | Type             | Required | Description                                                                 | Examples                                    |
|-------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `locationHistoryId`     | string           | Yes      | Unique identifier for the location history record (primary key)           | `LH-001`, `LH-KLA-042-MOVE-003`           |
| `traceableUnitId`       | string (FK)      | Yes      | Foreign key to TRU being tracked                                          | `TRU-PILE-CA-Klamath-042`                 |
| `geographicDataId`      | string (FK)      | Yes      | Foreign key to location at this point in time                            | `GEO-HARVEST-001`, `GEO-MILL-ENTRANCE-01` |
| `timestamp`             | string (date-time)| Yes     | When TRU was at this location                                             | `2025-07-21T10:30:00Z`                    |
| `locationEventType`     | string           | Yes      | Type of location event (enum)                                             | `arrival`, `departure`, `processing`, `storage`, `measurement` |
| `materialProcessingId`  | string (FK)      | No       | Processing event that triggered location change (optional)                | `PROC-LIMB-KLA-002`, `PROC-SORT-003`      |
| `operatorId`            | string (FK)      | No       | Operator responsible for location change                                  | `OP-TRUCK-DRIVER-001`, `OP-CRANE-002`     |
| `equipmentUsed`         | string           | No       | Equipment used for location change                                        | `harvester`, `forwarder`, `truck`, `crane` |
| `notes`                 | string           | No       | Additional context about location event                                   | `Weather delay due to rain`, `Quality inspection completed` |
| `distanceTraveled`      | number           | No       | Distance from previous location in kilometers (optional)                  | `12.5`, `45.8`, `150.2`                   |
| `transportMethod`       | string           | No       | Method of transportation (enum)                                           | `truck`, `rail`, `ship`, `conveyor`, `manual` |
| `isCurrentLocation`     | boolean          | Yes      | True if this is the current location                                      | `true`, `false`                           |
| `verificationMethods`   | array<string>    | No       | Methods used to verify location (enum array)                            | `["GPS", "RFID"]`, `["visual_confirmation", "biometric_scan"]` |
| `@id`                   | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                        | `https://github.com/carbondirect/BOOST/schemas/location-history/LH-001` |
| `lastUpdated`           | string (date-time)| No      | Timestamp of the most recent data update                                 | `2025-07-21T15:45:00Z`                    |

### Location Event Types

1. **arrival**
   - TRU arrives at a new location
   - Timestamp marks arrival time
   - Often paired with verification methods
   - May trigger processing events

2. **departure**
   - TRU leaves a location
   - Timestamp marks departure time
   - Transport method usually specified
   - Distance to next location may be calculated

3. **processing**
   - TRU undergoes processing at location
   - Links to MaterialProcessing entity
   - Location remains same, but TRU state changes
   - Processing operation triggers location history entry

4. **storage**
   - TRU stored at location for extended period
   - Temporary holding or staging
   - May include storage conditions in notes
   - Duration calculated from arrival/departure timestamps

5. **measurement**
   - Measurement activity at location
   - Links to MeasurementRecord entities
   - Quality assessment or volume verification
   - Often occurs at tracking points

### Transport Methods

- **truck**: Road transportation via logging trucks or other vehicles
- **rail**: Railway transportation for long distances
- **ship**: Water transportation via barges or ships
- **conveyor**: Mechanical conveyor systems (typically at mills)
- **manual**: Human-powered movement (short distances, handling)

### Verification Methods

- **GPS**: Global Positioning System coordinates
- **RFID**: Radio Frequency Identification scanning
- **visual_confirmation**: Human visual verification
- **biometric_scan**: Optical biometric pattern verification

### Key Features

1. **Complete Movement Tracking**
   - Chronological location history for each TRU
   - Transport method and distance tracking
   - Equipment and operator accountability
   - Current location flag management

2. **Processing Integration**
   - Link to MaterialProcessing operations
   - Processing-triggered location events
   - State change tracking at same location
   - Complete transformation history

3. **Verification Support**
   - Multiple verification methods per event
   - Automated and manual verification options
   - GPS accuracy and reliability tracking
   - Biometric integration for identification

4. **Audit Trail Completeness**
   - Every location change documented
   - Operator accountability for movements
   - Equipment usage tracking
   - Notes for contextual information

### Validation Rules

1. **Timeline Integrity**
   - Timestamps must be chronological for same TRU
   - Only one current location per TRU (isCurrentLocation = true)
   - Processing events must have valid materialProcessingId

2. **Location Consistency**
   - geographicDataId must reference valid GeographicData
   - Transport method must be appropriate for distance
   - Verification methods must be realistic for location type

3. **Current Location Management**
   - Only one LocationHistory entry per TRU can have isCurrentLocation = true
   - Current location must be most recent timestamp
   - Location updates must update previous current location flag

### Example Use Cases

1. **Harvest to Mill Transport**
   - Departure from harvest site with truck transport
   - Arrival at forest road staging area
   - Departure from staging area
   - Arrival at mill entrance with final verification

2. **Processing Location Events**
   - Arrival at processing facility
   - Processing event at same location (delimbing, crosscutting)
   - Storage event while awaiting next processing step
   - Departure after processing completion

3. **Multi-Modal Transportation**
   - Truck transport from forest to rail loading
   - Rail transport for long-distance movement
   - Truck transport from rail to final destination
   - Complete distance and method tracking

### Relationships
- LocationHistory belongs to one TraceableUnit
- LocationHistory references one GeographicData location
- LocationHistory may reference one MaterialProcessing event
- LocationHistory assigned to one Operator
- LocationHistory supports complete TRU movement audit trails
- LocationHistory enables current location queries for TRUs