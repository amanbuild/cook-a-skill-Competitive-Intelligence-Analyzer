---
name: competitive-analysis
description: Perform a deep competitive analysis for a solopreneur business. Use when mapping competitors in detail, finding exploitable gaps, understanding competitor strategy, benchmarking your own offering, or deciding how to position against the field. Goes deeper than the broad landscape mapping in market-research — this is focused dissection of specific competitors. Trigger on "analyze my competitors", "competitive analysis", "who are my competitors", "competitor deep-dive", "how do I beat the competition", "competitive landscape", "benchmark against competitors".
---

# Competitive Analysis

## Overview
Shallow competitive research (checking a few websites) is not enough. This playbook gives you a systematic way to dissect competitors across strategy, product, pricing, marketing, digital presence, and reviews — then synthesise findings into exploitable gaps and a positioning wedge.

When running this skill, Claude should work through each step sequentially, using web search and web_fetch to gather real data for each competitor before synthesizing results.

---

## Step 1: Identify and Tier Competitors

Not all competitors are equal. Categorize them before diving in.

**Direct competitors:** Solve the exact same problem for the exact same customer. Primary benchmarks.

**Indirect competitors:** Solve a related problem or serve the same customer differently. These matter because the customer is choosing between ALL options (including doing nothing).

**Aspirational competitors:** Not in the niche yet, but could be. Larger players who might expand into the space. Reveal what "winning at scale" looks like.

**Target:** Identify 3–5 direct, 2–3 indirect, 1–2 aspirational. Focus the deepest analysis on the top 3 direct competitors.

> **Claude instruction:** If the user hasn't specified competitors, use web search to identify the most prominent players in the space before proceeding. Search for "[product category] competitors", "[product category] alternatives", and "[product category] top tools".

---

## Step 2: Intelligence Gathering

For each top 3 direct competitor, collect data across these seven layers in order.

---

### Layer 1: Strategy & Positioning

Visit the competitor's homepage and about page. Extract:

- Stated mission or tagline
- Who they say they're for (target customer)
- Problem they claim to solve
- Core differentiator — the one angle they lean hardest on
- Who they do NOT serve (gaps in their positioning = opportunity)

---

### Layer 2: Product & Features

Visit their product page, features page, and documentation. Extract:

- What the product actually does (functional summary)
- Complexity level: simple tool / mid-complexity / full platform
- Key technical strengths
- Integration ecosystem (what tools it connects with)
- Anything visibly absent that users would expect

---

### Layer 3: Pricing & Business Model

Visit their pricing page. Extract:

- All pricing tiers and what's included
- Free tier or free trial — yes/no, and what's gated
- Pricing model: per-user / per-usage / flat-rate / freemium
- Pricing gaps: too expensive for small users? No mid-tier? Sudden price jump?

---

### Layer 4: Digital Presence & Traffic

This layer tracks quantitative signals of market traction. Collect both website traffic and Twitter/X presence.

#### 4a. Website Traffic

> **API Note:** Website traffic will be fetched via integrated API (e.g. Similarweb, Semrush) in a future version. Until then, Claude should navigate to `similarweb.com/website/[competitor-domain]` or search for "[competitor name] traffic similarweb" to retrieve estimates.

For each competitor, record:

| Metric | What to Record |
|--------|---------------|
| Monthly visits (est.) | e.g. "~45K/mo" |
| Traffic trend (3-month) | ↑ Growing / → Stable / ↓ Declining |
| Top traffic source | Organic / Direct / Referral / Paid |
| Top organic keywords | Top 3–5 keywords driving search traffic |
| Domain Authority (DA) | Score 1–100 from Moz or Ahrefs free lookup |

**Interpretation signals:**
- High traffic + declining trend → vulnerable incumbent, possibly losing relevance
- Low traffic + high DA → old brand, low current content investment (your opening)
- Heavy paid traffic → they're buying customers; organic may be weak

#### 4b. Twitter/X Followers

> **API Note:** Follower count will be auto-fetched via Twitter/X API in a future version. Until then, Claude should search for "[competitor name] twitter" to find their handle, then navigate to their profile to retrieve current data.

For each competitor, record:

| Metric | What to Record |
|--------|---------------|
| Twitter/X handle | e.g. "@competitorname" |
| Follower count | e.g. "8.2K" |
| Post frequency | Daily / Weekly / Rarely / Inactive |
| Engagement level | High (>3%) / Medium (1–3%) / Low (<1%) |
| Account tone | Educational / Promotional / Community / Mixed |

> **Claude instruction for engagement estimate:** Look at likes + replies on their last 5 posts. Sum them, divide by follower count, divide by 5. That's an approximate engagement rate.

