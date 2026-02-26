---
name: competitive-intelligence
version: "3.3"
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
| Traffic | SimilarWeb API [A] (`scripts/fetch_similarweb.py`) | SimilarWeb.com (manual) | Semrush | "Unknown" |
| Funding | Official announcement | Crunchbase | Media report | "Not publicly disclosed" |
| TVL | DefiLlama API `/tvl/{slug}` [A] | Dune | Protocol docs | Media recap |
| Volume (on-chain) | DefiLlama API `/summary/dexs/{slug}` [A] | Dune | CoinGecko | "Unknown" |
| Protocol fees / revenue | DefiLlama API `/summary/fees/{slug}` [A] | Token Terminal | Media estimate | "Unknown" |
| Token price / FDV | CoinGecko API v3 [A] | CoinMarketCap | Exchange data | "Unknown" |
| Reviews (non-crypto) | G2 | Capterra | TrustRadius | "No review data" |
| Social metrics | Platform native (X, Discord) | Social Blade | Media mentions | "Unknown" |

> **Conflict Resolution Rule**: When the same on-chain metric (TVL, fees, revenue, volume) is available from both DefiLlama and CoinGecko → **always use DefiLlama API**. CoinGecko is authoritative only for token price, market cap, and FDV. DefiLlama is authoritative for all protocol-level on-chain metrics.

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

## Step D.3: Web Traffic Enrichment (SimilarWeb API)

> **Run for ALL branches** (Crypto and Non-Crypto). Execute after Step D, before Step D.5/E.
> **Goal**: Fetch real-time web traffic metrics for every competitor domain via SimilarWeb API — deterministic, auditable, no hallucination.

### 4-Layer Pipeline

```
Step 1  POST /v1/visitsInfo for each domain  →  traffic_data_raw   (immutable audit)
Step 2  Normalize 9 metrics (deterministic)  →  traffic_metrics     (AI read-only)
Step 3  Store normalized layer               →  scripts/traffic.db
Step 4  AI reads traffic_metrics             →  §2.5 markdown table
```

### Execution Command

```bash
python3 scripts/fetch_similarweb.py \
  --domains "competitor1.com,competitor2.com,competitor3.com" \
  --run-id  "reportname_YYYY-MM" \
  --output  "section_2_5.md"
```

> ⚠️ `--domains` must be **comma-separated with no spaces**: `"a.com,b.com,c.com"`. Space-separated values (`"a.com b.com"`) cause an `"unrecognized arguments"` error — the script treats each space-separated token as a positional arg.

### Metrics Extracted (9 categories)

| # | Field | Source in API Response | Notes |
|---|-------|----------------------|-------|
| 1 | Monthly Visits (latest) | `EstimatedMonthlyVisits` max(date) | INT |
| 2 | MoM Change % | `EstimatedMonthlyVisits` prev month | NULL if < 2 months |
| 3 | Bounce Rate | `Engagments.BounceRate` | string → float |
| 4 | Pages / Visit | `Engagments.PagePerVisit` | string → float |
| 5 | Avg Visit Duration | `Engagments.TimeOnSite` | seconds → MM:SS |
| 6 | Global Rank | `GlobalRank.Rank` | INT |
| 7 | Top Country | `TopCountryShares[0]` | code + % share |
| 8 | Traffic Sources | `TrafficSources` | Direct/Search/Social/Referrals |
| 9 | Category Rank | `CategoryRank.Rank + .Category` | INT + name |

> **Fields NOT available** in `/v1/visitsInfo`: Audience gender, age groups, specific referrer domains.
> → Always render as `"Unknown"` — **never estimate or fabricate**.

### API Config

| Parameter | Value |
|-----------|-------|
| Endpoint | `POST https://similarweb-api1.p.rapidapi.com/v1/visitsInfo` |
| Body | `{"q": "domain.com"}` |
| Key header | `x-rapidapi-key: <SIMILARWEB_API_KEY>` |
| Host header | `x-rapidapi-host: similarweb-api1.p.rapidapi.com` |
| Rate limit | ~1.2s between calls |
| Key env var | `SIMILARWEB_API_KEY` (or hardcoded in script) |

### AI Report Rules (Step 4)

1. AI reads ONLY `traffic_metrics` table — **never raw_json**
2. `NULL` field → render as `"Unknown"` — **no inference**
3. No external API calls during report generation
4. All numbers must exist in normalized table
5. Each `run_id` is immutable — re-run = new `run_id`

**Output**: `scripts/section_2_5.md` → paste into §2.5 of report.

---

## Step D.5: Live Market Data 🔗 / Ecosystem Metrics 🏢

> **Both branches run this step** — with different methods. Execute after Step D, before Step E.
> **🔗 Crypto**: Fetch live token price, market cap, TVL, protocol fees from CoinGecko + DefiLlama APIs.
> **🏢 Non-Crypto**: Fetch GitHub traction, funding stage, skill/server counts, pricing, security benchmarks — see Non-Crypto subsection at end of this step.

### Universal Flow — Name → Market Data + TVL + Fees

