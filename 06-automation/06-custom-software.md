# Workflow C: Custom Software (Channel Workbench)

> Purpose: Design and build, with free tools and Claude as your pair programmer, one local app that holds the Channel Style Analyzer, the content queue with enforced gates, and the asset manager.
> Use when: Workflows A and B work, you have outgrown a spreadsheet, and you want rules enforced by software instead of by memory.
> Time needed: About 25 to 40 hours in total, one milestone per session of 2 to 5 hours (planning estimates, not measured).
> Needs: Python 3.11, a free Claude chat account (or any free coding assistant), `05-low-code-workflow.md` finished, a free GitHub account for version control.
> Cost: $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [HARDWARE], [WEEKLY_HOURS], [FACE_OR_FACELESS], [VOICE_MODE]
- The statuses, gates C1 to C8 and file names from `01-pipeline-architecture.md`, `03-bulk-systems.md` and `04-human-checkpoints.md`
- The starter analyzer in `07-build-your-own/05-channel-style-analyzer-starter.md`

## Decide first: do you need this?

Build Workflow C only if at least one of these is true: you run more than one channel, your sheet breaks regularly, you want gates the software refuses to skip, or you want to build software as a product of your own. If none is true, Workflows A and B are enough, and building software will take hours that should go into videos with real first-hand work in them.

## Architecture

The app is local-first. It runs on your computer at `http://localhost:8000`, stores data in one SQLite file, and keeps media in the same `workspace/` folder layout as `03-bulk-systems.md`. Local-first avoids hosting costs, keeps unpublished scripts private, and avoids storing API keys on someone else's server.

```
 Browser  http://localhost:8000
     |
 FastAPI app  --  Jinja2 HTML templates (no JavaScript build step)
     |
 services/
   analyzer   gates   assets   variation   metrics   exports   llm_client
     |
 data/workbench.db  (SQLite)          workspace/  (files, same layout as 03-bulk-systems.md)
     |
 llm_client (optional): Gemini free API tier, or a local model you run yourself.
 It receives topics, the Style Bible and your first-hand notes. It never receives pasted transcripts.
```

Three rules are built into the design. They exist for monetization and platform-policy reasons, not for style.

1. **No transcripts in generation.** Transcripts you paste are analysed once into style features. Script generation uses the [STYLE_BIBLE], never [TRANSCRIPT]. This keeps new content in the same family of style without carrying another creator's words.
2. **No scraping, no downloading.** The analyzer accepts text you paste from the public transcript panel and public metadata you type or fetch through the official Data API with a read-only key. The app has no module that downloads videos or crawls pages.
3. **No upload, schedule or publish code in v1.** The pipeline ends at `REVIEW_PASSED`. Publishing stays a person in YouTube Studio, or the private-upload script in `07-youtube-api-and-audit.md`.

## Data model

Paste this into `schema.sql`. It matches the statuses and gates used everywhere else in the repo.

