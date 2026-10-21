# Pipeline Architecture: Research to Analytics Feedback Loop

> **Purpose:** Show the full production pipeline as one diagram, and for every stage name the repo file, the free tool, the input and output files, what can be automated, and what must stay human.  
> **Use when:** Before you automate anything. Read this once, then run one video through the pipeline by hand.  
> **Time needed:** 45 minutes to read and fill P-AUTO-01.  
> **Needs:** Completed [STYLE_BIBLE] from 01-channel-dna, a Google account.  
> **Cost:** $0

## Inputs

- [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [COUNTRY]
- [HARDWARE], [WEEKLY_HOURS], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_LENGTH]
- [STYLE_BIBLE] (from `01-channel-dna/03-style-bible-template.md` filled by P-CDNA-02)

## The architecture in one diagram

Gates are marked `[C1]` to `[C8]`. A gate is a human checkpoint. No stage may start on a video until the gate before it has been passed by a person. The gates are defined in full in `04-human-checkpoints.md`.

```
 [CHANNEL_URL] + setup card
        |
        v
 1 RESEARCH ---------> dna/style-bible.md, dna/video-dna.md, dna/shorts-dna.md
        |
        v
 2 IDEATION ---------> videos/<slug>/topic.md, value-stack.md
        |
   [C1] IDEA GATE (human)            status: IDEA -> APPROVED
        |
        v
 3 SCRIPT -----------> outline.md, script.md, factcheck.md
        |
   [C2] SCRIPT GATE (human)          status: SCRIPTED -> SCRIPT_OK
        |
        v
 4 VOICE ------------> voice.wav, captions.srt
        |
   [C3] VOICE GATE (human)           status: VOICED
        |
        v
 5 VISUALS ----------> clips/, thumbnails/asset-log.csv rows
        |
   [C4] VISUALS GATE (human)         status: VISUALS_DONE
        |
        v
 6 EDIT -------------> final.mp4, edit-notes.md      status: EDITED
        |
        v
 7 THUMBNAIL --------> thumbnails/<slug>/thumb-A.jpg, thumb-B.jpg, thumb-C.jpg
        |
   [C5] THUMBNAIL GATE (human)       status: THUMB_DONE
        |
        v
 8 METADATA ---------> metadata.md, disclosure.md
        |
   [C6] METADATA GATE + [C7] DISCLOSURE GATE (human)   status: META_DONE
        |
        v
 9 REVIEW -----------> orig-score.md, review-log.md
        |
   [C8] FINAL WATCH (human)          status: REVIEW_PASSED
        |
        v
10 SCHEDULE ---------> scheduled in YouTube Studio      status: SCHEDULED
        |
        v
11 ANALYTICS --------> metrics rows, updated dna/ files, variation-log
        |
        +--------------------------------------> back to 1 RESEARCH and 2 IDEATION
```

Folder and file names follow `03-bulk-systems.md`. `<slug>` means a short folder name such as `L012-lentil-stew-under-3-dollars` (L for long form, S for Shorts, then a three-digit counter).

## Steps

1. Read the diagram and the eleven stage cards below. Do not skip the "must stay human" lines. They are the part that keeps the channel monetizable.
2. Run P-AUTO-01 below with your setup card values. It returns a stage-by-stage plan matched to your [HARDWARE] and [WEEKLY_HOURS].
3. Create the workspace folders listed in `03-bulk-systems.md`. Create no automation yet.
4. Produce one complete video by hand through all eleven stages, using the files named in the cards. Write down every step that took more than 15 minutes. Those are the stages worth automating.
5. Raise the automation level of one stage at a time, using the level scale below. Run three videos at a stage's new level before raising another stage.
6. Never connect two stages so that the output of the first publishes or advances without a gate when the diagram shows a gate.

## Automation levels

| Level | Meaning | Example |
|---|---|---|
| A0 | Fully manual | You write the script in a document |
| A1 | Assisted | You paste a repo prompt into a free chat tool and edit the reply |
| A2 | Batch | A sheet holds many rows, a tool drafts them, you review each |
| A3 | Triggered | A status change in the sheet starts a tool that drafts the next file |
| A4 | Unattended | Nothing starts or finishes without a person. **Forbidden for any stage.** |

The ceiling for every stage in this repo is A3 for drafting and A1 for judgment. There is no A4.

## Stage cards

### Stage 1 Research
- Repo files: `01-channel-dna/01-data-gathering.md`, `01-channel-dna/02-channel-analysis.md`, `01-channel-dna/03-style-bible-template.md`, `02-long-form/01-video-dna-analysis.md`, `03-shorts/01-shorts-dna-analysis.md`, `04-thumbnails/01-thumbnail-dna-analysis.md`. Prompts: P-CDNA-01, P-CDNA-02, P-LONG-01, P-SHORT-01, P-THUMB-01.
- Free tool: public watch page, the on-page transcript panel, public metadata, the official YouTube Data API, Google Sheets, a free chat LLM.
- Input files: [CHANNEL_URL], [TRANSCRIPT] text you copied by hand from the transcript panel.
- Output files: `dna/style-bible.md`, `dna/video-dna.md`, `dna/shorts-dna.md`, `thumbnails/thumb-dna-[CHANNEL_NAME].md`.
- Can be automated: tabulating patterns across transcripts you already collected, filling the [STYLE_BIBLE] sections, comparing hook structures.
- Must stay human: choosing which videos to study, collecting transcripts without downloading or scraping at scale, and judging whether a pattern is a style (copyable) or a protected expression (not copyable).

