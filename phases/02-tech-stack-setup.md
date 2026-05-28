# Phase 2: Tech Stack Setup

> **Goal**: Get a production-ready site live on Cloudflare Pages, with SEO infrastructure, analytics, and schema markup all working before publishing the first article.
> **Duration**: 2–4 days
> **Output**: Live deployed site at your domain

---

## 2.1 Tech Stack Decisions

### Why Astro

- **Static output** by default — fast, no server costs
- **SEO-friendly** — full control over `<head>`, schema, canonical tags
- **Component-based** — write once, reuse across pages
- **Partial hydration** — only load JS where needed
- **Content Collections** — type-safe content management built in

### Why Cloudflare Pages

- **Free tier**: 500 builds/month, unlimited bandwidth, unlimited sites
- **Global CDN**: fast everywhere
- **Custom domains**: free SSL, easy DNS management
- **Preview deployments**: every git push gets a preview URL

### Why Monorepo (If Running Multiple Sites)

- One codebase change = all sites updated simultaneously
- Shared UI components (header, footer, CTA buttons, review cards)
- Shared SEO infrastructure (one bug fix = fixed everywhere)
- Shared TypeScript types for content
- Lower total maintenance burden

---

## 2.2 Single Site Setup

### Prerequisites

```bash
# Install pnpm
npm install -g pnpm

# Node.js 18+ required
node --version
```

### Create Astro Project

```bash
pnpm create astro@latest my-site
# Choose: Empty project
# TypeScript: Yes (strict)
# Git: Yes

cd my-site
pnpm add @astrojs/tailwind @astrojs/sitemap
pnpm add -D tailwindcss
```

### Essential File Structure

```
my-site/
├── src/
│   ├── components/
│   │   ├── SEOHead.astro          # Meta tags, OG, canonical
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── CTA.astro              # Affiliate CTA button
│   │   ├── ReviewCard.astro       # Software review card
│   │   └── ComparisonTable.astro
│   ├── layouts/
│   │   ├── BaseLayout.astro       # HTML shell with <head>
│   │   ├── ArticleLayout.astro    # Blog/review layout
│   │   └── HomeLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── about.astro
│   │   └── [category]/
│   │       └── [slug].astro
│   ├── content/
│   │   ├── config.ts              # Content collection schemas
│   │   └── articles/
│   │       └── *.md               # Your articles
│   └── site.config.ts             # Site-wide configuration
├── public/
│   ├── favicon.svg
│   └── robots.txt
├── astro.config.mjs
└── package.json
```

---

## 2.3 Monorepo Setup (Multiple Sites)

### Root package.json

```json
{
  "name": "my-sites",
  "private": true,
  "scripts": {
    "dev:site-a": "pnpm --filter site-a dev",
    "dev:site-b": "pnpm --filter site-b dev",
    "build:all": "pnpm --filter './apps/*' build"
  }
}
```

### pnpm-workspace.yaml

```yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

### Directory Structure

```
my-sites/
├── apps/
│   ├── site-a/                    # hrpaypick.com
│   │   ├── src/
│   │   │   └── site.config.ts
│   │   ├── astro.config.mjs
│   │   └── package.json
│   ├── site-b/                    # cashflowpick.com
│   └── site-c/                    # commsadvisor.com
├── packages/
│   ├── ui/                        # Shared components
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── layouts/
│   │   │   │   └── BaseLayout.astro
│   │   │   └── index.ts
│   │   └── package.json
│   └── content-utils/             # Shared types
│       ├── src/
│       │   └── index.ts
│       └── package.json
└── package.json
```

### packages/content-utils/src/index.ts

```typescript
export interface OrganizationConfig {
  name: string;
  url: string;
  logo?: string;
}

export interface PersonConfig {
  name: string;
  url: string;
  jobTitle?: string;
}

export interface SiteConfig {
  lang: string;
  title: string;
  description: string;
  organization: OrganizationConfig;
  person?: PersonConfig;
  /** Microsoft Clarity project ID */
  clarityId?: string;
}
```

### packages/ui/src/layouts/BaseLayout.astro

```astro
---
import SEOHead from '../components/SEOHead.astro';
import type { SiteConfig } from '@mysite/content-utils';

interface Props {
  title: string;
  description: string;
  siteConfig: SiteConfig;
  ogImage?: string;
}

const { title, description, siteConfig, ogImage } = Astro.props;
---

<!doctype html>
<html lang={siteConfig.lang}>
  <head>
    <SEOHead title={title} description={description} ogImage={ogImage} />
    <!-- Microsoft Clarity -->
    {siteConfig.clarityId && (
      <script is:inline define:vars={{ clarityId: siteConfig.clarityId }}>
        (function(c,l,a,r,i,t,y){
          c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
          t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
          y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", clarityId);
      </script>
    )}
    <!-- JSON-LD Schema -->
    <script type="application/ld+json" set:html={JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": siteConfig.organization.name,
      "url": siteConfig.organization.url,
    })} />
    <slot name="head" />
  </head>
  <body>
    <slot name="header" />
    <slot />
    <slot name="footer" />
  </body>
