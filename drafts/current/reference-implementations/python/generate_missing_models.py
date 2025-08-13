#!/usr/bin/env python3
"""
Generate missing Python Pydantic models from BOOST JSON schemas.
This script automatically creates complete Python models for all entities missing from models.py
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any

def camel_to_snake(name):
    """Convert CamelCase to snake_case"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_pascal(name):
    """Convert snake_case to PascalCase"""
    return ''.join(word.capitalize() for word in name.split('_'))

def get_python_type(schema_type, schema_def):
    """Convert JSON schema type to Python type annotation"""
    if schema_type == "string":
        if "enum" in schema_def:
            return "str"  # Will handle enum separately
        elif "format" in schema_def:
            if schema_def["format"] in ["date", "date-time"]:
                return "datetime"
            elif schema_def["format"] == "email":
                return "str"
            elif schema_def["format"] == "uri":
                return "str"
        return "str"
    elif schema_type == "integer":
        return "int"
    elif schema_type == "number":
        return "float"
    elif schema_type == "boolean":
        return "bool"
    elif schema_type == "array":
        if "items" in schema_def:
            item_type = get_python_type(schema_def["items"].get("type", "Any"), schema_def["items"])
            return f"List[{item_type}]"
        return "List[Any]"
    elif schema_type == "object":
        return "Dict[str, Any]"
    else:
        return "Any"

def generate_enum_class(entity_name, field_name, enum_values):
    """Generate an enum class for a field"""
    enum_class_name = f"{entity_name}{snake_to_pascal(field_name)}"
    enum_entries = []
    
    for value in enum_values:
        if isinstance(value, str):
            # Convert to valid Python identifier
            key = value.upper().replace('-', '_').replace(' ', '_').replace('.', '_')
            enum_entries.append(f'    {key} = "{value}"')
    
    return f"""class {enum_class_name}(str, Enum):
    \"\"\"Enumeration values for {field_name} in {entity_name}.\"\"\"
{chr(10).join(enum_entries)}

"""

def generate_field_definition(field_name, field_def, entity_name):
    """Generate a Pydantic field definition"""
    field_type = field_def.get("type", "string")
    python_type = get_python_type(field_type, field_def)
    
    # Handle required vs optional
    is_required = True  # Will be determined by caller
    type_annotation = python_type if is_required else f"Optional[{python_type}]"
    
    # Build Field() parameters
    field_params = []
    
    # Add alias if field name has special characters or is different
    if field_name != camel_to_snake(field_name):
        field_params.append(f'alias="{field_name}"')
    
    # Add pattern for string fields
    if "pattern" in field_def:
        pattern = field_def["pattern"].replace("\\", "\\\\")  # Escape backslashes
        field_params.append(f'pattern=r"{pattern}"')
    
    # Add length constraints
    if "minLength" in field_def:
        field_params.append(f'min_length={field_def["minLength"]}')
    if "maxLength" in field_def:
        field_params.append(f'max_length={field_def["maxLength"]}')
    
    # Add numeric constraints
    if "minimum" in field_def:
        field_params.append(f'ge={field_def["minimum"]}')
    if "maximum" in field_def:
        field_params.append(f'le={field_def["maximum"]}')
    
    # Add description
    if "description" in field_def:
        desc = field_def["description"].replace('"', '\\"')
        field_params.append(f'description="{desc}"')
    
    # Handle enums
    enum_class = None
    if "enum" in field_def:
        enum_class = generate_enum_class(entity_name, field_name, field_def["enum"])
        type_annotation = f"{entity_name}{snake_to_pascal(field_name)}" if is_required else f"Optional[{entity_name}{snake_to_pascal(field_name)}]"
    
    # Construct field definition
    if not is_required:
        field_params.insert(0, "None")  # Default value for optional fields
    
    field_def_str = f"Field({', '.join(field_params)})" if field_params else "..."
    
    python_field_name = camel_to_snake(field_name)
    field_line = f"    {python_field_name}: {type_annotation} = {field_def_str}"
    
    return enum_class, field_line

def generate_model_class(entity_name, schema_data):
    """Generate a complete Pydantic model class"""
    schema = schema_data.get("schema", {})
    properties = schema.get("properties", {})
    required_fields = set(schema.get("required", []))
    
    class_name = snake_to_pascal(entity_name)
    
    # Skip JSON-LD fields as they're handled by base class
    skip_fields = {"@context", "@type", "@id"}
    
    enums = []
    fields = []
    
    for field_name, field_def in properties.items():
        if field_name in skip_fields:
            continue
            
        is_required = field_name in required_fields
        enum_class, field_line = generate_field_definition(field_name, field_def, class_name)
        
        if enum_class:
            enums.append(enum_class)
        
        # Adjust field line for optional fields
        if not is_required and "= Field(" in field_line:
            field_line = field_line.replace("= Field(", "= Field(None, ")
        elif not is_required and field_line.endswith("= ..."):
            field_line = field_line.replace("= ...", "= None")
            
        fields.append(field_line)
    
    # Generate the class
    class_code = f"""
{''.join(enums)}class {class_name}(BOOSTBaseModel):
    \"\"\"
    {class_name} entity model for BOOST standard.
    
    {schema.get('description', f'{class_name} entity in BOOST data model')}
    \"\"\"
    
{chr(10).join(fields)}

"""
    
    return class_code

def main():
    """Generate all missing Python models"""
    schema_dir = Path("../../schema")
    models_file = Path("models.py")
    
    # Read existing models to see what's already implemented
    existing_models = set()
    if models_file.exists():
        with open(models_file) as f:
            content = f.read()
            # Extract existing class names
            for match in re.finditer(r'^class (\w+)\(BOOSTBaseModel\):', content, re.MULTILINE):
                existing_models.add(camel_to_snake(match.group(1)))
    
    print(f"Found {len(existing_models)} existing models: {existing_models}")
    
    # Get all entities from directories.json
    directories_file = schema_dir / "directories.json"
    with open(directories_file) as f:
        directories_data = json.load(f)
    
    all_entities = set(directories_data["schema_directories"])
    missing_entities = all_entities - existing_models
    
    print(f"Need to generate {len(missing_entities)} missing models:")
    for entity in sorted(missing_entities):
        print(f"  - {entity}")
    
    # Generate models for missing entities
    generated_code = []
    generated_code.append("# Auto-generated models - DO NOT EDIT MANUALLY")
    generated_code.append("# Generated by generate_missing_models.py")
    generated_code.append("")
    
    for entity in sorted(missing_entities):
        schema_file = schema_dir / entity / "validation_schema.json"
        if not schema_file.exists():
            print(f"Warning: Schema file not found for {entity}")
            continue
            
        with open(schema_file) as f:
            schema_data = json.load(f)
        
        print(f"Generating model for {entity}...")
        model_code = generate_model_class(entity, schema_data)
        generated_code.append(model_code)
    
    # Write to new file
    output_file = "generated_models.py"
    with open(output_file, 'w') as f:
        f.write("""\"\"\"
Auto-generated BOOST Python models from JSON schemas.
Generated by generate_missing_models.py

Add these models to models.py after review.
\"\"\"

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum
from models import BOOSTBaseModel

""")
        f.write('\n'.join(generated_code))
    
    print(f"Generated {len(missing_entities)} models in {output_file}")
    print("Review the generated models and add them to models.py")

if __name__ == "__main__":
    main()