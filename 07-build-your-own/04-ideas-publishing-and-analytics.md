# Build Your Own, Part 4: Publishing and Analytics Tools

> **Purpose:** five tools to log metadata tests, record retention lessons, plan repurposing, read analytics, and check a video before upload  
> **Use when:** you have published videos or are close to your first upload  
> **Time needed:** 2 to 4 hours per tool  
> **Needs:** a free Google account, Python 3.11 or later for two tools, a free Claude or Gemini chat  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [VIDEO_LENGTH], [FACE_OR_FACELESS], [VOICE_MODE] from the setup card.
- Your tracking sheet from `09-operations/03-tracking-sheet.md` and your per-video checklist from `templates/per-video-checklist.md`.
- Your review log (`review-log.md`) from the pre-publish gate, if you follow the S6 and S7 workflow in `06-automation/04-human-checkpoints.md`.

## Steps

1. Decide your data route before you build anything. Two compliant routes exist:
   1. Manual CSV route (recommended, no API setup): YouTube Studio → Analytics → Advanced mode → pick a date range and a table → the export icon → Download as CSV or Google Sheets. Menu names change; VERIFY BEFORE RELYING at support.google.com/youtube.
   2. API route (optional): the YouTube Analytics API reads your own channel's metrics with OAuth. Reported details (verified 2026-10-20, secondary sources): `reports.query` takes dimensions and metrics such as day, video, views, estimatedMinutesWatched, averageViewDuration and subscribersGained; its quota is separate from the Data API's 10,000 daily units; and a recent change was reported to require the `youtube.readonly` scope in addition to `yt-analytics.readonly`. One source says impressions and impression click-through rate are available only in Studio. VERIFY BEFORE RELYING at developers.google.com/youtube/analytics.
2. Keep OAuth work out of your first build. OAuth consent screens in Testing status have strict limits and expiring authorizations; the details are in `06-automation/07-youtube-api-and-audit.md`.
3. Store logs in Google Sheets so they survive a computer failure. Name the file `[CHANNEL_NAME] - Ops`. Share it with nobody.
4. Do not build anything that uploads publicly, schedules publicly, or edits metadata at scale on its own. Every tool here ends in a human decision. This keeps the automation inside platform rules and keeps a person responsible for the final video.
5. Every limit in this file that is not marked verified is this repo's working number. YouTube publishes no pass score, and no tool here predicts monetization.
6. Build order: P-BUILD-20 first (it protects every upload), then P-BUILD-19, P-BUILD-16, P-BUILD-17, and P-BUILD-18 once you have at least five published videos.

## Prompts

### P-BUILD-16 — Metadata A/B Log

- What it does: records every title, thumbnail, and description variant you try, the exact dates each version was live, and the result, so you can read tests without fooling yourself.
- Why it helps: without a log you cannot tell a title effect from a day-of-week or topic effect; the log forces one change at a time and a minimum observation window.
- Free stack: Google Sheets and Apps Script. Optional: the test-and-compare feature in YouTube Studio if your channel has it.
- Difficulty: easy. Time to build: 2 hours.
- Risks: policy: changing a title or thumbnail to something deceptive is never acceptable; the metadata must match the video; ToS: no automation of metadata edits is built here. Evidence quality: sequential tests (version A this week, B next week) are weak evidence, so the sheet marks them as such. VERIFY BEFORE RELYING at support.google.com/youtube on whether Studio offers thumbnail or title testing for your channel and how it reports results.

**Purpose:** a test log with built-in sanity checks.
**Inputs:** [CHANNEL_NAME], [NICHE], [MIN_DAYS] (minimum days per version, default 7), [MIN_IMPRESSIONS] (default 1000).

