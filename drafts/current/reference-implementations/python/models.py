"""
BOOST Python Reference Implementation - Data Models
Enhanced with BioRAM Program Support (Fixed)

This module contains Pydantic models for all BOOST entities, providing
data validation, serialization, and JSON-LD context management.
"""

from datetime import datetime
from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum


class BOOSTBaseModel(BaseModel):
    """Base model for all BOOST entities with JSON-LD support."""
    
    context: Optional[Dict[str, Any]] = Field(None, alias="@context")
    type: str = Field(..., description="Entity type, e.g., Organization, TraceableUnit")
    id: str = Field(..., alias="@id", description="Unique URI identifier")
    last_updated: Optional[datetime] = Field(
        None,
        alias="lastUpdated",
        description="Timestamp of last update"
    )
    
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

    @model_validator(mode='before')
    @classmethod
    def set_type_if_missing(cls, data):
        """Set the type field based on class name if not provided."""
        if isinstance(data, dict):
            if 'type' not in data and '@type' not in data:
                data['type'] = cls.__name__
        return data


class OrganizationType(str, Enum):
    """Organization types defined in BOOST standard."""
    HARVESTER = "harvester"
    PROCESSOR = "processor"
    CERTIFIER = "certifier"
    TRANSPORTER = "transporter"
    SUPPLIER = "supplier"
    MANUFACTURER = "manufacturer"
    PRODUCER = "producer"
    IMPORTER = "importer"
    BLENDER = "blender"
    DISTRIBUTOR = "distributor"


class BioramEligibilityStatus(str, Enum):
    """BioRAM program eligibility status."""
    QUALIFIED = "qualified"
    PENDING = "pending"
    SUSPENDED = "suspended"
    NOT_ELIGIBLE = "not_eligible"


class FireHazardZone(str, Enum):
    """CAL FIRE fire hazard severity zones."""
    VERY_HIGH = "Very High"
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"


class FuelType(str, Enum):
    """BioRAM eligible fuel types."""
    LUMBER_MILL_RESIDUAL = "lumber_mill_residual"
    FOREST_HARVEST_RESIDUAL = "forest_harvest_residual"
    AGRICULTURAL_RESIDUE = "agricultural_residue"
    URBAN_WOOD_WASTE = "urban_wood_waste"
    CONSTRUCTION_DEMOLITION_WOOD = "construction_demolition_wood"
    ORCHARD_REMOVAL_MATERIAL = "orchard_removal_material"


class BiomassVolumeUnit(str, Enum):
    """Biomass volume measurement units."""
    BONE_DRY_TONNES = "bone_dry_tonnes"
    GREEN_TONNES = "green_tonnes"
    CUBIC_YARDS = "cubic_yards"


class HaulUnit(str, Enum):
    """Haul distance units."""
    MILES = "miles"
    KILOMETERS = "kilometers"


class UnitType(str, Enum):
    """Traceable unit types."""
    INDIVIDUAL_LOG = "individual_log"
    PILE = "pile"
    VOLUME_AGGREGATION = "volume_aggregation"
    PROCESSED_BATCH = "processed_batch"


class ProcessType(str, Enum):
    """Material processing types."""
    FELLING = "felling"
    DELIMBING = "delimbing"
    CROSSCUTTING = "crosscutting"
    CHIPPING = "chipping"
    DEBARKING = "debarking"
    ASSORTMENT = "assortment"


class PermitStatus(str, Enum):
    """Permit status options."""
    ACTIVE = "active"
    EXPIRED = "expired"
    PENDING = "pending"
    NOT_REQUIRED = "not_required"

class ClaimType(str, Enum):
    """Sustainability claim types."""
    SBP_COMPLIANT = "SBP-compliant"
    FSC_MIX = "FSC Mix"
    RSB_GLOBAL = "RSB Global"
    PEFC = "PEFC"
    ORGANIC = "organic"
    FSC_100 = "FSC 100%"
    FSC_RECYCLED = "FSC Recycled"
    ISCC_EU = "ISCC EU"
    RED_II = "RED II"