**What to look for:**
- Large following + low engagement → audience has gone cold; real reach is weaker than it appears
- Small following + high engagement → active niche community, a genuine competitive asset
- Absent or inactive account → Twitter/X is an open distribution channel to own
- Follower growth trajectory matters more than raw count

---

### Layer 5: Marketing & Distribution

Search for the competitor's blog, YouTube channel, and active social channels. Also check the Google Ads Transparency Center and Facebook Ad Library for paid activity.

- Primary customer acquisition channels
- Channels they're strongest on
- Channels they're ignoring (your opening)
- Content strategy: what topics they publish on (signals what they think customers care about)
- Referral or affiliate program: yes/no

---

### Layer 6: Customer Reviews

> **Claude instruction:** Search for "[competitor name] reviews", "[competitor name] reddit", "[competitor name] G2", and "[competitor name] Capterra". Read and synthesize at least 15–20 reviews per competitor. Categorize every complaint before writing the summary.

Complaint categories to watch for:

- **Feature gaps** — things users want but don't have
- **UX frustrations** — things that are clunky or confusing
- **Pricing complaints** — overpriced, unfair limits, sudden price hikes
- **Support failures** — slow, unhelpful, or absent support
- **Onboarding friction** — hard to get started, poor documentation

Also note the most praised aspects — these are table stakes you must match.

---

### Layer 7: Company Health & Trajectory

- Founded: year
- Funding: amount, stage, investors (Crunchbase)
- Headcount trend on LinkedIn: growing / stable / shrinking
- Recent news or product announcements: what direction are they moving?
- Geographic focus: local / global / niche vertical?

---

## Step 3: Build the Comparison Tables

After gathering data, present two side-by-side tables. These are the analytical centerpiece — make them scannable.

### Table A: Feature & Pricing Matrix

Columns = Your planned offering + each direct competitor. Rows = decision-relevant dimensions. Use ✅ / ❌ / ⚠️ for binary features, 1–5 scores for rated dimensions. Leave cells blank where data is unknown — unknown = a research task, not a guess.

```
| Dimension              | You (planned) | Competitor A | Competitor B | Competitor C |
|------------------------|:-------------:|:------------:|:------------:|:------------:|
| Price (monthly)        |               |              |              |              |
| Free tier?             |               |              |              |              |
| Ease of setup (1–5)    |               |              |              |              |
| [Key feature A]        |               |              |              |              |
| [Key feature B]        |               |              |              |              |
| Support quality (1–5)  |               |              |              |              |
| Key integrations       |               |              |              |              |
```

### Table B: Digital Presence Scorecard

```
| Metric                  | Competitor A | Competitor B | Competitor C |
|-------------------------|:------------:|:------------:|:------------:|
| Est. monthly traffic    |              |              |              |
| Traffic trend (3-mo)    |              |              |              |
| Domain Authority        |              |              |              |
| Twitter/X handle        |              |              |              |
| Twitter/X followers     |              |              |              |
| Twitter/X engagement    |              |              |              |
| Twitter/X activity      |              |              |              |
| Strongest channel       |              |              |              |
| Biggest channel gap     |              |              |              |
```

> 📡 *Traffic: Similarweb estimate — API integration pending*
> 📡 *Twitter/X: Manual profile lookup — API integration pending*

---

## Step 4: Synthesize Exploitable Gaps

From the matrix and review analysis, identify the top 3 exploitable gaps. A gap is exploitable when ALL of these are true:

1. Multiple competitors share the weakness — it's structural, not one player being sloppy
2. Customers complain about it — there is review evidence that real people care
3. It's solvable solo — within your skills, budget, and timeline
4. It's not table stakes — doing what everyone does doesn't create advantage

**For each gap, write a structured block:**

```
### Gap #N: [Short descriptive name]

**What it is:** [1–2 sentences describing the gap]

**Evidence:** [Specific complaints, review quotes, or data — cite source]

**Your solution:** [How you would specifically address this]

**Why competitors don't fix it:** [Too niche? Wrong business model? Conflicts with their strategy?]

**Effort to build:** Low / Medium / High
**Impact if solved:** Low / Medium / High
```

---

## Step 5: Define the Competitive Wedge

The wedge is the single sharp angle to enter the market on. Not "better at everything." It's "the only option that does X for Y."

**Formula:**
> "The only [product category] that [specific capability] for [specific customer type]."

**Examples:**
- "The only project management tool built specifically for solo consultants managing client work."
- "The only email marketing platform with AI-generated subject line A/B testing built into the free tier."

