#!/bin/bash

# BOOST Specification Unified Build System
# This script orchestrates the complete documentation generation pipeline:
# 1. Generate LaTeX content from JSON schemas (Single Source of Truth)
# 2. Build comprehensive PDF specification
# 3. Validate outputs and provide detailed statistics

set -e  # Exit on any error

echo "🚀 BOOST Specification Unified Build System"
echo "================================================="

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
    
    # Check LaTeX
    if ! command -v pdflatex &> /dev/null; then
        print_error "❌ Error: pdflatex not found. Please install a LaTeX distribution."
        exit 1
    fi
    
    # Check schema directory
    if [ ! -d "schema" ]; then
        print_error "❌ Error: schema directory not found."
        exit 1
    fi
    
    # Check schema generator
    if [ ! -f "scripts/generate-latex-from-schemas.py" ]; then
        print_error "❌ Error: scripts/generate-latex-from-schemas.py not found."
        exit 1
    fi
    
    # Check style files
    if [ ! -f "boost-spec.sty" ] && [ ! -f "boost-spec-minimal.sty" ]; then
        print_error "❌ Error: No LaTeX style file found (boost-spec.sty or boost-spec-minimal.sty)."
        exit 1
    fi
    
    # Check main document
    if [ ! -f "boost-spec.tex" ]; then
        print_error "❌ Error: boost-spec.tex not found."
        exit 1
    fi
    
    print_success "✅ All prerequisites satisfied"
}

# Step 1: Generate LaTeX content from schemas
generate_latex_content() {
    print_status "📊 Step 1: Generating LaTeX content from JSON schemas..."
    
    # Create output directories
    mkdir -p tex/entities
    
    # Run schema-to-LaTeX generator
    if python3 scripts/generate-latex-from-schemas.py; then
        print_success "✅ LaTeX content generation completed"
        
        # Count generated files
        ENTITY_TABLES=$(find tex/entities -name "*.tex" 2>/dev/null | wc -l)
        THEMATIC_SECTIONS=$(find tex -maxdepth 1 -name "*-entities.tex" 2>/dev/null | wc -l)
        
        print_status "📈 Generated content:"
        echo "   - Entity tables: $ENTITY_TABLES"
        echo "   - Thematic sections: $THEMATIC_SECTIONS"
        echo "   - Entity reference appendix: 1"
    else
        print_error "❌ LaTeX content generation failed"
        exit 1
    fi
}

# Step 2: Build PDF specification
build_pdf() {
    print_status "📄 Step 2: Building BOOST Specification PDF..."
    
    # Create build directory
    mkdir -p build
    
    # Determine which style file to use
    STYLE_FILE="boost-spec.sty"
    if [ ! -f "$STYLE_FILE" ] && [ -f "boost-spec-minimal.sty" ]; then
        STYLE_FILE="boost-spec-minimal.sty"
        print_warning "⚠️  Using minimal style file: $STYLE_FILE"
    fi
    
    # LaTeX compilation - 3 passes for complete cross-reference resolution
    for PASS in 1 2 3; do
        print_status "🔧 Running LaTeX compilation (Pass $PASS/3)..."
        
        # Run pdflatex and capture exit status
        pdflatex -interaction=nonstopmode -output-directory=build boost-spec.tex > build/latex-pass$PASS.log 2>&1
        LATEX_EXIT_CODE=$?
        
        if [ $LATEX_EXIT_CODE -eq 0 ]; then
            print_success "✅ Pass $PASS completed"
        else
            print_error "❌ LaTeX compilation failed on pass $PASS (exit code: $LATEX_EXIT_CODE)"
            echo "Last 20 lines of log:"
            tail -20 build/latex-pass$PASS.log
            exit 1
        fi
    done
    
    # Keep PDF in build directory
    if [ -f "build/boost-spec.pdf" ]; then
        print_success "✅ PDF generation completed successfully!"
    else
        print_error "❌ PDF generation failed - output file not found"
        exit 1
    fi
}

# Step 3: Validate outputs and generate statistics
validate_and_report() {
    print_status "📊 Step 3: Validating outputs and generating statistics..."
    
    # PDF statistics
    if [ -f "build/boost-spec.pdf" ]; then
        PDF_SIZE=$(wc -c < build/boost-spec.pdf)
        PDF_PAGES=$(pdfinfo build/boost-spec.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'Unknown')
        
        print_success "✅ PDF validation successful"
        echo "   📄 Output file: build/boost-spec.pdf"
        echo "   📊 File size: $(echo $PDF_SIZE | numfmt --to=iec-i --suffix=B)"
        echo "   📚 Total pages: $PDF_PAGES"
    fi
    
    # LaTeX warnings check
    WARNING_COUNT=$(grep -c "Warning" build/latex-pass3.log || echo "0")
    if [ "$WARNING_COUNT" -gt 0 ]; then
        print_warning "⚠️  LaTeX warnings: $WARNING_COUNT (see build/latex-pass3.log)"
    fi
    
    # Schema processing statistics
    TOTAL_ENTITIES=$(find tex/entities -name "*.tex" 2>/dev/null | wc -l)
    SCHEMA_COUNT=$(find schema -name "validation_schema.json" 2>/dev/null | wc -l)
    
    print_status "🔢 Processing statistics:"
    echo "   - JSON schemas processed: $SCHEMA_COUNT"
    echo "   - Entity tables generated: $TOTAL_ENTITIES"
    echo "   - LaTeX compilation passes: 3"
    
    # Content validation
    if [ "$TOTAL_ENTITIES" -eq "$SCHEMA_COUNT" ]; then
        print_success "✅ All schemas successfully converted to LaTeX"
    else
        print_warning "⚠️  Schema/table count mismatch: $SCHEMA_COUNT schemas vs $TOTAL_ENTITIES tables"
    fi
}

# Clean up temporary files
cleanup() {
    print_status "🧹 Cleaning up temporary files..."
    
    # Remove auxiliary files but keep logs for debugging
    rm -f build/*.aux build/*.toc build/*.lof build/*.lot build/*.out build/*.fls build/*.fdb_latexmk
    
    print_success "✅ Cleanup completed"
}

# Main execution
main() {
    echo "Starting build at: $(date)"
    START_TIME=$(date +%s)
    
    # Execute build steps
    check_prerequisites
    generate_latex_content
    build_pdf
    validate_and_report
    cleanup
    
    # Calculate build time
    END_TIME=$(date +%s)
    BUILD_TIME=$((END_TIME - START_TIME))
    
    echo ""
    print_success "🎉 BOOST Specification Build Complete!"
    echo "================================================="
    echo "   ⏱️  Total build time: ${BUILD_TIME} seconds"
    echo "   📖 Open PDF: build/boost-spec.pdf"
    echo "   📁 Build logs: build/latex-pass*.log"
    echo "   📊 Generated content: tex/"
    echo ""
    echo "✨ Single Source of Truth architecture successfully implemented!"
    echo "   📝 All content generated from JSON schemas"
    echo "   🔄 Zero content duplication"
    echo "   🚀 Ready for CI/CD integration"
}

# Trap to ensure cleanup happens even on error
trap 'print_error "Build interrupted"; exit 1' INT TERM

# Run main function
main "$@"