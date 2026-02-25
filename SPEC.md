# Competitive Intelligence Report — Spec

---

## 0. Core Philosophies

Every design decision in this skill must follow these 8 philosophies. When there's a conflict between "add more data" and "answer the strategic question" → always choose the strategic question.

| # | Philosophy | One-liner |
|---|-----------|-----------|
| P1 | **Decision-first** | The report is a decision tool, not a data summary |
| P2 | **Comparable > many data** | Less data that's comparable > lots of scattered data |
| P3 | **Evidence-first, no fabrication** | No source → "Unknown". Conflicting numbers → write range + note conflict |
| P4 | **Freshness matters** | **Metrics/traction**: prefer sources ≤3 months. If unavailable → fallback ≤12 months + flag "⚠️ Older". **Context/background**: allow ≤12 months, flag if >3 months. >12 months → drop entirely. Write "as of [date]" for every metric |
| P5 | **Positioning ≠ Execution** | Clearly separate "what they SAY" vs "what they DO" |
| P6 | **Map the battlefield** | Draw market structure, don't just list competitors |
| P7 | **Find strategic whitespace** | Must identify gaps you can attack |
| P8 | **Actionable > academic** | Every insight must answer "so what?" |

---

## 1. Problem Statement

**From daily work:**

Every time the Product/Strategy team needs competitive intel:
- Must manually Google each competitor, open dozens of tabs, data scattered everywhere
- Each competitor's data collected differently → can't compare after reading (violates P2)
- Final report is usually a data dump — lots of info but doesn't answer "what should we do" (violates P1, P8)
- Easy to confuse strong branding with strong execution — only reading homepage copy (violates P5)
- Can't draw competitive structure, just listing competitors individually (violates P6)
- Doesn't identify which gaps to attack (violates P7)
- Feedback from community, experts, news scattered — nobody consolidates it

**Scenario:**
> Analyst receives request: "Board meeting next week, need competitive landscape for pump.fun." Analyst spends 2 days. Output: beautiful comparison table but different data per competitor, nobody can answer "where should pump.fun attack next." Head of Product asks: "So what?" — nobody can answer.

---

## 2. Objective

| Field | Value |
|-------|-------|
| **Solves what** | Transform competitive research from data dump into strategic decision tool |
| **For whom** | Ops & Data Analyst, Product Team, Strategy Team |
| **Output** | Report answering 4 strategic questions: Who do we compete with? Why are they winning? Where's the whitespace? What should we do? |
| **Replaces what** | 1–2 days manual research → ~30 min AI research + user review |

---

## 3. Input Contract

### 3.1 Accepted Input Methods
- File upload (Markdown, .txt, or any text file)
- Direct chat message
- Combination of both

### 3.2 Required Fields

| Field | Validation | If missing |
|-------|-----------|-----------|
| **Product Name** | Non-empty, ≤100 characters | Ask user |
| **Description** | 2–5 sentences describing the product | Ask user |
| **Key Features** | ≥3 items | Ask user if < 3 |
| **Narrative / Positioning** | Must contain target audience + value proposition | Ask user if missing |

### 3.3 Optional Fields

| Field | Default if not provided |
|-------|----------------------|
| **Comparison Criteria** | AI selects 8–10 criteria based on industry |
| **Known Competitors** | AI discovers from scratch |

### 3.4 Input Validation Rules
- Missing required field → **STOP, ask, don't guess** (P3)
- Empty or non-text file → notify error, ask again

---

## 4. Output Contract

### 4.1 Files

| File | Format | Naming |
|------|--------|--------|
| Main report | Markdown (.md) | `[ProductName]_Competitive_Intel_[MonthYear].md` |
| Formal report | Word (.docx) | `[ProductName]_Competitive_Intel_[MonthYear].docx` |

### 4.2 Report Structure — 8.5 Sections

Sections are designed to answer strategic questions, not to collect data categories.