class Organization(BOOSTBaseModel):
    """Organization entity model with BioRAM support."""
    
    organization_id: str = Field(
        ..., 
        alias="organizationId",
        pattern=r"^ORG-[A-Z0-9-_]+$",
        min_length=5,
        max_length=50,
        description="Unique identifier for the organization"
    )
    organization_name: str = Field(
        ...,
        alias="organizationName", 
        min_length=2,
        max_length=200,
        description="Legal name of the organization"
    )
    organization_type: OrganizationType = Field(
        ..., 
        alias="organizationType",
        description="Type of organization"
    )
    primary_geographic_data_id: Optional[str] = Field(
        None,
        alias="primaryGeographicDataId",
        pattern=r"^GEO-[A-Z0-9-_]+$",
        description="Foreign key to primary operational location"
    )
    contact_email: Optional[str] = Field(
        None,
        alias="contactEmail",
        description="Primary contact email"
    )
    contact_phone: Optional[str] = Field(
        None,
        alias="contactPhone",
        description="Primary contact phone number"
    )
    website: Optional[str] = Field(
        None,
        description="Organization website URL"
    )
    
    # BioRAM-specific fields
    bioram_registration_id: Optional[str] = Field(
        None,
        alias="bioramRegistrationId",
        pattern=r"^CEC-BIO-[0-9]{3}$",
        description="CEC BioRAM registration identifier"
    )
    bioram_facility_id: Optional[str] = Field(
        None,
        alias="bioramFacilityId",
        pattern=r"^BIORAM-FAC-[0-9]{4}-[0-9]{3}$",
        description="BioRAM facility identifier"
    )
    power_purchase_agreement_id: Optional[str] = Field(
        None,
        alias="powerPurchaseAgreementId",
        description="Power purchase agreement identifier"
    )
    utility_offtaker: Optional[str] = Field(
        None,
        alias="utilityOfftaker",
        description="Utility company purchasing power"
    )
    california_sra: Optional[bool] = Field(
        None,
        alias="californiaSRA",
        description="Whether facility operates within California SRA"
    )
    bioram_eligibility_status: Optional[BioramEligibilityStatus] = Field(
        None,
        alias="bioramEligibilityStatus",
        description="Current BioRAM program eligibility status"
    )
    fire_hazard_zone_designation: Optional[FireHazardZone] = Field(
        None,
        alias="fireHazardZoneDesignation",
        description="CAL FIRE fire hazard severity zone designation"
    )

class TraceableUnit(BOOSTBaseModel):
    """Traceable Unit entity model with BOOST traceability integration."""
    
    traceable_unit_id: str = Field(
        ...,
        alias="traceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        min_length=5,
        max_length=50,
        description="Unique identifier for the traceable unit"
    )
    unit_type: UnitType = Field(
        ...,
        alias="unitType",
        description="Type of traceable unit"
    )
    unique_identifier: str = Field(
        ...,
        alias="uniqueIdentifier",
        description="Biometric signature, RFID tag, or QR code"
    )
    total_volume_m3: float = Field(
        ...,
        alias="totalVolumeM3",
        ge=0,
        description="Total volume in cubic meters"
    )
    current_geographic_data_id: Optional[str] = Field(
        None,
        alias="currentGeographicDataId",
        pattern=r"^GEO-[A-Z0-9-_]+$",
        description="Current location - uses EntityNameId convention"
    )
    harvest_geographic_data_id: str = Field(
        ...,
        alias="harvestGeographicDataId",
        pattern=r"^GEO-[A-Z0-9-_]+$",
        description="Harvest location - uses EntityNameId convention"
    )
    created_timestamp: datetime = Field(
        ...,
        alias="createdTimestamp",
        description="When the TRU was created"
    )
    harvester_id: str = Field(
        ...,
        alias="harvesterId",
        pattern=r"^ORG-[A-Z0-9-_]+$",
        description="Foreign key to harvesting organization"
    )
    operator_id: Optional[str] = Field(
        None,
        alias="operatorId",
        pattern=r"^OP-[A-Z0-9-_]+$",
        description="Foreign key to operator"
    )
    material_type_id: str = Field(
        ...,
        alias="materialTypeId",
        pattern=r"^MAT-[A-Z0-9-_]+$",
        description="Foreign key to Material entity"
    )
    assortment_type: Optional[str] = Field(
        None,
        alias="assortmentType",
        description="Type of wood assortment"
    )
    quality_grade: Optional[str] = Field(
        None,
        alias="qualityGrade",
        description="Quality grade classification"
    )
    is_multi_species: bool = Field(
        ...,
        alias="isMultiSpecies",
        description="True if contains multiple species"
    )
    attached_information: Optional[List[str]] = Field(
        None,
        alias="attachedInformation",
        description="All data linked to this TRU"
    )
    processing_history: Optional[List[str]] = Field(
        None,
        alias="processingHistory",
        description="Complete processing chain references"
    )
    parent_traceable_unit_id: Optional[str] = Field(
        None,
        alias="parentTraceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="For split/merge operations"
    )
    child_traceable_unit_ids: Optional[List[str]] = Field(
        None,
        alias="childTraceableUnitIds",
        description="For split/merge operations"
    )
    current_status: Optional[str] = Field(
        None,
        alias="currentStatus",
        description="Current status of the TRU"
    )
    sustainability_certification: Optional[str] = Field(
        None,
        alias="sustainabilityCertification",
        description="FSC, PEFC, etc. claims"
    )
    media_break_flags: Optional[List[str]] = Field(
        None,
        alias="mediaBreakFlags",
        description="Points where data continuity was lost"
    )


