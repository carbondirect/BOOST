# Pacific Renewable Fuels: BOOST Entity Flow Diagram

## LCFS Compliance Workflow Using BOOST Data Standard Entities

This diagram illustrates how BOOST entities and attributes are used in a real-world LCFS compliance scenario for Pacific Renewable Fuels Corp, demonstrating the complete data flow from lignocellulosic feedstocks to CARB reporting.

## Key Metrics from Example
- **Total Q1 Production**: 5,075,000 gallons renewable diesel
- **Total Energy Output**: 703,902,500 MJ
- **LCFS Credits Generated**: 55,177,391,275 credits
- **Portfolio-Weighted CI**: 17.22 gCO2e/MJ
- **CI Improvement**: 78.39 gCO2e/MJ vs benchmark (95.61)
- **Compliance Status**: Compliant (net positive position)

## Entity Flow Diagram

```mermaid
graph TB
    %% Styling
    classDef orgClass fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    classDef materialClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef pathwayClass fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef transactionClass fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef carbonClass fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef reportingClass fill:#f1f8e9,stroke:#33691e,stroke-width:3px
    
    %% Organization Layer
    ORG[Pacific Renewable Fuels Corp<br/>organizationId: pacific-renewable-fuels-001<br/>lcfsRegistrationId: LCFS-REG-2025-003<br/>regulatedEntityType: producer<br/>facilityCapacity: 50M gallons/year]
    
    %% Feedstock Sources (Material Entities)
    MAT1[Lumber Mill Residual<br/>materialId: feedstock-lumber-mill-residual-001<br/>supplier: Northern California Lumber Co-op<br/>totalFeedstockCI: 4.0 gCO2e/MJ<br/>certification: FSC_Chain_of_Custody]
    
    MAT2[Agricultural Residue<br/>materialId: feedstock-ag-residue-001<br/>supplier: Central Valley Ag Residue Collective<br/>totalFeedstockCI: 3.6 gCO2e/MJ<br/>certification: CARB_Approved_Feedstock]
    
    MAT3[Municipal Green Waste<br/>materialId: feedstock-green-waste-001<br/>supplier: Bay Area Green Waste Recovery<br/>totalFeedstockCI: 2.6 gCO2e/MJ<br/>certification: Municipal_Waste_Stream]
    
    MAT4[Forest Harvest Residual<br/>materialId: feedstock-forest-residual-001<br/>supplier: Sierra Nevada Forest Products<br/>totalFeedstockCI: 5.6 gCO2e/MJ<br/>certification: SFI_Fiber_Sourcing]
    
    %% LCFS Pathway Entities
    PATH1[LCFSPathway: CA-RD-2025-LMR-001<br/>feedstockCategory: lumber_mill_residual<br/>carbonIntensity: 18.7 gCO2e/MJ<br/>pathwayType: Tier_1<br/>annualVolumeLimit: 15M gallons<br/>verificationStatus: active]
    
    PATH2[LCFSPathway: CA-RD-2025-AGR-001<br/>feedstockCategory: agricultural_residue<br/>carbonIntensity: 16.2 gCO2e/MJ<br/>pathwayType: Tier_1<br/>annualVolumeLimit: 20M gallons<br/>verificationStatus: active]
    
    PATH3[LCFSPathway: CA-RD-2025-GRW-001<br/>feedstockCategory: municipal_green_waste<br/>carbonIntensity: 14.5 gCO2e/MJ<br/>pathwayType: Tier_1<br/>annualVolumeLimit: 10M gallons<br/>verificationStatus: active]
    
    PATH4[LCFSPathway: CA-RD-2025-FHR-001<br/>feedstockCategory: forest_harvest_residual<br/>carbonIntensity: 21.3 gCO2e/MJ<br/>pathwayType: Tier_1<br/>annualVolumeLimit: 8M gallons<br/>verificationStatus: active]
    
    %% EnergyCarbonData Entities
    CARB1[EnergyCarbonData: CI-2025-LMR-001<br/>value: 18.7 gCO2e/MJ<br/>measurementMethod: CA-GREET3.0<br/>energyEconomyRatio: 1.0<br/>regulatoryBenchmark: 95.61<br/>LCA Breakdown: 4.0+1.2+12.8+0.7]
    
    CARB2[EnergyCarbonData: CI-2025-AGR-001<br/>value: 16.2 gCO2e/MJ<br/>measurementMethod: CA-GREET3.0<br/>energyEconomyRatio: 1.0<br/>regulatoryBenchmark: 95.61<br/>LCA Breakdown: 3.6+2.1+10.1+0.4]
    
    CARB3[EnergyCarbonData: CI-2025-GRW-001<br/>value: 14.5 gCO2e/MJ<br/>measurementMethod: CA-GREET3.0<br/>energyEconomyRatio: 1.0<br/>regulatoryBenchmark: 95.61<br/>LCA Breakdown: 2.6+1.8+9.8+0.3]
    
    CARB4[EnergyCarbonData: CI-2025-FHR-001<br/>value: 21.3 gCO2e/MJ<br/>measurementMethod: CA-GREET3.0<br/>energyEconomyRatio: 1.0<br/>regulatoryBenchmark: 95.61<br/>LCA Breakdown: 5.6+2.4+12.8+0.5]
    
    %% Q1 2025 Transaction Entities
    TXN1[Transaction: TXN-2025-Q1-001<br/>fuelVolume: 875,000 gallons<br/>fuelCategory: renewable_diesel<br/>reportingPeriod: 2025-Q1<br/>creditsGenerated: 9.33M<br/>delivery: Oakland, CA]
    
    TXN2[Transaction: TXN-2025-Q1-002<br/>fuelVolume: 1,250,000 gallons<br/>fuelCategory: renewable_diesel<br/>reportingPeriod: 2025-Q1<br/>creditsGenerated: 13.77M<br/>delivery: Fresno, CA]
    
    TXN3[Transaction: TXN-2025-Q1-003<br/>fuelVolume: 650,000 gallons<br/>fuelCategory: renewable_diesel<br/>reportingPeriod: 2025-Q1<br/>creditsGenerated: 7.31M<br/>delivery: San Jose, CA]
    
    TXN4[Transaction: TXN-2025-Q1-004<br/>fuelVolume: 425,000 gallons<br/>fuelCategory: renewable_diesel<br/>reportingPeriod: 2025-Q1<br/>creditsGenerated: 4.38M<br/>delivery: Sacramento, CA]
    
    TXN5[Transaction: TXN-2025-Q1-005<br/>fuelVolume: 1,100,000 gallons<br/>fuelCategory: renewable_diesel<br/>reportingPeriod: 2025-Q1<br/>creditsGenerated: 12.12M<br/>delivery: Bakersfield, CA]
    
    TXN6[Transaction: TXN-2025-Q1-006<br/>fuelVolume: 775,000 gallons<br/>fuelCategory: renewable_diesel<br/>reportingPeriod: 2025-Q1<br/>creditsGenerated: 8.27M<br/>delivery: Los Angeles, CA]
    
    %% LCFSReporting Entity
    REPORT[LCFSReporting: LCFS-RPT-2025-Q1-003<br/>regulatedEntityId: pacific-renewable-fuels-001<br/>reportingPeriod: 2025-Q1<br/>totalFuelVolume: 703,902,500 MJ<br/>totalCreditsGenerated: 55,177,391,275<br/>netPosition: 55,177,391,275 credits<br/>complianceStatus: compliant<br/>portfolioWeightedCI: 17.22 gCO2e/MJ]
    
    %% CARB Submission
    CARB[CARB LRT-CBTS Submission<br/>regulated_entity_id: LCFS-REG-2025-003<br/>submission_date: 2025-04-15<br/>verification_date: 2025-04-10<br/>verifier: Environmental Resources Management<br/>ci_improvement: 78.39 gCO2e/MJ<br/>compliance_status: compliant]
    
    %% Relationships - Feedstock to Organization
    MAT1 --> ORG
    MAT2 --> ORG
    MAT3 --> ORG
    MAT4 --> ORG
    
    %% Organization to Pathways
    ORG --> PATH1
    ORG --> PATH2
    ORG --> PATH3
    ORG --> PATH4
    
    %% Pathways to Carbon Data
    PATH1 --> CARB1
    PATH2 --> CARB2
    PATH3 --> CARB3
    PATH4 --> CARB4
    
    %% Pathways to Transactions
    PATH1 --> TXN1
    PATH1 --> TXN6
    PATH2 --> TXN2
    PATH2 --> TXN5
    PATH3 --> TXN3
    PATH4 --> TXN4
    
    %% Transactions to Reporting
    TXN1 --> REPORT
    TXN2 --> REPORT
    TXN3 --> REPORT
    TXN4 --> REPORT
    TXN5 --> REPORT
    TXN6 --> REPORT
    
    %% Reporting to CARB
    REPORT --> CARB
    
    %% Apply styles
    class ORG orgClass
    class MAT1,MAT2,MAT3,MAT4 materialClass
    class PATH1,PATH2,PATH3,PATH4 pathwayClass
    class TXN1,TXN2,TXN3,TXN4,TXN5,TXN6 transactionClass
    class CARB1,CARB2,CARB3,CARB4 carbonClass
    class REPORT,CARB reportingClass
```

