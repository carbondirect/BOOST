# Transportation Classification Framework

## Overview

The BOOST data standard distinguishes between different types of transportation operations to ensure accurate tracking of both spatial movement and material transformation throughout the supply chain. This framework provides clear guidelines for classifying transportation activities and determining the appropriate entity structure for documentation.

## Core Principle

Transportation operations are classified based on whether they involve **material transformation** in addition to spatial movement:

- **Pure Movement**: Only spatial displacement → `LocationHistory`
- **Transformative Transport**: Material changes during transport → `MaterialProcessing` + `ProcessingHistory`
- **Complex Operations**: Both movement and transformation → Both entity types

## Classification Framework

### 1. Pure Transportation → LocationHistory

**Definition**: Transportation that involves only spatial movement without any change to the material characteristics, volume, composition, or configuration.

**Characteristics**:
- ✅ Spatial displacement only (Point A → Point B)
- ✅ Material identity and characteristics preserved
- ✅ No volume, species, or plant part changes
- ✅ Chain of custody maintained without transformation
- ✅ TRU remains unchanged except for location

**Examples**:
- Truck transport from harvest site to mill
- Rail shipment of wood chips
- Ship transport of pellets
- Conveyor movement within facility
- Forwarder transport from skid road to forest road

**Entity Structure**:
```json
{
  "locationEventType": "transportation",
  "transportMethod": "truck",
  "fromGeographicDataId": "GEO-HARVEST-SITE-042", 
  "toGeographicDataId": "GEO-MILL-ENTRANCE-001",
  "distanceTraveled": 45.2,
  "transportDuration": "PT1H30M",
  "equipmentUsed": "truck_logging_001",
  "operatorId": "OP-TRUCK-DRIVER-001"
}
```

### 2. Transformative Transportation → MaterialProcessing

**Definition**: Transportation-related operations that result in material transformation, volume changes, quality changes, or configuration modifications.

**Characteristics**:
- ✅ Material transformation occurs during transport process
- ✅ Volume, quality, or configuration changes
- ✅ Split or merge operations during loading/unloading
- ✅ TRU characteristics modified
- ✅ Processing chain progression

**Examples**:
- **Loading Operations**: Pile → Truckload (volume settling, configuration change)
- **Unloading with Sorting**: Mixed load → Separated piles by grade
- **Consolidation Loading**: Multiple small piles → Single transport load
- **Split Delivery**: Single truckload → Multiple delivery destinations
- **Quality Changes**: Moisture loss, contamination, damage during transport
- **In-Transit Processing**: Sorting, grading, or quality assessment during transport stops

**Entity Structure**:
```json
{
  "processType": "loading",
  "inputTraceableUnitId": "TRU-PILE-ROADSIDE-042",
  "outputTraceableUnitId": "TRU-TRUCKLOAD-042", 
  "inputVolume": 25.5,
  "outputVolume": 24.8,
  "volumeLoss": 0.7,
  "processTimestamp": "2025-07-15T14:30:00Z",
  "equipmentUsed": "loader_CAT_320",
  "qualityMetrics": "No contamination, proper load securing"
}
```

### 3. Complex Transportation → Both Entities

**Definition**: Transportation operations that involve both significant spatial movement AND material transformation, requiring documentation in both systems.

**Characteristics**:
- ✅ Meaningful spatial displacement (location change)
- ✅ Meaningful material transformation (processing change)
- ✅ Both aspects critical for traceability
- ✅ Complex supply chain operations

**Examples**:
- **Mobile Processing**: Harvester moving while processing (felling + transport)
- **Transport with Intermediate Processing**: Truck stops for sorting/grading en route
- **Load Consolidation Across Locations**: Collecting from multiple sites with mixing
- **Quality Assessment During Transport**: In-transit moisture testing affecting grade

**Entity Structure**:
Both LocationHistory (for movement) AND MaterialProcessing (for transformation):
```json
// LocationHistory record
{
  "locationEventType": "transport_with_processing",
  "materialProcessingId": "PROC-MOBILE-HARVEST-001",
  "transportMethod": "mobile_harvester",
  "distanceTraveled": 2.5
}

// MaterialProcessing record  
{
  "processType": "mobile_processing",
  "inputTraceableUnitId": "TRU-TREE-STANDING-042",
  "outputTraceableUnitId": "TRU-LOG-PROCESSED-042",
  "processingGeographicDataId": "GEO-HARVEST-PATH-042"
}
```

## Enhanced Process Types for Transportation

### Extended MaterialProcessing.processType Enum

The standard includes transport-specific process types to handle transformative transportation:

```typescript
type ProcessType = 
  // Traditional processing
  | "felling" | "delimbing" | "crosscutting" 
  | "chipping" | "debarking" | "assortment"
  // Transport-related processing  
  | "loading" | "unloading" | "consolidation" 
  | "transport_sorting" | "shipment_splitting"
  | "mobile_processing" | "in_transit_processing"
```

### Extended LocationHistory.locationEventType Enum

The standard includes processing-aware location event types:

```typescript
type LocationEventType = 
  // Pure movement
  | "arrival" | "departure" | "in_transit" | "storage"
  // Transport with processing elements
  | "transport_with_processing" | "loading_operation" 
  | "unloading_operation" | "consolidation_stop"
  // Standard processing-related
  | "processing" | "measurement"
```

## Decision Matrix

