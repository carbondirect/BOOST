"""
BOOST Tolerance Validation Reference Implementation

This module demonstrates concrete tolerance validation using the distributed
tolerance approach where tolerances are defined in the entities where they
physically manifest:
- Equipment accuracy tolerances in MeasurementRecord
- Process loss tolerances in MaterialProcessing  
- Regulatory compliance tolerances in CertificationScheme

Addresses Colin's feedback about "within tolerance for pelletizing" by providing
explicit validation logic with clear governance model.
"""

from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from decimal import Decimal
import math

@dataclass
class ToleranceValidationResult:
    """Result of tolerance validation with detailed feedback."""
    is_valid: bool
    entity_type: str
    tolerance_type: str
    actual_value: float
    expected_value: Optional[float] = None
    acceptable_range: Optional[Tuple[float, float]] = None
    deviation: Optional[float] = None
    message: str = ""


class EquipmentAccuracyValidator:
    """Validates measurements against equipment accuracy specifications."""
    
    # Equipment-specific accuracy standards (from MeasurementRecord entity)
    EQUIPMENT_ACCURACY = {
        "harvester": 0.02,      # ±2.0% for automated volume calculations
        "mill": 0.005,          # ±0.5% for scale-based measurements  
        "manual": 0.03,         # ±3.0% for manual measurements
        "optical": 0.015        # ±1.5% for 3D scanning systems
    }
    
    def validate_measurement_accuracy(self, measurement_data: Dict[str, Any]) -> ToleranceValidationResult:
        """
        Validate measurement against equipment accuracy specifications.
        
        Demonstrates how "within tolerance" becomes explicit validation
        against equipment-specific accuracy standards.
        """
        method = measurement_data.get("measurementMethod")
        measured_volume = measurement_data.get("measuredVolume", 0)
        expected_accuracy = measurement_data.get("expectedAccuracy") or self.EQUIPMENT_ACCURACY.get(method, 0.05)
        
        # Calculate acceptable range based on equipment accuracy
        tolerance_range = measured_volume * expected_accuracy
        min_acceptable = measured_volume - tolerance_range
        max_acceptable = measured_volume + tolerance_range
        
        # Check if accuracy validation was provided and verify
        accuracy_validation = measurement_data.get("accuracyValidation", {})
        provided_min = accuracy_validation.get("minAcceptable")
        provided_max = accuracy_validation.get("maxAcceptable")
        
        # Validate the accuracy validation itself
        if provided_min is not None and provided_max is not None:
            min_valid = abs(provided_min - min_acceptable) < 0.001
            max_valid = abs(provided_max - max_acceptable) < 0.001
            
            if not (min_valid and max_valid):
                return ToleranceValidationResult(
                    is_valid=False,
                    entity_type="MeasurementRecord",
                    tolerance_type="equipment_accuracy",
                    actual_value=measured_volume,
                    acceptable_range=(min_acceptable, max_acceptable),
                    message=f"Accuracy validation range incorrect. Expected: [{min_acceptable:.3f}, {max_acceptable:.3f}], Got: [{provided_min}, {provided_max}]"
                )
            
            within_tolerance = accuracy_validation.get("withinTolerance", True)
        else:
            within_tolerance = True
        
        return ToleranceValidationResult(
            is_valid=within_tolerance,
            entity_type="MeasurementRecord", 
            tolerance_type="equipment_accuracy",
            actual_value=measured_volume,
            expected_value=measured_volume,
            acceptable_range=(min_acceptable, max_acceptable),
            deviation=0,  # Self-validation for single measurement
            message=f"Measurement of {measured_volume} m³ using {method} equipment (±{expected_accuracy*100:.1f}% accuracy)"
        )


