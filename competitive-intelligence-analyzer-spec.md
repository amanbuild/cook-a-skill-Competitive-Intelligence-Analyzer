# Skill Spec: Competitive Intelligence Analyzer  
Version: 0.1 | Owner: Tiger  
Platform: Web / Research Tools  
Status: Draft — Pending Supervisor Review  

---

## 1. Problem Statement

Every time the product or strategy team needs to understand the competitive landscape, they must manually research each competitor across multiple scattered sources (websites, social media, review sites, analytics tools, funding databases).

Consequences:

- 1–3 days wasted to assemble a basic competitor overview  
- Data is fragmented (social, traffic, features, funding, reviews in different places)  
- Hard to compare competitors in a single, trusted view → decisions rely on gut feeling  
- Easy to miss emerging competitors or adjacent products  
- No consistent framework for identifying white-space and differentiation opportunities  

---

## 2. Skill Overview

**Input:** product spec `.md` file → clarifying questions → Skill identifies a list of 5–10 closest competitors → collects structured data (positioning, features, pricing, marketing channels, reviews, traction, funding, company health) → builds a comparison matrix and strategic insights.

**Output:**  
1 complete markdown block including:

- Competitor shortlist with rationale  
- Comparison table (features, positioning, traction, pricing, marketing, reviews, company health)  
- Highlighted competitive advantages and gaps vs. the market  
- Recommended opportunities and risks for product/strategy teams  

---

## 3. Target Users

- Ops & Data Analysts  
- Product Managers / Product Strategy  
- Growth / Marketing Strategy  
- Founders and BizOps  

**Prerequisite:** User already has a product spec `.md` file or a clear product description.

---

## 4. Input Requirements

### 4.1 `spec.md` — Required Fields

These fields must exist in the product spec, or be explicitly provided via clarifying questions.

| Field              | Description                                           | Usage in Skill                                           |
|--------------------|-------------------------------------------------------|----------------------------------------------------------|
| product_name       | Product / protocol / app name                        | Appears in all outputs and titles                       |
| product_category   | Category / niche (e.g., CRM, DeFi DEX, HR SaaS)      | Basis for competitor search and comparison dimensions   |
| target_customer    | ICP (who it’s for: segment, size, role)              | Guides competitor selection and positioning analysis    |
| jobs_to_be_done    | 1–3 core problems / use cases                        | Determines functional overlap with competitors          |
| key_features       | 3–10 core features / capabilities                    | Used to compare feature coverage and table stakes       |
| market_region      | Geography (e.g., US, EU, global)                     | Filters competitors to relevant markets                 |

### 4.2 Optional Fields

These fields strongly improve output quality but are not mandatory.

| Field                  | Description                                      | Impact When Missing                                      |
|------------------------|--------------------------------------------------|----------------------------------------------------------|
| pricing_model          | Pricing structure (e.g., per-seat, usage-based) | Pricing comparison becomes higher-level / approximate   |
| pricing_range          | Price tiers or ranges                            | Cannot highlight under/over-pricing precisely           |
| tech_stack             | Tech stack, chain (for crypto), infra           | Less accurate technical differentiation                 |
| go_to_market_channels  | Existing channels (SEO, paid, partnerships)      | Limited marketing/channel gap analysis                  |
| current_traction       | Any known KPIs (users, revenue, TVL)            | Harder to benchmark relative traction                   |
| competitors_known      | Known competitors list from user                | Skill may miss niche incumbents the user cares about    |
| constraints            | Regulatory / compliance / industry constraints   | Weaker risk & moat analysis                             |

### 4.3 Clarifying Questions (Mandatory)

Before generating any output, the skill MUST ask the following core questions (grouped in **one message**). If `spec.md` lacks key required fields, the skill may ask up to **3 additional questions** at the same time.

**Q1 — Goal of the Analysis**

> “What is the main goal of this competitive analysis?  
> (A) Market landscaping (see who’s out there)  
> (B) Positioning & messaging  
> (C) Feature roadmap & gaps  
> (D) Investor / fundraising materials  
> (E) Other — please specify.”

**Q2 — Market Scope**

> “Which market scope should we focus on?  
> (A) Global  
> (B) Specific regions (please list)  
> (C) Only English-speaking markets  
> (D) Only Web3/crypto-native projects (if relevant).”

**Q3 — Competitor Depth**

> “How deep should we go per competitor?  
> (A) Quick scan — more competitors (8–12) with lighter detail  
> (B) Deep dive — fewer competitors (5–7) with more depth  
> (C) Balanced default — 5–10 with standard depth (recommended).”

**Q4 — Known Competitors**

> “Do you already have competitors in mind that must be included?  
> If yes, list their names/URLs. If no, answer ‘None’.”

