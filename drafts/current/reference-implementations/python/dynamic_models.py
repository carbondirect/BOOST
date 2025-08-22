"""
BOOST Dynamic Models Facade
Provides clean access to dynamically generated Pydantic models and enums from JSON schemas.

This module replaces static models with dynamic model generation, ensuring models
always stay synchronized with JSON schemas and maintaining the "Dynamic Schema-Driven
Architecture" promised in the README.
"""

from typing import Dict, Any, Type, Optional, List
from pydantic import BaseModel
from enum import Enum
from pathlib import Path

try:
    from .schema_loader import SchemaLoader
except ImportError:
    from schema_loader import SchemaLoader


class DynamicModels:
    """Facade for accessing dynamically generated BOOST models and enums."""
    
    def __init__(self, schema_path: Optional[str] = None):
        """
        Initialize dynamic models facade.
        
        Args:
            schema_path: Path to BOOST schema directory
        """
        self.schema_loader = SchemaLoader(schema_path)
        self._models_cache = {}
        self._enums_cache = {}
    
    def get_model(self, entity_name: str) -> Type[BaseModel]:
        """
        Get a dynamically generated Pydantic model for an entity.
        
        Args:
            entity_name: Name of the entity (e.g., 'organization', 'traceable_unit')
            
        Returns:
            Pydantic model class for the entity
            
        Raises:
            ValueError: If entity not found in schemas
        """
        if entity_name in self._models_cache:
            return self._models_cache[entity_name]
        
        if entity_name in self.schema_loader.dynamic_models:
            model = self.schema_loader.dynamic_models[entity_name]
            self._models_cache[entity_name] = model
            return model
        
        raise ValueError(f"Entity '{entity_name}' not found in schemas. Available entities: {list(self.schema_loader.schemas.keys())}")
    
    def get_enum(self, entity_name: str, field_name: str) -> Type[Enum]:
        """
        Get a dynamically generated enum for an entity field.
        
        Args:
            entity_name: Name of the entity
            field_name: Name of the field with enum values
            
        Returns:
            Enum class for the field
            
        Raises:
            ValueError: If enum not found
        """
        enum_key = f"{entity_name}.{field_name}"
        
        if enum_key in self._enums_cache:
            return self._enums_cache[enum_key]
        
        if enum_key in self.schema_loader.enums:
            enum_class = self.schema_loader.enums[enum_key]
            self._enums_cache[enum_key] = enum_class
            return enum_class
        
        raise ValueError(f"Enum '{enum_key}' not found in schemas")
    
    def get_enum_values(self, entity_name: str, field_name: str) -> List[str]:
        """
        Get enum values for a field as strings.
        
        Args:
            entity_name: Name of the entity
            field_name: Name of the field with enum values
            
        Returns:
            List of valid enum values as strings
        """
        return self.schema_loader.get_field_enum_values(entity_name, field_name) or []
    
    def list_entities(self) -> List[str]:
        """List all available entity names."""
        return list(self.schema_loader.schemas.keys())
    
    def list_enums(self) -> List[str]:
        """List all available enum keys (entity.field format)."""
        return list(self.schema_loader.enums.keys())
    
    def validate_entity_data(self, entity_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate entity data against its schema.
        
        Args:
            entity_name: Name of the entity
            data: Data to validate
            
        Returns:
            Validated data
            
        Raises:
            ValueError: If validation fails
        """
        model = self.get_model(entity_name)
        instance = model(**data)
        return instance.model_dump(by_alias=True)


# Global instance for convenient access
_global_models = None

def get_models(schema_path: Optional[str] = None) -> DynamicModels:
    """
    Get the global DynamicModels instance.
    
    Args:
        schema_path: Path to schema directory (only used on first call)
        
    Returns:
        DynamicModels instance
    """
    global _global_models
    if _global_models is None:
        _global_models = DynamicModels(schema_path)
    return _global_models


# Convenience functions for backward compatibility
def get_organization_model():
    """Get Organization model class."""
    return get_models().get_model('organization')

def get_traceable_unit_model():
    """Get TraceableUnit model class."""
    return get_models().get_model('traceable_unit')

def get_transaction_model():
    """Get Transaction model class."""
    return get_models().get_model('transaction')

def get_material_processing_model():
    """Get MaterialProcessing model class."""
    return get_models().get_model('material_processing')

def get_organization_types():
    """Get OrganizationType enum values as strings."""
    return get_models().get_enum_values('organization', 'organizationType')

def get_unit_types():
    """Get UnitType enum values as strings."""
    return get_models().get_enum_values('traceable_unit', 'unitType')

def get_process_types():
    """Get ProcessType enum values as strings."""
    return get_models().get_enum_values('material_processing', 'processType')


# For backward compatibility with existing imports
class OrganizationType:
    """Backward compatibility for OrganizationType enum."""
    @classmethod
    def __getattr__(cls, name):
        org_types = get_organization_types()
        if name.lower() in org_types:
            return name.lower()
        raise AttributeError(f"'{cls.__name__}' has no attribute '{name}'")

class UnitType:
    """Backward compatibility for UnitType enum."""
    @classmethod
    def __getattr__(cls, name):
        unit_types = get_unit_types()
        if name.lower() in unit_types:
            return name.lower()
        raise AttributeError(f"'{cls.__name__}' has no attribute '{name}'")

class ProcessType:
    """Backward compatibility for ProcessType enum."""
    @classmethod
    def __getattr__(cls, name):
        process_types = get_process_types()
        if name.lower() in process_types:
            return name.lower()
        raise AttributeError(f"'{cls.__name__}' has no attribute '{name}'")


# Make specific enum values available for backward compatibility
# These will be populated dynamically from schemas
def _populate_enum_constants():
    """Populate enum constants for backward compatibility."""
    try:
        models = get_models()
        
        # Organization types
        org_types = models.get_enum_values('organization', 'organizationType')
        for org_type in org_types:
            setattr(OrganizationType, org_type.upper(), org_type)
        
        # Unit types  
        unit_types = models.get_enum_values('traceable_unit', 'unitType')
        for unit_type in unit_types:
            setattr(UnitType, unit_type.upper().replace('-', '_'), unit_type)
        
        # Process types
        process_types = models.get_enum_values('material_processing', 'processType')
        for process_type in process_types:
            setattr(ProcessType, process_type.upper(), process_type)
            
    except Exception as e:
        # Schema loading might fail in some contexts, that's OK
        pass

# Populate constants on module load
_populate_enum_constants()