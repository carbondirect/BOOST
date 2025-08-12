#!/usr/bin/env python3
"""
Clean HTML file for PDF conversion by removing interactive elements
"""
import re
import sys

def clean_html_for_pdf(input_file, output_file):
    """Clean HTML file for PDF conversion"""
    try:
        with open(input_file, 'r') as f:
            html = f.read()
        
        # Remove interactive elements for PDF
        html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub(r'onclick="[^"]*"', '', html)
        html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
        html = re.sub(r'class="[^"]*"', '', html)
        
        with open(output_file, 'w') as f:
            f.write(html)
            
        print(f"✅ Cleaned HTML saved to {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error cleaning HTML: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: clean-html-for-pdf.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    success = clean_html_for_pdf(input_file, output_file)
    sys.exit(0 if success else 1)