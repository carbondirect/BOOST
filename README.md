# Biomass Chain of Custody (CoC) Data Standard Community Group

## Overview
This repository contains the working draft and artifacts of the Biomass Chain of Custody (CoC) Data Standard, which defines a robust and interoperable data model for tracking biomass through complex supply chains. The standard supports transparent, verifiable, and consistent data exchange to enable sustainability, regulatory compliance, and supply chain integrity.

- **Charter:** 
- **Charter Effective Date:** 
- **Last Modified:** 

Feedback and contributions are welcomed via GitHub Issues and Pull Requests at [BOOST](https://github.com/carbondirect/BOOST).

W3C Community Group page: [BOOST-01](https://www.w3.org/community/boost-01/)


## Repo Structure:

*draft_coc_standards*: contains LaTex documents for existing chain of custody data standard definitions.

*entity_relationship_diagrams*: contains svg and png diagrams for specific CoC standards and associated data schemes. 



---

## Goals
The goals of the Biomass CoC Data Standard Community Group are to:
- Define an extensible and flexible data standard for use in biomass Chain of Custody systems. 
- Enable auditable tracking of biomass materials across the supply chain.
- Support certification and reporting schemes such as SBP, FSC, RSB, CalRecycle, LCFS, etc.
- Represent Chain of Custody (CoC) models including mass balance, physical separation, and crediting.
- Enable the creation of software to automate tracking and validation. 
- Promote interoperability across systems used by suppliers, regulators, certifiers, and end users.

---

## Scope
The standard will cover:
- **Organizations**: legal entities involved in handling or transferring biomass.
- **Biomass Consignments**: representations of batches or transactions of biomass.
- **Biomass Categories and Types**: classification schemes based on source and processing.
- **Sustainability Attributes**: including GHG data, certification, claims, and source details.
- **CoC Control Models**: mass balance, physical segregation, crediting.
- **Mass Balance Accounts**: tracking input and output flows.
- **Verification Statements and Certificates**: issued by third parties.
- **Transaction Documentation**: sales and delivery records.
- **Emission Reporting Fields**: data needed for SAR/SREG forms.

The standard will be designed for technical implementation using formats such as JSON Schema, XML, and RDF.

### Out of Scope
- Setting sustainability criteria (handled by regulatory and certification bodies).
- GHG emission methodologies (defined by various standards and entities).
- Audit and verification procedures.
- Certification scheme design and governance.
- Legal interpretation of contracts or organizational liability.

---

## Deliverables
- **Specification**: formal definition of high-level entities, fields, relationships, and control models.
- **Entity-Relationship Diagrams (ERDs)**: visual representations of data relationships.
- **JSON Payload Examples**: showing valid structure for common data flows.
- **Validation Schemas**: for checking data conformity.
- **Test Suites**: optional support for validation and implementation testing.
- **Reference Implementations**: optional tools and libraries.

---

## Why This Standard Matters

### Data Standards in Chain of Custody Systems
Chain of custody systems depend on data standards to ensure:
- Consistency in how data is captured and interpreted
- Secure and traceable tracking of transactions and materials
- Transparent and auditable verification of sustainability claims
- Reduce duplication of effort throughout the supply chain. 

### Key Elements of a CoC Data Standard
- **Identification Fields**: unique and structured item identifiers
- **Handler Information**: metadata about entities processing or transferring materials
- **Temporal and Location Data**: timestamps and location metadata for traceability
- **Authentication Metadata**: certificates, signatures, or third-party verification

### Role in Interoperability
Standardized data formats make it possible to:
- Share records across jurisdictions and organizations
- Integrate with legacy systems, regulatory platforms, and certification databases
- Maintain traceability across multi-step, multi-actor supply chains
- Automate validation between and within different chain of custody standards.

### Validation and Compliance
Validation rules help ensure:
- Required fields are present and correctly formatted
- Field types and constraints are respected
- Data supports legal and certification requirements

---

## Contribution Guidelines (make sure these are updated)
Participation is open to all. Contributors must agree to the W3C Community Contributor License Agreement (CLA). Contributions are welcome through:
- GitHub Pull Requests
- GitHub Issues
- Comments and discussion threads

---

## Governance
This group operates under the W3C Community and Business Group Process. Decisions are made by consensus and tracked in GitHub. Chair selection, amendments to the charter, and governance rules follow formal community group practices.

---

## Contact and Participation
- Open an issue or submit a PR at [TBD: GitHub Repository URL]
- Join the W3C Community Group (link TBD)

---
