---
name: competitive-intelligence
version: "3.1"
description: "Analyze competitors around the user's product and produce a decision-oriented report answering: Who are we competing with? Why are they winning? Where's the whitespace? What should we do?"
triggers:
  - "analyze my competitors"
  - "competitive analysis"
  - "competitive landscape"
  - "who are my competitors"
  - "benchmark against competitors"
input: "Product brief (name, description, features, narrative)"
output: "Markdown report with battlefield map, comparison matrix, deep dives, whitespace analysis, and action items"
do_not_use_for:
  - "General market research without a specific product (use narrative-research)"
  - "Product planning (use business-idea-plan)"
  - "Financial modeling or investment advice"
---

# Competitive Intelligence Report — Skill Instructions

## Core Philosophies (govern every decision)

1. **Decision-first** — Report answers strategic questions, not collects data
2. **Comparable > many data** — Standardized units, fields, timeframe across all competitors
3. **Evidence-first, no fabrication** — No source → "Unknown". Conflicts → range + note
4. **Freshness matters** — **Metrics/traction**: prefer sources ≤3 months. If unavailable → fallback ≤12 months + flag "⚠️ Older". **Context/background**: allow ≤12 months, flag if >3 months. >12 months → drop entirely. Always write "as of [date]"
5. **Positioning ≠ Execution** — Separate what they SAY vs what they DO
6. **Map the battlefield** — Structure of competition, not just a list
7. **Find strategic whitespace** — Point to gaps you can attack
8. **Actionable > academic** — Every insight answers "so what?"

---

## Hard Rules

| # | Rule |
|---|------|
| HR-1 | **No fake competitors.** Real URL required. |
| HR-2 | **No fake metrics.** Not found → "Unknown". |
| HR-3 | **No guessed pricing.** Not public → state so. |
| HR-4 | **Conflicting data → range + note conflict.** Never cherry-pick. |
| HR-5 | **Label Fact vs Inference.** Fact = has source. Inference = must be labeled "Inference:". |
| HR-6 | **Every metric has "as of [date]".** No date → lower confidence. |
| HR-7 | **Standardize units.** USD for money, monthly for traffic, daily average for volume. No mixing. |
| HR-8 | **User product = column 1** in comparison matrix. |
| HR-9 | **User-specified criteria must appear** in matrix. Never drop. |
| HR-10 | **Separate Positioning vs Execution** in every deep dive. |
| HR-11 | **Strengths/weaknesses from external sources** — not AI opinion. |
| HR-12 | **Each deep dive ≥2 of 4 sources** (community, expert, news, on-chain). Missing → "No [source] found." |
| HR-13 | **Every insight has "so what?"** — don't stop at observation. |
| HR-14 | **Whitespace must be actionable** — "attack where" not just "gap here". |
| HR-15 | **≥1 threat 🔴 Critical.** All-green = dishonest. |
| HR-16 | **Output language = input language.** |
| HR-17 | **Missing required input → STOP and ask.** |
| HR-18 | **Source confidence tier [A]–[D] required** for every source. D-source claims must flag ⚠️. |
| HR-19 | **Freshness gate.** Metrics: prefer ≤3mo, fallback ≤12mo + flag. >12mo → DROP. Search queries MUST include date filter. |
| HR-20 | **Deep dive selection by rubric.** Score all direct competitors → rank → deep dive top scorers. Show scores in Battlefield Map. |

---

## Source Confidence Taxonomy (HR-18)

| Tier | Definition | Examples |
|------|-----------|---------|
| [A] | Official / primary data | Official docs, on-chain indexers (DefiLlama, Dune), SEC filings, company blog |
| [B] | Reputable secondary | Reputable media (The Block, Messari, CoinDesk), Crunchbase, G2, Sacra |
| [C] | Community / opinion | Reddit, X threads, opinion blogs, Discord |
| [D] | Low-reliability | Unsourced aggregators, content farms, anonymous posts |

---

## Step A: Parse & Validate Input

**Required fields** (all 4):

