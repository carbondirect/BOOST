#!/usr/bin/env python3
"""
BOOST Schema-to-LaTeX Generator
Generates comprehensive LaTeX documentation from JSON schemas
This eliminates content duplication by using schemas as single source of truth
"""

import json
import os
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional

class BOOSTSchemaProcessor:
    def __init__(self, schema_dir: str = "../schema", output_dir: str = "tex"):
        self.schema_dir = Path(schema_dir)
        self.output_dir = Path(output_dir)
        self.entities = {}
        self.entity_relationships = defaultdict(list)
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
            
            if schema_path.exists():
                try:
                    with open(schema_path, 'r') as f:
                        schema_data = json.load(f)
                    
                    entity_info = self._extract_entity_info(entity_dir, schema_data)
                    if entity_info:
                        self.entities[entity_dir] = entity_info
                        self._extract_relationships(entity_dir, entity_info)
                        
                except Exception as e:
                    print(f"Error loading schema {schema_path}: {e}")
            else:
                print(f"Schema file not found: {schema_path}")
        
        print(f"Loaded {len(self.entities)} entity schemas")
    
    def _extract_entity_info(self, entity_dir: str, schema_data: dict) -> Optional[Dict]:
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
                'thematic_area': self._get_thematic_area(entity_dir)
            }
        except Exception as e:
            print(f"Error extracting info for {entity_dir}: {e}")
            return None
    
    def _extract_relationships(self, entity_dir: str, entity_info: dict):
        """Extract foreign key relationships from entity properties"""
        properties = entity_info.get('properties', {})
        
        for prop_name, prop_def in properties.items():
            # Look for EntityNameId pattern foreign keys
            if prop_name.endswith('Id') and prop_name != 'id' and prop_name != '@id':
                # Extract referenced entity from property name
                referenced_entity = prop_name[:-2]  # Remove 'Id' suffix
                
                # Convert to snake_case directory name
                referenced_entity_dir = self._camel_to_snake(referenced_entity)
                
                if referenced_entity_dir in [d for dirs in self.thematic_areas.values() for d in dirs]:
                    self.entity_relationships[entity_dir].append({
                        'field': prop_name,
                        'target_entity': referenced_entity_dir,
                        'description': prop_def.get('description', '')
                    })
    
    def _get_thematic_area(self, entity_dir: str) -> str:
        """Get thematic area for an entity"""
        for area, entities in self.thematic_areas.items():
            if entity_dir in entities:
                return area
        return 'Other'
    
    def _format_entity_name(self, entity_dir: str) -> str:
        """Convert entity directory name to proper title case"""
        words = entity_dir.replace('_', ' ').split()
        return ''.join(word.capitalize() for word in words)
    
    def _camel_to_snake(self, camel_str: str) -> str:
        """Convert CamelCase to snake_case"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\\1_\\2', camel_str)
        return re.sub('([a-z0-9])([A-Z])', r'\\1_\\2', s1).lower()
    
    def _format_property_type(self, prop_def: dict) -> str:
        """Format property type for LaTeX display"""
        prop_type = prop_def.get('type', 'unknown')
        
        if 'enum' in prop_def:
            enum_values = prop_def['enum']
            if len(enum_values) <= 3:
                # Escape underscores in enum values for LaTeX
                escaped_values = [str(value).replace('_', '\\_') for value in enum_values]
                return f"enum({', '.join(escaped_values)})"
            else:
                return f"enum({len(enum_values)} values)"
        elif prop_type == 'array':
            items = prop_def.get('items', {})
            item_type = items.get('type', 'unknown')
            return f"array<{item_type}>"
        elif prop_type == 'object':
            if 'properties' in prop_def:
                return "object (structured)"
            else:
                return "object"
        elif prop_type == 'number':
            if 'minimum' in prop_def or 'maximum' in prop_def:
                constraints = []
                if 'minimum' in prop_def:
                    constraints.append(f"≥{prop_def['minimum']}")
                if 'maximum' in prop_def:
                    constraints.append(f"≤{prop_def['maximum']}")
                return f"number ({', '.join(constraints)})"
            return "number"
        elif prop_type == 'string':
            if 'format' in prop_def:
                return f"string ({prop_def['format']})"
            elif 'pattern' in prop_def:
                return "string (pattern)"
            return "string"
        else:
            return prop_type
    
    def _escape_latex(self, text: str) -> str:
        """Escape special LaTeX characters"""
        if not text:
            return ""
        
        # Special case: if text contains both backslashes and underscores, use texttt
        if '\\' in text and '_' in text:
            # For complex combinations like "CAL_FIRE", wrap in texttt
            import re
            # Find patterns like WORD_WORD and wrap them in texttt
            text = re.sub(r'([A-Z_][A-Z0-9_]*)', r'\\texttt{\1}', text)
            # Now escape remaining characters normally, but skip underscore in texttt blocks
            return self._escape_latex_simple(text)
        
        # Normal escaping for other cases
        return self._escape_latex_simple(text)
    
    def _escape_latex_simple(self, text: str) -> str:
        """Simple LaTeX character escaping"""
        # LaTeX special character replacements (order matters)
        replacements = {
            '\\': '\\textbackslash{}',
            '&': '\\&',
            '%': '\\%',
            '$': '\\$',
            '#': '\\#',
            '^': '\\textasciicircum{}',
            '_': '\\_',
            '{': '\\{',
            '}': '\\}',
            '~': '\\textasciitilde{}'
        }
        
        result = text
        for char, replacement in replacements.items():
            result = result.replace(char, replacement)
        
        return result
    
    def generate_entity_table(self, entity_dir: str, entity_info: dict) -> str:
        """Generate LaTeX entity table for a single entity"""
        entity_name = entity_info['name']
        properties = entity_info.get('properties', {})
        required = entity_info.get('required', [])
        
        # Skip JSON-LD metadata properties
        skip_props = ['@context', '@type', '@id']
        
        latex_content = f"""% {entity_name} Entity Table
