#!/bin/bash

# Local CI/CD Testing Script
# This script runs various CI/CD workflow components locally

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOCAL_TEST_DIR="$PROJECT_ROOT/.github/local-testing"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging
log() {
    echo -e "${BLUE}[$(date '+%H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Help function
show_help() {
    cat << EOF
🧪 Local CI/CD Testing Script

Usage: $0 [OPTIONS] [TEST_TYPE]

TEST_TYPES:
    all             Run all available tests (default)
    schema          Test schema validation
    build           Test documentation build
    pr-validation   Test PR validation workflow
    release         Test release workflow (requires GitHub token)
    version-check   Test version checking

OPTIONS:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -d, --dry-run   Show what would be tested without running
    --act           Use act to run GitHub Actions locally
    --native        Run native scripts without act (faster, limited)

EXAMPLES:
    $0                          # Run all native tests
    $0 schema --verbose         # Test schema validation with verbose output
    $0 --act pr-validation      # Run PR validation using act
    $0 build --dry-run          # Show what build test would do

REQUIREMENTS:
    - Run setup.sh first to install dependencies
    - For --act mode: Docker must be running
    - For release tests: GitHub token in .secrets file

EOF
}

# Parse arguments
VERBOSE=false
DRY_RUN=false
USE_ACT=false
TEST_TYPE="all"

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -d|--dry-run)
            DRY_RUN=true
            shift
            ;;
        --act)
            USE_ACT=true
            shift
            ;;
        --native)
            USE_ACT=false
            shift
            ;;
        schema|build|pr-validation|release|version-check|all)
            TEST_TYPE=$1
            shift
            ;;
        *)
            error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Check prerequisites