| Field | Validation |
|-------|-----------|
| Product Name | Non-empty, ≤100 chars |
| Description | 2–5 sentences |
| Key Features | ≥3 items |
| Narrative / Positioning | Must contain target audience + value proposition |

**Optional**: Comparison Criteria, Known Competitors.

**Missing field → STOP.** Tell user what's missing. Don't proceed.

---

## Step B: Confirm Understanding + Industry Detection

```
📋 I understood your product as follows:
• Name: [name]
• Category: [inferred — EXPLICIT so user can correct]
• Industry branch: [🔗 Crypto / 🏢 Non-Crypto / Hybrid]
• Core value: [1 sentence]
• Key differentiators: [top 2–3]
• Comparison criteria: [list or "I'll select based on industry"]
• Known competitors: [list or "I'll discover from scratch"]

Does this look right?
```

User corrects → update, re-confirm. User OK → Step C.

**Industry Branch Detection** — Auto-detect based on product description:

| Signal Keywords | Branch | Metrics Focus | Extra Sources |
|----------------|--------|--------------|--------------|
| Token, chain, TVL, DeFi, wallet | 🔗 Crypto | TVL, volume, wallets, on-chain fees | DefiLlama, Dune, protocol dashboards |
| SaaS, pricing tiers, ARR, enterprise | 🏢 Non-Crypto | MRR/ARR, pricing, G2 rating, team size | G2, Capterra, SimilarWeb, Crunchbase |

If signals are ambiguous → use **both** branches, note the hybrid approach.

---

## Step C: Competitor Discovery & Battlefield Mapping (6–12 searches)

**Goal**: Not just find competitors — **map the structure of competition** (P6).

**Search 6–12 queries** across: category-based, feature-based, user-based, emerging, open-source, substitute behaviors.

**Classify into battlefield map:**

| Category | Definition |
|----------|-----------|
| 🎯 **Direct** | Same problem, same user, same approach |
| 🔄 **Indirect / Adjacent** | Same problem different approach, or expanding into your space |
| 🌱 **Emerging** | New entrants, forks, pre-launch |
| 🔀 **Substitutes** | Different tools/behaviors users use instead (e.g., "just launch manually on Raydium") |

For crypto projects, additionally tag: decentralized vs centralized, retail vs pro focus.

**Deep Dive Selection Rubric (HR-20)** — Score ALL direct competitors to determine deep dive priority:

| Criteria | Weight |
|----------|--------|
| ICP Overlap | 30 |
| Feature Overlap | 25 |
| Business Model Overlap | 20 |
| Traction Relevance | 15 |
| Recent Activity | 10 |

Rank by total score → deep dive top 3–5 → show scores in Battlefield Map.

**Edge cases**: 20+ found → list ALL, deep dive top 5 by rubric score. Known competitor not in search → add manually, note it.

**Output**: Battlefield map + full competitor list with URL, one-liner, tier, selection score.

---

## Step D: Deep Dive (top 3–5 by rubric — 3–5 searches PER competitor)

**For EACH competitor, collect from 4 sources:**

| Source | Search Pattern | Collects |
|--------|---------------|----------|
| 🗣️ Community | `[competitor] reddit twitter opinions` | Sentiment, praise, complaints |
| 🧠 Expert | `[competitor] review analysis blog 2025 2026` | Expert assessments, technical analysis |
| 📰 News | `[competitor] funding partnership news 2025 2026` | Funding, launches, incidents, pivots |
| ⛓️ On-chain (crypto) | `[competitor] TVL volume wallets metrics` | TVL, volume, fees, active wallets |

**Structure each profile in 2 layers (P5):**

**Layer A — Positioning (what they SAY):**
- Who do they say they serve? (their stated ICP)
- What's their USP / messaging?
- What narrative are they playing?

**Layer B — Execution (what they DO):**
- Traction: users, volume, traffic, social following (with "as of [date]")
- Product depth: feature breadth, shipping velocity, technical quality
- Monetization: revenue model clarity, fee structure, profitability signals
- Distribution: which channels drive growth, partnerships, viral mechanics

