# Competitive Intelligence Skill

AI-powered competitive intelligence reports that answer 4 strategic questions: **Who are we competing with? Why are they winning? Where's the whitespace? What should we do?**

Built for Ops & Data Analysts, Product Teams, and Strategy Teams. Replaces 1–2 days of manual research with ~30 min AI research + user review.

---

## Quick Start

### 1. Prepare input
Copy `skill/input-template.md` → fill in your product details (name, description, features, narrative).

### 2. Run in Claude chat
New conversation → paste the **Prompt Template** below → attach your filled input.

### 3. Review & save
Download the `.md` report → commit to `reports/`.

### 4. Iterate
Note feedback in `changelog.md`. Every 3–5 notes → update `skill/spec.md` + `skill/SKILL.md`.

---

## Prompt Template

```
You are a competitive research expert. I will send you a product spec.
Run a competitive intelligence report following this workflow:

Step A: Parse input → confirm product info back to me
Step B: I confirm → you begin research
Step C: Competitor Discovery & Battlefield Mapping (web search)
Step D: Deep Dive each competitor — Positioning vs Execution, multi-source evidence
Step E: Strategic Synthesis — who's winning & why, whitespace, threats
Step F: Generate .md report with 8.5 sections

Hard rules:
- Source confidence tier [A]–[D] for every source
- Freshness gate: metrics prefer ≤3 months, fallback ≤12 months + flag ⚠️. >12 months drop.
- Search queries for metrics MUST include date filter (year, "latest", "recent")
- Source priority ladder: use P1 source first (DefiLlama > Dune > media for on-chain)
- Deep dive selection: score 5 criteria (ICP 30, Feature 25, BizModel 20, Traction 15, Activity 10)
- Every claim must have source + "as of [date]"
- Clearly label Fact vs Inference
- Separate Positioning (what they SAY) vs Execution (what they DO)
- Strengths/weaknesses from external sources, not AI opinion
- Each deep dive covers ≥2 of 4 sources: Community, Expert, News, On-chain/Market
- ≥2 actionable whitespace opportunities with build tickets
- ≥1 threat rated High or Critical (unless justified low-threat environment)
- Action items specific enough to create tickets
- Self-assessment score: 5 dimensions × 20 points
- Fallback proxy when metric unavailable (clearly label proxy)
- Output density: deep dive 400–600 words, whitespace 200–300 words

Auto-detect industry branch:
- 🔗 Crypto: TVL, volume, wallets, on-chain fees | DefiLlama, Dune, protocol dashboards
- 🏢 Non-Crypto: MRR/ARR, pricing tiers, G2 rating, team size | G2, Capterra, SimilarWeb, Crunchbase

Here is my product spec:

[PASTE SPEC HERE]
```

---

## File Structure

```
competitive-intelligence/
├── README.md                          ← You are here
├── changelog.md                       ← Feedback log for iterations
├── skill/
│   ├── spec.md                        ← Source of truth (v3)
│   ├── SKILL.md                       ← Claude instructions (v3)
│   └── input-template.md              ← Template for product brief
└── reports/
    ├── pumpfun_Feb2026.md             ← v1 (archived)
    ├── pumpfun_v2_Feb2026.md          ← v2 (source tiers + selection rubric)
    ├── pumpfun_v3_Feb2026.md          ← v3 (freshness enforced) ✅ latest
    └── Polymarket_Feb2026.md          ← v2 (pre-freshness)
```

---

## Report Structure (8.5 Sections)

| # | Section | Answers | Key Features |
|---|---------|---------|-------------|
| 1 | Battlefield Map | Who are we competing with? | ASCII diagram, 4 tiers (direct / indirect / emerging / substitutes), selection scores |
| 2 | Comparison Matrix | How do we compare? | 🟢🟡🔴 ratings, standardized units, user product = column 1 |
| 3 | Deep Dive | What are they actually doing? | Positioning vs Execution layers, 4-source evidence, source tiers [A]–[D] |
| 4 | Who's Winning & Why | Why are they ahead or behind? | Per-factor analysis, each ends with "So what?" |
| 5 | Whitespace | Where can we attack? | Gap → Evidence → Actionable → Why winnable → Build ticket |
| 6 | Threats | What should we worry about? | Severity table with mitigation per threat |
| 7 | Action Items | What should we do? | Build / Watch / Benchmark tables with timelines |
| 8 | Sources & Confidence | How reliable is this? | URL + date + tier + age per source, confidence per section |
| 8.5 | Self-Assessment | How good is this report? | 5 dimensions × 20 points, user override field |

---

## Core Philosophies

| # | Philosophy | One-liner |
|---|-----------|-----------|
| P1 | Decision-first | The report is a decision tool, not a data dump |
| P2 | Comparable > many data | Less data that's comparable > lots of scattered data |
| P3 | Evidence-first | No source → "Unknown". Never fabricate. |
| P4 | Freshness matters | Metrics: prefer ≤3 months, fallback ≤12 months + flag. >12 months drop. |
| P5 | Positioning ≠ Execution | Separate what they SAY vs what they DO |
| P6 | Map the battlefield | Draw structure, don't just list |
| P7 | Find whitespace | Point to gaps you can attack |
| P8 | Actionable > academic | Every insight must answer "so what?" |

---

## Key Features (v3)

### Source Confidence Taxonomy
Every source labeled [A]–[D]. D-source claims flagged ⚠️.

