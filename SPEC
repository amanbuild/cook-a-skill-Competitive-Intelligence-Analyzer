# Competitive Intelligence Report — Spec

---

## 0. Core Philosophies

Mọi quyết định thiết kế trong skill này phải tuân theo 8 triết lý sau. Khi có conflict giữa "thêm data" và "trả lời câu hỏi chiến lược" → luôn chọn câu hỏi chiến lược.

| # | Philosophy | Một câu |
|---|-----------|---------|
| P1 | **Decision-first** | Report là công cụ ra quyết định, không phải bảng tổng hợp |
| P2 | **Comparable > nhiều data** | Ít data nhưng so sánh được > nhiều data rời rạc |
| P3 | **Evidence-first, no fabrication** | Không có nguồn → Unknown. Số mâu thuẫn → ghi range + note conflict |
| P4 | **Freshness matters** | **Metrics/traction**: ưu tiên sources ≤3 tháng. Không có → fallback ≤12 tháng + flag "⚠️ Older". **Context/background**: cho phép ≤12 tháng, flag nếu >3 tháng. >12 tháng → drop hoàn toàn. Ghi "as of [date]" cho mọi metric |
| P5 | **Positioning ≠ Execution** | Tách rõ "họ NÓI gì" vs "họ LÀM được gì" |
| P6 | **Map the battlefield** | Vẽ cấu trúc thị trường, không chỉ list competitors |
| P7 | **Find strategic whitespace** | Phải chỉ ra khoảng trống mình có thể đánh |
| P8 | **Actionable > academic** | Mọi insight phải trả lời "so what?" |

---

## 1. Problem Statement

**Từ công việc hàng ngày:**

Mỗi lần team Product/Strategy cần nắm tình hình đối thủ:
- Phải manually Google từng đối thủ, mở hàng chục tab, data rời rạc không nằm chung một chỗ
- Mỗi đối thủ thu thập một kiểu data → đọc xong không so sánh được (vi phạm P2)
- Report cuối cùng thường là data dump — nhiều thông tin nhưng không trả lời "nên làm gì" (vi phạm P1, P8)
- Dễ nhầm branding mạnh với execution mạnh — chỉ đọc homepage copy (vi phạm P5)
- Không vẽ được cấu trúc cạnh tranh, chỉ list từng đối thủ riêng lẻ (vi phạm P6)
- Không chỉ ra khoảng trống nào mình có thể đánh (vi phạm P7)
- Feedback từ community, experts, news nằm rải rác — không ai tổng hợp vào một chỗ

**Scenario:**
> Analyst nhận yêu cầu: "Board meeting tuần sau, cần competitive landscape cho pump.fun." Analyst mất 2 ngày. Output: bảng so sánh đẹp nhưng mỗi đối thủ data khác nhau, không ai trả lời được "pump.fun nên đánh đâu tiếp." Head of Product hỏi: "So what?" — không ai trả lời được.

---

## 2. Objective

| Field | Value |
|-------|-------|
| **Giải quyết cái gì** | Biến competitive research từ data dump thành công cụ ra quyết định chiến lược |
| **Cho ai** | Ops & Data Analyst, Product Team, Strategy Team |
| **Output** | Report trả lời 4 câu hỏi chiến lược: Cạnh tranh với ai? Họ thắng nhờ gì? Khoảng trống ở đâu? Mình nên làm gì? |
| **Thay thế gì** | 1–2 ngày manual research → ~30 phút AI research + user review |

---

## 3. Input Contract

### 3.1 Accepted Input Methods
- File upload (Markdown, .txt, hoặc bất kỳ text file)
- Chat message trực tiếp
- Kết hợp cả hai

### 3.2 Required Fields

| Field | Validation | Nếu thiếu |
|-------|-----------|-----------|
| **Product Name** | Non-empty, ≤100 ký tự | Hỏi user |
| **Description** | 2–5 câu mô tả sản phẩm | Hỏi user |
| **Key Features** | ≥3 items | Hỏi user nếu < 3 |
| **Narrative / Positioning** | Phải chứa target audience + value prop | Hỏi user nếu thiếu |

### 3.3 Optional Fields

| Field | Default nếu không có |
|-------|---------------------|
| **Comparison Criteria** | AI chọn 8–10 tiêu chí theo ngành |
| **Known Competitors** | AI tìm từ scratch |

### 3.4 Input Validation Rules
- Thiếu required field → **STOP, hỏi, không đoán** (P3)
- File rỗng hoặc non-text → thông báo lỗi, hỏi lại

---

## 4. Output Contract

### 4.1 Files

