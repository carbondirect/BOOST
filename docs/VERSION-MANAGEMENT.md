# BOOST Version Management System

This document describes the comprehensive version management system that ensures version synchronization between git tags and documentation across all formats (HTML, PDF).

## Overview

The BOOST project uses a **git-tag-based dynamic versioning system** that automatically synchronizes versions across all documentation formats. This prevents version drift and ensures consistency.

## Key Principles

### 1. Single Source of Truth
- **Git tags** are the authoritative source for version information
- Documentation uses `{{VERSION}}` placeholders that get replaced dynamically
- No hardcoded versions in source files (except CHANGELOG.md and README.md examples)

### 2. Dynamic Version Replacement
- Build system replaces `{{VERSION}}` with actual git-derived version
- Format: `v3.2.2-N-gSHA` where:
  - `v3.2.2` = latest release tag
  - `N` = commits ahead of tag
  - `gSHA` = short git commit hash

### 3. Multi-Layer Validation
- **Pre-commit hooks** prevent hardcoded versions from being committed
- **Pre-build validation** detects any hardcoded versions before building
- **Post-build validation** ensures version replacement worked correctly

## Implementation Details

### Files Using Version Placeholders

#### Required Files
These files **must** use `{{VERSION}}` placeholders:

1. **`boost-spec.bs`** (Bikeshed source)
   ```
   !Version: {{VERSION}}
   ```

2. **`boost-spec.tex`** (LaTeX main document)
   ```latex
   \fancyhead[R]{\small {{VERSION}}}
   ```

3. **`boost-spec.sty`** (LaTeX style package)
   ```latex
   \ProvidesPackage{boost-spec}[2025/08/22 {{VERSION}} BOOST Specification Style]
   {\Large Version {{VERSION}} \par}
   ```

#### Optional Files
- Markdown files in `includes/` directory may use `{{VERSION}}` if needed
- LaTeX files in `tex/` directory may use `{{VERSION}}` if needed

### Build Process Integration

#### 1. Pre-Build Validation
```bash
validate_no_hardcoded_versions()
```
- Scans all source files for hardcoded version patterns
- Excludes CHANGELOG.md and README.md (legitimate version references)
- **Fails build** if hardcoded versions found

#### 2. Version Substitution
```bash
substitute_version()
```
- Replaces `{{VERSION}}` with git-derived version in:
  - `*.bs` files
  - `includes/*.md` files  
  - `tex/*.tex` files
  - `*.sty` files

#### 3. Post-Build Validation
```bash
# Inside generate_build_statistics()
```
- Validates version appears correctly in generated HTML
- Validates version appears correctly in generated PDF
- **Fails build** if version synchronization failed

#### 4. Cleanup
```bash
restore_version_placeholders()
```
- Restores `{{VERSION}}` placeholders in all files
- Ensures source files remain clean for version control

## Git Hooks System

### Pre-Commit Hook
Location: `.githooks/pre-commit`

**Purpose**: Prevents hardcoded versions from being committed

**Detection Patterns**:
- `v[0-9]+\.[0-9]+\.[0-9]+.*BOOST`
- `Version [0-9]+\.[0-9]+\.[0-9]+`
- `version [0-9]+\.[0-9]+\.[0-9]+`

**Key File Validation**:
- Ensures `boost-spec.tex` uses `{{VERSION}}` in headers
- Ensures `boost-spec.sty` uses `{{VERSION}}` in package/version definitions
- Ensures `boost-spec.bs` uses `{{VERSION}}` for version metadata

### Setup Instructions
```bash
./scripts/setup-git-hooks.sh
```

## Best Practices

### ✅ DO
- Use `{{VERSION}}` placeholders for all version references
- Let the build system handle version management automatically
- Create git tags for releases (`git tag v3.2.3`)
- Test builds locally before pushing

### ❌ DON'T
- Hardcode versions in source files
- Manually edit generated HTML/PDF files
- Skip pre-commit hook setup
- Commit without testing build process

## Troubleshooting

### Problem: "Hardcoded versions detected"
**Solution**: Replace hardcoded versions with `{{VERSION}}` placeholders

**Example**:
```latex
❌ \fancyhead[R]{\small v3.2.2}
✅ \fancyhead[R]{\small {{VERSION}}}
```

### Problem: "Version synchronization validation failed"
**Cause**: Placeholder replacement didn't work
**Solution**: 
1. Check if files use `{{VERSION}}` placeholders
2. Verify build system processes the file type
3. Check for file permission issues

### Problem: Pre-commit hook blocks commit
**Solution**: 
1. Review the specific hardcoded versions flagged
2. Replace with `{{VERSION}}` placeholders
3. Commit again

## Version Examples

### Local Development Build
```
v3.2.2-3-gd6b5ce8
├── v3.2.2 (latest release tag)
├── 3 (commits ahead of tag)
└── gd6b5ce8 (short commit hash)
```

### Tagged Release Build
```
v3.2.3
└── v3.2.3 (exact tag match)
```

## Integration with CI/CD

The GitHub Actions workflow automatically:
1. Extracts version from git history
2. Runs all validation steps
3. Builds documentation with correct versions
4. Deploys to GitHub Pages
5. Validates deployment success

This ensures published documentation always shows correct versions matching the git repository state.

## Files Excluded from Version Management

- `CHANGELOG.md` - Contains historical version references
- `README.md` - Contains example version formats
- `*.html` and `*.pdf` - Generated files
- `build/` directory - Build artifacts
- `*.bak` files - Temporary backup files