# Phase 6: Backlink Building

> **Goal**: Reach DR 20+ by Month 6, DR 35+ by Month 12 through systematic link acquisition from free and low-cost sources.
> **Effort**: 2–4 hours per week ongoing
> **Priority**: High — backlinks determine how fast your content ranks

---

## 6.1 The DR Growth Timeline

Realistic expectations for a new site:

| Month | DR Target | Sessions Estimate | Revenue Estimate |
|-------|-----------|------------------|-----------------|
| 1 | 5–10 | 200–500 | $0 |
| 3 | 15–20 | 1,000–2,000 | $50–200 |
| 6 | 25–35 | 5,000–8,000 | $300–800 |
| 9 | 35–45 | 10,000–15,000 | $800–1,500 |
| 12 | 45–55 | 15,000–22,000 | $1,500–3,000 |

DR growth is not linear. It's slow at first (0–20), then accelerates as links compound.

---

## 6.2 Free Tier: DR80+ Links Available Today

These links require no money, can be done in 30 minutes each, and should all be done on or before launch day.

### Notion Published Page (DR 92)

```
1. Create Notion account (free)
2. Create new page with:
   - Title: "[Site Name] — [What It Does]"
   - 2–3 paragraphs describing your site
   - Topics/categories covered
   - Link to your site
   - Links to 3–5 specific articles
3. Click Share → Publish to web
4. Enable: "Allow search engines to index this page"
5. Done. The page is now publicly indexed.
```

This creates a permanent, do-follow link from notion.site (DR 92).

### Product Hunt (DR 91)

Product listing with your site URL in the product website field. Done in Phase 5.

### Crunchbase (DR 91)

```
1. crunchbase.com → Add your company
2. Fill in: company name, description, website, founding date, category
3. Add founder profile
4. Link company to founder profile
```

The website field is do-follow. Takes 15 minutes.

### Stripe Climate (DR 94)

```
1. If you use Stripe for any payments: go to Stripe Dashboard → Climate
2. Enable climate contributions (0.1% of revenue — negligible cost)
3. Stripe adds you to their Climate Badge page, which lists all 
   participating businesses with website links
```

Even at $0 revenue, you can sometimes qualify. Check current eligibility requirements.

### G2 (DR 91)

```
1. g2.com → vendor sign up
2. Create your product profile
3. Add: product name, website, description, category, screenshots, pricing
4. You need 5+ verified reviews to appear in search results
   → Ask customers/users you know to leave reviews
```

The profile page links back to your site.

### Capterra (DR 88)

```
1. vendor.capterra.com → Add your product
2. Similar process to G2
3. Takes 1–2 weeks for approval
```

### AlternativeTo (DR 82)

```
1. alternativeto.net/add-app
2. List your site as an alternative to 3–5 major tools in your niche
3. When someone searches "[Competitor] alternatives" on AT, you appear
```

Double value: backlink + discovery traffic.

### GitHub (DR 96)

```
If your site has any open-source component, tool, or even just the Astro template:
1. Create a public GitHub repository
2. Add README that links to your live site
3. Write a few sentences about what it is
```

Even a simple repository counts. The README link is do-follow.

---

## 6.3 Low-Cost Links (< $30)

### Paid Directories That Are Worth It

| Directory | Cost | DR | Notes |
|-----------|------|-----|-------|
| There Is An AI | Free–$49/yr | 65+ | If AI-adjacent site |
| Futurepedia | Free–$39/yr | 60+ | AI tool listing |
| SaaSManifest | Free | 55 | B2B SaaS directory |
| BetaList Featured | $129 once | 75 | Premium placement |

**Skip paid links from unknown DR30 sites.** They don't move the needle and risk a Google penalty.

### HARO / Source Requests (Free)

HARO (Help a Reporter Out) is now called Connectively. Journalists post requests for expert sources. If you're featured, you get a link from major publications (Forbes, Business Insider, TechCrunch).

```
Process:
1. Sign up at connectively.us (free)
2. Receive daily emails with source requests
3. Respond to requests in your niche (software, business, tech)
4. Tips for good responses:
   - Answer within 2 hours (competition is high)
   - Lead with your expert credential
   - Be specific and quotable
   - Include your site URL and short bio at the bottom
   - Keep under 300 words
```

**Response rate reality**: 1–5% of pitches get featured. Do this consistently over 3 months.

---

## 6.4 Community Link Building

### Reddit Mentions

Reddit (DR 91) links are almost all no-follow, but they drive real referral traffic and signal relevance.

**Strategy**: Become the go-to resource in subreddits relevant to your niche.

1. Create/use Reddit account that's at least 3 months old
2. Spend first 2 weeks just contributing — upvoting, commenting without links
3. Identify the 3–5 questions that come up repeatedly in your subreddits
4. Create articles specifically for those questions
5. When the question appears again, answer it genuinely + link