| # | Section | Strategic Question | Priority | Philosophy |
|---|---------|-------------------|----------|-----------|
| 1 | **Battlefield Map** | Who are we competing with, and what's the market structure? | 🔴 Must | P6 |
| 2 | **Standardized Comparison Matrix** | Apple-to-apple comparison on same criteria? | 🔴 Must | P2 |
| 3 | **Deep Dive: Positioning vs Execution** | What they say vs what they actually do? | 🔴 Must | P5, P3, P4 |
| 4 | **Who's Winning & Why** | Who's winning — by distribution/product/pricing/trust/speed? | 🔴 Must | P1 |
| 5 | **Strategic Whitespace** | Which gaps can we attack? | 🔴 Must | P7 |
| 6 | **Threats & Risk Signals** | What should we worry about? Who could surprise us? | 🟡 Should | P4 |
| 7 | **Action Items & Watchlist** | What exactly should we do? Who to monitor? | 🔴 Must | P8 |
| 8 | **Sources, Freshness & Confidence** | Where is data from, how fresh, how reliable? | 🔴 Must | P3, P4 |
| 8.5 | **Self-Assessment Score** | How good is this report? 5 dimensions × 20 points | 🟡 Should | P3 |

### 4.3 Language Rule
Output language = input language.

---

## 5. Workflow (A → B → C → D → E → F)

### Step A: Parse & Validate Input
- **Input**: File or chat from user
- **Process**: Extract fields, validate (Section 3.4)
- **Output**: Structured product brief or questions if incomplete
- **⚠️ Pitfall**: Unusual file format → notify, ask again

### Step B: Confirm Understanding
- **Input**: Product brief from Step A
- **Process**: Summarize for user to confirm: name, category, differentiators, criteria, known competitors
- **Output**: Confirmation. User corrects → return to Step A. User OK → Step C
- **⚠️ Pitfall**: AI infers wrong category → always explicitly state inferred category

### Step C: Competitor Discovery & Battlefield Mapping (6–12 searches)
- **Input**: Confirmed brief
- **Process**: Search using 8 patterns. Classify results into battlefield map:
  - 🎯 Direct competitors
  - 🔄 Indirect / adjacent
  - 🌱 Emerging / new entrants
  - 🔀 Substitute behaviors/tools (P6 — map alternatives too, not just companies)
  - If crypto: tag decentralized vs centralized, retail vs pro focus
- **Output**: Battlefield map + full competitor list
- **⚠️ Pitfall**: 20+ results → list ALL, deep dive top 5 direct
- **⚠️ Pitfall**: Known competitor not found → add manually, note it

### Step D: Deep Dive Research (top 5 direct — 3–5 searches PER competitor)
- **Input**: Competitor list from Step C
- **Process**: For each competitor, search 4 source types:

  | Source | Search Pattern | Collects |
  |-------|---------------|----------|
  | 🗣️ Community | `[competitor] reddit twitter opinions` | Sentiment, complaints, praised features |
  | 🧠 Expert | `[competitor] review analysis blog 2025 2026` | Expert assessment, technical analysis |
  | 📰 News | `[competitor] funding partnership news 2025 2026` | Funding, launches, incidents |
  | ⛓️ On-chain (crypto) | `[competitor] TVL volume wallets metrics` | TVL, volume, fees, active wallets |

- **Output**: Per competitor, separate into 2 layers (P5):
  - **Positioning layer**: What do they say? ICP, USP, narrative
  - **Execution layer**: Traction, product depth, shipping velocity, monetization, distribution channels
  - Every claim must cite source + write "as of [date]" (P3, P4)

- **Standardization rules (P2)**:
  - Currency: convert to USD
  - Traffic: monthly unique visitors
  - Social: X followers + engagement rate
  - Volume: daily average (crypto)
  - **Freshness enforcement (P4)**:
    - **Metrics/traction data** (volume, MAU, revenue, funding, traffic): prefer sources ≤3 months. If unavailable → fallback ≤12 months + flag "⚠️ Older — [X] months". >12 months → drop.
    - **Context/background** (product description, business model, founding story): allow ≤12 months, flag if >3 months "⚠️ Older — [X] months".
    - **>12 months**: Drop entirely. Do not cite. Only exception: founding date, historical milestone.
  - **Search query enforcement**: All metric/traction search queries MUST include year filter (e.g. "2026", "2025 2026", "latest", "recent"). See Section 6.6.
  - Conflicting data between sources → write range + note conflict

- **⚠️ Pitfall**: No data → "Unknown". Community bias negative → note, balance with expert + metrics
- **⚠️ Pitfall**: On-chain only for crypto → skip if not relevant

### Step E: Synthesize Strategic Analysis
- **Input**: Enriched profiles from Step D + comparison criteria
- **Process**:
  1. Build standardized comparison matrix (user criteria first, AI adds 3–5) (P2)
  2. Analyze "who's winning and why" — distribution, product, pricing, trust, speed (P1)
  3. Find whitespace — underserved user segments, commoditized features, winnable differentiations (P7)
  4. Assess threats + risk signals (P4)
  5. Generate action items + watchlist (P8)
