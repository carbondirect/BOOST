#!/bin/bash

# BOOST Unified Documentation Build System
# Uses single source of truth (JSON schemas) to generate both HTML and PDF
# Ensures perfect consistency between both documentation formats

set -e  # Exit on any error

echo "🚀 BOOST Unified Documentation Build System"
echo "================================================="
echo "Building from single source of truth (JSON schemas)"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

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

# Check prerequisites
check_prerequisites() {
    print_status "🔍 Checking prerequisites..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "❌ Error: python3 not found. Please install Python 3."
        exit 1
    fi
    
    # Check Bikeshed
    if ! command -v bikeshed &> /dev/null; then
        print_error "❌ Error: bikeshed not found. Please install Bikeshed."
        exit 1
    fi
    
    # Check LaTeX
    if ! command -v pdflatex &> /dev/null; then
        print_warning "⚠️  Warning: pdflatex not found. PDF generation will be skipped."
        PDF_ENABLED=false
    else
        PDF_ENABLED=true
    fi
    
    # Check schema directory
    if [ ! -d "schema" ]; then
        print_error "❌ Error: schema directory not found."
        exit 1
    fi
    
    # Check unified generator
    if [ ! -f "scripts/generate-unified-content.py" ]; then
        print_error "❌ Error: scripts/generate-unified-content.py not found."
        exit 1
    fi
    
    print_success "✅ Prerequisites satisfied"
}

# Step 1: Generate unified content from schemas
generate_unified_content() {
    print_status "📊 Step 1: Generating unified content from schemas..."
    
    # Run unified content generator
    if python3 scripts/generate-unified-content.py --schema-dir schema; then
        print_success "✅ Unified content generation completed"
        
        # Count generated files
        BIKESHED_COUNT=$(find includes/generated -name "*.inc.md" 2>/dev/null | wc -l)
        LATEX_COUNT=$(find tex/entities -name "*.tex" 2>/dev/null | wc -l)
        
        print_status "📈 Generated content:"
        echo "   - Bikeshed includes: $BIKESHED_COUNT"
        echo "   - LaTeX entity tables: $LATEX_COUNT"
        
        if [ "$BIKESHED_COUNT" -ne "$LATEX_COUNT" ]; then
            print_warning "⚠️  Warning: Mismatch in generated file counts"
        fi
    else
        print_error "❌ Unified content generation failed"
        exit 1
    fi
}

# Step 2: Build HTML documentation with Bikeshed
build_html() {
    print_status "📄 Step 2: Building HTML documentation with Bikeshed..."
    
    # Update includes in boost-spec.bs to use generated content
    # This would normally be done by updating the .bs file to reference generated includes
    
    # Run Bikeshed build
    if [ -f "build-spec.sh" ]; then
        chmod +x build-spec.sh
        if ./build-spec.sh; then
            print_success "✅ HTML generation completed"
        else
            print_error "❌ HTML generation failed"
            exit 1
        fi
    else
        print_error "❌ build-spec.sh not found"
        exit 1
    fi
}

# Step 3: Build PDF documentation with LaTeX
build_pdf() {
    if [ "$PDF_ENABLED" = false ]; then
        print_warning "⚠️  Skipping PDF build (LaTeX not available)"
        return
    fi
    
    print_status "📄 Step 3: Building PDF documentation with LaTeX..."
    
    # Create build directory
    mkdir -p build
    
    # Run LaTeX build
    if [ -f "build-pdf.sh" ]; then
        chmod +x build-pdf.sh
        if ./build-pdf.sh; then
            print_success "✅ PDF generation completed"
        else
            print_error "❌ PDF generation failed"
            exit 1
        fi
    else
        # Fallback to direct LaTeX compilation
        for PASS in 1 2 3; do
            print_status "🔧 Running LaTeX compilation (Pass $PASS/3)..."
            
            pdflatex -shell-escape -interaction=nonstopmode -output-directory=build boost-spec.tex > build/latex-pass$PASS.log 2>&1
            
            if [ $? -eq 0 ]; then
                print_success "✅ Pass $PASS completed"
            else
                print_error "❌ LaTeX compilation failed on pass $PASS"
                tail -20 build/latex-pass$PASS.log
                exit 1
            fi
        done
    fi
}

