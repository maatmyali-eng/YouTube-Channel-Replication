# Content Calendar (4 Weeks)

> **Purpose:** A copy-paste 4-week calendar that forces variety between uploads and builds the gate days in.  
> **Use when:** Before week 1, and again every 4 weeks.  
> **Time needed:** 20 minutes to fill; 5 minutes to update weekly.  
> **Needs:** Your [STYLE_BIBLE], the [tracking sheet](../09-operations/03-tracking-sheet.md), and the [per-video checklist](per-video-checklist.md).  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [WEEKLY_HOURS], [VIDEO_LENGTH], [STYLE_BIBLE].
- Prompt-specific placeholders, defined in P-OPS-04: [START_DATE], [UPLOADS_PER_WEEK_LONG], [UPLOADS_PER_WEEK_SHORT].

## Steps

1. Copy the blank table below into a Google Doc or into a new tab named `Calendar` in your tracker.
2. Choose the weekly cadence from your hours. Use this rule of thumb that comes from my own arithmetic, not from YouTube data: a long video takes about 4.5 hours start to finish and a Short about 1.25 hours when you use the chains in this repo. Do not schedule more than [WEEKLY_HOURS] per week, and keep one gate session per publish day.
3. Fill the "Angle" column first. Two adjacent uploads must not share the same angle or structure. The five structures this repo uses are: list, experiment, myth correction, case walkthrough, and viewer question.
4. Fill "Style element to keep" from your [STYLE_BIBLE] (for example, hook type or pacing rule) and "Original element" with the new thing you add. This column is your protection against the inauthentic content policy, which targets generic, repetitive, or template-based content with little variation between videos (verified 2026-10-21).
5. Put the gate date at least one day before the publish date. Gates are in [per-video checklist](per-video-checklist.md), [prepublish gate for long-form](../02-long-form/06-prepublish-gate.md), and [prepublish gate for Shorts](../03-shorts/06-prepublish-gate.md).
6. Publish by hand in Studio. If you use scheduling, schedule inside Studio. API publishing from an unaudited project stays private (verified 2026-10-21); see [YouTube API and audit](../06-automation/07-youtube-api-and-audit.md).
7. Each Sunday, update the Status column and move any slipped item to the next free slot; do not double up days.

### Blank template (copy this)

| Week | Date | Format | Working title | Angle | Structure | Style element to keep | Original element I add | Script done | Voice done | Visuals done | Thumbnail done | Gate date | Publish date | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | Long |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 1 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 1 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 2 |  | Long |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 2 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 2 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 3 |  | Long |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 3 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 3 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 4 |  | Long |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 4 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |
| 4 |  | Short |  |  |  |  |  | No | No | No | No |  |  | Planned |

Status values: Planned, In production, Gated, Published, Skipped (write the reason in Notes of your tracker).

### Worked example (neutral niche: home cooking on a budget)

Assumptions: [WEEKLY_HOURS] = 10, [FACE_OR_FACELESS] = faceless (hands and counter only, filmed by me), [VOICE_MODE] = my own recording, [VIDEO_LENGTH] = 8 minutes, start date Monday 2026-11-02. One long video plus one Short per week fits 10 hours (4.5 + 1.25 + gates and review). The second Short per week in the blank table is optional.