**Tracking**: Periodically search `site:reddit.com "[yoursite.com]"` to monitor mentions.

### Forum and Community Participation

Find communities where your target audience talks about software:
- Slack communities (many B2B SaaS niches have public Slacks)
- Discord servers
- Facebook groups for [niche] professionals
- LinkedIn groups

Build credibility first, link second. Ratio should be roughly 20:1 (20 helpful contributions for every 1 link).

---

## 6.5 Guest Posting

**Only target sites with:**
- DR > 40
- Real editorial standards (not a link farm)
- Audience overlap with your niche
- Content that gets social engagement

**Finding opportunities:**
```
Google searches:
- "write for us" [your niche] software
- "guest post" [your niche] tools
- "contribute" [your niche] blog
- intitle:"write for us" [category] SaaS
```

**Outreach template:**
```
Subject: Guest Post Idea: [Specific Title Relevant to Their Audience]

Hi [Name],

I've been reading [Site] for a while — particularly enjoyed [specific article].

I write about [your niche] at [yoursite.com] and think your audience would 
benefit from a piece on [topic idea].

Here's a rough outline:
[3–4 bullet points of what the article would cover]

My recent work: [Link to one of your best articles]

Would this be a fit for your editorial calendar?

[Name]
```

Expect 5–10% response rate. Plan for 20+ outreach messages to get 1–2 placements.

---

## 6.6 Link Acquisition via Tools

If you build a useful free tool, it naturally attracts links.

**Tools that work well for B2B SaaS affiliate sites:**

| Tool Idea | Why It Gets Links |
|-----------|-----------------|
| SaaS pricing calculator | Answers a real question, referenced in content |
| Feature comparison table | Journalists and bloggers link to it |
| ROI calculator | "Is [Tool] worth it?" — captures decision stage |
| Market size database | Referenced in industry content |
| Salary calculator | HR sites, media articles |

**Implementation**: Build with Astro + a bit of JavaScript. Free to host on Cloudflare Pages.

---

## 6.7 Chrome Extension Strategy

A Chrome extension (DR 99 from Chrome Web Store) gives you:
1. A DR99 backlink
2. Active users who see your brand
3. An install base for future promotions

**Minimum viable extension ideas for B2B SaaS affiliate sites:**
- Show Trustpilot/G2 rating overlay when browsing SaaS pricing pages
- Quick comparison lookup for tools you review
- Affiliate discount code finder for SaaS tools

**Development cost with AI tools (Claude, Cursor)**: 5–10 hours, $0 cost.

**Publishing**: Google requires a $5 one-time developer fee.

---

## 6.8 Link Building Pipeline (Weekly Routine)

**2 hours per week:**

| Day | Task | Time |
|-----|------|------|
| Monday | Monitor HARO/Connectively, respond to relevant requests | 30 min |
| Wednesday | Find and answer 3 Reddit threads in target subreddits | 30 min |
| Friday | 5 directory submission or outreach messages | 45 min |
| Ongoing | Track new links in Ahrefs (weekly check) | 15 min |

**Monthly:**
- Check competitor new backlinks in Ahrefs (copy their best sources)
- Submit to 5 new niche directories
- Evaluate guest post opportunities

---

## 6.9 Backlink Monitoring

**Free tools:**
- Ahrefs free backlink checker (limited)
- Google Search Console (shows links Google has discovered)
- Moz Link Explorer (free tier)

**What to track:**
```
Monthly metrics:
- Total referring domains (unique linking sites)
- DR (check monthly in Ahrefs)
- New links acquired this month
- Lost links this month
- Top traffic-sending referring domains
```

---

## 6.10 Phase 6 Checklist (Ongoing)

**Day 1 Links (do immediately)**
- [ ] Notion page published with search indexing enabled
- [ ] Product Hunt listing live
- [ ] Crunchbase company profile created
- [ ] G2 product listed
- [ ] Capterra product listed
- [ ] AlternativeTo listing added
- [ ] GitHub repo created (if applicable)

**Month 1**
- [ ] HARO/Connectively account active
- [ ] 3 Reddit threads answered with contextual links
- [ ] 10 directory submissions done
- [ ] SaaSHub approved (submitted at launch, ~30 day approval)

**Month 3**
- [ ] DR 15+ achieved
- [ ] 1 guest post published
- [ ] 20+ Reddit/community mentions
- [ ] Stripe Climate badge acquired

**Month 6**
- [ ] DR 25–35 achieved
- [ ] 50+ referring domains
- [ ] Chrome extension published (optional but high value)
- [ ] Tool page attracting natural links

→ **Ready for Phase 7: Ongoing Operations**