check_prerequisites() {
    log "Checking prerequisites..."
    
    if [ "$USE_ACT" = true ]; then
        if ! command -v act &> /dev/null; then
            error "act is not installed. Run setup.sh first or use --native mode"
            exit 1
        fi
        
        if ! docker info &> /dev/null; then
            error "Docker is not running. Please start Docker for act to work"
            exit 1
        fi
        
        success "act and Docker are available"
    else
        # Check native dependencies
        local missing=()
        
        command -v python3 &> /dev/null || missing+=("python3")
        command -v bikeshed &> /dev/null || missing+=("bikeshed")
        
        if [ ${#missing[@]} -ne 0 ]; then
            error "Missing dependencies: ${missing[*]}"
            echo "Run setup.sh to install dependencies"
            exit 1
        fi
        
        success "Native dependencies are available"
    fi
}

# Test schema validation
test_schema_validation() {
    log "Testing schema validation..."
    
    if [ "$DRY_RUN" = true ]; then
        echo "Would run schema validation tests"
        return 0
    fi
    
    if [ "$USE_ACT" = true ]; then
        # Use act to run schema validation workflow
        cd "$PROJECT_ROOT"
        act -j validate-schemas \
            --env-file "$LOCAL_TEST_DIR/.env" \
            --secret-file "$LOCAL_TEST_DIR/.secrets" \
            -W .github/workflows/schema-validation.yml
    else
        # Run native schema validation
        cd "$PROJECT_ROOT/drafts/current/specifications"
        
        python3 -c "
import json
import sys
import os
from pathlib import Path

schema_dir = Path('../schema')
errors = []
validated = 0
verbose = os.environ.get('VERBOSE', 'false') == 'true'

print('🔍 Validating JSON Schema files...')

for schema_file in schema_dir.rglob('validation_schema.json'):
    try:
        with open(schema_file, 'r') as f:
            schema_data = json.load(f)
        
        # Basic validation
        if 'schema' not in schema_data:
            errors.append(f'{schema_file}: Missing schema key')
            continue
        
        validated += 1
        if verbose:
            print(f'✅ {schema_file.relative_to(schema_dir)}')
        
    except json.JSONDecodeError as e:
        errors.append(f'{schema_file}: Invalid JSON - {e}')
    except Exception as e:
        errors.append(f'{schema_file}: Error - {e}')

if errors:
    print('❌ Schema validation errors:')
    for error in errors:
        print(f'  - {error}')
    sys.exit(1)

print(f'✅ Schema validation passed for {validated} schemas')
" VERBOSE=$VERBOSE
    fi
    
    success "Schema validation test completed"
}

# Test documentation build
test_build() {
    log "Testing documentation build..."
    
    if [ "$DRY_RUN" = true ]; then
        echo "Would run documentation build test"
        return 0
    fi
    
    cd "$PROJECT_ROOT/drafts/current/specifications"
    
    # Check if build script exists and is executable
    if [ ! -x "build-spec.sh" ]; then
        error "build-spec.sh not found or not executable"
        return 1
    fi
    
    # Create backup of any existing HTML
    if [ -f "boost-spec.html" ]; then
        mv boost-spec.html boost-spec.html.backup
        warning "Backed up existing boost-spec.html"
    fi
    
    # Run build
    log "Running build script..."
    if [ "$VERBOSE" = true ]; then
        ./build-spec.sh
    else
        ./build-spec.sh > "$LOCAL_TEST_DIR/logs/build.log" 2>&1
    fi
    
    # Validate output
    if [ -f "boost-spec.html" ]; then
        local size=$(wc -c < boost-spec.html)
        if [ "$size" -gt 100000 ]; then
            success "Build completed successfully (${size} bytes)"
        else
            warning "Build completed but output is small (${size} bytes)"
        fi
        
        # Basic content check
        if grep -q "BOOST" boost-spec.html; then
            success "Generated HTML contains expected BOOST content"
        else
            warning "Generated HTML may be missing BOOST content"
        fi
    else
        error "Build failed - no HTML output generated"
        return 1
    fi
    
    # Restore backup if it existed
    if [ -f "boost-spec.html.backup" ]; then
        mv boost-spec.html.backup boost-spec.html
        log "Restored original boost-spec.html"
    fi
}

# Test PR validation
test_pr_validation() {
    log "Testing PR validation workflow..."
    
    if [ "$DRY_RUN" = true ]; then
        echo "Would run PR validation tests"
        return 0
    fi
    
    if [ "$USE_ACT" = true ]; then
        cd "$PROJECT_ROOT"
        act pull_request \
            --env-file "$LOCAL_TEST_DIR/.env" \
            --secret-file "$LOCAL_TEST_DIR/.secrets" \
            -W .github/workflows/validate-pr.yml
    else
        # Run native PR validation components
        log "Running schema validation component..."
        test_schema_validation
        
        log "Running build test component..."
        test_build
    fi
    
    success "PR validation test completed"
}

# Test release workflow
test_release() {
    log "Testing release workflow..."
    
    if [ "$DRY_RUN" = true ]; then
        echo "Would run release workflow test"
        return 0
    fi
    
    # Check for GitHub token
    if [ "$USE_ACT" = true ] && [ ! -f "$LOCAL_TEST_DIR/.secrets" ]; then
        warning "No secrets file found. Some release tests may fail."
        warning "Create $LOCAL_TEST_DIR/.secrets with GITHUB_TOKEN for full testing"
    fi
    
    if [ "$USE_ACT" = true ]; then
        cd "$PROJECT_ROOT"
        # Simulate a tag push
        act push \
            --env-file "$LOCAL_TEST_DIR/.env" \
            --secret-file "$LOCAL_TEST_DIR/.secrets" \
            -W .github/workflows/release.yml \
            --input version=v3.0.0
    else
        # Native release testing (limited)
        log "Testing version validation logic..."
        
        # Test version parsing
        local test_versions=("v3.0.0" "v2.1.0" "v2.1.1" "invalid")
        
        for version in "${test_versions[@]}"; do
            log "Testing version: $version"
            
            if echo "$version" | grep -qE "^v[0-9]+\.[0-9]+\.[0-9]+$"; then
                success "Valid version format: $version"
                
                # Check if major version
                local clean_version=$(echo "$version" | sed 's/^v//')
                local minor=$(echo "$clean_version" | cut -d. -f2)
                local patch=$(echo "$clean_version" | cut -d. -f3)
                
                if [ "$minor" = "0" ] && [ "$patch" = "0" ]; then
                    success "Major version detected: $version"
                else
                    log "Non-major version: $version"
                fi
            else
                warning "Invalid version format: $version"
            fi
        done
    fi
    
    success "Release workflow test completed"
}

# Test version check
test_version_check() {
    log "Testing version check workflow..."
    
    if [ "$DRY_RUN" = true ]; then
        echo "Would run version check tests"
        return 0
    fi
    
    # Native version analysis testing
    local test_cases=(
        "v2.1.0:minor"
        "v2.0.1:patch"
        "v3.0.0:major"
    )
    
    for case in "${test_cases[@]}"; do
        local version=$(echo "$case" | cut -d: -f1)
        local expected_type=$(echo "$case" | cut -d: -f2)
        
        log "Testing version analysis: $version"
        
        # Parse version
        local clean_version=$(echo "$version" | sed 's/^v//')
        local major=$(echo "$clean_version" | cut -d. -f1)
        local minor=$(echo "$clean_version" | cut -d. -f2)
        local patch=$(echo "$clean_version" | cut -d. -f3)
        
        # Determine actual type
        local actual_type=""
        if [ "$minor" = "0" ] && [ "$patch" = "0" ]; then
            actual_type="major"
        elif [ "$patch" = "0" ]; then
            actual_type="minor"
        else
            actual_type="patch"
        fi
        
        if [ "$actual_type" = "$expected_type" ]; then
            success "Correct type detected: $version → $actual_type"
        else
            error "Type mismatch: $version → expected $expected_type, got $actual_type"
        fi
    done
    
    success "Version check test completed"
}

# Main test runner
main() {
    echo "🧪 BOOST CI/CD Local Testing"
    echo "============================="
    echo ""
    
    check_prerequisites
    
    # Create logs directory
    mkdir -p "$LOCAL_TEST_DIR/logs"
    
    case $TEST_TYPE in
        schema)
            test_schema_validation
            ;;
        build)
            test_build
            ;;
        pr-validation)
            test_pr_validation
            ;;
        release)
            test_release
            ;;
        version-check)
            test_version_check
            ;;
        all)
            log "Running all available tests..."
            test_schema_validation
            test_build
            test_pr_validation
            test_version_check
            # Skip release test in 'all' mode unless explicitly using act
            if [ "$USE_ACT" = true ]; then
                test_release
            else
                warning "Skipping release test in native mode (use --act for full release testing)"
            fi
            ;;
    esac
    
    echo ""
    success "All tests completed successfully!"
    echo ""
    echo "📋 Test results available in: $LOCAL_TEST_DIR/logs/"
    echo "🚀 Ready to push to GitHub for full CI/CD testing"
}

# Run main function
main "$@"