**→ Generation starts only after all Q1–Q4 are answered.**  
If required fields are missing in `spec.md`, ask **up to 3 extra** questions (e.g., to confirm product_category, target_customer, or market_region) in the same clarification step.

---

## 5. Processing Logic (Mandatory Sequence)

### Step 1: Spec Quality Check

Scan `spec.md` → compute **Readiness Score** to decide how far to proceed and how many assumptions to make.

**Scoring Method:**

- Each **required field (Section 4.1)**:
  - Complete & clear: **+1.5 points**  
  - Present but vague (“everyone”, “global” without context): **+0.5 points**  
  - Missing: **0 points**
- At least **2 useful optional fields (Section 4.2)**: **+1 point total** (not per field)

Total scale: **10 points** (6 required × 1.5 = 9 + 1 bonus).

**Actions by Score:**

- **8–10:** Proceed with full workflow and deep analysis.  
- **5–7:** Proceed, but:
  - Mark all assumptions clearly in the output  
  - Flag which fields were weak/missing  
- **< 5:**  
  - Stop.  
  - Output a **Readiness Report** listing:
    - Per-field scores  
    - Missing/vague fields with suggested questions  
  - Ask user to improve `spec.md` before continuing.

---

### Step 2: Product & Market Analysis

Determine:

- **Segment:** B2B vs B2C vs prosumer  
- **Complexity level:** simple tool / multi-product suite / full platform  
- **Purchase context:** low-touch self-serve vs sales-led / enterprise  
- **Risk & compliance sensitivity:** finance, health, infra, etc.  
- **Crypto-specific (if applicable):**
  - Chain (Solana/Ethereum/Base/other)  
  - On-chain/off-chain components  
  - TVL/volume relevance  

This step defines the **comparison lens**: what truly matters in this category (e.g., TVL & fees in DeFi, integrations & workflows in B2B SaaS).

---

### Step 3: Competitor Discovery

Use product_category, target_customer, and jobs_to_be_done to:

1. Generate **category keywords** and “alternatives to X” queries.  
2. Identify:
   - Direct competitors (same category & ICP)  
   - Indirect / adjacent competitors (solve same JTBD differently)  
3. Combine:
   - User-specified competitors (from Q4 and `competitors_known`)  
   - Discovered competitors.

Then:

- Rank the candidates by **relevance** to ICP, JTBD, and market_region.  
- Select **5–10** competitors based on Q3 preference (quick scan vs deep dive vs balanced).

---

### Step 4: Data Collection Per Competitor

For each selected competitor, gather structured data across the **6 layers** (mirroring your original description):

1. **Strategy & Positioning**  
   - Mission/tagline, who they say they serve, problem statement  
   - Core differentiator and what they clearly *do not* serve  

2. **Product & Features**  
   - Product description, complexity level (tool vs platform)  
   - Key features & technical strengths  
   - Integrations and ecosystem breadth  
   - Obvious missing features (from reviews and docs)  

3. **Pricing & Business Model**  
   - Pricing tiers and inclusions  
   - Free tier/trial presence and funnel shape  
   - Model: per-seat, per-usage, flat-rate, freemium, token-based (crypto)  
   - Relative pricing positioning (budget / mid-market / premium)  

4. **Marketing & Distribution**  
   - Acquisition channels: SEO, paid, content, social, referrals, partners  
   - Channel strengths & weaknesses  
   - Content strategy themes (what topics they emphasize)  

5. **Customer Reviews (Critical Layer)**  
   - Pull 20+ reviews where possible (G2, Capterra, Trustpilot, app stores, Reddit, X)  
   - Categorize feedback into:
     - Feature gaps  
     - UX frustrations  
     - Pricing complaints  
     - Support/onboarding complaints  
   - Track what customers praise as table stakes.

6. **Company Health & Trajectory**  
   - Founded year, funding (if any), investors (high-level)  
   - Headcount trend (approx., via LinkedIn)  
   - Product & company news direction (expansion vs consolidation)  

When data is not available or unclear, **explicitly mark** “Not found (checked: [sources])”.

---

### Step 5: Comparison Matrix Assembly

Normalize data into a **standard schema** so multiple competitors can be compared at a glance. For each competitor:

- **What is the product?**  
  - Niche & JTBD  
  - USP (speed, cost, UX, security, liquidity, compliance, integrations)  
  - Product status (idea / beta / GA / revenue-generating)  
  - Chain (for crypto)  

- **Market fit & traction (easiest to check):**  
  - Monthly website visits (approximate)  
  - Social followers (Twitter/X, LinkedIn, etc.)  
  - TVL / volume / fees (if relevant)  
  - Revenue or proxy metrics (if publicly hinted)  
  - Sustainability: incentives vs organic traction  

- **Pricing:**  
  - Fee/pricing model  
  - Transparent vs opaque pricing  
  - Value vs cost, with note if users feel it’s worth it (from reviews).