**Source Priority Ladder** — Per metric type, always use the highest-priority source available:

| Metric Type | P1 (best) | P2 | P3 | Fallback |
|------------|-----------|----|----|----------|
| Traffic | SimilarWeb | Semrush | Ahrefs | "Unknown" |
| Funding | Official announcement | Crunchbase | Media report | "Not publicly disclosed" |
| On-chain (crypto) | DefiLlama | Dune | Protocol docs | Media recap |
| Reviews (non-crypto) | G2 | Capterra | TrustRadius | "No review data" |
| Social metrics | Platform native (X, Discord) | Social Blade | Media mentions | "Unknown" |

**Fallback Proxy Policy** — When a primary metric is unavailable, use a proxy but ALWAYS label it:

| Missing Metric | Proxy | Label |
|---------------|-------|-------|
| Traffic | App downloads / Google Trends / on-chain wallets | `"Proxy: [X] used because traffic data unavailable"` |
| Revenue | Funding stage / team size | `"Proxy: [X] used because revenue not disclosed"` |
| Engagement rate | Follower count only | `"Proxy: follower count only — engagement data unavailable"` |
| MAU / DAU | On-chain active wallets / app store rankings | `"Proxy: [X] used because MAU not disclosed"` |

**Standardization rules (P2, P4):**
- Currency → USD
- Traffic → monthly uniques
- Social → followers + engagement rate
- Volume → daily average
- Conflicting numbers → range + note both sources
- No date → mark "date unknown, lower confidence"

**Freshness enforcement (HR-19):**
- **Metrics/traction** (volume, MAU, revenue, funding, traffic): prefer sources ≤3 months. If unavailable → fallback ≤12 months + flag "⚠️ Older — [X] months". >12 months → drop.
- **Context/background** (product model, founding, architecture): allow ≤12 months, flag if >3 months.
- **>12 months**: Drop entirely. Exception only: founding date, historical milestone.
- **Search query rule**: ALL metric searches MUST include date filter (year, "latest", "recent", month). E.g. `"Kalshi volume 2026"` not `"Kalshi volume"`.
- If first search returns only >3 month sources → try ≥2 more query variations with date filters. Still stale → fallback ≤12mo + flag. No ≤12mo → "Unknown".

**Strengths & weaknesses** must come from external sources (HR-11), structured as:
```
🗣️ Community says: "[finding]" — source: [URL], as of [date]
🧠 Expert says: "[finding]" — source: [URL], as of [date]
📰 News: "[development]" — source: [URL], as of [date]
⛓️ On-chain: [metric] — source: [platform], as of [date]
```

**Output**: Enriched profiles with positioning + execution layers, multi-source evidence.

---

## Step E: Strategic Synthesis

**This is the core intellectual work.** Steps C–D collect evidence. Step E answers the strategic questions.

### E1: Build Standardized Comparison Matrix (P2)
- User criteria first (HR-9), then AI adds 3–5
- User product = column 1 (HR-8)
- Each cell: 🟢🟡🔴 + text + source hint
- Same units, same timeframe across all columns
- Unknown data → "Unknown" (not blank, not guessed)
- Last row: "Overall Threat Level"

### E2: Who's Winning & Why (P1)
Answer: what factor is each top competitor winning on?
- Distribution advantage? (partnerships, viral mechanics, app store)
- Product advantage? (features, UX, technical depth)
- Pricing advantage? (cheaper, freemium, fee structure)
- Trust advantage? (brand, track record, regulatory compliance)
- Speed advantage? (shipping velocity, first-mover)

Not "Competitor A is strong" but "Competitor A is winning on distribution because [evidence]."

### E3: Strategic Whitespace (P7)
Must answer:
- What user segments are underserved by current players?
- What features has everyone copied → no longer a differentiator?
- What differentiation is still "winnable"?
- What positioning gap exists? (e.g., "no one owns the pro-user segment")

Each whitespace opportunity must be **actionable** (HR-14): what to build, who to target, why winnable.

