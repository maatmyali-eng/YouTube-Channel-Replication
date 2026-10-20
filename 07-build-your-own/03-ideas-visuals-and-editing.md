# Build Your Own, Part 3: Visuals and Editing Tools

> Purpose: five tools for captions, free-licensed footage, license records, thumbnails, and pacing checks | Use when: you make videos every week and want the repeatable parts automated | Time needed: 2 to 4 hours per tool | Needs: Python 3.11 or later, FFmpeg, a free Claude or Gemini chat | Cost: $0

## Inputs

- [FACE_OR_FACELESS], [VOICE_MODE], [HARDWARE], [VIDEO_LENGTH], [LANGUAGE] from the setup card.
- [STYLE_BIBLE] sections on color, typography, editing rhythm, and thumbnail composition (`01-channel-dna/03-style-bible-template.md`).
- The thumbnail rules and template codes from `04-thumbnails/01-thumbnail-dna-analysis.md` and `04-thumbnails/03-design-workflow-and-templates.md` for P-BUILD-14.

## Steps

1. Install the shared tools once:
   1. FFmpeg (free, open source). Windows: download a build from ffmpeg.org/download.html, unzip to `C:\ffmpeg`, add `C:\ffmpeg\bin` to PATH (Start → "Edit the system environment variables" → Environment Variables → Path → Edit → New). macOS: `brew install ffmpeg`. Linux: `sudo apt install ffmpeg`. Check with `ffmpeg -version`. The licence depends on the build you download (LGPL or GPL); VERIFY BEFORE RELYING on ffmpeg.org/legal.html. Using FFmpeg to process your own video does not put your video under its licence.
   2. Python packages are named inside each prompt. Always create a virtual environment first: `python -m venv .venv`, then activate it (Windows `.venv\Scripts\activate`; macOS and Linux `source .venv/bin/activate`).
2. Free stock footage and images: the Pexels License allows free commercial use without attribution, but you may not sell unmodified copies or redistribute the files as a stock collection, and recognisable people or trademarks can still create separate problems (verified 2026-10-20, pexels.com/terms-of-service and secondary summaries). The Pexels API default limit is 200 requests per hour and 20,000 per month, with a free path to higher limits if you meet their API terms, and their API documentation asks that you show a prominent link to Pexels when you use it (verified 2026-10-20, pexels.com/api/documentation). Pixabay now uses its own Pixabay Content License (free commercial use, no standalone redistribution; verified 2026-10-20, secondary source; VERIFY BEFORE RELYING at pixabay.com/service/license-summary). Licenses change, so P-BUILD-13 stores a dated copy of the license for every asset.
3. Not allowed anywhere in this repo: downloading other creators' clips, music, or thumbnails to reuse or edit. Everything these tools process is your own footage, your own AI-generated or self-made graphics (check the generator's terms for commercial use), or free-licensed material with a stored license record.
4. Build in this order if you are unsure: P-BUILD-13 (license archiver) first, because it protects everything else; then P-BUILD-12, P-BUILD-11, P-BUILD-15, and P-BUILD-14.
5. For each prompt: paste it into a fresh chat, replace the bracketed inputs, save the files it returns, run its three test cases, and only then use the tool on real work.
6. Keep API keys in environment variables (Windows: `setx PEXELS_API_KEY "your-key"` then reopen the terminal; macOS and Linux: add `export PEXELS_API_KEY="your-key"` to `~/.zshrc` or `~/.bashrc`). Never put keys in a file you commit.

## Prompts

### P-BUILD-11 — Caption Styler

