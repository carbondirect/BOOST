# BOOST Unified Documentation Build System

## Overview

The BOOST documentation now uses a **unified build system** that generates both HTML (Bikeshed) and PDF (LaTeX) documentation from a single source of truth - the JSON schemas. This ensures perfect consistency between both documentation formats.

## Components

### 1. Unified Content Generator (`scripts/generate-unified-content.py`)
- Loads all 33 entity schemas from `schema/` directory
- Generates Bikeshed includes in `includes/generated/`
- Generates LaTeX tables in `tex/entities/`
- Creates thematic sections for both formats
- Ensures identical content structure

### 2. Consistency Validator (`scripts/validate-consistency.py`)
- Validates all entities are documented in both formats
- Generates detailed reports with statistics
- Integrated into all build scripts
- Provides consistency score (currently 100%)

### 3. Build Scripts

#### Individual Builds
- `build-spec.sh` - Builds HTML with Bikeshed
- `build-pdf.sh` - Builds PDF with LaTeX
- Both include automatic consistency validation

#### Unified Build
- `build-unified.sh` - Complete build from schemas
- Generates content for both formats
- Builds HTML and PDF
- Validates consistency
- Generates comprehensive report

### 4. CI/CD Integration
- PDF build added to GitHub Actions workflow
- Consistency validation runs automatically
- Build reports generated for every deployment

## Usage

### Quick Start

```bash
# Generate unified content from schemas
python3 scripts/generate-unified-content.py

# Build everything with validation
./build-unified.sh

# Or build individually
./build-spec.sh  # HTML only
./build-pdf.sh   # PDF only

# Validate consistency
python3 scripts/validate-consistency.py
```

### Schema Updates

When schemas change:

1. **Automatic Updates**: Most changes are handled automatically
   - New fields appear in both formats
   - Enum values update dynamically
   - Descriptions propagate to documentation

2. **Manual Review**: Some changes may need attention
   - New entities require section placement
   - Relationship changes affect cross-references
   - Thematic organization updates

### Adding New Entities

1. Add schema to `schema/entity_name/validation_schema.json`
2. Run `python3 scripts/generate-unified-content.py`
3. Add entity to thematic area in generator scripts
4. Build documentation with `./build-unified.sh`
5. Verify with consistency validator

## Architecture

```
JSON Schemas (Single Source of Truth)
         |
         v
Unified Content Generator
         |
    +----+----+
    |         |
    v         v
Bikeshed   LaTeX
Content    Content
    |         |
    v         v
  HTML      PDF
    |         |
    +----+----+
         |
         v
Consistency Validator
         |
         v
    Build Report
```

## File Structure

```
specifications/
├── schema/                     # Source schemas (33 entities)
│   └── */validation_schema.json
├── scripts/
│   ├── generate-unified-content.py  # Unified generator
│   ├── validate-consistency.py      # Consistency checker
│   └── generate-latex-from-schemas.py
├── includes/generated/         # Generated Bikeshed content
│   └── *.inc.md
├── tex/
│   ├── entities/              # Generated LaTeX tables
│   │   └── *-table.tex
│   └── *-entities.tex         # Thematic sections
├── build/
│   ├── boost-spec.pdf         # Generated PDF
│   ├── consistency-report.json # Validation report
│   └── generation-report.json  # Generation statistics
├── boost-spec.bs              # Bikeshed source
├── boost-spec.tex             # LaTeX source
└── boost-spec.html            # Generated HTML
```

## Benefits

### Consistency
- **100% alignment** between HTML and PDF
- Single source of truth eliminates drift
- Automated validation catches issues early

### Maintainability
- Schema changes propagate automatically
- No manual synchronization needed
- Reduced documentation debt

### Quality
- Comprehensive validation at build time
- Detailed reports for troubleshooting
- CI/CD integration ensures continuous quality

## Validation Reports

### Generation Report (`build/generation-report.json`)
```json
{
  "entities_processed": 33,
  "bikeshed_files": 33,
  "latex_files": 33,
  "relationships_found": 45
}
```

### Consistency Report (`build/consistency-report.json`)
```json
{
  "consistency_score": 100.0,
  "bikeshed_documented": 33,
  "latex_documented": 33,
  "missing_in_bikeshed": 0,
  "missing_in_latex": 0
}
```

## Future Enhancements

### Planned Improvements
1. **YAML Configuration**: Define document structure in YAML
2. **Template System**: Customizable output templates
3. **Version Management**: Schema version tracking
4. **Diff Reports**: Show changes between builds
5. **Automated Testing**: Integration tests for documentation

### Long-term Vision
- Complete automation from schema to publication
- Multi-format support (EPUB, Markdown, etc.)
- Interactive documentation generation
- API documentation from schemas

## Troubleshooting

### Common Issues

#### LaTeX Build Errors
- Check `build/latex-pass*.log` for details
- Ensure all required packages installed
- Verify entity table syntax

#### Consistency Failures
- Review `build/consistency-report.json`
- Check for schema/documentation mismatch
- Run unified generator to sync

#### Missing Content
- Verify schema files exist
- Check thematic area assignments
- Regenerate with unified generator

## Support

For questions or issues:
- Check build reports in `build/` directory
- Review logs for detailed error messages
- Open issue in BOOST repository

## Credits

This unified build system was developed to ensure the BOOST specification maintains perfect consistency across all documentation formats while minimizing maintenance overhead.