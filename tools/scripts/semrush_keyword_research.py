"""
Semrush Keyword Research Scripts for B2B SaaS Affiliate Site Niche Research

Usage:
  pip install requests pandas scikit-learn

  Set SEMRUSH_API_KEY in environment or directly in the script.

  Key note: Use 'phrase_all' for keyword overview (NOT 'phrase_this' —
  phrase_this returns SV=0 for all keywords).
"""

import os
import requests
import pandas as pd
import time
from typing import Optional

SEMRUSH_API_KEY = os.getenv("SEMRUSH_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.semrush.com"


# ============================================================
# 1. KEYWORD OVERVIEW (SV, CPC, KD for a list of keywords)
# ============================================================

def get_keyword_overview(keywords: list[str], database: str = "us") -> pd.DataFrame:
    """
    Get SV, CPC, KD for a list of keywords.

    IMPORTANT: Must use phrase_all, not phrase_this.
    phrase_this returns SV=0 for all keywords (confirmed bug).
    """
    results = []
    for kw in keywords:
        params = {
            "type": "phrase_all",   # ← CRITICAL: use phrase_all
            "key": SEMRUSH_API_KEY,
            "phrase": kw,
            "export_columns": "Ph,Nq,Cp,Co,Kd,Nr",
            "database": database
        }
        resp = requests.get(BASE_URL, params=params)
        if resp.status_code == 200 and resp.text:
            lines = resp.text.strip().split("\n")
            if len(lines) > 1:
                row = lines[1].split(";")
                if len(row) >= 5:
                    results.append({
                        "keyword": row[0],
                        "sv": int(row[1]) if row[1].isdigit() else 0,
                        "cpc": float(row[2]) if row[2] else 0,
                        "competition": float(row[3]) if row[3] else 0,
                        "kd": float(row[4]) if row[4] else 99,
                        "results": int(row[5]) if len(row) > 5 and row[5].isdigit() else 0,
                    })
        time.sleep(0.5)  # Rate limiting

    return pd.DataFrame(results)


# ============================================================
# 2. RELATED KEYWORDS (Expand from seed keyword)
# ============================================================

def get_related_keywords(
    seed_keyword: str,
    database: str = "us",
    limit: int = 500,
    min_sv: int = 100,
    max_kd: int = 30,
    min_cpc: float = 1.0
) -> pd.DataFrame:
    """
    Get related keywords from a seed with filters applied.
    Used in Phase 1 to expand seed buckets.
    """
    params = {
        "type": "phrase_related",
        "key": SEMRUSH_API_KEY,
        "phrase": seed_keyword,
        "export_columns": "Ph,Nq,Cp,Co,Kd",
        "database": database,
        "display_limit": limit,
        "display_filter": f"+|Vol|Gt|{min_sv}+|Cp|Gt|{min_cpc}",
        "display_sort": "nq_desc"
    }

    resp = requests.get(BASE_URL, params=params)
    results = []

    if resp.status_code == 200 and resp.text:
        lines = resp.text.strip().split("\n")[1:]  # Skip header
        for line in lines:
            row = line.split(";")
            if len(row) >= 5:
                kd = float(row[4]) if row[4] else 99
                if kd <= max_kd:  # Apply KD filter
                    results.append({
                        "keyword": row[0],
                        "sv": int(row[1]) if row[1].isdigit() else 0,
                        "cpc": float(row[2]) if row[2] else 0,
                        "kd": kd,
                        "seed": seed_keyword,
                    })

    return pd.DataFrame(results)


# ============================================================
# 3. BATCH SEED EXPANSION (Phase 1 Main Function)
# ============================================================

TIER_1_SEEDS = [
    "gusto alternatives",
    "quickbooks alternatives",
    "clio alternatives",
    "zendesk alternatives",
    "workable alternatives",
    "docusign alternatives",
    "clickup alternatives",
    "1password alternatives",
    "hootsuite alternatives",
    "shopify alternatives",
]

TIER_2_SEEDS = [
    "ai customer service tools",
    "ai recruiting software",
    "ai legal software",
    "ai bookkeeping software",
    "surfer seo alternatives",
    "apollo.io alternatives",
    "ai marketing tools",
    "ai analytics tools",
]

TIER_3_SEEDS = [
    "best shopify apps for",
    "hubspot alternatives for",
    "salesforce alternatives small business",
    "notion alternatives",
    "figma alternatives",
    "zapier for",
    "project management software comparison",
    "crm software for small business",
]


def run_phase1_keyword_discovery(
    seeds: Optional[list[str]] = None,
    output_file: str = "phase1_raw_keywords.csv"
) -> pd.DataFrame:
    """
    Run Phase 1 keyword discovery across all seed buckets.
    Estimates ~2,000–5,000 Semrush API units.
    """
    if seeds is None:
        seeds = TIER_1_SEEDS + TIER_2_SEEDS + TIER_3_SEEDS

    all_keywords = pd.DataFrame()

    for i, seed in enumerate(seeds):
        print(f"[{i+1}/{len(seeds)}] Processing seed: '{seed}'")
        df = get_related_keywords(seed, limit=500, min_sv=100, max_kd=35, min_cpc=1.0)
        all_keywords = pd.concat([all_keywords, df], ignore_index=True)
        print(f"  → Found {len(df)} keywords")
        time.sleep(1)

    # Deduplicate
    all_keywords = all_keywords.drop_duplicates(subset=["keyword"])
    print(f"\nTotal unique keywords: {len(all_keywords)}")

    all_keywords.to_csv(output_file, index=False)
    print(f"Saved to {output_file}")

    return all_keywords


# ============================================================
# 4. DOMAIN ORGANIC KEYWORDS (Competitor Analysis)
# ============================================================

def get_competitor_keywords(
    domain: str,
    database: str = "us",
    limit: int = 100
) -> pd.DataFrame:
    """
    Get top organic keywords for a competitor domain.
    Used in Phase 1 Source G (competitor reverse discovery).
    """
    params = {
        "type": "domain_organic",
        "key": SEMRUSH_API_KEY,
        "domain": domain,
        "database": database,
        "display_limit": limit,
        "display_sort": "tr_desc",
        "export_columns": "Ph,Po,Pp,Pd,Nq,Cp,Ur,Tr,Tc,Co,Kd,Vu,Vd",
    }

    resp = requests.get(BASE_URL, params=params)
    results = []

    if resp.status_code == 200 and resp.text:
        lines = resp.text.strip().split("\n")[1:]
        for line in lines:
            row = line.split(";")
            if len(row) >= 6:
                results.append({
                    "keyword": row[0],
                    "position": int(row[1]) if row[1].isdigit() else 0,
                    "prev_position": int(row[2]) if row[2].isdigit() else 0,
                    "sv": int(row[4]) if row[4].isdigit() else 0,
                    "cpc": float(row[5]) if row[5] else 0,
                    "url": row[6] if len(row) > 6 else "",
                    "domain": domain,
                })

    return pd.DataFrame(results)


# ============================================================
# 5. CLUSTER SCORING (Phase 3)
# ============================================================

def score_keyword_cluster(df: pd.DataFrame, cluster_name: str) -> dict:
    """
    Score a cluster of keywords using the Phase 4 methodology.
    Input: DataFrame with columns: keyword, sv, cpc, kd
    """
    if df.empty:
        return {}

    total_sv = df["sv"].sum()
    avg_kd = df["kd"].mean()
    avg_cpc = df["cpc"].mean()
    low_kd_count = len(df[df["kd"] <= 20])
    kw_count = len(df)

    # Commercial keyword count
    commercial_patterns = ["best", "review", "vs", "alternative", "pricing", "cost", "cheap"]
    commercial_mask = df["keyword"].str.contains("|".join(commercial_patterns), case=False, na=False)
    commercial_count = commercial_mask.sum()

    # Opportunity score (higher = better opportunity)
    opportunity_score = (
        (avg_cpc * 3) +           # CPC weighted highest
        (total_sv / 5000) +       # Volume
        (25 - avg_kd) +           # Lower KD = better
        (low_kd_count * 0.5)      # More low-KD words = better
    ) * kw_count / 10

    top_keywords = df.nlargest(5, "sv")["keyword"].tolist()

    return {
        "cluster_name": cluster_name,
        "total_sv": total_sv,
        "avg_kd": round(avg_kd, 1),
        "avg_cpc": round(avg_cpc, 2),
        "low_kd_count": low_kd_count,
        "keyword_count": kw_count,
        "commercial_kw_count": int(commercial_count),
        "opportunity_score": round(opportunity_score, 1),
        "top_keywords": ", ".join(top_keywords),
        "passes_floor": (
            total_sv >= 150000 and
            avg_kd <= 30 and
            avg_cpc >= 3.0 and
            low_kd_count >= 15
        )
    }


# ============================================================
# 6. REVENUE ESTIMATOR
# ============================================================

def estimate_revenue(
    cluster_total_sv: int,
    avg_commission_usd: float,
    traffic_share: float = 0.05,
    ctr_to_affiliate: float = 0.10,
    conversion_rate: float = 0.015
) -> dict:
    """
    Estimate monthly affiliate revenue from a cluster.

    Default assumptions (conservative new site):
    - Traffic share: 5% of cluster SV
    - CTR to affiliate: 10% of sessions
    - Conversion rate: 1.5% of affiliate clicks
    """
    monthly_sessions = cluster_total_sv * traffic_share
    affiliate_clicks = monthly_sessions * ctr_to_affiliate
    conversions = affiliate_clicks * conversion_rate
    monthly_revenue = conversions * avg_commission_usd

    return {
        "monthly_sessions": round(monthly_sessions),
        "affiliate_clicks": round(affiliate_clicks),
        "conversions": round(conversions, 1),
        "monthly_revenue_usd": round(monthly_revenue),
        "time_to_2k_months": round(2000 / monthly_revenue) if monthly_revenue > 0 else "N/A",
    }


# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":
    # Example 1: Get keyword data for specific terms
    keywords = [
        "best payroll software",
        "gusto alternatives",
        "rippling vs gusto",
    ]
    df = get_keyword_overview(keywords)
    print(df.to_string())

    # Example 2: Expand from seed (Phase 1)
    # df = run_phase1_keyword_discovery(seeds=TIER_1_SEEDS[:3])

    # Example 3: Revenue estimate
    result = estimate_revenue(
        cluster_total_sv=300000,
        avg_commission_usd=80,
    )
    print(f"\nRevenue estimate for SV=300K cluster:")
    for k, v in result.items():
        print(f"  {k}: {v}")