class MaterialProcessing(BOOSTBaseModel):
    """Material Processing entity model for processing operations."""
    
    processing_id: str = Field(
        ...,
        alias="processingId",
        pattern=r"^MP-[A-Z0-9-_]+$",
        min_length=5,
        max_length=50,
        description="Unique identifier for processing operation"
    )
    input_traceable_unit_id: str = Field(
        ...,
        alias="inputTraceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Input traceable unit being processed"
    )
    output_traceable_unit_id: str = Field(
        ...,
        alias="outputTraceableUnitId", 
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Output traceable unit created"
    )
    process_type: ProcessType = Field(
        ...,
        alias="processType",
        description="Type of processing operation"
    )
    process_timestamp: datetime = Field(
        ...,
        alias="processTimestamp",
        description="When the processing operation occurred"
    )
    input_volume: float = Field(
        ...,
        alias="inputVolume",
        ge=0,
        description="Input volume before processing (cubic meters)"
    )
    output_volume: float = Field(
        ...,
        alias="outputVolume",
        ge=0,
        description="Output volume after processing (cubic meters)"
    )
    volume_loss: Optional[float] = Field(
        None,
        alias="volumeLoss",
        ge=0,
        description="Volume lost during processing (cubic meters)"
    )
    processing_geographic_data_id: Optional[str] = Field(
        None,
        alias="processingGeographicDataId",
        pattern=r"^GEO-[A-Z0-9-_]+$",
        description="Location where processing occurred"
    )
    operator_id: Optional[str] = Field(
        None,
        alias="operatorId",
        pattern=r"^OP-[A-Z0-9-_]+$",
        description="Operator who performed processing"
    )
    input_composition: Optional[str] = Field(
        None,
        alias="inputComposition",
        description="Species composition before processing"
    )
    output_composition: Optional[str] = Field(
        None,
        alias="outputComposition",
        description="Species composition after processing"
    )
    quality_metrics: Optional[str] = Field(
        None,
        alias="qualityMetrics",
        description="Quality assessment metrics"
    )
    equipment_used: Optional[str] = Field(
        None,
        alias="equipmentUsed",
        description="Equipment used for processing"
    )



