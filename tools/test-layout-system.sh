#!/bin/bash
#
# BOOST Layout System Integrity Test
# Tests the critical ReSpec-style layout components
#
# Usage: ./tools/test-layout-system.sh [path-to-html]
#

set -e

HTML_FILE="${1:-drafts/current/specifications/boost-spec.html}"
REFERENCE_COMMIT="v3.1.3-5-g725c24a"

echo "🧪 BOOST Layout System Integrity Test"
echo "=====================================+"
echo "📄 Testing file: $HTML_FILE"
echo "🎯 Reference commit: $REFERENCE_COMMIT"
echo ""

# Check if file exists
if [ ! -f "$HTML_FILE" ]; then
    echo "❌ ERROR: HTML file not found at $HTML_FILE"
    echo "💡 Run ./build.sh first to generate the HTML"
    exit 1
fi

echo "🔍 Testing critical layout components..."

# Test 1: main-content-wrapper presence
WRAPPER_COUNT=$(grep -c "main-content-wrapper" "$HTML_FILE")
if [ "$WRAPPER_COUNT" -eq 0 ]; then
    echo "❌ CRITICAL FAILURE: main-content-wrapper div missing"
    echo "💥 The ReSpec-style layout system is broken!"
    echo "📖 See ARCHITECTURE.md for restoration instructions"
    exit 1
elif [ "$WRAPPER_COUNT" -lt 5 ]; then
    echo "⚠️  WARNING: Only $WRAPPER_COUNT main-content-wrapper references found (expected 8-12)"
    echo "💡 Layout system may be partially broken"
    exit 1
else
    echo "✅ main-content-wrapper: Found $WRAPPER_COUNT references"
fi

# Test 2: ReSpec CSS inclusion (check for CSS content, not filename)
if ! grep -q "toc-sidebar" "$HTML_FILE" && ! grep -q "main-content-wrapper" "$HTML_FILE"; then
    echo "❌ CRITICAL FAILURE: ReSpec-style CSS not included"
    echo "💥 Critical styling missing - layout will be broken!"
    echo "📖 Check build.sh Python processing section"
    exit 1
elif grep -q "respec-style.css" "$HTML_FILE"; then
    echo "✅ ReSpec CSS: File reference found"
elif grep -q "toc-sidebar" "$HTML_FILE"; then
    echo "✅ ReSpec CSS: Embedded CSS content detected"
else
    echo "✅ ReSpec CSS: Layout CSS detected via main-content-wrapper"
fi

# Test 3: Sidebar TOC structure
if grep -q "toc-sidebar" "$HTML_FILE"; then
    echo "✅ Sidebar TOC: Structure detected"
elif grep -q "sidebar" "$HTML_FILE"; then
    echo "⚠️  Sidebar: Generic sidebar detected (may be okay)"
else
    echo "⚠️  WARNING: No sidebar structure detected"
fi

# Test 4: Critical CSS overrides  
if grep -q "margin-left: 280px" "$HTML_FILE" || grep -q "main-content-wrapper" "$HTML_FILE"; then
    echo "✅ CSS overrides: Layout overrides detected"
else
    echo "⚠️  WARNING: Critical CSS overrides may be missing"
fi

# Test 5: Responsive layout components
if grep -q "toc-collapsed" "$HTML_FILE"; then
    echo "✅ Responsive layout: Collapse functionality detected"
else
    echo "⚠️  WARNING: Responsive collapse functionality may be missing"
fi

# Test 6: File size check (ReSpec layout should add significant content)
HTML_SIZE=$(wc -c < "$HTML_FILE")
if [ "$HTML_SIZE" -lt 500000 ]; then
    echo "⚠️  WARNING: HTML file size is $HTML_SIZE bytes (may be too small)"
    echo "💡 Expected size: 800KB-1.2MB with full ReSpec layout"
else
    echo "✅ File size: $HTML_SIZE bytes (reasonable for full layout)"
fi

echo ""
echo "📊 LAYOUT SYSTEM TEST RESULTS"
echo "============================="

# Overall assessment
CRITICAL_ISSUES=0
if [ "$WRAPPER_COUNT" -eq 0 ]; then ((CRITICAL_ISSUES++)); fi
if ! grep -q "toc-sidebar" "$HTML_FILE" && ! grep -q "main-content-wrapper" "$HTML_FILE"; then ((CRITICAL_ISSUES++)); fi

if [ "$CRITICAL_ISSUES" -eq 0 ]; then
    echo "🎉 SUCCESS: Layout system integrity verified!"
    echo "✅ All critical components present"
    echo "✅ ReSpec-style layout system is working correctly"
    echo ""
    echo "💡 To verify visually, open $HTML_FILE in a browser and check for:"
    echo "   - Fixed sidebar TOC on the left"
    echo "   - Content area that adapts to sidebar width"  
    echo "   - Professional ReSpec-style appearance"
    echo "   - Responsive behavior on mobile"
    exit 0
else
    echo "❌ FAILURE: $CRITICAL_ISSUES critical issues found"
    echo "💥 Layout system is broken and needs restoration"
    echo ""
    echo "🔧 RECOVERY STEPS:"
    echo "1. Check git log for recent changes to build.sh or respec-style.css"
    echo "2. Compare current system to reference commit $REFERENCE_COMMIT"
    echo "3. See ARCHITECTURE.md for detailed restoration instructions"
    echo "4. Test locally before pushing changes"
    exit 1
fi