```
You are a Google Sheets and Apps Script expert. Build a "Metadata A/B Log" at $0 for the channel [CHANNEL_NAME] in [NICHE].

Tabs:
- Tests: A test ID, B video title (current), C video URL, D element tested (Title, Thumbnail, Description first lines, Hook), E hypothesis (one sentence), F test type (Studio test, Sequential, Different videos), G start date, H end date, I decision rule written BEFORE the test, J status.
- Versions: A test ID, B version letter, C exact text or thumbnail file name, D date live from, E date live to, F impressions, G click-through rate (percent, from Studio), H views from impressions, I average view duration, J average percentage viewed, K notes.
- Results: one row per test with the winner by CTR, the winner by average percentage viewed, and a "Safe to conclude?" column.
- Rules: cells that hold [MIN_DAYS] and [MIN_IMPRESSIONS] and a note that they are my working numbers.

Logic:
1. "Safe to conclude?" = "Yes" only if every version has at least [MIN_DAYS] days live and at least [MIN_IMPRESSIONS] impressions, and test type is not "Different videos". If test type is "Sequential" show "Weak evidence: confirm with another video". Otherwise show the missing requirement.
2. Winner by CTR must also not lose average percentage viewed by more than 10 percent relative (cell on the Rules tab, editable); otherwise the Results row says "CTR win, retention loss: check promise vs delivery".
3. Apps Script onEdit: when status becomes "Done", lock rows (protection warning only) and copy the decision to a tab named Learnings with date, element, what won, and a column "Add to Style Bible? yes/no".
4. Data validation on dates, percentages (0 to 100) and the dropdown fields.
5. A check that titles are 100 characters or less and flag any title over 60 characters in yellow as "may truncate" (60 is my working number; VERIFY the current display lengths).
6. A deception check: a column in Tests labelled "Does the new version still match the video's content? Yes/No". If No, status is forced to "Rejected".

Deliver: exact formulas, the full Apps Script, setup steps with menu paths, and 3 test cases with expected values (a clean 2-version test, a test with only 3 days, a test of type Different videos). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** a sheet design, formulas and script.
**If the output is weak:** ask for the Results tab formulas in a table with a sample 6-row data set and the expected output.

### P-BUILD-17 — Retention Notes Logger

- What it does: logs each video's retention graph dips and peaks with timestamps, matches them to script sections, and shows which section types lose viewers most often across videos.
- Why it helps: retention lessons stop living in your memory; after 5 to 10 videos the pattern tells you which hooks, transitions, and sections need a different treatment.
- Free stack: Google Sheets and Apps Script. Data from the Studio retention graph typed in by hand (or from API data, optional).
- Difficulty: easy to medium. Time to build: 2 to 3 hours.
- Risks: privacy: none for your own channel; accuracy: retention graph shapes depend on video length and traffic source, so compare similar videos only.

**Purpose:** convert retention graphs into section-level lessons.
**Inputs:** [VIDEO_LENGTH], [NICHE], a list of your script section names such as HOOK, SETUP, STEP, PAYOFF, OUTRO (use the section names from your Style Bible).

```
You are a Google Sheets and Apps Script expert. Build a "Retention Notes Logger" at $0 for a channel in [NICHE] with videos around [VIDEO_LENGTH].

Section names used in my scripts: [SECTION_NAMES].

Tabs:
- Videos: A video ID or title, B publish date, C length in seconds, D average percentage viewed, E percent still watching at 30 seconds, F percent still watching at the 25%, 50%, 75% marks (three columns), G traffic source note, H script file link.
- Events: A video, B timestamp (mm:ss), C event type (Dip, Plateau, Spike, Rewatch), D size in percentage points (estimate from the Studio graph), E what was on screen or being said (my words, under 20 words), F suspected cause (dropdown: Slow intro, Off-promise, Repeated point, Unclear visual, Audio problem, Sponsor or ad read, Long explanation, Abrupt tone shift, Other), G fix tried next time.
- Sections: A video, B section name, C start mm:ss, D end mm:ss.
- Lessons: formulas only.

Logic:
1. A helper in Events computes the section for each event by comparing the timestamp with Sections (start and end), using a lookup, and returns the section name in column H.
2. Lessons shows, per section name: number of dips, average dip size, most common suspected cause, and number of videos affected. Sort by total dip points.
3. Lessons shows a "Top 3 fixes to apply next video" block built from the three largest section and cause combinations, as text like "HOOK + Slow intro: seen in 4 of 7 videos".
4. A menu item "Make Style Bible note" writes a plain-text paragraph into a cell that I can paste into my Style Bible's pacing section, starting with "Based on N videos".
5. Add a "Comparable group" column in Videos (Short-long, Mid-long, Long) assigned automatically from length with cutoffs in cells I can edit, and make Lessons filterable by group.
6. Data validation for timestamps (mm:ss text), dropdowns, and sizes (0 to 100).

