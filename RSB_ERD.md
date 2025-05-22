Okay, I can provide a textual description of the entities and relationships for the RSB Chain of Custody system, drawing upon the information in the provided RSB Procedure for Traceability (RSB-PRO-20-001 V3.2) and the RSB Standard Amendment Woody Biomass (RSB-SA-01 V1.0), as well as the structure used for the SBP ERD description.

This description outlines the core components and their connections as defined or implied by these specific RSB documents. It would form the basis for a technical specification for data exchange within an RSB-compliant system for woody biomass.

Here is a textual representation of the key entities and their relationships:

**Key Entities and Their Attributes:**

Based on the requirements and concepts described in the RSB sources, the core entities for this data standard would include:

*   **Operator:** Represents a **legal entity** within the supply chain that **acquires, handles, or forwards RSB certified material**. For an operator to handle and forward RSB certified material, they must be **RSB certified**. This is the unit of certification.
    *   *Attributes:* **Operator Name**, Address, **RSB Certificate Reference Code**, **Scope of Certification** (including processes, sites, and applicable RSB certification schemes), Legal Entity Status (implied by "legal entity"). The operator appoints a management representative.

*   **RSB Certificate:** Represents the formal **certification** issued to an **Operator** confirming compliance with applicable RSB standards, including RSB-PRO-20-001.
    *   *Attributes:* **Certificate Reference Code**, Date of Issue (implied by validity), Date of Expiry (implied by validity), Scope (RSB certification schemes covered). Issued by a **Certification Body**.

*   **Certification Body (CB):** An **independent third-party organization** that verifies whether **Operators** comply with RSB requirements during audits. They issue RSB Certificates.
    *   *Attributes:* **CB Name**, Accreditation Status (implied by role).

*   **Supplier:** A legal entity from which an **Operator** **acquires RSB certified material**. Suppliers are subject to **verification and monitoring** by the Operator, particularly for Processing Residues and Post-consumer feedstock.
    *   *Attributes:* **Supplier Name**, Address, **RSB Certificate Reference Code** (if certified), **Type of Supplier** (producer, purchaser/collector from point of reclamation, trader).

*   **Customer:** A legal entity to which an **Operator** **forwards RSB certified material**. Forwarding is based on a contractual agreement.
    *   *Attributes:* **Customer Name**, Address.

*   **RSB Certified Material:** The physical biomass or related material (e.g., chemical intermediaries) that is **eligible for certification** under the RSB system. It is tracked along the **Supply Chain**.
    *   *Attributes:* **Quantity** (Volume/Mass, Units), **Material Type** (e.g., Roundwood, Sawmill residues, Pellets, Chips), **Raw Material Specification** (crop, production residue, end-of-life product), **Country of Origin**, **GHG Intensity**, **RSB Certification Scheme** (Global, EU RED, ICAO CORSIA, Japan), **Sustainability Claim**. (Represented in **Batch(es)** with **Product Information**).

*   **Site:** A physical location where **RSB certified material** is **acquired, handled, forwarded**, or where **internal processing steps** occur within an **Operator's** scope of certification. Operators must document all relevant sites.
    *   *Attributes:* **Site Name/Identifier**, Address, **Activity Type** (acquisition, handling, forwarding, processing).

*   **Batch:** A unit of **RSB certified material**, typically with **identical characteristics** like GHG intensity. **Product Information** is attached to each batch. Batches are documented, especially separately in the Identity Preserved model. Has a unique ID number.
    *   *Attributes:* **Batch ID**, **Linked Product Information**, **Quantity** (inherent to the batch size).

*   **Product Information:** Detailed information that must accompany every **Batch** of **RSB certified material** that is acquired, handled, or forwarded. Full requirements are in Annex I of RSB-PRO-20-001.
    *   *Attributes:* **Product Description**, **Raw Material Specification**, **Origin/Country of Origin**, **Quantity**, **Date of Acquisition/Shipment**, **Supplier/Customer Name and Address**, **Last Production/Processing Site Name and Address**, **Certification Scheme**, **Sustainability Claim(s)**, **Certificate Number**, **CB Name**, **Chain of Custody Model** used by supplier, **GHG Intensity**, **Delivery Note/Invoice ID**.

*   **Sales Documentation:** Official document (e.g., invoice, bill of lading) used for transactions of **RSB certified material**. It must include the required **Product Information** and can serve as the **Proof of Sustainability**. Must have a unique number.
    *   *Attributes:* **Unique Document ID**, **Date Issued** (implied by date of shipment), **Buyer Name/Address**, **Seller Name/Address**, **Product Description**, **Quantity**.

*   **Proof of Sustainability (PoS):** A document accompanying a batch of outgoing **RSB certified material**. It must include the required **Product Information**. It can be the regular **Sales Documentation**.
    *   *Attributes:* (Includes all **Product Information** attributes).

*   **Chain of Custody System:** The overall system implemented by an **Operator** to track **RSB certified material** through all processing and trading steps. It must meet the requirements of RSB-PRO-20-001.
    *   *Attributes:* **System Type** (implied by the chosen model), Operating Procedures, Necessary Infrastructures (software, tools).

