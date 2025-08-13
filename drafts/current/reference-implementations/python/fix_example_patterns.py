#!/usr/bin/env python3
"""
Fix common ID pattern issues in BOOST example files.
This script fixes the most common validation failures identified by the documentation consistency review.
"""

import json
import re
from pathlib import Path
from validation import BOOSTValidator

def fix_id_patterns(content, fixes):
    """Apply ID pattern fixes to JSON content"""
    for pattern, replacement in fixes.items():
        content = re.sub(pattern, replacement, content)
    return content

def fix_common_patterns():
    """Fix common ID pattern issues across all examples"""
    
    # Common ID pattern fixes
    id_fixes = {
        # TraceableUnit IDs - remove location descriptors
        r'"TRU-PILE-CA-Klamath-042"': '"TRU-PILE-042"',
        r'"TRU-LOG-CA-Klamath-042"': '"TRU-LOG-042"', 
        r'"TRU-PILE-MIXED-Klamath-042"': '"TRU-PILE-042"',
        
        # Geographic Data IDs - simplify
        r'"GEO-HARVEST-SITE-CA-Klamath-Ridge-04"': '"GEO-HARVEST-04"',
        
        # Transaction Batch IDs - fix pattern
        r'"TXB-KLA-042-001"': '"TB-KLA-042-001"',
        
        # Data Reconciliation IDs - fix pattern  
        r'"DR-KLA-042-RECON-001"': '"REC-KLA-042-001"',
        
        # Material Processing IDs - fix pattern
        r'"PROC-CROSSCUT-KLA-042-015"': '"MP-CROSSCUT-042-015"',
        
        # Tracking Point IDs - remove location descriptors
        r'"TP-MILL-ENTRANCE-Pacific-001"': '"TP-MILL-001"',
        
        # LCFS Reporting IDs - fix format
        r'"LCFS-RPT-2025-Q1-PACIFIC001"': '"LCFS-RPT-2025-Q1-PAC001"',
    }
    
    schema_dir = Path("../../schema")
    validator = BOOSTValidator()
    
    fixed_count = 0
    
    for entity_dir in schema_dir.iterdir():
        if entity_dir.is_dir():
            entity_name = entity_dir.name
            example_files = list(entity_dir.glob("*_example.json"))
            
            for example_file in example_files:
                try:
                    # Read original content
                    with open(example_file, 'r') as f:
                        original_content = f.read()
                        original_data = json.loads(original_content)
                    
                    # Check if it currently fails validation
                    is_valid_before, errors_before = validator.validate_entity(entity_name, original_data)
                    
                    if not is_valid_before:
                        print(f"Fixing {entity_name}...")
                        
                        # Apply fixes
                        fixed_content = fix_id_patterns(original_content, id_fixes)
                        
                        try:
                            fixed_data = json.loads(fixed_content)
                            
                            # Check if fixes helped
                            is_valid_after, errors_after = validator.validate_entity(entity_name, fixed_data)
                            
                            if len(errors_after) < len(errors_before):
                                # Write the fixed version
                                with open(example_file, 'w') as f:
                                    f.write(fixed_content)
                                
                                fixed_count += 1
                                print(f"  ✅ Improved {entity_name}: {len(errors_before)} → {len(errors_after)} errors")
                            else:
                                print(f"  ⚠️  No improvement for {entity_name}")
                        
                        except json.JSONDecodeError:
                            print(f"  ❌ JSON decode error after fixes for {entity_name}")
                    
                except Exception as e:
                    print(f"  💥 Error processing {entity_name}: {e}")
    
    print(f"\nFixed {fixed_count} example files")

if __name__ == "__main__":
    fix_common_patterns()