class ProcessLossValidator:
    """Validates processing losses against process-specific tolerances."""
    
    # Process-specific loss tolerances (from MaterialProcessing entity)
    PROCESS_TOLERANCES = {
        "pelletizing": {"expected": 0.02, "range": (0.015, 0.035)},    # 1.5-3.5%
        "chipping": {"expected": 0.015, "range": (0.005, 0.025)},     # 0.5-2.5%
        "transport": {"expected": 0.005, "range": (0.001, 0.01)},     # 0.1-1.0%
        "drying": {"expected": 0.10, "range": (0.05, 0.15)},          # 5-15% (mass loss)
        "debarking": {"expected": 0.08, "range": (0.05, 0.12)},       # 5-12%
        "sizing": {"expected": 0.015, "range": (0.005, 0.025)}        # 0.5-2.5%
    }
    
    def validate_process_loss(self, processing_data: Dict[str, Any]) -> ToleranceValidationResult:
        """
        Validate processing loss against process-specific tolerances.
        
        This directly addresses Colin's "within tolerance for pelletizing" question
        with explicit validation logic and clear tolerance definitions.
        """
        process_type = processing_data.get("processType")
        input_volume = processing_data.get("inputVolume", 0)
        output_volume = processing_data.get("outputVolume", 0) 
        volume_loss = processing_data.get("volumeLoss", 0)
        
        if input_volume == 0:
            return ToleranceValidationResult(
                is_valid=False,
                entity_type="MaterialProcessing",
                tolerance_type="process_loss",
                actual_value=0,
                message="Invalid input volume: cannot be zero"
            )
        
        # Calculate actual loss rate
        actual_loss_rate = volume_loss / input_volume
        
        # Get process-specific tolerances
        tolerances = self.PROCESS_TOLERANCES.get(process_type)
        if not tolerances:
            return ToleranceValidationResult(
                is_valid=False,
                entity_type="MaterialProcessing", 
                tolerance_type="process_loss",
                actual_value=actual_loss_rate,
                message=f"No tolerance specification found for process type: {process_type}"
            )
        
        expected_loss = tolerances["expected"]
        min_acceptable, max_acceptable = tolerances["range"]
        
        # Check if loss is within acceptable range
        within_tolerance = min_acceptable <= actual_loss_rate <= max_acceptable
        deviation = actual_loss_rate - expected_loss
        
        # Verify tolerance validation if provided
        tolerance_validation = processing_data.get("toleranceValidation", {})
        if tolerance_validation:
            provided_actual = tolerance_validation.get("actualLossRate")
            provided_within = tolerance_validation.get("withinTolerance")
            provided_deviation = tolerance_validation.get("deviationFromExpected")
            
            # Validate the validation data itself
            if provided_actual is not None and abs(provided_actual - actual_loss_rate) > 0.001:
                return ToleranceValidationResult(
                    is_valid=False,
                    entity_type="MaterialProcessing",
                    tolerance_type="process_loss", 
                    actual_value=actual_loss_rate,
                    message=f"Tolerance validation actualLossRate incorrect: expected {actual_loss_rate:.4f}, got {provided_actual}"
                )
            
            if provided_within is not None and provided_within != within_tolerance:
                return ToleranceValidationResult(
                    is_valid=False,
                    entity_type="MaterialProcessing",
                    tolerance_type="process_loss",
                    actual_value=actual_loss_rate,
                    message=f"Tolerance validation withinTolerance incorrect: expected {within_tolerance}, got {provided_within}"
                )
        
        return ToleranceValidationResult(
            is_valid=within_tolerance,
            entity_type="MaterialProcessing",
            tolerance_type="process_loss", 
            actual_value=actual_loss_rate,
            expected_value=expected_loss,
            acceptable_range=(min_acceptable, max_acceptable),
            deviation=deviation,
            message=f"{process_type} loss of {actual_loss_rate*100:.2f}% {'within' if within_tolerance else 'exceeds'} acceptable range {min_acceptable*100:.1f}%-{max_acceptable*100:.1f}%"
        )


