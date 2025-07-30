#!/usr/bin/env python3
"""
BOOST Python Reference Implementation - Basic Workflow Example

This example demonstrates the basic BOOST workflow:
1. Create a harvesting organization
2. Create a traceable unit from harvest
3. Process the material
4. Execute a transaction
5. Validate the entire workflow

Run with: python basic_workflow.py
"""

import sys
import os
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from boost_client import create_client


def main():
    """Demonstrate basic BOOST workflow."""
    
    print("=== BOOST Python Reference Implementation ===")
    print("Basic Workflow Example")
    print("=" * 50)
    
    # Initialize BOOST client with dynamic schema loading
    client = create_client()
    
    # Display available schema information
    schema_info = client.get_schema_info()
    print(f"   Loaded {len(schema_info['available_entities'])} entity types")
    print(f"   Schema loader: {schema_info['schema_loader']}")
    print(f"   Validator: {schema_info['validator']}")
    
    # Step 1: Create a harvesting organization
    print("\n1. Creating harvesting organization...")
    # Get available organization types from schema
    org_types = client.get_available_enum_values('organization', 'organizationType')
    print(f"   Available organization types: {org_types}")
    
    harvester = client.create_organization(
        organization_id="ORG-PACIFIC-FOREST-001",
        name="Pacific Forest Products LLC",
        org_type="harvester",  # Use string value from schema
        contact_email="operations@pacificforest.com",
        contact_phone="+15415550123",  # Fixed format to match schema
        established_date="1985-06-15"
    )
    harvester_data = harvester.model_dump(by_alias=True)
    print(f"   ✓ Created organization: {harvester_data['organizationName']}")
    
    # Step 2: Create a mill/processor organization
    print("\n2. Creating processing organization...")
    mill = client.create_organization(
        organization_id="ORG-GREENWOOD-MILL-001",
        name="Greenwood Processing Mill",
        org_type="processor",  # Use string value from schema
        contact_email="info@greenwoodmill.com",
        established_date="1995-03-22"
    )
    mill_data = mill.model_dump(by_alias=True)
    print(f"   ✓ Created organization: {mill_data['organizationName']}")
    
    # Step 3: Create a traceable unit from harvest
    print("\n3. Creating traceable unit from harvest...")
    # Get available unit types from schema
    unit_types = client.get_available_enum_values('traceable_unit', 'unitType')
    print(f"   Available unit types: {unit_types}")
    
    log_pile = client.create_traceable_unit(
        traceable_unit_id="TRU-LOG-PILE-001", 
        unit_type="pile",  # Use string value from schema
        harvester_id=harvester_data['organizationId'],
        total_volume_m3=125.5,
        harvest_geographic_data_id="GEO-FOREST-SITE-001",
        current_geographic_data_id="GEO-MILL-ENTRANCE-001",
        material_type_id="MAT-DOUGLAS-FIR-LOGS",
        quality_grade="A",  # Fixed to use enum value from schema
        sustainability_certification="FSC Mix Credit",
        unique_identifier="RFID-001-A",  # Added required field
        is_multi_species=False  # Added required field
    )
    log_pile_data = log_pile.model_dump(by_alias=True)
    print(f"   ✓ Created traceable unit: {log_pile_data['traceableUnitId']}")
    print(f"     Volume: {log_pile_data.get('totalVolumeM3', 'N/A')} m³")
    
    # Step 4: Create processed traceable unit
    print("\n4. Creating processed traceable unit...")
    lumber_batch = client.create_traceable_unit(
        traceable_unit_id="TRU-LUMBER-BATCH-001",
        unit_type="processed_batch",  # Use string value from schema 
        harvester_id=harvester_data['organizationId'],  # Added required field
        total_volume_m3=95.0,  # Some volume lost in processing
        current_geographic_data_id="GEO-MILL-WAREHOUSE-001",
        parent_traceable_unit_id=log_pile_data['traceableUnitId'],
        material_type_id="MAT-DOUGLAS-FIR-LUMBER",
        quality_grade="A",  # Fixed to use enum value from schema
        sustainability_certification="FSC Mix Credit",
        unique_identifier="BATCH-001-A",  # Added required field
        is_multi_species=False  # Added required field
    )
    lumber_batch_data = lumber_batch.model_dump(by_alias=True)
    print(f"   ✓ Created processed unit: {lumber_batch_data['traceableUnitId']}")
    print(f"     Volume: {lumber_batch_data.get('totalVolumeM3', 'N/A')} m³")
    
    # Step 5: Create processing operation
    print("\n5. Creating processing operation...")
    # Get available process types from schema
    process_types = client.get_available_enum_values('material_processing', 'processType')
    print(f"   Available process types: {process_types}")
    
    processing = client.create_material_processing(
        processing_id="PROC-SAWMILL-001",
        input_tru_id=log_pile_data['traceableUnitId'],
        output_tru_id=lumber_batch_data['traceableUnitId'],
        process_type="crosscutting",  # Use string value from schema
        input_volume=125.5,
        output_volume=95.0,
        volume_loss=30.5,  # Sawdust, bark, etc.
        processing_geographic_data_id="GEO-MILL-SAWLINE-001"
    )
    processing_data = processing.model_dump(by_alias=True)
    print(f"   ✓ Created processing operation: {processing_data['processingId']}")
    print(f"     Process type: {processing_data['processType']}")
    input_vol = processing_data.get('inputVolume', 0)
    output_vol = processing_data.get('outputVolume', 0)
    if input_vol > 0:
        print(f"     Volume efficiency: {(output_vol / input_vol * 100):.1f}%")
    
    # Step 6: Create a customer and transaction
    print("\n6. Creating transaction...")
    customer_id = "CUST-HOMEBUILDER-001"
    
    transaction = client.create_transaction(
        transaction_id="TXN-LUMBER-SALE-001",
        organization_id=mill_data['organizationId'],
        customer_id=customer_id,
        transaction_date="2025-07-30",
        traceable_unit_id=lumber_batch_data['traceableUnitId'],
        quantity=50.0,  # Partial sale
        quantity_unit="cubic_meters",
        contract_value=4250.00,
        contract_currency="USD",
        transaction_status="completed"  # Added required field
    )
    transaction_data = transaction.model_dump(by_alias=True)
    print(f"   ✓ Created transaction: {transaction_data['transactionId']}")
    print(f"     Value: ${transaction_data.get('contractValue', 'N/A')} {transaction_data.get('contractCurrency', 'N/A')}")
    print(f"     Quantity: {transaction_data.get('quantity', 'N/A')} {transaction_data.get('quantityUnit', 'N/A')}")
    
    # Step 7: Validate the workflow
    print("\n7. Validating workflow...")
    validation_results = client.validate_all()
    
    if validation_results['valid']:
        print("   ✓ All entities and relationships are valid!")
    else:
        print("   ✗ Validation errors found:")
        for error in validation_results['errors']:
            print(f"     - {error}")
    
    # Step 8: Display supply chain information
    print("\n8. Supply chain traceability...")
    supply_chain = client.get_supply_chain(lumber_batch_data['traceableUnitId'])
    
    if 'error' in supply_chain:
        print(f"   Error: {supply_chain['error']}")
    else:
        tru_data = supply_chain['traceable_unit'].model_dump(by_alias=True)
        print(f"   Traceable Unit: {tru_data['traceableUnitId']}")
        print(f"   Processing operations: {len(supply_chain['processing_history'])}")
        print(f"   Transactions: {len(supply_chain['transactions'])}")
        print(f"   Parent units: {len(supply_chain['parent_units'])}")
        
        if supply_chain['parent_units']:
            parent = supply_chain['parent_units'][0]
            parent_data = parent.model_dump(by_alias=True)
            print(f"   ├─ Parent TRU: {parent_data['traceableUnitId']}")
            print(f"   ├─ Original volume: {parent_data.get('totalVolumeM3', 'N/A')} m³")
            print(f"   └─ Harvester: {parent_data.get('harvesterId', 'N/A')}")
    
    # Step 9: Export to JSON-LD
    print("\n9. Exporting to JSON-LD...")
    jsonld_output = client.export_to_jsonld()
    
    # Save to file
    output_file = Path(__file__).parent / "basic_workflow_output.jsonld"
    with open(output_file, 'w') as f:
        f.write(jsonld_output)
    
    print(f"   ✓ Exported to: {output_file}")
    total_entities = (len(client.organizations) + len(client.traceable_units) + 
                     len(client.transactions) + len(client.material_processing) + len(client.claims))
    print(f"   Entities exported: {total_entities}")
    
    print("\n" + "=" * 50)
    print("Basic workflow completed successfully!")
    print("This demonstrates:")
    print("- Dynamic schema-driven architecture")
    print("- Organization management with enum validation")
    print("- Traceable unit creation and processing")
    print("- Supply chain relationships")
    print("- Transaction recording")
    print("- Comprehensive business logic validation")
    print("- JSON-LD export/import")
    print("- Robust schema compatibility")
    print("=" * 50)


if __name__ == "__main__":
    main()