**Test the wedge against these three questions:**
1. Would a target customer immediately understand why this is different?
2. Is it defensible for at least 6–12 months before a competitor copies it?
3. Can it be built and delivered solo?

If any answer is no, sharpen further.

---

## Step 6: Output Format

When presenting a completed competitive analysis, use exactly this structure. Every section must be present. If data is unavailable, write `[data unavailable — research task]` rather than skipping the section.

---

```markdown
# Competitive Analysis: [Business / Product Name]
**Date:** YYYY-MM-DD

---

## 1. Competitor Overview

### Direct Competitors
| Name | Founded | Funding | Employees | One-line Summary |
|------|---------|---------|-----------|-----------------|
|      |         |         |           |                 |

### Indirect & Aspirational
[Brief paragraph — no table needed]

---

## 2. Digital Presence Scorecard

| Metric                  | [Competitor A] | [Competitor B] | [Competitor C] |
|-------------------------|:--------------:|:--------------:|:--------------:|
| Est. monthly traffic    |                |                |                |
| Traffic trend (3-mo)    |                |                |                |
| Domain Authority        |                |                |                |
| Twitter/X handle        |                |                |                |
| Twitter/X followers     |                |                |                |
| Twitter/X engagement    |                |                |                |
| Twitter/X activity      |                |                |                |
| Strongest channel       |                |                |                |
| Biggest channel gap     |                |                |                |

> 📡 Traffic: Similarweb estimate (API integration pending)
> 📡 Twitter/X: Manual profile lookup (API integration pending)

---

## 3. Feature & Pricing Matrix

| Dimension              | You (planned) | [Comp A] | [Comp B] | [Comp C] |
|------------------------|:-------------:|:--------:|:--------:|:--------:|
| Price (monthly)        |               |          |          |          |
| Free tier?             |               |          |          |          |
| Ease of setup (1–5)    |               |          |          |          |
| [Feature A]            |               |          |          |          |
| [Feature B]            |               |          |          |          |
| Support quality (1–5)  |               |          |          |          |
| Key integrations       |               |          |          |          |

---

## 4. Review Intelligence Summary

### [Competitor A]
**Most praised:** [...]

**Top complaints:**
- **[Category]:** [Specific example or quote]
- **[Category]:** [Specific example or quote]

### [Competitor B]
[Same format]

### [Competitor C]
[Same format]

---

## 5. Exploitable Gaps

### Gap #1: [Name]
**What it is:** [...]
**Evidence:** [...]
**Your solution:** [...]
**Why competitors don't fix it:** [...]
**Effort:** Low / Medium / High | **Impact:** Low / Medium / High

### Gap #2: [Name]
[Same format]

### Gap #3: [Name]
[Same format]

---

## 6. Competitive Wedge

> **"The only [category] that [does X] for [audience Y]."**

**Why this wedge works:**
- [Reason tied to a specific gap]
- [Reason tied to competitor weakness]
- [Reason tied to target customer need]

**Defensibility window:** [e.g. "12–18 months before a funded player copies this"]

---

## 7. Strategic Recommendations

[3–5 prioritized actions based on the analysis. Each must reference a specific gap, weakness, or insight found above.]

1. **[Action]** — [Why, referencing what was found]
2. **[Action]** — [Why, referencing what was found]
3. **[Action]** — [Why, referencing what was found]

---

## 8. Monitoring Calendar

| Cadence | Task | Time |
|---------|------|------|
| Weekly | Google Alerts for top 2–3 competitor names | 5 min |
| Monthly | Read 5–10 new reviews on G2 / Capterra | 30 min |
| Monthly | Check Twitter/X follower delta for top competitors | 10 min |
| Quarterly | Refresh traffic data and re-run comparison matrix | 2 hrs |
| Quarterly | Re-evaluate competitive wedge — has anything closed or opened? | 30 min |
```

---

## Common Pitfalls

- **Copying instead of gap-finding.** Copying a competitor's strategy loses on price and polish. Find the holes, don't mirror the playbook.
- **Over-indexing on the well-funded player.** The small, focused competitor who actually serves your niche is often more dangerous and more instructive.
- **Reading only positive reviews.** Negative reviews are 10x more valuable. That's where real product-market gaps live.
- **Confusing follower count with reach.** A 5K engaged Twitter/X audience beats a 50K ghost audience. Always check engagement rate, not just the number.
- **Ignoring traffic trends.** A declining competitor with high current traffic is a window — their audience is already looking for alternatives.
- **Forgetting "do nothing" is a competitor.** Some customers will stick with a spreadsheet. The wedge must be compelling enough to justify switching cost.