### E4: Threats & Risk Signals (P4)
- ≥1 threat 🔴 Critical (HR-15)
- Include competitive threats (competitor moves) + structural threats (regulation, tech shifts)
- Each threat: severity + source + concrete mitigation (not "monitor")
- Fresh signals only — last 3 months for metrics, 12 months for context (HR-19)

### E5: Action Items & Watchlist (P8)
Every insight must produce "so what?":
- **Build**: Which feature/product to prioritize based on whitespace?
- **Message**: What positioning change based on competitive gaps?
- **Target**: Which segment to focus first?
- **Watch**: Which competitor + which metric + how often?
- **Benchmark**: Which KPIs to track against competitors regularly?

---

## Step F: Generate & Deliver

### F1: Generate Markdown (.md)

8.5 sections, each answers a strategic question:

| # | Section | Content |
|---|---------|---------|
| 1 | **Battlefield Map** | Visual structure: direct/indirect/emerging/substitutes. Not just a list — show relationships, dynamics. |
| 2 | **Standardized Comparison Matrix** | User product col 1, standardized units, 🟢🟡🔴 + text, threat levels. |
| 3 | **Deep Dive: Positioning vs Execution** | Per competitor: Layer A (say) + Layer B (do) + multi-source evidence + strengths/weaknesses from external sources. |
| 4 | **Who's Winning & Why** | Per top competitor: winning factor (distribution/product/pricing/trust/speed) + evidence. |
| 5 | **Strategic Whitespace** | ≥2 actionable gaps: underserved segments, commoditized features, winnable differentiations. |
| 6 | **Threats & Risk Signals** | Threat table: severity 🔴🟡🟢 + source + mitigation. ≥1 Critical. |
| 7 | **Action Items & Watchlist** | Build / Message / Target / Watch / Benchmark — specific enough to create tickets. |
| 8 | **Sources, Freshness & Confidence** | All URLs + dates + tier [A]-[D] + age in months. Confidence rating per section. Limitations paragraph. |
| 8.5 | **Self-Assessment Score** | 5 dimensions × 20 points (see below). |

**Output density targets:**

| Section | Target Length |
|---------|-------------|
| Battlefield Map | 300–500 words + tables + diagram |
| Comparison Matrix | Table only, no prose between rows |
| Deep Dive (per competitor) | 400–600 words |
| Who's Winning (per factor) | 150–250 words |
| Whitespace (per opportunity) | 200–300 words |
| Threats | Table + 1–2 sentence mitigation |
| Action Items | Bullet, ≤2 sentences per item |

### F2: Self-Assessment Score (Section 8.5)

| Dimension | Max | Measures |
|-----------|-----|---------|
| Evidence Quality | 20 | Source count, tier distribution, coverage gaps |
| Comparability | 20 | Standardized units, fair comparison across competitors |
| Strategic Usefulness | 20 | Answers all 4 strategic questions clearly |
| Freshness | 20 | % sources ≤3 months, flags applied correctly |
| Actionability | 20 | Build tickets with timelines, specificity |

If total <70 → add warning banner at top of report. If >30% sources are 3–12 months old → flag. Include a user override field.

### F3: Generate Word (.docx) — Optional
If a docx creation skill is available, generate .docx version (US Letter, Arial, professional tables, TOC, page numbers). If unavailable or fails → deliver .md only and notify user.

### F4: Deliver
Save to the current working directory or user-specified output path. Naming: `[ProductName]_Competitive_Intel_[MonthYear].md`. Present files + 3–4 sentence summary of key strategic findings.

---

## Example Input

```
Product Name: pump.fun
Description: Solana-native token launch platform. No-code meme token creation,
bonding curve trading, fair-launch mechanics, graduation to PumpSwap.

Key Features:
- No-code token creation on Solana
- Bonding curve trading from day one
- Fair-launch (no presales / no VC allocations)
- Fixed 1B supply template
- Auto graduation to PumpSwap
- Built-in discovery + viral social loop

Narrative: Target retail crypto on Solana — meme creators, speculators.
Value prop: "Launch and trade a meme coin instantly."
Differentiation: standardized fair-launch + bonding curve in one UX.

Comparison criteria: Launch friction, Token creation model, Trading mechanism,
Fair-launch policy, Graduation/DEX migration, Creator monetization, Trading fees,
Chain support, Discovery UX, Abuse/moderation controls

Known competitors: Moonshot, SunPump, Four.meme, Meteora, Raydium LaunchLab, Clanker
```