| File | Format | Naming |
|------|--------|--------|
| Report chính | Markdown (.md) | `[ProductName]_Competitive_Intel_[MonthYear].md` |
| Report formal | Word (.docx) | `[ProductName]_Competitive_Intel_[MonthYear].docx` |

### 4.2 Report Structure — 8 Sections

Sections được thiết kế để trả lời strategic questions, không phải collect data categories.

| # | Section | Strategic Question | Priority | Philosophy |
|---|---------|-------------------|----------|-----------|
| 1 | **Battlefield Map** | Mình đang cạnh tranh với AI, cấu trúc thị trường ra sao? | 🔴 Must | P6 |
| 2 | **Standardized Comparison Matrix** | So sánh apple-to-apple trên cùng tiêu chí? | 🔴 Must | P2 |
| 3 | **Deep Dive: Positioning vs Execution** | Họ nói gì vs họ làm được gì? | 🔴 Must | P5, P3, P4 |
| 4 | **Who's Winning & Why** | Ai đang thắng, nhờ distribution/product/pricing/trust/speed? | 🔴 Must | P1 |
| 5 | **Strategic Whitespace** | Khoảng trống nào mình có thể đánh? | 🔴 Must | P7 |
| 6 | **Threats & Risk Signals** | Cần lo gì? Ai có thể bất ngờ? | 🟡 Should | P4 |
| 7 | **Action Items & Watchlist** | Cụ thể nên làm gì? Theo dõi ai? | 🔴 Must | P8 |
| 8 | **Sources, Freshness & Confidence** | Data từ đâu, mới cỡ nào, tin được không? | 🔴 Must | P3, P4 |

### 4.3 Language Rule
Output language = input language. (P3 — respect context)

---

## 5. Workflow (A → B → C → D → E → F)

### Step A: Parse & Validate Input
- **Input**: File hoặc chat từ user
- **Process**: Extract fields, validate (Section 3.4)
- **Output**: Structured product brief hoặc câu hỏi nếu thiếu
- **⚠️ Pitfall**: File format lạ → thông báo, hỏi lại

### Step B: Confirm Understanding
- **Input**: Product brief từ Step A
- **Process**: Tóm tắt cho user confirm: tên, category, differentiators, criteria, known competitors
- **Output**: Confirmation. User sửa → quay Step A. User OK → Step C
- **⚠️ Pitfall**: AI suy sai category → luôn ghi rõ inferred category

### Step C: Competitor Discovery & Battlefield Mapping (6–12 searches)
- **Input**: Confirmed brief
- **Process**: Search theo 8 patterns. Classify kết quả thành battlefield map:
  - 🎯 Direct competitors
  - 🔄 Indirect / adjacent
  - 🌱 Emerging / new entrants
  - 🔀 Substitute behaviors/tools (P6 — không chỉ list companies, map cả alternatives)
  - Nếu crypto: tag decentralized vs centralized, retail vs pro focus
- **Output**: Battlefield map + full competitor list
- **⚠️ Pitfall**: 20+ results → list ALL, deep dive top 5 direct
- **⚠️ Pitfall**: Known competitor không thấy → thêm manually, ghi chú

### Step D: Deep Dive Research (top 5 direct — 3–5 searches PER competitor)
- **Input**: Competitor list từ Step C
- **Process**: Cho mỗi competitor, search 4 nguồn:

  | Nguồn | Search pattern | Thu thập |
  |-------|---------------|----------|
  | 🗣️ Community | `[competitor] reddit twitter opinions` | Sentiment, complaints, praised features |
  | 🧠 Expert | `[competitor] review analysis blog 2025 2026` | Expert assessment, technical analysis |
  | 📰 News | `[competitor] funding partnership news 2025 2026` | Funding, launches, incidents |
  | ⛓️ On-chain (crypto) | `[competitor] TVL volume wallets metrics` | TVL, volume, fees, active wallets |

- **Output**: Per competitor, tách 2 layers (P5):
  - **Positioning layer**: Họ nói gì? ICP, USP, narrative
  - **Execution layer**: Traction, product depth, shipping velocity, monetization, distribution channels
  - Mỗi claim phải cite source + ghi "as of [date]" (P3, P4)

