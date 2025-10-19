# NotebookLM Prompt Templates

This file contains templates and guidelines for creating effective NotebookLM audio overview prompts.

## Core Prompt Structure

Every NotebookLM prompt should include these elements:

1. **Learning objective** - What specific area is being covered
2. **Listener context** - Who the listener is and what they know
3. **Exclusions** - What NOT to cover (other areas handled separately)
4. **Tone and approach** - How to present the material
5. **Depth guidance** - Level of detail appropriate for this section

## Template: Single Learning Area Prompt

```
Topic: [Specific learning area from the overall topic]

Listener Profile:
- Background: [What the listener already knows]
- Expertise level: [beginner/intermediate/advanced]
- Learning goal: [What they want to achieve]

Coverage for this segment:
[Detailed description of what this specific overview should cover]

IMPORTANT - Do NOT cover:
- [Area 1]: This is covered in overview #X
- [Area 2]: This will be covered in overview #Y
- [Area 3]: This will be covered in overview #Z

Approach:
- [Tone guidance, e.g., "conversational but technical"]
- [Depth guidance, e.g., "provide code examples"]
- [Emphasis, e.g., "focus on practical applications"]
- [Format preferences, e.g., "use analogies to explain complex concepts"]

Additional context:
[Any other relevant information for this specific segment]
```

## Example: Firewall Deep Packet Inspection

```
Topic: Deep Packet Inspection (DPI) in Modern Firewalls

Listener Profile:
- Background: IT Director with strong networking foundation
- Already knows: ACLs, routing, port forwarding, TCP/IP fundamentals, basic firewall concepts
- Expertise level: Advanced networking, new to DPI specifics
- Learning goal: Understand DPI capabilities, implementation, and use cases

Coverage for this segment:
This overview should cover Deep Packet Inspection including:
- How DPI works at a technical level (beyond simple packet filtering)
- The difference between stateful inspection and DPI
- Common DPI use cases (application control, threat detection, QoS)
- Performance considerations and hardware requirements
- Privacy and legal implications
- Popular DPI implementations and vendors

IMPORTANT - Do NOT cover:
- Basic firewall concepts: Already covered in overview #1
- Intrusion Detection Systems (IDS): This will be covered in overview #3
- VPN and encrypted traffic handling: This will be covered in overview #4

Approach:
- Technical and detailed - this listener can handle deep technical content
- Use specific examples from enterprise firewall products (Palo Alto, Fortinet, etc.)
- Include performance metrics and benchmarks where relevant
- Focus on architectural decisions and trade-offs
- Discuss both on-premise and cloud implementations

Additional context:
The listener manages a mid-size enterprise network and is evaluating next-gen firewall solutions. They need to understand DPI capabilities to make informed purchasing decisions and architect effective security policies.
```

## Guidelines for Prompt Creation

### Listener Context Best Practices

1. **Be specific about existing knowledge** - List concrete topics/technologies they know
2. **Define expertise level clearly** - Use specific terms, not just beginner/intermediate/advanced
3. **State the practical goal** - Why they're learning this, what they'll do with it

### Exclusion Best Practices

1. **Be explicit** - Don't assume the AI will infer what to exclude
2. **Reference other overviews** - Help maintain coherence across the series
3. **Cover both past and future** - Exclude what was already covered AND what's coming later

### Coverage Scope

1. **Define boundaries clearly** - What's in scope vs. out of scope
2. **Provide structure guidance** - Suggest key subtopics if helpful
3. **Balance breadth and depth** - One focused area covered well > many topics covered superficially

### Tone and Approach

1. **Match listener expertise** - Don't talk down to advanced listeners or overwhelm beginners
2. **Specify teaching style** - Examples: conversational, academic, hands-on, theoretical
3. **Guide depth level** - Should they cover basic principles or dive into implementation details?

## Multi-Area Prompt Strategy

When creating prompts for multiple learning areas within one topic:

### Sequential Approach (Recommended)
Build knowledge progressively across overviews:
- Overview 1: Foundations (what later overviews will reference)
- Overview 2-N: Specific areas that build on foundations
- Final overview: Integration/advanced topics that combine earlier concepts

### Parallel Approach
When learning areas are independent:
- Each overview stands alone
- Minimal cross-referencing needed
- Order matters less

### Hybrid Approach
Combine sequential for some areas, parallel for others:
- Start with foundational overview
- Follow with parallel deep-dives into independent areas
- Conclude with integration overview

## Prompt Length Guidelines

**Optimal length: 150-300 words**
- Enough detail to guide effectively
- Not so long that key points get lost
- NotebookLM will work with longer prompts, but concise is better

**Too short (<100 words):**
- Risk of vague guidance
- May miss important exclusions
- Listener context might be unclear

**Too long (>400 words):**
- Key instructions may be buried
- Harder for NotebookLM to follow
- Suggests the scope should be split into multiple overviews

## Testing and Iteration

After generating prompts:

1. **Review for overlaps** - Do any prompts cover the same ground?
2. **Check exclusions** - Does every prompt clearly exclude other areas?
3. **Verify listener context** - Is it consistent across all prompts?
4. **Assess scope balance** - Are some areas too broad while others too narrow?

Consider creating a prompt summary table:

| # | Learning Area | Key Topics | Excludes | Builds On |
|---|---------------|------------|----------|-----------|
| 1 | Foundation    | A, B, C    | -        | -         |
| 2 | Advanced X    | D, E       | F, G     | #1        |
| 3 | Advanced Y    | F, G       | D, E     | #1        |
