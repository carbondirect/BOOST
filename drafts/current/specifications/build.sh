#!/bin/bash

# BOOST Specification Consolidated Build System
# Comprehensive build script with support for PDF, HTML, or both formats
# Uses single source of truth (JSON schemas) with proper validation
#
# Usage:
#   ./build.sh           # Build both HTML and PDF (default)
#   ./build.sh --html    # Build HTML only  
#   ./build.sh --pdf     # Build PDF only
#   ./build.sh --help    # Show help

# Note: Not using set -e to allow custom error handling for LaTeX warnings

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Configuration flags
BUILD_HTML=true
BUILD_PDF=true
SHOW_HELP=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --html)
            BUILD_HTML=true
            BUILD_PDF=false
            shift
            ;;
        --pdf)
            BUILD_HTML=false
            BUILD_PDF=true
            shift
            ;;
        --help)
            SHOW_HELP=true
            shift
            ;;
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Function for colored output
print_status() {
    echo -e "${BLUE}$1${NC}"
}

print_success() {
    echo -e "${GREEN}$1${NC}"
}

print_warning() {
    echo -e "${YELLOW}$1${NC}"
}

print_error() {
    echo -e "${RED}$1${NC}"
}

print_header() {
    echo -e "${BOLD}$1${NC}"
}

show_help() {
    print_header "🚀 BOOST Specification Build System"
    echo
    echo "USAGE:"
    echo "  ./build.sh           Build both HTML and PDF documentation (default)"
    echo "  ./build.sh --html    Build HTML documentation only"
    echo "  ./build.sh --pdf     Build PDF documentation only"
    echo "  ./build.sh --help    Show this help message"
    echo
    echo "OUTPUTS:"
    echo "  HTML: boost-spec.html"
    echo "  PDF:  build/boost-spec.pdf"
    echo
    echo "FEATURES:"
    echo "  ✅ Single source of truth (JSON schemas)"
    echo "  ✅ Automated version management from git tags"
    echo "  ✅ LaTeX cleanup and optimization"
    echo "  ✅ HTML/PDF consistency validation"
    echo "  ✅ Comprehensive build statistics"
    echo "  ✅ Error handling with detailed logs"
    echo
}

# Show help and exit if requested
if [ "$SHOW_HELP" = true ]; then
    show_help
    exit 0
fi

# Record build start time
BUILD_START_TIME=$(date +%s)

print_header "🚀 BOOST Specification Build System"
echo "================================================="

if [ "$BUILD_HTML" = true ] && [ "$BUILD_PDF" = true ]; then
    print_status "📋 Building both HTML and PDF documentation"
elif [ "$BUILD_HTML" = true ]; then
    print_status "📋 Building HTML documentation only"
else
    print_status "📋 Building PDF documentation only"
fi

# Dependency checks
check_dependencies() {
    print_status "🔧 Checking build dependencies..."
    
    local DEPS_OK=true
    
    # Check Python for schema processing
    if ! command -v python3 &> /dev/null; then
        print_error "❌ Error: python3 not found. Required for schema processing."
        DEPS_OK=false
    fi
    
    # Check Bikeshed for HTML if needed
    if [ "$BUILD_HTML" = true ]; then
        if ! command -v bikeshed &> /dev/null; then
            print_error "❌ Error: bikeshed not found. Required for HTML generation."
            DEPS_OK=false
        fi
    fi
    
    # Check LaTeX for PDF if needed
    if [ "$BUILD_PDF" = true ]; then
        if ! command -v pdflatex &> /dev/null; then
            print_error "❌ Error: pdflatex not found. Required for PDF generation."
            DEPS_OK=false
        fi
    fi
    
    if [ "$DEPS_OK" = false ]; then
        print_error "❌ Missing required dependencies. Build cannot continue."
        exit 1
    fi
    
    print_success "✅ All dependencies available"
}

# Extract version from git tags
extract_version() {
    print_status "🔧 Extracting version information..."
    
    # Priority 1: Use RELEASE_VERSION from CI/CD workflows
    if [ -n "$RELEASE_VERSION" ]; then
        VERSION="$RELEASE_VERSION"
        print_success "✅ Using pre-extracted version from CI/CD: $VERSION"
    # Priority 2: Local development with git access
    elif git rev-parse --git-dir >/dev/null 2>&1; then
        # Try detailed version first (for development builds)
        if git describe --tags >/dev/null 2>&1; then
            VERSION=$(git describe --tags --always)
            print_success "📋 Using detailed git version: $VERSION"
        else
            # Fallback to latest tag only
            VERSION=$(git describe --tags --abbrev=0 2>/dev/null)
            if [ -z "$VERSION" ]; then
                # No tags found, use commit hash
                SHORT_HASH=$(git rev-parse --short HEAD)
                VERSION="v0.0.0-${SHORT_HASH}"
                print_warning "⚠️  No git tags found, using commit hash: $VERSION"
            else
                print_success "📋 Using latest git tag: $VERSION"
            fi
        fi
    # Priority 3: Fallback when neither CI environment nor git is available
    else
        VERSION="v0.0.0-no-version-detected"
        print_warning "⚠️  No version detection possible, using fallback: $VERSION"
    fi
    
    print_success "🎯 Version selected: $VERSION"
}

