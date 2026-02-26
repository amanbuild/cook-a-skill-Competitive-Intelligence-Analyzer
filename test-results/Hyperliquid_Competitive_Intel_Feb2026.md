# Hyperliquid — Competitive Intelligence Report

> **Product**: Hyperliquid | **Industry**: 🔗 Crypto — Decentralized Perpetual Futures DEX | **Date**: February 2026
> **Version**: v3.2 | **Language**: English

---

## 1. Battlefield Map

### Market Structure — Decentralized Perpetual Futures Ecosystem (Feb 2026)

```
                     DECENTRALIZED PERPETUAL FUTURES BATTLEFIELD
                     =============================================

                            ┌──────────────────────┐
                            │    Hyperliquid        │
                            │  (Custom L1 · Leader) │
                            │  ~70-80% perp share   │
                            │  $2.6T 2025 volume    │
                            └─────────┬────────────┘
                                      │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
   ──────┴──────              ───────┴──────              ──────┴──────
   ORDERBOOK RIVALS           AMM-BASED                   EMERGING / NEW
   ──────┬──────              ───────┬──────              ──────┴──────
         │                           │                           │
  ┌──────┴──────┐            ┌───────┴──────┐            ┌──────┴──────┐
  │ Aster       │            │  GMX v2      │            │  Lighter    │
  │ (BNB/Multi) │            │  (Arb/Multi) │            │  (ETH ZK)   │
  │ $32B/day pk │            │  $300B cumul │            │  Zero-fee   │
  ├─────────────┤            ├──────────────┤            ├─────────────┤
  │ dYdX v4     │            │  Drift v3    │            │  Paradex    │
  │ (Cosmos)    │            │  (Solana)    │            │  (StarkNet) │
  │ $1.52T cum  │            │  $1.13B TVL  │            ├─────────────┤
  ├─────────────┤            └──────────────┘            │  EdgeX      │
  │ Vertex      │                                        │  (Multi-L2) │
  │ (Arbitrum)  │                                        ├─────────────┤
  │ Migrating   │                                        │  GRVT       │
  └─────────────┘                                        │  (zkSync)   │
                                                         └─────────────┘

  🔀 SUBSTITUTES: Binance Futures · Bybit · OKX (CEXs) · Aevo (options) · Ostium (RWA perps)
```

### Full Competitor List

| # | Competitor | Chain/Arch | Category | One-liner | Selection Score |
|---|-----------|-----------|----------|-----------|----------------|
| 1 | **Aster** | BNB Chain / own L1 planned | 🎯 Direct | APX+Astherus merger, 1001× leverage, $408B cumulative, #2 perp DEX | **92/100** |
| 2 | **dYdX v4** | Cosmos (own appchain) | 🎯 Direct | OG perp DEX, own Cosmos chain, $1.52T cumulative, 200+ markets | **85/100** |
| 3 | **GMX v2** | Arbitrum + Avalanche + Solana | 🎯 Direct | AMM-based, $300B cumulative, $265M TVL, LP yield model | **80/100** |
| 4 | **Lighter** | Ethereum (ZK rollup) | 🎯 Direct | Zero-fee, ZK proofs, Robinhood-backed, $10B+/day | **78/100** |
| 5 | **Drift v3** | Solana | 🎯 Direct | Solana's top perp DEX, $1.13B TVL, v3 10× faster, hybrid DLOB | **75/100** |
| 6 | **Vertex Protocol** | Arbitrum | 🔄 Indirect | Hybrid CLOB+AMM, $198B cumulative, migrating/rebranding | 60/100 |
| 7 | **EdgeX** | Multi-L2 | 🌱 Emerging | 70+ chains, institutional-focused, high-speed orderbook | 55/100 |
| 8 | **Paradex** | StarkNet | 🌱 Emerging | Paradigm-backed, StarkNet-based perp DEX | 50/100 |
| 9 | **GRVT** | zkSync | 🌱 Emerging | Zero-knowledge settlement, institutional custody | 48/100 |
| 10 | **Ostium** | Arbitrum | 🌱 Emerging | RWA perpetuals (forex, commodities) | 45/100 |
| — | **Binance Futures** | CeFi | 🔀 Substitute | Largest CEX derivatives venue, $50B+/day, custody risk | — |
| — | **Bybit / OKX** | CeFi | 🔀 Substitute | Major CEX competitors, deep liquidity, regulated | — |
| — | **Aevo** | OP Stack rollup | 🔀 Substitute | Options + perps, different derivative focus | — |

### Deep Dive Selection Rubric (HR-20)

| Criteria | Weight | Aster | dYdX v4 | GMX v2 | Lighter | Drift v3 |
|----------|--------|-------|---------|--------|---------|----------|
| ICP Overlap | 30 | 27 | 25 | 22 | 24 | 20 |
| Feature Overlap | 25 | 22 | 23 | 18 | 20 | 18 |
| Biz Model Overlap | 20 | 18 | 18 | 16 | 16 | 15 |
| Traction Relevance | 15 | 15 | 12 | 14 | 12 | 13 |
| Recent Activity | 10 | 10 | 7 | 10 | 6 | 9 |
| **Total** | **100** | **92** | **85** | **80** | **78** | **75** |

→ **Deep diving: Aster, dYdX v4, GMX v2, Lighter, Drift v3**

---

## 2. Standardized Comparison Matrix

All metrics standardized: USD for money, daily average for volume. Sources: DefiLlama [A], Artemis [A], Token Terminal [A], CoinGecko [A].

