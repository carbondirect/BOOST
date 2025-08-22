# **BOOST-ISEAL Chain of Custody Conformance Enhancement Plan**

## **Executive Summary** {#executive-summary}

This plan addresses critical gaps between the BOOST data standard and ISEAL Chain of Custody reference requirements to achieve full conformance with international CoC standards. Drawing on comprehensive analysis of the ISEAL Chain of Custody Models and Definitions v2 (2025), this enhancement plan identifies five critical areas requiring schema modifications to support explicit CoC model specification, system boundary management, and attribution methods while maintaining BOOST's advanced biomass-specific tracking capabilities.

**Current BOOST-ISEAL Conformance Score: 7/10**
**Target Post-Enhancement Score: 10/10**

### **Key Findings and Rationale**

Stakeholder analysis reveals that **BOOST provides superior foundational traceability infrastructure** compared to typical CoC implementations, with advanced features including biometric identification, multi-species tracking, and comprehensive volume reconciliation. However, explicit compliance with ISEAL standards requires formal CoC model specifications and system boundary controls that are currently implicit in the BOOST architecture.

The rationale for these enhancements rests on the critical need to support certification under ISEAL-aligned standards (FSC, PEFC, SBP, ISCC) while preserving BOOST's innovative biomass-specific capabilities. If implemented, this system could provide the most comprehensive CoC framework available for biomass supply chains.

---

## **Phase 1: Critical Compliance Infrastructure (Months 1-2)** {#phase-1}

### **1.1 CoC Model Specification Framework**

#### **Enhancement: Add CoC Model Field to TraceableUnit**

**Background**: ISEAL defines six distinct CoC models (Identity Preservation, Segregation, Controlled Blending, Mass Balance, Controlled Mass Balance, Book and Claim), each with specific requirements for material tracking and claim attribution.

**CoC Specifications**: 
- **Identity Preservation**: Materials from single source kept separate from all other materials
- **Segregation**: Certified materials kept separate from non-certified materials  
- **Mass Balance**: Certified and non-certified materials can be mixed with proportional attribution
- **Book and Claim**: Physical and administrative transfer decoupled entirely

```json
{
  "cocModel": {
    "type": "string",
    "enum": [
      "identity_preservation",
      "segregation", 
      "controlled_blending",
      "mass_balance",
      "controlled_mass_balance",
      "book_and_claim"
    ],
    "description": "ISEAL-compliant CoC model applied to this TRU"
  },
  "cocModelJustification": {
    "type": "string",
    "description": "Rationale for CoC model selection based on material characteristics and market requirements"
  }
}
```

**Implications**: Enables explicit CoC model tracking at the TRU level, supporting mixed-model supply chains where different materials follow different CoC requirements.

#### **Enhancement: System Boundary Entity**

**Background**: ISEAL requires clear definition of spatial and temporal boundaries within which CoC control is exercised.

```json
{
  "schema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://github.com/carbondirect/BOOST/schemas/system-boundary",
    "title": "System Boundary",
    "description": "ISEAL-compliant CoC system boundary definition",
    "type": "object",
    "properties": {
      "systemBoundaryId": {
        "type": "string",
        "pattern": "^SB-[A-Z0-9-_]+$"
      },
      "boundaryType": {
        "type": "string",
        "enum": ["organizational", "facility", "process_line", "product_group"]
      },
      "spatialBoundary": {
        "type": "string",
        "description": "Geographic or facility boundaries for CoC control"
      },
      "temporalRestrictions": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "restrictionType": {"type": "string"},
            "timeFrame": {"type": "string"},
            "justification": {"type": "string"}
          }
        }
      },
      "reconciliationPeriod": {
        "type": "string",
        "enum": ["daily", "weekly", "monthly", "quarterly", "annual"]
      },
      "organizationId": {
        "type": "string",
        "pattern": "^ORG-[A-Z0-9-_]+$"
      }
    }
  }
}
```

### **1.2 Attribution Method Framework**

#### **Enhancement: Attribution Specification in MaterialProcessing**

**Background**: ISEAL distinguishes between proportional attribution (matching physical blending) and non-proportional attribution (administrative allocation independent of physical mixing).

```json
{
  "attributionMethod": {
    "type": "string", 
    "enum": ["proportional", "non_proportional"],
    "description": "Method for assigning specified characteristics to outputs"
  },
  "attributionJustification": {
    "type": "string",
    "description": "Rationale for attribution method selection"
  },
  "attributionRules": {
    "type": "array",
    "items": {
      "type": "object", 
      "properties": {
        "inputCharacteristic": {"type": "string"},
        "outputAllocation": {"type": "number"},
        "allocationBasis": {"type": "string"}
      }
    }
  }
}
```

---

## **Phase 2: Product Group and Reconciliation Enhancement (Months 3-4)** {#phase-2}

### **2.1 Product Group Entity**

