# BOOST Version Nomenclature

This document provides comprehensive documentation of the version nomenclature system used throughout the BOOST project for precise build traceability and release management.

## Overview

BOOST uses Git-based semantic versioning with automated development build identification. Every build, documentation generation, and release can be traced back to its exact source code state using the version nomenclature system.

## Version Format

### Standard Format: `v3.1.3-5-gaac45b1`

All BOOST versions follow the **Git describe** format, providing complete traceability:

```
v3.1.3-5-gaac45b1
│  │ │ │ │
│  │ │ │ └── Short commit hash (7 chars)
│  │ │ └── Git indicator ("g" for git)
│  │ └── Commits since release tag
│  └── Minor version
└── Major version (with "v" prefix)
```

### Component Breakdown

| Component | Example | Type | Description |
|-----------|---------|------|-------------|
| **Version Tag** | `v3.1.3` | Release | Latest semantic version release (Major.Minor.Patch) |
| **Commit Count** | `-5` | Development | Number of commits since the release tag |
| **Git Prefix** | `-g` | Standard | Git convention indicator |
| **Commit Hash** | `aac45b1` | Identifier | Abbreviated SHA hash (unique identifier) |

## Version Types

### 1. Release Versions

**Format**: `v3.1.3`  
**Description**: Official tagged releases following semantic versioning  
**Examples**:
- `v3.0.0` - Major release (breaking changes)
- `v3.1.0` - Minor release (new features, backward compatible)
- `v3.1.3` - Patch release (bug fixes, backward compatible)

**Characteristics**:
- ✅ Tagged in Git
- ✅ Stable and production-ready  
- ✅ Trigger automated GitHub releases
- ✅ Available as downloadable packages

### 2. Development Versions

**Format**: `v3.1.3-5-gaac45b1`  
**Description**: Development builds between releases  
**Examples**:
- `v3.1.3-1-g0057230` - First commit after v3.1.3
- `v3.1.3-5-gaac45b1` - Fifth commit after v3.1.3
- `v3.2.0-2-gdef456` - Second commit after v3.2.0

**Characteristics**:
- ❌ Not tagged releases
- 🔄 Work in progress
- 📊 Show development activity level
- 🎯 Provide exact commit traceability

### 3. Pre-Release Versions

**Format**: `v3.2.0-alpha.1`, `v3.2.0-beta.2`, `v3.2.0-rc.1`  
**Description**: Pre-release candidates for testing  
**Examples**:
- `v3.2.0-alpha.1` - Alpha release
- `v3.2.0-beta.2` - Beta release  
- `v3.2.0-rc.1` - Release candidate

**Characteristics**:
- 🧪 Testing and validation
- ⚠️ Not production-ready
- 📦 Available for early feedback
- 🚀 Lead to stable releases

## Version Evolution Examples

### Typical Development Cycle

```
v3.1.3              ← Official release
├── v3.1.3-1-g057230 ← Bug fix commit
├── v3.1.3-2-gca1a0c ← Feature work begins  
├── v3.1.3-3-g615374 ← Continued development
├── v3.1.3-4-gfe2beb ← Testing and refinement
└── v3.1.3-5-gaac45b ← Current state

v3.1.4              ← Next patch release (tags v3.1.3-5-gaac45b)
└── v3.1.4-1-g123abc ← Post-release development continues...
```

### Major Release Cycle

```
v3.1.3              ← Current stable
├── v3.1.3-1-g057230
├── ...
├── v3.1.3-15-gdef456
├── v3.2.0-alpha.1   ← Alpha testing
├── v3.2.0-beta.1    ← Beta testing  
├── v3.2.0-rc.1      ← Release candidate
└── v3.2.0           ← Major release

v3.2.0-1-g789xyz    ← Development continues...
```

## Version Sources and Extraction

### 1. Git Tags (Primary)

```bash
# Latest tagged release
git describe --tags --abbrev=0
# Output: v3.1.3

# Detailed version with commit info
git describe --tags --always
# Output: v3.1.3-5-gaac45b1
```

### 2. Environment Variables (CI/CD)

```bash
# Pre-extracted in CI/CD workflows
export RELEASE_VERSION="v3.1.3-5-gaac45b1"

# Used in Docker containers without git access
echo "Building version: $RELEASE_VERSION"
```

### 3. Fallback Versions

