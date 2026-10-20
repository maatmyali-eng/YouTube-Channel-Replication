# Build Your Own, Part 1: Research and Ideation Tools

> Purpose: five small tools that find topics, mine audience questions, and map a channel's patterns | Use when: you want your own tooling instead of doing research by hand | Time needed: 1 to 4 hours per tool | Needs: a free Google account, a free Claude or Gemini chat, optionally Python 3.11 or later | Cost: $0

## Inputs

- [NICHE], [AUDIENCE], [LANGUAGE], [COUNTRY], [CHANNEL_URL], [CHANNEL_NAME] from `00-start-here/01-setup-card.md`.
- [HARDWARE] and [WEEKLY_HOURS] to decide which tool to build first.
- For tools that call YouTube: a free YouTube Data API key (steps below).
- For the structural ideas behind these tools, see `01-channel-dna/01-data-gathering.md` and `01-channel-dna/02-channel-analysis.md`.

## Steps

1. Pick ONE tool. Build order for most owners: P-BUILD-04 (backlog scorer, no code), then P-BUILD-03 (title patterns), then P-BUILD-01 (trend and gap finder). Build P-BUILD-02 and P-BUILD-05 only after you have a published channel to read.
2. Get a free YouTube Data API key (needed for P-BUILD-01, 02, 03, 05):
   1. Open console.cloud.google.com and sign in.
   2. Top bar project picker → New Project → name it `yt-research` → Create.
   3. Left menu → APIs & Services → Library → search "YouTube Data API v3" → Enable.
   4. APIs & Services → Credentials → Create credentials → API key. Copy it.
   5. Click the key → API restrictions → Restrict key → tick only "YouTube Data API v3" → Save.
   6. Menu names change. VERIFY BEFORE RELYING: console.cloud.google.com and developers.google.com/youtube/v3/getting-started.
3. Quota facts to design around: the Data API default is 10,000 units per day per project, resetting at midnight Pacific, and `search.list` costs 100 units per call (verified 2026-10-20, secondary sources; official page: developers.google.com/youtube/v3/determine_quota_cost). Other reads such as `videos.list`, `playlistItems.list` and `commentThreads.list` are listed at 1 unit each in older documentation. VERIFY BEFORE RELYING on the official quota page before you run anything in bulk. Every tool below therefore ends in a cheap call pattern and a run cap.
4. Google Apps Script limits for the Sheets-based tools (verified 2026-10-20): 6 minutes per execution, about 90 minutes of total trigger runtime per day on a free consumer account, 20 triggers per user per script, and a URL Fetch daily cap reported as 20,000 calls on consumer accounts. Source: developers.google.com/apps-script/guides/services/quotas. VERIFY BEFORE RELYING on the current table.
5. Open a new chat for each prompt. Paste the prompt, replace the bracketed inputs, and run what it gives you. Test with the three test cases the prompt asks for before trusting the output.
6. Keep every API key out of Sheets cells that you share. Store keys in Apps Script → Project Settings → Script properties, or in a local `.env` file that is never committed.
7. Data rules for this whole folder: use only the public watch page, the on-page transcript panel you copy by hand, public metadata, your own channel's data, and the official API. Do not download videos, do not scrape at scale, and do not store other people's comment author names.

## Prompts

### P-BUILD-01 — Trend and Gap Finder

- What it does: takes seed keywords, finds recent public videos for each, and flags topics where demand is high (views per day) and supply from comparable channels is thin.
- Why it helps: it replaces guessing with a ranked topic list, and the output is topics, not copied videos.
- Free stack: Google Sheets, Apps Script, YouTube Data API key. Optional: a Google Trends CSV you export by hand from trends.google.com.
- Difficulty: medium. Time to build: 3 to 4 hours.
- Risks: policy: none if you pick your own angle; ToS: the API Services terms restrict how long you may store API data (VERIFY BEFORE RELYING: developers.google.com/youtube/terms/developer-policies), so keep only the numbers you need; quota: capped at 20 searches per run; license: none.

**Purpose:** build a Sheets tool that ranks topic gaps.
**Inputs:** [NICHE], [AUDIENCE], [LANGUAGE], [COUNTRY], [SEED_KEYWORDS] (10 to 20 keywords, one per row), [MAX_SEARCHES] (default 20).

