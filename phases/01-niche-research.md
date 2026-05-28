# Phase 1: Niche Research — Full SOP

> **Goal**: Discover 300–600 candidate niches, score them systematically, and select the top 1–3 directions for your sites.
> **Duration**: 7–10 days (AI-assisted) or 3–4 weeks (manual)
> **Tools Required**: Semrush API, Ahrefs, Google Search, PartnerStack

---

## System Architecture

```
Phase 0: Revenue goals → hard filtering thresholds
    ↓
Phase 1: Platform discovery (300–600 candidates)
    ↓
Phase 2: Hard elimination (keep 50–120)
    ↓
Phase 3: Keyword cluster analysis (merge into 40–60 clusters)
    ↓
Phase 4: 100-point scoring (top 30 clusters)
    ↓
Phase 5: Three-site allocation
    ↓
Phase 6: Deep analysis (top 10)
    ↓
Phase 7: Final decision + first 20 article topics
```

---

## Phase 1: Platform Discovery

### Source A: G2 Software Categories

```
1. Scrape https://www.g2.com/categories
2. For each category record:
   - Category name
   - Product count
   - Top 3 product names
   - Total review count
3. Filter: product count ≥ 10, reviews ≥ 500
4. Expected output: 200–400 categories
```

### Source B: Capterra Categories

```
1. Scrape https://www.capterra.com/categories
2. Same fields as G2
3. Merge with G2, deduplicate (same niche = keep highest numbers)
4. Expected new additions: 50–100
```

### Source C: PartnerStack Marketplace

```
1. Visit https://partnerstack.com/marketplace
2. For each program record:
   - Product name
   - Category (map to G2/Capterra)
   - Commission type: recurring or one-time
   - Commission rate (%)
   - Product pricing tier
3. Flag: recurring commission ≥ 20% → high priority
4. Expected: 150–200 programs
```

### Source D: Impact.com

```
1. Visit https://app.impact.com/marketplace/
2. Filter: Software & Tech
3. Record: product name, category, commission rate, EPC
4. Map to G2/Capterra categories
```

### Source E: Semrush Seed Keywords

**Tier 1 Seeds (High CPC + Rich Affiliate Programs)**

| Seed Keyword | CPC Range | Why It's Valuable |
|-------------|-----------|------------------|
| gusto alternatives | $15–40 | Enterprise HR, high-converting |
| quickbooks alternatives | $15–35 | High affiliate commissions |
| clio alternatives | $20–60 | Legal tech, very high CPC, blue ocean |
| zendesk alternatives | $15–30 | Enterprise CX, AI disruption ongoing |
| workable alternatives | $12–25 | ATS/recruiting, B2B, high commissions |
| docusign alternatives | $12–25 | Every business needs e-sign |
| clickup alternatives | $10–25 | Massive long-tail |
| 1password alternatives | $15–40 | Security, high-value users |
| hootsuite alternatives | $8–18 | Social media, many tools |
| shopify alternatives | $8–20 | Ecommerce, infinite long-tail |

**Tier 2 Seeds (AI Disruption = New Low-KD Keywords)**

| Seed Keyword | Why It's Valuable |
|-------------|------------------|
| ai customer service tools | New keywords, competitive landscape unsettled |
| ai recruiting software | New, high CPC |
| ai legal software | Very high CPC, almost no competitors |
| ai bookkeeping software | High CPC, AI vs traditional comparison goldmine |
| surfer seo alternatives | Clear paying user base |
| apollo.io alternatives | $10–20 CPC, B2B sales |

**Tier 3 Seeds (Platform Ecosystems = Endless Long-tail)**

| Seed Keyword | Why It's Valuable |
|-------------|------------------|
| best shopify apps for | Thousands of long-tail combinations |
| hubspot alternatives for | CRM, high CPC |
| salesforce alternatives small business | Very high CPC, B2B |
| notion alternatives | Many comparison keywords |
| figma alternatives | Design, many affiliates |
| zapier for [industry] | Vertical long-tail, low competition |