- **Output**: Sections 2, 4, 5, 6, 7 content
- **⚠️ Pitfall**: All-green for user → bias. Must find gaps. If none found → not honest enough

### Step F: Generate & Deliver
- **Input**: All data from Steps C–E
- **Process**: Write 8.5-section report → .md → .docx → save both
- **Output**: 2 files in `/mnt/user-data/outputs/`
- **⚠️ Pitfall**: .docx fails → deliver .md, notify error

---

## 6. Hard Rules

| # | Rule | Philosophy |
|---|------|-----------|
| HR-1 | **No fake competitors.** Every competitor has a real URL. | P3 |
| HR-2 | **No fake metrics.** Not found → "Unknown". | P3 |
| HR-3 | **No guessed pricing.** Not public → state so. | P3 |
| HR-4 | **Conflicting numbers → write range + note conflict.** Never cherry-pick. | P3 |
| HR-5 | **Label Fact vs Inference.** Fact has source. Inference must be labeled "Inference:". | P3 |
| HR-6 | **Every metric has "as of [date]".** Metric without date → lower confidence. | P4 |
| HR-7 | **Standardize units.** USD, monthly, daily average. No mixing. | P2 |
| HR-8 | **User product = column 1** in comparison matrix. | P1 |
| HR-9 | **User-specified criteria MUST appear** in matrix. | P1 |
| HR-10 | **Separate Positioning vs Execution** in every deep dive. Never mix. | P5 |
| HR-11 | **Strengths/weaknesses from external sources** — not AI's own assessment. | P3 |
| HR-12 | **Each deep dive covers ≥2 of 4 sources.** Missing source → write "No [source] found." | P3 |
| HR-13 | **Every insight has "so what?"** — don't stop at observation. | P8 |
| HR-14 | **Whitespace must be actionable** — answer "attack where", not just "gap here". | P7 |
| HR-15 | **≥1 threat rated High or Critical.** All-green = not thorough enough. | P1 |
| HR-16 | **Output language = input language.** | — |
| HR-17 | **Missing required input → STOP and ask.** | P3 |
| HR-18 | **Source confidence tier required.** Every source labeled [A]–[D]. D-source claims must flag ⚠️. | P3 |
| HR-19 | **Freshness gate.** Metrics: prefer ≤3 months, fallback ≤12 months + flag "⚠️ Older". Context: ≤12 months OK, flag if >3 months. >12 months → DROP. Metric search queries MUST include date filter. | P4 |

---

## 6.6 Search Freshness Enforcement (P4)

**Problem**: Web search returns results by relevance, not recency. Without enforcement, reports will cite 6–9 month old sources for rapidly changing metrics.

### Rules

**1. Date filter in search queries:**
- All searches for **metrics/traction** (volume, MAU, revenue, funding, traffic, users) → MUST add date term to query
- Examples:
  - ✅ `"Kalshi volume February 2026"` or `"Kalshi volume 2026"`
  - ✅ `"Polymarket MAU latest 2026"`
  - ❌ `"Kalshi volume"` (no date → may return 2024 article)
- Accepted date terms: current year, "latest", "recent", "2025 2026", specific month

**2. Post-search freshness check:**
- After receiving results, check each source's age BEFORE citing:
  - **≤3 months**: ✅ Use for metrics + context (preferred)
  - **3–12 months**: ⚠️ Use for context. For metrics ONLY if no ≤3 month source exists (fallback) — flag "⚠️ Older — [X] months".
  - **>12 months**: ❌ Drop entirely. Exception: founding date, historical milestone.
- If NO source ≤12 months found for a metric → write "Unknown — no source within 12 months found".

**3. Source table enforcement:**
- Section 8 (Sources) MUST include "Age" column for every source
- Report self-check: if >30% of sources are in the 3–12 month range → flag warning in Section 8.5

### Examples

| Search purpose | Bad query | Good query |
|---------------|-----------|------------|
| Competitor volume | `Limitless exchange volume` | `Limitless exchange volume 2026` |
| MAU data | `Polymarket active users` | `Polymarket monthly active users latest 2026` |
| Funding round | `Kalshi funding` | `Kalshi funding 2025 2026 latest` |
| Product background | `Azuro protocol overview` | `Azuro protocol` (OK — context, no date needed) |

---

## 7. Acceptance Criteria

