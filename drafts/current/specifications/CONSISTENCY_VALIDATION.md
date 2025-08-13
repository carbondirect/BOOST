# BOOST Documentation Consistency Validation

## Overview

This document describes the consistency validation system for ensuring alignment between HTML (Bikeshed) and PDF (LaTeX) versions of the BOOST specification.

## Validation Script

The `scripts/validate-consistency.py` script performs automated checks to ensure both documentation formats contain the same entities and content structure.

### Features

- **Schema Coverage**: Verifies all 33 entities from the schema directory are documented
- **Cross-Format Check**: Ensures both HTML and PDF have the same entities
- **Detailed Reporting**: Generates JSON report with statistics and issues
- **Build Integration**: Automatically runs during build processes

### Usage

```bash
# Run standalone validation
python3 scripts/validate-consistency.py

# Run with strict mode (exits with error code on issues)
python3 scripts/validate-consistency.py --strict

# Specify different directory
python3 scripts/validate-consistency.py --spec-dir /path/to/specs
```

## Current Status

### ✅ Validated Consistency (as of latest build)

- **Schema Entities**: 33 total entities defined
- **Bikeshed Coverage**: 33/33 entities documented (100%)
- **LaTeX Coverage**: 33/33 entities documented (100%)
- **Consistency Score**: 100%

### Entity Documentation Status

All 33 entities are properly documented in both formats:

1. audit
2. biometric_identifier
3. certificate
4. certification_body
5. certification_scheme
6. claim
7. customer
8. data_reconciliation
9. energy_carbon_data
10. equipment
11. geographic_data
12. lcfs_pathway
13. lcfs_reporting
14. location_history
15. mass_balance_account
16. material
17. material_processing
18. measurement_record
19. moisture_content
20. operator
21. organization
22. processing_history
23. product_group
24. sales_delivery_document
25. species_component
26. supplier
27. supply_base
28. supply_base_report
29. traceable_unit
30. tracking_point
31. transaction
32. transaction_batch
33. verification_statement

### Known Issues

The LaTeX parser identifies some non-entity sections as entities due to pattern matching:
- `boost_moisture_content_validation_rules` - Actually a validation schema section
- `boost_operator_entity_validation_schema` - Actually a validation schema section
- `context_examples` - JSON-LD context examples section
- `relationships_generated` - Generated relationship documentation
- `summary_generated` - Generated summary section
- `thematic_areas` - Thematic area organization section

These are false positives and do not affect the actual entity documentation consistency.

## Build Integration

The validation script is integrated into all build processes:

### build-spec.sh (HTML)
```bash
./build-spec.sh
# Automatically runs validation after HTML generation
```

### build-pdf.sh (PDF)
```bash
./build-pdf.sh
# Automatically runs validation after PDF generation
```

### build-all.sh (Complete Build)
```bash
./build-all.sh
# Runs validation after complete documentation build
```

## Validation Report

After each validation run, a detailed report is saved to:
```
build/consistency-report.json
```

The report includes:
- List of all entities in each format
- Identified inconsistencies
- Statistics and metrics
- Consistency score

## Future Improvements

### Phase 1: Enhanced Validation (Completed ✅)
- Created validation script
- Integrated with build processes
- Generated comprehensive reports

### Phase 2: Unified Content Generation (Planned)
- Extend schema-to-content generator for both formats
- Create templates for shared content
- Ensure identical structure from single source

### Phase 3: CI/CD Integration (Planned)
- Add validation to GitHub Actions
- Generate comparison previews
- Fail builds on inconsistencies

## Maintaining Consistency

To maintain documentation consistency:

1. **When adding new entities**:
   - Add schema to `schema/entity_name/`
   - Add section to `boost-spec.bs` with dictionary include
   - Run `python3 scripts/generate-latex-from-schemas.py` to update LaTeX

2. **When modifying entities**:
   - Update schema definition
   - Regenerate LaTeX content
   - Verify both formats with validation script

3. **Before committing**:
   - Run `./build-all.sh` to build both formats
   - Check validation passes
   - Review `build/consistency-report.json` if issues found

## Contact

For questions or issues with the validation system, please open an issue in the BOOST repository.