Use this matrix to determine the appropriate classification:

| Transportation Scenario | Material Transformation? | Entity Choice | Rationale |
|-------------------------|--------------------------|---------------|-----------|
| **Truck A→B, no changes** | ❌ No | LocationHistory | Pure spatial movement |
| **Pile → Truckload** | ✅ Yes (configuration) | MaterialProcessing | Volume/config change |
| **Load sorting by destination** | ✅ Yes (split operation) | MaterialProcessing | Multiple outputs created |
| **Moisture loss in transport** | ✅ Yes (quality change) | MaterialProcessing | Quality characteristics changed |
| **GPS tracking en route** | ❌ No | LocationHistory | Spatial tracking only |
| **Mobile harvester moving** | ✅ Both | Both entities | Movement + processing |
| **Consolidation pickup route** | ✅ Both | Both entities | Multiple locations + mixing |
| **In-transit quality grading** | ✅ Both | Both entities | Movement + assessment |

## Transportation-Specific Fields

### LocationHistory Extensions for Transport

```json
{
  "transportMethod": "truck|rail|ship|conveyor|mobile_equipment",
  "distanceTraveled": 45.2,
  "transportDuration": "PT1H30M",
  "routeOptimization": "shortest_distance|fuel_efficient|regulatory_compliant",
  "carrierInformation": {
    "carrierId": "CARRIER-PACIFIC-TRANSPORT-001",
    "vehicleId": "TRUCK-LOG-042",
    "driverOperatorId": "OP-DRIVER-SMITH-001"
  },
  "transportCosts": {
    "fuelCost": 125.50,
    "laborCost": 85.00,
    "equipmentCost": 200.00,
    "totalCost": 410.50
  }
}
```

### MaterialProcessing Extensions for Transport

```json
{
  "transportProcessingMetadata": {
    "loadConfiguration": "loose_pile|secured_load|containerized",
    "loadingMethod": "grapple|conveyor|manual|crane",
    "qualityProtection": "covered|uncovered|climate_controlled",
    "segregationMaintained": true,
    "handlingDamageAssessment": "none|minor|moderate|significant"
  }
}
```

## Business Rules

### Volume Conservation in Transportation

1. **Pure Transportation**: Volume should remain constant (within measurement tolerance)
2. **Loading/Unloading**: Volume changes acceptable due to settling, compaction, or configuration
3. **Moisture-Related**: Volume changes due to drying must be documented with moisture measurements
4. **Damage-Related**: Volume losses due to handling damage must be documented and justified

### Chain of Custody During Transport

1. **Operator Continuity**: Operator responsibility must be clearly assigned throughout transport
2. **Location Verification**: GPS or equivalent verification required for regulatory compliance
3. **Media Break Prevention**: Biometric or equivalent identification maintained during transport
4. **Time Stamping**: Critical events (loading, departure, arrival, unloading) must be timestamped

### Claim Inheritance Through Transport

1. **Pure Transport**: Claims transfer unchanged to destination
2. **Transformative Transport**: Claims may need validation if material characteristics change
3. **Mixed Loads**: Claims for different TRUs must be maintained separately
4. **Quality Changes**: Claims may be invalidated if quality standards are compromised

## Integration with Kaulen Framework

The transportation framework directly supports Kaulen framework requirements:

### Three Critical Tracking Points
- **Harvest Site → Skid Road**: Often involves loading (transformative)
- **Skid Road → Forest Road**: Usually pure transport (spatial only)
- **Forest Road → Mill Entrance**: May involve unloading/sorting (transformative)

### Media-Interruption-Free Requirements
- Biometric identification maintained during transformative transport
- Continuous GPS tracking for pure transport
- Operator accountability throughout transport chain
- Equipment integration for real-time monitoring

### Volume Conservation Validation
- Input/output volume tracking for transformative transport
- Measurement reconciliation at critical tracking points
- Loss documentation and validation procedures
- Quality assessment integration

## Implementation Guidelines

### For Software Developers

1. **Classification Logic**: Implement decision matrix logic to automatically classify transport operations
2. **Dual Entity Support**: Design systems to handle both LocationHistory and MaterialProcessing for complex operations
3. **Volume Validation**: Implement volume conservation checks for transformative transport
4. **Chain Integrity**: Ensure processing chains remain intact through transport operations

### For Supply Chain Operators

1. **Operation Planning**: Consider transformation aspects when planning transport operations
2. **Data Collection**: Collect appropriate data based on transport classification
3. **Quality Monitoring**: Monitor for quality changes during transport that trigger processing classification
4. **Equipment Integration**: Use equipment data to automatically determine transformation occurrence

### For Auditors and Certification Bodies

1. **Audit Trail Review**: Verify appropriate classification of transport operations
2. **Volume Conservation**: Validate volume conservation across transport operations
3. **Chain of Custody**: Ensure continuous custody maintenance during transport
4. **Claim Validation**: Verify appropriate claim handling based on transport classification

## Conclusion

The transportation classification framework provides a systematic approach to handling the complexity of modern supply chain transportation while maintaining the precision required for comprehensive traceability. By distinguishing between pure movement and transformative transport, the framework ensures that all relevant information is captured without over-complicating simple operations.

This approach supports the media-interruption-free traceability requirements of the Kaulen framework while providing the flexibility needed for diverse transportation scenarios in biomass supply chains.