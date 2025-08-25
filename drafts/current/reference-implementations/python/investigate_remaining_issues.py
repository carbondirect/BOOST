#!/usr/bin/env python3
"""
Investigate and analyze remaining schema integrity issues.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict, Counter

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

schema_dir = Path(__file__).parent.parent.parent / "schema"


def load_schema(entity_name):
    """Load validation schema for an entity."""
    schema_file = schema_dir / entity_name / "validation_schema.json"
    if schema_file.exists():
        with open(schema_file, 'r') as f:
            return json.load(f)
    return None


def analyze_missing_fk_patterns():
    """Find documented relationships that lack FK patterns in schema properties."""
    print("🔍 Analyzing Missing FK Patterns")
    print("=" * 50)
    
    missing_patterns = []
    entities = [d.name for d in schema_dir.iterdir() if d.is_dir()]
    
    for entity_name in sorted(entities):
        schema = load_schema(entity_name)
        if not schema or 'schema' not in schema:
            continue
            
        properties = schema['schema'].get('properties', {})
        relationships = schema.get('boost_metadata', {}).get('relationships', [])
        
        # Check each relationship for corresponding FK pattern
        for rel in relationships:
            field = rel.get('field', '')
            target_entity = rel.get('targetEntity', '')
            
            # Skip if field doesn't exist in properties (these are the invalid ones we already fixed)
            if field not in properties:
                continue
                
            field_def = properties[field]
            
            # Check for FK pattern
            has_pattern = 'pattern' in field_def
            
            # For array fields, check items pattern
            if field_def.get('type') == 'array' and 'items' in field_def:
                has_pattern = has_pattern or 'pattern' in field_def['items']
            
            if not has_pattern:
                missing_patterns.append({
                    'entity': entity_name,
                    'field': field,
                    'target_entity': target_entity,
                    'relationship_type': rel.get('relationshipType', ''),
                    'field_type': field_def.get('type', 'unknown')
                })
    
    print(f"Found {len(missing_patterns)} relationships with missing FK patterns:")
    for issue in missing_patterns[:10]:  # Show first 10
        print(f"  • {issue['entity']}.{issue['field']} → {issue['target_entity']} ({issue['field_type']})")
    
    return missing_patterns


def analyze_field_duplication():
    """Analyze field duplication across entities."""
    print("\n🔄 Analyzing Field Duplication")
    print("=" * 50)
    
    field_usage = defaultdict(list)
    entities = [d.name for d in schema_dir.iterdir() if d.is_dir()]
    
    for entity_name in sorted(entities):
        schema = load_schema(entity_name)
        if not schema or 'schema' not in schema:
            continue
            
        properties = schema['schema'].get('properties', {})
        
        for field_name in properties.keys():
            if field_name not in ['@context', '@type', '@id']:  # Skip JSON-LD fields
                field_usage[field_name].append(entity_name)
    
    # Find highly duplicated fields
    duplicated_fields = {field: entities for field, entities in field_usage.items() if len(entities) > 2}
    
    print(f"Found {len(duplicated_fields)} fields used in 3+ entities:")
    for field, entities in sorted(duplicated_fields.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
        print(f"  • {field}: {len(entities)} entities ({', '.join(entities[:3])}{'...' if len(entities) > 3 else ''})")
    
    return duplicated_fields


def analyze_circular_dependencies():
    """Analyze potential circular dependencies."""
    print("\n🔄 Analyzing Circular Dependencies")
    print("=" * 50)
    
    entity_relationships = defaultdict(list)
    entities = [d.name for d in schema_dir.iterdir() if d.is_dir()]
    
    for entity_name in sorted(entities):
        schema = load_schema(entity_name)
        if not schema or 'schema' not in schema:
            continue
            
        relationships = schema.get('boost_metadata', {}).get('relationships', [])
        
        for rel in relationships:
            target = rel.get('targetEntity', '')
            if target:
                entity_relationships[entity_name].append(target.lower().replace(' ', '_'))
    
    # Find potential circular references
    circular_candidates = []
    for entity, targets in entity_relationships.items():
        for target in targets:
            if target in entity_relationships and entity in entity_relationships[target]:
                pair = tuple(sorted([entity, target]))
                if pair not in circular_candidates:
                    circular_candidates.append(pair)
    
    print(f"Found {len(circular_candidates)} potential circular dependency pairs:")
    for pair in circular_candidates:
        print(f"  • {pair[0]} ↔ {pair[1]}")
    
    return circular_candidates


def analyze_primary_key_self_references():
    """Check for missing self-referential metadata for primary keys."""
    print("\n🔑 Analyzing Primary Key Self-References")
    print("=" * 50)
    
    missing_self_refs = []
    entities = [d.name for d in schema_dir.iterdir() if d.is_dir()]
    
    for entity_name in sorted(entities):
        schema = load_schema(entity_name)
        if not schema or 'schema' not in schema:
            continue
            
        # Get primary key from metadata
        primary_key = schema.get('boost_metadata', {}).get('entity', {}).get('primaryKey', '')
        
        if primary_key:
            relationships = schema.get('boost_metadata', {}).get('relationships', [])
            
            # Check if primary key has self-referential relationship
            has_self_ref = any(rel.get('field') == primary_key for rel in relationships)
            
            if not has_self_ref:
                missing_self_refs.append({
                    'entity': entity_name,
                    'primary_key': primary_key
                })
    
    print(f"Found {len(missing_self_refs)} entities missing self-referential primary key metadata:")
    for issue in missing_self_refs[:10]:  # Show first 10
        print(f"  • {issue['entity']}.{issue['primary_key']}")
    
    return missing_self_refs


def generate_fix_recommendations(missing_patterns, duplicated_fields, circular_deps, missing_self_refs):
    """Generate specific fix recommendations."""
    print("\n💡 Fix Recommendations")
    print("=" * 50)
    
    print("\n1. Missing FK Patterns (High Priority):")
    priority_fixes = [p for p in missing_patterns if p['target_entity'] in ['GeographicData', 'Organization', 'TraceableUnit']]
    for fix in priority_fixes[:5]:
        target_pattern = get_expected_pattern(fix['target_entity'])
        print(f"  • Add pattern '{target_pattern}' to {fix['entity']}.{fix['field']}")
    
    print("\n2. Field Duplication (Medium Priority):")
    critical_dups = {field: entities for field, entities in duplicated_fields.items() if len(entities) >= 5}
    for field, entities in list(critical_dups.items())[:3]:
        print(f"  • Consider normalizing '{field}' (used in {len(entities)} entities)")
    
    print("\n3. Circular Dependencies (Medium Priority):")
    for pair in circular_deps[:3]:
        print(f"  • Review relationship chain: {pair[0]} ↔ {pair[1]}")
    
    print("\n4. Self-Reference Metadata (Low Priority):")
    print(f"  • Add self-referential metadata for {len(missing_self_refs)} primary keys")


def get_expected_pattern(target_entity):
    """Get expected FK pattern for target entity."""
    patterns = {
        'GeographicData': '^GEO-[A-Z0-9-_]+$',
        'Organization': '^ORG-[A-Z0-9-_]+$', 
        'TraceableUnit': '^TRU-[A-Z0-9-_]+$',
        'Operator': '^OP-[A-Z0-9-_]+$',
        'Material': '^MAT-[A-Z0-9-_]+$',
        'Certificate': '^CERT-[A-Z0-9-_]+$',
        'Equipment': '^EQ-[A-Z0-9-_]+$'
    }
    return patterns.get(target_entity, f'^{target_entity.upper()[:3]}-[A-Z0-9-_]+$')


def main():
    """Main analysis function."""
    print("🔍 BOOST Schema Remaining Issues Investigation")
    print("=" * 60)
    
    # Run all analyses
    missing_patterns = analyze_missing_fk_patterns()
    duplicated_fields = analyze_field_duplication() 
    circular_deps = analyze_circular_dependencies()
    missing_self_refs = analyze_primary_key_self_references()
    
    # Generate recommendations
    generate_fix_recommendations(missing_patterns, duplicated_fields, circular_deps, missing_self_refs)
    
    # Summary
    print(f"\n📊 Summary:")
    print(f"  • Missing FK patterns: {len(missing_patterns)}")
    print(f"  • Duplicated fields (3+ entities): {len(duplicated_fields)}")
    print(f"  • Circular dependencies: {len(circular_deps)}")
    print(f"  • Missing self-references: {len(missing_self_refs)}")
    
    return {
        'missing_patterns': missing_patterns,
        'duplicated_fields': duplicated_fields,
        'circular_deps': circular_deps,
        'missing_self_refs': missing_self_refs
    }


if __name__ == "__main__":
    try:
        results = main()
        print(f"\n🎯 Investigation complete! Ready to apply fixes.")
    except Exception as e:
        print(f"\n❌ Investigation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)