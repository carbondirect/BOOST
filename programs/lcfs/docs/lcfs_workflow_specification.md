# LCFS Reporting Workflow Specification

## BOOST Entity-Driven LCFS Compliance Process

This specification details the complete workflow for generating LCFS quarterly reports from BOOST entities, ensuring compliance with California Air Resources Board requirements.

---

## Overview

The LCFS reporting workflow transforms BOOST entity data into quarterly compliance reports submitted to CARB's LRT-CBTS system. The process involves data collection, validation, calculation, aggregation, and submission phases.

### Key Performance Indicators
- **Reporting Deadline**: 45 days after quarter end
- **Data Completeness**: 100% transaction coverage
- **Accuracy Target**: Zero calculation errors
- **Submission Success**: Automated CARB system integration

---

## Phase 1: Data Collection and Validation

### 1.1 Fuel Transaction Capture

**Input Entities:** Transaction, LCFSPathway, Organization

**Process:**
```
FOR each fuel transaction in reporting period:
  1. Validate Transaction entity completeness
  2. Verify LCFSPathway certification status
  3. Confirm Organization LCFS registration
  4. Check transaction date within reporting period
  5. Validate fuel volume and units
```

**Data Requirements:**
- Transaction.fuelVolume > 0
- Transaction.reportingPeriod = current quarter
- LCFSPathway.verificationStatus = "active"
- Organization.lcfsRegistrationId exists

**Error Handling:**
- Invalid transactions flagged for manual review
- Missing pathway data triggers pathway lookup
- Unregistered organizations excluded with notification

### 1.2 Carbon Intensity Data Validation

**Input Entities:** EnergyCarbonData, LCFSPathway

**Process:**
```
FOR each pathway used in transactions:
  1. Retrieve certified carbon intensity value
  2. Validate CI against CARB database
  3. Confirm CA-GREET version compliance
  4. Verify Energy Economy Ratio
  5. Check regulatory benchmark alignment
```

**Validation Rules:**
- EnergyCarbonData.dataCategory = "carbon_intensity"
- EnergyCarbonData.lcfsPathwayType ≠ "Not_LCFS"
- EnergyCarbonData.measurementMethod contains "CA-GREET3.0"
- EnergyCarbonData.value within acceptable range (0-1000 gCO2e/MJ)

---

## Phase 2: Credit/Deficit Calculation

### 2.1 Credit Calculation Algorithm

**Formula:**
```
Credits = (Benchmark_CI - Pathway_CI) × Fuel_Volume_MJ × EER × Conversion_Factor
```

**Variables:**
- **Benchmark_CI**: Annual regulatory benchmark (gCO2e/MJ)
- **Pathway_CI**: Certified pathway carbon intensity (gCO2e/MJ)
- **Fuel_Volume_MJ**: Fuel volume converted to megajoules
- **EER**: Energy Economy Ratio from pathway certification
- **Conversion_Factor**: Volume to energy conversion (BTU/gallon → MJ)

### 2.2 Step-by-Step Calculation Process

```python
# Pseudocode for credit calculation
def calculate_lcfs_credits(transaction, pathway, carbon_data):
    # 1. Get regulatory benchmark for fuel type and year
    benchmark_ci = get_regulatory_benchmark(
        fuel_type=transaction.fuelCategory,
        year=extract_year(transaction.reportingPeriod)
    )
    
    # 2. Convert fuel volume to energy units (MJ)
    fuel_volume_mj = convert_to_mj(
        volume=transaction.fuelVolume,
        unit=transaction.fuelVolumeUnit,
        fuel_type=transaction.fuelCategory
    )
    
    # 3. Calculate carbon intensity difference
    ci_difference = benchmark_ci - carbon_data.value
    
    # 4. Apply Energy Economy Ratio
    eer = carbon_data.energyEconomyRatio
    
    # 5. Calculate credits/deficits
    credits = ci_difference * fuel_volume_mj * eer
    
    return {
        'credits': max(credits, 0),  # Credits if positive
        'deficits': abs(min(credits, 0)),  # Deficits if negative
        'fuel_volume_mj': fuel_volume_mj,
        'ci_difference': ci_difference
    }
```

### 2.3 Volume Conversion Factors