Deliver: the formulas, the script, setup steps with menu paths, and 3 test cases with expected output (an event inside a section, an event at an exact section boundary, a video with no events). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** a working sheet and a lessons block.
**If the output is weak:** ask for "the lookup formula for column H alone, tested on 5 sample timestamps".

### P-BUILD-18 — Repurposing Planner

- What it does: takes the outline of a published long video and plans a small number of Shorts, each with a different angle, a new hook, new on-screen text, and a standalone reason to exist.
- Why it helps: it prevents the lazy "cut 10 clips from every video" pattern, which risks the repetitive or template-based content category (verified 2026-10-20) and the reused-content rules.
- Free stack: Google Sheets, optionally a free Claude or Gemini chat to propose angles.
- Difficulty: easy. Time to build: 1.5 to 2 hours.
- Risks: policy: Shorts must add value and vary; a weekly cap and a variety check are built in. The cap and thresholds are this repo's working numbers. For methods, see `03-shorts/05-repurposing-without-reuse.md`.

**Purpose:** a planner that limits and varies Shorts from one long video.
**Inputs:** [CHANNEL_NAME], [NICHE], [AUDIENCE], [MAX_SHORTS_PER_VIDEO] (default 3), [MAX_SHORTS_PER_WEEK] (default 5).

```
You are a Google Sheets and Apps Script expert. Build a "Repurposing Planner" at $0 for [CHANNEL_NAME] ([NICHE], audience [AUDIENCE]).

Tabs:
- LongVideos: A title, B publish date, C URL, D one-sentence thesis, E outline pasted by me (one beat per row in a second tab Beats).
- Beats: A video, B beat number, C timestamp, D beat summary, E standalone? (Yes/No: can a stranger understand it in under 45 seconds with no context), F contains a number, demo, or surprising fact? (Yes/No), G reusable as a Short? (formula: Yes only if E and F are both Yes).
- ShortsPlan: A short ID, B parent video, C beat number, D angle (dropdown: Myth, Mistake, Quick demo, Surprising number, Before-and-after, Question answered, Behind the scenes), E new hook line (written fresh, not cut from the long video's script), F new on-screen text, G new ending line or loop, H planned publish date, I status.
- Checks.

Logic and checks (all thresholds in cells on the Checks tab, labelled "my working numbers"):
1. Each long video gets at most [MAX_SHORTS_PER_VIDEO] rows in ShortsPlan, and the sheet turns a row red when exceeded.
2. At most [MAX_SHORTS_PER_WEEK] Shorts planned per calendar week across all videos; show the count per week.
3. No two Shorts in the same week with the same angle; show a warning.
4. A hook similarity check using an Apps Script function that compares hook lines (Jaccard of word sets) across the last 20 planned Shorts and warns at 0.5 or above.
5. A rule that column E must differ from the sentence at that beat in the long video: a checkbox column "Hook is new wording (I checked)" that must be TRUE before status can become "Ready".
6. A "Prompt" tab with a cell that builds, from the selected beat, this exact text for a chat: "Write 3 Shorts hooks (under 12 spoken words each) for this beat in [LANGUAGE], each using a different angle from this list: Myth, Mistake, Quick demo, Surprising number, Before-and-after, Question answered. The Short must make sense without the long video. Beat: <beat summary>. Do not reuse sentences from the long video."

Deliver: formulas, Apps Script, setup steps with menu paths, and 3 test cases with expected output (4 Shorts for one video, 2 Shorts with the same angle in a week, two near-identical hooks). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** a planning sheet with limits.
**If the output is weak:** ask it to list every check as "cell, condition, message" in one table so you can test each by hand.

### P-BUILD-19 — Analytics Dashboard in Google Sheets

- What it does: imports Studio CSV exports into one sheet and builds a dashboard of views, watch time, average view duration, subscribers per video, top traffic sources, and your progress toward the YPP thresholds.
- Why it helps: one place shows whether you are on pace for the thresholds in `08-monetization/01-reality-and-timeline-math.md` and which videos teach you something.
- Free stack: Google Sheets with pivot-style formulas and charts; no code required, optional Apps Script for imports.
- Difficulty: easy to medium. Time to build: 3 hours.
- Risks: accuracy: column names in Studio exports change, so the import tab maps columns by header text and stops with a message when a header is missing; policy: this reads your own data only. YPP thresholds change, so the dashboard keeps them in editable cells. Current values (verified 2026-10-20): Tier 1 needs 500 subscribers, 3 public uploads in 90 days, and 3,000 public watch hours in 12 months or 3M Shorts views in 90 days; Tier 2 needs 1,000 subscribers and 4,000 public watch hours in 12 months or 10M Shorts views in 90 days; new Tier 2 applicants from 1 February 2027 need 8,000 watch hours or 20M Shorts views. Shorts views and long-form watch hours do not combine. VERIFY BEFORE RELYING at support.google.com/youtube/answer/72851.

**Purpose:** a self-updating dashboard with YPP progress bars.
**Inputs:** [CHANNEL_NAME], [DAYS_TO_TRACK] (default 90), the Studio CSV files you export.

```
You are a Google Sheets and Apps Script expert. Build an "Analytics Dashboard" at $0 for [CHANNEL_NAME].

