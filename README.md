# indie-site-playbook — B2B SaaS Affiliate Site Builder

A complete, AI-executable playbook for building B2B SaaS affiliate review sites from zero to $2,000–$3,000/month.

Everything in this repo is derived from real execution: 4 live sites, verified affiliate income, and a documented path from niche selection through content, launch, backlinks, and monetization.

---

## What This Is

A Claude Code skill that guides you (or your AI agent) through every phase of building a B2B SaaS affiliate review site:

| Phase | What You Do | Output |
|-------|-------------|--------|
| 0 | Set revenue goals, define selection criteria | Scoring thresholds |
| 1 | Research 300–600 niche candidates across platforms | Ranked direction list |
| 2 | Build the site (Astro + Cloudflare Pages + monorepo) | Live site |
| 3 | Plan and write content (best X, alternatives, vs, reviews) | 20 published articles |
| 4 | Set up affiliate programs and monetization | Affiliate links live |
| 5 | Launch on Product Hunt, SaaSHub, directories | Backlinks + traffic |
| 6 | Build backlinks (free DR80–95 sources) | Domain authority |
| 7 | Operate and scale | Revenue growth |

## Target Outcome

- **M3**: Site live, 20 articles published, first affiliate clicks
- **M6**: 5,000–8,000 monthly sessions, first $200–$500/month
- **M12**: 15,000–22,000 monthly sessions, $2,000–$3,000/month

## Who This Is For

- Indie developers and creators building content sites
- Anyone who wants a systematic, data-driven approach to SaaS affiliate sites
- AI agents executing the full workflow autonomously

## How to Use

### With Claude Code

Add this skill to your Claude Code setup:

```bash
# Clone this repo
git clone https://github.com/YOUR_USERNAME/indie-site-playbook.git

# Copy the skill to your Claude config
cp indie-site-playbook/.claude/skills/indie-site-playbook.md ~/.claude/skills/
```

Then in Claude Code, invoke with:
```
/indie-site-playbook
```

### Manual Use

Read the phase files in order:
1. `phases/00-goal-setting.md`
2. `phases/01-niche-research.md`
3. `phases/02-tech-stack-setup.md`
4. `phases/03-content-creation.md`
5. `phases/04-affiliate-monetization.md`
6. `phases/05-launch-promotion.md`
7. `phases/06-backlink-building.md`
8. `phases/07-ongoing-operations.md`

---

## Tech Stack Used in Production

- **Framework**: Astro 5.x
- **Deployment**: Cloudflare Pages (free tier, 500 builds/month)
- **Structure**: pnpm monorepo (shared UI + content-utils packages)
- **Styling**: Tailwind CSS
- **Analytics**: Microsoft Clarity (free heatmaps + session recordings)
- **Schema**: JSON-LD (Organization, WebSite, Person)

## Real Sites Built With This Playbook

| Site | Niche | Status |
|------|-------|--------|
| hrpaypick.com | HR & Payroll Software | Live |
| cashflowpick.com | AP Automation & Expense Software | Live |
| commsadvisor.com | Help Desk & Communication Tools | Live |
| chinaabroadguide.com | China Business Abroad (ZH) | Live |

---

## License

MIT — use freely, fork it, build your own sites.
