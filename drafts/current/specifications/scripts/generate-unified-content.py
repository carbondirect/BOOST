#!/usr/bin/env python3
"""
BOOST Unified Content Generator
Generates both LaTeX and Bikeshed content from JSON schemas
Ensures perfect consistency between HTML and PDF documentation
"""

import json
import os
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional, Tuple
import argparse

class UnifiedContentGenerator:
    def __init__(self, schema_dir: str = "../schema", output_dir: str = "."):
        self.schema_dir = Path(schema_dir)
        self.output_dir = Path(output_dir)
        self.tex_dir = self.output_dir / "tex"
        self.includes_dir = self.output_dir / "includes" / "generated"
        
        self.entities = {}
        self.entity_relationships = defaultdict(list)
        
        # Thematic organization matching both formats
        self.thematic_areas = {
            'Core Traceability': ['traceable_unit', 'material_processing', 'processing_history', 'location_history', 'biometric_identifier'],
            'Organizational Foundation': ['organization', 'certificate', 'certification_body', 'certification_scheme', 'audit', 'operator'],
            'Material & Supply Chain': ['material', 'species_component', 'supplier', 'customer', 'supply_base', 'supply_base_report', 'equipment'],
            'Transaction Management': ['transaction', 'transaction_batch', 'sales_delivery_document'],
            'Measurement & Verification': ['measurement_record', 'claim', 'verification_statement', 'moisture_content'],
            'Geographic & Tracking': ['geographic_data', 'tracking_point'],
            'Compliance & Reporting': ['lcfs_pathway', 'lcfs_reporting', 'product_group', 'energy_carbon_data', 'data_reconciliation', 'mass_balance_account']
        }
    
    def load_schemas(self):
        """Load all JSON schemas from the schema directory"""
        directories_file = self.schema_dir / "directories.json"
        
        if not directories_file.exists():
            raise FileNotFoundError(f"Schema directories file not found: {directories_file}")
        
        with open(directories_file, 'r') as f:
            directories_data = json.load(f)
        
        schema_directories = directories_data.get('schema_directories', [])
        
        for entity_dir in schema_directories:
            schema_path = self.schema_dir / entity_dir / "validation_schema.json"
            dict_path = self.schema_dir / entity_dir / f"{entity_dir}_dictionary.md"
            
            if schema_path.exists():
                try:
                    with open(schema_path, 'r') as f:
                        schema_data = json.load(f)
                    
                    # Load dictionary content if available
                    dict_content = ""
                    if dict_path.exists():
                        with open(dict_path, 'r') as f:
                            dict_content = f.read()
                    
                    entity_info = self._extract_entity_info(entity_dir, schema_data, dict_content)
                    if entity_info:
                        self.entities[entity_dir] = entity_info
                        self._extract_relationships(entity_dir, entity_info)
                        
                except Exception as e:
                    print(f"Error loading schema {schema_path}: {e}")
        
        print(f"✅ Loaded {len(self.entities)} entity schemas")
    
    def _extract_entity_info(self, entity_dir: str, schema_data: dict, dict_content: str) -> Optional[Dict]:
        """Extract structured information from a JSON schema"""
        try:
            schema = schema_data.get('schema', {})
            
            return {
                'directory': entity_dir,
                'name': schema.get('title', self._format_entity_name(entity_dir)),
                'description': schema.get('description', ''),
                'properties': schema.get('properties', {}),
                'required': schema.get('required', []),
                'examples': schema.get('examples', []),
                'dictionary_content': dict_content,
                'thematic_area': self._get_thematic_area(entity_dir)
            }
        except Exception as e:
            print(f"Error extracting info for {entity_dir}: {e}")
            return None
    
    def _extract_relationships(self, entity_dir: str, entity_info: dict):
        """Extract foreign key relationships from entity properties"""
        properties = entity_info.get('properties', {})
        
        for prop_name, prop_def in properties.items():
            if prop_name.endswith('Id') and prop_name not in ['id', '@id', entity_dir + 'Id']:
                referenced_entity = prop_name[:-2]
                referenced_entity_dir = self._camel_to_snake(referenced_entity)
                
                if referenced_entity_dir in [d for dirs in self.thematic_areas.values() for d in dirs]:
                    self.entity_relationships[entity_dir].append({
                        'field': prop_name,
                        'target_entity': referenced_entity_dir,
                        'description': prop_def.get('description', '')
                    })
    
    def generate_bikeshed_content(self):
        """Generate Bikeshed include files from schemas"""
        print("\n📝 Generating Bikeshed content...")
        
        # Create output directory
        self.includes_dir.mkdir(parents=True, exist_ok=True)
        
        generated_count = 0
        
        for entity_dir, entity_info in self.entities.items():
            # Generate entity documentation include file
            include_file = self.includes_dir / f"{entity_dir}.inc.md"
            
            content = self._generate_bikeshed_entity_content(entity_dir, entity_info)
            
            with open(include_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated_count += 1
        
        # Generate thematic section includes
        for area_name, entities in self.thematic_areas.items():
            self._generate_bikeshed_thematic_section(area_name, entities)
        
        print(f"   ✅ Generated {generated_count} Bikeshed entity includes")
        print(f"   📁 Output: {self.includes_dir}")
    
    def _generate_bikeshed_entity_content(self, entity_dir: str, entity_info: dict) -> str:
        """Generate Bikeshed content for a single entity"""
        entity_name = entity_info['name']
        description = entity_info.get('description', '')
        properties = entity_info.get('properties', {})
        required = entity_info.get('required', [])
        
        # Start with entity header
        content = f"<!-- Auto-generated from {entity_dir}/validation_schema.json -->\n\n"
        
        # Add description if available
        if description:
            content += f"{description}\n\n"
        
        # Add ERD Navigator link
        entity_class = self._snake_to_pascal(entity_dir)
        content += f"**[View {entity_name} in ERD Navigator](erd-navigator/index.html?focus={entity_class})**\n\n"
        
        # Add relationships if any
        if entity_dir in self.entity_relationships:
            content += "### Relationships ### {{.unnumbered}}\n\n"
            for rel in self.entity_relationships[entity_dir]:
                target_name = self._format_entity_name(rel['target_entity'])
                content += f"- **{rel['field']}** → [[#{rel['target_entity'].replace('_', '-')}|{target_name}]]"
                if rel['description']:
                    content += f" - {rel['description']}"
                content += "\n"
            content += "\n"
        
        # Add property table
        if properties:
            content += "### Properties ### {{.unnumbered}}\n\n"
            content += "<table class=\"data\">\n"
            content += "<thead>\n<tr>\n"
            content += "<th>Field\n<th>Type\n<th>Description\n<th>Required\n"
            content += "</tr>\n</thead>\n<tbody>\n"
            
            # Sort properties: required first, then alphabetical
            sorted_props = sorted(properties.items(), 
                                key=lambda x: (x[0] not in required, x[0]))
            
            for prop_name, prop_def in sorted_props:
                prop_type = self._get_property_type(prop_def)
                prop_desc = prop_def.get('description', 'No description provided')
                is_required = "✓" if prop_name in required else ""
                
                content += "<tr>\n"
                content += f"<td><code>{prop_name}</code>\n"
                content += f"<td>{self._escape_html(prop_type)}\n"
                content += f"<td>{self._escape_html(prop_desc)}\n"
                content += f"<td>{is_required}\n"
                content += "</tr>\n"
            
            content += "</tbody>\n</table>\n"
        
        # Add dictionary content if available
        if entity_info.get('dictionary_content'):
            # Parse and include relevant parts of dictionary
            dict_lines = entity_info['dictionary_content'].split('\n')
            
            # Look for additional content sections
            in_section = False
            for line in dict_lines:
                if line.startswith('## '):
                    in_section = True
                    content += f"\n{line}\n"
                elif in_section and line.strip():
                    content += f"{line}\n"
        
        return content
    
    def _generate_bikeshed_thematic_section(self, area_name: str, entities: List[str]):
        """Generate a thematic section include file for Bikeshed"""
        filename = area_name.lower().replace(' ', '-').replace('&', 'and') + ".inc.md"
        include_file = self.includes_dir / filename
        
        content = f"<!-- Auto-generated thematic section: {area_name} -->\n\n"
        
        # Add section description based on area
        descriptions = {
            'Core Traceability': 'The foundational entities enabling end-to-end biomass tracking.',
            'Organizational Foundation': 'Entities managing organizations, certifications, and participants.',
            'Material & Supply Chain': 'Material classifications, suppliers, and supply chain management.',
            'Transaction Management': 'Commercial transactions and order fulfillment entities.',
            'Measurement & Verification': 'Quality measurements, claims, and verification entities.',
            'Geographic & Tracking': 'Location data and spatial tracking capabilities.',
            'Compliance & Reporting': 'Regulatory compliance and reporting entities.'
        }
        
        if area_name in descriptions:
            content += f"{descriptions[area_name]}\n\n"
        
        # Add entity list with links
        content += "### Entities in this section ### {{.unnumbered}}\n\n"
        for entity_dir in entities:
            if entity_dir in self.entities:
                entity_name = self.entities[entity_dir]['name']
                entity_id = entity_dir.replace('_', '-')
                content += f"- [[#{entity_id}|{entity_name}]]\n"
        
        with open(include_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def generate_latex_content(self):
        """Generate LaTeX content from schemas"""
        print("\n📝 Generating LaTeX content...")
        
        # Create output directories
        (self.tex_dir / "entities").mkdir(parents=True, exist_ok=True)
        
        generated_count = 0
        
        # Generate individual entity tables
        for entity_dir, entity_info in self.entities.items():
            tex_file = self.tex_dir / "entities" / f"{entity_dir.replace('_', '-')}-table.tex"
            
            content = self._generate_latex_entity_table(entity_dir, entity_info)
            
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated_count += 1
        
        # Generate thematic sections
        for area_name, entities in self.thematic_areas.items():
            self._generate_latex_thematic_section(area_name, entities)
        
        print(f"   ✅ Generated {generated_count} LaTeX entity tables")
        print(f"   📁 Output: {self.tex_dir}")
    
    def _generate_latex_entity_table(self, entity_dir: str, entity_info: dict) -> str:
        """Generate LaTeX entity table"""
        entity_name = entity_info['name']
        properties = entity_info.get('properties', {})
        required = entity_info.get('required', [])
        
        content = f"% {entity_name} Entity Table\n"
        content += f"% Auto-generated from {entity_dir}/validation_schema.json\n\n"
        
        content += f"\\begin{{entitytable}}{{{entity_name}}}\n"
        
        # Sort properties: required first
        sorted_props = sorted(properties.items(), 
                            key=lambda x: (x[0] not in required, x[0]))
        
        for prop_name, prop_def in sorted_props:
            prop_type = self._get_property_type_latex(prop_def)
            prop_desc = self._escape_latex(prop_def.get('description', 'No description provided'))
            
            field_cmd = "\\textbf{\\field{" if prop_name in required else "\\field{"
            content += f"{field_cmd}{prop_name}}} & {prop_type} & {prop_desc} \\\\\n"
        
        content += "\\end{entitytable}\n"
        
        return content
    
    def _generate_latex_thematic_section(self, area_name: str, entities: List[str]):
        """Generate LaTeX thematic section file"""
        filename = area_name.lower().replace(' ', '-').replace('&', 'and') + "-entities.tex"
        tex_file = self.tex_dir / filename
        
        content = f"% {area_name} Entities\n"
        content += "% Auto-generated from JSON schemas\n\n"
        
        for entity_dir in entities:
            if entity_dir in self.entities:
                entity_info = self.entities[entity_dir]
                entity_name = entity_info['name']
                entity_label = entity_dir.replace('_', '-')
                
                content += f"\n\\subsubsection{{{entity_name}}}\n"
                content += f"\\label{{sec:entity-{entity_label}}}\n\n"
                
                if entity_info.get('description'):
                    content += f"{self._escape_latex(entity_info['description'])}\n\n"
                
                # Add relationships box if any
                if entity_dir in self.entity_relationships:
                    content += "\\begin{informative}[title=Entity Relationships]\n"
                    content += "This entity references the following entities:\n"
                    content += "\\begin{itemize}\n"
                    for rel in self.entity_relationships[entity_dir]:
                        target_name = self._format_entity_name(rel['target_entity'])
                        desc = self._escape_latex(rel['description']) if rel['description'] else ''
                        content += f"    \\item \\field{{{rel['field']}}} → \\entity{{{target_name}}} ({desc})\n"
                    content += "\\end{itemize}\n"
                    content += "\\end{informative}\n\n"
                
                # Include the entity table
                table_file = f"entities/{entity_label}-table"
                content += f"\\input{{tex/{table_file}}}\n\n"
        
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Utility methods
    def _format_entity_name(self, entity_dir: str) -> str:
        """Convert snake_case directory name to Title Case"""
        return entity_dir.replace('_', ' ').title()
    
    def _snake_to_pascal(self, snake_str: str) -> str:
        """Convert snake_case to PascalCase"""
        return ''.join(word.capitalize() for word in snake_str.split('_'))
    
    def _camel_to_snake(self, camel_str: str) -> str:
        """Convert camelCase/PascalCase to snake_case"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _get_thematic_area(self, entity_dir: str) -> str:
        """Get thematic area for an entity"""
        for area, entities in self.thematic_areas.items():
            if entity_dir in entities:
                return area
        return "Other"
    
    def _get_property_type(self, prop_def: dict) -> str:
        """Extract property type for Bikeshed"""
        if 'enum' in prop_def:
            values = prop_def['enum']
            if len(values) <= 3:
                return f"enum({', '.join(str(v) for v in values)})"
            else:
                return f"enum({len(values)} values)"
        elif 'type' in prop_def:
            prop_type = prop_def['type']
            if prop_type == 'array':
                items = prop_def.get('items', {})
                item_type = items.get('type', 'any')
                return f"array&lt;{item_type}&gt;"
            elif prop_type == 'string':
                if 'format' in prop_def:
                    return f"string ({prop_def['format']})"
                elif 'pattern' in prop_def:
                    return "string (pattern)"
                return "string"
            elif prop_type == 'number':
                constraints = []
                if 'minimum' in prop_def:
                    constraints.append(f"≥{prop_def['minimum']}")
                if 'maximum' in prop_def:
                    constraints.append(f"≤{prop_def['maximum']}")
                if constraints:
                    return f"number ({', '.join(constraints)})"
                return "number"
            elif prop_type == 'object':
                return "object (structured)"
            elif isinstance(prop_type, list):
                return " | ".join(prop_type)
            return prop_type
        return "any"
    
    def _get_property_type_latex(self, prop_def: dict) -> str:
        """Extract property type for LaTeX"""
        # Similar to _get_property_type but without HTML escaping
        if 'enum' in prop_def:
            values = prop_def['enum']
            if len(values) <= 3:
                escaped_values = [self._escape_latex(str(v)) for v in values]
                return f"enum({', '.join(escaped_values)})"
            else:
                return f"enum({len(values)} values)"
        elif 'type' in prop_def:
            prop_type = prop_def['type']
            if prop_type == 'array':
                items = prop_def.get('items', {})
                item_type = items.get('type', 'any')
                return f"array<{item_type}>"
            elif prop_type == 'string':
                if 'format' in prop_def:
                    return f"string ({prop_def['format']})"
                elif 'pattern' in prop_def:
                    return "string (pattern)"
                return "string"
            elif prop_type == 'number':
                constraints = []
                if 'minimum' in prop_def:
                    constraints.append(f"≥{prop_def['minimum']}")
                if 'maximum' in prop_def:
                    constraints.append(f"≤{prop_def['maximum']}")
                if constraints:
                    return f"number ({', '.join(constraints)})"
                return "number"
            elif prop_type == 'object':
                return "object (structured)"
            elif isinstance(prop_type, list):
                return " | ".join([f"'{t}'" if t == 'null' else t for t in prop_type])
            return prop_type
        return "any"
    
    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters"""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;'))
    
    def _escape_latex(self, text: str) -> str:
        """Escape LaTeX special characters"""
        replacements = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
            '\\': r'\textbackslash{}'
        }
        result = text
        for char, replacement in replacements.items():
            result = result.replace(char, replacement)
        return result
    
    def generate_all(self):
        """Generate all content for both formats"""
        print("🚀 BOOST Unified Content Generator")
        print("=" * 60)
        
        # Load schemas
        print("\nLoading schemas...")
        self.load_schemas()
        
        # Generate content for both formats
        self.generate_bikeshed_content()
        self.generate_latex_content()
        
        # Generate summary report
        self.generate_summary_report()
        
        print("\n" + "=" * 60)
        print("✅ Unified content generation complete!")
        print("   Both HTML and PDF documentation will use identical content")
        print("   Run build scripts to generate final documentation")
    
    def generate_summary_report(self):
        """Generate a summary report of generated content"""
        report_file = self.output_dir / "build" / "generation-report.json"
        report_file.parent.mkdir(exist_ok=True)
        
        report = {
            "entities_processed": len(self.entities),
            "entities_list": sorted(self.entities.keys()),
            "bikeshed_files": len(list(self.includes_dir.glob("*.inc.md"))),
            "latex_files": len(list((self.tex_dir / "entities").glob("*.tex"))),
            "thematic_areas": {
                area: len(entities) for area, entities in self.thematic_areas.items()
            },
            "relationships_found": sum(len(rels) for rels in self.entity_relationships.values())
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Generation report saved to: {report_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate unified content for both Bikeshed and LaTeX from schemas"
    )
    parser.add_argument(
        "--schema-dir",
        default="../schema",
        help="Path to schema directory (default: ../schema)"
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory for generated content (default: current directory)"
    )
    parser.add_argument(
        "--format",
        choices=["all", "bikeshed", "latex"],
        default="all",
        help="Which format to generate (default: all)"
    )
    
    args = parser.parse_args()
    
    generator = UnifiedContentGenerator(args.schema_dir, args.output_dir)
    
    # Load schemas
    print("Loading schemas...")
    generator.load_schemas()
    
    # Generate requested format(s)
    if args.format in ["all", "bikeshed"]:
        generator.generate_bikeshed_content()
    
    if args.format in ["all", "latex"]:
        generator.generate_latex_content()
    
    # Generate summary
    generator.generate_summary_report()
    
    print("\n✅ Content generation complete!")


if __name__ == "__main__":
    main()