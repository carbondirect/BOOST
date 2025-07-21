This harmonized list provides a foundational data model, identifying the key information entities and attributes required across the reviewed programs for tracking biomass transactions and associated compliance requirements. Further refinement would involve detailed schema design, data validation rules, and defining relationships between these attributes, consistent with the vision for the BOOST data standard. The tensions noted in the interviews regarding privacy, granularity, and cost would need careful consideration in the final implementation details of any system built upon this harmonized model.

*   `documentId`
    *   Data Type: string or referenceId
    *   Description: A unique identification number for a document or record associated with a transaction or report. Required to link documents or deliveries to transactions.
    *   Relevant Programs: SBP, FSC, SFI, RSB, PEFC, LCFS, RFS.
*   `issueDate`
    *   Data Type: date
    *   Description: The date the associated document or record was issued.
    *   Relevant Programs: SBP.
*   `reportDate`
    *   Data Type: date
    *   Description: The date a specific report (e.g., RFS0801) was submitted.
    *   Relevant Programs: RFS.
*   `reportType`
    *   Data Type: enum (e.g., 'Original', 'Resubmission')
    *   Description: Indicates whether the report is the original submission or a correction/update.
    *   Relevant Programs: RFS.
*   `compliancePeriod`
    *   Data Type: string
    *   Description: Indicates the compliance period or quarter the information pertains to.
    *   Relevant Programs: RFS.
*   `reportYear`
    *   Data Type: integer
    *   Description: Indicates the compliance year of the report.
    *   Relevant Programs: RFS.
*   `isConfidentialBusinessInformation`
    *   Data Type: boolean
    *   Description: Flag indicating if the data is claimed as Confidential Business Information.
    *   Relevant Programs: RFS.
*   `reportingEntityId`
    *   Data Type: string or referenceId
    *   Description: A unique identifier for the company or entity submitting the report.
    *   Relevant Programs: RFS.
*   `reportingCompanyName`
    *   Data Type: string
    *   Description: The name of the company or entity submitting the report.
    *   Relevant Programs: RFS.
*   `facilityId`
    *   Data Type: string or referenceId
    *   Description: A unique identifier for a facility, such as a fuel production facility or a reporting facility.
    *   Relevant Programs: RFS, LCFS.
*   `supplierName`
    *   Data Type: string
    *   Description: The full name of the supplier organization.
    *   Relevant Programs: SFI, RSB, PEFC, Interview Findings.
*   `supplierAddress`
    *   Data Type: string
    *   Description: The full legal address of the supplier organization.
    *   Relevant Programs: SFI, RSB, PEFC.
*   `buyerName`
    *   Data Type: string
    *   Description: The legal name of the buyer organization.
    *   Relevant Programs: SBP.
*   `buyerAddress`
    *   Data Type: string
    *   Description: The full mailing address of the buyer organization.
    *   Relevant Programs: SBP.
*   `sellerName`
    *   Data Type: string
    *   Description: The legal name of the seller organization.
    *   Relevant Programs: SBP.
*   `sellerAddress`
    *   Data Type: string
    *   Description: The full mailing address of the seller organization.
    *   Relevant Programs: SBP.
*   `supplierCertificationStatus`
    *   Data Type: string or boolean
    *   Description: Indicates whether the supplier has valid certification under the relevant scheme. Verified before accepting claims. For LCFS, verification of supplier's valid fuel pathway certification is needed.
    *   Relevant Programs: SFI, RSB, PEFC, LCFS.
*   `certificationCode`
    *   Data Type: string
    *   Description: Unique identifier issued by the certification body or regulatory agency for a certification or pathway. Must be used on claims and labels.
    *   Relevant Programs: FSC, SFI, RSB, PEFC, LCFS, SBP.
*   `certificationStandard`
    *   Data Type: string
    *   Description: Identifies the certification standard (e.g., FSC, SBP, PEFC, RSB, SFI, ISCC, ISO 38200). Necessary for interoperability and cross-recognition.
    *   Relevant Programs: FSC, SBP, RSB, SFI, ISCC, PEFC, ISO 38200.
*   `certificateClaim`
    *   Data Type: string
    *   Description: The specific claim associated with the material (e.g., SBP-compliant, SBP-controlled, FSC 100%, FSC Mix, PEFC certified, RSB certified). Must follow approved formats.
    *   Relevant Programs: SBP, PEFC.
*   `applicableStandards`
    *   Data Type: list<string>
    *   Description: Lists all relevant standards that apply to the certificate scope.
    *   Relevant Programs: FSC, PEFC.
*   `productDescription`
    *   Data Type: string
    *   Description: A description of the product being transferred (e.g., "wood pellets," "wood chips"). Should match invoice descriptions.
    *   Relevant Programs: SBP, PEFC.
