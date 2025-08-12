#!/bin/bash

# BOOST Specification PDF Build Script
# This script generates PDF output from the LaTeX specification using boost-spec.sty

set -e  # Exit on any error

echo "📄 Building BOOST Specification PDF..."

# Check if LaTeX is available
if ! command -v pdflatex &> /dev/null; then
    echo "❌ Error: pdflatex not found. Please install a LaTeX distribution."
    exit 1
fi

# Check if boost-spec.sty exists
if [ ! -f "boost-spec.sty" ]; then
    echo "❌ Error: boost-spec.sty not found. Please ensure the style file is in the current directory."
    exit 1
fi

# Check if main document exists
if [ ! -f "boost-spec.tex" ]; then
    echo "❌ Error: boost-spec.tex not found. Please ensure the main LaTeX document exists."
    exit 1
fi

# Create output directory for temporary files
mkdir -p build

echo "🔧 Running LaTeX compilation (Pass 1/3)..."
# First pass - process document structure (with shell-escape for minted)
pdflatex -shell-escape -interaction=nonstopmode -output-directory=build boost-spec.tex > build/latex-pass1.log 2>&1

if [ $? -ne 0 ]; then
    echo "❌ LaTeX compilation failed on pass 1. Check build/latex-pass1.log for details."
    echo "Last 20 lines of log:"
    tail -20 build/latex-pass1.log
    exit 1
fi

echo "🔧 Running LaTeX compilation (Pass 2/3)..."
# Second pass - resolve cross-references (with shell-escape for minted)
pdflatex -shell-escape -interaction=nonstopmode -output-directory=build boost-spec.tex > build/latex-pass2.log 2>&1

if [ $? -ne 0 ]; then
    echo "❌ LaTeX compilation failed on pass 2. Check build/latex-pass2.log for details."
    echo "Last 20 lines of log:"
    tail -20 build/latex-pass2.log
    exit 1
fi

echo "🔧 Running LaTeX compilation (Pass 3/3)..."
# Third pass - finalize document with all references resolved (with shell-escape for minted)
pdflatex -shell-escape -interaction=nonstopmode -output-directory=build boost-spec.tex > build/latex-pass3.log 2>&1

if [ $? -ne 0 ]; then
    echo "❌ LaTeX compilation failed on pass 3. Check build/latex-pass3.log for details."
    echo "Last 20 lines of log:"
    tail -20 build/latex-pass3.log
    exit 1
fi

# Keep PDF in build directory
if [ -f "build/boost-spec.pdf" ]; then
    echo "✅ PDF generation completed successfully!"
    echo "📄 Output file: build/boost-spec.pdf"
    
    # Calculate file size
    PDF_SIZE=$(wc -c < build/boost-spec.pdf)
    
    echo "📊 Build statistics:"
    echo "   - PDF output size: $(echo $PDF_SIZE | numfmt --to=iec-i --suffix=B)"
    echo "   - Total pages: $(pdfinfo build/boost-spec.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'Unknown')"
    echo "   - LaTeX passes: 3"
    
    # Check for warnings in final log
    WARNING_COUNT=$(grep -c "Warning" build/latex-pass3.log || echo "0")
    if [ "$WARNING_COUNT" -gt 0 ]; then
        echo "⚠️  LaTeX warnings: $WARNING_COUNT (see build/latex-pass3.log)"
    fi
    
    # Clean up auxiliary files but keep logs and PDF
    echo "🧹 Cleaning up temporary files..."
    rm -f build/*.aux build/*.toc build/*.lof build/*.lot build/*.out build/*.fls build/*.fdb_latexmk build/*.idx
    
    echo ""
    echo "🎉 BOOST Specification PDF ready!"
    echo "   📖 Open: build/boost-spec.pdf"
    echo "   📁 Logs: build/latex-pass*.log"
    
else
    echo "❌ PDF generation failed - output file not found"
    exit 1
fi