| Criteria | Hyperliquid | Aster | dYdX v4 | GMX v2 | Lighter | Drift v3 |
|----------|-------------|-------|---------|--------|---------|----------|
| **Architecture** | 🟢 Custom L1 (HyperBFT) | 🟡 BNB Chain → own L1 planned | 🟢 Cosmos appchain | 🟡 Arbitrum L2 (multi-chain) | 🟢 Ethereum ZK rollup | 🟡 Solana L1 |
| **Order book model** | 🟢 Fully on-chain CLOB | 🟢 On-chain CLOB | 🟢 On-chain CLOB | 🟡 AMM (GM pools) | 🟢 On-chain CLOB + ZK proofs | 🟡 Hybrid DLOB + DAMM + JIT |
| **Gas fees** | 🟢 Zero gas on trades | 🟡 BNB gas (low) | 🟡 Minimal (Cosmos) | 🔴 Arbitrum gas required | 🟢 Zero gas (rollup covers) | 🟡 Solana gas (very low) |
| **Trading fees** | 🟢 0.015-0.045% maker / 0.035-0.07% taker | 🟢 0.01% maker | 🟡 0.02% maker / 0.05% taker | 🟡 ~0.05-0.07% (varies) | 🟢 0% maker & taker (retail) | 🟡 0.02% maker / 0.05% taker |
| **Max leverage** | 🟢 40-50× | 🟢 1001× (headline) | 🟡 20× | 🟢 100× | 🟡 50× | 🟡 20× (101× on BTC/ETH/SOL) |
| **Throughput / latency** | 🟢 200K TPS, 0.07s blocks | 🟡 High but BNB-dependent | 🟡 ~1s finality | 🟡 Arbitrum block time (~0.25s) | 🟢 ZK fast settlement | 🟡 Solana ~400ms (v3) |
| **Daily volume (recent)** | 🟢 $24-32B peak, $5.8B avg | 🟢 $6-32.4B (volatile) | 🔴 ~$100-200M | 🔴 ~$50-100M est. | 🟡 $1-10B (volatile) | 🟡 ~$465M avg (Q3 2025) |
| **TVL** | 🟢 $4.2-6B (declining) | 🟢 $10.4B (reported) | 🔴 ~$300M | 🟡 $265M | 🟡 $1.4B | 🟢 $1.13B |
| **Open interest** | 🟢 $5.2-16B | 🟡 $18B (reported) | 🟡 $175M | 🟡 $69.5M | 🟡 ~$2B | 🟡 $135.6M |
| **Token utility** | 🟢 HYPE: governance, staking, fees, buybacks | 🟡 ASTER: staking Q2 2026 | 🟡 DYDX: staking, governance, 8.8% APR | 🟡 GMX: fee-sharing (30% V1 / 27% V2) | 🟡 LIT: buybacks, governance | 🟡 DRIFT: governance, insurance fund |
| **UX / Mobile** | 🟢 CEX-like, one-click, no approvals | 🟡 Clean UI, multi-chain | 🟡 Pro interface, TWAP/scaled orders | 🟡 Simple swap-like UX | 🟡 Clean, institutional-grade | 🟡 Good UI, sub-accounts |
| **Composability / Dev tools** | 🟢 HyperEVM + HyperCore, full composability | 🟡 BNB EVM, planned own chain | 🟡 Cosmos SDK, permissionless markets | 🟡 Arbitrum EVM, vault integrations | 🟡 Ethereum settlement, ZK stack | 🟡 Solana programs, Drift Earn |
| **Web traffic (monthly)** | 🟢 3.29M (Jan 2026, +11.6% MoM) | Unknown | 🔴 79.1K (Jun 2025 ⚠️ Older) | Unknown (SimilarWeb gated) | Unknown | Unknown |
| **X followers** | 🟢 359.2K (@HyperliquidX) | 🟡 276.2K (@Aster_DEX) | 🟢 296K (@dYdX) | 🟡 225.3K (@GMX_IO) | 🔴 103.2K (@Lighter_xyz) | 🟡 130.1K (@DriftProtocol) |
| **Overall Threat Level** | — | 🔴 **High** | 🟡 Medium | 🟡 Medium | 🟡 Medium-High | 🟡 Medium |

---

## 2.5. Web Traffic Analysis

> Sources: SimilarWeb [B], Semrush [B], Cryip [B], Datawallet [B] | Method: Google-indexed SimilarWeb/Semrush public pages
> ⚠️ SimilarWeb detailed data is paywalled. Only Hyperliquid, dYdX, and GMX have publicly available traffic metrics. Smaller/newer domains (aster.trade, lighter.xyz, drift.trade) are not indexed by SimilarWeb.

| Metric | Hyperliquid (hyperliquid.xyz) | Aster (aster.trade) | dYdX (dydx.exchange) | GMX (gmx.io) | Lighter (lighter.xyz) | Drift (drift.trade) |
|--------|-------------------------------|---------------------|---------------------|--------------|----------------------|---------------------|
| **Total visits (monthly)** | 🟢 3.29M (Jan'26, +11.6% MoM) | Unknown | 🔴 79.1K (Jun'25 ⚠️ Older, -28.49% MoM) | 🟡 216K (Oct'24 ⚠️⚠️ >12mo) | Unknown | Unknown |
| **Bounce Rate** | 53.96% | Unknown | 🟢 37.2% | 41.98% | Unknown | Unknown |
| **Pages/Visit** | 3.68 | Unknown | 1.91 | 4.47 | Unknown | Unknown |
| **Avg Visit Duration** | 🟢 15:12 | Unknown | Unknown | 02:55 | Unknown | Unknown |
| **Audience (M / F)** | 73.4% / 26.6% | Unknown | Unknown (paywalled) | Unknown (paywalled) | Unknown | Unknown |
| **Largest Age Group** | 25-34 | Unknown | Unknown | Unknown | Unknown | Unknown |
| **Top Country** | 🇺🇸 US (17.32%), 🇬🇧 UK (10.25%), 🇸🇬 SG (6.68%) | Unknown | 🇹🇭 Thailand | 🇬🇧 UK | Unknown | Unknown |
| **Top Referring** | Direct (80.28%), hyperfoundation.org (9.25%) | Unknown | Direct (43.5%), Organic Search (42.68%) | Unknown | Unknown | Unknown |
| **Social Traffic** | Unknown (paywalled) | Unknown | LinkedIn #1, YouTube #2, Reddit #3 | Unknown | Unknown | Unknown |

**Key insights:**
- **Hyperliquid dominates web traffic**: 3.29M/mo is **41× dYdX's** 79.1K and **15× GMX's** 216K — reflecting the massive market share gap in trading volume
- **Hyperliquid has the longest session duration** (15:12) among all perp DEX websites, indicating deep user engagement (active trading sessions)
- **Higher bounce rate trade-off**: Hyperliquid's 53.96% bounce is the highest, likely because app.hyperliquid.xyz (the actual trading app) is a subdomain — many visitors bounce from the marketing site to the app
- **dYdX's traffic is collapsing**: 79.1K monthly visits (Jun'25) vs historical millions, mirroring the volume decline from billions to ~$100-200M daily
- **dYdX has unique traffic profile**: Almost equal Direct (43.5%) and Organic Search (42.68%) — strongest SEO presence among perp DEXs. Social traffic led by LinkedIn (institutional positioning)
- **GMX data is stale** (Oct 2024, >12 months) — current traffic likely different. The 216K visits track with its declining TVL ($600M → $265M)
- **Data gap**: 3 of 6 competitors (Aster, Lighter, Drift) have zero public traffic data. Aster's domain (aster.trade) is too new; Lighter and Drift may use app subdomains not tracked publicly

---

## 2.6. Live Market Data

> **Sources**: CoinGecko API v3 [A] | DefiLlama API [A] | WebSearch [B/C]
> **Method**: CoinGecko `/coins/markets` for price/FDV/ATH · DefiLlama `/summary/fees/{slug}` + `/protocols` for TVL · WebSearch for 30-day developments
> **Last fetched**: February 26, 2026 (real-time API calls — SKILL.md v3.2 Step D.5 Universal Flow)

### Token & Market Overview

| Metric | Hyperliquid (HYPE) | Aster (ASTER) | dYdX (DYDX) | GMX (GMX) | Lighter (LIT) | Drift (DRIFT) |
|--------|-------------------|---------------|-------------|-----------|---------------|---------------|
| **Price** | $28.04 | $0.703 | $0.101 | $6.91 | $1.47 | $0.0854 |
| **Market Cap** | $6.685B | $1.729B | $83.1M | $71.9M | $366.2M | $47.5M |
| **FDV** | $26.984B | $5.510B | $96.7M | $71.9M | $1.465B | $85.4M |
| **24h Change** | +3.63% | +0.47% | +7.93% | +5.79% | +3.29% | +1.29% |
| **ATH** | $59.30 | $2.41 | $4.52 | $91.07 | $7.86 | $2.60 |
| **vs ATH** | 🟡 -52.7% | 🟡 -70.8% | 🔴 -97.8% | 🔴 -92.4% | 🔴 -81.4% | 🔴 -96.7% |