*   **Chain of Custody Model:** The specific tracking method used within the **Chain of Custody System**. Options include Identity Preserved, Product Segregation, Mass Balance, Content Ratio Accounting, and Book & Claim. Different models have different rules for handling and mixing material. The model used by the supplier is part of the **Product Information**.
    *   *Attributes:* **Model Type** (Identity Preserved, Segregation, Mass Balance, Content Ratio Accounting, Book & Claim), Specific rules/parameters based on the type.

*   **Process:** An internal processing step within an **Operator's** scope of certification where **RSB certified material** is handled.
    *   *Attributes:* **Process Description/Identifier**. Occurs at a **Site**. May use **Conversion Factors**.

*   **Conversion Factor:** A factor used in certain **Chain of Custody Models** (Mass Balance, Content Ratio Accounting) to calculate the amount of output based on the input material quantity. It is monitored by the **Operator** and checked by the **CB**.
    *   *Attributes:* **Ratio Value**, Input Units, Output Units. Linked to a **Process** or group of products.

*   **Point of Origin:** The starting point of traceability for certain materials, particularly waste and residue-based chains and specific woody biomass categories like Thinnings or Roundwood. The GHG calculation starts from here for these categories.
    *   *Attributes:* **Geographical Location/Area**, Relevant Documentation (e.g., tree species collected).

*   **Feedstock Category (Woody Biomass):** Classification of the source material based on RSB-SA-01 requirements. Examples include Thinnings, Forestry Industry Processing Residues, SRWC, Roundwood, Invasive Alien Species. Specific requirements and eligibility criteria apply to each category.
    *   *Attributes:* **Category Type** (e.g., Thinnings, Processing Residues), **Specification Details** (e.g., definition of thinning, residue type). Linked to **RSB Certified Material**.

*   **Processing Residue:** Material category defined in RSB-PRO-20-001 and specified in RSB-SA-01 (e.g., sawmill residues, black liquor). Requires verification of eligibility. Source must have CoC certification for legality (for forestry processing residues).
    *   *Attributes:* (Inherits attributes from **RSB Certified Material**), **Verification Evidence**.

*   **Post-consumer Feedstock:** Material category defined in RSB-PRO-20-001 and RSB-STD-40-007 (adapted). Requires verification of eligibility. May be referred to as Waste from a post-consumer source.
    *   *Attributes:* (Inherits attributes from **RSB Certified Material**), **Verification Evidence**, **Point of Reclamation** (implied by collection from end-users).

*   **Supply Chain:** The sequence of stages (**Operator** links) through which **RSB certified material** passes, involving changes in legal and/or physical control. Traceability must be ensured through the chain.
    *   *Attributes:* Stages (feedstock production, processing, manufacturing, trading, distribution).

*   **Audit (Verification):** A process conducted by a **Certification Body** to assess an **Operator's** compliance with RSB standards. Includes checking records and systems. Supplier audits may be required.
    *   *Attributes:* **Audit ID** (implied), **Date(s)**, **Audited Operator ID**, **CB ID**, **Findings** (including Non-conformances).

*   **Non-conformance:** A failure to comply with an applicable RSB requirement, identified during an **Audit**. Requires corrective actions.
    *   *Attributes:* **Description**, Relevant **Requirement(s)** (implied), **Required Corrective Action**, Status (Open/Closed). Linked to an **Audit**.

*   **Supplier Audit Program:** A program required for certain **Supplier** types (Processing Residues, Post-consumer feedstock) where adequate evidence isn't available upon receipt.
    *   *Attributes:* **Program Details** (implied). Includes specific **Supplier(s)**. Involves **Audits** of suppliers.

*   **Supply Base Evaluation (SBE):** A process required for **Operators** sourcing from a defined Supply Base not fully covered by recognised certification or RRA. It includes **Risk Assessment**. Required for certain **Feedstock Categories** (Primary/Processing Residues not certified). Documented in an **SBR**.
    *   *Attributes:* Linked **Operator**, Date of Assessment (implied), Assessment Team Details (implied).

*   **Risk Assessment:** Part of the **SBE** process where an **Operator** evaluates the risk of non-conformance with RSB sustainability requirements (derived from Principles & Criteria) for sourced feedstock. Risks are rated as Low or Specified.
    *   *Attributes:* Linked **Supply Base** (implied by SBE), Date, Assessor Details (implied), **Risk Ratings** (Low/Specified) per indicator/criteria.

*   **Specified Risk:** A risk rating assigned when the risk of non-conformance is not negligible. It requires implementation of **Risk Management Measures**.
    *   *Attributes:* Linked **Requirement/Criterion** (implied), **Description of Risk** (implied), **Risk Rating** ('Specified').

*   **Risk Management Measure (RMM):** Actions implemented by an **Operator** to effectively reduce **Specified Risks** to a low level. Can include requirements from SBP-recognised schemes.
    *   *Attributes:* **Description of Measure**, Linked **Specified Risk(s)**, Means of Verification of effectiveness (implied).