```
You are a senior Google Apps Script developer. Build a "Trend and Gap Finder" for a YouTube creator. Everything must cost $0.

Context: niche [NICHE]; audience [AUDIENCE]; language [LANGUAGE]; country [COUNTRY].
Seed keywords are in a sheet tab named Seeds, column A, starting at A2.

Requirements:
1. Menu "Gap Finder" with items: Run research, Clear results, Show quota counter.
2. Store the API key in Script Properties under YT_API_KEY. Never write it into a cell.
3. For each seed keyword, call search.list (part=snippet, type=video, order=viewCount, publishedAfter = 90 days ago, relevanceLanguage = [LANGUAGE] code, regionCode = [COUNTRY] code, maxResults=15). Stop after [MAX_SEARCHES] searches per run and write how many were used to a cell named QuotaToday. Add 100 units per search and 1 unit per other call to a running counter stored in Script Properties that resets on a new Pacific date.
4. Batch the video IDs into videos.list (part=snippet,statistics,contentDetails, up to 50 IDs per call) and the channel IDs into channels.list (part=statistics).
5. In a tab named Results write one row per video: keyword, title, channel, subscribers, views, publish date, views_per_day, outlier_ratio = views_per_day divided by the median views_per_day of that channel's videos in the result set, duration in minutes, URL.
6. In a tab named Gaps write one row per keyword: number of results from channels under 50,000 subscribers, median views_per_day of those results, share of results older than 60 days, and a gap_score = (median views_per_day of small channels) divided by (number of small-channel results + 1). Sort descending. Add a column "Original angle needed" with the text "Write one sentence: what do I know, show, or test that these videos do not?" and leave it blank.
7. Handle errors: quota exceeded (stop and say so), empty results, HTTP 4xx and 5xx with one retry after 2 seconds, and the 6-minute execution limit (save progress and tell me to run again).
8. Do not store thumbnails, descriptions, or comments.

Deliver: the complete Code.gs, the exact steps to paste it into Extensions → Apps Script, how to add the Script Property, and 3 test cases with the exact expected result for each (a normal keyword, a keyword with zero results, a run where the quota counter is already near the cap). Mark anything you are unsure of as VERIFY BEFORE RELYING and name the official page.
```

**Expected output:** one `Code.gs` file, setup steps, three test cases.
**If the output is weak:** paste the error text from Apps Script → Executions and add "Fix this exact error and return the full corrected file, not a patch."

### P-BUILD-02 — Audience Comment Miner

- What it does: pulls public comments on your own videos (and optionally on a few public videos in your niche), strips author names, and groups them into questions, requests, confusion points, and objections.
- Why it helps: viewers' own questions become video ideas and script fixes, which makes content less generic.
- Free stack: Google Sheets, Apps Script, YouTube Data API key, then paste the cleaned sheet into a free Claude or Gemini chat for grouping.
- Difficulty: medium. Time to build: 3 hours.
- Risks: ToS and privacy: comments are personal data; keep no usernames, no channel IDs of commenters, and never quote a comment with a name attached; policy: do not use the comments to impersonate a commenter or to bait engagement.

**Purpose:** turn raw comments into a ranked list of audience needs.
**Inputs:** [VIDEO_IDS] (up to 10 video IDs), [MAX_COMMENTS_PER_VIDEO] (default 200), [NICHE], [AUDIENCE], [LANGUAGE].

```
You are a senior Google Apps Script developer and a careful data-privacy reviewer. Build a "Comment Miner" for a YouTube creator at $0.

Inputs: video IDs listed in a tab named Videos, column A from A2. Niche: [NICHE]. Audience: [AUDIENCE]. Language: [LANGUAGE]. Limit: [MAX_COMMENTS_PER_VIDEO] top-level comments per video.

Requirements:
1. Menu "Comment Miner" with: Fetch comments, Clean and tag, Export for AI grouping.
2. Fetch with commentThreads.list (part=snippet, order=relevance, maxResults=100, paging with pageToken). Keep ONLY: video ID, comment text, like count, published date. Do NOT store author names, author channel IDs, author photos, or reply authors.
3. Clean and tag with formulas or script only (no AI call): remove comments under 4 words, remove exact duplicates, remove comments containing URLs, and add a Type column using these rules: "Question" if it has a question mark or starts with how, why, what, when, where, can, does, is; "Request" if it contains "please", "make a video", "can you do", "next video"; "Complaint" if it contains "too fast", "too slow", "can't hear", "audio", "boring", "wrong"; otherwise "Other".
4. Export for AI grouping: build a single text block in a cell named ExportBox with up to 300 cleaned comments, one per line, each prefixed by its Type, ready to paste into a chat.
5. Add a tab named GroupingPrompt containing this fixed text for me to paste above the export: "Group these comments into at most 12 themes. For each theme give: a name, how many comments, 2 paraphrased examples (never quote exactly), the viewer's underlying need, and one original video idea that answers it for [AUDIENCE]. Rank themes by count. Do not invent comments."
6. Handle: comments disabled (HTTP 403 commentsDisabled) by skipping the video and logging it; quota exceeded; empty results; the 6-minute limit by saving progress.

Deliver: complete Code.gs, setup steps, and 3 test cases with exact expected results (a video with comments, a video with comments disabled, a video with fewer than 4-word comments only). Mark uncertain facts VERIFY BEFORE RELYING with the official page.
```

