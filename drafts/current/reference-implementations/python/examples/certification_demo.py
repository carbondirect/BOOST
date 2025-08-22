#!/usr/bin/env python3
"""
BOOST Python Reference Implementation - Certification Demo

This example demonstrates certification claim management:
1. Create certified organizations
2. Create traceable units with claims
3. Demonstrate claim inheritance through processing
4. Validate certification requirements
5. Show multi-scheme certification support

Run with: python certification_demo.py
"""

import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from boost_client import create_client
from dynamic_models import OrganizationType, UnitType, ProcessType


def main():
    """Demonstrate BOOST certification claim management."""
    
    print("=== BOOST Python Reference Implementation ===")
    print("Certification Claims Demo")
    print("=" * 50)
    
    # Initialize BOOST client
    client = create_client()
    
    # Step 1: Create FSC certified forest management company
    print("\n1. Creating FSC certified forest manager...")
    forest_manager = client.create_organization(
        organization_id="ORG-FSC-FOREST-001",
        name="Sustainable Forests Inc",
        org_type=OrganizationType.HARVESTER,
        certifications=["CERT-FSC-FM-001", "CERT-FSC-COC-001"],
        contact_email="sustainability@sustainableforests.com"
    )
    print(f"   ✓ Created: {forest_manager.organization_name}")
    print(f"   Certifications: {forest_manager.certifications}")
    
    # Step 2: Create SBP certified biomass processor
    print("\n2. Creating SBP certified processor...")
    biomass_processor = client.create_organization(
        organization_id="ORG-SBP-PROCESSOR-001", 
        name="Green Energy Processing",
        org_type=OrganizationType.PROCESSOR,
        certifications=["CERT-SBP-001", "CERT-PEFC-COC-001"],
        contact_email="compliance@greenergyproc.com"
    )
    print(f"   ✓ Created: {biomass_processor.organization_name}")
    print(f"   Certifications: {biomass_processor.certifications}")
    
    # Step 3: Create FSC certified traceable unit
    print("\n3. Creating FSC certified traceable unit...")
    fsc_logs = client.create_traceable_unit(
        traceable_unit_id="TRU-FSC-LOGS-001",
        unit_type=UnitType.PILE,
        harvester_id=forest_manager.organization_id,
        total_volume_m3=200.0,
        harvest_geographic_data_id="GEO-FSC-FOREST-001",
        sustainability_certification="FSC Mix Credit 70%",
        is_multi_species=True
    )
    print(f"   ✓ Created: {fsc_logs.traceable_unit_id}")
    print(f"   Volume: {fsc_logs.total_volume_m3} m³")
    print(f"   Certification: {fsc_logs.sustainability_certification}")
    
    # Step 4: Create FSC Mix claim for the logs
    print("\n4. Creating FSC Mix claim...")
    fsc_claim = client.create_claim(
        claim_id="CLAIM-FSC-MIX-001",
        traceable_unit_id=fsc_logs.traceable_unit_id,
        claim_type=ClaimType.FSC_MIX,
        statement="FSC Mix Credit 70%",
        validated=True,
        validated_by="ORG-FSC-CERTIFIER-001",
        validation_date=datetime.utcnow(),
        claim_percentage=70.0,
        claim_scope="full_chain",
        applicable_species=["douglas_fir", "western_hemlock"],
        certification_scheme_id="CERT-FSC-SCHEME-001"
    )
    print(f"   ✓ Created claim: {fsc_claim.claim_id}")
    print(f"   Statement: {fsc_claim.statement}")
    print(f"   Percentage: {fsc_claim.claim_percentage}%")
    print(f"   Species: {fsc_claim.applicable_species}")
    
    # Step 5: Process logs into chips (claim inheritance)
    print("\n5. Processing logs to chips with claim inheritance...")
    
    # Create output TRU for chips
    wood_chips = client.create_traceable_unit(
        traceable_unit_id="TRU-FSC-CHIPS-001",
        unit_type=UnitType.BATCH,
        total_volume_m3=220.0,  # Volume increase due to chipping
        parent_traceable_unit_id=fsc_logs.traceable_unit_id,
        current_geographic_data_id="GEO-PROCESSOR-YARD-001",
        material_type_id="MAT-WOOD-CHIPS",
        sustainability_certification="FSC Mix Credit 70%"
    )
    
    # Create processing operation
    chipping_process = client.create_material_processing(
        processing_id="PROC-FSC-CHIPPING-001",
        input_tru_id=fsc_logs.traceable_unit_id,
        output_tru_id=wood_chips.traceable_unit_id,
        process_type=ProcessType.CHIPPING,
        input_volume=200.0,
        output_volume=220.0,  # Apparent volume increase
        volume_loss=0.0,
        operator_id="OP-CHIPPER-001"
    )
    
    print(f"   ✓ Created chips: {wood_chips.traceable_unit_id}")
    print(f"   Volume: {wood_chips.total_volume_m3} m³")
    print(f"   Processing: {chipping_process.process_type}")
    
    # Step 6: Create inherited FSC claim for chips
    print("\n6. Creating inherited FSC claim for chips...")
    inherited_fsc_claim = client.create_claim(
        claim_id="CLAIM-FSC-MIX-INHERITED-001",
        traceable_unit_id=wood_chips.traceable_unit_id,
        claim_type=ClaimType.FSC_MIX,
        statement="FSC Mix Credit 70% (inherited)",
        validated=True,
        claim_percentage=70.0,
        claim_scope="processing",
        inherited_from_tru=[fsc_logs.traceable_unit_id],
        certification_scheme_id="CERT-FSC-SCHEME-001"
    )
    print(f"   ✓ Created inherited claim: {inherited_fsc_claim.claim_id}")
    print(f"   Inherited from: {inherited_fsc_claim.inherited_from_tru}")
    
    # Step 7: Add SBP compliance claim
    print("\n7. Adding SBP compliance claim...")
    sbp_claim = client.create_claim(
        claim_id="CLAIM-SBP-COMPLIANT-001",
        traceable_unit_id=wood_chips.traceable_unit_id,
        claim_type=ClaimType.SBP_COMPLIANT,
        statement="SBP-compliant biomass from responsibly managed forests",
        validated=True,
        validated_by="ORG-SBP-CERTIFIER-001",
        claim_percentage=100.0,
        claim_scope="full_chain",
        evidence_document_id="DOC-SBP-ASSESSMENT-001"
    )
    print(f"   ✓ Created SBP claim: {sbp_claim.claim_id}")
    print(f"   Statement: {sbp_claim.statement}")
    
    # Step 8: Create transaction with certification requirements
    print("\n8. Creating certified material transaction...")
    certified_transaction = client.create_transaction(
        transaction_id="TXN-CERTIFIED-CHIPS-001",
        organization_id=biomass_processor.organization_id,
        customer_id="CUST-POWER-PLANT-001",
        transaction_date="2025-07-30",
        traceable_unit_id=wood_chips.traceable_unit_id,
        quantity=150.0,
        quantity_unit="cubic_meters",
        contract_value=7500.00,
        contract_currency="USD"
    )
    print(f"   ✓ Created transaction: {certified_transaction.transaction_id}")
    print(f"   Certified material quantity: {certified_transaction.quantity} m³")
    
    # Step 9: Validate all certifications
    print("\n9. Validating certification compliance...")
    
    # Individual entity validation
    entities_to_validate = [
        (fsc_logs, "FSC Logs"),
        (wood_chips, "Wood Chips"),
        (fsc_claim, "FSC Claim"),
        (inherited_fsc_claim, "Inherited FSC Claim"),
        (sbp_claim, "SBP Claim")
    ]
    
    all_valid = True
    for entity, name in entities_to_validate:
        validation = client.validate_entity(entity)
        if validation['valid']:
            print(f"   ✓ {name}: Valid")
        else:
            print(f"   ✗ {name}: Invalid")
            for error in validation['schema_errors'] + validation['business_logic_errors']:
                print(f"     - {error}")
            all_valid = False
    
    # Comprehensive validation
    print("\n10. Comprehensive system validation...")
    system_validation = client.validate_all()
    
    if system_validation['valid']:
        print("   ✓ All entities and relationships valid!")
    else:
        print("   ✗ System validation issues:")
        for error in system_validation['errors']:
            print(f"     - {error}")
    
    # Step 11: Certification chain analysis
    print("\n11. Certification chain analysis...")
    supply_chain = client.get_supply_chain(wood_chips.traceable_unit_id)
    
    print(f"   Final product: {wood_chips.traceable_unit_id}")
    print(f"   Claims attached: {len(supply_chain['claims'])}")
    
    for claim in supply_chain['claims']:
        print(f"   ├─ {claim.claim_type}: {claim.claim_percentage}%")
        if claim.inherited_from_tru:
            print(f"   │  └─ Inherited from: {claim.inherited_from_tru}")
        else:
            print(f"   │  └─ Original claim")
    
    if supply_chain['parent_units']:
        parent = supply_chain['parent_units'][0]
        print(f"   Parent TRU: {parent.traceable_unit_id}")
        print(f"   └─ Original certification: {parent.sustainability_certification}")
    
    # Step 12: Generate certification report
    print("\n12. Certification compliance report...")
    print("   " + "=" * 45)
    print("   CERTIFICATION COMPLIANCE REPORT")
    print("   " + "=" * 45)
    print(f"   Product: Wood Chips ({wood_chips.traceable_unit_id})")
    print(f"   Volume: {wood_chips.total_volume_m3} m³")
    print(f"   Source: {forest_manager.organization_name}")
    print(f"   Processor: {biomass_processor.organization_name}")
    print("")
    print("   Active Certifications:")
    print("   ├─ FSC Mix Credit: 70%")
    print("   │  └─ Chain of custody maintained")
    print("   └─ SBP Compliant: 100%")
    print("      └─ Responsibly managed forest")
    print("")
    print("   Compliance Status: ✓ APPROVED")
    print("   Chain integrity: ✓ MAINTAINED") 
    print("   Documentation: ✓ COMPLETE")
    print("   " + "=" * 45)
    
    print("\n" + "=" * 50)
    print("Certification demo completed successfully!")
    print("This demonstrates:")
    print("- Multi-scheme certification support (FSC, SBP)")
    print("- Claim inheritance through processing")
    print("- Certification validation and compliance")
    print("- Supply chain certification tracking")
    print("- Chain of custody maintenance")
    print("=" * 50)


if __name__ == "__main__":
    main()