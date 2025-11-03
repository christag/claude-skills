# NotebookLM Prompt Templates

This file contains templates and guidelines for creating effective NotebookLM audio overview prompts.

## Core Prompt Structure

Every NotebookLM prompt should include these elements:

1. **Learning objective** - What specific area is being covered
2. **Listener context** - Who the listener is and what they know
3. **Coverage scope** - What to cover in this episode
4. **Previous coverage** - What was covered in the last episode (for continuity)
5. **Upcoming topics** - What will be covered in future episodes (to avoid going into detail)
6. **Exclusions** - What NOT to cover in detail (other areas handled separately)
7. **Approach and goals** - How to present the material, teaching style, and learning objectives
8. **Length suggestion** - Duration target: [~15 min] for standard, [~22 min] for longer episodes
9. **Additional context** - Any other relevant information

**IMPORTANT**: At least one audio overview per lesson must be a real-life case study focusing on real companies and their actual experiences with the topic.

## Template: Standard Learning Area Prompt

```
Topic: [Specific learning area from the overall topic] [~15 min]

Listener Profile:
- Background: [What the listener already knows]
- Expertise level: [beginner/intermediate/advanced]
- Learning goal: [What they want to achieve]

Coverage for this segment:
[Detailed description of what this specific overview should cover]

Previous episode covered:
[What was covered in the last episode - creates continuity]
[For first episode: "This is the first episode in the series"]

Upcoming episodes will cover:
[What will be covered in future episodes - helps avoid going into detail on these topics]
[For last episode: "This is the final episode in the series"]

IMPORTANT - Do NOT cover in detail:
- [Area 1]: Already covered in overview #X
- [Area 2]: Will be covered in overview #Y
- [Area 3]: Will be covered in overview #Z

Approach and Goals:
- Learning objectives: [What the listener should be able to do after this episode]
- Tone guidance: [e.g., "conversational but technical"]
- Depth guidance: [e.g., "provide code examples"]
- Teaching style: [e.g., "focus on practical applications"]
- Format preferences: [e.g., "use analogies to explain complex concepts"]

Additional context:
[Any other relevant information for this specific segment]

Length: [~15 min] or [~22 min]
```

## Template: Case Study Overview Prompt

```
Topic: Real-World Case Study - [Topic Area] [~22 min]

Listener Profile:
- Background: [What the listener already knows]
- Expertise level: [beginner/intermediate/advanced]
- Learning goal: [What they want to learn from real-world examples]

Coverage for this segment:
This case study overview should analyze real companies and their experiences with [topic]:
- [Company 1]: Their implementation, challenges, and outcomes
- [Company 2]: Their approach and lessons learned
- [Company 3]: Their success story or cautionary tale
- Common patterns across these real-world examples
- Key takeaways and best practices from actual implementations

Previous episode covered:
[What was covered in the last episode]

Upcoming episodes will cover:
[What will be covered in future episodes]

IMPORTANT - Do NOT cover in detail:
- Theoretical concepts: Already covered in overview #X
- Implementation details: Will be covered in overview #Y
- [Other areas]: Will be covered in overview #Z

Approach and Goals:
- Learning objectives: Understand how real companies have implemented [topic] and learn from their experiences
- Tone guidance: Analytical and insightful, focusing on real-world lessons
- Depth guidance: Provide specific details about company experiences, challenges faced, and solutions implemented
- Teaching style: Use concrete examples and real company names/stories
- Format preferences: Compare and contrast different company approaches

Additional context:
Focus on verifiable real-world examples from actual companies. Include both successes and failures to provide balanced perspective.

Length: [~22 min]
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

## Template: Quiz Prompt

```
Quiz: [Topic/Learning Area Name] (Based on Overview #X)
**Length**: [short/default/long]
**Difficulty**: [medium/hard]

Source Audio Overview: Overview #X - [Title]

Quiz Focus:
This quiz should test the listener's understanding of:
- [Key concept 1 from the audio overview]
- [Key concept 2 from the audio overview]
- [Key concept 3 from the audio overview]
- [Practical application or scenario from the overview]

Question Types to Include:
- [e.g., "Multiple choice on core concepts"]
- [e.g., "Scenario-based questions on implementation"]
- [e.g., "True/false on common misconceptions"]

Emphasis:
- [e.g., "Focus on practical application rather than memorization"]
- [e.g., "Include real-world scenarios similar to those discussed"]
- [e.g., "Test critical thinking about trade-offs"]

Difficulty Note:
[Guidance on what makes this quiz medium vs hard, e.g., "Include questions that require synthesizing multiple concepts" or "Test foundational knowledge only"]
```

## Prompt Length Guidelines

**Optimal length for Audio Overview Prompts: 200-350 words**
- Enough detail to guide effectively with new requirements
- Includes all required sections (coverage, previous, upcoming, approach, goals, length)
- Not so long that key points get lost
- NotebookLM will work with longer prompts, but concise is better

**Optimal length for Quiz Prompts: 100-200 words**
- Clear focus on key concepts
- Specific guidance on difficulty level
- Reference to source audio overview

**Too short:**
- Risk of vague guidance
- May miss important exclusions or continuity elements
- Listener context might be unclear

**Too long (>450 words for audio, >250 for quiz):**
- Key instructions may be buried
- Harder for NotebookLM to follow
- Suggests the scope should be split into multiple overviews

## Testing and Iteration

After generating audio overview prompts:

1. **Review for overlaps** - Do any prompts cover the same ground?
2. **Check continuity** - Does each prompt reference previous and upcoming content?
3. **Check exclusions** - Does every prompt clearly exclude other areas?
4. **Verify listener context** - Is it consistent across all prompts?
5. **Assess scope balance** - Are some areas too broad while others too narrow?
6. **Confirm case study** - Is there at least one real-world case study overview?
7. **Verify length suggestions** - Are lengths appropriate ([~15 min] or [~22 min])?

After generating quiz prompts:

1. **Coverage check** - Are all 4 quizzes present?
2. **Mapping verification** - Is each quiz clearly based on a specific audio overview?
3. **Difficulty distribution** - Mix of medium and hard difficulties?
4. **Length distribution** - Mix of short, default, and long lengths?
5. **Content alignment** - Do quiz topics match the audio overview content?

Consider creating a prompt summary table:

| # | Learning Area | Key Topics | Previous | Upcoming | Length |
|---|---------------|------------|----------|----------|--------|
| 1 | Foundation    | A, B, C    | None     | 2, 3, 4  | 15min  |
| 2 | Advanced X    | D, E       | 1        | 3, 4     | 15min  |
| 3 | Case Study    | Real cos.  | 1, 2     | 4        | 22min  |
| 4 | Advanced Y    | F, G       | 1, 2, 3  | None     | 15min  |

Quiz summary table:

| Quiz | Based On | Difficulty | Length  | Focus Topics |
|------|----------|------------|---------|--------------|
| 1    | Ovw #1   | Medium     | Default | A, B, C      |
| 2    | Ovw #2   | Medium     | Short   | D, E         |
| 3    | Ovw #3   | Hard       | Default | Case studies |
| 4    | Ovw #4   | Hard       | Long    | F, G         |