**Expected output:** `Code.gs`, a ready tab, and a grouping prompt.
**If the output is weak:** tell it which rule failed with one real example row and ask for a corrected function only.

### P-BUILD-03 — Title Pattern Miner

- What it does: reads the public titles, dates, lengths, and view counts of a channel's uploads and labels each title with a pattern, then reports which patterns perform above that channel's own median.
- Why it helps: it gives you pattern frequencies (structure, length, number use) to model without copying a single title.
- Free stack: Python 3.11, `requests`, `pandas`, YouTube Data API key; or Apps Script if you prefer Sheets.
- Difficulty: easy to medium. Time to build: 2 hours.
- Risks: policy: never reuse a source title; the output must be patterns only; ToS: public metadata through the official API only.

**Purpose:** convert a channel's title list into a pattern table.
**Inputs:** [CHANNEL_URL] (channel handle or channel ID), [MAX_VIDEOS] (default 200), [LANGUAGE].

```
You are a senior Python developer. Build "title_miner.py" at $0 using Python 3.11, requests, and pandas only.

Input: a YouTube channel handle or channel ID from [CHANNEL_URL]; language [LANGUAGE]; up to [MAX_VIDEOS] uploads.
Credentials: the API key is read from the environment variable YT_API_KEY.

Steps the script must perform:
1. Resolve the channel to its uploads playlist with channels.list (part=contentDetails), then page playlistItems.list to collect video IDs. Do not use search.list.
2. Call videos.list (part=snippet,statistics,contentDetails) in batches of 50.
3. Build a DataFrame with: video_id, title, published_at, duration_seconds, views, views_per_day (views divided by days since publishing, minimum 1 day), is_short (duration_seconds <= 180 as a heuristic, labelled as a heuristic).
4. Add pattern flags using plain rules: starts_with_number, contains_number, is_question, has_how_to, has_colon_or_dash_split, has_vs_or_versus, has_year, has_time_bound (words like days, hours, minutes, week), title_length_chars, title_word_count, uses_all_caps_word, uses_brackets.
5. Output three CSV files: titles_raw.csv, pattern_summary.csv (for each flag: count, share, median views_per_day with flag, median without, lift = with/without), cadence.csv (uploads per ISO week and by weekday).
6. Print a short plain-text report of the 5 patterns with highest lift that also have at least 8 videos, and write the sentence "These are structures, not titles. Do not reuse any title." at the top of the report.
7. Handle: invalid handle, private or empty channel, HTTP errors with one retry, missing statistics, and API quota exceeded (exit with a clear message).

Deliver: the full script, requirements.txt, run commands for Windows and macOS/Linux, and 3 test cases with expected outcomes (a normal channel, a channel with fewer than 8 videos, a wrong handle). Mark uncertain facts VERIFY BEFORE RELYING with the official page.
```

**Expected output:** `title_miner.py`, `requirements.txt`, and run instructions.
**If the output is weak:** ask "Re-read requirement 4 and show me one worked example row for each flag, then fix any flag whose example is wrong."

### P-BUILD-04 — Idea Backlog Scorer and Duplicate Guard

- What it does: a Google Sheet where every video idea is scored and checked against your own past titles and against the source channel's titles for near-duplicates.
- Why it helps: it stops you from drifting into templated, repetitive output (one of the YouTube inauthentic-content categories, verified 2026-10-20) and from accidentally echoing a source title.
- Free stack: Google Sheets with formulas and one Apps Script function. No API.
- Difficulty: easy. Time to build: 1 to 2 hours.
- Risks: none beyond data you paste yourself; the similarity threshold is this repo's own and not a YouTube rule.

**Purpose:** rank ideas and block duplicates.
**Inputs:** [NICHE], [AUDIENCE], [WEEKLY_HOURS], a tab of your own published titles, a tab of source-channel titles you copied from the public channel page.

