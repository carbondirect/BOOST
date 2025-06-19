#\!/bin/bash

set -e

REPO="carbondirect/BOOST"
PROJECT_ID="7"

echo "🚀 Creating final batch of issues to complete all 38"

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

# Continue Phase 3
echo "📋 Phase 3 continued"

create_issue_with_files \
    "Distribute review requests to working group and stakeholders" \
    "Coordinate distribution of review requests to all working group members, California agencies, certification bodies, and industry stakeholders. Provide structured review guidelines and feedback collection templates for comprehensive evaluation." \
    "type:review,priority:critical" \
    "Community Review and Refinement" \
    "- [meetings/kickoff_meeting.md](https://github.com/carbondirect/BOOST/blob/main/meetings/kickoff_meeting.md)
- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Host community review session for live Q&A and feedback" \
    "Organize and conduct live community review sessions for real-time feedback, questions, and discussion." \
    "type:review,priority:high" \
    "Community Review and Refinement" \
    "- [meetings/templates/meeting_template.md](https://github.com/carbondirect/BOOST/blob/main/meetings/templates/meeting_template.md)"

create_issue_with_files \
    "Collect and categorize all feedback by priority and impact" \
    "Systematically collect, organize, and prioritize all feedback received during the community review process." \
    "type:review,priority:high" \
    "Community Review and Refinement" \
    "- [CONTRIBUTING.md](https://github.com/carbondirect/BOOST/blob/main/CONTRIBUTING.md)"

create_issue_with_files \
    "Address critical feedback items that affect core functionality" \
    "Implement changes to address critical feedback that impacts core data model functionality, schema structure, or interoperability. Prioritize fixes that affect system integration, validation logic, or compliance requirements for v0.1 release readiness." \
    "type:validation,priority:critical" \
    "Community Review and Refinement" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)"

create_issue_with_files \
    "Test schema validation against California biomass use cases" \
    "Validate schema functionality using real California biomass supply chain scenarios including forestry residues, agricultural waste, and energy crops. Test data completeness, validation rules, and compliance reporting capabilities against actual use cases." \
    "type:validation,priority:critical" \
    "Community Review and Refinement" \
    "- [drafts/scripts/boost_example_payload.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/boost_example_payload.json)"

create_issue_with_files \
    "Validate SBP Data Transfer System compatibility" \
    "Ensure compatibility and interoperability with the SBP Data Transfer System for seamless integration." \
    "type:integration,priority:high" \
    "Community Review and Refinement" \
    "- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Update documentation based on usability feedback" \
    "Revise and improve documentation based on usability feedback received during community review." \
    "type:documentation,priority:high" \
    "Community Review and Refinement" \
    "- [drafts/BOOST_standard.tex](https://github.com/carbondirect/BOOST/blob/main/drafts/BOOST_standard.tex)
- [README.md](https://github.com/carbondirect/BOOST/blob/main/README.md)"

create_issue_with_files \
    "Create migration guide for existing systems" \
    "Develop comprehensive guide for migrating from existing biomass tracking systems to the BOOST standard." \
    "type:documentation,priority:medium" \
    "Community Review and Refinement" \
    "- [drafts/BOOST_standard.tex](https://github.com/carbondirect/BOOST/blob/main/drafts/BOOST_standard.tex)"

# Phase 4 issues
echo ""
echo "📋 Phase 4: Release Preparation and Publication"

create_issue_with_files \
    "Complete API documentation with usage examples" \
    "Finalize comprehensive API documentation including endpoint specifications, request/response examples, error handling, and integration patterns. Provide clear implementation guidance for developers adopting the BOOST standard in their systems." \
    "type:documentation,priority:critical" \
    "Release Preparation and Publication" \
    "- [drafts/BOOST_standard.tex](https://github.com/carbondirect/BOOST/blob/main/drafts/BOOST_standard.tex)"

create_issue_with_files \
    "Add versioning strategy and changelog for v0.1" \
    "Establish versioning strategy and create comprehensive changelog documenting all changes and improvements for the v0.1 release." \
    "type:documentation,priority:high" \
    "Release Preparation and Publication" \
    "- [project_planning/Version01.org](https://github.com/carbondirect/BOOST/blob/main/project_planning/Version01.org)"

echo "✅ Created 10 more issues\! Total: 28"

