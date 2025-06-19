#\!/bin/bash

set -e

REPO="carbondirect/BOOST"
PROJECT_ID="7"

echo "🚀 Creating remaining BOOST issues (Phase 2 continued)"

# Function to create issue with file links
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

# Continue Phase 2 issues
create_issue_with_files \
    "Draft JSON-LD/YAML-LD schema for Sustainability Information and claims" \
    "Create schemas for sustainability characteristics including certification claims, environmental data, source information, and compliance status. Link claims to specific consignments and enable claim verification and transfer mechanisms." \
    "type:schema,priority:critical" \
    "Drafting the Standard" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)
- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)
- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Draft Mass Balance Account tracking data structures" \
    "Define data structures for tracking volume balances and sustainability claims within organizations. Include account transactions, credit/debit tracking, claim allocation mechanisms, and reconciliation processes for managing certified vs controlled biomass volumes." \
    "type:schema,priority:high" \
    "Drafting the Standard" \
    "- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)
- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Create certification scheme integration patterns (FSC, PEFC, SBP)" \
    "Develop patterns for integrating with existing certification schemes including FSC, PEFC, and SBP standards." \
    "type:integration,priority:high" \
    "Drafting the Standard" \
    "- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)
- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Merge individual schemas into unified JSON-LD/YAML-LD context document" \
    "Integrate all individual entity schemas into a cohesive linked data context document. Ensure consistent naming conventions, resolve conflicts, and establish proper semantic relationships between all data elements for system interoperability." \
    "type:schema,priority:critical" \
    "Drafting the Standard" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)
- [drafts/scripts/boost_example_payload.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/boost_example_payload.json)"

create_issue_with_files \
    "Validate schema relationships and identify missing links" \
    "Review and validate all entity relationships in the schema to ensure logical consistency and identify any missing connections." \
    "type:validation,priority:high" \
    "Drafting the Standard" \
    "- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)"

create_issue_with_files \
    "Create sample data instances for each major entity type" \
    "Develop representative sample data instances for all major entity types to demonstrate schema usage and validate design." \
    "type:documentation,priority:high" \
    "Drafting the Standard" \
    "- [drafts/scripts/boost_example_payload.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/boost_example_payload.json)"

echo "✅ Created 7 more issues\! Total so far: 10"

