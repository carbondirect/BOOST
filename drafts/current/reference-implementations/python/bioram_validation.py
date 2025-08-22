"""
BOOST Python Reference Implementation - BioRAM Validation
Enhanced validation specifically for BioRAM program compliance

This module extends the base BOOST validation framework with BioRAM-specific
business logic validation, compliance checks, and reporting validation.
"""

import json
import re
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path
from dynamic_models import get_models
from validation import BOOSTValidator


class BioramValidator(BOOSTValidator):
    """Extended BOOST validator with BioRAM-specific validation rules."""
    
    def __init__(self, schema_base_path: Optional[str] = None):
        """Initialize BioRAM validator with enhanced validation rules."""
        super().__init__(schema_base_path)
        
        # BioRAM-specific validation rules
        self.bioram_rules = {
            'efficiency_standards': {
                'biomass_power_plant': {'min': 0.30, 'max': 0.60},
                'biogas_facility': {'min': 0.25, 'max': 0.55},
                'combined_heat_power': {'min': 0.35, 'max': 0.65}
            },
            'carbon_intensity_limits': {
                'lumber_mill_residual': {'max': 20.0},
                'forest_harvest_residual': {'max': 25.0},
                'agricultural_residue': {'max': 22.0},
                'urban_wood_waste': {'max': 30.0}
            },
            'fire_hazard_zones': {
                'bioram_eligible': ['Very High', 'High', 'Moderate'],
                'priority_zones': ['Very High', 'High']
            },
            'haul_distance_limits': {
                'economical_max': 100,  # miles
                'environmental_max': 150  # miles
            }
        }
    
    def validate_bioram_pathway(self, pathway_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate BioRAM pathway compliance.
        
        Args:
            pathway_data: BioRAM pathway data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Basic schema validation first
        is_valid, schema_errors = self.validate_entity('bioram_pathway', pathway_data)
        if not is_valid:
            errors.extend(schema_errors)
        
        # BioRAM-specific validation
        fuel_type = pathway_data.get('fuelType')
        facility_type = pathway_data.get('targetFacilityType')
        efficiency = pathway_data.get('efficiencyStandard')
        carbon_intensity = pathway_data.get('carbonIntensity')
        
        # Validate efficiency standards by facility type
        if facility_type and efficiency is not None:
            if facility_type in self.bioram_rules['efficiency_standards']:
                limits = self.bioram_rules['efficiency_standards'][facility_type]
                if efficiency < limits['min']:
                    errors.append(
                        f"Efficiency {efficiency} below minimum {limits['min']} "
                        f"for {facility_type}"
                    )
                if efficiency > limits['max']:
                    errors.append(
                        f"Efficiency {efficiency} above maximum {limits['max']} "
                        f"for {facility_type}"
                    )
        
        # Validate carbon intensity by fuel type
        if fuel_type and carbon_intensity is not None:
            if fuel_type in self.bioram_rules['carbon_intensity_limits']:
                max_ci = self.bioram_rules['carbon_intensity_limits'][fuel_type]['max']
                if carbon_intensity > max_ci:
                    errors.append(
                        f"Carbon intensity {carbon_intensity} exceeds limit {max_ci} "
                        f"for {fuel_type}"
                    )
        
        # Validate fire hazard zone eligibility
        fire_zones = pathway_data.get('fireHazardZoneEligibility', [])
        eligible_zones = self.bioram_rules['fire_hazard_zones']['bioram_eligible']
        for zone in fire_zones:
            if zone not in eligible_zones:
                errors.append(f"Fire hazard zone '{zone}' not BioRAM eligible")
        
        return len(errors) == 0, errors
    
    def validate_bioram_reporting(self, report_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate BioRAM reporting compliance.
        
        Args:
            report_data: BioRAM reporting data to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Basic schema validation first
        is_valid, schema_errors = self.validate_entity('bioram_reporting', report_data)
        if not is_valid:
            errors.extend(schema_errors)
        
        # BioRAM reporting-specific validation
        biomass_volume = report_data.get('totalBiomassVolume')
        energy_generated = report_data.get('totalEnergyGenerated')
        efficiency = report_data.get('overallEfficiency')
        efficiency_target = report_data.get('efficiencyTarget')
        compliance_status = report_data.get('complianceStatus')
        
        # Validate efficiency against target
        if efficiency is not None and efficiency_target is not None:
            if efficiency < efficiency_target:
                if compliance_status != 'efficiency_shortfall':
                    errors.append(
                        f"Efficiency {efficiency} below target {efficiency_target} "
                        f"but compliance status is '{compliance_status}', "
                        f"should be 'efficiency_shortfall'"
                    )
        
        # Validate energy conversion efficiency
        if biomass_volume and energy_generated and efficiency:
            # Typical biomass energy content: ~18-20 GJ/BDT, ~5.5 MWh/BDT theoretical
            theoretical_energy = biomass_volume * 5.5  # MWh
            calculated_efficiency = energy_generated / theoretical_energy
            
            # Allow 10% tolerance for calculation differences
            if abs(calculated_efficiency - efficiency) > 0.10:
                errors.append(
                    f"Reported efficiency {efficiency} inconsistent with "
                    f"calculated efficiency {calculated_efficiency:.3f} "
                    f"(volume: {biomass_volume} BDT, energy: {energy_generated} MWh)"
                )
        
        # Validate reporting period format
        reporting_period = report_data.get('reportingPeriod')
        if reporting_period and not re.match(r'^\d{4}-Q[1-4]$', reporting_period):
            errors.append(f"Invalid reporting period format: {reporting_period}")
        
        return len(errors) == 0, errors
    
    def validate_bioram_transaction(self, transaction_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate BioRAM transaction compliance.
        
        Args:
            transaction_data: Transaction data with BioRAM fields
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check for BioRAM-specific fields
        bioram_pathway_id = transaction_data.get('BioramPathwayId')
        biomass_volume = transaction_data.get('biomassVolume')
        fuel_type = transaction_data.get('fuelType')
        fuel_coordinates = transaction_data.get('fuelOriginCoordinates')
        within_sra = transaction_data.get('withinSRA')
        fire_zone = transaction_data.get('fireHazardSeverityZone')
        haul_distance = transaction_data.get('haulDistance')
        bioram_eligible = transaction_data.get('bioramEligible')
        
        # Validate BioRAM pathway ID format
        if bioram_pathway_id:
            if not re.match(r'^BIORAM-PWR-\d{4}-[A-Z]{2,4}-\d{3}$', bioram_pathway_id):
                errors.append(f"Invalid BioRAM pathway ID format: {bioram_pathway_id}")
        
        # Validate fuel origin coordinates
        if fuel_coordinates:
            lat = fuel_coordinates.get('latitude')
            lon = fuel_coordinates.get('longitude')
            
            if lat is not None and (lat < 32.0 or lat > 42.0):
                errors.append(f"Fuel origin latitude {lat} outside California range")
            
            if lon is not None and (lon < -125.0 or lon > -114.0):
                errors.append(f"Fuel origin longitude {lon} outside California range")
        
        # Validate fire hazard zone requirements
        if fire_zone and bioram_eligible:
            eligible_zones = self.bioram_rules['fire_hazard_zones']['bioram_eligible']
            if fire_zone not in eligible_zones:
                errors.append(
                    f"Fire hazard zone '{fire_zone}' not eligible for BioRAM program"
                )
        
        # Validate haul distance limits
        if haul_distance is not None:
            if haul_distance > self.bioram_rules['haul_distance_limits']['environmental_max']:
                errors.append(
                    f"Haul distance {haul_distance} miles exceeds environmental limit "
                    f"{self.bioram_rules['haul_distance_limits']['environmental_max']} miles"
                )
            elif haul_distance > self.bioram_rules['haul_distance_limits']['economical_max']:
                # Warning, not error
                pass  # Could add to warnings list if implemented
        
        # Validate SRA requirement for BioRAM eligibility
        if bioram_eligible and within_sra is False:
            errors.append("BioRAM eligible material must be sourced from within SRA")
        
        # Validate biomass volume units and ranges
        if biomass_volume is not None:
            if biomass_volume <= 0:
                errors.append("Biomass volume must be greater than 0")
            elif biomass_volume > 10000:  # Unreasonably large for single transaction
                errors.append(f"Biomass volume {biomass_volume} BDT seems unreasonably large")
        
        # Validate fuel ownership documentation
        landowner = transaction_data.get('landowner')
        parcel_id = transaction_data.get('parcelId')
        permit_number = transaction_data.get('calFirePermitNumber')
        
        if bioram_eligible:
            if not landowner:
                errors.append("Landowner required for BioRAM eligible transactions")
            if not parcel_id:
                errors.append("Parcel ID required for BioRAM eligible transactions")
            # CAL FIRE permit may not be required for all fuel types
        
        # Validate attestation requirements
        attestation_signatory = transaction_data.get('attestationSignatory')
        material_eligibility = transaction_data.get('materialEligibilityConfirmed')
        reporting_accuracy = transaction_data.get('reportingAccuracyConfirmed')
        
        if bioram_eligible:
            if not attestation_signatory:
                errors.append("Attestation signatory required for BioRAM eligible transactions")
            if material_eligibility is not True:
                errors.append("Material eligibility must be confirmed for BioRAM transactions")
            if reporting_accuracy is not True:
                errors.append("Reporting accuracy must be confirmed for BioRAM transactions")
        
        return len(errors) == 0, errors
    
    def validate_bioram_organization(self, org_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate BioRAM organization compliance.
        
        Args:
            org_data: Organization data with BioRAM fields
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check BioRAM-specific organization fields
        bioram_registration = org_data.get('bioramRegistrationId')
        bioram_facility_id = org_data.get('bioramFacilityId')
        eligibility_status = org_data.get('bioramEligibilityStatus')
        california_sra = org_data.get('californiaSRA')
        fire_zone = org_data.get('fireHazardZoneDesignation')
        
        # Validate BioRAM registration ID format
        if bioram_registration:
            if not re.match(r'^CEC-BIO-\d{3}$', bioram_registration):
                errors.append(f"Invalid BioRAM registration ID format: {bioram_registration}")
        
        # Validate facility ID format
        if bioram_facility_id:
            if not re.match(r'^BIORAM-FAC-\d{4}-\d{3}$', bioram_facility_id):
                errors.append(f"Invalid BioRAM facility ID format: {bioram_facility_id}")
        
        # Validate SRA requirement for BioRAM facilities
        if eligibility_status in ['qualified', 'pending'] and california_sra is False:
            errors.append("BioRAM qualified facilities must be within California SRA")
        
        # Validate fire hazard zone for facility location
        if fire_zone:
            valid_zones = ['Very High', 'High', 'Moderate', 'Low']
            if fire_zone not in valid_zones:
                errors.append(f"Invalid fire hazard zone designation: {fire_zone}")
        
        return len(errors) == 0, errors
    
    def comprehensive_bioram_validation(self, entities: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """
        Run comprehensive BioRAM validation on all entities.
        
        Args:
            entities: Dictionary with entity_type -> list of entities
            
        Returns:
            Dictionary with validation results
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'bioram_specific_results': {},
            'compliance_summary': {}
        }
        
        # Run base BOOST validation first
        base_results = self.comprehensive_validation(entities)
        results.update(base_results)
        
        # BioRAM-specific validation
        bioram_entities = ['bioram_pathway', 'bioram_reporting']
        bioram_enhanced_entities = ['transaction', 'organization']
        
        # Validate dedicated BioRAM entities
        for entity_type in bioram_entities:
            if entity_type in entities:
                entity_errors = []
                for i, entity in enumerate(entities[entity_type]):
                    if entity_type == 'bioram_pathway':
                        is_valid, errors = self.validate_bioram_pathway(entity)
                    elif entity_type == 'bioram_reporting':
                        is_valid, errors = self.validate_bioram_reporting(entity)
                    
                    if not is_valid:
                        entity_errors.extend([f"Entity {i}: {error}" for error in errors])
                
                results['bioram_specific_results'][entity_type] = {
                    'valid': len(entity_errors) == 0,
                    'errors': entity_errors
                }
                
                if entity_errors:
                    results['valid'] = False
                    results['errors'].extend(entity_errors)
        
        # Validate BioRAM fields in enhanced entities
        for entity_type in bioram_enhanced_entities:
            if entity_type in entities:
                entity_errors = []
                for i, entity in enumerate(entities[entity_type]):
                    # Check if entity has BioRAM fields
                    if self._has_bioram_fields(entity):
                        if entity_type == 'transaction':
                            is_valid, errors = self.validate_bioram_transaction(entity)
                        elif entity_type == 'organization':
                            is_valid, errors = self.validate_bioram_organization(entity)
                        
                        if not is_valid:
                            entity_errors.extend([f"Entity {i}: {error}" for error in errors])
                
                if entity_errors:
                    results['bioram_specific_results'][f'{entity_type}_bioram'] = {
                        'valid': False,
                        'errors': entity_errors
                    }
                    results['valid'] = False
                    results['errors'].extend(entity_errors)
        
        # Generate compliance summary
        results['compliance_summary'] = self._generate_compliance_summary(entities)
        
        return results
    
    def _has_bioram_fields(self, entity: Dict[str, Any]) -> bool:
        """Check if entity has any BioRAM-specific fields."""
        bioram_field_patterns = [
            'bioram', 'BioRAM', 'Bioram',
            'fuelType', 'biomassVolume', 'haulDistance',
            'fireHazardSeverityZone', 'withinSRA'
        ]
        
        for field in entity.keys():
            for pattern in bioram_field_patterns:
                if pattern in field:
                    return True
        return False
    
    def _generate_compliance_summary(self, entities: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Generate BioRAM compliance summary."""
        summary = {
            'total_bioram_entities': 0,
            'bioram_pathways': 0,
            'bioram_reports': 0,
            'bioram_transactions': 0,
            'bioram_organizations': 0,
            'eligible_transactions': 0,
            'compliance_rates': {}
        }
        
        # Count BioRAM entities
        if 'bioram_pathway' in entities:
            summary['bioram_pathways'] = len(entities['bioram_pathway'])
            summary['total_bioram_entities'] += summary['bioram_pathways']
        
        if 'bioram_reporting' in entities:
            summary['bioram_reports'] = len(entities['bioram_reporting'])
            summary['total_bioram_entities'] += summary['bioram_reports']
        
        # Count BioRAM-enhanced entities
        if 'transaction' in entities:
            bioram_txns = [t for t in entities['transaction'] if self._has_bioram_fields(t)]
            summary['bioram_transactions'] = len(bioram_txns)
            summary['eligible_transactions'] = len([
                t for t in bioram_txns if t.get('bioramEligible') is True
            ])
        
        if 'organization' in entities:
            bioram_orgs = [o for o in entities['organization'] if self._has_bioram_fields(o)]
            summary['bioram_organizations'] = len(bioram_orgs)
        
        return summary


def create_bioram_validator(schema_path: Optional[str] = None) -> BioramValidator:
    """
    Factory function to create a BioRAM validator.
    
    Args:
        schema_path: Optional path to schema directory
        
    Returns:
        BioramValidator instance
    """
    return BioramValidator(schema_path)
