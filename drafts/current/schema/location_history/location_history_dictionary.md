# LocationHistory

## LocationHistory

### Overview
The `LocationHistory` entity implements comprehensive location history tracking for TRUs with timestamps, processing links, and verification methods to support complete movement audit trails. This entity enables tracking every location change, transport method, and verification approach throughout the TRU lifecycle as required by the BOOST continuous traceability system.

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
<td>`locationHistoryId`
<td>string
<td>Yes
<td>Unique identifier for the location history record (primary key)
<td>`LH-001`, `LH-KLA-042-MOVE-003`
</tr>
<tr>
<td>`traceableUnitId`
<td>string (FK)
<td>Yes
<td>Foreign key to TRU being tracked
<td>`TRU-PILE-CA-Klamath-042`
</tr>
<tr>
<td>`geographicDataId`
<td>string (FK)
<td>Yes
<td>Foreign key to location at this point in time
<td>`GEO-HARVEST-001`, `GEO-MILL-ENTRANCE-01`
</tr>
<tr>
<td>`timestamp`
<td>string (date-time)
<td>Yes
<td>When TRU was at this location
<td>`2025-07-21T10:30:00Z`
</tr>
<tr>
<td>`locationEventType`
<td>string
<td>Yes
<td>Type of location event (enum)
<td>`arrival`, `departure`, `processing`, `storage`, `measurement`
</tr>
<tr>
<td>`materialProcessingId`
<td>string (FK)
<td>No
<td>Processing event that triggered location change (optional)
<td>`PROC-LIMB-KLA-002`, `PROC-SORT-003`
</tr>
<tr>
<td>`operatorId`
<td>string (FK)
<td>No
<td>Operator responsible for location change
<td>`OP-TRUCK-DRIVER-001`, `OP-CRANE-002`
</tr>
<tr>
<td>`equipmentUsed`
<td>string
<td>No
<td>Equipment used for location change
<td>`harvester`, `forwarder`, `truck`, `crane`
</tr>
<tr>
<td>`notes`
<td>string
<td>No
<td>Additional context about location event
<td>`Weather delay due to rain`, `Quality inspection completed`
</tr>
<tr>
<td>`distanceTraveled`
<td>number
<td>No
<td>Distance from previous location in kilometers (optional)
<td>`12.5`, `45.8`, `150.2`
</tr>
<tr>
<td>`transportMethod`
<td>string
<td>No
<td>Method of transportation (enum)
<td>`truck`, `rail`, `ship`, `conveyor`, `manual`
</tr>
<tr>
<td>`isCurrentLocation`
<td>boolean
<td>Yes
<td>True if this is the current location
<td>`true`, `false`
</tr>
<tr>
<td>`verificationMethods`
<td>array&lt;string&gt;
<td>No
<td>Methods used to verify location (enum array)
<td>`["GPS", "RFID"]`, `["visual_confirmation", "biometric_scan"]`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/location-history/LH-001`
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
### Location Event Types

1. **arrival**
     TRU arrives at a new location
     Timestamp marks arrival time
     Often paired with verification methods
     May trigger processing events

2. **departure**
     TRU leaves a location
     Timestamp marks departure time
     Transport method usually specified
     Distance to next location may be calculated

3. **processing**
     TRU undergoes processing at location
     Links to MaterialProcessing entity
     Location remains same, but TRU state changes
     Processing operation triggers location history entry

4. **storage**
     TRU stored at location for extended period
     Temporary holding or staging
     May include storage conditions in notes
     Duration calculated from arrival/departure timestamps

5. **measurement**
     Measurement activity at location
     Links to MeasurementRecord entities
     Quality assessment or volume verification
     Often occurs at tracking points

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
     Chronological location history for each TRU
     Transport method and distance tracking
     Equipment and operator accountability
     Current location flag management

2. **Processing Integration**
     Link to MaterialProcessing operations
     Processing-triggered location events
     State change tracking at same location
     Complete transformation history

3. **Verification Support**
     Multiple verification methods per event
     Automated and manual verification options
     GPS accuracy and reliability tracking
     Biometric integration for identification

4. **Audit Trail Completeness**
     Every location change documented
     Operator accountability for movements
     Equipment usage tracking
     Notes for contextual information

### Validation Rules

1. **Timeline Integrity**
     Timestamps must be chronological for same TRU
     Only one current location per TRU (isCurrentLocation = true)
     Processing events must have valid materialProcessingId

2. **Location Consistency**
     geographicDataId must reference valid GeographicData
     Transport method must be appropriate for distance
     Verification methods must be realistic for location type

3. **Current Location Management**
     Only one LocationHistory entry per TRU can have isCurrentLocation = true
     Current location must be most recent timestamp
     Location updates must update previous current location flag

### Example Use Cases

1. **Harvest to Mill Transport**
     Departure from harvest site with truck transport
     Arrival at forest road staging area
     Departure from staging area
     Arrival at mill entrance with final verification

2. **Processing Location Events**
     Arrival at processing facility
     Processing event at same location (delimbing, crosscutting)
     Storage event while awaiting next processing step
     Departure after processing completion

3. **Multi-Modal Transportation**
     Truck transport from forest to rail loading
     Rail transport for long-distance movement
     Truck transport from rail to final destination
     Complete distance and method tracking

### Relationships
- LocationHistory belongs to one TraceableUnit
- LocationHistory references one GeographicData location
- LocationHistory may reference one MaterialProcessing event
- LocationHistory assigned to one Operator
- LocationHistory supports complete TRU movement audit trails
- LocationHistory enables current location queries for TRUs