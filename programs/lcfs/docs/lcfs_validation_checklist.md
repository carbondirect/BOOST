# LCFS Compliance Validation Checklist

## BOOST Entity Data Quality and Regulatory Compliance Verification

This checklist ensures that BOOST entities contain complete, accurate, and LCFS-compliant data for quarterly reporting to CARB.

---

## Pre-Reporting Validation

### Organization Entity Validation ✓

**Required Attributes:**
- [ ] `organizationId` - Unique identifier present
- [ ] `name` - Legal entity name matches CARB registration
- [ ] `address` - Current business address
- [ ] `lcfsRegistrationId` - Valid CARB LCFS registration number
- [ ] `regulatedEntityType` - Correct party classification (producer/importer/blender/distributor)

**Validation Rules:**
- [ ] LCFS registration ID format: `LCFS-REG-YYYY-###`
- [ ] Registration status active in CARB system
- [ ] Entity type matches actual business operations
- [ ] Contact information current and reachable

**Critical Checks:**
- [ ] Organization registered for LCFS compliance period
- [ ] No pending enforcement actions or suspensions
- [ ] Quarterly reporting obligations current

---

### Transaction Entity Validation ✓

**Required Attributes:**
- [ ] `transactionId` - Unique transaction identifier
- [ ] `supplyingOrganizationId` - Valid supplier reference
- [ ] `customerOrganizationId` - Valid customer reference
- [ ] `transactionDate` - Within reporting period
- [ ] `fuelVolume` - Positive value > 0
- [ ] `fuelVolumeUnit` - Standard LCFS units (gallons/liters/GGE)
- [ ] `fuelCategory` - Valid LCFS fuel type
- [ ] `reportingPeriod` - Correct quarterly format (YYYY-QN)
- [ ] `lcfsPathwayId` - Active certified pathway
- [ ] `regulatedPartyRole` - Correct party role

**Validation Rules:**
- [ ] Transaction date within reporting quarter boundaries
- [ ] Fuel volume precision to required decimal places
- [ ] Fuel category matches pathway fuel product
- [ ] Pathway certification active on transaction date
- [ ] Regulated party role consistent with organization type

**Cross-Entity Validation:**
- [ ] Supplier organization exists and is active
- [ ] Customer organization valid (if applicable)
- [ ] Pathway referenced exists in LCFSPathway entity
- [ ] Transaction within supplier's operational scope

---

### LCFSPathway Entity Validation ✓

**Required Attributes:**
- [ ] `pathwayId` - Unique CARB pathway identifier
- [ ] `pathwayType` - Valid type (Lookup_Table/Tier_1/Tier_2)
- [ ] `feedstockCategory` - Approved feedstock type
- [ ] `fuelProduct` - Certified fuel product
- [ ] `facilityLocation` - Production facility address
- [ ] `carbonIntensity` - CARB-certified CI value
- [ ] `energyEconomyRatio` - Valid EER (if applicable)
- [ ] `certificationDate` - CARB certification date
- [ ] `expirationDate` - Pathway expiration date
- [ ] `verificationStatus` - Current status (active/suspended/expired)
- [ ] `caGreetVersion` - CA-GREET model version

**Validation Rules:**
- [ ] Pathway ID matches CARB database format
- [ ] Carbon intensity within acceptable range (0-1000 gCO2e/MJ)
- [ ] EER value appropriate for fuel type (1.0 for liquid fuels, >1.0 for alternatives)
- [ ] Certification date ≤ current date ≤ expiration date
- [ ] CA-GREET version 3.0 or approved alternative
- [ ] Verification status "active" for current transactions

**CARB System Cross-Check:**
- [ ] Pathway certified and published on CARB website
- [ ] No pending modifications or suspensions
- [ ] Annual verification completed (if required)
- [ ] Facility operational and compliant

---

### EnergyCarbonData Entity Validation ✓

**Required Attributes:**
- [ ] `energyCarbonDataId` - Unique data record identifier
- [ ] `dataCategory` - "carbon_intensity" for LCFS CI data
- [ ] `value` - Carbon intensity value
- [ ] `unit` - "gCO2e/MJ" for LCFS compliance
- [ ] `source` - Third-party verification source
- [ ] `measurementMethod` - CA-GREET version and methodology
- [ ] `lcfsPathwayType` - Pathway classification
- [ ] `energyEconomyRatio` - EER value
- [ ] `lifeCycleStage` - LCA stage (production/transport/etc.)
- [ ] `regulatoryBenchmark` - Annual LCFS benchmark

**Validation Rules:**
- [ ] CI value matches pathway certification ±0.1 gCO2e/MJ
- [ ] Unit standardized to gCO2e/MJ
- [ ] Measurement method includes CA-GREET3.0
- [ ] EER matches pathway certification exactly
- [ ] Regulatory benchmark current for reporting year
- [ ] Source references approved verifier

**Data Quality Checks:**
- [ ] CI value reasonable for fuel/feedstock combination
- [ ] No outliers requiring explanation
- [ ] Consistent with historical pathway data
- [ ] Third-party verification current (<1 year old)

---

### LCFSReporting Entity Validation ✓

**Required Attributes:**
- [ ] `reportingId` - Unique quarterly report identifier
- [ ] `regulatedEntityId` - Valid organization reference
- [ ] `reportingPeriod` - Correct quarter (YYYY-QN)
- [ ] `totalFuelVolume` - Aggregate fuel volume
- [ ] `totalCreditsGenerated` - Sum of period credits
- [ ] `totalDeficitsIncurred` - Sum of period deficits
- [ ] `netPosition` - Credits minus deficits
- [ ] `complianceStatus` - Compliance determination
- [ ] `submissionDate` - CARB submission timestamp
- [ ] `verificationDate` - Third-party verification date

