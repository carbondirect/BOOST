# BOOST Schema Validation Agents

This directory contains Claude Code sub-agents for comprehensive BOOST schema validation and integrity checking.

## Available Agents

### schema-integrity-reviewer

**Purpose**: Comprehensive validation of JSON schema integrity, foreign key relationships, and Python reference implementation alignment.

**Location**: `tools/agents/schema-integrity-reviewer.md`

## Setup Instructions

### Method 1: Claude Code Agent Directory Configuration

Claude Code can automatically discover agents in this directory. To enable:

1. **Check Claude Code Settings**: Ensure your Claude Code configuration includes agent discovery from the `tools/agents/` directory
2. **Repository Root**: Make sure you're running Claude Code from the BOOST repository root directory
3. **Agent Discovery**: Claude Code should automatically discover the `schema-integrity-reviewer` agent

### Method 2: Manual Agent Registration

If automatic discovery doesn't work:

1. **Copy to Claude Directory**: Copy the agent file to your local Claude agents directory:
   ```bash
   # Create local Claude agents directory if it doesn't exist
   mkdir -p ~/.claude/agents
   
   # Copy the schema integrity reviewer
   cp tools/agents/schema-integrity-reviewer.md ~/.claude/agents/
   ```

2. **Verify Installation**: Test that Claude Code can find the agent:
   ```
   /agents
   ```
   You should see `schema-integrity-reviewer` in the list.

### Method 3: Direct Agent Loading

You can also reference the agent directly:

1. **Use Task Tool**: Reference the agent file directly in a Task tool call
2. **Manual Prompting**: Copy the agent content and use it as a system prompt

## Usage

Once configured, invoke the agent in Claude Code:

```
schema-integrity-reviewer
```

The agent will automatically:
- Scan all 32 entity schemas for integrity issues
- Validate foreign key relationships and detect orphaned references  
- Check ERD configuration alignment
- Test Python reference implementation synchronization
- Generate detailed reports with actionable fixes

## Agent Capabilities

- **Orphaned Foreign Key Detection**: Finds broken references and missing entities
- **Data Model Design Validation**: Identifies normalization violations and data duplication
- **Multi-System Alignment**: Ensures consistency across schemas, ERD, and validation rules
- **Python Implementation Testing**: Validates reference implementation alignment
- **Pattern Standardization**: Verifies consistent ID patterns and naming conventions
- **Cross-Entity Validation**: Tests business logic rules and constraints
- **Comprehensive Reporting**: Provides specific file locations and fix instructions

## When to Use

- After modifying any JSON schema files
- Before creating pull requests with schema changes
- When adding new entities or relationships
- During troubleshooting of validation errors
- As part of regular schema maintenance

## Troubleshooting

### Agent Not Found
- Verify you're in the BOOST repository root directory
- Check that `tools/agents/schema-integrity-reviewer.md` exists
- Try Method 2 (manual registration) if automatic discovery fails

### Permission Issues
- Ensure Claude Code has read access to the `tools/agents/` directory
- Check file permissions on the agent definition file

### Agent Not Working
- Verify the agent file has valid YAML frontmatter
- Check that the agent description follows Claude Code agent format
- Review Claude Code logs for any parsing errors

## Contributing

When modifying or adding new agents:

1. Follow the existing agent format with YAML frontmatter
2. Include comprehensive examples in the description
3. Test the agent thoroughly before committing
4. Update this README with new agent documentation