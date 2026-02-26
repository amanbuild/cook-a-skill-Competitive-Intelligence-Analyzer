#!/usr/bin/env python3
"""
fetch_similarweb.py — SimilarWeb Traffic Enrichment Pipeline
Competitive Intelligence Skill | Step D.3

4-Step Architecture (deterministic, no hallucination):
  Step 1  POST /v1/visitsInfo → store raw_json (immutable audit layer)
  Step 2  Normalize 9 required metrics (deterministic extractor)
  Step 3  Store normalized → traffic_metrics (read-only for AI)
  Step 4  Generate §2.5 Web Traffic Analysis markdown table

Rules (enforced):
  - AI reads ONLY traffic_metrics, never raw_json
  - Missing values → NULL → rendered as "Unknown" in report
  - No estimation, no inference, no hallucination
  - Each run_id is immutable (new run = new run_id)

Usage:
  # Full pipeline (fetch + normalize + report):
  python3 fetch_similarweb.py \\
      --domains "pump.fun,raydium.io,moonshot.money" \\
      --run-id "pumpfun_2026-02"

  # Generate §2.5 markdown from existing DB run:
  python3 fetch_similarweb.py --run-id "pumpfun_2026-02" --report-only

  # Write §2.5 to file:
  python3 fetch_similarweb.py \\
      --domains "hyperliquid.xyz,dydx.exchange,gmx.io" \\
      --run-id "hyperliquid_2026-02" \\
      --output "section_2_5.md"

  # List all runs stored in DB:
  python3 fetch_similarweb.py --list-runs

  # Use custom DB path:
  python3 fetch_similarweb.py --run-id "..." --db "/path/to/custom.db"

Environment:
  SIMILARWEB_API_KEY  Override RapidAPI key (default: hardcoded key)

DB: scripts/traffic.db (SQLite, auto-created)
"""

import argparse
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Fix Windows console encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ─────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────
RAPIDAPI_KEY  = os.getenv("SIMILARWEB_API_KEY", "a0afb1b597msh3eec7896656b701p146162jsnc45aa6032179")
RAPIDAPI_HOST = "similarweb-api1.p.rapidapi.com"
ENDPOINT      = f"https://{RAPIDAPI_HOST}/v1/visitsInfo"
RATE_DELAY    = 1.2   # seconds between API calls (avoid rate-limit)
DB_PATH       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "traffic.db")


# ─────────────────────────────────────────────────────────────
# STEP 0: DATABASE SETUP
# ─────────────────────────────────────────────────────────────
def init_db(db_path: str) -> sqlite3.Connection:
    """Create SQLite DB + tables if not exist."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS traffic_data_raw (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id       TEXT    NOT NULL,
            domain       TEXT    NOT NULL,
            raw_json     TEXT,
            http_status  INTEGER,
            fetched_at   TEXT    NOT NULL,
            api_source   TEXT    DEFAULT 'rapidapi:similarweb-api1',
            error        TEXT,
            UNIQUE(run_id, domain)
        );

        CREATE TABLE IF NOT EXISTS traffic_metrics (
            id                         INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id                     TEXT    NOT NULL,
            domain                     TEXT    NOT NULL,
            -- Visits
            monthly_visits             INTEGER,
            monthly_visits_mom_change  REAL,
            snapshot_date              TEXT,
            monthly_visits_history     TEXT,   -- JSON: [{date, visits}]
            -- Engagement
            bounce_rate                REAL,
            pages_per_visit            REAL,
            avg_visit_duration_seconds REAL,
            -- Rankings
            global_rank                INTEGER,
            country_rank_code          TEXT,
            country_rank               INTEGER,
            category_rank              INTEGER,
            category_name              TEXT,
            -- Geography
            top_country_code           TEXT,
            top_country_share          REAL,
            -- Traffic Sources
            traffic_direct             REAL,
            traffic_search             REAL,
            traffic_social             REAL,
            traffic_referrals          REAL,
            traffic_paid               REAL,
            traffic_mail               REAL,
            -- Metadata
            fetched_at                 TEXT    NOT NULL,
            normalized_at              TEXT    NOT NULL,
            UNIQUE(run_id, domain)
        );
    """)
    conn.commit()
    return conn