# Schema processing and LaTeX generation
generate_schemas() {
    print_status "📝 Step 1: Generating documentation from schemas..."
    
    if [ -f "scripts/generate-latex-from-schemas.py" ]; then
        if python3 scripts/generate-latex-from-schemas.py; then
            print_success "✅ Schema processing completed"
        else
            print_error "❌ Schema processing failed"
            exit 1
        fi
    else
        print_warning "⚠️  Schema generation script not found, using existing content"
    fi
}

# Version placeholder substitution
substitute_version() {
    print_status "🔧 Replacing version placeholders with $VERSION..."
    
    # Replace in main Bikeshed file (using pipe delimiter to avoid issues with special chars)
    if [ -f "boost-spec.bs" ]; then
        sed -i.bak "s|{{VERSION}}|$VERSION|g" boost-spec.bs
        echo "   Updated boost-spec.bs"
    fi
    
    # Replace in include files
    if [ -d "includes" ]; then
        find includes -name "*.md" -exec sed -i.bak "s|{{VERSION}}|$VERSION|g" {} \;
        echo "   Updated includes/*.md files"
    fi
    
    # Replace version placeholders in tex files  
    if [ -d "tex" ]; then
        find tex -name "*.tex" -exec sed -i.bak "s|{{VERSION}}|$VERSION|g" {} \;
        echo "   Updated tex/*.tex files"
    fi
}