**Background**: ISEAL requires grouping of products treated as equivalent for tracking and reconciliation purposes.

```json
{
  "schema": {
    "$schema": "http://json-schema.org/draft-07/schema#", 
    "$id": "https://github.com/carbondirect/BOOST/schemas/product-group",
    "title": "Product Group",
    "description": "ISEAL-compliant product equivalency groups",
    "type": "object",
    "properties": {
      "productGroupId": {
        "type": "string",
        "pattern": "^PG-[A-Z0-9-_]+$"
      },
      "groupName": {
        "type": "string"
      },
      "equivalencyRules": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "criterion": {"type": "string"},
            "tolerance": {"type": "number"},
            "justification": {"type": "string"}
          }
        }
      },
      "systemBoundaryId": {
        "type": "string",
        "pattern": "^SB-[A-Z0-9-_]+$"
      },
      "reconciliationPeriod": {
        "type": "string",
        "enum": ["daily", "weekly", "monthly", "quarterly", "annual"]
      },
      "conversionFactors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "inputProduct": {"type": "string"},
            "outputProduct": {"type": "string"}, 
            "factor": {"type": "number"},
            "lossPercentage": {"type": "number"}
          }
        }
      }
    }
  }
}
```

### **2.2 Enhanced Volume Reconciliation Framework**

#### **Cross-stakeholder Key Findings and CoC Implications**

Stakeholder interviews underscored that **temporal reconciliation controls are essential for audit compliance** but often overlooked in implementation. The enhanced framework addresses this critical gap.

```json
{
  "reconciliationPeriodStart": {
    "type": "string",
    "format": "date-time"
  },
  "reconciliationPeriodEnd": {
    "type": "string", 
    "format": "date-time"
  },
  "reconciliationStatus": {
    "type": "string",
    "enum": ["in_progress", "balanced", "variance_identified", "variance_resolved"]
  },
  "varianceThreshold": {
    "type": "number",
    "description": "Acceptable variance percentage for reconciliation"
  },
  "varianceJustification": {
    "type": "string",
    "description": "Explanation for variances exceeding threshold"
  }
}
```

---

## **Phase 3: Advanced CoC Features (Months 5-6)** {#phase-3}

### **3.1 Mixed CoC Model Support**

#### **Enhancement: CoC Model Transitions**

**Background**: Real supply chains often require transitions between CoC models (e.g., Segregation at harvest, Mass Balance at processing).

```json
{
  "schema": {
    "$id": "https://github.com/carbondirect/BOOST/schemas/coc-transition",
    "title": "CoC Model Transition", 
    "description": "Tracking CoC model changes through supply chain",
    "type": "object",
    "properties": {
      "transitionId": {
        "type": "string",
        "pattern": "^COCT-[A-Z0-9-_]+$"
      },
      "traceableUnitId": {
        "type": "string",
        "pattern": "^TRU-[A-Z0-9-_]+$"
      },
      "fromCocModel": {
        "type": "string",
        "enum": ["identity_preservation", "segregation", "controlled_blending", "mass_balance", "controlled_mass_balance", "book_and_claim"]
      },
      "toCocModel": {
        "type": "string", 
        "enum": ["identity_preservation", "segregation", "controlled_blending", "mass_balance", "controlled_mass_balance", "book_and_claim"]
      },
      "transitionJustification": {
        "type": "string"
      },
      "transitionTimestamp": {
        "type": "string",
        "format": "date-time"
      },
      "operatorId": {
        "type": "string",
        "pattern": "^OP-[A-Z0-9-_]+$"
      }
    }
  }
}
```

### **3.2 Non-Proportional Attribution Support**

#### **Enhancement: Book and Claim Integration**

**Background**: Book and Claim models require complete decoupling of physical and administrative flows.

```json
{
  "administrativeTransfer": {
    "type": "object",
    "properties": {
      "certificateId": {"type": "string"},
      "transferDate": {"type": "string", "format": "date"},
      "volumeTransferred": {"type": "number"},
      "fromOrganizationId": {"type": "string"},
      "toOrganizationId": {"type": "string"}
    }
  },
  "physicalDecoupling": {
    "type": "boolean",
    "description": "True if administrative and physical flows are decoupled"
  }
}
```

---

## **Implementation Strategy** {#implementation}

### **Stakeholder-Specific Insights**

#### **Biomass Certification & Operations Experts**
*"The challenge isn't tracking—it's proving compliance with different CoC models simultaneously. BOOST needs explicit model specification."*

#### **Biomass Supply-Chain Experts** 
*"Volume reconciliation works, but auditors need to see temporal boundaries and attribution methods clearly documented."*

#### **California State Agencies**
*"ISEAL conformance is critical for LCFS pathway approval. The framework exists in BOOST but needs formal compliance structure."*

### **Chain of Custody Design Considerations**

