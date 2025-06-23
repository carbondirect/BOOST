Okay, I understand you're requesting a textual description of an Entity-Relationship Diagram (ERD) structure that integrates concepts and requirements from the provided SBP, RSB, FSC, and ISO sources, as well as the "Guidance Chain of Custody" document. This description aims to be similar in style and format to the "SBP Data Standard ERD Description" you provided, outlining key entities, their attributes, and the relationships between them.

As a text-based AI, I cannot generate a visual ERD image. However, I can provide a comprehensive textual description of the entities, their attributes as defined across the sources, and the key relationships that connect them, based on the information in your sources and our conversation history.

This structure represents the core components and their interactions necessary to document and transfer information about solid biomass for energy applications within a Chain of Custody system, drawing on the requirements of various standards and guidance documents.

Here is a textual representation of the key entities and their relationships, integrating concepts from the provided sources:

**Key Entities and Their Attributes:**

Based on the data elements identified in your sources [1, 6, 7, 85, etc.], the core entities for an integrated biomass data standard would include:

*   **Organization:** Represents a legal entity within the biomass supply chain that takes legal ownership of feedstock or biomass. This entity is also referred to as a "link" in the Chain of Custody.
    *   *Attributes:* **Organization Name**, **Address**, **Role** within the supply chain (e.g., source, transport, link, energy producer, Biomass Producer (BP), Trader, Energy Producer, Manufacturer), **Scope of Operations/Certification** (e.g., Product Types, Processes, Applicable Standards (SBP, FSC, RSB, etc.), Accounting Methodology like Mass Balance or Physical Separation), **Legal Entity Status**, **Unique Certificate Code/Number** (if certified) (e.g., SBP-XX-YY), **Contact Information**.
*   **Certification Scheme:** Represents a voluntary or recognized standard system related to biomass or wood Chain of Custody and sustainability. Governing or approving specific schemes is out of scope for the data standard.
    *   *Attributes:* **Scheme Name** (e.g., FSC, PEFC, SBP, RSB, ISO 38200, Guidance), **Recognition Status** (e.g., SBP-recognised, approved for specific criteria), **Version Number** (of the scheme standard).
*   **Certificate:** The formal certification document issued by an accredited Certification Body to an Organization.
    *   *Attributes:* **Certificate ID** (unique identifier with pattern validation), **Certificate Number** (official number as issued by certification body), **Date of Issue**, **Date of Expiry**, **Scope of Certification** (detailed description of what is covered), **Version Number** (integer version of the standard certified against, minimum 1), **Certification Body ID** (reference to issuing CB), **Organization ID** (reference to certificate holder), **Certification Scheme ID** (reference to applicable scheme), **Status** (active, expired, suspended, revoked, pending), **Product Types** (array of product types covered), **Processes** (array of processes covered), **Sites** (array of site objects with site ID, name, and address), **Accounting Methodology** (Mass Balance, Physical Separation, Credit System, Book and Claim), **Applicable Standards** (array of standards referenced), **Attachments** (array of certificate documents with filename, URL, and file type), **Last Updated** (timestamp of record update).
*   **Certification Body (CB):** An independent third-party organization accredited to perform certification activities against relevant standards.
    *   *Attributes:* **CB Name**, **Accreditation Status** (e.g., SBP accreditation in accordance with ISO 17065), **Accreditation Scope** (for specific standards like SBP Standards 1, 2, 4).
*   **Material/Feedstock:** The physical wood, wood-based products, or lignified materials (like bamboo), solid biomass, residues, or waste being tracked. This includes incoming or outgoing biomass/materials.
    *   *Attributes:* **Quantity** (Volume/Mass), **Type** (e.g., Pellets, Wood chips, Residues, Waste, Wood-based products), **Category** (e.g., Guidance Cat 1-5, SBP-compliant, SBP-controlled, Non-eligible input, RSB material type, FSC Recycled, Post-consumer, Pre-consumer), **Species** (common and scientific name, particularly for primary feedstock/processing residues), **Origin/Country of Harvest** (or more specific location), **Source** (e.g., Forest Management Unit, nature/landscape management, agriculture, biogenic waste, point of reclamation), **Raw Material Eligibility Statement** (e.g., eligible as production residue, end-of-life product under RSB), **GMO status** (if applicable).
*   **Supplier:** A legal entity from which an Organization purchases Material/Feedstock.
    *   *Attributes:* **Supplier Name**, **Address**, **Certificate Code** and **Claim** (if FSC/SBP/RSB certified), **Type of Supplier** (e.g., producer, collector, Trader, Forest Management Enterprise, processing site).
