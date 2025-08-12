#!/usr/bin/env python3
"""
Convert markdown tables to HTML tables in dictionary files for Bikeshed compatibility
"""

import os
import re
import glob

def convert_markdown_table_to_html(content):
    """Convert markdown tables to HTML tables with proper Bikeshed styling"""
    
    # Pattern to match markdown tables
    table_pattern = r'(\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n?)+)'
    
    def replace_table(match):
        table_text = match.group(1).strip()
        lines = [line.strip() for line in table_text.split('\n') if line.strip()]
        
        if len(lines) < 3:  # Need header, separator, and at least one data row
            return table_text  # Return original if not a proper table
        
        # Parse header row
        header_row = lines[0]
        header_cells = [cell.strip().strip('|').strip() for cell in header_row.split('|')[1:-1]]
        
        # Skip separator row (lines[1])
        
        # Parse data rows
        data_rows = []
        for line in lines[2:]:
            if '|' in line:
                cells = [cell.strip().strip('|').strip() for cell in line.split('|')[1:-1]]
                data_rows.append(cells)
        
        # Generate HTML table
        html = ['<table class="data">', '<thead>', '<tr>']
        
        # Add header cells
        for cell in header_cells:
            html.append(f'<th>{cell}')
        
        html.extend(['</tr>', '</thead>', '<tbody>'])
        
        # Add data rows
        for row in data_rows:
            html.append('<tr>')
            for cell in row:
                # Escape HTML entities in cell content
                escaped_cell = (cell.replace('&', '&amp;')
                                  .replace('<', '&lt;')
                                  .replace('>', '&gt;'))
                html.append(f'<td>{escaped_cell}')
            html.append('</tr>')
        
        html.extend(['</tbody>', '</table>'])
        
        return '\n'.join(html)
    
    # Replace all markdown tables with HTML tables
    result = re.sub(table_pattern, replace_table, content, flags=re.MULTILINE)
    return result

def process_dictionary_file(file_path):
    """Process a single dictionary file"""
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert tables
    new_content = convert_markdown_table_to_html(content)
    
    # Only write if content changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Converted tables in {file_path}")
        return True
    else:
        print(f"  ℹ️  No tables found in {file_path}")
        return False

def main():
    """Main function to process all dictionary files"""
    print("🔧 Converting markdown tables to HTML in dictionary files...")
    
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
    
    converted_count = 0
    for file_path in sorted(dictionary_files):
        if process_dictionary_file(file_path):
            converted_count += 1
    
    print(f"\n✅ Conversion complete!")
    print(f"   - Files processed: {len(dictionary_files)}")
    print(f"   - Files converted: {converted_count}")
    print(f"   - Tables now compatible with Bikeshed rendering")

if __name__ == "__main__":
    main()