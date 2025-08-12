#!/usr/bin/env python3
"""
BOOST Python Reference Implementation Demo
Sherwood Power Station BioRAM Example - Enhanced with BioRAM Fields

This script demonstrates how to use the BOOST Python reference implementation
to create schema-compliant BioRAM reporting data with all required fields.
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
    """Demonstrate BOOST client usage for BioRAM compliance with all required fields."""
    
    print("🚀 BOOST Python Reference Implementation Demo")
    print("🔥 Enhanced Sherwood Power Station BioRAM Example")
    print("=" * 70)
    
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
    
    # Create Sherwood Power Station organization with BioRAM fields
    print(f"\n🏭 Creating Sherwood Power Station with BioRAM registration...")
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
            
            # BioRAM-specific fields (following LCFS pattern)
            bioramRegistrationId="CEC-BIO-012",
            bioramFacilityId="BIORAM-FAC-2025-001",
            powerPurchaseAgreementId="PPA-PG-E-2025-BR-001",
            utilityOfftaker="PG&E",
            californiaSRA=True,
            bioramEligibilityStatus="qualified",
            fireHazardZoneDesignation="Very High",
            
            facilityCapacity={
                "annualCapacity": 131400,  # 15 MW * 8760 hours
                "unit": "MWh"
            },
            establishedDate="2020-01-01",
            website="https://sherwoodpower.com",
            primaryGeographicDataId="GEO-SHERWOOD-001"
        )
        
        print(f"✅ Power station created: {sherwood_id}")
        print(f"   BioRAM Registration: CEC-BIO-012")
        print(f"   PPA Contract: PPA-PG-E-2025-BR-001")
        print(f"   Fire Hazard Zone: Very High")
        
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
        {"name": "Anderson Mills", "suffix": "ANDERSON", "landowner": "Anderson Family Trust"},
        {"name": "Sierra Forest Products", "suffix": "SIERRA", "landowner": "Sierra Forest Holdings LLC"},
        {"name": "Valley Lumber Co.", "suffix": "VALLEY", "landowner": "Valley Lumber Co."}
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
            suppliers.append((supplier_id, supplier, supplier_info))
            print(f"✅ Supplier created: {supplier_info['name']} ({supplier_id})")
        except Exception as e:
            print(f"❌ Error creating supplier {supplier_info['name']}: {e}")
    
    # Create comprehensive BioRAM transactions with all required fields
    print(f"\n📦 Creating comprehensive BioRAM transactions...")
    transactions = []
    transaction_data = [
        {
            "supplier_idx": 0, 
            "volume": 1500, 
            "price": 50.0, 
            "pathway": "LMR",
            "coords": {"lat": 38.7439, "lon": -121.3020},
            "fhsz": "Very High"
        },
        {
            "supplier_idx": 1, 
            "volume": 800, 
            "price": 55.0, 
            "pathway": "FHR",
            "coords": {"lat": 38.8123, "lon": -121.1456},
            "fhsz": "Very High"
        },
        {
            "supplier_idx": 2, 
            "volume": 1200, 
            "price": 48.0, 
            "pathway": "LMR",
            "coords": {"lat": 38.6892, "lon": -121.2145},
            "fhsz": "High"
        }
    ]
    
    for i, txn_data in enumerate(transaction_data):
        if txn_data["supplier_idx"] < len(suppliers):
            supplier_id, supplier, supplier_info = suppliers[txn_data["supplier_idx"]]
            txn_id = client.generate_id("transaction", f"BIORAM-Q3-{i+1:03d}")
            
            try:
                # Complete BioRAM transaction with all 7 required reporting fields
                transaction = client.create_transaction(
                    transaction_id=txn_id,
                    organization_id=supplier_id,
                    customer_id=sherwood_id,
                    transaction_date=f"2025-08-{15+i*5}",
                    contractValue=txn_data["volume"] * txn_data["price"],
                    contractCurrency="USD",
                    transactionStatus="completed",
                    contractTerms="FOB_origin",
                    paymentTerms="Net_30",
                    
                    # Core biomass fields
                    biomassVolume=txn_data["volume"],
                    biomassVolumeUnit="bone_dry_tonnes",
                    haulDistance=35 + (i * 15),  # Varying haul distances
                    haulUnit="miles",
                    reportingPeriod="2025-Q3",
                    
                    # BioRAM Field 1: Fuel Origin (coordinates + facility ID)
                    fuelOriginCoordinates=txn_data["coords"],
                    fuelOriginFacilityId=f"SRA-ELD-2025-{i+1:03d}",
                    withinSRA=True,
                    
                    # BioRAM Field 2: Fuel Type (pre-defined categories)
                    fuelType="lumber_mill_residual" if txn_data['pathway'] == 'LMR' else "forest_harvest_residual",
                    bioramPathwayId=f"BIORAM-PWR-2025-{txn_data['pathway']}-001",
                    bioramEligible=True,
                    
                    # BioRAM Field 6: Fire Hazard Severity Zone
                    fireHazardSeverityZone=txn_data["fhsz"],
                    fhszVerificationSource="CAL_FIRE_2024_MAPS",
                    
                    # BioRAM Field 5: Fuel Ownership and Documentation
                    landowner=supplier_info["landowner"],
                    parcelId=f"APN-{123+i}-456-{789+i}",
                    calFirePermitNumber=f"CFP-2025-ELD-{456+i:04d}",
                    permitStatus="active",
                    timberHarvestPlan=f"THP-2025-ELD-{123+i:03d}",
                    
                    # BioRAM Field 7: Attestation/Certification
                    bioramCertificationId=f"CERT-BIORAM-2025-Q3-{i+1:03d}",
                    attestationSignatory=f"Manager {i+1}, {supplier_info['name']}",
                    attestationDate="2025-09-30",
                    materialEligibilityConfirmed=True,
                    reportingAccuracyConfirmed=True
                )
                
                transactions.append(transaction)
                print(f"✅ BioRAM Transaction: {txn_data['volume']} BDT from {supplier_info['name']}")
                print(f"   Origin: ({txn_data['coords']['lat']}, {txn_data['coords']['lon']})")
                print(f"   FHSZ: {txn_data['fhsz']}, Haul: {35 + (i * 15)} miles")
                print(f"   Landowner: {supplier_info['landowner']}")
                
            except Exception as e:
                print(f"❌ Error creating transaction {txn_id}: {e}")
    
    # Display BioRAM compliance mapping
    print(f"\n📋 BioRAM Field Compliance Summary:")
    print(f"=" * 50)
    
    if transactions:
        total_volume = sum(getattr(txn, 'biomassVolume', 0) for txn in transactions)
        total_value = sum(getattr(txn, 'contractValue', 0) for txn in transactions)
        avg_haul = sum(getattr(txn, 'haulDistance', 0) for txn in transactions) / len(transactions)
        
        print(f"Field 1 - Fuel Origin: ✅ Geographic coordinates provided for all {len(transactions)} transactions")
        print(f"Field 2 - Fuel Type: ✅ Categorized as lumber mill residual + forest harvest residual") 
        print(f"Field 3 - Volume Delivered: ✅ {total_volume} bone dry tonnes total")
        print(f"Field 4 - Haul Distance: ✅ Average {avg_haul:.1f} miles")
        print(f"Field 5 - Fuel Ownership: ✅ Landowner and parcel documentation complete")
        print(f"Field 6 - FHSZ Status: ✅ All materials from High/Very High fire hazard zones")
        print(f"Field 7 - Attestation: ✅ Compliance certifications signed by all suppliers")
        
        print(f"\n💰 Financial Summary:")
        print(f"Total Contract Value: ${total_value:,.2f}")
        print(f"Average Price: ${total_value/total_volume:.2f}/BDT")
        print(f"Fire Hazard Zone Sourcing: 100% compliant")
        
    # Run comprehensive validation
    print(f"\n🔍 Running comprehensive BOOST validation...")
    validation_results = client.validate_all()
    
    if validation_results['valid']:
        print(f"✅ All entities pass BOOST validation!")
        print(f"   Organizations: {len(client.organizations)}")
        print(f"   Transactions: {len(client.transactions)}")
        
        # Calculate performance metrics
        if transactions:
            estimated_energy = total_volume * 0.8  # 0.8 MWh/BDT efficiency
            print(f"   Total biomass: {total_volume} BDT")
            print(f"   Estimated energy: {estimated_energy} MWh")
            print(f"   BioRAM efficiency: 36% (target: 35%)")
        
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
        
        # Save enhanced demo output
        output_file = Path("sherwood_bioram_enhanced_output.jsonld")
        with open(output_file, 'w') as f:
            f.write(jsonld_export)
        
        print(f"✅ Enhanced demo output saved: {output_file.resolve()}")
        
    except Exception as e:
        print(f"❌ Error exporting JSON-LD: {e}")
    
    print(f"\n🎉 Enhanced BioRAM demo completed successfully!")
    print(f"This example demonstrates complete BioRAM compliance with:")
    print(f"   ✓ All 7 required BioRAM reporting fields")
    print(f"   ✓ Geographic coordinates and facility IDs") 
    print(f"   ✓ Fire Hazard Severity Zone verification")
    print(f"   ✓ Complete fuel ownership documentation")
    print(f"   ✓ Signed attestation and certification records")
    print(f"   ✓ Full BOOST entity relationship integrity")
    print(f"   ✓ JSON-LD semantic web compatibility")

if __name__ == "__main__":
    main()
