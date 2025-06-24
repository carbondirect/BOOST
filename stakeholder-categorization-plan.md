# GitHub Discussions Categorization Plan

## Overview
This document outlines the plan to reorganize GitHub discussions by stakeholder domains to improve accessibility and relevance for different user groups.

## New Discussion Categories to Create

### 🌍 Land Management
**Description**: For forestry agencies, land managers, and sustainability oversight
**Color**: Green

### 🏥 Public Health  
**Description**: For health agencies, contamination tracking, and safety compliance
**Color**: Red

### 🌱 Environmental
**Description**: For environmental agencies, emissions tracking, and impact assessment  
**Color**: Light Green

### 💼 Commercial
**Description**: For private sector, supply chain management, and business operations
**Color**: Blue

### 🔍 Auditors & Certification
**Description**: For certification bodies, auditors, and verification specialists
**Color**: Purple

### 📊 General Schema
**Description**: For entities relevant across all domains and technical discussions
**Color**: Gray

## Discussion Migration Plan

### Land Management Category
Move these discussions:
- #92 Certificate (sustainable land management practices)
- #91 CertificationScheme (FSC, SBP standards) 
- #94 MaterialFeedstock (biomass origin, species)
- #90 Organization (land owners, forest managers)
- #95 Supplier (upstream verification)
- #103 VerificationStatement (land use assessments)
- #105 ProductGroup (forest product classification)

### Public Health Category  
Move these discussions:
- #94 MaterialFeedstock (GMO status, contamination)
- #101 EnergyCarbonData (air quality impacts)
- #98 TransactionBatch (health incident traceability)
- #100 SaleDeliveryDocument (emergency response)
- #90 Organization (facility oversight)
- #93 CertificationBody (safety compliance)

### Environmental Category
Move these discussions:
- #101 EnergyCarbonData (GHG emissions and carbon intensity data)
- #94 MaterialFeedstock (biodiversity impact)
- #99 Claim (environmental claims verification)
- #104 MassBalanceAccount (environmental credits)
- #97 TransactionConsignment (cross-border compliance)
- #92 Certificate (environmental standards)
- #103 VerificationStatement (environmental validation)

### Commercial Category
Move these discussions:
- #90 Organization (business relationships)
- #97 TransactionConsignment (supply chain logistics)
- #98 TransactionBatch (inventory management)
- #100 SaleDeliveryDocument (commercial documentation)
- #104 MassBalanceAccount (accounting systems)
- #95 Supplier (business relationships)
- #96 Customer (customer management)
- #92 Certificate (market access)
- #99 Claim (marketing claims)

### Auditors & Certification Category
Move these discussions:
- #92 Certificate (certification documents)
- #93 CertificationBody (verification organizations)
- #91 CertificationScheme (audit requirements)
- #103 VerificationStatement (audit trails)
- #99 Claim (claims verification)
- #101 EnergyCarbonData (energy and carbon data verification)
- #90 Organization (compliance status)
- #104 MassBalanceAccount (volume reconciliation)
- #98 TransactionBatch (traceability audits)

### General Schema Category
Keep these discussions:
- Any future discussions about overall data model
- Cross-cutting technical discussions
- Integration and API discussions

## Implementation Steps

### Step 1: Create Categories (Web Interface Required)
Repository admin creates the 6 new discussion categories through GitHub web interface:
1. Go to: `https://github.com/carbondirect/BOOST/settings/discussions`
2. Click "New category" for each category listed above

### Step 2: Get New Category IDs
After creating categories, run this command to get the new category IDs:
```bash
gh api graphql -f query='
query {
  repository(owner: "carbondirect", name: "BOOST") {
    discussionCategories(first: 15) {
      nodes {
        id
        name
        description
      }
    }
  }
}'
```

### Step 3: Move Discussions Using GraphQL API
Once you have the new category IDs, use these commands to move discussions:

```bash
# Example: Move Organization discussion to Land Management category
gh api graphql -f query='
mutation {
  updateDiscussion(input: {
    discussionId: "D_kwDOOb4UX84AgT9U"
    categoryId: "NEW_LAND_MANAGEMENT_CATEGORY_ID"
  }) {
    discussion {
      id
      title
      category {
        name
      }
    }
  }
}'
```

### Discussion IDs for Reference:
- Organization: `D_kwDOOb4UX84AgT9U`
- CertificationScheme: `D_kwDOOb4UX84AgT9Z`
- Certificate: `D_kwDOOb4UX84AgT9a`
- CertificationBody: `D_kwDOOb4UX84AgT9c`
- MaterialFeedstock: `D_kwDOOb4UX84AgT9e`
- Supplier: `D_kwDOOb4UX84AgT9g`
- Customer: `D_kwDOOb4UX84AgT9h`
- TransactionConsignment: `D_kwDOOb4UX84AgT9i`
- TransactionBatch: `D_kwDOOb4UX84AgT9j`
- Claim: `D_kwDOOb4UX84AgT9k`
- SaleDeliveryDocument: `D_kwDOOb4UX84AgT9l`
- SAR: `D_kwDOOb4UX84AgT9n`
- SREG: `D_kwDOOb4UX84AgT9s`
- VerificationStatement: `D_kwDOOb4UX84AgT9u`
- MassBalanceAccount: `D_kwDOOb4UX84AgT9v`
- ProductGroup: `D_kwDOOb4UX84AgT9w`

### Step 4: Automated Migration Script
I can create an automated script to move all discussions once you provide the new category IDs.

### Step 5: Update Templates and Documentation
Create discussion templates for each category focusing on domain-specific feedback.

## Benefits

- **Targeted Navigation**: Stakeholders can focus on entities most relevant to their work
- **Improved Engagement**: Domain-specific context increases relevance and participation
- **Clearer Organization**: Reduces cognitive load for users reviewing entity schemas
- **Cross-Domain Visibility**: Entities appearing in multiple categories show interconnectedness
- **Professional Presentation**: Demonstrates understanding of diverse stakeholder needs

## Note on Implementation

Since creating discussion categories requires repository admin access through the web interface, this plan should be implemented by someone with appropriate permissions. The ERD navigator has already been updated to reflect this new organization structure.