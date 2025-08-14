## Interactive Entity Relationship Diagram ## {#interactive-erd}

The BOOST data model comprises 33 interconnected entities organized into 7 thematic areas. For comprehensive exploration of entity relationships and schema definitions, use our interactive ERD Navigator.

### ERD Navigator Overview ### {#erd-overview}

The **[Interactive ERD Navigator](erd-navigator/index.html)** provides:

- **Complete Entity Visualization** - All 33 BOOST entities with dynamic positioning and thematic color coding
- **Schema-Driven Details** - Field definitions, data types, and validation rules loaded directly from JSON schemas  
- **Interactive Filtering** - Focus on specific thematic areas or use TraceableUnit focus mode
- **Relationship Mapping** - Visual representation of 77+ entity relationships with dynamic highlighting
- **Direct Navigation** - Click entities to jump to their specification sections

<div class="erd-thumbnail-container">
<a href="erd-navigator/index.html" class="erd-thumbnail-link">
<img src="images/erd-navigator-thumbnail.svg" alt="BOOST Entity Relationship Diagram showing all 33 entities organized into 7 thematic areas with interconnecting relationships" class="erd-thumbnail">
<div class="erd-overlay">
<span class="erd-overlay-text">Click to Launch Interactive ERD Navigator</span>
</div>
</a>
</div>

<div class="erd-preview-container">

**Entity Areas:**
- **Core Traceability** (5 entities) - TraceableUnit, MaterialProcessing, ProcessingHistory, LocationHistory, BiometricIdentifier
- **Organizational Foundation** (6 entities) - Organization, Certificate, CertificationBody, CertificationScheme, Audit, Operator  
- **Material & Supply Chain** (7 entities) - Material, SpeciesComponent, Supplier, Customer, SupplyBase, SupplyBaseReport, Equipment
- **Transaction Management** (3 entities) - Transaction, TransactionBatch, SalesDeliveryDocument
- **Measurement & Verification** (4 entities) - MeasurementRecord, Claim, VerificationStatement, MoistureContent
- **Geographic & Tracking** (2 entities) - GeographicData, TrackingPoint
- **Compliance & Reporting** (6 entities) - LcfsPathway, LcfsReporting, ProductGroup, EnergyCarbonData, DataReconciliation, MassBalanceAccount

</div>

### Quick Access ### {#erd-quick-access}

<div class="erd-links">

**🌟 [Launch Full ERD Navigator](erd-navigator/index.html)**  
*Complete interactive visualization with all entities and relationships*

**🔍 [View Entity Documentation](#core-entities)**  
*Detailed specifications for each entity with field definitions*

**📋 [Explore Use Cases](#use-cases)**  
*Real-world examples showing entity interactions*

</div>

### Navigation Between ERD and Specification ### {#erd-navigation}

The ERD Navigator is fully integrated with this specification:

- **From ERD to Spec**: Click any entity in the ERD Navigator to jump to its detailed documentation section
- **From Spec to ERD**: Look for "🗂️ View in ERD" links throughout the entity sections
- **Context Preservation**: Navigation maintains your current view and filter settings where possible

This bidirectional navigation enables seamless exploration between the visual entity relationships and detailed technical specifications.

<style>
.erd-preview-container {
  background-color: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1rem 0;
}

.erd-links {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin: 1.5rem 0;
}

.erd-links a {
  display: block;
  padding: 12px 20px;
  background-color: #6f42c1;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  text-align: center;
  transition: all 0.2s ease;
}

.erd-links a:hover {
  background-color: #5a359a;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.erd-thumbnail-container {
  margin: 2rem 0;
  text-align: center;
  position: relative;
  display: inline-block;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transition: all 0.3s ease;
}

.erd-thumbnail-container:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
}

.erd-thumbnail-link {
  display: block;
  position: relative;
  text-decoration: none;
}

.erd-thumbnail {
  max-width: 100%;
  width: 600px;
  height: auto;
  display: block;
  border-radius: 12px;
}

.erd-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(111, 66, 193, 0.9);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 12px;
}

.erd-thumbnail-container:hover .erd-overlay {
  opacity: 1;
}

.erd-overlay-text {
  font-size: 1.2rem;
  font-weight: bold;
  text-align: center;
  padding: 1rem;
}

@media (min-width: 768px) {
  .erd-links {
    grid-template-columns: 1fr 1fr 1fr;
  }
}

@media print {
  .erd-links a {
    background-color: transparent;
    color: #6f42c1;
    border: 2px solid #6f42c1;
  }
  
  .erd-thumbnail-container {
    box-shadow: none;
    border: 2px solid #e9ecef;
  }
  
  .erd-overlay {
    display: none;
  }
  
  .erd-thumbnail {
    border-radius: 0;
  }
}
</style>