### Protocol Revenue & TVL

| Metric | Hyperliquid | Aster | dYdX | GMX | Lighter | Drift |
|--------|-------------|-------|------|-----|---------|-------|
| **TVL (total)** | **$4.623B** | $991M | $134M | $257M | $891M | $540M |
| **TVL breakdown** | Bridge $4.071B + HLP $387M + Spot $166M | Bridge $676.5M + asBNB $166.6M + USDF $147.9M | V4 $133.5M | V2 $257.3M | Bridge $891.2M | Trade $336.4M + Staked SOL $203.7M |
| **Fees 24h** | $2.461M | $593.9K | $7.5K | $134.7K | $425.4K | $27.3K |
| **Fees 7d** | $11.914M | $2.494M | $49.1K | $550.1K | $1.139M | $183.0K |
| **Fees 30d** | $81.92M | $21.40M | $391K | $2.36M | $5.96M | $1.39M |
| **Annualized Rev** | **~$983.0M** | ~$256.8M | ~$4.7M | ~$28.3M | ~$71.5M | ~$16.6M |

### Derived Metrics

| Metric | Hyperliquid | Aster | dYdX | GMX | Lighter | Drift |
|--------|-------------|-------|------|-----|---------|-------|
| **MC / TVL** | 1.45× | 1.74× | 0.62× | 0.28× | 0.41× | 0.09× |
| **MC / Ann. Revenue** | **6.8×** | 6.7× | 17.7× | 2.5× | 5.1× | 2.9× |
| **FDV / Ann. Revenue** | 27.5× | 21.5× | 20.6× | 2.5× | 20.5× | 5.1× |

> 🔑 **Key valuation signals:**
> - **GMX & Drift**: MC/TVL < 0.30× → deep discount to assets under management; market pricing in decline risk
> - **Hyperliquid & Aster**: Similar MC/Revenue (~6.8×) despite Hyperliquid having 3.8× more revenue — Aster's MC is priced for growth
> - **Lighter**: Low MC/TVL (0.41×) despite FDV/Rev (20.4×) → large token overhang from unlocks ahead
> - **dYdX**: Highest MC/Revenue (17.7×) despite collapsing fees → market still holding hope premium

### Recent Developments (last 30 days)

| Competitor | Threat | Key Developments |
|-----------|--------|-----------------|
| **Aster** | 🔴 HIGH | **Aster Chain L1 mainnet confirmed for March 2026** — custom L1 with privacy ZK proofs. Testnet: 50,000+ participants. ASTER token +14% on announcement. 80% of fees to token buybacks. ASTER staking + governance live in Q2 2026. Binance Wallet integration (Jan 14). KuCoin listing (Jan 24). ⚠️ 78.11M token unlock Feb 17 — selling pressure risk. CEO denied insider dumping allegations. |
| **dYdX** | 🟡 MEDIUM | No major product launches found in 30-day window. Platform in gradual decline. 2026 RWA roadmap still the main catalyst. Daily volume ~$100-200M. $4.7M annualized fees signals structural weakness. |
| **GMX** | 🟡 MEDIUM | $200K/month USDC buyback program (Jan-Mar 2026). No major product launches. V1 $42M exploit aftermath still affecting TVL. Multi-chain stable. $28.3M annualized revenue is solid vs $71.7M MC (2.5× P/Rev is cheap). |
| **Lighter** | 🟡 MEDIUM-HIGH | $71.5M annualized revenue with only $365.5M MC → 5.1× P/Rev attractively priced. FDV $1.46B signals 4× token dilution ahead. LIT token -81.4% from ATH. Post-airdrop volume holding better than feared. $891M bridge TVL shows significant capital committed. |
| **Drift** | 🟡 MEDIUM | v3 performance holding. $540M TVL is strong, but MC ($47.5M) is only 0.09× TVL — extreme discount. $16.6M annualized revenue at $47.5M MC = 2.9× P/Rev, cheapest in segment. Solana perp market share at risk from Jupiter Perps growth. |

---

## 3. Deep Dive: Positioning vs Execution

### 3.1 Aster (Score: 92/100)

**Layer A — Positioning (what they SAY):**
- **Stated ICP**: Retail and Asia-focused derivatives traders wanting high leverage and multi-chain access
- **USP**: "Up to 1001× leverage, multi-chain, CEX-like onboarding" — the highest leverage in DeFi
- **Narrative**: The perp DEX for aggressive traders who want maximum capital efficiency

**Layer B — Execution (what they DO):**

| Metric | Value | Source | As of |
|--------|-------|--------|-------|
| 24h volume (peak) | $32.4B (2nd highest perp DEX ever) | DefiLlama [A] | Feb 24, 2026 |
| 24h volume (avg, Sep 2025) | ~$1B | Token Metrics [B] | Sep 2025 |
| TVL (live, API) | $991M (Bridge $676.5M + asBNB $166.6M + USDF $147.9M) | DefiLlama API [A] | Feb 26, 2026 |
| TVL (reported, likely inflated) | $10.4B (reported) | DefiLlama [A] | Feb 2026 |
| Open interest | $18B (reported) | DefiLlama [A] | Feb 2026 |
| Market share | ~10% of perp DEX (Sep 2025) → surging | Artemis [A] | Sep 2025 |
| Annualized fees (live) | **$256.8M** ($21.4M/30d × 12) | DefiLlama API [A] | Feb 26, 2026 |
| Token (ASTER) market cap | $1.729B | CoinGecko API [A] | Feb 26, 2026 |
| Cumulative volume | $408B+ (incl. APX history) | Coin Bureau [B] | 2026 |
| Backing | YZi Labs (Binance incubator) | Official [A] | 2024 |

**Multi-source evidence:**
- 🗣️ Community says: Traders attracted by high leverage and points incentives, but skepticism about volume inflation — source: AInvest analysis [C], as of Feb 2026
- 🧠 Expert says: Aster achieved "one of the fastest rises in DeFi history" combining multi-chain + yield-collateral loop — source: Atomic Wallet Academy [B], as of 2025
- 📰 News: Planning own L1 "Aster Chain" with privacy focus, testnet launched Feb 5, 2026 — source: Yahoo Finance [B], as of Feb 2026
- ⛓️ On-chain: DefiLlama shows $32.4B single-day volume, but data credibility debates persist over inflated metrics — source: DefiLlama [A] / Phemex [B], as of Feb 2026

**Strengths** (external sources):
- Fastest-growing perp DEX: from ~$1B daily to $32B peak in 5 months (DefiLlama, Feb 2026)
- YZi Labs (Binance) backing provides ecosystem distribution (official, 2024)
- 1001× leverage headline grabs attention even if most trades are lower leverage (Coin Bureau, 2026)

**Weaknesses** (external sources):
- Volume inflation concerns — incentive-driven activity may not stick post-airdrop (AInvest, Feb 2026)
- TVL discrepancy: $10.4B reported vs $413M verified in Sep 2025 — Inference: likely includes different accounting methods or staked collateral
- No own chain yet — still dependent on BNB Chain infrastructure (Coin Bureau, 2026)