| Fuel Type | Unit | MJ Conversion Factor |
|-----------|------|---------------------|
| Gasoline | gallon | 121.3 MJ/gallon |
| Diesel | gallon | 138.7 MJ/gallon |
| Ethanol | gallon | 84.5 MJ/gallon |
| Renewable Diesel | gallon | 138.7 MJ/gallon |
| Hydrogen | kg | 142.0 MJ/kg |

---

## Phase 3: Quarterly Aggregation

### 3.1 LCFSReporting Entity Generation

**Process:**
```
FOR each regulated entity in reporting period:
  1. Aggregate all transactions by organization
  2. Sum total fuel volumes by category
  3. Calculate total credits generated
  4. Calculate total deficits incurred
  5. Determine net compliance position
  6. Set compliance status based on position
```

**Aggregation Logic:**
```python
def generate_quarterly_report(organization_id, reporting_period):
    # Get all transactions for organization in period
    transactions = get_transactions(
        organization_id=organization_id,
        reporting_period=reporting_period
    )
    
    total_fuel_volume = 0
    total_credits = 0
    total_deficits = 0
    
    for transaction in transactions:
        # Calculate credits for this transaction
        result = calculate_lcfs_credits(transaction)
        
        total_fuel_volume += result['fuel_volume_mj']
        total_credits += result['credits']
        total_deficits += result['deficits']
    
    net_position = total_credits - total_deficits
    compliance_status = determine_compliance_status(
        net_position, 
        organization_id
    )
    
    return LCFSReporting(
        regulatedEntityId=organization_id,
        reportingPeriod=reporting_period,
        totalFuelVolume=total_fuel_volume,
        totalCreditsGenerated=total_credits,
        totalDeficitsIncurred=total_deficits,
        netPosition=net_position,
        complianceStatus=compliance_status
    )
```

### 3.2 Compliance Status Determination

| Net Position | Compliance Status | Action Required |
|-------------|------------------|-----------------|
| Positive | "compliant" | No action needed |
| Zero | "compliant" | No action needed |
| Negative | "deficit" | Must acquire credits |
| Missing data | "pending" | Complete reporting |

---

## Phase 4: Report Generation and Submission

### 4.1 CARB Report Format Generation

**Output Format:** CARB-compliant XML/JSON for LRT-CBTS system

**Required Report Sections:**
1. **Regulated Entity Information**
   - Organization details from Organization entity
   - LCFS registration ID
   - Reporting period

2. **Fuel Transaction Summary**
   - Aggregated transaction data
   - Fuel type breakdown
   - Volume totals by pathway

3. **Credit/Deficit Summary**
   - Total credits generated
   - Total deficits incurred
   - Net position
   - Compliance status

4. **Detailed Transaction Records**
   - Individual transaction details
   - Pathway attributions
   - Carbon intensity values

### 4.2 Report Structure Template

```json
{
  "lcfs_quarterly_report": {
    "header": {
      "regulated_entity_id": "{{Organization.lcfsRegistrationId}}",
      "organization_name": "{{Organization.name}}",
      "reporting_period": "{{LCFSReporting.reportingPeriod}}",
      "submission_date": "{{LCFSReporting.submissionDate}}",
      "report_version": "1.0"
    },
    "summary": {
      "total_fuel_volume_mj": "{{LCFSReporting.totalFuelVolume}}",
      "total_credits_generated": "{{LCFSReporting.totalCreditsGenerated}}",
      "total_deficits_incurred": "{{LCFSReporting.totalDeficitsIncurred}}",
      "net_position": "{{LCFSReporting.netPosition}}",
      "compliance_status": "{{LCFSReporting.complianceStatus}}"
    },
    "transactions": [
      {
        "transaction_id": "{{Transaction.transactionId}}",
        "fuel_type": "{{Transaction.fuelCategory}}",
        "fuel_volume": "{{Transaction.fuelVolume}}",
        "fuel_volume_unit": "{{Transaction.fuelVolumeUnit}}",
        "pathway_id": "{{Transaction.lcfsPathwayId}}",
        "carbon_intensity": "{{EnergyCarbonData.value}}",
        "energy_economy_ratio": "{{EnergyCarbonData.energyEconomyRatio}}",
        "credits_generated": "calculated_value",
        "transaction_date": "{{Transaction.transactionDate}}"
      }
    ],
    "pathways": [
      {
        "pathway_id": "{{LCFSPathway.pathwayId}}",
        "pathway_type": "{{LCFSPathway.pathwayType}}",
        "fuel_product": "{{LCFSPathway.fuelProduct}}",
        "carbon_intensity": "{{LCFSPathway.carbonIntensity}}",
        "certification_date": "{{LCFSPathway.certificationDate}}",
        "verification_status": "{{LCFSPathway.verificationStatus}}"
      }
    ]
  }
}
```

