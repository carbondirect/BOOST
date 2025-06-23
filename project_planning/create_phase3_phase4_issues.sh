#\!/bin/bash

set -e

REPO="carbondirect/BOOST"
PROJECT_ID="7"

echo "🚀 Creating Phase 2 final + Phase 3 + Phase 4 issues"

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

# Finish Phase 2
echo "📋 Phase 2 final issues"

create_issue_with_files \
    "Document known issues and gaps for resolution" \
    "Catalog and document any known issues, gaps, or limitations identified during development for future resolution." \
    "type:documentation,priority:medium" \
    "Drafting the Standard" \
    "- [project_planning/Version01.org](https://github.com/carbondirect/BOOST/blob/main/project_planning/Version01.org)"

create_issue_with_files \
    "Add comprehensive definitions and terminology section" \
    "Develop comprehensive glossary and terminology section defining all technical terms, biomass categories, sustainability concepts, and data relationships. Ensure alignment with existing standards and regulations for consistent interpretation." \
    "type:documentation,priority:critical" \
    "Drafting the Standard" \
    "- [drafts/BOOST_standard.tex](https://github.com/carbondirect/BOOST/blob/main/drafts/BOOST_standard.tex)
- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Create metadata requirements for versioning and provenance" \
    "Define metadata requirements for version tracking, data provenance, and change management throughout the data lifecycle." \
    "type:schema,priority:high" \
    "Drafting the Standard" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)"

create_issue_with_files \
    "Develop reference implementation examples in Python/JavaScript" \
    "Create working code examples demonstrating how to implement and use the BOOST standard in common programming languages." \
    "type:validation,priority:high" \
    "Drafting the Standard" \
    "- [drafts/scripts/boost_example_payload.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/boost_example_payload.json)"

create_issue_with_files \
    "Build validation rules and constraints for data integrity" \
    "Implement comprehensive validation rules and constraints to ensure data quality and integrity across all schema elements." \
    "type:validation,priority:high" \
    "Drafting the Standard" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)"

create_issue_with_files \
    "Document California LCFS compliance mapping" \
    "Create detailed mapping between BOOST data elements and California Low Carbon Fuel Standard requirements. Document how the standard supports LCFS reporting, verification, and compliance processes for biomass fuel pathways." \
    "type:integration,priority:critical" \
    "Drafting the Standard" \
    "- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)
- [drafts/TransactionSchema.md](https://github.com/carbondirect/BOOST/blob/main/drafts/TransactionSchema.md)"

# Phase 3 issues
echo ""
echo "📋 Phase 3: Community Review and Refinement"

create_issue_with_files \
    "Publish draft v0.0 to GitHub repository with documentation" \
    "Release the complete draft v0.0 specification to the public GitHub repository with full documentation, examples, and usage guidelines. Ensure all schemas, validation rules, and reference materials are accessible for community review." \
    "type:process,priority:critical" \
    "Community Review and Refinement" \
    "- [README.md](https://github.com/carbondirect/BOOST/blob/main/README.md)
- [drafts/BOOST_standard.tex](https://github.com/carbondirect/BOOST/blob/main/drafts/BOOST_standard.tex)"

create_issue_with_files \
    "Create structured feedback template for GitHub issues" \
    "Develop standardized templates and guidelines for collecting structured feedback during the community review process." \
    "type:process,priority:high" \
    "Community Review and Refinement" \
    "- [CONTRIBUTING.md](https://github.com/carbondirect/BOOST/blob/main/CONTRIBUTING.md)"

echo "✅ Created 8 more issues\! Total: 18"