```sql
PRAGMA foreign_keys = ON;

-- One row per channel you run. Mirrors the setup card variables.
CREATE TABLE projects (
  id INTEGER PRIMARY KEY,
  channel_name TEXT NOT NULL,
  niche TEXT, audience TEXT, language TEXT, country TEXT,
  face_or_faceless TEXT, voice_mode TEXT, weekly_hours REAL,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Channels you study (public pages only).
CREATE TABLE source_channels (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES projects(id),
  channel_url TEXT NOT NULL, name TEXT
);

CREATE TABLE source_videos (
  id INTEGER PRIMARY KEY,
  source_channel_id INTEGER NOT NULL REFERENCES source_channels(id),
  video_url TEXT NOT NULL, title TEXT, published_date TEXT,
  duration_seconds INTEGER,
  format TEXT CHECK (format IN ('long','short')),
  transcript_text TEXT,              -- pasted by you; used only for analysis, never exported
  added_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Observations, written as your own paraphrase. No long verbatim passages.
CREATE TABLE style_features (
  id INTEGER PRIMARY KEY,
  source_video_id INTEGER NOT NULL REFERENCES source_videos(id),
  feature_group TEXT NOT NULL,       -- hook, structure, pacing, audio, visuals, title, thumbnail
  feature_key TEXT NOT NULL,
  feature_value TEXT NOT NULL,
  evidence_note TEXT                 -- timestamp plus a paraphrase
);

CREATE TABLE style_bibles (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES projects(id),
  version INTEGER NOT NULL,
  body_md TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (project_id, version)
);

CREATE TABLE ideas (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES projects(id),
  topic TEXT NOT NULL,
  format TEXT CHECK (format IN ('long','short')),
  audience_question TEXT,
  first_hand_angle TEXT,
  value_stack_layers TEXT,
  state TEXT NOT NULL DEFAULT 'open' CHECK (state IN ('open','approved','killed'))
);

CREATE TABLE videos (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES projects(id),
  idea_id INTEGER REFERENCES ideas(id),
  slug TEXT NOT NULL UNIQUE,         -- L012-lentil-stew-under-3-dollars
  format TEXT NOT NULL CHECK (format IN ('long','short')),
  status TEXT NOT NULL DEFAULT 'IDEA' CHECK (status IN
    ('IDEA','APPROVED','SCRIPTED','SCRIPT_OK','VOICED','VISUALS_DONE','EDITED',
     'THUMB_DONE','META_DONE','REVIEW_PASSED','SCHEDULED','PUBLISHED','ANALYSED','HOLD','KILLED')),
  title TEXT, duration_minutes REAL,
  disclosure_decision TEXT,
  last_updated TEXT NOT NULL DEFAULT (datetime('now'))
);

-- One row per gate attempt. The history is never edited or deleted.
CREATE TABLE gates (
  id INTEGER PRIMARY KEY,
  video_id INTEGER NOT NULL REFERENCES videos(id),
  gate_code TEXT NOT NULL CHECK (gate_code IN ('C1','C2','C3','C4','C5','C6','C7','C8')),
  result TEXT NOT NULL CHECK (result IN ('pass','fail')),
  reviewer TEXT NOT NULL,
  note TEXT NOT NULL CHECK (length(trim(note)) >= 10),
  change_made TEXT,                  -- "one thing I changed because of this gate"
  minutes_spent REAL NOT NULL,
  rubric_score INTEGER,              -- C8 only
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE assets (
  id INTEGER PRIMARY KEY,
  video_id INTEGER REFERENCES videos(id),
  file_path TEXT NOT NULL,
  kind TEXT CHECK (kind IN ('image','video','audio','music','font','other')),
  source_tool TEXT, prompt_text TEXT, terms_url TEXT,
  commercial_ok TEXT NOT NULL DEFAULT 'unknown' CHECK (commercial_ok IN ('yes','no','unknown')),
  realistic_synthetic TEXT NOT NULL DEFAULT 'unknown' CHECK (realistic_synthetic IN ('yes','no','unknown')),
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE thumbnails (
  id INTEGER PRIMARY KEY,
  video_id INTEGER NOT NULL REFERENCES videos(id),
  variant TEXT NOT NULL CHECK (variant IN ('A','B','C')),
  template TEXT NOT NULL CHECK (template IN ('T1','T2','T3','T4','T5')),
  palette TEXT, overlay_text TEXT, file_path TEXT,
  attributes_changed INTEGER,        -- out of 8, versus the source thumbnail
  UNIQUE (video_id, variant)
);

CREATE TABLE variation_log (
  id INTEGER PRIMARY KEY,
  video_id INTEGER NOT NULL REFERENCES videos(id),
  variable TEXT NOT NULL,            -- for example hook_type, structure, template, palette
  value TEXT NOT NULL
);

CREATE TABLE metrics (
  id INTEGER PRIMARY KEY,
  video_id INTEGER NOT NULL REFERENCES videos(id),
  captured_on TEXT NOT NULL,
  views INTEGER, impressions INTEGER, ctr REAL,
  avg_view_duration_seconds REAL, avg_percent_viewed REAL, subscribers_gained INTEGER,
  UNIQUE (video_id, captured_on)
);
```

## Gate rules the software enforces

