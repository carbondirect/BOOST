#\!/bin/bash

set -e

REPO="carbondirect/BOOST"
PROJECT_ID="7"
ORG_FILE="/Users/peter/src/BOOST/project_planning/Version01.org"

echo "🚀 Creating all BOOST issues with file links"
echo "Repository: $REPO"
echo "Project: #$PROJECT_ID"
echo "----------------------------------------"

# Function to create issue with file links
create_issue_with_files() {
    local title="$1"
    local description="$2"
    local labels="$3"
    local milestone="$4"
    local file_links="$5"
    
    # Build issue body with file links
    issue_body="$description"
    
    if [ -n "$file_links" ]; then
        issue_body="$issue_body

## Related Files
$file_links"
    fi
    
    # Add milestone info
    if [ -n "$milestone" ]; then
        issue_body="$issue_body

**Milestone:** $milestone"
    fi
    
    echo "🔖 Creating: $title"
    issue_url=$(gh issue create --repo "$REPO" \
        --title "$title" \
        --body "$issue_body" \
        --label "$labels")
    
    # Add to project
    gh project item-add "$PROJECT_ID" --owner carbondirect --url "$issue_url"
    
    # Assign to milestone if specified
    if [ -n "$milestone" ]; then
        gh issue edit "$issue_url" --milestone "$milestone"
    fi
    
    echo "✅ Created: $issue_url"
}

# Phase 1: Scoping and Alignment
echo ""
echo "📋 Phase 1: Scoping and Alignment"

create_issue_with_files \
    "Settle on JSON-LD/YAML-LD as serialization formats with schema structure principles" \
    "Establish technical architecture decisions including data format, schema validation approach, extensibility patterns, and linked data principles. Define how the standard will support interoperability and future enhancements." \
    "type:process,priority:critical" \
    "Scoping and Alignment" \
    "- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)
- [drafts/TransactionSchema.md](https://github.com/carbondirect/BOOST/blob/main/drafts/TransactionSchema.md)"

create_issue_with_files \
    "Define review milestones and feedback collection process" \
    "Establish structured process for collecting and managing feedback during community review phases." \
    "type:process,priority:medium" \
    "Scoping and Alignment" \
    "- [meetings/templates/meeting_template.md](https://github.com/carbondirect/BOOST/blob/main/meetings/templates/meeting_template.md)
- [CONTRIBUTING.md](https://github.com/carbondirect/BOOST/blob/main/CONTRIBUTING.md)"

# Phase 2: Drafting the Standard  
echo ""
echo "📋 Phase 2: Drafting the Standard"

create_issue_with_files \
    "Draft JSON-LD/YAML-LD schema for Consignment transactions (incoming/outgoing)" \
    "Define schema for biomass transfer transactions including quantities, dates, sustainability claims, documentation references, and chain of custody linkages. Support both incoming and outgoing consignments with full traceability data." \
    "type:schema,priority:critical" \
    "Drafting the Standard" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)
- [drafts/TransactionSchema.md](https://github.com/carbondirect/BOOST/blob/main/drafts/TransactionSchema.md)
- [drafts/images/IntegratedERD.org](https://github.com/carbondirect/BOOST/blob/main/drafts/images/IntegratedERD.org)"

echo "✅ Sample issues created with file links\!"
echo "🔗 Continue with remaining 35 issues..."

