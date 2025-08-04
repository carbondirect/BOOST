# ProductGroup

## ProductGroup

### Overview
The `ProductGroup` object represents a distinct category of materials or products, classified based on shared characteristics such as origin, transformation method, and chain-of-custody rules. These groups support traceability, classification, and certification alignment in biomass and materials supply chains. The primary key is `productGroupId`.

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
<td>`productGroupId`
<td>string
<td>Yes
<td>Unique identifier for the product group (primary key)
<td>`PG-FS-BIOCHAR-001`
</tr>
<tr>
<td>`productGroupName`
<td>string
<td>Yes
<td>Commercial or descriptive name of the product group
<td>`Forest Slash-Derived Biochar`
</tr>
<tr>
<td>`productCategory`
<td>string
<td>Yes
<td>High-level category of the product (enum)
<td>`solid_biomass`, `liquid_biofuel`, `biogas`
</tr>
<tr>
<td>`classification`
<td>string
<td>No
<td>Industry or regulatory classification code
<td>`ISO 17225-8`, `ISCC-EU-205`
</tr>
<tr>
<td>`description`
<td>string
<td>Yes
<td>Detailed description of the product group and its characteristics
<td>`Forest Slash-Derived Biochar (Western U.S., Wildfire Mitigation)`
</tr>
<tr>
<td>`typicalUses`
<td>array&lt;string&gt;
<td>No
<td>Common applications and end-uses for products in this group
<td>`["Soil amendment", "Carbon sequestration"]`
</tr>
<tr>
<td>`qualityStandards`
<td>array&lt;string&gt;
<td>No
<td>Quality standards and specifications applicable to this group
<td>`["IBI Biochar Standards", "EBC Premium Grade"]`
</tr>
<tr>
<td>`certificationRequirements`
<td>array&lt;string&gt;
<td>No
<td>Required certification schemes for this product group
<td>`["FSC Controlled Wood", "SBP-compliant biomass"]`
</tr>
<tr>
<td>`regulatoryClassification`
<td>string
<td>No
<td>Regulatory status or classification
<td>`"Biomass Byproduct - CAR Protocol"`
</tr>
<tr>
<td>`relatedMaterials`
<td>array&lt;object&gt;
<td>No
<td>Materials that belong to this product group
<td>See Material Object below
</tr>
<tr>
<td>`@id`
<td>string (uri)
<td>Yes
<td>Unique URI identifier for JSON-LD
<td>`https://github.com/carbondirect/BOOST/schemas/product-group/PG-001`
</tr>
<tr>
<td>`lastUpdated`
<td>string (date-time)
<td>No
<td>Timestamp of the most recent data update
<td>`2025-07-01T15:00:00Z`
</tr>
</tbody>
</table>
---

### Material Object

<table class="data">
<thead>
<tr>
<th>Field
<th>Type
<th>Required
<th>Description
</tr>
</thead>
<tbody>
<tr>
<td>`id`
<td>string
<td>Yes
<td>ID of the material
</tr>
<tr>
<td>`@type`
<td>string
<td>Yes
<td>Should equal `Material`
</tr>
</tbody>
</table>
---

### Example Use Cases

1. **Forest Slash-Derived Biochar**
     Category: solid_biomass
     Uses: Soil amendment, carbon sequestration
     Standards: IBI Biochar Standards, EBC Premium Grade
     Certifications: FSC Controlled Wood, SBP-compliant biomass

2. **Refined Bio-oil**
     Category: liquid_biofuel
     Uses: Transportation fuel, industrial heating
     Standards: EN 14214, ASTM D6751
     Certifications: ISCC EU, RSB Global

### Relationships
- Organization defines multiple ProductGroups
- ProductGroup is tracked by MassBalanceAccount
- ProductGroup categorizes multiple Materials
- Certificate certifies multiple ProductGroups