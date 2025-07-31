# BOOST Entity Attribute Flow: LCFS Implementation

## Detailed Entity Attribute Mapping

This diagram shows how specific BOOST entity attributes flow through the Pacific Renewable Fuels LCFS compliance workflow, demonstrating the practical application of the data standard.

```mermaid
graph LR
    %% Styling
    classDef entityHeader fill:#1565c0,color:#fff,stroke:#0d47a1,stroke-width:3px
    classDef attribute fill:#e3f2fd,stroke:#1976d2,stroke-width:1px
    classDef calculation fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef result fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    
    %% Material Entity Attributes
    subgraph MAT [" Material Entities"]
        direction TB
        MAT_ID[materialId: feedstock-lumber-mill-residual-001]
        MAT_TYPE[materialType: lumber_mill_residual]
        MAT_CI[totalFeedstockCI: 4.0 gCO2e/MJ]
        MAT_CERT[sustainabilityCertification: FSC_Chain_of_Custody]
        MAT_SUPPLIER[supplier: Northern California Lumber Co-op]
    end
    
    %% Organization Entity Attributes  
    subgraph ORG [" Organization Entity"]
        direction TB
        ORG_ID[organizationId: pacific-renewable-fuels-001]
        LCFS_REG[lcfsRegistrationId: LCFS-REG-2025-003]
        ENTITY_TYPE[regulatedEntityType: producer]
        CAPACITY[facilityCapacity: 50,000,000 gallons/year]
    end
    
    %% LCFSPathway Entity Attributes
    subgraph PATH [" LCFSPathway Entity"]
        direction TB
        PATH_ID[pathwayId: CA-RD-2025-LMR-001]
        PATH_TYPE[pathwayType: Tier_1]
        FEEDSTOCK_CAT[feedstockCategory: lumber_mill_residual]
        CARBON_INT[carbonIntensity: 18.7 gCO2e/MJ]
        EER[energyEconomyRatio: 1.0]
        VERIFY_STATUS[verificationStatus: active]
        ANNUAL_LIMIT[annualVolumeLimit: 15,000,000 gallons]
    end
    
    %% EnergyCarbonData Entity Attributes
    subgraph CARB_DATA [" EnergyCarbonData Entity"]
        direction TB
        CARB_ID[energyCarbonDataId: CI-2025-LMR-001]
        CI_VALUE[value: 18.7 gCO2e/MJ]
        CI_UNIT[unit: gCO2e/MJ]
        METHOD[measurementMethod: CA-GREET3.0]
        BENCHMARK[regulatoryBenchmark: 95.61 gCO2e/MJ]
        LIFECYCLE[lifeCycleStage: production]
        LCA_FEEDSTOCK[lcaBreakdown.feedstock: 4.0]
        LCA_TRANSPORT[lcaBreakdown.transport: 1.2]
        LCA_PROCESSING[lcaBreakdown.processing: 12.8]
        LCA_DIST[lcaBreakdown.distribution: 0.7]
    end
    
    %% Transaction Entity Attributes
    subgraph TXN [" Transaction Entity"]
        direction TB
        TXN_ID[transactionId: TXN-2025-Q1-001]
        FUEL_VOL[fuelVolume: 875,000 gallons]
        FUEL_UNIT[fuelVolumeUnit: gallons]
        FUEL_CAT[fuelCategory: renewable_diesel]
        REPORTING_PER[reportingPeriod: 2025-Q1]
        PATHWAY_REF[lcfsPathwayId: CA-RD-2025-LMR-001]
        PARTY_ROLE[regulatedPartyRole: producer]
        DELIVERY[deliveryLocation: Oakland, CA]
    end
    
    %% Credit Calculation Process
    subgraph CALC [" LCFS Credit Calculation"]
        direction TB
        CONV_FORMULA[Formula: Volume × 138.7 MJ/gallon]
        FUEL_MJ[Result: 121,362,500 MJ]
        CI_DIFF[CI Difference: 95.61 - 18.7 = 76.91 gCO2e/MJ]
        CREDIT_CALC[Credits: 76.91 × 121,362,500 × 1.0]
        CREDITS_GEN[Credits Generated: 9,333,989,875]
    end
    
    %% LCFSReporting Entity Attributes
    subgraph REPORT [" LCFSReporting Entity"]
        direction TB
        REPORT_ID[reportingId: LCFS-RPT-2025-Q1-003]
        REG_ENTITY[regulatedEntityId: pacific-renewable-fuels-001]
        REPORT_PERIOD[reportingPeriod: 2025-Q1]
        TOTAL_FUEL[totalFuelVolume: 703,902,500 MJ]
        TOTAL_CREDITS[totalCreditsGenerated: 55,177,391,275]
        NET_POS[netPosition: 55,177,391,275 credits]
        COMPLIANCE[complianceStatus: compliant]
        PORTFOLIO_CI[portfolioWeightedCI: 17.22 gCO2e/MJ]
        SUBMIT_DATE[submissionDate: 2025-04-15T14:30:00Z]
        VERIFY_DATE[verificationDate: 2025-04-10T10:00:00Z]
    end
    
    %% CARB Submission Attributes
    subgraph CARB_SUB [" CARB LRT-CBTS Submission"]
        direction TB
        CARB_ENTITY[regulated_entity_id: LCFS-REG-2025-003]
        CARB_ORG[organization_name: Pacific Renewable Fuels Corp]
        CARB_PERIOD[reporting_period: 2025-Q1]
        CARB_VERSION[report_version: 1.0]
        CARB_CONTACT[contact: Sarah Chen, LCFS Compliance Manager]
        CARB_FUEL_GAL[total_fuel_volume_gallons: 5,075,000]
        CARB_FUEL_MJ[total_fuel_volume_mj: 703,902,500]
        CARB_CREDITS[total_credits_generated: 55,177,391,275]
        CARB_COMPLIANCE[compliance_status: compliant]
        CARB_CI[portfolio_weighted_ci: 17.22]
        CARB_IMPROVEMENT[ci_improvement_vs_benchmark: 78.39]
        VERIFIER[verifier_name: Environmental Resources Management]
    end
    
    %% Attribute Flow Connections
    MAT_TYPE --> FEEDSTOCK_CAT
    MAT_CI --> LCA_FEEDSTOCK
    
    ORG_ID --> REG_ENTITY
    LCFS_REG --> CARB_ENTITY
    ENTITY_TYPE --> PARTY_ROLE
    
    PATH_ID --> PATHWAY_REF
    CARBON_INT --> CI_VALUE
    CARBON_INT --> CI_DIFF
    EER --> CREDIT_CALC
    
    FUEL_VOL --> CONV_FORMULA
    FUEL_VOL --> CARB_FUEL_GAL
    CONV_FORMULA --> FUEL_MJ
    FUEL_MJ --> CARB_FUEL_MJ
    FUEL_MJ --> TOTAL_FUEL
    
    CI_DIFF --> CREDIT_CALC
    CREDITS_GEN --> TOTAL_CREDITS
    TOTAL_CREDITS --> CARB_CREDITS
    
    REPORTING_PER --> REPORT_PERIOD
    REPORT_PERIOD --> CARB_PERIOD
    
    NET_POS --> CARB_COMPLIANCE
    PORTFOLIO_CI --> CARB_CI
    
    %% Apply styles
    class MAT,ORG,PATH,CARB_DATA,TXN,REPORT,CARB_SUB entityHeader
    class MAT_ID,MAT_TYPE,MAT_CI,MAT_CERT,MAT_SUPPLIER,ORG_ID,LCFS_REG,ENTITY_TYPE,CAPACITY,PATH_ID,PATH_TYPE,FEEDSTOCK_CAT,CARBON_INT,EER,VERIFY_STATUS,ANNUAL_LIMIT,CARB_ID,CI_VALUE,CI_UNIT,METHOD,BENCHMARK,LIFECYCLE,LCA_FEEDSTOCK,LCA_TRANSPORT,LCA_PROCESSING,LCA_DIST,TXN_ID,FUEL_VOL,FUEL_UNIT,FUEL_CAT,REPORTING_PER,PATHWAY_REF,PARTY_ROLE,DELIVERY,REPORT_ID,REG_ENTITY,REPORT_PERIOD,TOTAL_FUEL,TOTAL_CREDITS,NET_POS,COMPLIANCE,PORTFOLIO_CI,SUBMIT_DATE,VERIFY_DATE,CARB_ENTITY,CARB_ORG,CARB_PERIOD,CARB_VERSION,CARB_CONTACT,CARB_FUEL_GAL,CARB_FUEL_MJ,CARB_CREDITS,CARB_COMPLIANCE,CARB_CI,CARB_IMPROVEMENT,VERIFIER attribute
    class CONV_FORMULA,FUEL_MJ,CI_DIFF,CREDIT_CALC calculation
    class CREDITS_GEN result
```

