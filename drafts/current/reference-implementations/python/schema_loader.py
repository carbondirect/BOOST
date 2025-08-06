"""
BOOST Python Reference Implementation - Dynamic Schema Loader

This module provides dynamic loading and management of BOOST schemas,
making the implementation robust to schema changes by generating
models and validation rules directly from JSON schemas.
"""

import json
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Type, Union, Tuple
from pathlib import Path
from enum import Enum

try:
    # Try importing Pydantic v2
    from pydantic.v1 import BaseModel, Field, create_model, validator
    from pydantic.v1.fields import FieldInfo
    PYDANTIC_V2 = False
except ImportError:
    try:
        # Fallback to Pydantic v1
        from pydantic import BaseModel, Field, create_model, validator
        from pydantic.fields import FieldInfo
        PYDANTIC_V2 = False
    except ImportError:
        raise ImportError("Pydantic v1 or v2 is required")


class SchemaLoader:
    """Dynamic schema loader that generates models and validation from JSON schemas."""
    
    def __init__(self, schema_base_path: Optional[str] = None):
        """
        Initialize schema loader.
        
        Args:
            schema_base_path: Path to BOOST schema directory
        """
        if schema_base_path is None:
            current_dir = Path(__file__).parent
            self.schema_base_path = current_dir.parent.parent / "schema"
        else:
            self.schema_base_path = Path(schema_base_path)
        
        self.schemas: Dict[str, Dict] = {}
        self.cross_entity_rules: Dict = {}
        self.business_logic_rules: Dict = {}
        self.entity_metadata: Dict[str, Dict] = {}
        self.dynamic_models: Dict[str, Type[BaseModel]] = {}
        self.enums: Dict[str, Type[Enum]] = {}
        
        self._load_schemas()
        self._discover_relationships()
        self._generate_dynamic_models()
    
    def _load_schemas(self):
        """Load all schemas and extract metadata."""
        try:
            # Load individual entity schemas
            for entity_dir in self.schema_base_path.iterdir():
                if entity_dir.is_dir() and (entity_dir / "validation_schema.json").exists():
                    schema_file = entity_dir / "validation_schema.json"
                    with open(schema_file, 'r') as f:
                        schema_data = json.load(f)
                        
                        # Extract schema and metadata
                        if 'schema' in schema_data:
                            self.schemas[entity_dir.name] = schema_data['schema']
                            if 'boost_metadata' in schema_data:
                                self.entity_metadata[entity_dir.name] = schema_data['boost_metadata']
                        else:
                            self.schemas[entity_dir.name] = schema_data
            
            # Load cross-entity validation rules
            cross_entity_file = self.schema_base_path / "cross_entity_validation.json"
            if cross_entity_file.exists():
                with open(cross_entity_file, 'r') as f:
                    self.cross_entity_rules = json.load(f)
            
            # Load business logic validation rules
            business_logic_file = self.schema_base_path / "business_logic_validation.json"
            if business_logic_file.exists():
                with open(business_logic_file, 'r') as f:
                    self.business_logic_rules = json.load(f)
                    
        except Exception as e:
            print(f"Warning: Could not load all schemas: {e}")
    
    def _discover_relationships(self):
        """Discover entity relationships from schemas and metadata."""
        self.relationships = {}
        self.primary_keys = {}
        
        # Extract primary keys from metadata
        for entity_name, metadata in self.entity_metadata.items():
            if 'entity' in metadata and 'primaryKey' in metadata['entity']:
                self.primary_keys[entity_name] = metadata['entity']['primaryKey']
            else:
                # Fallback: infer from schema properties
                schema = self.schemas.get(entity_name, {})
                properties = schema.get('properties', {})
                # Look for fields ending with 'Id' that are required
                required_fields = schema.get('required', [])
                for field_name, field_schema in properties.items():
                    if field_name.endswith('Id') and field_name in required_fields:
                        # Check if it's likely a primary key (not foreign key)
                        if not self._is_foreign_key(field_name, entity_name):
                            self.primary_keys[entity_name] = field_name
                            break
        
        # Extract relationships from metadata
        for entity_name, metadata in self.entity_metadata.items():
            if 'relationships' in metadata:
                self.relationships[entity_name] = metadata['relationships']
    
    def _is_foreign_key(self, field_name: str, entity_name: str) -> bool:
        """Check if a field is likely a foreign key."""
        # Simple heuristic: if field name doesn't start with entity name, likely FK
        entity_base = entity_name.replace('_', '').lower()
        field_base = field_name.replace('_', '').lower().replace('id', '')
        return not field_base.startswith(entity_base)
    
    def _generate_dynamic_models(self):
        """Generate Pydantic models dynamically from schemas."""
        # First pass: create enums
        for entity_name, schema in self.schemas.items():
            self._create_enums_for_entity(entity_name, schema)
        
        # Second pass: create models
        for entity_name, schema in self.schemas.items():
            self._create_model_for_entity(entity_name, schema)
    
    def _create_enums_for_entity(self, entity_name: str, schema: Dict[str, Any]):
        """Create dynamic enums for entity schema."""
        properties = schema.get('properties', {})
        
        for field_name, field_schema in properties.items():
            if 'enum' in field_schema:
                enum_name = f"{entity_name.title().replace('_', '')}{field_name.title().replace('_', '')}Enum"
                enum_values = {val.upper().replace('-', '_').replace(' ', '_'): val 
                              for val in field_schema['enum']}
                
                # Create dynamic enum
                dynamic_enum = Enum(enum_name, enum_values)
                self.enums[f"{entity_name}.{field_name}"] = dynamic_enum
    
    def _create_model_for_entity(self, entity_name: str, schema: Dict[str, Any]):
        """Create a dynamic Pydantic model for an entity."""
        properties = schema.get('properties', {})
        required_fields = schema.get('required', [])
        
        # Add serialization methods that work in both v1 and v2
        def model_to_dict(self, by_alias: bool = True):
            if hasattr(self, 'model_dump'):  # v2
                return self.model_dump(by_alias=by_alias)
            return self.dict(by_alias=by_alias)  # v1
        
        # Base model fields
        model_fields = {}
        
        # Add JSON-LD context fields
        if '@context' in properties:
            model_fields['context'] = (Optional[Dict[str, Any]], Field(None, alias="@context"))
        
        if '@type' in properties:
            type_schema = properties.get('@type', {})
            if 'const' in type_schema:
                # Fixed type value
                model_fields['type'] = (str, Field(type_schema['const'], alias="@type"))
            else:
                model_fields['type'] = (str, Field(..., alias="@type"))
        
        if '@id' in properties:
            model_fields['id'] = (str, Field(..., alias="@id"))
        
        # Process other properties
        for field_name, field_schema in properties.items():
            if field_name.startswith('@'):
                continue  # Already handled above
                
            python_field_name = self._to_python_field_name(field_name)
            field_type, field_info = self._create_field_from_schema(
                entity_name, field_name, field_schema, field_name in required_fields
            )
            model_fields[python_field_name] = (field_type, field_info)
        
        # Add lastUpdated if not present
        if 'lastUpdated' not in properties and 'last_updated' not in model_fields:
            model_fields['last_updated'] = (Optional[datetime], Field(None, alias="lastUpdated"))
        
        # Create model class name
        model_name = entity_name.title().replace('_', '')
        
        # Create the dynamic model
        model_config = type('Config', (), {
            'allow_population_by_name': True,
            'json_encoders': {datetime: lambda v: v.isoformat()},
            'validate_assignment': True,
            'arbitrary_types_allowed': True
        })
        
        # Add dict method that works in both v1 and v2
        def to_dict(self, by_alias: bool = True):
            if hasattr(self, 'model_dump'):  # v2
                return self.model_dump(by_alias=by_alias)
            return self.dict(by_alias=by_alias)  # v1
        
        # Create the base model
        dynamic_model = create_model(
            model_name,
            __config__=model_config,
            **model_fields
        )
        
        # Add the to_dict method to the model
        dynamic_model.to_dict = to_dict
        
        # Add custom validators if needed
        self._add_custom_validators(dynamic_model, entity_name, schema)
        
        self.dynamic_models[entity_name] = dynamic_model
    
    def _to_python_field_name(self, field_name: str) -> str:
        """Convert schema field name to Python field name."""
        # Convert camelCase to snake_case
        result = re.sub('([A-Z]+)([A-Z][a-z])', r'\1_\2', field_name)
        result = re.sub('([a-z\\d])([A-Z])', r'\1_\2', result)
        return result.lower()
    
    def _create_field_from_schema(self, entity_name: str, field_name: str, 
                                field_schema: Dict[str, Any], required: bool) -> Tuple[Type, FieldInfo]:
        """Create a Pydantic field from JSON schema definition."""
        field_type = self._get_python_type_from_schema(entity_name, field_name, field_schema)
        
        # Build field constraints
        field_kwargs = {
            'alias': field_name,
            'description': field_schema.get('description', '')
        }
        
        # Add validation constraints
        if 'minLength' in field_schema:
            field_kwargs['min_length'] = field_schema['minLength']
        if 'maxLength' in field_schema:
            field_kwargs['max_length'] = field_schema['maxLength']
        if 'minimum' in field_schema:
            field_kwargs['ge'] = field_schema['minimum']
        if 'maximum' in field_schema:
            field_kwargs['le'] = field_schema['maximum']
        if 'pattern' in field_schema:
            field_kwargs['pattern'] = field_schema['pattern']
        
        # Handle required vs optional
        if required:
            field_info = Field(..., **field_kwargs)
        else:
            field_info = Field(None, **field_kwargs)
            # Make type optional if not required
            if hasattr(field_type, '__origin__') and field_type.__origin__ is not Union:
                field_type = Optional[field_type]
        
        return field_type, field_info
    
    def _get_python_type_from_schema(self, entity_name: str, field_name: str, 
                                   field_schema: Dict[str, Any]) -> Type:
        """Convert JSON schema type to Python type."""
        schema_type = field_schema.get('type', 'string')
        
        # Handle case where type is a list (e.g., ['string', 'null'])
        if isinstance(schema_type, list):
            # Take the first non-null type
            for t in schema_type:
                if t != 'null':
                    schema_type = t
                    break
            else:
                schema_type = 'string'  # fallback
        
        # Handle enums first
        if 'enum' in field_schema:
            enum_key = f"{entity_name}.{field_name}"
            if enum_key in self.enums:
                return self.enums[enum_key]
            else:
                # Fallback to string for unknown enums
                return str
        
        # Handle arrays
        if schema_type == 'array':
            items_schema = field_schema.get('items', {})
            item_type = self._get_python_type_from_schema(entity_name, f"{field_name}_item", items_schema)
            return List[item_type]
        
        # Handle objects
        if schema_type == 'object':
            return Dict[str, Any]
        
        # Handle basic types
        type_mapping = {
            'string': str,
            'integer': int,
            'number': float,
            'boolean': bool
        }
        
        # Special handling for date/datetime fields
        if field_schema.get('format') == 'date':
            return str  # Keep as string for date fields
        elif field_schema.get('format') == 'date-time':
            return datetime
        elif field_schema.get('@type') == 'http://www.w3.org/2001/XMLSchema#date':
            return str
        elif field_schema.get('@type') == 'http://www.w3.org/2001/XMLSchema#dateTime':
            return datetime
        
        return type_mapping.get(schema_type, str)
    
    def _add_custom_validators(self, model_class: Type[BaseModel], entity_name: str, schema: Dict[str, Any]):
        """Add custom validators to the model based on business logic."""
        # Add type validator to ensure @type is set correctly
        expected_type = schema.get('properties', {}).get('@type', {}).get('const')
        if expected_type:
            def validate_type(cls, v):
                return expected_type
            
            # Add validator to model
            setattr(model_class, 'validate_type', validator('type', pre=True, always=True)(validate_type))
        
        # Add business logic validators based on entity type
        if entity_name == 'material_processing':
            def validate_volume_conservation(cls, values):
                input_vol = values.get('input_volume')
                output_vol = values.get('output_volume') 
                vol_loss = values.get('volume_loss', 0)
                
                if all(v is not None for v in [input_vol, output_vol, vol_loss]):
                    if input_vol < (output_vol + vol_loss):
                        raise ValueError("Volume conservation violation: input must be >= output + loss")
                return values
            
            # Add root validator
            setattr(model_class, 'validate_volume_conservation', 
                   validator('*', pre=False, allow_reuse=True)(lambda cls, v, values: validate_volume_conservation(cls, values)))
    
    def get_model(self, entity_name: str) -> Optional[Type[BaseModel]]:
        """Get dynamic model for entity type."""
        return self.dynamic_models.get(entity_name)
    
    def get_enum(self, entity_name: str, field_name: str) -> Optional[Type[Enum]]:
        """Get dynamic enum for entity field."""
        return self.enums.get(f"{entity_name}.{field_name}")
    
    def get_primary_key(self, entity_name: str) -> Optional[str]:
        """Get primary key field name for entity."""
        return self.primary_keys.get(entity_name)
    
    def get_relationships(self, entity_name: str) -> List[Dict[str, Any]]:
        """Get relationship definitions for entity."""
        return self.relationships.get(entity_name, [])
    
    def get_schema(self, entity_name: str) -> Optional[Dict[str, Any]]:
        """Get JSON schema for entity."""
        return self.schemas.get(entity_name)
    
    def get_all_entity_types(self) -> List[str]:
        """Get list of all available entity types."""
        return list(self.schemas.keys())
    
    def get_field_enum_values(self, entity_name: str, field_name: str) -> List[str]:
        """Get enum values for a field from schema."""
        schema = self.schemas.get(entity_name, {})
        field_schema = schema.get('properties', {}).get(field_name, {})
        return field_schema.get('enum', [])
    
    def is_field_required(self, entity_name: str, field_name: str) -> bool:
        """Check if field is required for entity."""
        schema = self.schemas.get(entity_name, {})
        required_fields = schema.get('required', [])
        return field_name in required_fields
    
    def get_field_constraints(self, entity_name: str, field_name: str) -> Dict[str, Any]:
        """Get validation constraints for a field."""
        schema = self.schemas.get(entity_name, {})
        field_schema = schema.get('properties', {}).get(field_name, {})
        
        constraints = {}
        if 'minLength' in field_schema:
            constraints['min_length'] = field_schema['minLength']
        if 'maxLength' in field_schema:
            constraints['max_length'] = field_schema['maxLength']
        if 'minimum' in field_schema:
            constraints['minimum'] = field_schema['minimum']
        if 'maximum' in field_schema:
            constraints['maximum'] = field_schema['maximum']
        if 'pattern' in field_schema:
            constraints['pattern'] = field_schema['pattern']
        if 'enum' in field_schema:
            constraints['enum'] = field_schema['enum']
            
        return constraints
    
    def validate_schema_compatibility(self, entity_name: str, data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate data against current schema, reporting compatibility issues."""
        schema = self.get_schema(entity_name)
        if not schema:
            return False, [f"Unknown entity type: {entity_name}"]
        
        errors = []
        warnings = []
        
        # Check for unknown fields (potential schema additions)
        schema_properties = schema.get('properties', {})
        for field_name in data.keys():
            if field_name not in schema_properties:
                warnings.append(f"Unknown field '{field_name}' - may be from newer schema version")
        
        # Check for missing required fields (potential schema changes)
        required_fields = schema.get('required', [])
        for field_name in required_fields:
            if field_name not in data:
                errors.append(f"Missing required field '{field_name}'")
        
        # Check enum values
        for field_name, field_value in data.items():
            if field_name in schema_properties:
                field_schema = schema_properties[field_name]
                if 'enum' in field_schema and field_value not in field_schema['enum']:
                    errors.append(f"Invalid enum value '{field_value}' for field '{field_name}'. Valid values: {field_schema['enum']}")
        
        return len(errors) == 0, errors + warnings
    
    def refresh_schemas(self):
        """Reload schemas from disk and regenerate models."""
        self.schemas.clear()
        self.cross_entity_rules.clear()
        self.business_logic_rules.clear()
        self.entity_metadata.clear()
        self.dynamic_models.clear()
        self.enums.clear()
        
        self._load_schemas()
        self._discover_relationships()
        self._generate_dynamic_models()


def create_schema_loader(schema_path: Optional[str] = None) -> SchemaLoader:
    """Factory function to create a schema loader."""
    return SchemaLoader(schema_path)