Based on our analysis, we recommend a **phased implementation approach** that prioritizes critical compliance gaps while maintaining backward compatibility:

#### **Phase 1 Implementation Timeline**
- **Month 1**: CoC Model specification in TraceableUnit schema
- **Month 2**: System Boundary entity creation and integration
- **Month 3**: Attribution method framework in MaterialProcessing

#### **Phase 2 Implementation Timeline**  
- **Month 4**: Product Group entity development
- **Month 5**: Enhanced volume reconciliation controls
- **Month 6**: Temporal boundary enforcement

#### **Phase 3 Implementation Timeline**
- **Month 7**: Mixed CoC model support
- **Month 8**: Non-proportional attribution capabilities
- **Month 9**: Full ISEAL conformance validation

### **Migration and Backward Compatibility**

**Existing TraceableUnit entities** will be enhanced with optional CoC model fields, defaulting to "segregation" for backward compatibility. **System boundaries will be auto-generated** for existing organizational entities during migration.

**Data migration strategy** includes:
1. **Preserve existing TRU data** while adding CoC model specifications
2. **Generate default system boundaries** based on organizational relationships
3. **Map existing MaterialProcessing** to proportional attribution by default
4. **Create product groups** from existing Material entity groupings

---

## **Validation and Compliance Framework** {#validation}

### **ISEAL Conformance Checklist**

#### **Core Requirements** ✓
- [x] **Input/Output Tracking**: MaterialProcessing entity with volume reconciliation
- [x] **Traceability**: TraceableUnit with location and processing history  
- [x] **Specified Characteristics**: Material reference table and quality grades
- [x] **Claims Management**: Claim entity with certification scheme integration
- [ ] **CoC Model Specification**: *Enhancement required*
- [ ] **System Boundaries**: *Enhancement required*
- [ ] **Attribution Methods**: *Enhancement required*

#### **Advanced Features** ✓  
- [x] **Multi-species Tracking**: SpeciesComponent entity
- [x] **Geographic Tracking**: LocationHistory with geographic references
- [x] **Biometric Identification**: Unique identifier support in TraceableUnit
- [x] **Volume Reconciliation**: Built-in conversion factors and loss tracking

### **Compliance Testing Strategy**

Drawing on these findings, we recommend comprehensive testing against ISEAL model requirements:

1. **Identity Preservation Testing**: Single-source TRU tracking through complete supply chain
2. **Segregation Testing**: Certified/non-certified material separation validation
3. **Mass Balance Testing**: Proportional attribution accuracy in mixed processing
4. **Book and Claim Testing**: Administrative transfer without physical coupling

---

## **Expected Outcomes and Benefits** {#outcomes}

### **Immediate Benefits (Phase 1)**
- **100% ISEAL CoC Model Conformance** for all six recognized models
- **Explicit compliance documentation** for certification audits
- **Reduced audit complexity** through clear CoC model specification

### **Medium-term Benefits (Phase 2)**  
- **Enhanced product group management** supporting complex supply chains
- **Automated reconciliation controls** reducing manual oversight requirements
- **Improved temporal boundary enforcement** ensuring audit trail integrity

### **Long-term Benefits (Phase 3)**
- **Industry-leading CoC flexibility** supporting mixed-model supply chains
- **Complete ISEAL standard alignment** enabling certification under any scheme
- **Future-proof architecture** supporting emerging CoC model requirements

If implemented, this system could establish BOOST as the **definitive standard for biomass chain of custody tracking**, combining ISEAL conformance with advanced biomass-specific capabilities that exceed traditional CoC system functionality.

### **Risk Mitigation**

**Technical Risk**: Schema changes requiring extensive migration
- *Mitigation*: Backward-compatible optional fields with intelligent defaults

**Compliance Risk**: Incomplete ISEAL conformance preventing certification  
- *Mitigation*: Staged implementation with incremental conformance validation

**Stakeholder Risk**: Complexity overwhelming smaller organizations
- *Mitigation*: Simplified default configurations for basic CoC model compliance

---

## **Resource Requirements and Timeline** {#resources}

### **Development Resources**
- **Schema Development**: 2 FTE months for entity design and validation  
- **Implementation**: 4 FTE months for backend integration
- **Testing and Validation**: 3 FTE months for ISEAL conformance testing
- **Documentation**: 1 FTE month for compliance documentation

### **Total Timeline**: 9 months for complete ISEAL conformance implementation

### **Success Metrics**
- **100% ISEAL CoC Model Support** across all six recognized models
- **Zero compliance gaps** in certification audit scenarios  
- **90% stakeholder satisfaction** with enhanced CoC capabilities
- **25% reduction in audit preparation time** through explicit compliance framework

---

**This enhancement plan provides a comprehensive roadmap for achieving full ISEAL Chain of Custody conformance while maintaining BOOST's industry-leading biomass traceability capabilities.**