| Move to status | Requires |
|---|---|
| APPROVED | A `pass` row for C1, and the idea has `first_hand_angle` and `value_stack_layers` filled |
| SCRIPT_OK | A `pass` row for C2 |
| VOICED | A `pass` row for C3 |
| VISUALS_DONE | A `pass` row for C4, and no asset on the video with `commercial_ok` of `no` or `unknown` |
| THUMB_DONE | A `pass` row for C5, and each thumbnail row has `attributes_changed` of 4 or more (a rule of this repo) |
| META_DONE | `pass` rows for C6 and C7, and `disclosure_decision` filled |
| REVIEW_PASSED | A `pass` row for C8 with `rubric_score` of 80 or more and `minutes_spent` at least `duration_minutes` |
| SCHEDULED | Current status is REVIEW_PASSED |

Other rules: a status may move forward one step at a time, or to HOLD or KILLED. A gate row needs a reviewer name and a note of at least 10 characters. A gate row is never edited. A new attempt is a new row. At most 3 videos may sit between SCRIPT_OK and REVIEW_PASSED. These numbers are this repo's rules, not YouTube numbers.

## Module list

| Module | File | Responsibility |
|---|---|---|
| Database | `app/db.py` | Open SQLite, run `schema.sql`, helper functions |
| Setup | `app/routes/projects.py` | Store the setup card values |
| Analyzer | `app/services/analyzer.py` | Take pasted transcripts and metadata, run the analysis prompt, store `style_features`, assemble a new Style Bible version |
| Queue board | `app/routes/videos.py` | Show videos by status, create from approved ideas |
| Gate engine | `app/services/gates.py` | Apply the table above. Refuse illegal moves with a clear message |
| Asset manager | `app/services/assets.py` | Log assets, import `thumbnails/asset-log.csv`, flag unknown licences |
| Thumbnails | `app/routes/thumbnails.py` | Variants A, B and C, template rotation, attribute counter |
| Variation guard | `app/services/variation.py` | Compare a new video against the last five and report RED pairs |
| Metrics | `app/services/metrics.py` | Import the YouTube Studio CSV export, show per-video trends |
| Export | `app/services/exports.py` | Write the `Pipeline` sheet layout as CSV, write `review-log.md` for each video |
| LLM client | `app/services/llm_client.py` | One function `ask(prompt)`. Reads the provider and model from `.env`. Never receives transcripts for generation |
| Tests | `tests/` | pytest tests for gates, assets and variation |