*   **Customer:** A legal entity to which an Organization sells Material/Biomass.
    *   *Attributes:* **Customer Name**, **Address**.
*   **Transaction/Consignment:** Represents the transfer of a quantity of Material/Biomass between legal owners. This can be a general concept (Guidance, ISO, FSC, RSB) or a specific digital record (SBP DTS Transaction). Given the structure derived from SBP, this can be represented by **DTS Transaction** (the formal digital record) and **Transaction Batch** (the quantity within the digital record linked to claims/data). Guidance's "consignment" maps well to SBP's "transaction batch".
    *   *Attributes (DTS Transaction):* **Unique DTS Transaction ID**, **Supplying Organization**, **Customer Organization**, **Date** (of transaction/delivery), **Linked Sales/Delivery Document ID**.
    *   *Attributes (Transaction Batch):* **Linked Production Batch ID** (for SBP), **Quantity**, **Associated Claim ID**, **Energy & Carbon Data**. Represents physical biomass.
*   **Claim:** Identifies the certified or controlled nature of biomass associated with a transaction or product. Can be scheme-specific.
    *   *Attributes:* **Claim Type** (e.g., SBP-compliant, SBP-controlled, FSC Mix, FSC Recycled, RSB Global, RSB EU RED), **Linked Transaction/Transaction Batch ID**, **Statement** (e.g., that feedstock qualifies as processing residues/post-consumer under SBP). Claims must be validated/verified.
*   **Sales/Delivery Document:** Official documentation accompanying a transfer of physical biomass.
    *   *Attributes:* **Unique Document ID**, **Date Issued**, **Buyer Name/Address**, **Seller Name/Address**, **Product Description**, **Quantity**, **Linked DTS Transaction ID** (for SBP), **Seller's Certificate Code and Claim** (if applicable), **Reference to Transport Documentation**, **Supplementary Evidence Indicator/Reference** (for full claims).
*   **Sustainability Information:** Data points describing characteristics based on source and criteria. While not a distinct entity in itself, it is a collection of attributes linked to Material/Feedstock and Transaction Batch entities.
    *   *Examples:* Biomass Category (Guidance 1-5), Risk-based approach outcome (yes/no), Regional Risk Assessment outcomes, Data demonstrating secondary/tertiary residual flows (for Category 5), GHG emissions data (raw material, transport, etc.), Linked Verification Statement ID, Proof of Sustainability (RSB), Additional compliance claims (e.g., Low ILUC Risk Biomass, no GMO).
*   **Mass Balance Account:** An accounting mechanism used by Organizations to track volumes of biomass/material with specific characteristics (claims, categories, etc.). Used to track eligible input and certified output over time.
    *   *Attributes:* **Linked Product Group ID**, **Period Inputs**, **Period Outputs**, **Current Balance**, **Defined Balancing Period**, **Conversion Factors Used**. Managed by an Organization/Site. Must be auditable/verifiable.
*   **Product Group:** A categorization of product types used by Organizations (especially BPs) for applying Chain of Custody methods and making claims.
    *   *Attributes:* **Unique Product Group ID**, **Product Type Description**, **Feedstock Classification Rules**. Managed by an Organization/Site.
*   **Energy & Carbon Data:** Specific data points required to calculate GHG emissions and savings.
    *   *Attributes:* **Data Type** (e.g., moisture content, transport distance, fuel consumption figures, fossil fuel comparator), **Value**, **Unit**, **Source** (e.g., linked SAR/SREG, Measurement method, theoretical calculation). Associated with Production Batches or Transaction Batches.
*   **SAR (SBP Audit Report on Energy and Carbon Data):** A specific report template completed by SBP BPs containing static energy and carbon data for a defined Reporting Period.
    *   *Attributes:* **SAR Version/Type** (e.g., Pellets, Woodchips Stationary, Woodchips Mobile), **Linked BP Organization**, **Reporting Period ID**, **Contains Energy and Carbon Data details**. Must be uploaded to the DTS.
*   **SREG (SBP Report on Energy and Carbon for Supplied Biomass):** A specific report template completed by SBP Organizations covering transport-related energy and carbon data not included in the SAR.
    *   *Attributes:* **SREG Version/Type** (e.g., Inland, Sea), **Linked Organization**, **Linked Transaction Batch(es)**, **Contains specific Energy and Carbon Data details** (e.g., transport distances, fuel consumption). Uses the DTS.
*   **Verification Statement:** A statement issued by independent third parties (Conformity Assessment Bodies) to verify certain aspects of conformance. Required to be linked to the relevant consignment/biomass.
    *   *Attributes:* **Statement ID**, **Date** (of statement/verification), **Issuing Body/Conformity Assessment Body**, **Scope** (e.g., covering specific requirements not covered by a certification scheme).