**Semrush API Call for Each Seed:**

```python
params = {
    "type": "phrase_related",
    "phrase": seed_keyword,
    "database": "us",
    "display_limit": 500,
    "display_filter": "+|Kd|Lt|30+|Vol|Gt|100+|Cp|Gt|1",
    "export_columns": "Ph,Nq,Cp,Kd,Nr",
    "display_sort": "nq_desc",
}
# Note: use phrase_related, NOT phrase_this (phrase_this returns SV=0)
```

### Source F: Reddit Community Signals

```
Subreddits to monitor:
  r/SaaS, r/microsaas, r/EntrepreneurRideAlong
  r/SEO, r/Entrepreneur, r/indiehackers

Search patterns:
  "what tool do you use for"
  "best software for"
  "looking for a tool that"
  "alternative to"
  "recommend a"

Filter: niche has ≥ 50 relevant discussion threads
Signal: genuine user demand, not just search volume
```

### Source G: Competitor Site Reverse Discovery

```
Known B2B SaaS affiliate sites (extract their top keyword categories):
  - softwaresuggest.com
  - tekpon.com
  - bloggingwizard.com
  - thewordpoint.com

In Semrush: Domain Overview → Top Keywords → filter by category
High-frequency categories across competitors = validated traffic opportunities
```

### Source H: Demand Validation Lists

```
1. toolify.ai/revenue — AI tool revenue rankings
   - Top 100 tools by monthly revenue
   - Categories with ≥ 3 tools = validated monetization

2. trustmrr.com — Weekly MRR leaderboard
   - Recent entrants = growing categories

Filter: ≥ 3 tools in same category in top 100 = proven money category
```

### Source I: Word Root Expansion

```
High-value word roots (combine with any industry):
  Generator, Calculator, Checker, Analyzer, Tracker
  Converter, Builder, Monitor, Optimizer, Automator
  Scheduler, Dashboard, Manager, Sender, Editor

Examples:
  "invoice generator" → high SV, clear commercial intent
  "payroll calculator" → decision stage, high CPC
  "email tracker" → tool comparison, multiple affiliates

Query: Semrush phrase_all for [industry] + [root] combinations
Filter: SV ≥ 500, CPC ≥ $3
```

---

## Phase 2: Hard Elimination

Run every candidate through these gates:

```
GATE 1 — Affiliate programs exist?
  Check: PartnerStack + Impact.com + product websites
  Fail: Top 3 tools in category have zero public affiliate programs → eliminate

GATE 2 — CPC acceptable?
  Check: Semrush "best [category] software" CPC
  Fail: CPC < $3 → eliminate

GATE 3 — Enough search volume?
  Check: Semrush "best [category] software" monthly SV
  Fail: Global SV < 1,000 and no long-tail cluster → eliminate

GATE 4 — SERP not completely locked out?
  Check: Google top 5 results for "best [category] software"
  Fail: All top 5 are DR > 85 AND G2+Capterra+Trustpilot occupy top 3 → eliminate

GATE 5 — AI Overview not blocking traffic?
  Check: Google the top 3 keywords manually
  Fail: ≥ 2 core keywords trigger AI Overview with no clickable links → eliminate

GATE 6 — Market not declining?
  Check: Google Trends, 5-year view
  Fail: Consistent 5-year decline → eliminate
```

### Quick Score (8-point system, need ≥ 5 to advance)

| Dimension | Max | Threshold |
|-----------|-----|-----------|
| Core keyword SV | 2 | ≥50K=2, ≥10K=1.5, ≥3K=1, ≥1K=0.5 |
| Core keyword CPC | 2 | ≥$20=2, ≥$10=1.5, ≥$5=1, ≥$3=0.5 |
| Affiliate programs | 2 | ≥5 recurring=2, 3–4=1.5, 1–2=1 |
| SERP competitiveness | 2 | DR<40 in top 5=2, DR40–60=1.5, all DR>85=0 |