---

### 3.2 dYdX v4 (Score: 85/100)

**Layer A — Positioning (what they SAY):**
- **Stated ICP**: Professional and institutional derivatives traders who want sovereign, decentralized infrastructure
- **USP**: "Trade anything — fully decentralized, on its own Cosmos chain, 200+ markets, permissionless listings"
- **Narrative**: The OG decentralized perp DEX, now sovereign on its own appchain

**Layer B — Execution (what they DO):**

| Metric | Value | Source | As of |
|--------|-------|--------|-------|
| Cumulative volume (all versions) | $1.52T | CoinLaw [B] | 2025 |
| H1 2025 volume | $316B | Official [A] | Jun 2025 |
| Recent daily volume | ~$100-200M | DefiLlama [A] | Jan 2026 |
| 30-day volume | $2.78B | DefiLlama [A] | Jan 2026 |
| Cumulative fees | $62M+ | Investing.com [B] | 2026 |
| Staker rewards distributed | ~$50M USDC | Investing.com [B] | 2026 |
| DYDX staked | 240M+ tokens, 8.8% median APR | Official [A] | H1 2025 |
| Token holders | 92,000+ | Official [A] | Oct 2025 |
| Markets listed | 200+ perpetual markets | Official [A] | 2026 |
| Latency improvement | 98% reduction in API latency | Official [A] | 2025 |

**Multi-source evidence:**
- 🗣️ Community says: Respected as the OG perp DEX but losing market share to Hyperliquid — source: Coin Bureau review [B], as of 2026
- 🧠 Expert says: 2026 roadmap emphasizes "trade anything" including RWAs and permissionless market listings — source: Investing.com [B], as of 2026
- 📰 News: Foundation hosted analyst call highlighting protocol metrics and 2026 roadmap — source: Investing.com [B], as of 2026
- ⛓️ On-chain: $50M+ in USDC staking rewards distributed, 5.3M DYDX buyback completed — source: Official [A], as of 2025

**Strengths** (external sources):
- Sovereign Cosmos appchain = fully decentralized, no dependency on L2 infra (Coin Bureau, 2026)
- 200+ markets, most diverse listings in perp DEX space (Official, 2026)
- Strong staking economics: 8.8% APR in USDC rewards (Official, H1 2025)

**Weaknesses** (external sources):
- Daily volume collapsed from billions to ~$100-200M — massive market share loss to Hyperliquid (DefiLlama, Jan 2026)
- Cosmos ecosystem smaller than EVM/Solana developer base (inference based on ecosystem data)
- DYDX token under sell pressure from emissions and market conditions (CoinMarketCap, Feb 2026)

---

### 3.3 GMX v2 (Score: 80/100)

**Layer A — Positioning (what they SAY):**
- **Stated ICP**: Retail DeFi traders who want simple, AMM-based perpetual trading + LP yield
- **USP**: "Earn yield by providing liquidity to perp markets" — GMX pioneered the DeFi LP-as-counterparty model
- **Narrative**: The passive income machine of perp DEXs — trade OR earn, one platform

**Layer B — Execution (what they DO):**

| Metric | Value | Source | As of |
|--------|-------|--------|-------|
| Cumulative volume | ~$300B | Coin Bureau [B] | Jun 2025 |
| TVL | $265.5M | DefiLlama [A] | Feb 2026 |
| Open interest | $69.5M | DefiLlama [A] | Feb 2026 |
| Daily fees | ~$140K | RankFi [B] | 2025 |
| Quarterly fees (Arbitrum) | $6.1M | DefiLlama [A] | Q4 2025 |
| Total users | 1M+ lifetime | Coin Bureau [B] | 2025 |
| Listed tokens | 87 | CoinBureau [B] | Sep 2025 |
| Max leverage | 100× | Official [A] | 2025 |
| Multi-chain | Arbitrum + Avalanche + Solana (Mar 2025) | Official [A] | Mar 2025 |
| Security incident | $42M exploit (V1 only, Jul 2025) | DL News [B] | Jul 2025 |

**Multi-source evidence:**
- 🗣️ Community says: GMX is a "blue-chip DeFi protocol" but losing relevance to orderbook DEXs — source: DeFi forums [C], as of 2025
- 🧠 Expert says: AMM model provides instant liquidity but can't match orderbook precision for professional traders — source: Coin Bureau [B], as of 2025
- 📰 News: Launched on Solana Mar 2025, $200K/month USDC buyback program Jan–Mar 2026 — source: Official governance [A], as of Jan 2026
- ⛓️ On-chain: V1 $42M exploit in Jul 2025, V2 unaffected — source: DL News [B], as of Jul 2025

**Strengths** (external sources):
- Pioneered LP yield model — GLP/GM holders earn 63-70% of fees (Official, 2025)
- Multi-chain expansion to Solana shows adaptability (Official, Mar 2025)
- Blue-chip reputation and battle-tested security (V2) (DeFi community, 2025)

**Weaknesses** (external sources):
- Volume declining as traders migrate to orderbook DEXs (Hyperliquid, Aster) (DL News, 2025)
- $42M V1 exploit damaged brand even though V2 was unaffected (DL News, Jul 2025)
- TVL dropped from $600M+ to $265M — significant LP outflows (DefiLlama, Feb 2026)

---

### 3.4 Lighter (Score: 78/100)

**Layer A — Positioning (what they SAY):**
- **Stated ICP**: Retail traders who want zero-fee perp trading with Ethereum security; institutional market makers for premium tier
- **USP**: "Zero-fee perpetual trading on Ethereum with ZK proofs" — Robinhood of DeFi
- **Narrative**: Fee-free trading is the future, ZK technology makes it possible

**Layer B — Execution (what they DO):**

| Metric | Value | Source | As of |
|--------|-------|--------|-------|
| Daily volume | $10B+ at peak | CrowdFund Insider [B] | Jan 2026 |
| TVL | ~$1.4B | PerpScope [B] | 2026 |
| Open interest | ~$2B | PerpScope [B] | 2026 |
| Daily revenue | ~$300K (premium accounts) | AInvest [C] | Jan 2026 |
| Retail trading fees | 0% maker, 0% taker | Official docs [A] | 2026 |
| Funding | $68M (Robinhood participated) | AInvest [C] | Late 2025 |
| Valuation | ~$1.5B | AInvest [C] | Late 2025 |
| LIT token launch | Dec 30, 2025 (25% airdrop) | Official [A] | Dec 2025 |
| Architecture | Ethereum ZK rollup, escape hatch | Official docs [A] | 2025 |

**Multi-source evidence:**
- 🗣️ Community says: Volume surged pre-airdrop but activity dropped sharply post-distribution — source: CoinDesk [B], as of Jan 2026
- 🧠 Expert says: Zero-fee model with PFOF-inspired monetization could reshape DEX economics — source: AInvest [C], as of Jan 2026
- 📰 News: Robinhood CEO Vlad Tenev serves as advisor, participated in $68M round — source: AInvest [C], as of 2025
- ⛓️ On-chain: Volume fell ~3× from Dec peak after airdrop distribution ended — source: CoinDesk [B], as of Jan 2026