### 4.3 CARB System Integration

**Submission Process:**
1. **Authentication**: OAuth 2.0 with CARB LRT-CBTS system
2. **Validation**: Pre-submission data validation against CARB schemas
3. **Submission**: Automated API upload to CARB system
4. **Confirmation**: Receipt acknowledgment and tracking number
5. **Status Tracking**: Monitor processing status and error handling

**API Integration Points:**
- **Endpoint**: `https://www.arb.ca.gov/lcfs/lrt-cbts/api/v1/reports`
- **Method**: POST with multipart/form-data
- **Authentication**: Bearer token from CARB OAuth
- **Response**: JSON with submission status and tracking ID

---

## Phase 5: Verification and Audit Support

### 5.1 Third-Party Verification Support

**Verification Data Package:**
- Complete transaction audit trail from BOOST entities
- Pathway certification documentation
- Carbon intensity verification records
- Mass balance calculations
- Supply chain documentation

**Required Documentation:**
```
Verification Package Contents:
├── Transaction_Records/
│   ├── transaction_details.json
│   ├── fuel_delivery_documents.pdf
│   └── pathway_attributions.json
├── Carbon_Intensity/
│   ├── ci_calculations.xlsx
│   ├── ca_greet_inputs.json
│   └── third_party_verification.pdf
├── Supply_Chain/
│   ├── feedstock_tracking.json
│   ├── material_flow_diagram.png
│   └── mass_balance_account.xlsx
└── Compliance/
    ├── quarterly_summary.json
    ├── credit_calculations.xlsx
    └── compliance_attestation.pdf
```

### 5.2 Audit Trail Generation

**Audit Requirements:**
- Complete data lineage from source to report
- Immutable transaction records
- Verification of calculation accuracy
- Supply chain transparency
- Regulatory compliance documentation

**Audit Data Sources:**
1. **Transaction Entities**: Complete fuel transfer records
2. **Material Entities**: Feedstock origin and processing
3. **Certificate Entities**: Pathway certifications and renewals
4. **Audit Entities**: Third-party verification records
5. **VerificationStatement Entities**: Compliance confirmations

---

## Implementation Timeline

### Phase Implementation Schedule

| Phase | Duration | Key Activities | Deliverables |
|-------|----------|----------------|--------------|
| **Phase 1** | 4 weeks | Entity enhancement, data validation | Enhanced ERD, validation rules |
| **Phase 2** | 6 weeks | Calculation engine, aggregation logic | Credit calculation system |
| **Phase 3** | 4 weeks | Report generation, CARB integration | Automated reporting system |
| **Phase 4** | 6 weeks | Testing, verification support | Production-ready system |
| **Phase 5** | 2 weeks | Training, documentation | User guides, maintenance docs |

### Critical Path Dependencies

1. **CARB API Access**: Obtain production credentials for LRT-CBTS
2. **Pathway Database**: Sync with current CARB pathway certifications
3. **Benchmark Values**: Annual regulatory benchmark integration
4. **Testing Environment**: CARB sandbox for development testing
5. **Verification Partners**: Integration with approved third-party verifiers

---

## Success Metrics

### Operational Metrics
- **Report Accuracy**: 99.9% calculation accuracy
- **Submission Success**: 100% automated submission rate
- **Processing Time**: <2 hours for quarterly report generation
- **Data Completeness**: 100% transaction capture rate

### Compliance Metrics
- **Deadline Adherence**: 100% on-time submissions
- **Verification Success**: Zero verification failures
- **Audit Readiness**: Complete audit trail availability
- **Regulatory Alignment**: Full LCFS requirement compliance

This workflow specification ensures complete LCFS compliance through systematic processing of BOOST entity data into regulatory-compliant quarterly reports.