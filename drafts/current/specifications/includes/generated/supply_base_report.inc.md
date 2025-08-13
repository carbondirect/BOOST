<!-- Auto-generated from supply_base_report/validation_schema.json -->

SupplyBaseReport entity in BOOST data model

**🗂️ [View Supply Base Report in ERD Navigator](erd-navigator/index.html?focus=SupplyBaseReport)**

### Relationships ### {{.unnumbered}}

- **organizationId** → [[#organization|Organization]]

### Properties ### {{.unnumbered}}

<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Description
<th>Required
</tr>
</thead>
<tbody>
<tr>
<td><code>@context</code>
<td>object (structured)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@id</code>
<td>string (uri)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>@type</code>
<td>enum(SupplyBaseReport)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>organizationId</code>
<td>string
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>preparationDate</code>
<td>string (date)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>sbrId</code>
<td>string (pattern)
<td>No description provided
<td>✓
</tr>
<tr>
<td><code>publicationUrl</code>
<td>string (uri)
<td>No description provided
<td>
</tr>
<tr>
<td><code>reportGeographicDataId</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>sourcingPractices</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>supplyBaseIds</code>
<td>array&amp;lt;string&amp;gt;
<td>Array of SupplyBase IDs that this report covers
<td>
</tr>
<tr>
<td><code>supplyBaseSummary</code>
<td>string
<td>No description provided
<td>
</tr>
<tr>
<td><code>sustainabilityMeasures</code>
<td>string
<td>No description provided
<td>
</tr>
</tbody>
</table>

## SupplyBaseReport
### Overview
The `SupplyBaseReport` entity manages sustainability reporting documentation for supply base operations within the BOOST traceability system. Supply Base Reports are comprehensive documents that detail sustainability practices, environmental management, social considerations, and operational performance across defined supply base areas. This entity supports regulatory compliance, certification requirements, stakeholder communication, and continuous improvement tracking for sustainable forest management operations.
### Fields
<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Required
<th>Description
<th>Examples
</tr>
</thead>
<tbody>
<tr>
<td>`sbrId`
<td>string
<td>Yes
<td>Unique identifier for the supply base report (primary key)
<td>`SBR-001`, `SBR-KLAMATH-2024-ANNUAL`
</tr>
<tr>
<td>`organizationId`
<td>string (FK)
<td>Yes
<td>Foreign key to organization preparing the report
<td>`ORG-PACIFIC-FOREST-001`, `ORG-KLAMATH-HARVEST`
</tr>
<tr>
<td>`preparationDate`
<td>string (date)
<td>Yes
<td>Date when the report was prepared or finalized
<td>`2024-03-31`, `2024-12-31`
</tr>
<tr>
<td>`supplyBaseSummary`
<td>string
<td>No
<td>Executive summary of supply base operations and performance
<td>`Annual report covering 75,000 acres of sustainably managed forest operations`
</tr>
<tr>
<td>`sourcingPractices`
<td>string
<td>No
<td>Description of sourcing practices and methodologies
<td>`Selective harvesting with ecosystem-based management principles`
</tr>
<tr>
<td>`sustainabilityMeasures`
<td>string
<td>No
<td>Summary of sustainability measures and performance indicators
<td>`Biodiversity conservation, water quality protection, carbon sequestration`
</tr>
<tr>
<td>`publicationUrl`
<td>string (uri)
<td>No
<td>URL where the complete report is publicly accessible
<td>`https://reports.company.com/supply-base/SBR-KLAMATH-2024.pdf`
</tr>
<tr>
<td>`reportGeographicDataId`
<td>string (FK)
<td>No
<td>Foreign key to geographic area covered by report
<td>`GEO-SUPPLY-BASE-KLAMATH-001`, `GEO-REGION-PACIFIC-NW`
</tr>
<tr>
<td>`supplyBaseIds`
<td>array&lt;string&gt;
<td>No
<td>Array of supply base identifiers covered by this report
<td>`["SB-KLAMATH-FOREST", "SB-CASCADE-REGION", "SB-OLYMPIC-UNIT"]`
</tr>
<tr>
<td>`reportingPeriod`
<td>string
<td>No
<td>Time period covered by the report
<td>`2024 Annual Report`, `Q1-Q3 2024`, `January 1 - December 31, 2024`
</tr>
<tr>
<td>`certificationCompliance`
<td>array&lt;string&gt;
<td>No
<td>Certification schemes addressed in the report
<td>`["FSC Forest Management", "SFI Forest Management", "PEFC Sustainable Forest Management"]`
</tr>
<tr>
<td>`stakeholderEngagement`
<td>string
<td>No
<td>Summary of stakeholder consultation and engagement activities
<td>`Community meetings, indigenous consultation, environmental group engagement`
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/supply-base-report/SBR-001`
</tr>
</tbody>
</table>
### Report Types
1. **Annual Sustainability Report**
    - Comprehensive yearly performance assessment
    - Financial, environmental, and social performance metrics
    - Stakeholder engagement and community impact summary
    - Continuous improvement goals and achievements
2. **Certification Compliance Report**
    - Specific reporting for certification scheme requirements
    - FSC, SFI, PEFC, or other certification standard compliance
    - Audit findings and corrective action implementation
    - Certificate maintenance and renewal documentation
3. **Regulatory Compliance Report**
    - Government agency reporting requirements
    - Environmental impact assessment updates
    - Endangered species protection compliance
    - Water quality and air quality monitoring results
4. **Stakeholder Communication Report**
    - Public disclosure of sustainability practices
    - Community engagement and social impact assessment
    - Indigenous rights and consultation documentation
    - Transparency and accountability demonstration
### Key Components
1. **Supply Base Description**
    - Geographic boundaries and area coverage
    - Forest type and species composition
    - Ownership structure and management arrangements
    - Infrastructure and operational capabilities
2. **Sustainability Performance**
    - Environmental protection measures and outcomes
    - Biodiversity conservation initiatives and results
    - Carbon sequestration and climate change mitigation
    - Water quality protection and monitoring
3. **Social Responsibility**
    - Community engagement and consultation processes
    - Indigenous rights recognition and implementation
    - Worker safety and welfare programs
    - Local economic impact and development
4. **Economic Viability**
    - Financial performance and operational efficiency
    - Market access and customer satisfaction
    - Innovation and technology adoption
    - Long-term economic sustainability
### Reporting Standards
1. **Global Reporting Initiative (GRI)**
    - Internationally recognized sustainability reporting framework
    - Comprehensive environmental, social, and governance metrics
    - Stakeholder engagement and materiality assessment
    - Standardized performance indicators and disclosure requirements
2. **Forest Stewardship Council (FSC) Requirements**
    - Annual surveillance report requirements
    - Management plan implementation and monitoring
    - Stakeholder consultation documentation
    - Continuous improvement demonstration
3. **Sustainable Forestry Initiative (SFI) Standards**
    - Annual progress report on SFI objectives
    - Fiber sourcing and procurement practice documentation
    - Conservation and biodiversity protection measures
    - Community engagement and outreach activities
4. **Sustainable Biomass Partnership (SBP) Framework**
    - Supply base evaluation and risk assessment
    - Mitigation measure implementation and effectiveness
    - Monitoring and verification system performance
    - Continuous improvement and adaptive management
### Key Features
1. **Multi-Standard Compliance**
    - Integration of multiple certification scheme requirements
    - Comprehensive coverage of sustainability dimensions
    - Alignment with international reporting standards
    - Streamlined reporting for multiple audiences
2. **Geographic Integration**
    - Spatial analysis and mapping of operations
    - Geographic information system (GIS) integration
    - Regional and landscape-level impact assessment
    - Multi-jurisdictional compliance coordination
3. **Performance Monitoring**
    - Key performance indicator tracking and analysis
    - Environmental monitoring data integration
    - Social impact measurement and evaluation
    - Economic performance assessment and benchmarking
4. **Stakeholder Transparency**
    - Public accessibility and transparency
    - Stakeholder feedback integration
    - Community consultation documentation
    - Third-party verification and validation
### Example Use Cases
1. **FSC Forest Management Annual Report**
    - Report Type: Annual certification compliance report
    - Coverage: 50,000-acre FSC-certified forest management unit
    - Content: Environmental monitoring, social engagement, economic performance
    - Audience: FSC auditors, stakeholders, local communities
    - Publication: Public website with full transparency
2. **SBP Supply Base Evaluation Report**
    - Report Type: Biomass sustainability assessment
    - Coverage: Regional biomass supply base covering multiple counties
    - Content: Risk assessment, mitigation measures, monitoring results
    - Audience: SBP certification body, biomass customers, regulators
    - Publication: SBP public database and company website
3. **Integrated Multi-Standard Report**
    - Report Type: Comprehensive sustainability report
    - Coverage: Large integrated forest products company operations
    - Content: FSC, SFI, and PEFC compliance plus GRI framework
    - Audience: Multiple certification bodies, investors, communities
    - Publication: Annual report with detailed appendices
### Validation Rules
1. **Report Requirements**
    - sbrId must be unique across system
    - organizationId must reference valid Organization
    - preparationDate must be valid date format
    - Report must cover defined time period and geographic area
2. **Content Consistency**
    - supplyBaseIds must reference valid SupplyBase entities
    - reportGeographicDataId must encompass all covered supply bases
    - Certification compliance must align with organization certificates
    - Performance data must be supported by monitoring evidence
3. **Publication Standards**
    - publicationUrl must be accessible if provided
    - Report must meet applicable transparency requirements
    - Stakeholder consultation must be documented appropriately
    - Third-party verification must be completed if required
### Relationships
- SupplyBaseReport prepared by one Organization
- SupplyBaseReport covers multiple SupplyBase entities
- SupplyBaseReport documents geographic area through GeographicData reference
- SupplyBaseReport supports Certificate maintenance and compliance verification
- SupplyBaseReport enables stakeholder transparency and regulatory compliance
