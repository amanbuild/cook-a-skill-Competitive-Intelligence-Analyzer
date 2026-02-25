# Skill Card

## Competitive Intelligence Analyzer

> **v3.1** | Crypto + Non-Crypto | English

---

### What It Does

Transforms a product brief into a **decision-oriented competitive intelligence report** that answers 4 strategic questions:

1. **Who** are we competing with?
2. **Why** are they winning?
3. **Where** is the whitespace?
4. **What** should we do?

---

### Before vs After

| | Before (Manual) | After (With Skill) |
|---|-----------------|-------------------|
| **Time** | 1–2 days | ~30 min + review |
| **Searches** | Ad hoc Googling, dozens of tabs | 20–40 structured queries with date filters |
| **Data quality** | Different format per competitor, can't compare | Standardized units (USD, monthly, daily avg) across all |
| **Source tracking** | None or inconsistent | Every claim has source + date + confidence tier [A]–[D] |
| **Freshness** | Cites 2-year-old articles without noticing | Freshness gate: prefer ≤3mo, fallback ≤12mo + flag, >12mo drop |
| **Output** | Data dump — "here's what I found" | Strategic report — "here's what you should do" |
| **Actionability** | Vague recommendations | Ticket-ready build items with timelines |

---

### Report Output (8.5 Sections)

| # | Section | Answers |
|---|---------|---------|
| 1 | Battlefield Map | Market structure: direct / indirect / emerging / substitutes |
| 2 | Comparison Matrix | Apple-to-apple with standardized metrics |
| 3 | Deep Dives | Positioning (what they SAY) vs Execution (what they DO) |
| 4 | Who's Winning & Why | Winning factor per competitor + evidence |
| 5 | Strategic Whitespace | Attackable gaps with build tickets |
| 6 | Threats & Risk Signals | Severity table with concrete mitigations |
| 7 | Action Items & Watchlist | Build / Message / Target / Watch / Benchmark |
| 8 | Sources & Confidence | URL + date + tier + age for every source |
| 8.5 | Self-Assessment | 5 dimensions x 20 points = 100 max |

---

### Key Features

| Feature | How It Works |
|---------|-------------|
| **Source Confidence [A]–[D]** | Every source labeled. D-tier claims flagged. |
| **Deep Dive Selection Rubric** | 100-point scoring: ICP(30) + Feature(25) + BizModel(20) + Traction(15) + Activity(10) |
| **Source Priority Ladder** | Per metric type, try highest-priority source first (e.g., DefiLlama > Dune > media) |
| **Fallback Proxy Policy** | When metric unavailable, use proxy but always label: `"Proxy: X used because Y unavailable"` |
| **Freshness Enforcement** | All metric searches MUST include date filter. Stale results retried 2+ times. |
| **Industry Branch Detection** | Auto-detect Crypto vs Non-Crypto vs Hybrid based on product description |
| **Output Density Targets** | Word counts per section. No padding. Tables preferred over prose. |
| **Self-Assessment Scoring** | Auto-rates report quality. Score <70 triggers warning banner. |

---

### Input Required

```
Product Name        ← required
Description         ← 2-5 sentences
Key Features        ← minimum 3
Narrative           ← target audience + value prop + differentiation
Comparison Criteria ← optional (AI selects if blank)
Known Competitors   ← optional (AI discovers if blank)
```

---

### Tools & Data Sources

| Layer | Tools |
|-------|-------|
| **AI Engine** | Claude (reasoning, synthesis, report writing) |
| **Research** | Web Search with date-filtered queries |
| **On-chain** (Crypto) | DefiLlama, Dune Analytics, Token Terminal, protocol dashboards |
| **Market** (Non-Crypto) | SimilarWeb, G2, Capterra, Crunchbase, Semrush |
| **News/Expert** | The Block, Messari, CoinDesk, industry blogs |
| **Community** | Reddit, X/Twitter, Discord sentiment |
| **Output** | Markdown (.md) + optional Word (.docx) |

---

### Hard Rules (20 total)

The skill enforces 20 hard rules (HR-1 to HR-20) that prevent common report failures:

- No fabricated competitors, metrics, or pricing
- Conflicting data shown as range, never cherry-picked
- Every metric has "as of [date]"
- Fact vs Inference always labeled
- Positioning vs Execution always separated
- At least 1 threat rated Critical (all-green = dishonest)
- Whitespace must be actionable ("attack where" not just "gap here")
- Output language matches input language

---

### Test Results

| # | Product | Industry | Score | Date |
|---|---------|----------|-------|------|
| 1 | pump.fun | Crypto — Meme Token Launchpad | 82/100 | Feb 2026 |
| 2 | Hyperliquid | Crypto — Perpetual Futures DEX | 87/100 | Feb 2026 |

Reports available in [`test-results/`](test-results/).

---

### Limitations

- Cannot access paywalled data (Sacra, Semrush premium, gated reports)
- Cannot verify claims behind logins (private dashboards, Discord-only announcements)
- Self-assessment scores are AI estimates, not ground truth
- Bot/wash activity inflates public metrics industry-wide — report flags but cannot filter
- Single-session scope: no persistent memory across report versions

---

### Expansion Roadmap

| Priority | Feature | Status |
|----------|---------|--------|
| P1 | Auto-refresh mode (monthly re-run, diff vs previous) | Planned |
| P1 | Non-Crypto SaaS vertical optimization (G2/Capterra deep integration) | Planned |
| P2 | Slack/Notion integration for action item tracking | Planned |
| P2 | PDF/slide deck export for board presentations | Planned |
| P3 | Multi-language output support | Planned |
| P3 | Historical trend analysis (cross-report comparison) | Planned |

---

### File Structure

```
cook-a-skill-Competitive-Intelligence-Analyzer/
├── SKILL-CARD.md          ← This file
├── README.md              ← Quick start + prompt template
├── SPEC.md                ← Source of truth (full specification)
├── SKILL.md               ← Claude instructions (execution guide)
├── input-template.md      ← Template for product brief
└── test-results/          ← Sample reports
    ├── pumpfun_Competitive_Intel_Feb2026.md
    └── Hyperliquid_Competitive_Intel_Feb2026.md
```