Data in: I export CSV files from YouTube Studio → Analytics → Advanced mode and paste them into tabs named Import_Videos, Import_Daily, and Import_Traffic. Do not use any API in this version.

Requirements:
1. Config tab with editable cells: the YPP thresholds (Tier 1: subscribers 500, uploads in 90 days 3, watch hours 3000 in 12 months, Shorts views 3,000,000 in 90 days; Tier 2: subscribers 1000, watch hours 4000, Shorts views 10,000,000; and a second set labelled "Tier 2 for new applicants from 1 Feb 2027": watch hours 8000, Shorts views 20,000,000), each with a note "Check support.google.com/youtube/answer/72851 before relying".
2. A header mapper: a table on Config that lists the header text I expect for each field (video title, publish time, views, watch time (hours), average view duration, subscribers, impressions, impressions click-through rate) and an Apps Script function that checks each Import tab for those headers and shows a dialog naming any missing header. Do not guess columns.
3. Dashboard tab: last [DAYS_TO_TRACK] days of views, watch hours, subscribers gained; per-video table sorted by views with views per day since publishing, average view duration, and subscribers gained per 1,000 views; top 5 traffic sources.
4. YPP progress block: current subscribers, public watch hours in the last 365 days from Import_Daily (sum of watch hours column), Shorts views in the last 90 days if I fill a manual cell (because Shorts and long-form views are reported separately), uploads in the last 90 days counted from Import_Videos, and progress bars (REPT formula) toward each threshold. Show "Shorts views and long-form watch hours do not combine" in a note.
5. A projection row: average weekly watch hours over the last 4 weeks, and estimated weeks to reach each watch-hour threshold at that pace, labelled "straight-line estimate, not a forecast".
6. A "Learnings" block: the three videos with the best and the three with the worst average percentage viewed (if the column exists), with a free-text cell next to each for my note.
7. Charts: weekly views, weekly watch hours, subscribers per video. Use native Sheets charts.
8. A menu "Dashboard" with: Check headers, Clear imports, Refresh.

Deliver: the formulas, the script, setup steps with exact menu paths for creating charts in Sheets, and 3 test cases with expected outputs using small invented sample data (10 rows). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** a sheet design with formulas and a script.
**If the output is weak:** paste your real CSV header row and ask it to rewrite the header mapper and the two formulas that fail.

### P-BUILD-20 — Upload-Readiness Checker

- What it does: a command-line checklist that reads a small per-video file and your review log, and refuses a "READY" result until title, description, tags, thumbnail file, captions, license log, AI disclosure decision, sponsorship disclosure, and review gates are all complete.
- Why it helps: most avoidable problems come from skipped steps at the last minute; the checker makes the gate mechanical.
- Free stack: Python 3.11 standard library, `pathlib`, `json`, `re`.
- Difficulty: easy to medium. Time to build: 3 hours.
- Risks: policy: the checker proves you completed your own list, not that YouTube will approve anything. Items about disclosure follow the snapshot (verified 2026-10-20): realistic altered or synthetic content must be disclosed in YouTube Studio under "Altered or synthetic content", YouTube may add the label itself, and undisclosed branded content can be auto-labeled. VERIFY BEFORE RELYING at support.google.com/youtube for wording. Title, description, and tag limits in the checker are common figures that you must VERIFY BEFORE RELYING.