Stack: Python 3.11, FastAPI, Jinja2, SQLite through the standard `sqlite3` module, pytest. These are free and open source (VERIFY BEFORE RELYING: licence on each project's page). Streamlit is a simpler alternative if you prefer a single script, at the cost of less control over routes and tests.

## Build order

| Milestone | Outcome | Estimate | Done when |
|---|---|---|---|
| M0 | Skeleton runs, schema loads, one test passes | 2 h | `pytest` passes and the home page loads |
| M1 | Projects, ideas and videos can be created and listed | 3 h | You can add an idea and promote it to a video row |
| M2 | Gate engine and review logs | 5 h | Every rule in the table has a failing and a passing test |
| M3 | Asset manager | 4 h | A video with an unknown-licence asset cannot reach VISUALS_DONE |
| M4 | Channel Style Analyzer | 6 h | A pasted transcript yields stored features and a Style Bible version |
| M5 | Variation guard and thumbnail rotation | 4 h | A repeated template three times in a row is flagged |
| M6 | Metrics import and feedback view | 4 h | A Studio CSV loads and a per-video table appears |
| M7 | Export, backup, packaging | 3 h | A fresh clone runs from the README in under 15 minutes |

## Steps

1. Create a private GitHub repository named `channel-workbench` and a folder with the same name.
2. Paste the schema above into `schema.sql`.
3. Open a new chat with Claude. Paste P-AUTO-14 (the project brief) as the first message, with [SCHEMA_SQL] replaced by the contents of `schema.sql`.
4. For each milestone, paste its prompt (P-AUTO-15 to P-AUTO-22) in order, replacing [CURRENT_FILES] with the full text of the files that milestone changes. Send only those files, not the whole project, so that the free chat does not run out of room (VERIFY BEFORE RELYING: current message and context limits of your free chat tier).
5. After each milestone, run `pytest`, run the app, tick the milestone's "Done when" line, and commit with a message such as `M2 gate engine`.
6. Start a new chat for each milestone. Paste P-AUTO-14 again first.
7. Do not start a milestone until the previous one passes its tests.

## Prompts

### P-AUTO-14 — Project Brief (paste first in every chat)

Purpose: Give the assistant the full context and non-negotiable rules for the app.
Inputs: [CHANNEL_NAME], [SCHEMA_SQL] (the SQL above).

```
You are a senior Python developer pair-programming with a beginner. We are building "Channel Workbench", a local-first app for a one-person YouTube channel named [CHANNEL_NAME].

Stack: Python 3.11, FastAPI, Jinja2 templates, SQLite via the standard sqlite3 module, pytest. No JavaScript build step. Everything must be free and open source.

Purpose: a Channel Style Analyzer, a content queue with enforced human checkpoints, and an asset manager.

Database schema (do not change it unless I ask): [SCHEMA_SQL]

Gate rules to enforce in code, not only in the interface:
- Statuses move forward one step at a time, or to HOLD or KILLED.
- APPROVED needs a pass row for C1 and a filled first_hand_angle and value_stack_layers on the idea.
- SCRIPT_OK needs C2. VOICED needs C3. VISUALS_DONE needs C4 and no asset whose commercial_ok is no or unknown. THUMB_DONE needs C5 and every thumbnail with attributes_changed of 4 or more. META_DONE needs C6 and C7 and a filled disclosure_decision. REVIEW_PASSED needs C8 with rubric_score of 80 or more and minutes_spent of at least duration_minutes. SCHEDULED needs REVIEW_PASSED.
- Gate rows need a reviewer and a note of at least 10 characters, and are never edited or deleted.
- At most 3 videos may sit between SCRIPT_OK and REVIEW_PASSED.

Hard rules for the whole project:
1. Never write code that uploads, schedules or publishes a video.
2. Never write code that downloads videos or audio, or crawls or scrapes web pages. Transcripts are pasted in by the user. Metadata may come only from the official YouTube Data API with a read-only key, or be typed in.
3. Never send pasted transcripts to any model for script generation. Transcripts are used only by the analyzer to produce style features written as paraphrase.
4. Never include code that clones a real person's voice or likeness.
5. Do not guess library versions, model names, or licence terms. If unsure, write VERIFY BEFORE RELYING and name the official page.
6. Every function gets a short comment written for a beginner. Return complete files, not fragments, unless I ask for a patch.
7. After each answer, give the exact terminal commands to run and the output I should see.

Reply only with: "Brief received. Send the milestone prompt."
```

Expected output: The single confirmation line.
If the output is weak: If the assistant starts writing code, reply "Do not write code yet. Confirm the brief only."

### P-AUTO-15 — Milestone M0: Skeleton

Purpose: Create the project skeleton, database loader and first test.
Inputs: [PROJECT_BRIEF] is already in the chat. No files yet.

```
Milestone M0. Create the project skeleton.
Deliver these complete files: requirements.txt (lower version bounds only), .gitignore (ignore .env, data/, __pycache__, .venv), .env.example (settings DB_PATH, WORKSPACE_DIR, LLM_PROVIDER, LLM_MODEL, LLM_API_KEY, all empty or with safe defaults), schema.sql (the schema from the brief), app/__init__.py, app/db.py (function get_connection that creates the data/ folder, opens SQLite with foreign keys on and rows as dictionaries, and applies schema.sql once), app/main.py (FastAPI app with a home page route that lists the count of videos per status), app/templates/base.html and app/templates/home.html (plain HTML, no CSS framework), tests/test_db.py (a test that builds an in-memory database from schema.sql, inserts one project and one video, and checks the status check constraint rejects an invalid status).
Then give: the commands to create a virtual environment, install packages, run pytest, and start the server with uvicorn, and the exact page and test output I should see.
```

Expected output: Eight files and the run commands.
If the output is weak: Paste the full error text and the file it names, and ask for a corrected file only.

### P-AUTO-16 — Milestone M1: Projects, Ideas, Videos

Purpose: Add the three basic record types with simple pages.
Inputs: [CURRENT_FILES] (app/db.py, app/main.py, app/templates/base.html, app/templates/home.html).

```
Milestone M1. Here are my current files: [CURRENT_FILES]
Add: a project setup page (create and edit one project from the setup card values), an ideas page (list, add, mark approved or killed; an idea cannot be marked approved unless first_hand_angle and value_stack_layers are filled), and a videos page (list by status; create a video from an approved idea with a slug that matches ^[LS][0-9]{3}-[a-z0-9]+(-[a-z0-9]+)*$ and an automatically increasing three-digit counter that is never reused, even for killed videos).
Do not add status changes yet. New videos start at IDEA.
Use plain HTML forms and POST routes with redirects. Put database functions in app/services/queries.py, not inside the routes.
Add pytest tests for: the slug rule, the counter never reusing a number, and the approval rule on ideas.
Return complete changed and new files, then the commands and expected output.
```

Expected output: New route files, templates, queries module and tests.
If the output is weak: Ask the assistant to list every file it changed before returning code, and check the list against what you pasted.

### P-AUTO-17 — Milestone M2: Gate Engine

Purpose: Make the checkpoint rules unskippable.
Inputs: [CURRENT_FILES] (app/db.py, app/services/queries.py, app/routes/videos.py, tests/).

```
Milestone M2. Here are my current files: [CURRENT_FILES]
Build app/services/gates.py with: record_gate(video_id, gate_code, result, reviewer, note, change_made, minutes_spent, rubric_score) that inserts a row and refuses a note shorter than 10 characters; and move_status(video_id, new_status) that applies every rule in the brief and raises a GateError with a plain-language message naming the missing gate or rule. Implement the one-step-forward rule, HOLD and KILLED from any status, and the limit of 3 videos between SCRIPT_OK and REVIEW_PASSED.
Add a video detail page with a form to record each gate and a button for each allowed next status. Show gate history newest first, and show the GateError message in red when a move is refused.
Add a function export_review_log(video_id) that writes review-log.md into workspace/videos/<slug>/ using this exact layout, with pass or fail typed after "pass/fail": the eight lines C1 to C8 in the form "C1 Idea:        date ____  pass/fail ____  note ____".
Write pytest tests: one failing and one passing case for every row of the gate rules, plus tests for the gate row never being editable and for the limit of 3.
Return complete files, commands and expected output.
```

Expected output: Gate engine, detail page, export function, tests.
If the output is weak: Ask for a table listing each rule, the function that enforces it, and the test that proves it. Any rule with no test is unfinished.

### P-AUTO-18 — Milestone M3: Asset Manager

Purpose: Log every outside asset with its licence status and block unsafe ones.
Inputs: [CURRENT_FILES] (app/services/gates.py, app/db.py, app/templates/video detail page).

```
Milestone M3. Here are my current files: [CURRENT_FILES]
Build app/services/assets.py and an assets page. Features: add an asset to a video (file_path, kind, source_tool, prompt_text, terms_url, commercial_ok, realistic_synthetic); list assets with a red badge for commercial_ok of no or unknown; import thumbnails/asset-log.csv with the columns file, tool, date, prompt, terms_url, commercial_ok (map file to file_path, tool to source_tool, prompt to prompt_text; treat any value other than yes as unknown); a per-video summary line saying how many assets are unsafe and how many are realistic synthetic media that need a disclosure decision.
Connect it to the gate engine: move_status to VISUALS_DONE must fail if any asset on the video has commercial_ok of no or unknown.
Never fetch a URL. terms_url is stored as text only.
Write tests for the CSV import (valid file, missing column, bad commercial_ok value) and for the VISUALS_DONE block.
Return complete files, commands and expected output.
```

Expected output: Asset module, page, CSV import, tests.
If the output is weak: Provide a sample CSV of five rows including one bad row and ask for the test cases to use it.

### P-AUTO-19 — Milestone M4: Channel Style Analyzer

Purpose: Turn pasted transcripts and metadata into stored style features and a Style Bible version.
Inputs: [CURRENT_FILES] (app/db.py, app/services/llm_client.py if it exists, tests/), the content of `07-build-your-own/05-channel-style-analyzer-starter.md` as [STARTER_NOTES], and the analysis prompt P-CDNA-01 from `01-channel-dna/02-channel-analysis.md` as [ANALYSIS_PROMPT].

```
Milestone M4. Here are my current files: [CURRENT_FILES]
Starter notes: [STARTER_NOTES]
The analysis prompt I already use by hand: [ANALYSIS_PROMPT]

Build: (1) a source page where I add a studied channel URL and add videos with url, title, published date, duration, format, and a large text box for a transcript I copied by hand from the public transcript panel; (2) app/services/llm_client.py with one function ask(prompt) that supports a Gemini free-tier API provider and a local-model provider chosen by LLM_PROVIDER in .env, retries on rate-limit errors with a growing wait, and raises a clear error if the model name is empty (do not invent model names); (3) app/services/analyzer.py with analyze_video(source_video_id) that sends the transcript with the analysis prompt, asks for JSON only, validates the JSON, and stores rows in style_features. The stored evidence_note must be a paraphrase with a timestamp. Reject any evidence_note that exceeds 15 words in a single quoted span; (4) build_style_bible(project_id) that takes all stored features, asks the model to write a new Style Bible in the template structure of 01-channel-dna/03-style-bible-template.md using features only, and saves it as the next version.
Safety rules: transcripts are sent only to analyze_video and nowhere else. No function may fetch a web page or download media. Add a visible notice on the source page that only transcripts the owner copied by hand from public pages should be pasted, and that the Style Bible, not the transcript, is what generation uses.
Write tests using a fake ask() function that returns canned JSON: valid JSON, invalid JSON, evidence_note over the word limit, and an empty model name.
Return complete files, commands and expected output.
```

Expected output: Source page, LLM client, analyzer, Style Bible builder, tests.
If the output is weak: Ask for the exact JSON schema the analyzer expects, and paste a real analysis result to check that the schema fits.

### P-AUTO-20 — Milestone M5: Variation Guard and Thumbnail Rotation

Purpose: Catch template-like sameness automatically.
Inputs: [CURRENT_FILES] (app/db.py, app/services/gates.py, tests/), and the template codes T1 to T5 and the 8 attributes from `04-thumbnails/` as [THUMB_RULES].

```
Milestone M5. Here are my current files: [CURRENT_FILES]
Thumbnail rules from my repo: [THUMB_RULES]

Build app/services/variation.py and a thumbnails page.
Thumbnails page: for a video, record variants A, B and C with template (T1 to T5), palette, overlay_text, file_path and attributes_changed (0 to 8). Warn if overlay_text has more than 4 words. Warn if attributes_changed is below 4. Warn if the same template was used on the last 2 published videos.
Variation guard: log values for the variables hook_type, structure, thumbnail_template and palette per video in variation_log. Function check_batch(video_ids) compares each video against the last five published videos and returns RED when two videos share the same hook_type AND the same structure, and RED when any video has no first_hand_angle. Show a table with RED rows highlighted.
Connect: move_status to THUMB_DONE fails if any thumbnail has attributes_changed below 4.
Write tests for each warning and each RED condition.
Return complete files, commands and expected output.
```

Expected output: Variation module, thumbnails page, tests.
If the output is weak: Paste three fake videos with identical hooks and ask the assistant to show the table the guard should print.

### P-AUTO-21 — Milestone M6: Metrics and Feedback

Purpose: Import analytics and show what held attention.
Inputs: [CURRENT_FILES] (app/db.py, tests/), and [CSV_SAMPLE] (the first 5 rows of a CSV you exported from YouTube Studio analytics, with channel-private numbers removed if you wish).

```
Milestone M6. Here are my current files: [CURRENT_FILES]
Here are the first rows of a real YouTube Studio analytics export: [CSV_SAMPLE]

Build app/services/metrics.py: import_csv(path) that reads this exact format (detect columns by header names, not position, and tell me which headers it could not find), matches each row to a video by title or by a video id column if present, stores rows in metrics, and reports unmatched rows instead of guessing. Add a page with a per-video table (views, impressions, CTR, average view duration, average percent viewed, subscribers gained) and a page that groups videos by hook_type and by thumbnail template and shows the averages with the number of videos behind each average. Print a plain note when a group has fewer than 5 videos: "too few videos to conclude".
Do not call any YouTube API in this milestone.
Write tests for header detection, unmatched rows, and the "too few videos" note.
Return complete files, commands and expected output.
```

Expected output: Import function, pages, tests.
If the output is weak: Ask the assistant to print the header-detection result for your CSV before writing the import.

### P-AUTO-22 — Milestone M7: Export, Backup, Packaging

Purpose: Make the project safe to back up and easy to rebuild.
Inputs: [CURRENT_FILES] (app/services/exports.py if it exists, app/db.py, README if it exists).

```
Milestone M7. Here are my current files: [CURRENT_FILES]
Build: (1) app/services/exports.py with export_pipeline_csv(path) that writes the 22 columns of my Google Sheet Pipeline tab (slug, format, status, topic, audience_question, first_hand_angle, value_stack_layers, outline, script_draft, script_final_link, factcheck_notes, voice_file, thumb_text, title, description, disclosure_decision, orig_score, reviewer_initials, scheduled_date, publish_url, notes, last_updated) from the database, leaving columns the database does not hold empty; (2) a backup command, python -m app.backup, that copies data/workbench.db to a dated file in a backups/ folder and keeps the 10 newest; (3) a README.md with install steps for Windows, macOS and Linux, how to run, how to back up, how to run the tests, and a "what this app will never do" section listing: no uploading, no scheduling, no publishing, no downloading, no scraping; (4) a final test that creates a fresh database, runs a full fake video from IDEA to REVIEW_PASSED through the gate engine with all gates recorded, and confirms SCHEDULED is allowed only after that.
Return complete files, commands and expected output.
```

Expected output: Export, backup, README, end-to-end test.
If the output is weak: Ask for the end-to-end test alone first and make it pass before the README.

## Testing checklist

Run all of these before you trust the app with real work.

- [ ] `pytest` passes, and each gate rule has one failing and one passing test.
- [ ] A fresh clone, following only the README, runs in under 15 minutes.
- [ ] A video cannot jump from IDEA to SCHEDULED by any route, including by editing the URL or the form by hand.
- [ ] A gate row with a short note, no reviewer, or a minutes value below the C8 floor is refused.
- [ ] A video with one unknown-licence asset is blocked at VISUALS_DONE.
- [ ] Three videos with the same hook type and structure produce a RED line.
- [ ] Search the code for `insert(`, `requests.get`, `urllib`, `yt_dlp` and `youtube-dl`. The only network call allowed is inside `llm_client.py`.
- [ ] No prompt sent for script generation contains any `transcript_text` value.
- [ ] `.env` and `data/` are in `.gitignore`, and `git status` shows neither.
- [ ] You restored a backup into a fresh database and the video list matched.
- [ ] Stopping the app mid-write does not corrupt the database (SQLite transaction test).

## Free hosting options (verify before relying)

Keep the app local unless you have a reason not to. The table lists what the sources I checked on 2026-10-20 say, and they disagree on some points, so open each pricing page before choosing.

| Option | Reported free limits | Traps | Suits this app? |
|---|---|---|---|
| Your own computer | No limits | Needs the computer on. Back up the SQLite file | Yes, recommended |
| GitHub Pages | Free static hosting | Static only, no Python backend, and a public site | No (use for a public notes page only) |
| Cloudflare Pages | Reported free static hosting with unlimited bandwidth | Static only. Server code runs as Workers (reported 100,000 requests per day, 10 ms CPU per request) in JavaScript or TypeScript, not Python | No for this build |
| Render free web service | Reported 512 MB RAM, spins down after 15 minutes without traffic, cold start of about 30 to 60 seconds. One source in my search said the free web service was removed | The local disk is lost on spin-down, so SQLite would be wiped. VERIFY BEFORE RELYING that the tier still exists | Not with SQLite |
| Vercel Hobby | Reported 100 GB bandwidth | Reported as personal, non-commercial use only, which rules out a monetized channel's tooling | No |
| Supabase free | Hosted Postgres | Reported to pause an inactive free project after about a week | Only after you rewrite the data layer |

Do not host the app publicly. It would hold your unpublished scripts, your analytics, and possibly API keys. If you later add YouTube Data API features, hosting an app for other users brings YouTube API Services policy obligations (see `07-youtube-api-and-audit.md`).

## Done when

- [ ] All milestones M0 to M7 are committed with passing tests.
- [ ] The app enforces every row of the gate rules table, tested.
- [ ] The analyzer stores features as paraphrase and the Style Bible is the only input to script generation.
- [ ] No code path in the project uploads, schedules, publishes, downloads or scrapes.
- [ ] You ran one real video through the app from IDEA to REVIEW_PASSED.
- [ ] A restore from backup works.

## Next

[07-youtube-api-and-audit.md](07-youtube-api-and-audit.md)
