#!/usr/bin/env python3
"""
Comprehensive schema validation for BOOST documentation build
"""
import json
import re
import sys
from pathlib import Path

def validate_schemas():
    """Run comprehensive schema validation"""
    schema_dir = Path('schema')
    errors = []
    warnings = []
    
    # Load all schemas
    schemas = {}
    entities = {}
    
    for schema_file in schema_dir.rglob('validation_schema.json'):
        try:
            with open(schema_file, 'r') as f:
                schema_data = json.load(f)
            
            if 'boost_metadata' in schema_data and 'entity' in schema_data['boost_metadata']:
                entity_info = schema_data['boost_metadata']['entity']
                entity_name = entity_info['name']
                entities[entity_name] = schema_data
                
        except Exception as e:
            errors.append(f'Error loading {schema_file}: {e}')
    
    print(f'✅ Loaded and validated {len(entities)} entity schemas')
    
    # Additional production validations - All entity patterns
    fk_patterns = {
        'ORG-': 'Organization',
        'TRU-': 'TraceableUnit', 
        'OP-': 'Operator',
        'GEO-': 'GeographicData',
        'AUD-': 'Audit',
        'BIO-': 'BiometricIdentifier',
        'CB-': 'CertificationBody',
        'CERT-': 'Certificate',
        'CERT-SCHEME-': 'CertificationScheme',
        'CLA-': 'Claim',
        'CUST-': 'Customer',
        'DOC-': 'SalesDeliveryDocument',
        'ECD-': 'EnergyCarbonData',
        'EQ-': 'Equipment',
        'LCFS-RPT-': 'LcfsReporting',
        'LH-': 'LocationHistory',
        'MAT-': 'Material',
        'MBA-': 'MassBalanceAccount',
        'MCV-': 'MoistureContent',
        'MP-': 'MaterialProcessing',
        'MR-': 'MeasurementRecord',
        'PG-': 'ProductGroup',
        'PH-': 'ProcessingHistory',
        'REC-': 'DataReconciliation',
        'SB-': 'SupplyBase',
        'SBR-': 'SupplyBaseReport',
        'SC-': 'SpeciesComponent',
        'SUP-': 'Supplier',
        'TB-': 'TransactionBatch',
        'TP-': 'TrackingPoint',
        'TXN-': 'Transaction',
        'VS-': 'VerificationStatement'
    }
    
    # Validate FK integrity
    for entity_name, schema_data in entities.items():
        properties = schema_data['schema'].get('properties', {})
        for prop_name, prop_def in properties.items():
            if 'pattern' in prop_def:
                pattern = prop_def['pattern']
                match = re.search(r'\\^([A-Z]+-)', pattern)
                if match:
                    prefix = match.group(1)
                    if prefix in fk_patterns:
                        target_entity = fk_patterns[prefix]
                        if target_entity not in entities:
                            errors.append(f'{entity_name}.{prop_name}: References missing entity {target_entity}')
    
    if errors:
        print('❌ Schema validation errors:')
        for error in errors:
            print(f'  - {error}')
        return False
    
    if warnings:
        print('⚠️ Schema validation warnings:')
        for warning in warnings:
            print(f'  - {warning}')
    
    print('✅ Schema validation passed')
    return True

if __name__ == "__main__":
    success = validate_schemas()
    sys.exit(0 if success else 1)