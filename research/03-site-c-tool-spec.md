# Site C — Tool/Data Property Spec

> **Job of Site C (Phase 5):** a free interactive tool that earns *natural* backlinks (people cite calculators), bootstraps domain authority faster than articles, and funnels intent traffic into Site A/B's affiliate articles. Tools get linked; listicles get scraped.

---

## Primary recommendation (AU): **True Cost of an Australian Employee Calculator**

> Market = Australia-focused (see `04-australia-market.md`). This AU-specific version is *stronger* than the generic global one because super + state payroll tax + WorkCover are uniquely Australian numbers no US site computes — that's both the link magnet and the ranking moat.

**Why this one wins.** It sits on top of the AU-monetizable anchors — **Deel (US$1,500/customer)** and **Remote (recurring %)** for the "hire compliantly in Australia" CTA, plus **Xero/MYOB** for the payroll-software CTA. An AU founder asking "what does this $90k hire *actually* cost me once I add super, payroll tax and WorkCover?" is exactly the buyer those programs pay for, and it's a question every Australian employer Googles.

### What it computes (AU-specific inputs)
Input: gross salary, state/territory, employment type. Output: fully-loaded annual cost:
1. **Direct employee** — base + **superannuation (11.5%→12%)** + **state payroll tax** (varies: NSW 5.45%, VIC 4.85%, etc., above threshold) + **WorkCover/workers' comp** + leave loading
2. **Contractor** — base rate + platform fee (e.g. Deel ~US$49/contractor) + super caveats (AU contractor-super rules)
3. **EOR** — base + employer costs + EOR margin

Side-by-side delta + a "cheapest compliant path" verdict, then CTAs: *"Run AU payroll with Xero / MYOB →"* and *"Hire compliantly via Deel / Remote →"* (affiliate links).

### Why it earns links (AU)
- AU accountants, bookkeepers, and HR bloggers cite super + payroll-tax numbers constantly; a single accurate calculator becomes the reference.
- Per-state data = shareable permutations (`/cost-of-employee/nsw`, `/cost-of-employee/vic`…) — programmatic-SEO surface with genuine AU-regulatory depth US competitors can't replicate.
- EOFY / super-rate-change cycles drive recurring link + traffic spikes every July.
- Ties straight into the highest AU bounties (Deel US$1,500) while being a 100% AU-targeted keyword — low competition, high intent.

### Link-velocity estimate
Conservative **3–6 natural links/month** once indexed and seeded (HARO + a Product Hunt launch + 10 outreach emails to existing "cost to hire" listicles). Calculators in this space routinely hit DR-boosting links from payroll vendors' own blogs.

### Affiliate tie-in (the reason it's not just a vanity tool)
Every result screen routes to a Site A article (`best EOR software`, `deel vs papaya`, `best payroll for remote teams`) carrying the $1,500–$3,000 bounties. Tool = top of funnel; article = conversion.

---

## Runner-up options (build later or A/B)

| Tool | Feeds | Link appeal | Affiliate pull |
|---|---|---|---|
| **Superannuation calculator (employer cost)** | Site A | Very high — uniquely AU, evergreen | Xero / MYOB |
| **Payroll tax threshold checker (by AU state)** | Site A | High — state-by-state, employers search yearly | Xero / MYOB |
| **Xero vs MYOB pricing comparison table** | Site A | Medium — scrapeable but linkable if maintained | Xero (30% recurring) / MYOB |
| **E-signature cost / per-envelope calculator** | Site B | Medium | PandaDoc / Zoho / DocuSign |

> Avoid building Site C around compliance/AML — no affiliate payout downstream (see `01-affiliate-program-map.md`).

---

## Build notes (ties into Phase 2 tech stack)

- **Stack fit:** Astro island + a small client-side JS calculator component; per-country pages can be statically generated from a JSON data file (`packages/content-utils`). No backend needed → still free on Cloudflare Pages.
- **Schema:** add `SoftwareApplication` / `HowTo` or `FAQPage` JSON-LD for rich results.
- **Data source:** seed employer-tax rates per country from public gov/OECD data; cite sources on-page (E-E-A-T).
- **Moat:** keep the country dataset current — staleness kills both trust and links. A quarterly refresh is the maintenance cost.
- **Reuse:** the calculator component lives in `packages/ui`, so Site A can embed a mini-widget version inline in articles.

### Launch sequence (Phase 5)
1. Ship calculator + 10 top-country pages.
2. Product Hunt + SaaSHub submission (free DR links).
3. Outreach: email 10–15 existing "cost to hire internationally" listicles offering the calculator as a resource.
4. HARO: answer remote-work / hiring-cost queries, link the tool.

→ Target: **DR 20+ within 6 months**, with the calculator carrying the bulk of natural links while Site A/B articles carry the revenue.