**For EACH competitor (including user's product), execute this flow:**

#### Step 1 — Resolve CoinGecko ID
```
https://api.coingecko.com/api/v3/coins/list
```
Match order: 1) Exact name (case-insensitive) → 2) Symbol match → 3) Contains match.
- 1 match → use that ID
- Multiple matches → fetch `/simple/price` for each, pick highest market cap
- No match / uncertain → `Unknown` (do NOT guess)

#### Step 2 — Fetch Price + Market Cap
```
https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true
```
Extract: `usd` (price), `usd_market_cap` (MC), `usd_24h_change` (24h %)

#### Step 3 — Fetch FDV + ATH
```
https://api.coingecko.com/api/v3/coins/markets?ids={id}&vs_currency=usd
```
Extract: `fully_diluted_valuation`, `ath`, `ath_change_percentage`

#### Step 4 — Resolve DefiLlama Slug
```
https://api.llama.fi/protocols
```
Match by name (same logic as Step 1). Multiple matches → pick TVL > 0, then chain if known.
No match → `TVL = N/A (not DeFi / not indexed)`

#### Step 5 — Fetch TVL (aggregate all sub-slugs)
```
https://api.llama.fi/tvl/{slug}
```
Many protocols have multiple slugs (e.g., `hyperliquid-bridge`, `hyperliquid-hlp`, `hyperliquid-spot-orderbook`). Sum all relevant slugs → total TVL. Label breakdown: `Bridge $X + Pool $Y = $Z`

#### Step 6 — Fetch Protocol Fees
```
https://api.llama.fi/summary/fees/{slug}
```
Extract: `total24h`, `total7d`, `total30d`. Compute: `annualized = total30d × 12`.

#### Step 7 — Derived Metrics
If both MC and TVL available: `MC/TVL = market_cap / tvl`
If both MC and annualized revenue: `Price-to-Revenue = market_cap / annualized_revenue`
If both FDV and annualized revenue: `FDV/Revenue = fdv / annualized_revenue`

#### Step 8 — Recent Developments (30-day)
For each HIGH / MEDIUM-HIGH threat competitor, search:
```
"{competitor name}" 2026 news update (last 30 days)
```
Extract: major product launches, token unlocks, exchange listings, exploit/incident, partnership, funding.

#### Step 9 — Output per competitor
```
Token: {symbol}
Price: ${X}         | Market Cap: ${X}    | FDV: ${X}
24h: {X}%           | vs ATH: {X}%
TVL: ${X} ({breakdown})
Fees 24h: ${X}      | Fees 30d: ${X}      | Annualized Rev: ${X}
MC/TVL: {X}×        | MC/Rev: {X}×        | FDV/Rev: {X}×
Key development (30d): {1 sentence}
```

**Rules:**
- No token → `Token = N/A` (not error)
- TVL = N/A if not DeFi (AI tokens, L1 chains, infra)
- Fees = N/A if not indexed on DefiLlama fees
- API fails → write `[API error: {slug}]` and continue
- Do NOT fabricate. No source → "Unknown"
- **Multi-slug TVL**: Many protocols have multiple DefiLlama slugs (e.g., `lighter` + `lighter-bridge`). Sum ALL relevant slugs → label breakdown `"Bridge $X + Pool $Y = $Z total"`. Never use only 1 slug if multiples exist.

---

### 🏢 Non-Crypto Branch — Ecosystem Metrics

For non-crypto products, §2.6 replaces token/TVL/fees tables with developer & business ecosystem signals.

**Fetch for each competitor:**

| Signal | Source | How to Fetch |
|--------|--------|-------------|
| GitHub Stars + Forks | GitHub API [A] | `https://api.github.com/repos/{owner}/{repo}` → `stargazers_count`, `forks_count` |
| Skill / Server Count | Official website [A] | Product homepage / "Browse" / "Explore" page |
| Funding Stage | Crunchbase / official blog [B] | Web search `"{company} funding 2026"` |
| Pricing Tiers | Official pricing page [A] | Free / Freemium / Paid tiers |
| Security Benchmarks | Snyk [A] / CVE databases | Web search `"{company} security snyk 2026"` |
| Revenue Model | Official docs [A] | Transaction fee / SaaS / Ads / None |
| Recent 30d Developments | Web search [B] | `"{competitor}" 2026 launch update` |

**Output per competitor (paste into §2.6):**

```
Skills/Servers: {count}
GitHub Stars: {count}       | Forks: {count}
Funding: {stage}            | Investors: {names or "Unknown"}
Monthly Traffic: {X}/mo     (from §2.5)
Monetization: {model}       | Pricing: {tier}
Security: {score or "Not benchmarked"}
Key development (30d): {1 sentence}
```

**§2.6 section header template (non-crypto):**

```
> Sources: GitHub API [A] + official websites [A] + Crunchbase [B]
> Note: Non-crypto product. §2.6 tracks developer ecosystem metrics instead of TVL/token price.
> Conflict Resolution: Official documentation [A] authoritative for pricing/features.
```

