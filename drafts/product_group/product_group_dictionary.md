# Data Dictionary

## ProductGroup

### Overview
The `ProductGroup` object represents a distinct category of materials or products, classified based on shared characteristics such as origin, transformation method, and chain-of-custody rules. These groups support traceability, classification, and certification alignment in biomass and materials supply chains. The primary key is `productGroupId`.

### Fields

| Field                         | Type             | Required | Description                                                                 | Examples                                    |
|------------------------------|------------------|----------|-----------------------------------------------------------------------------|---------------------------------------------|
| `productGroupId`             | string           | Yes      | Unique identifier for the product group (primary key)                      | `PG-FS-001`                                 |
| `productTypeDescription`     | string           | Yes      | Commercial or descriptive name of the product group                        | `Pelletized Biofuel from Forest Slash`      |
| `feedstockClassificationRules` | string         | Yes      | Rules defining acceptable raw inputs and sourcing requirements             | `Must consist of non-merchantable forest residues...` |
| `relatedTransactionConsignments` | array<object> | No       | Links to transactions using this product group                             | See Transaction Consignment Object below     |
| `relatedMaterialFeedstocks`  | array<object>    | No       | Raw material feedstocks included in this group                             | See Material Feedstock Object below          |
| `relatedCertificates`        | array<object>    | No       | Certifications relevant to this product group                              | See Certificate Object below                 |
| `lastUpdated`                | string (date-time) | No     | Timestamp of the most recent data update                         | `2025-07-01T15:00:00Z`                       |

---

### Transaction Consignment Object

| Field   | Type   | Required | Description                            |
|---------|--------|----------|----------------------------------------|
| `id`    | string | Yes      | Unique ID of the consignment           |
| `@type` | string | Yes      | Should equal `TransactionConsignment` |

---

### Material Feedstock Object

| Field   | Type   | Required | Description                           |
|---------|--------|----------|---------------------------------------|
| `id`    | string | Yes      | ID of the feedstock source or lot     |
| `@type` | string | Yes      | Should equal `MaterialFeedstock`      |

---

### Certificate Object

| Field   | Type   | Required | Description                      |
|---------|--------|----------|----------------------------------|
| `id`    | string | Yes      | ID of the associated certificate |
| `@type` | string | Yes      | Should equal `Certificate`       |

---

### Example Use Cases

- **Forest Slash**: Residuals from wildfire mitigation or thinning, traceable through FSC Controlled Wood.
- **Engineered Hardwood**: Multi-layer flooring product with certified veneer and recycled HDF core.
=