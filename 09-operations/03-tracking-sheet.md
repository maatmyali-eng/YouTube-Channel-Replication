# Tracking Sheet (Google Sheets)

> **Purpose:** One Google Sheet that records every upload, computes pace toward the YPP thresholds, and drives a 30-minute weekly review.  
> **Use when:** After your first upload, and every week after that.  
> **Time needed:** 40 minutes to build; 30 minutes per weekly review.  
> **Needs:** A Google account, Google Sheets, access to YouTube Studio → Analytics and Earn.  
> **Cost:** $0  

## Inputs

- [CHANNEL_NAME], [NICHE], [WEEKLY_HOURS].
- The KPI thresholds in [growth levers and KPIs](../08-monetization/04-growth-levers-and-kpis.md). This file does not restate them. You copy them into the Settings tab in step 3, so there is one source of truth.
- Prompt-specific placeholders, defined in P-OPS-03: [KPI_TABLE], [VIDEO_LIST], [WEEK_NOTES].

## Steps

### 1. Create the workbook

1. Go to sheets.google.com → Blank spreadsheet. Name it `[CHANNEL_NAME] tracker`.
2. Create four tabs named exactly: `Settings`, `Videos`, `Weekly`, `Notes`. Exact names matter because the formulas below refer to them.

### 2. Build the Videos tab (one row per upload)

Put these headers in row 1, columns A to S. Fill rows from row 2 down. Enter performance numbers 7 days after publishing, and update them again at 28 days.

| Col | Header | What to enter | Formula or validation |
|---|---|---|---|
| A | Row ID | `V001`, `V002`, `S001` for Shorts | none |
| B | Publish date | Date the video went public | Format → Number → Date |
| C | Format | Long or Short | Data → Data validation → Dropdown: Long, Short |
| D | Title | Final published title | none |
| E | Angle | One phrase: what makes this video different from the previous one | none |
| F | Gates passed | Yes or No | Dropdown: Yes, No (from [per-video checklist](../templates/per-video-checklist.md)) |
| G | Disclosure answered | Yes or No | Dropdown: Yes, No (the altered or synthetic and paid promotion questions in Studio) |
| H | Impressions (day 7) | Studio → Analytics → Reach | none |
| I | CTR % (day 7) | Studio → Analytics → Reach | enter as a percent |
| J | Views (day 7) | Studio → Analytics → Overview | none |
| K | Avg view duration (min) | Studio → Analytics → Engagement; convert mm:ss to minutes | none |
| L | Length (min) | Video length in minutes | none |
| M | Avg % viewed | Calculated | `=IF(AND(L2>0,K2>0),K2/L2,"")` |
| N | Engaged views (Shorts) | Studio → Analytics → Engagement, Shorts only | none |
| O | Est. watch hours | Estimate only | `=IF(AND(J2>0,K2>0,C2="Long"),J2*K2/60,"")` |
| P | Subs gained | Studio → Analytics → Audience | none |
| Q | Subs per 100 views | Calculated | `=IF(J2>0,P2/J2*100,"")` |
| R | Originality score | Score from [scoring rubric](../05-originality-layer/02-scoring-rubric.md) | none |
| S | Notes | Anything unusual, including strikes and claims | none |

Copy formulas in M, O, and Q down 200 rows (select the cell, drag the fill handle, or press Ctrl+C then paste into the range M2:M201).

Important: column O is an estimate for spotting trends. The number that decides eligibility is the one shown in Studio → Earn. Never enter column O into the Weekly tab as your official hours.

### 3. Build the Settings tab

Column A holds labels and column B holds values.

| Cell | Label | Value |
|---|---|---|
| B1 | Path (Long or Short) | Long |
| B2 | Target subscribers | Copy from the threshold you chose in [reality and timeline math](../08-monetization/01-reality-and-timeline-math.md) |
| B3 | Target qualified watch hours (Long path) or engaged Shorts views in 90 days (Short path) | Same source |
| B4 | Deadline date | The date you apply or the date the window ends |
| B5 | On-pace ratio | Copy from the KPI file |
| B6 | Watch ratio | Copy from the KPI file |
| B7 | Minimum impressions before judging CTR | Copy from the KPI file |
| B8 | Minimum days before judging a video | Copy from the KPI file |
| B9 | Uploads needed in 90 days | 3 (YPP Tier 1 requires 3 public uploads in 90 days; verified 2026-10-21, source: tella.com YPP guide) |

Use only the values from the KPI file. The labels in rows B5 to B8 are placeholders for whatever names that file uses; if its names differ, rename column A to match so the weekly review reads the same as the rules.

If you plan to apply on or after 1 Feb 2027, use the higher thresholds (8,000 watch hours or 20 million Shorts views) and confirm the subscriber figure first (VERIFY BEFORE RELYING on the YouTube Help partner program page; two secondary sources say 1,000 subscribers stays).

### 4. Build the Weekly tab (one row per Sunday)

Headers in row 1:

| Col | Header | Enter or formula |
|---|---|---|
| A | Week start | Date of the Monday |
| B | Subscribers | Studio → Earn, enter by hand |
| C | Qualified watch hours | Studio → Earn, enter by hand |
| D | Shorts engaged views, 90 days | Studio → Earn, enter by hand |
| E | Public uploads, last 90 days | `=COUNTIFS(Videos!$B:$B,">="&(A2-90),Videos!$B:$B,"<="&A2)` |
| F | Weeks left | `=MAX(1,(Settings!$B$4-A2)/7)` |
| G | Required gain per week | `=IF(Settings!$B$1="Long",MAX(0,Settings!$B$3-C2),MAX(0,Settings!$B$3-D2))/F2` |
| H | Actual gain last week | `=IF(ROW()=2,"",IF(Settings!$B$1="Long",C2-C1,D2-D1))` (rows from 3 down; leave H2 blank) |
| I | Pace ratio | `=IF(AND(ISNUMBER(H3),G3>0),H3/G3,"")` |
| J | Status | `=IF(I3="","",IF(I3>=Settings!$B$5,"On pace",IF(I3>=Settings!$B$6,"Watch","Behind")))` |
| K | Subscribers gap | `=MAX(0,Settings!$B$2-B2)` |
| L | Upload rule met | `=IF(E2>=Settings!$B$9,"Yes","No")` |
| M | One change for next week | Text, one sentence |

Rows 3 down use the same formulas; paste G, I, J, K, L down. Add conditional formatting: select J2:J200 → Format → Conditional formatting → "Text is exactly" → On pace (green), Watch (yellow), Behind (red).

For the Shorts path, remember Shorts watch time does not count toward the watch-hour path, and Shorts views never combine with long-form hours (verified 2026-10-20). If you pursue both, keep two Settings blocks and two Weekly tabs.

### 5. The weekly review routine (30 minutes, same weekday)

1. **Minutes 0 to 5.** Open Studio → Earn. Enter subscribers, qualified watch hours, and Shorts engaged views into a new Weekly row.
2. **Minutes 5 to 12.** Fill the Videos tab for any upload that is now 7 or 28 days old. Skip judging any video that has not reached the minimum days and impressions in Settings.
3. **Minutes 12 to 18.** Read the Status cell. If it says Behind, find which lever is weak using [growth levers and KPIs](../08-monetization/04-growth-levers-and-kpis.md): CTR (thumbnail and title), watch ratio (hook and middle), or volume (uploads).
4. **Minutes 18 to 24.** Open [troubleshooting](02-troubleshooting-faq.md) for the matching group, pick one fix, and write it in column M.
5. **Minutes 24 to 30.** Update the [content calendar](../templates/content-calendar.md) so next week's angles differ from this week's. Check any claim, strike, or notice and log it in Notes.

Change one thing per week. If you change the thumbnail style, the topic, and the length together, you cannot tell which one worked.

### 6. The Notes tab

Columns: Date | Type (Claim, Strike, Notice, Policy change, Tool limit) | Exact text | Action taken | Result. Paste notices word for word.

## Prompts

### P-OPS-03 — Weekly review analysis

**Purpose:** Turn your Weekly and Videos rows into one decision for next week.

**Inputs:** [KPI_TABLE] (paste the last 4 rows of the Weekly tab), [VIDEO_LIST] (paste the last 5 rows of the Videos tab), [WEEK_NOTES] (anything that happened that the numbers do not show), [NICHE], [WEEKLY_HOURS].

```
You are a cautious YouTube analyst. Use only the data below. If the data is too thin for a conclusion, say so.

Niche: [NICHE]
Weekly hours I can work: [WEEKLY_HOURS]

Weekly KPI rows (columns: week start, subscribers, qualified watch hours, Shorts engaged views 90d, uploads in 90d, required weekly gain, actual weekly gain, pace ratio, status):
[KPI_TABLE]

Recent video rows (columns: date, format, title, angle, impressions, CTR, views, average view duration, length, average percent viewed, subs gained, originality score):
[VIDEO_LIST]

Notes this week:
[WEEK_NOTES]

Do this:
1. State whether I am on pace, watching, or behind, and by how much, using only my numbers.
2. Identify the weakest of these three levers: click-through rate, percent viewed, upload volume. Explain which rows show it.
3. Give exactly ONE change for next week, with a hypothesis, the single number I should check, and the day to check it.
4. List any row where the originality score is low or two consecutive angles are similar, and tell me how to vary the next video.
5. Flag any policy risk visible in my notes (claims, strikes, undisclosed synthetic content, undisclosed sponsorship).

Do not predict views, income, or approval. Do not suggest copying another channel's material.
```

**Expected output:** Five short sections ending with one change and one number to check.

**If the output is weak:** Paste more rows, include video lengths, and ask for "no general advice, only conclusions that cite a row".

## Done when

- [ ] Four tabs exist with the exact names above.
- [ ] Settings values were copied from the KPI file, not invented.
- [ ] The Status cell shows a value after the second weekly row.
- [ ] You completed one weekly review in 30 minutes and wrote one change in column M.

## Next

[Content calendar template](../templates/content-calendar.md)
