# Source Finding Strategies

Guidelines for finding high-quality, LLM-readable sources for NotebookLM.

## Source Quality Criteria

### Must-Have Requirements

1. **Publicly accessible** - No login, no paywall, no subscription
2. **Active/online** - URL returns 200 status, not 404 or server error
3. **LLM-readable** - Not blocking crawlers, has meaningful text content
4. **Substantive content** - Has enough depth to be valuable (>500 words typically)

### Quality Indicators

1. **Authority** - Written by experts or reputable organizations
2. **Depth** - Provides detailed explanations, not just surface-level overviews
3. **Currency** - Recent enough to be relevant (depends on topic)
4. **Practical** - Includes examples, use cases, or actionable information
5. **Clear** - Well-written and organized

### Red Flags

1. **Paywalls** - WSJ, NYT, Medium premium, academic journals without open access
2. **Login walls** - LinkedIn articles, Quora, some Medium content
3. **Crawler blocking** - Sites that block automated access
4. **Too promotional** - Marketing material posing as educational content
5. **Outdated** - Technology articles from 2010 about current best practices
6. **Too basic** - Elementary content when audience is advanced
7. **Too advanced** - PhD-level papers when audience is intermediate

## Source Types by Reliability

### Tier 1: Highly Reliable

**Official documentation**
- Vendor docs (AWS, Google Cloud, etc.)
- Official project documentation (React, Python, etc.)
- Standards bodies (W3C, IEEE, RFC documents)
- Government resources (.gov sites)

**Academic/Research**
- University course materials (OpenCourseWare)
- Open-access papers (arXiv, PLOS, etc.)
- Research blogs from universities
- Technical reports from research institutions

**Professional/Technical**
- Technical blogs from major companies (Google Developers, Cloudflare Blog)
- Engineering team blogs (Uber, Airbnb, Netflix engineering)
- Well-known technical sites (MDN, Stack Overflow Docs)
- Established technical publishers (O'Reilly, Manning free chapters)

### Tier 2: Generally Good

**Community resources**
- Well-maintained GitHub repos with docs
- Established technical blogs (CSS-Tricks, Smashing Magazine)
- Tutorial sites (freeCodeCamp, DigitalOcean tutorials)
- Conference talks/slides (when available as articles)

**News/Analysis**
- Tech news sites (Ars Technica, The Verge technical articles)
- Industry analysis (Gartner free reports, Forrester blogs)
- Professional journals with open articles

### Tier 3: Use Selectively

**Individual blogs**
- Personal technical blogs (verify expertise)
- Medium articles (check author credentials)
- Dev.to posts (vary widely in quality)

**Q&A sites**
- Stack Overflow (for specific technical topics)
- Reddit technical subreddits (when well-sourced)

### Avoid

- Sites requiring login (LinkedIn, Quora, etc.)
- Paywalled content
- Social media posts (Twitter threads, Instagram, etc.)
- YouTube videos (NotebookLM needs text)
- Sites with aggressive anti-scraping measures
- Pure marketing content
- Forums (too unstructured)

## Search Strategy

### Step 1: Identify Search Terms

For topic "Firewall Deep Packet Inspection":
- Primary: "deep packet inspection firewall"
- Technical: "DPI implementation", "stateful inspection vs DPI"
- Specific: "firewall DPI performance", "deep packet inspection techniques"
- Vendor-specific: "Palo Alto DPI", "Fortinet deep inspection"

### Step 2: Use Multiple Search Approaches

**Broad topic search**
- Start with general search to find comprehensive resources
- Look for tutorial series or complete guides

**Specific area search**
- Search for each learning area individually
- Find specialized deep-dives

**Cross-reference search**
- "X vs Y" comparisons
- "X and Y" integration topics
- "X for Y use case" practical applications

**Documentation search**
- Add "documentation" or "guide" to searches
- Search specific vendor/product docs

### Step 3: Evaluate Results

For each potential source:
1. Check URL validity (use validate_sources.py)
2. Verify content quality (skim the article)
3. Confirm coverage (does it actually cover what you need?)
4. Check depth (is it detailed enough for the listener's level?)

## Coverage Matrix Strategy

Create a matrix to ensure all learning areas are well-covered:

| Source | Bread | Proteins | Cheeses | Vegetables | Overall Quality |
|--------|-------|----------|---------|------------|-----------------|
| Source 1 | ✓✓ | ✓ | - | - | High |
| Source 2 | ✓ | ✓✓ | ✓✓ | ✓ | High |
| Source 3 | - | ✓ | ✓✓ | ✓✓ | Medium |

Legend:
- ✓✓ = Comprehensive coverage
- ✓ = Mentioned/partial coverage
- - = Not covered

**Goal:** Each learning area should have:
- At least 3 sources with comprehensive coverage (✓✓)
- At least 5 sources with any coverage (✓ or ✓✓)

## Source Count Guidelines

**10 sources (minimum)**
- Use when topic is narrow
- Use when sources are very comprehensive
- Risk: May lack depth in some areas

**15 sources (recommended)**
- Sweet spot for most topics
- Good balance of breadth and depth
- Provides redundancy for validation

**20 sources (maximum)**
- Use for very broad topics
- Use when sources are narrow/specialized
- Risk: May be overwhelming for NotebookLM

## Source Diversity

Aim for diversity in:

**Content type:**
- Tutorials (how-to guides)
- Conceptual explanations (what and why)
- Reference documentation (specifications)
- Case studies (real-world applications)
- Comparisons (technology A vs B)

**Perspective:**
- Vendor/creator perspective
- Independent technical analysis
- Academic research
- Practitioner experience
- Industry analyst view

**Depth level:**
- Beginner introductions (even for advanced topics - for foundations)
- Intermediate tutorials
- Advanced deep-dives
- Expert-level analysis

## Example: Finding Sources for "Sandwich Making"

**Learning areas:** bread, proteins, cheeses, vegetables

**Search strategy:**

1. **Comprehensive resources (3-5 sources)**
   - "complete guide to sandwich making"
   - "art of sandwich making"
   - "sandwich cookbook free online"

2. **Bread-specific (3-4 sources)**
   - "bread types for sandwiches"
   - "choosing sandwich bread"
   - "artisan bread for sandwiches"

3. **Protein-specific (3-4 sources)**
   - "sandwich proteins guide"
   - "deli meat selection"
   - "vegetarian sandwich proteins"

4. **Cheese-specific (3-4 sources)**
   - "cheese for sandwiches"
   - "melting cheese types"
   - "cheese pairing sandwiches"

5. **Vegetable-specific (3-4 sources)**
   - "sandwich vegetables guide"
   - "fresh vegetables sandwiches"
   - "preparing vegetables for sandwiches"

**Expected results:**
- Some sources will cover multiple areas (that's good!)
- Comprehensive guides might cover all areas
- Specialized sources provide depth in one area
- Total of 10-20 unique sources

## Quality Assurance

Before finalizing source list:

1. **Run validation script**
   ```bash
   scripts/validate_sources.py url1 url2 url3 ... --verbose
   ```

2. **Manual spot-check**
   - Open 3-5 sources and verify quality
   - Ensure they're actually readable and substantive
   - Check that they match listener expertise level

3. **Coverage verification**
   - Create coverage matrix
   - Ensure no learning area is underrepresented
   - Ensure no learning area dominates (unless intentional)

4. **Diversity check**
   - Not all sources from one site/author
   - Mix of content types (tutorial, reference, analysis)
   - Range of perspectives
