# Competitive Intelligence Analyzer — Spec

**Owner:** Amando  
**Primary Users:** Ops & Data Analyst / Product Team / Strategy  
**Goal:** Generate an auditable competitive landscape report from a single product spec.

---

## 1) Objective

From one product specification (Markdown or plain text), the skill will:

- Extract **Domain / Category / ICP / JTBD / USP hypothesis / Key features**
- Discover **5–10 competitors** (direct + optional adjacent, based on scope)
- Collect **public, source-linked data** per competitor  
  - **MVP Required:** **Similarweb monthly visits** + **X (Twitter) followers**
  - **Crypto Optional:** TVL / volume / audits / chain support when publicly available
- Output a **single Markdown report** containing:
  - competitor list + rationale
  - comparison matrix
  - actionable insights (advantages/gaps/whitespace)
  - sources appendix for auditing

**Hard rules**
- **No fabrication.** If you cannot verify, write `Unknown`.
- Every important claim must be **evidence-linked** (URL + retrieved date).
- Conflicting numbers must be marked as **CONFLICT** and shown side-by-side with sources.

---

## 2) Problem Statement

Competitive research is usually manual: teams check each competitor one-by-one (social followers, web traffic, TVL if crypto, traction, features). This is slow, scattered across sources, hard to compare, and easy to miss emerging competitors.

---

## 3) Business Value

- A single, structured, auditable view of the competitive landscape
- Decisions based on **real data**, not gut feel
- Fast re-assessment whenever the market changes

---

## 4) Scope

### 4.1 In Scope (MVP)
- Input: **1 product spec** (Markdown or text)
- Output: **1 Markdown competitive report**
- Competitors: **5–10**
- Required data fields per competitor:
  - official website + short description
  - **Similarweb monthly visits** (or `Unknown`)
  - **X followers**
  - evidence-linked feature summary (from product/docs pages)
  - optional traction proxies (funding/users/TVL/volume) if publicly sourced

### 4.2 Out of Scope (MVP)
- Login-only / paywalled sources
- Estimating MAU/revenue or “guessing” traction
- Full market studies, legal/financial due diligence

---

## 5) Input Contract

### 5.1 Required fields to extract (from spec)
The skill must extract at minimum:
- Product name
- Category / narrative (e.g., on-chain analytics, perp DEX, infra, wallet)
- Target user (ICP)
- Core problem (JTBD)
- Key features (3–10)
- Differentiator hypothesis (USP)
- Market scope if present (B2B/B2C, regions, chains)

### 5.2 Optional user controls
- Competitor scope: `direct | adjacent | both`
- Geo focus: `global | US | SEA | ...`
- Chain focus (crypto): `ETH | SOL | BSC | ...`
- Competitor count: `5..10`
- Must-include competitor list (user provided)

---

## 6) Output Contract (Markdown)

### 6.1 Required report sections
1. **Executive Summary** (5–10 bullets)
2. **Product Understanding** (ICP / JTBD / USP / Features)
3. **Competitor Set (5–10)**  
   - Name, URL, 1-line description  
   - “Why included” rationale
4. **Comparison Matrix** (side-by-side table)
5. **Key Insights & Actions**
   - competitive advantages (yours vs market)
   - parity baseline (features everyone has)
   - gaps (features you lack vs leaders)
   - whitespace (underserved angles)
   - research TODOs (missing data → explicit tasks)
6. **Sources Appendix**
   - per competitor: sources grouped by field (traffic, social, pricing, TVL, audits, features)

### 6.2 Comparison Matrix (normalized)
**Columns:** Your product + each competitor  
**Rows (recommended 10–12 for crypto-first, but works broadly):**
- Positioning (1-liner)
- Target users (ICP)
- Primary chain(s) supported (crypto)
- Core features (3–5 bullets)
- Differentiator claim (evidence-linked)
- Pricing model (Free/Freemium/Subscription/Fees/Token) + source
- **X followers** + source
- **Similarweb monthly visits** + source
- Crypto traction (optional): TVL / volume / OI / integrations + source
- Trust signals: audits/bug bounty + source
- Integrations/ecosystem + source
- Notable gaps (`Evidence` or `Unknown`)

**Data rules**
- If no reliable source: write `Unknown`
- If multiple reliable sources disagree: show both + mark `CONFLICT`

---

## 7) Workflow (Deterministic)

### Step A — Parse & Normalize Product Spec
- Extract: name, category, ICP, JTBD, USP hypothesis, features
- Map into a **stable taxonomy** for better competitor discovery (crypto-first examples):
  - Trading (Perps/Spot), Wallet, On-chain Analytics, Infra/RPC, Bridge,
    Lending, Launchpad, Security, Data/Indexing, Copy Trading, Portfolio

### Step B — Competitor Discovery (5–10)
**Discovery approach (no guessing):**
- Build seed keywords from: category + ICP + top features + chains
- Search candidates via:
  - “alternatives”, “competitors”, “similar to”
  - public directories/listings (where available)
- Deduplicate by domain
- Use a simple explainable fit score:
  - +2 same direct category
  - +1 same ICP
  - +1 same chain/ecosystem
  - +1 major feature overlap
- Select top N, plus 1–2 adjacent if scope = `both`

### Step C — Data Collection (per competitor)
Collect each field with:
- `value`
- `source_url`
- `retrieved_at`

**MVP required collectors**
- X followers (from X profile or reliable API output)
- Similarweb monthly visits (from Similarweb page/API output)

**Optional crypto collectors**
- TVL (e.g., DeFiLlama if available)
- Volume/OI (public analytics sources)
- Audits (audit report pages)
- Pricing (pricing/docs pages)

### Step D — Evidence-Linked Feature Mapping
- Normalize features into a shared vocabulary by category
- Each feature claim must cite a product/docs source

### Step E — Report Generation + QA
- Generate matrix and insights based on:
  - USP vs competitor differentiator claims
  - common features (parity baseline)
  - missing features (gaps)
  - traction signals (only if sourced; never infer)
- Produce sources appendix for auditability

---

## 8) Data Quality, Freshness & Conflicts

### 8.1 “No-source, no-number”
Any metric without a verifiable source is `Unknown`.

### 8.2 Freshness guidance (MVP)
- Social followers: ideally retrieved within **7 days** (include timestamp regardless)
- Traffic: use the **most recent month available** in Similarweb output

### 8.3 Conflict handling
When two reliable sources disagree:
- show both values
- label `CONFLICT`
- include both sources and retrieval timestamps

---

## 9) Acceptance Criteria (Definition of Done)

A run is considered successful if:

- Produces **5–10 competitors** with inclusion rationale
- Each competitor includes, at minimum:
  - website + description
  - **X followers + source**
  - **Similarweb monthly visits + source** (or `Unknown` + reason)
- Includes a **10–12 row comparison matrix**
- Includes **≥5 actionable insights** + explicit **Research TODOs**
- Includes a **Sources Appendix** that allows auditing each key claim

---

## 10) Failure Modes & Edge Cases

- **Not enough competitors found:** return 3–5 and explain constraints; suggest widening scope/keywords
- **No Similarweb data:** set `Unknown` and add TODO (consider Ahrefs/SEMrush as alternatives)
- **Very new project:** rely on category + adjacent competitors; mark uncertainty explicitly
- **Ambiguous brand/domain:** prioritize official site/docs; exclude lookalikes unless verified
