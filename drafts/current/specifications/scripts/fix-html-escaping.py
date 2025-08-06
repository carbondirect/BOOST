#!/usr/bin/env python3
"""
Fix HTML escaping in existing HTML tables in dictionary files
"""

import os
import re
import glob

def fix_html_escaping(content):
    """Fix HTML escaping in table cells"""
    
    # Pattern to find table cell content
    def escape_cell_content(match):
        cell_content = match.group(1)
        # Escape HTML entities in cell content
        escaped_content = (cell_content.replace('&', '&amp;')
                         .replace('<', '&lt;')
                         .replace('>', '&gt;'))
        return f'<td>{escaped_content}'
    
    # Apply escaping to table cells
    result = re.sub(r'<td>([^<]*)', escape_cell_content, content)
    return result

def process_dictionary_file(file_path):
    """Process a single dictionary file"""
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix HTML escaping
    new_content = fix_html_escaping(content)
    
    # Only write if content changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Fixed HTML escaping in {file_path}")
        return True
    else:
        print(f"  ℹ️  No changes needed in {file_path}")
        return False

def main():
    """Main function to process all dictionary files"""
    print("🔧 Fixing HTML escaping in dictionary files...")
    
    # Find all dictionary files via symlinks
    dictionary_files = []
    schema_dirs = glob.glob('schema/*/')
    
    for schema_dir in schema_dirs:
        dict_files = glob.glob(f"{schema_dir}*_dictionary.md")
        dictionary_files.extend(dict_files)
    
    if not dictionary_files:
        print("❌ No dictionary files found!")
        return
    
    print(f"📁 Found {len(dictionary_files)} dictionary files")
    
    fixed_count = 0
    for file_path in sorted(dictionary_files):
        if process_dictionary_file(file_path):
            fixed_count += 1
    
    print(f"\n✅ HTML escaping fix complete!")
    print(f"   - Files processed: {len(dictionary_files)}")
    print(f"   - Files fixed: {fixed_count}")

if __name__ == "__main__":
    main()