# BOOST Documentation Build System

This directory contains the BOOST W3C Community Group specification documentation build system with comprehensive PDF and HTML generation from a **Single Source of Truth** architecture.

## **Documentation Outputs** {#documentation-outputs}

### **📖 Primary Documentation**
- **[📄 BOOST Specification PDF](build/boost-spec.pdf)** - Complete 88+ page specification with all 36 entities
- **[🌐 HTML Specification](boost-spec.html)** - W3C-compliant interactive documentation
- **[📊 Interactive ERD Navigator](erd-navigator/index.html)** - Explore entity relationships visually
- **[🗂️ Schema Directory](../schema/)** - 36 JSON validation schemas (single source of truth)

### **📋 Reports & Analysis**
- **[📈 Build Reports](build/)** - Generation statistics, consistency analysis, and build logs
- **[📝 CHANGELOG](CHANGELOG.md)** - Complete version history and recent improvements
- **[🔍 Consistency Reports](build/consistency-report.json)** - Cross-format validation results

### **🛠️ Development Resources**
- **[⚙️ Build System Documentation](UNIFIED_BUILD_SYSTEM.md)** - Advanced build configuration
- **[✅ Enhancement Plans](../planning_documents/README.md)** - GitHub Issues-based project planning

## Quick Start

```bash
# Build both HTML and PDF documentation (recommended)
./build.sh

# Build only HTML (faster for development)
./build.sh --html

# Build only PDF (for testing LaTeX changes)
./build.sh --pdf

# Show help and all available options
./build.sh --help
```

**Output location**: All generated files are in the `build/` directory.

## Architecture Overview

The BOOST documentation system implements a **Single Source of Truth** approach:

1. **JSON Schemas** (`../schema/*/validation_schema.json`) define all 36 entity structures
2. **Python generators** (`scripts/`) convert schemas to LaTeX and HTML content
3. **Consolidated build script** (`build.sh`) orchestrates the complete documentation generation pipeline
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
├── ../schema/               # JSON Schema definitions (36 entities)
├── boost-spec.tex           # Main LaTeX document
├── boost-spec.sty           # LaTeX style package
└── build.sh                 # Consolidated build system (replaces all previous scripts)
```

## Build System Details

### Consolidated Build System (`build.sh`)

The unified build process supports flexible output generation:

#### **Default Build** (`./build.sh`)
- **Content Generation**: Converts all 36 JSON schemas to LaTeX documentation
- **HTML Generation**: Bikeshed-based responsive W3C-compliant HTML with ReSpec styling
- **PDF Compilation**: 3-pass LaTeX build with enhanced error detection
- **Validation**: Comprehensive statistics, warnings analysis, and consistency checking
- **Version Management**: Automatic git tag-based version extraction
- **Cleanup**: Removes intermediate files while preserving build logs

**Output**: 
- `boost-spec.html` - Complete HTML documentation
- `build/boost-spec.pdf` - Professional PDF (88+ pages with all entities)

#### **HTML-Only Build** (`./build.sh --html`)
- Fast development iteration with HTML generation only
- Ideal for content review and validation
- Includes mobile-friendly navigation and ReSpec styling

#### **PDF-Only Build** (`./build.sh --pdf`)
- Focused LaTeX compilation for testing formatting changes
- 3-pass compilation with comprehensive warning analysis
- Enhanced error detection distinguishing critical errors from acceptable warnings

## Entity Coverage

The system documents **all 36 entities** across **7 thematic areas**:

- **Core Traceability** (6): TraceableUnit, MaterialProcessing, ProcessingHistory, LocationHistory, BiometricIdentifier, IdentificationMethod
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
# Check build logs (comprehensive error analysis included)
ls build/latex-pass*.log

# View detailed LaTeX warnings analysis
./build.sh --pdf  # Shows warning classification and summaries

# Validate schema processing
find tex/entities -name "*.tex" | wc -l  # Should be 36
```

### Clean Rebuild

```bash
# Remove all generated content
rm -rf build/ tex/*-entities.tex tex/entity-reference-generated.tex

# Full regeneration with comprehensive analysis
./build.sh
```

## Version Management

The build system automatically manages versioning using Git tags and commit information:

### **Version Format in Builds**

All generated documentation includes version information in the format: `vX.Y.Z-N-gHHHHHHH`

- **`vX.Y.Z`**: Latest release tag (semantic versioning)
- **`-N`**: Number of commits since the release
- **`gHHHHHHH`**: Short commit hash for exact traceability

### **Version Sources** (Priority Order)

1. **`RELEASE_VERSION`** environment variable (CI/CD workflows)
2. **Git describe** with full tag and commit info (development)
3. **Fallback** version when git is unavailable

### **Build Integration**

- **HTML Headers**: Show exact version used for generation
- **PDF Metadata**: Include version for reproducibility
- **Build Logs**: Version information logged for debugging
- **CI/CD**: Automatic version extraction and validation

This ensures every build can be traced back to its exact source code state.

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