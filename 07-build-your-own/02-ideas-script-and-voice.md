# Build Your Own, Part 2: Script and Voice Tools

> **Purpose:** five checkers and helpers that keep scripts varied, original, and cleanly voiced  
> **Use when:** you produce scripts or AI voiceover regularly  
> **Time needed:** 1.5 to 3 hours per tool  
> **Needs:** Python 3.11 or later, a free Claude or Gemini chat, optionally a Google account  
> **Cost:** $0

## Inputs

- [LANGUAGE], [VOICE_MODE], [VIDEO_LENGTH], [NICHE], [AUDIENCE], [STYLE_BIBLE] from the setup card and `01-channel-dna/03-style-bible-template.md`.
- A folder of your own scripts named `scripts/`, one `.md` or `.txt` file per video.
- For the similarity checker only: the source channel's transcript, copied by hand from the on-page transcript panel into `source/source-transcript.txt` (see `01-channel-dna/01-data-gathering.md`).

## Steps

1. Create the project folder once:
   1. Make a folder named `script-tools`.
   2. Inside it, make the sub-folders `scripts`, `source`, `reports`, `lexicon`, `audio`.
   3. Open a terminal in that folder and run `python -m venv .venv`.
   4. Activate it: Windows `.venv\Scripts\activate`; macOS and Linux `source .venv/bin/activate`.
2. Add `source/` and `reports/` to `.gitignore`. The source transcript is a private working copy for your own comparison only. Delete it when the video is published, and never publish, redistribute, or feed it into any generator as text to rewrite.
3. Why these tools matter. YouTube's July 2026 clarification names generic, repetitive, or template-based content with little variation between videos as non-monetizable inauthentic content (verified 2026-10-20, techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos). The separate reused-content policy did not change. Every threshold in this file is this repo's own working number, not a YouTube rule. YouTube publishes no similarity score. VERIFY BEFORE RELYING on support.google.com/youtube for current policy wording.
4. Run order for a script: P-BUILD-08 hook check, P-BUILD-06 variety check, P-BUILD-07 source-similarity check, P-BUILD-09 pronunciation fixer, generate voice, P-BUILD-10 round-trip check.
5. Free local voice tools referenced here: Kokoro TTS (Apache-licensed weights; `pip install kokoro>=0.9.4`; needs espeak-ng; verified 2026-10-20) and Piper TTS (VERIFY BEFORE RELYING on its current licence at github.com/rhasspy/piper, since licensing of voices varies by voice model). For transcription, Whisper (VERIFY BEFORE RELYING on the licence of the exact package you install: github.com/openai/whisper or github.com/SYSTRAN/faster-whisper).
6. Keep a single `requirements.txt` per tool. Use only the packages named in the prompt.

## Prompts

### P-BUILD-06 — Script Variety Checker

- What it does: compares all your scripts against each other and flags structural sameness: identical openings, the same section order every time, repeated sentence starters, and large shared phrases.
- Why it helps: it catches the "template with swapped nouns" problem before upload, which is the pattern YouTube's inauthentic-content rule targets.
- Free stack: Python 3.11 standard library only (`re`, `collections`, `difflib`, `statistics`, `json`).
- Difficulty: easy to medium. Time to build: 2 to 3 hours.
- Risks: policy: it is a self-check, not proof of anything; a pass does not guarantee monetization; license: none.

**Purpose:** detect templating across your own scripts.
**Inputs:** [SCRIPTS_DIR] (default `scripts`), [MIN_SCRIPTS] (default 3), [LANGUAGE].

