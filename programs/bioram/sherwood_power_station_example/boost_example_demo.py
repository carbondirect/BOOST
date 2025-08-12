#!/usr/bin/env python3
"""
BOOST Python Reference Implementation Demo
Sherwood Power Station BioRAM Example

This script demonstrates how to use the BOOST Python reference implementation
to create schema-compliant BioRAM reporting data for biomass power generation.
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
    """Demonstrate BOOST client usage for BioRAM compliance."""
    
    print("🚀 BOOST Python Reference Implementation Demo")
    print("🔥 Sherwood Power Station BioRAM Example")
    print("=" * 60)
    
    # Initialize BOOST client
    schema_path = str((boost_python_path / "../schema").resolve())
    client = create_client(schema_path=schema_path)
    
    # Get schema information
    schema_info = client.get_schema_info()
    print(f"\n📋 Schema Information:")
    print(f"Available entities: {len(schema_info['available_entities'])}")
    print(f"Entities: {', '.join(schema_info['available_entities'])}")
    
    # Show available enum values for BioRAM
    print(f"\n🔍 Dynamic Schema Introspection:")
    org_types = client.get_available_enum_values('organization', 'organizationType')
    transaction_statuses = client.get_available_enum_values('transaction', 'transactionStatus')
    print(f"Organization types: {org_types}")
    print(f"Transaction statuses: {transaction_statuses}")
    
    # Create Sherwood Power Station organization
    print(f"\n🏭 Creating Sherwood Power Station organization...")
    sherwood_id = client.generate_id("organization", "SHERWOOD")
    
    try:
        sherwood_station = client.create_organization(
            organization_id=sherwood_id,
            name="Sherwood Power Station",
            org_type="producer",
            contactEmail="operations@sherwoodpower.com",
            contactPhone="+1-916-555-0182",
            regulatedEntityType="producer",
            operationalStatus="active",
            facilityCapacity={
                "annualCapacity": 131400,  # 15 MW * 8760 hours
                "unit": "MWh"
            },
            establishedDate="2020-01-01",
            website="https://sherwoodpower.com",
            primaryGeographicDataId="GEO-SHERWOOD-001"
        )
        
        print(f"✅ Power station created: {sherwood_id}")
        
        # Validate the organization
        validation = client.validate_entity(sherwood_station)
        if validation['valid']:
            print(f"✅ Power station passes all validation rules")
        else:
            print(f"❌ Validation errors: {validation['schema_errors']} {validation['business_logic_errors']}")
        
    except Exception as e:
        print(f"❌ Error creating power station: {e}")
        return
    
    # Create biomass suppliers
    print(f"\n🌲 Creating biomass supplier organizations...")
    suppliers = []
    supplier_data = [
        {"name": "Anderson Mills", "suffix": "ANDERSON"},
        {"name": "Sierra Forest Products", "suffix": "SIERRA"},
        {"name": "Valley Lumber Co.", "suffix": "VALLEY"}
    ]
    
    for supplier_info in supplier_data:
        supplier_id = client.generate_id("organization", supplier_info["suffix"])
        try:
            supplier = client.create_organization(
                organization_id=supplier_id,
                name=supplier_info["name"],
                org_type="supplier",
                contactEmail=f"contact@{supplier_info['suffix'].lower()}.com",
                contactPhone="+1-530-555-0100",
                regulatedEntityType="not_regulated",
                operationalStatus="active",
                primaryGeographicDataId=f"GEO-{supplier_info['suffix']}-001"
            )
            suppliers.append((supplier_id, supplier))
            print(f"✅ Supplier created: {supplier_info['name']} ({supplier_id})")
        except Exception as e:
            print(f"❌ Error creating supplier {supplier_info['name']}: {e}")
    
    # Create biomass procurement transactions
    print(f"\n📦 Creating biomass procurement transactions...")
    transactions = []
    transaction_data = [
        {"supplier_idx": 0, "volume": 1500, "price": 50.0, "pathway": "LMR"},
        {"supplier_idx": 1, "volume": 800, "price": 55.0, "pathway": "FHR"},
        {"supplier_idx": 2, "volume": 1200, "price": 48.0, "pathway": "LMR"}
    ]
    
    for i, txn_data in enumerate(transaction_data):
        if txn_data["supplier_idx"] < len(suppliers):
            supplier_id, supplier = suppliers[txn_data["supplier_idx"]]
            txn_id = client.generate_id("transaction", f"Q3-{i+1:03d}")
            
            try:
                transaction = client.create_transaction(
                    transaction_id=txn_id,
                    organization_id=supplier_id,
                    customer_id=sherwood_id,
                    transaction_date="2025-08-15",
                    contractValue=txn_data["volume"] * txn_data["price"],
                    contractCurrency="USD",
                    transactionStatus="completed",
                    biomassVolume=txn_data["volume"],
                    biomassVolumeUnit="bone_dry_tonnes",
                    pathwayId=f"BIORAM-PWR-2025-{txn_data['pathway']}-001",
                    reportingPeriod="2025-Q3",
                    haulDistance=45,
                    haulUnit="miles",
                    fireHazardZoneStatus=True,
                    contractTerms="FOB_origin",
                    paymentTerms="Net_30"
                )
                
                transactions.append(transaction)
                print(f"✅ Transaction created: {txn_data['volume']} BDT from {supplier.organizationName}")
                
            except Exception as e:
                print(f"❌ Error creating transaction {txn_id}: {e}")
    
    # Create BioRAM pathway entities
    print(f"\n⚡ Creating BioRAM pathway definitions...")
    pathways = []
    pathway_data = [
        {
            "id": "BIORAM-PWR-2025-LMR-001",
            "feedstock": "lumber_mill_residual",
            "ci": 15.2,
            "efficiency": 0.36
        },
        {
            "id": "BIORAM-PWR-2025-FHR-001", 
            "feedstock": "forest_harvest_residual",
            "ci": 18.4,
            "efficiency": 0.34
        }
    ]
    
    for pathway_info in pathway_data:
        try:
            # Note: This would use client.create_bioram_pathway() if available
            print(f"✅ Pathway referenced: {pathway_info['id']} ({pathway_info['feedstock']})")
            print(f"   CI: {pathway_info['ci']} gCO2e/MJ, Efficiency: {pathway_info['efficiency']*100}%")
        except Exception as e:
            print(f"❌ Error with pathway {pathway_info['id']}: {e}")
    
    # Run comprehensive validation
    print(f"\n🔍 Running comprehensive BOOST validation...")
    validation_results = client.validate_all()
    
    if validation_results['valid']:
        print(f"✅ All entities pass BOOST validation!")
        print(f"   Organizations: {len(client.organizations)}")
        print(f"   Transactions: {len(client.transactions)}")
        
        # Calculate summary metrics
        total_biomass = sum(txn.biomassVolume for txn in transactions if hasattr(txn, 'biomassVolume'))
        estimated_energy = total_biomass * 0.8  # 0.8 MWh/BDT efficiency
        print(f"   Total biomass: {total_biomass} BDT")
        print(f"   Estimated energy: {estimated_energy} MWh")
        
    else:
        print(f"❌ Validation errors found:")
        for error in validation_results.get('errors', []):
            print(f"   - {error}")
    
    # Export to JSON-LD
    print(f"\n📤 Exporting to JSON-LD...")
    try:
        jsonld_export = client.export_to_jsonld(include_context=True)
        export_data = json.loads(jsonld_export)
        
        print(f"✅ JSON-LD export completed")
        print(f"   Entities exported: {len(export_data.get('@graph', []))}")
        print(f"   Context terms: {len(export_data.get('@context', {}))}")
        
        # Save demo output
        output_file = Path("sherwood_bioram_demo_output.jsonld")
        with open(output_file, 'w') as f:
            f.write(jsonld_export)
        
        print(f"✅ Demo output saved: {output_file.resolve()}")
        
    except Exception as e:
        print(f"❌ Error exporting JSON-LD: {e}")
    
    # Display BioRAM compliance summary
    print(f"\n🎯 BioRAM Compliance Summary:")
    print(f"=" * 40)
    print(f"Power Station: Sherwood Power Station (15 MW)")
    print(f"Reporting Period: Q3 2025")
    print(f"Biomass Suppliers: {len(suppliers)}")
    print(f"Total Transactions: {len(transactions)}")
    if transactions:
        total_volume = sum(getattr(txn, 'biomassVolume', 0) for txn in transactions)
        total_value = sum(getattr(txn, 'contractValue', 0) for txn in transactions)
        print(f"Total Biomass Volume: {total_volume} bone dry tonnes")
        print(f"Total Contract Value: ${total_value:,.2f}")
        print(f"Average Price: ${total_value/total_volume:.2f}/BDT")
        print(f"Fire Hazard Zone Sourcing: 100% (all transactions)")
    
    print(f"\n🎉 BOOST BioRAM demo completed successfully!")
    print(f"The BOOST Python reference implementation provides:")
    print(f"   ✓ Dynamic schema-driven validation for biomass power")
    print(f"   ✓ Automatic enum value checking for BioRAM compliance")
    print(f"   ✓ JSON-LD semantic web compatibility")
    print(f"   ✓ Future-proof design for schema evolution")
    print(f"   ✓ Complete biomass supply chain tracking")
    print(f"   ✓ Multi-pathway BioRAM compliance support")

if __name__ == "__main__":
    main()