## Example Output Excerpt — Section 4: Who's Winning & Why

```markdown
## 4. Who's Winning & Why

### pump.fun — Winning on: Speed + Distribution
pump.fun dominates through launch friction (<30 seconds, wallet-only) and viral
social mechanics. Community feedback on Twitter/X consistently highlights the
"instant gratification" loop. On-chain: ~2M tokens created as of Feb 2025 [DeFiLlama].
**So what?** Speed is pump.fun's moat today. Competitors copying the bonding curve
won't catch up unless they match the distribution + social loop.

### Raydium LaunchLab — Winning on: Liquidity Infrastructure
Raydium's advantage isn't the launchpad — it's being the default AMM. Tokens
graduating from Raydium stay in-ecosystem with deeper liquidity pools.
**So what?** This is a structural advantage pump.fun addressed with PumpSwap.
Monitor whether PumpSwap liquidity reaches Raydium parity.

### Four.meme — Winning on: Chain Diversification
Only major player on BNB Chain. Captures users who won't bridge to Solana.
Expert analysis [The Block, Jan 2025] notes BNB meme volume grew 340% in Q4 2024.
**So what?** Chain lock-in is real. pump.fun's Solana-only bet is a deliberate
trade-off. If BNB/Base meme volume exceeds Solana → reassess.
```

---

## Failure Modes

| # | Failure | Handling |
|---|---------|---------|
| FM-1 | Missing required input | STOP. Ask. Don't proceed. |
| FM-2 | Niche market, few competitors | Expand indirect + substitutes (P6). Note in limitations. |
| FM-3 | Crowded market 20+ | List ALL. Deep dive top 5 by rubric score. |
| FM-4 | Private company, no data | "Unknown". Use proxy signals (Fallback Proxy Policy). NEVER fabricate. |
| FM-5 | Data conflict | Write range + note conflict. NEVER cherry-pick. |
| FM-6 | Community overwhelmingly negative | Note bias. Balance with expert + metrics. |
| FM-7 | Known competitor not found | Add manually. Research separately. Write "limited public info". |
| FM-8 | AI misunderstands product | Step B catches this. User corrects → restart. |
| FM-9 | .docx generation fails | Deliver .md. Notify error. |
| FM-10 | On-chain data for non-crypto | Skip on-chain source. Don't force it. |
| FM-11 | Only stale sources (>3mo) for metric | Try ≥2 query variations with date filter. Still stale → fallback ≤12mo + flag. No ≤12mo → "Unknown". |

---

## Acceptance Criteria

All must be true:

### Completeness
- [ ] 8.5 sections present, none empty
- [ ] ≥3 direct competitors deep-dived
- [ ] Battlefield map has ≥2 categories
- [ ] ≥2 whitespace opportunities

### Data quality
- [ ] Real URLs, no fabricated metrics
- [ ] Standardized units (USD, monthly, daily)
- [ ] "as of [date]" on every metric
- [ ] Conflicts noted with range
- [ ] Fact vs Inference labeled
- [ ] Source tiers [A]–[D] labeled (HR-18)
- [ ] Freshness flags applied (HR-19)

### Strategic depth
- [ ] Positioning vs Execution separated
- [ ] "Winning on what" answered per competitor
- [ ] Whitespace actionable with build tickets
- [ ] Action items ticket-ready
- [ ] Watchlist has competitor + metric + frequency

### Evidence
- [ ] ≥2/4 sources per deep dive
- [ ] Strengths/weaknesses cite external sources
- [ ] Sources table: URL + date + tier + age
- [ ] Limitations paragraph is honest

### Delivery
- [ ] .md delivered (+ .docx if available, or error noted)
- [ ] Naming convention correct
- [ ] Language matches input
