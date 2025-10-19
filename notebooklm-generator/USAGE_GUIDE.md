# NotebookLM Creator Skill - Usage Guide

## Overview

The NotebookLM Creator skill helps you build comprehensive, structured learning content for Google NotebookLM. It automates the process of finding quality sources, validating their accessibility, and creating tailored prompts for audio overview generation.

## What You Get

After using this skill, you'll have:
- **Validated source list**: 10-20 URLs that are publicly accessible and LLM-readable
- **Custom prompts**: One prompt per learning area, optimized for NotebookLM
- **Usage instructions**: Step-by-step guide to create your notebook

## Quick Start (Single Lesson)

### Step 1: Provide Your Topic Information

Tell Claude:
1. **Main topic**: "I want to learn about [topic]"
2. **Learning areas**: "Specifically, I want to cover [area 1], [area 2], [area 3], and [area 4]"
3. **Your background**: "I already know [things you know] and want to learn [things you want to know]"
4. **Your level**: beginner/intermediate/advanced

**Example:**
```
I want to create a NotebookLM lesson on Firewall Configuration.

The specific areas I want to cover are:
- Access Control Lists (ACLs)
- Network Address Translation (NAT)
- VPN setup
- Logging and monitoring

I'm an IT Director who already knows networking fundamentals, TCP/IP, 
and basic routing, but I want to learn advanced firewall configuration 
for enterprise environments. I'm at an advanced level.
```

### Step 2: Claude Will:
1. Search for high-quality sources on your topic
2. Validate that all sources are accessible
3. Generate custom prompts for each learning area
4. Provide you with a complete lesson plan

### Step 3: Use the Lesson Plan
1. Go to Google NotebookLM (notebooklm.google.com)
2. Create a new notebook
3. Add all the sources Claude found
4. For each audio overview:
   - Click "Generate Audio Overview"
   - Copy/paste the corresponding prompt
   - Generate and listen

## Batch Processing (Multiple Lessons)

### Step 1: Create Batch Specification

Create a JSON file with your lesson specifications (see example_batch_spec.json):

```json
{
  "lessons": [
    {
      "topic": "Your Topic",
      "learning_areas": ["area1", "area2", "area3"],
      "listener_context": {
        "knows": ["thing1", "thing2"],
        "wants_to_learn": ["goal1", "goal2"],
        "skill_level": "intermediate"
      },
      "target_sources": 15
    }
  ]
}
```

### Step 2: Process with Claude

"Use the NotebookLM Creator skill in batch mode to process this specification file."

### Step 3: Get Results

Claude will create individual lesson plan files for each topic, plus a summary.

## Using with Claude Code

The skill is designed to work seamlessly with Claude Code for large-scale processing:

### In Claude Code:

```bash
# Process batch specification
claude-code "Use the notebooklm-creator skill to process batch_spec.json 
and create lesson plans for all topics"
```

Claude Code can:
- Process 100+ lessons automatically
- Save all lesson plans to organized directories
- Validate all sources in batches
- Generate comprehensive reports

## Tips for Best Results

### Define Learning Areas Clearly
- Be specific: "bread selection" not just "bread"
- Keep areas focused: 3-6 learning areas per topic
- Ensure areas don't overlap too much

### Provide Good Listener Context
- List specific things you already know
- Be clear about your expertise level
- State your practical goal/use case

### Choose Appropriate Source Count
- **10 sources**: Narrow, well-documented topics
- **15 sources** (recommended): Most topics
- **20 sources**: Broad topics or specialized deep-dives

### Review the Output
- Check that sources cover all learning areas
- Verify prompts have clear exclusions
- Ensure prompts match your expertise level

## Example Lesson Plan Output

You'll receive a markdown document like this:

```markdown
# NotebookLM Lesson Plan: Firewall Configuration

## Sources (15)

1. Cisco Firewall Configuration Guide - https://...
   Coverage: ACLs, NAT, logging
   
2. VPN Setup Best Practices - https://...
   Coverage: VPN, security
   
[... 13 more sources ...]

## Audio Overview Prompts

### Overview 1: Access Control Lists (ACLs)

Topic: Access Control Lists in Enterprise Firewalls

Listener Profile:
- Background: IT Director with strong TCP/IP and routing knowledge
- Expertise level: Advanced networking, familiar with basic firewall concepts
- Learning goal: Master enterprise-level ACL configuration and optimization

[... full prompt ...]

### Overview 2: Network Address Translation (NAT)

[... full prompt ...]

[... more overviews ...]

## Usage Instructions

1. Create a new notebook in Google NotebookLM
2. Add all 15 sources to the notebook
3. For each audio overview:
   - Click "Generate Audio Overview"
   - Copy and paste the corresponding prompt above
   - Generate the overview
4. Listen to overviews in sequence (1→2→3→4)
```

## Troubleshooting

### Sources Fail Validation

**Problem**: Some sources return errors or are inaccessible

**Solutions**:
- Claude will automatically find replacement sources
- If many sources fail, Claude may adjust the search strategy
- You can request specific types of sources (documentation vs tutorials)

### Prompts Seem to Overlap

**Problem**: Multiple prompts cover similar content

**Solutions**:
- Review the learning areas - they may be too similar
- Ask Claude to restructure with clearer boundaries
- Consider combining similar areas into one overview

### Not Enough Depth

**Problem**: Sources or prompts seem too basic

**Solutions**:
- Emphasize your expertise level more clearly
- Request "advanced" or "expert-level" content
- Specify technical depth you expect (e.g., "include code examples", "discuss implementation details")

### Too Technical

**Problem**: Content is more advanced than needed

**Solutions**:
- Clarify your actual knowledge level
- Request "beginner-friendly" or "introductory" content
- Specify practical focus over theoretical

## Advanced Features

### Custom Source Validation

If you have specific source requirements, tell Claude:
- "Only use official documentation"
- "Prefer recent sources (last 2 years)"
- "Include both tutorials and reference material"

### Prompt Customization

Request specific prompt features:
- "Make prompts emphasize practical examples"
- "Include specific vendors: Palo Alto, Fortinet"
- "Focus on cloud implementations"

### Sequential Learning

For building knowledge progressively:
- Structure learning areas from basic to advanced
- Tell Claude to build each overview on previous ones
- Request foundational overview before specialized ones

## Integration with Other Tools

### Notion Integration

After getting your lesson plan:
1. Create a new Notion page for the topic
2. Add source list as a database
3. Track progress through overviews
4. Add notes from each audio overview

### Calendar Integration

Schedule learning time:
1. Create calendar events for each overview
2. Include the prompt in event description
3. Add NotebookLM link to event

## File Reference

**Included in skill:**
- `SKILL.md`: Main skill documentation
- `scripts/validate_sources.py`: URL validation tool
- `scripts/generate_lesson_structure.py`: Batch processing helper
- `references/prompt_templates.md`: Prompt writing guide
- `references/source_finding.md`: Source discovery strategies

**Example files provided:**
- `example_batch_spec.json`: Batch processing template

## Support

For issues or questions:
1. Review the SKILL.md file for detailed workflows
2. Check references/ directory for templates and strategies
3. Ask Claude to explain any part of the process
4. Request modifications to fit your specific needs

## Version History

**v1.0** (Current)
- Single lesson creation
- Batch processing support
- Source validation
- Custom prompt generation
- Claude Code compatible
