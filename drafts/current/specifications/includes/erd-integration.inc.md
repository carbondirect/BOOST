## Interactive Entity Relationship Diagram ## {#interactive-erd}

The BOOST data model comprises 33 interconnected entities organized into 7 thematic areas. For comprehensive exploration of entity relationships and schema definitions, use our interactive ERD Navigator.

### ERD Navigator Overview ### {#erd-overview}

The **[🌟 Interactive ERD Navigator](erd-navigator/index.html)** provides:

- **Complete Entity Visualization** - All 33 BOOST entities with dynamic positioning and thematic color coding
- **Schema-Driven Details** - Field definitions, data types, and validation rules loaded directly from JSON schemas  
- **Interactive Filtering** - Focus on specific thematic areas or use TraceableUnit focus mode
- **Relationship Mapping** - Visual representation of 77+ entity relationships with dynamic highlighting
- **Direct Navigation** - Click entities to jump to their specification sections

<div class="erd-preview-container">

**🎯 Entity Areas:**
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
}
</style>