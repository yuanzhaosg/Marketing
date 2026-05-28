# Phase 4: Affiliate & Monetization Setup

> **Goal**: Join affiliate programs for the top tools in your niche, set up tracking, and configure all revenue paths before traffic arrives.
> **Duration**: 3–5 days (parallel with content writing)

---

## 4.1 Where to Find Affiliate Programs

### Primary Sources (check in order)

1. **PartnerStack** — [partnerstack.com/marketplace](https://partnerstack.com/marketplace)
   - Most B2B SaaS companies use PartnerStack
   - Easy application, fast approval for established niches
   - Handles payments automatically

2. **Impact.com** — [app.impact.com/marketplace](https://app.impact.com/marketplace)
   - Enterprise SaaS tools often use Impact
   - Higher payouts, longer cookie windows

3. **ShareASale** — [shareasale.com](https://shareasale.com)
   - Older platform, still has many B2B tools
   - Good for tools that aren't on PartnerStack/Impact

4. **Direct affiliate pages** — Check each tool's website footer
   - Look for: "Affiliate", "Partners", "Referral Program"
   - Many high-payout programs are direct (Wise, Stripe, etc.)

5. **Google search** — `[tool name] affiliate program commission`

---

## 4.2 What to Look For in an Affiliate Program

### Green Flags

```
✅ Recurring commission (20%+ of monthly subscription)
✅ Long cookie window (90+ days)
✅ Net-30 or Net-60 payment terms
✅ No minimum payout (or low minimum: $25–50)
✅ Real-time dashboard with click + conversion data
✅ Dedicated affiliate manager contact
✅ Product has good G2/Capterra ratings (you'll actually recommend it)
```

### Red Flags

```
❌ One-time commission only on low-ticket products (<$50)
❌ 7-day cookie window or less
❌ "Commission by negotiation" (often means low payout)
❌ No tracking dashboard
❌ Product has poor reviews (your trust = your asset)
❌ Requires approval but never responds
```

### Target Commission Economics

| Niche | Typical Tool Price | Recurring Rate | Avg Monthly Commission |
|-------|-------------------|----------------|----------------------|
| HR/Payroll | $100–500/mo | 20–30% | $20–150/mo per referral |
| Legal Tech | $500–1000/mo | 20–25% | $100–250/mo per referral |
| Help Desk | $100–400/mo | 20–30% | $20–120/mo per referral |
| AP Automation | $200–800/mo | 15–25% | $30–200/mo per referral |
| Accounting SaaS | $30–200/mo | 20–30% | $6–60/mo per referral |

---

## 4.3 Applying to Programs

### Application Checklist

Before applying, make sure your site has:
- [ ] At least 5 published articles
- [ ] Professional design (not a blank template)
- [ ] About page explaining who you are
- [ ] Contact page with real email
- [ ] Affiliate disclosure page

### Application Message Template

```
Subject: Affiliate Partnership Application — [Your Site Name]

Hi [Name],

I run [yoursite.com], an independent review site focused on [category] software 
for [target audience]. We publish detailed, unbiased comparisons — no sponsored 
rankings.

Our readers are [job title] at [company size] companies actively evaluating 
[category] solutions. We've been live for [X months] and currently publish 
[X] new articles per month.

I'd love to feature [Tool Name] as a recommended option in our comparisons 
and guide our readers to your product when it's the right fit.

Can I join your affiliate program?

[Your name]
[yoursite.com]
```

---

## 4.4 UTM Tracking Setup

Track every affiliate click so you know which content converts.

### URL Structure

```
https://[tool].com/?utm_source=[yoursite]&utm_medium=affiliate&utm_campaign=[article-slug]

Example:
https://gusto.com/signup?utm_source=hrpaypick&utm_medium=affiliate&utm_campaign=gusto-alternatives

For PartnerStack links, they handle tracking — just note which article the link is in.
```

### Creating a Centralized Link File

Keep all affiliate links in one place for easy updating:

```typescript
// src/data/affiliateLinks.ts
export const affiliateLinks = {
  gusto: {
    main: 'https://gusto.com/partner/hrpaypick',
    signup: 'https://gusto.com/signup?ref=hrpaypick',
    pricing: 'https://gusto.com/pricing?ref=hrpaypick',
  },
  rippling: {
    main: 'https://www.rippling.com/?utm_source=hrpaypick',
  },
  // ... etc
} as const;
```

This way if a link changes, you update it in one place.

---

## 4.5 CTA Component

### src/components/AffiliateButton.astro

```astro
---
interface Props {
  href: string;
  label: string;
  variant?: 'primary' | 'secondary';
  small?: boolean;
}

const { href, label, variant = 'primary', small = false } = Astro.props;
---

<a
  href={href}
  target="_blank"
  rel="noopener noreferrer nofollow"
  class={`
    inline-flex items-center gap-2 font-semibold rounded-lg transition-colors
    ${variant === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-700' : 'border border-blue-600 text-blue-600 hover:bg-blue-50'}
    ${small ? 'px-4 py-2 text-sm' : 'px-6 py-3 text-base'}
  `}
>
  {label}
  <span aria-hidden="true">→</span>
</a>
```

### Usage in articles

```astro
import AffiliateButton from '../components/AffiliateButton.astro';
import { affiliateLinks } from '../data/affiliateLinks';

<AffiliateButton 
  href={affiliateLinks.gusto.main} 
  label="Try Gusto free for 30 days" 
/>
```

---

## 4.6 Affiliate Disclosure

Required by FTC guidelines in the US. Add to every article:

```markdown
**Disclosure**: This article contains affiliate links. If you purchase through 
our links, we may earn a commission at no extra cost to you. We only recommend 
tools we've genuinely evaluated.
```

Place it:
- At the top of every review/comparison article
- In your site footer
- On a dedicated `/affiliate-disclosure/` page

---

## 4.7 Revenue Dashboard

Track these numbers weekly:

| Metric | Where to Find It |
|--------|-----------------|
| Affiliate clicks | PartnerStack / Impact dashboard |
| Conversions | PartnerStack / Impact dashboard |
| Revenue this month | PartnerStack / Impact dashboard |
| Revenue per article | Link each CTA to specific campaign |
| Top earning articles | Compare campaign revenue in dashboards |
| Conversion rate by article | Conversions ÷ clicks per campaign |

### Spreadsheet Template

```
Date | Article | Clicks | Conversions | Revenue | CVR | Notes
2026-01-15 | gusto-alternatives | 45 | 2 | $180 | 4.4% | Ranked #7
2026-01-15 | best-payroll-software | 120 | 3 | $240 | 2.5% | Ranked #12
```

---

## 4.8 Diversification Strategy

Don't rely on one affiliate program. Aim for:

- **3–5 programs per niche** minimum
- At least one backup option for each tool you recommend
- Mix of price points (one $30/mo tool, one $200/mo tool)
- Mix of commission structures (pure recurring + some higher one-time)

If one program cuts commissions or closes, you still have income.

---

## 4.9 Phase 4 Checklist

- [ ] PartnerStack account created
- [ ] Impact.com account created
- [ ] Applied to top 10 programs in your niche
- [ ] At least 5 programs approved
- [ ] affiliateLinks.ts file created with all links
- [ ] AffiliateButton component built and working
- [ ] UTM parameters added to all affiliate links
- [ ] Affiliate disclosure on all articles and footer
- [ ] Revenue dashboard set up (spreadsheet or Notion)

→ **Ready for Phase 5: Launch & Promotion**