```
You are a Google Sheets and Apps Script expert. Build an "Idea Backlog Scorer and Duplicate Guard" at $0 for a creator in [NICHE] with audience [AUDIENCE] and [WEEKLY_HOURS] hours per week.

Tabs required:
- Ideas: columns A idea title, B one-sentence promise, C original angle (what I know, show, or test that others do not), D search demand 1-5, E gap 1-5, F fit with style 1-5, G effort 1-5 (5 = hardest), H score, I duplicate flag, J status (Idea, Approved, Scripted, Published).
- MyTitles: column A, my published titles.
- SourceTitles: column A, titles from the channel I am modelling.

Rules:
1. H = (D + E + F) * 2 - G, and if column C is empty then H shows "Add original angle" instead of a number.
2. I uses an Apps Script custom function SIM(title, range) that lowercases, strips punctuation and stopwords (English list embedded in the script), builds word sets, and returns the highest Jaccard similarity against the range. Flag "Duplicate of mine" if similarity against MyTitles is 0.5 or higher, "Too close to source" if similarity against SourceTitles is 0.4 or higher, else "OK". State clearly in a note that these thresholds are my own working numbers and can be edited in cells L1 and L2.
3. Conditional formatting: red for duplicate flags, green for score 12 or higher with an original angle.
4. A tab named Top5 using QUERY or SORT to show the five highest-scored ideas with status Idea.
5. Add data validation for D, E, F, G (whole numbers 1-5) and J (list).

Deliver: exact cell formulas, the full Apps Script, step-by-step setup with menu paths, and 3 test cases with expected values (an idea with no angle, an idea copying one of my titles, an idea 0.45 similar to a source title). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** a working sheet plan, formulas, and a script.
**If the output is weak:** ask it to "return every formula in one table with the cell address, formula text, and a sample value".

### P-BUILD-05 — Series and Cadence Mapper

- What it does: maps a channel's playlists, series lengths, episode naming schemes, upload weekdays and gaps between uploads.
- Why it helps: series structure and cadence are part of the Style Bible; this makes them measurable instead of eyeballed.
- Free stack: Python 3.11, `requests`, `pandas`, optional `matplotlib`, YouTube Data API key.
- Difficulty: easy to medium. Time to build: 2 to 3 hours.
- Risks: policy: model the structure, not the series concept's exact name or format branding; ToS: official API only.

**Purpose:** quantify series and cadence.
**Inputs:** [CHANNEL_URL], [MAX_PLAYLISTS] (default 30).

```
You are a senior Python developer. Build "series_mapper.py" at $0 with Python 3.11, requests, pandas and optional matplotlib.

Input: [CHANNEL_URL]; API key from environment variable YT_API_KEY; at most [MAX_PLAYLISTS] playlists.

Do the following:
1. Resolve the channel ID, then list public playlists with playlists.list (part=snippet,contentDetails, maxResults=50, paging).
2. For each playlist call playlistItems.list (part=snippet,contentDetails, paging) and videos.list (batches of 50) to get title, publish date, duration and views.
3. Detect episode naming: a regex pass for "Part N", "Episode N", "#N", "N/N", "Day N", and a leading or trailing number; report the dominant scheme per playlist.
4. Compute per playlist: episode count, average gap in days between episodes, median duration, median views_per_day, and whether views rise or fall across episodes (Spearman rank correlation of episode order against views_per_day, computed in pure pandas).
5. Compute channel cadence: uploads per week for the last 26 weeks, most common weekday and hour (UTC, and also in the timezone I pass with --tz), longest gap in days.
6. Outputs: series.csv, cadence.csv, and cadence_report.md written in the section headings "Series structure", "Naming scheme", "Cadence", "What to model" (structure only, never titles).
7. Handle: no playlists, auto-generated playlists, private playlists, HTTP errors with one retry, and quota exceeded.

Deliver: the full script, requirements.txt, run commands for Windows and macOS/Linux, and 3 test cases with expected outcomes. Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `series_mapper.py`, CSV outputs, and a Markdown report you can paste into the cadence section of the Style Bible.
**If the output is weak:** ask for "a unit test file using a fake API response so I can test without spending quota".

## Done when

- You have chosen one tool and built it from its prompt.
- The tool passed all three test cases it listed, and you ran it once on your own channel or a public channel's metadata.
- Your API key is in Script Properties or an environment variable and in no shared file.
- Your quota counter shows you stayed well under 10,000 units on the test day.
- You wrote down which pattern or gap you will use in your next video, as structure and topic only.

## Next

Continue with [Script and voice tools](./02-ideas-script-and-voice.md).