**Calculation Validation:**
- [ ] Total fuel volume = sum of transaction volumes
- [ ] Credit calculations mathematically correct
- [ ] Deficit calculations accurate
- [ ] Net position = credits - deficits
- [ ] Compliance status reflects net position
- [ ] All calculations use approved conversion factors

**Timing Validation:**
- [ ] Submission within 45 days of quarter end
- [ ] Verification completed before submission
- [ ] All transactions included in reporting period
- [ ] No duplicate transaction counting

---

## Data Completeness Verification

### Transaction Coverage ✓

**Completeness Checks:**
- [ ] All fuel transactions captured for reporting period
- [ ] No missing transaction batches or deliveries
- [ ] Sales documents reconcile with transaction records
- [ ] Third-party confirmations obtained where required

**Volume Reconciliation:**
- [ ] Transaction volumes match delivery receipts
- [ ] Inventory reconciliation completed
- [ ] No unexplained volume discrepancies
- [ ] Mass balance accounts current

### Pathway Attribution ✓

**Attribution Verification:**
- [ ] All transactions assigned to certified pathways
- [ ] Pathway selections appropriate for feedstock/fuel combination
- [ ] No use of expired or suspended pathways
- [ ] Pathway CI values current and verified

### Supporting Documentation ✓

**Required Documentation:**
- [ ] Feedstock purchase agreements and invoices
- [ ] Fuel production records and certificates of analysis
- [ ] Transportation and delivery documentation
- [ ] Third-party verification statements
- [ ] Mass balance account reconciliation
- [ ] Pathway certification documents

---

## Regulatory Compliance Verification

### CARB Requirements ✓

**Regulatory Checklist:**
- [ ] Annual compliance obligation calculated correctly
- [ ] Quarterly reporting deadlines met
- [ ] Credit deficit reconciliation current
- [ ] Enforcement actions resolved
- [ ] Fee payments current

**Third-Party Verification:**
- [ ] Approved verifier engaged (if required)
- [ ] Verification scope covers all material aspects
- [ ] Verification opinion unqualified
- [ ] Corrective actions implemented

### Data Security and Privacy ✓

**Security Requirements:**
- [ ] Confidential business information protected
- [ ] Data transmission encrypted (TLS 1.3)
- [ ] Access controls implemented and audited
- [ ] Audit trail complete and immutable
- [ ] Backup and recovery procedures tested

---

## Pre-Submission Final Checks

### Report Generation ✓

**Final Validation:**
- [ ] All entity data validated and approved
- [ ] Calculations independently verified
- [ ] Report format compliant with CARB specifications
- [ ] Supporting documentation organized and complete
- [ ] Internal review and approval obtained

**Technical Checks:**
- [ ] API connectivity to CARB LRT-CBTS confirmed
- [ ] Authentication credentials current
- [ ] Report file format validated
- [ ] Submission backup procedures ready
- [ ] Error handling procedures tested

### Submission Readiness ✓

**Go/No-Go Criteria:**
- [ ] All validation checks passed
- [ ] Senior management approval obtained
- [ ] Legal review completed (if required)
- [ ] Contingency plans prepared
- [ ] Submission window confirmed

**Post-Submission:**
- [ ] CARB acknowledgment received
- [ ] Submission tracking number recorded
- [ ] Processing status monitored
- [ ] Error resolution procedures activated (if needed)
- [ ] Compliance status updated

---

## Ongoing Monitoring

### Quarterly Maintenance ✓

**Regular Updates:**
- [ ] Pathway certification status monitored
- [ ] Regulatory benchmark updates applied
- [ ] CA-GREET model updates implemented
- [ ] Verifier approvals current
- [ ] System performance metrics reviewed

### Annual Review ✓

**Annual Compliance Review:**
- [ ] Full-year compliance position assessed
- [ ] Pathway portfolio optimized
- [ ] Process improvements identified
- [ ] Training needs assessed
- [ ] Technology upgrades planned

**Continuous Improvement:**
- [ ] Data quality metrics trending
- [ ] Process efficiency measurements
- [ ] Stakeholder feedback incorporated
- [ ] Best practices documented
- [ ] Knowledge transfer completed

---

## Error Resolution Procedures

### Data Quality Issues ✓

**Issue Categories:**
- [ ] Missing required attributes
- [ ] Invalid data values
- [ ] Calculation errors
- [ ] Cross-reference failures
- [ ] Timing discrepancies

**Resolution Process:**
1. [ ] Issue identification and logging
2. [ ] Root cause analysis
3. [ ] Corrective action implementation
4. [ ] Re-validation of affected data
5. [ ] Process improvement documentation

### Regulatory Compliance Issues ✓

**Compliance Failures:**
- [ ] Pathway certification problems
- [ ] Verification statement issues
- [ ] Calculation methodology errors
- [ ] Documentation deficiencies
- [ ] Submission timing failures

**Escalation Procedures:**
1. [ ] Immediate notification to compliance team
2. [ ] Legal counsel engagement (if required)
3. [ ] CARB communication as appropriate
4. [ ] Corrective action plan development
5. [ ] Implementation and monitoring

This comprehensive validation checklist ensures BOOST entities meet all LCFS requirements and support successful quarterly compliance reporting to CARB.