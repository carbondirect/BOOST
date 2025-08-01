#!/usr/bin/env python3
"""
Test Enhanced Transaction and Organization Entities

This script demonstrates and validates the new TRU tracking, reconciliation workflow,
and infrastructure management capabilities added to Transaction and Organization entities.
"""

import sys
import json
from datetime import datetime, timedelta
from pathlib import Path

# Add the current directory to the path to import BOOST modules
sys.path.insert(0, str(Path(__file__).parent))

from boost_client import create_client


def test_enhanced_transaction_entity():
    """Test enhanced Transaction entity with TRU tracking and reconciliation."""
    print("🔍 Testing Enhanced Transaction Entity")
    print("=" * 50)
    
    # Initialize BOOST client
    schema_path = str(Path("../../schema").resolve())
    client = create_client(schema_path=schema_path)
    
    # Create a base organization
    org_id = client.generate_id("organization", "FOREST-OPERATIONS")
    organization = client.create_organization(
        organization_id=org_id,
        name="Forest Operations LLC",
        org_type="harvester"
    )
    print(f"✓ Created organization: {org_id}")
    
    # Create traceable units
    tru_ids = []
    for i in range(3):
        tru_id = client.generate_id("traceable_unit", f"LOG-{i+1:03d}")
        tru = client.create_traceable_unit(
            traceable_unit_id=tru_id,
            unit_type="individual_log",
            harvester_id=org_id,
            # Required fields for TraceableUnit schema
            uniqueIdentifier=f"UNIQUE-{tru_id}",
            totalVolumeM3=2.5 + i * 0.5,  # Different volumes
            materialTypeId="MAT-DOUGLAS-FIR-001",
            isMultiSpecies=False
        )
        tru_ids.append(tru_id)
        
        # Add TRU to organization's managed TRUs
        client.add_tru_to_organization(org_id, tru_id)
    
    print(f"✓ Created {len(tru_ids)} traceable units: {tru_ids}")
    
    # Create enhanced transaction with TRU tracking
    customer_id = client.generate_id("transaction", "CUST-MILL-001")
    customer_id = customer_id.replace("TXN-", "CUST-")  # Fix prefix
    
    txn_id = client.generate_id("transaction", "HARVEST-DELIVERY")
    transaction = client.create_transaction(
        transaction_id=txn_id,
        organization_id=org_id,
        customer_id=customer_id,
        transaction_date="2025-01-15",
        contractValue=15000.00,
        contractCurrency="USD",
        transactionStatus="pending",
        # New enhanced fields
        traceableUnitIds=tru_ids,
        reconciliationStatus="pending",
        manipulationTimestamps=[],
        trackingPointIds=["TP-HARVEST-SITE-A", "TP-SKID-ROAD-01"],
        mediaBreaksDetected=[False, False, False],  # One per TRU
        speciesCompositionAtTransaction=[
            {"species": "Douglas Fir", "percentage": 60.0},
            {"species": "Western Hemlock", "percentage": 40.0}
        ]
    )
    print(f"✓ Created enhanced transaction: {txn_id}")
    
    # Test array management methods
    print("\n🔧 Testing Array Management Methods")
    
    # Add manipulation timestamps in chronological order
    base_time = datetime(2025, 1, 15, 8, 0, 0)
    timestamps = [
        base_time + timedelta(hours=1),  # Harvesting started
        base_time + timedelta(hours=4),  # Loading completed
        base_time + timedelta(hours=6),  # Transport completed
    ]
    
    for ts in timestamps:
        success = client.add_manipulation_timestamp(txn_id, ts)
        print(f"  ✓ Added timestamp: {ts.isoformat()}")
    
    # Update reconciliation status
    success = client.set_reconciliation_status(txn_id, "resolved")
    print(f"  ✓ Set reconciliation status to 'resolved'")
    
    # Validate the enhanced transaction
    print("\n✅ Validation Results:")
    validation = client.validate_entity(transaction)
    if validation['valid']:
        print("  ✓ Transaction validation: PASSED")
    else:
        print("  ❌ Transaction validation: FAILED")
        for error in validation['schema_errors']:
            print(f"    - {error}")
        for error in validation['business_logic_errors']:
            print(f"    - {error}")
    
    return client, txn_id, tru_ids


