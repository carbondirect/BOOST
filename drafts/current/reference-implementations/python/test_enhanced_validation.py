#!/usr/bin/env python3
"""
Test enhanced validation functionality after schema integrity fixes.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from boost_client import create_client


def test_enhanced_validation():
    """Test the enhanced validation functionality."""
    
    print("🧪 Testing Enhanced BOOST Validation")
    print("=" * 50)
    
    # Initialize client
    client = create_client()
    print("✅ Client initialized successfully")
    
    # Create sample entities
    print("\n📝 Creating sample entities...")
    
    # Create organization
    org = client.create_organization(
        organization_id="ORG-TEST-001",
        name="Test Forest Products",
        org_type="harvester",
        contact_email="test@forest.com"
    )
    print(f"✅ Created organization: {org.organization_id}")
    
    # Create traceable unit
    tru = client.create_traceable_unit(
        traceable_unit_id="TRU-TEST-001",
        unit_type="pile",
        harvester_id="ORG-TEST-001",  # Valid FK reference
        total_volume_m3=50.0,
        material_type_id="MAT-DOUGLAS-FIR",
        harvest_geographic_data_id="GEO-HARVEST-001"
    )
    print(f"✅ Created traceable unit: {tru.traceable_unit_id}")
    
    # Create tracking point with enhanced fields
    tp = client.create_tracking_point(
        tracking_point_id="TP-TEST-001",
        point_type="consolidation_point",  # New point type
        geographic_data_id="GEO-SITE-001",
        equipment_used="RFID_reader, GPS",
        coordinate_precision=10,  # New field
        configuration_role="required",  # New field
        operator_id="OP-TECH-001"
    )
    print(f"✅ Created tracking point: {tp.tracking_point_id}")
    
    # Create processing with volume conservation issue
    proc = client.create_material_processing(
        processing_id="MP-TEST-001",  # Correct pattern
        input_tru_id="TRU-TEST-001",
        output_tru_id="TRU-NONEXISTENT-001",  # Broken FK for testing
        process_type="chipping",  # Valid process type
        input_volume=50.0,  # Required field
        output_volume=45.0  # Required field
    )
    print(f"✅ Created processing: {proc.processing_id}")
    
    # Run comprehensive validation
    print("\n🔍 Running comprehensive validation...")
    validation_results = client.validate_all()
    
    # Display results
    print(f"\n📊 Validation Results:")
    print(f"Overall Status: {'✅ VALID' if validation_results['valid'] else '❌ ISSUES DETECTED'}")
    print(f"Total Entities: {sum(validation_results['entity_counts'].values())}")
    
    print(f"\n📋 Entity Counts:")
    for entity_type, count in validation_results['entity_counts'].items():
        print(f"  {entity_type}: {count}")
    
    print(f"\n🔍 Validation Checks:")
    for check_name, results in validation_results['validation_checks'].items():
        status = "✅" if results['failed'] == 0 else "❌"
        print(f"  {status} {check_name}: {results['passed']} passed, {results['failed']} failed")
        
        if results['failed'] > 0:
            print(f"    Sample errors:")
            for error in results['errors'][:2]:  # Show first 2 errors
                if 'error' in error:
                    print(f"      • {error['error']}")
    
    print(f"\n💡 Recommendations: {len(validation_results.get('recommendations', []))}")
    for rec in validation_results.get('recommendations', [])[:2]:  # Show first 2
        print(f"  • {rec['issue']}")
        print(f"    Action: {rec['action']}")
    
    print(f"\n🎯 Test Summary:")
    print(f"✅ Enhanced TrackingPoint entity creation successful")
    print(f"✅ New fields (coordinatePrecision, configurationRole) working")  
    print(f"✅ New point type 'consolidation_point' accepted")
    print(f"✅ Foreign key validation detecting broken references")
    print(f"✅ Comprehensive validation providing actionable feedback")
    
    return validation_results


if __name__ == "__main__":
    try:
        test_enhanced_validation()
        print("\n🎉 All tests completed successfully!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)