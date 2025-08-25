#!/usr/bin/env python3
"""
Comprehensive BOOST Schema Integrity Analysis
Validates foreign key relationships, data model design, and cross-entity consistency
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict

class SchemaIntegrityAnalyzer:
    def __init__(self, schema_dir: str = "schema"):
        self.schema_dir = Path(schema_dir)
        self.entities = {}
        self.fk_patterns = {}
        self.entity_patterns = {}
        self.relationships = {}
        self.issues = {
            'critical': [],
            'important': [],
            'minor': []
        }
        
    def load_all_schemas(self):
        """Load all schema files and extract metadata"""
        directories_file = self.schema_dir / "directories.json"
        
        if directories_file.exists():
            with open(directories_file) as f:
                directories_data = json.load(f)
                entity_list = directories_data.get("schema_directories", [])
        else:
            # Fallback: scan directory
            entity_list = [d.name for d in self.schema_dir.iterdir() if d.is_dir()]
            
        print(f"Loading schemas for {len(entity_list)} entities...")
        
        for entity_dir in entity_list:
            schema_path = self.schema_dir / entity_dir / "validation_schema.json"
            if schema_path.exists():
                try:
                    with open(schema_path) as f:
                        schema_data = json.load(f)
                        self.entities[entity_dir] = schema_data
                        self._extract_entity_metadata(entity_dir, schema_data)
                except Exception as e:
                    self.add_issue('critical', f"Failed to load schema for {entity_dir}: {e}")
            else:
                self.add_issue('critical', f"Missing validation_schema.json for {entity_dir}")
                
        print(f"Successfully loaded {len(self.entities)} schemas")
        
    def _extract_entity_metadata(self, entity_name: str, schema_data: Dict):
        """Extract foreign key patterns and relationships from schema"""
        schema = schema_data.get('schema', {})
        boost_metadata = schema_data.get('boost_metadata', {})
        
        # Extract primary key pattern
        entity_info = boost_metadata.get('entity', {})
        primary_key = entity_info.get('primaryKey', '')
        
        # Get primary key pattern from schema properties
        properties = schema.get('properties', {})
        if primary_key and primary_key in properties:
            pattern_def = properties[primary_key].get('pattern', '')
            if pattern_def:
                self.entity_patterns[entity_name] = pattern_def
                
        # Extract foreign key relationships
        relationships = boost_metadata.get('relationships', [])
        self.relationships[entity_name] = relationships
        
        # Extract foreign key patterns from properties
        fk_fields = {}
        for field_name, field_def in properties.items():
            # Look for fields ending in 'Id' that have patterns
            if field_name.endswith('Id') or field_name.endswith('id'):
                pattern = field_def.get('pattern', '')
                if pattern:
                    fk_fields[field_name] = {
                        'pattern': pattern,
                        'description': field_def.get('description', ''),
                        'required': field_name in schema.get('required', [])
                    }
                    
        if fk_fields:
            self.fk_patterns[entity_name] = fk_fields
            
    def add_issue(self, severity: str, description: str, location: str = None):
        """Add an integrity issue"""
        issue = {
            'description': description,
            'location': location
        }
        self.issues[severity].append(issue)
        
    def validate_foreign_key_integrity(self):
        """Validate all foreign key references have valid targets"""
        print("\n=== VALIDATING FOREIGN KEY INTEGRITY ===")
        
        # Build map of entity patterns to entity names
        pattern_to_entity = {}
        for entity_name, pattern in self.entity_patterns.items():
            pattern_to_entity[pattern] = entity_name
            
        orphaned_fks = []
        pattern_mismatches = []
        
        for source_entity, fk_fields in self.fk_patterns.items():
            for field_name, field_info in fk_fields.items():
                fk_pattern = field_info['pattern']
                
                # Find matching target entity by pattern
                target_entity = None
                for entity_name, entity_pattern in self.entity_patterns.items():
                    if fk_pattern == entity_pattern:
                        target_entity = entity_name
                        break
                        
                if not target_entity:
                    # Check if this might be a relationship field
                    relationship_target = None
                    for rel in self.relationships.get(source_entity, []):
                        if rel['field'] == field_name:
                            relationship_target = rel['targetEntity']
                            break
                            
                    if relationship_target:
                        # Check if target entity exists
                        target_dir = self._entity_name_to_dir(relationship_target)
                        if target_dir not in self.entities:
                            self.add_issue('critical', 
                                f"Orphaned FK: {source_entity}.{field_name} references non-existent entity {relationship_target}",
                                f"schema/{source_entity}/validation_schema.json")
                        else:
                            # Check pattern consistency
                            expected_pattern = self.entity_patterns.get(target_dir, '')
                            if expected_pattern and fk_pattern != expected_pattern:
                                self.add_issue('critical',
                                    f"Pattern mismatch: {source_entity}.{field_name} pattern '{fk_pattern}' doesn't match target {relationship_target} pattern '{expected_pattern}'",
                                    f"schema/{source_entity}/validation_schema.json")
                    else:
                        self.add_issue('critical',
                            f"Orphaned FK pattern: {source_entity}.{field_name} with pattern '{fk_pattern}' has no corresponding target entity",
                            f"schema/{source_entity}/validation_schema.json")
                            
    def _entity_name_to_dir(self, entity_name: str) -> str:
        """Convert entity name to directory name"""
        # Convert PascalCase to snake_case
        return re.sub(r'(?<!^)(?=[A-Z])', '_', entity_name).lower()
        
    def validate_relationship_completeness(self):
        """Ensure all FK relationships have proper metadata"""
        print("\n=== VALIDATING RELATIONSHIP COMPLETENESS ===")
        
        for entity_name, fk_fields in self.fk_patterns.items():
            entity_relationships = {rel['field']: rel for rel in self.relationships.get(entity_name, [])}
            
            for field_name, field_info in fk_fields.items():
                if field_name not in entity_relationships:
                    self.add_issue('important',
                        f"Missing relationship metadata: {entity_name}.{field_name} has FK pattern but no boost_metadata.relationships entry",
                        f"schema/{entity_name}/validation_schema.json")
                        
        # Check for relationship metadata without corresponding FK fields
        for entity_name, relationships in self.relationships.items():
            entity_fk_fields = self.fk_patterns.get(entity_name, {})
            
            for rel in relationships:
                field_name = rel['field']
                if field_name not in entity_fk_fields:
                    # Check if field exists in schema at all
                    schema_props = self.entities[entity_name]['schema']['properties']
                    if field_name not in schema_props:
                        self.add_issue('critical',
                            f"Invalid relationship: {entity_name} relationship references non-existent field '{field_name}'",
                            f"schema/{entity_name}/validation_schema.json")
                    elif not schema_props[field_name].get('pattern'):
                        self.add_issue('important',
                            f"Relationship field missing pattern: {entity_name}.{field_name} has relationship metadata but no FK pattern",
                            f"schema/{entity_name}/validation_schema.json")
                            
    def validate_data_model_design(self):
        """Analyze data model for design violations"""
        print("\n=== VALIDATING DATA MODEL DESIGN ===")
        
        # Check for data duplication between entities
        field_usage = defaultdict(list)
        
        for entity_name, schema_data in self.entities.items():
            properties = schema_data['schema'].get('properties', {})
            for field_name in properties.keys():
                if field_name not in ['@context', '@type', '@id']:
                    field_usage[field_name].append(entity_name)
                    
        # Flag fields used in multiple entities (potential duplication)
        for field_name, entities in field_usage.items():
            if len(entities) > 1 and not field_name.endswith('Id'):
                self.add_issue('important',
                    f"Potential data duplication: Field '{field_name}' appears in multiple entities: {', '.join(entities)}",
                    f"Multiple schema files")
                    
        # Check for circular dependencies
        self._check_circular_dependencies()
        
    def _check_circular_dependencies(self):
        """Check for circular reference dependencies"""
        # Build dependency graph
        dependencies = {}
        
        for entity_name, relationships in self.relationships.items():
            deps = set()
            for rel in relationships:
                target_entity = rel['targetEntity']
                target_dir = self._entity_name_to_dir(target_entity)
                if target_dir != entity_name:  # Exclude self-references
                    deps.add(target_dir)
            dependencies[entity_name] = deps
            
        # Check for cycles using DFS
        def has_cycle(node, visited, rec_stack):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in dependencies.get(node, set()):
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True
                    
            rec_stack.remove(node)
            return False
            
        visited = set()
        for entity in dependencies:
            if entity not in visited:
                if has_cycle(entity, visited, set()):
                    self.add_issue('important',
                        f"Potential circular dependency detected involving entity: {entity}",
                        f"schema/{entity}/validation_schema.json")
                        
    def validate_pattern_consistency(self):
        """Validate naming patterns and conventions"""
        print("\n=== VALIDATING PATTERN CONSISTENCY ===")
        
        # Check ID pattern consistency
        pattern_prefixes = {}
        for entity_name, pattern in self.entity_patterns.items():
            # Extract prefix from pattern like ^ORG-[A-Z0-9-_]+$
            match = re.match(r'\^([A-Z]+)-', pattern)
            if match:
                prefix = match.group(1)
                if prefix in pattern_prefixes and pattern_prefixes[prefix] != entity_name:
                    self.add_issue('critical',
                        f"Duplicate ID prefix: Both {pattern_prefixes[prefix]} and {entity_name} use prefix '{prefix}'",
                        f"schema/{entity_name}/validation_schema.json")
                pattern_prefixes[prefix] = entity_name
                
        # Check for entities missing primary key patterns
        for entity_name in self.entities:
            if entity_name not in self.entity_patterns:
                self.add_issue('important',
                    f"Missing primary key pattern: Entity {entity_name} has no identifiable ID pattern",
                    f"schema/{entity_name}/validation_schema.json")
                    
        # Validate required JSON-LD fields
        for entity_name, schema_data in self.entities.items():
            required = schema_data['schema'].get('required', [])
            json_ld_fields = ['@context', '@type', '@id']
            
            for field in json_ld_fields:
                if field not in required:
                    self.add_issue('important',
                        f"Missing required JSON-LD field: {entity_name} should require '{field}'",
                        f"schema/{entity_name}/validation_schema.json")
                        
    def generate_summary_report(self):
        """Generate comprehensive integrity report"""
        print("\n" + "="*80)
        print("BOOST SCHEMA INTEGRITY REVIEW REPORT")
        print("="*80)
        
        print(f"\nExecutive Summary:")
        print(f"- Total entities analyzed: {len(self.entities)}")
        print(f"- Entities with FK relationships: {len([e for e in self.entities if e in self.fk_patterns])}")
        print(f"- Critical issues found: {len(self.issues['critical'])}")
        print(f"- Important issues found: {len(self.issues['important'])}")
        print(f"- Minor issues found: {len(self.issues['minor'])}")
        
        # Report issues by severity
        for severity in ['critical', 'important', 'minor']:
            issues = self.issues[severity]
            if issues:
                print(f"\n{severity.upper()} ISSUES ({len(issues)}):")
                print("-" * 40)
                for i, issue in enumerate(issues, 1):
                    print(f"{i}. {issue['description']}")
                    if issue.get('location'):
                        print(f"   Location: {issue['location']}")
                    print()
                    
    def run_full_analysis(self):
        """Run complete integrity analysis"""
        self.load_all_schemas()
        self.validate_foreign_key_integrity()
        self.validate_relationship_completeness()
        self.validate_data_model_design()
        self.validate_pattern_consistency()
        self.generate_summary_report()
        
        return self.issues

if __name__ == "__main__":
    analyzer = SchemaIntegrityAnalyzer()
    issues = analyzer.run_full_analysis()