class Transaction(BOOSTBaseModel):
    """Transaction entity model with BioRAM support."""
    
    transaction_id: str = Field(
        ..., 
        alias="transactionId",
        pattern=r"^TXN-[A-Z0-9-_]+$",
        description="Unique identifier for the transaction"
    )
    organization_id: str = Field(
        ...,
        alias="OrganizationId",
        pattern=r"^ORG-[A-Z0-9-_]+$",
        description="Seller organization ID"
    )
    customer_id: str = Field(
        ...,
        alias="CustomerId",
        pattern=r"^CUST-[A-Z0-9-_]+$",
        description="Buyer customer ID"
    )
    transaction_date: str = Field(
        ...,
        alias="transactionDate",
        description="Date of transaction (YYYY-MM-DD)"
    )
    contract_value: Optional[float] = Field(
        None,
        alias="contractValue",
        ge=0,
        description="Total contract value"
    )
    contract_currency: Optional[str] = Field(
        None,
        alias="contractCurrency",
        description="Currency for contract value"
    )
    
    # BioRAM-specific fields
    bioram_pathway_id: Optional[str] = Field(
        None,
        alias="BioramPathwayId",
        pattern=r"^BIORAM-PWR-[0-9]{4}-[A-Z]{2,4}-[0-9]{3}$",
        description="BioRAM pathway identifier"
    )
    biomass_volume: Optional[float] = Field(
        None,
        alias="biomassVolume",
        ge=0,
        description="Volume of biomass fuel in transaction"
    )
    biomass_volume_unit: Optional[BiomassVolumeUnit] = Field(
        None,
        alias="biomassVolumeUnit",
        description="Unit of measurement for biomass volume"
    )
    fuel_type: Optional[FuelType] = Field(
        None,
        alias="fuelType",
        description="BioRAM eligible fuel type classification"
    )
    fuel_origin_coordinates: Optional[Dict[str, float]] = Field(
        None,
        alias="fuelOriginCoordinates",
        description="Geographic coordinates of biomass fuel origin"
    )
    within_sra: Optional[bool] = Field(
        None,
        alias="withinSRA",
        description="Whether fuel source is within California SRA"
    )
    fire_hazard_severity_zone: Optional[FireHazardZone] = Field(
        None,
        alias="fireHazardSeverityZone",
        description="CAL FIRE fire hazard severity zone designation"
    )
    bioram_eligible: Optional[bool] = Field(
        None,
        alias="bioramEligible",
        description="Whether transaction meets BioRAM eligibility"
    )
    haul_distance: Optional[float] = Field(
        None,
        alias="haulDistance",
        ge=0,
        description="Transportation distance from source to facility"
    )
    haul_unit: Optional[HaulUnit] = Field(
        None,
        alias="haulUnit",
        description="Unit of measurement for haul distance"
    )
    landowner: Optional[str] = Field(
        None,
        alias="landowner",
        description="Legal landowner of biomass source location"
    )
    bioram_certification_id: Optional[str] = Field(
        None,
        alias="bioramCertificationId",
        description="BioRAM compliance certification identifier"
    )
    attestation_signatory: Optional[str] = Field(
        None,
        alias="attestationSignatory",
        description="Name and title of person attesting to BioRAM compliance"
    )
    material_eligibility_confirmed: Optional[bool] = Field(
        None,
        alias="materialEligibilityConfirmed",
        description="Confirmation that material meets BioRAM eligibility"
    )

class Claim(BOOSTBaseModel):
    """Sustainability claim entity model."""
    
    claim_id: str = Field(
        ...,
        alias="claimId",
        pattern=r"^CLA-[A-Z0-9-_]+$",
        min_length=5,
        max_length=50,
        description="Unique identifier for the claim"
    )
    traceable_unit_id: str = Field(
        ...,
        alias="TraceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Referenced traceable unit"
    )
    claim_type: ClaimType = Field(
        ...,
        alias="claimType",
        description="Type of sustainability claim"
    )
    certification_scheme_id: Optional[str] = Field(
        None,
        alias="CertificationSchemeId",
        pattern=r"^CERT-SCHEME-[A-Z0-9-_]+$",
        description="Certification scheme reference"
    )
    statement: str = Field(
        ...,
        description="Formal claim statement"
    )
    validated: bool = Field(
        ...,
        description="Whether claim has been validated"
    )
    validated_by: Optional[str] = Field(
        None,
        alias="validatedBy",
        description="Validator organization/person ID"
    )
    validation_date: Optional[datetime] = Field(
        None,
        alias="validationDate",
        description="When claim was validated"
    )
    applicable_species: Optional[List[str]] = Field(
        None,
        alias="applicableSpecies",
        description="Species this claim applies to"
    )
    claim_percentage: Optional[float] = Field(
        None,
        alias="claimPercentage",
        ge=0,
        le=100,
        description="Percentage of material covered by claim"
    )



