# MaterialBatch to TraceableUnit (TRU) Migration Guide

## Overview

This guide describes the conceptual changes when migrating from the MaterialBatch-centric data model to the new TraceableUnit (TRU)-centric model as part of the Kaulen Framework implementation.

## Core Conceptual Changes

### Primary Entity Transformation
- **MaterialBatch** → **TraceableUnit (TRU)** becomes the primary traceable entity
- **Material** → **Material (Enhanced)** becomes a reference table only (no longer traceable)
- **New supporting entities** added for comprehensive traceability infrastructure

### Data Model Evolution

#### MaterialBatch → TraceableUnit Field Mapping

| MaterialBatch Field | TraceableUnit Field | Notes |
|-------------------|-------------------|-------|
| `materialBatchId` | `traceableUnitId` | Prefixed with "TRU-" |
| `batchNumber` | `legacyBatchNumber` | Preserved for historical reference |
| `materialType` | `materialTypeId` | Now references Material entity |
| `volume` | `totalVolume` | Enhanced with multi-species support |
| `weight` | `totalWeight` | Direct mapping |
| `location` | `currentGeographicDataId` | Now references GeographicData entity |
| `harvestLocation` | `harvestGeographicDataId` | Enhanced geographic integration |
| `harvestDate` | `harvestTimestamp` | More precise timestamp format |
| `processedBy` | `harvesterId` | Now references Organization entity |
| `operator` | `operatorId` | Now references Operator entity |
| `qualityGrade` | `qualityAssessment` | Enhanced quality tracking |
| `certifications` | → Claims | Now handled through separate Claim entities |

#### New TRU Capabilities
- **Multi-species support** - `isMultiSpecies`, `speciesComponents` array
- **Plant part categorization** - Detailed plant part composition and transformation tracking
- **Biometric identification** - `uniqueIdentifier` with biometric signatures
- **Processing history** - Complete audit trail through MaterialProcessing entities
- **Parent/child relationships** - Support for split/merge operations
- **Enhanced status tracking** - Current processing status and location

## New Entity Relationships

### Core Infrastructure Entities
- **TrackingPoint** - Physical locations where TRUs are identified and measured
- **BiometricIdentifier** - Optical identification without physical attachments
- **MaterialProcessing** - Complete processing operation documentation
- **MeasurementRecord** - All measurements taken at tracking points
- **LocationHistory** - Movement tracking through supply chain

### Enhanced Support Entities
- **Organization** - Companies and institutions with geographic operational areas
- **Operator** - Individual workers with certifications and equipment qualifications
- **GeographicData** - Spatial data with GeoJSON compliance
- **SpeciesComponent** - Individual species within multi-species TRUs with plant part composition
- **CertificationScheme** - Certification standard definitions and requirements
- **Material (Enhanced)** - Material types with plant part specifications and processing methods

## Key Functional Changes

### From Batch-Centric to TRU-Centric
- **Individual traceability** - Each log, pile, or processing batch becomes a unique TRU
- **Continuous identification** - Biometric patterns maintain identity without physical tags
- **Processing chain visibility** - Complete audit trail from harvest to final processing
- **Volume conservation tracking** - Precise measurement reconciliation at each step

### Enhanced Traceability Features
- **Three critical tracking points** - Standardized measurement and verification locations
- **Media-interruption-free** - Optical identification prevents traceability gaps
- **Multi-species composition** - Species-level tracking within mixed material TRUs
- **Plant part categorization** - Detailed tracking of plant components and transformations
- **Geographic integration** - Spatial data throughout the supply chain

### Sustainability Claim Evolution
- **Species-specific claims** - Claims can apply to individual species within TRUs
- **Claim inheritance** - Sustainability claims follow TRUs through processing
- **Enhanced validation** - Third-party verification with evidence documentation
- **Percentage tracking** - Precise claim percentages with mass balance calculations

## Migration Implications

### Data Structure Impact
- **Normalized relationships** - Foreign key relationships replace embedded data
- **Enhanced referential integrity** - Comprehensive validation across all entities
- **Expanded data model** - From ~5 core entities to ~15 interconnected entities
- **Improved data quality** - Structured validation and business rule enforcement

### Functional Capabilities
- **Real-time tracking** - Location and processing status updates
- **Comprehensive measurements** - Multiple measurement types and methods
- **Equipment integration** - Direct connection to harvesting and processing equipment
- **Audit trail completeness** - Every operation, movement, and measurement documented

### System Integration
- **API enhancements** - RESTful endpoints for all TRU-centric operations
- **Reporting capabilities** - Enhanced analytics and compliance reporting
- **External system integration** - Equipment, certification, and geographic data systems
- **Scalability improvements** - Optimized for high-volume operations

## Business Process Changes

### Harvest Operations
- **TRU creation** at point of harvest with biometric capture
- **Initial measurements** using harvester-mounted equipment
- **Species identification** and composition documentation
- **Geographic location** precise coordinate capture

### Processing Operations
- **Input/output TRU tracking** for every processing step
- **Plant part transformations** tracking changes in plant components during processing
- **Volume conservation** validation with reconciliation procedures
- **Quality transformation** documentation through processing chain
- **Split/merge operations** with proper TRU genealogy tracking

### Transportation
- **Location history** documentation for all TRU movements
- **Chain of custody** maintenance across organizational boundaries
- **Real-time tracking** integration with transportation systems
- **Arrival verification** at each destination with measurement validation

### Quality and Compliance
- **Measurement reconciliation** between different tracking points
- **Claim validation** with species-specific applicability
- **Certification tracking** through processing and organizational changes
- **Audit trail generation** for compliance reporting and verification

## Migration Benefits

### Enhanced Traceability
- **Individual entity tracking** instead of batch-level aggregation
- **Continuous identification** without physical attachment dependencies
- **Complete audit trails** from standing tree to final product
- **Multi-species visibility** within mixed material flows
- **Plant part composition tracking** enabling circular economy and waste optimization

### Improved Data Quality
- **Structured validation** with comprehensive business rules
- **Referential integrity** across all entity relationships
- **Measurement accuracy** with reconciliation and validation
- **Geographic precision** with spatial data integration

### System Capabilities
- **Scalable architecture** supporting large-scale operations
- **Integration-ready** design for equipment and external systems
- **Compliance-focused** structure supporting multiple certification schemes
- **Analytics-enabled** data model for operational insights and reporting

## Conclusion

The migration from MaterialBatch to TraceableUnit represents a fundamental evolution from batch-centric to individual entity-centric traceability. This transformation enables media-interruption-free tracking, species-specific sustainability claims, comprehensive plant part categorization, and complete supply chain visibility while maintaining data integrity and supporting scalable operations.