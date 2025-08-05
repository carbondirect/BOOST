#!/usr/bin/env python3

import sys
from pathlib import Path
from datetime import datetime

# Add BOOST Python reference implementation to path
boost_python_path = Path("../../../drafts/current/reference-implementations/python")
sys.path.insert(0, str(boost_python_path.resolve()))

from boost_client import create_client

def main():
    # Initialize with dynamic schema loading
    schema_path = str(Path("../../../drafts/current/schema").resolve())
    client = create_client(schema_path=schema_path)
    
    print("✅ BOOST client initialized")
    
    # Create mill waste supplier organization
    feedstock_org = client.create_organization(
        organization_id="ORG-MILL-SUPPLIER-001",
        organizationName="Regional Mill Waste Supplier",
        organizationType="supplier",
        contactEmail="contact@millsupplier.com",
        contactPhone="+1-555-123-4567",
        regulatedEntityType="supplier",
        operationalStatus="active"
    )
    
    # Validate organization
    org_validation = client.validate_entity(feedstock_org)
    if org_validation['valid']:
        print("✅ Feedstock supplier organization validated")
    else:
        print("❌ Organization validation errors:", org_validation['schema_errors'])
    
    # Create a transaction
    transaction = client.create_transaction(
        transaction_id="TXN-2025-Q1-001",
        organization_id="ORG-MILL-SUPPLIER-001",
        transaction_date=datetime.now().isoformat(),
        contract_value=75000.00,
        contract_currency="USD",
        transaction_status="completed",
        feedstock_type="mill_waste",
        feedstock_volume=500,
        feedstock_unit="bone_dry_tonnes",
        pathway_id="PATH-BIORAM-001"
    )
    
    # Validate transaction
    txn_validation = client.validate_entity(transaction)
    if txn_validation['valid']:
        print("✅ Transaction validated")
    else:
        print("❌ Transaction validation errors:", txn_validation['schema_errors'])
    
    # Export as JSON-LD
    jsonld_output = client.export_jsonld([feedstock_org, transaction])
    print("\n✅ Exported entities as JSON-LD")
    
    # Perform comprehensive validation
    validation_results = client.validate_all()
    if validation_results['valid']:
        print("✅ All entities passed comprehensive validation")
    else:
        print("❌ Comprehensive validation errors:", validation_results['errors'])

if __name__ == "__main__":
    main()