*   **Due Diligence System (DDS):** A risk management process established and implemented by Organizations to verify information regarding the characteristics of all input material and assess/mitigate risks. SBP's Supply Base Evaluation (SBE) is a form of DDS for feedstock sourcing.
    *   *Attributes:* **Defined Requirements** (used for material inclusion/exclusion), **Assessment Process/Methodology**. Managed by an Organization. Relevant for a risk-based approach, particularly for Guidance Category 2 biomass.
*   **Supply Base (SB):** Defines the boundaries of sourcing areas for an Organization, including all relevant operators and stages from harvesting to the Organization's operations.
    *   *Attributes:* **Defined Geographical Boundaries**, **Description of Operators** involved in the supply chain within the SB (company names, addresses, contact person, certification status, stages covered). Must be kept up-to-date.
*   **Risk Assessment:** The process of evaluating the risk of non-conformance with specific criteria (e.g., SBP Standard 1 indicators, sustainability criteria) for feedstock sourced from a Supply Base. Part of a DDS/SBE process.
    *   *Attributes:* **Linked Supply Base ID**, **Date of Assessment**, **Assessor Details** (including demonstrated competence), **Risk Ratings per Criterion/Indicator** (e.g., Low or Specified). Undertaken by a BP Organization.
*   **Standard Indicator/Requirement:** A specific, auditable requirement from a standard (e.g., SBP Standard 1 indicator, FSC requirement, Guidance criteria). Risk Assessment evaluates against these.
    *   *Attributes:* **Indicator/Requirement ID**, **Description**, **Related Principle/Criterion**.
*   **Specified Risk (SBP):** An indicator rating assigned during SBP Risk Assessment when the risk of non-conformance with SBP Standard 1 is not negligible.
    *   *Attributes:* **Linked SBP Standard 1 Indicator ID**, **Description of Risk**, **Justification for Rating**. Outcome of Risk Assessment.
*   **Risk Management Measure (RMM) (SBP):** Actions implemented by a BP Organization to effectively reduce SBP Specified Risks to a low level.
    *   *Attributes:* **Description of Measure**, **Linked Specified Risk(s)**, **Means of Verification** of effectiveness.
*   **Supply Base Verifier (SBV) (SBP):** Evidence or means of verification used to assess conformance with SBP Standard 1 indicators in the Supply Base during an SBE/Risk Assessment.
    *   *Attributes:* **Description of SBV**, **Linked SBP Standard 1 Indicator(s)**, **Source/Type of Evidence**.
*   **Supply Base Report (SBR) (SBP):** A public report prepared by an SBP BP on its Supply Base and SBE findings. Prepared using the SBP Audit Portal.
    *   *Attributes:* **Report ID**, **Preparation Date**, **Linked Organisation**, **Summary of Supply Base**, **Summary of Risk Assessment**, **Description of RMMs**. Must be updated annually and available to stakeholders.
*   **Stakeholder:** A person or organisation that can affect, be affected by, or perceive themselves to be affected by a decision or activity. Organisations must engage with stakeholders.
    *   *Attributes:* **Stakeholder ID**, **Name/Organisation**, **Contact Information**, **Geographical Location/Scope**, **Interest/Expertise**. Records of engagement must be maintained.
*   **Stakeholder Engagement Plan (SEP):** A documented procedure outlining how an Organisation identifies, engages with, and responds to stakeholders.
    *   *Attributes:* **SEP ID**, **Linked Organisation**, **Procedure Description**, **List of Identified Stakeholders**.
*   **Complaint:** A formal expression of dissatisfaction regarding conformance with requirements. Stakeholders may submit complaints.
    *   *Attributes:* **Complaint ID**, **Date Received**, **Description of Allegation**, **Source** (Stakeholder), **Linked Organisation** (being complained against), **Resolution Status**, **Date Closed**. Managed by the Organization and CB.
*   **Audit/Evaluation:** An assessment conducted by a Certification Body (CB) to verify an Organisation's conformance with applicable standards.
    *   *Attributes:* **Audit ID**, **Type** (e.g., Initial, Surveillance, Transfer), **Date(s)**, **Audited Organisation ID**, **CB ID**, **Findings** (e.g., Non-conformances, Opportunities for Improvement), **Report URL/Location** (e.g., Audit Portal). CBs review stakeholder comments before the audit.
