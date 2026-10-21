# Growth Levers and KPIs

> Purpose: Use policy-safe growth levers, read YouTube Studio analytics correctly, and make double-down or pivot decisions from fixed thresholds.
> Use when: At every weekly review (Days 7, 14, 21, 28) and after every 5 uploads.
> Time needed: 30 minutes per weekly review.
> Needs: YouTube Studio access, the tracking sheet, and the minimum daily views from 01-reality-and-timeline-math.md.
> Cost: $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS]
- Your target threshold and its minimum average daily views (from [01-reality-and-timeline-math.md](01-reality-and-timeline-math.md))
- Tracking sheet from [../09-operations/03-tracking-sheet.md](../09-operations/03-tracking-sheet.md)

## Steps

### 1. Use only policy-safe growth levers

Each lever is something you can do without risking a strike or demonetization. The banned versions are in [06-mistakes-to-avoid.md](06-mistakes-to-avoid.md).

| Lever | Do this | Never do this |
|---|---|---|
| Topic selection | Pick topics from your own comments, from the questions viewers ask under reference channels (public pages only), from YouTube search suggestions, and from the Research tab in YouTube Studio. Score every topic with [../05-originality-layer/02-scoring-rubric.md](../05-originality-layer/02-scoring-rubric.md). | Scrape at scale, or copy another creator's video topic and structure line by line. |
| Packaging (title and thumbnail) | Make one clear promise per video. The first 30 seconds must deliver what the title and thumbnail promise. Use your own thumbnail design (see [../04-thumbnails/03-design-workflow-and-templates.md](../04-thumbnails/03-design-workflow-and-templates.md)). | Mislead with metadata, use a copied thumbnail, or show a scene that is not in the video. |
| Consistency | Publish at your band's quota from [02-30-day-plan.md](02-30-day-plan.md). Keep the same weekly slot so viewers know when to look. | Raise the quota by skipping the pre-publish gate. |
| Series structure | Group related videos in playlists and end each with a pointer to the next one. | Clone the same video template with only the topic word swapped. |
| Community | Reply to every comment in the first 48 hours. Pin one question that invites a specific answer. Use the Community tab when your channel has it. | Buy comments, run comment pods, or reply with copy-pasted text. |
| Comments as research | Read the comments for what viewers did not understand. Make the next video answer it. | Treat a single angry comment as data. |
| Collaborations | Contact channels of similar size in [NICHE]. Offer a concrete idea, such as a joint video, an answer video or a shout-out. | Subscriber-for-subscriber swaps, paid subscriber exchanges, or undisclosed paid shout-outs. |

### 2. Read YouTube Studio analytics

Menu labels in YouTube Studio change. VERIFY BEFORE RELYING on the labels below against what you see on screen. Open YouTube Studio > Analytics and read these in order. Set the date range to "Last 28 days" for channel numbers, and to the video's first 7 days or 28 days for a single video.

1. Overview: Views, Watch time (hours), Subscribers. These are your threshold numbers. Compare watch time with the target hours in the timeline file.
2. Content > select a video > Reach: Impressions, Impressions click-through rate (CTR), and Traffic source types. CTR tells you whether the packaging works. Traffic sources tell you where views come from: Browse features, Suggested videos, YouTube search, Shorts feed and External.
3. Content > select a video > Engagement: Average view duration, Average percentage viewed, and Audience retention. The retention graph shows where viewers leave. A sharp drop in the first 30 seconds is a hook problem. A slow slope is normal. A drop at one moment is a pacing or topic problem at that moment.
4. Audience: Returning viewers versus new viewers and subscribers. A rise in returning viewers shows the series idea works.
5. Research tab: searches viewers make on YouTube, including searches with few matching videos. Use it to pick topics.
6. Shorts rows: "Viewed vs swiped away" and Average percentage viewed. A low viewed rate means the first second does not hold attention.
7. Revenue tab: appears after YPP acceptance. RPM and estimated revenue.

Two reading rules:

- Judge a long-form video at day 7 and day 28, and a Short at day 7. Early numbers change as YouTube tests the video with different viewers.
- Compare against your own channel median, not against other channels. Needing 5 or more uploads before you compute a median.

### 3. Compute the three KPIs that drive decisions

1. Pace ratio = your 28-day average daily views ÷ the minimum average daily views your target needs (from the timeline file). Example: your target is 4,000 hours at a 4-minute average view duration, which needs at least 164 views per day. You average 82 views per day. Pace ratio = 82 ÷ 164 = 0.50.
2. Packaging index = this video's CTR ÷ the median CTR of your last 5 videos with at least 1,000 impressions each.
3. Retention index = this video's average percentage viewed ÷ the median average percentage viewed of your last 5 videos.

The subscriber rate (new subscribers per 1,000 views) is a fourth number to log. Use it to estimate the views you need for 500 or 1,000 subscribers, as shown in the timeline file.

### 4. Apply the thresholds

These thresholds are this repo's operating rules. They come from arithmetic, not from YouTube benchmarks. Change them after 10 uploads if your data supports a different level.

