# NotebookLM Creator Skill 

**What's inside**:
- ✅ SKILL.md - Complete workflow and guidelines
- ✅ validate_sources.py - URL validation script
- ✅ generate_lesson_structure.py - Batch processing helper
- ✅ prompt_templates.md - Templates for creating prompts
- ✅ source_finding.md - Source discovery strategies
- ✅ LICENSE.txt - MIT license

### 2. Documentation
**Files**: 
- `USAGE_GUIDE.md` - How to use the skill
- `EXAMPLE_OUTPUT.md` - Complete example lesson plan
- `SUMMARY.md` - Technical overview and architecture
- `example_batch_spec.json` - Batch processing template

---

## 🚀 Quick Start

### Install the Skill

**Option A: Claude.ai (Web/Mobile/Desktop)**
1. Download `notebooklm-creator.zip`
2. Go to Settings → Skills
3. Click "Upload Skill"
4. Select the zip file
5. Start using in new chats

**Option B: Claude Code**
1. Extract the zip to your skills directory
2. Use via SSH: `claude-code "use notebooklm-creator skill..."`

### Create Your First Lesson

Just tell Claude:
```
I want to create a NotebookLM lesson on [your topic].

The specific areas I want to cover are:
- [Area 1]
- [Area 2]
- [Area 3]
- [Area 4]

I already know [what you know] and want to learn [what you want to know].
I'm at a [beginner/intermediate/advanced] level.
```

Claude will:
1. Find 10-20 quality sources
2. Validate they're all accessible
3. Generate custom prompts for each area
4. Give you a complete lesson plan

---

## 📊 What Makes This Skill Unique

### Intelligent Source Discovery
- Finds sources that actually work (no paywalls, no logins)
- Validates every URL before including it
- Ensures comprehensive coverage of all learning areas
- Balances breadth (comprehensive guides) and depth (specialized resources)

### Custom-Tailored Prompts
Each prompt includes:
- **Your context** - What you already know
- **Specific coverage** - What this overview should teach
- **Clear exclusions** - What NOT to cover (handled by other overviews)
- **Tone guidance** - Matched to your expertise level

This prevents overlap and ensures each audio overview is focused and valuable.

### Scalable Architecture
- **Single lesson**: Interactive, conversational creation
- **Batch mode**: Process 100+ topics from JSON
- **Claude Code compatible**: Automate curriculum development

---

## 💡 Use Cases

### Personal Learning
Create focused lesson plans on topics you want to master:
- Technical skills (Docker, Kubernetes, React)
- Professional development (leadership, communication)
- Hobbies (photography, cooking, woodworking)

### Team Training
Build comprehensive learning curricula for your team:
- Onboarding programs
- Technical upskilling
- Compliance training

### Content Creation
Develop educational content:
- Course development
- Tutorial series
- Knowledge base articles

---

## 📋 How It Works

### The Process

**Step 1: Requirements Gathering**
- What's the main topic?
- What specific areas should be covered?
- What does the learner already know?
- What's their expertise level?

**Step 2: Source Discovery**
- Search for quality sources on the topic
- Find 10-20 URLs covering all learning areas
- Ensure source diversity (docs, tutorials, analysis)

**Step 3: Validation**
- Verify all URLs are active
- Check for paywalls and login requirements
- Ensure content is substantive and LLM-readable

**Step 4: Prompt Generation**
- Create one prompt per learning area
- Tailor to listener's expertise level
- Add clear exclusions to prevent overlap
- Include specific coverage guidance

**Step 5: Delivery**
- Complete source list with descriptions
- Ready-to-use prompts
- Usage instructions
- NotebookLM setup guide

---

## 🎯 Example Results

See `EXAMPLE_OUTPUT.md` for a complete example of a lesson plan on "Firewall Deep Packet Inspection" with:
- 15 validated sources
- 4 custom prompts (one per learning area)
- Coverage matrix showing which sources cover which areas
- Complete usage instructions

---

## 🔧 Technical Architecture

### Why This Design?

**Scripts for Deterministic Tasks**
- URL validation needs to be reliable
- Can't rely on LLM for "is this URL accessible?"
- Scripts provide consistent, testable results

**References for Knowledge**
- Templates and strategies change over time
- Keeping them separate makes updates easy
- Claude loads them only when needed

**Both Single and Batch Modes**
- Single: Great for exploration and learning
- Batch: Essential for scale (100+ lessons)
- Same workflow, different interfaces

### Key Design Principles