**Additional tables** — add as available for the domain:
- **Security Benchmarks table** — if Snyk or equivalent data available (see SkillMarket AI report for example)
- **Funding & Stage table** — one row per competitor; include Stage, Funding amount if known, Key Investors, Revenue Model
- **Recent 30-Day Developments** — narrative paragraph per HIGH/MEDIUM-HIGH threat competitor

**Rules (Non-Crypto):**
- GitHub API public endpoint — no auth required for public repos
- If repo not found → `"Unknown"` (do NOT fabricate star count)
- Skill count = official count from website, not estimated; if unavailable → `"Unknown"`
- Security data: only cite if from authoritative source (Snyk, CVE, official security report)

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

| # | Section | Content | Crypto only? |
|---|---------|---------|-------------|
| 1 | **Battlefield Map** | Visual structure: direct/indirect/emerging/substitutes. Not just a list — show relationships, dynamics. | No |
| 2 | **Standardized Comparison Matrix** | User product col 1, standardized units, 🟢🟡🔴 + text, threat levels. Include Web traffic row + X followers row. | No |
| 2.5 | **Web Traffic Analysis** | Dedicated traffic table: rows = metrics (visits, bounce, top country, traffic mix, social, global rank, category rank), columns = competitors. **Method: Run `scripts/fetch_similarweb.py` (Step D.3) → paste output. API source = SimilarWeb RapidAPI [A].** Gender/age always "Unknown" (not in API). Mark "Unknown" if domain not indexed, don't fabricate. | No |
| 2.6 | **Live Market Data** 🔗 / **Ecosystem Metrics** 🏢 | 🔗 Crypto: Token prices, FDV, ATH, TVL, fees 24h/7d/30d, annualized revenue, MC/TVL, MC/Rev, FDV/Rev, recent 30d developments. Source: CoinGecko [A] + DefiLlama [A]. / 🏢 Non-Crypto: GitHub stars/forks, funding stage, skill/server counts, pricing, security benchmarks, revenue model. Source: GitHub API [A] + official docs [A] + Crunchbase [B]. | **Both branches** (different content) |
| 3 | **Deep Dive: Positioning vs Execution** | Per competitor: Layer A (say) + Layer B (do) + multi-source evidence + strengths/weaknesses from external sources. | No |
| 4 | **Who's Winning & Why** | Per top competitor: winning factor (distribution/product/pricing/trust/speed) + evidence. | No |
| 5 | **Strategic Whitespace** | ≥2 actionable gaps: underserved segments, commoditized features, winnable differentiations. | No |
| 6 | **Threats & Risk Signals** | Threat table: severity 🔴🟡🟢 + source + mitigation. ≥1 Critical. | No |
| 7 | **Action Items & Watchlist** | Build / Message / Target / Watch / Benchmark — specific enough to create tickets. | No |
| 8 | **Sources, Freshness & Confidence** | All URLs + dates + tier [A]-[D] + age in months. Confidence rating per section. Limitations paragraph. | No |
| 8.5 | **Self-Assessment Score** | 5 dimensions × 20 points (see below). | No |

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
| FM-12 | DefiLlama: protocol has multiple slugs | Sum ALL relevant slugs → label breakdown `"Bridge $X + Pool $Y = $Z total"`. Never use only 1 slug if multiples exist. Verify via `/protocols` list. |
| FM-13 | CoinGecko: multiple tokens match same name | Fetch `/simple/price` for each match → pick highest market cap. Log discarded as `"(discarded — lower MC)"`. |
| FM-14 | SimilarWeb: snapshot date > 3 months old | Note actual snapshot date + flag ⚠️ Older. Use most recent complete month available, do not fabricate. |
| FM-15 | SimilarWeb: domain returns 0 visits | Domain not indexed. Render as `"0"` + note `"(not indexed — FM-15)"`. Do NOT fabricate traffic estimate. |

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

### Live Market Data (🔗 Crypto only)
- [ ] Section 2.6 present with token prices from CoinGecko API (not web-scraped)
- [ ] TVL sourced from DefiLlama API, aggregated across ALL relevant sub-slugs (FM-12)
- [ ] Fees 30d + annualized revenue computed for each indexed protocol
- [ ] MC/TVL and MC/Revenue ratios calculated where data available
- [ ] Recent 30-day developments for HIGH/MEDIUM-HIGH threat competitors
- [ ] API errors documented as `[API error: {slug}]`, not silently dropped
- [ ] No-token protocols correctly marked "N/A" (not "Unknown" — different meaning)

### Ecosystem Metrics (🏢 Non-Crypto only)
- [ ] Section 2.6 present with GitHub stars, funding stage, skill/server counts
- [ ] Security benchmarks included if Snyk or equivalent data available
- [ ] Funding stage documented for all competitors (even if "Unknown")
- [ ] Monetization / pricing model documented for each competitor
- [ ] Non-crypto nature explicitly noted in §2.6 section header
- [ ] SimilarWeb 0-visit domains noted as "(not indexed — FM-15)", not fabricated
