#\!/bin/bash

set -e

REPO="carbondirect/BOOST"
PROJECT_ID="7"

echo "🚀 Creating final 10 issues to complete all 38"

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

# Final Phase 4 issues
echo "📋 Phase 4 final issues"

create_issue_with_files \
    "Create comprehensive test suite with validation examples" \
    "Develop complete test suite with comprehensive validation examples for all schema components and use cases." \
    "type:validation,priority:high" \
    "Release Preparation and Publication" \
    "- [drafts/scripts/biomass_coc_schema.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/biomass_coc_schema.json)
- [drafts/scripts/boost_example_payload.json](https://github.com/carbondirect/BOOST/blob/main/drafts/scripts/boost_example_payload.json)"

create_issue_with_files \
    "Conduct final working group review meeting" \
    "Host final working group meeting to review the complete v0.1 specification, address any remaining concerns, and ensure consensus on release readiness. Document final decisions and prepare for formal approval vote." \
    "type:review,priority:critical" \
    "Release Preparation and Publication" \
    "- [meetings/templates/meeting_template.md](https://github.com/carbondirect/BOOST/blob/main/meetings/templates/meeting_template.md)
- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Approve v0.1 release with formal working group vote" \
    "Conduct formal working group vote to approve the v0.1 standard for public release. Follow W3C Community Group consensus procedures and document the decision with any dissenting opinions or conditions for future versions." \
    "type:process,priority:critical" \
    "Release Preparation and Publication" \
    "- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Share pre-release with California agencies (PUC, IOUs)" \
    "Distribute pre-release version to California Public Utilities Commission and Investor-Owned Utilities for final stakeholder review." \
    "type:review,priority:high" \
    "Release Preparation and Publication" \
    "- [meetings/kickoff_meeting.md](https://github.com/carbondirect/BOOST/blob/main/meetings/kickoff_meeting.md)"

create_issue_with_files \
    "Distribute to certification bodies (FSC, PEFC, SBP) for review" \
    "Share pre-release with major certification bodies for final compatibility review and feedback." \
    "type:review,priority:high" \
    "Release Preparation and Publication" \
    "- [BOOST_Charter.org](https://github.com/carbondirect/BOOST/blob/main/BOOST_Charter.org)"

create_issue_with_files \
    "Collect any last-minute critical feedback" \
    "Gather and address any final critical feedback from stakeholders before public release." \
    "type:review,priority:medium" \
    "Release Preparation and Publication" \
    "- [CONTRIBUTING.md](https://github.com/carbondirect/BOOST/blob/main/CONTRIBUTING.md)"

create_issue_with_files \
    "Publish v0.1 specification to GitHub with release notes" \
    "Execute the official v0.1 release including GitHub release creation, version tagging, and comprehensive release notes. Ensure all documentation, schemas, examples, and tools are properly packaged and accessible to the public." \
    "type:process,priority:critical" \
    "Release Preparation and Publication" \
    "- [README.md](https://github.com/carbondirect/BOOST/blob/main/README.md)
- [drafts/BOOST_standard.tex](https://github.com/carbondirect/BOOST/blob/main/drafts/BOOST_standard.tex)"

create_issue_with_files \
    "Create W3C Community Group announcement and summary" \
    "Draft and publish official W3C Community Group announcement summarizing the v0.1 release, key features, implementation guidance, and next steps. Communicate the standard's value proposition and adoption pathway to the broader community." \
    "type:documentation,priority:critical" \
    "Release Preparation and Publication" \
    "- [README.md](https://github.com/carbondirect/BOOST/blob/main/README.md)
- [w3c.json](https://github.com/carbondirect/BOOST/blob/main/w3c.json)"

create_issue_with_files \
    "Share on public mailing list with implementation guidance" \
    "Announce the v0.1 release on public mailing lists with comprehensive implementation guidance and adoption resources." \
    "type:process,priority:high" \
    "Release Preparation and Publication" \
    "- [README.md](https://github.com/carbondirect/BOOST/blob/main/README.md)"

create_issue_with_files \
    "Set up feedback collection process for post-release improvements" \
    "Establish ongoing feedback collection and improvement processes for future versions of the standard." \
    "type:process,priority:medium" \
    "Release Preparation and Publication" \
    "- [CONTRIBUTING.md](https://github.com/carbondirect/BOOST/blob/main/CONTRIBUTING.md)"

echo "✅ Created final 10 issues\!"
echo "🎉 Total issues created: 38 (all TODO/DOING tasks)"

