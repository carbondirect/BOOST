# BOOST Documentation Build System

This directory contains the BOOST W3C Community Group specification documentation build system with comprehensive PDF and HTML generation from a **Single Source of Truth** architecture.

## Quick Start

```bash
# Build complete PDF with all 33 entities (recommended)
./build-all.sh

# Build only PDF (faster for testing)
./build-pdf.sh

# Build only HTML  
./build-spec.sh
```

**Output location**: All generated files are in the `build/` directory.

## Architecture Overview

The BOOST documentation system implements a **Single Source of Truth** approach:

1. **JSON Schemas** (`schema/*/validation_schema.json`) define all entity structures
2. **Python generators** (`scripts/`) convert schemas to LaTeX and HTML content
3. **Build scripts** orchestrate the complete documentation generation pipeline
4. **Style files** provide professional W3C-compliant formatting

## Directory Structure

```
specifications/
├── build/                    # All generated outputs (PDF, HTML, logs)
├── scripts/                  # Python content generators
│   ├── generate-latex-from-schemas.py
│   ├── generate-entity-tables.py
│   └── convert-tables-to-html.py
├── tex/                      # Generated LaTeX content
│   ├── *-entities.tex       # 7 thematic entity sections
│   ├── entities/            # Individual entity tables
│   └── entity-reference-generated.tex
├── schema/                   # JSON Schema definitions (33 entities)
├── boost-spec.tex           # Main LaTeX document
├── boost-spec-minimal.sty   # LaTeX style package
├── build-all.sh             # Complete build pipeline
├── build-pdf.sh             # PDF-only build
└── build-spec.sh            # HTML-only build
```

## Build System Details

### Complete Build (`build-all.sh`)

The comprehensive build process:

1. **Content Generation**: Converts all 33 JSON schemas to LaTeX documentation
2. **PDF Compilation**: 3-pass LaTeX build with minted syntax highlighting
3. **Validation**: Statistics, warnings, and completeness checking
4. **Cleanup**: Removes temporary files while preserving logs

**Output**: `build/boost-spec.pdf` (67 pages with all entities)

### PDF Build (`build-pdf.sh`)

Focused PDF generation:
- Uses existing LaTeX content in `tex/`
- 3-pass compilation for cross-references
- Detailed build statistics and error reporting
- Preserves build logs for debugging

### HTML Build (`build-spec.sh`)

Bikeshed-based HTML generation:
- Generates responsive W3C-compliant HTML
- Includes mobile-friendly navigation
- ReSpec styling with toggle functionality

## Entity Coverage

The system documents **all 33 entities** across **7 thematic areas**:

- **Core Traceability** (5): TraceableUnit, MaterialProcessing, ProcessingHistory, LocationHistory, BiometricIdentifier
- **Organizational Foundation** (6): Organization, Certificate, CertificationBody, CertificationScheme, Audit, Operator  
- **Material & Supply Chain** (7): Material, SpeciesComponent, Equipment, Supplier, Customer, SupplyBase, SupplyBaseReport
- **Transaction Management** (3): Transaction, TransactionBatch, SalesDeliveryDocument
- **Measurement & Verification** (4): MeasurementRecord, Claim, VerificationStatement, MoistureContent
- **Geographic & Tracking** (2): GeographicData, TrackingPoint
- **Compliance & Reporting** (6): LCFSPathway, LCFSReporting, ProductGroup, EnergyCarbonData, DataReconciliation, MassBalanceAccount

## Prerequisites

### Required Software

```bash
# LaTeX distribution (for PDF)
# macOS: brew install --cask mactex
# Ubuntu: sudo apt-get install texlive-full

# Python 3 (for content generation)
python3 --version  # Should be 3.7+

# Bikeshed (for HTML)
pip install bikeshed

# Optional: PDF utilities
# macOS: brew install poppler  # for pdfinfo
```

### Verification

```bash
# Check prerequisites
pdflatex --version
python3 --version
bikeshed --version
```

## Advanced Usage

### Custom Content Generation

```bash
# Regenerate only entity content from schemas
python3 scripts/generate-latex-from-schemas.py

# Generate specific entity tables
python3 scripts/generate-entity-tables.py

# Fix HTML formatting issues
python3 scripts/fix-html-escaping.py
```

### Debug Build Issues

```bash
# Check build logs
ls build/latex-pass*.log

# View last compilation errors
tail -20 build/latex-pass3.log

# Validate schema processing
find tex/entities -name "*.tex" | wc -l  # Should be 33
```

### Clean Rebuild

```bash
# Remove all generated content
rm -rf build/ tex/*-entities.tex tex/entity-reference-generated.tex

# Full regeneration
./build-all.sh
```

## Integration Features

- **Minted Syntax Highlighting**: JSON examples with proper formatting
- **W3C Compliance**: Community Group specification standards
- **Cross-References**: Automatic entity relationship linking  
- **ERD Navigator Integration**: Links to interactive entity diagrams
- **Mobile Responsive**: HTML output works on all devices
- **CI/CD Ready**: All scripts designed for automated builds

## Troubleshooting

### Common Issues

**LaTeX compilation fails**: Check that `_minted-*` directories are writable and `--shell-escape` is enabled.

**Missing entities**: Run `python3 scripts/generate-latex-from-schemas.py` to regenerate content from schemas.

**Build takes too long**: Use `./build-pdf.sh` for faster PDF-only builds during development.

**PDF not found**: Check `build/boost-spec.pdf` - all outputs are now in the build directory.

### Getting Help

- Check build logs in `build/` directory
- Ensure all prerequisites are installed
- Verify schema files exist in `schema/` directories
- Run `./build-all.sh` for most comprehensive output and error reporting