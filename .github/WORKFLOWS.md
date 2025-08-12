# BOOST GitHub Actions Workflows Documentation

This document provides comprehensive documentation for all GitHub Actions workflows in the BOOST repository, covering automation for documentation builds, releases, and version management.

## 🔄 Overview

The BOOST repository uses GitHub Actions to automate documentation building, validation, and release management. All workflows are containerized using a pre-built Docker image for fast, consistent builds.

### Key Features
- **🐳 Docker Containerization**: All builds use `ghcr.io/carbondirect/boost/boost-builder:latest` for 4-6x faster execution
- **🚀 Automatic Releases**: All semantic version tags trigger full release packages  
- **✅ Schema Validation**: Comprehensive validation of 33+ entity schemas
- **📄 Multi-Format Output**: HTML, PDF, and interactive ERD Navigator generation
- **🔍 Version Analysis**: Intelligent version type detection and appropriate release handling

## 📋 Workflow Summary

| Workflow | Trigger | Purpose | Container | Duration |
|----------|---------|---------|-----------|----------|
| [🏷️ Release Documentation](#release-documentation) | Version tags (`v*.*.*`) | Build & publish release packages | ✅ Docker | ~3-4 min |
| [🏷️ Version Management](#version-management) | Version tags (`v*.*.*`) | Analyze versions & provide guidance | ❌ Native | ~5 sec |
| [📚 Build Documentation](#build-documentation) | Push to branches | Build development docs & deploy | ✅ Docker | ~2-3 min |
| [🐳 Docker Image Builder](#docker-image-builder) | Dockerfile changes | Build & push container images | ❌ Native | ~5-8 min |

## 🏷️ Release Documentation

**File**: `.github/workflows/release.yml`  
**Trigger**: Push tags matching `v[0-9]+.[0-9]+.[0-9]+` (all semantic versions)  
**Container**: `ghcr.io/carbondirect/boost/boost-builder:latest`

### Purpose
Builds and publishes complete release packages for **all semantic version types** (major, minor, patch).

### Key Changes (Recent Update)
- **Before**: Only major versions (v1.0.0, v2.0.0) triggered releases
- **After**: All versions (v1.0.0, v1.2.3, v2.1.0) trigger automatic releases
- **Performance**: 4-6x faster builds using Docker containerization

### Jobs

#### 1. 📦 Build Release Documentation
**Runtime**: ~3-4 minutes (Docker containerized)

**Steps**:
1. **Environment Setup**
   - Uses pre-built Docker image with all dependencies (TeXLive, Python, Bikeshed, Pandoc)
   - Verifies containerized environment tools

2. **Version Analysis**
   - Validates semantic version format (`v1.2.3`)
   - Determines version type (major/minor/patch)
   - Generates appropriate release names:
     - Major: "Biomass Open Origin Standard for Tracking (BOOST) v3.0.0 - Major Release"  
     - Minor: "Biomass Open Origin Standard for Tracking (BOOST) v2.1.0 - Minor Release"
     - Patch: "Biomass Open Origin Standard for Tracking (BOOST) v2.0.1 - Patch Release"

3. **Schema Validation**
   - Validates all 33+ entity schemas for release quality
   - Checks JSON syntax, required properties, BOOST metadata
   - Ensures foreign key integrity across all entities

4. **Documentation Build**
   - Builds HTML documentation using Bikeshed
   - Generates PDF using LaTeX (3-pass compilation)
   - Creates interactive ERD Navigator
   - Applies ReSpec styling for professional presentation

5. **Release Package Creation**  
   - Creates structured release directory with all artifacts
   - Includes HTML docs, PDF, ERD Navigator, and schema files
   - Generates comprehensive README with usage instructions
   - Creates both ZIP and TAR.GZ archives

6. **Artifact Upload**
   - Uploads complete release package as GitHub Actions artifact
   - 90-day retention for release packages
   - Available for download and inspection

#### 2. 🚀 Create GitHub Release
**Condition**: Only runs for tag pushes (not manual dispatches)

**Steps**:
1. **Release Notes Generation**
   - Creates comprehensive release notes based on version type
   - Includes breaking change warnings for major versions
   - Lists all included components and quick links

2. **GitHub Release Creation**
   - Publishes GitHub release with generated notes
   - Attaches ZIP and TAR.GZ packages for download
   - Marks pre-releases appropriately (alpha, beta, rc versions)
   - Updates "latest" release pointer for stable versions

### Usage Examples

#### Automatic Release (Recommended)
```bash
# Create and push any semantic version tag
git tag v2.1.3
git push origin v2.1.3

# This automatically:
# 1. Triggers release workflow
# 2. Builds complete documentation 
# 3. Creates GitHub release
# 4. Uploads downloadable packages
```

#### Manual Release
```bash
# Use GitHub Actions UI or CLI
gh workflow run release.yml -f version=v2.1.3 -f force_release=true
```

## 🏷️ Version Management  

**File**: `.github/workflows/version-check.yml`  
**Trigger**: Push tags matching `v*.*.*` (all version tags)  
**Container**: Native Ubuntu runner

### Purpose  
Provides analysis and guidance for version tags, documenting the new automatic release policy.

### Jobs

#### 1. 📋 Analyze Version Tag
**Runtime**: ~5 seconds

**Process**:
- Parses version components (major.minor.patch)
- Identifies version type and explains what will happen  
- Creates detailed step summary with:
  - Version breakdown table
  - Automatic release confirmation
  - Links to documentation and artifacts

**Sample Output**:
```
🏷️ Version Analysis: v2.1.3

Version Type: **PATCH**

| Component | Value |
|-----------|-------|  
| Major     | 2     |
| Minor     | 1     |
| Patch     | 3     |

✅ Release workflow will trigger automatically for all versions
- Complete documentation build with PDF generation
- GitHub release creation with artifacts  
- Release type: Patch Release
- Automatic package creation and distribution
```

#### 2. 📈 Plan Next Version
**Trigger**: Manual workflow dispatch
**Purpose**: Planning tool for version increments

**Features**:
- Validates version increment logic
- Shows current → next version progression  
- Explains what will happen when tag is created
- Provides copy-paste commands for release creation

#### 3. 📢 Version Policy Reminder
**Purpose**: Documents current release policy for non-tag pushes

**Key Message**: "All semantic version tags now trigger automatic releases"

## 📚 Build Documentation

**File**: `.github/workflows/build-deploy.yml`  
**Trigger**: Push to main, develop, feature/*, fix/*, docs/* branches  
**Container**: `ghcr.io/carbondirect/boost/boost-builder:latest`

### Purpose
Builds development documentation and deploys to GitHub Pages for the main branch.

### Key Features
- **Docker Containerization**: Uses pre-built image for fast builds (~2-3 minutes)
- **Branch-Specific Behavior**: 
  - `main` branch: Build + deploy to GitHub Pages
  - Other branches: Build only (no deployment)
- **Comprehensive Validation**: Schema validation, build verification, ERD Navigator generation

### Jobs

#### 1. 📖 Build Documentation  
**Runtime**: ~2-3 minutes (Docker containerized)

**Process**:
1. **Containerized Setup**
   - Pulls latest Docker image with all dependencies pre-installed
   - Verifies Python, Bikeshed, TeXLive, and Pandoc availability

2. **Version Extraction**
   - Uses git tags or commit hash for version identification
   - Supports both tagged and untagged builds

3. **Schema Validation**  
   - Runs comprehensive validation script for all entity schemas
   - Validates JSON syntax, cross-references, and business rules

4. **Documentation Build**
   - Executes `build-spec.sh` for HTML generation
   - Applies ReSpec styling and responsive design
   - Generates interactive ERD Navigator

5. **Build Validation**
   - Verifies HTML file generation and size
   - Checks for required content sections  
   - Validates ERD Navigator components
   - Reports build statistics

6. **PDF Generation** (All Branches)
   - Multi-pass LaTeX compilation for complete PDF
   - Fallback to Pandoc HTML→PDF conversion if needed
   - Branch-specific PDF naming

#### 2. 🌐 Deploy to GitHub Pages
**Condition**: Only runs for main branch pushes  
**Runtime**: ~1-2 minutes

**Process**:
1. **Artifact Download**: Retrieves build outputs from previous job
2. **Pages Preparation**: 
   - Creates landing page with download links
   - Copies HTML documentation, ERD Navigator, and schema files  
   - Links to GitHub repository for schema browsing
3. **GitHub Pages Deployment**: Publishes to `carbondirect.github.io/BOOST`

### Build Outputs

#### Development Builds (All Branches)
- HTML documentation (`boost-spec.html`)
- PDF documentation (`boost-spec-dev-{branch}.pdf` for non-main branches)
- Interactive ERD Navigator (`erd-navigator/`)
- Build statistics and validation reports

#### Production Deployment (Main Branch Only)  
- Live website at https://carbondirect.github.io/BOOST
- Landing page with download options
- Direct access to documentation and ERD Navigator
- Schema file browsing via GitHub repository links

## 🐳 Docker Image Builder

**File**: `.github/workflows/docker-image.yml`  
**Trigger**: 
- Push to main branch with changes to `tools/Dockerfile`
- Manual workflow dispatch
**Container**: Native Ubuntu runner (builds containers)

### Purpose
Maintains the pre-built Docker image used by all documentation build workflows.

### Features
- **Automated Rebuilds**: Triggers when Dockerfile changes
- **Multi-Tag Support**: Creates `latest`, `main`, and commit-specific tags
- **GitHub Container Registry**: Publishes to `ghcr.io/carbondirect/boost/boost-builder`
- **Build Caching**: Uses GitHub Actions cache for faster rebuilds

### Image Contents
The Docker image includes all dependencies for BOOST documentation builds:

- **Base**: Ubuntu 22.04 LTS
- **LaTeX**: Full TeXLive distribution with extra fonts and packages  
- **Python**: Python 3.11 with pip, Bikeshed, JSONSchema, Pydantic
- **Tools**: Pandoc, Git, Curl
- **Pre-initialization**: Bikeshed spec database updated and cached

### Performance Impact
Using the pre-built image provides:
- **4-6x faster builds**: From 8-10 minutes to 2-3 minutes
- **Consistent environment**: Same dependencies every time
- **Reliability**: Eliminates dependency installation failures
- **Cost efficiency**: Reduced GitHub Actions compute time

### Usage in Other Workflows
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/carbondirect/boost/boost-builder:latest
      options: --pull=missing
```

## 🔧 Development and Maintenance

### Local Testing

#### Test Documentation Build Locally
```bash
# Clone and test development build
git clone https://github.com/carbondirect/BOOST.git
cd BOOST/drafts/current/specifications
./build-spec.sh

# View output
open boost-spec.html
```

#### Test with Docker Container
```bash  
# Pull the same container used in CI
docker pull ghcr.io/carbondirect/boost/boost-builder:latest

# Run interactive container
docker run -it --rm -v $(pwd):/workspace ghcr.io/carbondirect/boost/boost-builder:latest

# Inside container - test build
cd /workspace/drafts/current/specifications  
./build-spec.sh
```

### Workflow Maintenance

#### Updating Dependencies
1. Modify `tools/Dockerfile` with new requirements
2. Push to main branch - this triggers automatic image rebuild
3. New builds will use updated dependencies automatically

#### Adding New Build Steps
1. Update appropriate workflow file (`.github/workflows/*.yml`)
2. Test changes in feature branch (build-only, no deployment)
3. Merge to main to enable full functionality

#### Troubleshooting Failed Builds
1. **Check workflow logs**: GitHub Actions provides detailed step-by-step logs
2. **Verify container image**: Ensure Docker image built successfully  
3. **Local reproduction**: Use same Docker image to reproduce issues
4. **Schema validation**: Run schema validation scripts locally

### Performance Monitoring

#### Build Time Targets
- **Development builds**: 2-3 minutes (containerized)
- **Release builds**: 3-4 minutes (containerized with full validation)
- **Docker image builds**: 5-8 minutes (only when Dockerfile changes)

#### Quality Metrics
- **Schema validation**: 100% pass rate required
- **Build success rate**: >99% for main branch
- **PDF generation**: Consistent multi-format output
- **Deployment reliability**: Zero-downtime GitHub Pages updates

## 🆕 Recent Updates (December 2024)

### Release Strategy Changes
- **Expanded automatic releases** from major-only to all semantic versions
- **Enhanced release naming** with version-type-specific titles
- **Improved release notes** with breaking change indicators

### Docker Containerization
- **4-6x performance improvement** through pre-built dependencies
- **Consistent build environment** across all workflows
- **Reduced failure rates** by eliminating dependency installation issues

### Documentation Improvements  
- **Comprehensive workflow documentation** (this file)
- **Clear usage examples** for all common scenarios
- **Maintenance guides** for ongoing development

This workflow system provides robust, fast, and reliable automation for the BOOST documentation project, ensuring high-quality outputs and seamless releases for all stakeholders.