# Clean LaTeX intermediate files
cleanup_latex_files() {
    print_status "🧹 Cleaning intermediate LaTeX files..."
    if [ -d "build" ]; then
        # Remove all LaTeX intermediate files
        rm -f build/*.aux build/*.toc build/*.lof build/*.lot build/*.out
        rm -f build/*.fls build/*.fdb_latexmk build/*.idx build/*.ind build/*.ilg
        rm -f build/*.nav build/*.snm build/*.vrb  # beamer files
        rm -f build/*.bbl build/*.blg              # bibtex files
        rm -f build/*.synctex.gz                   # sync files
        rm -f build/boost-spec.log                 # main log file (pass logs preserved)
        
        # Clean minted cache directory
        if [ -d "build/_minted" ]; then
            echo "   Clearing minted syntax highlighting cache..."
            rm -rf build/_minted
        fi
        
        # Ensure _minted directory exists with correct permissions for Docker
        mkdir -p build/_minted
        chmod 755 build/_minted
        echo "   Created _minted cache directory with proper permissions"
        
        print_success "   ✅ Intermediate files cleaned"
    fi
}

# Build HTML documentation
build_html() {
    print_status "📄 Step 2: Building HTML documentation..."
    
    # Generate HTML with Bikeshed
    print_status "🔧 Generating HTML with Bikeshed..."
    if bikeshed spec boost-spec.bs boost-spec.html --die-on=warning; then
        print_success "📝 Bikeshed HTML generation completed"
    else
        print_warning "⚠️  Bikeshed completed with warnings, attempting to continue..."
        # Try without die-on-warning
        if bikeshed spec boost-spec.bs boost-spec.html; then
            print_warning "📝 Bikeshed HTML generation completed with warnings"
        else
            print_error "❌ HTML generation failed"
            exit 1
        fi
    fi
    
    # Apply ReSpec-style CSS modifications
    print_status "🎨 Adding ReSpec-style CSS to HTML output..."
    
    python3 -c "
import re
import sys

# Read the generated HTML
try:
    with open('boost-spec.html', 'r') as f:
        html = f.read()
except Exception as e:
    print(f'ERROR: Could not read boost-spec.html: {e}')
    sys.exit(1)

# Add critical CSS overrides for proper layout
critical_overrides = '''<style>
/* Critical CSS overrides for proper ReSpec layout */
.main-content-wrapper {
    margin-left: 280px !important;
    width: calc(100vw - 280px) !important;
    box-sizing: border-box !important;
}
.main-content-wrapper.toc-collapsed {
    margin-left: 48px !important;
    width: calc(100vw - 48px) !important;
}
</style>'''

# Insert at end of body instead since there's no </head> tag
modified_html = re.sub(r'</body>', critical_overrides + '\n</body>', html)

try:
    with open('boost-spec.html', 'w') as f:
        f.write(modified_html)
    print('ReSpec-style CSS and layout modifications successfully added to boost-spec.html')
except Exception as e:
    print(f'ERROR: Could not write modified HTML: {e}')
    sys.exit(1)
"
    
    if [ $? -eq 0 ]; then
        print_success "✅ ReSpec-style CSS added successfully!"
    else
        print_error "❌ Failed to add ReSpec-style CSS"
        exit 1
    fi
    
    print_success "✅ HTML generation completed!"
}

# Build PDF documentation
build_pdf() {
    print_status "📄 Step 3: Building PDF documentation..."
    
    # Create output directory with proper permissions for Docker
    mkdir -p build
    chmod 755 build
    
    # Verify Pygments is available for minted
    if command -v pygmentize &> /dev/null; then
        echo "   Pygments available at: $(which pygmentize)"
    else
        print_warning "⚠️  pygmentize command not found, checking for python3 -m pygments"
        if python3 -c "import pygments; print('Pygments version:', pygments.__version__)" 2>/dev/null; then
            echo "   Pygments Python module available"
        else
            print_error "❌ Pygments not available - minted syntax highlighting will fail"
            exit 1
        fi
    fi
    
    # Clean intermediate files before building
    cleanup_latex_files
    
    # LaTeX compilation (3 passes for references)
    for pass in 1 2 3; do
        print_status "🔧 Running LaTeX compilation (Pass $pass/3)..."
        # For TeX Live 2021 compatibility, avoid -output-directory with minted
        pdflatex -shell-escape -interaction=nonstopmode boost-spec.tex > "build/latex-pass$pass.log" 2>&1
        LATEX_EXIT_CODE=$?
        
        # Check for critical LaTeX errors regardless of exit code
        CRITICAL_ERRORS=$(grep -c "^! \|Emergency stop\|Fatal error\|Runaway argument" "build/latex-pass$pass.log" 2>/dev/null || echo "0")
        
        if [ $LATEX_EXIT_CODE -eq 0 ]; then
            echo "   Pass $pass completed successfully"
        elif [ "$CRITICAL_ERRORS" -gt 0 ]; then
            print_error "❌ LaTeX compilation failed on pass $pass with critical errors"
            echo "Critical errors found:"
            grep -A2 "^! \|Emergency stop\|Fatal error\|Runaway argument" "build/latex-pass$pass.log" || echo "See build/latex-pass$pass.log for details"
            exit 1
        elif [ -f "boost-spec.pdf" ]; then
            print_warning "⚠️  Pass $pass completed with non-critical warnings (exit code: $LATEX_EXIT_CODE)"
            echo "   PDF was generated successfully despite warnings"
        elif [ $pass -eq 3 ]; then
            # Only fail on final pass if PDF wasn't generated and no critical errors
            print_error "❌ LaTeX compilation failed on final pass $pass (exit code: $LATEX_EXIT_CODE)"
            echo ""
            echo "🔍 LaTeX Error Analysis:"
            echo "========================"
            
            # Show critical errors first
            if grep -q "^! \|Emergency stop\|Fatal error" "build/latex-pass$pass.log" 2>/dev/null; then
                echo "Critical LaTeX errors:"
                grep -A3 -B1 "^! \|Emergency stop\|Fatal error" "build/latex-pass$pass.log" | head -20
                echo ""
            fi
            
            # Show undefined control sequence errors
            if grep -q "Undefined control sequence" "build/latex-pass$pass.log" 2>/dev/null; then
                echo "Undefined control sequence errors:"
                grep -A2 -B1 "Undefined control sequence" "build/latex-pass$pass.log" | head -10
                echo ""
            fi
            
            # Show missing file errors
            if grep -q "File.*not found\|No file" "build/latex-pass$pass.log" 2>/dev/null; then
                echo "Missing file errors:"
                grep -A1 -B1 "File.*not found\|No file" "build/latex-pass$pass.log" | head -10
                echo ""
            fi
            
            echo "Last 20 lines of log:"
            tail -20 "build/latex-pass$pass.log"
            echo ""
            echo "💡 Full log available at: build/latex-pass$pass.log"
            exit 1
        else
            # Early passes: warnings are acceptable, continue to next pass
            print_warning "⚠️  Pass $pass completed with warnings (exit code: $LATEX_EXIT_CODE)"
            echo "   Continuing to next pass - warnings are expected in early LaTeX passes"
        fi
        
        # Report warnings summary for each pass
        WARNING_COUNT=$(grep -c "LaTeX Warning\|pdfTeX warning" "build/latex-pass$pass.log" 2>/dev/null || echo "0")
        if [ "$WARNING_COUNT" -gt 0 ]; then
            echo "   Found $WARNING_COUNT LaTeX warnings"
        fi
    done
    
    # Move generated PDF to build directory for consistency
    if [ -f "boost-spec.pdf" ]; then
        mv boost-spec.pdf build/
        # Also move other LaTeX output files to build directory
        mv boost-spec.aux build/ 2>/dev/null || true
        mv boost-spec.log build/ 2>/dev/null || true  
        mv boost-spec.toc build/ 2>/dev/null || true
        mv boost-spec.out build/ 2>/dev/null || true
        mv boost-spec.fls build/ 2>/dev/null || true
        mv boost-spec.fdb_latexmk build/ 2>/dev/null || true
        print_success "✅ PDF generation completed successfully!"
        
        # Comprehensive warning analysis
        print_status "🔍 Analyzing LaTeX warnings and issues..."
        
        # Check for remaining undefined references (should be resolved by pass 3)
        UNDEFINED_REFS=$(grep -c "LaTeX Warning: Reference .* undefined" "build/latex-pass3.log" 2>/dev/null || echo "0")
        UNDEFINED_CITES=$(grep -c "LaTeX Warning: Citation .* undefined" "build/latex-pass3.log" 2>/dev/null || echo "0")
        RERUN_WARNINGS=$(grep -c "LaTeX Warning: Label(s) may have changed. Rerun" "build/latex-pass3.log" 2>/dev/null || echo "0")
        
        if [ "${UNDEFINED_REFS:-0}" -gt 0 ] 2>/dev/null; then
            print_warning "⚠️  Found $UNDEFINED_REFS undefined references in final pass"
            grep "LaTeX Warning: Reference .* undefined" "build/latex-pass3.log" | head -5
        fi
        
        if [ "${UNDEFINED_CITES:-0}" -gt 0 ] 2>/dev/null; then
            print_warning "⚠️  Found $UNDEFINED_CITES undefined citations in final pass"
            grep "LaTeX Warning: Citation .* undefined" "build/latex-pass3.log" | head -5
        fi
        
        if [ "${RERUN_WARNINGS:-0}" -gt 0 ] 2>/dev/null; then
            print_warning "⚠️  Labels may have changed - consider adding a 4th LaTeX pass"
        fi
        
        # Summary of acceptable vs problematic warnings
        TOTAL_WARNINGS=$(grep -c "LaTeX Warning\|pdfTeX warning" "build/latex-pass3.log" 2>/dev/null || echo "0")
        ACCEPTABLE_WARNINGS=$(grep -c "destination with the same identifier\|File .* has changed" "build/latex-pass3.log" 2>/dev/null || echo "0")
        PROBLEMATIC_WARNINGS=$((TOTAL_WARNINGS - ACCEPTABLE_WARNINGS))
        
        if [ "$PROBLEMATIC_WARNINGS" -gt 0 ]; then
            print_warning "📊 Warning Summary: $PROBLEMATIC_WARNINGS problematic warnings, $ACCEPTABLE_WARNINGS acceptable warnings"
        else
            echo "   📊 Warning Summary: All $TOTAL_WARNINGS warnings are acceptable (page identifiers, file changes)"
        fi
        
    else
        print_error "❌ PDF generation failed - output file not found"
        exit 1
    fi
}

# Generate build statistics and validation
generate_statistics() {
    print_status "📊 Step 4: Generating build statistics and validation..."
    
    # Initialize statistics
    local HTML_EXISTS=false
    local PDF_EXISTS=false
    local HTML_SIZE=0
    local PDF_SIZE=0
    local PDF_PAGES=0
    
    # Collect HTML statistics
    if [ -f "boost-spec.html" ]; then
        HTML_EXISTS=true
        HTML_SIZE=$(wc -c < boost-spec.html)
    fi
    
    # Collect PDF statistics
    if [ -f "build/boost-spec.pdf" ]; then
        PDF_EXISTS=true
        PDF_SIZE=$(wc -c < build/boost-spec.pdf)
        PDF_PAGES=$(pdfinfo build/boost-spec.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'Unknown')
        
        # Check for LaTeX warnings
        WARNING_COUNT=$(grep -c "Warning" build/latex-pass3.log 2>/dev/null || echo "0")
    fi
    
    # Display statistics
    print_success "📊 Build Statistics:"
    
    if [ "$HTML_EXISTS" = true ]; then
        echo "   📄 HTML: boost-spec.html ($(echo $HTML_SIZE | numfmt --to=iec-i --suffix=B))"
    fi
    
    if [ "$PDF_EXISTS" = true ]; then
        echo "   📄 PDF: build/boost-spec.pdf ($(echo $PDF_SIZE | numfmt --to=iec-i --suffix=B), $PDF_PAGES pages)"
        if [ "$WARNING_COUNT" -gt 0 ] 2>/dev/null; then
            echo "   ⚠️  LaTeX warnings: $WARNING_COUNT (see build/latex-pass3.log)"
        fi
    fi
    
    echo "   🔧 LaTeX passes: 3"
    
    # Run consistency validation if available
    if [ -f "scripts/validate-consistency.py" ] && [ "$HTML_EXISTS" = true ] && [ "$PDF_EXISTS" = true ]; then
        print_status "🔍 Running documentation consistency check..."
        if python3 scripts/validate-consistency.py >/dev/null 2>&1; then
            print_success "   ✅ HTML/PDF consistency check passed"
        else
            print_warning "   ⚠️  Consistency check found issues (see build/consistency-report.json)"
        fi
    fi
}

# Restore version placeholders
restore_version_placeholders() {
    print_status "🧹 Restoring version placeholders in source files..."
    
    # Restore main Bikeshed file
    if [ -f "boost-spec.bs" ]; then
        sed -i.bak "s|$VERSION|{{VERSION}}|g" boost-spec.bs
        rm -f boost-spec.bs.bak 2>/dev/null || true
        echo "   Restored boost-spec.bs"
    fi
    
    # Restore include files
    if [ -d "includes" ]; then
        find includes -name "*.md" -exec sed -i.bak "s|$VERSION|{{VERSION}}|g" {} \;
        find includes -name "*.bak" -delete 2>/dev/null || true
        echo "   Restored includes/*.md files"
    fi
    
    # Restore tex files
    if [ -d "tex" ]; then
        find tex -name "*.tex" -exec sed -i.bak "s|$VERSION|{{VERSION}}|g" {} \;
        find tex -name "*.bak" -delete 2>/dev/null || true  
        echo "   Restored tex/*.tex files"
    fi
}

# Final cleanup
final_cleanup() {
    print_status "🧹 Final cleanup..."
    
    # Clean up intermediate files but keep logs and outputs
    if [ "$BUILD_PDF" = true ]; then
        rm -f build/*.aux build/*.toc build/*.lof build/*.lot build/*.out
        rm -f build/*.fls build/*.fdb_latexmk build/*.idx build/*.ind build/*.ilg
        rm -f build/*.nav build/*.snm build/*.vrb
        rm -f build/*.bbl build/*.blg
        rm -f build/*.synctex.gz
        # Keep _minted cache for faster subsequent builds
    fi
    
    print_success "✅ Cleanup completed"
}

# Main build process
main() {
    # Check dependencies
    check_dependencies
    
    # Extract version information
    extract_version
    
    # Generate schema-driven content
    generate_schemas
    
    # Substitute version placeholders
    substitute_version
    
    # Build HTML if requested
    if [ "$BUILD_HTML" = true ]; then
        build_html
    fi
    
    # Build PDF if requested
    if [ "$BUILD_PDF" = true ]; then
        build_pdf
    fi
    
    # Generate statistics and validation
    generate_statistics
    
    # Restore version placeholders
    restore_version_placeholders
    
    # Final cleanup
    final_cleanup
    
    # Calculate build time
    BUILD_END_TIME=$(date +%s)
    BUILD_TIME=$((BUILD_END_TIME - BUILD_START_TIME))
    
    # Success message
    print_header "🎉 Build Completed Successfully!"
    print_success "================================================="
    echo "   ⏱️  Total build time: ${BUILD_TIME} seconds"
    
    if [ "$BUILD_HTML" = true ] && [ -f "boost-spec.html" ]; then
        echo "   📖 HTML: boost-spec.html"
    fi
    
    if [ "$BUILD_PDF" = true ] && [ -f "build/boost-spec.pdf" ]; then
        echo "   📖 PDF: build/boost-spec.pdf"
        echo "   📁 Logs: build/latex-pass*.log"
    fi
    
    echo "   ✨ Git tag-based version management: $VERSION"
    echo "   📊 Single source of truth: JSON schemas → Documentation"
}

# Error handling
trap 'print_error "❌ Build failed. Check error messages above."; restore_version_placeholders 2>/dev/null; exit 1' ERR

# Run main build process
main

print_success "✨ BOOST Specification build system completed successfully!"