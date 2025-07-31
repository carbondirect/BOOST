"""
BOOST Python Reference Implementation - Validation Utilities

This module provides JSON Schema validation utilities for BOOST entities,
cross-entity relationship validation, and business logic validation.
"""

import json
import os
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
import jsonschema
from jsonschema import validate, ValidationError
from datetime import datetime


class BOOSTValidator:
    """Main validation class for BOOST entities."""
    
    def __init__(self, schema_base_path: Optional[str] = None):
        """
        Initialize validator with schema files.
        
        Args:
            schema_base_path: Path to BOOST schema directory. If None, uses relative path.
        """
        if schema_base_path is None:
            # Default to the schema directory in the repository
            current_dir = Path(__file__).parent
            self.schema_base_path = current_dir.parent.parent / "schema"
        else:
            self.schema_base_path = Path(schema_base_path)
        
        self.schemas: Dict[str, Dict] = {}
        self.cross_entity_rules: Dict = {}
        self.business_logic_rules: Dict = {}
        
        self._load_schemas()
    
    def _load_schemas(self):
        """Load all JSON schemas from the schema directory."""
        try:
            # Load individual entity schemas
            for entity_dir in self.schema_base_path.iterdir():
                if entity_dir.is_dir() and (entity_dir / "validation_schema.json").exists():
                    schema_file = entity_dir / "validation_schema.json"
                    with open(schema_file, 'r') as f:
                        schema_data = json.load(f)
                        # Extract the actual schema from the wrapper structure
                        if 'schema' in schema_data:
                            self.schemas[entity_dir.name] = schema_data['schema']
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
    
    def validate_entity(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate a single entity against its JSON schema.
        
        Args:
            entity_type: Type of entity (e.g., 'organization', 'traceable_unit')
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        if entity_type not in self.schemas:
            return False, [f"Unknown entity type: {entity_type}"]
        
        try:
            validate(instance=entity_data, schema=self.schemas[entity_type])
            return True, []
        except ValidationError as e:
            return False, [str(e)]
    
    def validate_required_fields(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate that all required fields are present.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        if entity_type not in self.schemas:
            return False, [f"Unknown entity type: {entity_type}"]
        
        schema = self.schemas[entity_type]
        required_fields = schema.get('required', [])
        errors = []
        
        for field in required_fields:
            if field not in entity_data:
                errors.append(f"Missing required field: {field}")
        
        return len(errors) == 0, errors
    
    def validate_foreign_keys(self, entities: Dict[str, List[Dict[str, Any]]]) -> Tuple[bool, List[str]]:
        """
        Validate foreign key references between entities.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Create lookup tables for all entities
        entity_lookup = {}
        for entity_type, entity_list in entities.items():
            entity_lookup[entity_type] = {}
            for entity in entity_list:
                # Get the primary key field for this entity type
                primary_key = self._get_primary_key_field(entity_type)
                if primary_key and primary_key in entity:
                    entity_lookup[entity_type][entity[primary_key]] = entity
        
        # Validate foreign key references
        foreign_key_rules = self.cross_entity_rules.get('foreignKeyConstraints', {})
        
        for entity_type, fk_rules in foreign_key_rules.items():
            if entity_type.lower() in entities:
                for entity in entities[entity_type.lower()]:
                    for field_name, fk_rule in fk_rules.get('properties', {}).items():
                        if field_name in entity:
                            target_entity = fk_rule.get('targetEntity')
                            if target_entity and target_entity.lower() in entity_lookup:
                                fk_value = entity[field_name]
                                if fk_value not in entity_lookup[target_entity.lower()]:
                                    errors.append(
                                        f"Foreign key violation: {entity_type}.{field_name} "
                                        f"references non-existent {target_entity}: {fk_value}"
                                    )
        
        return len(errors) == 0, errors
    
    def validate_business_logic(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate business logic rules for an entity.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Volume and mass conservation for MaterialProcessing
        if entity_type == 'material_processing':
            errors.extend(self._validate_volume_conservation(entity_data))
        
        # Species composition validation for TraceableUnit
        elif entity_type == 'traceable_unit':
            errors.extend(self._validate_species_composition(entity_data))
        
        # Transaction quantity validation
        elif entity_type == 'transaction':
            errors.extend(self._validate_transaction_quantities(entity_data))
        
        return len(errors) == 0, errors
    
    def _validate_volume_conservation(self, processing_data: Dict[str, Any]) -> List[str]:
        """Validate volume conservation in material processing."""
        errors = []
        
        input_vol = processing_data.get('inputVolume')
        output_vol = processing_data.get('outputVolume')
        vol_loss = processing_data.get('volumeLoss', 0)
        
        if all(v is not None for v in [input_vol, output_vol]):
            if input_vol < (output_vol + vol_loss):
                errors.append(
                    f"Volume conservation violation: input ({input_vol}) < "
                    f"output ({output_vol}) + loss ({vol_loss})"
                )
        
        return errors
    
    def _validate_species_composition(self, tru_data: Dict[str, Any]) -> List[str]:
        """Validate species composition percentages sum to 100%."""
        errors = []
        
        species_composition = tru_data.get('speciesComposition', [])
        if species_composition:
            total_percentage = sum(
                species.get('percentage', 0) for species in species_composition
            )
            if abs(total_percentage - 100.0) > 0.01:  # Allow small floating point errors
                errors.append(
                    f"Species composition percentages sum to {total_percentage}%, must equal 100%"
                )
        
        return errors
    
    def _validate_transaction_quantities(self, transaction_data: Dict[str, Any]) -> List[str]:
        """Validate transaction quantities are reasonable."""
        errors = []
        
        quantity = transaction_data.get('quantity')
        if quantity is not None:
            if quantity <= 0:
                errors.append("Transaction quantity must be greater than 0")
            if quantity > 999999:  # Arbitrary large number check
                errors.append("Transaction quantity seems unreasonably large")
        
        return errors
    
    def _get_primary_key_field(self, entity_type: str) -> Optional[str]:
        """Get the primary key field name for an entity type."""
        primary_key_mapping = {
            'organization': 'organizationId',
            'traceable_unit': 'traceableUnitId',
            'transaction': 'transactionId',
            'material_processing': 'processingId',
            'claim': 'claimId',
            'certificate': 'certificateId',
            'geographic_data': 'geographicDataId'
        }
        return primary_key_mapping.get(entity_type.lower())
    
    def validate_temporal_consistency(self, entities: Dict[str, List[Dict[str, Any]]]) -> Tuple[bool, List[str]]:
        """
        Validate temporal consistency across related entities.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check that processing dates are after harvest dates
        if 'material_processing' in entities and 'traceable_unit' in entities:
            tru_lookup = {
                tru['traceableUnitId']: tru 
                for tru in entities['traceable_unit']
                if 'traceableUnitId' in tru
            }
            
            for processing in entities['material_processing']:
                input_tru_id = processing.get('inputTraceableUnitId')
                process_time = processing.get('processTimestamp')
                
                if input_tru_id and input_tru_id in tru_lookup and process_time:
                    harvest_date = tru_lookup[input_tru_id].get('createdTimestamp')
                    if harvest_date:
                        try:
                            process_dt = datetime.fromisoformat(process_time.replace('Z', '+00:00'))
                            harvest_dt = datetime.fromisoformat(harvest_date.replace('Z', '+00:00'))
                            
                            if process_dt < harvest_dt:
                                errors.append(
                                    f"Processing timestamp ({process_time}) is before "
                                    f"harvest timestamp ({harvest_date}) for TRU {input_tru_id}"
                                )
                        except ValueError:
                            errors.append(f"Invalid timestamp format in processing or TRU data")
        
        return len(errors) == 0, errors
    
    def comprehensive_validation(self, entities: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """
        Run comprehensive validation on a set of entities.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Dictionary with validation results
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'entity_results': {}
        }
        
        # Validate individual entities
        for entity_type, entity_list in entities.items():
            entity_errors = []
            for i, entity in enumerate(entity_list):
                # Schema validation
                is_valid, errors = self.validate_entity(entity_type, entity)
                if not is_valid:
                    entity_errors.extend([f"Entity {i}: {error}" for error in errors])
                
                # Business logic validation
                is_valid, errors = self.validate_business_logic(entity_type, entity)
                if not is_valid:
                    entity_errors.extend([f"Entity {i}: {error}" for error in errors])
            
            results['entity_results'][entity_type] = {
                'valid': len(entity_errors) == 0,
                'errors': entity_errors
            }
            
            if entity_errors:
                results['valid'] = False
                results['errors'].extend(entity_errors)
        
        # Cross-entity validation
        is_valid, errors = self.validate_foreign_keys(entities)
        if not is_valid:
            results['valid'] = False
            results['errors'].extend(errors)
        
        # Temporal validation
        is_valid, errors = self.validate_temporal_consistency(entities)
        if not is_valid:
            results['valid'] = False
            results['errors'].extend(errors)
        
        return results


def create_validator(schema_path: Optional[str] = None) -> BOOSTValidator:
    """
    Factory function to create a BOOST validator.
    
    Args:
        schema_path: Optional path to schema directory
        
    Returns:
        BOOSTValidator instance
    """
    return BOOSTValidator(schema_path)