class RegulatoryComplianceValidator:
    """Validates regulatory compliance tolerances from CertificationScheme."""
    
    # Regulatory compliance tolerances (from CertificationScheme entity)
    REGULATORY_TOLERANCES = {
        "CARB_LCFS": {"volume_deviation": 0.005, "mass_deviation": 0.005},  # ±0.5%
        "EU_RED": {"volume_deviation": 0.01, "mass_deviation": 0.01},       # ±1.0%
        "RFS2": {"volume_deviation": 0.0075, "mass_deviation": 0.0075}      # ±0.75%
    }
    
    def validate_regulatory_compliance(self, certification_data: Dict[str, Any], 
                                     measurement_chain: List[Dict[str, Any]]) -> ToleranceValidationResult:
        """
        Validate regulatory compliance tolerance for volume/mass conservation.
        
        Only handles regulatory reporting tolerances - equipment and process tolerances
        are handled by their respective validators.
        """
        scheme_name = certification_data.get("schemeName", "")
        compliance_tolerances = certification_data.get("complianceTolerances", {})
        
        # Extract or infer regulatory standard
        reporting_standard = compliance_tolerances.get("reportingStandard")
        if not reporting_standard:
            if "CARB" in scheme_name or "LCFS" in scheme_name:
                reporting_standard = "CARB_LCFS"
            elif "RED" in scheme_name or "EU" in scheme_name:
                reporting_standard = "EU_RED"
            elif "RFS" in scheme_name:
                reporting_standard = "RFS2"
            else:
                return ToleranceValidationResult(
                    is_valid=False,
                    entity_type="CertificationScheme",
                    tolerance_type="regulatory_compliance", 
                    actual_value=0,
                    message=f"Cannot determine regulatory standard for scheme: {scheme_name}"
                )
        
        # Get regulatory tolerance specifications
        reg_tolerances = self.REGULATORY_TOLERANCES.get(reporting_standard)
        if not reg_tolerances:
            return ToleranceValidationResult(
                is_valid=False,
                entity_type="CertificationScheme",
                tolerance_type="regulatory_compliance",
                actual_value=0, 
                message=f"No regulatory tolerances defined for standard: {reporting_standard}"
            )
        
        # Calculate end-to-end volume conservation across measurement chain
        if not measurement_chain:
            return ToleranceValidationResult(
                is_valid=False,
                entity_type="CertificationScheme", 
                tolerance_type="regulatory_compliance",
                actual_value=0,
                message="No measurement chain provided for compliance validation"
            )
        
        initial_volume = measurement_chain[0].get("inputVolume", 0)
        final_volume = measurement_chain[-1].get("outputVolume", 0)
        
        if initial_volume == 0:
            return ToleranceValidationResult(
                is_valid=False,
                entity_type="CertificationScheme",
                tolerance_type="regulatory_compliance", 
                actual_value=0,
                message="Invalid initial volume for compliance calculation"
            )
        
        # Calculate total volume conservation deviation
        volume_deviation = abs(1 - (final_volume / initial_volume))
        max_allowed_deviation = reg_tolerances["volume_deviation"]
        
        within_compliance = volume_deviation <= max_allowed_deviation
        
        return ToleranceValidationResult(
            is_valid=within_compliance,
            entity_type="CertificationScheme",
            tolerance_type="regulatory_compliance",
            actual_value=volume_deviation,
            expected_value=0.0,
            acceptable_range=(0.0, max_allowed_deviation), 
            deviation=volume_deviation,
            message=f"{reporting_standard} compliance: {volume_deviation*100:.2f}% volume deviation {'within' if within_compliance else 'exceeds'} ±{max_allowed_deviation*100:.1f}% limit"
        )