% Auto-generated from JSON schema

\\begin{{entitytable}}{{{entity_name}}}
"""
        
        # Sort properties: required first, then alphabetical
        sorted_props = sorted(properties.items(), key=lambda x: (x[0] not in required, x[0]))
        
        for prop_name, prop_def in sorted_props:
            if prop_name in skip_props:
                continue
                
            prop_type = self._format_property_type(prop_def)
            description = self._escape_latex(prop_def.get('description', 'No description provided'))
            
            # Truncate long descriptions
            if len(description) > 80:
                description = description[:77] + '...'
            
            # Format field name, bold if required
            field_name = f"\\field{{{prop_name}}}"
            if prop_name in required:
                field_name = f"\\textbf{{{field_name}}}"
            
            latex_content += f"{field_name} & {prop_type} & {description} \\\\\n"
        
        latex_content += "\\end{entitytable}\n"
        return latex_content
    
    def generate_entity_section(self, entity_dir: str, entity_info: dict) -> str:
        """Generate complete LaTeX section for an entity"""
        entity_name = entity_info['name']
        description = self._escape_latex(entity_info.get('description', ''))
        thematic_area = entity_info['thematic_area']
        relationships = self.entity_relationships.get(entity_dir, [])
        
        # Create section header
        section_id = entity_dir.replace('_', '-')
        latex_content = f"""
\\subsection{{{entity_name}}}
\\label{{sec:entity-{section_id}}}

{description}
"""
        
        # Add thematic area information
        area_colors = {
            'Core Traceability': 'coretraceability',
            'Organizational Foundation': 'organizational', 
            'Material & Supply Chain': 'materialsupply',
            'Transaction Management': 'transaction',
            'Measurement & Verification': 'sustainability',
            'Geographic & Tracking': 'geographic',
            'Compliance & Reporting': 'reporting'
        }
        
        area_color = area_colors.get(thematic_area, 'normative')
        
        if relationships:
            latex_content += f"""
\\begin{{informative}}[title=Entity Relationships]
This entity references the following entities:
\\begin{{itemize}}
"""
            for rel in relationships:
                target_name = self._format_entity_name(rel['target_entity'])
                latex_content += f"    \\item \\field{{{rel['field']}}} → \\entity{{{target_name}}} ({self._escape_latex(rel['description'])})\n"
            
            latex_content += """\\end{itemize}
\\end{informative}
"""
        
        # Add entity table
        latex_content += f"""
**[View {entity_name} in ERD Navigator](erd-navigator/index.html?focus={entity_name.replace(' ', '')})**

{self.generate_entity_table(entity_dir, entity_info)}
"""
        
        return latex_content
    
    def generate_all_entity_tables(self):
        """Generate all individual entity table files"""
        entities_dir = self.output_dir / "entities"
        entities_dir.mkdir(parents=True, exist_ok=True)
        
        for entity_dir, entity_info in self.entities.items():
            table_content = self.generate_entity_table(entity_dir, entity_info)
            output_file = entities_dir / f"{entity_dir.replace('_', '-')}-table.tex"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(table_content)
            
            print(f"Generated entity table: {output_file}")
    
    def generate_thematic_sections(self):
        """Generate LaTeX sections organized by thematic areas"""
        
        for area_name, entity_dirs in self.thematic_areas.items():
            area_filename = area_name.lower().replace(' ', '-').replace('&', 'and')
            output_file = self.output_dir / f"{area_filename}-entities.tex"
            
            latex_content = f"""% {area_name} Entities