# Step 4: Validate consistency
validate_consistency() {
    print_status "📊 Step 4: Validating HTML/PDF consistency..."
    
    if [ -f "scripts/validate-consistency.py" ]; then
        if python3 scripts/validate-consistency.py; then
            print_success "✅ Documentation consistency validated"
            
            # Show consistency score
            if [ -f "build/consistency-report.json" ]; then
                SCORE=$(python3 -c "import json; print(json.load(open('build/consistency-report.json'))['statistics']['consistency_score'])")
                echo "   📊 Consistency score: ${SCORE}%"
            fi
        else
            print_warning "⚠️  Consistency validation found issues"
            
            # Show details from report
            if [ -f "build/consistency-report.json" ]; then
                python3 -c "
import json
report = json.load(open('build/consistency-report.json'))
issues = report.get('inconsistencies', [])
if issues:
    print('   Issues found:')
    for issue in issues[:5]:  # Show first 5 issues
        print(f'   - {issue}')
    if len(issues) > 5:
        print(f'   ... and {len(issues)-5} more')
"
            fi
        fi
    else
        print_warning "⚠️  Consistency validator not found"
    fi
}

# Step 5: Generate final report
generate_report() {
    print_status "📋 Step 5: Generating build report..."
    
    # Collect statistics
    HTML_EXISTS=false
    PDF_EXISTS=false
    HTML_SIZE=0
    PDF_SIZE=0
    PDF_PAGES=0
    
    if [ -f "boost-spec.html" ]; then
        HTML_EXISTS=true
        HTML_SIZE=$(wc -c < boost-spec.html)
    fi
    
    if [ -f "build/boost-spec.pdf" ]; then
        PDF_EXISTS=true
        PDF_SIZE=$(wc -c < build/boost-spec.pdf)
        PDF_PAGES=$(pdfinfo build/boost-spec.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo '0')
    fi
    
    # Create report
    cat > build/unified-build-report.md << EOF
# BOOST Unified Build Report

## Build Summary
- **Date**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
- **Schema Count**: $(find schema -name "validation_schema.json" | wc -l)
- **HTML Generated**: $([ "$HTML_EXISTS" = true ] && echo "✅ Yes" || echo "❌ No")
- **PDF Generated**: $([ "$PDF_EXISTS" = true ] && echo "✅ Yes" || echo "❌ No")

## Output Files
EOF
    
    if [ "$HTML_EXISTS" = true ]; then
        echo "- **HTML**: boost-spec.html ($(echo $HTML_SIZE | numfmt --to=iec-i --suffix=B))" >> build/unified-build-report.md
    fi
    
    if [ "$PDF_EXISTS" = true ]; then
        echo "- **PDF**: build/boost-spec.pdf ($(echo $PDF_SIZE | numfmt --to=iec-i --suffix=B), $PDF_PAGES pages)" >> build/unified-build-report.md
    fi
    
    # Add consistency information
    if [ -f "build/consistency-report.json" ]; then
        SCORE=$(python3 -c "import json; print(json.load(open('build/consistency-report.json'))['statistics']['consistency_score'])")
        echo "" >> build/unified-build-report.md
        echo "## Consistency Validation" >> build/unified-build-report.md
        echo "- **Consistency Score**: ${SCORE}%" >> build/unified-build-report.md
    fi
    
    print_success "✅ Build report generated: build/unified-build-report.md"
}

# Clean up temporary files
cleanup() {
    print_status "🧹 Cleaning up temporary files..."
    
    # Remove auxiliary files but keep important outputs
    rm -f build/*.aux build/*.toc build/*.lof build/*.lot build/*.out build/*.fls build/*.fdb_latexmk
    
    # Clean up backup files
    find . -name "*.bak" -delete 2>/dev/null || true
    
    print_success "✅ Cleanup completed"
}

# Main execution
main() {
    echo "Starting unified build at: $(date)"
    START_TIME=$(date +%s)
    
    # Execute build steps
    check_prerequisites
    generate_unified_content
    build_html
    build_pdf
    validate_consistency
    generate_report
    cleanup
    
    # Calculate build time
    END_TIME=$(date +%s)
    BUILD_TIME=$((END_TIME - START_TIME))
    
    echo ""
    print_success "🎉 BOOST Unified Documentation Build Complete!"
    echo "================================================="
    echo "   ⏱️  Total build time: ${BUILD_TIME} seconds"
    
    if [ -f "boost-spec.html" ]; then
        echo "   📖 HTML: boost-spec.html"
    fi
    
    if [ -f "build/boost-spec.pdf" ]; then
        echo "   📖 PDF: build/boost-spec.pdf"
    fi
    
    echo "   📊 Reports: build/"
    echo ""
    echo "✨ Single Source of Truth build completed successfully!"
    echo "   Both HTML and PDF generated from the same schema-driven content"
}

# Trap to ensure cleanup happens even on error
trap 'print_error "Build interrupted"; cleanup; exit 1' INT TERM

# Run main function
main "$@"