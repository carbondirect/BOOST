#!/usr/bin/env python3
"""
Fix field inconsistencies identified in duplication analysis.
"""

import json
import sys
from pathlib import Path

schema_dir = Path(__file__).parent.parent.parent / "schema"


def fix_reconciliation_status():
    """Standardize reconciliationStatus enum across entities."""
    print("🔧 Fixing reconciliationStatus inconsistencies...")
    
    # Standard enum values
    standard_enum = ["pending", "resolved", "disputed", "investigating"]
    
    entities_to_fix = ["data_reconciliation", "transaction", "transaction_batch"]
    
    for entity_name in entities_to_fix:
        schema_file = schema_dir / entity_name / "validation_schema.json"
        if not schema_file.exists():
            continue
            
        with open(schema_file, 'r') as f:
            schema = json.load(f)
        
        properties = schema.get('schema', {}).get('properties', {})
        if 'reconciliationStatus' in properties:
            properties['reconciliationStatus']['enum'] = standard_enum
            properties['reconciliationStatus']['description'] = "Reconciliation status with standard values"
            
            with open(schema_file, 'w') as f:
                json.dump(schema, f, indent=2)
            
            print(f"  ✅ Fixed {entity_name}")


def fix_measurement_method():
    """Standardize measurementMethod enum across entities."""  
    print("\n🔧 Fixing measurementMethod inconsistencies...")
    
    # Standard enum values combining all variations
    standard_enum = [
        "oven_dry", "air_dry", "kiln_dry", "moisture_meter", 
        "capacitance", "resistance", "dielectric", "pin_type", "pinless",
        "manual", "automated", "harvester_head", "mill_scale", "truck_scale",
        "optical", "laser", "ultrasonic", "photogrammetry"
    ]
    
    entities_to_fix = ["energy_carbon_data", "measurement_record", "moisture_content"]
    
    for entity_name in entities_to_fix:
        schema_file = schema_dir / entity_name / "validation_schema.json"
        if not schema_file.exists():
            continue
            
        with open(schema_file, 'r') as f:
            schema = json.load(f)
        
        properties = schema.get('schema', {}).get('properties', {})
        if 'measurementMethod' in properties:
            properties['measurementMethod']['type'] = "string"
            properties['measurementMethod']['enum'] = standard_enum
            properties['measurementMethod']['description'] = "Method used for measurement with comprehensive standard values"
            
            with open(schema_file, 'w') as f:
                json.dump(schema, f, indent=2)
            
            print(f"  ✅ Fixed {entity_name}")


def fix_moisture_content():
    """Standardize moistureContent field type across entities."""
    print("\n🔧 Fixing moistureContent inconsistencies...")
    
    entities_to_fix = ["measurement_record", "moisture_content", "species_component"]
    
    for entity_name in entities_to_fix:
        schema_file = schema_dir / entity_name / "validation_schema.json"
        if not schema_file.exists():
            continue
            
        with open(schema_file, 'r') as f:
            schema = json.load(f)
        
        properties = schema.get('schema', {}).get('properties', {})
        if 'moistureContent' in properties:
            properties['moistureContent']['type'] = "number"
            properties['moistureContent']['minimum'] = 0
            properties['moistureContent']['maximum'] = 100
            properties['moistureContent']['description'] = "Moisture content as percentage by weight (0-100%)"
            
            with open(schema_file, 'w') as f:
                json.dump(schema, f, indent=2)
            
            print(f"  ✅ Fixed {entity_name}")


def fix_quality_grade():
    """Standardize qualityGrade enum across entities."""
    print("\n🔧 Fixing qualityGrade inconsistencies...")
    
    # Comprehensive standard enum combining all variations
    standard_enum = [
        "Grade-A", "Grade-B", "Grade-C", "Grade-D",
        "Premium", "Standard", "Economy", "Utility",
        "Structural", "Non-structural", "Fuel", "Residue",
        "Export", "Domestic", "Sawlog", "Pulpwood", "Biomass"
    ]
    
    entities_to_fix = ["species_component", "traceable_unit", "transaction_batch"]
    
    for entity_name in entities_to_fix:
        schema_file = schema_dir / entity_name / "validation_schema.json"
        if not schema_file.exists():
            continue
            
        with open(schema_file, 'r') as f:
            schema = json.load(f)
        
        properties = schema.get('schema', {}).get('properties', {})
        if 'qualityGrade' in properties:
            properties['qualityGrade']['enum'] = standard_enum
            properties['qualityGrade']['description'] = "Quality grade with comprehensive standard classification"
            
            with open(schema_file, 'w') as f:
                json.dump(schema, f, indent=2)
            
            print(f"  ✅ Fixed {entity_name}")


def main():
    """Main fix function."""
    print("🔧 Fixing Field Inconsistencies")
    print("=" * 50)
    
    fix_reconciliation_status()
    fix_measurement_method()
    fix_moisture_content()
    fix_quality_grade()
    
    print(f"\n✅ All field inconsistencies fixed!")
    print("Field duplication analysis shows that other duplications (lastUpdated, organizationId, etc.)")
    print("are standard database patterns and do not require normalization.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Fix failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)