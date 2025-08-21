# BOOST Project Writing Style Guide

This document serves as a context file for maintaining consistent writing style across the BOOST project, based on the Interagency Chain of Custody Report template.

## Document Structure and Hierarchy

### Header Conventions
- **Document Title**: Use bold formatting for primary document titles
- **Major Sections**: Use `# **Section Name**` with bold formatting and `{#anchor}` IDs
- **Subsections**: Follow hierarchical numbering with consistent formatting:
  - `## Section {#anchor}`
  - `### Subsection`
  - `#### **Bold Subsection Title**`
  - `##### **Background/CoC Specifications/etc.**`
  - `###### **Table/Figure Numbers**`

### Table and Figure Formatting
- Tables: Use `###### **Table X.** Description` format
- Figures: Use `###### **Figure X.** Description` format  
- Include descriptive captions that explain the content and context
- Use consistent pipe table formatting with left-aligned headers

### Cross-References and Anchors
- Include `{#anchor-name}` for all major sections to enable cross-referencing
- Use descriptive anchor names that match section content
- Reference other sections using standard markdown links where appropriate

## Writing Tone and Style

### Professional Academic Tone
- Use formal, professional language appropriate for government and industry stakeholders
- Maintain objectivity while presenting findings and recommendations
- Balance technical precision with accessibility for diverse audiences

### Sentence Structure
- **Complex sentences**: Use sophisticated sentence structures that connect multiple ideas
- **Example**: "The project employed a multi-method approach to balance technical rigor with practical applicability, beginning with a meta-analysis of existing biomass tracking systems and CoC models, including a comprehensive review of relevant national and international policies and standards."
- **Parallel structure**: Use consistent grammatical patterns in lists and series
- **Subordinate clauses**: Employ dependent clauses to provide context and nuance

### Paragraph Development
- **Lead with topic sentences** that introduce the main concept
- **Support with evidence**: Follow with specific examples, stakeholder quotes, and data
- **Connect ideas**: Use transitional phrases to link concepts within and between paragraphs
- **Conclude with implications**: End paragraphs by explaining significance or next steps

### Technical Language and Terminology
- **Define acronyms** on first use, then use consistently throughout
- **Use domain-specific terminology** accurately (CoC, biomass, traceability, etc.)
- **Include technical precision** while maintaining readability
- **Provide context** for technical concepts when introducing them

## Content Organization Patterns

### Stakeholder Analysis Framework
When presenting stakeholder perspectives, use this structure:
1. **Cross-stakeholder key findings and CoC implications** - overarching themes
2. **Stakeholder-Specific Insights** - detailed perspectives by group:
   - Biomass Certification & Operations Experts
   - Biomass Supply-Chain Experts  
   - Biomass Reporting Stakeholders
   - NGO and Tribal Community Stakeholders
   - California State Agencies
3. **Chain of Custody Design Considerations** - synthesis and implications

### Program Analysis Framework
For policy/program analysis, follow this pattern:
1. **Background** - context, purpose, scope
2. **CoC Specifications** - technical requirements and implementation details
3. **Implications** - relevance to BOOST development

### Recommendations Structure
- **Lead with methodology** explaining how recommendations were developed
- **Present specific actionable items** using bold headings for each recommendation
- **Include implementation details** with phases, timelines, and stakeholder roles
- **Connect to broader goals** showing alignment with policy objectives

## Language Conventions

### Voice and Perspective
- Use **active voice** predominantly: "The project employed..." rather than "Was employed by the project..."
- Use **third person** perspective for objectivity
- Include **direct stakeholder quotes** in italics with proper attribution
- Use **we/our** only when referring to the research team's actions or recommendations

### Precision and Clarity
- **Quantify where possible**: Use specific numbers, percentages, and measurements
- **Qualify statements appropriately**: Use "potentially," "likely," "indicates" when appropriate
- **Distinguish between findings and recommendations**: Clear separation between what was discovered and what is proposed
- **Use evidence-based language**: Support claims with data, quotes, or documented sources

### Common Phrases and Transitions
- "Drawing on these findings..." (transitioning to recommendations)
- "Stakeholder interviews underscored that..." (introducing key themes)
- "If implemented, this system could..." (describing potential benefits)
- "The rationale for [X] rests on..." (explaining justification)
- "Based on our analysis, we recommend..." (presenting recommendations)

## Formatting Standards

### Lists and Bullets
- Use **bullet points** for unstructured lists
- Use **numbered lists** for sequential processes or phases
- Use **bold headings** within lists for emphasis
- Maintain **parallel structure** across list items