| Tier | Examples |
|------|---------|
| [A] | Official docs, on-chain indexers (DefiLlama, Dune), SEC filings, Wikipedia |
| [B] | Reputable media (The Block, Messari, CoinDesk), Sacra, Crunchbase, G2 |
| [C] | Community (Reddit, X threads, opinion blogs) |
| [D] | Unsourced aggregators, content farms |

### Freshness Enforcement (HR-19)

| Source Age | Metrics / Traction | Context / Background |
|-----------|-------------------|---------------------|
| ≤3 months | ✅ Preferred | ✅ OK |
| 3–12 months | ⚠️ Fallback — use only if no ≤3 month source, flag "⚠️ Older" | ⚠️ OK + flag |
| >12 months | ❌ Drop | ❌ Drop |

All metric search queries MUST include a date filter (`"2026"`, `"latest"`, `"recent"`).

### Deep Dive Selection Rubric
100-point scoring system determines which competitors get deep dived:

| Criteria | Weight |
|----------|--------|
| ICP Overlap | 30 |
| Feature Overlap | 25 |
| Business Model Overlap | 20 |
| Traction Relevance | 15 |
| Recent Activity | 10 |

Score all direct competitors → rank → deep dive top scorers → show scores in Battlefield Map.

### Source Priority Ladder
Per metric type, always use the highest-priority source available:

| Metric Type | P1 | P2 | P3 | Fallback |
|------------|----|----|----|----|
| Traffic | SimilarWeb | Semrush | Ahrefs | "Unknown" |
| Funding | Official announcement | Crunchbase | Media | "Not publicly disclosed" |
| On-chain (crypto) | DefiLlama | Dune | Protocol docs | Media recap |
| Reviews (non-crypto) | G2 | Capterra | TrustRadius | "No review data" |

### Fallback Proxy Policy
When a primary metric is unavailable:

| Missing Metric | Proxy |
|---------------|-------|
| Traffic | App downloads / Google Trends branded search / on-chain wallets |
| Revenue | Funding stage as scale proxy / team size |
| Engagement rate | Follower count only + note "engagement unavailable" |

All proxies MUST be labeled: `"Proxy: [X] used because [Y] unavailable"`

### Industry Branch Detection
Auto-detected at Step B based on product description:

| Signal | Branch | Metrics Focus | Extra Sources |
|--------|--------|--------------|--------------|
| Token, chain, TVL, DeFi | 🔗 Crypto | TVL, volume, wallets, on-chain fees | DefiLlama, Dune, protocol dashboards |
| SaaS, pricing tiers, ARR | 🏢 Non-Crypto | MRR/ARR, pricing, G2 rating, team size | G2, Capterra, SimilarWeb, Crunchbase |

### Output Density Guidelines

| Section | Target | Format |
|---------|--------|--------|
| Battlefield Map | 300–500 words + tables + diagram | — |
| Comparison Matrix | Table only | No prose between rows |
| Deep Dive (per competitor) | 400–600 words | Layer A ~100w, Layer B ~200w + table, Evidence ~100–200w, Threat ~50–100w |
| Who's Winning (per competitor) | 150–250 words | Lead with factor + evidence, end with "So what?" |
| Whitespace (per opportunity) | 200–300 words | Gap → Evidence → Actionable → Why winnable → Ticket |
| Threats | Table + 1–2 sentence mitigation | No narrative |
| Action Items | Bullet, ≤2 sentences per item | Tables for Build / Watch / Benchmark |
| Sources | Table only | URL + date + tier + age |
| Self-Assessment | Table + 1 sentence per dimension | No long justification |

### Self-Assessment Scoring

| Dimension | Max | Measures |
|-----------|-----|---------|
| Evidence Quality | 20 | Source count, tier distribution, coverage gaps |
| Comparability | 20 | Standardized units, fair comparison across competitors |
| Strategic Usefulness | 20 | Answers all 4 strategic questions clearly |
| Freshness | 20 | % sources ≤3 months, flags applied correctly |
| Actionability | 20 | Build tickets with timelines, specificity |

---

## Reports

| # | Product | Version | Date | Score | File |
|---|---------|---------|------|-------|------|
| 1 | pump.fun | v1 | Feb 2026 | — | [pumpfun_Feb2026.md](reports/pumpfun_Feb2026.md) |
| 2 | pump.fun | v2 | Feb 2026 | 81/100 | [pumpfun_v2_Feb2026.md](reports/pumpfun_v2_Feb2026.md) |
| 3 | pump.fun | v3 | Feb 2026 | 84/100 | [pumpfun_v3_Feb2026.md](reports/pumpfun_v3_Feb2026.md) |
| 4 | Polymarket | v2 | Feb 2026 | 87/100 | [Polymarket_Feb2026.md](reports/Polymarket_Feb2026.md) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | Feb 2026 | Initial 8-section report structure, 8 philosophies, pump.fun test |
| v2 | Feb 2026 | +Source tiers [A]–[D], +Selection rubric (100-pt scoring), +Priority ladder, +Fallback proxies, +Self-assessment scoring (5×20), +Output density guidelines, +Crypto / Non-crypto branch detection, +Deep dive micro-example |
| v3 | Feb 2026 | +Freshness enforcement (HR-19): metrics prefer ≤3mo / fallback ≤12mo / >12mo drop. +Date filter required in search queries. +Age column in source table. +FM-11 stale source handling |

---

## Changelog

See [changelog.md](changelog.md) for detailed feedback notes per iteration.
