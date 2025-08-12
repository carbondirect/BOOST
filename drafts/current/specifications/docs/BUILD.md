# BOOST Documentation Build System Architecture

This document provides comprehensive technical documentation for the BOOST specification build system, designed for developers, maintainers, and contributors.

## Overview

The BOOST documentation build system implements a **Single Source of Truth** architecture where all documentation is generated from JSON Schema definitions. This ensures consistency, eliminates duplication, and provides a reliable foundation for both PDF and HTML outputs.

## Core Principles

### 1. Single Source of Truth
- **JSON Schemas** (`schema/*/validation_schema.json`) are the definitive source of entity structure
- **Python generators** transform schemas into presentation formats
- **No manual duplication** of entity definitions across formats

### 2. Separation of Concerns
- **Content generation** (Python scripts)
- **Document compilation** (LaTeX/Bikeshed)
- **Output management** (Build scripts)
- **Style/formatting** (Style files)

### 3. Reproducible Builds
- All builds are deterministic and reproducible
- Complete dependency tracking
- Comprehensive logging and error reporting

## Build System Components

### Python Content Generators (`scripts/`)

#### `generate-latex-from-schemas.py`
**Purpose**: Converts all JSON schemas to comprehensive LaTeX documentation

**Input**: 
- `schema/*/validation_schema.json` files (33 entities)
- Entity relationship metadata

**Output**:
- `tex/*-entities.tex` (7 thematic sections)
- `tex/entity-reference-generated.tex` (appendix)
- Individual entity tables in `tex/entities/`

**Key Features**:
- Automatic thematic grouping of entities
- Foreign key relationship detection and documentation
- LaTeX table formatting with proper escaping
- ERD Navigator integration links

#### `generate-entity-tables.py` 
**Purpose**: Generate individual entity table files

**Usage**: Focused generation of specific entity documentation

#### `convert-tables-to-html.py`
**Purpose**: Transform LaTeX tables to HTML format for web output

#### `fix-html-escaping.py` & `fix-indentation.py`
**Purpose**: Post-processing utilities for format-specific corrections

### Build Orchestration Scripts

#### `build-all.sh` - Complete Pipeline
```bash
┌─ Prerequisites Check
├─ Content Generation (Python)
├─ PDF Compilation (3-pass LaTeX)
├─ Validation & Statistics
└─ Cleanup
```

**When to use**: 
- Complete rebuilds
- CI/CD pipelines
- Release preparation
- When schema changes

#### `build-pdf.sh` - PDF Focus
```bash
┌─ Prerequisites Check
├─ LaTeX Compilation (3-pass)
├─ Statistics & Warnings
└─ Cleanup
```

**When to use**:
- Development iterations
- LaTeX debugging
- Style testing

#### `build-spec.sh` - HTML Focus  
```bash
┌─ Bikeshed Compilation
├─ ReSpec Styling Injection
└─ Mobile Responsiveness
```

**When to use**:
- Web preview
- HTML-specific debugging
- Style development

## File Organization

### Source Files
```
specifications/
├── boost-spec.tex              # Main LaTeX document
├── boost-spec-minimal.sty      # LaTeX style definitions
├── boost-spec.bs               # Bikeshed specification
├── tex/                        # LaTeX content sections
│   ├── introduction.tex
│   ├── conformance.tex
│   ├── traceability-system.tex
│   ├── data-model.tex
│   ├── plant-parts.tex
│   ├── examples.tex
│   ├── serialization.tex
│   ├── use-cases.tex
│   ├── security-considerations.tex
│   └── resources-community.tex
└── schema/                     # Entity definitions (33 directories)
    ├── traceable_unit/
    ├── material_processing/
    ├── organization/
    └── ... (30 more)
```

### Generated Files
```
specifications/
├── build/                      # All outputs (not in git)
│   ├── boost-spec.pdf         # Final PDF (67 pages)
│   ├── boost-spec.html        # Final HTML
│   ├── latex-pass*.log        # Build logs
│   └── _minted-*/             # Syntax highlighting cache
└── tex/                       # Generated content (not in git)
    ├── *-entities.tex         # 7 thematic sections
    ├── entity-reference-generated.tex
    └── entities/              # Individual entity tables
        ├── traceable-unit-table.tex
        ├── organization-table.tex
        └── ... (33 total)
```

## Entity Processing Pipeline

### Schema Discovery
1. Scan `schema/` directories for `validation_schema.json`
2. Extract entity metadata (title, description, properties)
3. Detect foreign key relationships via naming conventions
4. Group entities into thematic areas

### Thematic Organization
The system automatically groups entities into 7 thematic areas:

1. **Core Traceability**: TraceableUnit, MaterialProcessing, ProcessingHistory, LocationHistory, BiometricIdentifier
2. **Organizational Foundation**: Organization, Certificate, CertificationBody, CertificationScheme, Audit, Operator
3. **Material & Supply Chain**: Material, SpeciesComponent, Equipment, Supplier, Customer, SupplyBase, SupplyBaseReport
4. **Transaction Management**: Transaction, TransactionBatch, SalesDeliveryDocument  
5. **Measurement & Verification**: MeasurementRecord, Claim, VerificationStatement, MoistureContent
6. **Geographic & Tracking**: GeographicData, TrackingPoint
7. **Compliance & Reporting**: LCFSPathway, LCFSReporting, ProductGroup, EnergyCarbonData, DataReconciliation, MassBalanceAccount

### LaTeX Generation Process

#### Field Processing
- **Required fields** (`"required": true`) → Bold formatting
- **Optional fields** → Regular formatting
- **Data types** → Extracted from JSON Schema type/format
- **Constraints** → Min/max values, patterns, enum values
- **Descriptions** → From schema descriptions or fallback text

#### Table Generation
```latex
\begin{entitytable}{Entity Name}
\textbf{\field{requiredField}} & type (constraints) & Description \\
\field{optionalField} & type & Description \\
\end{entitytable}
```

#### Relationship Documentation
- Foreign key detection via `*Id` pattern
- Automatic cross-references to target entities
- Informative boxes with relationship summaries

## LaTeX Compilation Details

### Multi-Pass Compilation
The PDF build uses 3 LaTeX passes to resolve all references:

1. **Pass 1**: Process document structure, generate `.aux` files
2. **Pass 2**: Resolve cross-references, update `.toc`
3. **Pass 3**: Finalize all references and generate final PDF

### Minted Integration
- **Shell escape enabled** (`--shell-escape`) for Pygments
- **Cache management** via `_minted-*` directories  
- **JSON syntax highlighting** in examples
- **Custom styling** with background colors and frames

### Style Features (`boost-spec-minimal.sty`)
- **W3C compliance** formatting
- **Entity table environment** (`\begin{entitytable}`)
- **Field highlighting** (`\field{fieldName}`)
- **Informative boxes** for relationships
- **Color scheme** with professional blue/gray palette

## Build System Integration

### Prerequisites Validation
All build scripts validate:
- LaTeX installation (`pdflatex`, `makeindex`)
- Python 3.7+ availability
- Required Python libraries
- Schema directory structure
- Style file presence

### Error Handling
- **Detailed logging** for all build steps
- **Exit codes** for CI/CD integration
- **Warning summaries** in build output
- **Log preservation** for debugging

### Performance Optimization
- **Incremental builds** when possible
- **Parallel processing** where applicable
- **Efficient cleanup** of temporary files
- **Build caching** for unchanged content

## Validation and Quality Assurance

### Content Validation
- **Entity count verification**: 33 entities expected
- **Schema completeness**: All schemas have required fields
- **Foreign key integrity**: All references resolve to valid entities
- **LaTeX syntax validation**: Compilation success required

### Output Validation  
- **PDF structure**: Page count, file size, metadata
- **HTML validity**: W3C compliance, responsive design
- **Cross-references**: All internal links functional
- **Syntax highlighting**: JSON examples properly formatted

### Quality Metrics
- **Build time tracking**
- **Warning/error counts**  
- **File size statistics**
- **Content coverage reports**

## Troubleshooting Guide

### Common Build Failures

#### LaTeX Compilation Errors
**Symptoms**: Build fails during PDF generation
**Solutions**:
- Check `build/latex-pass*.log` files
- Verify `--shell-escape` is enabled
- Ensure minted directories are writable
- Check for Unicode characters in generated content

#### Schema Processing Errors
**Symptoms**: Missing entities, incomplete tables
**Solutions**:
- Validate JSON schema syntax
- Check schema directory structure
- Verify foreign key naming conventions
- Review Python script error output

#### Missing Dependencies
**Symptoms**: "Command not found" errors
**Solutions**:
- Install full LaTeX distribution (MacTeX, TeX Live)
- Update Python to 3.7+
- Install Bikeshed via pip
- Check PATH configuration

### Debug Strategies

#### Incremental Testing
```bash
# Test schema processing only
python3 scripts/generate-latex-from-schemas.py

# Test single LaTeX pass
pdflatex -shell-escape -output-directory=build boost-spec.tex

# Test with minimal content
# (temporarily remove entity includes)
```

#### Log Analysis
```bash
# View compilation errors
tail -50 build/latex-pass3.log

# Check warning patterns
grep -i "warning" build/latex-pass*.log

# Validate minted operations
ls -la build/_minted-*
```

