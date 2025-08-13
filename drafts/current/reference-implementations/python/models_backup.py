"""
BOOST Python Reference Implementation - Data Models

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
        alias="lastUpdated",
        default_factory=lambda: datetime.utcnow().isoformat(), 
        description="Timestamp of last update"
    )
    
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

    @model_validator(mode='before')
    def set_type(cls, values):
        # Automatically set the 'type' field based on the class name
        type_name = cls.__name__
        if 'type' not in values or values['type'] is None:
            values['type'] = type_name
        return values


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


class Organization(BOOSTBaseModel):
    """Organization entity model."""
    
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
    operational_areas: Optional[List[str]] = Field(
        None,
        alias="operationalAreas",
        description="List of geographic area IDs where organization operates"
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
    certifications: Optional[List[str]] = Field(
        None,
        description="List of certification IDs held by organization"
    )
    established_date: Optional[str] = Field(
        None,
        alias="establishedDate",
        description="Date organization was established (YYYY-MM-DD)"
    )
    tax_id: Optional[str] = Field(
        None,
        alias="taxId",
        description="Tax identification number"
    )
    website: Optional[str] = Field(
        None,
        description="Organization website URL"
    )
    
    @field_validator('type', mode='before')
    def set_type(cls, v):
        return "Organization"


class UnitType(str, Enum):
    """Traceable unit types."""
    LOG = "log"
    PILE = "pile"
    TRUCK_LOAD = "truck_load"
    CONTAINER = "container"
    BATCH = "batch"


class TraceableUnit(BOOSTBaseModel):
    """Traceable Unit entity model."""
    
    traceable_unit_id: str = Field(
        ...,
        alias="traceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Unique identifier for the traceable unit"
    )
    unit_type: UnitType = Field(
        ...,
        alias="unitType",
        description="Type of traceable unit"
    )
    unique_identifier: Optional[str] = Field(
        None,
        alias="uniqueIdentifier",
        description="Physical identifier (RFID, barcode, etc.)"
    )
    total_volume_m3: Optional[float] = Field(
        None,
        alias="totalVolumeM3",
        ge=0,
        description="Total volume in cubic meters"
    )
    current_geographic_data_id: Optional[str] = Field(
        None,
        alias="currentGeographicDataId",
        pattern=r"^GEO-[A-Z0-9-_]+$",
        description="Current location of the unit"
    )
    harvest_geographic_data_id: Optional[str] = Field(
        None,
        alias="harvestGeographicDataId",
        pattern=r"^GEO-[A-Z0-9-_]+$",
        description="Original harvest location"
    )
    created_timestamp: Optional[datetime] = Field(
        None,
        alias="createdTimestamp",
        description="When the unit was created"
    )
    harvester_id: Optional[str] = Field(
        None,
        alias="harvesterId",
        pattern=r"^ORG-[A-Z0-9-_]+$",
        description="Organization that harvested this unit"
    )
    operator_id: Optional[str] = Field(
        None,
        alias="operatorId",
        pattern=r"^OP-[A-Z0-9-_]+$",
        description="Operator responsible for this unit"
    )
    material_type_id: Optional[str] = Field(
        None,
        alias="materialTypeId",
        description="Material type classification"
    )
    assortment_type: Optional[str] = Field(
        None,
        alias="assortmentType",
        description="Product assortment classification"
    )
    quality_grade: Optional[str] = Field(
        None,
        alias="qualityGrade",
        description="Quality grade assessment"
    )
    is_multi_species: Optional[bool] = Field(
        None,
        alias="isMultiSpecies",
        description="Whether unit contains multiple species"
    )
    attached_information: Optional[List[str]] = Field(
        None,
        alias="attachedInformation",
        description="Additional metadata about the unit"
    )
    processing_history: Optional[List[str]] = Field(
        None,
        alias="processingHistory",
        description="List of processing operation IDs"
    )
    parent_traceable_unit_id: Optional[str] = Field(
        None,
        alias="parentTraceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Parent TRU ID if derived from another unit"
    )
    child_traceable_unit_ids: Optional[List[str]] = Field(
        None,
        alias="childTraceableUnitIds",
        description="Child TRU IDs if unit was split"
    )
    current_status: Optional[str] = Field(
        None,
        alias="currentStatus",
        description="Current status of the unit"
    )
    sustainability_certification: Optional[str] = Field(
        None,
        alias="sustainabilityCertification",
        description="Sustainability certification claim"
    )
    media_break_flags: Optional[List[str]] = Field(
        None,
        alias="mediaBreakFlags",
        description="Any chain of custody breaks"
    )
    
    @field_validator('type', mode='before')
    def set_type(cls, v):
        return "TraceableUnit"


class Transaction(BOOSTBaseModel):
    """Transaction entity model."""
    
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
    traceable_unit_id: Optional[str] = Field(
        None,
        alias="TraceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Traceable unit being transacted"
    )
    transaction_date: str = Field(
        ...,
        alias="transactionDate",
        description="Date of transaction (YYYY-MM-DD)"
    )
    quantity: Optional[float] = Field(
        None,
        ge=0,
        description="Quantity being transacted"
    )
    quantity_unit: Optional[str] = Field(
        None,
        alias="quantityUnit",
        description="Unit of measurement for quantity"
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
    sales_delivery_document_id: Optional[str] = Field(
        None,
        alias="SalesDeliveryDocumentId",
        description="Associated sales/delivery document"
    )
    
    @field_validator('type', mode='before')
    def set_type(cls, v):
        return "Transaction"


class ProcessType(str, Enum):
    """Material processing types."""
    FELLING = "felling"
    DELIMBING = "delimbing"
    CROSSCUTTING = "crosscutting"
    CHIPPING = "chipping"
    DEBARKING = "debarking"
    ASSORTMENT = "assortment"


class MaterialProcessing(BOOSTBaseModel):
    """Material Processing entity model."""
    
    processing_id: str = Field(
        ...,
        alias="processingId",
        pattern=r"^PROC-[A-Z0-9-_]+$",
        description="Unique identifier for processing operation"
    )
    input_traceable_unit_id: str = Field(
        ...,
        alias="inputTraceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Input traceable unit"
    )
    output_traceable_unit_id: str = Field(
        ...,
        alias="outputTraceableUnitId", 
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="Output traceable unit"
    )
    process_type: ProcessType = Field(
        ...,
        alias="processType",
        description="Type of processing operation"
    )
    process_timestamp: Optional[datetime] = Field(
        None,
        alias="processTimestamp",
        description="When processing occurred"
    )
    input_volume: Optional[float] = Field(
        None,
        alias="inputVolume",
        ge=0,
        description="Input volume"
    )
    output_volume: Optional[float] = Field(
        None,
        alias="outputVolume",
        ge=0,
        description="Output volume"
    )
    volume_loss: Optional[float] = Field(
        None,
        alias="volumeLoss",
        ge=0,
        description="Volume lost during processing"
    )
    input_mass: Optional[float] = Field(
        None,
        alias="inputMass",
        ge=0,
        description="Input mass"
    )
    output_mass: Optional[float] = Field(
        None,
        alias="outputMass",
        ge=0,
        description="Output mass"
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
    
    @field_validator('type', mode='before')
    def set_type(cls, v):
        return "MaterialProcessing"
    
    @model_validator(mode='before')
    def validate_volume_conservation(cls, values):
        """Validate that volume is conserved during processing."""
        input_vol = values.get('input_volume')
        output_vol = values.get('output_volume')
        vol_loss = values.get('volume_loss', 0)
        
    #     if all(v is not None for v in [input_vol, output_vol, vol_loss]):
    #         if input_vol < (output_vol + vol_loss):
    #             raise ValueError("Volume conservation violation: input must be >= output + loss")
        
    #     return values


class ClaimType(str, Enum):
    """Sustainability claim types."""
    FSC_MIX = "FSC Mix"
    FSC_100 = "FSC 100%"
    FSC_RECYCLED = "FSC Recycled"
    PEFC = "PEFC"
    SBP_COMPLIANT = "SBP-compliant"
    ISCC_EU = "ISCC EU"
    RED_II = "RED II"


class Claim(BOOSTBaseModel):
    """Sustainability claim entity model."""
    
    claim_id: str = Field(
        ...,
        alias="claimId",
        pattern=r"^CLAIM-[A-Z0-9-_]+$",
        description="Unique identifier for the claim"
    )
    traceable_unit_id: str = Field(
        ...,
        alias="traceableUnitId",
        pattern=r"^TRU-[A-Z0-9-_]+$",
        description="TRU this claim applies to"
    )
    claim_type: ClaimType = Field(
        ...,
        alias="claimType",
        description="Type of sustainability claim"
    )
    certification_scheme_id: Optional[str] = Field(
        None,
        alias="certificationSchemeId",
        pattern=r"^CERT-[A-Z0-9-_]+$",
        description="Certification scheme details"
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
    claim_scope: Optional[str] = Field(
        None,
        alias="claimScope",
        description="Scope of claim through supply chain"
    )
    evidence_document_id: Optional[str] = Field(
        None,
        alias="evidenceDocumentId",
        description="Supporting evidence document"
    )
    claim_expiry: Optional[datetime] = Field(
        None,
        alias="claimExpiry",
        description="When claim expires"
    )
    inherited_from_tru: Optional[List[str]] = Field(
        None,
        alias="inheritedFromTRU",
        description="TRU IDs from which claim was inherited"
    )
    
    @field_validator('type', mode='before')
    def set_type(cls, v):
        return "Claim"


# Additional models can be added here following the same pattern
# Certificate, CertificationScheme, GeographicData, etc.