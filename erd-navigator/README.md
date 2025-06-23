# BOOST ERD Navigator

This directory contains an interactive Entity Relationship Diagram navigator for stakeholder feedback on the BOOST data standard.

## Purpose

The ERD Navigator provides a user-friendly interface for stakeholders to:
- View the complete BOOST entity relationship diagram
- Navigate directly to discussion threads for each entity
- Provide feedback without requiring GitHub repository access or version control knowledge

## Structure

- `index.html` - Main interactive page with ERD display and entity links
- Links to 16 entity-specific GitHub Discussions (#90-#105)
- Connected to corresponding GitHub Issues (#74-#89)

## Features

- **Visual Navigation**: Interactive ERD diagram showing all entities and relationships
- **Direct Links**: Click-through navigation to entity-specific discussion threads
- **Stakeholder Friendly**: No technical knowledge required
- **Mobile Responsive**: Works on all device sizes
- **Professional Styling**: GitHub-style design for consistency

## Access

The ERD Navigator is available at:
- **Live Site**: https://carbondirect.github.io/BOOST/erd-navigator/
- **Main Site**: https://carbondirect.github.io/BOOST/ (includes link to navigator)

## Entity Coverage

All 16 entities from the integrated ERD are included:
- Organization, CertificationScheme, Certificate, CertificationBody
- MaterialFeedstock, Supplier, Customer
- TransactionConsignment, TransactionBatch, Claim
- SaleDeliveryDocument, SAR, SREG
- VerificationStatement, MassBalanceAccount, ProductGroup

## Maintenance

This navigator is automatically updated when:
- ERD diagram changes (boost_erd.svg file updates)
- New discussions are created
- Entity schemas are modified

## ERD File Structure

The ERD is maintained as:
- `boost_erd.mermaid` - Source Mermaid script (edit this to update the diagram)
- `boost_erd.svg` - Generated SVG diagram (regenerate with `mmdc -i boost_erd.mermaid -o boost_erd.svg`)

The site integrates with the existing GitHub Pages setup without overriding the main specification page.