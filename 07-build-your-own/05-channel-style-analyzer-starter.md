# Build Your Own, Part 5: Channel Style Analyzer Starter

> **Purpose:** build a local tool that measures a channel's public style and assembles a Style Bible in the exact format of your template  
> **Use when:** you model a new channel and want the analysis repeatable  
> **Time needed:** 1 to 2 days across milestones  
> **Needs:** Python 3.11 or later, a free Claude or Gemini chat, optionally a free YouTube Data API key  
> **Cost:** $0

## Inputs

- [CHANNEL_URL], [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE] from the setup card.
- [STYLE_BIBLE_TEMPLATE_TEXT]: the full text of `01-channel-dna/03-style-bible-template.md`, pasted into the starter prompt. The tool reads its headings at run time, so the output always matches your template, even after you edit the template.
- 8 to 15 transcripts of the source channel's videos, copied by hand from the on-page transcript panel (see `01-channel-dna/01-data-gathering.md`), saved as `data/transcripts/<video_id>.txt`.
- Optional: a free YouTube Data API key (steps in `07-build-your-own/01-ideas-research-and-ideation.md`).

## Steps

1. Create the project folder `channel-style-analyzer` and open a terminal there. Run `python -m venv .venv` and activate it (Windows `.venv\Scripts\activate`; macOS and Linux `source .venv/bin/activate`).
2. Copy the contents of `01-channel-dna/03-style-bible-template.md`. You will paste it in place of [STYLE_BIBLE_TEMPLATE_TEXT] in P-BUILD-21.
3. Open a new free chat, paste P-BUILD-21 with the brackets filled in, and let it build milestone M0. Save each file it returns. Then reply "continue" for M1, and so on through M7. Run each milestone's tests before asking for the next one.
4. Collect source data by hand and by the official API only:
   1. Transcripts: on a video's public watch page open the description → "Show transcript", select the text, copy it, paste it into `data/transcripts/<video_id>.txt`. Transcripts are copyrighted text. Keep them local, add `data/` to `.gitignore`, never upload them to a public place, and delete them when your Style Bible is finished and checked.
   2. Metadata: let the tool call the official Data API with your key (optional), or paste titles and dates into `data/metadata.csv` by hand.
   3. Thumbnails: look at them in the browser and write notes in `data/thumbnail_notes.csv`. Do not download or edit another creator's thumbnails.
5. Run the pipeline: `python analyzer.py init`, then `collect`, `measure`, `pack`. Paste each file in `packs/` into a free chat one at a time and save each reply as `responses/<same number>.md`. Then run `assemble` and `lint`.
6. Read the final `output/style_bible.md` with the template open next to it. Every template heading must be present, in order, and no sentence of more than 8 words may be copied from the source. Fix any weak section with the "If the output is weak" step of the prompt that built it, or with the follow-up prompt P-BUILD-22.
7. Use the result as [STYLE_BIBLE] in every later prompt in this repo.

## Prompts

### P-BUILD-21 — Channel Style Analyzer: Full Starter Prompt

- What it does: builds a local Python command-line tool, in milestones M0 to M7, that measures a channel's style from transcripts and public metadata, prepares prompts for a free AI chat, and assembles a Style Bible with the same headings as your template.
- Why it helps: it makes the channel analysis repeatable for any channel, keeps measured facts separate from AI opinion, and lints the output so the Style Bible contains style, not source text.
- Free stack: Python 3.11 standard library plus `requests` (optional, for the YouTube Data API) and `pytest` for tests. No paid service, no database server, no web framework.
- Difficulty: medium to hard. Time to build: 1 to 2 days.
- Risks: ToS: transcripts come from the public watch page by hand and metadata from the official API only, no downloading videos and no scraping; copyright: source transcripts are private working files, deleted after use, and the Style Bible must not carry source sentences; policy: the tool models style, structure, and pacing, and produces nothing that reuses another creator's words, voice, footage, or branding.