```
You are a senior Python developer. Build "variety_check.py" with the Python standard library only, at $0.

Input: all .md and .txt files in [SCRIPTS_DIR]; language [LANGUAGE]. Needs at least [MIN_SCRIPTS] files, otherwise print "Add more scripts first" and exit.

For each script compute:
1. Opening fingerprint: first 40 words, lowercased, punctuation removed.
2. Section signature: the ordered list of Markdown headings or lines starting with "SECTION", "ACT", "PART", or "HOOK", reduced to their first word.
3. Sentence-start profile: the 10 most common first words of sentences and their share.
4. Sentence length: mean, median and standard deviation in words.
5. Phrase set: all 5-word shingles.

For each pair of scripts compute: Jaccard similarity of 5-word shingles; difflib ratio of the opening fingerprints; difflib ratio of the section signatures.

Flags (thresholds are this repo's working numbers and must be editable at the top of the file as constants):
- SHINGLE_FAIL = 0.15 pair shingle Jaccard.
- OPENING_FAIL = 0.6 opening ratio.
- SECTION_FAIL = 0.9 section ratio (same structure again and again).
- STARTER_FAIL = 0.20 share of sentences beginning with the same word in one script.
- LENGTH_FAIL = standard deviation under 4 words (monotone rhythm).

Outputs: reports/variety_report.md with a table of pairs and flags, a plain-English "What to change" list for each flagged script, and a final PASS or REVIEW line. Also write reports/variety_report.json. Never print more than 12 words from any script in the report.

Handle: empty files, files under 150 words (skip with a note), non-UTF-8 text, and mixed line endings.

Deliver: the complete script, run commands for Windows and macOS/Linux, and 3 test cases with exact expected results (3 genuinely different scripts, 2 scripts with the same opening, 3 scripts with identical section order). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `variety_check.py` plus a report format.
**If the output is weak:** give it two of your scripts that should fail and ask it to tune only the constants and explain each change.

### P-BUILD-07 — Source-Similarity Self-Checker

- What it does: compares your new script with the source channel's transcript that you hold privately and shows the longest shared word runs and overall overlap.
- Why it helps: your goal is the same style, never the same words; this shows you the exact sentences to rewrite before voiceover.
- Free stack: Python 3.11 standard library; optional `scikit-learn` (BSD licence, VERIFY BEFORE RELYING) for TF-IDF cosine.
- Difficulty: medium. Time to build: 2 to 3 hours.
- Risks: ToS and copyright: the transcript is copyrighted text. Copy it only by hand from the on-page transcript panel, keep it local, use it only for comparison, delete it after publishing. Never paste it into an AI chat as a source to paraphrase. Policy: this tool does not make copied ideas original; if the structure of an entire video is a close copy, change the topic, not just the words.

**Purpose:** find and remove verbatim and near-verbatim overlap.
**Inputs:** [NEW_SCRIPT_PATH], [SOURCE_TRANSCRIPT_PATH], [LANGUAGE].

```
You are a senior Python developer. Build "similarity_check.py" at $0 with the standard library; add scikit-learn as an optional import for TF-IDF cosine, and fall back gracefully if it is missing.

Inputs: --new [NEW_SCRIPT_PATH], --source [SOURCE_TRANSCRIPT_PATH], language [LANGUAGE]. Source transcripts may include timestamps such as "0:32" or "00:01:15" on their own lines; strip them.

Compute:
1. Longest common run of words (case-insensitive, punctuation removed) and print its length and position in the new script.
2. All shared runs of 6 or more words, with line numbers in the new script.
3. Share of the new script's 5-word shingles that also occur in the source.
4. Sentence-level similarity: for each sentence in the new script, the best difflib ratio against all source sentences; list sentences scoring 0.8 or higher.
5. If scikit-learn is installed: TF-IDF cosine similarity at document level and per paragraph.
6. A "structure echo" check: compare the ordered list of paragraph word counts (as a rough rhythm fingerprint) and report the correlation using pure Python; label it "rhythm only, not a copy test".

Working thresholds (constants at the top, labelled "repo working numbers, not YouTube rules"): longest run under 8 words; shingle share under 3 percent; no sentence at 0.8 or higher.

Output reports/similarity_report.md. Show flagged lines from the NEW script only, never print source text longer than 6 words. End with PASS or REWRITE and a short list of the lines to rewrite.

Handle: missing files, empty files, very large files (over 200,000 words), non-UTF-8 text.

Deliver: the full script, install and run commands, and 3 test cases with expected outputs (an original script, a script with one pasted 12-word sentence, a script that is the source with synonyms swapped). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `similarity_check.py` and a clear PASS or REWRITE report.
**If the output is weak:** ask for "a --debug flag that prints the three nearest source sentence numbers for each flagged line, without printing the source text".

### P-BUILD-08 — Hook Library Builder

- What it does: stores your own hooks tagged by mechanic, tracks how often each mechanic was used, blocks over-reuse, and helps you write fresh variants.
- Why it helps: hooks are where templated channels look the same; a rotation rule enforces variety.
- Free stack: Google Sheets, Apps Script, optional free Claude or Gemini chat for variants.
- Difficulty: easy. Time to build: 1.5 to 2 hours.
- Risks: policy: log hooks you wrote, never the source channel's exact hook lines. Mechanics only, for example "specific number plus stakes".

