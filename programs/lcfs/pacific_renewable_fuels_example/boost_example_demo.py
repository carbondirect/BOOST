#!/usr/bin/env python3
"""
BOOST Python Reference Implementation Demo
Pacific Renewable Fuels LCFS Example

This script demonstrates how to use the BOOST Python reference implementation
to create schema-compliant LCFS reporting data.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Add BOOST Python reference implementation to path
boost_python_path = Path("../../drafts/current/reference-implementations/python")
sys.path.insert(0, str(boost_python_path.resolve()))

try:
    from boost_client import create_client
    print("✅ BOOST Python reference implementation imported successfully")
except ImportError as e:
    print(f"❌ Failed to import BOOST client: {e}")
    print("Make sure the BOOST Python reference implementation is available")
    sys.exit(1)

def main():
    """Demonstrate BOOST client usage for LCFS compliance."""
    
    print("🚀 BOOST Python Reference Implementation Demo")
    print("=" * 50)
    
    # Initialize BOOST client
    schema_path = str((boost_python_path / "../schema").resolve())
    client = create_client(schema_path=schema_path)
    
    # Get schema information
    schema_info = client.get_schema_info()
    print(f"\n📋 Schema Information:")
    print(f"Available entities: {len(schema_info['available_entities'])}")
    print(f"Entities: {', '.join(schema_info['available_entities'])}")
    
    # Show available enum values
    print(f"\n🔍 Dynamic Schema Introspection:")
    org_types = client.get_available_enum_values('organization', 'organizationType')
    fuel_categories = client.get_available_enum_values('transaction', 'fuelCategory')
    print(f"Organization types: {org_types}")
    print(f"Fuel categories: {fuel_categories}")
    
    # Create a sample organization
    print(f"\n🏢 Creating BOOST-compliant organization...")
    org_id = client.generate_id("organization", "DEMO")
    
    try:
        organization = client.create_organization(
            organization_id=org_id,
            name="Demo Renewable Fuels Corp",
            org_type="producer",
            contactEmail="demo@renewablefuels.com",
            contactPhone="+1-555-123-4567",
            regulatedEntityType="producer",
            operationalStatus="active"
        )
        
        print(f"✅ Organization created: {org_id}")
        
        # Validate the organization
        validation = client.validate_entity(organization)
        if validation['valid']:
            print(f"✅ Organization passes all validation rules")
        else:
            print(f"❌ Validation errors: {validation['schema_errors']} {validation['business_logic_errors']}")
        
    except Exception as e:
        print(f"❌ Error creating organization: {e}")
        return
    
    # Create a sample transaction
    print(f"\n💰 Creating BOOST-compliant transaction...")
    txn_id = client.generate_id("transaction", "DEMO")
    
    try:
        transaction = client.create_transaction(
            transaction_id=txn_id,
            organization_id=org_id,
            customer_id=org_id,  # Self-referential for demo
            transaction_date="2025-07-31",
            contractValue=100000.00,
            contractCurrency="USD",
            transactionStatus="completed",
            fuelVolume=30000.0,
            fuelVolumeUnit="gallons",
            fuelCategory="renewable_diesel",
            reportingPeriod="2025-Q3",
            regulatedPartyRole="producer"
        )
        
        print(f"✅ Transaction created: {txn_id}")
        
        # Validate everything
        print(f"\n🔍 Running comprehensive validation...")
        validation_results = client.validate_all()
        
        if validation_results['valid']:
            print(f"✅ All entities pass BOOST validation!")
            print(f"   Organizations: {len(client.organizations)}")
            print(f"   Transactions: {len(client.transactions)}")
        else:
            print(f"❌ Validation errors found:")
            for error in validation_results.get('errors', []):
                print(f"   - {error}")
        
        # Export to JSON-LD
        print(f"\n📤 Exporting to JSON-LD...")
        jsonld_export = client.export_to_jsonld(include_context=True)
        export_data = json.loads(jsonld_export)
        
        print(f"✅ JSON-LD export completed")
        print(f"   Entities exported: {len(export_data.get('@graph', []))}")
        print(f"   Context terms: {len(export_data.get('@context', {}))}")
        
        # Save demo output
        output_file = Path("boost_demo_output.jsonld")
        with open(output_file, 'w') as f:
            f.write(jsonld_export)
        
        print(f"✅ Demo output saved: {output_file.resolve()}")
        
    except Exception as e:
        print(f"❌ Error creating transaction: {e}")
        return
    
    print(f"\n🎉 BOOST demo completed successfully!")
    print(f"The BOOST Python reference implementation provides:")
    print(f"   ✓ Dynamic schema-driven validation")
    print(f"   ✓ Automatic enum value checking")
    print(f"   ✓ JSON-LD semantic web compatibility")
    print(f"   ✓ Future-proof design for schema evolution")

if __name__ == "__main__":
    main()