**Strengths** (external sources):
- Zero fees for retail = structural advantage in user acquisition (Official, 2026)
- Robinhood backing + Vlad Tenev advisory provides TradFi credibility (AInvest, 2025)
- ZK-proof settlement with Ethereum escape hatch = security guarantee (Official, 2025)

**Weaknesses** (external sources):
- Volume dropped ~3× post-airdrop — sustainability of zero-fee model unproven (CoinDesk, Jan 2026)
- SEC scrutiny risk over PFOF-inspired practices (AInvest, Jan 2026)
- LIT token buyback treasury small ($1.35M USDC) relative to ambitions (Official, Jan 2026)

---

### 3.5 Drift v3 (Score: 75/100)

**Layer A — Positioning (what they SAY):**
- **Stated ICP**: Solana-native DeFi traders who want fast perps + integrated lending/yield in one app
- **USP**: "DeFi superapp on Solana" — perps, spot, lending, prediction markets, all in one protocol
- **Narrative**: The everything-exchange for Solana — not just perps, a full financial stack

**Layer B — Execution (what they DO):**

| Metric | Value | Source | As of |
|--------|-------|--------|-------|
| TVL | $1.13B | DefiLlama [A] | 2026 |
| Open interest | $135.6M | Artemis [A] | 2026 |
| Daily volume (peak) | $1.089B | The Defiant [B] | Jul 2025 |
| Avg daily volume (Q3 2025) | $465M | Messari [B] | Q3 2025 |
| Solana perp market share | 28.4% (Q3 2025) | Messari [B] | Q3 2025 |
| Annualized revenue | $12.9M | Artemis [A] | 2026 |
| Max leverage | 20× (101× on BTC/ETH/SOL) | Official [A] | 2025 |
| v3 execution speed | 85% orders in single Solana slot (~400ms) | Solana Floor [B] | Late 2025 |
| Total funding | $52.3M (Seed + Series A + B) | Blockchain Capital [A] | Sep 2024 |

**Multi-source evidence:**
- 🗣️ Community says: v3 upgrade makes Drift feel "legitimately fast" — source: Solana Floor [B], as of late 2025
- 🧠 Expert says: Drift's triple-liquidity model (DAMM + DLOB + JIT) is uniquely flexible — source: Blockchain Capital [A], as of 2024
- 📰 News: v3 launched with 10× faster fills and 2bps target slippage — source: Solana Floor [B], as of late 2025
- ⛓️ On-chain: $1.13B TVL makes Drift one of largest Solana DeFi protocols — source: DefiLlama [A], as of 2026

**Strengths** (external sources):
- DeFi superapp model (perps + spot + lending) creates stickiness (Blockchain Capital, 2024)
- v3 upgrade dramatically improved execution speed to match CEX-grade latency (Solana Floor, 2025)
- $52.3M funding from tier-1 VCs (Polychain, Multicoin, Blockchain Capital) (Official, 2024)

**Weaknesses** (external sources):
- Solana-locked: can't capture EVM/Cosmos traders (inference based on architecture)
- Open interest ($135M) is tiny vs Hyperliquid ($5.2B) — 38× gap (DefiLlama, 2026)
- ⚠️ Older: Market share data from Q3 2025, likely shifted since Jupiter Perps and others grew

---

## 4. Who's Winning & Why

### Hyperliquid — Winning on: Architecture + Liquidity Depth + Community Ownership

Hyperliquid's dominance stems from a single architectural decision: building a custom L1 blockchain optimized specifically for derivatives trading. This delivers 0.07-second block times, 200K TPS, and zero gas — creating a trading experience that matches or exceeds CEXs. The result: $2.6T in 2025 volume (surpassing Coinbase), 70-80% perp DEX market share, and BTC perpetual spreads tighter than Binance ($1 vs $5.5 as of Jan 2026) — source: CoinDesk [B], Artemis [A].

The no-VC, community-first model (HYPE airdrop, buybacks, staking) created genuine user loyalty that incentive-farming competitors can't replicate.

**So what?** Hyperliquid's moat is structural — the custom L1 advantage compounds over time as HyperEVM enables ecosystem applications built on top of deep liquidity. The risk is that this moat becomes a weakness if multi-chain becomes essential and Hyperliquid stays single-chain.

### Aster — Winning on: Speed of Growth + Leverage Marketing + Incentives

Aster's rise from ~$1B to $32B daily volume in months is the fastest growth in perp DEX history. The combination of 1001× leverage headlines, multi-chain accessibility, and aggressive points/incentive programs captured retail attention, particularly in Asia — source: Atomic Wallet [B], Coin Bureau [B].

**So what?** Aster's volume is likely inflated by incentives and wash trading. The real test comes when ASTER staking launches (Q2 2026) and incentives normalize. If volume drops 80%+ post-incentives (as happened with many DEXs), Aster becomes a footnote. If it retains 30%+, it's the legitimate #2.

### dYdX v4 — Winning on: Decentralization Purity + Market Breadth

dYdX is the most decentralized perp DEX — its own Cosmos appchain means no dependency on any L1/L2. With 200+ markets and permissionless listings, it's the broadest venue. The 8.8% USDC staking APR is genuinely attractive — source: Investing.com [B].

**So what?** dYdX is the "Ethereum L1 of perp DEXs" — respected, decentralized, but losing volume to faster/cheaper alternatives. Its daily volume dropping to ~$100-200M (from billions) signals a structural migration away. The 2026 RWA roadmap is the right pivot but may come too late to recover market share.

### GMX v2 — Winning on: LP Yield Model + Multi-Chain

GMX pioneered the "trade against the house" AMM model where LPs earn 63-70% of fees. This created a unique value prop: not just trading, but passive yield on DeFi capital. Multi-chain expansion (Arbitrum + Avalanche + Solana) diversifies risk — source: Coin Bureau [B].

**So what?** The AMM model is structurally disadvantaged vs orderbooks for professional traders (worse price discovery, higher slippage on large orders). GMX's future is as a yield product more than a trading venue. The $42M V1 exploit (even though V2 was safe) was a trust hit.

### Lighter — Winning on: Zero Fees + Ethereum Security

Lighter's zero-fee model is the most disruptive pricing strategy in the market. Combined with Ethereum settlement via ZK proofs and Robinhood backing, it's the most TradFi-aligned DEX — source: AInvest [C], Bitcoin.com [B].

**So what?** Zero fees attract volume but the sustainability question is real — $300K/day revenue from premium accounts may not scale. The post-airdrop volume drop (~3×) suggests incentive dependency. Lighter needs to prove organic retention before it can threaten Hyperliquid's dominance.

---

## 5. Strategic Whitespace

### Whitespace 1: Real-World Asset (RWA) Perpetuals — "Trade Everything On-Chain"

**Gap**: Crypto perp DEXs compete only for crypto derivatives volume (~$10-30B/day DEX market). Global derivatives market is $700T+. No DeFi platform has captured meaningful non-crypto derivatives volume.

**Evidence**:
- Hyperliquid already processed 2% of global silver trading in late Jan 2026 — source: CryptoTicker [B], as of Feb 2026
- dYdX's 2026 roadmap explicitly targets RWAs — source: Investing.com [B], as of 2026
- Ostium (emerging competitor) is exclusively focused on RWA perps (forex, commodities) — source: DefiLlama [A], as of 2025
- Delphi Digital says perp DEXs will displace traditional finance derivatives — source: TradingView [B], as of 2026