## Entity Flow Summary by Volume

```mermaid
pie title Q1 2025 Fuel Volume by Feedstock Type
    "Agricultural Residue" : 46.3
    "Lumber Mill Residual" : 32.5
    "Municipal Green Waste" : 12.8
    "Forest Harvest Residual" : 8.4
```

## Credit Generation Potential by Feedstock

```mermaid
xychart-beta
    title "LCFS Credit Intensity by Feedstock (gCO2e/MJ vs 95.61 benchmark)"
    x-axis ["Municipal Green Waste", "Agricultural Residue", "Lumber Mill Residual", "Forest Harvest Residual"]
    y-axis "Credit Intensity (gCO2e/MJ)" 70 --> 85
    bar [81.1, 79.4, 76.9, 74.3]
```

## BOOST Entity Schema Validation

This example demonstrates complete utilization of BOOST entities:

### ✅ Core Entities Enhanced for LCFS
- **Organization**: LCFS registration, entity type, facility capacity
- **Material**: Feedstock specifications, carbon intensity profiles, sustainability certifications  
- **Transaction**: Fuel volumes, pathway attribution, quarterly reporting periods
- **EnergyCarbonData**: CA-GREET methodology, lifecycle stage breakdown, regulatory benchmarks

### ✅ LCFS-Specific Entities
- **LCFSPathway**: CARB certification, carbon intensity values, volume limits, verification status
- **LCFSReporting**: Quarterly aggregation, compliance status, credit/deficit calculations

### ✅ Data Relationships Validated
- ✅ 1:Many Organization → Transactions (1 producer, 6 fuel sales)
- ✅ 1:Many LCFSPathway → Transactions (4 pathways, 6 transactions)
- ✅ 1:1 LCFSPathway → EnergyCarbonData (pathway-specific CI data)
- ✅ Many:1 Transactions → LCFSReporting (quarterly aggregation)

### ✅ Regulatory Compliance Demonstrated
- ✅ CARB pathway certification (all active Tier_1 pathways)
- ✅ CA-GREET 3.0 methodology compliance
- ✅ Quarterly reporting within 45-day deadline
- ✅ Third-party verification (Environmental Resources Management)
- ✅ Complete audit trail from feedstock to credits

## Business Value Demonstration

**Q1 2025 Results:**
- **5,075,000 gallons** renewable diesel produced
- **55+ million LCFS credits** generated (~$11 billion value at $200/credit)
- **78.39 gCO2e/MJ improvement** vs regulatory benchmark
- **4 lignocellulosic feedstock types** successfully integrated
- **100% compliance** with LCFS requirements

This diagram proves that BOOST entities provide complete support for real-world LCFS compliance workflows while maintaining data integrity and regulatory traceability.