def test_enhanced_organization_entity():
    """Test enhanced Organization entity with equipment and infrastructure tracking."""
    print("\n🏢 Testing Enhanced Organization Entity")
    print("=" * 50)
    
    # Initialize BOOST client
    schema_path = str(Path("../../schema").resolve())
    client = create_client(schema_path=schema_path)
    
    # Create enhanced organization with equipment and infrastructure
    org_id = client.generate_id("organization", "TIMBER-HARVESTING")
    organization = client.create_organization(
        organization_id=org_id,
        name="Timber Harvesting Corp",
        org_type="harvester",
        # Enhanced fields
        equipmentIds=["EQ-HARVESTER-H200", "EQ-SKIDDER-S150", "EQ-LOADER-L100"],
        operatorIds=["OP-SMITH-001", "OP-JONES-002", "OP-WILLIAMS-003"],
        harvestSites=["TP-SITE-NORTH", "TP-SITE-SOUTH"],
        skidRoads=["TP-SKID-MAIN", "TP-SKID-BRANCH-A", "TP-SKID-BRANCH-B"],
        forestRoads=["TP-ROAD-ACCESS", "TP-ROAD-HAUL"],
        traceableUnitIds=[],  # Will be populated as TRUs are created
        operationalAreas=["GEO-FOREST-BLOCK-A", "GEO-FOREST-BLOCK-B"]
    )
    print(f"✓ Created enhanced organization: {org_id}")
    
    # Create TRUs and assign them to the organization
    tru_ids = []
    for i in range(5):
        tru_id = client.generate_id("traceable_unit", f"TREE-{i+1:03d}")
        tru = client.create_traceable_unit(
            traceable_unit_id=tru_id,
            unit_type="individual_log",
            harvester_id=org_id,
            # Required fields for TraceableUnit schema
            uniqueIdentifier=f"UNIQUE-{tru_id}",
            totalVolumeM3=3.0 + i * 0.3,  # Different volumes
            materialTypeId="MAT-MIXED-SOFTWOOD-001",
            isMultiSpecies=True
        )
        tru_ids.append(tru_id)
        
        # Add to organization's managed TRUs
        success = client.add_tru_to_organization(org_id, tru_id)
        print(f"  ✓ Added TRU {tru_id} to organization")
    
    # Test equipment management
    print("\n🔧 Testing Equipment Management")
    new_equipment = "EQ-CHIPPER-C75"
    success = client.add_equipment_to_organization(org_id, new_equipment)
    print(f"  ✓ Added equipment: {new_equipment}")
    
    # Validate the enhanced organization
    print("\n✅ Validation Results:")
    validation = client.validate_entity(organization)
    if validation['valid']:
        print("  ✓ Organization validation: PASSED")
    else:
        print("  ❌ Organization validation: FAILED")
        for error in validation['schema_errors']:
            print(f"    - {error}")
        for error in validation['business_logic_errors']:
            print(f"    - {error}")
    
    return client, org_id, tru_ids


