"""
BOOST Python Reference Implementation - Dynamic Schema-Driven Validation

This module provides schema-driven validation utilities that automatically
adapt to schema changes without requiring code modifications.
"""

import json
import re
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple, Type
from pathlib import Path
import jsonschema
from jsonschema import validate, ValidationError

try:
    from .schema_loader import SchemaLoader
except ImportError:
    from schema_loader import SchemaLoader


class DynamicBOOSTValidator:
    """Schema-driven validator that adapts to schema changes automatically."""
    
    def __init__(self, schema_loader: Optional[SchemaLoader] = None, schema_path: Optional[str] = None):
        """
        Initialize dynamic validator.
        
        Args:
            schema_loader: Pre-configured schema loader
            schema_path: Path to schema directory (if schema_loader not provided)
        """
        if schema_loader is not None:
            self.schema_loader = schema_loader
        else:
            try:
                from .schema_loader import create_schema_loader
            except ImportError:
                from schema_loader import create_schema_loader
            self.schema_loader = create_schema_loader(schema_path)
    
    def validate_entity(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate entity against its JSON schema.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        schema = self.schema_loader.get_schema(entity_type)
        if not schema:
            return False, [f"Unknown entity type: {entity_type}"]
        
        try:
            validate(instance=entity_data, schema=schema)
            return True, []
        except ValidationError as e:
            return False, [str(e)]
        except Exception as e:
            return False, [f"Validation error: {str(e)}"]
    
    def validate_required_fields(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate that all required fields are present.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        schema = self.schema_loader.get_schema(entity_type)
        if not schema:
            return False, [f"Unknown entity type: {entity_type}"]
        
        required_fields = schema.get('required', [])
        errors = []
        
        for field in required_fields:
            if field not in entity_data:
                errors.append(f"Missing required field: {field}")
        
        return len(errors) == 0, errors
    
    def validate_field_constraints(self, entity_type: str, field_name: str, 
                                 field_value: Any) -> Tuple[bool, List[str]]:
        """
        Validate a specific field value against its constraints.
        
        Args:
            entity_type: Type of entity
            field_name: Name of field
            field_value: Value to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        constraints = self.schema_loader.get_field_constraints(entity_type, field_name)
        errors = []
        
        # String length constraints
        if isinstance(field_value, str):
            if 'min_length' in constraints and len(field_value) < constraints['min_length']:
                errors.append(f"Field '{field_name}' too short (min: {constraints['min_length']})")
            if 'max_length' in constraints and len(field_value) > constraints['max_length']:
                errors.append(f"Field '{field_name}' too long (max: {constraints['max_length']})")
            if 'pattern' in constraints:
                if not re.match(constraints['pattern'], field_value):
                    errors.append(f"Field '{field_name}' doesn't match pattern: {constraints['pattern']}")
        
        # Numeric constraints
        if isinstance(field_value, (int, float)):
            if 'minimum' in constraints and field_value < constraints['minimum']:
                errors.append(f"Field '{field_name}' below minimum: {constraints['minimum']}")
            if 'maximum' in constraints and field_value > constraints['maximum']:
                errors.append(f"Field '{field_name}' above maximum: {constraints['maximum']}")
        
        # Enum constraints
        if 'enum' in constraints and field_value not in constraints['enum']:
            errors.append(f"Field '{field_name}' has invalid value. Valid options: {constraints['enum']}")
        
        return len(errors) == 0, errors
    
    def validate_foreign_keys(self, entities: Dict[str, List[Dict[str, Any]]]) -> Tuple[bool, List[str]]:
        """
        Validate foreign key references between entities using dynamic discovery.
        
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
            primary_key = self.schema_loader.get_primary_key(entity_type)
            
            if primary_key:
                for entity in entity_list:
                    if primary_key in entity:
                        entity_lookup[entity_type][entity[primary_key]] = entity
        
        # Validate relationships using dynamic discovery
        for entity_type, entity_list in entities.items():
            relationships = self.schema_loader.get_relationships(entity_type)
            
            for entity in entity_list:
                for relationship in relationships:
                    field_name = relationship.get('field')
                    target_entity = relationship.get('targetEntity', '').lower()
                    required = relationship.get('required', False)
                    
                    if field_name in entity:
                        fk_value = entity[field_name]
                        
                        # Handle array of foreign keys
                        if isinstance(fk_value, list):
                            for fk_item in fk_value:
                                if target_entity in entity_lookup:
                                    if fk_item not in entity_lookup[target_entity]:
                                        errors.append(
                                            f"Foreign key violation: {entity_type}.{field_name} "
                                            f"references non-existent {target_entity}: {fk_item}"
                                        )
                        else:
                            # Single foreign key
                            if target_entity in entity_lookup:
                                if fk_value not in entity_lookup[target_entity]:
                                    errors.append(
                                        f"Foreign key violation: {entity_type}.{field_name} "
                                        f"references non-existent {target_entity}: {fk_value}"
                                    )
                    elif required:
                        errors.append(f"Missing required foreign key: {entity_type}.{field_name}")
        
        return len(errors) == 0, errors
    
    def validate_business_logic(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate business logic rules dynamically loaded from configuration.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        business_rules = self.schema_loader.business_logic_rules
        
        # Get execution order from configuration
        execution_order = business_rules.get('validationExecution', {}).get('executionOrder', [
            'volumeMassConservation', 'temporalLogicRules', 'geographicLogicRules',
            'speciesCompositionRules', 'certificationLogicRules', 'regulatoryComplianceRules',
            'economicLogicRules', 'qualityAssuranceRules'
        ])
        
        # Execute validation rules in configured order
        for rule_category in execution_order:
            if rule_category in business_rules:
                category_errors = self._validate_business_rule_category(
                    entity_type, entity_data, rule_category, business_rules[rule_category]
                )
                errors.extend(category_errors)
        
        return len(errors) == 0, errors
    
    def _validate_business_rule_category(self, entity_type: str, entity_data: Dict[str, Any], 
                                       category: str, rules: Dict[str, Any]) -> List[str]:
        """
        Validate a specific category of business rules.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            category: Rule category name
            rules: Rules configuration for this category
            
        Returns:
            List of validation errors
        """
        errors = []
        
        if category == 'volumeMassConservation':
            if entity_type == 'material_processing':
                volume_rules = rules.get('materialProcessing', {})
                errors.extend(self._validate_volume_conservation(entity_data, volume_rules))
                errors.extend(self._validate_mass_conservation(entity_data, volume_rules))
                errors.extend(self._validate_density_consistency(entity_data, volume_rules))
            elif entity_type == 'transaction':
                transaction_rules = rules.get('transactionQuantities', {})
                errors.extend(self._validate_transaction_quantities(entity_data, transaction_rules))
        
        elif category == 'temporalLogicRules':
            errors.extend(self._validate_temporal_business_logic(entity_type, entity_data, rules))
        
        elif category == 'geographicLogicRules':
            errors.extend(self._validate_geographic_business_logic(entity_type, entity_data, rules))
        
        elif category == 'speciesCompositionRules':
            if entity_type == 'traceable_unit':
                errors.extend(self._validate_species_composition(entity_data, rules))
                errors.extend(self._validate_species_compatibility(entity_data, rules))
        
        elif category == 'certificationLogicRules':
            if entity_type == 'claim':
                errors.extend(self._validate_certification_logic(entity_data, rules))
        
        elif category == 'economicLogicRules':
            if entity_type == 'transaction':
                errors.extend(self._validate_economic_logic(entity_data, rules))
        
        elif category == 'qualityAssuranceRules':
            if entity_type in ['traceable_unit', 'material_processing']:
                errors.extend(self._validate_quality_assurance(entity_data, rules))
        
        elif category == 'regulatoryComplianceRules':
            errors.extend(self._validate_regulatory_compliance(entity_type, entity_data, rules))
        
        # New validation categories for enhanced entities
        elif category == 'truTransactionConsistency':
            # This is handled at the comprehensive validation level, not per-entity
            pass
        
        elif category == 'reconciliationWorkflow':
            is_valid, rule_errors = self.validate_reconciliation_workflow(entity_type, entity_data)
            if not is_valid:
                errors.extend(rule_errors)
        
        elif category == 'timestampChronology':
            is_valid, rule_errors = self.validate_timestamp_chronology(entity_type, entity_data)
            if not is_valid:
                errors.extend(rule_errors)
        
        elif category == 'organizationalConsistency':
            is_valid, rule_errors = self.validate_organization_operational_consistency(entity_type, entity_data)
            if not is_valid:
                errors.extend(rule_errors)
        
        return errors
    
    def _validate_volume_conservation(self, processing_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate volume conservation using dynamic rules."""
        errors = []
        
        volume_conservation = rules.get('volumeConservation', {})
        if not volume_conservation:
            return errors
        
        input_vol = processing_data.get('inputVolume')
        output_vol = processing_data.get('outputVolume')
        vol_loss = processing_data.get('volumeLoss', 0)
        
        if all(v is not None for v in [input_vol, output_vol]):
            # Check basic conservation rule
            rule_formula = volume_conservation.get('validation', {}).get('formula', '')
            if 'inputVolume >= (outputVolume + volumeLoss)' in rule_formula:
                if input_vol < (output_vol + vol_loss):
                    tolerance = volume_conservation.get('validation', {}).get('tolerance', 0.001)
                    if abs(input_vol - (output_vol + vol_loss)) > tolerance:
                        errors.append(
                            f"Volume conservation violation: input ({input_vol}) < "
                            f"output ({output_vol}) + loss ({vol_loss})"
                        )
            
            # Check for process-specific exceptions
            process_type = processing_data.get('processType')
            exceptions = volume_conservation.get('exceptions', [])
            
            for exception in exceptions:
                if exception.get('processType') == process_type:
                    max_increase = exception.get('maxVolumeIncrease', 1.0)
                    if output_vol > input_vol * max_increase:
                        errors.append(
                            f"Volume increase exceeds limit for {process_type}: "
                            f"max {max_increase}x allowed"
                        )
        
        return errors
    
    def _validate_species_composition(self, tru_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate species composition using dynamic rules."""
        errors = []
        
        composition_math = rules.get('compositionMath', {})
        percentage_sum_rule = composition_math.get('percentageSum', {})
        
        if not percentage_sum_rule:
            return errors
        
        species_composition = tru_data.get('speciesComposition', [])
        if species_composition:
            total_percentage = sum(
                species.get('percentage', 0) for species in species_composition
            )
            
            # Get tolerance from rules
            tolerance = percentage_sum_rule.get('validation', {}).get('tolerance', 0.01)
            target_sum = 100.0
            
            if abs(total_percentage - target_sum) > tolerance:
                errors.append(
                    f"Species composition percentages sum to {total_percentage}%, "
                    f"must equal {target_sum}% (tolerance: ±{tolerance}%)"
                )
            
            # Validate individual bounds
            individual_bounds = composition_math.get('individualBounds', {})
            if individual_bounds:
                min_pct = individual_bounds.get('validation', {}).get('minPercentage', 0.0)
                max_pct = individual_bounds.get('validation', {}).get('maxPercentage', 100.0)
                
                for species in species_composition:
                    pct = species.get('percentage', 0)
                    if pct < min_pct or pct > max_pct:
                        errors.append(
                            f"Species percentage {pct}% outside valid range "
                            f"[{min_pct}%, {max_pct}%]"
                        )
        
        return errors
    
    def _validate_transaction_quantities(self, transaction_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate transaction quantities using dynamic rules."""
        errors = []
        
        availability_check = rules.get('availabilityCheck', {})
        if not availability_check:
            return errors
        
        quantity = transaction_data.get('quantity')
        if quantity is not None:
            # Basic quantity validation
            if quantity <= 0:
                errors.append("Transaction quantity must be greater than 0")
            
            # Check minimum transaction size if configured
            min_transaction = rules.get('minimumTransactionSize', {})
            if min_transaction:
                min_volume = min_transaction.get('validation', {}).get('minimumVolume', 0)
                min_value = min_transaction.get('validation', {}).get('minimumValue', 0)
                
                if quantity < min_volume:
                    errors.append(f"Transaction quantity {quantity} below minimum {min_volume}")
                
                contract_value = transaction_data.get('contractValue', 0)
                if contract_value < min_value:
                    errors.append(f"Transaction value {contract_value} below minimum {min_value}")
        
        return errors
    
    def _validate_mass_conservation(self, processing_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate mass conservation using dynamic rules."""
        errors = []
        
        mass_conservation = rules.get('massConservation', {})
        if not mass_conservation:
            return errors
        
        input_mass = processing_data.get('inputMass')
        output_mass = processing_data.get('outputMass')
        
        if all(v is not None for v in [input_mass, output_mass]):
            rule_formula = mass_conservation.get('validation', {}).get('formula', '')
            if 'inputMass >= outputMass' in rule_formula:
                tolerance = mass_conservation.get('validation', {}).get('tolerance', 0.001)
                if input_mass < output_mass and abs(input_mass - output_mass) > tolerance:
                    errors.append(
                        f"Mass conservation violation: input ({input_mass}) < output ({output_mass})"
                    )
            
            # Check typical loss rates
            process_type = processing_data.get('processType')
            if process_type:
                typical_rates = mass_conservation.get('typicalLossRates', {}).get(process_type, {})
                if typical_rates:
                    loss_rate = (input_mass - output_mass) / input_mass if input_mass > 0 else 0
                    min_loss = typical_rates.get('min', 0)
                    max_loss = typical_rates.get('max', 1)
                    
                    if loss_rate < min_loss or loss_rate > max_loss:
                        errors.append(
                            f"Mass loss rate {loss_rate:.3f} outside typical range for {process_type}: "
                            f"[{min_loss}, {max_loss}]"
                        )
        
        return errors
    
    def _validate_density_consistency(self, processing_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate density consistency using dynamic rules."""
        errors = []
        
        density_rules = rules.get('densityConsistency', {})
        if not density_rules:
            return errors
        
        input_mass = processing_data.get('inputMass')
        input_volume = processing_data.get('inputVolume')
        
        if all(v is not None and v > 0 for v in [input_mass, input_volume]):
            density = input_mass / input_volume
            
            # Check species ranges - this would need species info from linked TRU
            species_ranges = density_rules.get('validation', {}).get('speciesRanges', {})
            
            # For now, check against general wood density range
            general_min = min(r['min'] for r in species_ranges.values()) if species_ranges else 0.2
            general_max = max(r['max'] for r in species_ranges.values()) if species_ranges else 1.0
            
            if density < general_min or density > general_max:
                errors.append(
                    f"Calculated density {density:.3f} outside realistic range [{general_min}, {general_max}]"
                )
        
        return errors
    
    def _validate_temporal_business_logic(self, entity_type: str, entity_data: Dict[str, Any], 
                                        rules: Dict[str, Any]) -> List[str]:
        """Validate temporal business logic rules."""
        errors = []
        
        # Processing timeframes validation
        if entity_type == 'material_processing':
            processing_timeframes = rules.get('processingTimeframes', {})
            
            # Freshness degradation check
            freshness_rules = processing_timeframes.get('freshnessDegradation', {})
            if freshness_rules:
                process_timestamp = entity_data.get('processTimestamp')
                if process_timestamp:
                    # This would require harvest date from linked TRU - placeholder for now
                    material_type = entity_data.get('materialType', 'unknown')
                    freshness_limits = freshness_rules.get('validation', {})
                    
                    if material_type in freshness_limits:
                        max_days = freshness_limits[material_type].get('maxDays', 365)
                        # Implementation would check against harvest date
        
        return errors
    
    def _validate_geographic_business_logic(self, entity_type: str, entity_data: Dict[str, Any], 
                                          rules: Dict[str, Any]) -> List[str]:
        """Validate geographic business logic rules."""
        errors = []
        
        # Transportation distance validation
        if entity_type == 'transaction':
            transport_rules = rules.get('transportationDistance', {})
            economic_viability = transport_rules.get('economicViability', {})
            
            if economic_viability:
                # This would require geographic data - placeholder for implementation
                pass
        
        return errors
    
    def _validate_species_compatibility(self, tru_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate species compatibility using dynamic rules."""
        errors = []
        
        species_compatibility = rules.get('speciesCompatibility', {})
        ecosystem_rules = species_compatibility.get('ecosystemConsistency', {})
        
        if ecosystem_rules:
            species_composition = tru_data.get('speciesComposition', [])
            if len(species_composition) > 1:  # Mixed species
                ecosystems = ecosystem_rules.get('validation', {})
                
                # Check if all species are from compatible ecosystems
                species_names = [s.get('speciesName', '').lower() for s in species_composition]
                
                for ecosystem, compatible_species in ecosystems.items():
                    if isinstance(compatible_species, list):
                        compatible_species = [s.lower() for s in compatible_species]
                        if any(species in compatible_species for species in species_names):
                            # Check if ALL species are compatible
                            incompatible = [s for s in species_names if s not in compatible_species]
                            if incompatible:
                                errors.append(
                                    f"Species {incompatible} not compatible with {ecosystem} ecosystem"
                                )
                            break
        
        return errors
    
    def _validate_certification_logic(self, claim_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate certification logic rules."""
        errors = []
        
        chain_rules = rules.get('chainOfCustodyRules', {})
        certificate_validity = chain_rules.get('certificateValidity', {})
        
        if certificate_validity:
            # Check certificate expiry
            claim_expiry = claim_data.get('claimExpiry')
            if claim_expiry:
                try:
                    from datetime import datetime
                    if isinstance(claim_expiry, str):
                        expiry_dt = datetime.fromisoformat(claim_expiry.replace('Z', '+00:00'))
                        if expiry_dt < datetime.now(expiry_dt.tzinfo):
                            errors.append("Claim certificate has expired")
                except (ValueError, TypeError):
                    errors.append("Invalid claim expiry date format")
        
        return errors
    
    def _validate_economic_logic(self, transaction_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate economic logic rules."""
        errors = []
        
        pricing_rules = rules.get('pricingReasonableness', {})
        market_price_rules = pricing_rules.get('marketPriceRange', {})
        
        if market_price_rules:
            contract_value = transaction_data.get('contractValue')
            quantity = transaction_data.get('quantity')
            
            if all(v is not None and v > 0 for v in [contract_value, quantity]):
                price_per_unit = contract_value / quantity
                
                # Check against market ranges - would need material type classification
                price_ranges = market_price_rules.get('validation', {}).get('pricePerUnit', {})
                tolerance = market_price_rules.get('validation', {}).get('tolerance', 0.5)
                
                # For now, use a general reasonable range
                general_min = 10  # Minimum reasonable price
                general_max = 500  # Maximum reasonable price
                
                if price_per_unit < general_min * (1 - tolerance):
                    errors.append(f"Price per unit {price_per_unit} seems unreasonably low")
                elif price_per_unit > general_max * (1 + tolerance):
                    errors.append(f"Price per unit {price_per_unit} seems unreasonably high")
        
        return errors
    
    def _validate_quality_assurance(self, entity_data: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
        """Validate quality assurance rules."""
        errors = []
        
        moisture_rules = rules.get('moistureContentLimits', {})
        if moisture_rules:
            moisture_content = entity_data.get('moistureContent')
            if moisture_content is not None:
                species_limits = moisture_rules.get('speciesSpecificLimits', {}).get('validation', {})
                
                # Use general limits if species-specific not available
                general_min = 5  # Minimum reasonable moisture
                general_max = 70  # Maximum reasonable moisture
                
                if moisture_content < general_min or moisture_content > general_max:
                    errors.append(
                        f"Moisture content {moisture_content}% outside reasonable range "
                        f"[{general_min}%, {general_max}%]"
                    )
        
        contamination_rules = rules.get('contaminationLimits', {})
        if contamination_rules:
            acceptable_levels = contamination_rules.get('acceptableLevels', {}).get('validation', {})
            
            for contaminant, max_level in acceptable_levels.items():
                if contaminant != 'units':
                    contamination_level = entity_data.get(f'{contaminant}Contamination')
                    if contamination_level is not None and contamination_level > max_level:
                        errors.append(
                            f"{contaminant.title()} contamination {contamination_level}% exceeds "
                            f"maximum allowed {max_level}%"
                        )
        
        return errors
    
    def _validate_regulatory_compliance(self, entity_type: str, entity_data: Dict[str, Any], 
                                      rules: Dict[str, Any]) -> List[str]:
        """Validate regulatory compliance rules."""
        errors = []
        
        # LCFS compliance for claims
        if entity_type == 'claim':
            lcfs_rules = rules.get('lcfsCompliance', {})
            pathway_validity = lcfs_rules.get('pathwayValidity', {})
            
            if pathway_validity:
                claim_type = entity_data.get('claimType', '')
                if 'LCFS' in claim_type or 'lcfs' in claim_type.lower():
                    # Check pathway certification
                    validation_config = pathway_validity.get('validation', {})
                    if validation_config.get('carbCertified'):
                        # Implementation would check CARB certification status
                        pass
        
        # EU RED compliance
        red_rules = rules.get('euRedCompliance', {})
        if red_rules and entity_type == 'claim':
            sustainability_criteria = red_rules.get('sustainabilityCriteria', {})
            if sustainability_criteria:
                # Implementation would check RED sustainability criteria
                pass
        
        return errors
    
    def validate_temporal_consistency(self, entities: Dict[str, List[Dict[str, Any]]]) -> Tuple[bool, List[str]]:
        """
        Validate temporal consistency using dynamic schema analysis.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Get temporal logic rules
        temporal_rules = self.schema_loader.business_logic_rules.get('temporalLogicRules', {})
        
        # Check processing timeframes
        processing_timeframes = temporal_rules.get('processingTimeframes', {})
        chronological_order = processing_timeframes.get('chronologicalOrder', {})
        
        if chronological_order and 'material_processing' in entities and 'traceable_unit' in entities:
            # Build TRU lookup
            tru_lookup = {}
            for tru in entities['traceable_unit']:
                tru_id_field = self.schema_loader.get_primary_key('traceable_unit')
                if tru_id_field and tru_id_field in tru:
                    tru_lookup[tru[tru_id_field]] = tru
            
            # Validate processing vs harvest dates
            for processing in entities['material_processing']:
                input_tru_id = processing.get('inputTraceableUnitId')
                process_time = processing.get('processTimestamp')
                
                if input_tru_id and input_tru_id in tru_lookup and process_time:
                    harvest_date = tru_lookup[input_tru_id].get('createdTimestamp')
                    if harvest_date:
                        try:
                            if isinstance(process_time, str):
                                process_dt = datetime.fromisoformat(process_time.replace('Z', '+00:00'))
                            else:
                                process_dt = process_time
                                
                            if isinstance(harvest_date, str):
                                harvest_dt = datetime.fromisoformat(harvest_date.replace('Z', '+00:00'))
                            else:
                                harvest_dt = harvest_date
                            
                            buffer_days = chronological_order.get('validation', {}).get('bufferDays', 0)
                            if process_dt < harvest_dt:
                                errors.append(
                                    f"Processing timestamp ({process_time}) is before "
                                    f"harvest timestamp ({harvest_date}) for TRU {input_tru_id}"
                                )
                        except (ValueError, TypeError) as e:
                            errors.append(f"Invalid timestamp format: {str(e)}")
        
        return len(errors) == 0, errors
    
    def comprehensive_validation(self, entities: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """
        Run comprehensive validation on a set of entities using dynamic schemas.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Dictionary with validation results
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'entity_results': {},
            'schema_info': {
                'available_entities': self.schema_loader.get_all_entity_types(),
                'validation_timestamp': datetime.now().isoformat()
            }
        }
        
        # Validate individual entities
        for entity_type, entity_list in entities.items():
            entity_errors = []
            entity_warnings = []
            
            for i, entity in enumerate(entity_list):
                # Schema validation
                is_valid, errors = self.validate_entity(entity_type, entity)
                if not is_valid:
                    entity_errors.extend([f"Entity {i}: {error}" for error in errors])
                
                # Schema compatibility check
                is_compatible, compat_messages = self.schema_loader.validate_schema_compatibility(entity_type, entity)
                for msg in compat_messages:
                    if 'Unknown field' in msg:
                        entity_warnings.append(f"Entity {i}: {msg}")
                    else:
                        entity_errors.append(f"Entity {i}: {msg}")
                
                # Business logic validation
                is_valid, errors = self.validate_business_logic(entity_type, entity)
                if not is_valid:
                    entity_errors.extend([f"Entity {i}: {error}" for error in errors])
            
            results['entity_results'][entity_type] = {
                'valid': len(entity_errors) == 0,
                'errors': entity_errors,
                'warnings': entity_warnings,
                'count': len(entity_list)
            }
            
            if entity_errors:
                results['valid'] = False
                results['errors'].extend(entity_errors)
            
            results['warnings'].extend(entity_warnings)
        
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
        
        # TRU-Transaction consistency validation
        is_valid, errors = self.validate_tru_transaction_consistency(entities)
        if not is_valid:
            results['valid'] = False
            results['errors'].extend(errors)
        
        return results
    
    def validate_tru_transaction_consistency(self, entities: Dict[str, List[Dict[str, Any]]]) -> Tuple[bool, List[str]]:
        """
        Validate TRU-transaction consistency using entity relationships.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        if 'transaction' not in entities or 'traceable_unit' not in entities:
            return True, errors  # Skip if entities not present
        
        # Build TRU lookup
        tru_lookup = {}
        for tru in entities['traceable_unit']:
            tru_id_field = self.schema_loader.get_primary_key('traceable_unit')
            if tru_id_field and tru_id_field in tru:
                tru_lookup[tru[tru_id_field]] = tru
        
        # Validate TRU references in transactions
        for transaction in entities['transaction']:
            tru_ids = transaction.get('traceableUnitIds', [])
            media_breaks = transaction.get('mediaBreaksDetected', [])
            
            # Check that all referenced TRUs exist
            for tru_id in tru_ids:
                if tru_id not in tru_lookup:
                    errors.append(f"Transaction {transaction.get('transactionId', 'unknown')} references non-existent TRU: {tru_id}")
            
            # Validate media breaks array length matches TRU array length
            if tru_ids and media_breaks and len(media_breaks) != len(tru_ids):
                errors.append(
                    f"Transaction {transaction.get('transactionId', 'unknown')}: "
                    f"mediaBreaksDetected array length ({len(media_breaks)}) must match "
                    f"traceableUnitIds array length ({len(tru_ids)})"
                )
        
        return len(errors) == 0, errors
    
    def validate_reconciliation_workflow(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate reconciliation workflow logic for transactions.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        if entity_type != 'transaction':
            return True, errors  # Only applies to transactions
        
        status = entity_data.get('reconciliationStatus')
        if not status:
            return True, errors  # Skip if no reconciliation status
        
        # Validate status transitions and requirements
        valid_statuses = ['pending', 'resolved', 'disputed']
        if status not in valid_statuses:
            errors.append(f"Invalid reconciliation status: {status}. Valid values: {valid_statuses}")
        
        # Additional validation based on status
        if status == 'resolved':
            # For resolved status, ensure we have manipulation timestamps indicating processing
            timestamps = entity_data.get('manipulationTimestamps', [])
            if not timestamps:
                errors.append("Reconciliation status 'resolved' requires manipulation timestamps")
        
        elif status == 'disputed':
            # For disputed status, could require additional documentation
            # This is a placeholder for future business rule expansion
            pass
        
        return len(errors) == 0, errors
    
    def validate_timestamp_chronology(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate chronological order of timestamps in transactions.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        if entity_type != 'transaction':
            return True, errors  # Only applies to transactions
        
        timestamps = entity_data.get('manipulationTimestamps', [])
        transaction_date = entity_data.get('transactionDate')
        
        if not timestamps:
            return True, errors  # Skip if no manipulation timestamps
        
        try:
            # Convert timestamps to datetime objects for comparison
            datetime_objects = []
            for ts in timestamps:
                if isinstance(ts, str):
                    # Handle different timestamp formats
                    ts_clean = ts.replace('Z', '+00:00')
                    dt = datetime.fromisoformat(ts_clean)
                    datetime_objects.append(dt)
                else:
                    datetime_objects.append(ts)
            
            # Check chronological order
            for i in range(1, len(datetime_objects)):
                if datetime_objects[i] < datetime_objects[i-1]:
                    errors.append(
                        f"Manipulation timestamps not in chronological order: "
                        f"{timestamps[i]} is before {timestamps[i-1]}"
                    )
            
            # Validate against transaction date if available
            if transaction_date:
                try:
                    tx_date = datetime.fromisoformat(f"{transaction_date}T00:00:00+00:00")
                    for i, dt in enumerate(datetime_objects):
                        if dt.date() < tx_date.date():
                            errors.append(
                                f"Manipulation timestamp {timestamps[i]} is before transaction date {transaction_date}"
                            )
                except ValueError:
                    pass  # Skip if transaction date format is invalid
                    
        except (ValueError, TypeError) as e:
            errors.append(f"Invalid timestamp format in manipulation timestamps: {str(e)}")
        
        return len(errors) == 0, errors
    
    def validate_organization_operational_consistency(self, entity_type: str, entity_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate operational consistency for enhanced organization fields.
        
        Args:
            entity_type: Type of entity
            entity_data: Entity data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        if entity_type != 'organization':
            return True, errors  # Only applies to organizations
        
        org_type = entity_data.get('organizationType')
        equipment_ids = entity_data.get('equipmentIds', [])
        harvest_sites = entity_data.get('harvestSites', [])
        tru_ids = entity_data.get('traceableUnitIds', [])
        
        # Validate that harvester organizations have appropriate resources
        if org_type == 'harvester':
            if not equipment_ids and harvest_sites:
                errors.append("Harvester organizations with harvest sites should have equipment assignments")
            
            if harvest_sites and not tru_ids:
                errors.append("Harvester organizations with harvest sites should manage TRUs")
        
        # Validate that processor organizations have appropriate setup
        elif org_type == 'processor':
            if tru_ids and not equipment_ids:
                errors.append("Processor organizations managing TRUs should have processing equipment")
        
        # Validate infrastructure consistency
        skid_roads = entity_data.get('skidRoads', [])
        forest_roads = entity_data.get('forestRoads', [])
        
        if harvest_sites and not (skid_roads or forest_roads):
            errors.append("Organizations with harvest sites should have transportation infrastructure (skid roads or forest roads)")
        
        return len(errors) == 0, errors
    
    def refresh_schemas(self):
        """Reload schemas and regenerate validation rules."""
        self.schema_loader.refresh_schemas()


def create_dynamic_validator(schema_loader: Optional[SchemaLoader] = None, 
                           schema_path: Optional[str] = None) -> DynamicBOOSTValidator:
    """Factory function to create a dynamic BOOST validator."""
    return DynamicBOOSTValidator(schema_loader, schema_path)