## Key Attribute Relationships Demonstrated

### 1. **Material → Pathway Linkage**
- `Material.materialType` (lumber_mill_residual) → `LCFSPathway.feedstockCategory` (lumber_mill_residual)
- `Material.totalFeedstockCI` (4.0) → `EnergyCarbonData.lcaBreakdown.feedstock` (4.0)

### 2. **Organization → Regulatory Compliance**
- `Organization.organizationId` → `LCFSReporting.regulatedEntityId`
- `Organization.lcfsRegistrationId` → `CARB.regulated_entity_id`
- `Organization.regulatedEntityType` → `Transaction.regulatedPartyRole`

### 3. **Pathway → Transaction Attribution**
- `LCFSPathway.pathwayId` → `Transaction.lcfsPathwayId`
- `LCFSPathway.carbonIntensity` → Credit calculation input
- `LCFSPathway.energyEconomyRatio` → Credit multiplier

### 4. **Transaction → Calculation Pipeline**
- `Transaction.fuelVolume` (gallons) → Energy conversion → MJ
- `Transaction.reportingPeriod` → `LCFSReporting.reportingPeriod`
- Credit calculation: (Benchmark CI - Pathway CI) × Volume MJ × EER

### 5. **Reporting → CARB Submission**
- `LCFSReporting.totalCreditsGenerated` → `CARB.total_credits_generated`
- `LCFSReporting.portfolioWeightedCI` → `CARB.portfolio_weighted_ci`
- `LCFSReporting.complianceStatus` → `CARB.compliance_status`

## Validation of BOOST Entity Design

✅ **Complete Coverage**: All required LCFS attributes are captured in BOOST entities  
✅ **Data Integrity**: Consistent attribute types and relationships across entities  
✅ **Regulatory Compliance**: Direct mapping to CARB reporting requirements  
✅ **Scalability**: Framework supports multiple feedstocks, pathways, and transactions  
✅ **Traceability**: Full audit trail from feedstock to final compliance reporting  

## Business Logic Implementation

This attribute flow demonstrates that BOOST entities successfully encode the complex business logic required for LCFS compliance:

- **Multi-feedstock optimization** (4 lignocellulosic types)
- **Pathway-specific credit calculation** (4 certified CARB pathways)  
- **Quarterly aggregation** (6 transactions → 1 report)
- **Regulatory submission** (BOOST → CARB LRT-CBTS format)
- **Third-party verification** (complete data lineage)