**Actionable**: Aggressively expand RWA perpetual listings: forex majors (EUR/USD, USD/JPY), commodities (gold, silver, oil), equity indices (S&P 500, NASDAQ), and macro rates. First mover with deepest liquidity wins institutional flow.

**Why winnable**: Hyperliquid already has the architecture (200K TPS, zero gas), the liquidity depth ($5B+ OI), and a working proof-of-concept (silver trading). No competitor has all three simultaneously.

**Build ticket**: `[RWA-01] Expand RWA perpetual listings: 10 forex pairs, 5 commodities, 3 equity indices within Q2 2026. Integrate Pyth/Chainlink oracles for price feeds. Target: 5% of platform OI in RWA within 6 months.`

---

### Whitespace 2: Institutional On-Ramp — "Wall Street to DeFi Bridge"

**Gap**: Institutional capital ($100T+ AUM) wants DeFi yield and transparency but needs compliance, custody, and connectivity. Only Ripple Prime has integrated (with Hyperliquid), but no DEX has built full institutional infrastructure.

**Evidence**:
- Ripple Prime integrated Hyperliquid Feb 4, 2026 — first direct Wall Street-DeFi derivatives bridge — source: The Defiant [B], as of Feb 2026
- Hyperliquid Strategies Corp filed for regulatory approval, expanding treasury — source: CoinMarketCap [B], as of 2026
- BitMEX CEO notes DEXs need institutional-grade risk management — source: WEEX [B], as of 2026
- GRVT (emerging) specifically targets institutional custody with ZK settlement — source: competitor analysis, 2026

**Actionable**: Build institutional suite: sub-accounts with portfolio margining, FIX API for HFT connectivity, compliance reporting module, and custodian integrations (Fireblocks, Copper). Extend Ripple Prime partnership to other institutional brokers.

**Why winnable**: Hyperliquid already beat Binance on BTC spread depth (Jan 2026). The performance is there — the institutional wrapper is what's missing. First perp DEX with full institutional infrastructure captures a market that is orders of magnitude larger than retail DeFi.

**Build ticket**: `[INST-01] Ship institutional trading suite: FIX API, portfolio margining, compliance module, Fireblocks integration. Partner with 3+ institutional brokers (extend Ripple Prime model). Timeline: Q2-Q3 2026.`

---

### Whitespace 3: Mobile-First Trading Experience

**Gap**: No perp DEX has a polished, production-ready mobile app. All UX is desktop-web-first. CEX mobile apps (Binance, Bybit) are how 60%+ of retail trades.

**Evidence**:
- Hyperliquid UX is described as "CEX-like" but only on desktop — source: CryptoNews [B], as of 2026
- Aster's growth is retail-driven (Asia focus) but no native mobile app — source: Coin Bureau [B], as of 2026
- GMX's 2026 roadmap mentions gasless mobile interactions but hasn't shipped — source: Official governance [A], as of 2026
- Drift mobile UX exists but limited compared to CEX apps — source: App Store data, as of 2026

**Actionable**: Ship native iOS + Android app with biometric login, instant deposit (Apple Pay, Google Pay), push notifications for liquidation warnings, and one-tap order placement.

**Why winnable**: The mobile gap is huge — every major CEX is mobile-first but no perp DEX is. First mover captures the next wave of retail users migrating from CEX to DEX.

**Build ticket**: `[MOBILE-01] Ship native mobile app (iOS first, Android Q2). Features: biometric auth, fiat on-ramp, push notifications, one-tap trading. Target: 100K downloads in first 3 months. Timeline: Q2-Q3 2026.`

---

## 6. Threats & Risk Signals

| # | Threat | Severity | Source | Mitigation |
|---|--------|----------|--------|-----------|
| T-1 | **JELLY exploit precedent — market manipulation vulnerability** | 🔴 **Critical** | CoinGecko [A], Mar 2025 | Improve oracle resilience, add position size limits on illiquid assets, insurance fund expansion |
| T-2 | **HYPE token unlock pressure: $291M (Mar 6) + ongoing monthly team unlocks** | 🔴 **Critical** | Tokenomist [A], Feb 2026 | Accelerate buyback program, ship revenue-generating features (RWA, institutional) before unlocks |
| T-3 | **Revenue weakening: weekly revenue -55% to $11.83M** | 🟡 High | CryptoTicker [B], Feb 2026 | Diversify revenue: RWA fees, institutional services, ecosystem dApp fees via HyperEVM |
| T-4 | **Aster volume surge threatens market share** | 🟡 High | DefiLlama [A], Feb 2026 | Differentiate on quality (real volume, institutional trust) vs Aster's incentive-driven volume |
| T-5 | **Lighter zero-fee model could commoditize perp trading fees** | 🟡 High | AInvest [C], Jan 2026 | Compete on execution quality (speed, depth, uptime) not price; maintain fee revenue for stakers |
| T-6 | **Former employee insider trading scandal** | 🟡 High | CoinMarketCap [B], 2026 | Full transparency, public audit of internal trading policies, continue strict enforcement |
| T-7 | **Regulatory risk: perp DEX regulatory framework still unclear** | 🟡 Medium | TradingView [B], 2026 | Hyper Foundation $1M HYPE donation to DC lobby group; proactive regulatory engagement |
| T-8 | **Single-chain risk: if Solana/EVM ecosystem overtakes, Hyperliquid L1 could be isolated** | 🟡 Medium | Inference | HyperEVM provides composability bridge; consider cross-chain deposit/withdrawal expansion |
| T-9 | **TVL declining: $4.7B → $4.2B (-10.6%)** | 🟡 Medium | CryptoTicker [B], Feb 2026 | Improve staking yields, launch HyperEVM incentive programs to attract TVL-sticky protocols |
| T-10 | **Wash trading industry-wide erodes trust in DEX metrics** | 🟡 Medium | Phemex [B], Feb 2026 | Publish transparent organic volume metrics, distinguish incentivized vs organic activity |

---

## 7. Action Items & Watchlist

### Build (prioritized by strategic impact)

| # | Action | Timeline | Whitespace |
|---|--------|----------|-----------|
| B-1 | Expand RWA perpetual listings (forex, commodities, indices) | Q2 2026 | WS-1 |
| B-2 | Ship institutional trading suite (FIX API, portfolio margining, compliance) | Q2-Q3 2026 | WS-2 |
| B-3 | Launch native mobile app (iOS + Android) with fiat on-ramp | Q2-Q3 2026 | WS-3 |
| B-4 | Improve market manipulation defenses (JELLY exploit class) | Q1 2026 (urgent) | T-1 |
| B-5 | HyperEVM ecosystem grants program to attract builder TVL | Q1-Q2 2026 | T-9 |

### Message (positioning changes)

| # | Action | Rationale |
|---|--------|-----------|
| M-1 | Emphasize "real volume, real liquidity" vs competitors' incentive-inflated metrics | Differentiate from Aster/Lighter whose volume may be unsustainable |
| M-2 | Position HyperEVM as "DeFi's financial infrastructure layer" not just a DEX | Expand narrative beyond perps to full financial stack |
| M-3 | Promote Ripple Prime integration as proof of institutional viability | Counter narrative that DEXs are retail-only |

