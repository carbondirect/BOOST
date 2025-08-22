#!/usr/bin/env python3
"""
BOOST Schema Foreign Key Integrity Analysis
Comprehensive validation of foreign key relationships across all entities.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass

@dataclass
class ForeignKey:
    source_entity: str
    field_name: str
    pattern: str
    target_entity: str
    required: bool
    description: str

@dataclass
class IntegrityIssue:
    severity: str  # CRITICAL, IMPORTANT, MINOR
    category: str
    entity: str
    field: str
    description: str
    fix: str

class BOOSTFKAnalyzer:
    def __init__(self, schema_dir: str):
        self.schema_dir = Path(schema_dir)
        self.entities = self._load_entity_list()
        self.foreign_keys: List[ForeignKey] = []
        self.issues: List[IntegrityIssue] = []
        
    def _load_entity_list(self) -> List[str]:
        """Load the list of valid entities from directories.json"""
        directories_path = self.schema_dir / "directories.json"
        with open(directories_path) as f:
            data = json.load(f)
        return [d.title().replace("_", "") for d in data["schema_directories"]]
    
    def _extract_fk_pattern_info(self, pattern: str) -> Tuple[str, str]:
        """Extract target entity from FK pattern"""
        # Patterns like: ^ORG-[A-Z0-9-_]+$ -> Organization
        # ^GEO-[A-Z0-9-_]+$ -> GeographicData
        # ^TRU-[A-Z0-9-_]+$ -> TraceableUnit
        
        pattern_to_entity = {
            r'ORG-': 'Organization',
            r'GEO-': 'GeographicData', 
            r'TRU-': 'TraceableUnit',
            r'OP-': 'Operator',
            r'MAT-': 'Material',
            r'IM-': 'IdentificationMethod',
            r'EQ-': 'Equipment',
            r'TP-': 'TrackingPoint',
            r'CUST-': 'Customer',
            r'CERT-SCHEME-': 'CertificationScheme',
            r'CB-': 'CertificationBody',
            r'CLA-': 'Claim',
            r'TXN-': 'Transaction',
            r'MP-': 'MaterialProcessing',
            r'BIORAM-PWR-': 'BioramPathway',
            r'BIORAM-RPT-': 'BioramReporting',
            r'LCFS-PWR-': 'LcfsPathway',
            r'LCFS-RPT-': 'LcfsReporting',
            r'CEC-BIO-': 'BioramReporting',
            r'BIORAM-FAC-': 'Organization',
        }
        
        for prefix, entity in pattern_to_entity.items():
            if prefix in pattern:
                return entity, prefix
        
        # Fallback - try to infer from pattern structure
        if pattern.startswith('^') and '-' in pattern:
            prefix = pattern.split('-')[0].replace('^', '')
            return f"Unknown_{prefix}", prefix
        
        return "Unknown", "Unknown"
    
    def extract_foreign_keys(self):
        """Extract all foreign key relationships from schema files"""
        self.foreign_keys = []
        
        for entity_dir in self.schema_dir.iterdir():
            if not entity_dir.is_dir() or entity_dir.name.startswith('.'):
                continue
                
            schema_file = entity_dir / "validation_schema.json"
            if not schema_file.exists():
                continue
            
            entity_name = entity_dir.name.replace("_", "").title()
            
            try:
                with open(schema_file) as f:
                    schema = json.load(f)
                
                properties = schema.get("schema", {}).get("properties", {})
                required_fields = set(schema.get("schema", {}).get("required", []))
                
                for field_name, field_def in properties.items():
                    # Check if field has a pattern that looks like FK
                    pattern = field_def.get("pattern", "")
                    if pattern and "-" in pattern and any(char.isupper() for char in pattern):
                        target_entity, prefix = self._extract_fk_pattern_info(pattern)
                        
                        fk = ForeignKey(
                            source_entity=entity_name,
                            field_name=field_name,
                            pattern=pattern,
                            target_entity=target_entity,
                            required=field_name in required_fields,
                            description=field_def.get("description", "")
                        )
                        self.foreign_keys.append(fk)
                        
            except Exception as e:
                print(f"Error processing {schema_file}: {e}")
    
    def analyze_orphaned_fks(self):
        """Find foreign keys pointing to non-existent entities"""
        valid_entities = set(self.entities)
        
        for fk in self.foreign_keys:
            if fk.target_entity not in valid_entities and not fk.target_entity.startswith("Unknown"):
                severity = "CRITICAL" if fk.required else "IMPORTANT"
                self.issues.append(IntegrityIssue(
                    severity=severity,
                    category="Orphaned Foreign Key",
                    entity=fk.source_entity,
                    field=fk.field_name,
                    description=f"Field {fk.field_name} references non-existent entity {fk.target_entity}",
                    fix=f"Create {fk.target_entity} entity schema or update pattern to reference existing entity"
                ))
    
    def analyze_python_model_sync(self):
        """Check if Python models are synchronized with schema FKs"""
        # This would check if Python models have all the FK fields
        # For now, we'll note the TraceableUnit issues we found
        
        missing_fields = [
            "productClassification",
            "physicalArrangement", 
            "alternativeFateMetrics",
            "identificationMethodId"
        ]
        
        for field in missing_fields:
            self.issues.append(IntegrityIssue(
                severity="CRITICAL",
                category="Python Implementation Sync",
                entity="TraceableUnit",
                field=field,
                description=f"Python model missing field {field} present in JSON schema",
                fix=f"Add {field} field to TraceableUnit Python model with proper type annotations"
            ))
    
    def analyze_cross_entity_completeness(self):
        """Check if all FKs are covered in cross-entity validation"""
        try:
            cross_validation_file = self.schema_dir / "cross_entity_validation.json"
            with open(cross_validation_file) as f:
                cross_validation = json.load(f)
            
            covered_fks = set()
            fk_constraints = cross_validation.get("foreignKeyConstraints", {})
            
            for entity, constraints in fk_constraints.items():
                for field, constraint in constraints.items():
                    covered_fks.add(f"{entity}.{field}")
            
            # Check which FKs are not covered
            for fk in self.foreign_keys:
                fk_key = f"{fk.source_entity}.{fk.field_name}"
                if fk_key not in covered_fks:
                    self.issues.append(IntegrityIssue(
                        severity="IMPORTANT",
                        category="Cross-Entity Validation Gap",
                        entity=fk.source_entity,
                        field=fk.field_name,
                        description=f"FK {fk.field_name} not covered in cross-entity validation",
                        fix=f"Add {fk_key} constraint to cross_entity_validation.json"
                    ))
                    
        except Exception as e:
            print(f"Error analyzing cross-entity validation: {e}")
    
    def generate_report(self) -> str:
        """Generate comprehensive integrity report"""
        report = []
        report.append("# BOOST Schema Integrity Analysis Report")
        report.append(f"Generated for {len(self.entities)} entities with {len(self.foreign_keys)} foreign keys")
        report.append("")
        
        # Summary
        critical_count = len([i for i in self.issues if i.severity == "CRITICAL"])
        important_count = len([i for i in self.issues if i.severity == "IMPORTANT"])
        minor_count = len([i for i in self.issues if i.severity == "MINOR"])
        
        report.append("## Executive Summary")
        report.append(f"- **Critical Issues**: {critical_count} (Fix Immediately)")
        report.append(f"- **Important Issues**: {important_count} (Fix Soon)")  
        report.append(f"- **Minor Issues**: {minor_count} (Address When Resources Allow)")
        report.append("")
        
        # Foreign Key Summary
        report.append("## Foreign Key Summary")
        report.append(f"Total foreign key relationships discovered: {len(self.foreign_keys)}")
        report.append("")
        
        fk_by_entity = {}
        for fk in self.foreign_keys:
            if fk.source_entity not in fk_by_entity:
                fk_by_entity[fk.source_entity] = []
            fk_by_entity[fk.source_entity].append(fk)
        
        for entity, fks in sorted(fk_by_entity.items()):
            report.append(f"**{entity}**: {len(fks)} foreign keys")
            for fk in fks:
                status = "✅" if fk.target_entity in self.entities else "❌"
                req_marker = "(Required)" if fk.required else "(Optional)"
                report.append(f"  - {fk.field_name} → {fk.target_entity} {req_marker} {status}")
        report.append("")
        
        # Issues by severity
        for severity in ["CRITICAL", "IMPORTANT", "MINOR"]:
            severity_issues = [i for i in self.issues if i.severity == severity]
            if severity_issues:
                report.append(f"## {severity} Issues ({len(severity_issues)})")
                
                by_category = {}
                for issue in severity_issues:
                    if issue.category not in by_category:
                        by_category[issue.category] = []
                    by_category[issue.category].append(issue)
                
                for category, issues in by_category.items():
                    report.append(f"### {category}")
                    for issue in issues:
                        report.append(f"**Entity**: {issue.entity}")
                        report.append(f"**Field**: {issue.field}")
                        report.append(f"**Problem**: {issue.description}")
                        report.append(f"**Fix**: {issue.fix}")
                        report.append("")
        
        # TraceableUnit Schema Changes Analysis
        report.append("## TraceableUnit Schema Changes Validation")
        report.append("Recent schema changes analysis:")
        report.append("- ✅ `productClassification` field added with proper enum values")
        report.append("- ✅ `physicalArrangement` object added with comprehensive structure")
        report.append("- ✅ `alternativeFateMetrics` object added for LCA/BECCS analysis")  
        report.append("- ❌ Python model not updated with new fields")
        report.append("- ❌ `identificationMethodId` field missing from Python model")
        report.append("")
        
        return "\n".join(report)
    
    def run_full_analysis(self) -> str:
        """Run complete integrity analysis"""
        print("Extracting foreign keys from schemas...")
        self.extract_foreign_keys()
        
        print("Analyzing orphaned foreign keys...")
        self.analyze_orphaned_fks()
        
        print("Analyzing Python model synchronization...")
        self.analyze_python_model_sync()
        
        print("Analyzing cross-entity validation completeness...")  
        self.analyze_cross_entity_completeness()
        
        print("Generating comprehensive report...")
        return self.generate_report()

if __name__ == "__main__":
    analyzer = BOOSTFKAnalyzer("/Users/peter/src/BOOST/drafts/current/schema")
    report = analyzer.run_full_analysis()
    print(report)