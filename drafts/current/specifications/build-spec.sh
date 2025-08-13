#!/bin/bash

# BOOST Specification Build Script  
# This script generates HTML using direct dictionary references via symlinks

set -e  # Exit on any error

echo "🚀 Building BOOST Specification with Direct Dictionary References..."

# Extract version from environment or git tags (authoritative source)
echo "🔧 Extracting version information..."

# Check if RELEASE_VERSION is set (from CI/CD workflows)
if [ -n "$RELEASE_VERSION" ]; then
    VERSION="$RELEASE_VERSION"
    echo "📋 Using release version from environment: $VERSION"
elif git rev-parse --git-dir >/dev/null 2>&1; then
    # Get the latest version tag, fallback to commit hash if no tags
    VERSION=$(git describe --tags --abbrev=0 2>/dev/null)
    if [ -z "$VERSION" ]; then
        # No tags found, use commit hash
        SHORT_HASH=$(git rev-parse --short HEAD)
        VERSION="v0.0.0-${SHORT_HASH}"
        echo "⚠️  No git tags found, using commit hash: $VERSION"
    else
        echo "📋 Using git tag: $VERSION"
    fi
else
    # Not a git repository, use fallback
    VERSION="v0.0.0-no-version-detected"
    echo "⚠️  Not a git repository, using fallback: $VERSION"
fi

# Replace version placeholders in all source files
echo "🔧 Replacing version placeholders with $VERSION..."

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

# Generate HTML with Bikeshed (using symlinked dictionary includes)
echo "🔧 Generating HTML with Bikeshed..."
bikeshed spec boost-spec.bs

# Add ReSpec-style CSS to the generated HTML
echo "🎨 Adding ReSpec-style CSS to HTML output..."
if [ -f "respec-style.css" ] && [ -f "boost-spec.html" ]; then
    # Create a backup of the original HTML
    cp boost-spec.html boost-spec-original.html
    
    # Insert the ReSpec-style CSS and modify layout structure
    python3 -c "
import re
import sys

# Read the HTML file
with open('boost-spec.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Read the ReSpec-style CSS
with open('respec-style.css', 'r', encoding='utf-8') as f:
    respec_css = f.read()

# DIRECTLY REMOVE the problematic Bikeshed body styles that cause centering
html_content = re.sub(r'max-width: 50em;[\s]*\/\*[^*]*\*\/', '', html_content)
html_content = re.sub(r'margin: 0 auto;[\s]*\/\*[^*]*\*\/', '', html_content)
html_content = re.sub(r'max-width: 50em;', '', html_content)
html_content = re.sub(r'margin: 0 auto;', 'margin: 0;', html_content)

# 1. Insert CSS after existing styles AND add overrides at the end
pattern = r'(</style>)(\s*<body[^>]*>)'
replacement = r'\1\n<style>\n' + respec_css + r'\n</style>\2'
modified_html = re.sub(pattern, replacement, html_content, flags=re.MULTILINE | re.DOTALL)

# Add critical overrides right before </head> to ensure they come last
critical_overrides = '''
<style>
/* CRITICAL OVERRIDES - Must be last to override Bikeshed */
body {
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw !important;
    position: relative !important;
}
body.h-entry {
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw !important;
    position: relative !important;
}
/* Debug borders to visualize layout */
#toc {
    border: 2px solid red !important;
    background: rgba(255,0,0,0.1) !important;
}
.main-content-wrapper {
    border: 2px solid blue !important;
    background: rgba(0,0,255,0.1) !important;
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
modified_html = re.sub(r'</body>', critical_overrides + '\n</body>', modified_html)

# 2. Fix document structure for proper ReSpec layout:
# Structure should be: body -> [toggle button] -> [TOC fixed sidebar] -> [main wrapper with header + content]
# Find the body opening tag
body_start = modified_html.find('<body')
if body_start == -1:
    print('ERROR: Could not find <body> tag')
    sys.exit(1)
    
body_end = modified_html.find('>', body_start) + 1

# Find the ToC navigation
toc_start = modified_html.find('<nav', body_end)
if toc_start == -1:
    print('ERROR: Could not find ToC navigation')
    sys.exit(1)
    
# Find the end of ToC navigation
toc_nav_start = toc_start
nav_count = 1
pos = modified_html.find('>', toc_start) + 1
while nav_count > 0 and pos < len(modified_html):
    if modified_html[pos:pos+5] == '<nav ':
        nav_count += 1
    elif modified_html[pos:pos+6] == '</nav>':
        nav_count -= 1
        if nav_count == 0:
            pos += 6
            break
    pos += 1
toc_end = pos

# Extract parts
body_tag = modified_html[body_start:body_end]
before_toc = modified_html[body_end:toc_start]  # This includes the header content
toc_nav = modified_html[toc_start:toc_end]
after_toc = modified_html[toc_end:]  # This is the main specification content

# Remove any existing closing tags from after_toc
after_toc = re.sub(r'</body>\s*</html>\s*$', '', after_toc.strip())

# Rebuild with proper ReSpec structure:
# 1. Body (toggle button removed due to Bikeshed conflicts)
# 2. Fixed TOC sidebar 
# 3. Main content wrapper containing BOTH header and specification content
wrapped_main_content = f'<div class=\"main-content-wrapper\">{before_toc}{after_toc}</div>'

modified_html = (modified_html[:body_start] + 
                body_tag + toc_nav + wrapped_main_content)

# 3. Remove Bikeshed's existing toggle functionality and add our own
# First remove any existing toggle elements created by Bikeshed
modified_html = re.sub(r'<[^>]*id=[\"\\']toc-toggle[\"\\'][^>]*>[^<]*</[^>]+>', '', modified_html)
modified_html = re.sub(r'createSidebarToggle\\(\\);', '', modified_html)
# Also disable the toggleSidebar function calls that cause errors
modified_html = re.sub(r'toggleSidebar\\([^)]*\\);', '', modified_html)
# Disable the Bikeshed sidebar media query listener
modified_html = re.sub(r'sidebarMedia\\.addListener\\(autoToggle\\);', '', modified_html)

# 4. Add minimal JavaScript to prevent Bikeshed conflicts
js_code = '''
<script>
// Override Bikeshed's toggle functionality completely
createSidebarToggle = function() {}; // Disable Bikeshed toggle creation
toggleSidebar = function() {}; // Disable Bikeshed toggle function
// Disable any problematic Bikeshed media queries and auto-toggles
if (typeof sidebarMedia !== 'undefined') {
    sidebarMedia.removeListener = function() {};
    sidebarMedia.addListener = function() {};
}
// Prevent Bikeshed from adding toc-sidebar/toc-inline classes
document.addEventListener('DOMContentLoaded', function() {
    document.body.classList.remove('toc-sidebar', 'toc-inline');
    
    // Add event listener as backup in case onclick fails
    const toggle = document.querySelector('.toc-toggle');
    if (toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            toggleToc();
        });
    }
});
// Override any window resize handlers that might interfere
window.addEventListener('resize', function() {
    document.body.classList.remove('toc-sidebar', 'toc-inline');
});