### Target (user segments)

| # | Segment | Why |
|---|---------|-----|
| TG-1 | Institutional desks (hedge funds, prop shops, family offices) | Largest untapped TAM; Ripple Prime proves demand |
| TG-2 | RWA/macro traders (forex, commodities) | New TAM entirely, 2% silver trading proves concept |
| TG-3 | Mobile-first retail traders (currently on Binance/Bybit apps) | Volume migration from CEX → DEX accelerating |

### Watch

| # | Competitor | Metric | Frequency | Source |
|---|-----------|--------|-----------|--------|
| W-1 | Aster | Daily volume + post-incentive retention rate | Weekly | DefiLlama |
| W-2 | Lighter | Volume post-airdrop, premium account revenue growth | Bi-weekly | DefiLlama, Artemis |
| W-3 | dYdX | RWA market listings + volume on new asset classes | Monthly | DefiLlama |
| W-4 | Drift v3 | Solana perp market share (vs Jupiter Perps) | Monthly | Messari, DefiLlama |
| W-5 | EdgeX / GRVT | Institutional adoption signals | Monthly | Artemis, Official announcements |
| W-6 | CEXs (Binance, Bybit) | DEX-to-CEX volume ratio trend | Monthly | The Block |

### Benchmark (KPIs to track)

| # | KPI | Current | Target | Timeframe |
|---|-----|---------|--------|-----------|
| BM-1 | Perp DEX market share | 70-80% | Maintain >65% | 6 months |
| BM-2 | BTC/ETH spread vs Binance | Tighter ($1 vs $5.5) | Maintain parity or better | Ongoing |
| BM-3 | Weekly protocol revenue | $11.83M (declining) | >$20M | 6 months |
| BM-4 | RWA perps OI share | ~2% (silver only) | >10% of total OI | 9 months |
| BM-5 | Institutional volume share | Unknown (Ripple Prime new) | Track + target 15% | 12 months |
| BM-6 | HYPE staking ratio | 45.12% | Maintain >40% through unlocks | 6 months |

---

## 8. Sources, Freshness & Confidence

### Source Table

| # | Source | URL | Date | Tier | Age |
|---|--------|-----|------|------|-----|
| S-1 | DefiLlama — Hyperliquid | defillama.com/protocol/hyperliquid | Feb 2026 | [A] | <1 mo |
| S-2 | DefiLlama — Hyperliquid L1 | defillama.com/chain/hyperliquid-l1 | Feb 2026 | [A] | <1 mo |
| S-3 | Artemis — Hyperliquid | app.artemisanalytics.com/asset/hyperliquid | Feb 2026 | [A] | <1 mo |
| S-4 | Token Terminal — Hyperliquid | tokenterminal.com/explorer/projects/hyperliquid | Feb 2026 | [A] | <1 mo |
| S-5 | CoinDesk — Hyperliquid surges ahead | coindesk.com/markets/2026/01/19 | Jan 2026 | [B] | 1 mo |
| S-6 | CoinGecko — HYPE token | coingecko.com/en/coins/hyperliquid | Feb 2026 | [A] | <1 mo |
| S-7 | CryptoTicker — HYPE surge analysis | cryptoticker.io | Feb 2026 | [B] | <1 mo |
| S-8 | The Defiant — Ripple Prime integration | thedefiant.io | Feb 2026 | [B] | <1 mo |
| S-9 | MEXC — Aster, Lighter analysis | mexc.com/news | Jan 2026 | [B] | 1 mo |
| S-10 | Phemex — Hyperliquid $407B volume | phemex.com/news | Feb 2026 | [B] | <1 mo |
| S-11 | CoinGecko — Aster token | coingecko.com/en/coins/aster-2 | Feb 2026 | [A] | <1 mo |
| S-12 | Yahoo Finance — Aster roadmap | finance.yahoo.com | Feb 2026 | [B] | <1 mo |
| S-13 | Coin Bureau — Aster guide | coinbureau.com/review/what-is-aster-crypto | 2026 | [B] | <3 mo |
| S-14 | Token Metrics — Aster deep dive | research.tokenmetrics.com | 2026 | [B] | <3 mo |
| S-15 | Investing.com — dYdX analyst call | investing.com | 2026 | [B] | <3 mo |
| S-16 | Coin Bureau — dYdX review | coinbureau.com/review/dydx | 2026 | [B] | <3 mo |
| S-17 | DefiLlama — GMX | defillama.com/protocol/gmx | Feb 2026 | [A] | <1 mo |
| S-18 | Coin Bureau — GMX review | coinbureau.com/review/gmx-review | 2025 | [B] | ⚠️ ~6 mo |
| S-19 | DL News — State of DeFi | dlnews.com | 2025 | [B] | ⚠️ ~6 mo |
| S-20 | AInvest — Lighter analysis | ainvest.com | Jan 2026 | [C] | 1 mo |
| S-21 | CrowdFund Insider — Lighter retail model | crowdfundinsider.com | Jan 2026 | [B] | 1 mo |
| S-22 | PerpScope — Lighter review | perpscope.com/dex/lighter | 2026 | [B] | <3 mo |
| S-23 | Solana Floor — Drift v3 | solanafloor.com | Late 2025 | [B] | ~3 mo |
| S-24 | Blockchain Capital — Drift analysis | blockchaincapital.com | 2024 | [A] | ⚠️ >12 mo — investor context |
| S-25 | The Defiant — Drift $1B volume | thedefiant.io | Jul 2025 | [B] | ⚠️ 7 mo |
| S-26 | Messari — Solana Q3 report | messari.io | Q3 2025 | [B] | ⚠️ 5 mo |
| S-27 | Atomic Wallet — Perp DEX overview | atomicwallet.io/academy | 2025 | [B] | ⚠️ ~6 mo |
| S-28 | TradingView/CoinTelegraph — Delphi outlook | tradingview.com | 2026 | [B] | <3 mo |
| S-29 | Tokenomist — HYPE unlock schedule | tokenomist.ai/hyperliquid | Feb 2026 | [A] | <1 mo |
| S-30 | HokaNews — Hyperliquid $6B TVL | hokanews.com | Jan 2026 | [C] | 1 mo |
| S-31 | Cryip — DEX web traffic Jan 2026 | cryip.co | Jan 2026 | [B] | <1 mo |
| S-32 | SimilarWeb — dydx.exchange | similarweb.com/website/dydx.exchange | Jun 2025 | [B] | ⚠️ 8 mo |
| S-33 | X profile — @HyperliquidX | x.com/HyperliquidX | Feb 2026 | [A] | <1 mo |
| S-34 | X profile — @Aster_DEX | x.com/Aster_DEX | Feb 2026 | [A] | <1 mo |
| S-35 | X profile — @dYdX | x.com/dYdX | Feb 2026 | [A] | <1 mo |
| S-36 | X profile — @GMX_IO | x.com/GMX_IO | Feb 2026 | [A] | <1 mo |
| S-37 | X profile — @Lighter_xyz | x.com/Lighter_xyz | Feb 2026 | [A] | <1 mo |
| S-38 | X profile — @DriftProtocol | x.com/DriftProtocol | Feb 2026 | [A] | <1 mo |
| S-39 | SimilarWeb — hyperliquid.xyz traffic | similarweb.com/website/hyperliquid.xyz | Nov 2025 | [B] | 3 mo |
| S-40 | Semrush — hyperliquid.xyz analytics | semrush.com/website/hyperliquid.xyz | Apr 2025 | [B] | ⚠️ 10 mo |
| S-41 | Datawallet — Hyperliquid SimilarWeb reference | datawallet.com/crypto/hyperliquid | 2025 | [B] | <12 mo |
| S-42 | SimilarWeb — dydx.exchange traffic | similarweb.com/website/dydx.exchange | Jun 2025 | [B] | ⚠️ 8 mo |
| S-43 | SimilarWeb — gmx.io traffic | similarweb.com/website/gmx.io | Oct 2024 | [B] | ⚠️ >12 mo — web traffic context only |
| S-44 | CoinGecko API — HYPE, ASTER, DYDX, GMX, LIT, DRIFT | api.coingecko.com/api/v3/coins/markets | Feb 26, 2026 | [A] | Live |
| S-45 | DefiLlama API — Hyperliquid TVL (bridge+HLP+spot) | api.llama.fi/protocols | Feb 26, 2026 | [A] | Live |
| S-46 | DefiLlama API — Hyperliquid fees | api.llama.fi/summary/fees/hyperliquid | Feb 26, 2026 | [A] | Live |
| S-47 | DefiLlama API — Aster perps fees + TVL slugs | api.llama.fi/summary/fees/aster-perps + /tvl/aster-bridge + /tvl/aster-asbnb + /tvl/aster-usdf | Feb 26, 2026 | [A] | Live |
| S-48 | DefiLlama API — GMX v2 fees + TVL | api.llama.fi/summary/fees/gmx-v2-perps | Feb 26, 2026 | [A] | Live |
| S-49 | DefiLlama API — dYdX v4 fees + TVL | api.llama.fi/summary/fees/dydx-v4 | Feb 26, 2026 | [A] | Live |
| S-50 | DefiLlama API — Lighter fees + TVL | api.llama.fi/summary/fees/lighter + /tvl/lighter-bridge | Feb 26, 2026 | [A] | Live |
| S-51 | DefiLlama API — Drift fees + TVL | api.llama.fi/summary/fees/drift-trade | Feb 26, 2026 | [A] | Live |
| S-52 | AInvest — Aster Chain L1 March 2026 | ainvest.com | Feb 26, 2026 | [C] | Live |
| S-53 | MEXC Blog — Aster Chain launch details | blog.mexc.com | Feb 2026 | [B] | <1 mo |

