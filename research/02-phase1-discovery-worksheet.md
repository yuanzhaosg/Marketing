# Phase 1 Manual-Discovery Worksheet

> Fill these tables by hand this week — no Semrush needed yet. Each row runs a candidate niche through the Phase 2 hard gates. Anything that fails ANY instant-elimination gate is struck out before you spend a cent on keyword tools.
>
> Pre-filled rows reflect the affiliate research in `01-affiliate-program-map.md`. Confirm the cells marked `⟵ check` yourself.

---

## A. The 6 Hard Gates (Phase 2) — pass/fail per niche

Mark ✅/❌. **Any ❌ on an instant-elimination gate = niche eliminated.**

> **Market = Australia-focused.** Use Semrush `au` database. Affiliate cells reflect `04-australia-market.md` (AU Gate-1 research).

| Niche | G1 Affiliates exist (≥5 public) | G2 CPC ≥ $3 | G3 SV ≥ 1k+longtail | G4 SERP not locked (a top-5 DR<40) | G5 No AIO killing clicks | G6 Trend not declining | Verdict |
|---|---|---|---|---|---|---|---|
| AU accounting (Xero/MYOB) | ✅ (Xero 30% rec, MYOB, QB AU) | ⟵ check | ⟵ check | ⟵ check | ⟵ check | ⟵ check | **likely PASS** |
| Hiring / EOR in Australia | ✅ (Deel, Remote) | ⟵ check (high) | ⟵ check | ⟵ check | ⟵ check | ⟵ check | **likely PASS** |
| E-signature (AU audience) | ✅ (PandaDoc/Zoho/DocuSign) | ⟵ check | ⟵ check | ⟵ check | ⟵ check | ⟵ check | **likely PASS** |
| AU-native HR/payroll (Emp Hero, Deputy) | ❌ advisor-gated | — | — | — | — | — | **ELIMINATED (G1)** — content moat only, no $ |
| AU legal practice mgmt (LEAP/Smokeball) | ❌ referral/channel only | — | — | — | — | — | **ELIMINATED (G1)** |

> Gate definitions: see `phases/01-niche-research.md` §Phase 2. AIO = Google AI Overview. Check G4/G5 by Googling the core keyword in an incognito window.

---

## B. G2 / Capterra category snapshot

For each surviving niche, open the matching G2 + Capterra category and record:

| Niche | Category URL | # products | Top 3 tools (AU) | Total reviews | Notes |
|---|---|---|---|---|---|
| Accounting (AU) | g2.com/categories/accounting | | Xero / MYOB / QuickBooks AU | | Xero = default, review "alternatives" |
| EOR / global hiring | g2.com/categories/employer-of-record-eor | | Deel / Remote / Papaya | | AU-targeted keywords |
| E-signature | g2.com/categories/e-signature | | DocuSign / PandaDoc / Annature | | Annature = AU editorial diff (no $) |

> Filter: keep categories with **≥10 products AND ≥500 reviews** (proxy for real demand + monetizable competition).

---

## C. SERP eyeball (Gates 4 & 5) — the cheap competition check

Google each core keyword in **incognito**. Record the top 5 organic results.

**Keyword: `_______________________`**

| Rank | URL / domain | Est. DR (use a free DR checker) | Content type (listicle / review / vendor / forum / media) | Date |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

- AI Overview present? **Y / N** — if Y, does it have clickable citations? **Y / N**
- Any Reddit / forum result in top 10? **Y / N** (good signal — Google rewarding non-corporate content)
- **Verdict:** at least one top-5 with DR < 40? **Y / N** → if N, this keyword is locked; find a longer-tail entry point.

Repeat for the 3–5 core AU keywords per niche, e.g. `best accounting software australia`, `xero alternatives`, `xero vs myob`, `employer of record australia`, `cost to hire an employee australia`, `best electronic signature software australia`, `is an electronic signature legal in australia`.

---

## D. Quick Score (8-point, need ≥5 to advance) — Phase 2

| Niche | Core SV (0–2) | Core CPC (0–2) | Affiliates (0–2) | SERP (0–2) | **Total** |
|---|---|---|---|---|---|
| AU accounting | | | 1.5–2.0 (Xero recurring) | | |
| Hiring / EOR AU | | | 2.0 (Deel/Remote) | | |
| E-signature | | | 2.0 (5 programs) | | |

> Scoring bands in `phases/01-niche-research.md` §Phase 2. CPC/SV cells need Semrush; affiliate cells are pre-scored from the research.

---

## E. Decision log

- [ ] Niches surviving all 6 gates: ___________________________________
- [ ] Eliminated + reason: AML/compliance (G1, US research) · AU-native HR & AU legal PM (G1, advisor/referral-gated)
- [ ] Niches advancing to Semrush `au` validation (Phase 3): AU accounting · EOR-in-AU · e-signature
- [ ] Site A / B / C assignment confirmed: A=AU accounting+EOR · B=e-sign · C=AU employee-cost calculator
- [ ] Date Semrush trial starts: __________  → run `tools/scripts/semrush_keyword_research.py` with `database="au"`

→ Once A/B survive the gates, move to Semrush keyword validation, then Phase 6 deep analysis.
