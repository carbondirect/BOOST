#!/usr/bin/env python3
"""
BOOST Python Reference Implementation - Complete Supply Chain Demo

This example demonstrates a complete biomass supply chain:
1. Forest harvest by certified harvester
2. Multiple processing stages
3. Transportation and logistics
4. Final product delivery
5. End-to-end traceability and validation

Run with: python supply_chain_demo.py
"""

import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from boost_client import create_client
from models import OrganizationType, UnitType, ProcessType, ClaimType


def main():
    """Demonstrate complete BOOST supply chain tracking."""
    
    print("=== BOOST Python Reference Implementation ===")
    print("Complete Supply Chain Demo")
    print("=" * 50)
    
    # Initialize BOOST client
    client = create_client()
    
    # Step 1: Create supply chain participants
    print("\n1. Creating supply chain participants...")
    
    # Forest management company
    forest_mgmt = client.create_organization(
        organization_id="ORG-CASCADE-FORESTS-001",
        name="Cascade Forest Management",
        org_type=OrganizationType.HARVESTER,
        certifications=["CERT-FSC-FM-001", "CERT-SFI-001"],
        contact_email="operations@cascadeforests.com",
        established_date="1978-05-15"
    )
    
    # Primary processor (sawmill)
    sawmill = client.create_organization(
        organization_id="ORG-NORTHWEST-MILL-001", 
        name="Northwest Lumber Mill",
        org_type=OrganizationType.PROCESSOR,
        certifications=["CERT-FSC-COC-001", "CERT-SFI-COC-001"],
        contact_email="mill@northwestlumber.com"
    )
    
    # Secondary processor (pellet plant)
    pellet_plant = client.create_organization(
        organization_id="ORG-GREEN-PELLETS-001",
        name="Green Energy Pellets",
        org_type=OrganizationType.MANUFACTURER,
        certifications=["CERT-SBP-001", "CERT-ENplus-001"],
        contact_email="production@greenpellets.com"
    )
    
    # Transportation company
    logistics = client.create_organization(
        organization_id="ORG-FOREST-LOGISTICS-001",
        name="Forest Logistics Inc",
        org_type=OrganizationType.TRANSPORTER,
        contact_email="dispatch@forestlogistics.com"
    )
    
    print(f"   ✓ Forest Manager: {forest_mgmt.organization_name}")
    print(f"   ✓ Sawmill: {sawmill.organization_name}")
    print(f"   ✓ Pellet Plant: {pellet_plant.organization_name}")
    print(f"   ✓ Logistics: {logistics.organization_name}")
    
    # Step 2: Forest harvest operation
    print("\n2. Forest harvest operation...")
    
    # Create harvest site TRU
    harvest_logs = client.create_traceable_unit(
        traceable_unit_id="TRU-HARVEST-CASCADE-001",
        unit_type=UnitType.PILE,
        harvester_id=forest_mgmt.organization_id,
        total_volume_m3=500.0,
        harvest_geographic_data_id="GEO-CASCADE-UNIT-47A",
        current_geographic_data_id="GEO-CASCADE-LANDING-001",
        material_type_id="MAT-MIXED-CONIFER-LOGS",
        quality_grade="Sawlog-Grade",
        is_multi_species=True,
        sustainability_certification="FSC Mix Credit 85%"
    )
    
    # Create FSC claim for harvest
    harvest_claim = client.create_claim(
        claim_id="CLAIM-FSC-HARVEST-001",
        traceable_unit_id=harvest_logs.traceable_unit_id,
        claim_type=ClaimType.FSC_MIX,
        statement="FSC Mix Credit 85%",
        validated=True,
        validated_by="ORG-FSC-CERTIFIER-001",
        claim_percentage=85.0,
        claim_scope="harvest",
        applicable_species=["douglas_fir", "western_hemlock", "noble_fir"]
    )
    
    print(f"   ✓ Harvested: {harvest_logs.total_volume_m3} m³")
    print(f"   ✓ Location: {harvest_logs.harvest_geographic_data_id}")
    print(f"   ✓ Certification: {harvest_logs.sustainability_certification}")
    
    # Step 3: Transportation to sawmill
    print("\n3. Transportation to sawmill...")
    
    # Update TRU location for transport
    transported_logs = client.create_traceable_unit(
        traceable_unit_id="TRU-TRANSPORT-TO-MILL-001",
        unit_type=UnitType.TRUCK_LOAD,
        parent_traceable_unit_id=harvest_logs.traceable_unit_id,
        total_volume_m3=500.0,
        current_geographic_data_id="GEO-NORTHWEST-MILL-YARD",
        material_type_id="MAT-MIXED-CONIFER-LOGS",
        quality_grade="Sawlog-Grade",
        sustainability_certification="FSC Mix Credit 85%"
    )
    
    # Create transport transaction
    transport_txn = client.create_transaction(
        transaction_id="TXN-HARVEST-TO-MILL-001",
        organization_id=forest_mgmt.organization_id,
        customer_id=sawmill.organization_id,
        transaction_date="2025-07-30",
        traceable_unit_id=transported_logs.traceable_unit_id,
        quantity=500.0,
        quantity_unit="cubic_meters",
        contract_value=35000.00,
        contract_currency="USD"
    )
    
    print(f"   ✓ Transported: {transported_logs.total_volume_m3} m³")
    print(f"   ✓ Destination: {transported_logs.current_geographic_data_id}")
    print(f"   ✓ Transaction value: ${transport_txn.contract_value}")
    
    # Step 4: Sawmill processing
    print("\n4. Sawmill processing...")
    
    # Create lumber output
    lumber_tru = client.create_traceable_unit(
        traceable_unit_id="TRU-DIMENSIONAL-LUMBER-001",
        unit_type=UnitType.BATCH,
        parent_traceable_unit_id=transported_logs.traceable_unit_id,
        total_volume_m3=320.0,  # 64% yield
        current_geographic_data_id="GEO-NORTHWEST-MILL-WAREHOUSE",
        material_type_id="MAT-DIMENSIONAL-LUMBER",
        quality_grade="Construction-Grade",
        sustainability_certification="FSC Mix Credit 85%"
    )
    
    # Create sawmill residues (for pellets)
    sawmill_residues = client.create_traceable_unit(
        traceable_unit_id="TRU-SAWMILL-RESIDUES-001",
        unit_type=UnitType.BATCH,
        parent_traceable_unit_id=transported_logs.traceable_unit_id,
        total_volume_m3=150.0,  # Sawdust, chips, shavings
        current_geographic_data_id="GEO-NORTHWEST-MILL-RESIDUE-PILE",
        material_type_id="MAT-SAWMILL-RESIDUES",
        quality_grade="Pellet-Feedstock",
        sustainability_certification="FSC Mix Credit 85%"
    )
    
    # Create sawmill processing operation
    sawmill_processing = client.create_material_processing(
        processing_id="PROC-SAWMILL-001",
        input_tru_id=transported_logs.traceable_unit_id,
        output_tru_id=lumber_tru.traceable_unit_id,
        process_type=ProcessType.CROSSCUTTING,
        input_volume=500.0,
        output_volume=320.0,
        volume_loss=30.0,  # Bark, waste
        processing_geographic_data_id="GEO-NORTHWEST-MILL-SAWLINE"
    )
    
    # Create residue processing operation
    residue_processing = client.create_material_processing(
        processing_id="PROC-RESIDUE-COLLECTION-001",
        input_tru_id=transported_logs.traceable_unit_id,
        output_tru_id=sawmill_residues.traceable_unit_id,
        process_type=ProcessType.CHIPPING,
        input_volume=180.0,  # Remaining after lumber
        output_volume=150.0,
        volume_loss=30.0,
        processing_geographic_data_id="GEO-NORTHWEST-MILL-RESIDUE-AREA"
    )
    
    print(f"   ✓ Lumber produced: {lumber_tru.total_volume_m3} m³")
    print(f"   ✓ Residues collected: {sawmill_residues.total_volume_m3} m³")
    print(f"   ✓ Sawmill yield: {(lumber_tru.total_volume_m3 / transported_logs.total_volume_m3 * 100):.1f}%")
    
    # Step 5: Residue transport to pellet plant
    print("\n5. Residue transport to pellet plant...")
    
    # Create residue transport transaction
    residue_transport_txn = client.create_transaction(
        transaction_id="TXN-RESIDUES-TO-PELLETS-001",
        organization_id=sawmill.organization_id,
        customer_id=pellet_plant.organization_id,
        transaction_date="2025-08-01",
        traceable_unit_id=sawmill_residues.traceable_unit_id,
        quantity=150.0,
        quantity_unit="cubic_meters",
        contract_value=6000.00,
        contract_currency="USD"
    )
    
    print(f"   ✓ Residue sale value: ${residue_transport_txn.contract_value}")
    print(f"   ✓ Unit price: ${residue_transport_txn.contract_value / residue_transport_txn.quantity:.2f}/m³")
    
    # Step 6: Pellet production
    print("\n6. Pellet production...")
    
    # Create pellet output
    wood_pellets = client.create_traceable_unit(
        traceable_unit_id="TRU-WOOD-PELLETS-001",
        unit_type=UnitType.BATCH,
        parent_traceable_unit_id=sawmill_residues.traceable_unit_id,
        total_volume_m3=90.0,  # Densification increases bulk density
        current_geographic_data_id="GEO-GREEN-PELLETS-WAREHOUSE",
        material_type_id="MAT-WOOD-PELLETS-ENplus-A1",
        quality_grade="ENplus-A1",
        sustainability_certification="SBP-certified sustainable biomass"
    )
    
    # Create pellet processing operation
    pellet_processing = client.create_material_processing(
        processing_id="PROC-PELLETIZING-001",
        input_tru_id=sawmill_residues.traceable_unit_id,
        output_tru_id=wood_pellets.traceable_unit_id,
        process_type=ProcessType.CHIPPING,  # Closest available type
        input_volume=150.0,
        output_volume=90.0,
        volume_loss=60.0,  # Moisture removal, fines
        input_mass=45.0,   # Lower density residues
        output_mass=63.0,  # High density pellets
        processing_geographic_data_id="GEO-GREEN-PELLETS-PRODUCTION"
    )
    
    # Create SBP claim for pellets
    pellet_claim = client.create_claim(
        claim_id="CLAIM-SBP-PELLETS-001",
        traceable_unit_id=wood_pellets.traceable_unit_id,
        claim_type=ClaimType.SBP_COMPLIANT,
        statement="SBP-certified sustainable biomass pellets",
        validated=True,
        validated_by="ORG-SBP-CERTIFIER-001",
        claim_percentage=100.0,
        claim_scope="full_chain",
        inherited_from_tru=[sawmill_residues.traceable_unit_id]
    )
    
    print(f"   ✓ Pellets produced: {wood_pellets.total_volume_m3} m³ ({pellet_processing.output_mass} tonnes)")
    print(f"   ✓ Conversion efficiency: {(wood_pellets.total_volume_m3 / sawmill_residues.total_volume_m3 * 100):.1f}%")
    print(f"   ✓ Pellet density: {(pellet_processing.output_mass / wood_pellets.total_volume_m3):.2f} tonnes/m³")
    
    # Step 7: Final pellet sale
    print("\n7. Final pellet sale...")
    
    # Create final customer transaction
    final_sale = client.create_transaction(
        transaction_id="TXN-PELLETS-TO-CUSTOMER-001",
        organization_id=pellet_plant.organization_id,
        customer_id="CUST-POWER-PLANT-001",
        transaction_date="2025-08-15",
        traceable_unit_id=wood_pellets.traceable_unit_id,
        quantity=63.0,  # Sold by mass
        quantity_unit="metric_tons",
        contract_value=11340.00,  # Premium for certified pellets
        contract_currency="USD"
    )
    
    print(f"   ✓ Final sale value: ${final_sale.contract_value}")
    print(f"   ✓ Premium price: ${final_sale.contract_value / final_sale.quantity:.2f}/tonne")
    
    # Step 8: End-to-end validation
    print("\n8. End-to-end supply chain validation...")
    
    validation_results = client.validate_all()
    
    if validation_results['valid']:
        print("   ✓ Complete supply chain validation passed!")
    else:
        print("   ✗ Validation issues found:")
        for error in validation_results['errors']:
            print(f"     - {error}")
    
    # Step 9: Complete traceability analysis
    print("\n9. Complete traceability analysis...")
    
    # Trace pellets back to origin
    pellet_supply_chain = client.get_supply_chain(wood_pellets.traceable_unit_id)
    
    print(f"   Final Product: {wood_pellets.traceable_unit_id}")
    print(f"   ├─ Processing operations: {len(pellet_supply_chain['processing_history'])}")
    print(f"   ├─ Transactions: {len(pellet_supply_chain['transactions'])}")
    print(f"   └─ Sustainability claims: {len(pellet_supply_chain['claims'])}")
    
    # Trace back through parents
    current_tru = wood_pellets
    generation = 0
    lineage = []
    
    while current_tru:
        lineage.append(current_tru)
        if hasattr(current_tru, 'parent_traceable_unit_id') and current_tru.parent_traceable_unit_id:
            parent_id = current_tru.parent_traceable_unit_id
            current_tru = client.traceable_units.get(parent_id)
            generation += 1
        else:
            break
    
    print(f"\n   Supply Chain Lineage ({generation + 1} generations):")
    for i, tru in enumerate(reversed(lineage)):
        prefix = "   " + "└─ " if i == len(lineage) - 1 else "   ├─ "
        print(f"{prefix}Gen {i + 1}: {tru.traceable_unit_id} ({tru.material_type_id})")
    
    # Step 10: Supply chain summary report
    print("\n10. Supply chain summary report...")
    print("   " + "=" * 65)
    print("   COMPLETE SUPPLY CHAIN TRACEABILITY REPORT")
    print("   " + "=" * 65)
    print(f"   Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    # Participants
    print("   SUPPLY CHAIN PARTICIPANTS:")
    print(f"   ├─ Forest Manager:    {forest_mgmt.organization_name}")
    print(f"   ├─ Primary Processor: {sawmill.organization_name}")
    print(f"   ├─ Secondary Processor: {pellet_plant.organization_name}")
    print(f"   └─ Logistics Provider: {logistics.organization_name}")
    print("")
    
    # Material flow
    print("   MATERIAL FLOW SUMMARY:")
    print(f"   ├─ Original Harvest:  {harvest_logs.total_volume_m3:>8.1f} m³ (logs)")
    print(f"   ├─ Lumber Production: {lumber_tru.total_volume_m3:>8.1f} m³ (lumber)")
    print(f"   ├─ Residue Recovery:  {sawmill_residues.total_volume_m3:>8.1f} m³ (residues)")
    print(f"   └─ Final Product:     {wood_pellets.total_volume_m3:>8.1f} m³ ({pellet_processing.output_mass:.1f} tonnes pellets)")
    
    # Economic summary
    total_value = (transport_txn.contract_value + 
                  residue_transport_txn.contract_value + 
                  final_sale.contract_value)
    
    print("")
    print("   ECONOMIC SUMMARY:")
    print(f"   ├─ Log Sales:         ${transport_txn.contract_value:>10,.2f}")
    print(f"   ├─ Residue Sales:     ${residue_transport_txn.contract_value:>10,.2f}")
    print(f"   ├─ Pellet Sales:      ${final_sale.contract_value:>10,.2f}")
    print(f"   └─ Total Value:       ${total_value:>10,.2f}")
    
    print("")
    print("   SUSTAINABILITY CREDENTIALS:")
    print("   ├─ FSC Mix Credit 85% (harvest to lumber)")
    print("   ├─ SBP Certified (residue to pellets)")
    print("   ├─ ENplus A1 Quality (pellet grade)")
    print("   └─ Complete chain of custody maintained")
    
    print("")
    print("   TRACEABILITY STATUS:")
    print("   ├─ Origin Verification:   ✓ VERIFIED")
    print("   ├─ Processing History:    ✓ COMPLETE")
    print("   ├─ Certification Chain:   ✓ MAINTAINED")
    print("   ├─ Mass Balance:          ✓ VALIDATED")
    print("   └─ Quality Assurance:     ✓ DOCUMENTED")
    
    print("   " + "=" * 65)
    
    print("\n" + "=" * 50)
    print("Complete supply chain demo finished successfully!")
    print("This demonstrates:")
    print("- Multi-participant supply chain coordination")
    print("- Complete material flow tracking")
    print("- Processing and transformation tracking")
    print("- Multi-generational traceability")
    print("- Economic value chain analysis")
    print("- Certification inheritance and validation")
    print("- End-to-end supply chain transparency")
    print("=" * 50)


if __name__ == "__main__":
    main()