*   `productGroup`
    *   Data Type: list<string>
    *   Description: A list of product types covered by the CoC system, often specifying associated materials and control systems used. Biomass Producers categorize product type into product groups for mass balancing.
    *   Relevant Programs: FSC, SFI, RSB, PEFC, SBP.
*   `materialCategory`
    *   Data Type: list<string>
    *   Description: Classification of input material based on its status within a certification scheme (e.g., Certified, Recycled, Controlled Sources, Non-certified, Neutral material). Determines eligibility for claims.
    *   Relevant Programs: SFI, RSB, PEFC, ISO 38200.
*   `feedstockType`
    *   Data Type: string
    *   Description: Specific classification of the raw material (e.g., logging slash, thinning, shrub removal, mill waste, wastes, recycled materials, wood pellets, chips, residues, TOF, post-consumer wood, energy crops, ag residues).
    *   Relevant Programs: ISCC, SBP, BioMAT, BioRAM, LCFS, RFS, Canada CFR, Interview Findings.
*   `feedstockLocationName`
    *   Data Type: string
    *   Description: The name of the specific location where the feedstock was sourced (e.g., name of the farm, forest, or tree plantation).
    *   Relevant Programs: RFS.
*   `fuelSourceCategory`
    *   Data Type: string
    *   Description: General category of the fuel source (e.g., Biogas, Dairy/Agricultural, Sustainable Forest Biomass).
    *   Relevant Programs: BioMAT.
*   `fuelSourceContentDescription`
    *   Data Type: string
    *   Description: Description of the fuel source content (e.g., logging slash, thinning, shrub removal, mill waste).
    *   Relevant Programs: BioMAT.
*   `fuelSourceContentPercentage`
    *   Data Type: decimal
    *   Description: Percentage of the declared fuel source category (e.g., ≥80% for BioRAM SFM, ≥60% for BioRAM HHZ).
    *   Relevant Programs: BioMAT, BioRAM.
*   `originGeographicCoordinates`
    *   Data Type: geographicCoordinates (point or polygon)
    *   Description: Precise geospatial location data for the feedstock origin, such as GPS coordinates or polygon boundaries. Required for EUDR (plot level, polygons for >4ha) and LCFS. Relevant for BioRAM, RFS (identifying land boundaries), Canada CFR (site-level). Desired by NGOs and Tribes. Agencies track treated acres and link to carbon inventory. Can be sensitive data.
    *   Relevant Programs: BioRAM, LCFS, RFS, EUDR, Canada CFR, Interview Findings (NGOs, Tribes, Agencies).
*   `originAreaReference`
    *   Data Type: string
    *   Description: Reference identifier for a sourcing area, such as Township-Range-Section. Used where precise GPS might be difficult or to accommodate legacy systems.
    *   Relevant Programs: Interview Findings (Certification Experts, Supply-Chain Experts).
*   `landOwnershipType`
    *   Data Type: string
    *   Description: Categorization of the land ownership or manager (e.g., Private, State, Federal, Tribal). Relevant for RFS eligibility.
    *   Relevant Programs: RFS, Interview Findings (NGOs, Tribes, Agencies).
*   `fireHazardSeverityZoneStatus`
    *   Data Type: string
    *   Description: Classification of the origin location based on Fire Hazard Severity Zone (FHSZ) status (Moderate, High, Very High). Required for BioRAM HHZ sourcing.
    *   Relevant Programs: BioRAM.
*   `managementPlanReference`
    *   Data Type: string or referenceId
    *   Description: Reference to a forest management plan or silvicultural prescription governing harvesting practices (e.g., THP number, NEPA document). Required for RFS and CA Forest Practice Act (THP). Linked to LCFS/PUC harvest-area tags.
    *   Relevant Programs: CA Forest Practice Act, RFS, Interview Findings (NGOs, Tribes, Agencies, Reporting Stakeholders).
*   `permitId`
    *   Data Type: string or referenceId
    *   Description: Identifier for relevant permits or authorizations associated with the sourcing location or activity (e.g., THP number, permit status). Relevant for BioRAM and RFS. Desired by reporting stakeholders.
    *   Relevant Programs: BioRAM, RFS, Interview Findings (Reporting Stakeholders, Supply-Chain Experts).
*   `approvalPathway`
    *   Data Type: string
    *   Description: The regulatory or procedural pathway by which activities were approved (e.g., NEPA, THP, BIA systems). Relevant for linking origin data to specific processes.
    *   Relevant Programs: Interview Findings (NGOs, Tribes).
*   `quantityDelivered`
    *   Data Type: decimal
    *   Description: The total quantity of feedstock or product delivered or transferred in a specific transaction. Required for volume tracking and compliance calculations.
    *   Relevant Programs: RFS, SBP, SFI, PEFC, LCFS, BioRAM.