</html>
```

---

## 2.4 SEO Head Component

### src/components/SEOHead.astro

```astro
---
interface Props {
  title: string;
  description: string;
  canonical?: string;
  ogImage?: string;
  ogType?: string;
  noindex?: boolean;
}

const {
  title,
  description,
  canonical = Astro.url.href,
  ogImage,
  ogType = 'website',
  noindex = false,
} = Astro.props;

const siteUrl = Astro.site?.toString() ?? '';
---

<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content={description} />
<link rel="canonical" href={canonical} />
{noindex && <meta name="robots" content="noindex, nofollow" />}

<!-- Open Graph -->
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
<meta property="og:type" content={ogType} />
<meta property="og:url" content={canonical} />
{ogImage && <meta property="og:image" content={ogImage.startsWith('http') ? ogImage : `${siteUrl}${ogImage}`} />}

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content={title} />
<meta name="twitter:description" content={description} />
{ogImage && <meta name="twitter:image" content={ogImage.startsWith('http') ? ogImage : `${siteUrl}${ogImage}`} />}

<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
```

---

## 2.5 Site Configuration

### apps/site-a/src/site.config.ts

```typescript
import type { SiteConfig } from '@mysite/content-utils';

export const siteConfig: SiteConfig = {
  lang: 'en',
  title: 'HRPay Pick — HR & Payroll Software Reviews',
  description:
    'Independent guides to payroll and HR software for US small businesses. Unbiased comparisons — no sponsored rankings.',
  organization: {
    name: 'HRPay Pick',
    url: 'https://hrpaypick.com',
    logo: 'https://hrpaypick.com/favicon.svg',
  },
  clarityId: 'YOUR_CLARITY_ID',  // Get from clarity.microsoft.com
};
```

---

## 2.6 Content Collections

### src/content/config.ts

```typescript
import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.date(),
    updatedDate: z.date().optional(),
    author: z.string().default('Editorial Team'),
    category: z.string(),
    tags: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    noindex: z.boolean().default(false),
  }),
});

export const collections = { articles };
```

### src/content/articles/gusto-alternatives.md

```markdown
---
title: "7 Best Gusto Alternatives in 2026 (Cheaper & More Flexible)"
description: "Looking for a Gusto alternative? We tested 12 payroll tools and picked the 7 best. See pricing, pros/cons, and who each is best for."
publishDate: 2026-01-15
category: "Payroll Software"
tags: ["gusto", "alternatives", "payroll"]
---

[article content]
```

---

## 2.7 Cloudflare Pages Deployment

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial site setup"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2: Connect to Cloudflare Pages

1. Log into [dash.cloudflare.com](https://dash.cloudflare.com)
2. Workers & Pages → Create Application → Pages → Connect to Git
3. Select your repository
4. Build settings:
   - **Framework preset**: Astro
   - **Build command**: `pnpm build` (or `cd apps/site-a && pnpm build` for monorepo)
   - **Build output directory**: `dist`
5. Deploy

### Step 3: Add Custom Domain

1. In Cloudflare Pages → your project → Custom domains
2. Add domain → follow DNS instructions
3. SSL is automatic (Let's Encrypt)

### Monorepo Deployment Config

For each site in a monorepo, create a separate Cloudflare Pages project:

```
Site A build command: pnpm --filter site-a build
Site A output:        apps/site-a/dist

Site B build command: pnpm --filter site-b build
Site B output:        apps/site-b/dist
```

---

## 2.8 robots.txt and sitemap.xml

### public/robots.txt

```
User-agent: *
Allow: /

Sitemap: https://yoursite.com/sitemap-index.xml
```

### astro.config.mjs (enable sitemap)

```javascript
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://yoursite.com',
  integrations: [
    tailwind(),
    sitemap(),
  ],
});
```

---

## 2.9 Microsoft Clarity Setup

1. Visit [clarity.microsoft.com](https://clarity.microsoft.com)
2. Create new project → enter your site URL
3. Copy the Project ID (looks like: `pxxxxxxxx` — a short alphanumeric string)
4. Add to your `site.config.ts`:
   ```typescript
   clarityId: 'YOUR_CLARITY_PROJECT_ID',
   ```
5. Clarity script is auto-injected via BaseLayout

**What Clarity gives you (free):**
- Heatmaps (click, scroll, move)
- Session recordings
- Dead clicks and rage clicks
- Scroll depth tracking
- No traffic limits on free plan

---

## 2.10 Phase 2 Checklist

- [ ] Domain registered (Cloudflare Registrar recommended — no markup on renewals)
- [ ] Astro project initialized with Tailwind + Sitemap
- [ ] Site config file created with correct lang, title, description
- [ ] SEO Head component working (title, description, canonical, OG tags)
- [ ] BaseLayout rendering correctly
- [ ] robots.txt in place with sitemap reference
- [ ] Microsoft Clarity ID added and tracking script live
- [ ] Deployed to Cloudflare Pages with custom domain
- [ ] SSL certificate active (https:// working)
- [ ] Google Search Console property added (submit sitemap after first articles)

→ **Ready for Phase 3: Content Creation**
