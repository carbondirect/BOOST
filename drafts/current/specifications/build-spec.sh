#!/bin/bash

# BOOST Specification Build Script  
# This script generates HTML using direct dictionary references via symlinks

set -e  # Exit on any error

echo "🚀 Building BOOST Specification with Direct Dictionary References..."

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

# 1. Insert CSS after existing styles
pattern = r'(</style>)(\s*<body[^>]*>)'
replacement = r'\1\n<style>\n' + respec_css + r'\n</style>\2'
modified_html = re.sub(pattern, replacement, html_content, flags=re.MULTILINE | re.DOTALL)

# 2. Wrap all body content (except ToC) in a main content wrapper
# Find everything after the body tag
body_pattern = r'(<body[^>]*>)(.*?)(<nav[^>]*id=[\"\\']toc[\"\\'][^>]*>.*?</nav>)(.*?)(</body>)'
def wrap_content(match):
    body_open = match.group(1)
    before_toc = match.group(2)
    toc_nav = match.group(3)
    after_toc = match.group(4)
    body_close = match.group(5)
    
    # Add mobile toggle button and wrap non-ToC content
    mobile_toggle = '<button class=\"toc-toggle\" onclick=\"toggleToc()\" aria-label=\"Toggle navigation\"></button>'
    wrapped_content = f'<div class=\"main-content-wrapper\">{before_toc}{after_toc}</div>'
    
    return f'{body_open}{mobile_toggle}{toc_nav}{wrapped_content}{body_close}'

modified_html = re.sub(body_pattern, wrap_content, modified_html, flags=re.MULTILINE | re.DOTALL)

# 3. Add JavaScript for mobile toggle functionality
js_code = '''
<script>
function toggleToc() {
    const toc = document.getElementById('toc');
    const toggle = document.querySelector('.toc-toggle');
    
    toc.classList.toggle('show');
    toggle.classList.toggle('active');
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
</script>
'''

# Insert JavaScript before closing body tag
modified_html = re.sub(r'</body>', js_code + '\n</body>', modified_html)

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
    
else
    echo "❌ Build failed!"
    exit 1
fi