| Week | Date | Format | Working title | Angle | Structure | Style element to keep | Original element I add | Gate date | Publish date |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-11-04 | Long | Cooking a week of dinners from one grocery receipt | One receipt, tracked line by line | Case walkthrough | Hook: show the finished plate first | My own receipt and real prices from my local store | 2026-11-05 | 2026-11-06 |
| 1 | 2026-11-07 | Short | The pantry item I stopped buying | One swap, filmed once | Myth correction | Hook: one visual action in 2 seconds | My own before and after cost | 2026-11-08 | 2026-11-09 |
| 2 | 2026-11-11 | Long | Three ways to cook the same cheap cut of meat | Same ingredient, three methods, timed | Experiment | Pacing: a new shot every few seconds | My own timer results and taste notes | 2026-11-12 | 2026-11-13 |
| 2 | 2026-11-14 | Short | One pan, one minute check | Quick test of a common shortcut | Myth correction | Caption style from Style Bible | My own result | 2026-11-15 | 2026-11-16 |
| 3 | 2026-11-18 | Long | Answering your five questions about meal prep containers | Viewer comments become the outline | Viewer question | Open loop before each answer | Real comments from my channel (paraphrased, with no names) | 2026-11-19 | 2026-11-20 |
| 3 | 2026-11-21 | Short | The mistake in my first week | Honest correction of my own video | Case walkthrough | Hook as a question | My own mistake and fix | 2026-11-22 | 2026-11-23 |
| 4 | 2026-11-25 | Long | Ranking five budget breakfast ideas by effort | Effort score on a scale I define | List | Chapter markers | My scoring sheet shown on screen | 2026-11-26 | 2026-11-27 |
| 4 | 2026-11-28 | Short | Effort score of one recipe | One result from the ranking | Experiment | Same caption style | My own score | 2026-11-29 | 2026-11-30 |

The "Original element" column in every row names something only you can supply: your receipt, your timer results, your mistakes, your comments. If you cannot fill that cell, the video is not ready to plan.

## Prompts

### P-OPS-04 — Generate my 4-week content calendar

**Purpose:** Produce a filled calendar with varied angles and structures.

**Inputs:** [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [WEEKLY_HOURS], [VIDEO_LENGTH], [STYLE_BIBLE] (paste the filled Style Bible), [START_DATE] (YYYY-MM-DD), [UPLOADS_PER_WEEK_LONG], [UPLOADS_PER_WEEK_SHORT].

```
You are a content planner who must prevent templated output.

Niche: [NICHE]
Audience: [AUDIENCE]
Language: [LANGUAGE]
On camera or faceless: [FACE_OR_FACELESS]
Voice mode: [VOICE_MODE]
Weekly hours: [WEEKLY_HOURS]
Typical long video length: [VIDEO_LENGTH]
Start date: [START_DATE]
Long videos per week: [UPLOADS_PER_WEEK_LONG]
Shorts per week: [UPLOADS_PER_WEEK_SHORT]

Style Bible:
[STYLE_BIBLE]

Create a 4-week calendar as a Markdown table with these columns: Week | Date | Format | Working title | Angle | Structure | Style element to keep | Original element I add | Gate date | Publish date.

Rules:
1. Time budget: count 4.5 hours per long video and 1.25 hours per Short. Do not exceed my weekly hours; if the request exceeds them, reduce Shorts first and tell me.
2. Structures must come from this list only: list, experiment, myth correction, case walkthrough, viewer question. No two consecutive uploads share a structure or an angle.
3. Every "Original element I add" must be something I personally supply (my own test, data, footage, mistake, or viewer comment). Do not write generic entries such as "unique insights".
4. Style elements come only from my Style Bible. Do not reference another creator's actual titles, phrases, footage, music, or thumbnails.
5. Avoid health, finance, or legal claims presented as expert advice. If a topic touches them, mark it "sensitive: needs sources and a human on screen or in the credits".
6. Gate date is one day before publish date. Publish dates are on weekdays I can work.
7. Do not promise views or income.

After the table, list the 3 weakest rows (most likely to feel templated) and propose a sharper angle for each.
```

**Expected output:** A 12-row or fewer table plus a short list of the three weakest rows with sharper angles.

**If the output is weak:** Paste a list of your last 10 titles and add "reject any angle that overlaps with these".

## Done when

- [ ] All four weeks have an Angle and Original element filled for every row.
- [ ] No two adjacent rows share an angle or structure.
- [ ] Weekly hours total does not exceed [WEEKLY_HOURS].
- [ ] Every row has a gate date earlier than its publish date.

## Next

[Per-video checklist](per-video-checklist.md)