- What it does: converts a Whisper or editor-made `.srt` into a styled `.ass` subtitle file (font, size, outline, highlight word, safe margins) and optionally burns it into the video with FFmpeg.
- Why it helps: one style file gives every video the same caption look from your Style Bible, in seconds instead of manual work in an editor.
- Free stack: Python 3.11 standard library, FFmpeg, free fonts (Google Fonts, Open Font License; VERIFY BEFORE RELYING on each font's licence page).
- Difficulty: easy to medium. Time to build: 2 to 3 hours.
- Risks: policy: none; license: burned-in captions use your chosen font, so use only fonts with a free commercial licence; quality: auto-generated timings need a human read for names and numbers.

**Purpose:** consistent caption styling from a style file.
**Inputs:** [STYLE_BIBLE] (caption and typography section), [VIDEO_LENGTH], [FACE_OR_FACELESS], [FONT_NAME] (a font you installed), [CAPTION_STYLE] (see prompt).

```
You are a senior Python developer who knows the ASS subtitle format and FFmpeg. Build "caption_styler.py" at $0.

Usage: python caption_styler.py --srt captions.srt --style style.json --out captions.ass [--burn video.mp4 --burn-out video_captions.mp4]

Style input: a JSON file whose fields I define from my Style Bible: font name [FONT_NAME], font size, primary color, outline color, outline width, shadow, bold true/false, alignment (bottom-center or middle-center), vertical margin in pixels, max characters per line, max lines, highlight color, and the mode: "line" (whole line appears) or "word" (current word highlighted using ASS karaoke tags with timing split evenly across the words of each cue). My caption style description: [CAPTION_STYLE].

Requirements:
1. Parse SRT robustly (blank lines, BOM, Windows line endings, multi-line cues).
2. Re-wrap text to the max characters and max lines without splitting a word; if a cue exceeds max lines, split the cue in time proportionally to character count.
3. Provide two presets in the script: "horizontal" (1920x1080) and "vertical" (1080x1920, larger margins to keep text clear of the app interface; state that the safe area is my working number and VERIFY BEFORE RELYING on current platform UI overlays).
4. Write valid ASS with a [Script Info] block that sets PlayResX and PlayResY correctly for the preset, a [V4+ Styles] block, and [Events].
5. For --burn, run FFmpeg with the subtitles filter (escape Windows paths correctly), copy audio without re-encoding, use libx264 with crf 20 and preset medium, and print the exact command before running.
6. Add a "--check" mode that reports cues longer than 7 seconds, cues with more than 42 characters per line, overlaps, and cues starting before 0.
7. Handle: missing FFmpeg, missing font (warn that FFmpeg will substitute), empty SRT, invalid JSON, and times beyond the video duration.

Deliver: the full script, a sample style.json for horizontal and one for vertical, install steps for FFmpeg on Windows, macOS and Linux, and 3 test cases with exact expected output (a 3-cue SRT, a cue that needs splitting, a missing font). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `caption_styler.py`, two sample `style.json` files.
**If the output is weak:** paste the ASS file it produced and the FFmpeg error and ask for the corrected function only.

### P-BUILD-12 — Free-Licensed B-Roll Finder

- What it does: takes a shot list line by line, searches Pexels (and optionally Pixabay or Openverse) through their official APIs, shows previews and links, and saves the chosen clip with its license record.
- Why it helps: it replaces an hour of browsing with a ranked shortlist and makes the license trail automatic.
- Free stack: Python 3.11, `requests`, free Pexels API key (pexels.com/api, instant after sign-up), optional free Pixabay API key.
- Difficulty: medium. Time to build: 3 to 4 hours.
- Risks: ToS: stay within 200 requests per hour and 20,000 per month, do not work around limits, follow the API's attribution-link request (verified 2026-10-20); policy: stock-only visuals with a text-to-speech voice are a flagged high-risk format in this repo, so the finder is for supporting footage that sits inside original commentary, demonstration or analysis, never as the whole video; license: model and trademark issues remain your responsibility.

**Purpose:** a shot-list-to-footage search with license records.
**Inputs:** [SHOT_LIST_PATH] (one description per line), [FACE_OR_FACELESS], [NICHE], [ORIENTATION] (landscape or portrait), [MIN_SECONDS] (default 5).

```
You are a senior Python developer. Build "broll_finder.py" at $0 with Python 3.11, requests, and the standard library.

Usage: python broll_finder.py --shots [SHOT_LIST_PATH] --orientation [ORIENTATION] --min-seconds [MIN_SECONDS] --out broll/

The shot list has one visual description per line, for niche [NICHE]. Credentials from environment variables PEXELS_API_KEY and optionally PIXABAY_API_KEY.

Requirements:
1. For each line, extract 2 to 4 search keywords with a simple rule (drop stopwords, keep nouns by position; no AI call), then query the Pexels video search endpoint (https://api.pexels.com/videos/search) with orientation, size=medium, per_page=8. If PIXABAY_API_KEY is set, query Pixabay's video endpoint too. Do not call any other site.
2. Respect limits: keep a local file rate_state.json counting requests in the last hour and this month; stop before 180 requests per hour and 19,000 per month; read the X-Ratelimit headers when present; on HTTP 429 stop and print when to resume.
3. Filter out clips shorter than [MIN_SECONDS] and clips below 1280 pixels on the long side.
4. Write broll/shortlist.csv with one row per candidate: shot number, shot text, source, clip ID, page URL, creator name, duration, resolution, preview image URL, download URL of the preview-size file, license name, license page URL.
5. Write broll/shortlist.html: a simple page that lists each shot with its candidates' preview images as links (no scripts, no external assets) and a checkbox column I can tick; a footer line with a visible link to Pexels and Pixabay as their API terms request.
6. A second command: python broll_finder.py --pick broll/shortlist.csv --ids 12,18,31 downloads only the chosen clips into broll/chosen/ using the download URLs from the API, and appends one row per clip to broll/chosen/license_log.csv with fields: file name, source, clip ID, page URL, creator, license name, license page URL, date retrieved (UTC ISO). Do not download anything that was not picked.
7. Add a note at the top of every output file: "Check recognizable people and trademarks in each clip before use."
8. Handle: empty results, invalid key, network errors with one retry, and duplicate clips across shots.

Deliver: full script, requirements.txt, setup steps for the Pexels key and environment variables on Windows, macOS and Linux, and 3 test cases with exact expected results. Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `broll_finder.py`, a CSV, an HTML shortlist, and a license log.
**If the output is weak:** ask "show me only the rate-limit code and the exact response headers you read, and fix any assumption not in the Pexels documentation".

### P-BUILD-13 — License-Proof Archiver

- What it does: for every outside asset you use (stock clip, image, music file, font, template) it records the source URL, creator, license name, a dated copy of the license text, the file's SHA-256 hash, and the video it was used in.
- Why it helps: if a claim or question ever comes, you have a dated record; it also stops you from reusing an asset whose license changed.
- Free stack: Python 3.11 standard library, plus a CSV or SQLite file. Optional Google Sheets view.
- Difficulty: easy. Time to build: 2 hours.
- Risks: legal: the archive is evidence of what you saw, not a legal guarantee; ToS: save only the license text and page metadata, not whole site copies; policy: it has no effect on YouTube's reused-content rules, which depend on how much original value you add.

**Purpose:** a license evidence log.
**Inputs:** [ASSET_FOLDER], [VIDEO_TITLE_OR_ID] (the video each asset belongs to).

```
You are a senior Python developer. Build "license_archive.py" at $0 using only the Python standard library (sqlite3, hashlib, csv, argparse, urllib.request, datetime, pathlib).

Commands:
1. add: python license_archive.py add --file path --source-url URL --creator "Name" --license "License name" --license-url URL --video "[VIDEO_TITLE_OR_ID]" [--notes "text"]
   - Compute SHA-256 and file size.
   - Fetch the license URL with urllib (one request, 10-second timeout, a descriptive User-Agent) and save the text as licenses/YYYY-MM-DD_<domain>.html, plus a plain-text extraction with tags stripped to .txt. If the fetch fails, record "license text not saved" and keep going.
   - Insert one row into SQLite database archive.db and append to archive.csv.
2. scan: python license_archive.py scan --folder [ASSET_FOLDER] lists files in the folder that have no matching hash in the database ("unlogged assets") and exits with code 1 if any exist.
3. report: python license_archive.py report --video "[VIDEO_TITLE_OR_ID]" writes reports/<video>_licenses.md with a table of every asset used, source, creator, license, date retrieved, and a line "Attribution required: yes/no/check" based on a field I set with --attribution yes|no|check (default check).
4. recheck: python license_archive.py recheck --older-than 180 re-fetches license URLs for rows older than 180 days and flags any whose text hash changed.
5. A simple allowlist file allowed_licenses.txt with one license name per line; "add" warns when the license name is not on the list and asks for confirmation (--yes to skip).

Schema fields: id, file_name, sha256, size_bytes, source_url, creator, license_name, license_url, license_text_path, license_text_sha256, video, attribution, notes, date_retrieved_utc.

Handle: duplicate hashes (warn, do not duplicate), missing files, unreachable URLs, non-UTF-8 pages.

Deliver: the full script, an example allowed_licenses.txt (Pexels License, Pixabay Content License, CC0, CC BY 4.0, Open Font License 1.1, and a note that I must read each license myself), run commands, and 3 test cases with expected output (add and report, scan with one unlogged file, recheck with a changed page). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `license_archive.py`, a database, CSV and dated license copies.
**If the output is weak:** ask for a SQL query list for the 5 reports you need (all assets of one video, assets by license, unlogged assets, stale rows, duplicate hashes).

### P-BUILD-14 — Batch Thumbnail Composer

- What it does: builds several thumbnail variants from a template (background, subject cut-out you own or generated, title text, one accent shape) so you can compare options quickly.
- Why it helps: layout, text size, and color are fixed by your rules, so every variant is on-brand and you only vary one element at a time for testing.
- Free stack: Python 3.11, `Pillow` (HPND licence; VERIFY BEFORE RELYING), free fonts, your own or generated art.
- Difficulty: medium. Time to build: 3 to 4 hours.
- Risks: policy: no misleading imagery, no fake UI, no real person's face or logo you have no right to use; license: confirm the commercial terms of any AI image generator you use; copying: do not trace or recreate another creator's thumbnail layout pixel for pixel, use composition principles only.

**Purpose:** a template-driven thumbnail variant generator.
**Inputs:** [THUMB_RULES] (paste the rules from your thumbnail DNA and templates files: colors, safe zones, text length, subject placement, and template codes), [CHANNEL_NAME], [FACE_OR_FACELESS], [FONT_NAME].

```
You are a senior Python developer and graphic designer. Build "thumb_composer.py" at $0 using Python 3.11 and Pillow only.

Rules I follow (paste of my thumbnail rules): [THUMB_RULES]. Channel: [CHANNEL_NAME]. Face or faceless: [FACE_OR_FACELESS]. Font file: [FONT_NAME] (a .ttf or .otf in the fonts folder).

Usage: python thumb_composer.py --config jobs.json --out out/

jobs.json is a list of jobs. Each job has: id, title_text (the on-image text), template (one of the codes from my rules), background_image path, subject_image path (PNG with transparent background, optional), accent_color hex, text_color hex, and a "variants" list. Each variant changes exactly ONE of: text_color, accent_color, subject_side (left or right), subject_scale, title_text_alt, crop_zoom.

Requirements:
1. Output 1280x720 JPEG at quality 90, under 2 MB each (if larger, reduce quality in steps of 5 until under 2 MB; state that I must VERIFY BEFORE RELYING on current YouTube thumbnail size and format limits at support.google.com/youtube).
2. Fit text by shrinking font size until it fits the safe text box defined in my rules; never exceed the maximum word count in my rules (the script must read it from a constant I set at the top and refuse longer text).
3. Draw text with a stroke and optional shadow; draw one accent shape (bar, circle, or arrow) defined by the template code.
4. Run automatic checks and write checks.csv: text contrast ratio (WCAG formula) against the average color behind the text box; text box inside the safe zone; the bottom-right corner area kept clear for the video duration badge (my working number: 12 percent width, 8 percent height, VERIFY the current overlay); thumbnail readable at 168x94 pixels (render the small version and report the pixel height of the text).
5. Export a contact sheet contact_<id>.jpg showing all variants side by side with labels A, B, C, and so on.
6. Write out/<id>_test_plan.md stating which single element differs between variants, so my A/B result can be read cleanly.
7. Handle: missing fonts, missing images, transparent background errors, non-RGB images, and very long text.

Deliver: the full script, requirements.txt, a sample jobs.json with 2 jobs and 3 variants each for the niche "home cooking on a budget" that uses placeholder images created by the script itself (solid color gradients and a drawn plate icon), and 3 test cases with expected results. Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `thumb_composer.py`, a sample `jobs.json`, contact sheets, a checks file.
**If the output is weak:** ask for "a --debug mode that draws the safe zones and text box as colored rectangles on each output".

### P-BUILD-15 — Visual Pacing Linter

- What it does: analyses your rough cut with FFmpeg scene detection and silence detection, then flags long static stretches, missing visual changes, and dead air against your Style Bible's editing rhythm.
- Why it helps: retention drops often follow long, unchanged screens; the linter lists the exact timestamps to fix before export.
- Free stack: FFmpeg, ffprobe, Python 3.11 standard library.
- Difficulty: medium. Time to build: 3 hours.
- Risks: none on policy; accuracy: scene detection reads cuts and strong changes, not meaning, so a motion graphic that changes slowly can look static.

**Purpose:** check a rough cut against your editing-rhythm rules.
**Inputs:** [STYLE_BIBLE] (editing rhythm: average seconds per shot, maximum seconds without a visual change), [VIDEO_LENGTH], [VIDEO_PATH].

```
You are a senior Python developer who knows FFmpeg filters. Build "pacing_lint.py" at $0 using Python 3.11 standard library, FFmpeg and ffprobe.

Usage: python pacing_lint.py --video [VIDEO_PATH] --max-static 8 --target-avg 4.5 --scene-threshold 0.30 --silence-db -35 --silence-min 1.2

The numbers above are defaults; I will replace them with the values from my Style Bible editing-rhythm section: [STYLE_BIBLE]. Total expected length: [VIDEO_LENGTH].

Steps:
1. Get duration with ffprobe.
2. Detect scene changes by running ffmpeg with the select filter "select='gt(scene,THRESHOLD)',showinfo" and parse pts_time values from stderr.
3. Detect silence with the silencedetect filter and parse silence_start and silence_end.
4. Detect near-freeze segments with the freezedetect filter (n=-60dB, d=3).
5. Compute: number of visual changes, average seconds between changes, the longest stretch without a change, all stretches longer than --max-static, silences longer than --silence-min (excluding the first 0.5 seconds and the last 1 second), and freeze segments.
6. Make a pacing timeline: a plain-text bar of 60 characters per minute with "|" at each change, so I can see density.
7. Write reports/pacing_report.md with a PASS, REVIEW or FAIL line (PASS: average within 25 percent of target and no stretch over max-static; REVIEW: one of them off; FAIL: both off). State that these rules are my Style Bible's, not YouTube's.
8. Write reports/pacing_flags.csv with timecode (HH:MM:SS), type, duration and a suggested fix from this fixed list: "add b-roll", "add on-screen text", "zoom or reframe", "cut the pause", "insert a diagram", "split the shot".
9. Handle: missing FFmpeg, no audio stream, videos over 60 minutes (warn about time), and files with variable frame rate.

Deliver: the full script, install checks, run commands for Windows, macOS and Linux, and 3 test cases with expected results (a clip with cuts every 3 seconds, a 20-second still image, a video with a 5-second silence). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `pacing_lint.py` and a pacing report with timecodes.
**If the output is weak:** paste the FFmpeg stderr from one run and ask for the parsing regexes to be corrected against that real text.

## Done when

- P-BUILD-13 is built and every outside asset in your last video has a row, a dated license copy, and a hash.
- At least one of the other four tools passed its three test cases on real footage or real art.
- Every Pexels or Pixabay request you made stayed inside the free limits (check `rate_state.json`).
- Your caption style and thumbnail rules live in files, not in your head.
- No clip, track, font, or image in your video lacks a license record or an "own work" note.

## Next

Continue with [Publishing and analytics tools](./04-ideas-publishing-and-analytics.md).
