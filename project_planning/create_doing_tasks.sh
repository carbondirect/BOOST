#\!/bin/bash

set -e

REPO="carbondirect/BOOST"
PROJECT_ID="7"

echo "🚀 Creating 2 DOING tasks (in progress)"

create_issue_with_files() {
    local title="$1"
    local description="$2"
    local labels="$3"
    local milestone="$4"
    local file_links="$5"
    
    issue_body="$description"
    
    if [ -n "$file_links" ]; then
        issue_body="$issue_body

## Related Files
$file_links"
    fi
    
    if [ -n "$milestone" ]; then
        issue_body="$issue_body

**Milestone:** $milestone"
    fi
    
    echo "🔖 Creating: $title"
    issue_url=$(gh issue create --repo "$REPO" \
        --title "$title" \
        --body "$issue_body" \
        --label "$labels")
    
    gh project item-add "$PROJECT_ID" --owner carbondirect --url "$issue_url"
    
    if [ -n "$milestone" ]; then
        gh issue edit "$issue_url" --milestone "$milestone"
    fi
    
    echo "✅ Created: $issue_url"
}

# DOING tasks (in progress)
echo "📋 DOING tasks (work in progress)"

create_issue_with_files \
    "Define core data entities (Organizations, Consignments, Sustainability Info)" \
    "Establish the fundamental data objects that represent supply chain participants, biomass transactions, and sustainability characteristics. Define attributes, relationships, and constraints for each entity type to ensure comprehensive coverage of biomass chain of custody requirements.

## Work completed:
- drafts/scripts/biomass_coc_schema.json - Initial JSON schema with basic organization, producer, and recipient structures
- drafts/TransactionSchema.md - Harmonized data model identifying key attributes across certification programs  
- drafts/images/IntegratedERD.org - Textual description of integrated entity relationships from multiple standards

**Status:** Basic entity definitions exist but need expansion to full JSON-LD/YAML-LD schemas with complete attribute coverage." \
    "type:schema,priority:critical" \
    "Scoping and Alignment" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)
- [drafts/TransactionSchema.md](https://github.com/carbondirect/BOOST/blob/main/drafts/TransactionSchema.md)
- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)"

create_issue_with_files \
    "Draft JSON-LD/YAML-LD schema for Organization entities with roles and scope" \
    "Create machine-readable schemas defining organizations in the biomass supply chain including producers, processors, traders, and end users. Include roles, legal identifiers, certification status, and operational scope for comprehensive entity representation.

## Work completed:
- drafts/scripts/biomass_coc_schema.json - Basic organization schema with name, address, role, and certification fields
- drafts/images/IntegratedERD.org - Organization entity attributes including roles, scope, and certification details
- drafts/TransactionSchema.md - Organization-related data elements across multiple certification programs

**Status:** Initial organization schema exists but needs expansion to full JSON-LD format with linked data context and comprehensive attribute coverage." \
    "type:schema,priority:critical" \
    "Drafting the Standard" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)
- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)
- [drafts/TransactionSchema.md](https://github.com/carbondirect/BOOST/blob/main/drafts/TransactionSchema.md)"

echo "✅ Created 2 DOING tasks\!"
echo "🎉 Grand total: 40 issues (38 TODO + 2 DOING)"