## Maintenance and Development

### Adding New Entities
1. Create schema directory: `schema/new_entity/`
2. Add `validation_schema.json`
3. Run `python3 scripts/generate-latex-from-schemas.py`
4. Update thematic grouping in generator if needed
5. Test complete build: `./build-all.sh`

### Modifying Existing Entities
1. Edit `schema/entity_name/validation_schema.json`
2. Regenerate: `python3 scripts/generate-latex-from-schemas.py` 
3. Test build: `./build-pdf.sh`
4. Validate output completeness

### Style Updates
1. Edit `boost-spec-minimal.sty`
2. Test with: `./build-pdf.sh`
3. Check visual formatting in PDF
4. Validate across all entity types

### Script Maintenance
- **Error handling**: Robust exception management
- **Logging**: Comprehensive debug output  
- **Documentation**: Inline comments and docstrings
- **Testing**: Validate against all schema variations

## CI/CD Integration

### Docker Containerization
The BOOST build system uses Docker containerization for fast, consistent builds across all environments.

#### Pre-Built Container Image
- **Image**: `ghcr.io/carbondirect/boost/boost-builder:latest`
- **Contents**: Ubuntu 22.04 + full LaTeX + Python + Bikeshed + Pandoc
- **Performance**: 4-6x faster builds (2-4 min vs 8-10 min)
- **Reliability**: Eliminates dependency installation failures

#### Local Testing with Docker
```bash
# Use the same container as CI/CD
docker pull ghcr.io/carbondirect/boost/boost-builder:latest

# Run interactive build environment
docker run -it --rm -v $(pwd):/workspace ghcr.io/carbondirect/boost/boost-builder:latest

# Inside container
cd /workspace/drafts/current/specifications
./build-spec.sh
```

### GitHub Actions Workflows
The repository includes comprehensive automation workflows:

#### Release Documentation (`release.yml`)
```yaml
# Triggered by any semantic version tag
jobs:
  build-release:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/carbondirect/boost/boost-builder:latest
      options: --pull=missing
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Build HTML documentation
        working-directory: drafts/current/specifications
        run: ./build-spec.sh
      
      - name: Generate PDF documentation  
        working-directory: drafts/current/specifications
        run: |
          # Multi-pass LaTeX compilation
          pdflatex -interaction=nonstopmode boost-spec.tex
          pdflatex -interaction=nonstopmode boost-spec.tex
          pdflatex -interaction=nonstopmode boost-spec.tex
```

#### Development Builds (`build-deploy.yml`)
```yaml
# Triggered by branch pushes
jobs:
  build-documentation:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/carbondirect/boost/boost-builder:latest
      options: --pull=missing
    steps:
      - name: Build HTML documentation
        working-directory: drafts/current/specifications
        run: ./build-spec.sh
      
      - name: Deploy to GitHub Pages
        if: github.ref == 'refs/heads/main'
        # Deploy to https://carbondirect.github.io/BOOST/
```

#### Version Management (`version-check.yml`)
```yaml
# Provides version analysis and release guidance
# Runtime: ~5 seconds (no container needed)
```

#### Docker Image Maintenance (`docker-image.yml`)
```yaml
# Builds and maintains the container image
# Triggered by changes to tools/Dockerfile
```

### Quality Gates
All automated builds enforce comprehensive quality standards:

#### Schema Validation
- All 33+ entity schemas must validate successfully
- JSON syntax correctness across all schema files
- Foreign key integrity validation (no orphaned references)
- BOOST metadata completeness for all entities

#### Build Validation  
- HTML documentation must generate without errors
- PDF compilation must complete successfully (when applicable)
- ERD Navigator must build with all entity relationships
- File size validation (HTML >200KB, reasonable PDF size)

#### Content Validation
- All entity schemas documented in generated content
- Cross-references and links functional
- Required content sections present (introduction, entities, examples)
- No critical LaTeX warnings or build failures

#### Performance Standards
- **Containerized builds**: Complete within 2-4 minutes
- **Release builds**: Complete within 3-4 minutes including full validation
- **Schema validation**: Complete within 30 seconds
- **Container availability**: Image pulls successful

#### Deployment Requirements (Main Branch)
- GitHub Pages deployment successful
- Landing page generation with working links  
- ERD Navigator accessibility
- Schema file availability through GitHub repository links

**Workflow Documentation**: See [.github/WORKFLOWS.md](../../../../.github/WORKFLOWS.md) for complete workflow documentation and troubleshooting guides.

This build system provides a robust, maintainable foundation for the BOOST specification documentation, ensuring consistency, quality, and ease of maintenance as the specification evolves.