1. **Progressive Disclosure**
   - Metadata always loaded (skill name/description)
   - SKILL.md loaded when skill is used
   - References loaded only when needed

2. **Quality Over Quantity**
   - 10-20 sources (validated and valuable)
   - 150-300 word prompts (focused and actionable)
   - Each area covered by 3+ sources minimum

3. **User-Centric**
   - Prompts tailored to listener's level
   - Clear exclusions prevent wasted time
   - Practical usage instructions included

---

## 📖 Documentation Reference

### For Using the Skill
📄 **USAGE_GUIDE.md** - Start here
- Quick start guide
- Single lesson walkthrough
- Batch processing instructions
- Troubleshooting tips

### For Understanding the Output
📄 **EXAMPLE_OUTPUT.md** - See what you'll get
- Complete lesson plan example
- All 15 sources with descriptions
- All 4 prompts with full text
- Usage instructions

### For Technical Details
📄 **SUMMARY.md** - Architecture and design
- Technical decisions
- File structure
- Maintenance notes
- Extension guide

### For Batch Processing
📄 **example_batch_spec.json** - Template
- JSON format for multiple lessons
- Example listener contexts
- Different topic types

---

## ✅ Quality Checklist

Your lesson plans will meet these standards:

**Source Quality**
- ✅ 10-20 sources per topic
- ✅ All URLs validated and accessible
- ✅ No paywalls or login requirements
- ✅ Mix of comprehensive and specialized sources
- ✅ Each learning area covered by 3+ sources

**Prompt Quality**
- ✅ One prompt per learning area
- ✅ 150-300 words each (optimal length)
- ✅ Clear exclusions to avoid overlap
- ✅ Tailored to listener's expertise level
- ✅ Specific coverage guidance

**Coverage Quality**
- ✅ Balanced across all learning areas
- ✅ No gaps in essential topics
- ✅ Appropriate depth for audience
- ✅ Diverse perspectives (vendor, independent, academic)

---

## 🛠️ Customization Options

### Source Preferences
Tell Claude your preferences:
- "Only use official documentation"
- "Prefer recent sources (last 2 years)"
- "Include both beginner and advanced content"
- "Focus on practical tutorials over theory"

### Prompt Style
Request specific prompt features:
- "Make prompts conversational"
- "Include specific vendors: [list]"
- "Focus on cloud implementations"
- "Emphasize code examples"

### Learning Structure
Organize learning areas:
- "Build knowledge progressively" (sequential)
- "Make areas independent" (parallel)
- "Start with foundations, then specialize" (hybrid)

---

## 🔄 Workflow Integration

### With Notion
1. Create Notion page for the topic
2. Add source list as database
3. Track progress through overviews
4. Add notes from each audio

### With Google Calendar
1. Schedule learning sessions
2. Include prompts in event descriptions
3. Add NotebookLM links
4. Block focus time

### With Jira
1. Create epic for learning initiative
2. Tasks for each overview
3. Track team progress
4. Link to lesson plans

---

## 🎓 Learning Outcomes

After using this skill, you'll be able to:

✅ Create professional-quality NotebookLM lesson plans
✅ Find and validate quality learning sources efficiently
✅ Write effective prompts for audio overview generation
✅ Structure learning content to avoid redundancy
✅ Scale lesson creation to 100+ topics
✅ Build comprehensive training curricula

---

## 📞 Next Steps

### 1. Install the Skill
Download and install `notebooklm-creator.zip`

### 2. Try a Test Lesson
Create a lesson on a topic you know well to see how it works

### 3. Review the Output
Check the sources and prompts for quality

### 4. Use in NotebookLM
Actually create the notebook and generate an audio overview

### 5. Iterate
Refine your approach based on what you learn

### 6. Scale Up
Use batch mode for larger projects

---

## 📂 File Manifest

All files are in `/mnt/user-data/outputs/`:

```
notebooklm-creator.zip          ← The skill package (install this)
USAGE_GUIDE.md                  ← How to use the skill
EXAMPLE_OUTPUT.md               ← Complete lesson plan example
SUMMARY.md                      ← Technical overview
example_batch_spec.json         ← Batch processing template
THIS_FILE.md                    ← You are here
```

---

## 🎉 You're Ready!

Everything you need is in this folder. Just unzip this folder into your skills directory.

**Download it and start creating amazing NotebookLM lesson plans!**

Questions? Just ask Claude - the skill includes comprehensive documentation and Claude can explain any part of the process.