### Stage 2 Ideation
- Repo files: `02-long-form/02-script-prompt-chain.md` (P-LONG-02), `03-shorts/03-batch-scripts.md` (P-SHORT-03), `05-originality-layer/01-differentiation-method.md` (P-ORIG-02), `07-build-your-own/01-ideas-research-and-ideation.md`.
- Free tool: Google Sheets, Google Forms, YouTube search autocomplete, a free chat LLM.
- Input files: `dna/style-bible.md`, the `Intake` tab of the pipeline sheet, the list of already published titles.
- Output files: `videos/<slug>/topic.md`, `videos/<slug>/value-stack.md`, a new row in the `Pipeline` tab.
- Can be automated: generating many topic candidates, removing duplicates against published titles, drafting the Value Stack plan.
- Must stay human: gate C1. A person supplies the first-hand layer (a real test, a real number, a real experience). A topic with no first-hand layer does not get approved.

### Stage 3 Script
- Repo files: `02-long-form/02-script-prompt-chain.md` (P-LONG-03 outline, P-LONG-04 script, P-LONG-05 hook variants, P-LONG-06 retention edit, P-LONG-07 fact-check), `03-shorts/02-script-prompt-chain.md` (P-SHORT-02).
- Free tool: a free chat LLM tier, or the Gemini API free tier through `02-no-code-workflow.md`.
- Input files: `topic.md`, `value-stack.md`, `dna/style-bible.md`.
- Output files: `outline.md`, `script.md`, `factcheck.md`.
- Can be automated: first drafts, hook variants, retention edit suggestions, a list of claims that need a source.
- Must stay human: gate C2. A person adds the first-hand material, checks every factual claim against a primary source, and reads the script aloud.

### Stage 4 Voice
- Repo file: `02-long-form/03-voice-and-audio.md`.
- Free tool: your own recording, Kokoro TTS (Apache 2.0, verified 2026-10-20), Piper TTS (VERIFY BEFORE RELYING: licence and voice-model terms on the Piper project page), Whisper for captions (VERIFY BEFORE RELYING: licence on the Whisper project page).
- Input files: `script.md` marked SCRIPT_OK.
- Output files: `voice.wav`, `captions.srt`.
- Can be automated: rendering the approved script to audio, generating captions.
- Must stay human: gate C3. A person listens to the whole audio. A synthetic voice of a real person you do not own the rights to is never allowed. Disclosure decisions follow the table in `02-long-form/03-voice-and-audio.md`.

### Stage 5 Visuals
- Repo files: `02-long-form/04-visual-production.md`, `03-shorts/04-vertical-visuals-and-editing.md`.
- Free tool: your own footage, Canva free (VERIFY BEFORE RELYING: licence terms for each element on the Canva licence page), ComfyUI with Wan 2.2 (Apache 2.0, verified 2026-10-20) only if [HARDWARE] has a strong GPU.
- Input files: `script.md`, `voice.wav`.
- Output files: a `clips/` folder in the video folder, one row per asset in `thumbnails/asset-log.csv`.
- Can be automated: scene-by-scene image prompt lists, the asset log rows.
- Must stay human: gate C4. A person checks the licence of every asset and decides whether realistic synthetic imagery needs disclosure.

### Stage 6 Edit
- Repo file: `02-long-form/04-visual-production.md` (editing section), `03-shorts/04-vertical-visuals-and-editing.md`.
- Free tool: DaVinci Resolve free, CapCut free (VERIFY BEFORE RELYING: export limits, watermark and commercial-use terms for both).
- Input files: `voice.wav`, `clips/`, `captions.srt`, the P-LONG-06 retention notes.
- Output files: `final.mp4`, `edit-notes.md`.
- Can be automated: silence trimming, caption burn-in, an assembly checklist generated from the script.
- Must stay human: pacing, cuts, and the original commentary or demonstration that makes the video more than a slideshow.

### Stage 7 Thumbnail
- Repo files: `04-thumbnails/02-original-generation.md` (P-THUMB-02), `04-thumbnails/03-design-workflow-and-templates.md`, `04-thumbnails/04-ab-testing-and-safety.md`.
- Free tool: Canva free, plus the image tools listed in `04-thumbnails/02-original-generation.md`.
- Input files: `topic.md`, `thumb-dna-[CHANNEL_NAME].md`, last five templates used.
- Output files: `thumbnails/<slug>/thumb-A.jpg`, `thumb-B.jpg`, `thumb-C.jpg`.
- Can be automated: prompt text, layout and text suggestions, variant lists.
- Must stay human: gate C5. A person runs the resemblance audit and confirms the thumbnail promises only what the video delivers.

