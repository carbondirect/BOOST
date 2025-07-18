# BOOST <> Dept. of Conservation

---

## Outline

- BOOST Overview (5-10 minutes)
- Discuss Agency Engagement (10-15 minutes)
- Review BOOST Entity-Relationship Diagram (20-30 minutes)
    - *DISCUSSION:* Are we missing entities?
    - Specific entities *DISCUSSION*:
        - Do we have the right attributes? 
        - What are we missing?
- Discuss possible phase 2 pilot development

Note: 
- We are hosting targeted meetings with CA agencies to ensure we understand need 
- Version 0.1 will be released in Q2 of 2025.


---

<img src="img/boost_logo.png" alt="logo" style="height: 400px;">

--

## What BOOST is


- A specification defining data formats, field definitions, and validation rules
- A common vocabulary enabling consistent interpretation of biomass chain-of-custody information
- A framework establishing relationships between different types of information
- A validation mechanism ensuring data quality and consistency

--

## What BOOST Is Not

- **Not Software**: BOOST does not prescribe specific applications, databases, or user interfaces. 
- **Not a Database**: BOOST does not create centralized storage or control where data resides. 
- **Not Dashboards or Analytics**: BOOST does not define how data should be visualized or analyzed. 
- **Not a Certification Scheme**: BOOST does not establish sustainability criteria or certification requirements. 

Note: 
- **Not Software** Organizations remain free to choose their preferred software platforms while adhering to BOOST data exchange requirements. 
- **Not Database** Each organization maintains control over their data while following standard formats for sharing.
- **Not Dashboards or Analytics**: It provides the foundation that enables various analytical tools to work with standardized data.
- **Not a Certification Scheme**: It provides the structure for documenting compliance with existing schemes.

--

## WHAT are the goals

*To improve transparency, verification and trust in biomass supply chains*

*Reduce operational costs and increase access to markets for biomass producers and consumers*

---

## Agency Egagement

- **CDFA** `DONE` 
- **CalRecycle** *Scheduled*
- **CPUC** *Scheduled*
- **CARB** *Scheduled*
- **CalFire** *TBS*

Note: 
- **CDFA** Added addtional entities/attributes to development backlog for
    - LocationHistory
	- ProcessingHistory
	- Material caratersistics (Composting, etc)
     - piece size
     - anatomical part (bark, leaves, seed, hull, mixed)
     - C:N ratio
 - Reporting : volume-based exemmptions

---

## Stakeholder Egagement 

- LCFS reporting workflow review
    - Loamist + Allotrope

Note:
- How does LCFS reporting functionally work?

---

## Core Components of the CoC Data Standard

*DRAFT* [Entity Relationship Diagram](https://carbondirect.github.io/BOOST/erd-navigator/)

**Framing Questions**

+ *Did we get the right set of entities?*
+ *Did we get the right attributes for entities you care about?*
+ *Are the relationships between entities appropriate?*

Note: 
- how to integrate with DoC geological and resource mapping databases, 
- support environmental permitting coordination across agencies