**Purpose:** a hook log with reuse limits.
**Inputs:** [NICHE], [AUDIENCE], [STYLE_BIBLE] (hook mechanics section), [HOOK_MECHANICS] (the list from your Style Bible).

```
You are a Google Sheets and Apps Script expert. Build a "Hook Library" at $0 for niche [NICHE], audience [AUDIENCE].

Hook mechanics to support (edit list lives in a tab named Lists): [HOOK_MECHANICS]. If I leave it empty, use these ten: curiosity gap, contrarian claim, specific number, stakes up front, cold-open scene, direct question, myth-bust, before-and-after, challenge with a limit, "what nobody tells you".

Tabs:
- Hooks: A date, B video title, C hook text (my own words), D mechanic (dropdown from Lists), E spoken seconds (number), F first-30-seconds retention percent (blank until known), G reuse note.
- Rotation: shows each mechanic, the count used in my last 10 videos, and the status OK if used 2 times or fewer, "Rest it" if 3 or more.
- Variants: where I paste a hook and get a prompt.

Rules:
1. An Apps Script onEdit trigger on Hooks!D shows a pop-up warning if that mechanic is "Rest it".
2. A menu item "Build variant prompt" writes this text to Variants!A1, filled with the selected hook: "Rewrite this hook 6 ways using these mechanics: [chosen mechanics]. Each must be under 20 spoken words, for [AUDIENCE], in [LANGUAGE]. Do not reuse any distinctive phrase from the original. Add one line saying which promise the video must then deliver."
3. A tab named BestByMechanic that averages column F by mechanic once at least 3 values exist.
4. Add data validation for E and F.

Deliver: formulas, full Apps Script, setup steps with menu paths, and 3 test cases with exact expected results (a fresh mechanic, a mechanic used 3 times in the last 10, a row with retention filled). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** a hook log with rotation rules.
**If the output is weak:** ask for the Rotation formulas alone, with a sample table of 12 rows and the result you should see.

### P-BUILD-09 — Pronunciation Fixer

- What it does: rewrites a script into a voice-ready text file with numbers, units, acronyms, currency and hard names respelled according to a lexicon you grow over time.
- Why it helps: flat or wrong pronunciations are the quickest way an AI voice sounds cheap; one lexicon fixes a word everywhere.
- Free stack: Python 3.11 standard library; works with Kokoro, Piper, or any TTS that reads plain text.
- Difficulty: easy. Time to build: 1.5 to 2 hours.
- Risks: license: none; quality: respelling is plain text and works on any engine, while phoneme markup differs per engine (VERIFY BEFORE RELYING: Kokoro and Piper documentation for custom pronunciation syntax).

**Purpose:** a repeatable text preprocessor.
**Inputs:** [LANGUAGE], [VOICE_MODE], [LEXICON_START] (10 to 30 problem words you already know, as "word => respelling" lines).

```
You are a senior Python developer. Build "fix_text.py" at $0 with the Python standard library only.

Usage: python fix_text.py --in script.md --out voice_text.txt --lexicon lexicon/lexicon.csv [--review]

Language: [LANGUAGE]. Voice mode: [VOICE_MODE]. Starting lexicon entries: [LEXICON_START].

Behaviour:
1. Strip Markdown: headings, bold, italics, links (keep link text), bullet markers, and any line starting with "VISUAL:", "B-ROLL:", "NOTE:" or text inside square brackets that is a production note.
2. Apply the lexicon: CSV with columns term, respelling, case_sensitive (yes/no), whole_word (yes/no), note. Longest term first.
3. Normalise for speech (English rules; if [LANGUAGE] is not English, apply only the lexicon and the Markdown strip and say so in the report): currency ($5.50 to "five dollars fifty cents"), percentages, ordinals, years (1998 to "nineteen ninety-eight", 2026 to "twenty twenty-six"), times (3:30 pm), units (kg, km, ml, tbsp, tsp, C and F with degree), common abbreviations (e.g., i.e., vs., approx.), and spelled-out acronyms listed in a second CSV named acronyms.csv (column term, spoken).
4. Add pauses: insert a blank line between paragraphs, and replace " - " and "..." with a comma-plus-space or period as appropriate, so engines pause naturally.
5. In --review mode print a table: each changed token, original, replacement, line number.
6. Write reports/fix_report.md listing words that look unusual but were not in the lexicon (capitalised words not at sentence start that are not English dictionary-like, detected by a built-in list of 3,000 common words you embed or load from a file named common_words.txt that you create with the 3,000 most common words), so I can add them.
7. Handle: missing lexicon, bad CSV rows (report and continue), empty input.