# BioRAM Program Entities

class FacilityType(str, Enum):
    """BioRAM target facility types."""
    BIOMASS_POWER_PLANT = "biomass_power_plant"
    BIOGAS_FACILITY = "biogas_facility"
    COMBINED_HEAT_POWER = "combined_heat_power"


class EligibilityStatus(str, Enum):
    """BioRAM eligibility status."""
    ACTIVE = "active"
    SUSPENDED = "suspended"
    EXPIRED = "expired"
    PENDING_APPROVAL = "pending_approval"


class BioramPathway(BOOSTBaseModel):
    """BioRAM Pathway entity model."""
    
    pathway_id: str = Field(
        ...,
        alias="pathwayId",
        pattern=r"^BIORAM-PWR-[0-9]{4}-[A-Z]{2,4}-[0-9]{3}$",
        description="BioRAM pathway identifier"
    )
    fuel_type: FuelType = Field(
        ...,
        alias="fuelType",
        description="BioRAM eligible fuel type classification"
    )
    target_facility_type: FacilityType = Field(
        ...,
        alias="targetFacilityType",
        description="Type of facility this pathway applies to"
    )
    efficiency_standard: float = Field(
        ...,
        alias="efficiencyStandard",
        ge=0.20,
        le=0.60,
        description="Minimum efficiency requirement for BioRAM eligibility"
    )
    carbon_intensity: float = Field(
        ...,
        alias="carbonIntensity",
        ge=0,
        le=50,
        description="Carbon intensity in gCO2e/MJ for biomass fuel"
    )
    certification_date: str = Field(
        ...,
        alias="certificationDate",
        description="CEC BioRAM pathway certification date (YYYY-MM-DD)"
    )
    eligibility_status: EligibilityStatus = Field(
        ...,
        alias="eligibilityStatus",
        description="Current CEC eligibility status"
    )
    fire_hazard_zone_eligibility: Optional[List[FireHazardZone]] = Field(
        None,
        alias="fireHazardZoneEligibility",
        description="Eligible CAL FIRE hazard severity zones"
    )


class ComplianceStatus(str, Enum):
    """BioRAM compliance status."""
    COMPLIANT = "compliant"
    EFFICIENCY_SHORTFALL = "efficiency_shortfall"
    SOURCING_VIOLATION = "sourcing_violation"
    PENDING_REVIEW = "pending_review"


class BioramReporting(BOOSTBaseModel):
    """BioRAM Reporting entity model."""
    
    reporting_id: str = Field(
        ...,
        alias="reportingId",
        pattern=r"^BIORAM-RPT-[0-9]{4}-Q[1-4]-[A-Z0-9]{3,8}$",
        description="Unique identifier for the quarterly BioRAM report"
    )
    facility_entity_id: str = Field(
        ...,
        alias="facilityEntityId",
        pattern=r"^ORG-[A-Z0-9-_]+$",
        description="Reference to biomass facility Organization entity"
    )
    reporting_period: str = Field(
        ...,
        alias="reportingPeriod",
        pattern=r"^[0-9]{4}-Q[1-4]$",
        description="Reporting quarter in YYYY-QN format"
    )
    total_biomass_volume: float = Field(
        ...,
        alias="totalBiomassVolume",
        ge=0,
        description="Total biomass fuel consumed in bone dry tonnes"
    )
    total_energy_generated: float = Field(
        ...,
        alias="totalEnergyGenerated",
        ge=0,
        description="Total electrical energy generated in MWh"
    )
    overall_efficiency: float = Field(
        ...,
        alias="overallEfficiency",
        ge=0.15,
        le=0.60,
        description="Overall facility efficiency"
    )
    compliance_status: ComplianceStatus = Field(
        ...,
        alias="complianceStatus",
        description="Overall BioRAM compliance status"
    )
    transaction_ids: Optional[List[str]] = Field(
        None,
        alias="transactionIds",
        description="Array of Transaction entity IDs for fuel procurement"
    )


# Additional models can be added here following the same pattern