function toggleToc() {
    const toc = document.getElementById('toc');
    const toggle = document.querySelector('.toc-toggle');
    const mainContent = document.querySelector('.main-content-wrapper');
    
    if (!toc || !toggle || !mainContent) {
        console.error('TOC toggle: Required elements not found');
        return;
    }
    
    // Toggle collapsed state for desktop
    if (window.innerWidth > 768) {
        toc.classList.toggle('collapsed');
        toggle.classList.toggle('collapsed');
        mainContent.classList.toggle('toc-collapsed');
    } else {
        // Mobile behavior - show/hide sidebar
        toc.classList.toggle('show');
        toggle.classList.toggle('active');
    }
}

// Close ToC when clicking outside on mobile
document.addEventListener('click', function(event) {
    if (window.innerWidth <= 768) {
        const toc = document.getElementById('toc');
        const toggle = document.querySelector('.toc-toggle');
        
        if (!toc.contains(event.target) && !toggle.contains(event.target)) {
            toc.classList.remove('show');
            toggle.classList.remove('active');
        }
    }
});

// Handle window resize to ensure proper state
window.addEventListener('resize', function() {
    const toc = document.getElementById('toc');
    const toggle = document.querySelector('.toc-toggle');
    
    if (window.innerWidth > 768) {
        // Reset mobile classes when switching to desktop
        toc.classList.remove('show');
        toggle.classList.remove('active');
    } else {
        // Reset desktop classes when switching to mobile
        toc.classList.remove('collapsed');
        toggle.classList.remove('collapsed');
        document.querySelector('.main-content-wrapper').classList.remove('toc-collapsed');
    }
});
</script>
'''

# Insert JavaScript before existing Bikeshed scripts to override them
script_pattern = r'(<script[^>]*>)'
if re.search(script_pattern, modified_html):
    modified_html = re.sub(script_pattern, js_code + r'\1', modified_html, count=1)
elif '</body>' in modified_html:
    modified_html = re.sub(r'</body>', js_code + '\n</body>', modified_html)
else:
    # Add JavaScript and closing tags if they're missing
    modified_html += js_code + '\n</body>\n</html>'

# Write the modified HTML back
with open('boost-spec.html', 'w', encoding='utf-8') as f:
    f.write(modified_html)

print('ReSpec-style CSS and layout modifications successfully added to boost-spec.html')
"
    echo "✅ ReSpec-style CSS added successfully!"
else
    echo "⚠️  ReSpec-style CSS file not found or HTML not generated, skipping CSS injection."
fi

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
    
    # Run consistency validation if script exists
    if [ -f "scripts/validate-consistency.py" ]; then
        echo ""
        echo "🔍 Running documentation consistency check..."
        if python3 scripts/validate-consistency.py >/dev/null 2>&1; then
            echo "   ✅ HTML/PDF consistency check passed"
        else
            echo "   ⚠️  Consistency check found issues (see build/consistency-report.json)"
        fi
    fi
    
else
    echo "❌ Build failed!"
    exit 1
fi

# Cleanup: restore version placeholders in source files
echo "🧹 Restoring version placeholders in source files..."

# Restore main Bikeshed file (using pipe delimiter to avoid issues with special chars)
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

echo "✨ Git tag-based version management completed - source files ready for git commit"