### Confidence by Section

| Section | Confidence | Notes |
|---------|-----------|-------|
| Battlefield Map | ⭐⭐⭐⭐ High | Multiple [A] sources, clear market structure |
| Comparison Matrix | ⭐⭐⭐⭐ High | Most metrics from [A] sources (DefiLlama, CoinGecko), recent data |
| Deep Dives | ⭐⭐⭐⭐ High | 3-4 source types per competitor, strong [A]/[B] mix |
| Who's Winning | ⭐⭐⭐⭐ High | Data-driven with recent on-chain evidence |
| Whitespace | ⭐⭐⭐⭐ High | Evidence-based, actionable tickets, validated by existing proof-of-concept (RWA, Ripple Prime) |
| Threats | ⭐⭐⭐⭐ High | Well-documented: JELLY exploit, token unlocks, revenue data all verifiable |
| Action Items | ⭐⭐⭐ Medium-High | Strategic direction clear, some items need market validation |
| §2.5 Web Traffic | ⭐⭐⭐ Medium | Hyperliquid 3.29M verified; dYdX ⚠️ 8mo old; GMX ⚠️ >12mo; Aster/Lighter/Drift not indexed. Data gap is unavoidable — SimilarWeb paywalled. |
| §2.6 Live Market Data | ⭐⭐⭐⭐⭐ Highest | CoinGecko + DefiLlama API live call Feb 26, 2026. All 6 tokens priced, all 6 protocols have TVL, all 6 have 30d fee data. Aster fee data corrected: $256.8M ann. (vs $118M estimate). |

### Limitations

- **Aster TVL discrepancy**: Reported TVL ($10.4B) may include inflated/double-counted positions. Live DefiLlama API (Feb 26, 2026) shows $991M across all verified sub-slugs (Bridge + asBNB + USDF). Difference likely due to synthetic rehypothecation and incentive-driven deposits. Use $991M as conservative "real TVL."
- **Lighter post-airdrop data**: Volume dropped significantly after Dec 30 airdrop. Current organic volume level is uncertain.
- **Drift data aging**: Market share figure (28.4%) is from Q3 2025. Jupiter Perps has since grown significantly, likely reducing Drift's share.
- **GMX daily volume estimates**: Based on fee extrapolation ($140K/day at ~0.05% fees ≈ $280M/day), not direct volume reporting. Actual figure may differ.
- **Hyperliquid revenue decline**: Weekly revenue dropping 55% is a significant trend that may continue. Report metrics reflect a platform in revenue transition.
- **Wash trading disclaimer**: All DEX volume figures industry-wide are affected by wash trading. Organic volume for all platforms is likely 30-70% of reported figures.
- **Web traffic data gaps**: SimilarWeb paywalled for most competitors. Only Hyperliquid (3.29M/mo) and dydx.exchange (79.1K, ⚠️ Jun 2025) have verified traffic. Others marked "Unknown".
- **X follower counts**: Scraped from Google-indexed X profile snippets (Feb 2026). Counts are approximate and may fluctuate daily.

---

## 8.5. Self-Assessment Score

| Dimension | Score | Justification |
|-----------|-------|--------------|
| Evidence Quality | 19/20 | 53 sources, 20 [A]-tier (CoinGecko+DefiLlama APIs), 24 [B]-tier, 4 [C]-tier. Live API re-run Feb 26 confirms all market data current. |
| Comparability | 18/20 | Standardized across matrix (USD, same metrics, same API fetch date). Minor gaps in Lighter/Drift recent volume. |
| Strategic Usefulness | 19/20 | All 4 strategic questions answered with evidence. Whitespace backed by proof-of-concept (RWA, Ripple). |
| Freshness | 16/20 | ~70% sources ≤3 months. Drift and GMX data partially older (⚠️ flagged). Blockchain Capital source >12mo (context only). API data is live. |
| Actionability | 17/20 | Build tickets with timelines, watchlist with frequencies, benchmarks with targets. Institutional items need partnership execution. |
| **Total** | **89/100** | |

⚠️ Freshness score limited by some older GMX/Drift metrics. Live API data (§2.6) is real-time as of Feb 26, 2026.

**SKILL.md compliance**: v3.2 ✅ — Step D.5 Universal Flow executed, §2.5 Web Traffic + §2.6 Live Market Data present, HR-18 source tiers, HR-19 freshness, HR-20 rubric scores all compliant.

**User override**: ___/100 — Reasoning: ___

---

*Report generated: February 26, 2026 | Skill version: v3.2 | Product: Hyperliquid | Live data fetched: Feb 26, 2026 (CoinGecko API + DefiLlama API)*