*   **Non-conformance:** A failure to meet an applicable requirement identified during an Audit.
    *   *Attributes:* **Non-conformance ID**, **Description**, **Applicable Standard(s) and Requirement(s)**, **Severity** (Minor/Major), **Linked Audit ID**, **Required Corrective Action**, **Status** (Open/Closed). Identified by a CB.
*   **Production Batch (SBP):** A unit of biomass production created by an SBP BP, attributed with identical feedstock, energy, and carbon data. Source for Transaction Batches.
    *   *Attributes:* **Unique Production Batch ID**, **Linked Feedstock Input(s)**, **Associated Energy and Carbon Data**. Created by a BP Organization.
*   **Feedstock Input (SBP):** Represents raw woody material or processing residues used by an SBP BP in biomass production.
    *   *Attributes:* **Quantity** (Volume/Mass), **Feedstock Category** (SBP-compliant, SBP-controlled, Non-eligible input, Primary feedstock, Processing residues, post-consumer feedstock), **Species** (for Primary/Processing Residues), **Origin/Sourcing Area identifier**, **Level of Control Required** (e.g., visual inspection, supplier audits), **Self-declaration** (from supplier, can be additional evidence). Linked to a Supplier. Contributes to a Production Batch.

**Key Relationships Between Entities:**

These relationships define how the entities interact and information flows or is linked across the Chain of Custody:

*   An **Organization** *is certified against* **Certification Scheme(s)** and *is issued* a **Certificate** by a **CB**.
*   An **Organization** *manages* its **Chain of Custody System** (this system handles the management of Material, Transactions, Data, etc.).
*   An **Organization** *implements* a **Due Diligence System (DDS)** to verify information about **Material/Feedstock**.
*   An **Organization** *operates* **Mass Balance Account(s)**, often linked to specific **Product Group(s)**.
*   An **Organization** *manages* **Product Group(s)**.
*   An **Organization** (BP) *defines* its **Supply Base**.
*   A **Supply Base** *is evaluated through* a **Risk Assessment**, which *evaluates against* **Standard Indicator/Requirement(s)**.
*   A **Risk Assessment** *identifies* **Specified Risk(s)** (SBP specific).
*   **Specified Risk(s)** (SBP specific) *requires* **Risk Management Measure(s)** which are *implemented by* the **Organization** (BP).
*   **Standard Indicator/Requirement(s)** *is verified using* **Supply Base Verifier(s)** (SBP specific).
*   An **Organization** (BP) *prepares* a **Supply Base Report (SBR)** (SBP specific) that *reports on* **Risk Assessment** and **RMMs**.
*   An **Organization** *sources* **Material/Feedstock (Feedstock Input)** *from* **Supplier(s)**.
*   An **Organization** (BP) *creates* **Production Batch(es)** (SBP specific) *from* **Material/Feedstock (Feedstock Input)**.
*   **Material/Feedstock**, **Production Batch(es)**, and **Transaction Batch(es)** *are characterized by* **Energy & Carbon Data** and **Sustainability Information**.
*   An **Organization** (BP) *completes* **SAR(s)** (SBP specific) *containing* **Energy & Carbon Data** *for* **Production Batch(es)**.
*   **Production Batch(es)** (SBP specific) *are divided into* **Transaction Batch(es)** (SBP specific).
*   An **Organization** *registers* **Transaction(s)** with a **Customer**. This is represented in SBP by an **Organization** *registering* **DTS Transaction(s)**.
*   A **DTS Transaction** (SBP specific) *includes* **Transaction Batch(es)**.
*   A **Transaction/Transaction Batch** *is associated with* a **Claim** and **Sustainability Information**.
*   A **Transaction** (or **DTS Transaction**) *is documented by* a **Sales/Delivery Document**.
*   An **Organization** *completes* **SREG(s)** (SBP specific) *containing* **Energy & Carbon Data** *related to* **Transaction Batch(es)**.
*   A **Verification Statement** *is issued by* a **Third Party/Conformity Assessment Body** and *is linked to* a **Transaction/Consignment/Biomass (Transaction Batch)**.
*   An **Organization** *has* a **Stakeholder Engagement Plan (SEP)** and *engages with* **Stakeholder(s)**.
*   A **Stakeholder** *may submit* **Complaint(s)** *against* an **Organization**.
*   A **CB** *conducts* **Audit(s)/Evaluation(s)** *of* an **Organization**.
*   An **Audit** *identifies* **Non-conformance(s)**.

This integrated structure captures the essential data elements and their interdependencies necessary to document and trace biomass through the Chain of Custody according to the principles and requirements found in the diverse set of sources you provided. Additional details like validation rules and system mappings would build upon this structure to ensure data quality and interoperability.