*   **Supply Base Report (SBR):** A report prepared by the **Operator** documenting the **Supply Base Definition**, **SBE**, **Risk Assessment findings**, and **RMMs**. It is made available to **Stakeholders**.
    *   *Attributes:* Report ID (implied), Preparation Date, Linked **Operator**, Summary of Supply Base (implied), Summary of Risk Assessment findings (implied), Description of RMMs (implied).

*   **Supply Base Verifier (SBV):** Information or evidence used by an **Operator** to assess risks and conformance during the **SBE/Risk Assessment** process.
    *   *Attributes:* **Description of Verifier**, **Type of Evidence** (e.g., document, record, interview), Linked **Requirement(s)/Risks** (implied).

*   **Stakeholder:** Any person, group, or entity engaged by the **Operator** during the **SBE process** (referencing SBP Standard 2 requirements).
    *   *Attributes:* **Name/Organisation**, Contact Information (implied), **Engagement Records** (correspondence, comments, justification for withholding information). Feedback is provided to them.

*   **Due Diligence System (DDS):** While not formally defined as a top-level entity in these RSB excerpts, the concept is referenced via ISO 38200 and SBP Standard 2. The RSB system incorporates elements analogous to a DDS through requirements for **Supplier validation and monitoring** and the overall **risk-based approach** to feedstock sourcing. It represents a **process** used by the **Operator** to verify information about **Input Material** characteristics and compliance with requirements.

**Key Relationships Between Entities:**

Here are some of the critical relationships linking these entities, enabling traceability and data flow in the RSB CoC system:

*   An **Operator** *is certified under* an **RSB Certification Scheme**, *issued by* a **Certification Body (CB)** as an **RSB Certificate**.
*   An **RSB Certificate** *defines the Scope for* an **Operator**.
*   An **Operator** *implements* a **Chain of Custody System**.
*   A **Chain of Custody System** *uses* one or more **Chain of Custody Model(s)**.
*   An **Operator** *manages activities at* **Site(s)**.
*   A **Site** *may contain* **Process(es)**.
*   A **Process** *may use* **Conversion Factor(s)**.
*   An **Operator** *sources* **RSB Certified Material** *from* **Supplier(s)**.
*   An **Operator** *sells/forwards* **RSB Certified Material** *to* **Customer(s)**.
*   **Supplier(s)** *provide* **RSB Certified Material** *to* **Operator(s)**.
*   **Customer(s)** *receive* **RSB Certified Material** *from* **Operator(s)**.
*   **RSB Certified Material** *is represented in* **Batch(es)**.
*   **Batch(es)** *have associated* **Product Information**.
*   **Product Information** *is included on* **Sales Documentation**.
*   **Sales Documentation** *may serve as* **Proof of Sustainability (PoS)**.
*   **Sales Documentation** *records* a **Transaction** between a selling **Operator** and a buying **Customer**.
*   An **RSB Certification Scheme** *is associated with* **Sustainability Claim(s)**.
*   **RSB Certified Material** *carries* a **Sustainability Claim**. The claim is validated via the **Chain of Custody System/Model**.
*   A **Certification Body (CB)** *conducts* **Audit(s)/Verification(s)** *of* an **Operator**.
*   An **Audit** *may identify* **Non-conformance(s)**.
*   An **Operator** *implements* a **Supplier Audit Program** *for* specific **Supplier(s)** of **Processing Residues** and **Post-consumer Feedstock**.
*   An **Operator** *conducts* a **Supply Base Evaluation (SBE)** *for sourcing* certain **Feedstock Categories**.
*   A **Supply Base Evaluation (SBE)** *includes* a **Risk Assessment**.
*   A **Risk Assessment** *may identify* **Specified Risk(s)**.
*   An **Operator** *implements* **Risk Management Measure(s)** *to mitigate* **Specified Risk(s)**.
*   An **Operator** *uses* **Supply Base Verifier(s)** *in the* **SBE/Risk Assessment**.
*   An **Operator** *prepares* a **Supply Base Report (SBR)** *documenting the* **SBE, Risk Assessment, and RMMs**.
*   An **Operator** *engages with* **Stakeholder(s)** *during the* **SBE process**.
*   Specific **Feedstock Categories** (Woody Biomass) *have defined* **Requirements** in RSB-SA-01.
*   **Processing Residues** and **Post-consumer Feedstock** *are types of* **RSB Certified Material** requiring specific **Verification** by the Operator.
*   The **GHG Calculation** *starts from the* **Point of Origin** *for certain* **Feedstock Categories** (e.g., Thinnings, Roundwood).
*   An **Operator** *maintains records about* **Supplier(s)**, materials supplied, and certificate code.

This structure captures the essential components and their interconnections within the RSB Chain of Custody system, specifically referencing the details found in the provided RSB-PRO-20-001 and RSB-SA-01 sources. It highlights the flow of material, the roles of different parties, the documentation requirements, the verification processes, and the specific considerations for different types of woody biomass feedstock.
