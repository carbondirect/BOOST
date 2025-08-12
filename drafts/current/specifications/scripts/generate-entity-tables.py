#!/usr/bin/env python3
"""
Generate LaTeX entity tables from BOOST JSON schema files
Converts JSON schema validation files into LaTeX entity table format
"""

import json
import os
import sys
from pathlib import Path

def extract_entity_info(schema_path):
    """Extract entity information from JSON schema file"""
    try:
        with open(schema_path, 'r') as f:
            data = json.load(f)
        
        # Get the schema object
        schema = data.get('schema', {})
        
        # Extract basic info
        entity_name = schema.get('title', 'Unknown')
        description = schema.get('description', '')
        properties = schema.get('properties', {})
        required = schema.get('required', [])
        
        return {
            'name': entity_name,
            'description': description,
            'properties': properties,
            'required': required
        }
    except Exception as e:
        print(f"Error processing {schema_path}: {e}")
        return None

def format_property_type(prop_def):
    """Format property type for LaTeX table"""
    prop_type = prop_def.get('type', 'unknown')
    
    if 'enum' in prop_def:
        return f"enum({len(prop_def['enum'])} values)"
    elif prop_type == 'array':
        items = prop_def.get('items', {})
        item_type = items.get('type', 'unknown')
        return f"array<{item_type}>"
    elif prop_type == 'object':
        return "object"
    else:
        return prop_type

def generate_entity_table(entity_info, output_path):
    """Generate LaTeX entity table file"""
    
    entity_name = entity_info['name']
    properties = entity_info['properties']
    required = entity_info['required']
    
    latex_content = f"""% {entity_name} Entity Table
% Auto-generated from JSON schema

\\begin{{entitytable}}{{{entity_name}}}
"""
    
    # Add each property as a table row
    for prop_name, prop_def in properties.items():
        prop_type = format_property_type(prop_def)
        description = prop_def.get('description', 'No description provided')
        
        # Clean up description for LaTeX
        description = description.replace('&', '\\&').replace('%', '\\%').replace('_', '\\_')
        if len(description) > 60:
            description = description[:57] + '...'
        
        # Mark required fields
        field_name = f"\\field{{{prop_name}}}"
        if prop_name in required:
            field_name = f"\\textbf{{{field_name}}}"
        
        latex_content += f"{field_name} & {prop_type} & {description} \\\\\n"
    
    latex_content += "\\end{entitytable}\n"
    
    # Write to file
    with open(output_path, 'w') as f:
        f.write(latex_content)
    
    print(f"Generated entity table: {output_path}")

def main():
    # Schema directory
    schema_dir = Path("schema")
    if not schema_dir.exists():
        print("Error: schema directory not found")
        return
    
    # Output directory for entity tables
    output_dir = Path("tex/entities")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Core entities to process first
    core_entities = [
        'traceable_unit',
        'organization', 
        'material',
        'geographic_data',
        'material_processing'
    ]
    
    # Process core entities
    for entity_dir in core_entities:
        schema_path = schema_dir / entity_dir / "validation_schema.json"
        if schema_path.exists():
            entity_info = extract_entity_info(schema_path)
            if entity_info:
                output_file = output_dir / f"{entity_dir.replace('_', '-')}-table.tex"
                generate_entity_table(entity_info, output_file)
        else:
            print(f"Schema not found: {schema_path}")
    
    # Process all other entities
    for entity_dir in schema_dir.iterdir():
        if entity_dir.is_dir() and entity_dir.name not in core_entities:
            schema_path = entity_dir / "validation_schema.json"
            if schema_path.exists():
                entity_info = extract_entity_info(schema_path)
                if entity_info:
                    output_file = output_dir / f"{entity_dir.name.replace('_', '-')}-table.tex"
                    generate_entity_table(entity_info, output_file)
            else:
                print(f"Schema not found: {schema_path}")
    
    print(f"\nEntity table generation complete!")
    print(f"Generated files in: {output_dir}")

if __name__ == "__main__":
    main()