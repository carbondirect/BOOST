"""
BOOST Python Reference Implementation - Main Client Library

This module provides a high-level client interface for working with BOOST
biomass chain of custody data, including entity management, validation,
and supply chain tracking.
"""

import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from pathlib import Path

try:
    from .schema_loader import SchemaLoader
    from .dynamic_validation import DynamicBOOSTValidator
except ImportError:
    # Handle absolute imports when run directly
    from schema_loader import SchemaLoader
    from dynamic_validation import DynamicBOOSTValidator


class BOOSTClient:
    """Main client for BOOST biomass chain of custody operations."""
    
    def __init__(self, context_url: Optional[str] = None, schema_path: Optional[str] = None):
        """
        Initialize BOOST client.
        
        Args:
            context_url: URL to JSON-LD context (optional)
            schema_path: Path to BOOST schema directory (optional)
        """
        self.context_url = context_url or "https://github.com/carbondirect/BOOST/context"
        self.schema_loader = SchemaLoader(schema_path)
        self.validator = DynamicBOOSTValidator(self.schema_loader)
        
        # Entity storage
        self.organizations: Dict[str, Any] = {}
        self.traceable_units: Dict[str, Any] = {}
        self.transactions: Dict[str, Any] = {}
        self.material_processing: Dict[str, Any] = {}
        self.claims: Dict[str, Any] = {}
        
        # Default context for JSON-LD
        self.default_context = {
            "@context": {
                "boost": "https://github.com/carbondirect/BOOST/schemas#",
                "schema": "http://schema.org/",
                "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#"
            }
        }
    
    def create_organization(
        self,
        organization_id: str,
        name: str,
        org_type: str,
        **kwargs
    ) -> Any:
        """
        Create a new Organization entity.
        
        Args:
            organization_id: Unique organization identifier
            name: Organization name
            org_type: Type of organization
            **kwargs: Additional optional fields
            
        Returns:
            Dynamic Organization instance
        """
        # Validate org_type against schema enums
        valid_types = self.schema_loader.get_field_enum_values('organization', 'organizationType')
        if valid_types and org_type not in valid_types:
            raise ValueError(f"Invalid organization type '{org_type}'. Valid types: {valid_types}")
        
        org_data = {
            "@context": self.default_context["@context"],
            "@type": "Organization",
            "@id": f"https://github.com/carbondirect/BOOST/schemas/organization/{organization_id}",
            "organizationId": organization_id,
            "organizationName": name,
            "organizationType": org_type,
            "lastUpdated": datetime.utcnow(),
            **kwargs
        }
        
        # Use dynamic model
        OrganizationModel = self.schema_loader.get_model('organization')
        if not OrganizationModel:
            raise ValueError("Organization schema not loaded")
        
        organization = OrganizationModel(**org_data)
        self.organizations[organization_id] = organization
        return organization
    
    def create_traceable_unit(
        self,
        traceable_unit_id: str,
        unit_type: str,
        harvester_id: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Create a new TraceableUnit entity.
        
        Args:
            traceable_unit_id: Unique TRU identifier
            unit_type: Type of traceable unit
            harvester_id: Organization that harvested this unit
            **kwargs: Additional optional fields
            
        Returns:
            Dynamic TraceableUnit instance
        """
        # Validate unit_type against schema enums
        valid_types = self.schema_loader.get_field_enum_values('traceable_unit', 'unitType')
        if valid_types and unit_type not in valid_types:
            raise ValueError(f"Invalid unit type '{unit_type}'. Valid types: {valid_types}")
        
        tru_data = {
            "@context": self.default_context["@context"],
            "@type": "TraceableUnit", 
            "@id": f"https://github.com/carbondirect/BOOST/schemas/traceable-unit/{traceable_unit_id}",
            "traceableUnitId": traceable_unit_id,
            "unitType": unit_type,
            "createdTimestamp": datetime.utcnow(),
            "lastUpdated": datetime.utcnow(),
            **kwargs
        }
        
        if harvester_id:
            tru_data["harvesterId"] = harvester_id
        
        # Use dynamic model
        TraceableUnitModel = self.schema_loader.get_model('traceable_unit')
        if not TraceableUnitModel:
            raise ValueError("TraceableUnit schema not loaded")
        
        traceable_unit = TraceableUnitModel(**tru_data)
        self.traceable_units[traceable_unit_id] = traceable_unit
        return traceable_unit
    
    def create_transaction(
        self,
        transaction_id: str,
        organization_id: str,
        customer_id: str,
        transaction_date: str,
        **kwargs
    ) -> Any:
        """
        Create a new Transaction entity.
        
        Args:
            transaction_id: Unique transaction identifier
            organization_id: Seller organization ID
            customer_id: Buyer customer ID
            transaction_date: Date of transaction (YYYY-MM-DD)
            **kwargs: Additional optional fields
            
        Returns:
            Dynamic Transaction instance
        """
        transaction_data = {
            "@context": self.default_context["@context"],
            "@type": "Transaction",
            "@id": f"https://github.com/carbondirect/BOOST/schemas/transaction/{transaction_id}",
            "transactionId": transaction_id,
            "OrganizationId": organization_id,
            "CustomerId": customer_id,
            "transactionDate": transaction_date,
            "lastUpdated": datetime.utcnow(),
            **kwargs
        }
        
        # Use dynamic model
        TransactionModel = self.schema_loader.get_model('transaction')
        if not TransactionModel:
            raise ValueError("Transaction schema not loaded")
        
        transaction = TransactionModel(**transaction_data)
        self.transactions[transaction_id] = transaction
        return transaction
    
    def create_material_processing(
        self,
        processing_id: str,
        input_tru_id: str,
        output_tru_id: str,
        process_type: str,
        **kwargs
    ) -> Any:
        """
        Create a new MaterialProcessing entity.
        
        Args:
            processing_id: Unique processing identifier
            input_tru_id: Input traceable unit ID
            output_tru_id: Output traceable unit ID
            process_type: Type of processing operation
            **kwargs: Additional optional fields
            
        Returns:
            Dynamic MaterialProcessing instance
        """
        # Validate process_type against schema enums
        valid_types = self.schema_loader.get_field_enum_values('material_processing', 'processType')
        if valid_types and process_type not in valid_types:
            raise ValueError(f"Invalid process type '{process_type}'. Valid types: {valid_types}")
        
        processing_data = {
            "@context": self.default_context["@context"],
            "@type": "MaterialProcessing",
            "@id": f"https://github.com/carbondirect/BOOST/schemas/processing/{processing_id}",
            "processingId": processing_id,
            "inputTraceableUnitId": input_tru_id,
            "outputTraceableUnitId": output_tru_id,
            "processType": process_type,
            "processTimestamp": datetime.utcnow(),
            "lastUpdated": datetime.utcnow(),
            **kwargs
        }
        
        # Use dynamic model
        MaterialProcessingModel = self.schema_loader.get_model('material_processing')
        if not MaterialProcessingModel:
            raise ValueError("MaterialProcessing schema not loaded")
        
        processing = MaterialProcessingModel(**processing_data)
        self.material_processing[processing_id] = processing
        return processing
    
    def create_claim(
        self,
        claim_id: str,
        traceable_unit_id: str,
        claim_type: str,
        statement: str,
        validated: bool = False,
        **kwargs
    ) -> Any:
        """
        Create a new sustainability Claim entity.
        
        Args:
            claim_id: Unique claim identifier
            traceable_unit_id: TRU this claim applies to
            claim_type: Type of sustainability claim
            statement: Formal claim statement
            validated: Whether claim has been validated
            **kwargs: Additional optional fields
            
        Returns:
            Dynamic Claim instance
        """
        # Validate claim_type against schema enums
        valid_types = self.schema_loader.get_field_enum_values('claim', 'claimType')
        if valid_types and claim_type not in valid_types:
            raise ValueError(f"Invalid claim type '{claim_type}'. Valid types: {valid_types}")
        
        claim_data = {
            "@context": self.default_context["@context"],
            "@type": "Claim",
            "@id": f"https://github.com/carbondirect/BOOST/schemas/claim/{claim_id}",
            "claimId": claim_id,
            "traceableUnitId": traceable_unit_id,
            "claimType": claim_type,
            "statement": statement,
            "validated": validated,
            "lastUpdated": datetime.utcnow(),
            **kwargs
        }
        
        # Use dynamic model
        ClaimModel = self.schema_loader.get_model('claim')
        if not ClaimModel:
            raise ValueError("Claim schema not loaded")
        
        claim = ClaimModel(**claim_data)
        self.claims[claim_id] = claim
        return claim
    
    def validate_entity(self, entity: Any) -> Dict[str, Any]:
        """
        Validate a single entity.
        
        Args:
            entity: Entity to validate
            
        Returns:
            Validation result dictionary
        """
        entity_type = entity.type.lower().replace(' ', '_')
        entity_data = entity.dict(by_alias=True)
        
        # Schema validation
        is_valid, schema_errors = self.validator.validate_entity(entity_type, entity_data)
        
        # Business logic validation
        is_logic_valid, logic_errors = self.validator.validate_business_logic(entity_type, entity_data)
        
        return {
            'valid': is_valid and is_logic_valid,
            'schema_errors': schema_errors,
            'business_logic_errors': logic_errors,
            'entity_type': entity_type,
            'entity_id': getattr(entity, f"{entity_type.replace('_', '')}_id", "unknown")
        }
    
    def validate_all(self) -> Dict[str, Any]:
        """
        Validate all entities and their relationships.
        
        Returns:
            Comprehensive validation results
        """
        all_entities = {
            'organization': [org.dict(by_alias=True) for org in self.organizations.values()],
            'traceable_unit': [tru.dict(by_alias=True) for tru in self.traceable_units.values()],
            'transaction': [txn.dict(by_alias=True) for txn in self.transactions.values()],
            'material_processing': [proc.dict(by_alias=True) for proc in self.material_processing.values()],
            'claim': [claim.dict(by_alias=True) for claim in self.claims.values()]
        }
        
        return self.validator.comprehensive_validation(all_entities)
    
    def get_supply_chain(self, traceable_unit_id: str) -> Dict[str, Any]:
        """
        Get the complete supply chain for a traceable unit.
        
        Args:
            traceable_unit_id: Starting TRU ID
            
        Returns:
            Supply chain information
        """
        if traceable_unit_id not in self.traceable_units:
            return {'error': f'TraceableUnit {traceable_unit_id} not found'}
        
        supply_chain = {
            'traceable_unit': self.traceable_units[traceable_unit_id],
            'processing_history': [],
            'transactions': [],
            'claims': [],
            'parent_units': [],
            'child_units': []
        }
        
        # Find related processing operations
        for proc_id, processing in self.material_processing.items():
            if (processing.input_traceable_unit_id == traceable_unit_id or 
                processing.output_traceable_unit_id == traceable_unit_id):
                supply_chain['processing_history'].append(processing)
        
        # Find related transactions
        for txn_id, transaction in self.transactions.items():
            if hasattr(transaction, 'traceable_unit_id') and transaction.traceable_unit_id == traceable_unit_id:
                supply_chain['transactions'].append(transaction)
        
        # Find related claims
        for claim_id, claim in self.claims.items():
            if claim.traceable_unit_id == traceable_unit_id:
                supply_chain['claims'].append(claim)
        
        # Find parent and child units
        tru = self.traceable_units[traceable_unit_id]
        if tru.parent_traceable_unit_id and tru.parent_traceable_unit_id in self.traceable_units:
            supply_chain['parent_units'].append(self.traceable_units[tru.parent_traceable_unit_id])
        
        if tru.child_traceable_unit_ids:
            for child_id in tru.child_traceable_unit_ids:
                if child_id in self.traceable_units:
                    supply_chain['child_units'].append(self.traceable_units[child_id])
        
        return supply_chain
    
    def export_to_jsonld(self, include_context: bool = True) -> str:
        """
        Export all entities to JSON-LD format.
        
        Args:
            include_context: Whether to include @context in output
            
        Returns:
            JSON-LD string representation
        """
        export_data = []
        
        # Add all entities
        for entity_dict in [self.organizations, self.traceable_units, self.transactions, 
                           self.material_processing, self.claims]:
            for entity in entity_dict.values():
                entity_data = entity.dict(by_alias=True)
                if not include_context and '@context' in entity_data:
                    del entity_data['@context']
                export_data.append(entity_data)
        
        if include_context and export_data:
            # Add global context
            result = {
                "@context": self.default_context["@context"],
                "@graph": export_data
            }
            return json.dumps(result, indent=2, default=str)
        else:
            return json.dumps(export_data, indent=2, default=str)
    
    def import_from_jsonld(self, jsonld_data: Union[str, Dict]) -> Dict[str, Any]:
        """
        Import entities from JSON-LD data.
        
        Args:
            jsonld_data: JSON-LD string or dictionary
            
        Returns:
            Import results with counts and errors
        """
        if isinstance(jsonld_data, str):
            data = json.loads(jsonld_data)
        else:
            data = jsonld_data
        
        results = {
            'imported': {
                'organizations': 0,
                'traceable_units': 0,
                'transactions': 0,
                'material_processing': 0,
                'claims': 0
            },
            'errors': []
        }
        
        # Handle both @graph format and direct array
        entities = data.get('@graph', data if isinstance(data, list) else [data])
        
        for entity_data in entities:
            try:
                entity_type = entity_data.get('@type', '').lower()
                
                if entity_type == 'organization':
                    OrganizationModel = self.schema_loader.get_model('organization')
                    if OrganizationModel:
                        org = OrganizationModel(**entity_data)
                        org_data = org.dict(by_alias=True)
                        self.organizations[org_data['organizationId']] = org
                        results['imported']['organizations'] += 1
                    
                elif entity_type == 'traceableunit':
                    TraceableUnitModel = self.schema_loader.get_model('traceable_unit')
                    if TraceableUnitModel:
                        tru = TraceableUnitModel(**entity_data)
                        tru_data = tru.dict(by_alias=True)
                        self.traceable_units[tru_data['traceableUnitId']] = tru
                        results['imported']['traceable_units'] += 1
                    
                elif entity_type == 'transaction':
                    TransactionModel = self.schema_loader.get_model('transaction')
                    if TransactionModel:
                        txn = TransactionModel(**entity_data)
                        txn_data = txn.dict(by_alias=True)
                        self.transactions[txn_data['transactionId']] = txn
                        results['imported']['transactions'] += 1
                    
                elif entity_type == 'materialprocessing':
                    MaterialProcessingModel = self.schema_loader.get_model('material_processing')
                    if MaterialProcessingModel:
                        proc = MaterialProcessingModel(**entity_data)
                        proc_data = proc.dict(by_alias=True)
                        self.material_processing[proc_data['processingId']] = proc
                        results['imported']['material_processing'] += 1
                    
                elif entity_type == 'claim':
                    ClaimModel = self.schema_loader.get_model('claim')
                    if ClaimModel:
                        claim = ClaimModel(**entity_data)
                        claim_data = claim.dict(by_alias=True)
                        self.claims[claim_data['claimId']] = claim
                        results['imported']['claims'] += 1
                    
            except Exception as e:
                results['errors'].append(f"Error importing {entity_type}: {str(e)}")
        
        return results
    
    def generate_id(self, entity_type: str, prefix: Optional[str] = None) -> str:
        """
        Generate a unique ID for an entity.
        
        Args:
            entity_type: Type of entity (organization, traceable_unit, etc.)
            prefix: Optional prefix for the ID
            
        Returns:
            Generated unique ID
        """
        type_prefixes = {
            'organization': 'ORG',
            'traceable_unit': 'TRU', 
            'transaction': 'TXN',
            'material_processing': 'PROC',
            'claim': 'CLAIM'
        }
        
        base_prefix = type_prefixes.get(entity_type, 'BOOST')
        full_prefix = f"{base_prefix}-{prefix}" if prefix else base_prefix
        unique_suffix = str(uuid.uuid4())[:8].upper()
        
        return f"{full_prefix}-{unique_suffix}"
    
    def get_available_enum_values(self, entity_type: str, field_name: str) -> List[str]:
        """
        Get available enum values for a field from the schema.
        
        Args:
            entity_type: Type of entity
            field_name: Name of the field
            
        Returns:
            List of valid enum values
        """
        return self.schema_loader.get_field_enum_values(entity_type, field_name)
    
    def get_schema_info(self) -> Dict[str, Any]:
        """
        Get information about loaded schemas.
        
        Returns:
            Schema information dictionary
        """
        return {
            'available_entities': self.schema_loader.get_all_entity_types(),
            'schema_loader': type(self.schema_loader).__name__,
            'validator': type(self.validator).__name__,
            'context_url': self.context_url
        }
    
    def refresh_schemas(self):
        """
        Reload schemas and update dynamic models.
        """
        self.schema_loader.refresh_schemas()
        # Validator will automatically use updated schema_loader


def create_client(context_url: Optional[str] = None, schema_path: Optional[str] = None) -> BOOSTClient:
    """
    Factory function to create a BOOST client.
    
    Args:
        context_url: Optional JSON-LD context URL
        schema_path: Optional path to schema directory
        
    Returns:
        BOOSTClient instance
    """
    return BOOSTClient(context_url, schema_path)