**Purpose:** a repeatable, $0 analyzer that outputs a template-matching Style Bible.
**Inputs:** [CHANNEL_URL], [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [FACE_OR_FACELESS], [VOICE_MODE], [STYLE_BIBLE_TEMPLATE_TEXT] (the full text of my Style Bible template), [MAX_TRANSCRIPTS] (default 15).

```
You are a senior Python engineer and a careful technical writer. Build a tool called "Channel Style Analyzer" with me, one milestone at a time. Everything must cost $0. Use Python 3.11, the standard library, and only these third-party packages: requests (optional, for the YouTube Data API) and pytest (tests). No databases other than plain files, no web framework, no paid API, no browser automation, no scraping.

PURPOSE
Measure the style of one YouTube channel from public information, then assemble a Style Bible whose headings and order exactly match my template. The Style Bible describes style, structure, and rules for creating NEW content. It must never contain another creator's sentences.

CONTEXT
Channel to model: [CHANNEL_URL] ([CHANNEL_NAME]). Niche: [NICHE]. Audience: [AUDIENCE]. Language: [LANGUAGE]. Face or faceless: [FACE_OR_FACELESS]. Voice mode: [VOICE_MODE]. Up to [MAX_TRANSCRIPTS] transcripts.

MY STYLE BIBLE TEMPLATE (the tool must parse this at run time and reproduce its headings in the same order; do not hard-code any heading):
[STYLE_BIBLE_TEMPLATE_TEXT]

DATA RULES (state them in the README the tool writes)
- Transcripts are copied by hand from the public watch page's transcript panel into data/transcripts/<video_id>.txt. The tool never downloads video or audio.
- Metadata comes from the official YouTube Data API (key in environment variable YT_API_KEY) or from a hand-made data/metadata.csv. The tool uses videos.list, channels.list and playlistItems.list only, never search.list, never comment endpoints. State that I must VERIFY BEFORE RELYING on the API terms at developers.google.com/youtube/terms/developer-policies, including any limit on how long data may be stored.
- Thumbnails are described by me in data/thumbnail_notes.csv. The tool never downloads thumbnails.
- data/ and output/ go in .gitignore. The README says: delete data/transcripts when the Style Bible is final.

OUTPUTS
- data/metrics.json: measured numbers per video and a channel summary.
- packs/NN.md: one prompt file per top-level section (second-level heading, or first-level if the template has no second-level headings) of the template, each containing the measured facts that section needs and a fill-in instruction.
- output/style_bible.md: the assembled Style Bible, same headings in the same order as the template.
- output/lint_report.md: results of the checks in M6.

FILE STRUCTURE (create exactly this)
channel-style-analyzer/
  analyzer.py                (command-line entry: init, collect, measure, pack, assemble, lint, all)
  analyzer/__init__.py
  analyzer/config.py         (paths, constants, thresholds, all editable, each labelled "working number")
  analyzer/template.py       (parse the template into sections; keep order, heading level, and any instruction text)
  analyzer/transcripts.py    (load and clean transcript files; parse timestamps)
  analyzer/metrics.py        (all measurements)
  analyzer/metadata.py       (API collection and CSV loading; title patterns; cadence)
  analyzer/packs.py          (build the section packs)
  analyzer/assemble.py       (merge responses into the Style Bible)
  analyzer/lint.py           (validation checks)
  tests/fixtures/            (invented sample transcripts, a 3-section sample template, a sample metadata.csv)
  tests/test_*.py
  data/transcripts/  data/thumbnail_notes.csv  data/metadata.csv
  packs/  responses/  output/
  README.md  requirements.txt  .gitignore

MILESTONES (build one per reply, then stop and wait for me to say "continue"; each milestone ends with exact run commands, the files created, and the tests to run)
M0 Skeleton: folder tree, config.py, the CLI with sub-commands that print "not built yet", README with the data rules, .gitignore, requirements.txt, and a pytest smoke test.
M1 Template parser: template.py reads my template text from data/style_bible_template.md, returns an ordered list of sections with level, heading text, any bullet or blank-field instructions, and any placeholder tokens in square brackets; `analyzer.py init` writes that file from stdin or from a path argument and prints the heading outline.
M2 Transcript loader and cleaner: handle timestamp lines such as "0:32" or "01:15:04" on their own line followed by text, or inline "[0:32]"; remove music tags like [Music], [Applause]; produce a list of timed segments; compute words per minute when timestamps exist; handle missing timestamps by treating the file as untimed.
M3 Metrics: per video and channel summary: word count; duration if known; words per minute; sentence count; mean, median, and standard deviation of sentence length in words; question share; exclamation share; second-person rate per 100 words (you, your, yours, yourself; adapt to [LANGUAGE] with a small editable word list in config); first-person rate; contraction rate; number tokens per 100 words; the 15 most common sentence starters; reading ease (Flesch, English only, otherwise "n/a"); hook window metrics for the first 30 seconds (or first 80 words if untimed): word count, question count, number count, second-person rate; open-loop markers per 1,000 words using an editable phrase list (examples: "in a moment", "later in this video", "we'll get to", "stick around", "but first", "before we"); call-to-action positions as a percentage of video length using an editable phrase list (subscribe, like, comment, link below, newsletter, sponsor); transition markers per 1,000 words (first, next, then, finally, now, so); segment length distribution. Never store more than 8 consecutive words of any transcript in metrics.json.
M4 Metadata: collect via API or load CSV; per video: title, publish date, duration, views, views per day; title patterns (starts with number, contains number, question, how-to, colon split, versus, brackets, ALL-CAPS word, year); title length mean and spread; upload cadence by week and weekday; series detection from "Part N", "Episode N", "#N", "Day N". Respect quota: only videos.list, channels.list, playlistItems.list; print the units used. Handle quota errors, invalid keys, private channels, and network failures with one retry. Read thumbnail_notes.csv (columns: video_id, layout, text_words, text_position, dominant_colors, subject, face_yes_no, notes) and summarize it.
M5 Packs and assemble: for each top-level template section build packs/NN.md containing: the section heading and its instructions copied from the template; the measured facts relevant to that section selected by keyword matching between the heading text and a mapping table in config.py (editable: for example headings containing "hook" get hook-window metrics; "pacing" or "edit" get words per minute and segment lengths; "title" gets title patterns; "cadence" or "series" gets cadence and series data; "voice" or "tone" gets sentence and pronoun metrics; "thumbnail" gets the thumbnail summary); any section with no mapped metrics gets the full channel summary; and a fixed instruction block. The instruction block must say: "Fill this section of my Style Bible for new content in [NICHE] for [AUDIENCE] in [LANGUAGE]. Use only the measured facts and the transcript excerpts I attach below, if any. Describe style as rules, ranges, and mechanics, never as quotes. Do not copy any sentence of more than 8 words from the sources. Where a fact is not measurable from the data, write 'NOT MEASURED: <what to check by hand>' instead of guessing. Return the section with the same heading and the same sub-structure as the template." Provide an option --with-excerpts N that appends up to N short excerpts per video, each a maximum of 40 words, chosen from the hook window and the final 10 percent of the transcript, labelled as study material that must not be reused. assemble: read responses/NN.md files, verify each begins with the exact template heading, merge in template order, insert "NOT FILLED" for missing responses, and write output/style_bible.md.
M6 Lint: checks, each PASS or FAIL with a reason: (1) every template heading is present once, in order, at the right level; (2) no heading was added or renamed; (3) no run of 9 or more consecutive words from any source transcript appears in the Style Bible (case-insensitive, punctuation removed; report only the run length and the Style Bible line number, never the source text); (4) no leftover template placeholder in square brackets that I had not intended (list them); (5) no "NOT FILLED" markers; (6) count of "NOT MEASURED" markers, reported as a to-do list; (7) the Style Bible contains no claims of guaranteed results (search for "guarantee", "full proof", "will earn"); (8) word count per section within 30 percent below or above a size range I can set in config. Exit code 0 only if checks 1, 2, 3, 5 and 7 pass. The 9-word threshold and other thresholds are my own working numbers, not platform rules.
M7 Polish: the "all" command that runs collect, measure, pack and prints the next manual step; a --dry-run flag; clear error messages; a final README section "How to use this Style Bible" pointing to the next steps in my repo; a "delete working data" command that asks for confirmation and removes data/transcripts.

TEST CASES (write them as pytest tests plus fixtures)
T1 Sentence metrics: a fixture transcript of exactly 3 sentences of 5, 10 and 15 words must give mean 10, median 10, and a standard deviation I can compute by hand (state the expected number).
T2 Timestamp parsing: a fixture with lines "0:00", "0:30", "1:00" and known word counts must give an exact words-per-minute value (state the expected number).
T3 Template parsing: a 3-section sample template with one nested heading and one placeholder must return exactly 3 sections in order, with the nested heading attached to its parent and the placeholder listed.
T4 Pack mapping: a heading "Hook mechanics" must receive hook-window metrics; a heading "Posting cadence" must receive cadence data; a heading "Misc" must receive the full summary.
T5 Lint copy detection: a Style Bible fixture that contains one 9-word run from a fixture transcript must FAIL check 3, and the same fixture with the run reduced to 8 words must PASS.
T6 Assemble order: responses given out of order (03, 01, 02) must still be assembled in template order; a missing response must produce "NOT FILLED" and make lint FAIL.
T7 Failure handling: missing transcripts folder, empty transcript, invalid API key, and quota exceeded must each give a one-line human-readable message and a non-zero exit code.
All fixtures must be invented text in the neutral niche "home cooking on a budget". Do not use real creators' text in any fixture.

RULES FOR YOU
- Write complete files only: no placeholders, no "..." gaps, no TODO comments.
- At the end of each milestone list: files created or changed (full paths), commands to run on Windows and on macOS or Linux, and the expected output of each command.
- If you are unsure of any fact (API behaviour, limits, licences), write VERIFY BEFORE RELYING and name the official page.
- Do not add features I did not ask for. If you see a risk or a better design, say so in two sentences before building.
Start with M0 now.
```

**Expected output:** a milestone-by-milestone build that ends in a command-line tool with passing tests and a Style Bible whose headings match your template.
**If the output is weak:** at the failing milestone, paste the exact error and the file it concerns and say: "Return the full corrected file and the test that proves the fix. Do not move on to the next milestone." If the template parser gets your headings wrong, paste the three lines around the problem heading from your template and ask for the parser function only, with a new test.

### P-BUILD-22 — Channel Style Analyzer: Extension Prompt

- What it does: adds the next layer to the finished analyzer: a cache, multi-channel comparison, a section-level re-run, and an optional automated chat step.
- Why it helps: a second and third channel become cheap to analyze; you can compare your own channel's measured style against the model channel's, and you can re-fill one weak section without redoing the rest.
- Free stack: the same as P-BUILD-21. Optional: a free Gemini API key (limits and model names change; VERIFY BEFORE RELYING at ai.google.dev/gemini-api/docs/rate-limits). Without it everything stays a manual copy and paste.
- Difficulty: medium. Time to build: 4 to 6 hours.
- Risks: ToS: an automated chat call sends your pack text, which may include transcript excerpts, to a third-party service; check that service's terms before sending, and send measured metrics only when in doubt; quota: free tiers have request limits and can change.

**Purpose:** extend the working analyzer in four defined steps.
**Inputs:** [CURRENT_FILES] (paste the output of `python analyzer.py --help` and the file tree), [EXTENSION_GOAL] (choose any of: cache, compare, refill, auto), [CHANNEL_NAME], [LANGUAGE].

```
You are a senior Python engineer extending my existing "Channel Style Analyzer" (Python 3.11, standard library plus optional requests and pytest, $0). It already has the commands init, collect, measure, pack, assemble, lint, all, and a template parser that reproduces my Style Bible template headings.

Current state:
[CURRENT_FILES]

Extensions I want now: [EXTENSION_GOAL]. Build only the ones I named, one per reply, in this order if several: cache, compare, refill, auto. After each one stop and wait for "continue".

Definitions:
1. cache: store the API responses and the computed metrics per video in cache/ as JSON with the video ID, fetch date, and a hash of the transcript file; "measure" recomputes only videos whose transcript hash changed; add "cache clear" and "cache status". Never cache transcript text itself, only metrics.
2. compare: a command "compare --a data_dir_A --b data_dir_B" that reads two metrics.json files (for example the model channel and my own channel) and writes output/compare.md with a table of every numeric metric for A and B, the ratio B/A, and a plain-language "gap list" that names the five largest differences and what each would mean for the Style Bible, never suggesting copying text. If channel B has fewer than 5 videos, print a warning that the comparison is weak.
3. refill: a command "refill --section NN" that regenerates only packs/NN.md with an extra block listing the lint failures for that section and the previous response, so a weak section can be improved without redoing the rest; assemble must then use the new response.
4. auto (optional, off by default): a command "auto --section NN" that sends one pack to the Gemini API using the key in GEMINI_API_KEY and the model name in an environment variable GEMINI_MODEL, writes the reply to responses/NN.md, sleeps between calls (GEMINI_SLEEP_SECONDS, default 8), stops on the first rate-limit error, never retries more than once, and refuses to run unless the pack was built without --with-excerpts. Print a clear warning before any call that the pack text will be sent to a third-party service. Mark every free-tier fact VERIFY BEFORE RELYING.

For each extension deliver: the complete changed or new files (full contents), new tests with expected values worked out by hand, run commands for Windows and for macOS or Linux, and one paragraph on risks. Keep the template-matching behaviour and the lint checks unchanged. Language of the material: [LANGUAGE]; channel under study: [CHANNEL_NAME].
```

**Expected output:** the extensions you selected, each as full files plus tests.
**If the output is weak:** ask it to restate the current command list and which existing function each change touches before it writes code, then re-run the extension.

## Done when

- `python analyzer.py all` runs without error on your transcripts and prints the next manual step.
- Every pack was run in a free chat and every reply is saved in `responses/`.
- `output/style_bible.md` has the same headings, in the same order, as `01-channel-dna/03-style-bible-template.md`.
- `lint` shows PASS for template headings, no added headings, no 9-word source runs, no "NOT FILLED" markers, and no guarantee language.
- Every "NOT MEASURED" item has been checked by hand or crossed out with a reason.
- The folder `data/transcripts` is deleted and you kept only `output/style_bible.md` and your own notes.
- You pasted the finished Style Bible into [STYLE_BIBLE] on your setup card.

## Next

Continue with [Reality and timeline math](../08-monetization/01-reality-and-timeline-math.md).