### Report completeness
- [ ] 8.5 sections present, none empty
- [ ] ≥3 direct competitors deep-dived
- [ ] Battlefield map has ≥2 categories (not just "direct")
- [ ] Whitespace section has ≥2 actionable opportunities

### Data quality (P2, P3, P4)
- [ ] Every competitor has a real URL
- [ ] No metrics fabricated
- [ ] Units standardized (USD, monthly, daily)
- [ ] Every metric has "as of [date]"
- [ ] Conflicting numbers show range + note
- [ ] Fact vs Inference clearly distinguished
- [ ] Source tiers [A]–[D] labeled
- [ ] Freshness flags applied per HR-19

### Strategic depth (P1, P5, P7, P8)
- [ ] Deep dives separate Positioning vs Execution
- [ ] "Who's winning & why" answers with specific winning factors
- [ ] Whitespace identifies ≥2 attackable gaps
- [ ] Action Items specific enough to create tickets
- [ ] Watchlist includes competitor + metric + frequency

### Evidence quality (P3)
- [ ] Each deep dive covers ≥2 of 4 source types
- [ ] Strengths/weaknesses cite external sources
- [ ] Sources section has URL + date + tier + age
- [ ] Limitations paragraph is honest

### Deliverables
- [ ] .md + .docx (or .docx error noted)
- [ ] Naming convention correct
- [ ] Language matches input

---

## 8. Failure Modes & Handling

| # | Failure Mode | Handling |
|---|-------------|---------|
| FM-1 | Missing required input | STOP. Ask. Don't proceed until complete. |
| FM-2 | Niche market, few competitors | Still complete. Expand indirect + substitutes (P6). Note in limitations. |
| FM-3 | Crowded market 20+ | List ALL. Deep dive top 5. Document selection criteria. |
| FM-4 | Private company, no data | "Unknown". Use proxy signals. NEVER fabricate. (P3) |
| FM-5 | Data conflict between sources | Write range + note conflict. NEVER cherry-pick. (P3) |
| FM-6 | Community feedback overwhelmingly negative | Note bias. Balance with expert + metrics. (P3) |
| FM-7 | Known competitor not found in search | Add manually. Research separately. Write "limited public info". |
| FM-8 | AI misunderstands user's product | Step B catches this. User corrects → restart. |
| FM-9 | .docx generation fails | Deliver .md. Notify error. |
| FM-10 | On-chain data for non-crypto product | Skip on-chain source. Don't force it. |
| FM-11 | **Search only returns stale sources (>3 months) for a metric** | Try ≥2 query variations with date filter. Still stale → fallback to best ≤12 month source + flag "⚠️ Older — [X] months". No ≤12 month source → write "Unknown". (P4, HR-19) |

---

## 9. Example Input — pump.fun

### Product Name ✅ Required
pump.fun

### Description ✅ Required
pump.fun is a Solana-native token launch platform that lets anyone create and trade meme tokens instantly with a no-code flow. It uses a bonding curve model so tokens are tradable from launch without needing a traditional liquidity pool setup. The platform positions itself around fair-launch mechanics (no presales / no insider allocations) and low-friction creation for viral, community-driven coins. Tokens can later graduate from the bonding curve and migrate into Pump.fun's trading infrastructure (PumpSwap).

### Key Features ✅ Required
- No-code token creation on Solana
- Bonding curve trading from day one
- Fair-launch structure (no presales / no VC allocations)
- Fixed token supply template (1B supply standard)
- Graduation / migration flow to PumpSwap
- Built-in discovery + viral social loop

### Narrative / Positioning ✅ Required
- **Target audience**: Retail crypto users on Solana — meme coin creators, speculators, trend chasers
- **Value proposition**: "Launch and trade a meme coin instantly" — no coding, low friction, immediate liquidity
- **Differentiation**: Standardized fair-launch + bonding-curve flow combining creation, trading, migration in one UX

### Comparison Criteria 🟡 Optional
- Launch friction
- Token creation model
- Trading mechanism
- Fair-launch policy
- Graduation / DEX migration
- Creator monetization
- Trading fees
- Chain ecosystem support
- Discovery UX
- Abuse / moderation controls

### Known Competitors 🟡 Optional
- Moonshot, SunPump, Four.meme, Meteora, Raydium LaunchLab, Clanker, pump forks on other chains

---

## 10. File Structure

```
competitive-intelligence-skill/
├── spec.md                     # This file — source of truth
├── SKILL.md                    # Instructions for Claude (must match spec)
└── input-template.md           # Template for user's product brief
```