class BOOSTToleranceValidator:
    """
    Main tolerance validation coordinator that demonstrates Colin's governance model:
    - Equipment manufacturers set measurement accuracy (MeasurementRecord)
    - Industry standards set process loss tolerances (MaterialProcessing)  
    - Regulators set compliance reporting tolerances (CertificationScheme)
    """
    
    def __init__(self):
        self.equipment_validator = EquipmentAccuracyValidator()
        self.process_validator = ProcessLossValidator()
        self.compliance_validator = RegulatoryComplianceValidator()
    
    def validate_pelletizing_example(self) -> List[ToleranceValidationResult]:
        """
        Demonstrate Colin's specific "within tolerance for pelletizing" scenario
        with explicit validation showing WHO sets the tolerance and WHERE it lives.
        """
        
        # Example pelletizing process data
        pelletizing_data = {
            "processingId": "MP-PELLET-001",
            "processType": "pelletizing",
            "inputVolume": 100.0,
            "outputVolume": 98.2,
            "volumeLoss": 1.8,
            "expectedLossRate": 0.02,
            "acceptableRange": [0.015, 0.035],
            "processStandard": "industry_standard",
            "toleranceValidation": {
                "actualLossRate": 0.018,
                "withinTolerance": True,
                "deviationFromExpected": -0.002
            }
        }
        
        # Example measurement data for pelletizing input
        measurement_data = {
            "recordId": "MR-PELLET-INPUT-001", 
            "measurementMethod": "mill",
            "measuredVolume": 100.0,
            "expectedAccuracy": 0.005,
            "calibrationStandard": "NIST_traceable",
            "accuracyValidation": {
                "minAcceptable": 99.5,
                "maxAcceptable": 100.5,
                "withinTolerance": True
            }
        }
        
        # Example certification scheme for regulatory compliance
        certification_data = {
            "schemeName": "CARB LCFS Compliance",
            "complianceTolerances": {
                "volumeDeviation": 0.005,
                "reportingStandard": "CARB_LCFS"
            }
        }
        
        # Validate all three tolerance types
        results = []
        
        # 1. Equipment accuracy validation (WHO: Equipment manufacturers)
        measurement_result = self.equipment_validator.validate_measurement_accuracy(measurement_data)
        results.append(measurement_result)
        
        # 2. Process loss validation (WHO: Industry standards) - This answers Colin's question!
        process_result = self.process_validator.validate_process_loss(pelletizing_data)
        results.append(process_result)
        
        # 3. Regulatory compliance validation (WHO: Regulators)
        measurement_chain = [{
            "inputVolume": 100.0,
            "outputVolume": 98.2
        }]
        compliance_result = self.compliance_validator.validate_regulatory_compliance(
            certification_data, measurement_chain)
        results.append(compliance_result)
        
        return results
    
    def print_validation_results(self, results: List[ToleranceValidationResult]):
        """Print validation results with clear governance attribution."""
        
        governance_attribution = {
            "MeasurementRecord": "Equipment Manufacturer",
            "MaterialProcessing": "Industry Standard",
            "CertificationScheme": "Regulatory Authority"
        }
        
        print("BOOST Tolerance Validation Results")
        print("=" * 50)
        print("Addressing Colin's questions:")
        print("- What are the acceptable error rates? → Defined in each entity")
        print("- Who sets the tolerance? → Clear governance model")  
        print("- Where does it live? → In the entity where tolerance applies")
        print()
        
        for i, result in enumerate(results, 1):
            authority = governance_attribution.get(result.entity_type, "Unknown")
            
            print(f"{i}. {result.tolerance_type.upper()} VALIDATION")
            print(f"   Entity: {result.entity_type}")
            print(f"   Authority: {authority}")
            print(f"   Status: {'✓ VALID' if result.is_valid else '✗ INVALID'}")
            print(f"   Message: {result.message}")
            
            if result.acceptable_range:
                min_val, max_val = result.acceptable_range
                print(f"   Acceptable Range: {min_val:.4f} - {max_val:.4f}")
                
            if result.deviation is not None:
                print(f"   Deviation: {result.deviation:+.4f}")
                
            print()


def main():
    """Demonstrate the tolerance validation system addressing Colin's concerns."""
    
    validator = BOOSTToleranceValidator()
    
    print("BOOST Distributed Tolerance Validation")
    print("Demonstrating solution to Colin's 'within tolerance for pelletizing' question")
    print()
    
    # Run the pelletizing example
    results = validator.validate_pelletizing_example()
    validator.print_validation_results(results)
    
    # Show that "within tolerance for pelletizing" is now explicit
    pelletizing_result = next((r for r in results if r.tolerance_type == "process_loss"), None)
    if pelletizing_result:
        print("COLIN'S QUESTION ANSWERED:")
        print(f"'Within tolerance for pelletizing' means:")
        print(f"  - Actual loss: {pelletizing_result.actual_value*100:.2f}%")
        print(f"  - Expected loss: {pelletizing_result.expected_value*100:.2f}%") 
        print(f"  - Acceptable range: {pelletizing_result.acceptable_range[0]*100:.1f}% - {pelletizing_result.acceptable_range[1]*100:.1f}%")
        print(f"  - Authority: Industry Standard")
        print(f"  - Location: MaterialProcessing.acceptableRange field")


if __name__ == "__main__":
    main()