| Decision | Trigger | Action |
|---|---|---|
| Double down on a topic cluster | Two videos in the same cluster each reach at least 125% of your channel median views at day 28 | Make 3 more videos in that cluster. Give each a different angle, structure and hook. Pass each through the originality rubric. |
| Fix packaging | Packaging index below 0.75 on 3 videos in a row, with retention index at 0.9 or above | Redesign titles and thumbnails. Test one thumbnail change at a time per [../04-thumbnails/04-ab-testing-and-safety.md](../04-thumbnails/04-ab-testing-and-safety.md). |
| Fix the hook and pacing | Retention index below 0.8 on 3 videos in a row, with packaging index at 0.9 or above | Rewrite the first 30 seconds with P-LONG-05 and tighten with P-LONG-06. |
| Keep going | Pace ratio between 0.5 and 1.0 and rising for 3 weeks | Hold the quota. Change one thing per week. |
| On pace | Pace ratio 1.0 or higher for 4 weeks | Keep the system. Protect quality. Re-run the timeline file monthly. |
| Pivot a topic cluster | 3 videos in a cluster each at or below 50% of channel median views at day 28 | Stop the cluster. Return to topic selection. |
| Pivot the lane | After 8 weeks at quota, the primary lane's pace ratio is below 0.25 and the other lane's pace ratio is at least double it | Move the main effort to the other lane (long-form or Shorts). |
| Pivot the concept | After 12 weeks and at least 20 uploads, pace ratio is below 0.10 on both lanes and average rubric score is 80 or higher | The problem is positioning. Return to [../05-originality-layer/01-differentiation-method.md](../05-originality-layer/01-differentiation-method.md) and the Style Bible. |
| Fix quality first | Average rubric score below 80, or any gate failure on a published video | Stop adding volume until the score is back to 80 or higher. |

Remember that Shorts views and watch hours do not combine. Do not count one lane toward the other lane's threshold.

### 5. Log the numbers

Write one row per video and one row per week in the tracking sheet. Columns: date, video, format, impressions, CTR, views at 7 days, views at 28 days, average view duration, average percentage viewed, subscribers gained, packaging index, retention index, rubric score, pace ratio, decision.

## Prompts

### P-MONEY-04 — Weekly KPI review

Purpose: Turn your pasted Studio numbers into the decisions in Step 4, with arithmetic.

Inputs: [CHANNEL_NAME], [NICHE]; [TARGET] (the threshold you are working toward, for example "4,000 watch hours" or "10M Shorts views in 90 days"); [MIN_DAILY_VIEWS] (the minimum average daily views for that target, from the timeline file); [WEEKS_AT_QUOTA] (weeks you have published at quota); [UPLOADS_COUNT] (uploads so far); [KPI_TABLE] (your tracking-sheet rows for the last 10 videos, pasted as text); [LAST_28_DAY_AVG_DAILY_VIEWS] (from Studio).

```
You are a YouTube analytics reviewer. Do all arithmetic in the open. Do not invent numbers and do not use benchmarks from outside my data. If a number is missing, say what is missing and what to copy from YouTube Studio.

Channel: [CHANNEL_NAME]
Niche: [NICHE]
Target: [TARGET]
Minimum average daily views for the target: [MIN_DAILY_VIEWS]
Weeks at quota: [WEEKS_AT_QUOTA]
Uploads so far: [UPLOADS_COUNT]
Last 28-day average daily views: [LAST_28_DAY_AVG_DAILY_VIEWS]
Last 10 videos (columns: date, video, format, impressions, CTR, views at 7 days, views at 28 days, average view duration, average percentage viewed, subscribers gained, rubric score):
[KPI_TABLE]

Compute:
1. Pace ratio = last 28-day average daily views / minimum average daily views.
2. For each video with at least 1,000 impressions: packaging index = its CTR / median CTR of the last 5 such videos; retention index = its average percentage viewed / median of the last 5.
3. Median views at 28 days for the channel, and each video's percentage of that median.
4. Subscribers per 1,000 views, and the views needed for 500 and 1,000 subscribers at that rate.

Then apply these rules and state which rows fire, with the numbers that trigger each:
- Double down on a topic cluster: two videos in one cluster each at 125% or more of the median at day 28.
- Fix packaging: packaging index below 0.75 on 3 videos in a row and retention index 0.9 or above.
- Fix hook and pacing: retention index below 0.8 on 3 videos in a row and packaging index 0.9 or above.
- Keep going: pace ratio 0.5 to 1.0 and rising for 3 weeks.
- On pace: pace ratio 1.0 or higher for 4 weeks.
- Pivot a topic cluster: 3 videos in one cluster at or below 50% of the median at day 28.
- Pivot the lane: after 8 weeks at quota, primary lane pace ratio below 0.25 and the other lane's pace ratio at least double.
- Pivot the concept: after 12 weeks and 20 uploads, pace ratio below 0.10 on both lanes and average rubric score 80 or higher.
- Fix quality first: average rubric score below 80 or any gate failure.

Output: a table of computed numbers, a list of rules that fired, and exactly one change to make next week. Do not recommend anything that involves buying views, sub-for-sub, or misleading titles or thumbnails.
```

Expected output: Computed indexes, the list of rules that fire, and one change for next week.

If the output is weak: Reply "Show the median calculation for CTR and average percentage viewed as sorted lists, and recompute each index."

## Done when

- Every upload has a row in the tracking sheet with CTR, retention and 7-day and 28-day views.
- You can state your current pace ratio and what it means.
- Each weekly review ends with one decision from the table and one change.
- No growth action you took appears in the "Never do this" column.

## Next

[05-income-scenarios.md](05-income-scenarios.md)