# ─────────────────────────────────────────────────────────────
# STEP 1: FETCH RAW DATA
# ─────────────────────────────────────────────────────────────
def _api_call(domain: str) -> tuple:
    """POST /v1/visitsInfo. Returns (data_dict_or_None, http_status, error_msg_or_None)."""
    payload = json.dumps({"q": domain}).encode()
    req = Request(
        ENDPOINT,
        data=payload,
        headers={
            "Content-Type":    "application/json",
            "x-rapidapi-host": RAPIDAPI_HOST,
            "x-rapidapi-key":  RAPIDAPI_KEY,
            "User-Agent":      "curl/8.4.0",
            "Accept":          "*/*",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode()), resp.status, None
    except HTTPError as e:
        body = e.read().decode()[:500]
        return None, e.code, f"HTTP {e.code}: {body}"
    except URLError as e:
        return None, 0, f"URLError: {e.reason}"
    except Exception as e:
        return None, 0, str(e)


def step1_fetch(conn: sqlite3.Connection, run_id: str, domains: list):
    """Fetch each domain → insert into traffic_data_raw (immutable raw layer)."""
    print(f"\n[Step 1] Fetching {len(domains)} domain(s) → traffic_data_raw")
    for i, domain in enumerate(domains, 1):
        print(f"  [{i}/{len(domains)}] {domain} ...", end=" ", flush=True)
        data, status, error = _api_call(domain)
        fetched_at = datetime.now(timezone.utc).isoformat()
        raw_json   = json.dumps(data, ensure_ascii=False) if data else None

        conn.execute("""
            INSERT INTO traffic_data_raw (run_id, domain, raw_json, http_status, fetched_at, error)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(run_id, domain) DO UPDATE SET
                raw_json    = excluded.raw_json,
                http_status = excluded.http_status,
                fetched_at  = excluded.fetched_at,
                error       = excluded.error
        """, (run_id, domain, raw_json, status, fetched_at, error))
        conn.commit()

        if error:
            print(f"FAIL  [{status}] {error[:80]}")
        else:
            visits = data.get("Engagments", {}).get("Visits", "?")
            print(f"OK    visits={visits}  http={status}")

        if i < len(domains):
            time.sleep(RATE_DELAY)


# ─────────────────────────────────────────────────────────────
# STEP 2: NORMALIZE (DETERMINISTIC EXTRACTOR)
# ─────────────────────────────────────────────────────────────
def _safe_float(v, decimals=4):
    """Convert string/float to float, return None on failure."""
    try:
        return round(float(v), decimals)
    except (TypeError, ValueError):
        return None


def normalize(raw_json_str: str) -> dict:
    """
    Extract exactly 9 metric categories from raw JSON.
    RULES:
      - Never infer or estimate missing values → always None
      - Never read keys that don't exist → None
      - MoM change: only if ≥ 2 months of history, prev != 0
    """
    try:
        d = json.loads(raw_json_str)
    except Exception:
        return {}

    # ── A. Monthly Visits (latest snapshot) + history ──────────
    emv            = d.get("EstimatedMonthlyVisits") or {}
    monthly_visits = None
    snapshot_date  = None
    history        = []
    if emv:
        sorted_dates   = sorted(emv.keys())
        snapshot_date  = sorted_dates[-1]
        monthly_visits = emv[snapshot_date]
        history        = [{"date": k, "visits": v} for k, v in sorted(emv.items())]

    # MoM % change (only when prev month available and non-zero)
    mom_change = None
    if len(history) >= 2:
        curr = history[-1]["visits"]
        prev = history[-2]["visits"]
        if prev and prev != 0:
            mom_change = round((curr - prev) / prev * 100, 2)

    # ── B. Engagement ──────────────────────────────────────────
    eng             = d.get("Engagments") or {}
    bounce_rate     = _safe_float(eng.get("BounceRate"))
    pages_per_visit = _safe_float(eng.get("PagePerVisit"))
    avg_duration    = _safe_float(eng.get("TimeOnSite"))

    # ── C. Rankings ────────────────────────────────────────────
    global_rank = (d.get("GlobalRank") or {}).get("Rank")
    cr          = d.get("CountryRank") or {}
    cr_code     = cr.get("CountryCode")
    cr_rank     = cr.get("Rank")
    catr        = d.get("CategoryRank") or {}
    cat_rank    = catr.get("Rank")
    try:
        cat_rank = int(cat_rank)
    except (TypeError, ValueError):
        cat_rank = None
    cat_name = catr.get("Category")

    # ── D. Top Country ─────────────────────────────────────────
    tc_list = d.get("TopCountryShares") or []
    tc_code  = tc_list[0].get("CountryCode") if tc_list else None
    tc_share = tc_list[0].get("Value")       if tc_list else None

    # ── E. Traffic Sources ─────────────────────────────────────
    src = d.get("TrafficSources") or {}
    # NOTE: keys use title case in API response
    t_direct   = src.get("Direct")
    t_search   = src.get("Search")
    t_social   = src.get("Social")
    t_referral = src.get("Referrals")
    t_paid     = src.get("Paid Referrals")
    t_mail     = src.get("Mail")

    return {
        "monthly_visits":             monthly_visits,
        "monthly_visits_mom_change":  mom_change,
        "snapshot_date":              snapshot_date,
        "monthly_visits_history":     json.dumps(history),
        "bounce_rate":                bounce_rate,
        "pages_per_visit":            pages_per_visit,
        "avg_visit_duration_seconds": avg_duration,
        "global_rank":                global_rank,
        "country_rank_code":          cr_code,
        "country_rank":               cr_rank,
        "category_rank":              cat_rank,
        "category_name":              cat_name,
        "top_country_code":           tc_code,
        "top_country_share":          tc_share,
        "traffic_direct":             t_direct,
        "traffic_search":             t_search,
        "traffic_social":             t_social,
        "traffic_referrals":          t_referral,
        "traffic_paid":               t_paid,
        "traffic_mail":               t_mail,
    }


# ─────────────────────────────────────────────────────────────
# STEP 3: STORE NORMALIZED
# ─────────────────────────────────────────────────────────────
def step3_normalize_store(conn: sqlite3.Connection, run_id: str):
    """Read raw rows → normalize → insert into traffic_metrics."""
    print(f"\n[Step 3] Normalizing → traffic_metrics")
    rows = conn.execute(
        "SELECT domain, raw_json, fetched_at FROM traffic_data_raw "
        "WHERE run_id=? AND raw_json IS NOT NULL",
        (run_id,)
    ).fetchall()

    normalized_at = datetime.now(timezone.utc).isoformat()

    for row in rows:
        domain     = row["domain"]
        raw_json   = row["raw_json"]
        fetched_at = row["fetched_at"]
        m          = normalize(raw_json)

        if not m:
            print(f"  {domain}: SKIP (parse error)")
            continue

        conn.execute("""
            INSERT INTO traffic_metrics (
                run_id, domain,
                monthly_visits, monthly_visits_mom_change, snapshot_date, monthly_visits_history,
                bounce_rate, pages_per_visit, avg_visit_duration_seconds,
                global_rank, country_rank_code, country_rank, category_rank, category_name,
                top_country_code, top_country_share,
                traffic_direct, traffic_search, traffic_social,
                traffic_referrals, traffic_paid, traffic_mail,
                fetched_at, normalized_at
            ) VALUES (
                ?,?,
                ?,?,?,?,
                ?,?,?,
                ?,?,?,?,?,
                ?,?,
                ?,?,?,
                ?,?,?,
                ?,?
            )
            ON CONFLICT(run_id, domain) DO UPDATE SET
                monthly_visits             = excluded.monthly_visits,
                monthly_visits_mom_change  = excluded.monthly_visits_mom_change,
                snapshot_date              = excluded.snapshot_date,
                monthly_visits_history     = excluded.monthly_visits_history,
                bounce_rate                = excluded.bounce_rate,
                pages_per_visit            = excluded.pages_per_visit,
                avg_visit_duration_seconds = excluded.avg_visit_duration_seconds,
                global_rank                = excluded.global_rank,
                country_rank_code          = excluded.country_rank_code,
                country_rank               = excluded.country_rank,
                category_rank              = excluded.category_rank,
                category_name              = excluded.category_name,
                top_country_code           = excluded.top_country_code,
                top_country_share          = excluded.top_country_share,
                traffic_direct             = excluded.traffic_direct,
                traffic_search             = excluded.traffic_search,
                traffic_social             = excluded.traffic_social,
                traffic_referrals          = excluded.traffic_referrals,
                traffic_paid               = excluded.traffic_paid,
                traffic_mail               = excluded.traffic_mail,
                fetched_at                 = excluded.fetched_at,
                normalized_at              = excluded.normalized_at
        """, (
            run_id, domain,
            m["monthly_visits"], m["monthly_visits_mom_change"],
            m["snapshot_date"],  m["monthly_visits_history"],
            m["bounce_rate"],    m["pages_per_visit"], m["avg_visit_duration_seconds"],
            m["global_rank"],    m["country_rank_code"], m["country_rank"],
            m["category_rank"],  m["category_name"],
            m["top_country_code"], m["top_country_share"],
            m["traffic_direct"], m["traffic_search"],    m["traffic_social"],
            m["traffic_referrals"], m["traffic_paid"],   m["traffic_mail"],
            fetched_at, normalized_at,
        ))
        conn.commit()

        v_str = f"{m['monthly_visits']:,}" if m["monthly_visits"] else "NULL"
        b_str = f"{m['bounce_rate']*100:.1f}%" if m["bounce_rate"] else "NULL"
        r_str = f"#{m['global_rank']:,}" if m["global_rank"] else "NULL"
        print(f"  {domain:30s}  visits={v_str:>12s}  bounce={b_str:>7s}  global={r_str}")


# ─────────────────────────────────────────────────────────────
# STEP 4: GENERATE §2.5 MARKDOWN (AI READ-ONLY LAYER)
# ─────────────────────────────────────────────────────────────
def _fmt_visits(v):
    if v is None:         return "Unknown"
    if v >= 1_000_000:    return f"{v/1_000_000:.1f}M"
    if v >= 1_000:        return f"{v/1_000:.0f}K"
    return str(v)

def _fmt_pct(v, decimals=1):
    if v is None: return "Unknown"
    return f"{v * 100:.{decimals}f}%"

def _fmt_duration(seconds):
    if seconds is None: return "Unknown"
    s = int(seconds)
    m, sec = divmod(s, 60)
    return f"{m}:{sec:02d}"

def _fmt_mom(v):
    if v is None: return ""
    sign = "+" if v >= 0 else ""
    return f" ({sign}{v:.1f}% MoM)"

def _fmt_rank(v):
    if v is None: return "Unknown"
    return f"#{v:,}"


def step4_generate_report(conn: sqlite3.Connection, run_id: str) -> str:
    """
    AI READ-ONLY: reads traffic_metrics, outputs §2.5 markdown.
    RULES:
      - Only reads from traffic_metrics (never raw_json)
      - NULL → "Unknown" (never estimate)
      - No external calls
    """
    rows = conn.execute(
        """SELECT * FROM traffic_metrics
           WHERE run_id = ?
           ORDER BY
             CASE WHEN monthly_visits IS NULL THEN 1 ELSE 0 END,
             monthly_visits DESC""",
        (run_id,)
    ).fetchall()

    if not rows:
        return f"_No traffic metrics found for run_id=`{run_id}`. Run without --report-only first._"

    domains   = [r["domain"] for r in rows]
    snap_date = rows[0]["snapshot_date"] or "Unknown"
    norm_at   = (rows[0]["normalized_at"] or "")[:10]

    sep       = " | "
    col_align = "|".join([":----------:"] * len(domains))

    def trow(label, values):
        return f"| {label} | {sep.join(str(v) for v in values)} |"

    lines = [
        "### §2.5 Web Traffic Analysis",
        "",
        f"| Metric | {sep.join(domains)} |",
        f"|--------|{col_align}|",
    ]

    # ── Row 1: Monthly Visits ──
    vals = [f"**{_fmt_visits(r['monthly_visits'])}**{_fmt_mom(r['monthly_visits_mom_change'])}"
            for r in rows]
    lines.append(trow("Monthly Visits", vals))

    # ── Row 2: Bounce Rate ──
    lines.append(trow("Bounce Rate",
        [_fmt_pct(r["bounce_rate"]) for r in rows]))

    # ── Row 3: Pages / Visit ──
    lines.append(trow("Pages / Visit",
        [f"{r['pages_per_visit']:.2f}" if r["pages_per_visit"] is not None else "Unknown"
         for r in rows]))

    # ── Row 4: Avg Visit Duration ──
    lines.append(trow("Avg Visit Duration",
        [_fmt_duration(r["avg_visit_duration_seconds"]) for r in rows]))

    # ── Row 5: Audience Gender (not in API → always Unknown) ──
    lines.append(trow("Audience (M/F)", ["Unknown"] * len(rows)))

    # ── Row 6: Largest Age Group (not in API → always Unknown) ──
    lines.append(trow("Largest Age Group", ["Unknown"] * len(rows)))

    # ── Row 7: Top Country ──
    vals = []
    for r in rows:
        cc = r["top_country_code"]
        sh = r["top_country_share"]
        vals.append(f"{cc} ({sh*100:.0f}%)" if (cc and sh is not None) else "Unknown")
    lines.append(trow("Top Country", vals))

    # ── Row 8: Traffic Mix ──
    vals = []
    for r in rows:
        parts = []
        if r["traffic_direct"]    is not None: parts.append(f"Direct {r['traffic_direct']*100:.0f}%")
        if r["traffic_search"]    is not None: parts.append(f"Search {r['traffic_search']*100:.0f}%")
        if r["traffic_referrals"] is not None: parts.append(f"Ref {r['traffic_referrals']*100:.0f}%")
        vals.append(" / ".join(parts) if parts else "Unknown")
    lines.append(trow("Traffic Mix (D/S/R)", vals))

    # ── Row 9: Social Traffic ──
    lines.append(trow("Social Traffic",
        [_fmt_pct(r["traffic_social"]) for r in rows]))

    # ── Row 10: Global Rank ──
    lines.append(trow("Global Rank",
        [_fmt_rank(r["global_rank"]) for r in rows]))

    # ── Row 11: Category Rank ──
    vals = []
    for r in rows:
        if r["category_rank"] and r["category_name"]:
            cat_short = r["category_name"].split("/")[-1].replace("_", " ").title()
            vals.append(f"#{r['category_rank']} {cat_short}")
        elif r["category_rank"]:
            vals.append(f"#{r['category_rank']}")
        else:
            vals.append("Unknown")
    lines.append(trow("Category Rank", vals))

    lines += [
        "",
        "> **⚠ Data Availability Notes:**",
        "> - `Audience (M/F)` and `Largest Age Group`: not returned by `/v1/visitsInfo` endpoint. Use SimilarWeb.com manually for demographics.",
        "> - `Traffic Mix` = Direct / Search / Referrals (paid referrals excluded from display).",
        "> - `MoM` = month-over-month % change vs prior month (requires ≥ 2 months in history).",
        "",
        "**Appendix:**",
        f"> Traffic Source: `RapidAPI similarweb-api1 /v1/visitsInfo`  ",
        f"> Snapshot Date: `{snap_date}`  ",
        f"> Fetched At: `{norm_at}`  ",
        f"> Run ID: `{run_id}`  ",
    ]

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# HELPER: list all runs
# ─────────────────────────────────────────────────────────────
def list_runs(conn: sqlite3.Connection):
    """Print summary of all run_ids stored in DB."""
    rows = conn.execute("""
        SELECT r.run_id,
               COUNT(DISTINCT r.domain)  AS domains_raw,
               COUNT(DISTINCT m.domain)  AS domains_norm,
               MAX(r.fetched_at)         AS last_fetch
        FROM traffic_data_raw r
        LEFT JOIN traffic_metrics m ON r.run_id = m.run_id AND r.domain = m.domain
        GROUP BY r.run_id
        ORDER BY last_fetch DESC
    """).fetchall()

    if not rows:
        print("No runs found in DB.")
        return

    print(f"\n{'Run ID':<35}  {'Raw':>5}  {'Norm':>5}  {'Last Fetched'}")
    print("─" * 70)
    for r in rows:
        print(f"{r['run_id']:<35}  {r['domains_raw']:>5}  {r['domains_norm']:>5}  {r['last_fetch'][:19]}")


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="SimilarWeb Traffic Pipeline — Step D.3 of Competitive Intelligence Skill",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--domains",      help="Comma-separated domain list (e.g. 'pump.fun,raydium.io')")
    parser.add_argument("--domains-file", help="Text file with one domain per line")
    parser.add_argument("--run-id",       help="Unique run identifier (e.g. 'pumpfun_2026-02')")
    parser.add_argument("--report-only",  action="store_true",
                        help="Skip fetch; read from DB and generate §2.5 markdown")
    parser.add_argument("--output",       help="Write §2.5 markdown to this file path")
    parser.add_argument("--list-runs",    action="store_true", help="List all stored runs")
    parser.add_argument("--db",           default=DB_PATH,
                        help=f"SQLite DB path (default: {DB_PATH})")
    args = parser.parse_args()

    conn = init_db(args.db)

    # ── List runs ──────────────────────────────────────────────
    if args.list_runs:
        list_runs(conn)
        conn.close()
        return

    if not args.run_id:
        parser.error("--run-id is required (unless using --list-runs)")

    # ── Full pipeline ──────────────────────────────────────────
    if not args.report_only:
        domains = []
        if args.domains:
            domains = [d.strip() for d in args.domains.split(",") if d.strip()]
        if args.domains_file:
            with open(args.domains_file, encoding="utf-8") as f:
                domains += [ln.strip() for ln in f if ln.strip()]
        if not domains:
            parser.error("Provide --domains or --domains-file when not using --report-only")

        step1_fetch(conn, args.run_id, domains)
        step3_normalize_store(conn, args.run_id)

    # ── Report ────────────────────────────────────────────────
    print(f"\n[Step 4] Generating §2.5 markdown  run_id={args.run_id}")
    report = step4_generate_report(conn, args.run_id)
    print("\n" + "━" * 70)
    print(report)
    print("━" * 70)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n→ Written to: {args.output}")

    conn.close()


if __name__ == "__main__":
    main()