**Purpose:** a pre-upload gate with no exceptions for missing items.
**Inputs:** [VIDEO_FOLDER] (one folder per video), [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [MIN_RUBRIC_SCORE] (default 80).

```
You are a senior Python developer. Build "ready_check.py" at $0 with the Python 3.11 standard library only.

Usage: python ready_check.py --folder [VIDEO_FOLDER]

Each video folder should contain:
- ready.json with fields: title, description, tags (list), category (text), language, thumbnail_file, captions_file, final_video_file, made_for_kids (true/false), has_paid_promotion (true/false), uses_realistic_synthetic_media (true/false), synthetic_disclosure_set_in_studio (true/false), voice_is_synthetic (true/false), voice_decision_note (text), sources_list_file, license_log_file, originality_note (one to three sentences: what is original in this video).
- review-log.md with lines that begin C1 through C8. Each of those lines should end with "pass/fail" followed by what I typed, either pass or fail. The C8 line should also carry the words "rubric score" followed by a number.
- The files named in ready.json.

Checks, each printing PASS or FAIL with a one-line reason:
1. All fields present and non-empty.
2. Title length 1 to 100 characters; warn above 60 (working number). Description under 5,000 characters; warn if the first 150 characters are empty of the main topic words (the topic words come from the title, minus stopwords). Tags: total length under 500 characters; warn if more than 15 tags (working number). All limits are in constants at the top, flagged VERIFY BEFORE RELYING.
3. Title and description contain none of: ALL-CAPS words longer than 5 letters beyond two in a row, three or more exclamation marks, the phrases "guaranteed", "100% free money", "get rich", "full proof" (list editable). Report what was found.
4. Thumbnail file exists, is JPG or PNG, 2 MB or smaller, and its dimensions are 16:9 (use a pure-Python image header reader for PNG and JPEG sizes).
5. Captions file exists and is valid SRT with monotonically increasing times.
6. Final video file exists, and ffprobe (if available) reports duration, resolution and the presence of an audio stream; if ffprobe is missing, warn and continue.
7. Disclosure logic: if uses_realistic_synthetic_media is true then synthetic_disclosure_set_in_studio must be true; if voice_is_synthetic is true then voice_decision_note must be non-empty; if has_paid_promotion is true then the description must contain the word "sponsored", "ad", or "paid promotion" within its first 200 characters and the Studio paid-promotion setting must be done by hand (print a reminder).
8. sources_list_file exists and has at least one non-empty line; license_log_file exists and has a row for each asset file in the folder named "assets" (compare file names).
9. review-log.md: C1 through C8 each read pass; C8 has a rubric score of at least [MIN_RUBRIC_SCORE]. If any line is blank or fail, report which one.
10. originality_note has at least 20 words and does not start with a generic phrase such as "this video is about".

Final line: READY or NOT READY, and write ready_report.md in the folder. Exit code 0 only if READY. Never modify any file in the folder except writing ready_report.md. Never upload anything.

Deliver: the full script, an example ready.json and review-log.md for a video in the niche "home cooking on a budget", run commands for Windows, macOS and Linux, and 3 test cases with exact expected results (a fully ready folder, a folder with C5 failing, a folder using synthetic media without the Studio disclosure). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `ready_check.py` with sample files.
**If the output is weak:** ask it to add a `--json` mode that prints the results as machine-readable output, so you can later run the checker from an automation.

## Done when

- P-BUILD-20 runs on your last video folder and reports READY or lists specific failures you fixed.
- Your dashboard shows your real current numbers against the YPP thresholds, and you checked those thresholds on YouTube's own page today.
- Every metadata test has a decision rule written before the test and a minimum window.
- No tool in your setup uploads publicly, schedules publicly, or edits metadata on its own.
- You can state in one line what each Short adds that its parent video does not.

## Next

Continue with [Channel Style Analyzer starter](./05-channel-style-analyzer-starter.md).