**KGR Quick Check** (for borderline cases):
```
KGR = Monthly SV / allintitle results
KGR > 1.0 → very low competition, prioritize
KGR 0.25–1.0 → acceptable competition
KGR < 0.25 → competitive, check SERP DR carefully
```

---

## Phase 3: Keyword Cluster Analysis

For each direction that passed Phase 2, generate 5 seed keywords:
- `best [direction] software`
- `[direction] tools`
- `[direction] alternatives`
- `[direction] platform`
- `ai [direction] software`

Expand each with Semrush phrase_related (limit 300).

**Hard filter the expanded keywords:**
```
Keep only: KD ≤ 25 AND SV ≥ 150 AND CPC ≥ $2
```

**Cluster the results** (use TF-IDF + KMeans, or manually group by topic).

**Eliminate clusters where:**
```
Total cluster SV < 150,000 → ceiling too low
Average KD > 30 → new site can't compete
Average CPC < $3 → not commercial enough
Count of KD ≤ 20 keywords < 15 → nothing to rank for in year 1
```

**Keep top 30–40 clusters for Phase 4 scoring.**

---

## Phase 4: 100-Point Scoring System

Score each cluster on 7 dimensions:

### A: Search Volume (0–15 pts)

| Monthly SV | Score |
|-----------|-------|
| ≥ 500,000 | 15 |
| ≥ 200,000 | 13 |
| ≥ 100,000 | 11 |
| ≥ 50,000 | 9 |
| ≥ 20,000 | 7 |
| ≥ 10,000 | 5 |
| ≥ 5,000 | 3 |
| ≥ 1,000 | 1 |

Bonus: +2 if cluster has ≥ 30 keywords with KD ≤ 20

### B: CPC (0–25 pts) — Highest Weight

| CPC | Score |
|-----|-------|
| ≥ $80 | 25 |
| ≥ $50 | 22 |
| ≥ $30 | 19 |
| ≥ $20 | 16 |
| ≥ $15 | 13 |
| ≥ $10 | 10 |
| ≥ $7 | 7 |
| ≥ $5 | 5 |
| ≥ $3 | 3 |
| ≥ $2 | 1 |

### C: Affiliate Program Quality (0–25 pts) — Highest Weight

**Commission Rate (0–12 pts)**
- Recurring ≥ 40% → 12 pts
- Recurring 30–40% → 10 pts
- Recurring 20–30% → 9 pts
- Recurring 10–20% → 6 pts
- One-time ≥ 30% → 7 pts
- One-time 10–20% → 3 pts

**Program Count (0–7 pts)**
- ≥ 20 programs → 7 pts
- 10–19 → 5 pts
- 5–9 → 4 pts
- 3–4 → 2 pts
- 1–2 → 1 pt

**Average Product Price (0–6 pts)**
- ≥ $500/month → 6 pts (enterprise)
- ≥ $200/month → 5 pts
- ≥ $100/month → 4 pts
- ≥ $50/month → 2 pts
- < $50/month → 1 pt

### D: SERP Competitiveness (0–20 pts)

**DR Distribution (0–8 pts)**
- Top 5 includes DR < 30 site → 8 pts
- Top 5 includes DR 30–50 → 6 pts
- Top 5 includes DR 50–65 → 4 pts
- Top 5 minimum DR 65–80 → 2 pts
- All top 5 DR > 80 → 0 pts

**Content Types (0–6 pts)**
- Has listicle pages (not just major media) → +5
- Has review content → +4
- Has Reddit/forum results → +2
- All results are product official sites / major media → 0

**AI Overview Status (−5 to +6 pts)**
- No AI Overview → +6
- AIO with clickable citations → +3
- AIO without citations → 0
- AIO dominates, no citations → −5

### E: Keyword Depth (0–10 pts)