*   `quantityUnits`
    *   Data Type: enum (e.g., 'Short Ton', 'Cubic Feet', 'Gallon')
    *   Description: The units of measurement for the quantity delivered.
    *   Relevant Programs: RFS. BioRAM uses Tons.
*   `volumeTrackingRecords`
    *   Data Type: string or referenceId
    *   Description: Reference to internal records or documentation supporting the tracking of input/output volumes, essential for mass balance verification.
    *   Relevant Programs: SFI, RSB, PEFC, LCFS, Interview Findings (Supply-Chain Experts, Reporting Stakeholders).
*   `massEnergyBalanceData`
    *   Data Type: string or referenceId
    *   Description: Data or reference to data required for performing mass or energy balance calculations to track feedstock attributes. Required for LCFS and SBP (mass balance). Supported by ISO 38200 and RSB. Functional but non-digital in BioRAM.
    *   Relevant Programs: LCFS, SBP, ISO 38200, RSB, BioRAM.
*   `cocModel`
    *   Data Type: enum (e.g., 'Physical Separation', 'Percentage', 'Credit', 'Mass Balance', 'Identity Preserved', 'Book and Claim')
    *   Description: The Chain of Custody control method applied to the material. Different programs support different models.
    *   Relevant Programs: FSC, SBP, RSB, SFI, ISCC, PEFC, ISO 38200, LCFS, RenovaBio, Canada CFR.
*   `shipmentDate`
    *   Data Type: date
    *   Description: The date the material was loaded or shipped for delivery.
    *   Relevant Programs: SBP.
*   `transportDocumentReference`
    *   Data Type: string or referenceId
    *   Description: Reference number or identifier for related transport documentation, such as trip tickets or load documents. Required for BioMAT verification, RFS.
    *   Relevant Programs: BioMAT, RFS, SBP.
*   `haulDistance`
    *   Data Type: decimal
    *   Description: The distance the material was transported, often from origin to facility. Used in GHG and feasibility assessments.
    *   Relevant Programs: BioRAM, Interview Findings (State Agencies, Reporting Stakeholders).
*   `traceabilityLevel`
    *   Data Type: string (e.g., 'Item/batch-level', 'Batch-level', 'Lot-level')
    *   Description: The granularity at which traceability is required or supported. EUDR emphasizes shipment-level linkage to plot.
    *   Relevant Programs: FSC, SBP, RSB, SFI, ISCC, PEFC, ISO 38200, RFS, EUDR, Canada CFR.
*   `sustainabilityAttributes`
    *   Data Type: string or referenceId
    *   Description: Data points or reference to documentation detailing compliance with sustainability criteria (e.g., biodiversity protection, labor rights, land use changes). Required by many programs. SBP requires verified data linked to low risk sourcing.
    *   Relevant Programs: ISCC, SBP, RSB, SFI, PEFC, ISO 38200, LCFS, RFS, EU RED III, EUDR, RenovaBio, Canada CFR, Interview Findings (NGOs, Tribes, Reporting Stakeholders, Certification Experts).
*   `ghgData`
    *   Data Type: string or referenceId
    *   Description: Data or reference to data required for calculating Greenhouse Gas emissions associated with the biomass supply chain (e.g., energy use, carbon content, emission factors). Required by SBP, RSB, ISCC, ISO 38200, LCFS, RFS, EU RED III, RenovaBio, Canada CFR. Collected and communicated via SBP DTS.
    *   Relevant Programs: SBP, RSB, ISCC, ISO 38200, LCFS, RFS, EU RED III, RenovaBio, Canada CFR, Interview Findings (Reporting Stakeholders, Certification Experts).
*   `documentationReference`
    *   Data Type: string or referenceId
    *   Description: Reference to electronic documentation files submitted with a report or associated with a transaction, such as maps, permits, or coordinate files.
    *   Relevant Programs: RFS.
*   `internalAuditRecords`
    *   Data Type: string or referenceId
    *   Description: Reference to documentation of internal audits related to the CoC system. Required by most certification schemes.
    *   Relevant Programs: SFI, RSB, ISO 38200, PEFC, ISCC, FSC, SBP.
*   `thirdPartyAuditReports`
    *   Data Type: string or referenceId
    *   Description: Reference to reports from mandatory independent third-party audits verifying compliance. Required by most certification schemes.
    *   Relevant Programs: SBP, RSB, SFI, ISCC, PEFC, ISO 38200, LCFS, RFS.
*   `ddsResults`
    *   Data Type: string or referenceId
    *   Description: Results or reference to the results of the Due Diligence System (DDS) risk assessment and mitigation measures. Mandatory for certain CoC models or non-certified inputs. Required by ISO 38200, SFI, RSB, PEFC. Potentially included in BOOST scope.
    *   Relevant Programs: ISO 38200, SFI, RSB, PEFC, EUDR, BOOST (potential).
