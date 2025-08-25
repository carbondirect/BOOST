#!/usr/bin/env python3
"""
Analyze field duplication patterns to determine if they're problematic or standard.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict, Counter

schema_dir = Path(__file__).parent.parent.parent / "schema"


def analyze_field_semantics():
    """Analyze if duplicated fields have consistent semantics across entities."""
    print("🔍 Analyzing Field Duplication Semantics")
    print("=" * 50)
    
    field_definitions = defaultdict(list)
    entities = [d.name for d in schema_dir.iterdir() if d.is_dir()]
    
    for entity_name in sorted(entities):
        schema_file = schema_dir / entity_name / "validation_schema.json"
        if not schema_file.exists():
            continue
            
        with open(schema_file, 'r') as f:
            schema = json.load(f)
            
        properties = schema.get('schema', {}).get('properties', {})
        
        for field_name, field_def in properties.items():
            if field_name not in ['@context', '@type', '@id']:  # Skip JSON-LD fields
                field_definitions[field_name].append({
                    'entity': entity_name,
                    'type': field_def.get('type', 'unknown'),
                    'description': field_def.get('description', ''),
                    'pattern': field_def.get('pattern', ''),
                    'enum': field_def.get('enum', [])
                })
    
    # Analyze highly duplicated fields
    problematic_fields = []
    standard_fields = []
    
    for field_name, definitions in field_definitions.items():
        if len(definitions) <= 2:  # Only analyze fields in 3+ entities
            continue
            
        # Check consistency
        types = set(d['type'] for d in definitions)
        patterns = set(d['pattern'] for d in definitions if d['pattern'])
        enums = [tuple(d['enum']) for d in definitions if d['enum']]
        
        is_consistent = True
        issues = []
        
        # Type consistency
        if len(types) > 1:
            is_consistent = False
            issues.append(f"Inconsistent types: {types}")
        
        # Pattern consistency (for same type)
        if len(patterns) > 1:
            is_consistent = False 
            issues.append(f"Inconsistent patterns: {patterns}")
        
        # Enum consistency
        if len(set(enums)) > 1:
            is_consistent = False
            issues.append(f"Inconsistent enums: {len(set(enums))} variations")
        
        field_analysis = {
            'field': field_name,
            'entity_count': len(definitions),
            'entities': [d['entity'] for d in definitions],
            'consistent': is_consistent,
            'issues': issues,
            'common_type': list(types)[0] if len(types) == 1 else 'mixed'
        }
        
        if is_consistent:
            standard_fields.append(field_analysis)
        else:
            problematic_fields.append(field_analysis)
    
    return problematic_fields, standard_fields


def categorize_duplicated_fields(problematic_fields, standard_fields):
    """Categorize field duplication by impact level."""
    print("\n📊 Field Duplication Analysis Results")
    print("=" * 50)
    
    print(f"\n❌ Problematic Fields ({len(problematic_fields)}):")
    for field in sorted(problematic_fields, key=lambda x: x['entity_count'], reverse=True):
        print(f"  • {field['field']}: {field['entity_count']} entities")
        for issue in field['issues']:
            print(f"    - {issue}")
        print(f"    - Entities: {', '.join(field['entities'][:5])}")
        print()
    
    print(f"\n✅ Consistent Standard Fields ({len(standard_fields)}):")
    
    # Categorize standard fields
    metadata_fields = []
    business_fields = []
    reference_fields = []
    
    for field in standard_fields:
        fname = field['field'].lower()
        if any(x in fname for x in ['updated', 'timestamp', 'date', 'created']):
            metadata_fields.append(field)
        elif any(x in fname for x in ['id', 'ref']):
            reference_fields.append(field)
        else:
            business_fields.append(field)
    
    print(f"\n  📅 Metadata Fields ({len(metadata_fields)}):")
    for field in sorted(metadata_fields, key=lambda x: x['entity_count'], reverse=True)[:5]:
        print(f"    • {field['field']}: {field['entity_count']} entities (standard pattern)")
    
    print(f"\n  🔗 Reference Fields ({len(reference_fields)}):")
    for field in sorted(reference_fields, key=lambda x: x['entity_count'], reverse=True)[:5]:
        print(f"    • {field['field']}: {field['entity_count']} entities (standard pattern)")
    
    print(f"\n  📋 Business Fields ({len(business_fields)}):")
    for field in sorted(business_fields, key=lambda x: x['entity_count'], reverse=True)[:5]:
        print(f"    • {field['field']}: {field['entity_count']} entities")
    
    return metadata_fields, business_fields, reference_fields


def generate_duplication_recommendations(problematic_fields, metadata_fields, business_fields):
    """Generate specific recommendations for field duplication."""
    print(f"\n💡 Duplication Recommendations")
    print("=" * 50)
    
    print("1. Problematic Fields (Need Review):")
    if problematic_fields:
        for field in problematic_fields[:3]:
            print(f"  • {field['field']}: Standardize definition across {field['entity_count']} entities")
    else:
        print("  ✅ No problematic field inconsistencies found!")
    
    print("\n2. Metadata Fields (Standard Pattern):")
    lastUpdated_count = next((f['entity_count'] for f in metadata_fields if f['field'] == 'lastUpdated'), 0)
    if lastUpdated_count > 0:
        print(f"  ✅ lastUpdated in {lastUpdated_count} entities is STANDARD and appropriate")
        print("     This follows normal database audit trail patterns")
    
    print("\n3. Reference Fields (Standard Pattern):")
    for field in sorted(metadata_fields + business_fields, key=lambda x: x['entity_count'], reverse=True)[:3]:
        if 'Id' in field['field']:
            print(f"  ✅ {field['field']} duplication is normal for FK relationships")
    
    print("\n4. Overall Assessment:")
    if not problematic_fields:
        print("  ✅ Field duplication patterns are largely appropriate and follow database design best practices")
        print("  ✅ Standard fields like 'lastUpdated', 'organizationId', 'traceableUnitId' are expected duplicates")
        print("  📋 No immediate normalization required - duplication serves valid business purposes")
    else:
        print(f"  ⚠️ {len(problematic_fields)} fields need definition standardization")


def main():
    """Main analysis function."""
    print("🔍 BOOST Field Duplication Analysis")
    print("=" * 50)
    
    problematic_fields, standard_fields = analyze_field_semantics()
    
    metadata_fields, business_fields, reference_fields = categorize_duplicated_fields(
        problematic_fields, standard_fields
    )
    
    generate_duplication_recommendations(problematic_fields, metadata_fields, business_fields)
    
    return {
        'problematic_fields': problematic_fields,
        'standard_fields': standard_fields,
        'metadata_fields': metadata_fields,
        'business_fields': business_fields
    }


if __name__ == "__main__":
    try:
        results = main()
        print(f"\n🎯 Field duplication analysis complete!")
    except Exception as e:
        print(f"\n❌ Analysis failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)