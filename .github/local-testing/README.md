# 🧪 Local CI/CD Testing

This directory contains tools for testing the BOOST documentation CI/CD pipeline locally before pushing to GitHub.

## 🚀 Quick Start

1. **Setup (one-time)**:
   ```bash
   cd .github/local-testing
   ./setup.sh
   ```

2. **Run tests**:
   ```bash
   ./test-local.sh                    # Run all native tests (fastest)
   ./test-local.sh schema --verbose   # Test schema validation with details
   ./test-local.sh --act build        # Test build using GitHub Actions simulation
   ```

## 🎯 What Can Be Tested Locally

### ✅ **Fully Testable (Native Mode)**
- **Schema Validation**: JSON syntax, structure, FK integrity
- **Documentation Build**: HTML generation, ReSpec styling, output validation
- **Version Analysis**: Version format validation, type detection
- **Build Scripts**: All build components and validation logic

### ✅ **Testable with Act (GitHub Actions Simulation)**  
- **Complete Workflows**: Full workflow execution simulation
- **Environment Variables**: Test with real GitHub Actions environment
- **Job Dependencies**: Multi-job workflow testing
- **Matrix Builds**: Parallel execution testing

### ⚠️ **Limited/Simulated**
- **GitHub API Calls**: Requires real tokens, limited rate limits
- **GitHub Pages Deployment**: Can be simulated but not actually deployed
- **Release Creation**: Can test logic but won't create real releases
- **Pull Request Events**: Simulated events, not real PRs

### ❌ **Cannot Be Tested Locally**
- **Real GitHub Pages Deployment**: Must push to test actual deployment
- **Real Release Creation**: Requires actual repository and permissions
- **Branch Protection Rules**: GitHub-specific features
- **Workflow Triggers**: Real PR/push/tag events

## 🛠️ Testing Tools

### **Native Testing (Fastest)**
- Direct execution of validation scripts
- Immediate feedback
- No Docker dependency
- Limited to script logic testing

```bash
./test-local.sh schema              # Test schema validation
./test-local.sh build               # Test documentation build  
./test-local.sh version-check       # Test version analysis
./test-local.sh all                 # Run all native tests
```

### **Act Testing (Most Complete)**
- Full GitHub Actions workflow simulation
- Real environment variable handling
- Complete job execution
- Requires Docker

```bash
./test-local.sh --act pr-validation # Simulate PR validation workflow
./test-local.sh --act build         # Simulate build workflow
./test-local.sh --act release       # Simulate release workflow (needs token)
```

## 📋 Test Types

### **Schema Validation** (`schema`)
Tests all JSON schema files for:
- Valid JSON syntax
- Required schema structure
- BOOST metadata completeness
- Foreign key pattern validation
- Entity relationship integrity

```bash
./test-local.sh schema --verbose
```

### **Documentation Build** (`build`)
Tests the complete documentation build process:
- Bikeshed HTML generation
- ReSpec CSS styling application
- Output file validation
- Content verification
- File size checks

```bash
./test-local.sh build
```

### **PR Validation** (`pr-validation`)
Combines schema validation and build testing:
- All schema validation checks
- Complete build process
- Output quality validation
- Simulates PR workflow checks

```bash
./test-local.sh pr-validation
```

### **Release Workflow** (`release`)
Tests release workflow components:
- Version format validation
- Major version detection
- Release notes generation
- Artifact package creation (simulated)

```bash
./test-local.sh release
# or with act for full simulation:
./test-local.sh --act release
```

### **Version Check** (`version-check`)
Tests version analysis logic:
- Version format parsing
- Major/minor/patch detection
- Release policy enforcement
- Version increment validation

```bash
./test-local.sh version-check
```

## ⚙️ Configuration

### **Environment Variables** (`.env`)
```bash
# Test version for release workflows
TEST_VERSION=v3.0.0

# Repository simulation
GITHUB_REPOSITORY=carbondirect/BOOST
GITHUB_REF_NAME=main
GITHUB_SHA=abc123456789
```

### **Secrets** (`.secrets`)
```bash
# GitHub token for API testing (optional)
GITHUB_TOKEN=ghp_your_token_here
```

### **Act Configuration** (`.actrc`)
```bash
# Ubuntu images for GitHub Actions simulation
-P ubuntu-latest=catthehacker/ubuntu:act-latest

# Environment and artifacts
--env-file .github/local-testing/.env
--artifact-server-path .github/local-testing/artifacts
```

## 📊 Test Output

### **Success Example**
```
🧪 BOOST CI/CD Local Testing
=============================

🔍 Checking prerequisites...
✅ Native dependencies are available
🔍 Testing schema validation...
✅ Schema validation passed for 34 schemas
🔍 Testing documentation build...
✅ Build completed successfully (472,623 bytes)
✅ Generated HTML contains expected BOOST content
✅ All tests completed successfully!
```

### **Failure Example**
```
🧪 BOOST CI/CD Local Testing
=============================

❌ Schema validation errors:
  - geographic_data: Missing primary key pattern
  - material_processing: Foreign key field missing validation pattern

❌ Build failed - no HTML output generated
```

## 🎯 Testing Strategy

### **Before Every Commit**
```bash
./test-local.sh all
```

### **Before Major Changes**
```bash
./test-local.sh --act pr-validation
```

### **Before Release**
```bash
./test-local.sh --act release
```

### **Continuous Development**
```bash
# Quick schema check after schema changes
./test-local.sh schema

# Quick build check after documentation changes
./test-local.sh build
```

## 🚨 Troubleshooting

### **Common Issues**

**Docker not running (act mode)**:
```bash
# Start Docker Desktop or Docker daemon
docker info  # Should show Docker info
```

**Missing dependencies**:
```bash
./setup.sh  # Re-run setup script
```

**Bikeshed errors**:
```bash
bikeshed update  # Update Bikeshed spec database
```

**Permission denied**:
```bash
chmod +x setup.sh test-local.sh
```

### **Debugging Options**

**Verbose output**:
```bash
./test-local.sh schema --verbose
```

**Dry run (see what would happen)**:
```bash
./test-local.sh build --dry-run
```

**Act debugging**:
```bash
./test-local.sh --act pr-validation --verbose
```

## 🔗 Integration with Development Workflow

### **Recommended Workflow**

1. **Make changes** to schemas, documentation, or workflows
2. **Test locally** with appropriate test type:
   ```bash
   ./test-local.sh schema      # After schema changes
   ./test-local.sh build       # After documentation changes  
   ./test-local.sh all         # Before committing
   ```
3. **Fix any issues** identified locally
4. **Commit and push** with confidence
5. **GitHub Actions** will run the same tests in the cloud

### **Git Hooks Integration** (Optional)

Add to `.git/hooks/pre-commit`:
```bash
#!/bin/bash
cd .github/local-testing
./test-local.sh all --verbose
```

This ensures all tests pass before every commit.

## 📈 Benefits

- **🚀 Faster Development**: Catch issues before pushing
- **💰 Cost Effective**: Reduce GitHub Actions minutes usage
- **🔍 Better Debugging**: Local logs and immediate feedback
- **🛡️ Quality Assurance**: Same validation logic as production
- **⚡ Quick Iteration**: Test changes instantly

## 🎉 Summary

Local testing provides **80-90% coverage** of the CI/CD pipeline functionality, allowing you to:

- Validate all schemas and catch integrity issues
- Test complete documentation builds
- Simulate GitHub Actions workflows
- Debug issues with immediate feedback
- Reduce failed pushes and iterations

For the remaining 10-20% (actual deployments, real GitHub API interactions), you'll still need to push to GitHub, but with much higher confidence that everything will work! 🚀