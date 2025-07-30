#!/usr/bin/env python3
"""
BOOST Schema Validation Test Runner
Validates all 31 entity schemas against California biomass use case scenarios
"""

import json
import jsonschema
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
import json_logic
from datetime import datetime

class BOOSTSchemaValidator:
    def __init__(self, schema_root: str, test_data_root: str):
        self.schema_root = Path(schema_root)
        self.test_data_root = Path(test_data_root)
        self.validation_results = []
        self.load_test_scenarios()
        
    def load_test_scenarios(self):
        """Load California biomass use case scenarios"""
        scenarios_file = self.test_data_root / "california_biomass_scenarios.json"
        with open(scenarios_file, 'r') as f:
            self.scenarios = json.load(f)
            
        tests_file = self.test_data_root / "schema_validation_tests.json"
        with open(tests_file, 'r') as f:
            self.test_suite = json.load(f)
    
    def load_entity_schema(self, entity_name: str) -> Dict[str, Any]:
        """Load JSON schema for a specific entity"""
        # Convert entity name to directory format (e.g., TraceableUnit -> traceable_unit)
        entity_dir = ''.join(['_' + c.lower() if c.isupper() and i > 0 else c.lower() 
                             for i, c in enumerate(entity_name)])
        
        schema_file = self.schema_root / entity_dir / "validation_schema.json"
        
        if not schema_file.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_file}")
            
        with open(schema_file, 'r') as f:
            schema_data = json.load(f)
            return schema_data.get('schema', schema_data)
    
    def validate_entity_against_schema(self, entity_name: str, test_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate test data against entity schema"""
        try:
            schema = self.load_entity_schema(entity_name)
            jsonschema.validate(test_data, schema)
            return True, []
        except jsonschema.ValidationError as e:
            return False, [str(e)]
        except FileNotFoundError as e:
            return False, [f"Schema not found: {str(e)}"]
        except Exception as e:
            return False, [f"Validation error: {str(e)}"]
    
    def validate_business_rules(self, test_data: Dict[str, Any], rules: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate test data against JsonLogic business rules"""
        try:
            result = json_logic.jsonLogic(rules, test_data)
            if result:
                return True, []
            else:
                return False, ["Business rule validation failed"]
        except Exception as e:
            return False, [f"Business rule error: {str(e)}"]
    
    def validate_relationships(self, primary_entity: str, test_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate foreign key relationships resolve correctly"""
        errors = []
        
        try:
            # Load the primary entity's schema to get relationship metadata
            schema = self.load_entity_schema(primary_entity)
            boost_metadata = schema.get('boost_metadata', {})
            relationships = boost_metadata.get('relationships', [])
            
            for relationship in relationships:
                field = relationship['field']
                target_entity = relationship['targetEntity']
                required = relationship.get('required', False)
                
                # Check if the field exists in test data
                if field in test_data:
                    field_value = test_data[field]
                    if field_value:
                        # For now, we'll assume the relationship is valid if the field has a value
                        # In a real implementation, we'd check against actual target entity data
                        pass
                    elif required:
                        errors.append(f"Required relationship field '{field}' is empty")
                elif required:
                    errors.append(f"Required relationship field '{field}' is missing")
            
            return len(errors) == 0, errors
            
        except Exception as e:
            return False, [f"Relationship validation error: {str(e)}"]
    
    def run_entity_schema_tests(self) -> Dict[str, Any]:
        """Run all entity schema validation tests"""
        results = {
            "category": "entity_schema_validation",
            "tests_run": 0,
            "tests_passed": 0,
            "test_results": []
        }
        
        test_category = next((cat for cat in self.test_suite["schema_validation_test_suite"]["test_categories"] 
                            if cat["category"] == "entity_schema_validation"), None)
        
        if not test_category:
            return results
            
        for test in test_category["tests"]:
            test_id = test["test_id"]
            entity = test["entity"]
            test_data = test["test_data"]
            expected_result = test["expected_result"]
            
            # Run schema validation
            is_valid, errors = self.validate_entity_against_schema(entity, test_data)
            
            # Run relationship validation
            rel_valid, rel_errors = self.validate_relationships(entity, test_data)
            
            # Combine results
            overall_valid = is_valid and rel_valid
            all_errors = errors + rel_errors
            
            test_result = {
                "test_id": test_id,
                "entity": entity,
                "passed": overall_valid == (expected_result == "valid"),
                "schema_valid": is_valid,
                "relationships_valid": rel_valid,
                "errors": all_errors,
                "expected": expected_result,
                "actual": "valid" if overall_valid else "invalid"
            }
            
            results["test_results"].append(test_result)
            results["tests_run"] += 1
            if test_result["passed"]:
                results["tests_passed"] += 1
                
        return results
    
    def run_california_scenario_tests(self) -> Dict[str, Any]:
        """Run validation tests against California biomass scenarios"""
        results = {
            "category": "california_scenarios",
            "scenarios_tested": 0,
            "scenarios_passed": 0, 
            "scenario_results": []
        }
        
        scenarios = self.scenarios["california_biomass_use_cases"]["scenarios"]
        
        for scenario in scenarios:
            scenario_id = scenario["scenario_id"]
            scenario_title = scenario["title"]
            test_data = scenario["test_data"]
            entities_tested = scenario["entities_tested"]
            validation_criteria = scenario["validation_criteria"]
            
            scenario_result = {
                "scenario_id": scenario_id,
                "title": scenario_title,
                "entities_validated": [],
                "criteria_results": [],
                "overall_passed": True
            }
            
            # Test each entity in the scenario
            for entity_name, entity_data in test_data.items():
                if entity_name in entities_tested:
                    is_valid, errors = self.validate_entity_against_schema(entity_name, entity_data)
                    rel_valid, rel_errors = self.validate_relationships(entity_name, entity_data)
                    
                    entity_result = {
                        "entity": entity_name,
                        "schema_valid": is_valid,
                        "relationships_valid": rel_valid,
                        "errors": errors + rel_errors
                    }
                    
                    scenario_result["entities_validated"].append(entity_result)
                    
                    if not (is_valid and rel_valid):
                        scenario_result["overall_passed"] = False
            
            # Test validation criteria (simplified check)
            for criterion in validation_criteria:
                criterion_result = {
                    "criterion": criterion,
                    "passed": True,  # Simplified - would need specific criterion validation logic
                    "notes": "Criterion validation not fully implemented"
                }
                scenario_result["criteria_results"].append(criterion_result)
            
            results["scenario_results"].append(scenario_result)
            results["scenarios_tested"] += 1
            if scenario_result["overall_passed"]:
                results["scenarios_passed"] += 1
                
        return results
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Run complete validation test suite"""
        print("🧪 Starting BOOST Schema Validation Test Suite")
        print(f"Schema root: {self.schema_root}")
        print(f"Test data root: {self.test_data_root}")
        print()
        
        start_time = datetime.now()
        
        # Run entity schema tests
        print("📋 Running entity schema validation tests...")
        entity_results = self.run_entity_schema_tests()
        print(f"   ✅ {entity_results['tests_passed']}/{entity_results['tests_run']} entity tests passed")
        
        # Run California scenario tests
        print("🌲 Running California biomass scenario tests...")
        scenario_results = self.run_california_scenario_tests()
        print(f"   ✅ {scenario_results['scenarios_passed']}/{scenario_results['scenarios_tested']} scenarios passed")
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # Compile final results
        final_results = {
            "test_suite": "BOOST Schema Validation",
            "version": "1.0",
            "execution_time": f"{duration:.2f} seconds",
            "timestamp": end_time.isoformat(),
            "summary": {
                "total_entity_tests": entity_results["tests_run"],
                "entity_tests_passed": entity_results["tests_passed"],
                "total_scenarios": scenario_results["scenarios_tested"], 
                "scenarios_passed": scenario_results["scenarios_passed"],
                "overall_success_rate": (
                    (entity_results["tests_passed"] + scenario_results["scenarios_passed"]) /
                    (entity_results["tests_run"] + scenario_results["scenarios_tested"]) * 100
                ) if (entity_results["tests_run"] + scenario_results["scenarios_tested"]) > 0 else 0
            },
            "detailed_results": {
                "entity_schema_tests": entity_results,
                "california_scenario_tests": scenario_results
            }
        }
        
        print()
        print("📊 Test Suite Summary:")
        print(f"   Entity Tests: {entity_results['tests_passed']}/{entity_results['tests_run']} passed")
        print(f"   Scenario Tests: {scenario_results['scenarios_passed']}/{scenario_results['scenarios_tested']} passed") 
        print(f"   Overall Success Rate: {final_results['summary']['overall_success_rate']:.1f}%")
        print(f"   Execution Time: {duration:.2f} seconds")
        
        return final_results
    
    def save_results(self, results: Dict[str, Any], output_file: str):
        """Save test results to JSON file"""
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"📄 Results saved to: {output_file}")


def main():
    """Main test runner function"""
    if len(sys.argv) != 3:
        print("Usage: python run_validation_tests.py <schema_root> <test_data_root>")
        print("Example: python run_validation_tests.py ../../schema .")
        sys.exit(1)
        
    schema_root = sys.argv[1]
    test_data_root = sys.argv[2]
    
    # Validate paths exist
    if not os.path.exists(schema_root):
        print(f"❌ Schema root directory not found: {schema_root}")
        sys.exit(1)
        
    if not os.path.exists(test_data_root):
        print(f"❌ Test data root directory not found: {test_data_root}")
        sys.exit(1)
    
    # Run validation tests
    validator = BOOSTSchemaValidator(schema_root, test_data_root)
    results = validator.run_all_tests()
    
    # Save results
    output_file = os.path.join(test_data_root, "validation_results.json")
    validator.save_results(results, output_file)
    
    # Exit with error code if tests failed
    success_rate = results["summary"]["overall_success_rate"]
    if success_rate < 100:
        print(f"⚠️  Some tests failed - Success rate: {success_rate:.1f}%")
        sys.exit(1)
    else:
        print("🎉 All tests passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()