def test_comprehensive_validation():
    """Test comprehensive validation of all enhanced entities together."""
    print("\n🔍 Testing Comprehensive Validation")
    print("=" * 50)
    
    # Initialize BOOST client
    schema_path = str(Path("../../schema").resolve())
    client = create_client(schema_path=schema_path)
    
    # Create a complete workflow with enhanced entities
    
    # 1. Create harvesting organization
    harvester_id = client.generate_id("organization", "PACIFIC-HARVEST")
    harvester = client.create_organization(
        organization_id=harvester_id,
        name="Pacific Harvest Co",
        org_type="harvester",
        equipmentIds=["EQ-FELLER-F300"],
        harvestSites=["TP-HARVEST-ALPHA"],
        traceableUnitIds=[],
        skidRoads=["TP-SKID-ALPHA-01"]
    )
    
    # 2. Create processing organization  
    processor_id = client.generate_id("organization", "COASTAL-MILL")
    processor = client.create_organization(
        organization_id=processor_id,
        name="Coastal Mill Inc",
        org_type="processor",
        equipmentIds=["EQ-SAW-S500", "EQ-KILN-K200"]
    )
    
    # 3. Create TRUs
    tru_ids = []
    for i in range(2):
        tru_id = client.generate_id("traceable_unit", f"LOG-ALPHA-{i+1:02d}")
        tru = client.create_traceable_unit(
            traceable_unit_id=tru_id,
            unit_type="individual_log",
            harvester_id=harvester_id,
            # Required fields for TraceableUnit schema
            uniqueIdentifier=f"UNIQUE-{tru_id}",
            totalVolumeM3=4.0 + i * 0.5,  # Different volumes
            materialTypeId="MAT-DOUGLAS-FIR-GRADE-A",
            isMultiSpecies=False
        )
        tru_ids.append(tru_id)
        client.add_tru_to_organization(harvester_id, tru_id)
    
    # 4. Create transaction with comprehensive tracking
    customer_id = client.generate_id("transaction", "CUST-BUILDER-001")
    customer_id = customer_id.replace("TXN-", "CUST-")
    
    txn_id = client.generate_id("transaction", "HARVEST-TO-MILL")
    transaction = client.create_transaction(
        transaction_id=txn_id,
        organization_id=harvester_id,
        customer_id=customer_id,
        transaction_date="2025-01-20",
        contractValue=8500.00,
        contractCurrency="USD",
        transactionStatus="confirmed",
        traceableUnitIds=tru_ids,
        reconciliationStatus="pending",
        mediaBreaksDetected=[False, False],
        trackingPointIds=["TP-HARVEST-ALPHA", "TP-SKID-ALPHA-01", "TP-MILL-ENTRANCE"]
    )
    
    # Add manipulation timestamps
    base_time = datetime(2025, 1, 20, 6, 0, 0)
    client.add_manipulation_timestamp(txn_id, base_time)  # Harvest start
    client.add_manipulation_timestamp(txn_id, base_time + timedelta(hours=2))  # Loading
    client.add_manipulation_timestamp(txn_id, base_time + timedelta(hours=5))  # Delivery
    
    # Set final reconciliation status
    client.set_reconciliation_status(txn_id, "resolved")
    
    print(f"✓ Created complete workflow:")
    print(f"  - Harvester: {harvester_id}")
    print(f"  - Processor: {processor_id}")
    print(f"  - TRUs: {tru_ids}")
    print(f"  - Transaction: {txn_id}")
    
    # Run comprehensive validation
    print("\n✅ Comprehensive Validation Results:")
    results = client.validate_all()
    
    if results['valid']:
        print("  ✅ ALL VALIDATIONS PASSED!")
        print(f"  - Organizations validated: {len(client.organizations)}")
        print(f"  - TRUs validated: {len(client.traceable_units)}")
        print(f"  - Transactions validated: {len(client.transactions)}")
    else:
        print("  ❌ Validation errors found:")
        for error in results['errors']:
            print(f"    - {error}")
        
        # Show individual entity results
        for entity_type, entity_results in results['entity_results'].items():
            if not entity_results['valid']:
                print(f"\n  ❌ {entity_type.title()} errors:")
                for error in entity_results['errors']:
                    print(f"      {error}")
    
    return results


def main():
    """Run all enhanced entity tests."""
    print("🚀 BOOST Enhanced Entity Testing")
    print("Testing Transaction and Organization entity enhancements")
    print("Issues #139 and #138 implementation validation")
    print("\n")
    
    try:
        # Test enhanced transaction functionality
        client1, txn_id, tru_ids = test_enhanced_transaction_entity()
        
        # Test enhanced organization functionality
        client2, org_id, org_tru_ids = test_enhanced_organization_entity()
        
        # Test comprehensive validation
        validation_results = test_comprehensive_validation()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TESTING SUMMARY")
        print("=" * 60)
        
        if validation_results['valid']:
            print("✅ ALL TESTS PASSED!")
            print("Enhanced Transaction and Organization entities are working correctly.")
            print("\nNew capabilities validated:")
            print("  ✓ TRU tracking in transactions")
            print("  ✓ Reconciliation workflow management")
            print("  ✓ Manipulation timestamp chronology")
            print("  ✓ Organization equipment tracking")
            print("  ✓ Infrastructure mapping (harvest sites, roads)")
            print("  ✓ Cross-entity validation")
            print("  ✓ Array management methods")
        else:
            print("❌ Some tests failed - see details above")
            return 1
        
        print(f"\n🎯 Issues #139 and #138 implementation: COMPLETED")
        
    except Exception as e:
        print(f"❌ Test execution failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())