% Auto-generated from JSON schemas

"""
            
            for entity_dir in entity_dirs:
                if entity_dir in self.entities:
                    entity_section = self.generate_entity_section(entity_dir, self.entities[entity_dir])
                    latex_content += entity_section + "\n"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(latex_content)
            
            print(f"Generated thematic section: {output_file}")
    
    def generate_entity_reference_appendix(self):
        """Generate comprehensive entity reference appendix"""
        output_file = self.output_dir / "entity-reference-generated.tex"
        
        latex_content = """% Complete Entity Reference Appendix
% Auto-generated from JSON schemas

\\subsection{Entity Summary Table}
\\label{sec:entity-summary-generated}

\\begin{longtable}{@{}p{0.25\\textwidth}p{0.15\\textwidth}p{0.45\\textwidth}p{0.1\\textwidth}@{}}
\\toprule
\\textbf{Entity} & \\textbf{Thematic Area} & \\textbf{Description} & \\textbf{Fields} \\\\
\\midrule
\\endfirsthead
\\toprule
\\textbf{Entity} & \\textbf{Thematic Area} & \\textbf{Description} & \\textbf{Fields} \\\\
\\midrule
\\endhead
\\bottomrule
\\endfoot
"""
        
        # Sort entities by thematic area, then by name
        sorted_entities = sorted(
            self.entities.items(),
            key=lambda x: (x[1]['thematic_area'], x[1]['name'])
        )
        
        for entity_dir, entity_info in sorted_entities:
            entity_name = entity_info['name']
            thematic_area = entity_info['thematic_area']
            description = self._escape_latex(entity_info.get('description', ''))
            
            # Truncate description for table
            if len(description) > 60:
                description = description[:57] + '...'
            
            field_count = len([p for p in entity_info.get('properties', {}).keys() 
                             if p not in ['@context', '@type', '@id']])
            
            latex_content += f"{entity_name} & {self._escape_latex(thematic_area)} & {description} & {field_count} \\\\\n"
        
        latex_content += """\\end{longtable}

\\subsection{Entity Relationship Map}
\\label{sec:entity-relationships-generated}

The following table shows all foreign key relationships between entities:

\\begin{longtable}{@{}p{0.2\\textwidth}p{0.2\\textwidth}p{0.2\\textwidth}p{0.3\\textwidth}@{}}
\\toprule
\\textbf{Source Entity} & \\textbf{Field} & \\textbf{Target Entity} & \\textbf{Description} \\\\
\\midrule
\\endfirsthead
\\toprule
\\textbf{Source Entity} & \\textbf{Field} & \\textbf{Target Entity} & \\textbf{Description} \\\\
\\midrule
\\endhead
\\bottomrule
\\endfoot
"""
        
        # Add relationship information
        for entity_dir, relationships in self.entity_relationships.items():
            if relationships:
                source_entity = self.entities[entity_dir]['name']
                for rel in relationships:
                    target_entity = self._format_entity_name(rel['target_entity'])
                    field_name = rel['field']
                    description = self._escape_latex(rel['description'])
                    
                    if len(description) > 40:
                        description = description[:37] + '...'
                    
                    latex_content += f"{source_entity} & \\field{{{field_name}}} & {target_entity} & {description} \\\\\n"
        
        latex_content += "\\end{longtable}\n"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"Generated entity reference appendix: {output_file}")
    
    def generate_all(self):
        """Generate all LaTeX content from schemas"""
        print("Loading schemas...")
        self.load_schemas()
        
        print("Generating entity tables...")
        self.generate_all_entity_tables()
        
        print("📝 Generating thematic sections...")
        self.generate_thematic_sections()
        
        print("📚 Generating entity reference appendix...")
        self.generate_entity_reference_appendix()
        
        print(f"✅ Generated LaTeX content for {len(self.entities)} entities")
        print(f"📁 Output directory: {self.output_dir}")

def main():
    """Main entry point"""
    try:
        processor = BOOSTSchemaProcessor()
        processor.generate_all()
        
        print("\n🎉 Schema-to-LaTeX generation complete!")
        print("📄 Ready to build PDF with: ./build-pdf.sh")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())