When Git is unavailable:
- `v0.0.0-no-version-detected` - Clear fallback indication
- `v0.0.0-dev-[hash]` - Development with commit hash only

## Integration Points

### Documentation Builds

- **HTML Headers**: `<meta name="version" content="v3.1.3-5-gaac45b1">`
- **PDF Metadata**: Embedded in document properties
- **Build Logs**: Version logged for debugging
- **File Names**: `boost-spec-v3.1.3-5-gaac45b1.pdf`

### CI/CD Workflows

- **GitHub Actions**: Automatic version extraction
- **Docker Containers**: Version passed via environment variables  
- **Artifact Names**: `boost-docs-v3.1.3-5-gaac45b1.zip`
- **Release Naming**: "BOOST v3.1.3 - Patch Release"

### Development Tools

- **Build Scripts**: `./build.sh` shows version in output
- **Schema Validation**: Version context in error reports
- **Test Results**: Version tracking for issue reproduction

## Practical Usage

### For Developers

```bash
# Check current version
git describe --tags --always

# Build with version info
cd drafts/current/specifications
./build.sh  # Shows version: v3.1.3-5-gaac45b1

# Reproduce specific build
git checkout aac45b1
./build.sh  # Exact same environment
```

### For Issue Reporting

When reporting issues, always include the full version:

```
Issue: LaTeX compilation fails
Version: v3.1.3-5-gaac45b1
Platform: macOS 14.1
Build command: ./build.sh --pdf
```

### For Release Management

```bash
# Create new release
git tag v3.1.4
git push origin v3.1.4

# This automatically:
# 1. Triggers release workflow
# 2. Builds documentation with version v3.1.4
# 3. Creates GitHub release
# 4. Updates version references
```

## Version Validation

### Valid Version Formats

✅ **Correct**:
- `v3.1.3` (release)
- `v3.1.3-5-gabc123` (development)  
- `v3.2.0-alpha.1` (pre-release)
- `v0.0.0-dev-abc123` (untagged development)

❌ **Invalid**:
- `3.1.3` (missing "v" prefix)
- `v3.1` (incomplete semantic version)
- `latest` (not specific)
- `main-abc123` (not version format)

### Automated Validation

The build system validates version formats:

1. **Semantic Version Check**: Ensures proper Major.Minor.Patch format
2. **Git Hash Validation**: Verifies commit hash exists
3. **Tag Verification**: Confirms tags follow versioning standards
4. **Environment Consistency**: Validates version across build steps

## Troubleshooting

### Common Issues

**Problem**: Version shows as `v0.0.0-no-version-detected`  
**Solution**: Ensure Git is available and repository has tags
```bash
git fetch --tags
git describe --tags
```

**Problem**: Version format inconsistent between builds  
**Solution**: Use standardized extraction in CI/CD:
```bash
VERSION=$(git describe --tags --always)
export RELEASE_VERSION="$VERSION"
```

**Problem**: Docker container shows wrong version  
**Solution**: Version must be extracted outside container:
```yaml
# Extract before container
- name: Extract version
  run: echo "VERSION=$(git describe --tags --always)" >> $GITHUB_ENV

# Pass to container  
container:
  env:
    RELEASE_VERSION: ${{ env.VERSION }}
```

## Best Practices

### For Contributors

1. **Always include version** in issue reports and pull requests
2. **Use full format** (`v3.1.3-5-gaac45b1`) not just tag (`v3.1.3`)
3. **Test version extraction** locally before pushing changes
4. **Validate build output** includes correct version information

### For Maintainers

1. **Use semantic versioning** for all tags
2. **Pre-extract versions** in CI/CD workflows
3. **Validate version formats** in automated checks
4. **Document version changes** in release notes

### For Release Management

1. **Tag consistently** following semantic versioning
2. **Verify version extraction** in all build workflows
3. **Update documentation** to reflect version changes
4. **Test full release cycle** before major version changes

## References

- [Semantic Versioning Specification](https://semver.org/)
- [Git Describe Documentation](https://git-scm.com/docs/git-describe)
- [BOOST GitHub Actions Workflows](.github/WORKFLOWS.md)
- [BOOST Build System Documentation](drafts/current/specifications/README.md)

---

This version nomenclature system ensures complete traceability and reproducibility across all BOOST documentation builds and releases.