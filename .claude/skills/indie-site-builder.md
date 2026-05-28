# indie-site-builder — B2B SaaS Affiliate Site Skill

Use this skill when the user wants to build a B2B SaaS affiliate review site, or asks for help with any step of the process: niche selection, site setup, content creation, affiliate monetization, launch, backlink building, or ongoing operations.

## Trigger Conditions

Use this skill when the user mentions:
- "build an indie site", "做独立站", "affiliate site", "niche site"
- "find a profitable niche", "选题", "方向挖掘", "关键词调研"
- "set up Astro site", "Cloudflare Pages deployment"
- "affiliate program", "联盟营销", "AdSense alternative"
- "backlinks for new site", "Product Hunt launch", "SaaSHub"
- "how to get first traffic", "SEO for new site", "DR building"
- Any question about the phases below

---

## Initial Assessment

Before starting, determine where the user is in the journey:

```
Ask: "Where are you right now?"

A. Haven't chosen a niche yet → Start at Phase 0
B. Have a niche, need to build the site → Start at Phase 2
C. Site is live, need content → Start at Phase 3
D. Content exists, need traffic → Start at Phase 5–6
E. Running site, need to scale → Start at Phase 7
```

Also check:
- Do they have a Semrush account? (Phase 1 requires API)
- Do they have a domain? (Phase 2 requires this)
- What's their monthly time budget? (affects content plan)

---

## Phase Overview

### Phase 0: Goal Setting
**File**: `phases/00-goal-setting.md`

Set revenue targets and translate them into keyword selection criteria.
- Target: $2,000–$3,000/month by M12
- Required cluster SV ≥ 300,000
- Required KD ≤ 25 count ≥ 30
- CPC ≥ $8 minimum
- ≥ 5 recurring affiliate programs in niche

### Phase 1: Niche Research
**File**: `phases/01-niche-research.md`

Full 7-phase SOP for discovering and scoring 300–600 candidates:
- G2, Capterra, PartnerStack scraping
- Semrush API keyword clustering
- 100-point scoring system
- Three-site allocation framework

**Key output**: Top 10 niche directions with full data

### Phase 2: Tech Stack Setup
**File**: `phases/02-tech-stack-setup.md`

Build the Astro + Cloudflare Pages site from scratch:
- Monorepo structure (pnpm workspaces)
- Shared UI and content-utils packages
- Microsoft Clarity analytics
- Schema markup
- SEO head configuration

**Key output**: Live site deployed to Cloudflare Pages

### Phase 3: Content Creation
**File**: `phases/03-content-creation.md`

Plan and write the first 20 articles:
- Content types: Best X, Alternatives, vs, Review, How-to
- Keyword prioritization (KD ≤ 20 first)
- Anti-AI-detection writing guidelines
- E-E-A-T signals
- Internal linking structure

**Key output**: 20 published articles targeting P1 keywords

### Phase 4: Affiliate & Monetization Setup
**File**: `phases/04-affiliate-monetization.md`

Set up affiliate programs and revenue tracking:
- PartnerStack and Impact.com signup
- Affiliate link placement strategy
- UTM tracking setup
- CTA component implementation
- Revenue dashboard

**Key output**: All affiliate links live, tracking configured

### Phase 5: Launch & Promotion
**File**: `phases/05-launch-promotion.md`

Launch across platforms for initial traffic and backlinks:
- Product Hunt launch (full strategy)
- SaaSHub submission
- Directory submissions
- Social media posts (X/Twitter, LinkedIn)
- Community engagement (Reddit, Indie Hackers)

**Key output**: First 50+ backlinks, initial traffic spike

### Phase 6: Backlink Building
**File**: `phases/06-backlink-building.md`

Systematic DR building from free and low-cost sources:
- Free DR80–95 backlinks (Notion, Stripe Climate, Crunchbase, G2, PH)
- Reddit and community engagement
- HARO / journalist outreach
- Guest post opportunities
- Chrome extension strategy

**Key output**: DR 20+ within 6 months

### Phase 7: Ongoing Operations
**File**: `phases/07-ongoing-operations.md`

Weekly and monthly routines for scaling:
- Content update schedule
- Keyword rank tracking
- Affiliate revenue monitoring
- Link building pipeline
- Site health checks

**Key output**: Systematic operation toward $2K+/month

---

## Quick Reference: Free DR80+ Backlinks

These can be done immediately after launch. Do all of them on Day 1:

| Source | DR | Type | Action |
|--------|-----|------|--------|
| Notion (published page) | 92 | Do-follow | Create page, publish to web, enable search indexing |
| Product Hunt | 91 | Do-follow | Submit product listing |
| Stripe Climate | 94 | Do-follow | Enable 0.1% climate contribution → get badge page |
| Crunchbase | 91 | Do-follow | Create company/product profile |
| G2 | 91 | Do-follow | Claim or create product listing |
| Capterra | 88 | Do-follow | Submit product |
| GitHub | 96 | Do-follow | Create repo with README linking site |
| Chrome Web Store | 99 | Do-follow | Publish small extension |
| SaaSHub | 78 | Do-follow | Submit product (takes ~30 days to approve) |

---

## Tech Stack Quick Reference

```
Framework:    Astro 5.x
Hosting:      Cloudflare Pages (free)
Package mgr:  pnpm 9.x
Monorepo:     pnpm workspaces
Styling:      Tailwind CSS 3.x
Analytics:    Microsoft Clarity (free)
Schema:       JSON-LD via Astro components
Fonts:        Google Fonts or self-hosted
Images:       Astro Image optimization
```

### Monorepo Structure
```
my-sites/
├── apps/
│   ├── site-one/          # First niche site
│   ├── site-two/          # Second niche site
│   └── site-three/        # Third niche site
├── packages/
│   ├── ui/                # Shared components
│   └── content-utils/     # Shared types & utilities
├── package.json
└── pnpm-workspace.yaml
```

---

## Content Types and Priority Order

Write in this order for fastest path to traffic:

1. **Alternatives pages** — `[Tool] alternatives` — High commercial intent, often KD ≤ 25
2. **Best X pages** — `best [category] software` — High SV, builds authority
3. **vs pages** — `[Tool A] vs [Tool B]` — Decision-stage, high conversion
4. **Review pages** — `[Tool] review` — Long-tail, brand searches
5. **How-to guides** — Builds topical authority, attracts links

---

## Revenue Math (Reality Check)

Conservative model for M12:

```
Cluster total SV:        300,000
Your traffic share (5%):  15,000 sessions/month
CTR to affiliate links:      10% = 1,500 clicks
Conversion rate:            1.5% = 22 conversions
Average commission:          $80
Monthly revenue:          ~$1,760

With two strong clusters:  ~$3,000–$4,000/month
```

---

## Related Skills

- **seo-audit**: Technical SEO audit for live sites
- **ai-seo**: Optimize for AI Overviews and LLM citations
- **programmatic-seo**: Generate pages at scale from data
- **schema**: Implement structured data for rich results
- **cro**: Optimize pages for affiliate conversion

---

## References

See individual phase files in `phases/` directory for full execution details.
See `tools/scripts/` for Semrush API Python scripts.
See `templates/` for article templates.