*   `labelUseRecords`
    *   Data Type: string or referenceId
    *   Description: Records of the use of certification labels, including claim type, product, and approval.
    *   Relevant Programs: SFI, RSB, PEFC.
*   `trainingRecords`
    *   Data Type: string or referenceId
    *   Description: Documentation of training provided to staff involved in CoC implementation. Required for ISO 38200 and SBP.
    *   Relevant Programs: RSB, ISO 38200, SBP.
*   `outsourcingAgreements`
    *   Data Type: string or referenceId
    *   Description: Written contracts with subcontractors performing CoC activities, defining roles and compliance requirements. Required by SBP and PEFC.
    *   Relevant Programs: RSB, PEFC, SBP.
*   `verificationDocuments`
    *   Data Type: string or referenceId
    *   Description: Documents or references to documents used for verification of compliance, such as signed attestations. Required for BioMAT and BioRAM.
    *   Relevant Programs: BioMAT, BioRAM, Interview Findings (Reporting Stakeholders, NGOs, Tribes).
*   `supplyChainEntities`
    *   Data Type: list<string> or list<referenceId>
    *   Description: Identification of the types of parties involved in the supply chain (e.g., haulers, processors, traders). RSB system must handle multiple operator types.
    *   Relevant Programs: RSB, Interview Findings (State Agencies).
*   `processingInformation`
    *   Data Type: string or referenceId
    *   Description: Data or reference to data about processing steps the biomass undergoes.
    *   Relevant Programs: RSB.
*   `economicPricingData`
    *   Data Type: decimal (sensitive)
    *   Description: Information related to pricing or costs. Often considered confidential and sensitive.
    *   Relevant Programs: Interview Findings (State Agencies, Supply-Chain Experts, Reporting Stakeholders, NGOs, Tribes).
*   `siteActivity`
    *   Data Type: string
    *   Description: Description of the role or activity of a certified site within the supply chain (e.g., trader, processor, printer).
    *   Relevant Programs: FSC.
*   `conversionFactors`
    *   Data Type: decimal or referenceId
    *   Description: Data or reference to data for conversion ratios between different units or forms of biomass. Required for LCFS and SBP.
    *   Relevant Programs: RSB, ISO 38200, LCFS, SBP.
*   `originCountry`
    *   Data Type: string
    *   Description: The country where the biomass originated. Relevant for EUDR risk classification and RenovaBio origin verification (linking to CAR).
    *   Relevant Programs: EUDR, RenovaBio, BOOST (potential).
*   `verificationStatements`
    *   Data Type: string or referenceId
    *   Description: Reference to statements issued by independent verifiers.
    *   Relevant Programs: BOOST (potential).
*   `complianceDocuments`
    *   Data Type: string or referenceId
    *   Description: Reference to specific documents required for compliance reporting (e.g., RFS0801 report).
    *   Relevant Programs: RFS.
*   `fuelPathwayCode`
    *   Data Type: string
    *   Description: CARB-assigned unique code for a certified fuel pathway.
    *   Relevant Programs: LCFS.
*   `jointApplicantAgreements`
    *   Data Type: string or referenceId
    *   Description: Formal agreements between entities sharing responsibility for a fuel pathway.
    *   Relevant Programs: LCFS.
*   `bookClaimRecords`
    *   Data Type: string or referenceId
    *   Description: Documentation supporting book-and-claim accounting methods. Applicable for specific LCFS pathways (electricity, biomethane). RSB also supports Book and Claim.
    *   Relevant Programs: LCFS, RSB.
*   `geographicSourcingConstraints`
    *   Data Type: string
    *   Description: Description of any geographic restrictions or limitations on sourcing. BioMAT has no statutory locational limit. BioRAM requires sourcing from specific HHZs.
    *   Relevant Programs: BioMAT.
*   `certificateOfEligibilityReference`
    *   Data Type: string or referenceId
    *   Description: Reference to the CEC RPS certification required for BioMAT projects.
    *   Relevant Programs: BioMAT.
*   `fuelOriginReference`
    *   Data Type: string
    *   Description: Geographic coordinates or a facility/source ID specifying the origin of the fuel for BioRAM.
    *   Relevant Programs: BioRAM.
*   `volumeDeliveredUnits`
    *   Data Type: string
    *   Description: Units used for reporting volume delivered (e.g., Tons).
    *   Relevant Programs: BioRAM.
*   `fuelOwnershipDocumentationReference`
    *   Data Type: string or referenceId
    *   Description: Reference to documentation regarding fuel ownership and status (e.g., landowner name, parcel ID, permit status). Includes CAL FIRE permit or exemption status.
    *   Relevant Programs: BioRAM.
*   `attestationReference`
    *   Data Type: string or referenceId
    *   Description: Reference to signed attestations certifying compliance (monthly or quarterly). Required for BioMAT.
    *   Relevant Programs: BioMAT, BioRAM.