- **Standardization rules (P2)**:
  - Tiền tệ: quy về USD
  - Traffic: monthly unique visitors
  - Social: X followers + engagement rate
  - Volume: daily average (crypto)
  - Timeframe: ưu tiên 12 tháng gần nhất
  - **Freshness enforcement (P4)**:
    - **Metrics/traction data** (volume, MAU, revenue, funding, traffic): ưu tiên sources ≤3 tháng. Nếu không tìm được → fallback ≤12 tháng + flag "⚠️ Older — [X] months". >12 tháng → drop.
    - **Context/background** (product description, business model, founding story): cho phép ≤12 tháng, flag nếu >3 tháng "⚠️ Older — [X] months".
    - **>12 tháng**: Drop hoàn toàn. Không cite. Ngoại lệ duy nhất: founding date, historical milestone.
  - **Search query enforcement**: Mọi search query cho metrics/traction PHẢI include year filter (e.g. "2026", "2025 2026", "latest", "recent"). Xem Section 6.6.
  - Nếu data mâu thuẫn giữa nguồn → ghi range + note conflict

- **⚠️ Pitfall**: Không có data → "Unknown". Community bias negative → note, balance bằng expert + metrics
- **⚠️ Pitfall**: On-chain chỉ cho crypto → skip nếu không relevant

### Step E: Synthesize Strategic Analysis
- **Input**: Enriched profiles từ Step D + comparison criteria
- **Process**:
  1. Build standardized comparison matrix (user criteria first, AI thêm 3–5) (P2)
  2. Analyze "who's winning and why" — distribution, product, pricing, trust, speed (P1)
  3. Find whitespace — user segments underserved, features commoditized, differentiations winnable (P7)
  4. Assess threats + risk signals (P4)
  5. Generate action items + watchlist (P8)
- **Output**: Sections 2, 4, 5, 6, 7 content
- **⚠️ Pitfall**: All-green cho user → bias. Phải có gaps. Nếu không tìm ra → chưa đủ honest

### Step F: Generate & Deliver
- **Input**: All data từ Steps C–E
- **Process**: Write 8-section report → .md → .docx → save both
- **Output**: 2 files in `/mnt/user-data/outputs/`
- **⚠️ Pitfall**: .docx fails → deliver .md, thông báo lỗi

---

## 6. Hard Rules

| # | Rule | Philosophy |
|---|------|-----------|
| HR-1 | **Không bịa competitor.** Mọi competitor có URL thật. | P3 |
| HR-2 | **Không bịa metrics.** Không tìm được → "Unknown". | P3 |
| HR-3 | **Không đoán pricing.** Không public → ghi rõ. | P3 |
| HR-4 | **Số mâu thuẫn → ghi range + note conflict.** Không cherry-pick. | P3 |
| HR-5 | **Phân biệt Fact vs Inference.** Fact có nguồn. Inference phải label rõ "Inference:". | P3 |
| HR-6 | **Mọi metric ghi "as of [date]".** Metric không có date → giảm confidence. | P4 |
| HR-7 | **Chuẩn hóa đơn vị.** USD, monthly, daily average. Không mix. | P2 |
| HR-8 | **User product = cột 1** trong comparison matrix. | P1 |
| HR-9 | **User-specified criteria PHẢI xuất hiện** trong matrix. | P1 |
| HR-10 | **Tách Positioning vs Execution** cho mỗi deep dive. Không trộn lẫn. | P5 |
| HR-11 | **Strengths/weaknesses từ external sources** — không phải AI tự nhận xét. | P3 |
| HR-12 | **Mỗi deep dive cover ≥2/4 nguồn.** Thiếu nguồn → ghi "No [source] found." | P3 |
| HR-13 | **Mọi insight phải có "so what?"** — không dừng ở observation. | P8 |
| HR-14 | **Whitespace phải actionable** — trả lời "đánh ở đâu", không chỉ "gap ở đây". | P7 |
| HR-15 | **Ít nhất 1 threat 🔴 Critical.** All-green = chưa nghĩ kỹ. | P1 |
| HR-16 | **Output language = input language.** | — |
| HR-17 | **Thiếu required input → STOP và hỏi.** | P3 |
| HR-18 | **Source confidence tier required.** Mọi source gắn label [A]–[D]. D-source claims phải flag ⚠️. | P3 |
| HR-19 | **Freshness gate.** Metrics: ưu tiên ≤3 tháng, fallback ≤12 tháng + flag "⚠️ Older". Context: ≤12 tháng OK, flag nếu >3 tháng. >12 tháng → DROP. Search queries cho metrics PHẢI có date filter. | P4 |

---

## 7. Acceptance Criteria

### Report completeness
- [ ] 8 sections present, không rỗng
- [ ] ≥3 direct competitors deep-dived
- [ ] Battlefield map có ≥2 categories (không chỉ "direct")
- [ ] Whitespace section có ≥2 actionable opportunities

### Data quality (P2, P3, P4)
- [ ] Mọi competitor có URL thật
- [ ] Không metric nào bị bịa
- [ ] Đơn vị chuẩn hóa (USD, monthly, daily)
- [ ] Mọi metric có "as of [date]"
- [ ] Số mâu thuẫn ghi range + note
- [ ] Fact vs Inference phân biệt rõ

