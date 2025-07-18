# Data Dictionary

## ProductGroup

### Overview
The `ProductGroup` object represents a distinct category of materials or products, classified based on shared characteristics such as origin, transformation method, and chain-of-custody rules. These groups support traceability, classification, and certification alignment in biomass and materials supply chains. The primary key is `productGroupId`.

### Fields

| Field                         | Type             | Required | Description                                                                 | Examples                                    |
|------------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `productGroupId`             | string           | Yes      | Unique identifier for the product group (primary key)                      | `PG-FS-BIOCHAR-001`                         |
| `productGroupName`           | string           | Yes      | Commercial or descriptive name of the product group                        | `Forest Slash-Derived Biochar`              |
| `productCategory`            | string           | Yes      | High-level category of the product (enum)                                  | `solid_biomass`, `liquid_biofuel`, `biogas` |
| `classification`             | string           | No       | Industry or regulatory classification code                                  | `ISO 17225-8`, `ISCC-EU-205`               |
| `description`                | string           | Yes      | Detailed description of the product group and its characteristics          | `Forest Slash-Derived Biochar (Western U.S., Wildfire Mitigation)` |
| `typicalUses`                | array<string>    | No       | Common applications and end-uses for products in this group                | `["Soil amendment", "Carbon sequestration"]` |
| `qualityStandards`           | array<string>    | No       | Quality standards and specifications applicable to this group              | `["IBI Biochar Standards", "EBC Premium Grade"]` |
| `certificationRequirements`  | array<string>    | No       | Required certification schemes for this product group                      | `["FSC Controlled Wood", "SBP-compliant biomass"]` |
| `regulatoryClassification`   | string           | No       | Regulatory status or classification                                        | `"Biomass Byproduct - CAR Protocol"`        |
| `relatedMaterials`          | array<object>    | No       | Materials that belong to this product group                                | See Material Object below                    |
| `@id`                        | string (uri)     | Yes      | Unique URI identifier for JSON-LD                                         | `https://github.com/carbondirect/BOOST/schemas/product-group/PG-001` |
| `lastUpdated`                | string (date-time)| No      | Timestamp of the most recent data update                                  | `2025-07-01T15:00:00Z`                      |

---

### Material Object

| Field   | Type   | Required | Description                           |
|---------|--------|----------|---------------------------------------|
| `id`    | string | Yes      | ID of the material                    |
| `@type` | string | Yes      | Should equal `Material`               |

---

### Example Use Cases

1. **Forest Slash-Derived Biochar**
   - Category: solid_biomass
   - Uses: Soil amendment, carbon sequestration
   - Standards: IBI Biochar Standards, EBC Premium Grade
   - Certifications: FSC Controlled Wood, SBP-compliant biomass

2. **Refined Bio-oil**
   - Category: liquid_biofuel
   - Uses: Transportation fuel, industrial heating
   - Standards: EN 14214, ASTM D6751
   - Certifications: ISCC EU, RSB Global

### Relationships
- Organization defines multiple ProductGroups
- ProductGroup is tracked by MassBalanceAccount
- ProductGroup categorizes multiple Materials
- Certificate certifies multiple ProductGroups