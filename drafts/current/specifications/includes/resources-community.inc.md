# Resources & Community # {#resources-community}

This section provides access to BOOST presentations, working group documentation, and community resources.

## Presentations & Demonstrations ## {#presentations}

### Core Presentations ### {#core-presentations}

<div class="presentation-grid">

**BOOST Kickoff Presentation**
Overview of the BOOST data standard initiative, project goals, and working group approach.
<a href="../presentations/boost_kickoff.html" class="presentation-link">View Presentation →</a>

**Transaction Object Examples** 
Technical demonstration of data structures and transaction examples in the BOOST standard.
<a href="../presentations/transaction_object_examples.html" class="presentation-link">View Examples →</a>

</div>

### Agency Engagement ### {#agency-engagement}

Presentations developed for California state agencies to demonstrate BOOST applicability and gather feedback.

<div class="presentation-grid">

**CalRecycle Engagement**
BOOST presentation for California Department of Resources Recycling and Recovery, covering biomass conversion, SB 498 reporting, and waste diversion systems.
<a href="../presentations/ae_calrecycle.html" class="presentation-link">View Presentation →</a>

**CDFA Engagement**
BOOST presentation for California Department of Food and Agriculture, exploring agricultural biomass traceability and potential pilot development opportunities.
<a href="../presentations/ae_cdfa.html" class="presentation-link">View Presentation →</a>

**Department of Conservation**
BOOST presentation for California Department of Conservation, focusing on forest management data standards and conservation tracking requirements.
<a href="../presentations/ae_doc.html" class="presentation-link">View Presentation →</a>

</div>

### Standards & Technical ### {#standards-technical}

Technical presentations exploring BOOST integration with existing regulatory frameworks and standards.

<div class="presentation-grid">

**BOOST + LCFS Integration**
Technical presentation on BOOST integration with California's Low Carbon Fuel Standard (LCFS), covering relevant entities and chain of custody requirements.
<a href="../presentations/st_lcfs.html" class="presentation-link">View Presentation →</a>

</div>

## Interactive Tools ## {#interactive-tools}

### Entity Relationship Diagram Navigator ### {#erd-navigator-section}

Explore the complete BOOST data model through the interactive ERD Navigator, featuring all 33 entities across 7 thematic areas.

**[Interactive ERD Navigator](erd-navigator/index.html)**

The ERD Navigator provides:
- Interactive visualization of all entity relationships
- Schema-based field definitions and validation rules  
- Thematic filtering (Core Traceability, Organizational, Material & Supply, etc.)
- Dynamic zoom, pan, and relationship highlighting
- Direct links to entity documentation sections

<a href="erd-navigator/index.html" class="erd-navigator-link">Launch ERD Navigator →</a>

## Working Group Documentation ## {#working-group-docs}

### Meeting Notes ### {#meeting-notes}

Access notes and documentation from BOOST working group meetings and presentations.

<div class="meeting-grid">

**Kickoff Meeting**
Initial project kickoff meeting notes and presentation materials.
<a href="https://github.com/carbondirect/BOOST/blob/main/meetings/kickoff_meeting.md" class="meeting-link">Meeting Notes →</a>
<a href="https://github.com/carbondirect/BOOST/blob/main/meetings/kickoff_meetingNotes.md" class="meeting-link secondary">Additional Notes →</a>

**June 11, 2025**
Working group meeting notes and action items from June 11th session.
<a href="https://github.com/carbondirect/BOOST/blob/main/meetings/meeting_6_11_25.md" class="meeting-link">Meeting Notes →</a>
<a href="https://github.com/carbondirect/BOOST/blob/main/meetings/meetingNotes_6_11_25.md" class="meeting-link secondary">Additional Notes →</a>

**June 25, 2025**
Latest working group meeting notes and updates from June 25th session.
<a href="https://github.com/carbondirect/BOOST/blob/main/meetings/BOOST_meeting_6_25_2025.md" class="meeting-link">Meeting Notes →</a>
<a href="https://github.com/carbondirect/BOOST/blob/main/meetings/meetingNotes_6_25_25.md" class="meeting-link secondary">Additional Notes →</a>

</div>

## Community Participation ## {#community-participation}

### BOOST Membership ### {#boost-membership}

**Chair:**
- Peter Tittmann (Carbon Direct)

**Participants:**
- Investor ab AB
- Bodie Cabiyo (Carbon Direct)
- Dani Charles (Veriflux)
- Kylee Durrett (Green Diamond)
- Vanessa Felix (Tule River Economic Development Corporation)
- Marieke Fenton (California Air Resources Board)
- Robert Hambrect (Allotrope Partners)
- Liam Kilroy (Carbon Direct)
- Jeremy Loeb (California Air Resources Board)
- Andy Miller (Loamist)
- Mahmoud Nabil
- Sarah Oldson (Cascade Resource Consultants, LLC)
- Daniel Sanchez (Carbon Direct)
- Clarke Stevenson (The Watershed Research and Training Center)
- Martin Twer (The Watershed Research & Training Center)

### Stakeholder Feedback ### {#stakeholder-feedback}

Industry stakeholders are welcome to provide feedback on BOOST entity schemas. The [interactive ERD Navigator](erd-navigator/index.html) enables exploration of the data model and input on each entity definition.

**How to Provide Feedback:**
1. Explore entities using the [ERD Navigator](erd-navigator/index.html)
2. Review entity schemas and field definitions
3. Submit feedback via [GitHub Issues](https://github.com/carbondirect/BOOST/issues)
4. Join [W3C Community Group discussions](https://lists.w3.org/Archives/Public/public-boost-01/)

<style>
.presentation-grid, .meeting-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin: 1rem 0;
}

.presentation-link, .meeting-link, .erd-navigator-link {
  display: inline-block;
  padding: 8px 16px;
  background-color: #0066cc;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  margin-top: 0.5rem;
  margin-right: 0.5rem;
}

.meeting-link.secondary {
  background-color: #28a745;
}

.erd-navigator-link {
  background-color: #6f42c1;
  padding: 12px 24px;
  font-size: 1.1em;
}

.presentation-link:hover, .meeting-link:hover, .erd-navigator-link:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

@media (min-width: 768px) {
  .presentation-grid, .meeting-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media print {
  .presentation-link, .meeting-link, .erd-navigator-link {
    background-color: transparent;
    color: #0066cc;
    border: 1px solid #0066cc;
  }
}
</style>