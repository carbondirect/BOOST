#!/usr/bin/env python3
"""
Fix indentation issues in dictionary files for Bikeshed compatibility
"""

import os
import re
import glob

def fix_indentation(content):
    """Fix indentation issues in markdown content"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Fix indentation for list items that are 3 spaces (need to be 4 for Bikeshed)
        if line.startswith('   - ') and not line.startswith('    '):
            # Change 3-space indent to 4-space indent
            fixed_line = '    ' + line[4:]
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_dictionary_file(file_path):
    """Process a single dictionary file"""
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix indentation
    new_content = fix_indentation(content)
    
    # Only write if content changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Fixed indentation in {file_path}")
        return True
    else:
        print(f"  INFO:  No indentation issues in {file_path}")
        return False

def main():
    """Main function to process all dictionary files"""
    print("🔧 Fixing indentation issues in dictionary files...")
    
    # Find all dictionary files
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
    
    print(f"\n✅ Indentation fix complete!")
    print(f"   - Files processed: {len(dictionary_files)}")
    print(f"   - Files fixed: {fixed_count}")

if __name__ == "__main__":
    main()