### Strategic depth (P1, P5, P7, P8)
- [ ] Deep dives tách Positioning vs Execution
- [ ] "Who's winning & why" trả lời winning factor cụ thể
- [ ] Whitespace chỉ ra ≥2 khoảng trống đánh được
- [ ] Action Items cụ thể — PM có thể tạo ticket từ đây
- [ ] Watchlist có competitor + metric + frequency

### Evidence quality (P3, P11, P12)
- [ ] Mỗi deep dive cover ≥2/4 nguồn feedback
- [ ] Strengths/weaknesses cite external sources
- [ ] Sources section có URL + date + confidence notes
- [ ] Limitations paragraph honest

### Deliverables
- [ ] .md + .docx (hoặc .docx error noted)
- [ ] Naming convention đúng
- [ ] Language match input

---

## 6.6 Search Freshness Enforcement (P4)

Vấn đề: Web search trả về kết quả theo relevance, không theo freshness. Nếu không enforce, report sẽ cite source 6–9 tháng tuổi cho metrics liên tục thay đổi.

### Rules

**1. Date filter trong search queries:**
- Mọi search cho **metrics/traction** (volume, MAU, revenue, funding, traffic, users) → PHẢI thêm date term vào query
- Ví dụ:
  - ✅ `"Kalshi volume February 2026"` hoặc `"Kalshi volume 2026"`
  - ✅ `"Polymarket MAU latest 2026"`
  - ❌ `"Kalshi volume"` (không có date → có thể trả về 2024 article)
- Date terms chấp nhận: năm hiện tại, "latest", "recent", "2025 2026", tháng cụ thể

**2. Post-search freshness check:**
- Sau khi nhận kết quả, kiểm tra tuổi mỗi source TRƯỚC khi cite:
  - **≤3 tháng**: ✅ Dùng cho metrics + context (preferred)
  - **3–12 tháng**: ⚠️ Dùng cho context. Cho metrics CHỈ khi không có source ≤3 tháng (fallback) — flag "⚠️ Older — [X] months".
  - **>12 tháng**: ❌ Drop hoàn toàn. Ngoại lệ: founding date, historical milestone.
- Nếu KHÔNG tìm được source ≤12 tháng cho metric → ghi "Unknown — no source within 12 months found".

**3. Source table enforcement:**
- Section 8 (Sources) PHẢI có cột "Age" cho mỗi source
- Report tự kiểm tra: nếu >30% sources thuộc nhóm 3–12 tháng → flag warning trong Section 8.5

### Ví dụ

| Search purpose | Bad query | Good query |
|---------------|-----------|------------|
| Competitor volume | `Limitless exchange volume` | `Limitless exchange volume 2026` |
| MAU data | `Polymarket active users` | `Polymarket monthly active users latest 2026` |
| Funding round | `Kalshi funding` | `Kalshi funding 2025 2026 latest` |
| Product background | `Azuro protocol overview` | `Azuro protocol` (OK — context, no date needed) |

---

## 8. Failure Modes & Handling

| # | Failure Mode | Xử lý |
|---|-------------|--------|
| FM-1 | Thiếu required input | STOP. Hỏi. Không tiếp cho đến khi đủ. |
| FM-2 | Niche market, ít đối thủ | Vẫn complete. Mở rộng indirect + substitutes (P6). Ghi trong limitations. |
| FM-3 | Crowded market 20+ | List ALL. Deep dive top 5. Ghi selection criteria. |
| FM-4 | Private company, no data | "Unknown". Dùng proxy signals. KHÔNG bịa. (P3) |
| FM-5 | Data conflict giữa sources | Ghi range + note conflict. KHÔNG cherry-pick. (P3) |
| FM-6 | Community feedback quá negative | Note bias. Balance bằng expert + metrics. (P3) |
| FM-7 | Known competitor không tìm thấy | Thêm manually. Research riêng. Ghi "limited public info". |
| FM-8 | AI hiểu sai sản phẩm user | Step B bắt. User sửa → restart. |
| FM-9 | .docx generation fails | Deliver .md. Thông báo lỗi. |
| FM-10 | On-chain data cho non-crypto product | Skip on-chain source. Không ép. |
| FM-11 | **Search chỉ trả source cũ (>3 tháng) cho metric** | Thử ≥2 query variations với date filter. Vẫn cũ → fallback dùng source ≤12 tháng + flag "⚠️ Older — [X] months". Không có ≤12 tháng → ghi "Unknown". (P4, HR-19) |

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