### Stage 8 Metadata
- Repo files: `02-long-form/05-metadata-and-seo.md` (P-LONG-09).
- Free tool: free chat LLM, Google Sheets.
- Input files: `script.md`, `captions.srt`, the final thumbnail text.
- Output files: `metadata.md`, `disclosure.md`.
- Can be automated: title options, description drafts, chapter lists from captions.
- Must stay human: gates C6 and C7. A person confirms the title and description match the video and decides the "Altered or synthetic content" setting in YouTube Studio.

### Stage 9 Review
- Repo files: `02-long-form/06-prepublish-gate.md`, `03-shorts/06-prepublish-gate.md`, `05-originality-layer/02-scoring-rubric.md` (P-ORIG-01), `05-originality-layer/03-sensitive-topics-and-personas.md`.
- Free tool: a free chat LLM for the rubric run, your own eyes for the watch.
- Input files: every file above for the slug.
- Output files: `orig-score.md`, `review-log.md`.
- Can be automated: running the rubric prompt and the checklist.
- Must stay human: gate C8. A person watches the full video at normal speed. A score of 80 or more is necessary but not sufficient.

### Stage 10 Schedule
- Repo files: `06-automation/07-youtube-api-and-audit.md`, `templates/content-calendar.md`.
- Free tool: YouTube Studio scheduling.
- Input files: `final.mp4`, the chosen thumbnail, `metadata.md`.
- Output: a scheduled video in Studio, status SCHEDULED, the date written back to the sheet.
- Can be automated: calendar rows and reminders.
- Must stay human: the upload and the Schedule button. A `videos.insert` call from an unaudited API project created after 28 July 2020 is locked private until the project passes a compliance audit, and the default upload bucket is about 100 `videos.insert` calls per day (verified 2026-10-20). Design for review followed by manual or Studio-scheduled publishing.

### Stage 11 Analytics feedback loop
- Repo files: `08-monetization/04-growth-levers-and-kpis.md`, `09-operations/03-tracking-sheet.md`.
- Free tool: YouTube Studio analytics, Google Sheets, a free chat LLM.
- Input files: the weekly export of per-video metrics.
- Output files: rows in the `Metrics` tab, an updated `dna/style-bible.md`, the variation log.
- Can be automated: a weekly summary of which hooks, titles and thumbnails held attention.
- Must stay human: deciding what to change. Move toward what your own audience rewards, not toward closer imitation of the source channel.

## Prompts

### P-AUTO-01 — Pipeline Planner

Purpose: Turn the setup card into a stage-by-stage plan with a tool, an automation level, and a time budget per stage.
Inputs: [CHANNEL_NAME], [NICHE], [AUDIENCE], [LANGUAGE], [HARDWARE], [WEEKLY_HOURS], [FACE_OR_FACELESS], [VOICE_MODE], [VIDEO_LENGTH], [STYLE_BIBLE], [PIPELINE_CARDS] (paste the eleven stage cards from this file).

```
You are a production planner for a small YouTube channel. Everything must cost $0.

Channel: [CHANNEL_NAME]. Niche: [NICHE]. Audience: [AUDIENCE]. Language: [LANGUAGE].
Hardware: [HARDWARE]. Hours per week available: [WEEKLY_HOURS].
On camera or faceless: [FACE_OR_FACELESS]. Voice: [VOICE_MODE]. Typical video length: [VIDEO_LENGTH].
Style Bible: [STYLE_BIBLE]
Stage cards: [PIPELINE_CARDS]

Produce a table with one row per stage (Research, Ideation, Script, Voice, Visuals, Edit, Thumbnail, Metadata, Review, Schedule, Analytics). Columns: Stage | Free tool chosen for my hardware | Automation level (A0 to A3 only) | Minutes per long video | Minutes per Short | Gate that follows | Biggest risk for my setup.

Rules:
1. Never use A4. Never recommend automatic publishing. Scheduling is done by a person in YouTube Studio.
2. Never recommend a paid tool, a trial that expires, or a tool whose free tier forbids commercial use. If you are unsure of a licence, write VERIFY BEFORE RELYING and name the official page.
3. Never recommend downloading other creators' videos or scraping at scale.
4. If my setup is faceless, state which stages carry the highest inauthentic-content risk and what first-hand element offsets it.
5. The total of minutes per week must fit inside [WEEKLY_HOURS]. If it does not, cut the number of videos per week, not the review gates.

After the table give: (a) the three stages to automate first and why, (b) the two stages to never automate beyond A1, (c) a plan for the first three videos, each with a target date.
```

Expected output: A table of eleven rows, then three short lists.
If the output is weak: Paste the stage cards again, add your real hours per stage from Step 4, and ask for a revised table that changes only the rows you name.

## Done when

- [ ] You can draw the diagram from memory, including the eight gates.
- [ ] P-AUTO-01 output is saved as `dna/pipeline-plan.md`.
- [ ] One video has passed all eleven stages by hand, with files in the names shown above.
- [ ] You have a list of the stages that took more than 15 minutes.
- [ ] No stage in your plan is set above A3.

## Next

[02-no-code-workflow.md](02-no-code-workflow.md)