Commercial keyword count (contains "best", "review", "vs", "alternative", "pricing"):
- ≥ 5,000 → 5 pts
- ≥ 2,000 → 4 pts
- ≥ 1,000 → 3 pts
- ≥ 500 → 2 pts
- ≥ 200 → 1 pt

Keyword diversity bonus (0–5 pts):
- ≥ 50 "alternative to [product]" keywords → +2
- ≥ 100 "vs" keywords → +1
- ≥ 50 "pricing/cost" keywords → +1
- ≥ 100 "for [industry]" vertical keywords → +1

### F: Conversion Funnel Completeness (0–5 pts)

Can you write all three funnel layers?
- Awareness layer: [How to use X], [What is X], [X guide]
- Comparison layer: [Best X software], [X vs Y], [X alternatives]
- Decision layer: [X pricing], [X review], [X free trial]

Score:
- All three layers possible AND SERP shows ranking opportunity → 5 pts
- Two layers possible, decision layer locked by authority sites → 3 pts
- Only awareness + comparison → 1 pt
- Only awareness (no monetizable content path) → 0 pts

### G: Trend (0–5 pts)

Google Trends (0–3 pts):
- Clear upward trend (last 12 months avg > prior 12 months by ≥ 30%) → 3 pts
- Stable growth (10–30%) → 2 pts
- Flat (±10%) → 1 pt
- Declining → 0 pts

Semrush YoY SV growth (0–2 pts):
- ≥ 20% YoY growth → 2 pts
- 0–20% → 1 pt
- Declining → 0 pts

---

## Phase 5: Three-Site Allocation

After scoring, assign top directions to site types:

**Site A — Authority Hub**
- Requirement: CPC ≥ $15, cluster SV ≥ 300,000, ≥ 5 recurring affiliates
- Strategy: Full coverage (Best X / Review / Alternative / vs)
- Keyword overlap with other sites: < 30%

**Site B — Commercial Vertical**
- Requirement: CPC ≥ $8, strong topic independence from Site A
- Strategy: Narrower niche, fewer but higher-converting articles
- Avoid: same exact product names as Site A (PBN risk if same owner)

**Site C — Tool/Data Site**
- Requirement: Clear tool opportunity (calculator, comparison table, database)
- Strategy: Tools attract natural backlinks, bootstrap DR faster
- Examples: Payroll calculator, SaaS pricing comparison table, ROI calculator

---

## Phase 6: Deep Analysis (Top 10 Only)

For each top-10 direction, produce a deep analysis report covering:

1. **Keyword Universe** — Top 50 keywords by priority (P1: KD<20, P2: KD 20–35, P3: KD>35)
2. **SERP Analysis** — Full top-10 breakdown (URL, DR, word count, content type, date)
3. **Competitor Deep-Dive** — Weakest competitor's content gaps and how to beat them
4. **Affiliate Program Audit** — Full list with commissions, cookie windows, pricing
5. **Revenue Projection** — 3 scenarios (8K / 15K / 30K monthly sessions)
6. **Link Acquisition Feasibility** — % of competitor backlinks you can replicate
7. **Risk Assessment** — SERP risk, affiliate risk, niche risk

---

## Phase 7: Final Decision

Output format:

```
FINAL RECOMMENDATION
====================

Site A: [Niche Name]
  Score: XX/100 | CPC: $XX | Cluster SV: XXX,000
  Reason: [2 sentences based on data]
  First 20 articles: [list with KD and SV for each]

Site B: [Niche Name]
  Score: XX/100 | CPC: $XX | Cluster SV: XXX,000
  Keyword overlap with Site A: XX%

Site C: [Niche Name]
  Score: XX/100
  Tool opportunity: [specific tool idea]
  Estimated backlink velocity: [X natural links/month]

M12 Revenue Projection:
  Conservative: $X,XXX/month
  Base case:    $X,XXX/month
  Optimistic:   $X,XXX/month
```

→ **Ready for Phase 2: Tech Stack Setup**
