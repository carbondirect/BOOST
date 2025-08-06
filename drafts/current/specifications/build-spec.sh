#!/bin/bash

# BOOST Specification Build Script  
# This script generates HTML using direct dictionary references via symlinks

set -e  # Exit on any error

echo "🚀 Building BOOST Specification with Direct Dictionary References..."

# Generate HTML with Bikeshed (using symlinked dictionary includes)
echo "🔧 Generating HTML with Bikeshed..."
bikeshed spec boost-spec.bs

# Report results
if [ -f "boost-spec.html" ]; then
    echo "✅ Build completed successfully!"
    echo "📄 HTML output: boost-spec.html"
    
    # Calculate file sizes
    SPEC_SIZE=$(wc -c < boost-spec.bs)
    HTML_SIZE=$(wc -c < boost-spec.html)
    
    echo "📊 Build statistics:"
    echo "   - Specification size: $(echo $SPEC_SIZE | numfmt --to=iec-i --suffix=B)"
    echo "   - HTML output size: $(echo $HTML_SIZE | numfmt --to=iec-i --suffix=B)"
    
    # Count dictionary files being referenced via symlinks
    DICT_COUNT=$(find schema -name "*_dictionary.md" | wc -l 2>/dev/null || echo "0")
    echo "   - Dictionary files available: $DICT_COUNT"
    echo "   - Using direct dictionary references via symlinks ✨"
    
else
    echo "❌ Build failed!"
    exit 1
fi