Matrix is delivered as a markdown table plus brief notes per competitor for context.

---

### Step 6: Advantage & Gap Analysis

Using the matrix:

- Identify where **your product leads**:
  - Specific feature edges  
  - Better pricing model for certain segments  
  - Simpler/better UX for a given JTBD  
  - Stronger focus on neglected ICP segments or regions  

- Identify **where competitors lead**:
  - Features or integrations you lack  
  - Clearer messaging or tighter positioning  
  - Stronger traction/funding or brand trust  

- Distill **opportunities**:
  - Underserved segments  
  - Pricing gaps (no entry-tier, no mid-tier, etc.)  
  - Channels no one is using strongly  
  - Repeated user complaints across competitors (e.g., complexity, support)  

---

### Step 7: Output Assembly

Compile everything into **one markdown block** in this order:

1. **Executive Summary** (5–10 bullets)
   - Product name and analysis goal (from Q1)  
   - Number of competitors analyzed and type (direct/adjacent)  
   - 3–5 key insights (e.g., “market crowded on feature X, weak on Y”)  
   - Top 3 opportunities & top 3 risks  
   - Readiness Score and any major assumptions  

2. **Competitor Shortlist**  
   - Table with: Name, URL, Category, ICP, Why relevant  

3. **Comparison Matrix**  
   - Main matrix covering:
     - Positioning highlights  
     - Feature coverage (relative to your key_features)  
     - Pricing model & relative level  
     - Traction proxies (traffic, social, TVL, etc.)  
     - Company health signals  

4. **Layered Analysis (Layers 1–6)**  
   - Section per layer, summarizing cross-competitor patterns  
   - Explicitly call out repeated complaints and praises  

5. **Your Product vs Market**  
   - Advantage summary  
   - Weakness/gap summary  
   - Suggested strategic directions (positioning/roadmap/pricing/GTMs)  

6. **Sources & Caveats**  
   - List of main data sources used (categories, not raw URLs)  
   - Note about approximate nature of public metrics  
   - List all explicit assumptions used due to missing data  

---

## 8. Business Rules

**Always Do:**

- Clearly mark assumptions and missing data (never silently guess).  
- Keep competitor count within requested range (Q3) and justify inclusions.  
- Treat user’s listed competitors as **must-include** unless clearly out-of-scope.  
- Use recent and reputable sources for funding/headcount when available.  
- State the **date context** for metrics (e.g., “as of Feb 2026”).  

**Never Do:**

- Do NOT fabricate metrics (revenue, TVL, funding) if not found. Summarize qualitatively instead.  
- Do NOT claim exact market share unless backed by clear, cited data.  
- Do NOT present estimates without a “rough/approximate” disclaimer when appropriate.  
- Do NOT ignore user constraints on scope or region.  
- Do NOT recommend strategic pivots without clearly stating trade-offs and uncertainties.  

**Ask First:**

- When product touches **regulated domains** (finance, health, children, personal data), ask if there are specific regulatory constraints to consider.  
- When product is chain-specific, confirm if **multi-chain expansion** is in scope before recommending it.  

---

## 9. Success Criteria

Output is considered successful when:

- Product / strategy team can use the report to:
  - Understand the **current competitive landscape** in 1 reading  
  - Clearly explain “how we differ” vs. top 5–10 competitors  
  - Identify at least 3–5 **prioritized opportunities or risks**  

- PM / founder can:
  - Feed the comparison directly into roadmap discussions (feature gaps)  
  - Use sections of the report in investor decks / internal memos without heavy editing  

- Analysts can:
  - Re-run the skill later with an updated spec and get **consistent structure**, enabling time-based comparison.  

---

## 10. MVP Boundary (Minimum Viable — 2 Days)

**In Scope (MVP):**

- Readiness Score and spec quality check with rubric (Section 5 Step 1)  
- Automatic discovery and selection of **5–10** relevant competitors  
- Standardized comparison matrix covering:
  - Positioning & ICP  
  - Key features & integrations (relative to product spec)  
  - Pricing model and rough level  
  - Basic traction proxies (traffic/social/TVL when relevant)  
  - High-level company health (age, funding presence/absence, headcount trend approx.)  
- Core layered analysis:
  - Layers 1–5 required (Strategy, Product, Pricing, Marketing, Reviews)  
  - Layer 6 (company health) at high level only (no deep financial modeling)  
- Advantage/gap summary and clear list of opportunities/risks  

**Out of Scope (for later versions):**

- Automated chart/graph generation (visual dashboards)  
- Direct integrations with paid tools (Ahrefs, Similarweb, Crunchbase API, etc.)  
- Ongoing monitoring / alerts for new competitors or major changes  
- Deep financial modeling (LTV/CAC, runway estimates, full revenue projections)  
- Multi-language source analysis and output  

---