### Emphasis and Highlighting
- **Bold** for section headings, key terms, and important concepts
- ***Bold italics*** for critical stakeholder quotes or key findings
- *Italics* for emphasis within text and direct quotes
- `Monospace` for technical terms, data fields, or code elements

### Citations and References
- Include placeholder sections for References and supporting materials
- Use descriptive in-text references to tables, figures, and appendices
- Maintain consistent formatting for external document references

## Content Integration Guidelines

### Stakeholder Voice Integration
- **Quote extensively** from stakeholder interviews to support findings
- **Attribute perspectives** to specific stakeholder groups
- **Use quotes strategically** to illustrate key points and add credibility
- **Balance different viewpoints** while identifying common themes

### Data and Evidence Presentation
- **Lead with qualitative themes**, support with quantitative data where available
- **Use tables effectively** to compare systems, requirements, or findings
- **Integrate visual elements** (figures, diagrams) to clarify complex concepts
- **Reference appendices** for detailed supporting information

### Regulatory and Policy Context
- **Ground recommendations** in existing regulatory frameworks
- **Show alignment** with policy objectives and requirements  
- **Address compliance needs** throughout the analysis
- **Consider implementation feasibility** within existing systems

This style guide should be used as a template for all BOOST project documentation to ensure consistency with the professional, comprehensive approach established in the Interagency Chain of Custody Report.

## Build Architecture Awareness

The BOOST project uses a **unified documentation build system** where JSON schemas serve as the authoritative source for all entity documentation. Understanding and adhering to this architecture is critical for maintaining consistency across all documentation formats.

### Schema-First Development Workflow

**ALWAYS follow this sequence when making documentation changes:**

1. **JSON Schemas are Authoritative**: All entity documentation is generated from JSON schemas located in `/drafts/current/schema/[entity]/validation_schema.json`
2. **Never Edit Generated Content Directly**: Do not modify:
   - LaTeX tables in `tex/entities/[entity]-table.tex`
   - Bikeshed includes in `includes/generated/[entity].inc.md`
   - Generated thematic sections in `tex/[theme]-entities.tex`
3. **Update Schemas First**: Make changes to the JSON schemas, then regenerate documentation
4. **Use Unified Build Process**: Always use `./build.sh` for documentation generation
5. **Validate Consistency**: Run consistency checks after any schema or documentation updates

### Required Build Commands

**For Documentation Generation:**
```bash
# Generate documentation from schemas
python3 scripts/generate-latex-from-schemas.py

# Build HTML and/or PDF documentation
./build.sh [--html|--pdf|--help]

# Validate consistency across formats
python3 scripts/validate-consistency.py
```

**Before Any Documentation Commits:**
```bash
# Always run full validation
python3 scripts/validate-consistency.py --strict
# Target consistency score: 100%
```

### Documentation-Consistency-Reviewer Agent Integration

When making substantial documentation changes, particularly those affecting multiple entities or cross-references:

1. **Invoke the documentation-consistency-reviewer agent** for cross-format validation
2. **Validate schema-to-documentation pipeline integrity**
3. **Ensure consistency between HTML (Bikeshed) and PDF (LaTeX) outputs**
4. **Check for missing or orphaned entity documentation**

### Critical Architecture Rules

**DO:**
- ✅ Update JSON schemas as the primary source of truth
- ✅ Use `./build.sh` for all documentation generation
- ✅ Run consistency validation before committing changes  
- ✅ Invoke documentation-consistency-reviewer agent for complex changes
- ✅ Follow the schema-first development workflow
- ✅ Validate that all 35+ entities are properly documented across formats

**DON'T:**
- ❌ Edit generated LaTeX tables or Bikeshed includes directly
- ❌ Commit documentation changes without running consistency validation
- ❌ Add entities to documentation without corresponding JSON schemas
- ❌ Skip the unified build process for "quick fixes"
- ❌ Ignore consistency validation failures (target: 100% consistency score)

### Build System Health Monitoring

The build system includes automated consistency validation that should always pass:
- **Target consistency score**: 100%
- **Total documented entities**: Must match schema count (currently 35+)
- **Cross-format alignment**: HTML and PDF must contain identical entity coverage
- **No orphaned content**: All documented entities must have corresponding schemas

### Integration with Existing Style Guidelines

These build architecture requirements complement the writing style guidelines above. When following the professional academic tone and formatting standards, always ensure that content changes flow through the proper schema-first development workflow to maintain the single source of truth principle that ensures consistency across all BOOST project documentation formats.