# BOOST Community Group Update: ERD Navigator and Entity Schema Review

**Subject:** Introducing the BOOST ERD Navigator - Your Input Needed on Core Entity Schemas

---

Dear BOOST Community Group Members,

We're excited to share a significant milestone in the development of the Biomass Open Origin Standard for Tracking (BOOST). We've launched an interactive **Entity Relationship Diagram (ERD) Navigator** that maps out the core data structure for biomass chain of custody tracking, and we need your expertise to help refine it.

## What We've Built

**🗂️ ERD Navigator:** An interactive web tool that visualizes the 17 core entities that form the foundation of BOOST's data standard. You can explore the complete data model, zoom in on specific relationships, and jump directly to detailed discussions about each entity.

**📍 Access the Navigator:** [https://github.com/carbondirect/BOOST/tree/main/erd-navigator](https://github.com/carbondirect/BOOST/tree/main/erd-navigator)

**💬 GitHub Discussions:** Each of the 17 entities has a dedicated discussion thread where we're gathering detailed feedback on schema design, attributes, and real-world applicability.

## Where We Are in Development

BOOST is currently in the **entity schema design phase**. We've consolidated our research from multiple certification programs (SBP, FSC, PEFC, RSB, LCFS, RFS, and others) into a focused set of 17 core entities that capture the essential data needed for biomass supply chain tracking:

- **Organizations & Certification:** Organization, Certificate, CertificationScheme, CertificationBody
- **Materials & Supply Chain:** Material, Supplier, Customer, Transaction, TransactionBatch
- **Claims & Verification:** Claim, SalesDeliveryDocument, VerificationStatement
- **Mass Balance & Tracking:** MassBalanceAccount, ProductGroup, EnergyCarbonData
- **Compliance & Reporting:** SupplyBaseReport, Audit

This represents a practical, implementable model that balances comprehensive tracking with real-world usability.

## What We're Asking For

**We're not expecting everyone to comment on everything.** Instead, we encourage you to engage where your expertise and interests align:

### 🎯 **Engage Where You Have Expertise**
- **Supply chain operators:** Focus on entities like Material, Transaction, Supplier/Customer
- **Certification bodies:** Review Certificate, CertificationScheme, Audit entities
- **Software developers:** Examine data types, relationships, and integration challenges
- **Regulatory experts:** Assess compliance-related entities like VerificationStatement, SupplyBaseReport
- **NGOs and sustainability advocates:** Evaluate tracking capabilities for environmental and social criteria

### 🔍 **Types of Feedback We Value**
- **Field completeness:** Are we missing critical attributes?
- **Data types:** Are the proposed data structures realistic and implementable?
- **Real-world applicability:** Will this work with your current systems and processes?
- **Validation requirements:** What business rules and constraints are essential?
- **Integration challenges:** What obstacles do you foresee in adoption?

### 📝 **How to Participate**
1. **Explore the ERD Navigator** to understand the overall data model
2. **Click on entities** that relate to your work or interests
3. **Join the GitHub discussions** for those specific entities
4. **Share your perspective** - even brief comments are valuable

**New to GitHub?** No problem! Creating a free account takes just 2 minutes: [github.com/signup](https://github.com/signup)

## Why This Matters

Your feedback during this schema design phase directly influences the final standard. The decisions we make now about data structure, required fields, and relationships will impact:

- How easily systems can integrate with BOOST
- What information can be tracked and verified
- How effectively the standard serves different stakeholder needs
- The operational burden on supply chain participants

## Timeline

We're seeking feedback over the **next 4-6 weeks** to finalize the core entity schemas. This will enable us to move forward with detailed JSON schema development, validation rules, and pilot implementations.

## Questions or Alternative Feedback Channels

If you prefer email over GitHub, you can also send feedback to: **public-boost-01@w3.org**

For technical questions about the ERD Navigator or discussion process, feel free to reach out directly.

---

Thank you for your continued participation in developing this critical infrastructure for biomass supply chain transparency. Your diverse perspectives and real-world experience are essential to creating a standard that truly serves the biomass community.

Best regards,

The BOOST Community Group Coordinators

---
*This email was sent to BOOST W3C Community Group members. To modify your participation or learn more about BOOST, visit: https://www.w3.org/community/boost/*