# Income Scenarios

> **Purpose:** Show best, likely and worst income for days 1 to 30 and 31 to 90 with stated assumptions and arithmetic you can redo, and give a plan for results below the worst case.  
> **Use when:** At the Day 30 retro, and whenever someone tells you a number that sounds too good.  
> **Time needed:** 45 minutes.  
> **Needs:** The chosen route from 03-parallel-routes.md and your own prices.  
> **Cost:** $0

## Inputs

- [COUNTRY], [NICHE], [WEEKLY_HOURS]
- The route you chose in [03-parallel-routes.md](03-parallel-routes.md)
- Your tracking sheet from [../09-operations/03-tracking-sheet.md](../09-operations/03-tracking-sheet.md)

## Steps

### 1. Read these scenarios as arithmetic, not forecasts

Every figure below is an illustration built from assumptions I state. None of it is a benchmark, a statistic or a promise. All amounts are in US dollars for illustration. Replace each assumption with your own price and your own rates before you rely on any total. The worst case is $0, and it is a real outcome.

### 2. Assumptions (replace every one)

| Item | Assumption used below | Why it is only an assumption |
|---|---|---|
| Service job price | $25 per job | Your skill and local rates differ |
| Digital product price | $5 per sale | Your product and market differ |
| Product fees | 5% platform fee + 2.9% processing + $0.30 per sale | Secondary sources report these for free plans. VERIFY BEFORE RELYING on each platform's pricing page. |
| Affiliate commission | $3 per sale | Programs set their own rates |
| One small sponsorship | $50 once, only in the best case for days 31 to 90 | Brands rarely pay small channels |
| YouTube ad or fan-funding income | $0 until YPP approval | Approval needs thresholds plus roughly one month of review (see [01-reality-and-timeline-math.md](01-reality-and-timeline-math.md)) |
| Cost of running the plan | $0 | All tools in this repo are free |

Net product income for n sales at price P = n × P − (n × P × 0.05) − (n × P × 0.029) − (n × 0.30).

### 3. Days 1 to 30

| Line | Worst | Likely | Best |
|---|---|---|---|
| Service jobs | 0 | 1 | 3 |
| Service income | 0 × $25 = $0 | 1 × $25 = $25 | 3 × $25 = $75 |
| Product sales | 0 | 2 | 6 |
| Product gross | $0 | 2 × $5 = $10 | 6 × $5 = $30 |
| Product fees | $0 | $0.50 + $0.29 + $0.60 = $1.39 | $1.50 + $0.87 + $1.80 = $4.17 |
| Product net | $0 | $10 − $1.39 = $8.61 | $30 − $4.17 = $25.83 |
| Affiliate sales | 0 | 0 | 2 |
| Affiliate income | $0 | $0 | 2 × $3 = $6 |
| Sponsorship | $0 | $0 | $0 |
| YouTube-paid income | $0 | $0 | $0 |
| **Total, days 1 to 30** | **$0** | **$25 + $8.61 = $33.61** | **$75 + $25.83 + $6 = $106.83** |

### 4. Days 31 to 90

| Line | Worst | Likely | Best |
|---|---|---|---|
| Service jobs | 0 | 4 | 6 |
| Service income | $0 | 4 × $25 = $100 | 6 × $25 = $150 |
| Product sales | 0 | 8 | 20 |
| Product gross | $0 | 8 × $5 = $40 | 20 × $5 = $100 |
| Product fees | $0 | $2.00 + $1.16 + $2.40 = $5.56 | $5.00 + $2.90 + $6.00 = $13.90 |
| Product net | $0 | $40 − $5.56 = $34.44 | $100 − $13.90 = $86.10 |
| Affiliate sales | 0 | 5 | 15 |
| Affiliate income | $0 | 5 × $3 = $15 | 15 × $3 = $45 |
| Sponsorship | $0 | $0 | $50 |
| YouTube-paid income | $0 | $0 | $0 |
| **Total, days 31 to 90** | **$0** | **$100 + $34.44 + $15 = $149.44** | **$150 + $86.10 + $45 + $50 = $331.10** |
| **Cumulative, days 1 to 90** | **$0** | **$33.61 + $149.44 = $183.05** | **$106.83 + $331.10 = $437.93** |

The totals are small on purpose. A channel with no audience does not earn much in 90 days, and the plan's value is in what it builds: a skill sample, an offer, a list and a growing view count.

### 5. Why YouTube-paid income is $0 through day 90, even in the best case

Take a best-case channel that averages 500 views per day from day 1 at a 4-minute average view duration (a stretch for a new channel).

- Hours per day = 500 × 4 ÷ 60 = 33.3 hours.
- Tier 1 hours (3,000): 3,000 ÷ 33.3 = 90 days. Fan funding cannot start until after approval, which adds roughly one month of review (verified 2026-10-21: review takes about a month). That places first fan-funding income after day 120, and only if you also meet the subscriber and upload conditions and your country supports the feature.
- Ad-revenue path under the bar for applications from 1 Feb 2027 (8,000 hours): 8,000 ÷ 33.3 = 240 days, plus about 30 days of review, so approval near day 270.
- First ad payment: if RPM is $2, reaching a $100 balance needs $100 ÷ $2 × 1,000 = 50,000 monetized views, which is 100 days at 500 views per day. That is day 370, then up to 30 days to the month end, then a 21-day processing period (verified 2026-10-21, support.google.com/adsense/answer/65090), which puts the first ad payment between about day 391 and day 421.
- A channel that started today and somehow reached 4,000 hours by 31 Jan 2027 (102 days) would need 588 views per day from day 1 (see the timeline file). Its first payment would still be months away.

