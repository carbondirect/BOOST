#!/usr/bin/env python3
"""
BOOST Documentation Consistency Validator
Ensures HTML (Bikeshed) and PDF (LaTeX) specifications have identical content structure
"""

import re
import os
import json
from pathlib import Path
from typing import Set, Dict, List, Tuple
import argparse
import sys

class ConsistencyValidator:
    def __init__(self, spec_dir: str = "."):
        self.spec_dir = Path(spec_dir)
        self.bikeshed_file = self.spec_dir / "boost-spec.bs"
        self.latex_file = self.spec_dir / "boost-spec.tex"
        self.schema_dir = self.spec_dir / "schema"
        
        # Results storage
        self.bikeshed_entities = set()
        self.latex_entities = set()
        self.schema_entities = set()
        self.bikeshed_sections = {}
        self.latex_sections = {}
        self.inconsistencies = []
        
    def load_schema_entities(self) -> Set[str]:
        """Load all entities from schema directory"""
        entities = set()
        directories_file = self.schema_dir / "directories.json"
        
        if directories_file.exists():
            with open(directories_file, 'r') as f:
                data = json.load(f)
                entities = set(data.get('schema_directories', []))
        
        # Also scan for validation_schema.json files as backup
        for schema_file in self.schema_dir.glob("*/validation_schema.json"):
            entity_name = schema_file.parent.name
            entities.add(entity_name)
        
        return entities
    
    def parse_bikeshed_entities(self) -> Tuple[Set[str], Dict[str, str]]:
        """Parse Bikeshed file to extract entity documentation"""
        entities = set()
        sections = {}
        
        if not self.bikeshed_file.exists():
            print(f"❌ Bikeshed file not found: {self.bikeshed_file}")
            return entities, sections
        
        with open(self.bikeshed_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern 1: Entity sections with dictionary includes
        # <pre class=include>
        # path: schema/entity_name/entity_name_dictionary.md
        # </pre>
        dict_pattern = r'path:\s*schema/([^/]+)/\1_dictionary\.md'
        for match in re.finditer(dict_pattern, content):
            entity = match.group(1)
            entities.add(entity)
        
        # Pattern 2: Section headers with IDs
        # ### EntityName ### {#entity-id}
        section_pattern = r'^###\s+([^#]+?)\s+###\s*\{#([^}]+)\}'
        for match in re.finditer(section_pattern, content, re.MULTILINE):
            section_name = match.group(1).strip()
            section_id = match.group(2).strip()
            sections[section_id] = section_name
            
            # Try to map section to entity
            # Convert section name to snake_case
            entity_name = self._title_to_snake_case(section_name)
            if entity_name in self.schema_entities:
                entities.add(entity_name)
        
        return entities, sections
    
    def parse_latex_entities(self) -> Tuple[Set[str], Dict[str, str]]:
        """Parse LaTeX file to extract entity documentation"""
        entities = set()
        sections = {}
        
        if not self.latex_file.exists():
            print(f"❌ LaTeX file not found: {self.latex_file}")
            return entities, sections
        
        with open(self.latex_file, 'r', encoding='utf-8') as f:
            main_content = f.read()
        
        # First, get all included files
        included_files = []
        input_pattern = r'\\input\{([^}]+)\}'
        for match in re.finditer(input_pattern, main_content):
            included_file = match.group(1)
            if not included_file.endswith('.tex'):
                included_file += '.tex'
            included_files.append(included_file)
        
        # Parse main file and all included files
        all_content = main_content
        for include_file in included_files:
            include_path = self.spec_dir / include_file
            if include_path.exists():
                with open(include_path, 'r', encoding='utf-8') as f:
                    all_content += "\n" + f.read()
        
        # Pattern 1: Entity table environments
        # \begin{entitytable}{Entity Name}
        entitytable_pattern = r'\\begin\{entitytable\}\{([^}]+)\}'
        for match in re.finditer(entitytable_pattern, all_content):
            entity_name = match.group(1).strip()
            # Convert to snake_case
            entity = self._title_to_snake_case(entity_name)
            entities.add(entity)
        
        # Pattern 2: Entity labels in LaTeX
        # \label{sec:entity-entity-name}
        label_pattern = r'\\label\{sec:entity-([^}]+)\}'
        for match in re.finditer(label_pattern, all_content):
            entity_label = match.group(1)
            # Convert kebab-case to snake_case
            entity = entity_label.replace('-', '_')
            entities.add(entity)
        
        # Pattern 3: Section and subsection headers
        # \section{Section Name}
        # \subsection{Subsection Name}
        # \subsubsection{Subsubsection Name}
        section_pattern = r'\\(?:sub)*section\{([^}]+)\}'
        for match in re.finditer(section_pattern, all_content):
            section_name = match.group(1).strip()
            # Store with normalized key
            key = self._normalize_section_name(section_name)
            sections[key] = section_name
            
            # Try to map to entity
            entity_name = self._title_to_snake_case(section_name)
            if entity_name in self.schema_entities:
                entities.add(entity_name)
        
        return entities, sections
    
    def _title_to_snake_case(self, title: str) -> str:
        """Convert title case to snake_case"""
        # Remove special characters and convert to snake_case
        title = re.sub(r'[^\w\s]', '', title)
        title = re.sub(r'\s+', '_', title)
        # Handle camelCase within the string
        title = re.sub(r'([a-z])([A-Z])', r'\1_\2', title)
        return title.lower()
    
    def _normalize_section_name(self, name: str) -> str:
        """Normalize section name for comparison"""
        # Remove special characters and lowercase
        normalized = re.sub(r'[^\w\s]', '', name.lower())
        normalized = re.sub(r'\s+', ' ', normalized).strip()
        return normalized
    
    def validate_consistency(self) -> bool:
        """Run all consistency checks"""
        print("🔍 BOOST Documentation Consistency Validator\n")
        print("=" * 60)
        
        # Load all entities
        print("📊 Loading entity definitions...")
        self.schema_entities = self.load_schema_entities()
        print(f"   Found {len(self.schema_entities)} entities in schema directory")
        
        # Parse Bikeshed
        print("\n📄 Parsing Bikeshed specification...")
        self.bikeshed_entities, self.bikeshed_sections = self.parse_bikeshed_entities()
        print(f"   Found {len(self.bikeshed_entities)} documented entities")
        
        # Parse LaTeX
        print("\n📄 Parsing LaTeX specification...")
        self.latex_entities, self.latex_sections = self.parse_latex_entities()
        print(f"   Found {len(self.latex_entities)} documented entities")
        
        # Run consistency checks
        print("\n" + "=" * 60)
        print("🔍 Running Consistency Checks\n")
        
        all_valid = True
        
        # Check 1: Schema coverage
        print("1️⃣ Schema Coverage Check:")
        missing_in_bikeshed = self.schema_entities - self.bikeshed_entities
        missing_in_latex = self.schema_entities - self.latex_entities
        
        if missing_in_bikeshed:
            all_valid = False
            print(f"   ❌ Missing in Bikeshed ({len(missing_in_bikeshed)}):")
            for entity in sorted(missing_in_bikeshed):
                print(f"      - {entity}")
                self.inconsistencies.append(f"Entity '{entity}' not documented in Bikeshed")
        else:
            print("   ✅ All schema entities documented in Bikeshed")
        
        if missing_in_latex:
            all_valid = False
            print(f"   ❌ Missing in LaTeX ({len(missing_in_latex)}):")
            for entity in sorted(missing_in_latex):
                print(f"      - {entity}")
                self.inconsistencies.append(f"Entity '{entity}' not documented in LaTeX")
        else:
            print("   ✅ All schema entities documented in LaTeX")
        
        # Check 2: Cross-format consistency
        print("\n2️⃣ Cross-Format Consistency Check:")
        only_in_bikeshed = self.bikeshed_entities - self.latex_entities
        only_in_latex = self.latex_entities - self.bikeshed_entities
        
        if only_in_bikeshed:
            all_valid = False
            print(f"   ❌ Only in Bikeshed ({len(only_in_bikeshed)}):")
            for entity in sorted(only_in_bikeshed):
                print(f"      - {entity}")
                self.inconsistencies.append(f"Entity '{entity}' only in Bikeshed, not in LaTeX")
        
        if only_in_latex:
            all_valid = False
            print(f"   ❌ Only in LaTeX ({len(only_in_latex)}):")
            for entity in sorted(only_in_latex):
                print(f"      - {entity}")
                self.inconsistencies.append(f"Entity '{entity}' only in LaTeX, not in Bikeshed")
        
        if not only_in_bikeshed and not only_in_latex:
            print("   ✅ Both formats have identical entity coverage")
        
        # Check 3: Extra entities (not in schema)
        print("\n3️⃣ Extra Entity Check:")
        extra_in_bikeshed = self.bikeshed_entities - self.schema_entities
        extra_in_latex = self.latex_entities - self.schema_entities
        
        if extra_in_bikeshed:
            print(f"   ⚠️  Extra in Bikeshed (not in schema):")
            for entity in sorted(extra_in_bikeshed):
                print(f"      - {entity}")
        
        if extra_in_latex:
            print(f"   ⚠️  Extra in LaTeX (not in schema):")
            for entity in sorted(extra_in_latex):
                print(f"      - {entity}")
        
        if not extra_in_bikeshed and not extra_in_latex:
            print("   ✅ No extra entities found")
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 Validation Summary\n")
        
        if all_valid:
            print("✅ Documentation is CONSISTENT across formats!")
            print(f"   - {len(self.schema_entities)} entities in schemas")
            print(f"   - {len(self.bikeshed_entities)} entities in Bikeshed")
            print(f"   - {len(self.latex_entities)} entities in LaTeX")
        else:
            print(f"❌ Found {len(self.inconsistencies)} inconsistencies!")
            print("\n📋 Required Actions:")
            for i, issue in enumerate(self.inconsistencies, 1):
                print(f"   {i}. {issue}")
        
        # Generate report file
        self.generate_report()
        
        return all_valid
    
    def generate_report(self):
        """Generate detailed consistency report"""
        report_file = self.spec_dir / "build" / "consistency-report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        report = {
            "timestamp": str(Path(self.bikeshed_file).stat().st_mtime if self.bikeshed_file.exists() else "N/A"),
            "schema_entities": sorted(list(self.schema_entities)),
            "bikeshed_entities": sorted(list(self.bikeshed_entities)),
            "latex_entities": sorted(list(self.latex_entities)),
            "inconsistencies": self.inconsistencies,
            "statistics": {
                "total_schemas": len(self.schema_entities),
                "bikeshed_documented": len(self.bikeshed_entities),
                "latex_documented": len(self.latex_entities),
                "missing_in_bikeshed": len(self.schema_entities - self.bikeshed_entities),
                "missing_in_latex": len(self.schema_entities - self.latex_entities),
                "consistency_score": self._calculate_consistency_score()
            }
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: {report_file}")
    
    def _calculate_consistency_score(self) -> float:
        """Calculate a consistency score (0-100%)"""
        if not self.schema_entities:
            return 0.0
        
        total_checks = len(self.schema_entities) * 2  # Check in both formats
        passed_checks = len(self.bikeshed_entities & self.schema_entities) + \
                       len(self.latex_entities & self.schema_entities)
        
        return round((passed_checks / total_checks) * 100, 2)


def main():
    parser = argparse.ArgumentParser(
        description="Validate consistency between Bikeshed and LaTeX documentation"
    )
    parser.add_argument(
        "--spec-dir",
        default=".",
        help="Path to specifications directory (default: current directory)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code if inconsistencies found"
    )
    
    args = parser.parse_args()
    
    validator = ConsistencyValidator(args.spec_dir)
    is_valid = validator.validate_consistency()
    
    if args.strict and not is_valid:
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()