Deliver: the script, a starter lexicon.csv and acronyms.csv built from [LEXICON_START], run commands for Windows and macOS/Linux, and 3 test cases with expected output (prices and units, a hard name, a script with production notes). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `fix_text.py`, `lexicon.csv`, `acronyms.csv`.
**If the output is weak:** paste the exact sentence that read wrongly and the fixed form you want, then ask for the rule or lexicon row that solves it.

### P-BUILD-10 — TTS Round-Trip Checker

- What it does: transcribes your generated voiceover with Whisper, compares it to the script text, and lists the words the voice garbled, with timestamps.
- Why it helps: you do not have to listen to a full voiceover to find the bad words; the checker points to them and feeds the pronunciation lexicon.
- Free stack: Python 3.11, `faster-whisper` or `openai-whisper`, standard library `difflib`; runs on CPU with a small model.
- Difficulty: medium. Time to build: 3 hours.
- Risks: licence: VERIFY BEFORE RELYING on the Whisper package and model licences before use; quality: Whisper can mis-hear a word that was spoken correctly, so treat flags as listening prompts, not verdicts.

**Purpose:** find mispronounced words automatically.
**Inputs:** [SCRIPT_TEXT_PATH] (the voice-ready text from P-BUILD-09), [AUDIO_PATH], [WHISPER_MODEL] (default `small`), [LANGUAGE].

```
You are a senior Python developer. Build "roundtrip_check.py" at $0.

Usage: python roundtrip_check.py --text [SCRIPT_TEXT_PATH] --audio [AUDIO_PATH] --model [WHISPER_MODEL] --lang [LANGUAGE]

Use faster-whisper if installed, otherwise openai-whisper, and print which one ran. Run on CPU by default with a --device option. Request word timestamps.

Steps:
1. Transcribe the audio to a list of (word, start, end).
2. Normalise both texts: lowercase, strip punctuation, expand numbers with a small built-in number-to-words function for integers up to 999,999 so "1,200" and "twelve hundred" can match.
3. Align with difflib.SequenceMatcher on word lists. Report: word error rate (substitutions + deletions + insertions divided by script words), and each substitution, deletion and insertion with the timestamp from the transcript and 4 words of context.
4. Group repeated substitutions (same script word heard as the same wrong word) and output a suggested lexicon row for each: term, respelling blank for me to fill, and a note with the heard word.
5. Write reports/roundtrip_report.md and a CSV reports/lexicon_suggestions.csv matching the columns term, respelling, case_sensitive, whole_word, note.
6. Print PASS when WER is under 0.05 and no deletion run is longer than 3 words; otherwise LISTEN AT these timestamps (list). State that 0.05 is this repo's working number, not a standard.

Handle: missing ffmpeg (explain how to install it for free on Windows, macOS and Linux), audio longer than 30 minutes (process in 10-minute chunks and offset timestamps), model download failure, and empty transcript.

Deliver: the full script, requirements.txt, install and run commands, and 3 test cases with expected results (a clean read, a script with one name read wrongly, an audio file with a missing sentence). Mark uncertain facts VERIFY BEFORE RELYING.
```

**Expected output:** `roundtrip_check.py`, a timestamped problem list, and lexicon suggestions that feed back into P-BUILD-09.
**If the output is weak:** ask for a `--fake-transcript` mode that reads a JSON transcript so you can test the alignment logic without audio.

## Done when

- You built at least P-BUILD-06 and P-BUILD-07 and ran them on one real draft.
- A script that fails similarity or variety is rewritten, not just reworded, and then re-checked until the report reads PASS.
- Your lexicon has at least 20 rows and grows after each round-trip report.
- The source transcript file is deleted after the related video is published.
- You can state, in one sentence per video, what your script contains that the source does not.

## Next

Continue with [Visuals and editing tools](./03-ideas-visuals-and-editing.md).