Do the same arithmetic with your own daily views, your own average view duration and your own RPM.

### 6. Redo the arithmetic yourself

Spreadsheet columns: Line, Count, Unit price, Gross, Fees, Net. For each row:

- Gross = count × unit price.
- Fees for products = gross × 0.05 + gross × 0.029 + count × 0.30. Fees for services and affiliate income = $0 unless your payment platform charges more (check).
- Net = gross − fees.
- Scenario total = sum of the Net column.
- Hourly rate = scenario total ÷ hours you spent on that route (from your tracking sheet). Compare it with what the same hours would earn elsewhere.

### 7. If results are below the worst case

"Below the worst case" means any of these at Day 30: you published fewer than half your quota, a video got a policy warning, you spent money, or your parallel route got zero replies or zero page views. Follow this plan.

Step A (Days 31 to 34): find the failed stage. Check each in order and stop at the first one that fails.

| Stage | Symptom | Fix, with the file to use |
|---|---|---|
| Output | Fewer than half the planned videos published | Cut the quota one band, keep the gate. [02-30-day-plan.md](02-30-day-plan.md) |
| Distribution | Impressions near zero after 7 days | Check titles, the first 30 seconds and topic demand. [../02-long-form/05-metadata-and-seo.md](../02-long-form/05-metadata-and-seo.md) |
| Packaging | Impressions present, CTR below 75% of your median | Redesign thumbnails and titles. [04-growth-levers-and-kpis.md](04-growth-levers-and-kpis.md) |
| Retention | Viewers leave in the first 30 seconds | Rewrite the hook. P-LONG-05 in [../02-long-form/02-script-prompt-chain.md](../02-long-form/02-script-prompt-chain.md) |
| Offer | Views exist, nobody clicks or buys | Ask 5 viewers what they wanted. Change the offer, not the video. [03-parallel-routes.md](03-parallel-routes.md) |
| Compliance | A warning, a label or a claim | Stop uploading, follow [06-mistakes-to-avoid.md](06-mistakes-to-avoid.md) |

Step B (Days 35 to 41): change one thing, the one from Step A. Do not change anything else.

Step C (Days 42 to 45): re-measure with the same metrics. If the failed stage improved, keep going. If it did not, move to the next stage in the table.

Step D: spend nothing. The plan costs $0, and it stays at $0 even when results are poor.

Step E: at day 90, apply the "Pivot the concept" rule from the KPI file before you decide anything larger.

## Prompts

### P-MONEY-05 — Scenarios from my own assumptions

Purpose: Build best, likely and worst income tables for your route with your own numbers, and an honest YouTube-paid timeline.

Inputs: [COUNTRY], [NICHE], [WEEKLY_HOURS]; [ROUTE] (the route you chose); [SERVICE_PRICE], [PRODUCT_PRICE], [AFFILIATE_COMMISSION] (your prices in your currency, or "none"); [FEE_RULE] (platform and payment fees you pay, or "unknown"); [AVG_DAILY_VIEWS_ASSUMED] (daily long-form views you assume); [AVG_VIEW_DURATION_MIN]; [RPM_ASSUMED] (revenue per 1,000 views, or "unknown").

```
You are a careful financial-arithmetic assistant. You do not promise income. You show every calculation line by line. You do not invent prices, rates, fees or benchmarks; use only the numbers I give you. If a number is "unknown", write VERIFY BEFORE RELYING and tell me where to find it.

My facts:
- Country: [COUNTRY]
- Niche: [NICHE]
- Weekly hours: [WEEKLY_HOURS]
- Route I chose: [ROUTE]
- Service price: [SERVICE_PRICE]
- Product price: [PRODUCT_PRICE]
- Affiliate commission per sale: [AFFILIATE_COMMISSION]
- Fee rule: [FEE_RULE]
- Assumed average daily long-form views: [AVG_DAILY_VIEWS_ASSUMED]
- Average view duration in minutes: [AVG_VIEW_DURATION_MIN]
- RPM: [RPM_ASSUMED]

Task 1. Build a table for days 1 to 30 with columns Worst, Likely, Best and rows: count of units sold or jobs done, gross, fees, net, total. Make the worst column zero in every row. Choose counts that need no more hours than [WEEKLY_HOURS] allow and state the hours used.
Task 2. Build the same table for days 31 to 90 and a cumulative day 1 to 90 row.
Task 3. Using [AVG_DAILY_VIEWS_ASSUMED] and [AVG_VIEW_DURATION_MIN], compute the date in days from today when I would reach 3,000, 4,000 and 8,000 watch hours, then add about 30 days of review, and then compute the days until a first ad payment: balance needed = payment threshold; views needed = threshold / RPM x 1,000; days = views needed / daily views; then add up to 30 days to month end and 21 days processing. Mark any step that depends on a policy as VERIFY BEFORE RELYING if you cannot confirm it from an official page.
Task 4. State, in plain words, which row of each table I control directly and which depends on other people.

Output: three tables, the arithmetic under each, a list of VERIFY BEFORE RELYING items, and no sentence that predicts I will earn a specific amount.
```

Expected output: Two scenario tables with visible arithmetic, a day-count timeline for YouTube-paid income, and a list of unverified items.

If the output is weak: Reply "Show every multiplication and subtraction on its own line and recompute the totals from those lines."

## Done when

- You have your own worst, likely and best totals for days 1 to 30 and 31 to 90, with the arithmetic in your tracking sheet.
- You can say, with a number, when your first YouTube-paid money could arrive and why.
- At Day 30 you know whether you are at or below the worst case, and you have the matching next step.

## Next

[06-mistakes-to-avoid.md](06-mistakes-to-avoid.md)
